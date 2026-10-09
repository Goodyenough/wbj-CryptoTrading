from __future__ import annotations

import math
from pathlib import Path
import sys
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from crypto_trading_system.models import RawTicker
from crypto_trading_system.scanner import _analyze_ticker, _detect_market_regime, _fetch_closed_klines
from crypto_trading_system.config import load_settings


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


@pytest.mark.parametrize("symbol", ["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "TESTUSDT"])
def test_unknown_blocks_even_exempt_symbols_through_real_detector(symbol):
    class FailingClient:
        def klines(self, *args, **kwargs):
            raise RuntimeError("regime data unavailable")
    settings = load_settings(ROOT / "config/settings.toml")
    regime = _detect_market_regime(FailingClient(), settings, [], None)
    assert regime.status == "UNKNOWN" and not regime.allows_alt_buy
    ticker = RawTicker(symbol, symbol[:-4], 120, 2.0, 100_000_000, 100_000, 5.0)
    args = (ticker, _trend_series(220, 3600000), _trend_series(140, 14400000), _trend_series(220, 86400000), 2.0)
    allowed = _analyze_ticker(*args, min_history_days=180)
    assert allowed.action == "BUY_CANDIDATE"  # otherwise the blocking assertion is vacuous
    blocked = _analyze_ticker(*args, min_history_days=180, market_regime_status=regime.status,
                              market_regime_allows_buy=regime.allows_alt_buy,
                              risk_off_core_buy_enabled=True, risk_off_large_cap_buy_enabled=True)
    assert blocked.action == "WATCH_ONLY"
    assert any("UNKNOWN" in risk for risk in blocked.risks)


@pytest.mark.parametrize("status,allows,expected", [
    ("UNKNOWN", True, "WATCH_ONLY"),  # inconsistent caller metadata must not reopen unknown
    ("NEUTRAL", False, "BUY_CANDIDATE"),  # freeze existing strategy choice
    ("RISK_ON", True, "BUY_CANDIDATE"),
    (None, True, "BUY_CANDIDATE"),  # disabled filter contract
])
def test_regime_fix_preserves_neutral_and_disabled_behavior(status, allows, expected):
    ticker = RawTicker("TESTUSDT", "TEST", 120, 2.0, 100_000_000, 100_000, 5.0)
    candidate = _analyze_ticker(ticker, _trend_series(220, 3600000), _trend_series(140, 14400000),
                                _trend_series(220, 86400000), 2.0, min_history_days=180,
                                market_regime_status=status, market_regime_allows_buy=allows)
    assert candidate.action == expected


def test_fetch_closed_klines_uses_buffered_closed_rows_only():
    class Client:
        def klines(self, symbol, interval, limit):
            assert (symbol, interval, limit) == ("TESTUSDT", "1h", 5)
            return [_kline(index, 100 + index, 3_600_000) for index in range(5)]

    # The newest row is still inside the publication buffer; retain the latest
    # three eligible rows and preserve the requested count.
    as_of_ms = 4 * 3_600_000 + 60_000 + 30_000
    rows = _fetch_closed_klines(Client(), "TESTUSDT", "1h", 3, as_of_ms)
    assert [float(row[4]) for row in rows] == [101.0, 102.0, 103.0]


if __name__ == "__main__":
    test_risk_off_core_buy_switch_blocks_btc_candidate()
    print("test_scanner_regime=passed")
