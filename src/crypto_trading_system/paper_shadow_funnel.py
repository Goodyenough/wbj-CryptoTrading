from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import sqlite3
from typing import Any

from .config import Settings
from .database import connect_db, utc_now
from .paper_trader import CLOSED_STATUSES, OPEN_STATUSES
from .report_versions import next_report_version, versioned_markdown_filename


BEIJING = timezone(timedelta(hours=8), name="CST")
ALLOWED_VERDICTS = {
    "expected_low_frequency",
    "pipeline_loss",
    "lifecycle_blocked",
    "execution_observability_gap",
    "mixed_causes",
    "insufficient_observation_coverage",
}


def _parse_time(value: object) -> datetime | None:
    if value is None:
        return None
    try:
        text = str(value).replace("Z", "+00:00")
        parsed = datetime.fromisoformat(text)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    except (TypeError, ValueError):
        return None


def _in_window(value: object, start: datetime, end: datetime) -> bool:
    parsed = _parse_time(value)
    return parsed is not None and start <= parsed < end


def _row_dict(row: sqlite3.Row) -> dict[str, Any]:
    return {str(key): row[key] for key in row.keys()}


def _reconstructed_event(
    *,
    event_key: str,
    run_id: str | None,
    account_name: str,
    scan_id: str | None,
    symbol: str | None,
    source_rank: int | None,
    observation_id: str | None,
    plan_id: str | None,
    event_time: str,
    stage: str,
    event_type: str,
    reason_code: str | None,
    old_status: str | None = None,
    new_status: str | None = None,
    raw_json: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "event_id": f"reconstructed:{event_key}",
        "event_key": event_key,
        "run_id": run_id,
        "account_name": account_name,
        "scan_id": scan_id,
        "symbol": symbol,
        "source_rank": source_rank,
        "observation_id": observation_id,
        "plan_id": plan_id,
        "event_time": event_time,
        "stage": stage,
        "event_type": event_type,
        "reason_code": reason_code,
        "old_status": old_status,
        "new_status": new_status,
        "raw_json": json.dumps(
            {"observation_source": "reconstructed_from_existing_data", **(raw_json or {})},
            ensure_ascii=False,
            sort_keys=True,
        ),
        "created_at": event_time,
        "observation_source": "reconstructed_from_existing_data",
    }


def _actual_events(
    connection: sqlite3.Connection,
    account: str,
    start: datetime,
    end: datetime,
) -> list[dict[str, Any]]:
    rows = connection.execute(
        """
        SELECT * FROM paper_shadow_funnel_events
        WHERE account_name = ? AND event_time >= ? AND event_time < ?
        ORDER BY event_time, event_id
        """,
        (account, start.isoformat().replace("+00:00", "Z"), end.isoformat().replace("+00:00", "Z")),
    ).fetchall()
    result = [_row_dict(row) for row in rows]
    for row in result:
        row["observation_source"] = "instrumented"
    return result


def _reconstructed_events(
    connection: sqlite3.Connection,
    account: str,
    start: datetime,
    end: datetime,
) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    observations = connection.execute(
        """
        SELECT * FROM paper_shadow_candidate_observations
        WHERE account_name = ?
        ORDER BY scan_time, source_rank
        """,
        (account,),
    ).fetchall()
    plans = connection.execute(
        """
        SELECT * FROM paper_plans
        WHERE account_name = ?
        ORDER BY created_at, plan_id
        """,
        (account,),
    ).fetchall()
    paper_events = connection.execute(
        """
        SELECT e.*, p.account_name, p.source_scan_id, p.source_rank
        FROM paper_events e
        JOIN paper_plans p ON p.plan_id = e.plan_id
        WHERE p.account_name = ?
        ORDER BY e.event_time, e.event_id
        """,
        (account,),
    ).fetchall()

    actual_keys = {
        str(row["event_key"])
        for row in connection.execute(
            "SELECT event_key FROM paper_shadow_funnel_events WHERE account_name = ?",
            (account,),
        ).fetchall()
    }

    for row in observations:
        if _in_window(row["scan_time"], start, end):
            key = f"candidate_observed:{account}:{row['scan_id']}:{row['symbol']}"
            if key not in actual_keys:
                events.append(
                    _reconstructed_event(
                        event_key=key,
                        run_id=row["run_id"],
                        account_name=account,
                        scan_id=row["scan_id"],
                        symbol=row["symbol"],
                        source_rank=row["source_rank"],
                        observation_id=row["observation_id"],
                        plan_id=None,
                        event_time=str(row["scan_time"]),
                        stage="candidate_observed",
                        event_type="CANDIDATE_OBSERVED",
                        reason_code="candidate_recorded",
                        raw_json={"scanner_action": row["scanner_action"]},
                    )
                )

    for row in plans:
        plan_time = row["created_at"]
        if _in_window(plan_time, start, end):
            key = f"plan_created:{row['plan_id']}"
            if key not in actual_keys:
                events.append(
                    _reconstructed_event(
                        event_key=key,
                        run_id=row["created_run_id"],
                        account_name=account,
                        scan_id=row["source_scan_id"],
                        symbol=row["symbol"],
                        source_rank=row["source_rank"],
                        observation_id=None,
                        plan_id=row["plan_id"],
                        event_time=str(plan_time),
                        stage="plan_created",
                        event_type="PLAN_CREATED",
                        reason_code="existing_plan_row",
                        new_status="WATCHING",
                    )
                )

    for row in paper_events:
        event_time = row["event_time"]
        if not _in_window(event_time, start, end):
            continue
        event_type = str(row["event_type"])
        if event_type == "API_DELAY_SKIPPED":
            reason = str(row["reason"] or "").lower()
            reason_code = "ticker_error" if "ticker" in reason else "kline_error"
            stage = "plan_update_skipped"
            key = f"reconstructed:paper-event:{row['event_id']}"
        elif event_type == "ARCHIVED":
            reason_code = "newer_same_symbol_watching_plan"
            stage = "plan_archived_by_replacement"
            key = f"reconstructed:paper-event:{row['event_id']}"
        elif row["old_status"] != row["new_status"]:
            reason_code = event_type.lower()
            stage = "terminal_reached" if str(row["new_status"]) in CLOSED_STATUSES else "state_transition"
            key = f"reconstructed:paper-event:{row['event_id']}"
        else:
            continue
        events.append(
            _reconstructed_event(
                event_key=key,
                run_id=row["run_id"],
                account_name=account,
                scan_id=row["source_scan_id"],
                symbol=row["symbol"],
                source_rank=row["source_rank"],
                observation_id=None,
                plan_id=row["plan_id"],
                event_time=str(event_time),
                stage=stage,
                event_type=event_type,
                reason_code=reason_code,
                old_status=row["old_status"],
                new_status=row["new_status"],
                raw_json={"paper_event_id": row["event_id"], "reason": row["reason"]},
            )
        )
    return events


def _successful_run_counts(connection: sqlite3.Connection, start: datetime, end: datetime) -> dict[str, Any]:
    rows = connection.execute(
        """
        SELECT run_type, status, started_at FROM runs
        WHERE started_at >= ? AND started_at < ?
        ORDER BY started_at
        """,
        (start.isoformat().replace("+00:00", "Z"), end.isoformat().replace("+00:00", "Z")),
    ).fetchall()
    successes = Counter(str(row["run_type"]) for row in rows if row["status"] == "success")
    daily_dates = {
        datetime.fromisoformat(str(row["started_at"]).replace("Z", "+00:00"))
        .astimezone(BEIJING)
        .strftime("%Y-%m-%d")
        for row in rows
        if row["run_type"] == "daily_full" and row["status"] == "success"
    }
    return {
        "daily_success_runs": successes["daily_full"],
        "paper_4h_success_runs": successes["paper_4h_update"],
        "daily_success_dates": sorted(daily_dates),
        "failed_runs": sum(1 for row in rows if row["status"] == "failed"),
        "total_runs": len(rows),
    }


def build_shadow_funnel_audit(
    settings: Settings,
    *,
    account_name: str | None = None,
    days: int = 30,
    now: datetime | None = None,
) -> dict[str, Any]:
    if days < 1:
        raise ValueError("days must be >= 1")
    account = account_name or settings.paper.account_name
    end = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    start = end - timedelta(days=days)
    with connect_db(settings.output.database_path) as connection:
        connection.row_factory = sqlite3.Row
        events = _actual_events(connection, account, start, end)
        events.extend(_reconstructed_events(connection, account, start, end))
        events.sort(key=lambda row: (str(row["event_time"]), str(row["event_id"])))
        run_counts = _successful_run_counts(connection, start, end)
        observations = connection.execute(
            "SELECT * FROM paper_shadow_candidate_observations WHERE account_name = ?",
            (account,),
        ).fetchall()
        plans = connection.execute(
            "SELECT * FROM paper_plans WHERE account_name = ? ORDER BY created_at, plan_id",
            (account,),
        ).fetchall()
        decisions = connection.execute(
            "SELECT * FROM paper_shadow_decisions WHERE account_name = ? ORDER BY decision_time, opportunity_id",
            (account,),
        ).fetchall()
        outcomes = connection.execute(
            "SELECT * FROM paper_shadow_counterfactual_outcomes WHERE account_name = ?",
            (account,),
        ).fetchall()

    observations_window = [row for row in observations if _in_window(row["scan_time"], start, end)]
    plans_window = [row for row in plans if _in_window(row["created_at"], start, end)]
    decisions_window = [row for row in decisions if _in_window(row["decision_time"], start, end)]
    window_plan_ids_touched = {
        str(row["plan_id"])
        for row in events
        if row["plan_id"] is not None
        and _in_window(row["event_time"], start, end)
    }
    existing_plans_at_window_start = [
        row for row in plans
        if (_parse_time(row["created_at"]) or end) < start
        and str(row["status"]) in OPEN_STATUSES | CLOSED_STATUSES
    ]
    plan_ids_with_decisions = {str(row["plan_id"]) for row in decisions_window if row["plan_id"] is not None}
    terminal_plans = [
        row for row in plans
        if str(row["status"]) in CLOSED_STATUSES
        and _in_window(row["closed_at"] or row["updated_at"], start, end)
    ]
    open_plans = [row for row in plans if str(row["status"]) in OPEN_STATUSES]

    event_counts = Counter(str(row["stage"]) for row in events)
    event_types = Counter(str(row["event_type"]) for row in events)
    reason_counts = Counter(
        str(row["reason_code"] or "unknown")
        for row in events
        if str(row["stage"]) == "plan_update_skipped"
    )
    by_day: dict[str, Counter[str]] = defaultdict(Counter)
    by_symbol: dict[str, Counter[str]] = defaultdict(Counter)
    by_rank: dict[str, Counter[str]] = defaultdict(Counter)
    for row in events:
        parsed = _parse_time(row["event_time"])
        day = parsed.astimezone(BEIJING).strftime("%Y-%m-%d") if parsed else "unknown"
        symbol = str(row["symbol"] or "unknown")
        rank = str(row["source_rank"] if row["source_rank"] is not None else "unknown")
        by_day[day][str(row["stage"])] += 1
        by_symbol[symbol][str(row["stage"])] += 1
        by_rank[rank][str(row["stage"])] += 1

    plan_status_by_id = {str(row["plan_id"]): str(row["status"]) for row in plans}
    orphan_decisions = [
        row for row in decisions_window
        if row["plan_id"] is not None and str(row["plan_id"]) not in plan_status_by_id
    ]
    archived_plans = {
        str(row["plan_id"])
        for row in events
        if str(row["stage"]) == "plan_archived_by_replacement" and row["plan_id"]
    }
    evaluated_plans = {
        str(row["plan_id"])
        for row in events
        if str(row["stage"]) in {"plan_update_evaluated", "plan_update_skipped"} and row["plan_id"]
    }
    archived_without_entry_eval = [
        plan_id for plan_id in archived_plans
        if plan_id not in evaluated_plans
    ]
    terminal_outcome_pairs = {
        (str(row["symbol"]), str(row["line_name"]))
        for row in outcomes
        if int(row["right_censored"] or 1) == 0
    }
    terminal_outcome_by_observation = {
        str(row["observation_id"])
        for row in outcomes
        if int(row["right_censored"] or 1) == 0
    }
    observation_by_scan_symbol = {
        (str(row["scan_id"]), str(row["symbol"])): str(row["observation_id"])
        for row in observations
    }
    observation_by_id = {
        str(row["observation_id"]): row
        for row in observations
    }
    terminal_plans_without_shadow = []
    for plan in terminal_plans:
        observation_id = observation_by_scan_symbol.get((str(plan["source_scan_id"]), str(plan["symbol"])))
        if observation_id is None or observation_id not in terminal_outcome_by_observation:
            terminal_plans_without_shadow.append(str(plan["plan_id"]))
    candidate_terminal_without_plan_terminal = []
    for outcome in outcomes:
        if int(outcome["right_censored"] or 1) != 0:
            continue
        observation = observation_by_id.get(str(outcome["observation_id"]))
        if observation is None:
            candidate_terminal_without_plan_terminal.append(str(outcome["outcome_id"]))
            continue
        matching_plans = [
            plan for plan in plans
            if str(plan["symbol"]) == str(observation["symbol"])
            and str(plan["source_scan_id"]) == str(observation["scan_id"])
            and str(plan["status"]) in CLOSED_STATUSES
        ]
        if not matching_plans:
            candidate_terminal_without_plan_terminal.append(str(outcome["outcome_id"]))

    coverage_ok = (
        days >= 7
        and len(run_counts["daily_success_dates"]) >= 5
        and run_counts["paper_4h_success_runs"] >= 20
    )
    pipeline_signals = bool(orphan_decisions or terminal_plans_without_shadow)
    lifecycle_signals = bool(archived_without_entry_eval or (open_plans and not evaluated_plans))
    execution_signals = bool(
        reason_counts
        or run_counts["failed_runs"]
        or run_counts["paper_4h_success_runs"] < 20
    )
    if not coverage_ok:
        verdict = "insufficient_observation_coverage"
    else:
        active_causes = sum(bool(item) for item in (pipeline_signals, lifecycle_signals, execution_signals))
        if active_causes >= 2:
            verdict = "mixed_causes"
        elif pipeline_signals:
            verdict = "pipeline_loss"
        elif lifecycle_signals:
            verdict = "lifecycle_blocked"
        elif execution_signals:
            verdict = "execution_observability_gap"
        else:
            verdict = "expected_low_frequency"
    reason = {
        "insufficient_observation_coverage": "The requested window lacks the minimum daily/4h successful-run coverage.",
        "pipeline_loss": "Existing records contain plan/shadow association or terminal-outcome gaps that require investigation.",
        "lifecycle_blocked": "Plans are being archived before evaluation or remain open without update coverage.",
        "execution_observability_gap": "Run failures or update-skip events indicate incomplete execution observation.",
        "mixed_causes": "Pipeline, lifecycle, and/or execution signals coexist; isolate them before strategy conclusions.",
        "expected_low_frequency": "Observed reductions are explainable by the import and trigger funnel, with no detected linkage or execution gap.",
    }[verdict]

    result = {
        "account_name": account,
        "window": {
            "start_utc": start.isoformat().replace("+00:00", "Z"),
            "end_utc": end.isoformat().replace("+00:00", "Z"),
            "days": days,
        },
        "verdict": verdict,
        "reason": reason,
        "coverage": {
            **run_counts,
            "minimum_days": 7,
            "minimum_daily_success_runs": 5,
            "minimum_4h_success_runs": 20,
            "coverage_ok": coverage_ok,
        },
        "funnel_counts": {
            "candidate_observations": len(observations_window),
            "plan_level_plans_created": len(plans_window),
            "plan_level_plans_touched": len(window_plan_ids_touched),
            "existing_plans_at_window_start": len(existing_plans_at_window_start),
            "plan_linked_decisions": len({str(row["plan_id"]) for row in decisions_window if row["plan_id"]}),
            "mature_terminal_plans": len(terminal_plans),
            "open_plans_current": len(open_plans),
            "candidate_counterfactual_outcomes": len(outcomes),
            "candidate_terminal_counterfactual_outcomes": len(terminal_outcome_by_observation),
            "plan_ids_without_plan_linked_decision": len([row for row in plans_window if str(row["plan_id"]) not in plan_ids_with_decisions]),
            "archived_without_entry_evaluation": len(archived_without_entry_eval),
            "terminal_plans_without_terminal_shadow_outcome": len(terminal_plans_without_shadow),
            "candidate_terminal_without_plan_terminal": len(candidate_terminal_without_plan_terminal),
            "orphan_plan_linked_decisions": len(orphan_decisions),
        },
        "event_counts": dict(sorted(event_counts.items())),
        "event_type_counts": dict(sorted(event_types.items())),
        "plan_update_skip_reasons": dict(sorted(reason_counts.items())),
        "by_day": {key: dict(sorted(value.items())) for key, value in sorted(by_day.items())},
        "by_symbol": {key: dict(sorted(value.items())) for key, value in sorted(by_symbol.items())},
        "by_source_rank": {key: dict(sorted(value.items())) for key, value in sorted(by_rank.items())},
        "signals": {
            "pipeline_loss": pipeline_signals,
            "lifecycle_blocked": lifecycle_signals,
            "execution_observability_gap": execution_signals,
        },
        "open_plan_lifecycles": [
            {
                "plan_id": str(plan["plan_id"]),
                "symbol": str(plan["symbol"]),
                "status": str(plan["status"]),
                "source_scan_id": plan["source_scan_id"],
                "source_rank": plan["source_rank"],
                "created_at": plan["created_at"],
                "updated_at": plan["updated_at"],
                "event_types": sorted({str(row["event_type"]) for row in events if row["plan_id"] == plan["plan_id"]}),
            }
            for plan in open_plans
        ],
        "diagnostic_event_count": len(events),
        "reconstructed_event_count": sum(
            1 for row in events if row.get("observation_source") == "reconstructed_from_existing_data"
        ),
        "limitations": [
            "Historical reconstructed events are diagnostic evidence only and do not alter maturity or reconciliation gates.",
            "Candidate rows are correlated observations, not independent trades.",
            "No strategy configuration or paper state was changed by this audit.",
        ],
    }
    if verdict not in ALLOWED_VERDICTS:
        raise AssertionError(f"Unexpected funnel verdict: {verdict}")
    return result


def render_shadow_funnel_audit(audit: dict[str, Any], *, json_filename: str) -> str:
    counts = audit["funnel_counts"]
    coverage = audit["coverage"]
    lines = [
        "# Paper Shadow Funnel Audit",
        "",
        "## 目标",
        "",
        "- 本报告只诊断 `candidate -> plan -> terminal` 漏斗，不改变策略、paper 状态或 maturity 定义。",
        f"- account: `{audit['account_name']}`",
        f"- window: `{audit['window']['start_utc']}` -> `{audit['window']['end_utc']}`",
        f"- verdict: `{audit['verdict']}`",
        f"- reason: {audit['reason']}",
        "",
        "## 运行覆盖",
        "",
        "| 指标 | 当前 | 最低要求 |",
        "|---|---:|---:|",
        f"| daily success runs | {coverage['daily_success_runs']} | 5 |",
        f"| daily success dates | {len(coverage['daily_success_dates'])} | 5 |",
        f"| paper 4h success runs | {coverage['paper_4h_success_runs']} | 20 |",
        f"| failed runs | {coverage['failed_runs']} | 0（诊断信号） |",
        f"| coverage_ok | `{coverage['coverage_ok']}` | `true` |",
        "",
        "## 漏斗摘要",
        "",
        "| 阶段 | 数量 |",
        "|---|---:|",
        f"| candidate observations | {counts['candidate_observations']} |",
        f"| plan-level plans created in window | {counts['plan_level_plans_created']} |",
        f"| plan-level plans touched in window | {counts['plan_level_plans_touched']} |",
        f"| existing plans at window start | {counts['existing_plans_at_window_start']} |",
        f"| plan-linked decisions | {counts['plan_linked_decisions']} |",
        f"| mature terminal plans | {counts['mature_terminal_plans']} |",
        f"| current open plans | {counts['open_plans_current']} |",
        f"| candidate terminal counterfactual outcomes | {counts['candidate_terminal_counterfactual_outcomes']} |",
        f"| plans without plan-linked decision | {counts['plan_ids_without_plan_linked_decision']} |",
        f"| archived without entry evaluation | {counts['archived_without_entry_evaluation']} |",
        f"| terminal plans without terminal shadow outcome | {counts['terminal_plans_without_terminal_shadow_outcome']} |",
        f"| candidate terminal without plan terminal | {counts['candidate_terminal_without_plan_terminal']} |",
        f"| orphan plan-linked decisions | {counts['orphan_plan_linked_decisions']} |",
        "",
        "## 主要断点",
        "",
        "| 诊断信号 | 是否存在 |",
        "|---|---|",
        f"| pipeline_loss | `{audit['signals']['pipeline_loss']}` |",
        f"| lifecycle_blocked | `{audit['signals']['lifecycle_blocked']}` |",
        f"| execution_observability_gap | `{audit['signals']['execution_observability_gap']}` |",
        "",
        "## 更新跳过原因",
        "",
        "| reason_code | Count |",
        "|---|---:|",
    ]
    if audit["plan_update_skip_reasons"]:
        lines.extend(
            f"| `{key}` | {value} |"
            for key, value in audit["plan_update_skip_reasons"].items()
        )
    else:
        lines.append("| none | 0 |")
    lines.extend(["", "## 按日阶段计数", "", "| 日期 | 阶段计数 |", "|---|---|"])
    for day, values in audit["by_day"].items():
        lines.append(f"| `{day}` | " + ", ".join(f"{key}={value}" for key, value in values.items()) + " |")
    if not audit["by_day"]:
        lines.append("| none | 0 |")
    lines.extend(["", "## 当前开放计划生命周期", "", "| Plan | Symbol | Status | Source scan | Rank | Events |", "|---|---|---|---|---:|---|"])
    for item in audit["open_plan_lifecycles"]:
        lines.append(
            f"| `{item['plan_id']}` | `{item['symbol']}` | `{item['status']}` | `{item['source_scan_id']}` | "
            f"{item['source_rank']} | `{','.join(item['event_types']) or 'none'}` |"
        )
    if not audit["open_plan_lifecycles"]:
        lines.append("| none | n/a | n/a | n/a | n/a | n/a |")
    lines.extend([
        "",
        "## 限制",
        "",
        *[f"- {item}" for item in audit["limitations"]],
        "",
        f"- JSON sidecar: `{json_filename}`",
    ])
    return "\n".join(lines)


def write_shadow_funnel_audit_report(
    settings: Settings,
    *,
    account_name: str | None = None,
    days: int = 30,
    now: datetime | None = None,
    include_obsidian: bool = True,
) -> tuple[dict[str, Any], list[Path], Path]:
    audit = build_shadow_funnel_audit(settings, account_name=account_name, days=days, now=now)
    timestamp = now or datetime.now(timezone.utc)
    date_text = timestamp.astimezone(BEIJING).strftime("%Y-%m-%d")
    report_dir = settings.output.reports_dir / date_text
    obsidian_dir = (
        settings.output.obsidian_dir / "Reports" / date_text
        if include_obsidian and settings.output.obsidian_dir is not None
        else None
    )
    prefix = f"paper_shadow_funnel_audit_{date_text}_{audit['account_name']}"
    version = next_report_version([report_dir, obsidian_dir], prefix)
    markdown_name = versioned_markdown_filename(prefix, version)
    json_name = markdown_name.removesuffix(".md") + ".json"
    report_dir.mkdir(parents=True, exist_ok=True)
    json_path = report_dir / json_name
    json_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding="utf-8")
    markdown = render_shadow_funnel_audit(audit, json_filename=json_name)
    paths = [report_dir / markdown_name]
    paths[0].write_text(markdown, encoding="utf-8")
    if obsidian_dir is not None:
        obsidian_dir.mkdir(parents=True, exist_ok=True)
        (obsidian_dir / markdown_name).write_text(markdown, encoding="utf-8")
    return audit, paths, json_path
