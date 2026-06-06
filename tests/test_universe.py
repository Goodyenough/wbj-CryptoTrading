from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from crypto_trading_system.backtest import universe as universe_module
from crypto_trading_system.backtest.universe import (
    build_current_symbol_master,
    dynamic_universe_refresh_key,
    select_dynamic_universe_for_day,
    universe_preselection_score,
)
from crypto_trading_system.config import load_settings
from crypto_trading_system.models import RawTicker


class FakeBinanceClient:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def exchange_info(self) -> dict:
        return {
            "symbols": [
                _symbol("BTCUSDT", "BTC"),
                _symbol("ETHUSDT", "ETH"),
                _symbol("LOWUSDT", "LOW"),
                _symbol("USDCUSDT", "USDC"),
                _symbol("BADUSDT", "BAD", status="BREAK"),
            ]
        }

    def ticker_24hr(self) -> list[dict]:
        return [
            _ticker("BTCUSDT", 100.0, 1.0, 100_000_000, 100_000, 110.0, 90.0),
            _ticker("ETHUSDT", 10.0, 0.0, 90_000_000, 90_000, 11.0, 9.0),
            _ticker("LOWUSDT", 1.0, 10.0, 1_000, 10, 1.1, 1.0),
            _ticker("USDCUSDT", 1.0, 0.1, 200_000_000, 200_000, 1.001, 0.999),
            _ticker("BADUSDT", 1.0, 100.0, 200_000_000, 200_000, 2.0, 1.0),
        ]


def _symbol(symbol: str, base_asset: str, status: str = "TRADING") -> dict:
    return {
        "symbol": symbol,
        "status": status,
        "baseAsset": base_asset,
        "quoteAsset": "USDT",
        "isSpotTradingAllowed": True,
    }


def _ticker(
    symbol: str,
    price: float,
    pct_24h: float,
    quote_volume: float,
    trades: int,
    high: float,
    low: float,
) -> dict:
    return {
        "symbol": symbol,
        "lastPrice": str(price),
        "priceChangePercent": str(pct_24h),
        "quoteVolume": str(quote_volume),
        "count": str(trades),
        "highPrice": str(high),
        "lowPrice": str(low),
    }


def _kline(open_time: int, close: float, quote_volume: float, trades: int, interval_ms: int = 60 * 60_000) -> list:
    return [
        open_time,
        str(close - 1),
        str(close + 1),
        str(close - 2),
        str(close),
        "100",
        open_time + interval_ms - 1,
        str(quote_volume),
        trades,
        "50",
        str(quote_volume / 2),
        "0",
    ]


def _hourly(close_start: float, count: int, quote_volume: float, trades: int) -> list[list]:
    hour = 60 * 60_000
    return [_kline(index * hour, close_start + index, quote_volume, trades) for index in range(count)]


def test_fetch_universe_snapshot_filters_and_sorts() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    original = universe_module.BinanceClient
    universe_module.BinanceClient = FakeBinanceClient
    try:
        snapshot = universe_module.fetch_universe_snapshot(settings, max_symbols=2)
    finally:
        universe_module.BinanceClient = original

    assert snapshot.mode == "universe_snapshot"
    assert snapshot.candidate_count == 2
    assert snapshot.selected_count == 2
    assert snapshot.selected_symbols == ["BTCUSDT", "ETHUSDT"]
    assert "24h quote volume" in snapshot.filters


def test_build_current_symbol_master_source_limit_is_alphabetical() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    original = universe_module.BinanceClient
    universe_module.BinanceClient = FakeBinanceClient
    try:
        master = build_current_symbol_master(settings, source_limit=2)
    finally:
        universe_module.BinanceClient = original

    assert master.symbols == ["BTCUSDT", "ETHUSDT"]
    assert master.source_limit_applied is True


def test_universe_preselection_score_is_not_technical_score() -> None:
    liquid = RawTicker("AAAUSDT", "AAA", 10, 0, 100_000_000, 100_000, 10)
    pumpy = RawTicker("BBBUSDT", "BBB", 10, 1, 10_000_000, 100_000, 10)
    assert universe_preselection_score(liquid) > universe_preselection_score(pumpy)


def test_dynamic_universe_ignores_future_hourly_data() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    hour = 60 * 60_000
    klines_by_symbol = {
        "NOWUSDT": {"1h": _hourly(100, 31, 2_000_000, 2_000), "4h": [], "1d": []},
        "FUTUSDT": {
            "1h": _hourly(100, 31, 1_000, 10) + [_kline(31 * hour, 1_000, 100_000_000, 100_000)],
            "4h": [],
            "1d": [],
        },
    }
    selection = select_dynamic_universe_for_day(
        settings,
        ["NOWUSDT", "FUTUSDT"],
        klines_by_symbol,
        31 * hour,
        max_symbols=5,
    )

    assert selection.selected_symbols == ["NOWUSDT"]
    assert selection.filter_counts["low_quote_volume"] == 1


def test_dynamic_universe_filters_insufficient_history_without_crashing() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    hour = 60 * 60_000
    klines_by_symbol = {
        "NEWUSDT": {"1h": _hourly(100, 10, 100_000_000, 100_000), "4h": [], "1d": []},
    }
    selection = select_dynamic_universe_for_day(
        settings,
        ["NEWUSDT"],
        klines_by_symbol,
        31 * hour,
        max_symbols=5,
    )

    assert selection.selected_symbols == []
    assert selection.filter_counts["insufficient_24h"] == 1


def test_dynamic_universe_refresh_key_is_daily() -> None:
    hour = 60 * 60_000
    assert dynamic_universe_refresh_key(4 * hour) == dynamic_universe_refresh_key(20 * hour)
    assert dynamic_universe_refresh_key(4 * hour) != dynamic_universe_refresh_key(28 * hour)


if __name__ == "__main__":
    test_fetch_universe_snapshot_filters_and_sorts()
    test_build_current_symbol_master_source_limit_is_alphabetical()
    test_universe_preselection_score_is_not_technical_score()
    test_dynamic_universe_ignores_future_hourly_data()
    test_dynamic_universe_filters_insufficient_history_without_crashing()
    test_dynamic_universe_refresh_key_is_daily()
    print("test_universe=passed")
