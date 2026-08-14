from __future__ import annotations

from collections.abc import Iterable
from datetime import datetime, timezone
import math

from .models import DataQualityIssue, RawTicker


EXCLUDED_SUFFIXES = ("UPUSDT", "DOWNUSDT", "BULLUSDT", "BEARUSDT")

KLINE_INTERVAL_MS = {
    "1h": 60 * 60_000,
    "4h": 4 * 60 * 60_000,
    "1d": 24 * 60 * 60_000,
}


def _issue(
    code: str,
    message: str,
    *,
    provider: str = "Binance",
    severity: str = "ERROR",
    blocking: bool = True,
    context: dict[str, str | int | float] | None = None,
) -> DataQualityIssue:
    return DataQualityIssue(
        provider=provider,
        code=code,
        severity=severity,
        blocking=blocking,
        message=message,
        context=context or {},
    )


def _now_ms() -> int:
    return int(datetime.now(timezone.utc).timestamp() * 1000)


def validate_kline_series(
    symbol: str,
    interval: str,
    klines: list[list],
    expected_count: int,
    *,
    now_ms: int | None = None,
    extreme_range_pct: float = 40.0,
) -> list[DataQualityIssue]:
    """Validate the K-line series used by scanner signals.

    Scanner data is fail-closed: missing, stale, malformed, discontinuous, or
    anomalous candles are blocking because they can change indicators and the
    resulting trade plan.
    """
    step = KLINE_INTERVAL_MS.get(interval)
    if step is None:
        return [_issue("BINANCE_UNSUPPORTED_INTERVAL", f"Unsupported Binance interval: {interval}.")]

    issues: list[DataQualityIssue] = []
    if not klines:
        return [
            _issue(
                "BINANCE_KLINE_EMPTY",
                f"No Binance {interval} klines available for {symbol}.",
                context={"symbol": symbol, "interval": interval},
            )
        ]
    if len(klines) < expected_count:
        issues.append(
            _issue(
                "BINANCE_KLINE_INSUFFICIENT",
                f"Binance {interval} returned {len(klines)} candles; expected at least {expected_count}.",
                context={"symbol": symbol, "interval": interval, "actual_count": len(klines), "expected_count": expected_count},
            )
        )

    seen: set[int] = set()
    previous_open: int | None = None
    last_close_time: int | None = None
    for row_index, kline in enumerate(klines):
        context = {"symbol": symbol, "interval": interval, "row_index": row_index}
        if not isinstance(kline, (list, tuple)) or len(kline) < 9:
            issues.append(
                _issue("BINANCE_KLINE_MALFORMED", "Binance K-line row has too few fields.", context=context)
            )
            continue
        try:
            open_time = int(kline[0])
            opened = float(kline[1])
            high = float(kline[2])
            low = float(kline[3])
            close = float(kline[4])
            volume = float(kline[5])
            close_time = int(kline[6])
        except (TypeError, ValueError, OverflowError):
            issues.append(_issue("BINANCE_KLINE_MALFORMED", "Binance K-line contains non-numeric fields.", context=context))
            continue

        context.update({"open_time": open_time})
        if open_time in seen:
            issues.append(_issue("BINANCE_KLINE_DUPLICATE", "Duplicate Binance candle.", context=context))
        seen.add(open_time)
        if previous_open is not None and open_time - previous_open != step:
            issues.append(
                _issue(
                    "BINANCE_KLINE_GAP",
                    f"Binance {interval} candle gap detected between {previous_open} and {open_time}.",
                    context=context,
                )
            )

        values = (opened, high, low, close, volume)
        if not all(math.isfinite(value) for value in values) or high <= 0 or low <= 0 or opened <= 0 or close <= 0:
            issues.append(_issue("BINANCE_KLINE_INVALID_OHLCV", "Binance K-line contains invalid OHLCV values.", context=context))
        elif high < max(opened, close) or low > min(opened, close) or high < low or volume < 0:
            issues.append(_issue("BINANCE_KLINE_INVALID_OHLCV", "Binance K-line OHLCV relationship is invalid.", context=context))
        elif volume == 0:
            issues.append(_issue("BINANCE_KLINE_ZERO_VOLUME", "Zero-volume Binance candle in the signal window.", context=context))
        elif (high / low - 1) * 100 > extreme_range_pct:
            issues.append(
                _issue(
                    "BINANCE_KLINE_EXTREME_RANGE",
                    f"Binance candle range exceeds {extreme_range_pct:.0f}%.",
                    context={**context, "range_pct": (high / low - 1) * 100},
                )
            )
        previous_open = open_time
        last_close_time = close_time

    current_ms = _now_ms() if now_ms is None else now_ms
    if last_close_time is not None and last_close_time < current_ms - 2 * step:
        issues.append(
            _issue(
                "BINANCE_KLINE_STALE",
                f"Latest Binance {interval} candle is stale.",
                context={"symbol": symbol, "interval": interval, "last_close_time": last_close_time, "now_ms": current_ms},
            )
        )
    return issues


def validate_binance_primary_data(
    ticker: RawTicker,
    kline_series: dict[str, list[list]],
    expected_counts: dict[str, int],
    *,
    now_ms: int | None = None,
) -> list[DataQualityIssue]:
    """Validate the Binance ticker and all K-lines used for one candidate."""
    issues: list[DataQualityIssue] = []
    ticker_values = (ticker.price, ticker.pct_24h, ticker.quote_volume_24h, ticker.high_low_range_24h)
    if not all(math.isfinite(value) for value in ticker_values):
        issues.append(_issue("BINANCE_TICKER_NONFINITE", "Binance ticker contains a non-finite value.", context={"symbol": ticker.symbol}))
    if ticker.price <= 0 or ticker.quote_volume_24h < 0 or ticker.trades_24h < 0:
        issues.append(_issue("BINANCE_TICKER_INVALID", "Binance ticker contains invalid price, volume, or trade count.", context={"symbol": ticker.symbol}))
    if ticker.high_low_range_24h < 0:
        issues.append(_issue("BINANCE_TICKER_INVALID", "Binance ticker high/low range is negative.", context={"symbol": ticker.symbol}))

    for interval, expected_count in expected_counts.items():
        issues.extend(
            validate_kline_series(
                ticker.symbol,
                interval,
                kline_series.get(interval, []),
                expected_count,
                now_ms=now_ms,
            )
        )
    return issues


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
