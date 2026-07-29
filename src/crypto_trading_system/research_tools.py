from __future__ import annotations

from collections import Counter
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
import hashlib
import inspect
import json
from pathlib import Path
import random
import sqlite3
import subprocess

from .backtest.universe import SymbolMaster, load_symbol_master, save_symbol_master
from .config import Settings
from .database import connect_db
from .paper_trader import CLOSED_STATUSES, OPEN_STATUSES, load_all_paper_trades, load_paper_events
from .report_versions import next_report_version, versioned_markdown_filename


LARGE_CAP_SYMBOLS = ("BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT")


@dataclass(frozen=True)
class SignalFillTimingAudit:
    run_id: str
    report_date: str
    start_utc: str
    end_utc: str
    commit_hash: str
    symbols_count: int
    entry_reclaim_close_enabled: bool | None
    entry_reclaim_min_atr_enabled: bool | None
    entry_reclaim_min_atr: float | None
    max_active_positions: int | None
    intrabar_policy: str | None
    maker_fee_bps: float | None
    taker_fee_bps: float | None
    entry_slippage_bps: float | None
    stop_slippage_bps: float | None
    entered_trades: int
    same_bar_entry_and_exit_trades: int
    same_bar_entry_and_tp1_trades: int
    blocked_notes_persisted: int
    verdict: str
    reason: str


@dataclass(frozen=True)
class BlockedEntryEventExport:
    source_run_id: str
    replay_run_id: str
    report_date: str
    start_utc: str
    end_utc: str
    source_commit_hash: str
    source_symbols_count: int
    replay_symbols_count: int
    source_entered_trades: int
    replay_entered_trades: int
    dynamic_universe_mode: bool
    max_universe_symbols: int | None
    max_active_positions: int | None
    event_count: int
    same_bar_entry_exit_possible_events: int
    same_bar_entry_tp1_possible_events: int
    events_by_month: dict[str, int]
    events_by_symbol_top: list[tuple[str, int]]
    verdict: str
    reason: str
    events: list[dict]


@dataclass(frozen=True)
class ReplayConsistencyAudit:
    source_run_id: str
    replay_run_id: str
    report_date: str
    start_utc: str
    end_utc: str
    source_commit_hash: str
    source_trade_count: int
    replay_trade_count: int
    source_entered_trades: int
    replay_entered_trades: int
    source_closed_trades: int
    replay_closed_trades: int
    entered_signature_mismatches: int
    active_path_points: int
    active_path_mismatches: int
    open_plan_path_mismatches: int
    final_equity_delta: float
    blocked_events_json: str | None
    blocked_events_reference_count: int | None
    blocked_events_replay_count: int
    blocked_event_signature_mismatches: int | None
    candidate_ordering_evidence: str
    ordering_directly_persisted_in_source: bool
    verdict: str
    reason: str
    entered_mismatch_examples: list[dict]
    active_path_mismatch_examples: list[dict]
    blocked_event_mismatch_examples: list[dict]


@dataclass(frozen=True)
class StaleSlotObservation:
    trade_id: str
    symbol: str
    entered_at_utc: str
    stale_time_utc: str
    closed_at_utc: str | None
    tp1_hit_at_utc: str | None
    final_status: str
    entry_price: float
    stop_loss: float
    take_profit_1: float
    stale_close: float
    risk_per_unit: float
    forward_r_24: float | None
    forward_r_42: float | None
    forward_r_60: float | None
    eventual_continuation_r: float | None
    mfe_r_after_stale: float | None
    mae_r_after_stale: float | None
    first_hit_outcome_after_stale: str
    first_hit_time_utc: str | None
    right_censored: bool
    horizon_24_censored: bool
    horizon_42_censored: bool
    horizon_60_censored: bool


@dataclass(frozen=True)
class StaleSlotContinuationReview:
    source_run_id: str
    replay_run_id: str
    report_date: str
    start_utc: str
    end_utc: str
    source_commit_hash: str
    stale_bars: int
    stale_hours: int
    total_entered_trades: int
    eligible_pre_tp1_stale_slots: int
    excluded_tp1_before_stale: int
    excluded_closed_before_stale: int
    excluded_insufficient_price_data: int
    right_censored_count: int
    first_hit_outcomes: dict[str, int]
    forward_r_24_summary: dict[str, float | int | None]
    forward_r_42_summary: dict[str, float | int | None]
    forward_r_60_summary: dict[str, float | int | None]
    eventual_continuation_r_summary: dict[str, float | int | None]
    mfe_r_summary: dict[str, float | int | None]
    mae_r_summary: dict[str, float | int | None]
    verdict: str
    reason: str
    observations: list[StaleSlotObservation]


@dataclass(frozen=True)
class ReplacementPathOutcome:
    r_24: float | None
    r_42: float | None
    r_60: float | None
    first_hit_outcome: str
    first_hit_time_utc: str | None
    mfe_r: float | None
    mae_r: float | None
    right_censored: bool


@dataclass(frozen=True)
class BlockedCandidateVsStaleSlotEvent:
    event_id: str
    decision_time_utc: str
    month: str
    candidate_symbol: str
    candidate_rank: int
    selected_slot_trade_id: str
    selected_slot_symbol: str
    selected_slot_holding_bars: int
    eligible_stale_slots: int
    candidate_same_bar_stop_possible: bool
    candidate_same_bar_tp1_possible: bool
    candidate_r_42: float | None
    stale_slot_r_42: float | None
    net_replacement_delta_r_42: float | None
    net_replacement_delta_r_24: float | None
    net_replacement_delta_r_60: float | None
    lowest_unrealized_slot_delta_r_42: float | None
    oracle_upper_bound_delta_r_42: float | None
    candidate_first_hit: str
    stale_slot_first_hit: str
    right_censored: bool


@dataclass(frozen=True)
class BlockedCandidateVsStaleSlotReview:
    source_run_id: str
    replay_run_id: str
    report_date: str
    start_utc: str
    end_utc: str
    source_commit_hash: str
    stale_bars: int
    total_blocked_events: int
    rank1_blocked_events: int
    eligible_comparison_events: int
    rank1_without_eligible_stale_slot: int
    same_bar_stop_possible_events: int
    same_bar_tp1_possible_events: int
    right_censored_count: int
    net_delta_r_24_summary: dict[str, float | int | None]
    net_delta_r_42_summary: dict[str, float | int | None]
    net_delta_r_60_summary: dict[str, float | int | None]
    lowest_unrealized_delta_r_42_summary: dict[str, float | int | None]
    oracle_upper_bound_delta_r_42_summary: dict[str, float | int | None]
    first_hit_pair_counts: dict[str, int]
    month_leave_one_out_mean_r_42: dict[str, float | None]
    top_contribution_share_r_42: dict[str, float | int | None]
    verdict: str
    reason: str
    events: list[BlockedCandidateVsStaleSlotEvent]


@dataclass(frozen=True)
class ReplacementClosureAudit:
    source_run_id: str
    replay_run_id: str
    report_date: str
    stage1_json_path: str
    stage4_report_path: str
    start_utc: str
    end_utc: str
    total_blocked_events: int
    unique_blocked_timestamps: int
    rank1_blocked_events: int
    unique_rank1_timestamps: int
    eligible_comparison_events: int
    unique_comparison_timestamps: int
    unique_comparison_candidates: int
    unique_stale_trades: int
    stale_trade_duplicate_counts: dict[str, int]
    stale_trade_top1_share_pct: float | None
    stale_trade_top3_share_pct: float | None
    first_event_per_stale_trade_summaries: dict[str, dict[str, float | int | None]]
    exclude_2025_07_summaries: dict[str, dict[str, float | int | None]]
    exclude_same_bar_ambiguous_summaries: dict[str, dict[str, float | int | None]]
    cluster_bootstrap_mean_r_42: dict[str, float | int | None]
    top_contribution_share_r_42: dict[str, float | int | None]
    verdict: str
    reason: str


@dataclass(frozen=True)
class AtrReclaimN0ReadinessAudit:
    experiment_id: str
    report_date: str
    start_utc: str
    end_utc: str
    symbol_master_path: str
    symbol_master_source: str
    symbol_master_created_at_utc: str
    symbol_master_hash: str
    settings_hash: str
    experiments_hash: str
    git_commit: str
    git_dirty: bool
    baseline_config_snapshot: dict
    variant_overrides: dict
    fixed_conditions: dict
    symbol_master_count: int
    listing_dates_present: bool
    listed_after_start_count: int | None
    listed_after_start_examples: list[str]
    missing_listing_dates_count: int | None
    kline_coverage: dict[str, dict[str, int | float | str | list[str]]]
    prior_third_window_abtests: list[str]
    opportunity_alignment_fields: dict[str, bool]
    readiness_checks: dict[str, str]
    verdict: str
    reason: str


def _local_now() -> datetime:
    return datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=8), name="CST"))


def _local_date(timestamp_utc: str) -> str:
    return datetime.fromisoformat(timestamp_utc).astimezone(timezone(timedelta(hours=8), name="CST")).strftime("%Y-%m-%d")


def _local_timestamp(timestamp_utc: str) -> str:
    return datetime.fromisoformat(timestamp_utc).astimezone(timezone(timedelta(hours=8), name="CST")).strftime("%Y-%m-%d %H:%M:%S %Z")


def _parse_utc(timestamp: str) -> datetime:
    return datetime.fromisoformat(timestamp.replace("Z", "+00:00"))


def split_symbol_master_by_cap(
    input_path: Path,
    output_dir: Path | None = None,
    *,
    large_cap_symbols: tuple[str, ...] = LARGE_CAP_SYMBOLS,
) -> tuple[Path, Path]:
    master = load_symbol_master(input_path)
    output_dir = output_dir or input_path.parent
    large_set = set(large_cap_symbols)
    large_symbols = [symbol for symbol in master.symbols if symbol in large_set]
    alt_symbols = [symbol for symbol in master.symbols if symbol not in large_set]

    def subset(symbols: list[str], label: str) -> SymbolMaster:
        listing_dates = None
        if master.listing_dates is not None:
            listing_dates = {symbol: master.listing_dates[symbol] for symbol in symbols if symbol in master.listing_dates}
        return SymbolMaster(
            source=f"{master.source}; cap_split={label}",
            created_at_utc=datetime.now(timezone.utc).isoformat(timespec="seconds"),
            symbols=symbols,
            source_limit=None,
            source_limit_applied=False,
            filters=f"{master.filters}; cap_split={label}; large_cap_symbols={','.join(large_cap_symbols)}",
            listing_dates=listing_dates,
        )

    stem = input_path.stem
    large_path = output_dir / f"{stem}_large_cap.json"
    alt_path = output_dir / f"{stem}_altcoin.json"
    save_symbol_master(subset(large_symbols, "large_cap"), large_path)
    save_symbol_master(subset(alt_symbols, "altcoin"), alt_path)
    return large_path, alt_path


@dataclass(frozen=True)
class ExperimentIndexSource:
    path: Path
    report_type: str
    experiment_id: str
    start: str
    end: str
    changed_param: str
    old_value: str
    new_value: str
    verdict: str
    sample_sufficient: str
    reason: str
    next_action: str
    periods: int
    sufficient_periods: int
    created: str
    report_version: int


@dataclass(frozen=True)
class ExperimentIndexEntry:
    experiment_id: str
    source: ExperimentIndexSource
    evidence_paths: tuple[Path, ...]


def _frontmatter(text: str) -> dict[str, str]:
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


def _extract_raw_json(text: str, heading: str) -> dict:
    marker = f"## {heading}"
    start = text.find(marker)
    if start == -1:
        return {}
    fence_start = text.find("```json", start)
    if fence_start == -1:
        return {}
    json_start = text.find("\n", fence_start)
    fence_end = text.find("```", json_start + 1)
    if json_start == -1 or fence_end == -1:
        return {}
    try:
        parsed = json.loads(text[json_start + 1 : fence_end])
    except json.JSONDecodeError:
        return {}
    return parsed if isinstance(parsed, dict) else {}


def _bullet_value(text: str, key: str) -> str:
    prefix = f"- {key}:"
    for line in text.splitlines():
        if line.startswith(prefix):
            return line[len(prefix) :].strip().strip("`")
    return ""


def _report_version(fm: dict[str, str]) -> int:
    raw = fm.get("report_version", "v0").strip().lstrip("vV")
    return int(raw) if raw.isdigit() else 0


def _created_value(fm: dict[str, str]) -> str:
    return fm.get("created", "")


def _infer_period(path: Path) -> tuple[str, str]:
    parts = path.stem.split("_")
    dates = [part for part in parts if len(part) == 10 and part[4] == "-" and part[7] == "-"]
    if len(dates) >= 2:
        return dates[-2], dates[-1]
    return "n/a", "n/a"


def _format_period(start: str, end: str) -> str:
    if start == "n/a" and end == "n/a":
        return "n/a"
    return f"{start} -> {end}"


def _change_summary(changed_param: str, old_value: str, new_value: str) -> str:
    if not changed_param or changed_param == "n/a":
        return "n/a"
    if old_value and new_value:
        return f"`{changed_param}`: `{old_value}` -> `{new_value}`"
    return f"`{changed_param}`"


def _rel_report_path(path: Path, reports_dir: Path) -> Path:
    try:
        return path.relative_to(reports_dir)
    except ValueError:
        return path


def _next_action(verdict: str, sample_sufficient: str) -> str:
    if verdict == "candidate_keep_review":
        return "人工复核后决定是否 keep"
    if verdict == "reject_candidate":
        return "不要纳入默认策略"
    if sample_sufficient.lower() == "false":
        return "补样本或拉长区间后 retest"
    if verdict in {"retest", "no_data", "unknown"}:
        return "继续跨区间 retest"
    return "复核报告细节"


def _source_rank(source: ExperimentIndexSource) -> tuple[int, str, int]:
    priority = {"review": 3, "summary": 2, "abtest": 1}.get(source.report_type, 0)
    return priority, source.created, source.report_version


def _path_from_report_value(value: str, reports_dir: Path) -> Path | None:
    if not value:
        return None
    path = Path(value)
    if path.exists():
        return path
    candidate = reports_dir / value
    if candidate.exists():
        return candidate
    return None


def _abtest_change_from_path(path: Path | None) -> tuple[str, str, str]:
    if path is None or not path.exists():
        return "n/a", "", ""
    fm = _frontmatter(path.read_text(encoding="utf-8"))
    return fm.get("changed_param", "n/a"), fm.get("old_value", ""), fm.get("new_value", "")


def _build_review_source(path: Path, text: str) -> ExperimentIndexSource | None:
    fm = _frontmatter(text)
    experiment_id = fm.get("experiment_id") or fm.get("experiment")
    if not experiment_id:
        return None
    verdict = fm.get("verdict", "unknown")
    sample = fm.get("sample_sufficient", "unknown")
    return ExperimentIndexSource(
        path=path,
        report_type="review",
        experiment_id=experiment_id,
        start=fm.get("start", "n/a"),
        end=fm.get("end", "n/a"),
        changed_param=fm.get("changed_param", "n/a"),
        old_value=fm.get("old_value", ""),
        new_value=fm.get("new_value", ""),
        verdict=verdict,
        sample_sufficient=sample,
        reason=fm.get("reason", ""),
        next_action=fm.get("next_action") or _next_action(verdict, sample),
        periods=int(fm.get("periods", "0") or 0),
        sufficient_periods=int(fm.get("sufficient_periods", "0") or 0),
        created=_created_value(fm),
        report_version=_report_version(fm),
    )


def _build_summary_source(path: Path, text: str, reports_dir: Path) -> ExperimentIndexSource | None:
    fm = _frontmatter(text)
    experiment_id = fm.get("experiment_id")
    if not experiment_id:
        return None
    raw = _extract_raw_json(text, "Raw Summary")
    records = raw.get("records", []) if isinstance(raw.get("records"), list) else []
    starts = [str(record.get("start")) for record in records if record.get("start")]
    ends = [str(record.get("end")) for record in records if record.get("end")]
    start = min(starts) if starts else "n/a"
    end = max(ends) if ends else "n/a"
    source_reports = [record.get("path", "") for record in records if isinstance(record, dict)]
    first_report = _path_from_report_value(str(source_reports[0]), reports_dir) if source_reports else None
    changed_param, old_value, new_value = _abtest_change_from_path(first_report)
    verdict = fm.get("verdict", str(raw.get("verdict", "unknown")))
    sample = "true" if str(fm.get("variant_under_sample_periods", raw.get("variant_under_sample_periods", 0))) == "0" else "false"
    reason = str(raw.get("reason") or _bullet_value(text, "reason"))
    return ExperimentIndexSource(
        path=path,
        report_type="summary",
        experiment_id=experiment_id,
        start=start,
        end=end,
        changed_param=changed_param,
        old_value=old_value,
        new_value=new_value,
        verdict=verdict,
        sample_sufficient=sample,
        reason=reason,
        next_action=fm.get("next_action") or _next_action(verdict, sample),
        periods=int(fm.get("periods", raw.get("periods", 0)) or 0),
        sufficient_periods=int(fm.get("sufficient_periods", raw.get("sufficient_periods", 0)) or 0),
        created=_created_value(fm),
        report_version=_report_version(fm),
    )


def _build_abtest_source(path: Path, text: str) -> ExperimentIndexSource | None:
    fm = _frontmatter(text)
    experiment_id = fm.get("experiment_id")
    if not experiment_id:
        return None
    start, end = _infer_period(path)
    verdict = fm.get("verdict", "unknown")
    sample = fm.get("sample_sufficient", "unknown")
    return ExperimentIndexSource(
        path=path,
        report_type="abtest",
        experiment_id=experiment_id,
        start=start,
        end=end,
        changed_param=fm.get("changed_param", "n/a"),
        old_value=fm.get("old_value", ""),
        new_value=fm.get("new_value", ""),
        verdict=verdict,
        sample_sufficient=sample,
        reason=_bullet_value(text, "reason"),
        next_action=fm.get("next_action") or _next_action(verdict, sample),
        periods=1,
        sufficient_periods=1 if sample.lower() == "true" else 0,
        created=_created_value(fm),
        report_version=_report_version(fm),
    )


def _experiment_index_sources(root: Path) -> list[ExperimentIndexSource]:
    sources: list[ExperimentIndexSource] = []
    for path in sorted(root.glob("**/*.md")):
        source: ExperimentIndexSource | None = None
        text = path.read_text(encoding="utf-8")
        if path.name.startswith("abtest_summary_"):
            source = _build_summary_source(path, text, root)
        elif path.name.startswith("abtest_"):
            source = _build_abtest_source(path, text)
        elif path.name.endswith(".md") and "_review_" in path.name:
            source = _build_review_source(path, text)
        if source is not None:
            sources.append(source)
    return sources


def _experiment_index_entries(root: Path) -> list[ExperimentIndexEntry]:
    grouped: dict[str, list[ExperimentIndexSource]] = {}
    for source in _experiment_index_sources(root):
        grouped.setdefault(source.experiment_id, []).append(source)
    entries: list[ExperimentIndexEntry] = []
    for experiment_id, sources in grouped.items():
        selected = sorted(sources, key=_source_rank, reverse=True)[0]
        evidence = tuple(source.path for source in sorted(sources, key=_source_rank, reverse=True)[:5])
        entries.append(ExperimentIndexEntry(experiment_id=experiment_id, source=selected, evidence_paths=evidence))
    return sorted(entries, key=lambda entry: (entry.source.verdict, entry.experiment_id))


def build_experiment_index(settings: Settings, reports_dir: Path | None = None) -> tuple[str, list[Path]]:
    root = reports_dir or settings.output.reports_dir
    entries = _experiment_index_entries(root)

    now = _local_now()
    report_dir = settings.output.reports_dir / now.strftime("%Y-%m-%d")
    obsidian_dir = None if settings.output.obsidian_dir is None else settings.output.obsidian_dir / "Reports" / now.strftime("%Y-%m-%d")
    version = next_report_version([report_dir, obsidian_dir], f"experiment_index_{now.strftime('%Y-%m-%d')}")
    filename = versioned_markdown_filename(f"experiment_index_{now.strftime('%Y-%m-%d')}", version)
    lines = [
        "---",
        f"created: {now.strftime('%Y-%m-%d %H:%M:%S %Z')}",
        "tags:",
        "  - crypto",
        "  - trading-system",
        "  - experiment-index",
        f"report_version: v{version}",
        "---",
        "",
        f"# 实验结论索引 {now.strftime('%Y-%m-%d')} v{version}",
        "",
        "数据源：仅扫描项目 `reports/`；Obsidian 只作为输出目标，不作为输入源。`candidate_keep_review` 仍需人工决策，不会自动等同于 keep。",
        "",
        "## 需要关注",
        "",
        "| Experiment | Verdict | Reason | Next Action | Evidence |",
        "|---|---|---|---|---|",
    ]
    attention = [entry for entry in entries if entry.source.verdict in {"candidate_keep_review", "reject_candidate"}]
    if attention:
        for entry in attention:
            source = entry.source
            rel = _rel_report_path(source.path, settings.output.reports_dir)
            lines.append(
                f"| `{entry.experiment_id}` | {source.verdict} | {source.reason or 'n/a'} | "
                f"{source.next_action} | `{rel}` |"
            )
    else:
        lines.append("| n/a | n/a | 当前没有 candidate_keep_review 或 reject_candidate | n/a | n/a |")
    lines.extend(
        [
            "",
            "## 完整索引",
            "",
            "| Experiment | Source | Period | Change | Windows | Sufficient | Verdict | Reason | Next Action | Evidence |",
            "|---|---|---|---|---:|---:|---|---|---|---|",
        ]
    )
    for entry in entries:
        source = entry.source
        evidence = "<br>".join(f"`{_rel_report_path(path, settings.output.reports_dir)}`" for path in entry.evidence_paths)
        lines.append(
            f"| `{entry.experiment_id}` | {source.report_type} | {_format_period(source.start, source.end)} | "
            f"{_change_summary(source.changed_param, source.old_value, source.new_value)} | {source.periods} | "
            f"{source.sufficient_periods} | {source.verdict} | {source.reason or 'n/a'} | {source.next_action} | {evidence} |"
        )
    if not entries:
        lines.append("| n/a | n/a | n/a | n/a | 0 | 0 | no_data | n/a | 先运行 A/B 实验 | n/a |")
    text = "\n".join(lines) + "\n"

    paths: list[Path] = []
    for directory in [report_dir, obsidian_dir]:
        if directory is None:
            continue
        directory.mkdir(parents=True, exist_ok=True)
        out = directory / filename
        out.write_text(text, encoding="utf-8")
        paths.append(out)
    return text, paths


def _event_time(event) -> datetime:
    return datetime.fromisoformat(event.event_time_utc)


def _reclaim_follow_up(trade, events) -> str:
    pending = [
        event for event in events if event.event_type in {"RECLAIM_PENDING", "RECLAIM_PENDING_SET"}
    ]
    if not pending:
        return "n/a"
    first_time = _event_time(pending[0])
    later = [event for event in events if _event_time(event) > first_time]
    if any(event.event_type in {"ENTERED", "RECLAIM_CONFIRMED_ENTERED"} for event in later):
        return "reclaimed_entered"
    if any(event.event_type in {"INVALIDATED", "STOPPED"} for event in later):
        return "fell_below_stop_or_invalidated"
    if trade.last_price is not None and trade.last_price <= trade.stop_loss:
        return "fell_below_stop_or_invalidated"
    if trade.status == "WATCHING":
        return "still_waiting"
    if trade.status in CLOSED_STATUSES:
        return trade.status.lower()
    return "still_invalid"


def _scan_action_summary(settings: Settings) -> tuple[Counter, Counter]:
    action_counter: Counter = Counter()
    risk_off_counter: Counter = Counter()
    if not settings.output.database_path.exists():
        return action_counter, risk_off_counter
    today = _local_now().strftime("%Y-%m-%d")
    with connect_db(settings.output.database_path) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            """
            SELECT c.payload_json
            FROM scan_candidates c
            JOIN scan_runs r ON c.scan_id = r.scan_id
            WHERE date(r.timestamp_utc, '+8 hours') = ?
            """,
            (today,),
        ).fetchall()
    for row in rows:
        payload = json.loads(row["payload_json"])
        action = str(payload.get("action", "UNKNOWN"))
        action_counter[action] += 1
        haystack = " ".join(
            [
                str(payload.get("setup", "")),
                str(payload.get("verdict", "")),
                " ".join(str(item) for item in payload.get("risks", [])),
            ]
        ).upper()
        if "RISK_OFF" in haystack or "大盘环境未确认强势" in haystack:
            risk_off_counter[action] += 1
    return action_counter, risk_off_counter


def _run_health_summary(settings: Settings, now_utc: datetime) -> dict:
    since = (now_utc - timedelta(hours=24)).isoformat(timespec="seconds").replace("+00:00", "Z")
    with connect_db(settings.output.database_path) as connection:
        connection.row_factory = sqlite3.Row
        recent_rows = connection.execute(
            """
            SELECT run_type, status, COUNT(*) AS count
            FROM runs
            WHERE started_at >= ? AND run_type IN ('daily_full', 'paper_4h_update')
            GROUP BY run_type, status
            """,
            (since,),
        ).fetchall()
        latest_rows = connection.execute(
            """
            SELECT r.*
            FROM runs r
            JOIN (
                SELECT run_type, MAX(started_at) AS max_started
                FROM runs
                WHERE run_type IN ('daily_full', 'paper_4h_update')
                GROUP BY run_type
            ) latest
              ON r.run_type = latest.run_type AND r.started_at = latest.max_started
            """
        ).fetchall()
    counts: dict[str, Counter] = {
        "daily_full": Counter(),
        "paper_4h_update": Counter(),
    }
    for row in recent_rows:
        counts[str(row["run_type"])][str(row["status"])] = int(row["count"])
    latest = {str(row["run_type"]): dict(row) for row in latest_rows}
    return {
        "since": since,
        "counts": counts,
        "latest": latest,
    }


def _stale_running_runs(settings: Settings, now_utc: datetime, max_age_hours: float = 2.0) -> list[dict]:
    cutoff = (now_utc - timedelta(hours=max_age_hours)).isoformat(timespec="seconds").replace("+00:00", "Z")
    with connect_db(settings.output.database_path) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            """
            SELECT run_id, run_type, started_at, log_path
            FROM runs
            WHERE status = 'running' AND started_at <= ?
            ORDER BY started_at
            """,
            (cutoff,),
        ).fetchall()
    output: list[dict] = []
    for row in rows:
        started = _parse_utc(str(row["started_at"]))
        output.append(
            {
                "run_id": str(row["run_id"]),
                "run_type": str(row["run_type"]),
                "started_at": str(row["started_at"]),
                "age_hours": max(0.0, (now_utc - started).total_seconds() / 3600),
                "log_path": str(row["log_path"] or ""),
            }
        )
    return output


def _holding_42_bar_review(settings: Settings, threshold_hours: float = 168.0) -> list[dict]:
    with connect_db(settings.output.database_path) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            """
            SELECT snapshot_time, run_id, plan_id, symbol, status, current_price,
                   entry_price, stop_current, tp1, tp2, unrealized_pnl,
                   realized_pnl, holding_hours
            FROM paper_snapshots
            WHERE holding_hours IS NOT NULL
            ORDER BY plan_id, snapshot_time
            """
        ).fetchall()
        event_rows = connection.execute(
            """
            SELECT plan_id, event_time, event_type, reason
            FROM paper_events
            WHERE event_type IN ('TP1_HIT', 'TP2_HIT', 'CLOSED', 'STOPPED',
                                 'EMA_TRAILING_STOPPED', 'INVALIDATED', 'ARCHIVED')
            ORDER BY event_time
            """
        ).fetchall()
    by_plan: dict[str, list[sqlite3.Row]] = {}
    for row in rows:
        by_plan.setdefault(str(row["plan_id"]), []).append(row)
    events_by_plan: dict[str, list[sqlite3.Row]] = {}
    for row in event_rows:
        events_by_plan.setdefault(str(row["plan_id"]), []).append(row)

    review: list[dict] = []
    for plan_id, snapshots in by_plan.items():
        after_threshold = [row for row in snapshots if row["holding_hours"] is not None and float(row["holding_hours"]) >= threshold_hours]
        if not after_threshold:
            continue
        first = after_threshold[0]
        latest = snapshots[-1]
        after_prices = [float(row["current_price"]) for row in after_threshold if row["current_price"] is not None]
        after_pnls = [float(row["unrealized_pnl"]) for row in after_threshold if row["unrealized_pnl"] is not None]
        threshold_time = str(first["snapshot_time"])
        later_events = [
            row for row in events_by_plan.get(plan_id, [])
            if str(row["event_time"]) >= threshold_time
        ]
        outcome = "still_open" if str(latest["status"]) in OPEN_STATUSES else str(latest["status"]).lower()
        if later_events:
            outcome = str(later_events[-1]["event_type"]).lower()
        review.append(
            {
                "plan_id": plan_id,
                "symbol": str(latest["symbol"]),
                "status": str(latest["status"]),
                "threshold_time": threshold_time,
                "hours_at_threshold": float(first["holding_hours"]),
                "price_at_threshold": first["current_price"],
                "pnl_at_threshold": first["unrealized_pnl"],
                "latest_time": str(latest["snapshot_time"]),
                "latest_price": latest["current_price"],
                "latest_pnl": latest["unrealized_pnl"],
                "max_price_after": max(after_prices) if after_prices else None,
                "min_price_after": min(after_prices) if after_prices else None,
                "max_pnl_after": max(after_pnls) if after_pnls else None,
                "min_pnl_after": min(after_pnls) if after_pnls else None,
                "outcome_after": outcome,
            }
        )
    return sorted(review, key=lambda item: item["hours_at_threshold"], reverse=True)


def _fmt_optional(value: object, digits: int = 2) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        return f"{value:.{digits}f}"
    return str(value)


def _nested_get(data: dict, path: tuple[str, ...]) -> object | None:
    current: object = data
    for key in path:
        if not isinstance(current, dict) or key not in current:
            return None
        current = current[key]
    return current


def _as_bool(value: object | None) -> bool | None:
    if value is None:
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        lowered = value.lower()
        if lowered in {"true", "1", "yes"}:
            return True
        if lowered in {"false", "0", "no"}:
            return False
    return None


def _as_float(value: object | None) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _as_int(value: object | None) -> int | None:
    if value is None:
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _source_contains(source: str, needle: str) -> bool:
    return needle in source


def _source_line(source: str, needle: str) -> str:
    for line in source.splitlines():
        if needle in line:
            return line.strip()
    return "not found"


def build_signal_fill_timing_audit(
    settings: Settings,
    run_id: str,
    *,
    report_date: str | None = None,
) -> SignalFillTimingAudit:
    from .backtest import replay as replay_module
    from .trade_state import step_trade

    connection = connect_db(settings.output.database_path)
    try:
        run = connection.execute("SELECT * FROM backtest_runs WHERE run_id = ?", (run_id,)).fetchone()
        if run is None:
            raise ValueError(f"backtest run_id not found: {run_id}")
        trade_rows = connection.execute("SELECT * FROM backtest_trades WHERE run_id = ?", (run_id,)).fetchall()
    finally:
        connection.close()

    config = json.loads(run["config_json"] or "{}")
    symbols = json.loads(run["symbols_json"] or "[]")
    entered = [row for row in trade_rows if row["entered_at_utc"]]
    same_bar_entry_and_exit = [
        row
        for row in entered
        if row["closed_at_utc"] is not None and row["closed_at_utc"] == row["entered_at_utc"]
    ]
    same_bar_entry_and_tp1 = 0
    blocked_notes = 0
    for row in trade_rows:
        payload = json.loads(row["payload_json"] or "{}")
        if "max active positions" in str(payload.get("notes", "")).lower():
            blocked_notes += 1
        for event in payload.get("events", []):
            if (
                isinstance(event, dict)
                and event.get("event_type") == "TP1_HIT"
                and row["entered_at_utc"] is not None
                and event.get("event_time_utc") == row["entered_at_utc"]
            ):
                same_bar_entry_and_tp1 += 1

    replay_source = inspect.getsource(replay_module)
    step_source = inspect.getsource(step_trade)
    required_needles = [
        "# First advance exits for active positions, then process existing condition plans.",
        "watching.sort(key=lambda item: (-item.score, item.created_index, item.paper.symbol))",
        "_entry_reclaim_close_satisfied(",
        "raw_entry = item.paper.entry_high",
        "active_before_decision = _active_positions(all_trades)",
        "if len(active_before_decision) >= settings.backtest.max_active_positions:",
    ]
    source_complete = all(_source_contains(replay_source, needle) for needle in required_needles)
    same_call_entry_then_risk = _source_contains(step_source, 'if trade.status == "WATCHING":') and _source_contains(
        step_source,
        'if trade.status in {"ENTERED", "TP1_HIT"}',
    )

    if not source_complete:
        verdict = "timing_audit_blocked"
        reason = "replay source did not contain all expected timing/order markers; audit cannot verify behavior."
    elif same_call_entry_then_risk:
        verdict = "timing_audit_warn_same_bar_ambiguity"
        reason = (
            "replay order is inspectable, but WATCHING entry and same-bar stop/TP evaluation can occur in one "
            "step_trade call; later capacity diagnostics must explicitly account for same-bar ambiguity."
        )
    else:
        verdict = "timing_audit_pass"
        reason = "replay order and fill assumptions are inspectable and no same-call entry/exit ambiguity was detected."

    backtest_cfg = config.get("backtest", {}) if isinstance(config.get("backtest", {}), dict) else {}
    analysis_cfg = config.get("analysis", {}) if isinstance(config.get("analysis", {}), dict) else {}
    return SignalFillTimingAudit(
        run_id=run_id,
        report_date=report_date or _local_now().strftime("%Y-%m-%d"),
        start_utc=str(run["start_utc"]),
        end_utc=str(run["end_utc"]),
        commit_hash=str(run["commit_hash"]),
        symbols_count=len(symbols),
        entry_reclaim_close_enabled=_as_bool(analysis_cfg.get("entry_reclaim_close_enabled")),
        entry_reclaim_min_atr_enabled=_as_bool(analysis_cfg.get("entry_reclaim_min_atr_enabled")),
        entry_reclaim_min_atr=_as_float(analysis_cfg.get("entry_reclaim_min_atr")),
        max_active_positions=_as_int(backtest_cfg.get("max_active_positions")),
        intrabar_policy=None if backtest_cfg.get("intrabar") is None else str(backtest_cfg.get("intrabar")),
        maker_fee_bps=_as_float(backtest_cfg.get("maker_fee_bps")),
        taker_fee_bps=_as_float(backtest_cfg.get("taker_fee_bps")),
        entry_slippage_bps=_as_float(backtest_cfg.get("entry_slippage_bps")),
        stop_slippage_bps=_as_float(backtest_cfg.get("stop_slippage_bps")),
        entered_trades=len(entered),
        same_bar_entry_and_exit_trades=len(same_bar_entry_and_exit),
        same_bar_entry_and_tp1_trades=same_bar_entry_and_tp1,
        blocked_notes_persisted=blocked_notes,
        verdict=verdict,
        reason=reason,
    )


def render_signal_fill_timing_audit(audit: SignalFillTimingAudit) -> str:
    from .backtest import replay as replay_module
    from .trade_state import step_trade

    replay_source = inspect.getsource(replay_module)
    step_source = inspect.getsource(step_trade)
    now = _local_now()
    lines = [
        "---",
        f"created: {now.strftime('%Y-%m-%d %H:%M:%S %Z')}",
        "tags:",
        "  - crypto",
        "  - trading-system",
        "  - timing-audit",
        "experiment: signal_fill_timing_audit",
        f"run_id: {audit.run_id}",
        f"verdict: {audit.verdict}",
        "---",
        "",
        "# signal_fill_timing_audit",
        "",
        "## Plain-language conclusion",
        "",
        audit.reason,
        "",
        "This report is diagnostic only. It does not change `config/settings.toml`, backtest behavior, paper state, or strategy defaults.",
        "",
        "## Scope",
        "",
        "| Field | Value |",
        "|---|---:|",
        f"| run_id | `{audit.run_id}` |",
        f"| window | `{audit.start_utc}` -> `{audit.end_utc}` |",
        f"| commit_hash | `{audit.commit_hash}` |",
        f"| symbols | {audit.symbols_count} |",
        f"| max_active_positions | {_fmt_optional(audit.max_active_positions)} |",
        f"| intrabar_policy | `{_fmt_optional(audit.intrabar_policy)}` |",
        "",
        "## Timing Findings",
        "",
        "| Question | Current replay behavior | Risk read |",
        "|---|---|---|",
        "| `signal_time` | 4h reclaim is evaluated with the current bar close at `bar_time = bar_close_ms`. | Signal depends on a closed 4h candle. |",
        "| `decision_time` | Capacity is checked after entry-zone touch, reclaim confirmation, quantity sizing, cash sizing, and notional sizing. | Blocked events must be recorded after these earlier gates pass. |",
        "| `fill_time` | Entry raw price is `entry_high`, then `entry_fill` adds entry slippage; event time is the same `bar_time`. | Audit warning: signal confirmation and event timestamp are same-bar, while raw fill price is not explicitly next-bar open. |",
        "| exit/entry order | Existing active positions are advanced before WATCHING plans are processed. | Capacity snapshots must be taken after same-bar active exits/time exits. |",
        "| WATCHING order | WATCHING plans sort by `(-score, created_index, symbol)`. | Multi-candidate events must use this order for primary sample selection. |",
        "| same-bar entry risk | `step_trade` can move a WATCHING trade to ENTERED and then evaluate ENTERED/TP1_HIT stop/TP logic in the same call. | Same-bar entry/exit or TP1 outcomes need explicit ambiguity flags. |",
        "",
        "## Run Evidence",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| entered_trades | {audit.entered_trades} |",
        f"| same_bar_entry_and_exit_trades | {audit.same_bar_entry_and_exit_trades} |",
        f"| same_bar_entry_and_tp1_trades | {audit.same_bar_entry_and_tp1_trades} |",
        f"| persisted max-active skipped notes | {audit.blocked_notes_persisted} |",
        "",
        "Persisted max-active skipped notes are expected to be incomplete because later plan notes can overwrite skipped-entry attempts. Stage 1 must export blocked events directly from replay rather than infer them from final trade notes.",
        "",
        "## Cost And Fill Assumptions",
        "",
        "| Field | Value |",
        "|---|---:|",
        f"| maker_fee_bps | {_fmt_optional(audit.maker_fee_bps)} |",
        f"| taker_fee_bps | {_fmt_optional(audit.taker_fee_bps)} |",
        f"| entry_slippage_bps | {_fmt_optional(audit.entry_slippage_bps)} |",
        f"| stop_slippage_bps | {_fmt_optional(audit.stop_slippage_bps)} |",
        f"| entry_reclaim_close_enabled | {_fmt_optional(audit.entry_reclaim_close_enabled)} |",
        f"| entry_reclaim_min_atr_enabled | {_fmt_optional(audit.entry_reclaim_min_atr_enabled)} |",
        f"| entry_reclaim_min_atr | {_fmt_optional(audit.entry_reclaim_min_atr)} |",
        "",
        "## Source Markers",
        "",
        "| Behavior | Source marker |",
        "|---|---|",
        f"| active exits before watching entries | `{_source_line(replay_source, '# First advance exits')}` |",
        f"| WATCHING sort order | `{_source_line(replay_source, 'watching.sort')}` |",
        f"| reclaim check | `{_source_line(replay_source, '_entry_reclaim_close_satisfied(')}` |",
        f"| raw entry price | `{_source_line(replay_source, 'raw_entry = item.paper.entry_high')}` |",
        f"| capacity check | `{_source_line(replay_source, 'max_active_positions')}` |",
        f"| same-call ENTERED evaluation | `{_source_line(step_source, 'if trade.status in {\"ENTERED\", \"TP1_HIT\"}')}` |",
        "",
        "## Decision",
        "",
        f"`{audit.verdict}`",
        "",
        "## Next Action",
        "",
    ]
    if audit.verdict == "timing_audit_blocked":
        lines.append("Do not implement `blocked_entry_event_export` until the replay timing markers are clarified or restored.")
    elif audit.verdict == "timing_audit_warn_same_bar_ambiguity":
        lines.extend(
            [
                "Proceed to design `blocked_entry_event_export`, but include explicit fields for same-bar ambiguity:",
                "",
                "- `signal_time`",
                "- `decision_time`",
                "- `fill_time_assumption`",
                "- `active_snapshot_after_exits`",
                "- `same_bar_entry_exit_possible`",
                "- `same_bar_entry_tp1_possible`",
            ]
        )
    else:
        lines.append("Proceed to `blocked_entry_event_export` with the documented timing assumptions.")
    lines.extend(
        [
            "",
            "## Raw Summary",
            "",
            "```json",
            json.dumps(audit.__dict__, ensure_ascii=False, indent=2),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def write_signal_fill_timing_audit_report(
    settings: Settings,
    run_id: str,
    *,
    report_date: str | None = None,
) -> tuple[SignalFillTimingAudit, list[Path]]:
    date_text = report_date or _local_now().strftime("%Y-%m-%d")
    audit = build_signal_fill_timing_audit(settings, run_id, report_date=date_text)
    text = render_signal_fill_timing_audit(audit)
    report_dir = settings.output.reports_dir / date_text
    obsidian_dir = None if settings.output.obsidian_dir is None else settings.output.obsidian_dir / "Reports" / date_text
    prefix = f"signal_fill_timing_audit_{date_text}"
    version = next_report_version([report_dir, obsidian_dir], prefix)
    filename = versioned_markdown_filename(prefix, version)
    paths: list[Path] = []
    for directory in [report_dir, obsidian_dir]:
        if directory is None:
            continue
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / filename
        path.write_text(text, encoding="utf-8")
        paths.append(path)
    return audit, paths


def _apply_backtest_config_snapshot(settings: Settings, config: dict) -> Settings:
    import copy

    replay_settings = copy.deepcopy(settings)
    for section_name in ("analysis", "backtest"):
        section = config.get(section_name, {})
        if not isinstance(section, dict):
            continue
        target = getattr(replay_settings, section_name)
        for key, value in section.items():
            if hasattr(target, key):
                setattr(target, key, value)
    market_top_n = config.get("market_top_n")
    if market_top_n is not None:
        replay_settings.market.top_n = int(market_top_n)
    return replay_settings


def _source_run_row(settings: Settings, run_id: str) -> sqlite3.Row:
    with connect_db(settings.output.database_path) as connection:
        row = connection.execute("SELECT * FROM backtest_runs WHERE run_id = ?", (run_id,)).fetchone()
    if row is None:
        raise ValueError(f"backtest run_id not found: {run_id}")
    return row


def _source_entered_trades(settings: Settings, run_id: str) -> int:
    with connect_db(settings.output.database_path) as connection:
        row = connection.execute(
            """
            SELECT COUNT(*) AS count
            FROM backtest_trades
            WHERE run_id = ? AND entered_at_utc IS NOT NULL
            """,
            (run_id,),
        ).fetchone()
    return int(row["count"]) if row is not None else 0


def _stored_symbol_master(source_run_id: str, created_at_utc: str, symbols: list[str]) -> SymbolMaster:
    return SymbolMaster(
        source=f"stored backtest run {source_run_id}",
        created_at_utc=created_at_utc,
        symbols=symbols,
        source_limit=None,
        source_limit_applied=False,
        filters="stored symbols from source backtest run; listing_dates unavailable",
        listing_dates=None,
    )


def _blocked_event_dicts(result) -> list[dict]:
    return [asdict(event) for event in result.blocked_entry_events]


def _events_by_month(events: list[dict]) -> dict[str, int]:
    counts: Counter = Counter()
    for event in events:
        month = str(event["decision_time_utc"])[:7]
        counts[month] += 1
    return dict(sorted(counts.items()))


def _top_event_symbols(events: list[dict], limit: int = 10) -> list[tuple[str, int]]:
    counts: Counter = Counter(str(event["symbol"]) for event in events)
    return counts.most_common(limit)


def _replay_source_run(settings: Settings, run: sqlite3.Row, *, progress=None):
    from .backtest.replay import run_backtest_replay

    config = json.loads(run["config_json"] or "{}")
    symbols = [str(symbol).replace("/", "").upper() for symbol in json.loads(run["symbols_json"] or "[]")]
    if not symbols:
        raise ValueError(f"backtest run_id has no stored symbols: {run['run_id']}")
    replay_settings = _apply_backtest_config_snapshot(settings, config)
    dynamic_mode = bool(config.get("dynamic_universe_mode"))
    dynamic_summary = config.get("dynamic_universe_summary", {})
    if not isinstance(dynamic_summary, dict):
        dynamic_summary = {}
    max_symbols = _as_int(dynamic_summary.get("max_symbols"))
    dynamic_master = _stored_symbol_master(str(run["run_id"]), str(run["created_at_utc"]), symbols) if dynamic_mode else None
    result = run_backtest_replay(
        replay_settings,
        symbols,
        str(run["start_utc"]),
        str(run["end_utc"]),
        allow_data_gaps=True if dynamic_mode else False,
        dynamic_universe_mode=dynamic_mode,
        dynamic_symbol_master=dynamic_master,
        max_universe_symbols=max_symbols,
        progress=progress,
    )
    return result, replay_settings, symbols, dynamic_mode, max_symbols


def build_blocked_entry_event_export(
    settings: Settings,
    run_id: str,
    *,
    report_date: str | None = None,
    progress=None,
) -> BlockedEntryEventExport:
    run = _source_run_row(settings, run_id)
    result, replay_settings, symbols, dynamic_mode, max_symbols = _replay_source_run(settings, run, progress=progress)
    events = _blocked_event_dicts(result)
    event_count = len(events)
    replay_entered = sum(1 for trade in result.trades if trade.entered_at_utc is not None)
    same_bar_exit = sum(1 for event in events if event["same_bar_entry_exit_possible"])
    same_bar_tp1 = sum(1 for event in events if event["same_bar_entry_tp1_possible"])
    if event_count > 0:
        verdict = "blocked_events_exported"
        reason = (
            "Replay instrumentation exported max-active blocked-entry events with candidate timing, capacity "
            "snapshot, and same-bar ambiguity flags; use this as input for replay consistency audit."
        )
    else:
        verdict = "blocked_events_empty_review_needed"
        reason = (
            "The instrumented replay produced no max-active blocked-entry events; before moving to replacement "
            "logic, verify replay consistency against the source run."
        )

    return BlockedEntryEventExport(
        source_run_id=run_id,
        replay_run_id=result.run_id,
        report_date=report_date or _local_now().strftime("%Y-%m-%d"),
        start_utc=str(run["start_utc"]),
        end_utc=str(run["end_utc"]),
        source_commit_hash=str(run["commit_hash"]),
        source_symbols_count=len(symbols),
        replay_symbols_count=len(result.symbols),
        source_entered_trades=_source_entered_trades(settings, run_id),
        replay_entered_trades=replay_entered,
        dynamic_universe_mode=dynamic_mode,
        max_universe_symbols=max_symbols,
        max_active_positions=replay_settings.backtest.max_active_positions,
        event_count=event_count,
        same_bar_entry_exit_possible_events=same_bar_exit,
        same_bar_entry_tp1_possible_events=same_bar_tp1,
        events_by_month=_events_by_month(events),
        events_by_symbol_top=_top_event_symbols(events),
        verdict=verdict,
        reason=reason,
        events=events,
    )


def render_blocked_entry_event_export(export: BlockedEntryEventExport, *, json_filename: str | None = None) -> str:
    now = _local_now()
    lines = [
        "---",
        f"created: {now.strftime('%Y-%m-%d %H:%M:%S %Z')}",
        "tags:",
        "  - crypto",
        "  - trading-system",
        "  - blocked-entry-event-export",
        "experiment: blocked_entry_event_export",
        f"source_run_id: {export.source_run_id}",
        f"replay_run_id: {export.replay_run_id}",
        f"verdict: {export.verdict}",
        "---",
        "",
        "# blocked_entry_event_export",
        "",
        "## Plain-language conclusion",
        "",
        export.reason,
        "",
        "This report is diagnostic only. It does not change `config/settings.toml`, backtest behavior, paper state, strategy defaults, or saved backtest rows.",
        "",
        "## Scope",
        "",
        "| Field | Value |",
        "|---|---:|",
        f"| source_run_id | `{export.source_run_id}` |",
        f"| replay_run_id | `{export.replay_run_id}` |",
        f"| window | `{export.start_utc}` -> `{export.end_utc}` |",
        f"| source_commit_hash | `{export.source_commit_hash}` |",
        f"| source_symbols | {export.source_symbols_count} |",
        f"| replay_symbols | {export.replay_symbols_count} |",
        f"| dynamic_universe_mode | {str(export.dynamic_universe_mode).lower()} |",
        f"| max_universe_symbols | {_fmt_optional(export.max_universe_symbols)} |",
        f"| max_active_positions | {_fmt_optional(export.max_active_positions)} |",
        "",
        "## Event Summary",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| blocked_entry_events | {export.event_count} |",
        f"| source_entered_trades | {export.source_entered_trades} |",
        f"| replay_entered_trades | {export.replay_entered_trades} |",
        f"| same_bar_entry_exit_possible_events | {export.same_bar_entry_exit_possible_events} |",
        f"| same_bar_entry_tp1_possible_events | {export.same_bar_entry_tp1_possible_events} |",
    ]
    if json_filename:
        lines.append(f"| events_json | `{json_filename}` |")
    lines.extend(
        [
            "",
            "## Event Schema",
            "",
            "Each event records a candidate that already passed entry-zone touch, reclaim, sizing, cash, and notional gates, but was rejected by `max_active_positions`.",
            "",
            "- `fill_time_assumption`: how the replay models the would-be fill for the blocked candidate.",
            "- `active_snapshot_after_exits`: active positions after same-bar exits/time exits were processed and before the candidate decision.",
            "- `same_bar_entry_exit_possible`: whether the blocked candidate's same bar also touched its stop.",
            "- `same_bar_entry_tp1_possible`: whether the blocked candidate's same bar also touched TP1.",
            "- `candidate_rank`: order among WATCHING plans after sorting by `(-score, created_index, symbol)`.",
            "",
            "## Events By Month",
            "",
            "| Month | Events |",
            "|---|---:|",
        ]
    )
    if export.events_by_month:
        for month, count in export.events_by_month.items():
            lines.append(f"| {month} | {count} |")
    else:
        lines.append("| n/a | 0 |")
    lines.extend(["", "## Top Symbols", "", "| Symbol | Events |", "|---|---:|"])
    if export.events_by_symbol_top:
        for symbol, count in export.events_by_symbol_top:
            lines.append(f"| `{symbol}` | {count} |")
    else:
        lines.append("| n/a | 0 |")

    lines.extend(
        [
            "",
            "## First Events",
            "",
            "| # | Time | Symbol | Rank | Active | Same-bar stop | Same-bar TP1 | Active symbols |",
            "|---:|---|---|---:|---:|---|---|---|",
        ]
    )
    for index, event in enumerate(export.events[:20], start=1):
        active_symbols = ", ".join(str(slot["symbol"]) for slot in event["active_snapshot_after_exits"])
        lines.append(
            f"| {index} | `{event['decision_time_utc']}` | `{event['symbol']}` | "
            f"{event['candidate_rank']} | {event['active_count_before_decision']} | "
            f"{str(event['same_bar_entry_exit_possible']).lower()} | "
            f"{str(event['same_bar_entry_tp1_possible']).lower()} | {active_symbols or 'n/a'} |"
        )
    if not export.events:
        lines.append("| n/a | n/a | n/a | 0 | 0 | false | false | n/a |")
    lines.extend(
        [
            "",
            "## Decision",
            "",
            f"`{export.verdict}`",
            "",
            "## Next Action",
            "",
            "Run `replay_consistency_audit` before interpreting replacement value. The next check should confirm whether the instrumented replay reproduces the source run closely enough to use these blocked events.",
            "",
            "## Raw Summary",
            "",
            "```json",
            json.dumps(asdict(export), ensure_ascii=False, indent=2),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def write_blocked_entry_event_export_report(
    settings: Settings,
    run_id: str,
    *,
    report_date: str | None = None,
    progress=None,
) -> tuple[BlockedEntryEventExport, list[Path], Path]:
    date_text = report_date or _local_now().strftime("%Y-%m-%d")
    export = build_blocked_entry_event_export(settings, run_id, report_date=date_text, progress=progress)
    report_dir = settings.output.reports_dir / date_text
    obsidian_dir = None if settings.output.obsidian_dir is None else settings.output.obsidian_dir / "Reports" / date_text
    prefix = f"blocked_entry_event_export_{date_text}"
    version = next_report_version([report_dir, obsidian_dir], prefix)
    filename = versioned_markdown_filename(prefix, version)
    json_filename = filename.replace(".md", ".json")
    text = render_blocked_entry_event_export(export, json_filename=json_filename)
    paths: list[Path] = []
    for directory in [report_dir, obsidian_dir]:
        if directory is None:
            continue
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / filename
        path.write_text(text, encoding="utf-8")
        paths.append(path)
    report_dir.mkdir(parents=True, exist_ok=True)
    json_path = report_dir / json_filename
    json_path.write_text(json.dumps(asdict(export), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return export, paths, json_path


def _source_payload(run: sqlite3.Row) -> dict:
    payload = json.loads(run["payload_json"] or "{}")
    if not isinstance(payload, dict):
        raise ValueError(f"backtest run payload is not a JSON object: {run['run_id']}")
    return payload


def _trade_dicts_from_result(result) -> list[dict]:
    return [asdict(trade) for trade in result.trades]


def _entered_signature(trade: dict) -> tuple:
    return (
        str(trade.get("symbol", "")),
        str(trade.get("created_at_utc", "")),
        str(trade.get("entered_at_utc", "")),
        None if trade.get("entry_price_filled") is None else round(float(trade["entry_price_filled"]), 10),
        None if trade.get("quantity") is None else round(float(trade["quantity"]), 10),
    )


def _entered_trades(trades: list[dict]) -> list[dict]:
    return [trade for trade in trades if trade.get("entered_at_utc") is not None]


def _closed_trades(trades: list[dict]) -> list[dict]:
    return [trade for trade in trades if trade.get("closed_at_utc") is not None]


def _signature_mismatches(source_signatures: list[tuple], replay_signatures: list[tuple], limit: int = 10) -> list[dict]:
    source_counter = Counter(source_signatures)
    replay_counter = Counter(replay_signatures)
    examples: list[dict] = []
    for signature in sorted(set(source_counter) | set(replay_counter)):
        source_count = source_counter.get(signature, 0)
        replay_count = replay_counter.get(signature, 0)
        if source_count == replay_count:
            continue
        examples.append(
            {
                "signature": list(signature),
                "source_count": source_count,
                "replay_count": replay_count,
            }
        )
        if len(examples) >= limit:
            break
    return examples


def _counter_mismatch_count(left: list[tuple], right: list[tuple]) -> int:
    left_counter = Counter(left)
    right_counter = Counter(right)
    return sum(abs(left_counter.get(signature, 0) - right_counter.get(signature, 0)) for signature in set(left_counter) | set(right_counter))


def _equity_path_by_time(points: list[dict]) -> dict[str, dict]:
    return {str(point.get("timestamp_utc")): point for point in points if point.get("timestamp_utc")}


def _active_path_mismatches(source_points: list[dict], replay_points: list[dict], limit: int = 10) -> tuple[int, int, list[dict]]:
    source_by_time = _equity_path_by_time(source_points)
    replay_by_time = _equity_path_by_time(replay_points)
    active_mismatches = 0
    open_plan_mismatches = 0
    examples: list[dict] = []
    for timestamp in sorted(set(source_by_time) | set(replay_by_time)):
        source = source_by_time.get(timestamp)
        replay = replay_by_time.get(timestamp)
        source_active = None if source is None else int(source.get("open_positions", -1))
        replay_active = None if replay is None else int(replay.get("open_positions", -1))
        source_open_plans = None if source is None else int(source.get("open_plans", -1))
        replay_open_plans = None if replay is None else int(replay.get("open_plans", -1))
        mismatch = False
        if source_active != replay_active:
            active_mismatches += 1
            mismatch = True
        if source_open_plans != replay_open_plans:
            open_plan_mismatches += 1
            mismatch = True
        if mismatch and len(examples) < limit:
            examples.append(
                {
                    "timestamp_utc": timestamp,
                    "source_open_positions": source_active,
                    "replay_open_positions": replay_active,
                    "source_open_plans": source_open_plans,
                    "replay_open_plans": replay_open_plans,
                }
            )
    return active_mismatches, open_plan_mismatches, examples


def _blocked_event_signature(event: dict) -> tuple:
    active_symbols = tuple(str(slot.get("symbol", "")) for slot in event.get("active_snapshot_after_exits", []))
    return (
        str(event.get("decision_time_utc", "")),
        str(event.get("symbol", "")),
        int(event.get("candidate_rank", 0)),
        int(event.get("active_count_before_decision", 0)),
        active_symbols,
        bool(event.get("same_bar_entry_exit_possible", False)),
        bool(event.get("same_bar_entry_tp1_possible", False)),
    )


def _load_blocked_events_reference(path: Path | None) -> tuple[str | None, list[dict] | None]:
    if path is None:
        return None, None
    data = json.loads(path.read_text(encoding="utf-8"))
    events = data.get("events") if isinstance(data, dict) else None
    if not isinstance(events, list):
        raise ValueError(f"blocked events JSON has no events list: {path}")
    return str(path), [event for event in events if isinstance(event, dict)]


def build_replay_consistency_audit(
    settings: Settings,
    run_id: str,
    *,
    blocked_events_json: Path | None = None,
    report_date: str | None = None,
    progress=None,
) -> ReplayConsistencyAudit:
    from .backtest import replay as replay_module

    run = _source_run_row(settings, run_id)
    payload = _source_payload(run)
    source_trades = payload.get("trades", [])
    source_equity = payload.get("equity_curve", [])
    if not isinstance(source_trades, list) or not isinstance(source_equity, list):
        raise ValueError(f"backtest run payload lacks trades/equity_curve lists: {run_id}")

    result, _replay_settings, _symbols, _dynamic_mode, _max_symbols = _replay_source_run(settings, run, progress=progress)
    replay_trades = _trade_dicts_from_result(result)
    replay_equity = [asdict(point) for point in result.equity_curve]

    source_entered = _entered_trades(source_trades)
    replay_entered = _entered_trades(replay_trades)
    source_entered_signatures = [_entered_signature(trade) for trade in source_entered]
    replay_entered_signatures = [_entered_signature(trade) for trade in replay_entered]
    entered_mismatch_examples = _signature_mismatches(source_entered_signatures, replay_entered_signatures)
    entered_mismatches = _counter_mismatch_count(source_entered_signatures, replay_entered_signatures)

    active_mismatches, open_plan_mismatches, active_examples = _active_path_mismatches(source_equity, replay_equity)

    reference_path, reference_events = _load_blocked_events_reference(blocked_events_json)
    blocked_mismatch_examples: list[dict] = []
    blocked_signature_mismatches: int | None = None
    reference_count: int | None = None
    replay_event_dicts = _blocked_event_dicts(result)
    if reference_events is not None:
        reference_count = len(reference_events)
        reference_signatures = [_blocked_event_signature(event) for event in reference_events]
        replay_signatures = [_blocked_event_signature(event) for event in replay_event_dicts]
        blocked_mismatch_examples = _signature_mismatches(reference_signatures, replay_signatures)
        blocked_signature_mismatches = _counter_mismatch_count(reference_signatures, replay_signatures)

    source_final = float(payload.get("final_equity", 0.0) or 0.0)
    final_equity_delta = result.final_equity - source_final
    replay_source = inspect.getsource(replay_module)
    ordering_marker_found = _source_contains(
        replay_source,
        "watching.sort(key=lambda item: (-item.score, item.created_index, item.paper.symbol))",
    )
    if blocked_events_json is None:
        ordering_evidence = "source run did not persist blocked candidate order; current source marker was checked, but no prior event JSON was provided for repeat-order comparison."
    elif blocked_signature_mismatches == 0 and ordering_marker_found:
        ordering_evidence = "source run did not persist blocked candidate order directly; current source marker and repeated blocked-event signatures match the prior export."
    else:
        ordering_evidence = "candidate ordering could not be accepted because source marker or blocked-event repeat signatures did not match."

    hard_failures = [
        len(source_trades) != len(replay_trades),
        len(source_entered) != len(replay_entered),
        len(_closed_trades(source_trades)) != len(_closed_trades(replay_trades)),
        entered_mismatches != 0,
        active_mismatches != 0,
        abs(final_equity_delta) > 1e-6,
    ]
    repeat_failure = blocked_signature_mismatches is not None and blocked_signature_mismatches != 0
    repeat_missing = blocked_signature_mismatches is None
    if any(hard_failures) or repeat_failure:
        verdict = "replay_consistency_fail"
        reason = "The instrumented replay did not reproduce one or more required source-run or blocked-event consistency checks."
    elif repeat_missing:
        verdict = "replay_consistency_incomplete"
        reason = "Source/replay core path matched, but no prior blocked events JSON was supplied, so blocked-event repeat consistency was not verified."
    else:
        verdict = "replay_consistency_pass_with_ordering_limit"
        reason = (
            "Source/replay entered trades, final equity, active path, and prior blocked-event signatures match. "
            "Candidate ordering is accepted only indirectly because the original source run did not persist blocked candidate ordering."
        )

    return ReplayConsistencyAudit(
        source_run_id=run_id,
        replay_run_id=result.run_id,
        report_date=report_date or _local_now().strftime("%Y-%m-%d"),
        start_utc=str(run["start_utc"]),
        end_utc=str(run["end_utc"]),
        source_commit_hash=str(run["commit_hash"]),
        source_trade_count=len(source_trades),
        replay_trade_count=len(replay_trades),
        source_entered_trades=len(source_entered),
        replay_entered_trades=len(replay_entered),
        source_closed_trades=len(_closed_trades(source_trades)),
        replay_closed_trades=len(_closed_trades(replay_trades)),
        entered_signature_mismatches=entered_mismatches,
        active_path_points=len(set(_equity_path_by_time(source_equity)) | set(_equity_path_by_time(replay_equity))),
        active_path_mismatches=active_mismatches,
        open_plan_path_mismatches=open_plan_mismatches,
        final_equity_delta=final_equity_delta,
        blocked_events_json=reference_path,
        blocked_events_reference_count=reference_count,
        blocked_events_replay_count=len(replay_event_dicts),
        blocked_event_signature_mismatches=blocked_signature_mismatches,
        candidate_ordering_evidence=ordering_evidence,
        ordering_directly_persisted_in_source=False,
        verdict=verdict,
        reason=reason,
        entered_mismatch_examples=entered_mismatch_examples,
        active_path_mismatch_examples=active_examples,
        blocked_event_mismatch_examples=blocked_mismatch_examples,
    )


def render_replay_consistency_audit(audit: ReplayConsistencyAudit) -> str:
    now = _local_now()
    lines = [
        "---",
        f"created: {now.strftime('%Y-%m-%d %H:%M:%S %Z')}",
        "tags:",
        "  - crypto",
        "  - trading-system",
        "  - replay-consistency-audit",
        "experiment: replay_consistency_audit",
        f"source_run_id: {audit.source_run_id}",
        f"replay_run_id: {audit.replay_run_id}",
        f"verdict: {audit.verdict}",
        "---",
        "",
        "# replay_consistency_audit",
        "",
        "## Plain-language conclusion",
        "",
        audit.reason,
        "",
        "This report is diagnostic only. It does not change `config/settings.toml`, backtest behavior, paper state, strategy defaults, or saved backtest rows.",
        "",
        "## Scope",
        "",
        "| Field | Value |",
        "|---|---:|",
        f"| source_run_id | `{audit.source_run_id}` |",
        f"| replay_run_id | `{audit.replay_run_id}` |",
        f"| window | `{audit.start_utc}` -> `{audit.end_utc}` |",
        f"| source_commit_hash | `{audit.source_commit_hash}` |",
        f"| blocked_events_json | `{audit.blocked_events_json or 'not supplied'}` |",
        "",
        "## Consistency Checks",
        "",
        "| Check | Source | Replay | Mismatches |",
        "|---|---:|---:|---:|",
        f"| trades | {audit.source_trade_count} | {audit.replay_trade_count} | {abs(audit.source_trade_count - audit.replay_trade_count)} |",
        f"| entered_trades | {audit.source_entered_trades} | {audit.replay_entered_trades} | {audit.entered_signature_mismatches} |",
        f"| closed_trades | {audit.source_closed_trades} | {audit.replay_closed_trades} | {abs(audit.source_closed_trades - audit.replay_closed_trades)} |",
        f"| active_count_path | {audit.active_path_points} points | {audit.active_path_points} points | {audit.active_path_mismatches} |",
        f"| open_plan_path | {audit.active_path_points} points | {audit.active_path_points} points | {audit.open_plan_path_mismatches} |",
        f"| final_equity_delta | n/a | n/a | {audit.final_equity_delta:.10f} |",
        f"| blocked_event_repeat | {_fmt_optional(audit.blocked_events_reference_count)} | {audit.blocked_events_replay_count} | {_fmt_optional(audit.blocked_event_signature_mismatches)} |",
        "",
        "## Candidate Ordering Evidence",
        "",
        audit.candidate_ordering_evidence,
        "",
        "Important limitation: the original source run did not persist blocked candidate ordering directly. Ordering is therefore verified by replay source marker plus repeat blocked-event signatures, not by an independently persisted source ordering table.",
        "",
        "## Mismatch Examples",
        "",
        "```json",
        json.dumps(
            {
                "entered_mismatch_examples": audit.entered_mismatch_examples,
                "active_path_mismatch_examples": audit.active_path_mismatch_examples,
                "blocked_event_mismatch_examples": audit.blocked_event_mismatch_examples,
            },
            ensure_ascii=False,
            indent=2,
        ),
        "```",
        "",
        "## Decision",
        "",
        f"`{audit.verdict}`",
        "",
        "## Next Action",
        "",
    ]
    if audit.verdict == "replay_consistency_pass_with_ordering_limit":
        lines.append("Proceed to `stale_slot_continuation_review`. Do not calculate replacement outcome until stale-slot continuation value is reviewed independently.")
    elif audit.verdict == "replay_consistency_incomplete":
        lines.append("Rerun this audit with `--blocked-events-json` pointing to the Stage 1 JSON sidecar before moving forward.")
    else:
        lines.append("Stop the replacement roadmap and fix replay/export consistency before any stale-slot or replacement outcome analysis.")
    lines.extend(
        [
            "",
            "## Raw Summary",
            "",
            "```json",
            json.dumps(asdict(audit), ensure_ascii=False, indent=2),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def write_replay_consistency_audit_report(
    settings: Settings,
    run_id: str,
    *,
    blocked_events_json: Path | None = None,
    report_date: str | None = None,
    progress=None,
) -> tuple[ReplayConsistencyAudit, list[Path]]:
    date_text = report_date or _local_now().strftime("%Y-%m-%d")
    audit = build_replay_consistency_audit(
        settings,
        run_id,
        blocked_events_json=blocked_events_json,
        report_date=date_text,
        progress=progress,
    )
    text = render_replay_consistency_audit(audit)
    report_dir = settings.output.reports_dir / date_text
    obsidian_dir = None if settings.output.obsidian_dir is None else settings.output.obsidian_dir / "Reports" / date_text
    prefix = f"replay_consistency_audit_{date_text}"
    version = next_report_version([report_dir, obsidian_dir], prefix)
    filename = versioned_markdown_filename(prefix, version)
    paths: list[Path] = []
    for directory in [report_dir, obsidian_dir]:
        if directory is None:
            continue
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / filename
        path.write_text(text, encoding="utf-8")
        paths.append(path)
    return audit, paths


def _ms_from_iso(value: str) -> int:
    return int(_parse_utc(value).timestamp() * 1000)


def _iso_from_ms(value: int) -> str:
    return datetime.fromtimestamp(value / 1000, tz=timezone.utc).isoformat(timespec="seconds")


def _kline_close_ms(kline: list, step_ms: int) -> int:
    return int(kline[0]) + step_ms


def _kline_by_close_ms(klines: list[list], step_ms: int) -> dict[int, list]:
    return {_kline_close_ms(kline, step_ms): kline for kline in klines}


def _summary(values: list[float | None]) -> dict[str, float | int | None]:
    clean = sorted(float(value) for value in values if value is not None)
    if not clean:
        return {"n": 0, "mean": None, "median": None, "positive_pct": None, "min": None, "max": None}
    n = len(clean)
    mid = n // 2
    median = clean[mid] if n % 2 else (clean[mid - 1] + clean[mid]) / 2
    return {
        "n": n,
        "mean": sum(clean) / n,
        "median": median,
        "positive_pct": sum(1 for value in clean if value > 0) / n * 100,
        "min": clean[0],
        "max": clean[-1],
    }


def _fmt_summary_value(value: float | int | None) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, int):
        return str(value)
    return f"{value:.3f}"


def _close_or_exit_continuation_r(
    trade: dict,
    by_close: dict[int, list],
    *,
    stale_ms: int,
    target_ms: int,
    stale_close: float,
    risk_per_unit: float,
) -> tuple[float | None, bool]:
    closed_at = trade.get("closed_at_utc")
    closed_ms = None if closed_at is None else _ms_from_iso(str(closed_at))
    if closed_ms is not None and closed_ms <= target_ms and trade.get("exit_price_filled") is not None:
        return (float(trade["exit_price_filled"]) - stale_close) / risk_per_unit, False
    kline = by_close.get(target_ms)
    if kline is None:
        return None, True
    return (float(kline[4]) - stale_close) / risk_per_unit, False


def _eventual_continuation_r(
    trade: dict,
    klines_after_stale: list[list],
    *,
    stale_close: float,
    risk_per_unit: float,
) -> tuple[float | None, bool]:
    if trade.get("closed_at_utc") is not None and trade.get("exit_price_filled") is not None:
        return (float(trade["exit_price_filled"]) - stale_close) / risk_per_unit, False
    if not klines_after_stale:
        return None, True
    return (float(klines_after_stale[-1][4]) - stale_close) / risk_per_unit, True


def _first_hit_after_stale(
    klines_after_stale: list[list],
    *,
    stop_loss: float,
    take_profit_1: float,
    step_ms: int,
    intrabar_policy: str,
) -> tuple[str, str | None]:
    for kline in klines_after_stale:
        close_ms = _kline_close_ms(kline, step_ms)
        high = float(kline[2])
        low = float(kline[3])
        stop_hit = low <= stop_loss
        tp1_hit = high >= take_profit_1
        if stop_hit and tp1_hit:
            return ("stop_first_same_bar" if intrabar_policy == "stop_first" else "tp1_first_same_bar"), _iso_from_ms(close_ms)
        if stop_hit:
            return "stop", _iso_from_ms(close_ms)
        if tp1_hit:
            return "tp1", _iso_from_ms(close_ms)
    return "not_hit_by_end", None


def _stale_observation_from_trade(
    trade: dict,
    klines: list[list],
    *,
    stale_bars: int,
    step_ms: int,
    end_ms: int,
    intrabar_policy: str,
) -> tuple[StaleSlotObservation | None, str | None]:
    entered_at = trade.get("entered_at_utc")
    entry_price = trade.get("entry_price_filled")
    stop_loss = trade.get("stop_loss")
    take_profit_1 = trade.get("take_profit_1")
    if entered_at is None or entry_price is None or stop_loss is None or take_profit_1 is None:
        return None, "insufficient_trade_fields"
    entered_ms = _ms_from_iso(str(entered_at))
    stale_ms = entered_ms + stale_bars * step_ms
    if stale_ms > end_ms:
        return None, "insufficient_price_data"
    tp1_at = trade.get("tp1_hit_at_utc")
    if tp1_at is not None and _ms_from_iso(str(tp1_at)) <= stale_ms:
        return None, "tp1_before_stale"
    closed_at = trade.get("closed_at_utc")
    if closed_at is not None and _ms_from_iso(str(closed_at)) <= stale_ms:
        return None, "closed_before_stale"
    entry = float(entry_price)
    stop = float(stop_loss)
    tp1 = float(take_profit_1)
    risk_per_unit = entry - stop
    if risk_per_unit <= 0:
        return None, "insufficient_trade_fields"
    by_close = _kline_by_close_ms(klines, step_ms)
    stale_kline = by_close.get(stale_ms)
    if stale_kline is None:
        return None, "insufficient_price_data"
    stale_close = float(stale_kline[4])
    terminal_ms = end_ms
    if closed_at is not None:
        terminal_ms = min(terminal_ms, _ms_from_iso(str(closed_at)))
    klines_after_stale = [
        kline
        for kline in klines
        if stale_ms < _kline_close_ms(kline, step_ms) <= terminal_ms
    ]
    forward_24, horizon_24_censored = _close_or_exit_continuation_r(
        trade,
        by_close,
        stale_ms=stale_ms,
        target_ms=stale_ms + 24 * step_ms,
        stale_close=stale_close,
        risk_per_unit=risk_per_unit,
    )
    forward_42, horizon_42_censored = _close_or_exit_continuation_r(
        trade,
        by_close,
        stale_ms=stale_ms,
        target_ms=stale_ms + 42 * step_ms,
        stale_close=stale_close,
        risk_per_unit=risk_per_unit,
    )
    forward_60, horizon_60_censored = _close_or_exit_continuation_r(
        trade,
        by_close,
        stale_ms=stale_ms,
        target_ms=stale_ms + 60 * step_ms,
        stale_close=stale_close,
        risk_per_unit=risk_per_unit,
    )
    eventual_r, right_censored = _eventual_continuation_r(
        trade,
        klines_after_stale,
        stale_close=stale_close,
        risk_per_unit=risk_per_unit,
    )
    if klines_after_stale:
        mfe_r = (max(float(kline[2]) for kline in klines_after_stale) - stale_close) / risk_per_unit
        mae_r = (min(float(kline[3]) for kline in klines_after_stale) - stale_close) / risk_per_unit
    else:
        mfe_r = None
        mae_r = None
    first_hit, first_hit_time = _first_hit_after_stale(
        klines_after_stale,
        stop_loss=stop,
        take_profit_1=tp1,
        step_ms=step_ms,
        intrabar_policy=intrabar_policy,
    )
    return (
        StaleSlotObservation(
            trade_id=str(trade.get("trade_id", "")),
            symbol=str(trade.get("symbol", "")),
            entered_at_utc=str(entered_at),
            stale_time_utc=_iso_from_ms(stale_ms),
            closed_at_utc=None if closed_at is None else str(closed_at),
            tp1_hit_at_utc=None if tp1_at is None else str(tp1_at),
            final_status=str(trade.get("status", "")),
            entry_price=entry,
            stop_loss=stop,
            take_profit_1=tp1,
            stale_close=stale_close,
            risk_per_unit=risk_per_unit,
            forward_r_24=forward_24,
            forward_r_42=forward_42,
            forward_r_60=forward_60,
            eventual_continuation_r=eventual_r,
            mfe_r_after_stale=mfe_r,
            mae_r_after_stale=mae_r,
            first_hit_outcome_after_stale=first_hit,
            first_hit_time_utc=first_hit_time,
            right_censored=right_censored,
            horizon_24_censored=horizon_24_censored,
            horizon_42_censored=horizon_42_censored,
            horizon_60_censored=horizon_60_censored,
        ),
        None,
    )


def build_stale_slot_continuation_review(
    settings: Settings,
    run_id: str,
    *,
    stale_bars: int = 42,
    report_date: str | None = None,
    progress=None,
) -> StaleSlotContinuationReview:
    from .backtest.history import batch_load_klines_cached, interval_ms

    run = _source_run_row(settings, run_id)
    result, replay_settings, symbols, _dynamic_mode, _max_symbols = _replay_source_run(settings, run, progress=progress)
    step_ms = interval_ms(replay_settings.backtest.primary_interval)
    start_ms = _ms_from_iso(str(run["start_utc"]))
    end_ms = _ms_from_iso(str(run["end_utc"]))
    klines_by_symbol = batch_load_klines_cached(
        replay_settings,
        symbols,
        [replay_settings.backtest.primary_interval],
        start_ms,
        end_ms,
    )
    replay_trades = _trade_dicts_from_result(result)
    entered = _entered_trades(replay_trades)
    observations: list[StaleSlotObservation] = []
    exclusion_counts: Counter = Counter()
    interval = replay_settings.backtest.primary_interval
    for trade in entered:
        symbol = str(trade.get("symbol", ""))
        klines = klines_by_symbol.get(symbol, {}).get(interval, [])
        observation, exclusion = _stale_observation_from_trade(
            trade,
            klines,
            stale_bars=stale_bars,
            step_ms=step_ms,
            end_ms=end_ms,
            intrabar_policy=replay_settings.backtest.intrabar_policy,
        )
        if observation is not None:
            observations.append(observation)
        elif exclusion is not None:
            exclusion_counts[exclusion] += 1

    first_hit_outcomes = dict(sorted(Counter(obs.first_hit_outcome_after_stale for obs in observations).items()))
    right_censored_count = sum(1 for obs in observations if obs.right_censored)
    eventual_summary = _summary([obs.eventual_continuation_r for obs in observations])
    forward_42_summary = _summary([obs.forward_r_42 for obs in observations])
    if not observations:
        verdict = "stale_slot_sample_empty"
        reason = "No entered trades reached the pre-TP1 stale threshold, so the old-slot continuation value cannot be estimated from this run."
    elif int(eventual_summary["n"] or 0) < 10:
        verdict = "stale_slot_sample_thin_retest"
        reason = "Pre-TP1 stale slots exist, but the sample is too small for a stable continuation judgment; treat this as a diagnostic snapshot."
    elif float(eventual_summary["mean"] or 0.0) < 0 and float(forward_42_summary["mean"] or 0.0) < 0:
        verdict = "stale_slot_continuation_weak_retest"
        reason = "Pre-TP1 stale slots show negative average continuation after the stale time, supporting further capacity replacement research but not deployment."
    else:
        verdict = "stale_slot_continuation_not_weak"
        reason = "Pre-TP1 stale slots do not show broadly negative continuation value; replacement research priority should be reduced unless blocked-candidate evidence is very strong."

    return StaleSlotContinuationReview(
        source_run_id=run_id,
        replay_run_id=result.run_id,
        report_date=report_date or _local_now().strftime("%Y-%m-%d"),
        start_utc=str(run["start_utc"]),
        end_utc=str(run["end_utc"]),
        source_commit_hash=str(run["commit_hash"]),
        stale_bars=stale_bars,
        stale_hours=int(stale_bars * step_ms / 60 / 60 / 1000),
        total_entered_trades=len(entered),
        eligible_pre_tp1_stale_slots=len(observations),
        excluded_tp1_before_stale=int(exclusion_counts["tp1_before_stale"]),
        excluded_closed_before_stale=int(exclusion_counts["closed_before_stale"]),
        excluded_insufficient_price_data=int(exclusion_counts["insufficient_price_data"] + exclusion_counts["insufficient_trade_fields"]),
        right_censored_count=right_censored_count,
        first_hit_outcomes=first_hit_outcomes,
        forward_r_24_summary=_summary([obs.forward_r_24 for obs in observations]),
        forward_r_42_summary=forward_42_summary,
        forward_r_60_summary=_summary([obs.forward_r_60 for obs in observations]),
        eventual_continuation_r_summary=eventual_summary,
        mfe_r_summary=_summary([obs.mfe_r_after_stale for obs in observations]),
        mae_r_summary=_summary([obs.mae_r_after_stale for obs in observations]),
        verdict=verdict,
        reason=reason,
        observations=observations,
    )


def render_stale_slot_continuation_review(review: StaleSlotContinuationReview) -> str:
    now = _local_now()
    lines = [
        "---",
        f"created: {now.strftime('%Y-%m-%d %H:%M:%S %Z')}",
        "tags:",
        "  - crypto",
        "  - trading-system",
        "  - stale-slot-continuation-review",
        "experiment: stale_slot_continuation_review",
        f"source_run_id: {review.source_run_id}",
        f"replay_run_id: {review.replay_run_id}",
        f"verdict: {review.verdict}",
        "---",
        "",
        "# stale_slot_continuation_review",
        "",
        "## Plain-language conclusion",
        "",
        review.reason,
        "",
        "This report is diagnostic only. It does not compare blocked candidates, does not calculate replacement outcome, and does not change `config/settings.toml`, backtest behavior, paper state, strategy defaults, or saved backtest rows.",
        "",
        "## Scope",
        "",
        "| Field | Value |",
        "|---|---:|",
        f"| source_run_id | `{review.source_run_id}` |",
        f"| replay_run_id | `{review.replay_run_id}` |",
        f"| window | `{review.start_utc}` -> `{review.end_utc}` |",
        f"| source_commit_hash | `{review.source_commit_hash}` |",
        f"| stale_threshold | {review.stale_bars} bars = {review.stale_hours}h |",
        "",
        "## Sample Definition",
        "",
        "A slot is included only if it was an entered position that reached the stale threshold while still pre-TP1 and still open. `forward_R_*` is incremental R from the stale-time close, not whole-trade R.",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| total_entered_trades | {review.total_entered_trades} |",
        f"| eligible_pre_tp1_stale_slots | {review.eligible_pre_tp1_stale_slots} |",
        f"| excluded_tp1_before_stale | {review.excluded_tp1_before_stale} |",
        f"| excluded_closed_before_stale | {review.excluded_closed_before_stale} |",
        f"| excluded_insufficient_price_data | {review.excluded_insufficient_price_data} |",
        f"| right_censored_count | {review.right_censored_count} |",
        "",
        "## Continuation R Summary",
        "",
        "| Metric | n | mean | median | positive_pct | min | max |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for label, summary in [
        ("forward_R_24", review.forward_r_24_summary),
        ("forward_R_42", review.forward_r_42_summary),
        ("forward_R_60", review.forward_r_60_summary),
        ("eventual_continuation_R", review.eventual_continuation_r_summary),
        ("MFE_R_after_stale", review.mfe_r_summary),
        ("MAE_R_after_stale", review.mae_r_summary),
    ]:
        lines.append(
            f"| {label} | {_fmt_summary_value(summary['n'])} | {_fmt_summary_value(summary['mean'])} | "
            f"{_fmt_summary_value(summary['median'])} | {_fmt_summary_value(summary['positive_pct'])} | "
            f"{_fmt_summary_value(summary['min'])} | {_fmt_summary_value(summary['max'])} |"
        )
    lines.extend(["", "## First Hit After Stale", "", "| Outcome | Count |", "|---|---:|"])
    if review.first_hit_outcomes:
        for outcome, count in review.first_hit_outcomes.items():
            lines.append(f"| `{outcome}` | {count} |")
    else:
        lines.append("| n/a | 0 |")
    lines.extend(
        [
            "",
            "## First Observations",
            "",
            "| # | Symbol | Stale Time | Status | forward_R_42 | eventual_R | MFE_R | MAE_R | First Hit | Censored |",
            "|---:|---|---|---|---:|---:|---:|---:|---|---|",
        ]
    )
    for index, obs in enumerate(review.observations[:30], start=1):
        lines.append(
            f"| {index} | `{obs.symbol}` | `{obs.stale_time_utc}` | `{obs.final_status}` | "
            f"{_fmt_summary_value(obs.forward_r_42)} | {_fmt_summary_value(obs.eventual_continuation_r)} | "
            f"{_fmt_summary_value(obs.mfe_r_after_stale)} | {_fmt_summary_value(obs.mae_r_after_stale)} | "
            f"`{obs.first_hit_outcome_after_stale}` | {str(obs.right_censored).lower()} |"
        )
    if not review.observations:
        lines.append("| n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | false |")
    lines.extend(
        [
            "",
            "## Decision",
            "",
            f"`{review.verdict}`",
            "",
            "## Next Action",
            "",
        ]
    )
    if review.verdict == "stale_slot_continuation_weak_retest":
        lines.append("Proceed to `blocked_candidate_vs_stale_slot_review`, still as a diagnostic comparison only. Do not change `max_active_positions` or deploy replacement logic.")
    elif review.verdict == "stale_slot_continuation_not_weak":
        lines.append("Do not prioritize replacement until stronger blocked-candidate evidence exists; document why old-slot continuation is not broadly weak.")
    elif review.verdict == "stale_slot_sample_thin_retest":
        lines.append("Retest on broader or walk-forward windows before using stale-slot continuation as a capacity decision input.")
    else:
        lines.append("Stop this branch for the current run because no eligible stale slots were observed.")
    lines.extend(
        [
            "",
            "## Raw Summary",
            "",
            "```json",
            json.dumps(asdict(review), ensure_ascii=False, indent=2),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def write_stale_slot_continuation_review_report(
    settings: Settings,
    run_id: str,
    *,
    stale_bars: int = 42,
    report_date: str | None = None,
    progress=None,
) -> tuple[StaleSlotContinuationReview, list[Path]]:
    date_text = report_date or _local_now().strftime("%Y-%m-%d")
    review = build_stale_slot_continuation_review(
        settings,
        run_id,
        stale_bars=stale_bars,
        report_date=date_text,
        progress=progress,
    )
    text = render_stale_slot_continuation_review(review)
    report_dir = settings.output.reports_dir / date_text
    obsidian_dir = None if settings.output.obsidian_dir is None else settings.output.obsidian_dir / "Reports" / date_text
    prefix = f"stale_slot_continuation_review_{date_text}"
    version = next_report_version([report_dir, obsidian_dir], prefix)
    filename = versioned_markdown_filename(prefix, version)
    paths: list[Path] = []
    for directory in [report_dir, obsidian_dir]:
        if directory is None:
            continue
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / filename
        path.write_text(text, encoding="utf-8")
        paths.append(path)
    return review, paths


def _outcome_to_horizon(
    klines_after_decision: list[list],
    *,
    decision_ms: int,
    horizon_bars: int,
    reference_price: float,
    risk_per_unit: float,
    stop_loss: float,
    take_profit_1: float,
    step_ms: int,
    intrabar_policy: str,
) -> tuple[float | None, bool]:
    target_ms = decision_ms + horizon_bars * step_ms
    if risk_per_unit <= 0:
        return None, True
    for kline in klines_after_decision:
        close_ms = _kline_close_ms(kline, step_ms)
        if close_ms > target_ms:
            break
        high = float(kline[2])
        low = float(kline[3])
        stop_hit = low <= stop_loss
        tp1_hit = high >= take_profit_1
        if stop_hit and tp1_hit:
            price = stop_loss if intrabar_policy == "stop_first" else take_profit_1
            return (price - reference_price) / risk_per_unit, False
        if stop_hit:
            return (stop_loss - reference_price) / risk_per_unit, False
        if tp1_hit:
            return (take_profit_1 - reference_price) / risk_per_unit, False
    for kline in klines_after_decision:
        if _kline_close_ms(kline, step_ms) == target_ms:
            return (float(kline[4]) - reference_price) / risk_per_unit, False
    return None, True


def _path_outcome_from_decision(
    klines: list[list],
    *,
    decision_ms: int,
    reference_price: float,
    risk_per_unit: float,
    stop_loss: float,
    take_profit_1: float,
    step_ms: int,
    intrabar_policy: str,
) -> ReplacementPathOutcome:
    klines_after = [kline for kline in klines if _kline_close_ms(kline, step_ms) > decision_ms]
    r_24, censored_24 = _outcome_to_horizon(
        klines_after,
        decision_ms=decision_ms,
        horizon_bars=24,
        reference_price=reference_price,
        risk_per_unit=risk_per_unit,
        stop_loss=stop_loss,
        take_profit_1=take_profit_1,
        step_ms=step_ms,
        intrabar_policy=intrabar_policy,
    )
    r_42, censored_42 = _outcome_to_horizon(
        klines_after,
        decision_ms=decision_ms,
        horizon_bars=42,
        reference_price=reference_price,
        risk_per_unit=risk_per_unit,
        stop_loss=stop_loss,
        take_profit_1=take_profit_1,
        step_ms=step_ms,
        intrabar_policy=intrabar_policy,
    )
    r_60, censored_60 = _outcome_to_horizon(
        klines_after,
        decision_ms=decision_ms,
        horizon_bars=60,
        reference_price=reference_price,
        risk_per_unit=risk_per_unit,
        stop_loss=stop_loss,
        take_profit_1=take_profit_1,
        step_ms=step_ms,
        intrabar_policy=intrabar_policy,
    )
    first_hit, first_hit_time = _first_hit_after_stale(
        klines_after,
        stop_loss=stop_loss,
        take_profit_1=take_profit_1,
        step_ms=step_ms,
        intrabar_policy=intrabar_policy,
    )
    if klines_after and risk_per_unit > 0:
        mfe_r = (max(float(kline[2]) for kline in klines_after) - reference_price) / risk_per_unit
        mae_r = (min(float(kline[3]) for kline in klines_after) - reference_price) / risk_per_unit
    else:
        mfe_r = None
        mae_r = None
    return ReplacementPathOutcome(
        r_24=r_24,
        r_42=r_42,
        r_60=r_60,
        first_hit_outcome=first_hit,
        first_hit_time_utc=first_hit_time,
        mfe_r=mfe_r,
        mae_r=mae_r,
        right_censored=censored_24 or censored_42 or censored_60,
    )


def _slot_unrealized_r(slot: dict) -> float:
    cash_risk = slot.get("cash_risk")
    if cash_risk is None or float(cash_risk) <= 0:
        return 0.0
    return float(slot.get("unrealized_pnl") or 0.0) / float(cash_risk)


def _eligible_pre_tp1_stale_slots(event: dict, stale_bars: int) -> list[dict]:
    output = []
    for slot in event.get("active_snapshot_after_exits", []):
        if not isinstance(slot, dict):
            continue
        if str(slot.get("status")) != "ENTERED":
            continue
        if slot.get("tp1_hit_at_utc") is not None:
            continue
        holding_bars = slot.get("holding_bars")
        if holding_bars is None or int(holding_bars) < stale_bars:
            continue
        output.append(slot)
    return output


def _trade_by_id(trades: list[dict]) -> dict[str, dict]:
    return {str(trade.get("trade_id")): trade for trade in trades if trade.get("trade_id") is not None}


def _slot_outcome(
    slot: dict,
    trade_by_id: dict[str, dict],
    klines_by_symbol: dict[str, dict[str, list[list]]],
    *,
    interval: str,
    decision_ms: int,
    step_ms: int,
    intrabar_policy: str,
) -> ReplacementPathOutcome | None:
    trade = trade_by_id.get(str(slot.get("trade_id")))
    if trade is None:
        return None
    symbol = str(slot.get("symbol", ""))
    klines = klines_by_symbol.get(symbol, {}).get(interval, [])
    by_close = _kline_by_close_ms(klines, step_ms)
    decision_kline = by_close.get(decision_ms)
    if decision_kline is None:
        return None
    entry_price = trade.get("entry_price_filled")
    stop_loss = trade.get("stop_loss")
    take_profit_1 = trade.get("take_profit_1")
    if entry_price is None or stop_loss is None or take_profit_1 is None:
        return None
    risk_per_unit = float(entry_price) - float(stop_loss)
    if risk_per_unit <= 0:
        return None
    return _path_outcome_from_decision(
        klines,
        decision_ms=decision_ms,
        reference_price=float(decision_kline[4]),
        risk_per_unit=risk_per_unit,
        stop_loss=float(stop_loss),
        take_profit_1=float(take_profit_1),
        step_ms=step_ms,
        intrabar_policy=intrabar_policy,
    )


def _candidate_outcome(
    event: dict,
    klines_by_symbol: dict[str, dict[str, list[list]]],
    *,
    interval: str,
    decision_ms: int,
    step_ms: int,
    intrabar_policy: str,
) -> ReplacementPathOutcome | None:
    entry_price = event.get("candidate_entry_price_filled")
    stop_loss = event.get("candidate_stop_loss")
    take_profit_1 = event.get("candidate_take_profit_1")
    if entry_price is None or stop_loss is None or take_profit_1 is None:
        return None
    risk_per_unit = float(entry_price) - float(stop_loss)
    if risk_per_unit <= 0:
        return None
    symbol = str(event.get("symbol", ""))
    klines = klines_by_symbol.get(symbol, {}).get(interval, [])
    return _path_outcome_from_decision(
        klines,
        decision_ms=decision_ms,
        reference_price=float(entry_price),
        risk_per_unit=risk_per_unit,
        stop_loss=float(stop_loss),
        take_profit_1=float(take_profit_1),
        step_ms=step_ms,
        intrabar_policy=intrabar_policy,
    )


def _delta(candidate_r: float | None, slot_r: float | None) -> float | None:
    if candidate_r is None or slot_r is None:
        return None
    return candidate_r - slot_r


def _trimmed_mean(values: list[float], trim_pct: float = 0.2) -> float | None:
    clean = sorted(values)
    if not clean:
        return None
    trim = int(len(clean) * trim_pct)
    trimmed = clean[trim : len(clean) - trim] if trim > 0 and len(clean) > trim * 2 else clean
    return sum(trimmed) / len(trimmed) if trimmed else None


def _top_contribution_share(values: list[float | None]) -> dict[str, float | int | None]:
    clean = [float(value) for value in values if value is not None]
    positives = sorted([value for value in clean if value > 0], reverse=True)
    total_positive = sum(positives)
    return {
        "positive_n": len(positives),
        "top1_share_pct": None if total_positive <= 0 or not positives else positives[0] / total_positive * 100,
        "top3_share_pct": None if total_positive <= 0 or not positives else sum(positives[:3]) / total_positive * 100,
        "trimmed_mean_20pct": _trimmed_mean(clean, 0.2),
    }


def _month_leave_one_out(events: list[BlockedCandidateVsStaleSlotEvent]) -> dict[str, float | None]:
    months = sorted({event.month for event in events})
    output: dict[str, float | None] = {}
    for month in months:
        values = [event.net_replacement_delta_r_42 for event in events if event.month != month]
        output[month] = _summary(values)["mean"]
    return output


def build_blocked_candidate_vs_stale_slot_review(
    settings: Settings,
    run_id: str,
    *,
    stale_bars: int = 42,
    report_date: str | None = None,
    progress=None,
) -> BlockedCandidateVsStaleSlotReview:
    from .backtest.history import batch_load_klines_cached, interval_ms

    run = _source_run_row(settings, run_id)
    result, replay_settings, symbols, _dynamic_mode, _max_symbols = _replay_source_run(settings, run, progress=progress)
    interval = replay_settings.backtest.primary_interval
    step_ms = interval_ms(interval)
    start_ms = _ms_from_iso(str(run["start_utc"]))
    end_ms = _ms_from_iso(str(run["end_utc"]))
    klines_by_symbol = batch_load_klines_cached(replay_settings, symbols, [interval], start_ms, end_ms)
    replay_trades = _trade_dicts_from_result(result)
    trades_by_id = _trade_by_id(replay_trades)
    events = _blocked_event_dicts(result)
    rank1_events = [event for event in events if int(event.get("candidate_rank", 0)) == 1]
    comparison_events: list[BlockedCandidateVsStaleSlotEvent] = []
    without_eligible_stale = 0
    for event in rank1_events:
        eligible_slots = _eligible_pre_tp1_stale_slots(event, stale_bars)
        if not eligible_slots:
            without_eligible_stale += 1
            continue
        decision_ms = _ms_from_iso(str(event["decision_time_utc"]))
        candidate = _candidate_outcome(
            event,
            klines_by_symbol,
            interval=interval,
            decision_ms=decision_ms,
            step_ms=step_ms,
            intrabar_policy=replay_settings.backtest.intrabar_policy,
        )
        if candidate is None:
            without_eligible_stale += 1
            continue
        oldest_slot = sorted(
            eligible_slots,
            key=lambda slot: (-int(slot.get("holding_bars") or 0), str(slot.get("trade_id", ""))),
        )[0]
        lowest_unrealized_slot = sorted(eligible_slots, key=lambda slot: (_slot_unrealized_r(slot), str(slot.get("trade_id", ""))))[0]
        oldest_outcome = _slot_outcome(
            oldest_slot,
            trades_by_id,
            klines_by_symbol,
            interval=interval,
            decision_ms=decision_ms,
            step_ms=step_ms,
            intrabar_policy=replay_settings.backtest.intrabar_policy,
        )
        lowest_outcome = _slot_outcome(
            lowest_unrealized_slot,
            trades_by_id,
            klines_by_symbol,
            interval=interval,
            decision_ms=decision_ms,
            step_ms=step_ms,
            intrabar_policy=replay_settings.backtest.intrabar_policy,
        )
        if oldest_outcome is None:
            without_eligible_stale += 1
            continue
        slot_outcomes = [
            outcome
            for slot in eligible_slots
            for outcome in [
                _slot_outcome(
                    slot,
                    trades_by_id,
                    klines_by_symbol,
                    interval=interval,
                    decision_ms=decision_ms,
                    step_ms=step_ms,
                    intrabar_policy=replay_settings.backtest.intrabar_policy,
                )
            ]
            if outcome is not None
        ]
        oracle_delta = None
        slot_r_42_values = [outcome.r_42 for outcome in slot_outcomes if outcome.r_42 is not None]
        if candidate.r_42 is not None and slot_r_42_values:
            oracle_delta = candidate.r_42 - min(slot_r_42_values)
        comparison_events.append(
            BlockedCandidateVsStaleSlotEvent(
                event_id=str(event.get("event_id", "")),
                decision_time_utc=str(event["decision_time_utc"]),
                month=str(event["decision_time_utc"])[:7],
                candidate_symbol=str(event.get("symbol", "")),
                candidate_rank=int(event.get("candidate_rank", 0)),
                selected_slot_trade_id=str(oldest_slot.get("trade_id", "")),
                selected_slot_symbol=str(oldest_slot.get("symbol", "")),
                selected_slot_holding_bars=int(oldest_slot.get("holding_bars") or 0),
                eligible_stale_slots=len(eligible_slots),
                candidate_same_bar_stop_possible=bool(event.get("same_bar_entry_exit_possible", False)),
                candidate_same_bar_tp1_possible=bool(event.get("same_bar_entry_tp1_possible", False)),
                candidate_r_42=candidate.r_42,
                stale_slot_r_42=oldest_outcome.r_42,
                net_replacement_delta_r_42=_delta(candidate.r_42, oldest_outcome.r_42),
                net_replacement_delta_r_24=_delta(candidate.r_24, oldest_outcome.r_24),
                net_replacement_delta_r_60=_delta(candidate.r_60, oldest_outcome.r_60),
                lowest_unrealized_slot_delta_r_42=None if lowest_outcome is None else _delta(candidate.r_42, lowest_outcome.r_42),
                oracle_upper_bound_delta_r_42=oracle_delta,
                candidate_first_hit=candidate.first_hit_outcome,
                stale_slot_first_hit=oldest_outcome.first_hit_outcome,
                right_censored=candidate.right_censored or oldest_outcome.right_censored,
            )
        )

    delta_42_summary = _summary([event.net_replacement_delta_r_42 for event in comparison_events])
    positive_ratio = delta_42_summary["positive_pct"]
    mean_42 = delta_42_summary["mean"]
    right_censored_count = sum(1 for event in comparison_events if event.right_censored)
    if not comparison_events:
        verdict = "replacement_comparison_sample_empty"
        reason = "No rank-1 blocked events had an eligible pre-TP1 stale slot, so replacement comparison cannot be estimated from this run."
    elif right_censored_count / len(comparison_events) > 0.25:
        verdict = "replacement_comparison_inconclusive_censored"
        reason = "Replacement comparison has too much right-censoring for a stable judgment."
    elif mean_42 is not None and mean_42 > 0 and positive_ratio is not None and positive_ratio >= 55:
        verdict = "retest_replacement_candidate"
        reason = "Rank-1 blocked candidates outperform oldest eligible pre-TP1 stale slots on average and in a majority of comparison events, but this remains diagnostic and not deployable."
    else:
        verdict = "replacement_edge_not_supported"
        reason = "Rank-1 blocked candidates do not show a broad enough 42-bar net replacement edge over oldest eligible pre-TP1 stale slots."

    return BlockedCandidateVsStaleSlotReview(
        source_run_id=run_id,
        replay_run_id=result.run_id,
        report_date=report_date or _local_now().strftime("%Y-%m-%d"),
        start_utc=str(run["start_utc"]),
        end_utc=str(run["end_utc"]),
        source_commit_hash=str(run["commit_hash"]),
        stale_bars=stale_bars,
        total_blocked_events=len(events),
        rank1_blocked_events=len(rank1_events),
        eligible_comparison_events=len(comparison_events),
        rank1_without_eligible_stale_slot=without_eligible_stale,
        same_bar_stop_possible_events=sum(1 for event in comparison_events if event.candidate_same_bar_stop_possible),
        same_bar_tp1_possible_events=sum(1 for event in comparison_events if event.candidate_same_bar_tp1_possible),
        right_censored_count=right_censored_count,
        net_delta_r_24_summary=_summary([event.net_replacement_delta_r_24 for event in comparison_events]),
        net_delta_r_42_summary=delta_42_summary,
        net_delta_r_60_summary=_summary([event.net_replacement_delta_r_60 for event in comparison_events]),
        lowest_unrealized_delta_r_42_summary=_summary([event.lowest_unrealized_slot_delta_r_42 for event in comparison_events]),
        oracle_upper_bound_delta_r_42_summary=_summary([event.oracle_upper_bound_delta_r_42 for event in comparison_events]),
        first_hit_pair_counts=dict(sorted(Counter(f"{event.candidate_first_hit} vs {event.stale_slot_first_hit}" for event in comparison_events).items())),
        month_leave_one_out_mean_r_42=_month_leave_one_out(comparison_events),
        top_contribution_share_r_42=_top_contribution_share([event.net_replacement_delta_r_42 for event in comparison_events]),
        verdict=verdict,
        reason=reason,
        events=comparison_events,
    )


def render_blocked_candidate_vs_stale_slot_review(review: BlockedCandidateVsStaleSlotReview) -> str:
    now = _local_now()
    lines = [
        "---",
        f"created: {now.strftime('%Y-%m-%d %H:%M:%S %Z')}",
        "tags:",
        "  - crypto",
        "  - trading-system",
        "  - blocked-candidate-vs-stale-slot-review",
        "experiment: blocked_candidate_vs_stale_slot_review",
        f"source_run_id: {review.source_run_id}",
        f"replay_run_id: {review.replay_run_id}",
        f"verdict: {review.verdict}",
        "---",
        "",
        "# blocked_candidate_vs_stale_slot_review",
        "",
        "## Plain-language conclusion",
        "",
        review.reason,
        "",
        "This report is diagnostic only. It does not deploy replacement logic, does not change `max_active_positions`, and does not modify `config/settings.toml`, backtest behavior, paper state, strategy defaults, or saved backtest rows.",
        "",
        "## Scope",
        "",
        "| Field | Value |",
        "|---|---:|",
        f"| source_run_id | `{review.source_run_id}` |",
        f"| replay_run_id | `{review.replay_run_id}` |",
        f"| window | `{review.start_utc}` -> `{review.end_utc}` |",
        f"| source_commit_hash | `{review.source_commit_hash}` |",
        f"| stale_threshold | {review.stale_bars} bars |",
        "",
        "## Sample Definition",
        "",
        "Primary sample uses only `candidate_rank=1` blocked events. The replacement slot is the oldest active slot that is still pre-TP1 and has `holding_bars >= stale_bars`. Post-TP1 slots are excluded from V1 eligibility. Oracle is reported only as an upper bound.",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| total_blocked_events | {review.total_blocked_events} |",
        f"| rank1_blocked_events | {review.rank1_blocked_events} |",
        f"| eligible_comparison_events | {review.eligible_comparison_events} |",
        f"| rank1_without_eligible_stale_slot | {review.rank1_without_eligible_stale_slot} |",
        f"| same_bar_stop_possible_events | {review.same_bar_stop_possible_events} |",
        f"| same_bar_tp1_possible_events | {review.same_bar_tp1_possible_events} |",
        f"| right_censored_count | {review.right_censored_count} |",
        "",
        "## Net Replacement Delta R",
        "",
        "`net_replacement_delta_R = candidate_R - selected_stale_slot_R`; each leg is normalized by its own per-unit risk, so this is a path-quality diagnostic rather than a full portfolio PnL simulation.",
        "",
        "| Metric | n | mean | median | positive_pct | min | max |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for label, summary in [
        ("net_replacement_delta_R_24", review.net_delta_r_24_summary),
        ("net_replacement_delta_R_42", review.net_delta_r_42_summary),
        ("net_replacement_delta_R_60", review.net_delta_r_60_summary),
        ("lowest_unrealized_slot_delta_R_42", review.lowest_unrealized_delta_r_42_summary),
        ("oracle_upper_bound_delta_R_42", review.oracle_upper_bound_delta_r_42_summary),
    ]:
        lines.append(
            f"| {label} | {_fmt_summary_value(summary['n'])} | {_fmt_summary_value(summary['mean'])} | "
            f"{_fmt_summary_value(summary['median'])} | {_fmt_summary_value(summary['positive_pct'])} | "
            f"{_fmt_summary_value(summary['min'])} | {_fmt_summary_value(summary['max'])} |"
        )
    lines.extend(
        [
            "",
            "## Robustness",
            "",
            "| Metric | Value |",
            "|---|---:|",
            f"| positive_n | {_fmt_summary_value(review.top_contribution_share_r_42['positive_n'])} |",
            f"| top1_positive_contribution_share_pct | {_fmt_summary_value(review.top_contribution_share_r_42['top1_share_pct'])} |",
            f"| top3_positive_contribution_share_pct | {_fmt_summary_value(review.top_contribution_share_r_42['top3_share_pct'])} |",
            f"| 20pct_trimmed_mean_R_42 | {_fmt_summary_value(review.top_contribution_share_r_42['trimmed_mean_20pct'])} |",
            "",
            "## First-Hit Pairs",
            "",
            "| Candidate vs Stale Slot | Count |",
            "|---|---:|",
        ]
    )
    if review.first_hit_pair_counts:
        for pair, count in review.first_hit_pair_counts.items():
            lines.append(f"| `{pair}` | {count} |")
    else:
        lines.append("| n/a | 0 |")
    lines.extend(["", "## Month Leave-One-Out", "", "| Removed Month | Mean R42 |", "|---|---:|"])
    if review.month_leave_one_out_mean_r_42:
        for month, value in review.month_leave_one_out_mean_r_42.items():
            lines.append(f"| {month} | {_fmt_summary_value(value)} |")
    else:
        lines.append("| n/a | n/a |")
    lines.extend(
        [
            "",
            "## First Events",
            "",
            "| # | Time | Candidate | Slot | Slot Bars | Delta R42 | Candidate R42 | Slot R42 | Candidate Hit | Slot Hit | Same-bar Flags |",
            "|---:|---|---|---|---:|---:|---:|---:|---|---|---|",
        ]
    )
    for index, event in enumerate(review.events[:40], start=1):
        flags = []
        if event.candidate_same_bar_stop_possible:
            flags.append("stop")
        if event.candidate_same_bar_tp1_possible:
            flags.append("tp1")
        lines.append(
            f"| {index} | `{event.decision_time_utc}` | `{event.candidate_symbol}` | `{event.selected_slot_symbol}` | "
            f"{event.selected_slot_holding_bars} | {_fmt_summary_value(event.net_replacement_delta_r_42)} | "
            f"{_fmt_summary_value(event.candidate_r_42)} | {_fmt_summary_value(event.stale_slot_r_42)} | "
            f"`{event.candidate_first_hit}` | `{event.stale_slot_first_hit}` | {','.join(flags) or 'none'} |"
        )
    if not review.events:
        lines.append("| n/a | n/a | n/a | n/a | 0 | n/a | n/a | n/a | n/a | n/a | none |")
    lines.extend(["", "## Decision", "", f"`{review.verdict}`", "", "## Next Action", ""])
    if review.verdict == "retest_replacement_candidate":
        lines.append("Proceed only to a shadow replacement experiment design. Do not deploy and do not modify `max_active_positions` until a full state-machine shadow replay proves portfolio-level benefit after costs and path effects.")
    elif review.verdict == "replacement_edge_not_supported":
        lines.append("Do not proceed to shadow replacement yet. Revisit capacity only if a stronger, pre-declared slot selection rule or broader walk-forward evidence appears.")
    elif review.verdict == "replacement_comparison_inconclusive_censored":
        lines.append("Retest on a window with lower right-censoring before interpreting replacement value.")
    else:
        lines.append("Stop the replacement branch for this source run because no eligible diagnostic comparison sample was available.")
    lines.extend(
        [
            "",
            "## Raw Summary",
            "",
            "```json",
            json.dumps(asdict(review), ensure_ascii=False, indent=2),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def write_blocked_candidate_vs_stale_slot_review_report(
    settings: Settings,
    run_id: str,
    *,
    stale_bars: int = 42,
    report_date: str | None = None,
    progress=None,
) -> tuple[BlockedCandidateVsStaleSlotReview, list[Path]]:
    date_text = report_date or _local_now().strftime("%Y-%m-%d")
    review = build_blocked_candidate_vs_stale_slot_review(
        settings,
        run_id,
        stale_bars=stale_bars,
        report_date=date_text,
        progress=progress,
    )
    text = render_blocked_candidate_vs_stale_slot_review(review)
    report_dir = settings.output.reports_dir / date_text
    obsidian_dir = None if settings.output.obsidian_dir is None else settings.output.obsidian_dir / "Reports" / date_text
    prefix = f"blocked_candidate_vs_stale_slot_review_{date_text}"
    version = next_report_version([report_dir, obsidian_dir], prefix)
    filename = versioned_markdown_filename(prefix, version)
    paths: list[Path] = []
    for directory in [report_dir, obsidian_dir]:
        if directory is None:
            continue
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / filename
        path.write_text(text, encoding="utf-8")
        paths.append(path)
    return review, paths


def _event_value(event: dict, key: str) -> float | None:
    value = event.get(key)
    if value is None:
        return None
    return float(value)


def _events_summary(events: list[dict], key: str) -> dict[str, float | int | None]:
    return _summary([_event_value(event, key) for event in events])


def _first_event_per_stale_trade(events: list[dict]) -> list[dict]:
    first_by_trade: dict[str, dict] = {}
    for event in sorted(events, key=lambda item: str(item.get("decision_time_utc", ""))):
        trade_id = str(event.get("selected_slot_trade_id", ""))
        if trade_id and trade_id not in first_by_trade:
            first_by_trade[trade_id] = event
    return list(first_by_trade.values())


def _cluster_bootstrap_mean(events: list[dict], *, key: str, cluster_key: str, seed: int = 20260727, iterations: int = 5000) -> dict[str, float | int | None]:
    clusters: dict[str, list[float]] = {}
    for event in events:
        cluster = str(event.get(cluster_key, ""))
        value = _event_value(event, key)
        if not cluster or value is None:
            continue
        clusters.setdefault(cluster, []).append(value)
    cluster_means = [sum(values) / len(values) for values in clusters.values() if values]
    if not cluster_means:
        return {"clusters": 0, "iterations": iterations, "mean": None, "p05": None, "p50": None, "p95": None}
    rng = random.Random(seed)
    sampled_means: list[float] = []
    for _ in range(iterations):
        draw = [rng.choice(cluster_means) for _ in cluster_means]
        sampled_means.append(sum(draw) / len(draw))
    sampled_means.sort()

    def pct(p: float) -> float:
        index = int(round((len(sampled_means) - 1) * p))
        return sampled_means[index]

    return {
        "clusters": len(cluster_means),
        "iterations": iterations,
        "mean": sum(cluster_means) / len(cluster_means),
        "p05": pct(0.05),
        "p50": pct(0.50),
        "p95": pct(0.95),
    }


def build_replacement_closure_audit(
    stage1_json_path: Path,
    stage4_report_path: Path,
    *,
    report_date: str | None = None,
) -> ReplacementClosureAudit:
    stage1 = json.loads(stage1_json_path.read_text(encoding="utf-8"))
    stage4 = _extract_raw_json(stage4_report_path.read_text(encoding="utf-8"), "Raw Summary")
    blocked_events = stage1.get("events", []) if isinstance(stage1.get("events"), list) else []
    comparison_events = stage4.get("events", []) if isinstance(stage4.get("events"), list) else []
    rank1_events = [event for event in blocked_events if int(event.get("candidate_rank", 0) or 0) == 1]
    stale_counts = Counter(str(event.get("selected_slot_trade_id", "")) for event in comparison_events if event.get("selected_slot_trade_id"))
    total_comparisons = sum(stale_counts.values())
    first_per_stale = _first_event_per_stale_trade(comparison_events)
    no_july = [event for event in comparison_events if str(event.get("month", "")) != "2025-07"]
    no_same_bar = [
        event
        for event in comparison_events
        if not bool(event.get("candidate_same_bar_stop_possible")) and not bool(event.get("candidate_same_bar_tp1_possible"))
    ]
    stale_top = [count for _trade_id, count in stale_counts.most_common()]
    stale_top1_share = None if total_comparisons <= 0 else stale_top[0] / total_comparisons * 100
    stale_top3_share = None if total_comparisons <= 0 else sum(stale_top[:3]) / total_comparisons * 100
    summaries = {
        "net_replacement_delta_r_24": _events_summary(first_per_stale, "net_replacement_delta_r_24"),
        "net_replacement_delta_r_42": _events_summary(first_per_stale, "net_replacement_delta_r_42"),
        "net_replacement_delta_r_60": _events_summary(first_per_stale, "net_replacement_delta_r_60"),
    }
    no_july_summaries = {
        "net_replacement_delta_r_24": _events_summary(no_july, "net_replacement_delta_r_24"),
        "net_replacement_delta_r_42": _events_summary(no_july, "net_replacement_delta_r_42"),
        "net_replacement_delta_r_60": _events_summary(no_july, "net_replacement_delta_r_60"),
    }
    no_same_bar_summaries = {
        "net_replacement_delta_r_24": _events_summary(no_same_bar, "net_replacement_delta_r_24"),
        "net_replacement_delta_r_42": _events_summary(no_same_bar, "net_replacement_delta_r_42"),
        "net_replacement_delta_r_60": _events_summary(no_same_bar, "net_replacement_delta_r_60"),
    }
    cluster_bootstrap = _cluster_bootstrap_mean(
        comparison_events,
        key="net_replacement_delta_r_42",
        cluster_key="selected_slot_trade_id",
    )
    top_contribution = _top_contribution_share([_event_value(event, "net_replacement_delta_r_42") for event in comparison_events])
    first_r42 = summaries["net_replacement_delta_r_42"]
    no_july_r42 = no_july_summaries["net_replacement_delta_r_42"]
    no_same_bar_r42 = no_same_bar_summaries["net_replacement_delta_r_42"]
    bootstrap_p05 = cluster_bootstrap["p05"]
    if comparison_events and (
        (first_r42["median"] is not None and first_r42["median"] < 0)
        or (no_july_r42["mean"] is not None and no_july_r42["mean"] <= 0)
        or (no_same_bar_r42["median"] is not None and no_same_bar_r42["median"] < 0)
        or (isinstance(bootstrap_p05, float) and bootstrap_p05 < 0)
    ):
        verdict = "paused_no_stable_executable_edge"
        reason = "Stage 4 remains too concentrated and unstable after de-duplication and robustness checks, so capacity replacement should be frozen until a new pre-declared mechanism exists."
    else:
        verdict = "replacement_closure_requires_manual_review"
        reason = "Closure checks did not clearly reject the Stage 4 sample, but this is still only diagnostic and cannot justify deployment without a new pre-declared replacement mechanism."
    return ReplacementClosureAudit(
        source_run_id=str(stage4.get("source_run_id", stage1.get("source_run_id", ""))),
        replay_run_id=str(stage4.get("replay_run_id", "")),
        report_date=report_date or _local_now().strftime("%Y-%m-%d"),
        stage1_json_path=str(stage1_json_path),
        stage4_report_path=str(stage4_report_path),
        start_utc=str(stage4.get("start_utc", stage1.get("start_utc", ""))),
        end_utc=str(stage4.get("end_utc", stage1.get("end_utc", ""))),
        total_blocked_events=len(blocked_events),
        unique_blocked_timestamps=len({str(event.get("decision_time_utc", "")) for event in blocked_events}),
        rank1_blocked_events=len(rank1_events),
        unique_rank1_timestamps=len({str(event.get("decision_time_utc", "")) for event in rank1_events}),
        eligible_comparison_events=len(comparison_events),
        unique_comparison_timestamps=len({str(event.get("decision_time_utc", "")) for event in comparison_events}),
        unique_comparison_candidates=len({str(event.get("candidate_symbol", "")) for event in comparison_events}),
        unique_stale_trades=len(stale_counts),
        stale_trade_duplicate_counts=dict(stale_counts.most_common()),
        stale_trade_top1_share_pct=stale_top1_share,
        stale_trade_top3_share_pct=stale_top3_share,
        first_event_per_stale_trade_summaries=summaries,
        exclude_2025_07_summaries=no_july_summaries,
        exclude_same_bar_ambiguous_summaries=no_same_bar_summaries,
        cluster_bootstrap_mean_r_42=cluster_bootstrap,
        top_contribution_share_r_42=top_contribution,
        verdict=verdict,
        reason=reason,
    )


def render_replacement_closure_audit(audit: ReplacementClosureAudit) -> str:
    now = _local_now()
    lines = [
        "---",
        f"created: {now.strftime('%Y-%m-%d %H:%M:%S %Z')}",
        "tags:",
        "  - crypto",
        "  - trading-system",
        "  - replacement-closure-audit",
        "experiment: replacement_closure_audit",
        f"source_run_id: {audit.source_run_id}",
        f"replay_run_id: {audit.replay_run_id}",
        f"verdict: {audit.verdict}",
        "---",
        "",
        "# replacement_closure_audit",
        "",
        "## Plain-language conclusion",
        "",
        audit.reason,
        "",
        "This is a closure appendix for Stage 4 only. It does not introduce a trading rule, does not proceed to Stage 5 shadow replacement, does not raise `max_active_positions`, and does not modify production config.",
        "",
        "## Scope",
        "",
        "| Field | Value |",
        "|---|---:|",
        f"| source_run_id | `{audit.source_run_id}` |",
        f"| replay_run_id | `{audit.replay_run_id}` |",
        f"| window | `{audit.start_utc}` -> `{audit.end_utc}` |",
        f"| stage1_json | `{audit.stage1_json_path}` |",
        f"| stage4_report | `{audit.stage4_report_path}` |",
        "",
        "## Event Uniqueness",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| total_blocked_events | {audit.total_blocked_events} |",
        f"| unique_blocked_timestamps | {audit.unique_blocked_timestamps} |",
        f"| rank1_blocked_events | {audit.rank1_blocked_events} |",
        f"| unique_rank1_timestamps | {audit.unique_rank1_timestamps} |",
        f"| eligible_comparison_events | {audit.eligible_comparison_events} |",
        f"| unique_comparison_timestamps | {audit.unique_comparison_timestamps} |",
        f"| unique_comparison_candidates | {audit.unique_comparison_candidates} |",
        f"| unique_stale_trades | {audit.unique_stale_trades} |",
        f"| stale_trade_top1_share_pct | {_fmt_summary_value(audit.stale_trade_top1_share_pct)} |",
        f"| stale_trade_top3_share_pct | {_fmt_summary_value(audit.stale_trade_top3_share_pct)} |",
        "",
        "## Stale Trade Concentration",
        "",
        "| Stale Trade ID | Comparison Events |",
        "|---|---:|",
    ]
    if audit.stale_trade_duplicate_counts:
        for trade_id, count in audit.stale_trade_duplicate_counts.items():
            lines.append(f"| `{trade_id}` | {count} |")
    else:
        lines.append("| n/a | 0 |")
    lines.extend(
        [
            "",
            "## Robustness Summaries",
            "",
            "| Check | Metric | n | mean | median | positive_pct | min | max |",
            "|---|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for check_name, group in [
        ("first_event_per_stale_trade", audit.first_event_per_stale_trade_summaries),
        ("exclude_2025_07", audit.exclude_2025_07_summaries),
        ("exclude_same_bar_ambiguous", audit.exclude_same_bar_ambiguous_summaries),
    ]:
        for metric, summary in group.items():
            lines.append(
                f"| {check_name} | `{metric}` | {_fmt_summary_value(summary['n'])} | "
                f"{_fmt_summary_value(summary['mean'])} | {_fmt_summary_value(summary['median'])} | "
                f"{_fmt_summary_value(summary['positive_pct'])} | {_fmt_summary_value(summary['min'])} | {_fmt_summary_value(summary['max'])} |"
            )
    lines.extend(
        [
            "",
            "## Cluster Bootstrap",
            "",
            "| Metric | Value |",
            "|---|---:|",
        ]
    )
    for key in ["clusters", "iterations", "mean", "p05", "p50", "p95"]:
        lines.append(f"| {key} | {_fmt_summary_value(audit.cluster_bootstrap_mean_r_42.get(key))} |")
    lines.extend(
        [
            "",
            "## Winner Contribution",
            "",
            "| Metric | Value |",
            "|---|---:|",
            f"| positive_n | {_fmt_summary_value(audit.top_contribution_share_r_42['positive_n'])} |",
            f"| top1_positive_contribution_share_pct | {_fmt_summary_value(audit.top_contribution_share_r_42['top1_share_pct'])} |",
            f"| top3_positive_contribution_share_pct | {_fmt_summary_value(audit.top_contribution_share_r_42['top3_share_pct'])} |",
            f"| 20pct_trimmed_mean_R_42 | {_fmt_summary_value(audit.top_contribution_share_r_42['trimmed_mean_20pct'])} |",
            "",
            "## Decision",
            "",
            f"`{audit.verdict}`",
            "",
            "## Next Action",
            "",
            "Freeze the current capacity replacement branch. Resume capacity research only with a new pre-declared slot-selection mechanism or broader walk-forward evidence; otherwise move back to capacity-neutral `atr_reclaim_0_35` entry-quality attribution.",
            "",
            "## Raw Summary",
            "",
            "```json",
            json.dumps(asdict(audit), ensure_ascii=False, indent=2),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def write_replacement_closure_audit_report(
    settings: Settings,
    stage1_json_path: Path,
    stage4_report_path: Path,
    *,
    report_date: str | None = None,
) -> tuple[ReplacementClosureAudit, list[Path]]:
    date_text = report_date or _local_now().strftime("%Y-%m-%d")
    audit = build_replacement_closure_audit(stage1_json_path, stage4_report_path, report_date=date_text)
    text = render_replacement_closure_audit(audit)
    report_dir = settings.output.reports_dir / date_text
    obsidian_dir = None if settings.output.obsidian_dir is None else settings.output.obsidian_dir / "Reports" / date_text
    prefix = f"replacement_closure_audit_{date_text}"
    version = next_report_version([report_dir, obsidian_dir], prefix)
    filename = versioned_markdown_filename(prefix, version)
    paths: list[Path] = []
    for directory in [report_dir, obsidian_dir]:
        if directory is None:
            continue
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / filename
        path.write_text(text, encoding="utf-8")
        paths.append(path)
    return audit, paths


def _file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _git_commit() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return "unknown"


def _git_dirty() -> bool:
    try:
        return bool(subprocess.check_output(["git", "status", "--short", "--untracked-files=no"], text=True).strip())
    except Exception:
        return True


def _ms_from_date(date_text: str) -> int:
    return int(datetime.fromisoformat(date_text).replace(tzinfo=timezone.utc).timestamp() * 1000)


def _interval_expected_bars(start_ms: int, end_ms: int, interval: str) -> int:
    step = {"1h": 3_600_000, "4h": 14_400_000, "1d": 86_400_000}[interval]
    return max(0, int((end_ms - start_ms) // step))


def _kline_cache_coverage(
    settings: Settings,
    symbols: list[str],
    *,
    start_ms: int,
    end_ms: int,
    interval: str,
) -> dict[str, int | float | str | list[str]]:
    expected = _interval_expected_bars(start_ms, end_ms, interval)
    if expected <= 0 or not symbols:
        return {
            "symbols": len(symbols),
            "expected_bars_per_symbol": expected,
            "complete_symbols": 0,
            "partial_symbols": 0,
            "empty_symbols": len(symbols),
            "min_bars": 0,
            "avg_bars": 0.0,
            "coverage_pct": 0.0,
            "partial_examples": [],
            "empty_examples": symbols[:10],
        }
    placeholders = ",".join("?" for _ in symbols)
    with connect_db(settings.output.database_path) as connection:
        rows = connection.execute(
            f"""
            SELECT symbol, COUNT(*) AS bars
            FROM kline_cache
            WHERE source = 'Binance'
              AND interval = ?
              AND open_time >= ?
              AND open_time < ?
              AND is_closed = 1
              AND symbol IN ({placeholders})
            GROUP BY symbol
            """,
            [interval, start_ms, end_ms, *symbols],
        ).fetchall()
    counts = {str(row["symbol"]): int(row["bars"]) for row in rows}
    complete = [symbol for symbol in symbols if counts.get(symbol, 0) >= expected]
    partial = [symbol for symbol in symbols if 0 < counts.get(symbol, 0) < expected]
    empty = [symbol for symbol in symbols if counts.get(symbol, 0) == 0]
    total_expected = expected * len(symbols)
    total_observed = sum(min(counts.get(symbol, 0), expected) for symbol in symbols)
    return {
        "symbols": len(symbols),
        "expected_bars_per_symbol": expected,
        "complete_symbols": len(complete),
        "partial_symbols": len(partial),
        "empty_symbols": len(empty),
        "min_bars": min((counts.get(symbol, 0) for symbol in symbols), default=0),
        "avg_bars": total_observed / len(symbols),
        "coverage_pct": total_observed / total_expected * 100 if total_expected else 0.0,
        "partial_examples": partial[:10],
        "empty_examples": empty[:10],
    }


def _prior_window_abtest_reports(settings: Settings, start: str, end: str) -> list[str]:
    pattern = f"abtest_dynamic_universe_*_{start}_{end}_v*.md"
    return [str(path) for path in sorted(settings.output.reports_dir.glob(f"**/{pattern}"))]


def build_atr_reclaim_n0_readiness_audit(
    settings: Settings,
    *,
    experiment_id: str,
    symbol_master_path: Path,
    start: str,
    end: str,
    reports_date: str | None = None,
) -> AtrReclaimN0ReadinessAudit:
    master = load_symbol_master(symbol_master_path)
    start_ms = _ms_from_date(start)
    end_ms = _ms_from_date(end)
    warmup_start_ms = min(
        start_ms - settings.backtest.warmup_1h_bars * 3_600_000,
        start_ms - settings.backtest.warmup_4h_bars * 14_400_000,
        start_ms - settings.backtest.warmup_1d_bars * 86_400_000,
    )
    coverage = {
        interval: _kline_cache_coverage(settings, master.symbols, start_ms=warmup_start_ms, end_ms=end_ms, interval=interval)
        for interval in ["1h", "4h", "1d"]
    }
    listing_dates_present = master.listing_dates is not None
    listed_after_start: list[str] = []
    missing_listing_dates_count: int | None = None
    if master.listing_dates is not None:
        for symbol in master.symbols:
            listed = master.listing_dates.get(symbol)
            if listed is None:
                continue
            if listed > start:
                listed_after_start.append(f"{symbol}:{listed}")
        missing_listing_dates_count = sum(1 for symbol in master.symbols if symbol not in master.listing_dates)
    opportunity_fields = {
        "symbol": True,
        "decision_time_utc": True,
        "status": True,
        "baseline_first_hit": True,
        "baseline_r": True,
        "mfe_r": True,
        "mae_r": True,
        "reclaim_margin_atr": True,
        "distance_to_support_atr": True,
        "stop_distance_atr": True,
        "capacity_state_at_decision": False,
        "stable_opportunity_id_shared_by_baseline_variant": False,
    }
    checks: dict[str, str] = {}
    checks["git_clean"] = "pass" if not _git_dirty() else "warn_dirty_worktree"
    checks["listing_dates"] = "pass" if listing_dates_present else "warn_missing_listing_dates"
    checks["listed_after_start"] = "pass" if listed_after_start == [] else "warn_symbols_listed_after_window_start"
    checks["kline_cache_coverage"] = (
        "pass"
        if all(float(item["coverage_pct"]) >= 99.0 and int(item["empty_symbols"]) == 0 for item in coverage.values())
        else "warn_or_fail_incomplete_local_cache"
    )
    checks["opportunity_alignment"] = (
        "pass"
        if opportunity_fields["stable_opportunity_id_shared_by_baseline_variant"] and opportunity_fields["capacity_state_at_decision"]
        else "warn_not_strictly_capacity_path_neutral"
    )
    prior_window_reports = _prior_window_abtest_reports(settings, start, end)
    checks["prior_window_exists"] = "pass" if prior_window_reports else "warn_no_prior_third_window_abtest_reference"

    hard_fail = (
        (float(coverage["4h"]["coverage_pct"]) < 50.0 or float(coverage["1d"]["coverage_pct"]) < 50.0)
        and not prior_window_reports
    )
    if hard_fail:
        verdict = "n0_blocked_cache_incomplete"
        reason = "Third-window readiness is blocked because local kline cache coverage is too incomplete for a reliable confirmatory retest."
    elif not listing_dates_present:
        verdict = "n0_conditional_pass_with_universe_bias_warning"
        reason = "Third-window retest can be run as a diagnostic, but the fixed symbol master lacks listing_dates, so the result cannot be treated as a clean confirmatory validation without survivor-bias caveat."
    elif not opportunity_fields["stable_opportunity_id_shared_by_baseline_variant"]:
        verdict = "n0_conditional_pass_with_alignment_warning"
        reason = "Third-window retest can run, but opportunity-level mechanism evidence must be labeled approximate until stable baseline/variant opportunity IDs are available."
    else:
        verdict = "n0_pass_ready_for_confirmatory_retest"
        reason = "Data, configuration, universe, and opportunity-alignment prerequisites are sufficient for the pre-declared confirmatory retest."

    return AtrReclaimN0ReadinessAudit(
        experiment_id=experiment_id,
        report_date=reports_date or _local_now().strftime("%Y-%m-%d"),
        start_utc=f"{start}T00:00:00+00:00",
        end_utc=f"{end}T00:00:00+00:00",
        symbol_master_path=str(symbol_master_path),
        symbol_master_source=master.source,
        symbol_master_created_at_utc=master.created_at_utc,
        symbol_master_hash=_file_sha256(symbol_master_path),
        settings_hash=_file_sha256(Path("config/settings.toml")),
        experiments_hash=_file_sha256(Path("config/experiments.toml")),
        git_commit=_git_commit(),
        git_dirty=_git_dirty(),
        baseline_config_snapshot={
            "entry_reclaim_close_enabled": settings.analysis.entry_reclaim_close_enabled,
            "entry_reclaim_min_atr_enabled": settings.analysis.entry_reclaim_min_atr_enabled,
            "entry_reclaim_min_atr": settings.analysis.entry_reclaim_min_atr,
            "relative_strength_soft_gate_enabled": settings.analysis.relative_strength_soft_gate_enabled,
            "max_active_positions": settings.backtest.max_active_positions,
            "intrabar_policy": settings.backtest.intrabar_policy,
            "primary_interval": settings.backtest.primary_interval,
            "maker_fee_bps": settings.backtest.maker_fee_bps,
            "taker_fee_bps": settings.backtest.taker_fee_bps,
            "entry_slippage_bps": settings.backtest.entry_slippage_bps,
            "stop_slippage_bps": settings.backtest.stop_slippage_bps,
        },
        variant_overrides={
            "analysis.entry_reclaim_min_atr_enabled": True,
            "analysis.entry_reclaim_min_atr": 0.35,
        },
        fixed_conditions={
            "production_settings_toml_unchanged": True,
            "replacement_enabled": False,
            "max_active_positions_changed": False,
            "score_sorting_changed": False,
            "additional_filters_stacked": False,
            "main_test": "baseline_vs_fixed_atr_reclaim_0_35_only",
            "nearby_thresholds": "exploratory_only_if_run",
        },
        symbol_master_count=len(master.symbols),
        listing_dates_present=listing_dates_present,
        listed_after_start_count=None if master.listing_dates is None else len(listed_after_start),
        listed_after_start_examples=listed_after_start[:10],
        missing_listing_dates_count=missing_listing_dates_count,
        kline_coverage=coverage,
        prior_third_window_abtests=prior_window_reports,
        opportunity_alignment_fields=opportunity_fields,
        readiness_checks=checks,
        verdict=verdict,
        reason=reason,
    )


def render_atr_reclaim_n0_readiness_audit(audit: AtrReclaimN0ReadinessAudit) -> str:
    now = _local_now()
    lines = [
        "---",
        f"created: {now.strftime('%Y-%m-%d %H:%M:%S %Z')}",
        "tags:",
        "  - crypto",
        "  - trading-system",
        "  - atr-reclaim-n0-readiness",
        "experiment: atr_reclaim_n0_readiness_audit",
        f"experiment_id: {audit.experiment_id}",
        f"verdict: {audit.verdict}",
        "---",
        "",
        "# atr_reclaim_n0_readiness_audit",
        "",
        "## Plain-language conclusion",
        "",
        audit.reason,
        "",
        "This is Stage N0 only. It freezes and audits prerequisites for the next retest; it does not run the `atr_reclaim_0_35` A/B, does not deploy, does not change `settings.toml`, does not restart replacement, and does not change `max_active_positions`.",
        "",
        "## Scope",
        "",
        "| Field | Value |",
        "|---|---:|",
        f"| experiment_id | `{audit.experiment_id}` |",
        f"| window | `{audit.start_utc}` -> `{audit.end_utc}` |",
        f"| git_commit | `{audit.git_commit}` |",
        f"| git_dirty | {audit.git_dirty} |",
        f"| settings_hash | `{audit.settings_hash}` |",
        f"| experiments_hash | `{audit.experiments_hash}` |",
        f"| symbol_master | `{audit.symbol_master_path}` |",
        f"| symbol_master_hash | `{audit.symbol_master_hash}` |",
        f"| symbol_master_count | {audit.symbol_master_count} |",
        f"| symbol_master_created_at_utc | `{audit.symbol_master_created_at_utc}` |",
        "",
        "## Frozen Test Definition",
        "",
        "| Field | Value |",
        "|---|---|",
    ]
    for key, value in audit.baseline_config_snapshot.items():
        lines.append(f"| baseline.{key} | `{value}` |")
    for key, value in audit.variant_overrides.items():
        lines.append(f"| variant.{key} | `{value}` |")
    for key, value in audit.fixed_conditions.items():
        lines.append(f"| fixed.{key} | `{value}` |")
    lines.extend(
        [
            "",
            "## Symbol Master Audit",
            "",
            "| Metric | Value |",
            "|---|---:|",
            f"| source | `{audit.symbol_master_source}` |",
            f"| listing_dates_present | {audit.listing_dates_present} |",
            f"| listed_after_start_count | {_fmt_summary_value(audit.listed_after_start_count)} |",
            f"| missing_listing_dates_count | {_fmt_summary_value(audit.missing_listing_dates_count)} |",
            f"| listed_after_start_examples | `{', '.join(audit.listed_after_start_examples) or 'n/a'}` |",
            "",
            "## Local Kline Cache Coverage",
            "",
            "| Interval | Symbols | Expected Bars/Symbol | Complete | Partial | Empty | Min Bars | Avg Bars | Coverage % | Examples |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for interval, item in audit.kline_coverage.items():
        examples = list(item.get("empty_examples", [])) + list(item.get("partial_examples", []))
        lines.append(
            f"| `{interval}` | {item['symbols']} | {item['expected_bars_per_symbol']} | {item['complete_symbols']} | "
            f"{item['partial_symbols']} | {item['empty_symbols']} | {item['min_bars']} | {_fmt_summary_value(float(item['avg_bars']))} | "
            f"{_fmt_summary_value(float(item['coverage_pct']))} | `{', '.join(examples[:8]) or 'n/a'}` |"
        )
    lines.extend(
        [
            "",
            "## Opportunity Alignment Capability",
            "",
            "| Field | Available |",
            "|---|---:|",
        ]
    )
    for key, value in audit.opportunity_alignment_fields.items():
        lines.append(f"| `{key}` | {value} |")
    lines.extend(
        [
            "",
            "## Readiness Checks",
            "",
            "| Check | Status |",
            "|---|---|",
        ]
    )
    for key, value in audit.readiness_checks.items():
        lines.append(f"| `{key}` | `{value}` |")
    lines.extend(["", "## Prior Third-window A/B References", "", "| Path |", "|---|"])
    if audit.prior_third_window_abtests:
        for path in audit.prior_third_window_abtests[:20]:
            lines.append(f"| `{path}` |")
    else:
        lines.append("| n/a |")
    lines.extend(
        [
            "",
            "## N1 Gate",
            "",
            f"`{audit.verdict}`",
            "",
            "## Recommended Next Action",
            "",
        ]
    )
    if audit.verdict == "n0_blocked_cache_incomplete":
        lines.append("Do not run N1 yet. First repair or fetch missing local klines, then rerun this readiness audit.")
    elif audit.verdict == "n0_conditional_pass_with_universe_bias_warning":
        lines.append("N1 may run only as a clearly caveated third-window diagnostic. Do not call it clean confirmatory validation unless listing-date or historical membership evidence is added.")
    elif audit.verdict == "n0_conditional_pass_with_alignment_warning":
        lines.append("N1 may run as the fixed `0.35` system-level retest, but mechanism evidence must be labeled approximate until strict opportunity IDs and capacity-state fields are available.")
    else:
        lines.append("Proceed to N1 fixed `atr_reclaim_0_35` confirmatory retest. Nearby thresholds, if run, must be exploratory only.")
    lines.extend(
        [
            "",
            "## Raw Summary",
            "",
            "```json",
            json.dumps(asdict(audit), ensure_ascii=False, indent=2),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def write_atr_reclaim_n0_readiness_audit_report(
    settings: Settings,
    *,
    experiment_id: str,
    symbol_master_path: Path,
    start: str,
    end: str,
    reports_date: str | None = None,
) -> tuple[AtrReclaimN0ReadinessAudit, list[Path]]:
    date_text = reports_date or _local_now().strftime("%Y-%m-%d")
    audit = build_atr_reclaim_n0_readiness_audit(
        settings,
        experiment_id=experiment_id,
        symbol_master_path=symbol_master_path,
        start=start,
        end=end,
        reports_date=date_text,
    )
    text = render_atr_reclaim_n0_readiness_audit(audit)
    report_dir = settings.output.reports_dir / date_text
    obsidian_dir = None if settings.output.obsidian_dir is None else settings.output.obsidian_dir / "Reports" / date_text
    prefix = f"atr_reclaim_n0_readiness_audit_{date_text}"
    version = next_report_version([report_dir, obsidian_dir], prefix)
    filename = versioned_markdown_filename(prefix, version)
    paths: list[Path] = []
    for directory in [report_dir, obsidian_dir]:
        if directory is None:
            continue
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / filename
        path.write_text(text, encoding="utf-8")
        paths.append(path)
    return audit, paths


def generate_observation_dashboard(
    settings: Settings,
    account_name: str | None = None,
    run_id: str | None = None,
    run_type: str = "manual",
) -> tuple[str, list[Path]]:
    account = account_name or settings.paper.account_name
    trades = load_all_paper_trades(settings, account)
    events_by_trade = load_paper_events(settings, account)
    all_events = [event for events in events_by_trade.values() for event in events]
    reclaim_trades = [
        trade
        for trade in trades
        if any(
            event.event_type in {"RECLAIM_PENDING", "RECLAIM_PENDING_SET"}
            for event in events_by_trade.get(trade.paper_trade_id, [])
        )
    ]
    reclaim_outcomes = Counter(_reclaim_follow_up(trade, events_by_trade.get(trade.paper_trade_id, [])) for trade in reclaim_trades)
    ema_activations = sum(1 for event in all_events if event.event_type == "TP1_EMA_TRAILING_ACTIVATED")
    ema_raises = sum(1 for event in all_events if event.event_type == "TP1_EMA_TRAILING_RAISED")
    ema_stops = sum(
        1
        for event in all_events
        if event.event_type == "EMA_TRAILING_STOPPED"
        or (event.event_type == "STOPPED" and "EMA20 trailing stop" in event.message)
    )
    now = _local_now()
    now_utc = datetime.now(timezone.utc)
    run_health = _run_health_summary(settings, now_utc)
    stale_runs = _stale_running_runs(settings, now_utc)
    holding_42_rows = _holding_42_bar_review(settings)
    open_holding_hours = []
    for trade in trades:
        if trade.status in OPEN_STATUSES and trade.entered_at_utc:
            entered = datetime.fromisoformat(trade.entered_at_utc)
            open_holding_hours.append((trade.symbol, trade.status, (now_utc - entered).total_seconds() / 3600))
    action_counter, risk_off_counter = _scan_action_summary(settings)

    report_dir = settings.output.reports_dir / now.strftime("%Y-%m-%d")
    obsidian_dir = None if settings.output.obsidian_dir is None else settings.output.obsidian_dir / "Reports" / now.strftime("%Y-%m-%d")
    if run_type == "paper_4h_update":
        prefix = f"paper_4h_dashboard_{now.strftime('%H%M')}_{account}"
    else:
        prefix = f"paper_observation_dashboard_{now.strftime('%Y-%m-%d')}_{account}"
    version = next_report_version([report_dir, obsidian_dir], prefix)
    filename = versioned_markdown_filename(prefix, version)
    lines = [
        "---",
        f"created: {now.strftime('%Y-%m-%d %H:%M:%S %Z')}",
        "tags:",
        "  - crypto",
        "  - trading-system",
        "  - paper-observation",
        f"account: {account}",
        f"report_version: v{version}",
        "---",
        "",
        f"# 三周观察仪表 {now.strftime('%Y-%m-%d')} {account} v{version}",
        "",
        f"- Run ID：`{run_id or 'n/a'}`",
        f"- Run type：`{run_type}`",
        "- 数据来源：SQLite",
        "",
        "## 核心指标",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| RECLAIM_PENDING events | {sum(1 for event in all_events if event.event_type in {'RECLAIM_PENDING', 'RECLAIM_PENDING_SET'})} |",
        f"| Reclaim trades | {len(reclaim_trades)} |",
        f"| Reclaim fell below stop / invalidated | {reclaim_outcomes.get('fell_below_stop_or_invalidated', 0)} |",
        f"| Reclaim later entered | {reclaim_outcomes.get('reclaimed_entered', 0)} |",
        f"| Reclaim still waiting | {reclaim_outcomes.get('still_waiting', 0)} |",
        f"| TP1 EMA activations | {ema_activations} |",
        f"| TP1 EMA stop raises | {ema_raises} |",
        f"| TP1 EMA stop exits | {ema_stops} |",
        f"| Open entered/TP1 positions | {len(open_holding_hours)} |",
        f"| Positions over 42 x 4h / 168h | {len(holding_42_rows)} |",
        f"| Stale running runs >2h | {len(stale_runs)} |",
        "",
        "## Run Health / 自动任务健康",
        "",
        "| Metric | Value |",
        "|---|---:|",
        "| Expected 4h runs per full day | 5 |",
        f"| 4h success last 24h | {run_health['counts']['paper_4h_update'].get('success', 0)} |",
        f"| 4h failed last 24h | {run_health['counts']['paper_4h_update'].get('failed', 0)} |",
        f"| 4h running last 24h | {run_health['counts']['paper_4h_update'].get('running', 0)} |",
        f"| daily success last 24h | {run_health['counts']['daily_full'].get('success', 0)} |",
        f"| daily failed last 24h | {run_health['counts']['daily_full'].get('failed', 0)} |",
        "",
        "| Latest Run Type | Run ID | Status | Started | Finished |",
        "|---|---|---|---|---|",
    ]
    for latest_type in ["daily_full", "paper_4h_update"]:
        latest = run_health["latest"].get(latest_type)
        if latest:
            lines.append(
                f"| `{latest_type}` | `{latest['run_id']}` | {latest['status']} | "
                f"{_local_timestamp(str(latest['started_at']))} | "
                f"{_local_timestamp(str(latest['finished_at'])) if latest['finished_at'] else 'n/a'} |"
            )
        else:
            lines.append(f"| `{latest_type}` | n/a | n/a | n/a | n/a |")
    lines.extend([
        "",
        "## Stale Running Run 检测",
        "",
        "| Run ID | Type | Started | Age Hours | Log | Suggested Action |",
        "|---|---|---|---:|---|---|",
    ])
    if stale_runs:
        for row in stale_runs:
            suggested = f"python main.py db mark-run-failed --run-id {row['run_id']} --reason \"stale run inspected manually\""
            lines.append(
                f"| `{row['run_id']}` | `{row['run_type']}` | {_local_timestamp(row['started_at'])} | "
                f"{row['age_hours']:.1f} | `{row['log_path'] or 'n/a'}` | `{suggested}` |"
            )
    else:
        lines.append("| n/a | n/a | n/a | 0.0 | n/a | n/a |")
    lines.extend([
        "",
        "## 42-bar Holding Review",
        "",
        "| Symbol | Plan | Status | First observed >=168h | Price@first | PnL@first | Latest Price | Latest PnL | Max/Min Price After | Max/Min PnL After | Outcome |",
        "|---|---|---|---|---:|---:|---:|---:|---:|---:|---|",
    ])
    if holding_42_rows:
        for row in holding_42_rows:
            lines.append(
                f"| `{row['symbol']}` | `{row['plan_id']}` | {row['status']} | "
                f"{_local_timestamp(row['threshold_time'])} ({row['hours_at_threshold']:.1f}h) | "
                f"{_fmt_optional(row['price_at_threshold'], 6)} | {_fmt_optional(row['pnl_at_threshold'], 2)} | "
                f"{_fmt_optional(row['latest_price'], 6)} | {_fmt_optional(row['latest_pnl'], 2)} | "
                f"{_fmt_optional(row['max_price_after'], 6)} / {_fmt_optional(row['min_price_after'], 6)} | "
                f"{_fmt_optional(row['max_pnl_after'], 2)} / {_fmt_optional(row['min_pnl_after'], 2)} | "
                f"{row['outcome_after']} |"
            )
    else:
        lines.append("| n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |")
    lines.extend([
        "",
        "## 开放持仓时长",
        "",
        "| Symbol | Status | Holding Hours |",
        "|---|---|---:|",
    ])
    if open_holding_hours:
        for symbol, status, hours in sorted(open_holding_hours, key=lambda item: item[2], reverse=True):
            lines.append(f"| `{symbol}` | {status} | {hours:.1f} |")
    else:
        lines.append("| n/a | n/a | 0.0 |")
    lines.extend([
        "",
        "## 今日扫描 Action 与 RISK_OFF",
        "",
        "| Scope | BUY_CANDIDATE | WAIT_PULLBACK | WATCH_ONLY | REJECT | Other |",
        "|---|---:|---:|---:|---:|---:|",
    ])
    for label, counter in [("All candidates", action_counter), ("RISK_OFF-tagged", risk_off_counter)]:
        known = sum(counter.get(action, 0) for action in ["BUY_CANDIDATE", "WAIT_PULLBACK", "WATCH_ONLY", "REJECT"])
        lines.append(
            f"| {label} | {counter.get('BUY_CANDIDATE', 0)} | {counter.get('WAIT_PULLBACK', 0)} | "
            f"{counter.get('WATCH_ONLY', 0)} | {counter.get('REJECT', 0)} | {sum(counter.values()) - known} |"
        )
    lines.extend([
        "",
        "## RECLAIM_PENDING 明细",
        "",
        "| Symbol | Status | Stop | Last Price | Outcome | Last Pending |",
        "|---|---|---:|---:|---|---|",
    ])
    if reclaim_trades:
        for trade in reclaim_trades:
            events = events_by_trade.get(trade.paper_trade_id, [])
            pending = [
                event
                for event in events
                if event.event_type in {"RECLAIM_PENDING", "RECLAIM_PENDING_SET"}
            ]
            lines.append(
                f"| `{trade.symbol}` | {trade.status} | {trade.stop_loss:.8g} | "
                f"{'n/a' if trade.last_price is None else f'{trade.last_price:.8g}'} | "
                f"{_reclaim_follow_up(trade, events)} | {_local_timestamp(pending[-1].event_time_utc)} |"
            )
    else:
        lines.append("| n/a | n/a | n/a | n/a | no_reclaim_pending | n/a |")
    text = "\n".join(lines) + "\n"

    paths: list[Path] = []
    for directory in [report_dir, obsidian_dir]:
        if directory is None:
            continue
        directory.mkdir(parents=True, exist_ok=True)
        out = directory / filename
        out.write_text(text, encoding="utf-8")
        paths.append(out)
    return text, paths
