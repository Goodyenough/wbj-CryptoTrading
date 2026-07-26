from __future__ import annotations

from collections import Counter
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
import inspect
import json
from pathlib import Path
import sqlite3

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


def build_blocked_entry_event_export(
    settings: Settings,
    run_id: str,
    *,
    report_date: str | None = None,
    progress=None,
) -> BlockedEntryEventExport:
    from .backtest.replay import run_backtest_replay

    run = _source_run_row(settings, run_id)
    config = json.loads(run["config_json"] or "{}")
    symbols = [str(symbol).replace("/", "").upper() for symbol in json.loads(run["symbols_json"] or "[]")]
    if not symbols:
        raise ValueError(f"backtest run_id has no stored symbols: {run_id}")
    replay_settings = _apply_backtest_config_snapshot(settings, config)
    dynamic_mode = bool(config.get("dynamic_universe_mode"))
    dynamic_summary = config.get("dynamic_universe_summary", {})
    if not isinstance(dynamic_summary, dict):
        dynamic_summary = {}
    max_symbols = _as_int(dynamic_summary.get("max_symbols"))
    dynamic_master = _stored_symbol_master(run_id, str(run["created_at_utc"]), symbols) if dynamic_mode else None

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
