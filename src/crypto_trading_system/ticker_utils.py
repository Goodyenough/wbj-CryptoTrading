from __future__ import annotations

from .indicators import percent_change
from .models import RawTicker


def reconstruct_ticker(
    symbol: str,
    base_asset: str,
    klines_1h: list[list],
    as_of_index: int | None = None,
) -> RawTicker:
    if not klines_1h:
        raise ValueError("klines_1h is empty")
    index = len(klines_1h) - 1 if as_of_index is None else as_of_index
    if index < 0 or index >= len(klines_1h):
        raise IndexError("as_of_index is outside klines_1h")
    if index < 24:
        raise ValueError("at least 25 hourly candles are required to reconstruct 24h ticker fields")

    window = klines_1h[index - 23 : index + 1]
    price = float(klines_1h[index][4])
    previous_close = float(klines_1h[index - 24][4])
    pct_24h = percent_change(previous_close, price) or 0.0
    quote_volume_24h = sum(float(kline[7]) for kline in window)
    trades_24h = sum(int(kline[8]) for kline in window)
    high_24h = max(float(kline[2]) for kline in window)
    low_24h = min(float(kline[3]) for kline in window)
    high_low_range_24h = ((high_24h / low_24h) - 1) * 100 if low_24h > 0 else 0.0
    return RawTicker(
        symbol=symbol,
        base_asset=base_asset,
        price=price,
        pct_24h=pct_24h,
        quote_volume_24h=quote_volume_24h,
        trades_24h=trades_24h,
        high_low_range_24h=high_low_range_24h,
    )
