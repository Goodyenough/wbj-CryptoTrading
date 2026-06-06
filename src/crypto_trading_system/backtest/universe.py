from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import math
from typing import Callable

from ..config import Settings
from ..data_quality import filter_tickers, tradable_spot_symbols
from ..market_data import BinanceClient


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
    raw_tickers.sort(
        key=lambda ticker: (
            math.log10(max(ticker.quote_volume_24h, 1)) * 5
            + max(ticker.pct_24h, 0) * 2
            - max(ticker.high_low_range_24h - 40, 0)
        ),
        reverse=True,
    )
    limit = max_symbols if max_symbols is not None else settings.market.max_universe
    selected = raw_tickers[: max(0, limit)]
    snapshot = UniverseSnapshot(
        mode="universe_snapshot",
        source="Binance exchangeInfo + current 24hr ticker snapshot",
        snapshot_at_utc=datetime.now(timezone.utc).isoformat(timespec="seconds"),
        filters=(
            f"{settings.market.quote_asset} spot; 24h quote volume >= "
            f"{settings.market.min_quote_volume:,.0f}; trades >= {settings.market.min_trades:,}; "
            f"exclude bases={','.join(settings.market.exclude_bases)}; max_symbols={limit}"
        ),
        selected_symbols=[ticker.symbol for ticker in selected],
        candidate_count=len(raw_tickers),
        selected_count=len(selected),
    )
    if progress is not None:
        progress(f"universe snapshot selected {snapshot.selected_count}/{snapshot.candidate_count} symbols")
    return snapshot
