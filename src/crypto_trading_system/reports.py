from __future__ import annotations

from dataclasses import asdict
from datetime import datetime, timedelta, timezone
from html import escape
import json
from pathlib import Path

from .config import Settings
from .models import ScanResult, TradeCandidate
from .report_versions import next_report_version, versioned_markdown_filename


def _fmt_price(value: float) -> str:
    if value >= 10_000:
        return f"{value:,.2f}"
    if value >= 100:
        return f"{value:,.2f}"
    if value >= 1:
        return f"{value:.4f}"
    if value >= 0.01:
        return f"{value:.5f}"
    return f"{value:.8g}"


def _fmt_pct(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value:+.2f}%"


def _fmt_money(value: float) -> str:
    if value >= 1_000_000_000:
        return f"${value / 1_000_000_000:.2f}B"
    if value >= 1_000_000:
        return f"${value / 1_000_000:.1f}M"
    return f"${value:,.0f}"


def _fmt_money_optional(value: float | None) -> str:
    if value is None:
        return "n/a"
    return _fmt_money(value)


def _fmt_optional(value: float | None) -> str:
    if value is None:
        return "n/a"
    return _fmt_price(value)


def _fmt_diff_pct(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value:.2f}%"


def _fmt_point_diff(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value:.2f} pts"


def _local_timestamp(timestamp_utc: str) -> str:
    dt = datetime.fromisoformat(timestamp_utc)
    return dt.astimezone(timezone(timedelta(hours=8), name="CST")).strftime("%Y-%m-%d %H:%M:%S %Z")


def _local_date(timestamp_utc: str) -> str:
    dt = datetime.fromisoformat(timestamp_utc)
    return dt.astimezone(timezone(timedelta(hours=8), name="CST")).strftime("%Y-%m-%d")


def _project_report_dir(settings: Settings, timestamp_utc: str) -> Path:
    return settings.output.reports_dir / _local_date(timestamp_utc)


def _obsidian_report_dir(settings: Settings, timestamp_utc: str) -> Path | None:
    if settings.output.obsidian_dir is None:
        return None
    return settings.output.obsidian_dir / "Reports" / _local_date(timestamp_utc)


def _is_verify_report(result: ScanResult) -> bool:
    return result.scan_id.startswith("verify_")


def _report_title(result: ScanResult, report_version: str | None = None) -> str:
    version_suffix = f" {report_version}" if report_version else ""
    if _is_verify_report(result):
        symbol = result.candidates[0].symbol if result.candidates else "UNKNOWN"
        return f"Crypto 单币复核报告 {symbol}{version_suffix}"
    return f"Crypto 市场扫描报告{version_suffix}"


def _report_filename_prefix(result: ScanResult) -> str:
    report_date = _local_date(result.timestamp_utc)
    if _is_verify_report(result):
        symbol = result.candidates[0].symbol if result.candidates else "UNKNOWN"
        return f"verify_{symbol}_{report_date}"
    return f"market_scan_{report_date}"


def _plan_heading(result: ScanResult) -> str:
    if _is_verify_report(result):
        symbol = result.candidates[0].symbol if result.candidates else "UNKNOWN"
        return f"单币复核交易计划：{symbol}"
    return f"{len(result.candidates)} 个候选交易计划"


def _candidate_section_heading(result: ScanResult) -> str:
    if _is_verify_report(result):
        return "复核币种说明"
    return "候选币说明"


def _append_candidate_table(lines: list[str], candidates: list[TradeCandidate]) -> None:
    lines.extend(
        [
            "| Rank | Coin | Action | Setup | Entry Zone | Stop Loss | TP1 | TP2 / Exit Rule | R/R | Verdict |",
            "|---:|---|---|---|---:|---:|---:|---|---:|---|",
        ]
    )
    for candidate in candidates:
        lines.append(
            "| "
            f"{candidate.rank} | "
            f"`{candidate.base_asset}` | "
            f"`{candidate.action}` | "
            f"{candidate.setup} | "
            f"{_fmt_price(candidate.entry_low)} - {_fmt_price(candidate.entry_high)} | "
            f"{_fmt_price(candidate.stop_loss)} | "
            f"{_fmt_price(candidate.take_profit_1)} | "
            f"{_fmt_price(candidate.take_profit_2)} 或跌破 4h 关键支撑 | "
            f"{candidate.risk_reward_1:.2f}-{candidate.risk_reward_2:.2f} | "
            f"{candidate.verdict} |"
        )


def _append_data_cross_check_summary(lines: list[str], candidates: list[TradeCandidate]) -> None:
    lines.extend(
        [
            "| Rank | Coin | State | Identity | Max Price Diff | Max 24h Diff | Issue Codes | Message |",
            "|---:|---|---|---|---:|---:|---|---|",
        ]
    )
    for candidate in candidates:
        price_diffs = [
            check.price_diff_pct
            for check in candidate.data_checks
            if check.provider != "Binance" and check.price_diff_pct is not None
        ]
        pct_diffs = [
            check.pct_24h_diff
            for check in candidate.data_checks
            if check.provider != "Binance" and check.pct_24h_diff is not None
        ]
        issue_codes = sorted({issue.code for issue in candidate.data_quality_issues})
        lines.append(
            "| "
            f"{candidate.rank} | "
            f"`{candidate.base_asset}` | "
            f"{candidate.data_quality_state} ({candidate.data_quality_status}) | "
            f"{candidate.external_identity_status} | "
            f"{_fmt_diff_pct(max(price_diffs) if price_diffs else None)} | "
            f"{_fmt_point_diff(max(pct_diffs) if pct_diffs else None)} | "
            f"{', '.join(issue_codes) or 'none'} | "
            f"{candidate.data_quality_message} |"
        )


def _append_data_cross_check_table(lines: list[str], candidate: TradeCandidate) -> None:
    lines.extend(
        [
            "| Source | Status | Identity | Blocking | Asset ID | Price | 24h Change | 24h Volume | Price Diff | 24h Diff | Updated | Issue Codes | Message |",
            "|---|---|---|---:|---|---:|---:|---:|---:|---:|---|---|---|",
        ]
    )
    if not candidate.data_checks:
        lines.append("| n/a | DATA_NOT_CHECKED | NOT_CHECKED | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | No cross-check data recorded. |")
        return
    for check in candidate.data_checks:
        issue_codes = sorted({issue.code for issue in check.issues})
        lines.append(
            "| "
            f"{check.provider} | "
            f"{check.status} | "
            f"{check.identity_status} | "
            f"{'yes' if check.blocking else 'no'} | "
            f"{check.provider_asset_id or 'n/a'} | "
            f"{_fmt_optional(check.price_usd)} | "
            f"{_fmt_pct(check.pct_24h)} | "
            f"{_fmt_money_optional(check.volume_24h)} | "
            f"{_fmt_diff_pct(check.price_diff_pct)} | "
            f"{_fmt_point_diff(check.pct_24h_diff)} | "
            f"{check.last_updated or check.fetched_at_utc} | "
            f"{', '.join(issue_codes) or 'none'} | "
            f"{check.message} |"
        )


def _chart_rel_path(result: ScanResult, candidate: TradeCandidate) -> str:
    return f"charts/{result.scan_id}_{candidate.symbol}.svg"


def _line_y(value: float, minimum: float, maximum: float, top: float, height: float) -> float:
    if maximum <= minimum:
        return top + height / 2
    return top + (maximum - value) / (maximum - minimum) * height


def render_candidate_chart(candidate: TradeCandidate) -> str:
    candles = candidate.recent_4h_klines
    width = 960
    height = 460
    left = 70
    right = 210
    top = 35
    chart_height = 330
    bottom = top + chart_height
    chart_width = width - left - right

    prices: list[float] = []
    for candle in candles:
        prices.extend([float(candle["high"]), float(candle["low"])])
    prices.extend(
        [
            candidate.entry_low,
            candidate.entry_high,
            candidate.stop_loss,
            candidate.take_profit_1,
            candidate.take_profit_2,
            candidate.price,
        ]
    )
    minimum = min(prices) * 0.995
    maximum = max(prices) * 1.005
    step = chart_width / max(len(candles), 1)
    body_width = max(4, step * 0.56)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        f'<text x="{left}" y="22" font-family="Arial" font-size="16" font-weight="700">{escape(candidate.symbol)} 4h evidence chart</text>',
        f'<rect x="{left}" y="{top}" width="{chart_width}" height="{chart_height}" fill="#fafafa" stroke="#dddddd"/>',
    ]

    for idx in range(5):
        y = top + idx * chart_height / 4
        price = maximum - idx * (maximum - minimum) / 4
        parts.append(f'<line x1="{left}" y1="{y:.2f}" x2="{left + chart_width}" y2="{y:.2f}" stroke="#eeeeee"/>')
        parts.append(f'<text x="8" y="{y + 4:.2f}" font-family="Arial" font-size="11" fill="#555">{_fmt_price(price)}</text>')

    for idx, candle in enumerate(candles):
        x = left + idx * step + step / 2
        open_price = float(candle["open"])
        high = float(candle["high"])
        low = float(candle["low"])
        close = float(candle["close"])
        color = "#16a34a" if close >= open_price else "#dc2626"
        y_high = _line_y(high, minimum, maximum, top, chart_height)
        y_low = _line_y(low, minimum, maximum, top, chart_height)
        y_open = _line_y(open_price, minimum, maximum, top, chart_height)
        y_close = _line_y(close, minimum, maximum, top, chart_height)
        rect_y = min(y_open, y_close)
        rect_h = max(1.5, abs(y_close - y_open))
        parts.append(f'<line x1="{x:.2f}" y1="{y_high:.2f}" x2="{x:.2f}" y2="{y_low:.2f}" stroke="{color}" stroke-width="1.4"/>')
        parts.append(f'<rect x="{x - body_width / 2:.2f}" y="{rect_y:.2f}" width="{body_width:.2f}" height="{rect_h:.2f}" fill="{color}" opacity="0.82"/>')

    def plan_line(value: float, label: str, color: str, dash: str = "") -> None:
        y = _line_y(value, minimum, maximum, top, chart_height)
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        parts.append(f'<line x1="{left}" y1="{y:.2f}" x2="{left + chart_width}" y2="{y:.2f}" stroke="{color}" stroke-width="1.5"{dash_attr}/>')
        parts.append(f'<text x="{left + chart_width + 10}" y="{y + 4:.2f}" font-family="Arial" font-size="12" fill="{color}">{escape(label)} {_fmt_price(value)}</text>')

    plan_line(candidate.entry_low, "Entry low", "#2563eb", "4 4")
    plan_line(candidate.entry_high, "Entry high", "#2563eb", "4 4")
    plan_line(candidate.stop_loss, "Stop", "#dc2626")
    plan_line(candidate.take_profit_1, "TP1", "#16a34a")
    plan_line(candidate.take_profit_2, "TP2", "#15803d")
    plan_line(candidate.price, "Last", "#111827", "2 3")

    parts.extend(
        [
            f'<text x="{left}" y="{bottom + 28}" font-family="Arial" font-size="12" fill="#555">Candles: latest {len(candles)} x 4h Binance klines. Lines show entry zone, stop, TP1, TP2, and latest close.</text>',
            f'<text x="{left}" y="{bottom + 50}" font-family="Arial" font-size="12" fill="#555">This chart is generated from locally fetched OHLCV, so you can compare it with Binance or TradingView manually.</text>',
            "</svg>",
        ]
    )
    return "\n".join(parts)


def write_candidate_charts(result: ScanResult, report_dir: Path) -> None:
    chart_dir = report_dir / "charts"
    chart_dir.mkdir(parents=True, exist_ok=True)
    for candidate in result.candidates:
        chart_path = chart_dir / f"{result.scan_id}_{candidate.symbol}.svg"
        chart_path.write_text(render_candidate_chart(candidate), encoding="utf-8")


def generate_scan_report(
    result: ScanResult,
    settings: Settings,
    report_version: str | None = None,
    run_id: str | None = None,
    run_type: str = "manual",
) -> str:
    report_title = _report_title(result, report_version)
    version_lines = [] if report_version is None else [f"report_version: {report_version}"]
    version_summary = [] if report_version is None else [f"- 报告版本：{report_version}"]
    lines: list[str] = [
        "---",
        f"created: {_local_timestamp(result.timestamp_utc)}",
        "tags:",
        "  - crypto",
        "  - trading-system",
        f"  - {'single-symbol-verify' if _is_verify_report(result) else 'market-scan'}",
        f"scan_id: {result.scan_id}",
        *version_lines,
        "---",
        "",
        f"# {report_title}",
        "",
        f"- 报告时间：{_local_timestamp(result.timestamp_utc)}",
        f"- Run ID：`{run_id or 'n/a'}`",
        f"- Run type：`{run_type}`",
        f"- Data validation mode：`{result.validation_mode}`",
        "- 数据来源：SQLite",
        *version_summary,
        f"- 扫描 ID：{result.scan_id}",
        f"- 数据源：{result.source}",
        f"- 过滤条件：{result.filters}",
        f"- 默认单笔风险：账户权益的 {settings.analysis.risk_per_trade_pct * 100:.2f}%",
        "",
        "## 限制说明",
        "",
    ]

    for limitation in result.limitations:
        lines.append(f"- {limitation}")

    lines.extend(
        [
            "",
            f"## {_plan_heading(result)}",
            "",
        ]
    )
    _append_candidate_table(lines, result.candidates)

    lines.extend(
        [
            "",
            "## 数据交叉验证摘要",
            "",
            "价格差异以 Binance 当前价为基准；成交量口径不同，Binance 是 USDT 现货成交额，CoinGecko/CoinMarketCap 通常是全市场成交量。",
            "",
        ]
    )
    _append_data_cross_check_summary(lines, result.candidates)

    if _is_verify_report(result) and result.context_candidates:
        verified_symbol = result.candidates[0].symbol if result.candidates else ""
        lines.extend(
            [
                "",
                "## 当前大盘 5 个候选币对照",
                "",
                f"下面这张表是复核 `{verified_symbol}` 时同步跑出的当前大盘候选，方便你比较复核币和系统 Top 5 的相对位置。",
                "",
            ]
        )
        _append_candidate_table(lines, result.context_candidates)
        lines.extend(
            [
                "",
                "### 当前大盘候选数据交叉验证摘要",
                "",
            ]
        )
        _append_data_cross_check_summary(lines, result.context_candidates)

    lines.extend(["", f"## {_candidate_section_heading(result)}", ""])
    for candidate in result.candidates:
        rsi_text = "n/a" if candidate.rsi_4h is None else f"{candidate.rsi_4h:.2f}"
        volume_text = _fmt_money(candidate.quote_volume_24h)
        lines.extend(
            [
                f"### {candidate.rank}. {candidate.base_asset} `{candidate.symbol}`",
                "",
                f"![{candidate.symbol} evidence chart]({_chart_rel_path(result, candidate)})",
                "",
                f"- 入选原因：{candidate.setup}；24h {_fmt_pct(candidate.pct_24h)}，7d {_fmt_pct(candidate.pct_7d)}，4h RSI {rsi_text}，24h 成交额 {volume_text}。",
                f"- 交易失效条件：{candidate.invalidation}。",
                f"- 主要风险：{'；'.join(candidate.risks)}。",
                f"- 数据交叉验证：{candidate.data_quality_state} / {candidate.data_quality_status}；身份={candidate.external_identity_status}；{candidate.data_quality_message}",
                "",
                "#### 可点击人工验证",
                "",
                f"- [Binance 交易页]({candidate.binance_trade_url})",
                f"- [TradingView 图表]({candidate.tradingview_url})",
                f"- [CoinGecko 搜索]({candidate.coingecko_search_url})",
                f"- [CoinMarketCap 搜索]({candidate.coinmarketcap_search_url})",
                "",
                "#### 多数据源对照",
                "",
            ]
        )
        _append_data_cross_check_table(lines, candidate)
        lines.extend(
            [
                "",
                "#### 指标证据",
                "",
                "| 指标 | 数值 | 人工核对用途 |",
                "|---|---:|---|",
                f"| 当前价 | {_fmt_price(candidate.price)} | 与 Binance/TradingView 当前价格对照 |",
                f"| 24h 涨跌 | {_fmt_pct(candidate.pct_24h)} | 与交易所 24h 涨跌对照 |",
                f"| 7d 涨跌 | {_fmt_pct(candidate.pct_7d)} | 判断短线趋势是否延续 |",
                f"| 4h EMA20 | {_fmt_optional(candidate.ema20_4h)} | 判断短期趋势支撑 |",
                f"| 4h EMA50 | {_fmt_optional(candidate.ema50_4h)} | 判断中期趋势支撑 |",
                f"| 1d EMA20 | {_fmt_optional(candidate.ema20_1d)} | 判断日线趋势 |",
                f"| 1d EMA50 | {_fmt_optional(candidate.ema50_1d)} | 判断日线趋势 |",
                f"| 4h RSI14 | {rsi_text} | 判断是否过热/过弱 |",
                f"| 4h ATR14 | {_fmt_optional(candidate.atr_4h)} | 推导止损和入场缓冲 |",
                f"| 最近 18 根 4h 最低点 | {_fmt_optional(candidate.recent_low_4h_18)} | 支撑/止损参考 |",
                f"| 最近 36 根 4h 最高点 | {_fmt_optional(candidate.recent_high_4h_36)} | TP/压力参考 |",
                f"| 支撑位 | {_fmt_optional(candidate.support_level)} | 入场区间推导基础 |",
                "",
                "#### 交易计划推导",
                "",
                f"- 支撑位 = 最近低点、4h EMA20、4h EMA50、1d EMA20 中不高于当前价的最高有效支撑 = `{_fmt_optional(candidate.support_level)}`。",
                f"- 入场区间 = 支撑位附近 + ATR 缓冲 = `{_fmt_price(candidate.entry_low)} - {_fmt_price(candidate.entry_high)}`。",
                f"- 止损 = min(最近 18 根 4h 最低点 * 0.985, 入场中位价 - 1.15 * ATR14) = `{_fmt_price(candidate.stop_loss)}`。",
                f"- TP1 = max(最近 36 根 4h 最高点 * 0.995, 入场中位价 + 2R) = `{_fmt_price(candidate.take_profit_1)}`。",
                f"- TP2 = max(入场中位价 + 3R, TP1 * 1.04) = `{_fmt_price(candidate.take_profit_2)}`。",
                "",
                "#### 最近 10 根 4h K线",
                "",
                "| UTC 开盘时间 | Open | High | Low | Close | Quote Volume | Trades |",
                "|---|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for candle in candidate.recent_4h_klines[-10:]:
            lines.append(
                "| "
                f"{candle['open_time_utc']} | "
                f"{_fmt_price(float(candle['open']))} | "
                f"{_fmt_price(float(candle['high']))} | "
                f"{_fmt_price(float(candle['low']))} | "
                f"{_fmt_price(float(candle['close']))} | "
                f"{_fmt_money(float(candle['quote_volume']))} | "
                f"{int(candle['trades'])} |"
            )
        lines.append("")

    lines.extend(
        [
            "## 组合风控",
            "",
            "- 不要 5 个候选全部满仓买入。",
            "- 同时持仓总风险建议控制在账户权益的 3% - 5% 以内。",
            "- 如果 BTC/ETH 同时破位，暂停山寨币多头计划或降低仓位。",
            "- 第一版报告用于模拟盘和人工复核，不自动下单。",
            "",
            "## 原始数据",
            "",
            "```json",
            json.dumps([asdict(candidate) for candidate in result.candidates], ensure_ascii=False, indent=2),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def write_scan_reports(
    result: ScanResult,
    settings: Settings,
    include_obsidian: bool = True,
    run_id: str | None = None,
    run_type: str = "manual",
) -> list[Path]:
    project_report_dir = _project_report_dir(settings, result.timestamp_utc)
    obsidian_report_dir = _obsidian_report_dir(settings, result.timestamp_utc)
    target_dirs = [project_report_dir]
    if include_obsidian and obsidian_report_dir is not None:
        target_dirs.append(obsidian_report_dir)

    filename_prefix = _report_filename_prefix(result)
    report_version_number = next_report_version(target_dirs, filename_prefix)
    report_version = f"v{report_version_number}"
    filename = versioned_markdown_filename(filename_prefix, report_version_number)
    markdown = generate_scan_report(
        result,
        settings,
        report_version=report_version,
        run_id=run_id,
        run_type=run_type,
    )
    paths: list[Path] = []

    project_report_dir.mkdir(parents=True, exist_ok=True)
    write_candidate_charts(result, project_report_dir)
    project_path = project_report_dir / filename
    project_path.write_text(markdown, encoding="utf-8")
    paths.append(project_path)

    if include_obsidian and obsidian_report_dir is not None:
        obsidian_report_dir.mkdir(parents=True, exist_ok=True)
        write_candidate_charts(result, obsidian_report_dir)
        obsidian_path = obsidian_report_dir / filename
        obsidian_path.write_text(markdown, encoding="utf-8")
        paths.append(obsidian_path)

    return paths
