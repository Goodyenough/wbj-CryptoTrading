from __future__ import annotations

from pathlib import Path
import sqlite3
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from crypto_trading_system.database import connect_db, database_status, tracked_run
from crypto_trading_system.config import load_settings
from crypto_trading_system.models import PaperTrade
from crypto_trading_system.paper_db import build_paper_db_summary, export_paper_db
from crypto_trading_system import paper_trader as paper_trader_module
from crypto_trading_system.paper_trader import (
    _insert_paper_trade,
    _save_trade_update,
    _sync_paper_plan,
    update_paper_trades,
)
from crypto_trading_system.storage import init_db


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
    assert status["schema_version"] == "1"
    assert status["journal_mode"] == "wal"
    assert status["synchronous"] == 1
    assert status["foreign_keys"] == 1
    assert status["busy_timeout_ms"] == 30_000
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
    summary = build_paper_db_summary(path)
    assert "recent_runs" in summary
    assert "event_counts" in summary
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


class _FakeBinanceClient:
    close_time: int = 1
    close_price: float = 106.0

    def __init__(self, *args, **kwargs) -> None:
        pass

    def ticker_24hr(self) -> list[dict]:
        return [{"symbol": "TESTUSDT", "lastPrice": "103"}]

    def klines(self, symbol: str, interval: str, limit: int) -> list[list]:
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
    finally:
        paper_trader_module.BinanceClient = original_client
        _FakeBinanceClient.close_time = 1
        _FakeBinanceClient.close_price = 106.0
    with connect_db(path) as connection:
        assert connection.execute("SELECT status FROM paper_plans WHERE plan_id='plan1'").fetchone()[0] == "WATCHING"
        assert connection.execute(
            "SELECT COUNT(*) FROM paper_events WHERE event_type='API_DELAY_SKIPPED'"
        ).fetchone()[0] == 1


if __name__ == "__main__":
    test_database_init_is_idempotent_and_configured()
    test_tracked_run_records_success_and_failure()
    test_state_transition_and_stop_are_monotonic()
    test_summary_and_export_use_structured_tables()
    test_wal_allows_reader_during_write_transaction()
    test_paper_update_writes_event_plan_and_snapshot_atomically()
    test_unclosed_kline_records_skip_without_state_change()
    print("test_database=passed")
