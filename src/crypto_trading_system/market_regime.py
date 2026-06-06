from __future__ import annotations

from dataclasses import dataclass

from .indicators import ema, percent_change


@dataclass(frozen=True)
class MarketRegime:
    status: str
    allows_alt_buy: bool
    btc_trend_ok: bool
    eth_trend_ok: bool
    btc_pct_7d: float | None
    eth_pct_7d: float | None
    summary: str


def _closes(klines: list[list]) -> list[float]:
    return [float(kline[4]) for kline in klines]


def _trend_ok(closes: list[float]) -> bool:
    ema20 = ema(closes, 20)
    ema50 = ema(closes, 50)
    if ema20 is None or ema50 is None:
        return False
    return closes[-1] > ema20 > ema50


def classify_market_regime(btc_1d: list[list], eth_1d: list[list]) -> MarketRegime:
    if len(btc_1d) < 60 or len(eth_1d) < 60:
        return MarketRegime(
            status="UNKNOWN",
            allows_alt_buy=False,
            btc_trend_ok=False,
            eth_trend_ok=False,
            btc_pct_7d=None,
            eth_pct_7d=None,
            summary="BTC/ETH 日线历史不足，默认不放开山寨币买入。",
        )

    btc_closes = _closes(btc_1d)
    eth_closes = _closes(eth_1d)
    btc_pct_7d = percent_change(btc_closes[-8], btc_closes[-1])
    eth_pct_7d = percent_change(eth_closes[-8], eth_closes[-1])
    btc_trend_ok = _trend_ok(btc_closes)
    eth_trend_ok = _trend_ok(eth_closes)
    btc_not_breaking = btc_pct_7d is None or btc_pct_7d >= -5
    eth_not_breaking = eth_pct_7d is None or eth_pct_7d >= -8

    if btc_trend_ok and eth_trend_ok and btc_not_breaking and eth_not_breaking:
        return MarketRegime(
            status="RISK_ON",
            allows_alt_buy=True,
            btc_trend_ok=btc_trend_ok,
            eth_trend_ok=eth_trend_ok,
            btc_pct_7d=btc_pct_7d,
            eth_pct_7d=eth_pct_7d,
            summary="BTC/ETH 日线趋势均较强，允许山寨币买入候选。",
        )

    if not btc_not_breaking or not eth_not_breaking or (not btc_trend_ok and not eth_trend_ok):
        status = "RISK_OFF"
        summary = "BTC/ETH 大盘偏弱，山寨币买入候选降级为观察。"
    else:
        status = "NEUTRAL"
        summary = "BTC/ETH 大盘未完全确认强势，山寨币买入候选降级为观察。"
    return MarketRegime(
        status=status,
        allows_alt_buy=False,
        btc_trend_ok=btc_trend_ok,
        eth_trend_ok=eth_trend_ok,
        btc_pct_7d=btc_pct_7d,
        eth_pct_7d=eth_pct_7d,
        summary=summary,
    )
