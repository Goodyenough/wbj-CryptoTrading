from __future__ import annotations

import json
from pathlib import Path
import sqlite3
import sys
import tempfile
import threading
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from crypto_trading_system.database import connect_db, database_status, tracked_run
from crypto_trading_system import database as database_module
from crypto_trading_system.config import load_settings
from crypto_trading_system.models import PaperTrade, ScanResult
from crypto_trading_system.paper_db import audit_database_stability, build_paper_db_summary, export_paper_db
from crypto_trading_system import paper_trader as paper_trader_module
from crypto_trading_system.paper_trader import (
    _insert_paper_trade,
    _save_trade_update,
    _structured_step_event_type,
    _sync_paper_plan,
    add_from_scan,
    generate_paper_report,
    load_all_paper_trades,
    load_paper_events,
    update_paper_trades,
)
from crypto_trading_system.research_tools import generate_observation_dashboard
from crypto_trading_system.storage import init_db, save_scan_result
import main as main_module


def _temp_db() -> Path:
    return Path(tempfile.mkdtemp()) / "paper.db"


def _trade(status: str = "WATCHING") -> PaperTrade:
    return PaperTrade(
        paper_trade_id="plan1",
        account_name="demo",
        source_scan_id="scan1",
        source_rank=1,
        symbol="TESTUSDT",
        base_asset="TEST",
        status=status,
        created_at_utc="2026-06-12T00:00:00Z",
        updated_at_utc="2026-06-12T00:00:00Z",
        setup="test",
        verdict="test",
        entry_low=100.0,
        entry_high=105.0,
        planned_entry_mid=102.5,
        stop_loss=90.0,
        take_profit_1=120.0,
        take_profit_2=135.0,
        risk_reward_1=2.0,
        risk_reward_2=3.0,
        account_equity=10_000.0,
        risk_per_trade_pct=0.01,
        cash_risk=100.0,
    )


def _seed_scan_and_run(path: Path) -> None:
    with connect_db(path) as connection:
        connection.execute(
            """
            INSERT INTO runs(run_id, run_type, started_at, finished_at, status, created_at)
            VALUES ('run1', 'manual', '2026-06-12T00:00:00Z', '2026-06-12T00:00:01Z', 'success', '2026-06-12T00:00:00Z')
            """
        )
        connection.execute(
            """
            INSERT INTO scan_runs(scan_id, timestamp_utc, source, filters, limitations_json)
            VALUES ('scan1', '2026-06-12T00:00:00Z', 'test', 'test', '[]')
            """
        )
        connection.execute(
            """
            INSERT INTO market_scans(scan_id, run_id, scan_time, candidate_count, created_at)
            VALUES ('scan1', 'run1', '2026-06-12T00:00:00Z', 1, '2026-06-12T00:00:00Z')
            """
        )


def test_database_init_is_idempotent_and_configured() -> None:
    path = _temp_db()
    init_db(path)
    init_db(path)
    status = database_status(path)
    assert status["schema_version"] == "2"
    assert status["journal_mode"] == "wal"
    assert status["synchronous"] == 1
    assert status["foreign_keys"] == 1
    assert status["busy_timeout_ms"] == 30_000
    assert status["foreign_key_errors"] == []
    assert status["indexes_ok"] is True
    assert status["missing_indexes"] == []
    assert status["tables_ok"] is True


def test_tracked_run_records_success_and_failure() -> None:
    path = _temp_db()
    init_db(path)
    with tracked_run(path, "manual") as success_id:
        assert success_id
    try:
        with tracked_run(path, "manual"):
            raise ValueError("expected failure")
    except ValueError:
        pass
    with connect_db(path) as connection:
        rows = connection.execute(
            "SELECT status, error_message FROM runs WHERE run_type='manual' ORDER BY started_at"
        ).fetchall()
    assert [row["status"] for row in rows] == ["success", "failed"]
    assert "expected failure" in rows[-1]["error_message"]


def test_run_step_persists_run_id_step_and_lock_error() -> None:
    path = _temp_db()
    init_db(path)
    try:
        with tracked_run(path, "manual") as run_id:
            with main_module._run_step(run_id, "paper_update"):
                raise sqlite3.OperationalError("database is locked")
    except RuntimeError as exc:
        assert f"run_id={run_id}" in str(exc)
        assert "step=paper_update" in str(exc)
        assert "database is locked" in str(exc)
    else:
        raise AssertionError("Step context must preserve the failing run and step")

    with connect_db(path) as connection:
        row = connection.execute("SELECT status, error_message FROM runs WHERE run_id = ?", (run_id,)).fetchone()
    assert row["status"] == "failed"
    assert f"run_id={run_id}" in row["error_message"]
    assert "step=paper_update" in row["error_message"]
    assert "database is locked" in row["error_message"]


def test_state_transition_and_stop_are_monotonic() -> None:
    path = _temp_db()
    init_db(path)
    _seed_scan_and_run(path)
    trade = _trade()
    payload = {"stop_loss": 90.0}
    with connect_db(path) as connection:
        assert _insert_paper_trade(connection, trade, payload)
        _sync_paper_plan(connection, trade, run_id="run1", payload=payload)

    trade.status = "ENTERED"
    trade.stop_loss = 95.0
    trade.updated_at_utc = "2026-06-12T04:00:00Z"
    with connect_db(path) as connection:
        _save_trade_update(connection, trade, expected_status="WATCHING")
        _sync_paper_plan(connection, trade, run_id="run1")

    trade.status = "WATCHING"
    with connect_db(path) as connection:
        try:
            _save_trade_update(connection, trade, expected_status="ENTERED")
        except ValueError as exc:
            assert "Illegal paper state transition" in str(exc)
        else:
            raise AssertionError("State rollback should be rejected")

    trade.status = "ENTERED"
    trade.stop_loss = 90.0
    with connect_db(path) as connection:
        try:
            _save_trade_update(connection, trade, expected_status="ENTERED")
        except ValueError as exc:
            assert "cannot decrease" in str(exc)
        else:
            raise AssertionError("Stop decrease should be rejected")


def test_summary_and_export_use_structured_tables() -> None:
    path = _temp_db()
    init_db(path)
    _seed_scan_and_run(path)
    trade = _trade()
    with connect_db(path) as connection:
        connection.execute("UPDATE runs SET run_type='daily_full' WHERE run_id='run1'")
        connection.execute(
            "UPDATE market_scans SET candidate_count=3, buy_candidate_count=2 WHERE scan_id='scan1'"
        )
        assert _insert_paper_trade(connection, trade, {"stop_loss": 90.0})
        _sync_paper_plan(connection, trade, run_id="run1", payload={"stop_loss": 90.0})
        for index, event_type in enumerate(("PLAN_CREATED", "TP1_HIT", "TP1_EMA_TRAILING_ACTIVATED")):
            connection.execute(
                """
                INSERT INTO paper_events(
                    event_id, plan_id, run_id, event_time, event_type, symbol, created_at
                ) VALUES (?, 'plan1', 'run1', ?, ?, 'TESTUSDT', ?)
                """,
                (f"event{index}", f"2026-06-12T0{index}:00:00Z", event_type, f"2026-06-12T0{index}:00:00Z"),
            )
    summary = build_paper_db_summary(path)
    assert "recent_runs" in summary
    assert "event_counts" in summary
    assert summary["observation_totals"]["scan_count"] == 1
    assert summary["observation_totals"]["candidate_count"] == 3
    assert summary["observation_totals"]["buy_candidate_count"] == 2
    assert summary["observation_totals"]["paper_plan_count"] == 1
    assert summary["observation_totals"]["tp1_hit"] == 1
    assert summary["observation_totals"]["ema_trailing_activated"] == 1
    assert summary["run_type_summary"]["daily_full"]["success"] == 1
    assert summary["run_type_summary"]["daily_full"]["beijing_dates"] == ["2026-06-12"]
    output_dir = path.parent / "exports"
    exports = export_paper_db(path, output_dir)
    assert len(exports) == 3
    assert all(item.exists() for item in exports)


def test_wal_allows_reader_during_write_transaction() -> None:
    path = _temp_db()
    init_db(path)
    writer = connect_db(path)
    reader = connect_db(path)
    try:
        writer.execute("BEGIN IMMEDIATE")
        writer.execute(
            """
            INSERT INTO runs(run_id, run_type, started_at, status, created_at)
            VALUES ('concurrent', 'manual', '2026-06-12T00:00:00Z', 'running', '2026-06-12T00:00:00Z')
            """
        )
        count = reader.execute("SELECT COUNT(*) FROM runs").fetchone()[0]
        assert count >= 1
    finally:
        writer.rollback()
        writer.close()
        reader.close()


def test_locked_write_waits_then_marks_run_failed() -> None:
    path = _temp_db()
    init_db(path)
    original_timeout = database_module.BUSY_TIMEOUT_MS
    database_module.BUSY_TIMEOUT_MS = 50
    lock_started = threading.Event()

    def hold_write_lock() -> None:
        with connect_db(path) as blocker:
            blocker.execute("BEGIN IMMEDIATE")
            blocker.execute(
                """
                INSERT INTO runs(run_id, run_type, started_at, status, created_at)
                VALUES ('blocker', 'manual', '2026-06-12T00:00:00Z', 'running', '2026-06-12T00:00:00Z')
                """
            )
            lock_started.set()
            time.sleep(0.5)

    try:
        with tracked_run(path, "manual") as run_id:
            contender = connect_db(path)
            worker = threading.Thread(target=hold_write_lock)
            worker.start()
            assert lock_started.wait(timeout=1)
            started = time.monotonic()
            try:
                contender.execute(
                    """
                    INSERT INTO runs(run_id, run_type, started_at, status, created_at)
                    VALUES ('contended', 'manual', '2026-06-12T00:00:00Z', 'running', '2026-06-12T00:00:00Z')
                    """
                )
            except sqlite3.OperationalError as exc:
                assert "locked" in str(exc).lower()
                assert time.monotonic() - started >= 0.04
                raise
            finally:
                contender.close()
                worker.join(timeout=1)
    except sqlite3.OperationalError:
        pass
    finally:
        database_module.BUSY_TIMEOUT_MS = original_timeout

    with connect_db(path) as connection:
        row = connection.execute("SELECT status, error_message FROM runs WHERE run_id = ?", (run_id,)).fetchone()
    assert row["status"] == "failed", dict(row)
    assert "database is locked" in row["error_message"].lower()


class _FakeBinanceClient:
    close_time: int = 1
    close_price: float = 106.0
    kline_error: Exception | None = None

    def __init__(self, *args, **kwargs) -> None:
        pass

    def ticker_24hr(self) -> list[dict]:
        return [{"symbol": "TESTUSDT", "lastPrice": "103"}]

    def klines(self, symbol: str, interval: str, limit: int) -> list[list]:
        if self.kline_error is not None:
            raise self.kline_error
        return [
            [index, "100", "107", "99", str(self.close_price), "1", self.close_time, "1", 1, "1", "1", "0"]
            for index in range(25)
        ]


def _settings_for(path: Path):
    settings = load_settings(ROOT / "config" / "settings.toml")
    settings.output.database_path = path
    return settings


def test_paper_update_writes_event_plan_and_snapshot_atomically() -> None:
    path = _temp_db()
    init_db(path)
    _seed_scan_and_run(path)
    trade = _trade()
    with connect_db(path) as connection:
        assert _insert_paper_trade(connection, trade, {"stop_loss": 90.0})
        _sync_paper_plan(connection, trade, run_id="run1", payload={"stop_loss": 90.0})
    original_client = paper_trader_module.BinanceClient
    paper_trader_module.BinanceClient = _FakeBinanceClient
    try:
        updated = update_paper_trades(_settings_for(path), run_id="run1")
    finally:
        paper_trader_module.BinanceClient = original_client
    assert updated[0].status == "ENTERED"
    with connect_db(path) as connection:
        assert connection.execute("SELECT status FROM paper_plans WHERE plan_id='plan1'").fetchone()[0] == "ENTERED"
        assert connection.execute("SELECT COUNT(*) FROM paper_events WHERE event_type='ENTERED'").fetchone()[0] == 1
        assert connection.execute("SELECT COUNT(*) FROM paper_snapshots WHERE run_id='run1'").fetchone()[0] == 1


def test_plan_failure_rolls_back_atomically_and_next_plan_continues() -> None:
    path = _temp_db()
    init_db(path)
    _seed_scan_and_run(path)
    first = _trade()
    second = _trade()
    second.paper_trade_id = "plan2"
    second.source_rank = 2
    second.symbol = "SECONDUSDT"
    second.base_asset = "SECOND"
    with connect_db(path) as connection:
        assert _insert_paper_trade(connection, first, {"stop_loss": 90.0})
        _sync_paper_plan(connection, first, run_id="run1", payload={"stop_loss": 90.0})
        assert _insert_paper_trade(connection, second, {"stop_loss": 90.0})
        _sync_paper_plan(connection, second, run_id="run1", payload={"stop_loss": 90.0})

    class _TwoSymbolClient(_FakeBinanceClient):
        def ticker_24hr(self) -> list[dict]:
            return [
                {"symbol": "TESTUSDT", "lastPrice": "103"},
                {"symbol": "SECONDUSDT", "lastPrice": "103"},
            ]

    original_client = paper_trader_module.BinanceClient
    original_record_event = paper_trader_module._record_event

    def fail_first_event(connection, trade, *args, **kwargs):
        if trade.paper_trade_id == "plan1":
            raise RuntimeError("injected event failure")
        return original_record_event(connection, trade, *args, **kwargs)

    paper_trader_module.BinanceClient = _TwoSymbolClient
    paper_trader_module._record_event = fail_first_event
    try:
        try:
            update_paper_trades(_settings_for(path), run_id="run1")
        except RuntimeError as exc:
            assert "plan1/TESTUSDT" in str(exc)
            assert "injected event failure" in str(exc)
        else:
            raise AssertionError("A plan-level write failure must fail the overall update run")
    finally:
        paper_trader_module.BinanceClient = original_client
        paper_trader_module._record_event = original_record_event

    with connect_db(path) as connection:
        first_row = connection.execute("SELECT status FROM paper_plans WHERE plan_id='plan1'").fetchone()
        second_row = connection.execute("SELECT status FROM paper_plans WHERE plan_id='plan2'").fetchone()
        assert first_row["status"] == "WATCHING"
        assert second_row["status"] == "ENTERED"
        assert connection.execute("SELECT COUNT(*) FROM paper_events WHERE plan_id='plan1'").fetchone()[0] == 0
        assert connection.execute("SELECT COUNT(*) FROM paper_snapshots WHERE plan_id='plan1'").fetchone()[0] == 0
        assert connection.execute("SELECT COUNT(*) FROM paper_events WHERE plan_id='plan2'").fetchone()[0] == 1
        assert connection.execute("SELECT COUNT(*) FROM paper_snapshots WHERE plan_id='plan2'").fetchone()[0] == 1


def test_scan_and_plan_inherit_run_metadata() -> None:
    path = _temp_db()
    init_db(path)
    with connect_db(path) as connection:
        connection.execute(
            """
            INSERT INTO runs(
                run_id, run_type, started_at, finished_at, status, config_hash, created_at
            ) VALUES (
                'metadata_run', 'daily_full', '2026-06-12T00:00:00Z',
                '2026-06-12T00:00:01Z', 'success', 'config123', '2026-06-12T00:00:00Z'
            )
            """
        )
    result = ScanResult(
        scan_id="metadata_scan",
        timestamp_utc="2026-06-12T00:00:00Z",
        source="test",
        filters="test",
        limitations=["Market regime: RISK_OFF"],
        candidates=[],
    )
    save_scan_result(path, result, run_id="metadata_run")
    trade = _trade()
    trade.source_scan_id = "metadata_scan"
    with connect_db(path) as connection:
        scan = connection.execute(
            "SELECT market_regime, config_hash FROM market_scans WHERE scan_id='metadata_scan'"
        ).fetchone()
        assert scan["market_regime"] == "RISK_OFF"
        assert scan["config_hash"] == "config123"
        assert _insert_paper_trade(connection, trade, {"stop_loss": 90.0})
        _sync_paper_plan(connection, trade, run_id="metadata_run", payload={"stop_loss": 90.0})
        plan = connection.execute(
            "SELECT market_regime FROM paper_plans WHERE plan_id='plan1'"
        ).fetchone()
        assert plan["market_regime"] == "RISK_OFF"


def test_schema_v2_backfills_operational_plan_fields() -> None:
    path = _temp_db()
    init_db(path)
    _seed_scan_and_run(path)
    trade = _trade(status="ENTERED")
    trade.quantity = 12.5
    trade.entry_price = 103.0
    trade.entered_at_utc = "2026-06-12T01:00:00Z"
    trade.realized_pnl = 7.5
    trade.unrealized_pnl = 11.25
    trade.last_price = 104.5
    trade.notes = "migrated state"
    trade.tp1_trailing_ema_stop_active = True
    with connect_db(path) as connection:
        assert _insert_paper_trade(connection, trade, {"stop_loss": 90.0})
        _sync_paper_plan(connection, trade, run_id="run1", payload={"stop_loss": 90.0})
        connection.execute(
            """
            UPDATE paper_plans SET
                source_rank=NULL, quantity=NULL, entry_price=NULL, entered_at_utc=NULL,
                realized_pnl=0, unrealized_pnl=0, last_price=NULL, notes='',
                tp1_trailing_ema_stop_active=0
            WHERE plan_id='plan1'
            """
        )
    init_db(path)
    with connect_db(path) as connection:
        row = connection.execute(
            """
            SELECT source_rank, quantity, entry_price, entered_at_utc, realized_pnl,
                   unrealized_pnl, last_price, notes, tp1_trailing_ema_stop_active
            FROM paper_plans WHERE plan_id='plan1'
            """
        ).fetchone()
    assert row["source_rank"] == 1
    assert row["quantity"] == 12.5
    assert row["entry_price"] == 103.0
    assert row["entered_at_utc"] == "2026-06-12T01:00:00Z"
    assert row["realized_pnl"] == 7.5
    assert row["unrealized_pnl"] == 11.25
    assert row["last_price"] == 104.5
    assert row["notes"] == "migrated state"
    assert row["tp1_trailing_ema_stop_active"] == 1


def test_add_from_scan_writes_plan_created_once() -> None:
    path = _temp_db()
    init_db(path)
    _seed_scan_and_run(path)
    payload = {
        "action": "BUY_CANDIDATE",
        "symbol": "TESTUSDT",
        "base_asset": "TEST",
        "setup": "test setup",
        "verdict": "test verdict",
        "entry_low": 100.0,
        "entry_high": 105.0,
        "stop_loss": 90.0,
        "take_profit_1": 120.0,
        "take_profit_2": 135.0,
        "risk_reward_1": 2.0,
        "risk_reward_2": 3.0,
        "price": 103.0,
    }
    with connect_db(path) as connection:
        connection.execute(
            """
            INSERT INTO scan_candidates(
                scan_id, rank, symbol, base_asset, verdict, score, payload_json
            ) VALUES ('scan1', 1, 'TESTUSDT', 'TEST', 'test verdict', 1.0, ?)
            """,
            (json.dumps(payload),),
        )
    settings = _settings_for(path)
    first = add_from_scan(settings, scan_id="scan1", run_id="run1")
    second = add_from_scan(settings, scan_id="scan1", run_id="run1")
    assert first["added"] == 1
    assert second["added"] == 0
    with connect_db(path) as connection:
        assert connection.execute("SELECT COUNT(*) FROM paper_plans").fetchone()[0] == 1
        assert connection.execute(
            "SELECT COUNT(*) FROM paper_events WHERE event_type='PLAN_CREATED'"
        ).fetchone()[0] == 1


def test_unclosed_kline_records_skip_without_state_change() -> None:
    path = _temp_db()
    init_db(path)
    _seed_scan_and_run(path)
    trade = _trade()
    with connect_db(path) as connection:
        assert _insert_paper_trade(connection, trade, {"stop_loss": 90.0})
        _sync_paper_plan(connection, trade, run_id="run1", payload={"stop_loss": 90.0})
    original_client = paper_trader_module.BinanceClient
    _FakeBinanceClient.close_time = 4_102_444_800_000
    _FakeBinanceClient.close_price = 100.0
    paper_trader_module.BinanceClient = _FakeBinanceClient
    try:
        update_paper_trades(_settings_for(path), run_id="run1")
        update_paper_trades(_settings_for(path), run_id="run1")
    finally:
        paper_trader_module.BinanceClient = original_client
        _FakeBinanceClient.close_time = 1
        _FakeBinanceClient.close_price = 106.0
    with connect_db(path) as connection:
        assert connection.execute("SELECT status FROM paper_plans WHERE plan_id='plan1'").fetchone()[0] == "WATCHING"
        assert connection.execute(
            "SELECT COUNT(*) FROM paper_events WHERE event_type='API_DELAY_SKIPPED'"
        ).fetchone()[0] == 1
        assert connection.execute(
            "SELECT COUNT(*) FROM paper_trade_events WHERE event_type='API_DELAY_SKIPPED'"
        ).fetchone()[0] == 1
        plan = connection.execute(
            "SELECT updated_at, created_reason FROM paper_plans WHERE plan_id='plan1'"
        ).fetchone()
        assert plan["updated_at"] == "2026-06-12T00:00:00Z"
        assert plan["created_reason"] == ""


def test_kline_api_error_is_recorded_and_does_not_fail_run() -> None:
    path = _temp_db()
    init_db(path)
    _seed_scan_and_run(path)
    trade = _trade()
    with connect_db(path) as connection:
        assert _insert_paper_trade(connection, trade, {"stop_loss": 90.0})
        _sync_paper_plan(connection, trade, run_id="run1", payload={"stop_loss": 90.0})
    original_client = paper_trader_module.BinanceClient
    _FakeBinanceClient.kline_error = TimeoutError("exchange delayed")
    paper_trader_module.BinanceClient = _FakeBinanceClient
    try:
        updated = update_paper_trades(_settings_for(path), run_id="run1")
    finally:
        paper_trader_module.BinanceClient = original_client
        _FakeBinanceClient.kline_error = None
    assert len(updated) == 1
    assert updated[0].status == "WATCHING"
    with connect_db(path) as connection:
        row = connection.execute(
            "SELECT reason FROM paper_events WHERE event_type='API_DELAY_SKIPPED'"
        ).fetchone()
        assert row is not None
        assert "exchange delayed" in row["reason"]
        assert connection.execute(
            "SELECT COUNT(*) FROM paper_trade_events WHERE event_type='API_DELAY_SKIPPED'"
        ).fetchone()[0] == 1
        plan = connection.execute(
            "SELECT updated_at, created_reason FROM paper_plans WHERE plan_id='plan1'"
        ).fetchone()
        assert plan["updated_at"] == "2026-06-12T00:00:00Z"
        assert plan["created_reason"] == ""


def test_structured_event_names_cover_plan_requirements() -> None:
    assert _structured_step_event_type("ENTERED", "entered", True) == "RECLAIM_CONFIRMED_ENTERED"
    assert (
        _structured_step_event_type("STOPPED", "EMA20 trailing stop hit.", False)
        == "EMA_TRAILING_STOPPED"
    )
    assert _structured_step_event_type("CLOSED", "TP2 hit; trade closed.", False) == "TP2_HIT"
    assert _structured_step_event_type("TP1_HIT", "TP1 hit", False) == "TP1_HIT"


def test_report_contains_current_run_events_and_api_delay_count() -> None:
    root = Path(tempfile.mkdtemp())
    path = root / "paper.db"
    init_db(path)
    _seed_scan_and_run(path)
    trade = _trade()
    with connect_db(path) as connection:
        assert _insert_paper_trade(connection, trade, {"stop_loss": 90.0})
        _sync_paper_plan(connection, trade, run_id="run1", payload={"stop_loss": 90.0})
        connection.execute(
            """
            INSERT INTO paper_events(
                event_id, plan_id, run_id, event_time, event_type, symbol,
                old_status, new_status, reason, created_at
            ) VALUES (
                'delay1', 'plan1', 'run1', '2026-06-12T04:10:00Z',
                'API_DELAY_SKIPPED', 'TESTUSDT', 'WATCHING', 'WATCHING',
                '4h kline not closed', '2026-06-12T04:10:00Z'
            )
            """
        )
    settings = _settings_for(path)
    settings.output.reports_dir = root / "reports"
    settings.output.obsidian_dir = None
    original_client = paper_trader_module.BinanceClient
    paper_trader_module.BinanceClient = _FakeBinanceClient
    try:
        report, paths = generate_paper_report(
            settings,
            run_id="run1",
            run_type="paper_4h_update",
        )
    finally:
        paper_trader_module.BinanceClient = original_client
    assert paths
    assert "## 本次 Run 状态变化" in report
    assert "This run API delay skipped | 1" in report
    assert "API_DELAY_SKIPPED" in report
    assert paths[0].name.startswith("paper_4h_update_")


def test_structured_tables_remain_operational_without_legacy_rows() -> None:
    root = Path(tempfile.mkdtemp())
    path = root / "paper.db"
    init_db(path)
    _seed_scan_and_run(path)
    trade = _trade()
    with connect_db(path) as connection:
        assert _insert_paper_trade(connection, trade, {"stop_loss": 90.0})
        _sync_paper_plan(connection, trade, run_id="run1", payload={"stop_loss": 90.0})
        connection.execute("DELETE FROM paper_trade_events")
        connection.execute("DELETE FROM paper_trades")

    settings = _settings_for(path)
    settings.output.reports_dir = root / "reports"
    settings.output.obsidian_dir = None
    original_client = paper_trader_module.BinanceClient
    paper_trader_module.BinanceClient = _FakeBinanceClient
    try:
        updated = update_paper_trades(settings, run_id="run1")
        report, report_paths = generate_paper_report(
            settings,
            run_id="run1",
            run_type="paper_4h_update",
        )
        dashboard, dashboard_paths = generate_observation_dashboard(
            settings,
            run_id="run1",
            run_type="paper_4h_update",
        )
    finally:
        paper_trader_module.BinanceClient = original_client

    assert updated[0].status == "ENTERED"
    assert load_all_paper_trades(settings)[0].status == "ENTERED"
    events = load_paper_events(settings)["plan1"]
    assert any(event.event_type == "ENTERED" for event in events)
    assert report_paths and dashboard_paths
    assert "This run events" in report
    assert "Run ID" in dashboard
    with connect_db(path) as connection:
        assert connection.execute(
            "SELECT status FROM paper_plans WHERE plan_id='plan1'"
        ).fetchone()[0] == "ENTERED"
        assert connection.execute(
            "SELECT COUNT(*) FROM paper_events WHERE plan_id='plan1'"
        ).fetchone()[0] == 1
        assert connection.execute("SELECT COUNT(*) FROM paper_trades").fetchone()[0] == 0


def _seed_stability_days(path: Path, reports_dir: Path, day_count: int = 5) -> None:
    init_db(path)
    _seed_scan_and_run(path)
    trade = _trade()
    with connect_db(path) as connection:
        assert _insert_paper_trade(connection, trade, {"stop_loss": 90.0})
        _sync_paper_plan(connection, trade, run_id="run1", payload={"stop_loss": 90.0})
        for index in range(day_count):
            date_text = f"2026-06-{13 + index:02d}"
            run_id = f"daily_{index}"
            timestamp = f"{date_text}T12:05:00Z"
            connection.execute(
                """
                INSERT INTO runs(run_id, run_type, started_at, finished_at, status, created_at)
                VALUES (?, 'daily_full', ?, ?, 'success', ?)
                """,
                (run_id, timestamp, f"{date_text}T12:07:00Z", timestamp),
            )
            scan_id = f"daily_scan_{index}"
            connection.execute(
                """
                INSERT INTO scan_runs(scan_id, timestamp_utc, source, filters, limitations_json)
                VALUES (?, ?, 'test', 'test', '[]')
                """,
                (scan_id, timestamp),
            )
            connection.execute(
                """
                INSERT INTO market_scans(scan_id, run_id, scan_time, candidate_count, created_at)
                VALUES (?, ?, ?, 1, ?)
                """,
                (scan_id, run_id, timestamp, timestamp),
            )
            connection.execute(
                """
                INSERT INTO paper_snapshots(
                    snapshot_id, run_id, snapshot_time, plan_id, symbol, status, created_at
                ) VALUES (?, ?, ?, 'plan1', 'TESTUSDT', 'WATCHING', ?)
                """,
                (f"snapshot_{index}", run_id, timestamp, timestamp),
            )
            report_dir = reports_dir / date_text
            report_dir.mkdir(parents=True, exist_ok=True)
            (report_dir / f"market_scan_{date_text}_v1.md").write_text(run_id, encoding="utf-8")
            (report_dir / f"paper_report_{date_text}_demo_v1.md").write_text(run_id, encoding="utf-8")
            (report_dir / f"paper_observation_dashboard_{date_text}_demo_v1.md").write_text(
                run_id,
                encoding="utf-8",
            )


def test_stability_audit_requires_five_complete_consecutive_days() -> None:
    root = Path(tempfile.mkdtemp())
    path = root / "paper.db"
    reports_dir = root / "reports"
    _seed_stability_days(path, reports_dir)
    audit = audit_database_stability(path, reports_dir, required_days=5)
    assert audit["ready_for_4h_task"] is True
    assert audit["observed_day_count"] == 5
    assert all(item["ready"] for item in audit["run_checks"])


def test_stability_audit_rejects_missing_snapshot() -> None:
    root = Path(tempfile.mkdtemp())
    path = root / "paper.db"
    reports_dir = root / "reports"
    _seed_stability_days(path, reports_dir)
    with connect_db(path) as connection:
        connection.execute("DELETE FROM paper_snapshots WHERE run_id='daily_4'")
    audit = audit_database_stability(path, reports_dir, required_days=5)
    assert audit["ready_for_4h_task"] is False
    assert audit["run_checks"][-1]["snapshot_count"] == 0


def test_4h_batch_never_scans_or_creates_plans() -> None:
    batch_text = (ROOT / "scripts" / "paper_4h_update.bat").read_text(encoding="utf-8").lower()
    runner_text = (ROOT / "scripts" / "run_logged_paper_task.ps1").read_text(encoding="utf-8").lower()
    assert "run_logged_paper_task.ps1" in batch_text
    assert "-mode paper_4h" in batch_text
    assert '@("main.py", "paper", "cycle", "--run-type", "paper_4h_update"' in runner_text
    assert '"main.py", "scan"' not in runner_text
    assert '"add-from-scan"' not in runner_text
    assert "add-content -literalpath $logpath" in runner_text
    assert "-encoding utf8" in runner_text
    assert "exit $exitcode" in runner_text


def test_4h_cycle_updates_existing_plans_without_scanning_or_creating() -> None:
    path = _temp_db()
    init_db(path)
    _seed_scan_and_run(path)
    trade = _trade()
    with connect_db(path) as connection:
        assert _insert_paper_trade(connection, trade, {"stop_loss": 90.0})
        _sync_paper_plan(connection, trade, run_id="run1", payload={"stop_loss": 90.0})

    settings = _settings_for(path)
    output_root = path.parent / "reports"
    settings.output.reports_dir = output_root
    settings.output.obsidian_dir = path.parent / "obsidian"
    original_client = paper_trader_module.BinanceClient
    paper_trader_module.BinanceClient = _FakeBinanceClient
    try:
        run_id, updated, report_paths, dashboard_paths = main_module._run_paper_cycle(
            settings,
            account_name="demo",
            run_type="paper_4h_update",
            no_obsidian=True,
            settings_path=ROOT / "config" / "settings.toml",
        )
    finally:
        paper_trader_module.BinanceClient = original_client

    assert len(updated) == 1
    assert settings.output.obsidian_dir == path.parent / "obsidian"
    assert report_paths[0].name.startswith("paper_4h_update_")
    assert dashboard_paths[0].name.startswith("paper_4h_dashboard_")
    with connect_db(path) as connection:
        run = connection.execute("SELECT run_type, status FROM runs WHERE run_id = ?", (run_id,)).fetchone()
        assert tuple(run) == ("paper_4h_update", "success")
        assert connection.execute("SELECT COUNT(*) FROM market_scans").fetchone()[0] == 1
        assert connection.execute("SELECT COUNT(*) FROM paper_plans").fetchone()[0] == 1
        assert connection.execute("SELECT COUNT(*) FROM paper_snapshots WHERE run_id = ?", (run_id,)).fetchone()[0] == 1
        assert connection.execute("SELECT status FROM paper_plans WHERE plan_id='plan1'").fetchone()[0] == "ENTERED"


if __name__ == "__main__":
    test_database_init_is_idempotent_and_configured()
    test_tracked_run_records_success_and_failure()
    test_run_step_persists_run_id_step_and_lock_error()
    test_state_transition_and_stop_are_monotonic()
    test_summary_and_export_use_structured_tables()
    test_wal_allows_reader_during_write_transaction()
    test_locked_write_waits_then_marks_run_failed()
    test_paper_update_writes_event_plan_and_snapshot_atomically()
    test_plan_failure_rolls_back_atomically_and_next_plan_continues()
    test_scan_and_plan_inherit_run_metadata()
    test_schema_v2_backfills_operational_plan_fields()
    test_add_from_scan_writes_plan_created_once()
    test_unclosed_kline_records_skip_without_state_change()
    test_kline_api_error_is_recorded_and_does_not_fail_run()
    test_structured_event_names_cover_plan_requirements()
    test_report_contains_current_run_events_and_api_delay_count()
    test_structured_tables_remain_operational_without_legacy_rows()
    test_stability_audit_requires_five_complete_consecutive_days()
    test_stability_audit_rejects_missing_snapshot()
    test_4h_batch_never_scans_or_creates_plans()
    test_4h_cycle_updates_existing_plans_without_scanning_or_creating()
    print("test_database=passed")
