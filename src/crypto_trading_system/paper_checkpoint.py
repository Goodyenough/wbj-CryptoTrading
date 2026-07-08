from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
import json
from pathlib import Path

from .config import Settings
from .paper_audit import (
    DataLinkHealth,
    EnteredTradeRow,
    OpportunityRow,
    _local_now,
    build_data_link_health,
    build_entered_trade_rows,
    build_reclaim_opportunities,
    build_scan_candidate_opportunities,
)
from .paper_shadow_replay import (
    ShadowReplayRow,
    build_entry_reclaim_confirm_1bar_shadow,
    build_relative_strength_gate_shadow,
)
from .report_versions import next_report_version, versioned_markdown_filename


@dataclass(frozen=True)
class CheckpointDecision:
    verdict: str
    reason: str
    next_action: str


@dataclass(frozen=True)
class PaperCheckpoint:
    account: str
    start_date: str
    end_date: str
    data_link: DataLinkHealth
    opportunities: list[OpportunityRow]
    entered_trades: list[EnteredTradeRow]
    entry_reclaim_shadow: list[ShadowReplayRow]
    relative_strength_shadow: list[ShadowReplayRow]
    decision: CheckpointDecision


def _false_entry_opportunities(entered: list[EnteredTradeRow]) -> list[OpportunityRow]:
    return [
        OpportunityRow(
            source="ENTERED_TRADE",
            symbol=row.symbol,
            plan_id=row.plan_id,
            first_time=row.entered_at,
            reason=row.reason,
            entry=row.entry_price,
            stop=row.stop,
            tp1=row.tp1,
            max_price_after=row.max_price_after,
            min_price_after=row.min_price_after,
            reclaimed=True,
            hit_tp1=row.tp1_hit,
            hit_stop=row.status == "STOPPED",
            classification="false_entry",
            explanation=row.explanation,
            observation_bars=0,
            required_bars=42,
            maturity_status="mature" if row.status in {"STOPPED", "CLOSED", "INVALIDATED", "ARCHIVED"} else "open_unknown",
            classification_final=row.status in {"STOPPED", "CLOSED", "INVALIDATED", "ARCHIVED"},
            risk_r=None if row.entry_price is None or row.stop is None else row.entry_price - row.stop,
            mfe_r=row.mfe_r,
            mae_r=row.mae_r,
            counterfactual_pnl_r=-1.0 if row.status == "STOPPED" else None,
            first_hit="stop_first" if row.status == "STOPPED" else "none",
            time_to_first_hit_bars=None,
        )
        for row in entered
        if row.attribution in {"entry_issue", "selection_issue", "market_issue"} and row.status == "STOPPED"
    ]


def decide_checkpoint(
    data_link: DataLinkHealth,
    opportunities: list[OpportunityRow],
    *,
    min_mature_opportunities: int = 20,
    max_right_censored_ratio: float = 0.40,
) -> CheckpointDecision:
    maturity_counts = Counter(row.maturity_status for row in opportunities)
    mature_count = maturity_counts.get("mature", 0)
    right_censored_count = maturity_counts.get("right_censored", 0)
    right_censored_ratio = 0.0 if not opportunities else right_censored_count / len(opportunities)
    if not data_link.config_hash_stable:
        return CheckpointDecision(
            verdict="interim_report_required",
            reason="config_hash drift detected in the checkpoint window",
            next_action="Do not run formal strategy acceptance. Disclose config drift and continue observation.",
        )
    if data_link.verdict == "fail":
        return CheckpointDecision(
            verdict="interim_report_required",
            reason="data link health failed",
            next_action="Fix or disclose data-link failure before interpreting strategy behavior.",
        )
    if mature_count < min_mature_opportunities:
        return CheckpointDecision(
            verdict="wait_for_more_data",
            reason=f"mature opportunities {mature_count} < required {min_mature_opportunities}",
            next_action="Continue current daily + 4h observation and rerun checkpoint after more samples mature.",
        )
    if right_censored_ratio > max_right_censored_ratio:
        return CheckpointDecision(
            verdict="wait_for_more_data",
            reason=f"right-censored ratio {right_censored_ratio:.1%} > allowed {max_right_censored_ratio:.1%}",
            next_action="Treat the window as interim; avoid over-interpreting open or immature paths.",
        )
    return CheckpointDecision(
        verdict="formal_audit_ready",
        reason="data link is usable, config hash is stable, and opportunity samples are sufficiently mature",
        next_action="Run formal paper audit and both shadow replay reports before deciding whether any A/B should start.",
    )


def build_paper_checkpoint(settings: Settings, account: str, start_date: str, end_date: str) -> PaperCheckpoint:
    data_link = build_data_link_health(settings, account, start_date, end_date)
    reclaim = build_reclaim_opportunities(settings, account, start_date, end_date)
    scan = build_scan_candidate_opportunities(settings, start_date, end_date)
    entered = build_entered_trade_rows(settings, account, start_date, end_date)
    opportunities = reclaim + scan + _false_entry_opportunities(entered)
    entry_reclaim_shadow = build_entry_reclaim_confirm_1bar_shadow(settings, account, start_date, end_date)
    relative_strength_shadow = build_relative_strength_gate_shadow(settings, account, start_date, end_date)
    decision = decide_checkpoint(data_link, opportunities)
    return PaperCheckpoint(
        account=account,
        start_date=start_date,
        end_date=end_date,
        data_link=data_link,
        opportunities=opportunities,
        entered_trades=entered,
        entry_reclaim_shadow=entry_reclaim_shadow,
        relative_strength_shadow=relative_strength_shadow,
        decision=decision,
    )


def _counter(rows: list[OpportunityRow], attr: str) -> Counter:
    return Counter(str(getattr(row, attr)) for row in rows)


def _shadow_counter(rows: list[ShadowReplayRow]) -> Counter:
    return Counter(row.decision for row in rows)


def render_paper_checkpoint_report(checkpoint: PaperCheckpoint, report_version: int) -> str:
    now = _local_now()
    maturity_counts = _counter(checkpoint.opportunities, "maturity_status")
    classification_counts = _counter(checkpoint.opportunities, "classification")
    entry_counts = _shadow_counter(checkpoint.entry_reclaim_shadow)
    relative_counts = _shadow_counter(checkpoint.relative_strength_shadow)
    right_censored = maturity_counts.get("right_censored", 0)
    right_censored_ratio = 0.0 if not checkpoint.opportunities else right_censored / len(checkpoint.opportunities)
    lines = [
        "---",
        f"created: {now.strftime('%Y-%m-%d %H:%M:%S %Z')}",
        "tags:",
        "  - crypto",
        "  - trading-system",
        "  - paper-checkpoint",
        f"account: {checkpoint.account}",
        f"start_date: {checkpoint.start_date}",
        f"end_date: {checkpoint.end_date}",
        f"report_version: v{report_version}",
        f"verdict: {checkpoint.decision.verdict}",
        "---",
        "",
        f"# Paper Checkpoint {checkpoint.start_date} -> {checkpoint.end_date} {checkpoint.account} v{report_version}",
        "",
        "This checkpoint decides whether the window is ready for a formal paper audit. It does not modify settings, plans, events, snapshots, or paper state.",
        "",
        "## Decision",
        "",
        f"- verdict: {checkpoint.decision.verdict}",
        f"- reason: {checkpoint.decision.reason}",
        f"- next_action: {checkpoint.decision.next_action}",
        "",
        "## Data Link Gate",
        "",
        f"- data_link_verdict: {checkpoint.data_link.verdict}",
        f"- config_hash_stable: {str(checkpoint.data_link.config_hash_stable).lower()}",
        f"- config_hashes: {', '.join(checkpoint.data_link.config_hashes) if checkpoint.data_link.config_hashes else 'n/a'}",
        f"- stale_running_runs: {checkpoint.data_link.stale_running_runs}",
        f"- duplicate_events: {checkpoint.data_link.duplicate_events}",
        f"- impossible_event_order: {checkpoint.data_link.impossible_event_order}",
        f"- daily_success: {checkpoint.data_link.daily.success_runs}/{checkpoint.data_link.daily.expected_runs}",
        f"- paper_4h_success: {checkpoint.data_link.paper_4h.success_runs}/{checkpoint.data_link.paper_4h.expected_runs}",
        f"- note: {checkpoint.data_link.note}",
        "",
        "## Sample Maturity Gate",
        "",
        f"- opportunities: {len(checkpoint.opportunities)}",
        f"- mature: {maturity_counts.get('mature', 0)}",
        f"- right_censored: {right_censored}",
        f"- right_censored_ratio: {right_censored_ratio:.1%}",
        f"- open_unknown: {maturity_counts.get('open_unknown', 0)}",
        f"- entered_trades: {len(checkpoint.entered_trades)}",
        "",
        "## Opportunity Classification",
        "",
        "| Classification | Count |",
        "|---|---:|",
    ]
    for key, value in classification_counts.most_common():
        lines.append(f"| {key} | {value} |")
    if not classification_counts:
        lines.append("| n/a | 0 |")
    lines.extend([
        "",
        "## Shadow Replay Snapshot",
        "",
        "### entry_reclaim_confirm_1bar",
        "",
        "| Decision | Count |",
        "|---|---:|",
    ])
    for key, value in entry_counts.most_common():
        lines.append(f"| {key} | {value} |")
    if not entry_counts:
        lines.append("| n/a | 0 |")
    lines.extend([
        "",
        "### relative_strength_gate",
        "",
        "| Decision | Count |",
        "|---|---:|",
    ])
    for key, value in relative_counts.most_common():
        lines.append(f"| {key} | {value} |")
    if not relative_counts:
        lines.append("| n/a | 0 |")
    lines.extend([
        "",
        "## Commands For Next Step",
        "",
        "```powershell",
        f"python main.py paper audit --account {checkpoint.account} --start-date {checkpoint.start_date} --end-date {checkpoint.end_date}",
        f"python main.py paper shadow-replay --account {checkpoint.account} --start-date {checkpoint.start_date} --end-date {checkpoint.end_date} --variant entry_reclaim_confirm_1bar",
        f"python main.py paper shadow-replay --account {checkpoint.account} --start-date {checkpoint.start_date} --end-date {checkpoint.end_date} --variant relative_strength_gate",
        "```",
        "",
        "## Raw Summary",
        "",
        "```json",
        json.dumps(
            {
                "verdict": checkpoint.decision.verdict,
                "reason": checkpoint.decision.reason,
                "data_link_verdict": checkpoint.data_link.verdict,
                "config_hash_stable": checkpoint.data_link.config_hash_stable,
                "opportunities": len(checkpoint.opportunities),
                "maturity": dict(maturity_counts),
                "classifications": dict(classification_counts),
                "entry_reclaim_confirm_1bar": dict(entry_counts),
                "relative_strength_gate": dict(relative_counts),
            },
            ensure_ascii=False,
            indent=2,
        ),
        "```",
    ])
    return "\n".join(lines) + "\n"


def write_paper_checkpoint_report(
    settings: Settings,
    *,
    account_name: str | None,
    start_date: str,
    end_date: str,
) -> tuple[str, list[Path]]:
    account = account_name or settings.paper.account_name
    checkpoint = build_paper_checkpoint(settings, account, start_date, end_date)
    now = _local_now()
    report_dir = settings.output.reports_dir / now.strftime("%Y-%m-%d")
    obsidian_dir = None if settings.output.obsidian_dir is None else settings.output.obsidian_dir / "Reports" / now.strftime("%Y-%m-%d")
    prefix = f"paper_checkpoint_{start_date}_{end_date}_{account}"
    version = next_report_version([report_dir, obsidian_dir], prefix)
    filename = versioned_markdown_filename(prefix, version)
    text = render_paper_checkpoint_report(checkpoint, version)
    paths: list[Path] = []
    for directory in [report_dir, obsidian_dir]:
        if directory is None:
            continue
        directory.mkdir(parents=True, exist_ok=True)
        out = directory / filename
        out.write_text(text, encoding="utf-8")
        paths.append(out)
    return text, paths
