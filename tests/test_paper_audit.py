from __future__ import annotations

from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from crypto_trading_system import paper_audit as audit_module
from crypto_trading_system.config import load_settings
from crypto_trading_system.database import connect_db
from crypto_trading_system.paper_audit import (
    build_opportunity_funnel,
    build_benchmark_rows,
    build_entered_trade_rows,
    build_opportunity_reconciliation,
    build_reclaim_opportunities,
    render_paper_audit_report,
)
from crypto_trading_system.storage import init_db


class _FakeFetchResult:
    def __init__(self, symbol: str, closes: list[float]) -> None:
        self.symbol = symbol
        self.interval = "4h"
        self.klines = []
        base = 1_781_784_000_001
        for index, close in enumerate(closes):
            open_time = base + index * 14_400_000
            self.klines.append([open_time, close, close, close, close, 1.0, open_time + 14_399_999, 1.0, 1, 1.0, 1.0, 0])
        self.issues = []
        self.fetched_from_api = 0


def _settings(root: Path):
    settings = load_settings(Path("config/settings.toml"))
    settings.output.database_path = root / "paper.db"
    settings.output.reports_dir = root / "reports"
    settings.output.obsidian_dir = None
    return settings


def _seed_base(path: Path) -> None:
    init_db(path)
    with connect_db(path) as connection:
        connection.execute(
            """
            INSERT INTO runs(run_id, run_type, started_at, finished_at, status, created_at)
            VALUES ('run1', 'manual', '2026-06-18T16:00:00Z', '2026-06-18T16:00:01Z', 'success', '2026-06-18T16:00:00Z')
            """
        )


def _seed_plan(path: Path, *, plan_id: str = "plan1", status: str = "WATCHING", entered: bool = False) -> None:
    with connect_db(path) as connection:
        connection.execute(
            """
            INSERT INTO paper_plans(
                plan_id, account_name, source_scan_id, source_symbol, created_run_id,
                created_at, symbol, entry_low, entry_high, stop_initial, stop_current,
                tp1, tp2, status, created_reason, market_regime, raw_json, updated_at,
                entry_price, entered_at_utc, realized_pnl, unrealized_pnl
            ) VALUES (?, 'demo', NULL, 'TESTUSDT', 'run1', '2026-06-18T16:00:00Z',
                      'TESTUSDT', 100, 105, 90, 90, 125, 140, ?, 'test setup',
                      'RISK_OFF', '{}', '2026-06-18T16:00:00Z', ?, ?, -100, 0)
            """,
            (
                plan_id,
                status,
                105.0 if entered else None,
                "2026-06-18T20:00:00Z" if entered else None,
            ),
        )


def test_benchmark_rows_calculate_return_and_drawdown() -> None:
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        settings = _settings(Path(tmp))
        original = audit_module.fetch_klines_cached
        audit_module.fetch_klines_cached = lambda settings, symbol, *args, **kwargs: _FakeFetchResult(symbol, [100.0, 110.0, 105.0])
        try:
            rows = build_benchmark_rows(settings, "2026-06-19", "2026-07-02")
        finally:
            audit_module.fetch_klines_cached = original
    assert rows[0].return_pct is not None and abs(rows[0].return_pct - 5.0) < 0.0001
    assert rows[0].high_return_pct is not None and abs(rows[0].high_return_pct - 10.0) < 0.0001
    assert rows[0].max_drawdown_pct < 0


def test_reclaim_pending_dedupes_and_classifies_avoided_loser() -> None:
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        settings = _settings(Path(tmp))
        _seed_base(settings.output.database_path)
        _seed_plan(settings.output.database_path)
        with connect_db(settings.output.database_path) as connection:
            for event_id, event_time in [("e1", "2026-06-19T00:00:00Z"), ("e2", "2026-06-19T04:00:00Z")]:
                connection.execute(
                    """
                    INSERT INTO paper_events(event_id, plan_id, run_id, event_time, event_type, symbol, price, reason, created_at)
                    VALUES (?, 'plan1', 'run1', ?, 'RECLAIM_PENDING_SET', 'TESTUSDT', 100, 'blocked', ?)
                    """,
                    (event_id, event_time, event_time),
                )
            connection.execute(
                """
                INSERT INTO paper_snapshots(snapshot_id, run_id, snapshot_time, plan_id, symbol, status, current_price, created_at)
                VALUES ('s1', 'run1', '2026-06-19T08:00:00Z', 'plan1', 'TESTUSDT', 'WATCHING', 89, '2026-06-19T08:00:00Z')
                """
            )
        rows = build_reclaim_opportunities(settings, "demo", "2026-06-19", "2026-07-02")
    assert len(rows) == 1
    assert rows[0].classification == "avoided_loser"
    assert rows[0].hit_stop is True
    assert rows[0].maturity_status == "mature"
    assert rows[0].counterfactual_pnl_r == -1.0


def test_reclaim_pending_classifies_missed_winner() -> None:
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        settings = _settings(Path(tmp))
        _seed_base(settings.output.database_path)
        _seed_plan(settings.output.database_path)
        with connect_db(settings.output.database_path) as connection:
            connection.execute(
                """
                INSERT INTO paper_events(event_id, plan_id, run_id, event_time, event_type, symbol, price, reason, created_at)
                VALUES ('e1', 'plan1', 'run1', '2026-06-19T00:00:00Z', 'RECLAIM_PENDING_SET', 'TESTUSDT', 100, 'blocked', '2026-06-19T00:00:00Z')
                """
            )
            connection.execute(
                """
                INSERT INTO paper_snapshots(snapshot_id, run_id, snapshot_time, plan_id, symbol, status, current_price, created_at)
                VALUES ('s1', 'run1', '2026-06-19T08:00:00Z', 'plan1', 'TESTUSDT', 'WATCHING', 126, '2026-06-19T08:00:00Z')
                """
            )
        rows = build_reclaim_opportunities(settings, "demo", "2026-06-19", "2026-07-02")
    assert rows[0].classification == "missed_winner"
    assert rows[0].hit_tp1 is True
    assert rows[0].maturity_status == "mature"
    assert rows[0].mfe_r is not None and rows[0].mfe_r >= 1.0


def test_reclaim_pending_marks_right_censored_when_path_is_short_and_inconclusive() -> None:
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        settings = _settings(Path(tmp))
        _seed_base(settings.output.database_path)
        _seed_plan(settings.output.database_path)
        with connect_db(settings.output.database_path) as connection:
            connection.execute(
                """
                INSERT INTO paper_events(event_id, plan_id, run_id, event_time, event_type, symbol, price, reason, created_at)
                VALUES ('e1', 'plan1', 'run1', '2026-06-19T00:00:00Z', 'RECLAIM_PENDING_SET', 'TESTUSDT', 100, 'blocked', '2026-06-19T00:00:00Z')
                """
            )
            connection.execute(
                """
                INSERT INTO paper_snapshots(snapshot_id, run_id, snapshot_time, plan_id, symbol, status, current_price, created_at)
                VALUES ('s1', 'run1', '2026-06-19T04:00:00Z', 'plan1', 'TESTUSDT', 'WATCHING', 104, '2026-06-19T04:00:00Z')
                """
            )
        rows = build_reclaim_opportunities(settings, "demo", "2026-06-19", "2026-07-02")
    assert rows[0].classification == "neutral_or_unknown"
    assert rows[0].maturity_status == "right_censored"
    assert rows[0].classification_final is False


def test_opportunity_reconciliation_counts_raw_and_deduped_reclaim_events() -> None:
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        settings = _settings(Path(tmp))
        _seed_base(settings.output.database_path)
        _seed_plan(settings.output.database_path)
        with connect_db(settings.output.database_path) as connection:
            for event_id, event_time in [("e1", "2026-06-19T00:00:00Z"), ("e2", "2026-06-19T04:00:00Z")]:
                connection.execute(
                    """
                    INSERT INTO paper_events(event_id, plan_id, run_id, event_time, event_type, symbol, price, reason, created_at)
                    VALUES (?, 'plan1', 'run1', ?, 'RECLAIM_PENDING_SET', 'TESTUSDT', 100, 'blocked', ?)
                    """,
                    (event_id, event_time, event_time),
                )
        reclaim_rows = build_reclaim_opportunities(settings, "demo", "2026-06-19", "2026-07-02")
        reconciliation = build_opportunity_reconciliation(
            settings,
            "demo",
            "2026-06-19",
            "2026-07-02",
            reclaim_rows=reclaim_rows,
            scan_rows=[],
            false_entries=[],
        )
    assert reconciliation.raw_reclaim_pending_events == 2
    assert reconciliation.deduped_reclaim_plans == 1
    assert reconciliation.excluded_reclaim_duplicate_events == 1
    assert reconciliation.final_classified_opportunities == 1


def test_opportunity_funnel_counts_scan_actions_and_entered_plans() -> None:
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        settings = _settings(Path(tmp))
        _seed_base(settings.output.database_path)
        _seed_plan(settings.output.database_path, status="STOPPED", entered=True)
        with connect_db(settings.output.database_path) as connection:
            connection.execute(
                """
                INSERT INTO scan_runs(scan_id, timestamp_utc, source, filters, limitations_json)
                VALUES ('scan1', '2026-06-19T00:00:00Z', 'test', '{}', '[]')
                """
            )
            connection.execute(
                """
                INSERT INTO market_scans(scan_id, run_id, scan_time, config_hash, report_path, created_at)
                VALUES ('scan1', 'run1', '2026-06-19T00:00:00Z', 'hash', NULL, '2026-06-19T00:00:00Z')
                """
            )
            connection.execute(
                """
                INSERT INTO scan_candidates(
                    scan_id, symbol, rank, base_asset, verdict, score, action,
                    price, entry_low, entry_high, stop, tp1, reason, payload_json, created_at
                )
                VALUES ('scan1', 'TESTUSDT', 1, 'TEST', 'candidate', 80, 'BUY_CANDIDATE', 100, 100, 105, 90, 125, 'ok', '{}', '2026-06-19T00:00:00Z')
                """
            )
            connection.execute(
                """
                INSERT INTO scan_candidates(
                    scan_id, symbol, rank, base_asset, verdict, score, action,
                    price, entry_low, entry_high, stop, tp1, reason, payload_json, created_at
                )
                VALUES ('scan1', 'WEAKUSDT', 2, 'WEAK', 'watch', 50, 'WATCH_ONLY', 50, 50, 55, 45, 65, 'risk_off weak market', '{"market_regime":"RISK_OFF"}', '2026-06-19T00:00:00Z')
                """
            )
        rows = build_opportunity_funnel(settings, "demo", "2026-06-19", "2026-07-02", opportunities=[])
    by_stage = {row.stage: row for row in rows}
    assert by_stage["scanned_candidates"].count == 2
    assert by_stage["buy_candidates"].count == 1
    assert by_stage["watch_only_candidates"].count == 1
    assert by_stage["risk_off_blocked_candidates"].count == 1
    assert by_stage["entered_plans"].count == 1
    assert by_stage["stopped_plans"].count == 1


def test_entered_trade_review_calculates_r_and_entry_issue() -> None:
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        settings = _settings(Path(tmp))
        _seed_base(settings.output.database_path)
        _seed_plan(settings.output.database_path, status="STOPPED", entered=True)
        with connect_db(settings.output.database_path) as connection:
            for idx, price in enumerate([106.0, 89.0], start=1):
                run_id = f"run_snap_{idx}"
                timestamp = f"2026-06-19T0{idx}:00:00Z"
                connection.execute(
                    """
                    INSERT INTO runs(run_id, run_type, started_at, finished_at, status, created_at)
                    VALUES (?, 'paper_4h_update', ?, ?, 'success', ?)
                    """,
                    (run_id, timestamp, timestamp, timestamp),
                )
                connection.execute(
                    """
                    INSERT INTO paper_snapshots(snapshot_id, run_id, snapshot_time, plan_id, symbol, status, current_price, created_at)
                    VALUES (?, ?, ?, 'plan1', 'TESTUSDT', 'STOPPED', ?, ?)
                    """,
                    (f"s{idx}", run_id, timestamp, price, timestamp),
                )
        rows = build_entered_trade_rows(settings, "demo", "2026-06-19", "2026-07-02")
    assert len(rows) == 1
    assert rows[0].mfe_r is not None and rows[0].mfe_r < 0.5
    assert rows[0].attribution == "market_issue"


def test_report_contains_core_sections() -> None:
    text = render_paper_audit_report(
        account="demo",
        start_date="2026-06-19",
        end_date="2026-07-02",
        report_version=1,
        benchmarks=[],
        opportunities=[],
        entered_trades=[],
    )
    assert "## BTC/ETH Benchmark" in text
    assert "## Opportunity Audit Summary" in text
    assert "### Opportunity Maturity" in text
    assert "### Opportunity Funnel" in text
    assert "### Reclaim Reconciliation" in text
    assert "### Counterfactual R Summary" in text
    assert "## Entered Trades Review" in text


if __name__ == "__main__":
    test_benchmark_rows_calculate_return_and_drawdown()
    test_reclaim_pending_dedupes_and_classifies_avoided_loser()
    test_reclaim_pending_classifies_missed_winner()
    test_reclaim_pending_marks_right_censored_when_path_is_short_and_inconclusive()
    test_opportunity_reconciliation_counts_raw_and_deduped_reclaim_events()
    test_opportunity_funnel_counts_scan_actions_and_entered_plans()
    test_entered_trade_review_calculates_r_and_entry_issue()
    test_report_contains_core_sections()
