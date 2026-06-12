from __future__ import annotations

import csv
from datetime import datetime, timedelta, timezone
from pathlib import Path

from .database import connect_db


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
