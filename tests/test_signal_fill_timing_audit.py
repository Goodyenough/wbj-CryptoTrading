from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from crypto_trading_system.research_tools import (  # noqa: E402
    BlockedEntryEventExport,
    ReplayConsistencyAudit,
    build_signal_fill_timing_audit,
    render_blocked_entry_event_export,
    render_replay_consistency_audit,
    write_signal_fill_timing_audit_report,
)


def _settings(tmp_path: Path):
    reports_dir = tmp_path / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    return SimpleNamespace(
        output=SimpleNamespace(
            database_path=tmp_path / "audit.db",
            reports_dir=reports_dir,
            obsidian_dir=None,
        )
    )


def _create_backtest_tables(path: Path) -> None:
    connection = sqlite3.connect(path)
    try:
        connection.execute(
            """
            CREATE TABLE backtest_runs (
                run_id TEXT PRIMARY KEY,
                created_at_utc TEXT NOT NULL,
                symbols_json TEXT NOT NULL,
                start_utc TEXT NOT NULL,
                end_utc TEXT NOT NULL,
                config_json TEXT NOT NULL,
                commit_hash TEXT NOT NULL,
                metrics_json TEXT NOT NULL,
                report_path TEXT,
                payload_json TEXT NOT NULL
            )
            """
        )
        connection.execute(
            """
            CREATE TABLE backtest_trades (
                run_id TEXT NOT NULL,
                trade_id TEXT NOT NULL,
                symbol TEXT NOT NULL,
                status TEXT NOT NULL,
                created_at_utc TEXT NOT NULL,
                entered_at_utc TEXT,
                closed_at_utc TEXT,
                entry_price_raw REAL,
                entry_price_filled REAL,
                exit_price_raw REAL,
                exit_price_filled REAL,
                entry_fee REAL NOT NULL DEFAULT 0,
                exit_fee REAL NOT NULL DEFAULT 0,
                slippage_cost REAL NOT NULL DEFAULT 0,
                gross_pnl REAL NOT NULL DEFAULT 0,
                net_pnl REAL NOT NULL DEFAULT 0,
                r_multiple_net REAL,
                payload_json TEXT NOT NULL,
                PRIMARY KEY (run_id, trade_id)
            )
            """
        )
        connection.commit()
    finally:
        connection.close()


def _insert_run(path: Path, run_id: str = "run1") -> None:
    config = {
        "analysis": {
            "entry_reclaim_close_enabled": True,
            "entry_reclaim_min_atr_enabled": False,
            "entry_reclaim_min_atr": 0.0,
        },
        "backtest": {
            "max_active_positions": 5,
            "intrabar": "stop_first",
            "maker_fee_bps": 4,
            "taker_fee_bps": 10,
            "entry_slippage_bps": 5,
            "stop_slippage_bps": 10,
        },
    }
    connection = sqlite3.connect(path)
    try:
        connection.execute(
            """
            INSERT INTO backtest_runs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                run_id,
                "2026-07-26T00:00:00+00:00",
                json.dumps(["BTCUSDT", "ETHUSDT"]),
                "2025-06-01T00:00:00+00:00",
                "2026-06-01T00:00:00+00:00",
                json.dumps(config),
                "abc123",
                "{}",
                "report.md",
                "{}",
            ),
        )
        connection.execute(
            """
            INSERT INTO backtest_trades (
                run_id, trade_id, symbol, status, created_at_utc, entered_at_utc,
                closed_at_utc, net_pnl, r_multiple_net, payload_json
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                run_id,
                "trade1",
                "BTCUSDT",
                "STOPPED",
                "2025-06-01T00:00:00+00:00",
                "2025-06-02T04:00:00+00:00",
                "2025-06-02T04:00:00+00:00",
                -100,
                -1,
                json.dumps(
                    {
                        "notes": "Stop loss hit.",
                        "events": [
                            {
                                "event_type": "TP1_HIT",
                                "event_time_utc": "2025-06-02T04:00:00+00:00",
                            }
                        ],
                    }
                ),
            ),
        )
        connection.commit()
    finally:
        connection.close()


def test_signal_fill_timing_audit_reports_same_bar_warning(tmp_path: Path) -> None:
    settings = _settings(tmp_path)
    _create_backtest_tables(settings.output.database_path)
    _insert_run(settings.output.database_path)

    audit = build_signal_fill_timing_audit(settings, "run1", report_date="2026-07-27")

    assert audit.verdict == "timing_audit_warn_same_bar_ambiguity"
    assert audit.max_active_positions == 5
    assert audit.same_bar_entry_and_exit_trades == 1
    assert audit.same_bar_entry_and_tp1_trades == 1


def test_write_signal_fill_timing_audit_report_includes_required_sections(tmp_path: Path) -> None:
    settings = _settings(tmp_path)
    _create_backtest_tables(settings.output.database_path)
    _insert_run(settings.output.database_path)

    audit, paths = write_signal_fill_timing_audit_report(settings, "run1", report_date="2026-07-27")

    assert audit.verdict == "timing_audit_warn_same_bar_ambiguity"
    assert len(paths) == 1
    text = paths[0].read_text(encoding="utf-8")
    assert "# signal_fill_timing_audit" in text
    assert "`signal_time`" in text
    assert "`decision_time`" in text
    assert "`fill_time`" in text
    assert "same-bar ambiguity" in text
    assert '"run_id": "run1"' in text


def test_signal_fill_timing_audit_missing_run_raises(tmp_path: Path) -> None:
    settings = _settings(tmp_path)
    _create_backtest_tables(settings.output.database_path)

    try:
        build_signal_fill_timing_audit(settings, "missing")
    except ValueError as exc:
        assert "backtest run_id not found" in str(exc)
    else:
        raise AssertionError("expected missing run to raise ValueError")


def test_render_blocked_entry_event_export_includes_required_fields() -> None:
    export = BlockedEntryEventExport(
        source_run_id="source1",
        replay_run_id="replay1",
        report_date="2026-07-27",
        start_utc="2025-06-01T00:00:00+00:00",
        end_utc="2026-06-01T00:00:00+00:00",
        source_commit_hash="abc123",
        source_symbols_count=2,
        replay_symbols_count=2,
        source_entered_trades=1,
        replay_entered_trades=1,
        dynamic_universe_mode=True,
        max_universe_symbols=50,
        max_active_positions=5,
        event_count=1,
        same_bar_entry_exit_possible_events=1,
        same_bar_entry_tp1_possible_events=0,
        events_by_month={"2025-07": 1},
        events_by_symbol_top=[("ETHUSDT", 1)],
        verdict="blocked_events_exported",
        reason="test reason",
        events=[
            {
                "event_id": "event1",
                "run_id": "replay1",
                "symbol": "ETHUSDT",
                "trade_id": "trade1",
                "signal_time_utc": "2025-07-01T04:00:00+00:00",
                "decision_time_utc": "2025-07-01T04:00:00+00:00",
                "fill_time_assumption": "same_bar_entry_high_plus_slippage_after_reclaim_close",
                "block_reason": "max_active_positions",
                "candidate_rank": 3,
                "active_count_before_decision": 5,
                "active_snapshot_after_exits": [
                    {
                        "trade_id": "active1",
                        "symbol": "BTCUSDT",
                        "status": "ENTERED",
                        "entered_at_utc": "2025-06-30T00:00:00+00:00",
                        "tp1_hit_at_utc": None,
                        "score": 80.0,
                        "entry_price": 100.0,
                        "stop_loss": 90.0,
                        "quantity": 1.0,
                        "cash_risk": 10.0,
                        "unrealized_pnl": 1.0,
                        "realized_pnl": 0.0,
                        "holding_bars": 7,
                    }
                ],
                "candidate_score": 70.0,
                "candidate_created_at_utc": "2025-07-01T00:00:00+00:00",
                "candidate_entry_low": 10.0,
                "candidate_entry_high": 11.0,
                "candidate_stop_loss": 9.0,
                "candidate_take_profit_1": 13.0,
                "candidate_take_profit_2": 15.0,
                "candidate_raw_entry": 11.0,
                "candidate_entry_price_filled": 11.01,
                "candidate_cash_risk": 100.0,
                "equity_before_decision": 10000.0,
                "cash_before_decision": 5000.0,
                "same_bar_entry_exit_possible": True,
                "same_bar_entry_tp1_possible": False,
                "intrabar_policy": "stop_first",
            }
        ],
    )

    text = render_blocked_entry_event_export(export, json_filename="events.json")

    assert "# blocked_entry_event_export" in text
    assert "fill_time_assumption" in text
    assert "active_snapshot_after_exits" in text
    assert "same_bar_entry_exit_possible" in text
    assert "same_bar_entry_tp1_possible" in text
    assert "`events.json`" in text


def test_render_replay_consistency_audit_includes_limits_and_next_action() -> None:
    audit = ReplayConsistencyAudit(
        source_run_id="source1",
        replay_run_id="replay1",
        report_date="2026-07-27",
        start_utc="2025-06-01T00:00:00+00:00",
        end_utc="2026-06-01T00:00:00+00:00",
        source_commit_hash="abc123",
        source_trade_count=389,
        replay_trade_count=389,
        source_entered_trades=58,
        replay_entered_trades=58,
        source_closed_trades=58,
        replay_closed_trades=58,
        entered_signature_mismatches=0,
        active_path_points=2190,
        active_path_mismatches=0,
        open_plan_path_mismatches=0,
        final_equity_delta=0.0,
        blocked_events_json="events.json",
        blocked_events_reference_count=512,
        blocked_events_replay_count=512,
        blocked_event_signature_mismatches=0,
        candidate_ordering_evidence="source run did not persist blocked candidate order directly; current source marker and repeated blocked-event signatures match the prior export.",
        ordering_directly_persisted_in_source=False,
        verdict="replay_consistency_pass_with_ordering_limit",
        reason="test reason",
        entered_mismatch_examples=[],
        active_path_mismatch_examples=[],
        blocked_event_mismatch_examples=[],
    )

    text = render_replay_consistency_audit(audit)

    assert "# replay_consistency_audit" in text
    assert "entered_trades" in text
    assert "active_count_path" in text
    assert "blocked_event_repeat" in text
    assert "did not persist blocked candidate ordering directly" in text
    assert "Proceed to `stale_slot_continuation_review`" in text


if __name__ == "__main__":
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        test_signal_fill_timing_audit_reports_same_bar_warning(root / "audit")
        test_write_signal_fill_timing_audit_report_includes_required_sections(root / "write")
        test_signal_fill_timing_audit_missing_run_raises(root / "missing")
        test_render_blocked_entry_event_export_includes_required_fields()
        test_render_replay_consistency_audit_includes_limits_and_next_action()
