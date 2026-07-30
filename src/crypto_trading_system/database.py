from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sqlite3
import subprocess
import uuid


SCHEMA_VERSION = 2
BUSY_TIMEOUT_MS = 30_000
TERMINAL_PLAN_STATUSES = {"CLOSED", "STOPPED", "EXPIRED", "INVALIDATED", "ARCHIVED"}
REQUIRED_OBSERVATION_INDEXES = {
    "idx_runs_type_started",
    "idx_runs_status_started",
    "idx_scan_candidates_symbol",
    "idx_scan_candidates_scan_action",
    "idx_plans_symbol_status",
    "idx_plans_status_updated",
    "idx_event_plan_type",
    "idx_event_type_time",
    "idx_event_run",
    "idx_snapshot_run_plan",
    "idx_snapshot_plan_time",
    "idx_shadow_decision_time",
    "idx_shadow_opportunity_line",
}
REQUIRED_OBSERVATION_TABLES = {
    "runs",
    "market_scans",
    "scan_candidates",
    "paper_plans",
    "paper_events",
    "paper_snapshots",
    "paper_shadow_decisions",
}
OBSERVATION_UTC_COLUMNS = {
    "schema_metadata": ("updated_at",),
    "runs": ("started_at", "finished_at", "created_at"),
    "market_scans": ("scan_time", "created_at"),
    "scan_candidates": ("created_at",),
    "paper_plans": ("created_at", "updated_at", "closed_at", "entered_at_utc", "tp1_hit_at_utc"),
    "paper_events": ("event_time", "kline_time", "created_at"),
    "paper_snapshots": ("snapshot_time", "created_at"),
    "paper_shadow_decisions": ("decision_time", "kline_time", "created_at"),
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def connect_db(path: Path) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path, timeout=BUSY_TIMEOUT_MS / 1000)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys=ON")
    connection.execute(f"PRAGMA busy_timeout={BUSY_TIMEOUT_MS}")
    connection.execute("PRAGMA synchronous=NORMAL")
    return connection


def _table_columns(connection: sqlite3.Connection, table: str) -> set[str]:
    return {str(row[1]) for row in connection.execute(f"PRAGMA table_info({table})")}


def audit_utc_timestamps(connection: sqlite3.Connection) -> list[dict[str, object]]:
    errors: list[dict[str, object]] = []
    for table, columns in OBSERVATION_UTC_COLUMNS.items():
        available = _table_columns(connection, table)
        for column in columns:
            if column not in available:
                continue
            rows = connection.execute(
                f'SELECT rowid, "{column}" FROM "{table}" WHERE "{column}" IS NOT NULL'
            ).fetchall()
            for row in rows:
                value = str(row[1])
                valid_suffix = value.endswith("Z") or value.endswith("+00:00")
                try:
                    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
                    valid_timezone = parsed.tzinfo is not None and parsed.utcoffset() == timezone.utc.utcoffset(parsed)
                except ValueError:
                    valid_timezone = False
                if not (valid_suffix and valid_timezone):
                    errors.append(
                        {
                            "table": table,
                            "column": column,
                            "rowid": int(row[0]),
                            "value": value,
                        }
                    )
    return errors


def _add_column(connection: sqlite3.Connection, table: str, definition: str) -> None:
    column = definition.split()[0]
    if column not in _table_columns(connection, table):
        connection.execute(f"ALTER TABLE {table} ADD COLUMN {definition}")


def _config_hash(settings_path: Path | None) -> str | None:
    if settings_path is None or not settings_path.exists():
        return None
    return hashlib.sha256(settings_path.read_bytes()).hexdigest()[:16]


def _git_commit(project_root: Path | None) -> str | None:
    if project_root is None:
        return None
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=project_root,
            capture_output=True,
            text=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return result.stdout.strip() or None


def init_observation_db(path: Path) -> None:
    with connect_db(path) as connection:
        connection.execute("PRAGMA journal_mode=WAL")
        connection.execute("PRAGMA synchronous=NORMAL")
        connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS schema_metadata (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL,
                updated_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS runs (
                run_id TEXT PRIMARY KEY,
                run_type TEXT NOT NULL CHECK(run_type IN ('daily_full', 'paper_4h_update', 'manual', 'backfill')),
                started_at TEXT NOT NULL,
                finished_at TEXT,
                status TEXT NOT NULL CHECK(status IN ('running', 'success', 'failed')),
                config_hash TEXT,
                git_commit TEXT,
                log_path TEXT,
                error_message TEXT,
                created_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS market_scans (
                scan_id TEXT PRIMARY KEY,
                run_id TEXT NOT NULL,
                scan_time TEXT NOT NULL,
                market_regime TEXT,
                universe_size INTEGER,
                candidate_count INTEGER,
                buy_candidate_count INTEGER,
                watch_only_count INTEGER,
                risk_off_count INTEGER,
                config_hash TEXT,
                report_path TEXT,
                created_at TEXT NOT NULL,
                FOREIGN KEY(run_id) REFERENCES runs(run_id)
            );

            CREATE TABLE IF NOT EXISTS paper_plans (
                plan_id TEXT PRIMARY KEY,
                account_name TEXT NOT NULL,
                source_scan_id TEXT,
                source_symbol TEXT NOT NULL,
                created_run_id TEXT,
                created_at TEXT NOT NULL,
                symbol TEXT NOT NULL,
                entry_low REAL,
                entry_high REAL,
                stop_initial REAL,
                stop_current REAL,
                tp1 REAL,
                tp2 REAL,
                status TEXT NOT NULL,
                created_reason TEXT,
                market_regime TEXT,
                raw_json TEXT,
                updated_at TEXT NOT NULL,
                closed_at TEXT,
                FOREIGN KEY(source_scan_id) REFERENCES market_scans(scan_id),
                FOREIGN KEY(created_run_id) REFERENCES runs(run_id),
                UNIQUE(account_name, source_scan_id, source_symbol)
            );

            CREATE TABLE IF NOT EXISTS paper_events (
                event_id TEXT PRIMARY KEY,
                plan_id TEXT NOT NULL,
                run_id TEXT NOT NULL,
                event_time TEXT NOT NULL,
                event_type TEXT NOT NULL,
                symbol TEXT NOT NULL,
                price REAL,
                old_status TEXT,
                new_status TEXT,
                old_stop REAL,
                new_stop REAL,
                kline_time TEXT,
                reason TEXT,
                raw_json TEXT,
                created_at TEXT NOT NULL,
                FOREIGN KEY(plan_id) REFERENCES paper_plans(plan_id),
                FOREIGN KEY(run_id) REFERENCES runs(run_id),
                UNIQUE(plan_id, event_type, event_time)
            );

            CREATE TABLE IF NOT EXISTS paper_snapshots (
                snapshot_id TEXT PRIMARY KEY,
                run_id TEXT NOT NULL,
                snapshot_time TEXT NOT NULL,
                plan_id TEXT NOT NULL,
                symbol TEXT NOT NULL,
                status TEXT NOT NULL,
                current_price REAL,
                entry_price REAL,
                stop_current REAL,
                tp1 REAL,
                tp2 REAL,
                tp1_hit INTEGER,
                ema_trailing_active INTEGER,
                ema_stop REAL,
                unrealized_pnl REAL,
                realized_pnl REAL,
                holding_hours REAL,
                raw_json TEXT,
                created_at TEXT NOT NULL,
                FOREIGN KEY(run_id) REFERENCES runs(run_id),
                FOREIGN KEY(plan_id) REFERENCES paper_plans(plan_id),
                UNIQUE(run_id, plan_id)
            );

            CREATE TABLE IF NOT EXISTS paper_shadow_decisions (
                decision_id TEXT PRIMARY KEY,
                run_id TEXT,
                account_name TEXT NOT NULL,
                opportunity_id TEXT NOT NULL,
                plan_id TEXT,
                symbol TEXT NOT NULL,
                decision_time TEXT NOT NULL,
                kline_time TEXT,
                line_name TEXT NOT NULL,
                controls_paper INTEGER NOT NULL DEFAULT 0,
                decision TEXT NOT NULL,
                accepted INTEGER NOT NULL,
                reject_reason TEXT,
                reference_baseline_decision TEXT,
                atr_reclaim_0_35_decision TEXT,
                research_incumbent_decision TEXT,
                current_price REAL,
                last_4h_close REAL,
                entry_high REAL,
                atr_4h REAL,
                reclaim_margin_atr REAL,
                active_positions INTEGER,
                max_active_positions INTEGER,
                capacity_state TEXT,
                direct_filter_contribution_r REAL,
                path_capacity_contribution_r REAL,
                raw_json TEXT,
                created_at TEXT NOT NULL,
                FOREIGN KEY(plan_id) REFERENCES paper_plans(plan_id),
                FOREIGN KEY(run_id) REFERENCES runs(run_id),
                UNIQUE(opportunity_id, line_name, decision_time, kline_time)
            );

            CREATE INDEX IF NOT EXISTS idx_runs_type_started ON runs(run_type, started_at);
            CREATE INDEX IF NOT EXISTS idx_runs_status_started ON runs(status, started_at);
            CREATE INDEX IF NOT EXISTS idx_plans_symbol_status ON paper_plans(symbol, status);
            CREATE INDEX IF NOT EXISTS idx_plans_status_updated ON paper_plans(status, updated_at);
            CREATE INDEX IF NOT EXISTS idx_event_plan_type ON paper_events(plan_id, event_type);
            CREATE INDEX IF NOT EXISTS idx_event_type_time ON paper_events(event_type, event_time);
            CREATE INDEX IF NOT EXISTS idx_event_run ON paper_events(run_id);
            CREATE INDEX IF NOT EXISTS idx_snapshot_run_plan ON paper_snapshots(run_id, plan_id);
            CREATE INDEX IF NOT EXISTS idx_snapshot_plan_time ON paper_snapshots(plan_id, snapshot_time);
            CREATE INDEX IF NOT EXISTS idx_shadow_decision_time ON paper_shadow_decisions(decision_time);
            CREATE INDEX IF NOT EXISTS idx_shadow_opportunity_line ON paper_shadow_decisions(opportunity_id, line_name);
            """
        )
        scan_columns = [
            "action TEXT",
            "price REAL",
            "volume REAL",
            "market_regime TEXT",
            "entry_low REAL",
            "entry_high REAL",
            "stop REAL",
            "tp1 REAL",
            "tp2 REAL",
            "reason TEXT",
            "raw_json TEXT",
            "created_at TEXT",
        ]
        for definition in scan_columns:
            _add_column(connection, "scan_candidates", definition)
        plan_columns = [
            "source_rank INTEGER",
            "base_asset TEXT",
            "setup TEXT",
            "verdict TEXT",
            "planned_entry_mid REAL",
            "risk_reward_1 REAL",
            "risk_reward_2 REAL",
            "account_equity REAL",
            "risk_per_trade_pct REAL",
            "cash_risk REAL",
            "quantity REAL",
            "entry_price REAL",
            "entered_at_utc TEXT",
            "tp1_hit_at_utc TEXT",
            "exit_price REAL",
            "realized_pnl REAL NOT NULL DEFAULT 0",
            "unrealized_pnl REAL NOT NULL DEFAULT 0",
            "last_price REAL",
            "notes TEXT NOT NULL DEFAULT ''",
            "tp1_trailing_ema_stop_active INTEGER NOT NULL DEFAULT 0",
        ]
        for definition in plan_columns:
            _add_column(connection, "paper_plans", definition)
        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_scan_candidates_symbol ON scan_candidates(symbol)"
        )
        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_scan_candidates_scan_action ON scan_candidates(scan_id, action)"
        )
        connection.execute(
            "CREATE UNIQUE INDEX IF NOT EXISTS idx_scan_candidates_scan_symbol ON scan_candidates(scan_id, symbol)"
        )
        now = utc_now()
        connection.execute(
            """
            INSERT INTO schema_metadata(key, value, updated_at)
            VALUES ('schema_version', ?, ?)
            ON CONFLICT(key) DO UPDATE SET value=excluded.value, updated_at=excluded.updated_at
            """,
            (str(SCHEMA_VERSION), now),
        )
        _backfill_legacy_data(connection)


def _backfill_legacy_data(connection: sqlite3.Connection) -> None:
    now = utc_now()
    legacy_run_id = "backfill_legacy_v1"
    connection.execute(
        """
        INSERT OR IGNORE INTO runs(
            run_id, run_type, started_at, finished_at, status, created_at
        ) VALUES (?, 'backfill', ?, ?, 'success', ?)
        """,
        (legacy_run_id, now, now, now),
    )
    scan_rows = connection.execute("SELECT * FROM scan_runs").fetchall()
    for scan in scan_rows:
        candidates = connection.execute(
            "SELECT payload_json FROM scan_candidates WHERE scan_id = ? ORDER BY rank",
            (scan["scan_id"],),
        ).fetchall()
        payloads = [json.loads(row["payload_json"]) for row in candidates]
        actions = [str(payload.get("action", "")) for payload in payloads]
        risk_off_count = sum(
            1
            for payload in payloads
            if "大盘环境未确认强势" in " ".join(str(item) for item in payload.get("risks", []))
        )
        connection.execute(
            """
            INSERT OR IGNORE INTO market_scans(
                scan_id, run_id, scan_time, candidate_count, buy_candidate_count,
                watch_only_count, risk_off_count, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                scan["scan_id"],
                legacy_run_id,
                scan["timestamp_utc"],
                len(payloads),
                actions.count("BUY_CANDIDATE"),
                actions.count("WATCH_ONLY"),
                risk_off_count,
                scan["timestamp_utc"],
            ),
        )
        for payload in payloads:
            connection.execute(
                """
                UPDATE scan_candidates SET
                    action = COALESCE(action, ?), price = COALESCE(price, ?),
                    volume = COALESCE(volume, ?), entry_low = COALESCE(entry_low, ?),
                    entry_high = COALESCE(entry_high, ?), stop = COALESCE(stop, ?),
                    tp1 = COALESCE(tp1, ?), tp2 = COALESCE(tp2, ?),
                    reason = COALESCE(reason, ?), raw_json = COALESCE(raw_json, payload_json),
                    created_at = COALESCE(created_at, ?)
                WHERE scan_id = ? AND symbol = ?
                """,
                (
                    payload.get("action"), payload.get("price"), payload.get("quote_volume_24h"),
                    payload.get("entry_low"), payload.get("entry_high"), payload.get("stop_loss"),
                    payload.get("take_profit_1"), payload.get("take_profit_2"), payload.get("setup"),
                    scan["timestamp_utc"], scan["scan_id"], payload.get("symbol"),
                ),
            )
    trade_rows = connection.execute("SELECT * FROM paper_trades").fetchall()
    for trade in trade_rows:
        payload = json.loads(trade["payload_json"])
        connection.execute(
            """
            INSERT OR IGNORE INTO paper_plans(
                plan_id, account_name, source_scan_id, source_symbol, created_run_id,
                created_at, symbol, entry_low, entry_high, stop_initial, stop_current,
                tp1, tp2, status, created_reason, raw_json, updated_at, closed_at,
                source_rank, base_asset, setup, verdict, planned_entry_mid,
                risk_reward_1, risk_reward_2, account_equity, risk_per_trade_pct,
                cash_risk, quantity, entry_price, entered_at_utc, tp1_hit_at_utc,
                exit_price, realized_pnl, unrealized_pnl, last_price, notes,
                tp1_trailing_ema_stop_active
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                trade["paper_trade_id"], trade["account_name"], trade["source_scan_id"],
                trade["symbol"], legacy_run_id, trade["created_at_utc"], trade["symbol"],
                trade["entry_low"], trade["entry_high"],
                payload.get("stop_loss", trade["stop_loss"]),
                trade["stop_loss"], trade["take_profit_1"], trade["take_profit_2"],
                trade["status"], trade["notes"], trade["payload_json"],
                trade["updated_at_utc"], trade["closed_at_utc"],
                trade["source_rank"], trade["base_asset"], trade["setup"], trade["verdict"],
                trade["planned_entry_mid"], trade["risk_reward_1"], trade["risk_reward_2"],
                trade["account_equity"], trade["risk_per_trade_pct"], trade["cash_risk"],
                trade["quantity"], trade["entry_price"], trade["entered_at_utc"],
                trade["tp1_hit_at_utc"], trade["exit_price"], trade["realized_pnl"],
                trade["unrealized_pnl"], trade["last_price"], trade["notes"],
                trade["tp1_trailing_ema_stop_active"],
            ),
        )
        connection.execute(
            """
            UPDATE paper_plans SET
                source_rank=?,
                base_asset=?,
                setup=?,
                verdict=?,
                planned_entry_mid=?,
                risk_reward_1=?,
                risk_reward_2=?,
                account_equity=?,
                risk_per_trade_pct=?,
                cash_risk=?,
                quantity=?,
                entry_price=?,
                entered_at_utc=?,
                tp1_hit_at_utc=?,
                exit_price=?,
                realized_pnl=?,
                unrealized_pnl=?,
                last_price=?,
                notes=?,
                tp1_trailing_ema_stop_active=?
            WHERE plan_id=?
            """,
            (
                trade["source_rank"], trade["base_asset"], trade["setup"], trade["verdict"],
                trade["planned_entry_mid"], trade["risk_reward_1"], trade["risk_reward_2"],
                trade["account_equity"], trade["risk_per_trade_pct"], trade["cash_risk"],
                trade["quantity"], trade["entry_price"], trade["entered_at_utc"],
                trade["tp1_hit_at_utc"], trade["exit_price"], trade["realized_pnl"],
                trade["unrealized_pnl"], trade["last_price"], trade["notes"],
                trade["tp1_trailing_ema_stop_active"], trade["paper_trade_id"],
            ),
        )
    event_rows = connection.execute("SELECT * FROM paper_trade_events").fetchall()
    for event in event_rows:
        connection.execute(
            """
            INSERT OR IGNORE INTO paper_events(
                event_id, plan_id, run_id, event_time, event_type, symbol, price,
                reason, raw_json, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                event["event_id"], event["paper_trade_id"], legacy_run_id,
                event["event_time_utc"], event["event_type"], event["symbol"],
                event["price"], event["message"], json.dumps(dict(event), ensure_ascii=False),
                event["event_time_utc"],
            ),
        )


def start_run(
    path: Path,
    run_type: str,
    *,
    settings_path: Path | None = None,
    project_root: Path | None = None,
    log_path: Path | None = None,
) -> str:
    init_observation_db(path)
    now = utc_now()
    run_id = f"{now.replace('-', '').replace(':', '').replace('T', '_').replace('Z', '')}_{uuid.uuid4().hex[:8]}"
    with connect_db(path) as connection:
        connection.execute(
            """
            INSERT INTO runs(
                run_id, run_type, started_at, status, config_hash, git_commit, log_path, created_at
            ) VALUES (?, ?, ?, 'running', ?, ?, ?, ?)
            """,
            (
                run_id,
                run_type,
                now,
                _config_hash(settings_path),
                _git_commit(project_root),
                None if log_path is None else str(log_path),
                now,
            ),
        )
    return run_id


def finish_run(path: Path, run_id: str, *, success: bool, error_message: str | None = None) -> None:
    with connect_db(path) as connection:
        connection.execute(
            """
            UPDATE runs
            SET finished_at = ?, status = ?, error_message = ?
            WHERE run_id = ? AND status = 'running'
            """,
            (utc_now(), "success" if success else "failed", error_message, run_id),
        )


def mark_run_failed(path: Path, run_id: str, *, reason: str) -> dict:
    init_observation_db(path)
    if not reason.strip():
        raise ValueError("reason is required")
    with connect_db(path) as connection:
        existing = connection.execute("SELECT * FROM runs WHERE run_id = ?", (run_id,)).fetchone()
        if existing is None:
            raise ValueError(f"run not found: {run_id}")
        if existing["status"] != "running":
            raise ValueError(f"run is not running: {run_id} status={existing['status']}")
    finish_run(path, run_id, success=False, error_message=reason.strip())
    with connect_db(path) as connection:
        updated = connection.execute("SELECT * FROM runs WHERE run_id = ?", (run_id,)).fetchone()
    return dict(updated)


@contextmanager
def tracked_run(
    path: Path,
    run_type: str,
    *,
    settings_path: Path | None = None,
    project_root: Path | None = None,
    log_path: Path | None = None,
):
    run_id = start_run(
        path,
        run_type,
        settings_path=settings_path,
        project_root=project_root,
        log_path=log_path,
    )
    try:
        yield run_id
    except Exception as exc:
        finish_run(path, run_id, success=False, error_message=f"{type(exc).__name__}: {exc}")
        raise
    else:
        finish_run(path, run_id, success=True)


def database_status(path: Path) -> dict:
    init_observation_db(path)
    with connect_db(path) as connection:
        schema_row = connection.execute(
            "SELECT value FROM schema_metadata WHERE key = 'schema_version'"
        ).fetchone()
        tables = {
            str(row[0])
            for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table'")
        }
        latest_run = connection.execute(
            "SELECT * FROM runs ORDER BY started_at DESC LIMIT 1"
        ).fetchone()
        latest_failed = connection.execute(
            "SELECT * FROM runs WHERE status='failed' ORDER BY started_at DESC LIMIT 1"
        ).fetchone()
        open_plans = connection.execute(
            "SELECT COUNT(*) FROM paper_plans WHERE status NOT IN ('CLOSED','STOPPED','EXPIRED','INVALIDATED','ARCHIVED')"
        ).fetchone()[0]
        journal_mode = connection.execute("PRAGMA journal_mode").fetchone()[0]
        synchronous = connection.execute("PRAGMA synchronous").fetchone()[0]
        foreign_keys = connection.execute("PRAGMA foreign_keys").fetchone()[0]
        busy_timeout = connection.execute("PRAGMA busy_timeout").fetchone()[0]
        foreign_key_errors = [tuple(row) for row in connection.execute("PRAGMA foreign_key_check").fetchall()]
        utc_timestamp_errors = audit_utc_timestamps(connection)
        indexes = {
            str(row[0])
            for row in connection.execute(
                "SELECT name FROM sqlite_master WHERE type='index' AND name NOT LIKE 'sqlite_%'"
            ).fetchall()
        }
        missing_indexes = sorted(REQUIRED_OBSERVATION_INDEXES - indexes)
    return {
        "database_path": str(path.resolve()),
        "schema_version": None if schema_row is None else schema_row[0],
        "journal_mode": journal_mode,
        "synchronous": synchronous,
        "foreign_keys": foreign_keys,
        "busy_timeout_ms": busy_timeout,
        "foreign_key_errors": foreign_key_errors,
        "utc_timestamps_ok": not utc_timestamp_errors,
        "utc_timestamp_errors": utc_timestamp_errors,
        "indexes_ok": not missing_indexes,
        "missing_indexes": missing_indexes,
        "tables_ok": REQUIRED_OBSERVATION_TABLES.issubset(tables),
        "missing_tables": sorted(REQUIRED_OBSERVATION_TABLES - tables),
        "latest_run": None if latest_run is None else dict(latest_run),
        "latest_failed_run": None if latest_failed is None else dict(latest_failed),
        "open_plan_count": open_plans,
    }
