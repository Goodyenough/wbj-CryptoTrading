from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path

from .backtest.history import fetch_klines_cached
from .config import Settings
from .paper_audit import (
    BEIJING,
    OpportunityRow,
    _fmt,
    _iso_z,
    _local_now,
    _local_timestamp,
    _ms,
    _parse_window,
    _pct,
    _risk,
    build_reclaim_opportunities,
    build_scan_candidate_opportunities,
)
from .report_versions import next_report_version, versioned_markdown_filename


@dataclass(frozen=True)
class ShadowReplayRow:
    symbol: str
    opportunity_id: str
    source: str
    first_time: str
    entry_high: float | None
    entry_low: float | None
    stop: float | None
    tp1: float | None
    baseline_entry_time: str | None
    variant_entry_time: str | None
    baseline_entry_price: float | None
    variant_entry_price: float | None
    baseline_first_hit: str
    variant_first_hit: str
    baseline_mfe_r: float | None
    variant_mfe_r: float | None
    decision: str
    explanation: str


def _kline_time(kline: list) -> datetime:
    return datetime.fromtimestamp(int(kline[6]) / 1000, tz=timezone.utc)


def _fetch_closed_4h_path(settings: Settings, symbol: str, start_time: str, end_utc: datetime) -> list[list]:
    start = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
    fetched = fetch_klines_cached(
        settings,
        symbol,
        "4h",
        _ms(start - timedelta(hours=4)),
        _ms(end_utc + timedelta(hours=4)),
        allow_data_gaps=True,
    )
    return [
        kline for kline in fetched.klines
        if _kline_time(kline) >= start and _kline_time(kline) <= end_utc
    ]


def _first_hit_after_entry(
    klines: list[list],
    *,
    start_index: int,
    entry_price: float,
    stop: float | None,
    tp1: float | None,
) -> tuple[str, float | None]:
    risk = _risk(entry_price, stop)
    max_high = None
    near_tp1 = None if tp1 is None else entry_price + 0.8 * (tp1 - entry_price)
    for kline in klines[start_index + 1:]:
        high = float(kline[2])
        low = float(kline[3])
        max_high = high if max_high is None else max(max_high, high)
        if stop is not None and low <= stop:
            mfe_r = None if risk is None or max_high is None else (max_high - entry_price) / risk
            return "stop_first", mfe_r
        if tp1 is not None and high >= tp1:
            mfe_r = None if risk is None or max_high is None else (max_high - entry_price) / risk
            return "tp1_first", mfe_r
        if near_tp1 is not None and high >= near_tp1:
            mfe_r = None if risk is None or max_high is None else (max_high - entry_price) / risk
            return "near_tp1_first", mfe_r
    mfe_r = None if risk is None or max_high is None else (max_high - entry_price) / risk
    return "open_unknown", mfe_r


def _entry_reclaim_confirm_1bar_row(settings: Settings, opportunity: OpportunityRow, end_utc: datetime) -> ShadowReplayRow:
    if opportunity.entry is None:
        return ShadowReplayRow(
            symbol=opportunity.symbol,
            opportunity_id=opportunity.plan_id,
            source=opportunity.source,
            first_time=opportunity.first_time,
            entry_high=None,
            entry_low=None,
            stop=opportunity.stop,
            tp1=opportunity.tp1,
            baseline_entry_time=None,
            variant_entry_time=None,
            baseline_entry_price=None,
            variant_entry_price=None,
            baseline_first_hit="data_gap",
            variant_first_hit="data_gap",
            baseline_mfe_r=None,
            variant_mfe_r=None,
            decision="data_gap",
            explanation="missing entry level",
        )
    klines = _fetch_closed_4h_path(settings, opportunity.symbol, opportunity.first_time, end_utc)
    baseline_index = None
    for index, kline in enumerate(klines):
        close = float(kline[4])
        if close >= float(opportunity.entry):
            baseline_index = index
            break
    if baseline_index is None:
        return ShadowReplayRow(
            symbol=opportunity.symbol,
            opportunity_id=opportunity.plan_id,
            source=opportunity.source,
            first_time=opportunity.first_time,
            entry_high=opportunity.entry,
            entry_low=None,
            stop=opportunity.stop,
            tp1=opportunity.tp1,
            baseline_entry_time=None,
            variant_entry_time=None,
            baseline_entry_price=None,
            variant_entry_price=None,
            baseline_first_hit="no_baseline_entry",
            variant_first_hit="no_variant_entry",
            baseline_mfe_r=None,
            variant_mfe_r=None,
            decision="no_baseline_entry",
            explanation="price never closed back above entry_high",
        )

    baseline_kline = klines[baseline_index]
    baseline_entry_price = float(baseline_kline[4])
    baseline_first_hit, baseline_mfe_r = _first_hit_after_entry(
        klines,
        start_index=baseline_index,
        entry_price=baseline_entry_price,
        stop=opportunity.stop,
        tp1=opportunity.tp1,
    )

    variant_index = None
    if baseline_index + 1 < len(klines):
        confirm_kline = klines[baseline_index + 1]
        confirm_close = float(confirm_kline[4])
        confirm_low = float(confirm_kline[3])
        # In legacy plan rows entry_low is not available in OpportunityRow; use stop-safe confirmation
        # here and keep entry_low explicit as n/a in the report.
        if confirm_close >= float(opportunity.entry) and (opportunity.stop is None or confirm_low > float(opportunity.stop)):
            variant_index = baseline_index + 1

    if variant_index is None:
        if baseline_first_hit == "stop_first":
            decision = "filtered_loser"
            explanation = "1-bar confirmation would avoid a baseline stop-first path"
        elif baseline_first_hit in {"near_tp1_first", "tp1_first"}:
            decision = "missed_winner"
            explanation = "1-bar confirmation would skip a baseline near-TP1/TP1 path"
        else:
            decision = "filtered_unknown"
            explanation = "1-bar confirmation would skip an inconclusive baseline path"
        return ShadowReplayRow(
            symbol=opportunity.symbol,
            opportunity_id=opportunity.plan_id,
            source=opportunity.source,
            first_time=opportunity.first_time,
            entry_high=opportunity.entry,
            entry_low=None,
            stop=opportunity.stop,
            tp1=opportunity.tp1,
            baseline_entry_time=_iso_z(_kline_time(baseline_kline)),
            variant_entry_time=None,
            baseline_entry_price=baseline_entry_price,
            variant_entry_price=None,
            baseline_first_hit=baseline_first_hit,
            variant_first_hit="no_variant_entry",
            baseline_mfe_r=baseline_mfe_r,
            variant_mfe_r=None,
            decision=decision,
            explanation=explanation,
        )

    variant_kline = klines[variant_index]
    variant_entry_price = float(variant_kline[4])
    variant_first_hit, variant_mfe_r = _first_hit_after_entry(
        klines,
        start_index=variant_index,
        entry_price=variant_entry_price,
        stop=opportunity.stop,
        tp1=opportunity.tp1,
    )
    if baseline_first_hit == "stop_first" and variant_first_hit != "stop_first":
        decision = "improved_path"
    elif baseline_first_hit in {"near_tp1_first", "tp1_first"} and variant_first_hit == "stop_first":
        decision = "worse_path"
    else:
        decision = "delayed_entry"
    return ShadowReplayRow(
        symbol=opportunity.symbol,
        opportunity_id=opportunity.plan_id,
        source=opportunity.source,
        first_time=opportunity.first_time,
        entry_high=opportunity.entry,
        entry_low=None,
        stop=opportunity.stop,
        tp1=opportunity.tp1,
        baseline_entry_time=_iso_z(_kline_time(baseline_kline)),
        variant_entry_time=_iso_z(_kline_time(variant_kline)),
        baseline_entry_price=baseline_entry_price,
        variant_entry_price=variant_entry_price,
        baseline_first_hit=baseline_first_hit,
        variant_first_hit=variant_first_hit,
        baseline_mfe_r=baseline_mfe_r,
        variant_mfe_r=variant_mfe_r,
        decision=decision,
        explanation="baseline and variant both enter; compare first-hit path and R",
    )


def build_entry_reclaim_confirm_1bar_shadow(
    settings: Settings,
    account: str,
    start_date: str,
    end_date: str,
) -> list[ShadowReplayRow]:
    _start_utc, end_utc = _parse_window(start_date, end_date)
    opportunities = build_reclaim_opportunities(settings, account, start_date, end_date)
    opportunities += build_scan_candidate_opportunities(settings, start_date, end_date)
    rows: list[ShadowReplayRow] = []
    seen: set[str] = set()
    for opportunity in opportunities:
        key = f"{opportunity.source}:{opportunity.plan_id}"
        if key in seen:
            continue
        seen.add(key)
        rows.append(_entry_reclaim_confirm_1bar_row(settings, opportunity, end_utc))
    return rows


def render_shadow_replay_report(
    *,
    account: str,
    start_date: str,
    end_date: str,
    variant: str,
    report_version: int,
    rows: list[ShadowReplayRow],
) -> str:
    now = _local_now()
    decision_counts = Counter(row.decision for row in rows)
    baseline_entries = sum(1 for row in rows if row.baseline_entry_time)
    variant_entries = sum(1 for row in rows if row.variant_entry_time)
    lines = [
        "---",
        f"created: {now.strftime('%Y-%m-%d %H:%M:%S %Z')}",
        "tags:",
        "  - crypto",
        "  - trading-system",
        "  - shadow-replay",
        f"account: {account}",
        f"start_date: {start_date}",
        f"end_date: {end_date}",
        f"variant: {variant}",
        f"report_version: v{report_version}",
        "---",
        "",
        f"# Paper Shadow Replay {variant} {start_date} -> {end_date} {account} v{report_version}",
        "",
        "This is an offline diagnostic replay. It does not modify settings, plans, events, or paper state.",
        "",
        "## Summary",
        "",
        f"- opportunities: {len(rows)}",
        f"- baseline_entries: {baseline_entries}",
        f"- variant_entries: {variant_entries}",
        f"- filtered_loser: {decision_counts.get('filtered_loser', 0)}",
        f"- missed_winner: {decision_counts.get('missed_winner', 0)}",
        f"- improved_path: {decision_counts.get('improved_path', 0)}",
        f"- worse_path: {decision_counts.get('worse_path', 0)}",
        f"- delayed_entry: {decision_counts.get('delayed_entry', 0)}",
        "",
        "## Decision Counts",
        "",
        "| Decision | Count |",
        "|---|---:|",
    ]
    for decision, count in decision_counts.most_common():
        lines.append(f"| {decision} | {count} |")
    if not decision_counts:
        lines.append("| n/a | 0 |")
    lines.extend([
        "",
        "## Replay Details",
        "",
        "| Source | Symbol | ID | First Time | Baseline Entry | Variant Entry | Baseline Hit | Variant Hit | Baseline MFE_R | Variant MFE_R | Decision | Explanation |",
        "|---|---|---|---|---|---|---|---|---:|---:|---|---|",
    ])
    for row in rows:
        lines.append(
            f"| {row.source} | `{row.symbol}` | `{row.opportunity_id}` | {_local_timestamp(row.first_time)} | "
            f"{_local_timestamp(row.baseline_entry_time or '')} @ {_fmt(row.baseline_entry_price, 6)} | "
            f"{_local_timestamp(row.variant_entry_time or '')} @ {_fmt(row.variant_entry_price, 6)} | "
            f"{row.baseline_first_hit} | {row.variant_first_hit} | {_fmt(row.baseline_mfe_r, 2)} | "
            f"{_fmt(row.variant_mfe_r, 2)} | {row.decision} | {row.explanation} |"
        )
    lines.extend([
        "",
        "## Raw Summary",
        "",
        "```json",
        json.dumps(
            {
                "variant": variant,
                "opportunities": len(rows),
                "baseline_entries": baseline_entries,
                "variant_entries": variant_entries,
                "decisions": dict(decision_counts),
            },
            ensure_ascii=False,
            indent=2,
        ),
        "```",
    ])
    return "\n".join(lines) + "\n"


def write_shadow_replay_report(
    settings: Settings,
    *,
    account_name: str | None,
    start_date: str,
    end_date: str,
    variant: str,
) -> tuple[str, list[Path]]:
    account = account_name or settings.paper.account_name
    if variant != "entry_reclaim_confirm_1bar":
        raise ValueError(f"unsupported shadow replay variant: {variant}")
    rows = build_entry_reclaim_confirm_1bar_shadow(settings, account, start_date, end_date)
    now = _local_now()
    report_dir = settings.output.reports_dir / now.strftime("%Y-%m-%d")
    obsidian_dir = None if settings.output.obsidian_dir is None else settings.output.obsidian_dir / "Reports" / now.strftime("%Y-%m-%d")
    prefix = f"paper_shadow_replay_{variant}_{start_date}_{end_date}_{account}"
    version = next_report_version([report_dir, obsidian_dir], prefix)
    filename = versioned_markdown_filename(prefix, version)
    text = render_shadow_replay_report(
        account=account,
        start_date=start_date,
        end_date=end_date,
        variant=variant,
        report_version=version,
        rows=rows,
    )
    paths: list[Path] = []
    for directory in [report_dir, obsidian_dir]:
        if directory is None:
            continue
        directory.mkdir(parents=True, exist_ok=True)
        out = directory / filename
        out.write_text(text, encoding="utf-8")
        paths.append(out)
    return text, paths
