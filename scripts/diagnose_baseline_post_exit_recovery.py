"""Diagnose post-exit 1R recovery for the frozen baseline cohort.

This is a read-only, conditional diagnostic over the current-survivor
baseline cohort.  It starts at exit_bar + 1, censors at the next same-symbol
entry or the frozen window boundary, and never changes strategy settings.

Run from the repository root:

    python scripts/diagnose_baseline_post_exit_recovery.py
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import sqlite3
import subprocess
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PATHS = ROOT / "reports/2026-10-10/baseline_trade_path_attribution_2026-10-10_v1.csv"
DEFAULT_REPLAY_DIR = ROOT / "reports/2026-10-09/atr_fixed_history"
DEFAULT_DATABASE = ROOT / "data/crypto_trading.db"
DEFAULT_OUTPUT_DIR = ROOT / "reports/2026-10-14/baseline_post_exit_recovery_v1"
WINDOW_REPLAY = {
    "2024-07-01": DEFAULT_REPLAY_DIR / "2024-07-01_confirmation_close_baseline.json",
    "2025-06-01": DEFAULT_REPLAY_DIR / "2025-06-01_confirmation_close_baseline.json",
}
WINDOW_END_ISO = {
    "2024-07-01": "2025-06-01T00:00:00+00:00",
    "2025-06-01": "2026-06-01T00:00:00+00:00",
}
BAR_MS = 4 * 60 * 60 * 1000
HORIZONS = (20, 40, 80)
BENCHMARKS = ("BTCUSDT", "ETHUSDT")


def iso_ms(value: str) -> int:
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return int(dt.timestamp() * 1000)


def iso_utc(ms: int) -> str:
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).isoformat(timespec="seconds")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def wilson_interval(successes: int, total: int, z: float = 1.959963984540054) -> tuple[float | None, float | None]:
    if total <= 0:
        return None, None
    proportion = successes / total
    denominator = 1 + z * z / total
    center = (proportion + z * z / (2 * total)) / denominator
    margin = z * math.sqrt(proportion * (1 - proportion) / total + z * z / (4 * total * total)) / denominator
    return 100 * (center - margin), 100 * (center + margin)


def load_path_rows(path: Path) -> list[dict[str, Any]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        for field in (
            "entry_price_filled",
            "stop_loss",
            "net_pnl",
            "gross_pnl",
            "mae_r",
            "mfe_r",
            "realized_net_r",
        ):
            row[field] = float(row[field])
    return rows


def load_replay_entries(paths: dict[str, Path]) -> dict[str, dict[str, list[int]]]:
    result: dict[str, dict[str, list[int]]] = {}
    for window, path in paths.items():
        payload = json.loads(path.read_text(encoding="utf-8"))
        by_symbol: dict[str, list[int]] = {}
        for trade in payload["result"]["trades"]:
            entered = trade.get("entered_at_utc")
            if not entered:
                continue
            by_symbol.setdefault(trade["symbol"], []).append(iso_ms(entered))
        result[window] = {symbol: sorted(set(times)) for symbol, times in by_symbol.items()}
    return result


def next_entry_after(entries: Iterable[int], exit_ms: int) -> int | None:
    return next((entry for entry in entries if entry > exit_ms), None)


def choose_cutoff(exit_ms: int, window_end_ms: int, next_entry_ms: int | None, max_bars: int = 80) -> tuple[int, str]:
    candidates = [(exit_ms + (max_bars + 1) * BAR_MS, "max_horizon"), (window_end_ms, "window_end")]
    if next_entry_ms is not None:
        candidates.append((next_entry_ms, "next_same_symbol_entry"))
    return min(candidates, key=lambda item: item[0])


def query_bars(
    connection: sqlite3.Connection,
    symbol: str,
    exit_ms: int,
    cutoff_exclusive_ms: int,
) -> list[tuple[int, float, float, float, float]]:
    rows = connection.execute(
        """
        SELECT open_time, open, high, low, close
        FROM kline_cache
        WHERE source = 'Binance' AND symbol = ? AND interval = '4h'
          AND open_time > ? AND open_time < ?
        ORDER BY open_time
        """,
        (symbol, exit_ms, cutoff_exclusive_ms),
    ).fetchall()
    return [(int(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4])) for row in rows]


def contiguous_prefix(
    bars: list[tuple[int, float, float, float, float]],
    exit_ms: int,
) -> list[tuple[int, float, float, float, float]]:
    expected = exit_ms + BAR_MS
    result = []
    for bar in bars:
        if bar[0] != expected:
            break
        result.append(bar)
        expected += BAR_MS
    return result


def benchmark_return_pct(
    connection: sqlite3.Connection,
    timestamps: list[int],
    used_bars: set[tuple[Any, ...]],
) -> float | None:
    if not timestamps:
        return None
    returns = []
    for symbol in BENCHMARKS:
        placeholders = ",".join("?" for _ in timestamps)
        records = connection.execute(
            f"""
            SELECT open_time, open, high, low, close
            FROM kline_cache
            WHERE source = 'Binance' AND symbol = ? AND interval = '4h'
              AND open_time IN ({placeholders})
            ORDER BY open_time
            """,
            (symbol, *timestamps),
        ).fetchall()
        if len(records) != len(timestamps) or [int(row[0]) for row in records] != timestamps:
            return None
        for record in records:
            used_bars.add((symbol, int(record[0]), *[float(value) for value in record[1:]]))
        returns.append(100 * (float(records[-1][4]) / float(records[0][1]) - 1))
    return sum(returns) / len(returns)


def horizon_metrics(
    bars: list[tuple[int, float, float, float, float]],
    *,
    entry: float,
    stop: float,
    horizon: int,
) -> dict[str, Any]:
    risk = entry - stop
    if risk <= 0:
        raise ValueError("only positive-risk long trades are supported")
    observed = bars[:horizon]
    target_1r = entry + risk
    target_2r = entry + 2 * risk
    first_1r = next((index + 1 for index, bar in enumerate(observed) if bar[2] >= target_1r), None)
    first_2r = next((index + 1 for index, bar in enumerate(observed) if bar[2] >= target_2r), None)
    eligible = len(bars) >= horizon
    return {
        "eligible": eligible,
        "observed_bars": len(observed),
        "observed_recover_1r": first_1r is not None,
        "recover_1r": (first_1r is not None) if eligible else None,
        "time_to_recover_1r_bars": first_1r,
        "observed_recover_2r": first_2r is not None,
        "recover_2r": (first_2r is not None) if eligible else None,
        "max_favorable_r": max(((bar[2] - entry) / risk for bar in observed), default=None),
    }


def exit_iso_week(value: str) -> str:
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    year, week, _ = dt.isocalendar()
    return f"{year}-W{week:02d}"


def enrich_trade(
    row: dict[str, Any],
    *,
    connection: sqlite3.Connection,
    replay_entries: dict[str, dict[str, list[int]]],
    used_bars: set[tuple[Any, ...]],
) -> dict[str, Any]:
    window = row["window_start"]
    exit_ms = iso_ms(row["closed_at_utc"])
    window_end_ms = iso_ms(WINDOW_END_ISO[window])
    next_entry_ms = next_entry_after(replay_entries[window].get(row["symbol"], []), exit_ms)
    cutoff_ms, planned_reason = choose_cutoff(exit_ms, window_end_ms, next_entry_ms)
    raw_bars = query_bars(connection, row["symbol"], exit_ms, cutoff_ms)
    bars = contiguous_prefix(raw_bars, exit_ms)
    for bar in bars:
        used_bars.add((row["symbol"], *bar))

    planned_bars = max(0, (cutoff_ms - exit_ms - 1) // BAR_MS)
    if len(bars) < min(planned_bars, max(HORIZONS)):
        censor_reason = "kline_gap_or_missing"
    elif len(bars) < max(HORIZONS):
        censor_reason = planned_reason
    else:
        censor_reason = "none"

    result: dict[str, Any] = {
        "window_start": window,
        "trade_id": row["trade_id"],
        "symbol": row["symbol"],
        "entered_at_utc": row["entered_at_utc"],
        "exit_at_utc": row["closed_at_utc"],
        "exit_iso_week": exit_iso_week(row["closed_at_utc"]),
        "status": row["status"],
        "regime": row["regime"],
        "capacity_group": row["capacity_group"],
        "path_label": row["path_label"],
        "net_pnl": row["net_pnl"],
        "entry_price": row["entry_price_filled"],
        "initial_stop": row["stop_loss"],
        "risk_per_unit": row["entry_price_filled"] - row["stop_loss"],
        "pre_exit_mfe_r": row["mfe_r"],
        "pre_exit_mae_r": row["mae_r"],
        "next_entry_at_utc": iso_utc(next_entry_ms) if next_entry_ms is not None else None,
        "window_end_utc": WINDOW_END_ISO[window],
        "post_exit_first_bar_utc": iso_utc(bars[0][0]) if bars else None,
        "post_exit_last_bar_utc": iso_utc(bars[-1][0]) if bars else None,
        "cutoff_exclusive_utc": iso_utc(cutoff_ms),
        "planned_cutoff_reason": planned_reason,
        "post_exit_contiguous_bars": len(bars),
        "censor_reason_80": censor_reason,
        "near_unknown": (
            window == "2025-06-01"
            and row["capacity_group"] == "non_capacity"
            and row["net_pnl"] <= 0
            and row["path_label"] == "other_or_inconclusive"
        ),
    }
    for horizon in HORIZONS:
        metric = horizon_metrics(
            bars,
            entry=row["entry_price_filled"],
            stop=row["stop_loss"],
            horizon=horizon,
        )
        prefix = bars[:horizon]
        market_return = benchmark_return_pct(connection, [bar[0] for bar in prefix], used_bars) if metric["eligible"] else None
        result.update(
            {
                f"eligible_{horizon}": metric["eligible"],
                f"observed_bars_{horizon}": metric["observed_bars"],
                f"observed_recover_1r_{horizon}": metric["observed_recover_1r"],
                f"recover_1r_{horizon}": metric["recover_1r"],
                f"time_to_recover_1r_bars_{horizon}": metric["time_to_recover_1r_bars"],
                f"post_exit_max_favorable_r_{horizon}": metric["max_favorable_r"],
                f"market_btc_eth_median_return_pct_{horizon}": market_return,
                f"market_tailwind_{horizon}": (market_return > 0) if market_return is not None else None,
            }
        )
        if horizon == 40:
            result["recover_2r_40"] = metric["recover_2r"]
            result["observed_recover_2r_40"] = metric["observed_recover_2r"]
    return result


def summarize_rate(rows: list[dict[str, Any]], horizon: int) -> dict[str, Any]:
    eligible = [row for row in rows if row[f"eligible_{horizon}"]]
    recovered = [row for row in eligible if row[f"recover_1r_{horizon}"]]
    censored = [row for row in rows if not row[f"eligible_{horizon}"]]
    censored_recovered = [row for row in censored if row[f"observed_recover_1r_{horizon}"]]
    low, high = wilson_interval(len(recovered), len(eligible))
    return {
        "total": len(rows),
        "eligible": len(eligible),
        "censored": len(censored),
        "censored_pct": 100 * len(censored) / len(rows) if rows else None,
        "recovered": len(recovered),
        "recovery_rate_pct": 100 * len(recovered) / len(eligible) if eligible else None,
        "wilson_95_low_pct": low,
        "wilson_95_high_pct": high,
        "recovered_before_censor": len(censored_recovered),
    }


def aggregate_rates(rows: list[dict[str, Any]], windows: Iterable[str]) -> dict[str, dict[str, Any]]:
    output: dict[str, dict[str, Any]] = {}
    for window in windows:
        subset = [row for row in rows if row["window_start"] == window]
        output[window] = {str(horizon): summarize_rate(subset, horizon) for horizon in HORIZONS}
    return output


def group_k40(rows: list[dict[str, Any]], field: str) -> list[dict[str, Any]]:
    groups: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for row in rows:
        label = row[field]
        groups.setdefault((row["window_start"], str(label)), []).append(row)
    return [
        {"window_start": window, field: label, **summarize_rate(group, 40)}
        for (window, label), group in sorted(groups.items())
    ]


def leave_one_out(rows: list[dict[str, Any]], field: str) -> dict[str, dict[str, Any]]:
    output: dict[str, dict[str, Any]] = {}
    for window in WINDOW_END_ISO:
        eligible = [row for row in rows if row["window_start"] == window and row["eligible_40"]]
        rates = []
        for label in sorted({row[field] for row in eligible}):
            kept = [row for row in eligible if row[field] != label]
            if not kept:
                continue
            rate = 100 * sum(bool(row["recover_1r_40"]) for row in kept) / len(kept)
            rates.append((rate, label, len(kept)))
        output[window] = {
            "dimension": field,
            "min_rate_pct": min(rates)[0] if rates else None,
            "min_removed_label": min(rates)[1] if rates else None,
            "max_rate_pct": max(rates)[0] if rates else None,
            "max_removed_label": max(rates)[1] if rates else None,
            "variants": len(rates),
        }
    return output


def classify_verdict(summary: dict[str, Any]) -> tuple[str, list[str]]:
    primary = summary["primary_by_window_horizon"]
    symbol_loo = summary["concentration_k40"]["symbol"]
    week_loo = summary["concentration_k40"]["exit_week"]
    windows = list(WINDOW_END_ISO)
    k40 = [primary[window]["40"] for window in windows]
    all_horizon_rates = [
        primary[window][str(horizon)]["recovery_rate_pct"]
        for window in windows
        for horizon in HORIZONS
    ]
    reasons = []

    low_support = all(item["recovery_rate_pct"] is not None and item["recovery_rate_pct"] <= 30 for item in k40)
    low_support = low_support and all(rate is not None and rate <= 40 for rate in all_horizon_rates)
    low_support = low_support and all(item["wilson_95_high_pct"] is not None and item["wilson_95_high_pct"] <= 40 for item in k40)
    low_support = low_support and all(item["censored_pct"] <= 20 for item in k40)
    low_support = low_support and all(
        symbol_loo[window]["max_rate_pct"] is not None and symbol_loo[window]["max_rate_pct"] <= 40
        and week_loo[window]["max_rate_pct"] is not None and week_loo[window]["max_rate_pct"] <= 40
        for window in windows
    )
    if low_support:
        reasons.append("两个窗口K40均不高于30%，全部预注册horizon及集中度检查未越过40%")
        return "supports_no_follow_through_conditional", reasons

    high_support = all(item["recovery_rate_pct"] is not None and item["recovery_rate_pct"] >= 40 for item in k40)
    high_support = high_support and all(item["wilson_95_low_pct"] is not None and item["wilson_95_low_pct"] >= 30 for item in k40)
    high_support = high_support and all(item["censored_pct"] <= 20 for item in k40)
    high_support = high_support and all(
        symbol_loo[window]["min_rate_pct"] is not None and symbol_loo[window]["min_rate_pct"] >= 30
        and week_loo[window]["min_rate_pct"] is not None and week_loo[window]["min_rate_pct"] >= 30
        for window in windows
    )
    if high_support:
        non_tailwind = {
            row["window_start"]: row
            for row in summary["market_tailwind_k40"]
            if row["market_tailwind_40"] == "False"
        }
        if all(
            window in non_tailwind
            and non_tailwind[window]["eligible"] >= 5
            and non_tailwind[window]["recovery_rate_pct"] is not None
            and non_tailwind[window]["recovery_rate_pct"] >= 30
            for window in windows
        ):
            reasons.append("两个窗口K40均至少40%，区间、集中度和非市场顺风子组保留必要条件")
            return "supports_exit_timing_necessary_condition_conditional", reasons
        reasons.append("K40点估计偏高，但非市场顺风子组不足或低于30%，无法排除市场beta")

    for window, item in zip(windows, k40):
        reasons.append(
            f"{window}: K40={item['recovery_rate_pct']:.2f}% "
            f"(eligible={item['eligible']}, censored={item['censored']})"
        )
    return "insufficient_or_window_inconsistent", reasons


def fmt_pct(value: float | None) -> str:
    return "n/a" if value is None else f"{value:.2f}%"


def render_report(summary: dict[str, Any]) -> str:
    verdict = summary["verdict"]
    if verdict == "supports_no_follow_through_conditional":
        plain = "两个窗口的退出后恢复都低，条件性支持老 baseline 缺少持续动能；不应优先放宽退出。"
    elif verdict == "supports_exit_timing_necessary_condition_conditional":
        plain = "两个窗口的退出后恢复都高，退出可能过早的必要条件成立；这仍不证明修改退出能盈利。"
    else:
        plain = "两个窗口或稳健性检查没有给出同一方向，不能把亏损归为退出过早或慢性无跟随。"

    early = summary["primary_by_window_horizon"]["2024-07-01"]["40"]
    near = summary["primary_by_window_horizon"]["2025-06-01"]["40"]
    unknown_40 = summary["near_unknown_by_horizon"]["40"]
    unknown_80 = summary["near_unknown_by_horizon"]["80"]
    lines = [
        "# Baseline 退出后 1R 恢复率诊断",
        "",
        "> **CONDITIONAL / NON-GENERALIZABLE**：current-survivor 已烧窗口诊断，不替代 point-in-time 历史币池或自然前向验证。",
        "",
        "## 白话结论",
        "",
        plain,
        "",
        f"正式裁决：**`{verdict}`**。",
        "",
        f"早窗主口径为 {early['recovered']}/{early['eligible']}（{fmt_pct(early['recovery_rate_pct'])}），落在预声明的 30%–40% 灰区；近窗为 {near['recovered']}/{near['eligible']}（{fmt_pct(near['recovery_rate_pct'])}），落在低恢复区。近窗 17 笔 unknown 在 K40 完整样本中为 {unknown_40['recovered']}/{unknown_40['eligible']}，到 K80 也仅 {unknown_80['recovered']}/{unknown_80['eligible']}。",
        "",
        "本结果只用于选择下一条研究轴；没有修改 stop、TP、持仓时间、入场规则或生产配置。",
        "",
        "## 主样本恢复率",
        "",
        "| 窗口 | K | 总数 | 完整观察 | 删失 | 恢复 | 恢复率 | Wilson 95%区间 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for window, horizons in summary["primary_by_window_horizon"].items():
        for horizon in HORIZONS:
            item = horizons[str(horizon)]
            lines.append(
                f"| {window} | {horizon} | {item['total']} | {item['eligible']} | {item['censored']} | "
                f"{item['recovered']} | {fmt_pct(item['recovery_rate_pct'])} | "
                f"[{fmt_pct(item['wilson_95_low_pct'])}, {fmt_pct(item['wilson_95_high_pct'])}] |"
            )

    lines.extend([
        "",
        "删失交易不记作未恢复；`recovered_before_censor` 仅作描述性记录，不进入主恢复率分母。",
        "",
        "## 容量竞逐组（单列）",
        "",
        "| 窗口 | K | 总数 | 完整观察 | 恢复 | 恢复率 |",
        "|---|---:|---:|---:|---:|---:|",
    ])
    for window, horizons in summary["capacity_by_window_horizon"].items():
        for horizon in HORIZONS:
            item = horizons[str(horizon)]
            lines.append(
                f"| {window} | {horizon} | {item['total']} | {item['eligible']} | "
                f"{item['recovered']} | {fmt_pct(item['recovery_rate_pct'])} |"
            )

    lines.extend([
        "",
        "## 近窗 17 笔 unknown",
        "",
        "| K | 总数 | 完整观察 | 删失 | 恢复 | 恢复率 | Wilson 95%区间 |",
        "|---:|---:|---:|---:|---:|---:|---:|",
    ])
    for horizon in HORIZONS:
        item = summary["near_unknown_by_horizon"][str(horizon)]
        lines.append(
            f"| {horizon} | {item['total']} | {item['eligible']} | {item['censored']} | {item['recovered']} | "
            f"{fmt_pct(item['recovery_rate_pct'])} | [{fmt_pct(item['wilson_95_low_pct'])}, {fmt_pct(item['wilson_95_high_pct'])}] |"
        )

    lines.extend([
        "",
        "## K40 市场顺风分层",
        "",
        "市场顺风定义为同一 horizon 内 BTC/ETH 中位累计收益大于 0；它是 beta 锚，不是因果对照。",
        "",
        "| 窗口 | 市场顺风 | 完整观察 | 恢复 | 恢复率 |",
        "|---|---|---:|---:|---:|",
    ])
    for item in summary["market_tailwind_k40"]:
        lines.append(
            f"| {item['window_start']} | {item['market_tailwind_40']} | {item['eligible']} | "
            f"{item['recovered']} | {fmt_pct(item['recovery_rate_pct'])} |"
        )

    lines.extend([
        "",
        "## K40 regime 分层",
        "",
        "| 窗口 | regime | 完整观察 | 恢复 | 恢复率 |",
        "|---|---|---:|---:|---:|",
    ])
    for item in summary["regime_k40"]:
        lines.append(
            f"| {item['window_start']} | {item['regime']} | {item['eligible']} | "
            f"{item['recovered']} | {fmt_pct(item['recovery_rate_pct'])} |"
        )

    lines.extend([
        "",
        "## K40 集中度",
        "",
        "| 窗口 | 维度 | 移除一组后最低恢复率 | 最高恢复率 |",
        "|---|---|---:|---:|",
    ])
    for dimension, groups in summary["concentration_k40"].items():
        for window, item in groups.items():
            lines.append(
                f"| {window} | {dimension} | {fmt_pct(item['min_rate_pct'])}（移除 {item['min_removed_label']}） | "
                f"{fmt_pct(item['max_rate_pct'])}（移除 {item['max_removed_label']}） |"
            )

    lines.extend([
        "",
        "## 删失审计",
        "",
        "| 80根观察状态 | 交易数 |",
        "|---|---:|",
    ])
    for reason, count in summary["censor_reason_80"].items():
        lines.append(f"| {reason} | {count} |")

    lines.extend([
        "",
        "## 裁决依据",
        "",
    ])
    lines.extend(f"- {reason}" for reason in summary["verdict_reasons"])
    lines.extend([
        "",
        "## 解释边界",
        "",
        "- 恢复率高最多说明退出可能过早的必要条件成立，不证明继续持有或放宽止损能产生正净收益。",
        "- 恢复率低更适合证伪退出解释，但仍受 current-survivor 幸存者偏差和 4h bar 粒度限制。",
        "- 市场顺风、同币再次入场和窗口结束均已显式处理；不能用删失样本补成失败。",
        "- 本轮不自动创建退出参数实验，也不启动 `CRYPTOTRADIN-127`。",
        "",
        "逐笔结果见 `trades.csv`，机器可读汇总与输入/查询摘要见 `summary.json`。",
    ])
    return "\n".join(lines) + "\n"


def run(args: argparse.Namespace) -> dict[str, Any]:
    replay_paths = {
        window: args.replay_dir / path.name
        for window, path in WINDOW_REPLAY.items()
    }
    source_rows = load_path_rows(args.paths_csv)
    stopped_rows = [row for row in source_rows if row["status"] == "STOPPED"]
    replay_entries = load_replay_entries(replay_paths)
    used_bars: set[tuple[Any, ...]] = set()
    connection = sqlite3.connect(f"file:{args.database.as_posix()}?mode=ro", uri=True)
    try:
        rows = [
            enrich_trade(
                row,
                connection=connection,
                replay_entries=replay_entries,
                used_bars=used_bars,
            )
            for row in stopped_rows
        ]
    finally:
        connection.close()

    primary = [row for row in rows if row["capacity_group"] == "non_capacity"]
    capacity = [row for row in rows if row["capacity_group"] == "capacity_contested"]
    unknown = [row for row in primary if row["near_unknown"]]
    if len(primary) != 87:
        raise ValueError(f"expected 87 non-capacity STOPPED rows, got {len(primary)}")
    if len(unknown) != 17:
        raise ValueError(f"expected 17 near-window unknown losses, got {len(unknown)}")

    canonical_bars = json.dumps(sorted(used_bars), separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    summary: dict[str, Any] = {
        "experiment": "baseline_post_exit_recovery_v1",
        "taskboard": "CRYPTOTRADIN-128",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "scope": {
            "universe": "current-survivor conditional",
            "venue": "Binance spot USDT",
            "timeframe": "4h",
            "start": "exit_bar+1",
            "risk": "entry_price_filled - original stop_loss",
            "horizons": list(HORIZONS),
            "primary_horizon": 40,
            "window_end_exclusive": WINDOW_END_ISO,
            "next_entry_censoring": True,
        },
        "counts": {
            "all_stopped": len(rows),
            "non_capacity_stopped": len(primary),
            "capacity_contested_stopped": len(capacity),
            "near_unknown": len(unknown),
        },
        "primary_by_window_horizon": aggregate_rates(primary, WINDOW_END_ISO),
        "capacity_by_window_horizon": aggregate_rates(capacity, WINDOW_END_ISO),
        "near_unknown_by_horizon": {str(horizon): summarize_rate(unknown, horizon) for horizon in HORIZONS},
        "market_tailwind_k40": group_k40(primary, "market_tailwind_40"),
        "regime_k40": group_k40(primary, "regime"),
        "concentration_k40": {
            "symbol": leave_one_out(primary, "symbol"),
            "exit_week": leave_one_out(primary, "exit_iso_week"),
        },
        "censor_reason_80": {},
        "reproducibility": {
            "git_head_before_changes": subprocess.run(
                ["git", "rev-parse", "HEAD"], cwd=ROOT, check=True, capture_output=True, text=True
            ).stdout.strip(),
            "paths_csv_sha256": sha256_file(args.paths_csv),
            "replay_sha256": {window: sha256_file(path) for window, path in replay_paths.items()},
            "queried_bars_sha256": hashlib.sha256(canonical_bars).hexdigest(),
            "queried_bar_rows": len(used_bars),
            "script_sha256": sha256_file(Path(__file__)),
        },
    }
    for reason in sorted({row["censor_reason_80"] for row in rows}):
        summary["censor_reason_80"][reason] = sum(row["censor_reason_80"] == reason for row in rows)
    verdict, reasons = classify_verdict(summary)
    summary["verdict"] = verdict
    summary["verdict_reasons"] = reasons

    args.output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = args.output_dir / "trades.csv"
    json_path = args.output_dir / "summary.json"
    report_path = args.output_dir / "report.md"
    fieldnames = list(rows[0])
    with csv_path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    json_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report_path.write_text(render_report(summary), encoding="utf-8")
    print(json.dumps({"csv": str(csv_path), "json": str(json_path), "report": str(report_path), "verdict": verdict}, ensure_ascii=False))
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--paths-csv", type=Path, default=DEFAULT_PATHS)
    parser.add_argument("--replay-dir", type=Path, default=DEFAULT_REPLAY_DIR)
    parser.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    run(parser.parse_args())


if __name__ == "__main__":
    main()
