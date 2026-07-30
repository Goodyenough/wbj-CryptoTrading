from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import sqlite3

from .config import Settings
from .database import connect_db
from .paper_trader import CLOSED_STATUSES, OPEN_STATUSES
from .report_versions import next_report_version, versioned_markdown_filename


@dataclass(frozen=True)
class ShadowMaturityReview:
    account_name: str
    decision_count: int
    opportunity_count: int
    candidate_only_count: int
    decision_level_count: int
    mature_terminal_count: int
    right_censored_open_count: int
    unknown_plan_count: int
    right_censored_ratio_pct: float
    line_counts: dict[str, int]
    stage_counts: dict[str, int]
    capacity_counts: dict[str, int]
    scanner_action_counts: dict[str, int]
    terminal_status_counts: dict[str, int]
    opportunity_summaries: list[dict[str, object]]
    diagnostics: dict[str, object]
    verdict: str
    reason: str


def _parse_raw_json(value: str | None) -> dict:
    if not value:
        return {}
    try:
        parsed = json.loads(value)
    except json.JSONDecodeError:
        return {}
    return parsed if isinstance(parsed, dict) else {}


def _stage_for_row(row: sqlite3.Row, raw: dict) -> str:
    stage = raw.get("stage")
    if isinstance(stage, str) and stage:
        return stage
    if row["plan_id"] is None:
        return "candidate_level_unknown"
    return "decision_level_unknown"


def _maturity_for_row(row: sqlite3.Row) -> str:
    if row["plan_id"] is None:
        return "candidate_only_no_plan_link"
    plan_status = row["plan_status"]
    if plan_status in CLOSED_STATUSES:
        return "mature_terminal"
    if plan_status in OPEN_STATUSES:
        return "right_censored_open"
    return "unknown_plan_status"


def build_shadow_maturity_review(settings: Settings, account_name: str | None = None) -> ShadowMaturityReview:
    account = account_name or settings.paper.account_name
    with connect_db(settings.output.database_path) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            """
            SELECT
                d.*,
                p.status AS plan_status
            FROM paper_shadow_decisions d
            LEFT JOIN paper_plans p ON p.plan_id = d.plan_id
            WHERE d.account_name = ?
            ORDER BY d.decision_time, d.opportunity_id, d.line_name
            """,
            (account,),
        ).fetchall()
        open_plan_rows = connection.execute(
            """
            SELECT plan_id, symbol, status, entry_low, entry_high, updated_at
            FROM paper_plans
            WHERE account_name = ? AND status IN ('WATCHING', 'ENTERED', 'TP1_HIT')
            ORDER BY updated_at DESC, plan_id
            """,
            (account,),
        ).fetchall()
        latest_scan = connection.execute(
            """
            SELECT scan_id, scan_time, candidate_count, buy_candidate_count, watch_only_count
            FROM market_scans
            ORDER BY scan_time DESC
            LIMIT 1
            """
        ).fetchone()
        latest_daily_run = connection.execute(
            """
            SELECT run_id, status, started_at, finished_at
            FROM runs
            WHERE run_type = 'daily_full'
            ORDER BY started_at DESC
            LIMIT 1
            """
        ).fetchone()
        latest_4h_run = connection.execute(
            """
            SELECT run_id, status, started_at, finished_at
            FROM runs
            WHERE run_type = 'paper_4h_update'
            ORDER BY started_at DESC
            LIMIT 1
            """
        ).fetchone()

    line_counts: Counter[str] = Counter()
    stage_counts: Counter[str] = Counter()
    capacity_counts: Counter[str] = Counter()
    scanner_action_counts: Counter[str] = Counter()
    terminal_status_counts: Counter[str] = Counter()
    maturity_counts: Counter[str] = Counter()
    opportunities: set[str] = set()
    opportunity_summary: dict[str, dict[str, object]] = {}

    for row in rows:
        raw = _parse_raw_json(row["raw_json"])
        opportunity_id = str(row["opportunity_id"])
        line_counts[str(row["line_name"])] += 1
        stage_counts[_stage_for_row(row, raw)] += 1
        capacity_counts[str(row["capacity_state"] or "unknown")] += 1
        scanner_action = raw.get("scanner_action")
        scanner_action_counts[str(scanner_action or "unknown")] += 1
        opportunities.add(opportunity_id)
        maturity = _maturity_for_row(row)
        maturity_counts[maturity] += 1
        summary = opportunity_summary.setdefault(
            opportunity_id,
            {
                "opportunity_id": opportunity_id,
                "rows": 0,
                "lines": set(),
                "maturity": Counter(),
                "capacity": Counter(),
                "scanner_action": Counter(),
            },
        )
        summary["rows"] = int(summary["rows"]) + 1
        summary["lines"].add(str(row["line_name"]))
        summary["maturity"][maturity] += 1
        summary["capacity"][str(row["capacity_state"] or "unknown")] += 1
        summary["scanner_action"][str(scanner_action or "unknown")] += 1
        if maturity == "mature_terminal":
            terminal_status_counts[str(row["plan_status"])] += 1

    decision_level_count = sum(
        count
        for maturity, count in maturity_counts.items()
        if maturity in {"mature_terminal", "right_censored_open", "unknown_plan_status"}
    )
    mature_terminal_count = int(maturity_counts.get("mature_terminal", 0))
    right_censored_open_count = int(maturity_counts.get("right_censored_open", 0))
    unknown_plan_count = int(maturity_counts.get("unknown_plan_status", 0))
    right_censored_ratio_pct = (
        right_censored_open_count / decision_level_count * 100 if decision_level_count else 0.0
    )

    if not rows:
        verdict = "no_shadow_samples_yet"
        reason = "paper_shadow_decisions is empty for this account."
    elif decision_level_count == 0:
        verdict = "candidate_context_only"
        reason = "Only candidate-level context exists; no plan-level decision outcomes can be reviewed yet."
    elif mature_terminal_count == 0:
        verdict = "decision_samples_not_mature"
        reason = "Plan-level decisions exist, but all known plan-linked samples are still open or unresolved."
    else:
        verdict = "maturity_review_available"
        reason = "At least one plan-linked shadow decision has reached a terminal paper status."

    open_plan_count = len(open_plan_rows)
    watching_plan_count = sum(1 for row in open_plan_rows if str(row["status"]) == "WATCHING")
    diagnostics: dict[str, object] = {
        "open_plan_count": open_plan_count,
        "watching_plan_count": watching_plan_count,
        "latest_scan": dict(latest_scan) if latest_scan is not None else None,
        "latest_daily_run": dict(latest_daily_run) if latest_daily_run is not None else None,
        "latest_4h_run": dict(latest_4h_run) if latest_4h_run is not None else None,
        "open_plans": [
            {
                "plan_id": str(row["plan_id"]),
                "symbol": str(row["symbol"]),
                "status": str(row["status"]),
                "entry_low": row["entry_low"],
                "entry_high": row["entry_high"],
                "updated_at": str(row["updated_at"]),
            }
            for row in open_plan_rows[:10]
        ],
    }
    if not rows:
        if open_plan_count == 0:
            next_trigger = "Wait for the next daily scan/import to create candidate-level shadow rows."
        elif watching_plan_count > 0:
            next_trigger = (
                "Wait for the next daily scan/import candidate rows, or for a WATCHING plan to touch "
                "entry_high during a 4h paper update so plan-linked shadow decisions can be recorded."
            )
        else:
            next_trigger = (
                "Wait for a plan-linked 4h decision point from open entered/TP1 plans, or for the next "
                "daily scan/import to create candidate-level shadow rows."
            )
    elif decision_level_count == 0:
        next_trigger = "Wait for a WATCHING plan to touch entry_high during a 4h paper update."
    elif mature_terminal_count == 0:
        next_trigger = "Wait for plan-linked shadow decisions to reach terminal paper statuses."
    else:
        next_trigger = "Review direct filtering and capacity/path contribution once the sample reaches the pre-set threshold."
    diagnostics["next_trigger"] = next_trigger

    return ShadowMaturityReview(
        account_name=account,
        decision_count=len(rows),
        opportunity_count=len(opportunities),
        candidate_only_count=int(maturity_counts.get("candidate_only_no_plan_link", 0)),
        decision_level_count=decision_level_count,
        mature_terminal_count=mature_terminal_count,
        right_censored_open_count=right_censored_open_count,
        unknown_plan_count=unknown_plan_count,
        right_censored_ratio_pct=right_censored_ratio_pct,
        line_counts=dict(sorted(line_counts.items())),
        stage_counts=dict(sorted(stage_counts.items())),
        capacity_counts=dict(sorted(capacity_counts.items())),
        scanner_action_counts=dict(sorted(scanner_action_counts.items())),
        terminal_status_counts=dict(sorted(terminal_status_counts.items())),
        opportunity_summaries=[
            {
                "opportunity_id": str(item["opportunity_id"]),
                "rows": int(item["rows"]),
                "lines": ",".join(sorted(item["lines"])),
                "maturity": ",".join(f"{key}:{value}" for key, value in sorted(item["maturity"].items())),
                "capacity": ",".join(f"{key}:{value}" for key, value in sorted(item["capacity"].items())),
                "scanner_action": ",".join(
                    f"{key}:{value}" for key, value in sorted(item["scanner_action"].items())
                ),
            }
            for item in sorted(opportunity_summary.values(), key=lambda value: str(value["opportunity_id"]))
        ],
        diagnostics=diagnostics,
        verdict=verdict,
        reason=reason,
    )


def _counter_table(counter: dict[str, int], key_name: str) -> list[str]:
    if not counter:
        return [f"| {key_name} | Count |", "|---|---:|", "| none | 0 |"]
    lines = [f"| {key_name} | Count |", "|---|---:|"]
    lines.extend(f"| `{key}` | {value} |" for key, value in counter.items())
    return lines


def render_shadow_maturity_report(review: ShadowMaturityReview, version: int) -> str:
    opportunity_lines = [
        "| Opportunity | Rows | Lines | Maturity | Capacity | Scanner action |",
        "|---|---:|---|---|---|---|",
    ]
    if review.opportunity_summaries:
        opportunity_lines.extend(
            (
                f"| `{item['opportunity_id']}` | {item['rows']} | `{item['lines']}` | "
                f"`{item['maturity']}` | `{item['capacity']}` | `{item['scanner_action']}` |"
            )
            for item in review.opportunity_summaries
        )
    else:
        opportunity_lines.append("| none | 0 |  |  |  |  |")
    latest_scan = review.diagnostics.get("latest_scan")
    latest_daily = review.diagnostics.get("latest_daily_run")
    latest_4h = review.diagnostics.get("latest_4h_run")
    open_plan_lines = [
        "| Plan | Symbol | Status | Entry low | Entry high | Updated |",
        "|---|---|---|---:|---:|---|",
    ]
    open_plans = review.diagnostics.get("open_plans", [])
    if open_plans:
        open_plan_lines.extend(
            (
                f"| `{item['plan_id']}` | `{item['symbol']}` | `{item['status']}` | "
                f"{item['entry_low']} | {item['entry_high']} | {item['updated_at']} |"
            )
            for item in open_plans
        )
    else:
        open_plan_lines.append("| none | n/a | n/a | n/a | n/a | n/a |")

    lines = [
        f"# atr_reclaim prospective shadow maturity review v{version}",
        "",
        "## Scope",
        "",
        "- This report is read-only. It does not change `config/settings.toml`, paper plans, paper events, snapshots, or strategy defaults.",
        "- `reference_baseline` is the original strategy without `atr_reclaim_0_35`.",
        "- `atr_reclaim_0_35_shadow` is the independent forward reference line for original strategy plus `0.35`.",
        "- `research_incumbent` is the current research baseline, not an automatic paper deployment.",
        "",
        "## Verdict",
        "",
        f"- verdict: `{review.verdict}`",
        f"- reason: {review.reason}",
        "",
        "## Maturity Summary",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| decisions | {review.decision_count} |",
        f"| opportunities | {review.opportunity_count} |",
        f"| candidate-only rows | {review.candidate_only_count} |",
        f"| plan-linked decision rows | {review.decision_level_count} |",
        f"| mature terminal rows | {review.mature_terminal_count} |",
        f"| right-censored open rows | {review.right_censored_open_count} |",
        f"| unknown plan rows | {review.unknown_plan_count} |",
        f"| right-censored ratio | {review.right_censored_ratio_pct:.2f}% |",
        "",
        "## Waiting Diagnostics",
        "",
        f"- open_plan_count: {review.diagnostics.get('open_plan_count', 0)}",
        f"- watching_plan_count: {review.diagnostics.get('watching_plan_count', 0)}",
        f"- latest_scan: `{latest_scan.get('scan_id') if isinstance(latest_scan, dict) else 'n/a'}` "
        f"at `{latest_scan.get('scan_time') if isinstance(latest_scan, dict) else 'n/a'}`",
        f"- latest_daily_run: `{latest_daily.get('run_id') if isinstance(latest_daily, dict) else 'n/a'}` "
        f"status=`{latest_daily.get('status') if isinstance(latest_daily, dict) else 'n/a'}`",
        f"- latest_4h_run: `{latest_4h.get('run_id') if isinstance(latest_4h, dict) else 'n/a'}` "
        f"status=`{latest_4h.get('status') if isinstance(latest_4h, dict) else 'n/a'}`",
        f"- next_trigger: {review.diagnostics.get('next_trigger')}",
        "",
        "### Open Plans",
        "",
        *open_plan_lines,
        "",
        "## By Line",
        "",
        *_counter_table(review.line_counts, "Line"),
        "",
        "## By Opportunity",
        "",
        *opportunity_lines,
        "",
        "## By Stage",
        "",
        *_counter_table(review.stage_counts, "Stage"),
        "",
        "## By Capacity State",
        "",
        *_counter_table(review.capacity_counts, "Capacity state"),
        "",
        "## By Scanner Action",
        "",
        *_counter_table(review.scanner_action_counts, "Scanner action"),
        "",
        "## Terminal Outcomes",
        "",
        *_counter_table(review.terminal_status_counts, "Plan status"),
        "",
        "## Interpretation",
        "",
        "- Candidate-only rows are useful for confirming that all three lines saw the same scan candidate, but they do not prove trade quality.",
        "- Plan-linked rows can become maturity evidence only after the linked paper plan reaches a terminal status.",
        "- Until mature terminal samples are sufficient, `atr_reclaim_0_35` remains a prospective shadow reference, not a paper deployment rule.",
        "",
    ]
    return "\n".join(lines)


def write_shadow_maturity_report(settings: Settings, account_name: str | None = None) -> tuple[ShadowMaturityReview, list[Path]]:
    review = build_shadow_maturity_review(settings, account_name=account_name)
    now = datetime.now(timezone(timedelta(hours=8)))
    date_text = now.strftime("%Y-%m-%d")
    report_dir = settings.output.reports_dir / date_text
    obsidian_dir = None if settings.output.obsidian_dir is None else settings.output.obsidian_dir / "Reports" / date_text
    prefix = f"paper_shadow_maturity_review_{date_text}_{review.account_name}"
    version = next_report_version([report_dir, obsidian_dir], prefix)
    filename = versioned_markdown_filename(prefix, version)
    text = render_shadow_maturity_report(review, version)
    paths: list[Path] = []
    for directory in [report_dir, obsidian_dir]:
        if directory is None:
            continue
        directory.mkdir(parents=True, exist_ok=True)
        out = directory / filename
        out.write_text(text, encoding="utf-8")
        paths.append(out)
    return review, paths
