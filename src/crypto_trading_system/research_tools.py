from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import sqlite3

from .backtest.universe import SymbolMaster, load_symbol_master, save_symbol_master
from .config import Settings
from .database import connect_db
from .paper_trader import CLOSED_STATUSES, OPEN_STATUSES, load_all_paper_trades, load_paper_events
from .report_versions import next_report_version, versioned_markdown_filename


LARGE_CAP_SYMBOLS = ("BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT")


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
