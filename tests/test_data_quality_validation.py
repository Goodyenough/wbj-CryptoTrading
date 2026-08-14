from __future__ import annotations

from dataclasses import replace
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from crypto_trading_system.config import load_settings
from crypto_trading_system.data_quality import validate_binance_primary_data, validate_kline_series
from crypto_trading_system.data_validation import _provider_failure, _with_data_checks, cross_validate_candidates
from crypto_trading_system.data_validation import CoinGeckoClient
from crypto_trading_system import data_validation as data_validation_module
from crypto_trading_system.models import DataQualityIssue, DataSourceCheck, RawTicker, TradeCandidate
from crypto_trading_system.models import ScanResult
from crypto_trading_system.paper_trader import add_from_scan
from crypto_trading_system.scanner import _apply_data_quality_filter
from crypto_trading_system.storage import init_db, save_scan_result


def _kline(index: int, interval_ms: int, *, volume: float = 100.0, range_pct: float = 1.0) -> list:
    open_time = index * interval_ms
    low = 100.0
    high = low * (1 + range_pct / 100)
    return [
        open_time,
        100.2,
        high,
        low,
        100.5,
        volume,
        open_time + interval_ms - 1,
        100_000.0,
        1000,
        50.0,
        50_000.0,
        0,
    ]


def _candidate() -> TradeCandidate:
    return TradeCandidate(
        rank=1,
        symbol="TESTUSDT",
        base_asset="TEST",
        price=100.5,
        score=80.0,
        setup="test",
        verdict="test",
        entry_low=99.0,
        entry_high=101.0,
        stop_loss=95.0,
        take_profit_1=110.0,
        take_profit_2=120.0,
        risk_reward_1=2.0,
        risk_reward_2=4.0,
        pct_24h=2.0,
        pct_3d=3.0,
        pct_7d=5.0,
        quote_volume_24h=1_000_000.0,
        trades_24h=100_000,
        high_low_range_24h=5.0,
        rsi_1h=55.0,
        rsi_4h=55.0,
        ema20_4h=99.0,
        ema50_4h=98.0,
        ema20_1d=97.0,
        ema50_1d=96.0,
        atr_4h=2.0,
        macd_hist_4h=1.0,
        volume_ratio_24h=1.2,
        support_level=98.0,
        recent_low_4h_18=96.0,
        recent_high_4h_36=105.0,
        distance_to_support_pct=2.5,
        binance_trade_url="https://example.com/binance",
        tradingview_url="https://example.com/tradingview",
        coingecko_search_url="https://example.com/coingecko",
        coinmarketcap_search_url="https://example.com/cmc",
        invalidation="below support",
        action="BUY_CANDIDATE",
    )


def _check(provider: str, issues: list[DataQualityIssue], status: str = "DATA_WARNING") -> DataSourceCheck:
    return DataSourceCheck(
        provider=provider,
        status=status,
        provider_asset_id="test-id" if status == "DATA_OK" else None,
        provider_symbol="TEST",
        price_usd=100.5 if status == "DATA_OK" else None,
        pct_24h=2.0 if status == "DATA_OK" else None,
        volume_24h=1_000_000.0 if status == "DATA_OK" else None,
        last_updated=None,
        fetched_at_utc="2026-08-15T00:00:00Z",
        price_diff_pct=0.0 if status == "DATA_OK" else None,
        pct_24h_diff=0.0 if status == "DATA_OK" else None,
        volume_note="test",
        message="test",
        blocking=any(issue.blocking for issue in issues),
        identity_status="CONFIRMED" if status == "DATA_OK" else "UNCONFIRMED",
        issues=issues,
    )


def test_kline_health_blocks_gap_zero_volume_and_extreme_range() -> None:
    step = 60 * 60_000
    rows = [_kline(0, step), _kline(1, step, volume=0), _kline(3, step, range_pct=45)]
    issues = validate_kline_series("TESTUSDT", "1h", rows, expected_count=3, now_ms=4 * step)
    codes = {issue.code for issue in issues}
    assert "BINANCE_KLINE_GAP" in codes
    assert "BINANCE_KLINE_ZERO_VOLUME" in codes
    assert "BINANCE_KLINE_EXTREME_RANGE" in codes
    assert all(issue.blocking for issue in issues)


def test_primary_health_detects_stale_and_invalid_ticker() -> None:
    ticker = RawTicker("TESTUSDT", "TEST", 0.0, 2.0, -1.0, 100, -1.0)
    step = 60 * 60_000
    rows = [_kline(index, step) for index in range(3)]
    issues = validate_binance_primary_data(
        ticker,
        {"1h": rows, "4h": rows, "1d": rows},
        {"1h": 3, "4h": 3, "1d": 3},
        now_ms=10 * 24 * 60 * 60_000,
    )
    codes = {issue.code for issue in issues}
    assert "BINANCE_TICKER_INVALID" in codes
    assert "BINANCE_KLINE_STALE" in codes


def test_degraded_external_warning_is_allowed_only_in_paper_mode() -> None:
    candidate = _candidate()
    issue = DataQualityIssue(
        provider="CoinMarketCap",
        code="EXTERNAL_IDENTITY_AMBIGUOUS",
        severity="WARNING",
        blocking=False,
        message="multiple symbol matches",
    )
    checked = _with_data_checks(candidate, [_check("Binance", [], "DATA_OK"), _check("CoinMarketCap", [issue])])
    assert checked.data_quality_state == "DEGRADED"
    assert checked.external_identity_status == "UNCONFIRMED"
    settings = load_settings(ROOT / "config" / "settings.toml")
    paper = _apply_data_quality_filter([checked], settings, validation_mode="paper")
    strict = _apply_data_quality_filter([checked], settings, validation_mode="strict")
    assert paper[0].action == "BUY_CANDIDATE"
    assert strict[0].action == "WATCH_ONLY"


def test_blocking_price_warning_cannot_enter_paper() -> None:
    candidate = _candidate()
    issue = DataQualityIssue(
        provider="CoinGecko",
        code="EXTERNAL_PRICE_DIFF_WARNING",
        severity="WARNING",
        blocking=True,
        message="price difference exceeded warning threshold",
    )
    checked = _with_data_checks(candidate, [_check("Binance", [], "DATA_OK"), _check("CoinGecko", [issue])])
    assert checked.data_quality_state == "BLOCKED"
    settings = load_settings(ROOT / "config" / "settings.toml")
    filtered = _apply_data_quality_filter([checked], settings, validation_mode="paper")
    assert filtered[0].action == "WATCH_ONLY"


def test_provider_rate_limit_is_non_blocking() -> None:
    candidate = _candidate()
    check = _provider_failure(
        "CoinGecko",
        candidate,
        "2026-08-15T00:00:00Z",
        "HTTP 429",
        code="EXTERNAL_PROVIDER_RATE_LIMITED",
    )
    assert check.blocking is False
    assert check.issues[0].code == "EXTERNAL_PROVIDER_RATE_LIMITED"


def test_coingecko_mapping_ambiguity_is_structured_and_non_blocking() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    candidate = _candidate()
    original = data_validation_module._get_json

    def fake_get_json(base_url, path, params, headers, timeout_seconds, retries=2, pause_seconds=0.08):
        if path == "/search":
            return {
                "coins": [
                    {"id": "test-one", "symbol": "TEST", "market_cap_rank": 20},
                    {"id": "test-two", "symbol": "TEST", "market_cap_rank": 30},
                ]
            }
        return [{"id": "test-one", "symbol": "test", "current_price": 100.5, "price_change_percentage_24h": 2.0, "total_volume": 1000000}]

    data_validation_module._get_json = fake_get_json
    try:
        check = CoinGeckoClient(settings).market_check(candidate, "2026-08-15T00:00:00Z")
    finally:
        data_validation_module._get_json = original
    assert check.status == "DATA_WARNING"
    assert check.blocking is False
    assert check.identity_status == "UNCONFIRMED"
    assert check.issues[0].code == "EXTERNAL_IDENTITY_AMBIGUOUS"


def test_coingecko_price_warning_remains_blocking() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    candidate = _candidate()
    original = data_validation_module._get_json

    def fake_get_json(base_url, path, params, headers, timeout_seconds, retries=2, pause_seconds=0.08):
        if path == "/search":
            return {"coins": [{"id": "test-one", "symbol": "TEST", "market_cap_rank": 20}]}
        return [{"id": "test-one", "symbol": "test", "current_price": 102.0, "price_change_percentage_24h": 2.0, "total_volume": 1000000}]

    data_validation_module._get_json = fake_get_json
    try:
        check = CoinGeckoClient(settings).market_check(candidate, "2026-08-15T00:00:00Z")
    finally:
        data_validation_module._get_json = original
    assert check.status == "DATA_WARNING"
    assert check.blocking is True
    assert check.issues[0].code == "EXTERNAL_PRICE_DIFF_WARNING"


def test_paper_import_has_blocked_data_quality_defense_in_depth() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    database_path = Path(tempfile.mkdtemp()) / "paper.db"
    settings.output.database_path = database_path
    init_db(database_path)
    candidate = replace(
        _candidate(),
        data_quality_state="BLOCKED",
        data_quality_status="DATA_WARNING",
        data_quality_message="BLOCKED: price diff warning",
    )
    save_scan_result(
        database_path,
        ScanResult(
            scan_id="blocked_scan",
            timestamp_utc="2026-08-15T00:00:00Z",
            source="test",
            filters="test",
            limitations=[],
            candidates=[candidate],
            validation_mode="paper",
        ),
    )
    result = add_from_scan(settings, scan_id="blocked_scan")
    assert result["added"] == 0
    assert result["skipped_data_quality"] == 1


def test_cross_validation_requires_primary_health_input() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    settings.data_validation.enabled = False
    candidate = _candidate()
    checked, _ = cross_validate_candidates(
        settings,
        [candidate],
        primary_issues_by_symbol={candidate.symbol: []},
    )
    assert checked[0].data_quality_state == "DEGRADED"
    checked_without_primary, _ = cross_validate_candidates(settings, [candidate])
    assert checked_without_primary[0].data_quality_state == "BLOCKED"
    assert checked_without_primary[0].data_quality_issues[0].code == "BINANCE_PRIMARY_CHECK_MISSING"
