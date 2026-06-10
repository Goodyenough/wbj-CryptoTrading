from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import json
import math
from pathlib import Path
from typing import Callable

from ..config import Settings
from ..data_quality import EXCLUDED_SUFFIXES, filter_tickers, tradable_spot_symbols
from ..market_data import BinanceClient
from ..models import RawTicker
from ..ticker_utils import reconstruct_ticker
from .history import interval_ms


@dataclass
class UniverseSnapshot:
    mode: str
    source: str
    snapshot_at_utc: str
    filters: str
    selected_symbols: list[str]
    candidate_count: int
    selected_count: int

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class SymbolMaster:
    source: str
    created_at_utc: str
    symbols: list[str]
    source_limit: int | None
    source_limit_applied: bool
    filters: str
    listing_dates: dict[str, str] | None = None  # symbol -> "YYYY-MM-DD" of first 1d candle

    def to_dict(self) -> dict:
        return asdict(self)


def save_symbol_master(master: SymbolMaster, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(master.to_dict(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_symbol_master(path: Path) -> SymbolMaster:
    data = json.loads(path.read_text(encoding="utf-8"))
    required = {"source", "created_at_utc", "symbols", "source_limit", "source_limit_applied", "filters"}
    missing = sorted(required - set(data))
    if missing:
        raise ValueError(f"Symbol master file is missing required keys: {', '.join(missing)}")
    symbols = data["symbols"]
    if not isinstance(symbols, list) or not all(isinstance(symbol, str) and symbol for symbol in symbols):
        raise ValueError("Symbol master file must contain a non-empty string list in 'symbols'.")
    raw_listing = data.get("listing_dates")
    listing_dates: dict[str, str] | None = None
    if isinstance(raw_listing, dict):
        listing_dates = {str(k): str(v) for k, v in raw_listing.items()}
    return SymbolMaster(
        source=str(data["source"]),
        created_at_utc=str(data["created_at_utc"]),
        symbols=[symbol.replace("/", "").upper() for symbol in symbols],
        source_limit=data["source_limit"],
        source_limit_applied=bool(data["source_limit_applied"]),
        filters=str(data["filters"]),
        listing_dates=listing_dates,
    )


@dataclass
class DynamicUniverseSelection:
    date_utc: str
    decision_time_utc: str
    selected_symbols: list[str]
    candidate_count: int
    filter_counts: dict[str, int]

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class DynamicUniverseSummary:
    mode: str
    source: str
    created_at_utc: str
    refresh_frequency: str
    max_symbols: int
    master_count: int
    source_limit: int | None
    source_limit_applied: bool
    universe_refresh_count: int
    selected_count_min: int
    selected_count_avg: float
    selected_count_max: int
    top_selected_symbols: list[dict[str, int | str]]
    filter_counts: dict[str, int]
    selection_by_day: list[dict]
    limitations: list[str]

    def to_dict(self) -> dict:
        return asdict(self)


def universe_preselection_score(ticker: RawTicker) -> float:
    return (
        math.log10(max(ticker.quote_volume_24h, 1)) * 5
        + max(ticker.pct_24h, 0) * 2
        - max(ticker.high_low_range_24h - 40, 0)
    )


def _quote_filter_description(settings: Settings, limit: int | None = None) -> str:
    suffix = "" if limit is None else f"; max_symbols={limit}"
    return (
        f"{settings.market.quote_asset} spot; 24h quote volume >= "
        f"{settings.market.min_quote_volume:,.0f}; trades >= {settings.market.min_trades:,}; "
        f"exclude bases={','.join(settings.market.exclude_bases)}{suffix}"
    )


# Earliest possible Binance listing: 2017-07-14 (BNB)
_LISTING_EPOCH_MS = 1_500_000_000_000


def fetch_symbol_listing_dates(
    settings: Settings,
    symbols: list[str],
    *,
    progress: Callable[[str], None] | None = None,
) -> dict[str, str]:
    """Return a mapping of symbol -> YYYY-MM-DD of its first 1d candle on Binance."""
    client = BinanceClient(
        settings.market.base_url,
        timeout_seconds=settings.market.request_timeout_seconds,
        pause_seconds=settings.market.request_pause_seconds,
    )
    listing_dates: dict[str, str] = {}
    for i, symbol in enumerate(symbols):
        if progress is not None and i % 50 == 0:
            progress(f"fetching listing date {i + 1}/{len(symbols)}")
        try:
            klines = client.klines(symbol, "1d", limit=1, start_time_ms=_LISTING_EPOCH_MS)
            if klines:
                open_time_ms = int(klines[0][0])
                listing_dates[symbol] = datetime.fromtimestamp(open_time_ms / 1000, tz=timezone.utc).date().isoformat()
        except Exception:
            pass  # symbol with no history simply omitted
    return listing_dates


def listing_date_allows_analysis(
    listing_dates: dict[str, str] | None,
    symbol: str,
    bar_close_ms: int,
    min_history_days: int,
) -> bool:
    """Return False if listing_dates shows this symbol hasn't had enough history by bar_close_ms."""
    if not listing_dates:
        return True
    listing_str = listing_dates.get(symbol)
    if not listing_str:
        return True
    listing_ms = int(datetime.fromisoformat(listing_str + "T00:00:00+00:00").timestamp() * 1000)
    return bar_close_ms >= listing_ms + min_history_days * 86_400_000


def build_current_symbol_master(
    settings: Settings,
    *,
    source_limit: int | None = None,
    fetch_listing_dates: bool = False,
    progress: Callable[[str], None] | None = None,
) -> SymbolMaster:
    client = BinanceClient(
        settings.market.base_url,
        timeout_seconds=settings.market.request_timeout_seconds,
        pause_seconds=settings.market.request_pause_seconds,
    )
    if progress is not None:
        progress("loading Binance exchange info for dynamic universe symbol master")
    exchange_info = client.exchange_info()
    symbol_meta = tradable_spot_symbols(exchange_info, settings.market.quote_asset)
    excluded = {item.upper() for item in settings.market.exclude_bases}
    symbols: list[str] = []
    for symbol, meta in symbol_meta.items():
        base_asset = str(meta.get("baseAsset", "")).upper()
        if base_asset in excluded:
            continue
        if symbol.endswith(EXCLUDED_SUFFIXES):
            continue
        symbols.append(symbol)
    symbols = sorted(symbols)
    source_limit_applied = source_limit is not None and source_limit >= 0 and source_limit < len(symbols)
    if source_limit is not None:
        symbols = symbols[: max(0, source_limit)]
    master = SymbolMaster(
        source="Binance current exchangeInfo tradable USDT spot symbols",
        created_at_utc=datetime.now(timezone.utc).isoformat(timespec="seconds"),
        symbols=symbols,
        source_limit=source_limit,
        source_limit_applied=source_limit_applied,
        filters=(
            f"{settings.market.quote_asset} spot; exclude bases={','.join(settings.market.exclude_bases)}; "
            "exclude leveraged token suffixes=UPUSDT,DOWNUSDT,BULLUSDT,BEARUSDT"
        ),
    )
    if fetch_listing_dates:
        if progress is not None:
            progress(f"fetching listing dates for {len(master.symbols)} symbols (this may take a moment)")
        master.listing_dates = fetch_symbol_listing_dates(settings, master.symbols, progress=progress)
    if progress is not None:
        progress(
            f"dynamic universe symbol master contains {len(master.symbols)} symbols"
            + (" after source-limit" if source_limit_applied else "")
            + (" with listing dates" if master.listing_dates else "")
        )
    return master


def _closed_slice(klines: list[list], interval: str, decision_ms: int) -> list[list]:
    step = interval_ms(interval)
    return [kline for kline in klines if int(kline[0]) + step <= decision_ms]


def dynamic_universe_refresh_key(decision_ms: int) -> str:
    return datetime.fromtimestamp(decision_ms / 1000, tz=timezone.utc).date().isoformat()


def select_dynamic_universe_for_day(
    settings: Settings,
    symbol_master: list[str],
    klines_by_symbol: dict[str, dict[str, list[list]]],
    decision_ms: int,
    *,
    max_symbols: int,
) -> DynamicUniverseSelection:
    date_utc = dynamic_universe_refresh_key(decision_ms)
    decision_time_utc = datetime.fromtimestamp(decision_ms / 1000, tz=timezone.utc).isoformat(timespec="seconds")
    accepted: list[RawTicker] = []
    filter_counts = {
        "missing_1h": 0,
        "insufficient_24h": 0,
        "reconstruct_error": 0,
        "low_quote_volume": 0,
        "low_trades": 0,
        "stable_like": 0,
    }
    for symbol in symbol_master:
        per_interval = klines_by_symbol.get(symbol, {})
        k1h = _closed_slice(per_interval.get("1h", []), "1h", decision_ms)
        if not k1h:
            filter_counts["missing_1h"] += 1
            continue
        if len(k1h) < 25:
            filter_counts["insufficient_24h"] += 1
            continue
        try:
            ticker = reconstruct_ticker(
                symbol,
                _symbol_base(symbol, settings.market.quote_asset),
                k1h,
            )
        except Exception:
            filter_counts["reconstruct_error"] += 1
            continue
        if ticker.quote_volume_24h < settings.market.min_quote_volume:
            filter_counts["low_quote_volume"] += 1
            continue
        if ticker.trades_24h < settings.market.min_trades:
            filter_counts["low_trades"] += 1
            continue
        if 0.97 < ticker.price < 1.03 and ticker.high_low_range_24h < 1:
            filter_counts["stable_like"] += 1
            continue
        accepted.append(ticker)
    accepted.sort(key=universe_preselection_score, reverse=True)
    selected = accepted[: max(0, max_symbols)]
    return DynamicUniverseSelection(
        date_utc=date_utc,
        decision_time_utc=decision_time_utc,
        selected_symbols=[ticker.symbol for ticker in selected],
        candidate_count=len(accepted),
        filter_counts=filter_counts,
    )


def build_dynamic_universe_summary(
    master: SymbolMaster,
    selections: list[DynamicUniverseSelection],
    *,
    max_symbols: int,
) -> DynamicUniverseSummary:
    selected_counts = [len(selection.selected_symbols) for selection in selections]
    symbol_frequency: dict[str, int] = {}
    filter_counts: dict[str, int] = {}
    for selection in selections:
        for symbol in selection.selected_symbols:
            symbol_frequency[symbol] = symbol_frequency.get(symbol, 0) + 1
        for key, value in selection.filter_counts.items():
            filter_counts[key] = filter_counts.get(key, 0) + value
    top_selected = [
        {"symbol": symbol, "days_selected": count}
        for symbol, count in sorted(symbol_frequency.items(), key=lambda item: (-item[1], item[0]))[:20]
    ]
    return DynamicUniverseSummary(
        mode="dynamic_universe",
        source=master.source,
        created_at_utc=datetime.now(timezone.utc).isoformat(timespec="seconds"),
        refresh_frequency="daily",
        max_symbols=max_symbols,
        master_count=len(master.symbols),
        source_limit=master.source_limit,
        source_limit_applied=master.source_limit_applied,
        universe_refresh_count=len(selections),
        selected_count_min=min(selected_counts) if selected_counts else 0,
        selected_count_avg=(sum(selected_counts) / len(selected_counts)) if selected_counts else 0.0,
        selected_count_max=max(selected_counts) if selected_counts else 0,
        top_selected_symbols=top_selected,
        filter_counts=filter_counts,
        selection_by_day=[selection.to_dict() for selection in selections],
        limitations=[
            "Symbol master is built from current Binance exchangeInfo.",
            "Symbols that traded historically but are delisted today are not in the master list.",
            "First full run can be slow because 1h/4h/1d klines are cached for many symbols.",
        ],
    )


def _symbol_base(symbol: str, quote_asset: str) -> str:
    if symbol.endswith(quote_asset):
        return symbol[: -len(quote_asset)]
    return symbol


def fetch_universe_snapshot(
    settings: Settings,
    *,
    max_symbols: int | None = None,
    progress: Callable[[str], None] | None = None,
) -> UniverseSnapshot:
    client = BinanceClient(
        settings.market.base_url,
        timeout_seconds=settings.market.request_timeout_seconds,
        pause_seconds=settings.market.request_pause_seconds,
    )
    if progress is not None:
        progress("loading Binance exchange info for universe snapshot")
    exchange_info = client.exchange_info()
    symbol_meta = tradable_spot_symbols(exchange_info, settings.market.quote_asset)
    if progress is not None:
        progress("loading Binance 24h tickers for universe snapshot")
    tickers = client.ticker_24hr()
    raw_tickers = filter_tickers(
        tickers,
        symbol_meta,
        settings.market.min_quote_volume,
        settings.market.min_trades,
        settings.market.exclude_bases,
    )
    raw_tickers.sort(key=universe_preselection_score, reverse=True)
    limit = max_symbols if max_symbols is not None else settings.market.max_universe
    selected = raw_tickers[: max(0, limit)]
    snapshot = UniverseSnapshot(
        mode="universe_snapshot",
        source="Binance exchangeInfo + current 24hr ticker snapshot",
        snapshot_at_utc=datetime.now(timezone.utc).isoformat(timespec="seconds"),
        filters=_quote_filter_description(settings, limit),
        selected_symbols=[ticker.symbol for ticker in selected],
        candidate_count=len(raw_tickers),
        selected_count=len(selected),
    )
    if progress is not None:
        progress(f"universe snapshot selected {snapshot.selected_count}/{snapshot.candidate_count} symbols")
    return snapshot
