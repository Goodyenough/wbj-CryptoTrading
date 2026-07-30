from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
import sqlite3

from .config import Settings
from .database import connect_db
from .paper_trader import CLOSED_STATUSES, OPEN_STATUSES
from .report_versions import next_report_version, versioned_markdown_filename


EXPECTED_LINES = ("reference_baseline", "atr_reclaim_0_35_shadow", "research_incumbent")


@dataclass(frozen=True)
class ShadowReconciliationReview:
    account_name: str
    decision_count: int
    opportunity_count: int
    complete_opportunity_count: int
    incomplete_opportunity_count: int
    controls_paper_count: int
    mismatch_opportunity_count: int
    mature_terminal_opportunity_count: int
    right_censored_opportunity_count: int
    line_counts: dict[str, int]
    stage_counts: dict[str, int]
    decision_counts: dict[str, int]
    opportunity_summaries: list[dict[str, object]]
    diagnostics: dict[str, object]
    verdict: str
    reason: str


def _stage_for_row(row: sqlite3.Row) -> str:
    plan_id = row["plan_id"]
    if plan_id is None:
        return "candidate_level"
    return "paper_4h_decision"


def _maturity_for_status(status: str | None) -> str:
    if status in CLOSED_STATUSES:
        return "mature_terminal"
    if status in OPEN_STATUSES:
        return "right_censored_open"
    if status is None:
        return "candidate_only_or_unknown_plan"
    return "unknown_plan_status"


def _adjust_current_run(row: dict | None, current_run_id: str | None) -> dict | None:
    if row is None or current_run_id is None:
        return row
    if row.get("run_id") == current_run_id and row.get("status") == "running":
        adjusted = dict(row)
        adjusted["status"] = "success"
        adjusted["finished_at"] = adjusted.get("finished_at") or "assumed_success_after_report_generation"
        return adjusted
    return row


def build_shadow_reconciliation_review(
    settings: Settings,
    account_name: str | None = None,
    current_run_id: str | None = None,
) -> ShadowReconciliationReview:
    account = account_name or settings.paper.account_name
    with connect_db(settings.output.database_path) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            """
            SELECT d.*, p.status AS plan_status
            FROM paper_shadow_decisions d
            LEFT JOIN paper_plans p ON p.plan_id = d.plan_id
            WHERE d.account_name = ?
            ORDER BY d.opportunity_id, d.decision_time, d.line_name
            """,
            (account,),
        ).fetchall()
        open_plans = connection.execute(
            """
            SELECT plan_id, symbol, status, entry_low, entry_high, updated_at
            FROM paper_plans
            WHERE account_name = ? AND status IN ('WATCHING', 'ENTERED', 'TP1_HIT')
            ORDER BY updated_at DESC, plan_id
            """,
            (account,),
        ).fetchall()
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
    decision_counts: Counter[str] = Counter()
    by_opportunity: dict[str, list[sqlite3.Row]] = {}
    controls_paper_count = 0
    for row in rows:
        opportunity_id = str(row["opportunity_id"])
        by_opportunity.setdefault(opportunity_id, []).append(row)
        line_counts[str(row["line_name"])] += 1
        stage_counts[_stage_for_row(row)] += 1
        decision_counts[str(row["decision"])] += 1
        controls_paper_count += int(row["controls_paper"] or 0)

    opportunity_summaries: list[dict[str, object]] = []
    complete_opportunity_count = 0
    incomplete_opportunity_count = 0
    mismatch_opportunity_count = 0
    mature_terminal_opportunity_count = 0
    right_censored_opportunity_count = 0

    for opportunity_id, items in sorted(by_opportunity.items()):
        lines = {str(row["line_name"]) for row in items}
        missing_lines = [line for line in EXPECTED_LINES if line not in lines]
        decisions_by_line = {str(row["line_name"]): str(row["decision"]) for row in items}
        accepted_by_line = {str(row["line_name"]): int(row["accepted"]) for row in items}
        statuses = {str(row["plan_status"]) for row in items if row["plan_status"] is not None}
        maturities = {_maturity_for_status(row["plan_status"]) for row in items}
        complete = not missing_lines
        if complete:
            complete_opportunity_count += 1
        else:
            incomplete_opportunity_count += 1
        if len(set(decisions_by_line.values())) > 1 or len(set(accepted_by_line.values())) > 1:
            mismatch_opportunity_count += 1
        if "mature_terminal" in maturities:
            mature_terminal_opportunity_count += 1
        if "right_censored_open" in maturities:
            right_censored_opportunity_count += 1
        opportunity_summaries.append(
            {
                "opportunity_id": opportunity_id,
                "rows": len(items),
                "lines": ",".join(sorted(lines)),
                "missing_lines": ",".join(missing_lines) if missing_lines else "none",
                "decisions": ",".join(f"{key}:{value}" for key, value in sorted(decisions_by_line.items())),
                "accepted": ",".join(f"{key}:{value}" for key, value in sorted(accepted_by_line.items())),
                "maturity": ",".join(sorted(maturities)),
                "plan_status": ",".join(sorted(statuses)) if statuses else "none",
            }
        )

    diagnostics: dict[str, object] = {
        "expected_lines": list(EXPECTED_LINES),
        "open_plan_count": len(open_plans),
        "watching_plan_count": sum(1 for row in open_plans if str(row["status"]) == "WATCHING"),
        "latest_daily_run": _adjust_current_run(dict(latest_daily_run) if latest_daily_run is not None else None, current_run_id),
        "latest_4h_run": _adjust_current_run(dict(latest_4h_run) if latest_4h_run is not None else None, current_run_id),
        "open_plans": [
            {
                "plan_id": str(row["plan_id"]),
                "symbol": str(row["symbol"]),
                "status": str(row["status"]),
                "entry_low": row["entry_low"],
                "entry_high": row["entry_high"],
                "updated_at": str(row["updated_at"]),
            }
            for row in open_plans[:10]
        ],
    }

    if not rows:
        verdict = "no_shadow_samples_yet"
        reason = "paper_shadow_decisions is empty, so no three-line reconciliation can be performed."
    elif controls_paper_count:
        verdict = "reconciliation_failed_controls_paper"
        reason = "At least one shadow row has controls_paper=1; shadow lines must remain observational."
    elif incomplete_opportunity_count:
        verdict = "reconciliation_incomplete_missing_lines"
        reason = "At least one opportunity is missing one or more required reference lines."
    elif mature_terminal_opportunity_count == 0:
        verdict = "reconciliation_waiting_for_terminal_outcomes"
        reason = "All opportunities have the required lines, but no plan-linked opportunity is mature terminal yet."
    else:
        verdict = "reconciliation_ready_for_attribution"
        reason = "Required lines are present and at least one opportunity has a terminal plan status."

    return ShadowReconciliationReview(
        account_name=account,
        decision_count=len(rows),
        opportunity_count=len(by_opportunity),
        complete_opportunity_count=complete_opportunity_count,
        incomplete_opportunity_count=incomplete_opportunity_count,
        controls_paper_count=controls_paper_count,
        mismatch_opportunity_count=mismatch_opportunity_count,
        mature_terminal_opportunity_count=mature_terminal_opportunity_count,
        right_censored_opportunity_count=right_censored_opportunity_count,
        line_counts=dict(sorted(line_counts.items())),
        stage_counts=dict(sorted(stage_counts.items())),
        decision_counts=dict(sorted(decision_counts.items())),
        opportunity_summaries=opportunity_summaries,
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


def render_shadow_reconciliation_report(review: ShadowReconciliationReview, version: int) -> str:
    latest_daily = review.diagnostics.get("latest_daily_run")
    latest_4h = review.diagnostics.get("latest_4h_run")
    opportunity_lines = [
        "| Opportunity | Rows | Lines | Missing lines | Decisions | Accepted | Maturity | Plan status |",
        "|---|---:|---|---|---|---|---|---|",
    ]
    if review.opportunity_summaries:
        opportunity_lines.extend(
            (
                f"| `{item['opportunity_id']}` | {item['rows']} | `{item['lines']}` | "
                f"`{item['missing_lines']}` | `{item['decisions']}` | `{item['accepted']}` | "
                f"`{item['maturity']}` | `{item['plan_status']}` |"
            )
            for item in review.opportunity_summaries
        )
    else:
        opportunity_lines.append("| none | 0 |  |  |  |  |  |  |")

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
        f"# Paper Shadow Decision-State Reconciliation v{version}",
        "",
        "## Scope",
        "",
        "- This report is read-only and does not change `config/settings.toml`, paper plans, events, snapshots, or strategy defaults.",
        "- Required lines: `reference_baseline`, `atr_reclaim_0_35_shadow`, `research_incumbent`.",
        "- The goal is state reconciliation, not strategy validation.",
        "",
        "## Verdict",
        "",
        f"- verdict: `{review.verdict}`",
        f"- reason: {review.reason}",
        "",
        "## Summary",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| decisions | {review.decision_count} |",
        f"| opportunities | {review.opportunity_count} |",
        f"| complete opportunities | {review.complete_opportunity_count} |",
        f"| incomplete opportunities | {review.incomplete_opportunity_count} |",
        f"| controls_paper rows | {review.controls_paper_count} |",
        f"| mismatch opportunities | {review.mismatch_opportunity_count} |",
        f"| mature terminal opportunities | {review.mature_terminal_opportunity_count} |",
        f"| right-censored opportunities | {review.right_censored_opportunity_count} |",
        "",
        "## Run Context",
        "",
        f"- latest_daily_run: `{latest_daily.get('run_id') if isinstance(latest_daily, dict) else 'n/a'}` "
        f"status=`{latest_daily.get('status') if isinstance(latest_daily, dict) else 'n/a'}`",
        f"- latest_4h_run: `{latest_4h.get('run_id') if isinstance(latest_4h, dict) else 'n/a'}` "
        f"status=`{latest_4h.get('status') if isinstance(latest_4h, dict) else 'n/a'}`",
        f"- open_plan_count: {review.diagnostics.get('open_plan_count', 0)}",
        f"- watching_plan_count: {review.diagnostics.get('watching_plan_count', 0)}",
        "",
        "### Open Plans",
        "",
        *open_plan_lines,
        "",
        "## By Line",
        "",
        *_counter_table(review.line_counts, "Line"),
        "",
        "## By Stage",
        "",
        *_counter_table(review.stage_counts, "Stage"),
        "",
        "## By Decision",
        "",
        *_counter_table(review.decision_counts, "Decision"),
        "",
        "## By Opportunity",
        "",
        *opportunity_lines,
        "",
        "## Interpretation",
        "",
        "- Empty shadow decisions mean the system is still waiting for prospective samples.",
        "- Missing required lines block attribution because baseline, `0.35`, and incumbent would not share the same observation point.",
        "- Mature terminal opportunities are required before direct filtering or path/capacity contribution can be interpreted.",
        "- Any `controls_paper=1` row is a failure for this shadow phase unless explicitly approved later.",
        "",
    ]
    return "\n".join(lines)


def write_shadow_reconciliation_report(
    settings: Settings,
    account_name: str | None = None,
    current_run_id: str | None = None,
) -> tuple[ShadowReconciliationReview, list[Path]]:
    review = build_shadow_reconciliation_review(
        settings,
        account_name=account_name,
        current_run_id=current_run_id,
    )
    now = datetime.now(timezone(timedelta(hours=8)))
    date_text = now.strftime("%Y-%m-%d")
    report_dir = settings.output.reports_dir / date_text
    obsidian_dir = None if settings.output.obsidian_dir is None else settings.output.obsidian_dir / "Reports" / date_text
    prefix = f"paper_shadow_reconciliation_{date_text}_{review.account_name}"
    version = next_report_version([report_dir, obsidian_dir], prefix)
    filename = versioned_markdown_filename(prefix, version)
    text = render_shadow_reconciliation_report(review, version)
    paths: list[Path] = []
    for directory in [report_dir, obsidian_dir]:
        if directory is None:
            continue
        directory.mkdir(parents=True, exist_ok=True)
        out = directory / filename
        out.write_text(text, encoding="utf-8")
        paths.append(out)
    return review, paths
