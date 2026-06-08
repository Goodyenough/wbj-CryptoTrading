from __future__ import annotations

from pathlib import Path
import sqlite3
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from crypto_trading_system.backtest import history as history_module
from crypto_trading_system.backtest.history import fetch_klines_cached
from crypto_trading_system.config import load_settings


class EmptyKlineClient:
    calls = 0

    def __init__(self, *args, **kwargs) -> None:
        pass

    def klines(self, *args, **kwargs) -> list:
        EmptyKlineClient.calls += 1
        return []


def _settings_with_temp_db(tmp_path: Path):
    settings = load_settings(ROOT / "config" / "settings.toml")
    settings.output.database_path = tmp_path / "test_crypto_trading.db"
    settings.market.request_pause_seconds = 0
    return settings


def test_empty_binance_response_is_cached_as_unavailable_range() -> None:
    original_client = history_module.BinanceClient
    history_module.BinanceClient = EmptyKlineClient
    EmptyKlineClient.calls = 0
    try:
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
            settings = _settings_with_temp_db(Path(tmp))
            first = fetch_klines_cached(
                settings,
                "NEWUSDT",
                "4h",
                0,
                4 * 60 * 60_000,
                allow_data_gaps=True,
            )
            second = fetch_klines_cached(
                settings,
                "NEWUSDT",
                "4h",
                0,
                4 * 60 * 60_000,
                allow_data_gaps=True,
            )

            with sqlite3.connect(settings.output.database_path) as connection:
                rows = connection.execute("SELECT symbol, interval, reason FROM kline_unavailable_ranges").fetchall()
    finally:
        history_module.BinanceClient = original_client

    assert EmptyKlineClient.calls == 1
    assert first.klines == []
    assert second.klines == []
    assert first.fetched_from_api == 0
    assert second.fetched_from_api == 0
    assert rows == [("NEWUSDT", "4h", "binance_empty_response")]


def test_cached_unavailable_range_still_raises_when_data_gaps_disallowed() -> None:
    original_client = history_module.BinanceClient
    history_module.BinanceClient = EmptyKlineClient
    EmptyKlineClient.calls = 0
    try:
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
            settings = _settings_with_temp_db(Path(tmp))
            fetch_klines_cached(
                settings,
                "NEWUSDT",
                "4h",
                0,
                4 * 60 * 60_000,
                allow_data_gaps=True,
            )
            try:
                fetch_klines_cached(
                    settings,
                    "NEWUSDT",
                    "4h",
                    0,
                    4 * 60 * 60_000,
                    allow_data_gaps=False,
                )
            except ValueError as exc:
                assert "No klines available" in str(exc)
            else:
                raise AssertionError("Expected cached no-data marker to preserve strict data gap behavior")
    finally:
        history_module.BinanceClient = original_client

    assert EmptyKlineClient.calls == 1


if __name__ == "__main__":
    test_empty_binance_response_is_cached_as_unavailable_range()
    test_cached_unavailable_range_still_raises_when_data_gaps_disallowed()
    print("test_history=passed")
