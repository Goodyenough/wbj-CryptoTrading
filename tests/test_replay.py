from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from crypto_trading_system.backtest.history import interval_ms
from crypto_trading_system.backtest.history import KlineFetchResult
from crypto_trading_system.backtest import replay as replay_module
from crypto_trading_system.backtest.replay import _closed_slice, _effective_warmup_ms, _entry_reclaim_close_satisfied
from crypto_trading_system.backtest.universe import SymbolMaster
from crypto_trading_system.config import load_settings
from crypto_trading_system.ticker_utils import reconstruct_ticker


def make_kline(open_time: int, close: float, interval_ms: int = 60 * 60_000) -> list:
    return [
        open_time,
        str(close - 1),
        str(close + 1),
        str(close - 2),
        str(close),
        "100",
        open_time + interval_ms - 1,
        "1000",
        10,
        "50",
        "500",
        "0",
    ]


def test_reconstruct_ticker_ignores_future_data() -> None:
    klines = [make_kline(index * 60 * 60_000, 100 + index) for index in range(30)]
    baseline = reconstruct_ticker("TESTUSDT", "TEST", klines, as_of_index=24)
    klines_with_future = klines + [make_kline(30 * 60 * 60_000, 10_000)]
    repeated = reconstruct_ticker("TESTUSDT", "TEST", klines_with_future, as_of_index=24)
    assert baseline.price == repeated.price
    assert baseline.pct_24h == repeated.pct_24h
    assert baseline.quote_volume_24h == repeated.quote_volume_24h


def test_closed_slice_excludes_unclosed_daily_bar() -> None:
    day = 24 * 60 * 60_000
    klines = [make_kline(0, 100, day), make_kline(day, 110, day)]
    decision_time = day + 12 * 60 * 60_000
    closed = _closed_slice(klines, "1d", decision_time)
    assert len(closed) == 1
    assert int(closed[0][0]) == 0


def test_closed_slice_includes_signal_bar_only_after_close() -> None:
    four_h = 4 * 60 * 60_000
    klines = [make_kline(0, 100, four_h), make_kline(four_h, 105, four_h)]
    assert len(_closed_slice(klines, "4h", four_h - 1)) == 0
    assert len(_closed_slice(klines, "4h", four_h)) == 1


def test_effective_warmup_covers_min_history_plus_margin() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    minimum = (settings.analysis.min_history_days + 60) * interval_ms("1d")
    assert _effective_warmup_ms(settings) >= minimum


def test_entry_reclaim_close_requires_close_above_entry_high() -> None:
    assert _entry_reclaim_close_satisfied(False, close=99.0, entry_high=100.0) is True
    assert _entry_reclaim_close_satisfied(True, close=99.0, entry_high=100.0) is False
    assert _entry_reclaim_close_satisfied(True, close=100.0, entry_high=100.0) is True


def test_dynamic_universe_requires_btc_timeline() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    master = SymbolMaster(
        source="test",
        created_at_utc="2026-01-01T00:00:00+00:00",
        symbols=["AAAUSDT"],
        source_limit=None,
        source_limit_applied=False,
        filters="test",
    )

    def fake_fetch(settings, symbol, interval, start_time_ms, end_time_ms, **kwargs):
        return KlineFetchResult(symbol=symbol, interval=interval, klines=[], issues=[], fetched_from_api=0)

    original_fetch = replay_module.fetch_klines_cached
    replay_module.fetch_klines_cached = fake_fetch
    try:
        try:
            replay_module.run_backtest_replay(
                settings,
                [],
                "2025-01-01",
                "2025-01-02",
                dynamic_universe_mode=True,
                dynamic_symbol_master=master,
            )
        except ValueError as exc:
            assert "requires BTCUSDT 4h klines" in str(exc)
        else:
            raise AssertionError("Expected missing BTCUSDT timeline to raise ValueError")
    finally:
        replay_module.fetch_klines_cached = original_fetch


if __name__ == "__main__":
    test_reconstruct_ticker_ignores_future_data()
    test_closed_slice_excludes_unclosed_daily_bar()
    test_closed_slice_includes_signal_bar_only_after_close()
    test_effective_warmup_covers_min_history_plus_margin()
    test_entry_reclaim_close_requires_close_above_entry_high()
    test_dynamic_universe_requires_btc_timeline()
    print("test_replay=passed")
