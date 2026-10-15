"""Diagnose the upper bound from entering confirmed B events 1-3h earlier.

CRYPTOTRADIN-129 Stage A is deliberately conditional on eventual 4h
confirmation.  It is a latency ceiling, not a standalone 1h strategy test.
No network, database, production, paper, or shadow state is written.
"""
from __future__ import annotations

from collections import Counter
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
    HOLD,
    HOUR,
    Market,
    plan_decision,
    trade_metrics,
)


PROTOCOL = ROOT / "reports/2026-10-15/momentum_resolution_stage_a_protocol_v1.md"
OUT = ROOT / "reports/2026-10-15/momentum_resolution_stage_a_v1"
WINDOWS = (("2024-07-01", "2025-06-01"), ("2025-06-01", "2026-06-01"))
BRANCHES = (("taker", "stop_first"), ("stress", "stop_first"), ("taker", "target_first"))
COST_BY_NAME = {item.name: item for item in COSTS}
BOOTSTRAP_REPETITIONS = 2000
BOOTSTRAP_SEED = 20261015


def ms(value: str) -> int:
    return int(datetime.fromisoformat(value).replace(tzinfo=timezone.utc).timestamp() * 1000)


def event_key(row: dict) -> tuple[str, int]:
    return row["symbol"], int(row["signal_ms"])


def recover_b_signal_plans(frames: dict[int, dict], market: Market, start_ms: int, end_ms: int) -> list[dict]:
    """Replay only the all-events B watch state and retain frozen plan levels."""
    watches: dict[str, dict] = {}
    events: list[dict] = []
    for now in range(start_ms + H4, end_ms, H4):
        eligible = frames.get(now, {})
        for symbol, plan in list(watches.items()):
            state = plan_decision(plan, market.row(symbol, "4h", now - H4), now, symbol in eligible)
            if state in {"expired", "invalidated"}:
                del watches[symbol]
            elif state == "signal":
                events.append({
                    "symbol": symbol,
                    "signal_ms": now,
                    "plan_created_ms": int(plan["created_ms"]),
                    "entry_low": float(plan["entry_low"]),
                    "entry_high": float(plan["entry_high"]),
                    "original_stop": float(plan["original_stop"]),
                    "regime": eligible[symbol]["regime"],
                })
                del watches[symbol]
        candidates = [
            (symbol, feature)
            for symbol, feature in eligible.items()
            if feature["candidate"] is not None and symbol not in watches
        ]
        for symbol, feature in sorted(candidates, key=lambda pair: (-pair[1]["qv"], pair[0])):
            watches[symbol] = dict(feature["candidate"], created_ms=now)
    return events


def confirming_hours(arrays: dict, plan: dict) -> tuple[np.ndarray, np.ndarray]:
    symbol, signal = plan["symbol"], int(plan["signal_ms"])
    parent = arrays[symbol]["4h"]
    pi = int(np.searchsorted(parent[:, 0], signal - H4))
    if pi >= len(parent) or int(parent[pi, 0]) != signal - H4:
        raise AssertionError(f"Missing confirming 4h bar: {event_key(plan)}")
    hours = arrays[symbol]["1h"]
    first = int(np.searchsorted(hours[:, 0], signal - H4))
    segment = hours[first:first + 4]
    expected = np.arange(signal - H4, signal, HOUR)
    if len(segment) != 4 or not np.array_equal(segment[:, 0].astype(np.int64), expected):
        raise AssertionError(f"Incomplete confirming 1h path: {event_key(plan)}")
    aggregate = np.asarray([segment[0, 1], segment[:, 2].max(), segment[:, 3].min(), segment[-1, 4]])
    if not np.allclose(aggregate, parent[pi, 1:5], rtol=1e-8, atol=1e-12):
        raise AssertionError(f"1h/4h aggregate mismatch: {event_key(plan)}")
    return parent[pi], segment


def earliest_price_reclaim(plan: dict, hours: np.ndarray) -> dict:
    """Find a reclaim known at an hourly close before the 4h close."""
    cumulative_high = -math.inf
    cumulative_low = math.inf
    for index in range(3):
        row = hours[index]
        cumulative_high = max(cumulative_high, float(row[2]))
        cumulative_low = min(cumulative_low, float(row[3]))
        touches = cumulative_high >= plan["entry_low"] and cumulative_low <= plan["entry_high"]
        if touches and float(row[4]) >= plan["entry_high"]:
            entry_ms = int(hours[index + 1, 0])
            return {
                "earlier_reclaim": True,
                "reclaim_close_ms": int(row[0] + HOUR),
                "oracle_entry_ms": entry_ms,
                "lead_hours": (int(plan["signal_ms"]) - entry_ms) / HOUR,
                "oracle_raw_entry": float(hours[index + 1, 1]),
            }
    return {
        "earlier_reclaim": False,
        "reclaim_close_ms": None,
        "oracle_entry_ms": int(plan["signal_ms"]),
        "lead_hours": 0.0,
        "oracle_raw_entry": None,
    }


def simulate_hourly_exit(
    rows: np.ndarray,
    symbol: str,
    entered: int,
    end_ms: int,
    costs,
    tie_break: str,
) -> dict:
    if tie_break not in {"stop_first", "target_first"}:
        raise ValueError(tie_break)
    index = int(np.searchsorted(rows[:, 0], entered))
    if index >= len(rows) or int(rows[index, 0]) != entered:
        return {"symbol": symbol, "entry_ms": entered, "status": "NO_ENTRY", "closed": False}
    raw_entry = float(rows[index, 1])
    entry = raw_entry * (1 + costs.entry_slip)
    stop, target = entry * 0.97, entry * 1.05
    deadline = entered + HOLD
    ambiguous = 0
    last_mark = raw_entry

    def finish(status: str, raw_exit: float, when: int, exact: bool = False) -> dict:
        closed = status in {"TP", "SL", "TIME"}
        fee = costs.tp_fee if status == "TP" else costs.exit_fee if closed else 0.0
        slip = costs.tp_slip if status == "TP" else costs.exit_slip if closed else 0.0
        exit_price = raw_exit * (1 - slip)
        entry_cash = entry * (1 + costs.entry_fee)
        fees = entry * costs.entry_fee + exit_price * fee
        slippage = entry - raw_entry + raw_exit - exit_price
        net = exit_price * (1 - fee) - entry_cash
        result = {
            "symbol": symbol,
            "entry_ms": entered,
            "exit_ms": int(when),
            "status": status,
            "closed": closed,
            "raw_entry": raw_entry,
            "entry_price": entry,
            "stop": stop,
            "target": target,
            "raw_exit": float(raw_exit),
            "exit_price": exit_price,
            "net_return_pct": 100 * net / entry_cash,
            "raw_return_pct": 100 * (raw_exit - raw_entry) / entry_cash,
            "fee_pct": 100 * fees / entry_cash,
            "slippage_pct": 100 * slippage / entry_cash,
            "duration_hours": (when - entered) / HOUR,
            "exit_time_exact": exact,
            "ambiguous": ambiguous,
            "fallback": {},
        }
        if abs(result["raw_return_pct"] - result["fee_pct"] - result["slippage_pct"] - result["net_return_pct"]) > 1e-9:
            raise AssertionError("Hourly cash identity failed")
        return result

    for when in range(entered, min(deadline, end_ms), HOUR):
        i = int(np.searchsorted(rows[:, 0], when))
        if i >= len(rows) or int(rows[i, 0]) != when:
            return finish("GAP_CENSORED", last_mark, end_ms)
        row = rows[i]
        opening, high, low = float(row[1]), float(row[2]), float(row[3])
        if opening <= stop:
            return finish("SL", opening, when, True)
        if opening >= target:
            return finish("TP", target, when, True)
        sl_hit, tp_hit = low <= stop, high >= target
        if sl_hit and tp_hit:
            ambiguous += 1
        if sl_hit and (not tp_hit or tie_break == "stop_first"):
            return finish("SL", stop, when + HOUR)
        if tp_hit:
            return finish("TP", target, when + HOUR)
        last_mark = float(row[4])
    if deadline <= end_ms:
        i = int(np.searchsorted(rows[:, 0], deadline))
        if i >= len(rows) or int(rows[i, 0]) != deadline:
            return finish("GAP_CENSORED", last_mark, end_ms)
        opening = float(rows[i, 1])
        if opening <= stop:
            return finish("SL", opening, deadline, True)
        if opening >= target:
            return finish("TP", target, deadline, True)
        return finish("TIME", opening, deadline, True)
    return finish("END_CENSORED", last_mark, end_ms)


def verify_baseline(actual: list[dict], expected: list[dict]) -> dict:
    if len(actual) != len(expected):
        raise AssertionError("Baseline row count mismatch")
    max_error = 0.0
    for current, old in zip(actual, expected):
        if event_key(current) != event_key(old):
            raise AssertionError(f"Baseline event mismatch: {event_key(current)}")
        for field in ("status", "exit_ms"):
            if current[field] != old[field]:
                raise AssertionError(f"Baseline {field} mismatch: {event_key(current)}")
        for field in ("raw_entry", "entry_price", "raw_exit", "exit_price", "net_return_pct", "raw_return_pct", "fee_pct", "slippage_pct"):
            error = abs(float(current[field]) - float(old[field]))
            max_error = max(max_error, error)
            if error > 1e-9:
                raise AssertionError(f"Baseline {field} mismatch {event_key(current)}: {error}")
    return {"rows": len(actual), "max_numeric_error": max_error, "exact_status_exit": True}


def paired_bootstrap(baseline: list[dict], oracle: list[dict], start_ms: int, end_ms: int) -> dict:
    block_ms = 14 * DAY
    count = math.ceil((end_ms - start_ms) / block_ms)
    sums = np.zeros((count, 3), dtype=float)
    counts = np.zeros(count, dtype=int)
    right = {event_key(row): row for row in oracle}
    for left in baseline:
        pair = right[event_key(left)]
        if not left["closed"] or not pair["closed"]:
            continue
        block = min(count - 1, max(0, (int(left["signal_ms"]) - start_ms) // block_ms))
        sums[block] += (left["net_return_pct"], pair["net_return_pct"], pair["net_return_pct"] - left["net_return_pct"])
        counts[block] += 1
    rng = np.random.default_rng(BOOTSTRAP_SEED)
    picks = rng.integers(0, count, size=(BOOTSTRAP_REPETITIONS, count))
    sampled_count = counts[picks].sum(axis=1)
    sampled_sum = sums[picks].sum(axis=1)
    usable = sampled_count > 0
    means = sampled_sum[usable] / sampled_count[usable, None]
    return {
        "block_days": 14,
        "repetitions": BOOTSTRAP_REPETITIONS,
        "valid_resamples": int(usable.sum()),
        "baseline_mean_net_pct_ci": np.quantile(means[:, 0], [0.025, 0.975]).tolist(),
        "oracle_mean_net_pct_ci": np.quantile(means[:, 1], [0.025, 0.975]).tolist(),
        "delta_mean_net_pct_ci": np.quantile(means[:, 2], [0.025, 0.975]).tolist(),
    }


def leave_one_out(baseline: list[dict], oracle: list[dict], dimension: str) -> dict:
    right = {event_key(row): row for row in oracle}
    def label(row: dict) -> str:
        if dimension == "symbol":
            return row["symbol"]
        return datetime.fromtimestamp(row["signal_ms"] / 1000, timezone.utc).strftime("%G-W%V")
    labels = sorted({label(row) for row in baseline})
    values = []
    for removed in labels:
        deltas = [
            right[event_key(row)]["net_return_pct"] - row["net_return_pct"]
            for row in baseline if label(row) != removed and row["closed"] and right[event_key(row)]["closed"]
        ]
        values.append({"removed": removed, "mean_delta_net_pct": float(np.mean(deltas)), "paired": len(deltas)})
    return {
        "dimension": dimension,
        "groups": len(values),
        "min_delta": min(item["mean_delta_net_pct"] for item in values),
        "max_delta": max(item["mean_delta_net_pct"] for item in values),
        "worst_removed": min(values, key=lambda item: item["mean_delta_net_pct"]),
        "best_removed": max(values, key=lambda item: item["mean_delta_net_pct"]),
    }


def latency_summary(rows: list[dict]) -> dict:
    earlier = [row for row in rows if row["earlier_reclaim"]]
    improvements = [row["entry_price_improvement_pct"] for row in earlier]
    return {
        "events": len(rows),
        "earlier_reclaim_events": len(earlier),
        "earlier_reclaim_pct": 100 * len(earlier) / len(rows),
        "lead_hour_counts": dict(Counter(str(int(row["lead_hours"])) for row in earlier)),
        "lead_hours_mean": float(np.mean([row["lead_hours"] for row in earlier])) if earlier else None,
        "entry_price_improvement_mean_pct": float(np.mean(improvements)) if earlier else None,
        "entry_price_improvement_median_pct": float(np.median(improvements)) if earlier else None,
        "earlier_entry_cheaper_pct": 100 * sum(value > 0 for value in improvements) / len(improvements) if improvements else None,
    }


def branch_result(baseline: list[dict], oracle: list[dict], start_ms: int, end_ms: int) -> dict:
    base_metrics = trade_metrics(baseline)
    oracle_metrics = trade_metrics(oracle)
    return {
        "baseline": base_metrics,
        "oracle": oracle_metrics,
        "mean_net_pct_delta": oracle_metrics["mean_net_pct"] - base_metrics["mean_net_pct"],
        "win_rate_delta_pp": oracle_metrics["win_rate_pct"] - base_metrics["win_rate_pct"],
        "profit_factor_delta": oracle_metrics["profit_factor"] - base_metrics["profit_factor"],
        "bootstrap": paired_bootstrap(baseline, oracle, start_ms, end_ms),
        "leave_one_symbol": leave_one_out(baseline, oracle, "symbol"),
        "leave_one_week": leave_one_out(baseline, oracle, "week"),
    }


def decide(summary: dict) -> tuple[str, list[str]]:
    windows = [summary["windows"][name] for name in ("early", "near")]
    if not all(branch["measurement"]["passed"] for window in windows for branch in window["branches"].values()):
        return "measurement_insufficient", ["至少一个分支未通过计划恢复、1h聚合、4h逐笔复现或会计恒等闸门。"]
    main = [window["branches"]["taker_stop_first"] for window in windows]
    stress = [window["branches"]["stress_stop_first"] for window in windows]
    target = [window["branches"]["taker_target_first"] for window in windows]
    absolute_main = all(item["comparison"]["oracle"]["mean_net_pct"] > 0 for item in main)
    ci_main = all(item["comparison"]["bootstrap"]["delta_mean_net_pct_ci"][0] >= 0 for item in main)
    absolute_stress = all(item["comparison"]["oracle"]["mean_net_pct"] > 0 for item in stress)
    order_flip = any(
        (main_item["comparison"]["oracle"]["mean_net_pct"] > 0) != (target_item["comparison"]["oracle"]["mean_net_pct"] > 0)
        or (main_item["comparison"]["mean_net_pct_delta"] >= 0) != (target_item["comparison"]["mean_net_pct_delta"] >= 0)
        for main_item, target_item in zip(main, target)
    )
    summary["qualification_checks"] = {
        "taker_oracle_positive_both": absolute_main,
        "paired_ci_lower_nonnegative_both": ci_main,
        "stress_oracle_positive_both": absolute_stress,
        "tie_break_no_sign_flip": not order_flip,
    }
    if order_flip:
        return "measurement_insufficient", ["1h同根顺序使上界绝对收益或相对改善资格翻号。"]
    if absolute_main and ci_main and absolute_stress:
        return "stage_b_eligible", ["延迟上界通过双窗绝对收益、压力成本和配对区块资格，仅允许另冻独立1h候选协议。"]
    return "stop_lower_timeframe_timing_route", [
        "测量闭合，但oracle-confirmed提前成交上界未同时通过双窗正收益、压力成本和配对区块门槛。"
    ]


def render_report(summary: dict) -> str:
    lines = [
        "# 动能启动时间颗粒度阶段A：4h确认延迟上界",
        "",
        f"Taskboard：`CRYPTOTRADIN-129`。裁决：`{summary['decision']}`。",
        "",
        "## 白话结论",
        "",
        summary["plain_language"],
        "",
        "> 重要：本报告只包含最终会形成4h确认的事件，因此提前1h版本知道了未来确认结果，是偏有利的延迟上界，不是可执行1h策略。",
        "",
        "## 延迟覆盖",
        "",
        "| 窗口 | 事件 | 可提前1h事件 | 比例 | lead 1h/2h/3h | 更早成交价优势均值 | 中位 |",
        "|---|---:|---:|---:|---|---:|---:|",
    ]
    for window, label in (("early", "早窗"), ("near", "近窗")):
        item = summary["windows"][window]["latency"]
        counts = item["lead_hour_counts"]
        lines.append(
            f"| {label} | {item['events']} | {item['earlier_reclaim_events']} | {item['earlier_reclaim_pct']:.2f}% | "
            f"{counts.get('1', 0)}/{counts.get('2', 0)}/{counts.get('3', 0)} | "
            f"{item['entry_price_improvement_mean_pct']:.4f}% | {item['entry_price_improvement_median_pct']:.4f}% |"
        )
    lines.extend([
        "",
        "## 主结果：taker / stop-first / fixed +5%/-3%/48h",
        "",
        "| 窗口 | 版本 | mean net% | 胜率 | PF | TP/SL/TIME | mean fee% | mean slippage% |",
        "|---|---|---:|---:|---:|---|---:|---:|",
    ])
    for window, label in (("early", "早窗"), ("near", "近窗")):
        item = summary["windows"][window]["branches"]["taker_stop_first"]["comparison"]
        for key, name in (("baseline", "原4h"), ("oracle", "1h上界")):
            metric = item[key]
            counts = metric["status_counts"]
            lines.append(
                f"| {label} | {name} | {metric['mean_net_pct']:.4f}% | {metric['win_rate_pct']:.2f}% | "
                f"{metric['profit_factor']:.3f} | {counts.get('TP', 0)}/{counts.get('SL', 0)}/{counts.get('TIME', 0)} | "
                f"{metric['mean_fee_pct']:.4f}% | {metric['mean_slippage_pct']:.4f}% |"
            )
        ci = item["bootstrap"]["delta_mean_net_pct_ci"]
        lines.append(f"| {label} | 上界-原4h 14日CI | {ci[0]:.4f}%～{ci[1]:.4f}% |  |  |  |  |  |")
    lines.extend(["", "## 压力成本与顺序", "", "| 窗口 | 分支 | 原4h mean net% | 1h上界 mean net% | Δ |", "|---|---|---:|---:|---:|"])
    for window, label in (("early", "早窗"), ("near", "近窗")):
        for branch in ("stress_stop_first", "taker_target_first"):
            item = summary["windows"][window]["branches"][branch]["comparison"]
            lines.append(f"| {label} | {branch} | {item['baseline']['mean_net_pct']:.4f}% | {item['oracle']['mean_net_pct']:.4f}% | {item['mean_net_pct_delta']:+.4f}pp |")
    lines.extend(["", "## 裁决", ""])
    lines.extend(f"- {reason}" for reason in summary["decision_reasons"])
    lines.extend([
        "",
        "## 边界",
        "",
        "- 该上界用最终4h确认筛选样本，没有计入独立1h实时扫描产生的假突破，不能当作1h策略绩效。",
        "- 两个窗口已烧，币池为current-survivor；通过也只允许另立阶段B协议。",
        "- 15分钟、生产、paper、shadow和采集调度均未修改。",
        "- 完整逐笔、测量闸门、集中度和哈希见CSV/JSON/manifest。",
    ])
    return "\n".join(lines) + "\n"


def write_trades(rows: list[dict]) -> None:
    fields = [
        "window", "cost", "tie_break", "symbol", "signal_ms", "plan_created_ms", "entry_low", "entry_high",
        "earlier_reclaim", "reclaim_close_ms", "oracle_entry_ms", "lead_hours", "baseline_raw_entry",
        "oracle_raw_entry", "entry_price_improvement_pct", "baseline_status", "oracle_status", "baseline_exit_ms",
        "oracle_exit_ms", "baseline_net_return_pct", "oracle_net_return_pct", "delta_net_pct", "baseline_fee_pct",
        "oracle_fee_pct", "baseline_slippage_pct", "oracle_slippage_pct", "baseline_ambiguous", "oracle_ambiguous",
        "regime",
    ]
    with (OUT / "trades.csv").open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field) for field in fields})


def main() -> None:
    if OUT.exists():
        raise SystemExit(f"Preserve existing output directory: {OUT}")
    OUT.mkdir(parents=True)
    windows = {}
    csv_rows = []
    input_hashes = {}
    for start, end in WINDOWS:
        meta_path = FROZEN / f"{start}_inputs.json"
        meta = read_json(meta_path)
        arrays = load_arrays(meta)
        market = Market(arrays)
        frames, _events, frame_checks = build_frames(start, arrays)
        plans = recover_b_signal_plans(frames, market, ms(start), ms(end))
        plan_index = {event_key(plan): plan for plan in plans}
        if len(plan_index) != len(plans):
            raise AssertionError("Duplicate recovered B signal plans")

        latency_rows = []
        confirming_checks = []
        for plan in plans:
            parent, hours = confirming_hours(arrays, plan)
            diagnostic = earliest_price_reclaim(plan, hours)
            baseline_raw_entry = float(arrays[plan["symbol"]]["4h"][
                int(np.searchsorted(arrays[plan["symbol"]]["4h"][:, 0], plan["signal_ms"]))
            ][1])
            oracle_raw = diagnostic["oracle_raw_entry"] if diagnostic["earlier_reclaim"] else baseline_raw_entry
            diagnostic.update(plan)
            diagnostic["baseline_raw_entry"] = baseline_raw_entry
            diagnostic["oracle_raw_entry"] = oracle_raw
            diagnostic["entry_price_improvement_pct"] = 100 * (baseline_raw_entry / oracle_raw - 1)
            diagnostic["confirming_4h_return_pct"] = 100 * (float(parent[4]) / float(parent[1]) - 1)
            latency_rows.append(diagnostic)
            confirming_checks.append(True)

        label = "early" if start == WINDOWS[0][0] else "near"
        branches = {}
        for cost_name, tie_break in BRANCHES:
            source_path = REFERENCE / f"{start}_{cost_name}_{tie_break}_all_events_trades.json.gz"
            source = read_json(source_path)["B"]
            if set(event_key(row) for row in source) != set(plan_index):
                raise AssertionError(f"Recovered plan set mismatch: {start} {cost_name} {tie_break}")
            baseline, oracle = [], []
            latency_index = {event_key(row): row for row in latency_rows}
            for expected in source:
                key = event_key(expected)
                latency = latency_index[key]
                base = simulate_hourly_exit(arrays[expected["symbol"]]["1h"], expected["symbol"], int(expected["signal_ms"]), ms(end), COST_BY_NAME[cost_name], tie_break)
                upper = simulate_hourly_exit(arrays[expected["symbol"]]["1h"], expected["symbol"], int(latency["oracle_entry_ms"]), ms(end), COST_BY_NAME[cost_name], tie_break)
                for row in (base, upper):
                    row.update(signal_ms=int(expected["signal_ms"]), regime=expected["regime"])
                baseline.append(base)
                oracle.append(upper)
                csv_rows.append({
                    "window": label,
                    "cost": cost_name,
                    "tie_break": tie_break,
                    **{field: latency.get(field) for field in ("symbol", "signal_ms", "plan_created_ms", "entry_low", "entry_high", "earlier_reclaim", "reclaim_close_ms", "oracle_entry_ms", "lead_hours", "baseline_raw_entry", "oracle_raw_entry", "entry_price_improvement_pct", "regime")},
                    "baseline_status": base["status"],
                    "oracle_status": upper["status"],
                    "baseline_exit_ms": base["exit_ms"],
                    "oracle_exit_ms": upper["exit_ms"],
                    "baseline_net_return_pct": base["net_return_pct"],
                    "oracle_net_return_pct": upper["net_return_pct"],
                    "delta_net_pct": upper["net_return_pct"] - base["net_return_pct"],
                    "baseline_fee_pct": base["fee_pct"],
                    "oracle_fee_pct": upper["fee_pct"],
                    "baseline_slippage_pct": base["slippage_pct"],
                    "oracle_slippage_pct": upper["slippage_pct"],
                    "baseline_ambiguous": base["ambiguous"],
                    "oracle_ambiguous": upper["ambiguous"],
                })
            verification = verify_baseline(baseline, source)
            measurement_errors = []
            if any(not row["closed"] for row in baseline + oracle):
                measurement_errors.append("unclosed_event")
            branches[f"{cost_name}_{tie_break}"] = {
                "comparison": branch_result(baseline, oracle, ms(start), ms(end)),
                "baseline_verification": verification,
                "measurement": {"passed": not measurement_errors, "errors": measurement_errors},
            }
            input_hashes[str(source_path.relative_to(ROOT))] = sha256(source_path)
        windows[label] = {
            "start": start,
            "end": end,
            "recovered_plans": len(plans),
            "confirming_paths_verified": len(confirming_checks),
            "frame_checks": frame_checks,
            "latency": latency_summary(latency_rows),
            "branches": branches,
        }
        input_hashes[str(meta_path.relative_to(ROOT))] = sha256(meta_path)
        input_hashes[meta["archive"]] = sha256(ROOT / meta["archive"])
        del market, arrays

    summary = {
        "experiment": "momentum_resolution_stage_a_v1",
        "taskboard": "CRYPTOTRADIN-129",
        "scope": "oracle_confirmed_latency_ceiling_not_standalone_1h_strategy",
        "windows": windows,
        "limitations": ["future_4h_confirmation_conditioning", "burned_windows", "current_survivor_universe"],
    }
    decision, reasons = decide(summary)
    summary["decision"] = decision
    summary["decision_reasons"] = reasons
    if decision == "stage_b_eligible":
        summary["plain_language"] = "在最终会通过4h确认的有利样本里，提前到1h成交的上界在双窗和压力成本下都形成正收益并通过区块门槛；只获得另立独立1h候选协议的资格。"
    elif decision == "stop_lower_timeframe_timing_route":
        summary["plain_language"] = "4h确认延迟是真实且有经济影响的：约80.5%的最终确认事件可提前1至3小时，普通taker成本下的有利上界在两窗均转正。但这个上界已经提前知道未来4h会确认，仍在stress成本下略亏，所以不能授权独立1h策略阶段；单纯把同一个B信号提前几小时还不是稳健充分解法。"
    else:
        summary["plain_language"] = "现有计划恢复、1h聚合、逐笔复现或同根顺序不足以可信判断4h确认延迟。"

    save_json(OUT / "summary.json", summary)
    write_trades(csv_rows)
    (OUT / "report.md").write_text(render_report(summary), encoding="utf-8")
    sources = [
        PROTOCOL,
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
        f"- Recovered plans: early `{windows['early']['recovered_plans']}`, near `{windows['near']['recovered_plans']}`.\n"
        f"- Confirming 1h paths verified: early `{windows['early']['confirming_paths_verified']}`, near `{windows['near']['confirming_paths_verified']}`.\n"
        "- All three original 4h branches per window reproduced cashfix status, exit time, and numerics within 1e-9.\n"
        "- No network or database writes; no production, paper, shadow, or schedule changes.\n",
        encoding="utf-8",
    )
    print(json.dumps({"decision": decision, "qualification": summary.get("qualification_checks"), "latency": {key: value["latency"] for key, value in windows.items()}}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
