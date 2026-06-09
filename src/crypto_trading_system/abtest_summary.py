from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
import json
from pathlib import Path
import re
from typing import Any

from .config import Settings
from .report_versions import next_report_version, versioned_markdown_filename


METRIC_NAMES = [
    "trades",
    "closed_trades",
    "win_rate",
    "profit_factor",
    "sharpe",
    "max_drawdown_pct",
    "net_return_pct",
    "stop_rate",
    "avg_r",
]

EPSILON = 1e-9


@dataclass(frozen=True)
class AbtestReportRecord:
    path: Path
    experiment_id: str
    mode: str
    start: str
    end: str
    report_version: str
    verdict: str
    sample_sufficient: bool
    baseline: dict[str, Any]
    variant: dict[str, Any]
    dynamic_metadata: dict[str, str]


@dataclass(frozen=True)
class AbtestAggregateSummary:
    experiment_id: str
    mode: str
    records: list[AbtestReportRecord]
    sufficient_periods: int
    net_improved_periods: int
    profit_factor_improved_periods: int
    drawdown_improved_periods: int
    variant_under_sample_periods: int
    total_period_days: int
    unique_coverage_days: int
    overlap_periods: int
    universe_warnings: list[str]
    verdict: str
    reason: str
    report_paths: list[Path]


def _local_now() -> datetime:
    return datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=8), name="CST"))


def _fmt(value: Any, suffix: str = "") -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float) and value == float("inf"):
        return "inf"
    if isinstance(value, (int, float)):
        return f"{value:,.2f}{suffix}"
    return str(value)


def _metric_value(metrics: dict[str, Any], name: str) -> float | int | None:
    value = metrics.get(name)
    if isinstance(value, (int, float)):
        return value
    return None


def _delta(record: AbtestReportRecord, name: str) -> float | int | None:
    baseline = _metric_value(record.baseline, name)
    variant = _metric_value(record.variant, name)
    if baseline is None or variant is None:
        return None
    return variant - baseline


def _improved(record: AbtestReportRecord, name: str, *, lower_is_better: bool = False) -> bool:
    delta = _delta(record, name)
    if delta is None:
        return False
    if lower_is_better:
        return delta < -EPSILON
    return delta > EPSILON


def _extract_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    output: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        output[key.strip()] = value.strip()
    return output


def _extract_raw_metrics(text: str) -> dict[str, Any]:
    match = re.search(r"```json\s*(\{.*?\})\s*```", text, re.S)
    if not match:
        raise ValueError("A/B report does not contain a JSON metrics block.")
    data = json.loads(match.group(1))
    if not isinstance(data.get("baseline"), dict) or not isinstance(data.get("variant"), dict):
        raise ValueError("A/B report JSON block must contain baseline and variant metric objects.")
    return data


def _extract_dynamic_metadata(text: str) -> dict[str, str]:
    keys = {
        "baseline_master_count",
        "variant_master_count",
        "baseline_source_limit",
        "variant_source_limit",
        "baseline_universe_refreshes",
        "variant_universe_refreshes",
    }
    metadata: dict[str, str] = {}
    for line in text.splitlines():
        match = re.match(r"-\s+([a-z_]+):\s*(.*)$", line)
        if match and match.group(1) in keys:
            metadata[match.group(1)] = match.group(2).strip()
    return metadata


def _parse_report_name(path: Path, experiment_id: str, mode: str) -> tuple[str, str, str] | None:
    prefix = f"abtest_{mode}_{experiment_id}_"
    if not path.name.startswith(prefix) or not path.name.endswith(".md"):
        return None
    rest = path.name[len(prefix) : -3]
    match = re.fullmatch(r"(\d{4}-\d{2}-\d{2})_(\d{4}-\d{2}-\d{2})_v(\d+)", rest)
    if not match:
        return None
    return match.group(1), match.group(2), f"v{match.group(3)}"


def parse_abtest_report(path: Path, experiment_id: str, mode: str) -> AbtestReportRecord | None:
    parsed_name = _parse_report_name(path, experiment_id, mode)
    if parsed_name is None:
        return None
    start, end, report_version = parsed_name
    text = path.read_text(encoding="utf-8")
    frontmatter = _extract_frontmatter(text)
    raw_metrics = _extract_raw_metrics(text)
    dynamic_metadata = _extract_dynamic_metadata(text)
    baseline = raw_metrics["baseline"]
    variant = raw_metrics["variant"]
    sample_sufficient = bool(
        baseline.get("sample_sufficient")
        and variant.get("sample_sufficient")
        and frontmatter.get("sample_sufficient", "true").lower() == "true"
    )
    return AbtestReportRecord(
        path=path,
        experiment_id=frontmatter.get("experiment_id", experiment_id),
        mode=frontmatter.get("universe_mode", mode),
        start=start,
        end=end,
        report_version=report_version,
        verdict=frontmatter.get("verdict", "unknown"),
        sample_sufficient=sample_sufficient,
        baseline=baseline,
        variant=variant,
        dynamic_metadata=dynamic_metadata,
    )


def load_abtest_records(
    reports_dir: Path,
    experiment_id: str,
    mode: str,
    *,
    start: str | None = None,
    end: str | None = None,
) -> list[AbtestReportRecord]:
    if not reports_dir.exists():
        raise ValueError(f"Reports directory does not exist: {reports_dir}")
    records: list[AbtestReportRecord] = []
    for path in sorted(reports_dir.glob("abtest_*.md")):
        record = parse_abtest_report(path, experiment_id, mode)
        if record is None:
            continue
        if start is not None and record.start < start:
            continue
        if end is not None and record.end > end:
            continue
        records.append(record)
    return records


def select_non_overlapping_records(records: list[AbtestReportRecord]) -> list[AbtestReportRecord]:
    """Keep the largest set of non-overlapping periods, preferring earlier-ending windows."""
    selected: list[AbtestReportRecord] = []
    latest_end: date | None = None
    for record in sorted(records, key=lambda item: (_period_dates(item)[1], _period_dates(item)[0], item.path.name)):
        start, end = _period_dates(record)
        if latest_end is not None and start < latest_end:
            continue
        selected.append(record)
        latest_end = end
    return selected


def _summary_verdict(records: list[AbtestReportRecord]) -> tuple[str, str]:
    if not records:
        return "no_data", "No matching A/B reports were found."
    overlap_periods = _overlap_period_count(records)
    if overlap_periods:
        return "retest", "Some periods overlap, so the evidence is not fully independent."
    if any(not bool(record.variant.get("sample_sufficient")) for record in records):
        return "retest", "At least one variant period is below the closed-trade sample threshold."
    sufficient = [record for record in records if record.sample_sufficient]
    if not sufficient:
        return "retest", "No period has sufficient baseline and variant closed trades."

    net_improved = sum(1 for record in sufficient if _improved(record, "net_return_pct"))
    pf_improved = sum(1 for record in sufficient if _improved(record, "profit_factor"))
    drawdown_improved = sum(1 for record in sufficient if _improved(record, "max_drawdown_pct", lower_is_better=True))
    if net_improved == len(sufficient) and pf_improved == len(sufficient) and drawdown_improved == len(sufficient):
        return "candidate_keep_review", "All sufficient periods improved net return, Profit factor, and max drawdown; manual review is still required."
    if net_improved == 0 and pf_improved == 0:
        return "reject_candidate", "No sufficient period improved net return or Profit factor."
    return "retest", "Results are mixed or sample coverage is incomplete; continue cross-period testing."


def _period_dates(record: AbtestReportRecord) -> tuple[date, date]:
    return date.fromisoformat(record.start), date.fromisoformat(record.end)


def _period_days(record: AbtestReportRecord) -> int:
    start, end = _period_dates(record)
    return (end - start).days


def _unique_coverage_days(records: list[AbtestReportRecord]) -> int:
    if not records:
        return 0
    intervals = sorted(_period_dates(record) for record in records)
    merged: list[list[date]] = []
    for start, end in intervals:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
            continue
        if end > merged[-1][1]:
            merged[-1][1] = end
    return sum((end - start).days for start, end in merged)


def _overlap_period_count(records: list[AbtestReportRecord]) -> int:
    intervals = sorted(_period_dates(record) for record in records)
    overlaps = 0
    latest_end: date | None = None
    for start, end in intervals:
        if latest_end is not None and start < latest_end:
            overlaps += 1
        if latest_end is None or end > latest_end:
            latest_end = end
    return overlaps


def _source_limit_present(value: str | None) -> bool:
    return value is not None and value.lower() not in {"", "none", "n/a", "null"}


def _universe_warnings(records: list[AbtestReportRecord], mode: str) -> list[str]:
    warnings: list[str] = []
    if mode == "dynamic_universe" or any(record.mode == "dynamic" for record in records):
        warnings.append(
            "Dynamic universe uses current Binance exchangeInfo as the symbol master; historic delisted symbols may be missing."
        )
    source_limited = [
        record
        for record in records
        if _source_limit_present(record.dynamic_metadata.get("baseline_source_limit"))
        or _source_limit_present(record.dynamic_metadata.get("variant_source_limit"))
    ]
    if source_limited:
        warnings.append(
            f"{len(source_limited)}/{len(records)} periods used source_limit; rerun with a larger or uncapped master before keep review."
        )
    return warnings


def build_abtest_summary(
    records: list[AbtestReportRecord],
    experiment_id: str,
    mode: str,
) -> AbtestAggregateSummary:
    sufficient_periods = sum(1 for record in records if record.sample_sufficient)
    net_improved_periods = sum(1 for record in records if record.sample_sufficient and _improved(record, "net_return_pct"))
    profit_factor_improved_periods = sum(
        1 for record in records if record.sample_sufficient and _improved(record, "profit_factor")
    )
    drawdown_improved_periods = sum(
        1 for record in records if record.sample_sufficient and _improved(record, "max_drawdown_pct", lower_is_better=True)
    )
    variant_under_sample_periods = sum(1 for record in records if not bool(record.variant.get("sample_sufficient")))
    total_period_days = sum(_period_days(record) for record in records)
    unique_coverage_days = _unique_coverage_days(records)
    overlap_periods = _overlap_period_count(records)
    universe_warnings = _universe_warnings(records, mode)
    verdict, reason = _summary_verdict(records)
    return AbtestAggregateSummary(
        experiment_id=experiment_id,
        mode=mode,
        records=records,
        sufficient_periods=sufficient_periods,
        net_improved_periods=net_improved_periods,
        profit_factor_improved_periods=profit_factor_improved_periods,
        drawdown_improved_periods=drawdown_improved_periods,
        variant_under_sample_periods=variant_under_sample_periods,
        total_period_days=total_period_days,
        unique_coverage_days=unique_coverage_days,
        overlap_periods=overlap_periods,
        universe_warnings=universe_warnings,
        verdict=verdict,
        reason=reason,
        report_paths=[],
    )


def render_abtest_summary_report(summary: AbtestAggregateSummary, report_version: str) -> str:
    now = _local_now()
    lines = [
        "---",
        f"created: {now.strftime('%Y-%m-%d %H:%M:%S %Z')}",
        "tags:",
        "  - crypto",
        "  - trading-system",
        "  - abtest-summary",
        f"experiment_id: {summary.experiment_id}",
        f"mode: {summary.mode}",
        f"periods: {len(summary.records)}",
        f"sufficient_periods: {summary.sufficient_periods}",
        f"unique_coverage_days: {summary.unique_coverage_days}",
        f"overlap_periods: {summary.overlap_periods}",
        f"universe_warnings: {len(summary.universe_warnings)}",
        f"verdict: {summary.verdict}",
        f"report_version: {report_version}",
        "---",
        "",
        f"# A/B 多时段汇总 {summary.experiment_id} {report_version}",
        "",
        f"- experiment_id: `{summary.experiment_id}`",
        f"- mode: `{summary.mode}`",
        f"- periods: {len(summary.records)}",
        f"- sufficient_periods: {summary.sufficient_periods}",
        f"- total_period_days: {summary.total_period_days}",
        f"- unique_coverage_days: {summary.unique_coverage_days}",
        f"- overlap_periods: {summary.overlap_periods}",
        f"- universe_warnings: {len(summary.universe_warnings)}",
        f"- net_improved_periods: {summary.net_improved_periods}",
        f"- profit_factor_improved_periods: {summary.profit_factor_improved_periods}",
        f"- drawdown_improved_periods: {summary.drawdown_improved_periods}",
        f"- variant_under_sample_periods: {summary.variant_under_sample_periods}",
        f"- verdict: `{summary.verdict}`",
        f"- reason: {summary.reason}",
        "",
        "## Period Results",
        "",
        "| Period | Sample | Closed B -> V | Win B -> V | PF B -> V | Sharpe B -> V | MDD B -> V | Net B -> V | Stop B -> V | Verdict |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for record in summary.records:
        period = f"{record.start} -> {record.end}"
        baseline = record.baseline
        variant = record.variant
        lines.append(
            "| "
            + " | ".join(
                [
                    period,
                    "yes" if record.sample_sufficient else "no",
                    f"{_fmt(baseline.get('closed_trades'))} -> {_fmt(variant.get('closed_trades'))}",
                    f"{_fmt(baseline.get('win_rate'), '%')} -> {_fmt(variant.get('win_rate'), '%')}",
                    f"{_fmt(baseline.get('profit_factor'))} -> {_fmt(variant.get('profit_factor'))}",
                    f"{_fmt(baseline.get('sharpe'))} -> {_fmt(variant.get('sharpe'))}",
                    f"{_fmt(baseline.get('max_drawdown_pct'), '%')} -> {_fmt(variant.get('max_drawdown_pct'), '%')}",
                    f"{_fmt(baseline.get('net_return_pct'), '%')} -> {_fmt(variant.get('net_return_pct'), '%')}",
                    f"{_fmt(baseline.get('stop_rate'), '%')} -> {_fmt(variant.get('stop_rate'), '%')}",
                    record.verdict,
                ]
            )
            + " |"
        )

    lines.extend(["", "## Universe Bias Checks", ""])
    if summary.universe_warnings:
        lines.extend(f"- {warning}" for warning in summary.universe_warnings)
    else:
        lines.append("- No dynamic-universe bias warnings were detected from the source reports.")

    lines.extend(
        [
            "",
            "## Source Reports",
            "",
        ]
    )
    for record in summary.records:
        lines.append(f"- `{record.path}`")

    lines.extend(
        [
            "",
            "## Decision Rule",
            "",
            "- 汇总报告只给出 `candidate_keep_review`、`retest` 或 `reject_candidate`，不会自动修改默认配置。",
            "- 至少需要多个充足样本时段共同改善净收益、Profit factor 和最大回撤，才会标记 `candidate_keep_review`。",
            "- 时段存在重叠时，证据不视为完全独立，结论保持 `retest`。",
            "- 任一 variant 样本不足时，结论应偏向 `retest`。",
            "",
            "## Raw Summary",
            "",
            "```json",
            json.dumps(
                {
                    "experiment_id": summary.experiment_id,
                    "mode": summary.mode,
                    "periods": len(summary.records),
                    "sufficient_periods": summary.sufficient_periods,
                    "total_period_days": summary.total_period_days,
                    "unique_coverage_days": summary.unique_coverage_days,
                    "overlap_periods": summary.overlap_periods,
                    "universe_warnings": summary.universe_warnings,
                    "net_improved_periods": summary.net_improved_periods,
                    "profit_factor_improved_periods": summary.profit_factor_improved_periods,
                    "drawdown_improved_periods": summary.drawdown_improved_periods,
                    "variant_under_sample_periods": summary.variant_under_sample_periods,
                    "verdict": summary.verdict,
                    "reason": summary.reason,
                    "records": [
                        {
                            "path": str(record.path),
                            "start": record.start,
                            "end": record.end,
                            "sample_sufficient": record.sample_sufficient,
                            "dynamic_metadata": record.dynamic_metadata,
                            "baseline": record.baseline,
                            "variant": record.variant,
                        }
                        for record in summary.records
                    ],
                },
                ensure_ascii=False,
                indent=2,
                default=str,
            ),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def _project_report_dir(settings: Settings, report_date: str) -> Path:
    return settings.output.reports_dir / report_date


def _obsidian_report_dir(settings: Settings, report_date: str) -> Path | None:
    if settings.output.obsidian_dir is None:
        return None
    return settings.output.obsidian_dir / "Reports" / report_date


def write_abtest_summary_report(
    settings: Settings,
    summary: AbtestAggregateSummary,
    *,
    report_date: str | None = None,
    include_obsidian: bool = True,
) -> AbtestAggregateSummary:
    report_date = report_date or _local_now().strftime("%Y-%m-%d")
    target_dirs = [_project_report_dir(settings, report_date)]
    obsidian_dir = _obsidian_report_dir(settings, report_date)
    if include_obsidian and obsidian_dir is not None:
        target_dirs.append(obsidian_dir)
    prefix = f"abtest_summary_{summary.mode}_{summary.experiment_id}_{report_date}"
    version_number = next_report_version(target_dirs, prefix)
    version = f"v{version_number}"
    filename = versioned_markdown_filename(prefix, version_number)
    markdown = render_abtest_summary_report(summary, version)
    paths: list[Path] = []
    for directory in target_dirs:
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / filename
        path.write_text(markdown, encoding="utf-8")
        paths.append(path)
    return AbtestAggregateSummary(
        experiment_id=summary.experiment_id,
        mode=summary.mode,
        records=summary.records,
        sufficient_periods=summary.sufficient_periods,
        net_improved_periods=summary.net_improved_periods,
        profit_factor_improved_periods=summary.profit_factor_improved_periods,
        drawdown_improved_periods=summary.drawdown_improved_periods,
        variant_under_sample_periods=summary.variant_under_sample_periods,
        total_period_days=summary.total_period_days,
        unique_coverage_days=summary.unique_coverage_days,
        overlap_periods=summary.overlap_periods,
        universe_warnings=summary.universe_warnings,
        verdict=summary.verdict,
        reason=summary.reason,
        report_paths=paths,
    )
