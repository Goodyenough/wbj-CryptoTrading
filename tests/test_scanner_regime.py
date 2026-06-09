from __future__ import annotations

import math
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from crypto_trading_system.models import RawTicker
from crypto_trading_system.scanner import _analyze_ticker


def _kline(index: int, close: float, interval_ms: int) -> list:
    open_time = index * interval_ms
    return [
        open_time,
        str(close * 0.998),
        str(close * 1.004),
        str(close * 0.992),
        str(close),
        "100",
        open_time + interval_ms - 1,
        "1000000",
        1000,
        "50",
        "500000",
        "0",
    ]


def _trend_series(count: int, interval_ms: int) -> list[list]:
    return [
        _kline(index, 100 + index * 0.08 + math.sin(index / 2) * 2, interval_ms)
        for index in range(count)
    ]


def test_risk_off_core_buy_switch_blocks_btc_candidate() -> None:
    ticker = RawTicker("BTCUSDT", "BTC", 120, 2.0, 100_000_000, 100_000, 5.0)
    k1h = _trend_series(220, 60 * 60_000)
    k4h = _trend_series(140, 4 * 60 * 60_000)
    k1d = _trend_series(220, 24 * 60 * 60_000)

    allowed = _analyze_ticker(
        ticker,
        k1h,
        k4h,
        k1d,
        2.0,
        min_history_days=180,
        market_regime_allows_buy=False,
        market_regime_status="RISK_OFF",
        risk_off_core_buy_enabled=True,
    )
    blocked = _analyze_ticker(
        ticker,
        k1h,
        k4h,
        k1d,
        2.0,
        min_history_days=180,
        market_regime_allows_buy=False,
        market_regime_status="RISK_OFF",
        risk_off_core_buy_enabled=False,
    )

    assert allowed is not None
    assert blocked is not None
    assert allowed.action == "BUY_CANDIDATE"
    assert blocked.action == "WATCH_ONLY"


if __name__ == "__main__":
    test_risk_off_core_buy_switch_blocks_btc_candidate()
    print("test_scanner_regime=passed")
