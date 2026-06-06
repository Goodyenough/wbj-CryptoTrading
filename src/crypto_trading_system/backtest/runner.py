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


METRIC_LABELS = {
    "Trades": "Trades（计划总数）",
    "Closed trades": "Closed trades（已结束交易）",
    "Open trades": "Open trades（仍开放持仓）",
    "Win rate": "Win rate（胜率）",
    "Profit factor": "Profit factor（盈利因子）",
    "Avg R": "Avg R（平均R倍数）",
    "Net return": "Net return（净收益率）",
    "Max drawdown": "Max drawdown（最大回撤）",
    "Intrabar max drawdown": "Intrabar max drawdown（K线内最大回撤）",
    "TP1 touched rate": "TP1 touched rate（第一止盈触达率）",
    "TP2 close rate": "TP2 close rate（第二止盈平仓率）",
    "Stop rate": "Stop rate（止损率）",
    "Fee drag": "Fee drag（手续费拖累）",
    "Tail max single loss": "Tail max single loss（最大单笔亏损）",
    "CAGR": "CAGR（年化复合收益率）",
    "Sharpe": "Sharpe（夏普比率）",
    "Sortino": "Sortino（索提诺比率）",
    "Exposure": "Exposure（持仓暴露时间）",
    "Turnover": "Turnover（换手率）",
    "Sample sufficient": "Sample sufficient（样本是否充分）",
}


BENCHMARK_LABELS = {
    "BTC buy-hold": "BTC buy-hold（买入并持有BTC）",
    "ETH buy-hold": "ETH buy-hold（买入并持有ETH）",
    "Cash": "Cash（现金不交易）",
    "Equal-weight symbols": "Equal-weight symbols（等权持有本次币种）",
}


STATUS_LABELS = {
    "WATCHING": "WATCHING（观察中/等待入场）",
    "ENTERED": "ENTERED（已入场）",
    "TP1_HIT": "TP1_HIT（第一止盈已触达）",
    "STOPPED": "STOPPED（已止损）",
    "CLOSED": "CLOSED（已按TP2平仓）",
    "INVALIDATED": "INVALIDATED（未入场前失效）",
    "EXPIRED": "EXPIRED（观察计划过期）",
    "EXPIRED_END": "EXPIRED_END（回测结束仍未入场）",
}


TABLE_LABELS = {
    "Metric": "Metric（指标）",
    "Value": "Value（数值）",
    "Benchmark": "Benchmark（基准）",
    "Return": "Return（收益率）",
    "Symbol": "Symbol（交易对）",
    "Status": "Status（状态）",
    "Created": "Created（创建时间）",
    "Entry": "Entry（入场价）",
    "Exit": "Exit（出场价）",
    "Qty": "Qty（数量）",
    "Gross PnL": "Gross PnL（毛盈亏）",
    "Net PnL": "Net PnL（净盈亏）",
    "Net R": "Net R（净R倍数）",
    "Fees": "Fees（手续费）",
    "Notes": "Notes（备注）",
    "Unrealized Handling": "Unrealized Handling（未实现盈亏处理）",
    "Entry Zone": "Entry Zone（入场区间）",
    "Score": "Score（评分）",
    "Severity": "Severity（严重程度）",
    "Interval": "Interval（周期）",
    "Message": "Message（说明）",
}


def _metric_label(name: str) -> str:
    return METRIC_LABELS.get(name, name)


def _benchmark_label(name: str) -> str:
    return BENCHMARK_LABELS.get(name, name)


def _status_label(status: str) -> str:
    return STATUS_LABELS.get(status, status)


def _header(*names: str) -> str:
    return "| " + " | ".join(TABLE_LABELS.get(name, name) for name in names) + " |"


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
        f"sample_sufficient: {str(metrics.sample_sufficient).lower()}",
        f"universe_mode: {str(result.universe_mode).lower()}",
        f"universe_type: {result.universe_type}",
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
        f"- 样本是否充分：{str(metrics.sample_sufficient).lower()}",
        f"- 样本提示：{metrics.sample_warning or '样本数量未触发警告。'}",
        f"- Universe mode：{result.universe_type}",
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
        "- 只覆盖本次手动输入、快照选中或动态 universe 选中且可获取历史数据的 symbols，不代表完整历史市场 universe。",
        "",
        *(
            [
                "## Universe Snapshot / 当前市场快照选币",
                "",
                f"- Source / 来源：{result.universe_snapshot.get('source', 'n/a')}",
                f"- Snapshot time UTC / 快照时间：{result.universe_snapshot.get('snapshot_at_utc', 'n/a')}",
                f"- Filters / 筛选条件：{result.universe_snapshot.get('filters', 'n/a')}",
                (
                    "- Selected count / 入选数量："
                    f"{result.universe_snapshot.get('selected_count', len(result.universe_snapshot.get('selected_symbols', [])))}"
                ),
                f"- Replay count / 实际回放数量：{result.universe_snapshot.get('replay_count', len(result.symbols))}",
                f"- Candidate count after initial filters / 初筛候选数：{result.universe_snapshot.get('candidate_count', 'n/a')}",
                (
                    "- Selected symbols / 入选币种："
                    f"{', '.join(f'`{symbol}`' for symbol in result.universe_snapshot.get('selected_symbols', []))}"
                ),
                (
                    "- Skipped symbols without period history / 因回测区间无历史 K 线跳过："
                    f"{', '.join(f'`{symbol}`' for symbol in result.universe_snapshot.get('skipped_symbols_no_history', [])) or 'none'}"
                ),
                "",
                (
                    "> Warning / 警告：这是 universe snapshot 回测。它用当前 Binance 市场快照先选币，"
                    "再回放历史 K 线，所以不是完整的历史动态 universe 回测，仍可能存在幸存者偏差。"
                ),
                (
                    "> Limitation / 限制：当前快照只能验证“今天这个候选池”在历史中的表现，"
                    "不能完全验证历史上每一天真实会被选入的币。"
                ),
                "",
            ]
            if result.universe_mode and result.universe_snapshot
            else []
        ),
        *(
            [
                "## Dynamic Universe / 历史动态 Universe",
                "",
                f"- Source / 来源：{result.dynamic_universe_summary.get('source', 'n/a')}",
                f"- Master symbols / Master 币种数：{result.dynamic_universe_summary.get('master_count', 'n/a')}",
                f"- Source limit / 调试截断：{result.dynamic_universe_summary.get('source_limit', 'none')}",
                (
                    "- Source limit applied / 是否截断："
                    f"{str(result.dynamic_universe_summary.get('source_limit_applied', False)).lower()}"
                ),
                f"- Refresh frequency / 刷新频率：{result.dynamic_universe_summary.get('refresh_frequency', 'n/a')}",
                f"- Universe refreshes / Universe 刷新次数：{result.dynamic_universe_summary.get('universe_refresh_count', 0)}",
                (
                    "- Selected symbols per refresh / 每次入选数量："
                    f"min={result.dynamic_universe_summary.get('selected_count_min', 0)}, "
                    f"avg={result.dynamic_universe_summary.get('selected_count_avg', 0):.2f}, "
                    f"max={result.dynamic_universe_summary.get('selected_count_max', 0)}"
                ),
                (
                    "- Top selected symbols / 最常入选："
                    + (
                        ", ".join(
                            f"`{item['symbol']}`({item['days_selected']})"
                            for item in result.dynamic_universe_summary.get("top_selected_symbols", [])[:10]
                        )
                        or "none"
                    )
                ),
                "- Filter counts / 过滤统计：",
                "```json",
                json.dumps(result.dynamic_universe_summary.get("filter_counts", {}), ensure_ascii=False, indent=2),
                "```",
                (
                    "> Warning / 警告：dynamic universe 的 symbol master 来自当前 Binance exchangeInfo；"
                    "历史上曾交易但今天已退市的币不会进入 master list，因此仍有退市幸存者偏差。"
                ),
                (
                    "> Runtime / 耗时提示：第一次完整运行需要缓存大量 1h/4h/1d K 线，可能很慢；"
                    "缓存命中后后续回测会明显加快。"
                ),
                "",
            ]
            if result.universe_type == "dynamic" and result.dynamic_universe_summary
            else []
        ),
        "## 核心指标",
        "",
        _header("Metric", "Value"),
        "|---|---:|",
        f"| {_metric_label('Trades')} | {metrics.trades} |",
        f"| {_metric_label('Closed trades')} | {metrics.closed_trades} |",
        f"| {_metric_label('Open trades')} | {metrics.open_trades} |",
        f"| {_metric_label('Win rate')} | {_fmt(metrics.win_rate, '%')} |",
        f"| {_metric_label('Profit factor')} | {_fmt(metrics.profit_factor)} |",
        f"| {_metric_label('Avg R')} | {_fmt(metrics.avg_r)} |",
        f"| {_metric_label('Net return')} | {_fmt(metrics.net_return_pct, '%')} |",
        f"| {_metric_label('Max drawdown')} | {metrics.max_drawdown:,.2f} / {metrics.max_drawdown_pct:.2f}% |",
        f"| {_metric_label('Intrabar max drawdown')} | {metrics.intrabar_max_drawdown:,.2f} / {metrics.intrabar_max_drawdown_pct:.2f}% |",
        f"| {_metric_label('TP1 touched rate')} | {_fmt(metrics.tp1_rate, '%')} |",
        f"| {_metric_label('TP2 close rate')} | {_fmt(metrics.tp2_rate, '%')} |",
        f"| {_metric_label('Stop rate')} | {_fmt(metrics.stop_rate, '%')} |",
        f"| {_metric_label('Fee drag')} | {metrics.fee_drag:,.2f} USDT |",
        f"| {_metric_label('Tail max single loss')} | {metrics.tail_max_loss:,.2f} USDT |",
        f"| {_metric_label('CAGR')} | {_fmt(metrics.cagr, '%')} |",
        f"| {_metric_label('Sharpe')} | {_fmt(metrics.sharpe)} |",
        f"| {_metric_label('Sortino')} | {_fmt(metrics.sortino)} |",
        f"| {_metric_label('Exposure')} | {_fmt(metrics.exposure_pct, '%')} |",
        f"| {_metric_label('Turnover')} | {_fmt(metrics.turnover)} |",
        f"| {_metric_label('Sample sufficient')} | {str(metrics.sample_sufficient).lower()} |",
        "",
        "## 术语速查",
        "",
        "- PnL（Profit and Loss，盈亏）：交易赚了或亏了多少钱。",
        "- Gross PnL（毛盈亏）：未扣手续费和滑点前的盈亏。",
        "- Net PnL（净盈亏）：扣除手续费和滑点后的真实模拟盈亏。",
        "- R / Net R（风险倍数）：以单笔预设亏损风险为单位衡量结果，-1R 约等于亏掉一笔计划风险。",
        "- Drawdown（回撤）：账户从阶段高点跌到低点的幅度，用来衡量过程中的最大压力。",
        "- Profit factor（盈利因子）：总盈利除以总亏损，大于 1 才说明已闭合交易整体赚钱。",
        "- Sharpe（夏普比率）：单位波动获得的收益，样本少时容易失真。",
        "- Sortino（索提诺比率）：只惩罚下行波动的风险收益指标，样本少时也要谨慎看。",
        "- Exposure（持仓暴露时间）：回测期间有仓位在市场里的时间比例。",
        "- Turnover（换手率）：交易名义金额相对初始资金的规模。",
        "",
        "## Benchmark",
        "",
        _header("Benchmark", "Return"),
        "|---|---:|",
    ]
    for name, value in benchmarks.items():
        lines.append(f"| {_benchmark_label(name)} | {_fmt(value, '%')} |")

    lines.extend(
        [
            "",
            "## 已结束交易",
            "",
            _header("Symbol", "Status", "Created", "Entry", "Exit", "Qty", "Gross PnL", "Net PnL", "Net R", "Fees", "Notes"),
            "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for trade in closed:
        lines.append(
            "| "
            f"`{trade.symbol}` | {_status_label(trade.status)} | {trade.created_at_utc} | "
            f"{_fmt(trade.entry_price_filled)} | {_fmt(trade.exit_price_filled)} | {_fmt(trade.quantity)} | "
            f"{trade.gross_pnl:,.2f} | {trade.net_pnl:,.2f} | {_fmt(trade.r_multiple_net)} | "
            f"{trade.entry_fee + trade.exit_fee:,.2f} | {trade.notes} |"
        )

    lines.extend(
        [
            "",
            "## 回测结束仍开放",
            "",
            _header("Symbol", "Status", "Entry", "Qty", "Unrealized Handling", "Notes"),
            "|---|---|---:|---:|---|---|",
        ]
    )
    for trade in open_trades:
        lines.append(
            "| "
            f"`{trade.symbol}` | {_status_label(trade.status)} | {_fmt(trade.entry_price_filled)} | {_fmt(trade.quantity)} | "
            "按最后 close 计入净值，不计入胜率/profit_factor/avg_R | "
            f"{trade.notes} |"
        )

    lines.extend(
        [
            "",
            "## 未入场/过期计划",
            "",
            _header("Symbol", "Status", "Created", "Entry Zone", "Score", "Notes"),
            "|---|---|---|---:|---:|---|",
        ]
    )
    if not inactive:
        lines.append("| n/a | n/a | n/a | n/a | n/a | No inactive plans. |")
    for trade in inactive:
        lines.append(
            "| "
            f"`{trade.symbol}` | {_status_label(trade.status)} | {trade.created_at_utc} | "
            f"{_fmt(trade.entry_low)} - {_fmt(trade.entry_high)} | {trade.score:.2f} | {trade.notes} |"
        )

    lines.extend(
        [
            "",
            "## 数据质量摘要",
            "",
            _header("Severity", "Symbol", "Interval", "Message"),
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
    if result.universe_type == "dynamic":
        report_kind = "backtest_dynamic_universe"
    elif result.universe_type == "snapshot":
        report_kind = "backtest_universe"
    else:
        report_kind = "backtest"
    prefix = f"{report_kind}_{result.start_utc[:10]}_{result.end_utc[:10]}"
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
    universe_mode: bool = False,
    max_universe_symbols: int | None = None,
    dynamic_universe_mode: bool = False,
    source_limit: int | None = None,
    dynamic_symbol_master=None,
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
        universe_mode=universe_mode,
        max_universe_symbols=max_universe_symbols,
        dynamic_universe_mode=dynamic_universe_mode,
        source_limit=source_limit,
        dynamic_symbol_master=dynamic_symbol_master,
        progress=progress,
    )
    metrics = calculate_metrics(result)
    benchmarks = _benchmarks(settings, result, start, end, progress=progress)
    report_paths = _write_report(settings, result, metrics, benchmarks, include_obsidian)
    _save_backtest_result(settings, result, metrics, report_paths)
    return result, metrics, report_paths
