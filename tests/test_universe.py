from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from crypto_trading_system.backtest import universe as universe_module
from crypto_trading_system.backtest.universe import (
    build_current_symbol_master,
    dynamic_universe_refresh_key,
    listing_date_allows_analysis,
    load_symbol_master,
    save_symbol_master,
    select_dynamic_universe_for_day,
    SymbolMaster,
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


def test_symbol_master_json_round_trip(tmp_path: Path) -> None:
    path = tmp_path / "master.json"
    master = SymbolMaster(
        source="test",
        created_at_utc="2026-01-01T00:00:00+00:00",
        symbols=["btcusdt", "ETH/USDT"],
        source_limit=2,
        source_limit_applied=True,
        filters="unit-test",
    )

    save_symbol_master(master, path)
    loaded = load_symbol_master(path)

    assert loaded.source == "test"
    assert loaded.symbols == ["BTCUSDT", "ETHUSDT"]
    assert loaded.source_limit == 2
    assert loaded.source_limit_applied is True
    assert loaded.filters == "unit-test"


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


def test_symbol_master_listing_dates_round_trip(tmp_path: Path) -> None:
    path = tmp_path / "master_with_listing.json"
    master = SymbolMaster(
        source="test",
        created_at_utc="2026-01-01T00:00:00+00:00",
        symbols=["BTCUSDT", "ETHUSDT"],
        source_limit=None,
        source_limit_applied=False,
        filters="unit-test",
        listing_dates={"BTCUSDT": "2017-08-17", "ETHUSDT": "2017-08-17"},
    )
    save_symbol_master(master, path)
    loaded = load_symbol_master(path)
    assert loaded.listing_dates == {"BTCUSDT": "2017-08-17", "ETHUSDT": "2017-08-17"}


def test_symbol_master_listing_dates_none_for_old_file(tmp_path: Path) -> None:
    # Old master files don't have listing_dates; load_symbol_master should return None
    path = tmp_path / "old_master.json"
    master = SymbolMaster(
        source="test",
        created_at_utc="2026-01-01T00:00:00+00:00",
        symbols=["BTCUSDT"],
        source_limit=None,
        source_limit_applied=False,
        filters="unit-test",
        listing_dates=None,
    )
    save_symbol_master(master, path)
    # Patch out listing_dates from JSON to simulate old file format
    import json as _json
    data = _json.loads(path.read_text(encoding="utf-8"))
    data.pop("listing_dates", None)
    path.write_text(_json.dumps(data, indent=2) + "\n", encoding="utf-8")
    loaded = load_symbol_master(path)
    assert loaded.listing_dates is None


def test_listing_date_allows_analysis_no_dates() -> None:
    # Without listing_dates, always allow
    assert listing_date_allows_analysis(None, "ANYUSDT", 10**13, 180) is True
    assert listing_date_allows_analysis({}, "ANYUSDT", 10**13, 180) is True


def test_listing_date_allows_analysis_rejects_too_soon() -> None:
    # Symbol listed 2025-03-01; min_history_days=180; bar at 2025-05-01 (~61 days) -> reject
    from datetime import datetime, timezone
    listing = {"NEWUSDT": "2025-03-01"}
    day_ms = 86_400_000
    listing_ms = int(datetime.fromisoformat("2025-03-01T00:00:00+00:00").timestamp() * 1000)
    bar_too_soon = listing_ms + 61 * day_ms
    assert listing_date_allows_analysis(listing, "NEWUSDT", bar_too_soon, 180) is False


def test_listing_date_allows_analysis_accepts_after_history() -> None:
    # Symbol listed 2025-03-01; bar at 2025-10-01 (~214 days) -> allow
    from datetime import datetime, timezone
    listing = {"NEWUSDT": "2025-03-01"}
    day_ms = 86_400_000
    listing_ms = int(datetime.fromisoformat("2025-03-01T00:00:00+00:00").timestamp() * 1000)
    bar_ok = listing_ms + 214 * day_ms
    assert listing_date_allows_analysis(listing, "NEWUSDT", bar_ok, 180) is True


def test_listing_date_allows_analysis_unknown_symbol_passes() -> None:
    # Symbol not in listing_dates dict -> always allow
    assert listing_date_allows_analysis({"BTCUSDT": "2017-08-17"}, "NEWUSDT", 10**13, 180) is True


if __name__ == "__main__":
    test_fetch_universe_snapshot_filters_and_sorts()
    test_build_current_symbol_master_source_limit_is_alphabetical()
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        test_symbol_master_json_round_trip(Path(tmp))
        test_symbol_master_listing_dates_round_trip(Path(tmp))
        test_symbol_master_listing_dates_none_for_old_file(Path(tmp))
    test_universe_preselection_score_is_not_technical_score()
    test_dynamic_universe_ignores_future_hourly_data()
    test_dynamic_universe_filters_insufficient_history_without_crashing()
    test_dynamic_universe_refresh_key_is_daily()
    test_listing_date_allows_analysis_no_dates()
    test_listing_date_allows_analysis_rejects_too_soon()
    test_listing_date_allows_analysis_accepts_after_history()
    test_listing_date_allows_analysis_unknown_symbol_passes()
    print("test_universe=passed")
