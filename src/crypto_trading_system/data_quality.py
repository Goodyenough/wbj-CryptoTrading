from __future__ import annotations

from collections.abc import Iterable

from .models import RawTicker


EXCLUDED_SUFFIXES = ("UPUSDT", "DOWNUSDT", "BULLUSDT", "BEARUSDT")


def tradable_spot_symbols(
    exchange_info: dict,
    quote_asset: str,
) -> dict[str, dict]:
    symbols: dict[str, dict] = {}
    for item in exchange_info.get("symbols", []):
        if item.get("status") != "TRADING":
            continue
        if item.get("quoteAsset") != quote_asset:
            continue
        if not item.get("isSpotTradingAllowed"):
            continue
        symbols[item["symbol"]] = item
    return symbols


def filter_tickers(
    tickers: Iterable[dict],
    symbol_meta: dict[str, dict],
    min_quote_volume: float,
    min_trades: int,
    exclude_bases: Iterable[str],
) -> list[RawTicker]:
    excluded = {x.upper() for x in exclude_bases}
    accepted: list[RawTicker] = []

    for ticker in tickers:
        symbol = ticker.get("symbol", "")
        if symbol not in symbol_meta:
            continue
        if symbol.endswith(EXCLUDED_SUFFIXES):
            continue

        meta = symbol_meta[symbol]
        base_asset = str(meta.get("baseAsset", "")).upper()
        if base_asset in excluded:
            continue

        try:
            price = float(ticker["lastPrice"])
            pct_24h = float(ticker["priceChangePercent"])
            quote_volume = float(ticker["quoteVolume"])
            trades = int(ticker["count"])
            high = float(ticker["highPrice"])
            low = float(ticker["lowPrice"])
        except (KeyError, TypeError, ValueError):
            continue

        if price <= 0 or low <= 0:
            continue
        if quote_volume < min_quote_volume or trades < min_trades:
            continue

        high_low_range = (high / low - 1) * 100
        if 0.97 < price < 1.03 and high_low_range < 1:
            continue

        accepted.append(
            RawTicker(
                symbol=symbol,
                base_asset=base_asset,
                price=price,
                pct_24h=pct_24h,
                quote_volume_24h=quote_volume,
                trades_24h=trades,
                high_low_range_24h=high_low_range,
            )
        )

    return accepted

