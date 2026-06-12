from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import sqlite3

from .backtest.universe import SymbolMaster, load_symbol_master, save_symbol_master
from .config import Settings
from .paper_trader import CLOSED_STATUSES, OPEN_STATUSES, load_all_paper_trades, load_paper_events
from .report_versions import next_report_version, versioned_markdown_filename


LARGE_CAP_SYMBOLS = ("BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT")


def _local_now() -> datetime:
    return datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=8), name="CST"))


def _local_date(timestamp_utc: str) -> str:
    return datetime.fromisoformat(timestamp_utc).astimezone(timezone(timedelta(hours=8), name="CST")).strftime("%Y-%m-%d")


def _local_timestamp(timestamp_utc: str) -> str:
    return datetime.fromisoformat(timestamp_utc).astimezone(timezone(timedelta(hours=8), name="CST")).strftime("%Y-%m-%d %H:%M:%S %Z")


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
class ExperimentIndexRow:
    path: Path
    report_type: str
    experiment_id: str
    start: str
    end: str
    verdict: str
    sample_sufficient: str
    next_action: str


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


def _infer_period(path: Path) -> tuple[str, str]:
    parts = path.stem.split("_")
    dates = [part for part in parts if len(part) == 10 and part[4] == "-" and part[7] == "-"]
    if len(dates) >= 2:
        return dates[-2], dates[-1]
    return "n/a", "n/a"


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


def build_experiment_index(settings: Settings, reports_dir: Path | None = None) -> tuple[str, list[Path]]:
    root = reports_dir or settings.output.reports_dir
    rows: list[ExperimentIndexRow] = []
    for path in sorted(root.glob("**/*.md")):
        if not (path.name.startswith("abtest_") or path.name.startswith("abtest_summary_")):
            continue
        text = path.read_text(encoding="utf-8")
        fm = _frontmatter(text)
        experiment_id = fm.get("experiment_id", "unknown")
        verdict = fm.get("verdict", "unknown")
        sample = fm.get("sample_sufficient", "unknown")
        start, end = _infer_period(path)
        rows.append(
            ExperimentIndexRow(
                path=path,
                report_type="summary" if path.name.startswith("abtest_summary_") else "abtest",
                experiment_id=experiment_id,
                start=start,
                end=end,
                verdict=verdict,
                sample_sufficient=sample,
                next_action=_next_action(verdict, sample),
            )
        )

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
        "| Experiment | Type | Period | Verdict | Sample | Next Action | Report |",
        "|---|---|---|---|---|---|---|",
    ]
    for row in rows:
        rel = row.path.relative_to(settings.output.reports_dir) if row.path.is_relative_to(settings.output.reports_dir) else row.path
        lines.append(
            f"| `{row.experiment_id}` | {row.report_type} | {row.start} -> {row.end} | "
            f"{row.verdict} | {row.sample_sufficient} | {row.next_action} | `{rel}` |"
        )
    if not rows:
        lines.append("| n/a | n/a | n/a | no_data | n/a | 先运行 A/B 实验 | n/a |")
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
    pending = [event for event in events if event.event_type == "RECLAIM_PENDING"]
    if not pending:
        return "n/a"
    first_time = _event_time(pending[0])
    later = [event for event in events if _event_time(event) > first_time]
    if any(event.event_type == "ENTERED" for event in later):
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
    with sqlite3.connect(settings.output.database_path) as connection:
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


def generate_observation_dashboard(settings: Settings, account_name: str | None = None) -> tuple[str, list[Path]]:
    account = account_name or settings.paper.account_name
    trades = load_all_paper_trades(settings, account)
    events_by_trade = load_paper_events(settings, account)
    all_events = [event for events in events_by_trade.values() for event in events]
    reclaim_trades = [trade for trade in trades if any(e.event_type == "RECLAIM_PENDING" for e in events_by_trade.get(trade.paper_trade_id, []))]
    reclaim_outcomes = Counter(_reclaim_follow_up(trade, events_by_trade.get(trade.paper_trade_id, [])) for trade in reclaim_trades)
    ema_activations = sum(1 for event in all_events if event.event_type == "TP1_EMA_TRAILING_ACTIVATED")
    ema_raises = sum(1 for event in all_events if event.event_type == "TP1_EMA_TRAILING_RAISED")
    ema_stops = sum(1 for event in all_events if event.event_type == "STOPPED" and "EMA20 trailing stop" in event.message)
    now = _local_now()
    now_utc = datetime.now(timezone.utc)
    open_holding_hours = []
    for trade in trades:
        if trade.status in OPEN_STATUSES and trade.entered_at_utc:
            entered = datetime.fromisoformat(trade.entered_at_utc)
            open_holding_hours.append((trade.symbol, trade.status, (now_utc - entered).total_seconds() / 3600))
    action_counter, risk_off_counter = _scan_action_summary(settings)

    report_dir = settings.output.reports_dir / now.strftime("%Y-%m-%d")
    obsidian_dir = None if settings.output.obsidian_dir is None else settings.output.obsidian_dir / "Reports" / now.strftime("%Y-%m-%d")
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
        "## 核心指标",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| RECLAIM_PENDING events | {sum(1 for event in all_events if event.event_type == 'RECLAIM_PENDING')} |",
        f"| Reclaim trades | {len(reclaim_trades)} |",
        f"| Reclaim fell below stop / invalidated | {reclaim_outcomes.get('fell_below_stop_or_invalidated', 0)} |",
        f"| Reclaim later entered | {reclaim_outcomes.get('reclaimed_entered', 0)} |",
        f"| Reclaim still waiting | {reclaim_outcomes.get('still_waiting', 0)} |",
        f"| TP1 EMA activations | {ema_activations} |",
        f"| TP1 EMA stop raises | {ema_raises} |",
        f"| TP1 EMA stop exits | {ema_stops} |",
        f"| Open entered/TP1 positions | {len(open_holding_hours)} |",
        "",
        "## 开放持仓时长",
        "",
        "| Symbol | Status | Holding Hours |",
        "|---|---|---:|",
    ]
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
            pending = [event for event in events if event.event_type == "RECLAIM_PENDING"]
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
