from __future__ import annotations

import bisect
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
import uuid
from typing import Callable

from ..config import Settings
from ..models import PaperTrade, TradeCandidate
from ..market_regime import classify_market_regime
from ..risk import position_size
from ..scanner import _analyze_ticker
from ..ticker_utils import reconstruct_ticker
from ..trade_state import step_trade
from ..indicators import ema as _ema
from ..indicators import ema_series as _ema_series, ema_step as _ema_step
from ..indicators import percent_change
from .costs import entry_fill, stop_exit_fill, target_exit_fill
from .history import KlineQualityIssue, batch_load_klines_cached, fetch_klines_cached, interval_ms
from .universe import (
    SymbolMaster,
    build_current_symbol_master,
    build_dynamic_universe_summary,
    dynamic_universe_refresh_key,
    fetch_universe_snapshot,
    listing_date_allows_analysis,
    select_dynamic_universe_for_day,
)


def _listing_date_allows(
    master: SymbolMaster | None,
    symbol: str,
    bar_close_ms: int,
    min_history_days: int,
) -> bool:
    if master is None:
        return True
    return listing_date_allows_analysis(master.listing_dates, symbol, bar_close_ms, min_history_days)


def _benchmark_pct_24h(
    klines_by_symbol: dict[str, dict[str, list[list]]],
    bar_close_ms: int,
) -> float | None:
    returns: list[float] = []
    for symbol in ("BTCUSDT", "ETHUSDT"):
        k1h = _closed_slice(klines_by_symbol.get(symbol, {}).get("1h", []), "1h", bar_close_ms)
        if len(k1h) < 25:
            continue
        previous = float(k1h[-25][4])
        current = float(k1h[-1][4])
        pct = percent_change(previous, current)
        if pct is not None:
            returns.append(pct)
    return sum(returns) / len(returns) if returns else None


@dataclass
class BacktestTrade:
    trade_id: str
    symbol: str
    status: str
    created_at_utc: str
    updated_at_utc: str
    score: float
    action: str
    setup: str
    verdict: str
    entry_low: float
    entry_high: float
    stop_loss: float
    take_profit_1: float
    take_profit_2: float
    quantity: float | None = None
    entry_price_raw: float | None = None
    entry_price_filled: float | None = None
    exit_price_raw: float | None = None
    exit_price_filled: float | None = None
    entered_at_utc: str | None = None
    tp1_hit_at_utc: str | None = None
    closed_at_utc: str | None = None
    entry_fee: float = 0.0
    exit_fee: float = 0.0
    slippage_cost: float = 0.0
    gross_pnl: float = 0.0
    net_pnl: float = 0.0
    r_multiple_net: float | None = None
    notes: str = ""
    events: list[dict] = field(default_factory=list)


@dataclass
class EquityPoint:
    timestamp_utc: str
    equity: float
    cash: float
    open_positions: int
    open_plans: int
    intrabar_equity_low: float


@dataclass
class BacktestResult:
    run_id: str
    symbols: list[str]
    start_utc: str
    end_utc: str
    created_at_utc: str
    initial_equity: float
    final_equity: float
    cash: float
    trades: list[BacktestTrade]
    equity_curve: list[EquityPoint]
    data_issues: list[KlineQualityIssue]
    config_snapshot: dict
    limitations: list[str]
    universe_mode: bool = False
    universe_snapshot: dict | None = None
    universe_type: str = "manual"
    dynamic_universe_summary: dict | None = None


@dataclass
class _SimTrade:
    paper: PaperTrade
    record: BacktestTrade
    active_from_ms: int
    created_index: int
    score: float
    initial_cash_risk: float


def _iso_from_ms(value: int) -> str:
    return datetime.fromtimestamp(value / 1000, tz=timezone.utc).isoformat(timespec="seconds")


def _date_to_ms(value: str) -> int:
    dt = datetime.fromisoformat(value)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return int(dt.timestamp() * 1000)


def _symbol_base(symbol: str, quote_asset: str) -> str:
    if symbol.endswith(quote_asset):
        return symbol[: -len(quote_asset)]
    return symbol


def _closed_slice(klines: list[list], interval: str, decision_ms: int) -> list[list]:
    # klines are sorted by open_time ascending; a bar is "closed" when its close_time
    # (open_time + step) <= decision_ms, i.e. open_time <= decision_ms - step.
    # Use bisect to locate the cutoff in O(log n) instead of a full linear scan.
    cutoff = decision_ms - interval_ms(interval)
    idx = bisect.bisect_right(klines, cutoff, key=lambda k: int(k[0]))
    return klines[:idx]


def _effective_warmup_ms(settings: Settings) -> int:
    effective_1d_bars = max(
        settings.backtest.warmup_1d_bars,
        settings.analysis.min_history_days + 60,
    )
    return max(
        settings.backtest.warmup_1h_bars * interval_ms("1h"),
        settings.backtest.warmup_4h_bars * interval_ms("4h"),
        effective_1d_bars * interval_ms("1d"),
    )


def _active_positions(trades: list[_SimTrade]) -> list[_SimTrade]:
    return [item for item in trades if item.paper.status in {"ENTERED", "TP1_HIT"}]


def _open_plans(trades: list[_SimTrade]) -> list[_SimTrade]:
    return [item for item in trades if item.paper.status == "WATCHING"]


def _portfolio_equity(cash: float, trades: list[_SimTrade], mark_prices: dict[str, float]) -> float:
    equity = cash
    for item in _active_positions(trades):
        if item.paper.quantity:
            equity += item.paper.quantity * mark_prices.get(item.paper.symbol, item.paper.last_price or item.paper.entry_price or 0)
    return equity


def _portfolio_intrabar_low(cash: float, trades: list[_SimTrade], bars: dict[str, list]) -> float:
    equity = cash
    for item in _active_positions(trades):
        bar = bars.get(item.paper.symbol)
        price = float(bar[3]) if bar else (item.paper.last_price or item.paper.entry_price or 0)
        equity += (item.paper.quantity or 0) * price
    return equity


def _active_risk(trades: list[_SimTrade]) -> float:
    risk = 0.0
    for item in _active_positions(trades):
        if item.paper.quantity and item.paper.entry_price:
            risk += max(item.paper.entry_price - item.paper.stop_loss, 0) * item.paper.quantity
    return risk


def _entry_reclaim_close_satisfied(enabled: bool, close: float, entry_high: float) -> bool:
    return not enabled or close >= entry_high


def _candidate_to_sim_trade(
    result_id: str,
    candidate: TradeCandidate,
    created_at_utc: str,
    active_from_ms: int,
    created_index: int,
    settings: Settings,
    equity: float,
) -> _SimTrade:
    trade_id = uuid.uuid4().hex[:12]
    entry_mid = (candidate.entry_low + candidate.entry_high) / 2
    cash_risk = equity * settings.backtest.risk_per_trade_pct
    paper = PaperTrade(
        paper_trade_id=trade_id,
        account_name="backtest",
        source_scan_id=result_id,
        source_rank=candidate.rank,
        symbol=candidate.symbol,
        base_asset=candidate.base_asset,
        status="WATCHING",
        created_at_utc=created_at_utc,
        updated_at_utc=created_at_utc,
        setup=candidate.setup,
        verdict=candidate.verdict,
        entry_low=candidate.entry_low,
        entry_high=candidate.entry_high,
        planned_entry_mid=entry_mid,
        stop_loss=candidate.stop_loss,
        take_profit_1=candidate.take_profit_1,
        take_profit_2=candidate.take_profit_2,
        risk_reward_1=candidate.risk_reward_1,
        risk_reward_2=candidate.risk_reward_2,
        account_equity=equity,
        risk_per_trade_pct=settings.backtest.risk_per_trade_pct,
        cash_risk=cash_risk,
        last_price=candidate.price,
        notes="Backtest WATCHING condition plan.",
    )
    record = BacktestTrade(
        trade_id=trade_id,
        symbol=candidate.symbol,
        status="WATCHING",
        created_at_utc=created_at_utc,
        updated_at_utc=created_at_utc,
        score=candidate.score,
        action=candidate.action,
        setup=candidate.setup,
        verdict=candidate.verdict,
        entry_low=candidate.entry_low,
        entry_high=candidate.entry_high,
        stop_loss=candidate.stop_loss,
        take_profit_1=candidate.take_profit_1,
        take_profit_2=candidate.take_profit_2,
    )
    return _SimTrade(
        paper=paper,
        record=record,
        active_from_ms=active_from_ms,
        created_index=created_index,
        score=candidate.score,
        initial_cash_risk=cash_risk,
    )


def _sync_record(item: _SimTrade) -> None:
    trade = item.paper
    record = item.record
    record.status = trade.status
    record.updated_at_utc = trade.updated_at_utc
    record.quantity = trade.quantity
    record.entered_at_utc = trade.entered_at_utc
    record.tp1_hit_at_utc = trade.tp1_hit_at_utc
    record.closed_at_utc = trade.closed_at_utc
    record.entry_price_filled = trade.entry_price
    record.exit_price_filled = trade.exit_price
    record.gross_pnl = 0.0 if trade.entry_price is None or trade.exit_price is None or trade.quantity is None else (
        trade.exit_price - trade.entry_price
    ) * trade.quantity
    record.net_pnl = trade.realized_pnl
    if trade.cash_risk > 0 and trade.status in {"STOPPED", "CLOSED", "TIME_EXIT"}:
        record.r_multiple_net = trade.realized_pnl / trade.cash_risk
    record.notes = trade.notes


def _holding_bars_since_entry(trade: PaperTrade, bar_close_ms: int, primary_interval: str) -> int | None:
    if trade.entered_at_utc is None:
        return None
    entered_ms = _date_to_ms(trade.entered_at_utc)
    return max(0, (bar_close_ms - entered_ms) // interval_ms(primary_interval))


def _force_time_exit(
    item: _SimTrade,
    *,
    fill_price: float,
    fill_fee: float,
    slippage_cost: float,
    raw_price: float,
    bar_time: str,
) -> None:
    trade = item.paper
    if trade.entry_price is None or trade.quantity is None:
        return
    trade.status = "TIME_EXIT"
    trade.closed_at_utc = bar_time
    trade.updated_at_utc = bar_time
    trade.exit_price = fill_price
    trade.realized_pnl = (fill_price - trade.entry_price) * trade.quantity
    trade.unrealized_pnl = 0
    trade.notes = "Time exit: TP1 not touched within max_holding_bars_without_tp1."
    item.record.exit_price_raw = raw_price
    item.record.exit_fee = fill_fee
    item.record.slippage_cost += slippage_cost
    trade.realized_pnl -= fill_fee + item.record.entry_fee
    item.record.events.append(
        {
            "event_type": "TIME_EXIT",
            "message": trade.notes,
            "event_time_utc": bar_time,
            "price": fill_price,
        }
    )


def run_backtest_replay(
    settings: Settings,
    symbols: list[str],
    start_utc: str,
    end_utc: str,
    *,
    interval: str | None = None,
    intrabar: str | None = None,
    allow_data_gaps: bool = False,
    universe_mode: bool = False,
    max_universe_symbols: int | None = None,
    dynamic_universe_mode: bool = False,
    source_limit: int | None = None,
    dynamic_symbol_master: SymbolMaster | None = None,
    progress: Callable[[str], None] | None = None,
) -> BacktestResult:
    primary_interval = interval or settings.backtest.primary_interval
    if primary_interval != "4h":
        raise ValueError("MVP backtest currently supports 4h primary interval only.")
    intrabar_policy = intrabar or settings.backtest.intrabar_policy
    if settings.backtest.allow_leverage:
        raise ValueError("MVP backtest is spot-only and does not allow leverage.")
    if universe_mode and dynamic_universe_mode:
        raise ValueError("Use either universe snapshot mode or dynamic universe mode, not both.")

    run_id = uuid.uuid4().hex[:12]
    start_ms = _date_to_ms(f"{start_utc}T00:00:00+00:00" if len(start_utc) == 10 else start_utc)
    end_ms = _date_to_ms(f"{end_utc}T00:00:00+00:00" if len(end_utc) == 10 else end_utc)
    warmup_ms = _effective_warmup_ms(settings)
    fetch_start_ms = start_ms - warmup_ms
    fetch_end_ms = end_ms + interval_ms(primary_interval)
    universe_snapshot = None
    dynamic_master = dynamic_symbol_master
    dynamic_selections = []
    dynamic_universe_summary = None
    if universe_mode:
        snapshot = fetch_universe_snapshot(settings, max_symbols=max_universe_symbols, progress=progress)
        universe_snapshot = snapshot.to_dict()
        symbols = snapshot.selected_symbols
    if dynamic_universe_mode:
        if dynamic_master is None:
            dynamic_master = build_current_symbol_master(settings, source_limit=source_limit, progress=progress)
        symbols = dynamic_master.symbols
    symbols = [symbol.replace("/", "").upper() for symbol in symbols]
    if not symbols:
        raise ValueError("Backtest requires at least one symbol after universe selection.")
    skipped_symbols_no_history: list[str] = []

    klines_by_symbol: dict[str, dict[str, list[list]]] = {}
    regime_klines: dict[str, list[list]] = {}
    data_issues: list[KlineQualityIssue] = []
    symbols_to_fetch = list(dict.fromkeys(symbols + (["BTCUSDT", "ETHUSDT"] if dynamic_universe_mode else [])))
    total_symbols_to_fetch = len(symbols_to_fetch)

    # Phase 1: ensure all klines are in the local cache (downloads from Binance if needed).
    for symbol_index, symbol in enumerate(symbols_to_fetch, start=1):
        if progress is not None:
            if dynamic_universe_mode:
                progress(f"loading historical klines for dynamic universe symbol {symbol_index}/{total_symbols_to_fetch} {symbol}")
            else:
                progress(f"loading historical klines for {symbol}")
        for item_interval in ("1h", "4h", "1d"):
            if progress is not None and dynamic_universe_mode:
                progress(f"loading {symbol_index}/{total_symbols_to_fetch} {symbol} {item_interval} klines")
            fetched = fetch_klines_cached(
                settings,
                symbol,
                item_interval,
                fetch_start_ms,
                fetch_end_ms,
                allow_data_gaps=True if dynamic_universe_mode else allow_data_gaps,
                progress=progress,
            )
            data_issues.extend(fetched.issues)

    # Phase 2: bulk-load all klines for all symbols in a single SQLite query.
    if progress is not None:
        progress(f"bulk loading klines for {len(symbols_to_fetch)} symbols from cache")
    klines_by_symbol = batch_load_klines_cached(
        settings, symbols_to_fetch, ["1h", "4h", "1d"], fetch_start_ms, fetch_end_ms
    )

    if settings.analysis.market_regime_filter_enabled:
        for regime_symbol in ("BTCUSDT", "ETHUSDT"):
            if regime_symbol in klines_by_symbol:
                regime_klines[regime_symbol] = klines_by_symbol[regime_symbol]["1d"]
            else:
                fetched = fetch_klines_cached(
                    settings,
                    regime_symbol,
                    "1d",
                    fetch_start_ms,
                    fetch_end_ms,
                    allow_data_gaps=allow_data_gaps,
                    progress=progress,
                )
                regime_klines[regime_symbol] = fetched.klines
                data_issues.extend(fetched.issues)

    usable_symbols: list[str] = []
    for symbol in symbols:
        period_bars = [kline for kline in klines_by_symbol[symbol]["4h"] if start_ms <= int(kline[0]) < end_ms]
        if period_bars:
            usable_symbols.append(symbol)
        else:
            skipped_symbols_no_history.append(symbol)
            data_issues.append(
                KlineQualityIssue(
                    symbol,
                    primary_interval,
                    "ERROR",
                    "No primary interval klines inside requested backtest period.",
                )
            )
    symbols = symbols if dynamic_universe_mode else usable_symbols
    if universe_snapshot is not None:
        universe_snapshot["replay_symbols"] = usable_symbols
        universe_snapshot["replay_count"] = len(usable_symbols)
        universe_snapshot["skipped_symbols_no_history"] = skipped_symbols_no_history
    if not symbols:
        raise ValueError("Backtest has no symbols with primary interval history inside the requested period.")

    reference_symbol = "BTCUSDT" if dynamic_universe_mode else symbols[0]
    reference = klines_by_symbol.get(reference_symbol, {}).get("4h", [])
    bars = [kline for kline in reference if start_ms <= int(kline[0]) < end_ms]
    if dynamic_universe_mode and not bars:
        raise ValueError("Dynamic universe backtest requires BTCUSDT 4h klines for the requested period.")
    if dynamic_universe_mode and not allow_data_gaps:
        btc_errors = [
            issue.message
            for issue in data_issues
            if issue.symbol == "BTCUSDT" and issue.interval == primary_interval and issue.severity == "ERROR"
        ]
        if btc_errors:
            raise ValueError(f"BTCUSDT {primary_interval} data quality failed: {'; '.join(btc_errors[:3])}")
    cash = settings.backtest.initial_equity
    all_trades: list[_SimTrade] = []
    equity_curve: list[EquityPoint] = []
    kline_4h_by_open = {
        symbol: {int(kline[0]): kline for kline in per_interval["4h"]}
        for symbol, per_interval in klines_by_symbol.items()
    }

    # Per-symbol EMA running state: seeded on first bar that has enough history,
    # then updated incrementally with ema_step instead of full ema_series.
    # Keys: "ema20_4h", "ema50_4h", "ema20_1d", "ema50_1d"
    # Also tracks the last 4h/1d kline count seen to detect when a new bar is added.
    _ema_cache: dict[str, dict] = {}  # symbol -> {ema20_4h, ..., n4h, n1d}
    limitations = [
        "MVP spot backtest: WATCHING is a condition plan, not an exchange-submitted limit order.",
        "24h ticker fields are reconstructed from 1h klines and differ from live rolling /ticker/24hr precision.",
        "4h candles decide execution; no 5m/15m intrabar path reconstruction in this version.",
    ]
    if universe_mode:
        limitations.extend(
            [
                "Universe snapshot mode uses a current Binance market snapshot to choose symbols before historical replay.",
                "Universe snapshot mode is not a full historical dynamic universe; it can still have survivorship bias.",
                "Universe snapshot symbols with no primary-interval history inside the requested period are skipped.",
            ]
        )
    if dynamic_universe_mode:
        limitations.extend(
            [
                "Dynamic universe mode uses current Binance exchangeInfo as the symbol master.",
                "Symbols that traded historically but are delisted today are not included in the symbol master.",
                "Universe membership is refreshed daily using only closed historical klines available at that decision time.",
                "First full dynamic-universe run can be slow because many 1h/4h/1d klines must be cached.",
            ]
        )
    daily_universe_cache: dict[str, list[str]] = {}

    for bar_index, reference_bar in enumerate(bars):
        bar_open_ms = int(reference_bar[0])
        bar_close_ms = bar_open_ms + interval_ms(primary_interval)
        bar_time = _iso_from_ms(bar_close_ms)
        current_bars: dict[str, list] = {}
        mark_prices: dict[str, float] = {}
        for symbol in symbols_to_fetch:
            bar = kline_4h_by_open.get(symbol, {}).get(bar_open_ms)
            if bar is not None:
                current_bars[symbol] = bar
                mark_prices[symbol] = float(bar[4])

        # First advance exits for active positions, then process existing condition plans.
        for item in sorted(_active_positions(all_trades), key=lambda x: (x.created_index, x.paper.symbol)):
            bar = current_bars.get(item.paper.symbol)
            if bar is None:
                continue
            qty = item.paper.quantity or 0
            stop_fill = stop_exit_fill(item.paper.stop_loss, qty, settings.backtest)
            tp2_fill = target_exit_fill(item.paper.take_profit_2, qty, settings.backtest)
            ema20_4h_current: float | None = None
            ema20_4h_current_ready = False
            if settings.analysis.tp1_ema_trailing_stop_enabled or settings.backtest.max_holding_bars_conditional:
                k4h_closed = _closed_slice(klines_by_symbol[item.paper.symbol]["4h"], "4h", bar_close_ms)
                closes_4h = [float(k[4]) for k in k4h_closed]
                if len(closes_4h) >= 20:
                    ema20_4h_current = _ema(closes_4h, 20)
                    ema20_4h_current_ready = True
            events = step_trade(
                item.paper,
                high=float(bar[2]),
                low=float(bar[3]),
                close=float(bar[4]),
                open_price=float(bar[1]),
                event_time_utc=bar_time,
                intrabar=intrabar_policy,
                stop_exit_price_override=stop_fill.filled_price,
                tp2_exit_price_override=tp2_fill.filled_price,
                move_stop_to_breakeven_on_tp1=settings.analysis.tp1_move_stop_to_breakeven_enabled,
                tp1_trailing_ema_stop=ema20_4h_current,
                tp1_trailing_ema_stop_ready=ema20_4h_current_ready,
            )
            for event in events:
                item.record.events.append(asdict(event))
                if event.event_type in {"STOPPED", "CLOSED"} and item.paper.quantity:
                    fill = stop_fill if event.event_type == "STOPPED" else tp2_fill
                    item.record.exit_price_raw = fill.raw_price
                    item.record.exit_fee = fill.fee
                    item.record.slippage_cost += fill.slippage_cost
                    item.paper.realized_pnl -= fill.fee + item.record.entry_fee
                    cash += item.paper.quantity * fill.filled_price - fill.fee
            max_holding_bars = settings.backtest.max_holding_bars_without_tp1
            holding_bars = _holding_bars_since_entry(item.paper, bar_close_ms, primary_interval)
            if (
                max_holding_bars > 0
                and item.paper.status == "ENTERED"
                and item.paper.tp1_hit_at_utc is None
                and holding_bars is not None
                and holding_bars >= max_holding_bars
                and item.paper.quantity
            ):
                bar_close = float(bar[4])
                if settings.backtest.max_holding_bars_conditional:
                    # Conditional mode: only exit if close < EMA20 or close < entry price.
                    # Signals the trade is stalling/reversing rather than just running long.
                    entry_px = item.paper.entry_price or bar_close
                    below_entry = bar_close < entry_px
                    below_ema = ema20_4h_current_ready and bar_close < ema20_4h_current
                    trigger_exit = below_entry or below_ema
                else:
                    trigger_exit = True
                if trigger_exit:
                    time_fill = stop_exit_fill(bar_close, item.paper.quantity, settings.backtest)
                    _force_time_exit(
                        item,
                        fill_price=time_fill.filled_price,
                        fill_fee=time_fill.fee,
                        slippage_cost=time_fill.slippage_cost,
                        raw_price=time_fill.raw_price,
                        bar_time=bar_time,
                    )
                    cash += item.paper.quantity * time_fill.filled_price - time_fill.fee
            _sync_record(item)

        watching = [
            item
            for item in _open_plans(all_trades)
            if item.active_from_ms <= bar_open_ms
        ]
        watching.sort(key=lambda item: (-item.score, item.created_index, item.paper.symbol))
        for item in watching:
            bar = current_bars.get(item.paper.symbol)
            if bar is None:
                continue
            if bar_index - item.created_index > settings.backtest.watch_expiry_bars:
                item.paper.status = "EXPIRED"
                item.paper.closed_at_utc = bar_time
                item.paper.updated_at_utc = bar_time
                item.paper.notes = "Backtest WATCHING plan expired before entry."
                _sync_record(item)
                continue
            high = float(bar[2])
            low = float(bar[3])
            close = float(bar[4])
            if high < item.paper.entry_low or low > item.paper.entry_high:
                step_trade(
                    item.paper,
                    high=high,
                    low=low,
                    close=close,
                    open_price=float(bar[1]),
                    event_time_utc=bar_time,
                    intrabar=intrabar_policy,
                )
                _sync_record(item)
                continue
            if not _entry_reclaim_close_satisfied(
                settings.analysis.entry_reclaim_close_enabled,
                close,
                item.paper.entry_high,
            ):
                item.paper.last_price = close
                item.paper.updated_at_utc = bar_time
                item.paper.notes = "Watching: entry zone touched, but 4h close has not reclaimed entry_high."
                _sync_record(item)
                continue

            raw_entry = item.paper.entry_high
            estimated_qty = position_size(
                _portfolio_equity(cash, all_trades, mark_prices),
                settings.backtest.risk_per_trade_pct,
                raw_entry,
                item.paper.stop_loss,
            )
            if estimated_qty is None or estimated_qty <= 0:
                continue
            entry_preview = entry_fill(raw_entry, estimated_qty, settings.backtest)
            equity = _portfolio_equity(cash, all_trades, mark_prices)
            max_cash_qty = cash / (entry_preview.filled_price * (1 + settings.backtest.maker_fee_bps / 10_000))
            max_notional_qty = (equity * settings.backtest.max_position_notional_pct) / entry_preview.filled_price
            qty = min(estimated_qty, max_cash_qty, max_notional_qty)
            if qty <= 0:
                item.record.notes = "Skipped entry: insufficient cash."
                continue
            item.paper.cash_risk = max(entry_preview.filled_price - item.paper.stop_loss, 0) * qty
            if len(_active_positions(all_trades)) >= settings.backtest.max_active_positions:
                item.record.notes = "Skipped entry: max active positions reached."
                continue
            active_risk_after = _active_risk(all_trades) + item.paper.cash_risk
            if active_risk_after > equity * settings.backtest.total_active_risk_pct:
                item.record.notes = "Skipped entry: total active risk limit reached."
                continue
            final_entry = entry_fill(raw_entry, qty, settings.backtest)
            stop_fill = stop_exit_fill(item.paper.stop_loss, qty, settings.backtest)
            ema20_4h_entry: float | None = None
            ema20_4h_entry_ready = False
            if settings.analysis.tp1_ema_trailing_stop_enabled:
                k4h_closed_entry = _closed_slice(klines_by_symbol[item.paper.symbol]["4h"], "4h", bar_close_ms)
                closes_4h_entry = [float(k[4]) for k in k4h_closed_entry]
                if len(closes_4h_entry) >= 20:
                    ema20_4h_entry = _ema(closes_4h_entry, 20)
                    ema20_4h_entry_ready = True
            events = step_trade(
                item.paper,
                high=high,
                low=low,
                close=close,
                open_price=float(bar[1]),
                event_time_utc=bar_time,
                intrabar=intrabar_policy,
                entry_price_override=final_entry.filled_price,
                stop_exit_price_override=stop_fill.filled_price,
                move_stop_to_breakeven_on_tp1=settings.analysis.tp1_move_stop_to_breakeven_enabled,
                tp1_trailing_ema_stop=ema20_4h_entry,
                tp1_trailing_ema_stop_ready=ema20_4h_entry_ready,
            )
            for event in events:
                item.record.events.append(asdict(event))
                if event.event_type == "ENTERED" and item.paper.quantity:
                    item.record.entry_price_raw = final_entry.raw_price
                    item.record.entry_fee = final_entry.fee
                    item.record.slippage_cost += final_entry.slippage_cost
                    cash -= item.paper.quantity * final_entry.filled_price + final_entry.fee
                if event.event_type == "STOPPED" and item.paper.quantity:
                    item.record.exit_price_raw = stop_fill.raw_price
                    item.record.exit_fee = stop_fill.fee
                    item.record.slippage_cost += stop_fill.slippage_cost
                    item.paper.realized_pnl -= stop_fill.fee + item.record.entry_fee
                    cash += item.paper.quantity * stop_fill.filled_price - stop_fill.fee
            _sync_record(item)

        equity = _portfolio_equity(cash, all_trades, mark_prices)
        equity_curve.append(
            EquityPoint(
                timestamp_utc=bar_time,
                equity=equity,
                cash=cash,
                open_positions=len(_active_positions(all_trades)),
                open_plans=len(_open_plans(all_trades)),
                intrabar_equity_low=_portfolio_intrabar_low(cash, all_trades, current_bars),
            )
        )

        # Generate new condition plans after this bar is fully closed.
        if progress is not None and bar_index % 20 == 0:
            progress(f"backtest replay {bar_index + 1}/{len(bars)} bars")
        market_regime_allows_buy = True
        market_regime_status = None
        if settings.analysis.market_regime_filter_enabled:
            btc_1d = _closed_slice(regime_klines.get("BTCUSDT", []), "1d", bar_close_ms)
            eth_1d = _closed_slice(regime_klines.get("ETHUSDT", []), "1d", bar_close_ms)
            market_regime = classify_market_regime(
                btc_1d,
                eth_1d,
                btc_7d_drop_pct=settings.analysis.regime_btc_7d_drop_pct,
                eth_7d_drop_pct=settings.analysis.regime_eth_7d_drop_pct,
                require_both_trend=settings.analysis.regime_require_both_trend,
            )
            market_regime_allows_buy = market_regime.allows_alt_buy
            market_regime_status = market_regime.status
        benchmark_pct_24h = _benchmark_pct_24h(klines_by_symbol, bar_close_ms)
        unavailable = {item.paper.symbol for item in all_trades if item.paper.status in {"WATCHING", "ENTERED", "TP1_HIT"}}
        candidate_pool: list[TradeCandidate] = []
        analysis_symbols = symbols
        if dynamic_universe_mode:
            day_key = dynamic_universe_refresh_key(bar_close_ms)
            if day_key not in daily_universe_cache:
                selection = select_dynamic_universe_for_day(
                    settings,
                    symbols,
                    klines_by_symbol,
                    bar_close_ms,
                    max_symbols=max_universe_symbols or settings.market.max_universe,
                )
                dynamic_selections.append(selection)
                daily_universe_cache[day_key] = selection.selected_symbols
                if progress is not None:
                    progress(
                        f"dynamic universe {day_key}: selected {len(selection.selected_symbols)}/"
                        f"{selection.candidate_count} candidates"
                    )
            analysis_symbols = daily_universe_cache[day_key]
        for symbol in analysis_symbols:
            if symbol in unavailable:
                continue
            if not _listing_date_allows(dynamic_symbol_master, symbol, bar_close_ms, settings.analysis.min_history_days):
                continue
            k1h = _closed_slice(klines_by_symbol[symbol]["1h"], "1h", bar_close_ms)
            k4h = _closed_slice(klines_by_symbol[symbol]["4h"], "4h", bar_close_ms)
            k1d = _closed_slice(klines_by_symbol[symbol]["1d"], "1d", bar_close_ms)
            if len(k1h) < 168 or len(k4h) < 80 or len(k1d) < max(60, settings.analysis.min_history_days):
                continue

            # Update per-symbol EMA cache incrementally.
            n4h, n1d = len(k4h), len(k1d)
            cached = _ema_cache.get(symbol)
            if cached is None or n4h < 50 or n1d < 50:
                # Seed from scratch (first time or not enough history yet).
                closes_4h_seed = [float(k[4]) for k in k4h]
                closes_1d_seed = [float(k[4]) for k in k1d]
                _ema_cache[symbol] = {
                    "ema20_4h": _ema(closes_4h_seed, 20),
                    "ema50_4h": _ema(closes_4h_seed, 50),
                    "ema20_1d": _ema(closes_1d_seed, 20),
                    "ema50_1d": _ema(closes_1d_seed, 50),
                    "n4h": n4h,
                    "n1d": n1d,
                }
                cached = _ema_cache[symbol]
            else:
                # Incremental update: apply ema_step for each new 4h/1d bar since last call.
                new4h = n4h - cached["n4h"]
                new1d = n1d - cached["n1d"]
                if new4h > 0:
                    for k in k4h[-new4h:]:
                        c = float(k[4])
                        if cached["ema20_4h"] is not None:
                            cached["ema20_4h"] = _ema_step(cached["ema20_4h"], c, 20)
                        if cached["ema50_4h"] is not None:
                            cached["ema50_4h"] = _ema_step(cached["ema50_4h"], c, 50)
                    cached["n4h"] = n4h
                if new1d > 0:
                    for k in k1d[-new1d:]:
                        c = float(k[4])
                        if cached["ema20_1d"] is not None:
                            cached["ema20_1d"] = _ema_step(cached["ema20_1d"], c, 20)
                        if cached["ema50_1d"] is not None:
                            cached["ema50_1d"] = _ema_step(cached["ema50_1d"], c, 50)
                    cached["n1d"] = n1d

            ticker = reconstruct_ticker(
                symbol,
                _symbol_base(symbol, settings.market.quote_asset),
                k1h,
            )
            candidate = _analyze_ticker(
                ticker,
                k1h,
                k4h,
                k1d,
                settings.analysis.risk_reward_min,
                min_history_days=settings.analysis.min_history_days,
                market_regime_allows_buy=market_regime_allows_buy,
                market_regime_status=market_regime_status,
                risk_off_core_buy_enabled=settings.analysis.risk_off_core_buy_enabled,
                risk_off_large_cap_buy_enabled=settings.analysis.risk_off_large_cap_buy_enabled,
                pump_chase_24h_pct=settings.analysis.pump_chase_24h_pct,
                pump_chase_distance_pct=settings.analysis.pump_chase_distance_pct,
                pump_chase_penalty=settings.analysis.pump_chase_penalty,
                high_volatility_range_pct=settings.analysis.high_volatility_range_pct,
                high_volatility_penalty=settings.analysis.high_volatility_penalty,
                daily_trend_required=settings.analysis.daily_trend_required,
                relative_strength_soft_gate_enabled=settings.analysis.relative_strength_soft_gate_enabled,
                relative_strength_min_pct=settings.analysis.relative_strength_min_pct,
                benchmark_pct_24h=benchmark_pct_24h,
                precomputed_indicators=cached,
            )
            if candidate is not None and candidate.action == "BUY_CANDIDATE":
                candidate_pool.append(candidate)
        candidate_pool.sort(key=lambda item: item.score, reverse=True)
        current_open_plans = len(_open_plans(all_trades))
        for rank, candidate in enumerate(candidate_pool[: settings.market.top_n], start=1):
            if current_open_plans >= settings.backtest.max_open_plans:
                break
            candidate.rank = rank
            sim_trade = _candidate_to_sim_trade(
                run_id,
                candidate,
                bar_time,
                bar_close_ms,
                bar_index,
                settings,
                equity,
            )
            all_trades.append(sim_trade)
            current_open_plans += 1

    final_mark = {
        symbol: float(prior[-1][4])
        for symbol in symbols_to_fetch
        for prior in [[kline for kline in klines_by_symbol[symbol]["4h"] if int(kline[0]) < end_ms]]
        if prior
    }
    final_equity = _portfolio_equity(cash, all_trades, final_mark)
    final_time = _iso_from_ms(end_ms)
    for item in all_trades:
        if item.paper.status == "WATCHING":
            item.paper.status = "EXPIRED_END"
            item.paper.closed_at_utc = final_time
            item.paper.updated_at_utc = final_time
            item.paper.notes = "Backtest ended before condition plan entered."
        elif item.paper.status in {"ENTERED", "TP1_HIT"}:
            last_price = final_mark.get(item.paper.symbol, item.paper.last_price or 0)
            item.paper.last_price = last_price
            item.paper.unrealized_pnl = ((last_price - (item.paper.entry_price or last_price)) * (item.paper.quantity or 0))
            item.paper.updated_at_utc = final_time
            item.paper.notes = "Open at backtest end; mark-to-market only."
        _sync_record(item)

    result_symbols = symbols
    if dynamic_universe_mode:
        selected_symbols = sorted({symbol for selection in dynamic_selections for symbol in selection.selected_symbols})
        trade_symbols = sorted({item.record.symbol for item in all_trades})
        result_symbols = sorted(set(selected_symbols) | set(trade_symbols))
        if dynamic_master is None:
            raise ValueError("Dynamic universe mode requires a symbol master.")
        dynamic_universe_summary = build_dynamic_universe_summary(
            dynamic_master,
            dynamic_selections,
            max_symbols=max_universe_symbols or settings.market.max_universe,
        ).to_dict()

    return BacktestResult(
        run_id=run_id,
        symbols=result_symbols,
        start_utc=_iso_from_ms(start_ms),
        end_utc=_iso_from_ms(end_ms),
        created_at_utc=datetime.now(timezone.utc).isoformat(timespec="seconds"),
        initial_equity=settings.backtest.initial_equity,
        final_equity=final_equity,
        cash=cash,
        trades=[item.record for item in all_trades],
        equity_curve=equity_curve,
        data_issues=data_issues,
        config_snapshot={
            "backtest": asdict(settings.backtest),
            "analysis": asdict(settings.analysis),
            "market_top_n": settings.market.top_n,
            "universe_mode": universe_mode,
            "universe_snapshot": universe_snapshot,
            "dynamic_universe_mode": dynamic_universe_mode,
            "dynamic_universe_summary": dynamic_universe_summary,
        },
        limitations=limitations,
        universe_mode=universe_mode or dynamic_universe_mode,
        universe_snapshot=universe_snapshot,
        universe_type="dynamic" if dynamic_universe_mode else ("snapshot" if universe_mode else "manual"),
        dynamic_universe_summary=dynamic_universe_summary,
    )
