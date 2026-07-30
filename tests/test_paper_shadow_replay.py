from __future__ import annotations

from pathlib import Path
from datetime import datetime, timezone
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from crypto_trading_system import paper_shadow_replay as shadow_module
from crypto_trading_system.config import load_settings
from crypto_trading_system.database import connect_db
from crypto_trading_system.paper_shadow_replay import (
    build_entry_reclaim_confirm_1bar_shadow,
    build_relative_strength_gate_shadow,
    render_shadow_replay_report,
)
from crypto_trading_system.paper_audit import OpportunityRow
from crypto_trading_system.paper_shadow_experiments import (
    ExperimentDecisionRow,
    OpportunitySet,
    _outcome_from_opportunity,
    render_shadow_experiment_report,
    run_atr_reclaim_incumbent_shadow,
)
from crypto_trading_system.storage import init_db


class _FakeFetchResult:
    def __init__(self, klines: list[list]) -> None:
        self.symbol = "TESTUSDT"
        self.interval = "4h"
        self.klines = klines
        self.issues = []
        self.fetched_from_api = 0


def _settings(root: Path):
    settings = load_settings(Path("config/settings.toml"))
    settings.output.database_path = root / "paper.db"
    settings.output.reports_dir = root / "reports"
    settings.output.obsidian_dir = None
    return settings


def _seed_reclaim_plan(path: Path) -> None:
    init_db(path)
    with connect_db(path) as connection:
        connection.execute(
            """
            INSERT INTO runs(run_id, run_type, started_at, finished_at, status, created_at)
            VALUES ('run1', 'manual', '2026-06-19T00:00:00Z', '2026-06-19T00:01:00Z', 'success', '2026-06-19T00:00:00Z')
            """
        )
        connection.execute(
            """
            INSERT INTO paper_plans(
                plan_id, account_name, source_scan_id, source_symbol, created_run_id,
                created_at, symbol, entry_low, entry_high, stop_initial, stop_current,
                tp1, tp2, status, created_reason, market_regime, raw_json, updated_at
            ) VALUES ('plan1', 'demo', NULL, 'TESTUSDT', 'run1', '2026-06-19T00:00:00Z',
                      'TESTUSDT', 100, 105, 90, 90, 125, 140, 'WATCHING', 'test setup',
                      'RISK_OFF', '{}', '2026-06-19T00:00:00Z')
            """
        )
        connection.execute(
            """
            INSERT INTO paper_events(event_id, plan_id, run_id, event_time, event_type, symbol, price, reason, created_at)
            VALUES ('e1', 'plan1', 'run1', '2026-06-19T00:00:00Z', 'RECLAIM_PENDING_SET', 'TESTUSDT', 100, 'blocked', '2026-06-19T00:00:00Z')
            """
        )


def _kline(index: int, open_: float, high: float, low: float, close: float) -> list:
    open_time = int(datetime(2026, 6, 19, 0, 0, tzinfo=timezone.utc).timestamp() * 1000) + index * 14_400_000
    return [open_time, open_, high, low, close, 1.0, open_time + 14_399_999, 1.0, 1, 1.0, 1.0, 0]


def test_entry_reclaim_confirm_1bar_filters_stop_first_path() -> None:
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        settings = _settings(Path(tmp))
        _seed_reclaim_plan(settings.output.database_path)
        original = shadow_module.fetch_klines_cached
        shadow_module.fetch_klines_cached = lambda *args, **kwargs: _FakeFetchResult(
            [
                _kline(0, 100, 106, 99, 106),
                _kline(1, 106, 107, 89, 100),
            ]
        )
        try:
            rows = build_entry_reclaim_confirm_1bar_shadow(settings, "demo", "2026-06-19", "2026-07-02")
        finally:
            shadow_module.fetch_klines_cached = original
    assert len(rows) == 1
    assert rows[0].baseline_first_hit == "stop_first"
    assert rows[0].variant_first_hit == "no_variant_entry"
    assert rows[0].decision == "filtered_loser"


def test_shadow_replay_report_contains_summary_sections() -> None:
    text = render_shadow_replay_report(
        account="demo",
        start_date="2026-06-19",
        end_date="2026-07-02",
        variant="entry_reclaim_confirm_1bar",
        report_version=1,
        rows=[],
    )
    assert "## Summary" in text
    assert "## Decision Counts" in text
    assert "## Replay Details" in text


def test_relative_strength_gate_filters_weak_stop_first_path() -> None:
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        settings = _settings(Path(tmp))
        _seed_reclaim_plan(settings.output.database_path)
        original = shadow_module.fetch_klines_cached

        def fake_fetch(_settings, symbol, *_args, **_kwargs):
            if symbol == "TESTUSDT":
                return _FakeFetchResult(
                    [
                        _kline(0, 100, 106, 99, 106),
                        _kline(1, 106, 107, 89, 100),
                    ]
                )
            return _FakeFetchResult(
                [
                    _kline(0, 100, 101, 99, 100),
                    _kline(1, 100, 103, 99, 102),
                ]
            )

        shadow_module.fetch_klines_cached = fake_fetch
        try:
            rows = build_relative_strength_gate_shadow(settings, "demo", "2026-06-19", "2026-07-02")
        finally:
            shadow_module.fetch_klines_cached = original
    assert len(rows) == 1
    assert rows[0].baseline_first_hit == "stop_first"
    assert rows[0].variant_first_hit == "no_variant_entry"
    assert rows[0].decision == "filtered_loser"
    assert rows[0].relative_strength_pct is not None
    assert rows[0].relative_strength_pct < 0


def test_shadow_experiment_report_uses_fixed_set_and_negative_missed_winner_r() -> None:
    opportunity = OpportunityRow(
        source="WATCH_ONLY",
        symbol="TESTUSDT",
        plan_id="scan1:TESTUSDT",
        first_time="2026-07-03T12:00:00Z",
        reason="test",
        entry=100.0,
        entry_low=98.0,
        stop=90.0,
        tp1=120.0,
        max_price_after=119.0,
        min_price_after=95.0,
        reclaimed=True,
        hit_tp1=False,
        hit_stop=False,
        classification="missed_winner",
        explanation="test",
        maturity_status="mature",
        classification_final=True,
        mfe_r=1.9,
        counterfactual_pnl_r=1.9,
        first_hit="near_tp1_first",
        opportunity_set_key="WATCH_ONLY:scan1:TESTUSDT",
    )
    outcome, pnl_r = _outcome_from_opportunity(opportunity, accepted=False)
    assert outcome == "missed_winner"
    assert pnl_r == -1.9
    text = render_shadow_experiment_report(
        account="demo",
        start_date="2026-07-03",
        end_date="2026-07-25",
        experiment="relative_strength_soft_gate",
        report_version=1,
        opportunity_set=OpportunitySet("demo", "2026-07-03", "2026-07-25", [opportunity], "abc123"),
        rows=[
            ExperimentDecisionRow(
                experiment="relative_strength_soft_gate",
                variant="test_variant",
                symbol="TESTUSDT",
                opportunity_key="WATCH_ONLY:scan1:TESTUSDT",
                source="WATCH_ONLY",
                first_time="2026-07-03T12:00:00Z",
                market_regime="RISK_OFF",
                accepted=False,
                outcome=outcome,
                pnl_r=pnl_r,
                mfe_r=1.9,
                mae_r=-0.1,
                reason="test",
            )
        ],
        opportunity_set_path=Path("opportunity_set.json"),
    )
    assert "opportunity_set_hash: abc123" in text
    assert "| test_variant | 1 | 0 | 1 | 0 | 0 | 0 | 1 | -1.90 | n/a |" in text


def test_atr_reclaim_incumbent_shadow_keeps_independent_reference_line() -> None:
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        settings = _settings(Path(tmp))
        opportunity = OpportunityRow(
            source="WATCH_ONLY",
            symbol="TESTUSDT",
            plan_id="scan1:TESTUSDT",
            first_time="2026-06-19T00:00:00Z",
            reason="test",
            entry=100.0,
            entry_low=98.0,
            stop=90.0,
            tp1=120.0,
            max_price_after=119.0,
            min_price_after=95.0,
            reclaimed=True,
            hit_tp1=False,
            hit_stop=False,
            classification="missed_winner",
            explanation="test",
            maturity_status="mature",
            classification_final=True,
            mfe_r=1.9,
            counterfactual_pnl_r=1.9,
            first_hit="near_tp1_first",
            atr_4h=10.0,
            reclaim_margin_atr=0.2,
            opportunity_set_key="WATCH_ONLY:scan1:TESTUSDT",
        )
        original = shadow_module.fetch_klines_cached
        shadow_module.fetch_klines_cached = lambda *args, **kwargs: _FakeFetchResult(
            [
                _kline(0, 99, 103, 98, 102),
                _kline(1, 102, 103, 99, 101),
            ]
        )
        try:
            rows = run_atr_reclaim_incumbent_shadow(
                settings,
                OpportunitySet("demo", "2026-06-19", "2026-07-25", [opportunity], "abc123"),
            )
        finally:
            shadow_module.fetch_klines_cached = original
    by_variant = {row.variant: row for row in rows}
    assert set(by_variant) == {"reference_baseline", "atr_reclaim_0_35_shadow", "research_incumbent"}
    assert by_variant["reference_baseline"].accepted is True
    assert by_variant["atr_reclaim_0_35_shadow"].accepted is False
    assert by_variant["research_incumbent"].accepted is False
    assert by_variant["atr_reclaim_0_35_shadow"].direct_filter_contribution_r == -1.9
    assert by_variant["atr_reclaim_0_35_shadow"].capacity_state == "not_available_in_offline_opportunity_set"


if __name__ == "__main__":
    test_entry_reclaim_confirm_1bar_filters_stop_first_path()
    test_shadow_replay_report_contains_summary_sections()
    test_relative_strength_gate_filters_weak_stop_first_path()
    test_shadow_experiment_report_uses_fixed_set_and_negative_missed_winner_r()
    test_atr_reclaim_incumbent_shadow_keeps_independent_reference_line()
