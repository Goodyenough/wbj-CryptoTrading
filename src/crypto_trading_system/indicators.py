from __future__ import annotations

from collections.abc import Sequence


def percent_change(start: float, end: float) -> float | None:
    if start == 0:
        return None
    return (end / start - 1) * 100


def ema_series(values: Sequence[float], period: int) -> list[float]:
    if len(values) < period:
        return []
    multiplier = 2 / (period + 1)
    current = sum(values[:period]) / period
    output = [current]
    for value in values[period:]:
        current = value * multiplier + current * (1 - multiplier)
        output.append(current)
    return output


def ema(values: Sequence[float], period: int) -> float | None:
    series = ema_series(values, period)
    return series[-1] if series else None


def rsi(values: Sequence[float], period: int = 14) -> float | None:
    if len(values) < period + 1:
        return None
    gains: list[float] = []
    losses: list[float] = []
    for before, after in zip(values[-period - 1 : -1], values[-period:]):
        delta = after - before
        gains.append(max(delta, 0))
        losses.append(max(-delta, 0))

    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period
    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return 100 - 100 / (1 + rs)


def atr(klines: Sequence[Sequence], period: int = 14) -> float | None:
    if len(klines) < period + 1:
        return None
    true_ranges: list[float] = []
    for idx in range(1, len(klines)):
        high = float(klines[idx][2])
        low = float(klines[idx][3])
        previous_close = float(klines[idx - 1][4])
        true_ranges.append(max(high - low, abs(high - previous_close), abs(low - previous_close)))
    return sum(true_ranges[-period:]) / period


def macd(values: Sequence[float]) -> tuple[float | None, float | None, float | None]:
    ema12 = ema_series(values, 12)
    ema26 = ema_series(values, 26)
    if not ema12 or not ema26:
        return None, None, None

    aligned_ema12 = ema12[-len(ema26) :]
    macd_line = [fast - slow for fast, slow in zip(aligned_ema12, ema26)]
    signal_line = ema_series(macd_line, 9)
    if not signal_line:
        return macd_line[-1], None, None
    histogram = macd_line[-1] - signal_line[-1]
    return macd_line[-1], signal_line[-1], histogram

