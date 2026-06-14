from __future__ import annotations

import csv
from datetime import datetime, timedelta, timezone
from pathlib import Path
import re
from zoneinfo import ZoneInfo

from .database import audit_utc_timestamps, connect_db


BEIJING_TZ = ZoneInfo("Asia/Shanghai")


def audit_database_stability(path: Path, reports_dir: Path, required_days: int = 5) -> dict:
    beijing = BEIJING_TZ
    with connect_db(path) as connection:
        runs = [
            dict(row)
            for row in connection.execute(
                """
                SELECT * FROM runs
                WHERE run_type = 'daily_full'
                ORDER BY started_at DESC
                """
            ).fetchall()
        ]
        duplicate_plans = int(
            connection.execute(
                """
                SELECT COUNT(*) FROM (
                    SELECT account_name, source_scan_id, source_symbol, COUNT(*) AS count
                    FROM paper_plans
                    GROUP BY account_name, source_scan_id, source_symbol
                    HAVING count > 1
                )
                """
            ).fetchone()[0]
        )
        duplicate_events = int(
            connection.execute(
                """
                SELECT COUNT(*) FROM (
                    SELECT plan_id, event_type, event_time, COUNT(*) AS count
                    FROM paper_events
                    GROUP BY plan_id, event_type, event_time
                    HAVING count > 1
                )
                """
            ).fetchone()[0]
        )
        foreign_key_errors = [dict(row) for row in connection.execute("PRAGMA foreign_key_check").fetchall()]
        utc_timestamp_errors = audit_utc_timestamps(connection)

        daily_runs_by_date: dict[str, list[dict]] = {}
        for run in runs:
            started = datetime.fromisoformat(str(run["started_at"]).replace("Z", "+00:00"))
            date_text = started.astimezone(beijing).strftime("%Y-%m-%d")
            daily_runs_by_date.setdefault(date_text, []).append(run)
        duplicate_daily_run_dates = [
            {
                "date_beijing": date_text,
                "run_count": len(date_runs),
                "runs": [
                    {"run_id": str(run["run_id"]), "status": str(run["status"])}
                    for run in sorted(date_runs, key=lambda item: item["started_at"])
                ],
            }
            for date_text, date_runs in sorted(daily_runs_by_date.items())
            if len(date_runs) > 1
        ]
        daily_by_date = {date_text: date_runs[0] for date_text, date_runs in daily_runs_by_date.items()}
        selected_dates = sorted(daily_by_date, reverse=True)[:required_days]
        selected = [daily_by_date[date_text] for date_text in selected_dates]
        selected_config_hashes = sorted(
            {str(run["config_hash"]) for run in selected if run.get("config_hash")}
        )
        config_hash_errors: list[dict[str, object]] = []
        for run in selected:
            if not run.get("config_hash"):
                config_hash_errors.append(
                    {"run_id": str(run["run_id"]), "error": "missing_run_config_hash"}
                )
        if len(selected_config_hashes) > 1:
            config_hash_errors.append(
                {"error": "config_hash_drift", "observed_hashes": selected_config_hashes}
            )

        run_checks = []
        for run in sorted(selected, key=lambda item: item["started_at"]):
            run_id = str(run["run_id"])
            run_metadata_errors: list[dict[str, object]] = []
            finished_at = run.get("finished_at")
            if not finished_at:
                run_metadata_errors.append({"field": "finished_at", "error": "missing"})
            else:
                started_dt = datetime.fromisoformat(str(run["started_at"]).replace("Z", "+00:00"))
                finished_dt = datetime.fromisoformat(str(finished_at).replace("Z", "+00:00"))
                if finished_dt < started_dt:
                    run_metadata_errors.append(
                        {
                            "field": "finished_at",
                            "error": "before_started_at",
                            "value": str(finished_at),
                        }
                    )
            git_commit = str(run.get("git_commit") or "")
            if not re.fullmatch(r"[0-9a-f]{40}", git_commit):
                run_metadata_errors.append(
                    {"field": "git_commit", "error": "missing_or_invalid", "value": git_commit or None}
                )
            log_path = str(run.get("log_path") or "")
            if not log_path:
                run_metadata_errors.append({"field": "log_path", "error": "missing"})
            elif not Path(log_path).is_file():
                run_metadata_errors.append(
                    {"field": "log_path", "error": "file_not_found", "value": log_path}
                )
            if run["status"] == "success" and run.get("error_message"):
                run_metadata_errors.append(
                    {
                        "field": "error_message",
                        "error": "present_on_success",
                        "value": str(run["error_message"]),
                    }
                )
            scan_count = int(
                connection.execute("SELECT COUNT(*) FROM market_scans WHERE run_id = ?", (run_id,)).fetchone()[0]
            )
            scan_integrity_errors: list[dict[str, object]] = []
            scan_rows = connection.execute(
                """
                SELECT scan_id, candidate_count, buy_candidate_count, watch_only_count, config_hash
                FROM market_scans WHERE run_id = ?
                """,
                (run_id,),
            ).fetchall()
            for scan in scan_rows:
                if scan["config_hash"] != run["config_hash"]:
                    scan_integrity_errors.append(
                        {
                            "scan_id": str(scan["scan_id"]),
                            "field": "config_hash",
                            "declared": scan["config_hash"],
                            "observed": run["config_hash"],
                        }
                    )
                actual = connection.execute(
                    """
                    SELECT COUNT(*) AS candidate_count,
                           SUM(CASE WHEN action='BUY_CANDIDATE' THEN 1 ELSE 0 END) AS buy_candidate_count,
                           SUM(CASE WHEN action='WATCH_ONLY' THEN 1 ELSE 0 END) AS watch_only_count
                    FROM scan_candidates WHERE scan_id = ?
                    """,
                    (scan["scan_id"],),
                ).fetchone()
                for field in ("candidate_count", "buy_candidate_count", "watch_only_count"):
                    declared = int(scan[field] or 0)
                    observed = int(actual[field] or 0)
                    if declared != observed:
                        scan_integrity_errors.append(
                            {
                                "scan_id": str(scan["scan_id"]),
                                "field": field,
                                "declared": declared,
                                "observed": observed,
                            }
                        )
            snapshot_count = int(
                connection.execute("SELECT COUNT(*) FROM paper_snapshots WHERE run_id = ?", (run_id,)).fetchone()[0]
            )
            run_end = str(run.get("finished_at") or run["started_at"])
            expected_snapshot_plan_ids = {
                str(row[0])
                for row in connection.execute(
                    """
                    SELECT plan_id
                    FROM paper_plans
                    WHERE created_at <= ?
                      AND (closed_at IS NULL OR closed_at >= ?)
                      AND plan_id NOT IN (
                          SELECT plan_id FROM paper_events
                          WHERE run_id = ? AND event_type = 'ARCHIVED'
                      )
                    """,
                    (run_end, run["started_at"], run_id),
                ).fetchall()
            }
            snapshot_plan_ids = {
                str(row[0])
                for row in connection.execute(
                    "SELECT plan_id FROM paper_snapshots WHERE run_id = ?",
                    (run_id,),
                ).fetchall()
            }
            missing_snapshot_plan_ids = sorted(expected_snapshot_plan_ids - snapshot_plan_ids)
            started = datetime.fromisoformat(str(run["started_at"]).replace("Z", "+00:00"))
            date_text = started.astimezone(beijing).strftime("%Y-%m-%d")
            report_dir = reports_dir / date_text
            report_files = list(report_dir.glob("*.md")) if report_dir.exists() else []
            run_report_names = []
            report_metadata_errors: list[dict[str, str]] = []
            expected_run_id_line = f"- Run ID：`{run_id}`"
            expected_run_type_line = f"- Run type：`{run['run_type']}`"
            expected_source_line = "- 数据来源：SQLite"
            for report in report_files:
                try:
                    report_text = report.read_text(encoding="utf-8")
                    if expected_run_id_line in report_text:
                        run_report_names.append(report.name)
                        for field, expected in (
                            ("run_type", expected_run_type_line),
                            ("data_source", expected_source_line),
                        ):
                            if expected not in report_text:
                                report_metadata_errors.append(
                                    {"report": report.name, "field": field, "expected": expected}
                                )
                except OSError:
                    continue
            has_scan_report = any(name.startswith("market_scan_") for name in run_report_names)
            has_paper_report = any(name.startswith("paper_report_") for name in run_report_names)
            has_dashboard = any(name.startswith("paper_observation_dashboard_") for name in run_report_names)
            error_text = str(run.get("error_message") or "").lower()
            run_checks.append(
                {
                    "date_beijing": date_text,
                    "run_id": run_id,
                    "status": run["status"],
                    "run_metadata_errors": run_metadata_errors,
                    "scan_count": scan_count,
                    "scan_integrity_errors": scan_integrity_errors,
                    "snapshot_count": snapshot_count,
                    "expected_snapshot_count": len(expected_snapshot_plan_ids),
                    "missing_snapshot_plan_ids": missing_snapshot_plan_ids,
                    "database_locked": "database is locked" in error_text,
                    "market_scan_report": has_scan_report,
                    "paper_report": has_paper_report,
                    "observation_dashboard": has_dashboard,
                    "report_metadata_errors": report_metadata_errors,
                    "ready": (
                        run["status"] == "success"
                        and not run_metadata_errors
                        and scan_count == 1
                        and not scan_integrity_errors
                        and not missing_snapshot_plan_ids
                        and "database is locked" not in error_text
                        and has_scan_report
                        and has_paper_report
                        and has_dashboard
                        and not report_metadata_errors
                    ),
                }
            )

    required_window_complete = len(selected_dates) == required_days
    consecutive = bool(selected_dates)
    if len(selected_dates) > 1:
        date_values = [datetime.strptime(value, "%Y-%m-%d").date() for value in sorted(selected_dates)]
        consecutive = all((right - left).days == 1 for left, right in zip(date_values, date_values[1:]))
    ready = (
        required_window_complete
        and consecutive
        and all(item["ready"] for item in run_checks)
        and duplicate_plans == 0
        and duplicate_events == 0
        and not foreign_key_errors
        and not utc_timestamp_errors
        and not config_hash_errors
        and not duplicate_daily_run_dates
    )
    return {
        "required_days": required_days,
        "observed_daily_dates": sorted(selected_dates),
        "observed_day_count": len(selected_dates),
        "consecutive_days": consecutive,
        "required_window_complete": required_window_complete,
        "run_checks": run_checks,
        "duplicate_plan_groups": duplicate_plans,
        "duplicate_event_groups": duplicate_events,
        "foreign_key_errors": foreign_key_errors,
        "utc_timestamp_errors": utc_timestamp_errors,
        "observed_config_hashes": selected_config_hashes,
        "config_hash_errors": config_hash_errors,
        "duplicate_daily_run_dates": duplicate_daily_run_dates,
        "ready_for_4h_task": ready,
    }


def build_paper_db_summary(path: Path, limit: int = 10) -> dict:
    with connect_db(path) as connection:
        runs = [
            dict(row)
            for row in connection.execute(
                "SELECT * FROM runs ORDER BY started_at DESC LIMIT ?",
                (limit,),
            ).fetchall()
        ]
        failed_runs = [
            dict(row)
            for row in connection.execute(
                "SELECT * FROM runs WHERE status='failed' ORDER BY started_at DESC LIMIT ?",
                (limit,),
            ).fetchall()
        ]
        open_plans = [
            dict(row)
            for row in connection.execute(
                """
                SELECT plan_id, account_name, source_scan_id, symbol, status,
                       entry_low, entry_high, stop_initial, stop_current, tp1, tp2,
                       created_at, updated_at, closed_at
                FROM paper_plans
                WHERE status NOT IN ('CLOSED','STOPPED','EXPIRED','INVALIDATED','ARCHIVED')
                ORDER BY updated_at DESC
                """
            ).fetchall()
        ]
        event_counts = {
            str(row["event_type"]): int(row["count"])
            for row in connection.execute(
                "SELECT event_type, COUNT(*) AS count FROM paper_events GROUP BY event_type"
            ).fetchall()
        }
        status_counts = {
            str(row["status"]): int(row["count"])
            for row in connection.execute(
                "SELECT status, COUNT(*) AS count FROM paper_plans GROUP BY status"
            ).fetchall()
        }
        snapshot_counts = [
            dict(row)
            for row in connection.execute(
                """
                SELECT substr(snapshot_time, 1, 13) AS utc_period, COUNT(*) AS snapshot_count
                FROM paper_snapshots
                GROUP BY substr(snapshot_time, 1, 13)
                ORDER BY utc_period
                """
            ).fetchall()
        ]
        holding_rows = [
            dict(row)
            for row in connection.execute(
                """
                SELECT plan_id, symbol, status, MAX(holding_hours) AS holding_hours
                FROM paper_snapshots
                WHERE holding_hours IS NOT NULL
                GROUP BY plan_id, symbol, status
                ORDER BY holding_hours DESC
                """
            ).fetchall()
        ]
        reclaim_rows = connection.execute(
            """
            SELECT p.plan_id, p.status,
                   SUM(CASE WHEN e.event_type IN ('RECLAIM_PENDING','RECLAIM_PENDING_SET') THEN 1 ELSE 0 END) AS pending_count,
                   SUM(CASE WHEN e.event_type IN ('ENTERED','RECLAIM_CONFIRMED_ENTERED') THEN 1 ELSE 0 END) AS entered_count
            FROM paper_plans p
            JOIN paper_events e ON e.plan_id = p.plan_id
            GROUP BY p.plan_id, p.status
            HAVING pending_count > 0
            """
        ).fetchall()
        scan_totals = connection.execute(
            """
            SELECT COUNT(*) AS scan_count,
                   COALESCE(SUM(candidate_count), 0) AS candidate_count,
                   COALESCE(SUM(buy_candidate_count), 0) AS buy_candidate_count
            FROM market_scans
            """
        ).fetchone()
        plan_count = int(connection.execute("SELECT COUNT(*) FROM paper_plans").fetchone()[0])
        run_type_rows = connection.execute(
            """
            SELECT run_type, status, started_at
            FROM runs
            WHERE run_type IN ('daily_full', 'paper_4h_update')
            ORDER BY started_at
            """
        ).fetchall()
    reclaim_summary = {"total_plans": len(reclaim_rows), "later_entered": 0, "failed_or_invalidated": 0, "still_waiting": 0}
    for row in reclaim_rows:
        if int(row["entered_count"] or 0) > 0:
            reclaim_summary["later_entered"] += 1
        elif row["status"] in {"STOPPED", "INVALIDATED", "EXPIRED", "ARCHIVED"}:
            reclaim_summary["failed_or_invalidated"] += 1
        else:
            reclaim_summary["still_waiting"] += 1
    event_metric_types = {
        "tp1_hit": "TP1_HIT",
        "ema_trailing_activated": "TP1_EMA_TRAILING_ACTIVATED",
        "ema_stop_raised": "TP1_EMA_TRAILING_RAISED",
        "ema_trailing_stopped": "EMA_TRAILING_STOPPED",
        "api_delay_skipped": "API_DELAY_SKIPPED",
    }
    run_type_summary: dict[str, dict] = {}
    for run_type in ("daily_full", "paper_4h_update"):
        matching = [row for row in run_type_rows if row["run_type"] == run_type]
        local_dates = sorted(
            {
                datetime.fromisoformat(str(row["started_at"]).replace("Z", "+00:00"))
                .astimezone(BEIJING_TZ)
                .date()
                .isoformat()
                for row in matching
            }
        )
        run_type_summary[run_type] = {
            "total": len(matching),
            "success": sum(1 for row in matching if row["status"] == "success"),
            "failed": sum(1 for row in matching if row["status"] == "failed"),
            "running": sum(1 for row in matching if row["status"] == "running"),
            "beijing_dates": local_dates,
        }
    return {
        "recent_runs": runs,
        "failed_runs": failed_runs,
        "open_plans": open_plans,
        "plan_status_counts": status_counts,
        "event_counts": event_counts,
        "reclaim_summary": reclaim_summary,
        "observation_totals": {
            "scan_count": int(scan_totals["scan_count"]),
            "candidate_count": int(scan_totals["candidate_count"]),
            "buy_candidate_count": int(scan_totals["buy_candidate_count"]),
            "paper_plan_count": plan_count,
            "reclaim_pending_plan_count": reclaim_summary["total_plans"],
            **{name: int(event_counts.get(event_type, 0)) for name, event_type in event_metric_types.items()},
            "terminal_status_counts": {
                status: int(status_counts.get(status, 0))
                for status in ("CLOSED", "STOPPED", "EXPIRED", "INVALIDATED", "ARCHIVED")
            },
        },
        "run_type_summary": run_type_summary,
        "holding_hours": holding_rows,
        "snapshot_counts_utc_hour": snapshot_counts,
    }


def load_paper_db_events(path: Path, plan_id: str | None = None, limit: int = 200) -> list[dict]:
    sql = "SELECT * FROM paper_events"
    params: list[object] = []
    if plan_id:
        sql += " WHERE plan_id = ?"
        params.append(plan_id)
    sql += " ORDER BY event_time DESC LIMIT ?"
    params.append(limit)
    with connect_db(path) as connection:
        return [dict(row) for row in connection.execute(sql, tuple(params)).fetchall()]


def export_paper_db(path: Path, output_dir: Path) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    beijing = timezone(timedelta(hours=8))
    date_text = datetime.now(beijing).strftime("%Y-%m-%d")
    exports = [
        ("paper_db_summary", "paper_plans", "updated_at"),
        ("paper_events", "paper_events", "event_time"),
        ("paper_snapshots", "paper_snapshots", "snapshot_time"),
    ]
    paths: list[Path] = []
    with connect_db(path) as connection:
        for prefix, table, order_column in exports:
            rows = connection.execute(f"SELECT * FROM {table} ORDER BY {order_column}").fetchall()
            columns = [str(item[0]) for item in connection.execute(f"SELECT * FROM {table} LIMIT 0").description]
            out = output_dir / f"{prefix}_{date_text}.csv"
            with out.open("w", encoding="utf-8-sig", newline="") as handle:
                writer = csv.writer(handle)
                writer.writerow(columns)
                writer.writerows([tuple(row) for row in rows])
            paths.append(out)
    return paths
