from __future__ import annotations

from dataclasses import asdict
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import sqlite3
import subprocess
from typing import Callable

from ..config import Settings
from ..report_versions import next_report_version, versioned_markdown_filename
from ..storage import init_db
from .history import fetch_klines_cached
from .metrics import BacktestMetrics, calculate_metrics
from .replay import BacktestResult, run_backtest_replay


def _local_date(timestamp_utc: str) -> str:
    dt = datetime.fromisoformat(timestamp_utc)
    return dt.astimezone(timezone(timedelta(hours=8), name="CST")).strftime("%Y-%m-%d")


def _local_timestamp(timestamp_utc: str) -> str:
    dt = datetime.fromisoformat(timestamp_utc)
    return dt.astimezone(timezone(timedelta(hours=8), name="CST")).strftime("%Y-%m-%d %H:%M:%S %Z")


def _project_report_dir(settings: Settings, timestamp_utc: str) -> Path:
    return settings.output.reports_dir / _local_date(timestamp_utc)


def _obsidian_report_dir(settings: Settings, timestamp_utc: str) -> Path | None:
    if settings.output.obsidian_dir is None:
        return None
    return settings.output.obsidian_dir / "Reports" / _local_date(timestamp_utc)


def _fmt(value: float | None, suffix: str = "") -> str:
    if value is None:
        return "n/a"
    if value == float("inf"):
        return "inf"
    return f"{value:,.2f}{suffix}"


def _commit_hash() -> str:
    try:
        completed = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
        return completed.stdout.strip()
    except Exception:
        return "UNKNOWN"


def _date_ms(value: str) -> int:
    raw = f"{value}T00:00:00+00:00" if len(value) == 10 else value
    return int(datetime.fromisoformat(raw).timestamp() * 1000)


def _benchmark_return(
    settings: Settings,
    symbol: str,
    start: str,
    end: str,
    *,
    progress: Callable[[str], None] | None = None,
) -> float | None:
    start_ms = _date_ms(start)
    end_ms = _date_ms(end)
    try:
        fetched = fetch_klines_cached(
            settings,
            symbol,
            "4h",
            start_ms,
            end_ms,
            allow_data_gaps=True,
            progress=progress,
        )
    except Exception:
        return None
    klines = fetched.klines
    if len(klines) < 2:
        return None
    first = float(klines[0][4])
    last = float(klines[-1][4])
    fee = settings.backtest.taker_fee_bps / 10_000
    return ((last / first) * (1 - fee) - 1) * 100 if first > 0 else None


def _benchmarks(
    settings: Settings,
    result: BacktestResult,
    start: str,
    end: str,
    progress: Callable[[str], None] | None = None,
) -> dict[str, float | None]:
    values: dict[str, float | None] = {
        "BTC buy-hold": _benchmark_return(settings, "BTCUSDT", start, end, progress=progress),
        "ETH buy-hold": _benchmark_return(settings, "ETHUSDT", start, end, progress=progress),
        "Cash": 0.0,
    }
    symbol_returns = [
        item
        for item in (
            _benchmark_return(settings, symbol, start, end, progress=progress)
            for symbol in result.symbols
        )
        if item is not None
    ]
    values["Equal-weight symbols"] = sum(symbol_returns) / len(symbol_returns) if symbol_returns else None
    return values


def _render_report(
    result: BacktestResult,
    metrics: BacktestMetrics,
    benchmarks: dict[str, float | None],
    report_version: str,
) -> str:
    closed = [trade for trade in result.trades if trade.status in {"STOPPED", "CLOSED"}]
    open_trades = [trade for trade in result.trades if trade.status in {"ENTERED", "TP1_HIT"}]
    inactive = [trade for trade in result.trades if trade.status not in {"STOPPED", "CLOSED", "ENTERED", "TP1_HIT"}]
    commit_hash = _commit_hash()
    lines = [
        "---",
        f"created: {_local_timestamp(result.created_at_utc)}",
        "tags:",
        "  - crypto",
        "  - trading-system",
        "  - backtest",
        f"backtest_run_id: {result.run_id}",
        f"report_version: {report_version}",
        "---",
        "",
        f"# 回测报告 {result.start_utc[:10]} 至 {result.end_utc[:10]} {report_version}",
        "",
        f"- 回测 ID：`{result.run_id}`",
        f"- 交易对：{', '.join(f'`{symbol}`' for symbol in result.symbols)}",
        f"- UTC 区间：{result.start_utc} -> {result.end_utc}",
        f"- 初始权益：{result.initial_equity:,.2f} USDT",
        f"- 最终权益：{result.final_equity:,.2f} USDT",
        f"- 净收益：{_fmt(metrics.net_return_pct, '%')}",
        f"- 代码 commit：`{commit_hash}`",
        f"- 样本提示：{metrics.sample_warning or '样本数量未触发警告。'}",
        "",
        "## 回测假设",
        "",
        "- 决策在 4h bar 收盘后做，新 WATCHING 条件计划最早从下一根 bar 成交。",
        "- WATCHING 是条件计划，不是真实提交交易所的限价单；不预留现金，成交时检查现金、名义仓位和活跃风险。",
        "- intrabar 默认 stop_first；同 bar 同时触发止损和止盈时按止损优先。",
        "- 入场成交价取 entry_high + 滑点；TP1 是 TP1 touched，不减仓，不代表已兑现利润。",
        "- 使用固定 stop/TP，不实现动态支撑退出；4h K 线裁决成交，未使用 5m/15m 还原真实路径。",
        "- 24h ticker 字段由 1h K 线重建，与实时 Binance /ticker/24hr 存在粒度差异。",
        "- 未处理 tick size、step size、min notional、历史费率变化、BNB 折扣和 VIP 费率。",
        "- 只覆盖用户指定且可获取历史数据的 symbols，不代表完整历史市场 universe。",
        "",
        "## 核心指标",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| Trades | {metrics.trades} |",
        f"| Closed trades | {metrics.closed_trades} |",
        f"| Open trades | {metrics.open_trades} |",
        f"| Win rate | {_fmt(metrics.win_rate, '%')} |",
        f"| Profit factor | {_fmt(metrics.profit_factor)} |",
        f"| Avg R | {_fmt(metrics.avg_r)} |",
        f"| Net return | {_fmt(metrics.net_return_pct, '%')} |",
        f"| Max drawdown | {metrics.max_drawdown:,.2f} / {metrics.max_drawdown_pct:.2f}% |",
        f"| Intrabar max drawdown | {metrics.intrabar_max_drawdown:,.2f} / {metrics.intrabar_max_drawdown_pct:.2f}% |",
        f"| TP1 touched rate | {_fmt(metrics.tp1_rate, '%')} |",
        f"| TP2 close rate | {_fmt(metrics.tp2_rate, '%')} |",
        f"| Stop rate | {_fmt(metrics.stop_rate, '%')} |",
        f"| Fee drag | {metrics.fee_drag:,.2f} USDT |",
        f"| Tail max single loss | {metrics.tail_max_loss:,.2f} USDT |",
        f"| CAGR | {_fmt(metrics.cagr, '%')} |",
        f"| Sharpe | {_fmt(metrics.sharpe)} |",
        f"| Sortino | {_fmt(metrics.sortino)} |",
        f"| Exposure | {_fmt(metrics.exposure_pct, '%')} |",
        f"| Turnover | {_fmt(metrics.turnover)} |",
        "",
        "## Benchmark",
        "",
        "| Benchmark | Return |",
        "|---|---:|",
    ]
    for name, value in benchmarks.items():
        lines.append(f"| {name} | {_fmt(value, '%')} |")

    lines.extend(
        [
            "",
            "## 已结束交易",
            "",
            "| Symbol | Status | Created | Entry | Exit | Qty | Gross PnL | Net PnL | Net R | Fees | Notes |",
            "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for trade in closed:
        lines.append(
            "| "
            f"`{trade.symbol}` | {trade.status} | {trade.created_at_utc} | "
            f"{_fmt(trade.entry_price_filled)} | {_fmt(trade.exit_price_filled)} | {_fmt(trade.quantity)} | "
            f"{trade.gross_pnl:,.2f} | {trade.net_pnl:,.2f} | {_fmt(trade.r_multiple_net)} | "
            f"{trade.entry_fee + trade.exit_fee:,.2f} | {trade.notes} |"
        )

    lines.extend(
        [
            "",
            "## 回测结束仍开放",
            "",
            "| Symbol | Status | Entry | Qty | Unrealized Handling | Notes |",
            "|---|---|---:|---:|---|---|",
        ]
    )
    for trade in open_trades:
        lines.append(
            "| "
            f"`{trade.symbol}` | {trade.status} | {_fmt(trade.entry_price_filled)} | {_fmt(trade.quantity)} | "
            "按最后 close 计入净值，不计入胜率/profit_factor/avg_R | "
            f"{trade.notes} |"
        )

    lines.extend(
        [
            "",
            "## 未入场/过期计划",
            "",
            "| Symbol | Status | Created | Entry Zone | Score | Notes |",
            "|---|---|---|---:|---:|---|",
        ]
    )
    if not inactive:
        lines.append("| n/a | n/a | n/a | n/a | n/a | No inactive plans. |")
    for trade in inactive:
        lines.append(
            "| "
            f"`{trade.symbol}` | {trade.status} | {trade.created_at_utc} | "
            f"{_fmt(trade.entry_low)} - {_fmt(trade.entry_high)} | {trade.score:.2f} | {trade.notes} |"
        )

    lines.extend(
        [
            "",
            "## 数据质量摘要",
            "",
            "| Severity | Symbol | Interval | Message |",
            "|---|---|---|---|",
        ]
    )
    if not result.data_issues:
        lines.append("| OK | n/a | n/a | No issues recorded. |")
    for issue in result.data_issues[:80]:
        lines.append(f"| {issue.severity} | `{issue.symbol}` | {issue.interval} | {issue.message} |")
    if len(result.data_issues) > 80:
        lines.append(f"| INFO | n/a | n/a | Additional issues omitted: {len(result.data_issues) - 80}. |")

    lines.extend(
        [
            "",
            "## 原始配置快照",
            "",
            "```json",
            json.dumps(result.config_snapshot, ensure_ascii=False, indent=2),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def _write_report(
    settings: Settings,
    result: BacktestResult,
    metrics: BacktestMetrics,
    benchmarks: dict[str, float | None],
    include_obsidian: bool,
) -> list[Path]:
    project_dir = _project_report_dir(settings, result.created_at_utc)
    obsidian_dir = _obsidian_report_dir(settings, result.created_at_utc)
    target_dirs = [project_dir]
    if include_obsidian and obsidian_dir is not None:
        target_dirs.append(obsidian_dir)
    prefix = f"backtest_{result.start_utc[:10]}_{result.end_utc[:10]}"
    version_number = next_report_version(target_dirs, prefix)
    version = f"v{version_number}"
    filename = versioned_markdown_filename(prefix, version_number)
    markdown = _render_report(result, metrics, benchmarks, version)
    paths: list[Path] = []
    for directory in target_dirs:
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / filename
        path.write_text(markdown, encoding="utf-8")
        paths.append(path)
    return paths


def _save_backtest_result(
    settings: Settings,
    result: BacktestResult,
    metrics: BacktestMetrics,
    report_paths: list[Path],
) -> None:
    init_db(settings.output.database_path)
    commit_hash = _commit_hash()
    with sqlite3.connect(settings.output.database_path) as connection:
        connection.execute(
            """
            INSERT OR REPLACE INTO backtest_runs (
                run_id, created_at_utc, symbols_json, start_utc, end_utc,
                config_json, commit_hash, metrics_json, report_path, payload_json
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                result.run_id,
                result.created_at_utc,
                json.dumps(result.symbols, ensure_ascii=False),
                result.start_utc,
                result.end_utc,
                json.dumps(result.config_snapshot, ensure_ascii=False),
                commit_hash,
                json.dumps(asdict(metrics), ensure_ascii=False),
                str(report_paths[0]) if report_paths else None,
                json.dumps(asdict(result), ensure_ascii=False),
            ),
        )
        connection.execute("DELETE FROM backtest_trades WHERE run_id = ?", (result.run_id,))
        for trade in result.trades:
            connection.execute(
                """
                INSERT INTO backtest_trades (
                    run_id, trade_id, symbol, status, created_at_utc, entered_at_utc,
                    closed_at_utc, entry_price_raw, entry_price_filled,
                    exit_price_raw, exit_price_filled, entry_fee, exit_fee,
                    slippage_cost, gross_pnl, net_pnl, r_multiple_net, payload_json
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    result.run_id,
                    trade.trade_id,
                    trade.symbol,
                    trade.status,
                    trade.created_at_utc,
                    trade.entered_at_utc,
                    trade.closed_at_utc,
                    trade.entry_price_raw,
                    trade.entry_price_filled,
                    trade.exit_price_raw,
                    trade.exit_price_filled,
                    trade.entry_fee,
                    trade.exit_fee,
                    trade.slippage_cost,
                    trade.gross_pnl,
                    trade.net_pnl,
                    trade.r_multiple_net,
                    json.dumps(asdict(trade), ensure_ascii=False),
                ),
            )
        connection.execute("DELETE FROM backtest_metrics WHERE run_id = ?", (result.run_id,))
        for key, value in asdict(metrics).items():
            metric_value = float(value) if isinstance(value, (int, float)) and value not in {float("inf"), -float("inf")} else None
            connection.execute(
                """
                INSERT INTO backtest_metrics (run_id, metric_name, metric_value, metric_text)
                VALUES (?, ?, ?, ?)
                """,
                (result.run_id, key, metric_value, None if metric_value is not None else str(value)),
            )


def run_backtest(
    settings: Settings,
    symbols: list[str],
    start: str,
    end: str,
    *,
    interval: str | None = None,
    intrabar: str | None = None,
    allow_data_gaps: bool = False,
    include_obsidian: bool = True,
    progress: Callable[[str], None] | None = None,
) -> tuple[BacktestResult, BacktestMetrics, list[Path]]:
    result = run_backtest_replay(
        settings,
        symbols,
        start,
        end,
        interval=interval,
        intrabar=intrabar,
        allow_data_gaps=allow_data_gaps,
        progress=progress,
    )
    metrics = calculate_metrics(result)
    benchmarks = _benchmarks(settings, result, start, end, progress=progress)
    report_paths = _write_report(settings, result, metrics, benchmarks, include_obsidian)
    _save_backtest_result(settings, result, metrics, report_paths)
    return result, metrics, report_paths
