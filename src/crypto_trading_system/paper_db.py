from __future__ import annotations

import csv
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

from .database import connect_db


def audit_database_stability(path: Path, reports_dir: Path, required_days: int = 5) -> dict:
    beijing = ZoneInfo("Asia/Shanghai")
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

        daily_by_date: dict[str, dict] = {}
        for run in runs:
            started = datetime.fromisoformat(str(run["started_at"]).replace("Z", "+00:00"))
            date_text = started.astimezone(beijing).strftime("%Y-%m-%d")
            daily_by_date.setdefault(date_text, run)
        selected_dates = sorted(daily_by_date, reverse=True)[:required_days]
        selected = [daily_by_date[date_text] for date_text in selected_dates]

        run_checks = []
        for run in sorted(selected, key=lambda item: item["started_at"]):
            run_id = str(run["run_id"])
            scan_count = int(
                connection.execute("SELECT COUNT(*) FROM market_scans WHERE run_id = ?", (run_id,)).fetchone()[0]
            )
            snapshot_count = int(
                connection.execute("SELECT COUNT(*) FROM paper_snapshots WHERE run_id = ?", (run_id,)).fetchone()[0]
            )
            started = datetime.fromisoformat(str(run["started_at"]).replace("Z", "+00:00"))
            date_text = started.astimezone(beijing).strftime("%Y-%m-%d")
            report_dir = reports_dir / date_text
            report_files = list(report_dir.glob("*.md")) if report_dir.exists() else []
            run_report_names = []
            for report in report_files:
                try:
                    if run_id in report.read_text(encoding="utf-8"):
                        run_report_names.append(report.name)
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
                    "scan_count": scan_count,
                    "snapshot_count": snapshot_count,
                    "database_locked": "database is locked" in error_text,
                    "market_scan_report": has_scan_report,
                    "paper_report": has_paper_report,
                    "observation_dashboard": has_dashboard,
                    "ready": (
                        run["status"] == "success"
                        and scan_count == 1
                        and snapshot_count > 0
                        and "database is locked" not in error_text
                        and has_scan_report
                        and has_paper_report
                        and has_dashboard
                    ),
                }
            )

    consecutive = False
    if len(selected_dates) == required_days:
        date_values = [datetime.strptime(value, "%Y-%m-%d").date() for value in sorted(selected_dates)]
        consecutive = all((right - left).days == 1 for left, right in zip(date_values, date_values[1:]))
    ready = (
        len(selected_dates) == required_days
        and consecutive
        and all(item["ready"] for item in run_checks)
        and duplicate_plans == 0
        and duplicate_events == 0
        and not foreign_key_errors
    )
    return {
        "required_days": required_days,
        "observed_daily_dates": sorted(selected_dates),
        "observed_day_count": len(selected_dates),
        "consecutive_days": consecutive,
        "run_checks": run_checks,
        "duplicate_plan_groups": duplicate_plans,
        "duplicate_event_groups": duplicate_events,
        "foreign_key_errors": foreign_key_errors,
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
    reclaim_summary = {"total_plans": len(reclaim_rows), "later_entered": 0, "failed_or_invalidated": 0, "still_waiting": 0}
    for row in reclaim_rows:
        if int(row["entered_count"] or 0) > 0:
            reclaim_summary["later_entered"] += 1
        elif row["status"] in {"STOPPED", "INVALIDATED", "EXPIRED", "ARCHIVED"}:
            reclaim_summary["failed_or_invalidated"] += 1
        else:
            reclaim_summary["still_waiting"] += 1
    return {
        "recent_runs": runs,
        "failed_runs": failed_runs,
        "open_plans": open_plans,
        "plan_status_counts": status_counts,
        "event_counts": event_counts,
        "reclaim_summary": reclaim_summary,
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
