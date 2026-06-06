from __future__ import annotations

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
from .costs import entry_fill, stop_exit_fill, target_exit_fill
from .history import KlineQualityIssue, fetch_klines_cached, interval_ms


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
    step = interval_ms(interval)
    return [kline for kline in klines if int(kline[0]) + step <= decision_ms]


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
    if trade.cash_risk > 0 and trade.status in {"STOPPED", "CLOSED"}:
        record.r_multiple_net = trade.realized_pnl / trade.cash_risk
    record.notes = trade.notes


def run_backtest_replay(
    settings: Settings,
    symbols: list[str],
    start_utc: str,
    end_utc: str,
    *,
    interval: str | None = None,
    intrabar: str | None = None,
    allow_data_gaps: bool = False,
    progress: Callable[[str], None] | None = None,
) -> BacktestResult:
    primary_interval = interval or settings.backtest.primary_interval
    if primary_interval != "4h":
        raise ValueError("MVP backtest currently supports 4h primary interval only.")
    intrabar_policy = intrabar or settings.backtest.intrabar_policy
    if settings.backtest.allow_leverage:
        raise ValueError("MVP backtest is spot-only and does not allow leverage.")

    run_id = uuid.uuid4().hex[:12]
    start_ms = _date_to_ms(f"{start_utc}T00:00:00+00:00" if len(start_utc) == 10 else start_utc)
    end_ms = _date_to_ms(f"{end_utc}T00:00:00+00:00" if len(end_utc) == 10 else end_utc)
    warmup_ms = max(
        settings.backtest.warmup_1h_bars * interval_ms("1h"),
        settings.backtest.warmup_4h_bars * interval_ms("4h"),
        settings.backtest.warmup_1d_bars * interval_ms("1d"),
    )
    fetch_start_ms = start_ms - warmup_ms
    fetch_end_ms = end_ms + interval_ms(primary_interval)
    symbols = [symbol.replace("/", "").upper() for symbol in symbols]

    klines_by_symbol: dict[str, dict[str, list[list]]] = {}
    regime_klines: dict[str, list[list]] = {}
    data_issues: list[KlineQualityIssue] = []
    for symbol in symbols:
        if progress is not None:
            progress(f"loading historical klines for {symbol}")
        per_interval: dict[str, list[list]] = {}
        for item_interval in ("1h", "4h", "1d"):
            fetched = fetch_klines_cached(
                settings,
                symbol,
                item_interval,
                fetch_start_ms,
                fetch_end_ms,
                allow_data_gaps=allow_data_gaps,
                progress=progress,
            )
            per_interval[item_interval] = fetched.klines
            data_issues.extend(fetched.issues)
        klines_by_symbol[symbol] = per_interval
    if settings.analysis.market_regime_filter_enabled:
        for regime_symbol in ("BTCUSDT", "ETHUSDT"):
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

    reference = klines_by_symbol[symbols[0]]["4h"]
    bars = [kline for kline in reference if start_ms <= int(kline[0]) < end_ms]
    cash = settings.backtest.initial_equity
    all_trades: list[_SimTrade] = []
    equity_curve: list[EquityPoint] = []
    limitations = [
        "MVP spot backtest: WATCHING is a condition plan, not an exchange-submitted limit order.",
        "24h ticker fields are reconstructed from 1h klines and differ from live rolling /ticker/24hr precision.",
        "4h candles decide execution; no 5m/15m intrabar path reconstruction in this version.",
    ]

    for bar_index, reference_bar in enumerate(bars):
        bar_open_ms = int(reference_bar[0])
        bar_close_ms = bar_open_ms + interval_ms(primary_interval)
        bar_time = _iso_from_ms(bar_close_ms)
        current_bars: dict[str, list] = {}
        mark_prices: dict[str, float] = {}
        for symbol in symbols:
            matching = [kline for kline in klines_by_symbol[symbol]["4h"] if int(kline[0]) == bar_open_ms]
            if matching:
                current_bars[symbol] = matching[0]
                mark_prices[symbol] = float(matching[0][4])

        # First advance exits for active positions, then process existing condition plans.
        for item in sorted(_active_positions(all_trades), key=lambda x: (x.created_index, x.paper.symbol)):
            bar = current_bars.get(item.paper.symbol)
            if bar is None:
                continue
            qty = item.paper.quantity or 0
            stop_fill = stop_exit_fill(item.paper.stop_loss, qty, settings.backtest)
            tp2_fill = target_exit_fill(item.paper.take_profit_2, qty, settings.backtest)
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
            if high < item.paper.entry_low or low > item.paper.entry_high:
                step_trade(
                    item.paper,
                    high=high,
                    low=low,
                    close=float(bar[4]),
                    open_price=float(bar[1]),
                    event_time_utc=bar_time,
                    intrabar=intrabar_policy,
                )
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
            events = step_trade(
                item.paper,
                high=high,
                low=low,
                close=float(bar[4]),
                open_price=float(bar[1]),
                event_time_utc=bar_time,
                intrabar=intrabar_policy,
                entry_price_override=final_entry.filled_price,
                stop_exit_price_override=stop_fill.filled_price,
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
        if settings.analysis.market_regime_filter_enabled:
            btc_1d = _closed_slice(regime_klines.get("BTCUSDT", []), "1d", bar_close_ms)
            eth_1d = _closed_slice(regime_klines.get("ETHUSDT", []), "1d", bar_close_ms)
            market_regime_allows_buy = classify_market_regime(btc_1d, eth_1d).allows_alt_buy
        unavailable = {item.paper.symbol for item in all_trades if item.paper.status in {"WATCHING", "ENTERED", "TP1_HIT"}}
        candidate_pool: list[TradeCandidate] = []
        for symbol in symbols:
            if symbol in unavailable:
                continue
            k1h = _closed_slice(klines_by_symbol[symbol]["1h"], "1h", bar_close_ms)
            k4h = _closed_slice(klines_by_symbol[symbol]["4h"], "4h", bar_close_ms)
            k1d = _closed_slice(klines_by_symbol[symbol]["1d"], "1d", bar_close_ms)
            if len(k1h) < 168 or len(k4h) < 80 or len(k1d) < max(60, settings.analysis.min_history_days):
                continue
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
        symbol: float([k for k in klines_by_symbol[symbol]["4h"] if int(k[0]) < end_ms][-1][4])
        for symbol in symbols
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

    return BacktestResult(
        run_id=run_id,
        symbols=symbols,
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
        },
        limitations=limitations,
    )
