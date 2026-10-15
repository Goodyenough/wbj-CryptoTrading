"""Test a causal, real-time 1h reclaim candidate without future 4h filtering.

CRYPTOTRADIN-135 reuses frozen B watch plans and the latest completed 4h
eligibility frame.  It evaluates every first/second/third-hour reclaim, then
labels eventual 4h retention only after signal generation.  No network,
database, production, paper, shadow, or scheduler state is written.
"""
from __future__ import annotations

from collections import Counter, defaultdict
import csv
from datetime import datetime, timezone
import json
import math
from pathlib import Path
import subprocess
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from diagnose_momentum_resolution_stage_a import simulate_hourly_exit  # noqa: E402
from research_breakout_d6 import (  # noqa: E402
    FROZEN,
    REFERENCE,
    build_frames,
    load_arrays,
    read_json,
    save_json,
    sha256,
)
from short_horizon_core import (  # noqa: E402
    COSTS,
    DAY,
    H4,
    HOUR,
    Market,
    plan_decision,
    trade_metrics,
    valid_bar,
)


PROTOCOL = ROOT / "reports/2026-10-15/realtime_momentum_start_protocol_v1.md"
OUT = ROOT / "reports/2026-10-15/realtime_momentum_start_v1"
WINDOWS = (("early", "2024-07-01", "2025-06-01"), ("near", "2025-06-01", "2026-06-01"))
BRANCHES = (("taker", "stop_first"), ("stress", "stop_first"), ("taker", "target_first"))
COST_BY_NAME = {item.name: item for item in COSTS}
BOOTSTRAP_REPETITIONS = 2000
BOOTSTRAP_SEED = 20261015


def ms(value: str) -> int:
    return int(datetime.fromisoformat(value).replace(tzinfo=timezone.utc).timestamp() * 1000)


def event_key(row: dict) -> tuple[str, int, int]:
    return row["symbol"], int(row["signal_ms"]), int(row["plan_created_ms"])


def reclaim_after_hour(
    plan: dict,
    row: np.ndarray,
    cumulative_high: float,
    cumulative_low: float,
) -> tuple[bool, float, float]:
    """Apply the frozen price-only reclaim using only this completed hour."""
    if not valid_bar(row):
        raise ValueError("Invalid completed 1h bar")
    high = max(cumulative_high, float(row[2]))
    low = min(cumulative_low, float(row[3]))
    touches = high >= float(plan["entry_low"]) and low <= float(plan["entry_high"])
    triggered = bool(touches and float(row[4]) >= float(plan["entry_high"]))
    return triggered, high, low


def generate_rt1_candidates(
    frames: dict[int, dict],
    market: Market,
    start_ms: int,
    end_ms: int,
) -> tuple[list[dict], dict]:
    """Generate every causal RT1 event; never read the future 4h frame here."""
    watches: dict[str, dict] = {}
    events: list[dict] = []
    counts = Counter()

    for now in range(start_ms + H4, end_ms, H4):
        eligible = frames.get(now, {})

        # At the boundary, consume the previous completed 4h bar exactly as B.
        for symbol, plan in list(watches.items()):
            state = plan_decision(plan, market.row(symbol, "4h", now - H4), now, symbol in eligible)
            if state in {"expired", "invalidated", "signal"}:
                counts[f"4h_{state}"] += 1
                del watches[symbol]

        # New plans are created after boundary decisions and activate on later 1h closes.
        candidates = [
            (symbol, feature)
            for symbol, feature in eligible.items()
            if feature["candidate"] is not None and symbol not in watches
        ]
        for symbol, feature in sorted(candidates, key=lambda pair: (-pair[1]["qv"], pair[0])):
            watches[symbol] = dict(feature["candidate"], created_ms=now)
            counts["plans_created"] += 1

        cumulative: dict[str, tuple[float, float]] = {
            symbol: (-math.inf, math.inf) for symbol in watches if symbol in eligible
        }
        for offset in range(3):
            opened = now + offset * HOUR
            signal_ms = opened + HOUR
            for symbol in sorted(list(watches)):
                if symbol not in eligible:
                    continue
                row = market.row(symbol, "1h", opened)
                if row is None or not valid_bar(row):
                    counts["missing_or_invalid_signal_hour"] += 1
                    continue
                prior_high, prior_low = cumulative.get(symbol, (-math.inf, math.inf))
                triggered, high, low = reclaim_after_hour(watches[symbol], row, prior_high, prior_low)
                cumulative[symbol] = (high, low)
                counts["hourly_evaluations"] += 1
                if not triggered:
                    continue
                plan = watches.pop(symbol)
                entry_row = market.row(symbol, "1h", signal_ms)
                entry_available = bool(
                    entry_row is not None and valid_bar(entry_row) and float(entry_row[1]) > 0
                )
                event = {
                    "symbol": symbol,
                    "signal_ms": signal_ms,
                    "knowledge_cutoff_ms": signal_ms,
                    "entry_ms": signal_ms,
                    "entry_available": entry_available,
                    "raw_entry": float(entry_row[1]) if entry_available else None,
                    "plan_created_ms": int(plan["created_ms"]),
                    "trigger_interval_ms": now,
                    "hour_offset": offset + 1,
                    "entry_low": float(plan["entry_low"]),
                    "entry_high": float(plan["entry_high"]),
                    "original_stop": float(plan["original_stop"]),
                    "regime": eligible[symbol]["regime"],
                    "crash": bool(eligible[symbol]["crash"]),
                    "quote_volume": float(eligible[symbol]["qv"]),
                }
                if max(int(plan["created_ms"]), now, int(row[0] + HOUR)) > signal_ms:
                    raise AssertionError(f"Future information in RT1 event: {event_key(event)}")
                events.append(event)
                counts["rt1_candidates"] += 1
                counts[f"hour_offset_{offset + 1}"] += 1
                counts["entry_available"] += int(entry_available)

    counts["watches_at_end"] = len(watches)
    counts["causal_violations"] = sum(
        row["knowledge_cutoff_ms"] != row["signal_ms"]
        or row["plan_created_ms"] >= row["signal_ms"]
        for row in events
    )
    return events, dict(counts)


def add_post_signal_labels(
    events: list[dict],
    frames: dict[int, dict],
    market: Market,
    end_ms: int,
) -> dict:
    """Verify paths and add future labels only after the causal event set is frozen."""
    verified = 0
    retention_known = 0
    retained = 0
    for event in events:
        symbol = event["symbol"]
        opened = int(event["trigger_interval_ms"])
        parent = market.row(symbol, "4h", opened)
        hours = [market.row(symbol, "1h", opened + j * HOUR) for j in range(4)]
        if parent is None or any(row is None or not valid_bar(row) for row in hours):
            event["interval_verified"] = False
        else:
            aggregate = np.asarray([
                hours[0][1],
                max(row[2] for row in hours),
                min(row[3] for row in hours),
                hours[-1][4],
            ])
            event["interval_verified"] = bool(
                valid_bar(parent) and np.allclose(aggregate, parent[1:5], rtol=1e-8, atol=1e-12)
            )
        verified += int(event["interval_verified"])

        boundary = opened + H4
        if boundary < end_ms and boundary in frames and parent is not None:
            eligible = frames[boundary]
            plan = {
                "created_ms": event["plan_created_ms"],
                "entry_low": event["entry_low"],
                "entry_high": event["entry_high"],
                "original_stop": event["original_stop"],
            }
            event["retained_4h_confirmation"] = (
                plan_decision(plan, parent, boundary, symbol in eligible) == "signal"
            )
            retention_known += 1
            retained += int(event["retained_4h_confirmation"])
        else:
            event["retained_4h_confirmation"] = None
    return {
        "candidate_intervals_verified": verified,
        "candidate_intervals_total": len(events),
        "retention_known": retention_known,
        "retained": retained,
        "retained_pct": 100 * retained / retention_known if retention_known else None,
    }


def simulate_branch(
    events: list[dict],
    arrays: dict,
    end_ms: int,
    cost_name: str,
    tie_break: str,
) -> tuple[list[dict], int]:
    rows = []
    canceled = 0
    costs = COST_BY_NAME[cost_name]
    for event in events:
        if not event["entry_available"]:
            canceled += 1
            continue
        trade = simulate_hourly_exit(
            arrays[event["symbol"]]["1h"],
            event["symbol"],
            int(event["entry_ms"]),
            end_ms,
            costs,
            tie_break,
        )
        trade.update(event)
        trade.update(cost=cost_name, tie_break=tie_break)
        rows.append(trade)
    return rows, canceled


def symbol_only(rows: list[dict]) -> tuple[list[dict], int]:
    active_until: dict[str, int] = {}
    accepted = []
    blocked = 0
    for row in sorted(rows, key=lambda item: (item["entry_ms"], item["symbol"], item["plan_created_ms"])):
        if int(row["entry_ms"]) < active_until.get(row["symbol"], -1):
            blocked += 1
            continue
        accepted.append(row)
        active_until[row["symbol"]] = int(row["exit_ms"]) if row["closed"] else 2**63 - 1
    return accepted, blocked


def absolute_bootstrap(rows: list[dict], start_ms: int, end_ms: int) -> dict:
    days = max(1, (end_ms - start_ms) // DAY)
    data = np.zeros((days, 2), dtype=float)
    for row in rows:
        if not row["closed"]:
            continue
        index = min(days - 1, max(0, (int(row["entry_ms"]) - start_ms) // DAY))
        data[index, 0] += float(row["net_return_pct"])
        data[index, 1] += 1
    block_days = 14
    blocks = math.ceil(days / block_days)
    rng = np.random.default_rng(BOOTSTRAP_SEED)
    begins = rng.integers(0, max(1, days - block_days + 1), size=(BOOTSTRAP_REPETITIONS, blocks))
    indices = (begins[:, :, None] + np.arange(min(block_days, days))).reshape(BOOTSTRAP_REPETITIONS, -1)[:, :days]
    samples = data[indices].sum(axis=1)
    usable = samples[:, 1] > 0
    means = samples[usable, 0] / samples[usable, 1]
    return {
        "block_days": block_days,
        "repetitions": BOOTSTRAP_REPETITIONS,
        "valid_resamples": int(usable.sum()),
        "mean_net_pct_ci": np.quantile(means, [0.025, 0.975]).tolist() if len(means) else None,
    }


def leave_one_out(rows: list[dict], dimension: str) -> dict:
    closed = [row for row in rows if row["closed"]]

    def label(row: dict) -> str:
        if dimension == "symbol":
            return row["symbol"]
        return datetime.fromtimestamp(row["entry_ms"] / 1000, timezone.utc).strftime("%G-W%V")

    labels = sorted({label(row) for row in closed})
    values = []
    for removed in labels:
        kept = [float(row["net_return_pct"]) for row in closed if label(row) != removed]
        if kept:
            values.append({"removed": removed, "mean_net_pct": float(np.mean(kept)), "trades": len(kept)})
    return {
        "dimension": dimension,
        "groups": len(values),
        "min_mean_net_pct": min((item["mean_net_pct"] for item in values), default=None),
        "max_mean_net_pct": max((item["mean_net_pct"] for item in values), default=None),
        "worst_removed": min(values, key=lambda item: item["mean_net_pct"]) if values else None,
    }


def grouped_summary(rows: list[dict], field: str) -> dict:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        value = row.get(field)
        label = "unknown" if value is None else str(value).lower() if isinstance(value, bool) else str(value)
        grouped[label].append(row)
    return {label: trade_metrics(items) for label, items in sorted(grouped.items())}


def weekend_label(row: dict) -> str:
    weekday = datetime.fromtimestamp(row["entry_ms"] / 1000, timezone.utc).weekday()
    return "weekend" if weekday >= 5 else "weekday"


def window_summary(
    events: list[dict],
    generation: dict,
    labels: dict,
    arrays: dict,
    start_ms: int,
    end_ms: int,
    start: str,
) -> tuple[dict, list[dict]]:
    branches = {}
    csv_rows = []
    for cost_name, tie_break in BRANCHES:
        name = f"{cost_name}_{tie_break}"
        rows, canceled = simulate_branch(events, arrays, end_ms, cost_name, tie_break)
        symbol_rows, blocked = symbol_only(rows)
        symbol_keys = {event_key(item) for item in symbol_rows}
        reference = read_json(REFERENCE / f"{start}_{cost_name}_{tie_break}_all_events_trades.json.gz")["B"]
        primary_metrics = trade_metrics(rows)
        symbol_metrics = trade_metrics(symbol_rows)
        for row in rows:
            row["symbol_only_accepted"] = event_key(row) in symbol_keys
            csv_rows.append(row)
        branch = {
            "all_events": primary_metrics,
            "symbol_only": symbol_metrics,
            "reference_4h_b": trade_metrics(reference),
            "bootstrap": absolute_bootstrap(rows, start_ms, end_ms),
            "leave_one_symbol": leave_one_out(rows, "symbol"),
            "leave_one_week": leave_one_out(rows, "week"),
            "entry_canceled": canceled,
            "symbol_only_blocked": blocked,
        }
        if name == "taker_stop_first":
            branch["by_retained_4h_confirmation"] = grouped_summary(rows, "retained_4h_confirmation")
            branch["by_regime"] = grouped_summary(rows, "regime")
            weekend_groups: dict[str, list[dict]] = defaultdict(list)
            for row in rows:
                weekend_groups[weekend_label(row)].append(row)
            branch["by_weekend"] = {
                label: trade_metrics(items) for label, items in sorted(weekend_groups.items())
            }
        branches[name] = branch

    return {
        "generation": generation,
        "post_signal_labels": labels,
        "candidate_density": {
            "events": len(events),
            "symbols": len({row["symbol"] for row in events}),
            "signal_weeks": len({
                datetime.fromtimestamp(row["signal_ms"] / 1000, timezone.utc).strftime("%G-W%V")
                for row in events
            }),
            "events_per_30d": 30 * len(events) / ((end_ms - start_ms) / DAY),
            "hour_offsets": dict(Counter(str(row["hour_offset"]) for row in events)),
        },
        "branches": branches,
    }, csv_rows


def decide(summary: dict) -> tuple[str, list[str]]:
    windows = [summary["windows"][name] for name in ("early", "near")]
    measurement_ok = all(window["measurement"]["passed"] for window in windows)
    if not measurement_ok:
        return "measurement_insufficient", ["至少一个窗口未通过因果时点、1h/4h聚合、成交覆盖或删失闸门。"]

    main = [window["branches"]["taker_stop_first"] for window in windows]
    stress = [window["branches"]["stress_stop_first"] for window in windows]
    target = [window["branches"]["taker_target_first"] for window in windows]
    sample_ok = all(
        item["all_events"]["closed_trades"] >= 30 and item["all_events"]["signal_weeks"] >= 20
        for item in main
    )
    main_positive = all(item["all_events"]["mean_net_pct"] > 0 and item["all_events"]["profit_factor"] > 1 for item in main)
    ci_positive = all(item["bootstrap"]["mean_net_pct_ci"][0] >= 0 for item in main)
    stress_positive = all(item["all_events"]["mean_net_pct"] > 0 for item in stress)
    symbol_positive = all(item["symbol_only"]["mean_net_pct"] > 0 for item in main)
    target_positive = all(item["all_events"]["mean_net_pct"] > 0 for item in target)
    loo_positive = all(
        item["leave_one_symbol"]["min_mean_net_pct"] > 0
        and item["leave_one_week"]["min_mean_net_pct"] > 0
        for item in main
    )
    summary["qualification_checks"] = {
        "sample_sufficient_both": sample_ok,
        "taker_positive_pf_gt_1_both": main_positive,
        "bootstrap_lower_nonnegative_both": ci_positive,
        "stress_positive_both": stress_positive,
        "symbol_only_positive_both": symbol_positive,
        "target_first_positive_both": target_positive,
        "leave_one_out_positive_both": loo_positive,
    }
    if all(summary["qualification_checks"].values()):
        return "realtime_signal_supported_for_new_validation", [
            "唯一RT1实时候选在双窗、压力成本、同币不重叠、区块区间和集中度闸门下均保持正值。"
        ]

    both_nonpositive = all(item["all_events"]["mean_net_pct"] <= 0 for item in main)
    any_ci_upper_nonpositive = any(item["bootstrap"]["mean_net_pct_ci"][1] <= 0 for item in main)
    if both_nonpositive or any_ci_upper_nonpositive:
        return "reject_current_realtime_reclaim", [
            "完整实时候选集在双窗均未形成正主口径净期望，或至少一窗区块区间已排除正均值。"
        ]
    return "retest_or_insufficient", [
        "完整实时候选集出现窗口、成本、区间或集中度不一致；不能支持当前RT1，也不足以否定所有1h信号。"
    ]


def render_report(summary: dict) -> str:
    def number(value, digits=3) -> str:
        return "—" if value is None else f"{value:.{digits}f}"

    lines = [
        "# 实时1h动能启动候选：全样本因果验证",
        "",
        f"Taskboard：`CRYPTOTRADIN-135`。裁决：`{summary['decision']}`。",
        "",
        "## 白话结论",
        "",
        summary["plain_language"],
        "",
        "> RT1信号生成没有使用未来4h确认；`retained_4h_confirmation`只在事件集合冻结后添加，用来解释假突破。",
        "",
        "## 候选与4h保持率",
        "",
        "| 窗口 | RT1候选 | 币数 | 信号周 | 每30日 | 1h/2h/3h | 保持到4h确认 |",
        "|---|---:|---:|---:|---:|---|---:|",
    ]
    for window, label in (("early", "早窗"), ("near", "近窗")):
        item = summary["windows"][window]
        density = item["candidate_density"]
        offsets = density["hour_offsets"]
        labels = item["post_signal_labels"]
        lines.append(
            f"| {label} | {density['events']} | {density['symbols']} | {density['signal_weeks']} | "
            f"{density['events_per_30d']:.1f} | {offsets.get('1', 0)}/{offsets.get('2', 0)}/{offsets.get('3', 0)} | "
            f"{labels['retained']}/{labels['retention_known']} ({labels['retained_pct']:.2f}%) |"
        )

    lines.extend([
        "",
        "## 主结果：fixed +5%/-3%/48h",
        "",
        "| 窗口 | 分支/层次 | closed | mean net% | 95%区间 | 胜率 | PF | TP/SL/TIME |",
        "|---|---|---:|---:|---|---:|---:|---|",
    ])
    for window, label in (("early", "早窗"), ("near", "近窗")):
        item = summary["windows"][window]
        for branch_name, branch_label in (
            ("taker_stop_first", "taker/all"),
            ("stress_stop_first", "stress/all"),
            ("taker_target_first", "target-first/all"),
        ):
            branch = item["branches"][branch_name]
            metric = branch["all_events"]
            counts = metric["status_counts"]
            ci = branch["bootstrap"]["mean_net_pct_ci"]
            lines.append(
                f"| {label} | {branch_label} | {metric['closed_trades']} | {metric['mean_net_pct']:.4f}% | "
                f"[{ci[0]:.4f}, {ci[1]:.4f}] | {metric['win_rate_pct']:.2f}% | {metric['profit_factor']:.3f} | "
                f"{counts.get('TP', 0)}/{counts.get('SL', 0)}/{counts.get('TIME', 0)} |"
            )
        branch = item["branches"]["taker_stop_first"]
        metric = branch["symbol_only"]
        counts = metric["status_counts"]
        lines.append(
            f"| {label} | taker/symbol-only | {metric['closed_trades']} | {metric['mean_net_pct']:.4f}% | — | "
            f"{metric['win_rate_pct']:.2f}% | {metric['profit_factor']:.3f} | "
            f"{counts.get('TP', 0)}/{counts.get('SL', 0)}/{counts.get('TIME', 0)} |"
        )

    lines.extend([
        "",
        "## 假突破归因（taker / stop-first）",
        "",
        "| 窗口 | 事后4h标签 | closed | mean net% | 胜率 | PF |",
        "|---|---|---:|---:|---:|---:|",
    ])
    for window, label in (("early", "早窗"), ("near", "近窗")):
        groups = summary["windows"][window]["branches"]["taker_stop_first"]["by_retained_4h_confirmation"]
        for group in ("true", "false", "unknown"):
            if group not in groups:
                continue
            metric = groups[group]
            lines.append(
                f"| {label} | {group} | {metric['closed_trades']} | {metric['mean_net_pct']:.4f}% | "
                f"{number(metric['win_rate_pct'], 2)}% | {number(metric['profit_factor'])} |"
            )

    lines.extend(["", "## 裁决", ""])
    lines.extend(f"- {reason}" for reason in summary["decision_reasons"])
    lines.extend([
        "",
        "## 资格检查",
        "",
    ])
    lines.extend(f"- `{key}`：`{value}`" for key, value in summary.get("qualification_checks", {}).items())
    lines.extend([
        "",
        "## 边界",
        "",
        "- 两个窗口已烧且币池带current-survivor偏差；即使通过也只能进入新数据/前向shadow验证。",
        "- all-events允许假想持仓重叠，只回答信号质量；symbol-only仅限制同币重叠，不是完整账户回测。",
        "- 未扫描任何1h、ATR、成交量、regime或退出参数；未运行15分钟。",
        "- 生产、paper、shadow、采集调度和默认配置均未修改。",
    ])
    return "\n".join(lines) + "\n"


def write_trades(rows: list[dict]) -> None:
    fields = [
        "window", "cost", "tie_break", "symbol", "signal_ms", "knowledge_cutoff_ms", "entry_ms",
        "plan_created_ms", "trigger_interval_ms", "hour_offset", "entry_low", "entry_high", "original_stop",
        "regime", "crash", "quote_volume", "retained_4h_confirmation", "interval_verified",
        "symbol_only_accepted", "status", "closed", "exit_ms", "raw_entry", "entry_price", "stop", "target",
        "raw_exit", "exit_price", "net_return_pct", "raw_return_pct", "fee_pct", "slippage_pct",
        "duration_hours", "exit_time_exact", "ambiguous",
    ]
    with (OUT / "trades.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    windows = {}
    all_csv = []
    input_hashes = {}
    for window, start, end in WINDOWS:
        meta_path = FROZEN / f"{start}_inputs.json"
        meta = read_json(meta_path)
        arrays = load_arrays(meta)
        frames, _event_map, frame_checks = build_frames(start, arrays)
        market = Market(arrays)
        start_ms, end_ms = ms(start), ms(end)
        events, generation = generate_rt1_candidates(frames, market, start_ms, end_ms)
        labels = add_post_signal_labels(events, frames, market, end_ms)
        result, csv_rows = window_summary(events, generation, labels, arrays, start_ms, end_ms, start)
        result["frame_checks"] = frame_checks
        main_metrics = result["branches"]["taker_stop_first"]["all_events"]
        canceled = result["branches"]["taker_stop_first"]["entry_canceled"]
        censored_pct = 100 * main_metrics["censored"] / max(1, main_metrics["trades"])
        measurement_reasons = []
        if generation.get("causal_violations", 0):
            measurement_reasons.append("causal_violations")
        if generation.get("missing_or_invalid_signal_hour", 0):
            measurement_reasons.append("missing_or_invalid_signal_hour")
        if labels["candidate_intervals_verified"] != labels["candidate_intervals_total"]:
            measurement_reasons.append("candidate_interval_aggregation")
        if 100 * canceled / max(1, len(events)) > 1:
            measurement_reasons.append("entry_canceled_gt_1pct")
        if censored_pct > 1:
            measurement_reasons.append("censored_gt_1pct")
        result["measurement"] = {
            "passed": not measurement_reasons,
            "reasons": measurement_reasons,
            "entry_canceled": canceled,
            "censored_pct": censored_pct,
        }
        for row in csv_rows:
            row["window"] = window
        all_csv.extend(csv_rows)
        windows[window] = result
        input_hashes[str(meta_path.relative_to(ROOT))] = sha256(meta_path)
        archive = ROOT / meta["archive"]
        input_hashes[str(archive.relative_to(ROOT))] = sha256(archive)
        feature_path = FROZEN / f"{start}_features.json.gz"
        input_hashes[str(feature_path.relative_to(ROOT))] = sha256(feature_path)

    summary = {
        "task": "CRYPTOTRADIN-135",
        "protocol": str(PROTOCOL.relative_to(ROOT)),
        "windows": windows,
    }
    decision, reasons = decide(summary)
    summary["decision"] = decision
    summary["decision_reasons"] = reasons
    if decision == "realtime_signal_supported_for_new_validation":
        summary["plain_language"] = "只用当时已完成的1h与4h信息，RT1在完整候选集、压力成本和简单同币不重叠约束下仍保持正收益；它只获得进入未使用数据或前向shadow验证的资格，尚不能上线。"
    elif decision == "reject_current_realtime_reclaim":
        summary["plain_language"] = "把所有实时可见的早期reclaim都纳入后，当前RT1定义不能形成稳定正净收益。阶段A看起来更好，主要来自先知道哪些事件最终会获得4h确认；这个具体实时定义应否定。"
    elif decision == "retest_or_insufficient":
        summary["plain_language"] = "RT1没有形成跨窗口、成本和集中度一致的证据。当前定义不能升级，但结果也不足以否定所有1h动能启动信号。"
    else:
        summary["plain_language"] = "因果时点、数据聚合、成交覆盖或删失未通过，当前结果不能用于判断实时动能信号。"

    save_json(OUT / "summary.json", summary)
    write_trades(all_csv)
    (OUT / "report.md").write_text(render_report(summary), encoding="utf-8")
    sources = [
        PROTOCOL,
        ROOT / "scripts/research_realtime_momentum_start.py",
        ROOT / "scripts/diagnose_momentum_resolution_stage_a.py",
        ROOT / "scripts/research_breakout_d6.py",
        ROOT / "scripts/short_horizon_core.py",
    ]
    manifest = {
        "completed_utc": datetime.now(timezone.utc).isoformat(),
        "head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "source_sha256": {str(path.relative_to(ROOT)): sha256(path) for path in sources},
        "input_sha256": input_hashes,
        "outputs": {},
    }
    for name in ("summary.json", "trades.csv", "report.md"):
        manifest["outputs"][name] = sha256(OUT / name)
    save_json(OUT / "run_manifest.json", manifest)
    (OUT / "verification.md").write_text(
        "# Verification\n\n"
        f"- Decision: `{decision}`.\n"
        f"- Early candidates: `{windows['early']['candidate_density']['events']}`; near candidates: `{windows['near']['candidate_density']['events']}`.\n"
        f"- Causal violations: early `{windows['early']['generation'].get('causal_violations', 0)}`, near `{windows['near']['generation'].get('causal_violations', 0)}`.\n"
        f"- Candidate 1h/4h aggregation: early `{windows['early']['post_signal_labels']['candidate_intervals_verified']}/{windows['early']['post_signal_labels']['candidate_intervals_total']}`, near `{windows['near']['post_signal_labels']['candidate_intervals_verified']}/{windows['near']['post_signal_labels']['candidate_intervals_total']}`.\n"
        "- Event generation never reads retained_4h_confirmation; future retention is added only after the event list is frozen.\n"
        "- No network or database writes; no production, paper, shadow, schedule, or configuration changes.\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "decision": decision,
        "qualification": summary.get("qualification_checks"),
        "windows": {
            name: {
                "candidates": value["candidate_density"]["events"],
                "retained_pct": value["post_signal_labels"]["retained_pct"],
                "measurement": value["measurement"],
                "taker": value["branches"]["taker_stop_first"]["all_events"],
                "stress": value["branches"]["stress_stop_first"]["all_events"],
            }
            for name, value in windows.items()
        },
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
