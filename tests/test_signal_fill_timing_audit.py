from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from crypto_trading_system.research_tools import (  # noqa: E402
    build_signal_fill_timing_audit,
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


if __name__ == "__main__":
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        test_signal_fill_timing_audit_reports_same_bar_warning(root / "audit")
        test_write_signal_fill_timing_audit_report_includes_required_sections(root / "write")
        test_signal_fill_timing_audit_missing_run_raises(root / "missing")
