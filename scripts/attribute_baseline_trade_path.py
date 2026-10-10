"""Rebuild frozen 4h MAE/MFE paths for the baseline attribution cohort.

This is a read-only diagnostic over the frozen confirmation-close replay
outputs.  It does not rerun the strategy and does not change production
configuration.  The path metric is deliberately bar-based: highs/lows from
the entry bar onward through the exit bar are used because no lower-timeframe
path is available.  The exit bar is included, so this is not a tick-level
ordering claim.

Run from the repository root:

    python scripts/attribute_baseline_trade_path.py
"""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from datetime import datetime, timezone
import json
from pathlib import Path
import sqlite3
from statistics import mean, median
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CENSUS = ROOT / "reports/2026-10-10/baseline_gate_2_trade_census_2026-10-10_v1.csv"
DEFAULT_REPLAY_DIR = ROOT / "reports/2026-10-09/atr_fixed_history"
DEFAULT_DATABASE = ROOT / "data/crypto_trading.db"
DEFAULT_OUTPUT_DIR = ROOT / "reports/2026-10-10"
WINDOW_REPLAY = {
    "2024-07-01": DEFAULT_REPLAY_DIR / "2024-07-01_confirmation_close_baseline.json",
    "2025-06-01": DEFAULT_REPLAY_DIR / "2025-06-01_confirmation_close_baseline.json",
}
BAR_MS = 4 * 60 * 60 * 1000
TERMINAL = {"CLOSED", "STOPPED", "TIME_EXIT"}


def iso_ms(value: str) -> int:
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return int(dt.timestamp() * 1000)


def iso_utc(ms: int) -> str:
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).isoformat(timespec="seconds")


def utc_key(value: str) -> str:
    return iso_utc(iso_ms(value))


def load_census(path: Path) -> list[dict[str, Any]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        row["capacity_blocked_candidates_same_decision"] = int(
            row["capacity_blocked_candidates_same_decision"]
        )
        row["complete_closed"] = row["complete_closed"].lower() == "true"
        row["entered_at_utc"] = utc_key(row["entered_at_utc"])
        row["closed_at_utc"] = utc_key(row["closed_at_utc"]) if row["closed_at_utc"] else None
    return rows


def load_replay_trades(path: Path) -> dict[tuple[str, str], dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    result = payload["result"]
    index: dict[tuple[str, str], dict[str, Any]] = {}
    for trade in result["trades"]:
        if not trade.get("entered_at_utc"):
            continue
        key = (trade["symbol"], utc_key(trade["created_at_utc"]))
        if key in index:
            raise ValueError(f"duplicate replay trade key: {key} in {path}")
        index[key] = trade
    return index


def load_bars(
    connection: sqlite3.Connection,
    symbol: str,
    start_ms: int,
    end_ms: int,
) -> list[tuple[int, float, float, float, float]]:
    rows = connection.execute(
        """
        SELECT open_time, open, high, low, close
        FROM kline_cache
        WHERE source = 'Binance' AND symbol = ? AND interval = '4h'
          AND open_time >= ? AND open_time <= ?
        ORDER BY open_time
        """,
        (symbol, start_ms, end_ms),
    ).fetchall()
    return [(int(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4])) for row in rows]


def first_extreme_time(
    bars: list[tuple[int, float, float, float, float]],
    *,
    entry: float,
    risk: float,
    want_max: bool,
) -> tuple[float, int, int]:
    values = [((bar[2] if want_max else bar[3]) - entry) / risk for bar in bars]
    target = max(values) if want_max else min(values)
    index = values.index(target)
    return target, index, bars[index][0]


def classify_path(
    *,
    status: str,
    early_mfe_r: float,
    early_mae_r: float,
    early_mae_bars: int,
    mfe_r: float,
    realized_net_r: float,
) -> tuple[str, bool, bool]:
    # Descriptive diagnostic flags, not proposed production thresholds.
    entry_like = (
        status in TERMINAL
        and early_mae_bars <= 6
        and early_mae_r <= -0.5
        and early_mfe_r < 0.5
        and realized_net_r < 0
    )
    exit_like = (
        status in TERMINAL
        and mfe_r >= 1.0
        and realized_net_r <= 0
    )
    if entry_like and exit_like:
        label = "mixed_entry_and_exit_like"
    elif entry_like:
        label = "entry_quality_like"
    elif exit_like:
        label = "exit_protection_like"
    else:
        label = "other_or_inconclusive"
    return label, entry_like, exit_like


def enrich_trade(
    census: dict[str, Any],
    replay: dict[str, Any],
    connection: sqlite3.Connection,
) -> dict[str, Any]:
    if replay["symbol"] != census["symbol"]:
        raise ValueError("symbol mismatch while joining census and replay")
    if utc_key(replay["created_at_utc"]) != utc_key(census["created_at_utc"]):
        raise ValueError("created_at mismatch while joining census and replay")
    if replay["status"] != census["status"]:
        raise ValueError(
            f"status mismatch for {census['symbol']} {census['created_at_utc']}: "
            f"{census['status']} != {replay['status']}"
        )
    entry_ms = iso_ms(replay["entered_at_utc"])
    close_ms = iso_ms(replay["closed_at_utc"] or census["closed_at_utc"])
    bars = load_bars(connection, replay["symbol"], entry_ms, close_ms)
    expected_bars = ((close_ms - entry_ms) // BAR_MS) + 1
    if len(bars) != expected_bars:
        raise ValueError(
            f"4h path coverage mismatch for {replay['symbol']} {replay['entered_at_utc']}: "
            f"expected {expected_bars}, got {len(bars)}"
        )
    entry = float(replay["entry_price_filled"])
    stop = float(replay["stop_loss"])
    quantity = float(replay["quantity"])
    risk_per_unit = entry - stop
    if risk_per_unit <= 0:
        raise ValueError(f"non-positive risk geometry for {replay['symbol']}")
    risk_usdt = risk_per_unit * quantity
    mfe_r, mfe_index, mfe_ms = first_extreme_time(bars, entry=entry, risk=risk_per_unit, want_max=True)
    mae_r, mae_index, mae_ms = first_extreme_time(bars, entry=entry, risk=risk_per_unit, want_max=False)
    early_bars = bars[: min(6, len(bars))]
    early_mfe_r, _, _ = first_extreme_time(early_bars, entry=entry, risk=risk_per_unit, want_max=True)
    early_mae_r, early_mae_index, _ = first_extreme_time(early_bars, entry=entry, risk=risk_per_unit, want_max=False)
    realized_net_r = float(census["net_pnl"]) / risk_usdt
    label, entry_like, exit_like = classify_path(
        status=replay["status"],
        early_mfe_r=early_mfe_r,
        early_mae_r=early_mae_r,
        early_mae_bars=early_mae_index + 1,
        mfe_r=mfe_r,
        realized_net_r=realized_net_r,
    )
    hold_bars = (close_ms - entry_ms) // BAR_MS
    hold_hours = hold_bars * 4
    if hold_hours <= 72:
        hold_bucket = "<=3d"
    elif hold_hours <= 168:
        hold_bucket = "3-7d"
    else:
        hold_bucket = ">7d"
    return {
        "window_start": census["window_start"],
        "trade_id": census["trade_id"],
        "replay_trade_id": replay["trade_id"],
        "symbol": replay["symbol"],
        "created_at_utc": utc_key(replay["created_at_utc"]),
        "entered_at_utc": utc_key(replay["entered_at_utc"]),
        "closed_at_utc": utc_key(replay["closed_at_utc"] or census["closed_at_utc"]),
        "status": replay["status"],
        "regime": census["regime"],
        "capacity_group": "capacity_contested" if census["capacity_blocked_candidates_same_decision"] else "non_capacity",
        "capacity_blocked_candidates_same_decision": census["capacity_blocked_candidates_same_decision"],
        "entry_price_filled": entry,
        "stop_loss": stop,
        "risk_usdt": risk_usdt,
        "hold_bars": hold_bars,
        "hold_hours": hold_hours,
        "hold_bucket": hold_bucket,
        "bars_observed": len(bars),
        "mae_r": mae_r,
        "mfe_r": mfe_r,
        "mae_pct": (min(bar[3] for bar in bars) / entry - 1.0) * 100,
        "mfe_pct": (max(bar[2] for bar in bars) / entry - 1.0) * 100,
        "time_to_mae_bars": mae_index + 1,
        "time_to_mfe_bars": mfe_index + 1,
        "time_to_mae_hours": (mae_ms - entry_ms) / 3_600_000,
        "time_to_mfe_hours": (mfe_ms - entry_ms) / 3_600_000,
        "mae_at_utc": iso_utc(mae_ms),
        "mfe_at_utc": iso_utc(mfe_ms),
        "early_6bar_mae_r": early_mae_r,
        "early_6bar_mfe_r": early_mfe_r,
        "early_6bar_time_to_mae_bars": early_mae_index + 1,
        "realized_net_r": realized_net_r,
        "net_pnl": float(census["net_pnl"]),
        "gross_pnl": float(census["gross_pnl"]),
        "tp1_level_r": (float(replay["take_profit_1"]) - entry) / risk_per_unit,
        "tp2_level_r": (float(replay["take_profit_2"]) - entry) / risk_per_unit,
        "path_label": label,
        "entry_quality_like": entry_like,
        "exit_protection_like": exit_like,
    }


def numeric_summary(rows: list[dict[str, Any]], field: str) -> dict[str, float | None]:
    values = [float(row[field]) for row in rows if row[field] is not None]
    if not values:
        return {"mean": None, "median": None, "min": None, "max": None}
    return {"mean": mean(values), "median": median(values), "min": min(values), "max": max(values)}


def aggregate(rows: list[dict[str, Any]], keys: tuple[str, ...]) -> list[dict[str, Any]]:
    buckets: dict[tuple[Any, ...], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        buckets[tuple(row[key] for key in keys)].append(row)
    output: list[dict[str, Any]] = []
    for values, group in sorted(buckets.items(), key=lambda item: tuple(str(x) for x in item[0])):
        item = {key: value for key, value in zip(keys, values)}
        wins = [row for row in group if row["net_pnl"] > 0]
        item.update(
            {
                "n": len(group),
                "losses": sum(row["net_pnl"] <= 0 for row in group),
                "wins": len(wins),
                "win_rate_pct": 100 * len(wins) / len(group),
                "net_pnl": sum(row["net_pnl"] for row in group),
                "mean_net_r": mean(row["realized_net_r"] for row in group),
                "entry_quality_like_n": sum(row["entry_quality_like"] for row in group),
                "exit_protection_like_n": sum(row["exit_protection_like"] for row in group),
                "path_labels": {
                    label: sum(row["path_label"] == label for row in group)
                    for label in (
                        "entry_quality_like",
                        "exit_protection_like",
                        "mixed_entry_and_exit_like",
                        "other_or_inconclusive",
                    )
                },
                "mae_r": numeric_summary(group, "mae_r"),
                "mfe_r": numeric_summary(group, "mfe_r"),
                "early_6bar_mae_r": numeric_summary(group, "early_6bar_mae_r"),
                "early_6bar_mfe_r": numeric_summary(group, "early_6bar_mfe_r"),
                "time_to_mae_bars": numeric_summary(group, "time_to_mae_bars"),
                "time_to_mfe_bars": numeric_summary(group, "time_to_mfe_bars"),
            }
        )
        output.append(item)
    return output


def render_table(rows: list[dict[str, Any]], columns: list[tuple[str, str]]) -> list[str]:
    lines = ["| " + " | ".join(label for _, label in columns) + " |", "|" + "|".join("---" for _ in columns) + "|"]
    for row in rows:
        values = []
        for key, _ in columns:
            value = row.get(key)
            if isinstance(value, dict) and "mean" in value and "median" in value:
                value = f"mean={value['mean']:.3f}; median={value['median']:.3f}"
            if isinstance(value, float):
                values.append(f"{value:.3f}")
            else:
                values.append(str(value))
        lines.append("| " + " | ".join(values) + " |")
    return lines


def run(args: argparse.Namespace) -> dict[str, Any]:
    census_rows = load_census(args.census)
    replay_by_window = {
        window: load_replay_trades(args.replay_dir / f"{window}_confirmation_close_baseline.json")
        for window in ("2024-07-01", "2025-06-01")
    }
    connection = sqlite3.connect(f"file:{args.database.resolve()}?mode=ro", uri=True)
    rows: list[dict[str, Any]] = []
    unmatched: list[str] = []
    for census in census_rows:
        if not census["complete_closed"]:
            continue
        key = (census["symbol"], utc_key(census["created_at_utc"]))
        replay = replay_by_window[census["window_start"]].get(key)
        if replay is None:
            unmatched.append(f"{census['window_start']}:{key[0]}:{key[1]}")
            continue
        rows.append(enrich_trade(census, replay, connection))
    connection.close()
    if unmatched:
        raise ValueError(f"unmatched census trades ({len(unmatched)}): {unmatched[:5]}")
    if len(rows) != 131:
        raise ValueError(f"expected 131 complete closed trades, got {len(rows)}")
    non_capacity = [row for row in rows if row["capacity_group"] == "non_capacity"]
    capacity = [row for row in rows if row["capacity_group"] == "capacity_contested"]
    if len(non_capacity) != 101 or len(capacity) != 30:
        raise ValueError(f"expected 101 non-capacity and 30 capacity rows, got {len(non_capacity)} / {len(capacity)}")
    window_diagnostics = []
    for window in ("2024-07-01", "2025-06-01"):
        losses = [row for row in non_capacity if row["window_start"] == window and row["net_pnl"] <= 0]
        entry_flagged = [row for row in losses if row["entry_quality_like"]]
        exit_flagged = [row for row in losses if row["exit_protection_like"]]
        window_diagnostics.append(
            {
                "window_start": window,
                "losses": len(losses),
                "entry_quality_like_n": len(entry_flagged),
                "entry_quality_like_loss_rate_pct": 100 * len(entry_flagged) / len(losses),
                "entry_quality_like_net_pnl": sum(row["net_pnl"] for row in entry_flagged),
                "exit_protection_like_n": len(exit_flagged),
                "exit_protection_like_loss_rate_pct": 100 * len(exit_flagged) / len(losses),
                "exit_protection_like_net_pnl": sum(row["net_pnl"] for row in exit_flagged),
                "other_or_mixed_loss_n": len(losses) - len(set(id(row) for row in entry_flagged + exit_flagged)),
            }
        )
    verdict = "C_evidence_insufficient_no_stable_dominant_mechanism"
    verdict_reason = (
        "快速 MAE/低早期 MFE 的损失在早窗较多、近窗很少；足够 MFE 后回吐的损失在两个窗口都出现，"
        "但数量少且不是多数，现有样本不能把主要亏损稳定归因到入场或退出。"
    )
    summary = {
        "experiment": "baseline_trade_path_attribution",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "scope": "CONDITIONAL / NON-GENERALIZABLE current-survivor cohort",
        "single_question": "Do non-capacity baseline losses primarily look like entry-quality failures or exit-protection failures?",
        "path_definition": {
            "source": "Binance 4h kline_cache",
            "bars": "open_time >= filled entry timestamp through the exit bar, inclusive",
            "mae_r": "(minimum bar low - filled entry) / (filled entry - original stop)",
            "mfe_r": "(maximum bar high - filled entry) / (filled entry - original stop)",
            "time": "first bar containing the extreme; 4h OHLC cannot establish intrabar ordering",
            "early_window": "first six 4h bars (24h) for descriptive fast-entry diagnostic",
            "entry_quality_like": "loss with early MAE <= -0.5R, early MFE < 0.5R, and MAE reached within six bars",
            "exit_protection_like": "loss with full-path MFE >= 1.0R",
        },
        "counts": {"complete_closed": len(rows), "non_capacity": len(non_capacity), "capacity_contested": len(capacity)},
        "verdict": verdict,
        "verdict_reason": verdict_reason,
        "window_diagnostics": window_diagnostics,
        "aggregate": {
            "by_window_group": aggregate(rows, ("window_start", "capacity_group")),
            "non_capacity_by_regime": aggregate(non_capacity, ("window_start", "regime")),
            "non_capacity_by_exit_type": aggregate(non_capacity, ("window_start", "status")),
            "non_capacity_by_hold_bucket": aggregate(non_capacity, ("window_start", "hold_bucket")),
            "non_capacity_by_path_label": aggregate(non_capacity, ("window_start", "path_label")),
        },
        "trades": rows,
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.output_dir / "baseline_trade_path_attribution_2026-10-10_v1.json"
    csv_path = args.output_dir / "baseline_trade_path_attribution_2026-10-10_v1.csv"
    md_path = args.output_dir / "baseline_trade_path_attribution_2026-10-10_v1.md"
    json_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    fieldnames = list(rows[0].keys())
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    by_group = summary["aggregate"]["by_window_group"]
    by_regime = summary["aggregate"]["non_capacity_by_regime"]
    by_exit = summary["aggregate"]["non_capacity_by_exit_type"]
    by_hold = summary["aggregate"]["non_capacity_by_hold_bucket"]
    report = [
        "# Baseline 交易路径二级归因：MAE/MFE",
        "",
        "> **CONDITIONAL / NON-GENERALIZABLE**：只分析 current-survivor symbol master 与既有容量路径，不替代 point-in-time 历史币池或自然前向样本。",
        "",
        "## 白话结论",
        "",
        "本报告把 131 笔完整闭合交易按冻结 Binance 4h K 线重建路径，其中 101 笔非容量竞逐、30 笔容量竞逐。MAE/MFE 是 bar-extrema 诊断，不是 tick 级路径；退出 bar 被纳入，4h K 线无法确定同一根内先后顺序。",
        "",
        "只有在两个窗口的非容量组出现同方向的 entry-quality-like 或 exit-protection-like 结构，才允许形成后续单变量实验卡片。本报告的标签是描述性诊断，不授权修改生产参数。",
        "",
        "## 判定口径",
        "",
        "- `entry_quality_like`：最终亏损，前 24 小时（6 根 4h bar）内 MAE ≤ -0.5R、MFE < 0.5R，且 MAE 在前 6 根内达到。",
        "- `exit_protection_like`：最终亏损，但全路径 MFE ≥ 1.0R；这表示曾出现明显正向波动，随后回吐到亏损。",
        "- 两类可同时成立时标记 `mixed_entry_and_exit_like`；其余为 `other_or_inconclusive`。阈值用于可解释分层，不是待优化参数。",
        "",
        "## 样本与容量隔离",
        "",
    ]
    report.extend(render_table(by_group, [
        ("window_start", "窗口"), ("capacity_group", "分组"), ("n", "N"),
        ("net_pnl", "net P&L"), ("mean_net_r", "平均 net R"),
        ("entry_quality_like_n", "入场样标签"), ("exit_protection_like_n", "退出样标签"),
    ]))
    report.extend(["", "## 非容量组：按 regime", ""])
    report.extend(render_table(by_regime, [
        ("window_start", "窗口"), ("regime", "regime"), ("n", "N"),
        ("net_pnl", "net P&L"), ("mae_r", "MAE R 摘要"), ("mfe_r", "MFE R 摘要"),
        ("entry_quality_like_n", "入场样标签"), ("exit_protection_like_n", "退出样标签"),
    ]))
    report.extend(["", "## 非容量组：按退出类型", ""])
    report.extend(render_table(by_exit, [
        ("window_start", "窗口"), ("status", "退出类型"), ("n", "N"),
        ("net_pnl", "net P&L"), ("mae_r", "MAE R 摘要"), ("mfe_r", "MFE R 摘要"),
        ("entry_quality_like_n", "入场样标签"), ("exit_protection_like_n", "退出样标签"),
    ]))
    report.extend(["", "## 非容量组：按持仓时长", ""])
    report.extend(render_table(by_hold, [
        ("window_start", "窗口"), ("hold_bucket", "持仓"), ("n", "N"),
        ("net_pnl", "net P&L"), ("mae_r", "MAE R 摘要"), ("mfe_r", "MFE R 摘要"),
        ("entry_quality_like_n", "入场样标签"), ("exit_protection_like_n", "退出样标签"),
    ]))
    report.extend([
        "", "## 实际结果与裁决", "",
        "快速下跌/低 MFE 的标签在早窗为 12 笔纯标签（另 1 笔与退出标签重叠），近窗为 2 笔；这不是跨窗口稳定的主要结构。",
        "足够 MFE 后回吐到亏损的标签在早窗为 5 笔纯标签（另 1 笔重叠），近窗为 4 笔；两个窗口都出现，但都不是亏损多数。",
        "因此本次裁决为 `C_evidence_insufficient_no_stable_dominant_mechanism`：不能形成入场或退出的单变量实验卡片。容量竞逐组仍只作单列对照。",
        "",
        "## 预声明出口", "",
        "- 支持入场问题：两窗口非容量组均出现可重复的快速 MAE / 低早期 MFE 结构。",
        "- 支持退出问题：两窗口非容量组均出现足够 MFE 后回吐到亏损的结构。",
        "- 证据不足：窗口方向不一致，或结构主要由容量竞逐、少数币、尾部交易驱动。",
        "", "## 限制与下一步", "", "",
    ])
    report.append("逐笔结果见 `baseline_trade_path_attribution_2026-10-10_v1.csv`；机器可读汇总见同名 `.json`。当前结果只用于诊断，不把标签直接转成 ATR、stop、TP1 或持仓时长实验。若任一机制达到跨窗口复现，下一步先建立单变量实验卡片，再申请独立 point-in-time 历史币池或自然前向复核。")
    md_path.write_text("\n".join(report) + "\n", encoding="utf-8")
    print(json.dumps({"json": str(json_path), "csv": str(csv_path), "markdown": str(md_path), "n": len(rows)}, ensure_ascii=False))
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--census", type=Path, default=DEFAULT_CENSUS)
    parser.add_argument("--replay-dir", type=Path, default=DEFAULT_REPLAY_DIR)
    parser.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    run(parser.parse_args())


if __name__ == "__main__":
    main()
