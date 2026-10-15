"""Attribute CRYPTOTRADIN-133's ATR-exit result to TP, SL, and interaction.

This read-only study replays the same frozen B all-events entries under the
four preregistered exit policies.  It does not change production, paper,
shadow, configuration, or the SQLite database.
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

from research_atr_adaptive_short_exit import (  # noqa: E402
    BRANCHES,
    COST_BY_NAME,
    FROZEN,
    REFERENCE,
    WINDOWS,
    enrich_and_simulate,
    event_key,
    ms,
    verify_fixed,
)
from research_breakout_d6 import load_arrays, read_json, save_json, sha256  # noqa: E402
from short_horizon_core import DAY, H4, HOLD, Market, trade_metrics  # noqa: E402


PROTOCOL = ROOT / "reports/2026-10-15/atr_exit_component_attribution_protocol_v1.md"
OUT = ROOT / "reports/2026-10-15/atr_exit_component_attribution_v1"
POLICIES = (
    "fixed_fixed",
    "atr_tp_fixed_sl",
    "fixed_tp_atr_sl",
    "atr_atr",
)
SINGLE_COMPONENTS = ("atr_tp_fixed_sl", "fixed_tp_atr_sl")
DISPLAY = {
    "fixed_fixed": "fixed+fixed",
    "atr_tp_fixed_sl": "ATR_TP+fixed_SL",
    "fixed_tp_atr_sl": "fixed_TP+ATR_SL",
    "atr_atr": "ATR+ATR",
}
QUALIFY_COSTS = ("taker", "stress")
QUALIFY_TIES = ("stop_first", "target_first")
BOOTSTRAP_REPETITIONS = 2000
BOOTSTRAP_SEED = 20261015


def add_path(row: dict, market: Market, end_ms: int, tie_break: str) -> None:
    """Add a descriptive complete-48h path using the row's own levels."""
    entered = int(row["entry_ms"])
    deadline = entered + HOLD
    if deadline > end_ms:
        row.update(path_complete_48h=False, first_touch="INCOMPLETE", reachable_set="")
        return
    stop, target = float(row["stop"]), float(row["target"])
    maximum = minimum = float(row["raw_entry"])
    stop_order = target_order = None
    double_touch = 0

    def record(kind: str, order: tuple[int, int]) -> None:
        nonlocal stop_order, target_order
        if kind == "SL" and stop_order is None:
            stop_order = order
        if kind == "TP" and target_order is None:
            target_order = order

    for opened in range(entered, deadline, H4):
        pieces, _source = market.segments(row["symbol"], opened)
        if not pieces:
            row.update(path_complete_48h=False, first_touch="GAP", reachable_set="")
            return
        for bar, _step in pieces:
            when, opening = int(bar[0]), float(bar[1])
            high, low = float(bar[2]), float(bar[3])
            maximum, minimum = max(maximum, high), min(minimum, low)
            if opening <= stop:
                record("SL", (when, 0))
            elif opening >= target:
                record("TP", (when, 0))
            sl_hit, tp_hit = low <= stop, high >= target
            if sl_hit and tp_hit:
                double_touch += 1
                first, second = (("SL", "TP") if tie_break == "stop_first" else ("TP", "SL"))
                record(first, (when, 1))
                record(second, (when, 2))
            elif sl_hit:
                record("SL", (when, 1))
            elif tp_hit:
                record("TP", (when, 1))

    deadline_row = market.row(row["symbol"], "4h", deadline)
    if deadline_row is None:
        row.update(path_complete_48h=False, first_touch="GAP", reachable_set="")
        return
    opening = float(deadline_row[1])
    maximum, minimum = max(maximum, opening), min(minimum, opening)
    if opening <= stop:
        record("SL", (deadline, 0))
    elif opening >= target:
        record("TP", (deadline, 0))

    reachable = [kind for kind, order in (("TP", target_order), ("SL", stop_order)) if order is not None]
    if not reachable:
        first_touch = "NONE"
    elif target_order is None:
        first_touch = "SL"
    elif stop_order is None:
        first_touch = "TP"
    else:
        first_touch = "TP" if target_order < stop_order else "SL"
    entry = float(row["entry_price"])
    mfe = 100 * (maximum / entry - 1)
    mae = 100 * (minimum / entry - 1)
    row.update(
        path_complete_48h=True,
        mfe_48h_pct=mfe,
        mae_48h_pct=mae,
        first_touch=first_touch,
        reachable_set="|".join(reachable) if reachable else "NONE",
        path_double_touch_bars=double_touch,
        uncaptured_pct=max(0.0, mfe - max(0.0, float(row["raw_return_pct"]))),
    )


def attach_common_r(rows_by_policy: dict[str, list[dict]]) -> None:
    fixed = {event_key(row): row for row in rows_by_policy["fixed_fixed"]}
    if len(fixed) != len(rows_by_policy["fixed_fixed"]):
        raise AssertionError("Duplicate fixed events")
    for policy, rows in rows_by_policy.items():
        if {event_key(row) for row in rows} != set(fixed):
            raise AssertionError(f"Event set mismatch for {policy}")
        for row in rows:
            denominator = float(fixed[event_key(row)]["planned_risk_pct"])
            if denominator <= 0:
                raise AssertionError("Non-positive common-risk denominator")
            total_cost = float(row["fee_pct"]) + float(row["slippage_pct"])
            row.update(
                exit_policy=DISPLAY[policy],
                gross_return_pct=float(row["raw_return_pct"]),
                total_cost_pct=total_cost,
                own_planned_risk_pct=float(row["planned_risk_pct"]),
                own_net_r=float(row["net_r"]),
                own_cost_r=float(row["cost_r"]),
                common_planned_risk_pct=denominator,
                gross_common_r=float(row["raw_return_pct"]) / denominator,
                net_common_r=float(row["net_return_pct"]) / denominator,
                cost_common_r=total_cost / denominator,
            )


def measurement_checks(rows_by_policy: dict[str, list[dict]]) -> dict:
    errors: list[str] = []
    keys = {policy: [event_key(row) for row in rows] for policy, rows in rows_by_policy.items()}
    baseline_keys = keys["fixed_fixed"]
    for policy, policy_keys in keys.items():
        if policy_keys != baseline_keys:
            errors.append(f"ordered_event_set:{policy}")
    for index, baseline_key in enumerate(baseline_keys):
        closed_flags = []
        for policy in POLICIES:
            row = rows_by_policy[policy][index]
            closed_flags.append(bool(row["closed"]))
            gross = float(row["gross_return_pct"])
            costs = float(row["total_cost_pct"])
            net = float(row["net_return_pct"])
            own_risk = float(row["own_planned_risk_pct"])
            common_risk = float(row["common_planned_risk_pct"])
            if abs(gross - costs - net) > 1e-9:
                errors.append(f"cash_identity:{policy}:{baseline_key}")
            if abs(net / own_risk - float(row["own_net_r"])) > 1e-9:
                errors.append(f"own_r_identity:{policy}:{baseline_key}")
            if abs(net / common_risk - float(row["net_common_r"])) > 1e-9:
                errors.append(f"common_r_identity:{policy}:{baseline_key}")
            if abs(costs / common_risk - float(row["cost_common_r"])) > 1e-9:
                errors.append(f"common_cost_identity:{policy}:{baseline_key}")
        if len(set(closed_flags)) != 1:
            errors.append(f"policy_dependent_censoring:{baseline_key}")
        if not all(closed_flags):
            errors.append(f"unclosed_event:{baseline_key}")
    return {
        "passed": not errors,
        "events": len(baseline_keys),
        "errors": errors[:100],
        "error_count": len(errors),
    }


def common_r_curve(rows: list[dict]) -> dict:
    equity = [10_000.0]
    for row in sorted(rows, key=lambda item: (item["signal_ms"], item["symbol"])):
        if row["closed"]:
            equity.append(equity[-1] * (1 + 0.01 * row["net_common_r"]))
    values = np.asarray(equity)
    return {
        "final_return_pct": 100 * (values[-1] / values[0] - 1),
        "max_drawdown_pct": 100 * float(np.max(1 - values / np.maximum.accumulate(values))),
    }


def policy_metrics(rows: list[dict]) -> dict:
    result = trade_metrics(rows)
    closed = [row for row in rows if row["closed"]]
    net = np.asarray([row["net_return_pct"] for row in closed])
    own = np.asarray([row["own_net_r"] for row in closed])
    common = np.asarray([row["net_common_r"] for row in closed])
    result.update(
        median_net_pct=float(np.median(net)),
        mean_own_net_r=float(own.mean()),
        median_own_net_r=float(np.median(own)),
        mean_common_net_r=float(common.mean()),
        median_common_net_r=float(np.median(common)),
        mean_total_cost_pct=float(np.mean([row["total_cost_pct"] for row in closed])),
        mean_own_cost_r=float(np.mean([row["own_cost_r"] for row in closed])),
        mean_common_cost_r=float(np.mean([row["cost_common_r"] for row in closed])),
        common_r_p05=float(np.quantile(common, 0.05)),
        common_r_worst=float(common.min()),
        common_r_curve=common_r_curve(closed),
        path_complete=sum(bool(row.get("path_complete_48h")) for row in rows),
        mfe_48h_median_pct=float(np.median([row["mfe_48h_pct"] for row in rows if row.get("path_complete_48h")])),
        mae_48h_median_pct=float(np.median([row["mae_48h_pct"] for row in rows if row.get("path_complete_48h")])),
        uncaptured_median_pct=float(np.median([row["uncaptured_pct"] for row in rows if row.get("path_complete_48h")])),
        first_touch_counts=dict(Counter(row.get("first_touch", "INCOMPLETE") for row in rows)),
    )
    return result


def paired_block_bootstrap(
    rows_by_policy: dict[str, list[dict]], start_ms: int, end_ms: int
) -> dict:
    block_ms = 14 * DAY
    blocks = math.ceil((end_ms - start_ms) / block_ms)
    sums = np.zeros((blocks, len(POLICIES)), dtype=float)
    counts = np.zeros(blocks, dtype=int)
    indices = [{event_key(row): row for row in rows_by_policy[p]} for p in POLICIES]
    for row in rows_by_policy["fixed_fixed"]:
        key = event_key(row)
        paired = [index[key] for index in indices]
        if not all(item["closed"] for item in paired):
            continue
        block = min(blocks - 1, max(0, (int(row["signal_ms"]) - start_ms) // block_ms))
        sums[block] += [item["net_common_r"] for item in paired]
        counts[block] += 1
    rng = np.random.default_rng(BOOTSTRAP_SEED)
    picks = rng.integers(0, blocks, size=(BOOTSTRAP_REPETITIONS, blocks))
    sampled_counts = counts[picks].sum(axis=1)
    sampled_sums = sums[picks].sum(axis=1)
    usable = sampled_counts > 0
    means = sampled_sums[usable] / sampled_counts[usable, None]
    base = means[:, 0]
    result = {
        "block_days": 14,
        "repetitions": BOOTSTRAP_REPETITIONS,
        "valid_resamples": int(usable.sum()),
        "policy_mean_common_r_ci": {},
        "delta_vs_fixed_common_r_ci": {},
    }
    for position, policy in enumerate(POLICIES):
        result["policy_mean_common_r_ci"][policy] = np.quantile(means[:, position], [0.025, 0.975]).tolist()
        result["delta_vs_fixed_common_r_ci"][policy] = np.quantile(means[:, position] - base, [0.025, 0.975]).tolist()
    effects = factorial_effects_from_values(means)
    result["factorial_common_r_ci"] = {
        name: np.quantile(values, [0.025, 0.975]).tolist() for name, values in effects.items()
    }
    return result


def factorial_effects_from_values(values: np.ndarray) -> dict[str, np.ndarray]:
    fixed, tp, sl, both = (values[..., index] for index in range(4))
    return {
        "tp_marginal": (tp + both - fixed - sl) / 2,
        "sl_marginal": (sl + both - fixed - tp) / 2,
        "interaction": both - tp - sl + fixed,
    }


def factorial_effects(rows_by_policy: dict[str, list[dict]]) -> dict:
    result = {}
    for unit, field in (("net_pct", "net_return_pct"), ("common_r", "net_common_r")):
        means = np.asarray([[np.mean([row[field] for row in rows_by_policy[p]]) for p in POLICIES]])
        result[unit] = {key: float(value[0]) for key, value in factorial_effects_from_values(means).items()}
    return result


def transition_summary(fixed: list[dict], both: list[dict]) -> dict:
    right = {event_key(row): row for row in both}
    groups: dict[str, list[tuple[dict, dict]]] = defaultdict(list)
    for left in fixed:
        pair = right[event_key(left)]
        groups[f"{left['status']}->{pair['status']}"].append((left, pair))
    cells = []
    total_common = total_pct = 0.0
    for transition, pairs in sorted(groups.items()):
        common = [right_row["net_common_r"] - left["net_common_r"] for left, right_row in pairs]
        pct = [right_row["net_return_pct"] - left["net_return_pct"] for left, right_row in pairs]
        total_common += sum(common)
        total_pct += sum(pct)
        cells.append({
            "transition": transition,
            "count": len(pairs),
            "mean_delta_common_r": float(np.mean(common)),
            "total_delta_common_r": float(sum(common)),
            "mean_delta_net_pct": float(np.mean(pct)),
            "total_delta_net_pct": float(sum(pct)),
        })
    direct_common = sum(row["net_common_r"] for row in both) - sum(row["net_common_r"] for row in fixed)
    direct_pct = sum(row["net_return_pct"] for row in both) - sum(row["net_return_pct"] for row in fixed)
    return {
        "cells": cells,
        "total_delta_common_r": total_common,
        "direct_delta_common_r": direct_common,
        "total_delta_net_pct": total_pct,
        "direct_delta_net_pct": direct_pct,
        "closure_error_common_r": total_common - direct_common,
        "closure_error_net_pct": total_pct - direct_pct,
    }


def qualification(summary: dict, candidate: str) -> dict:
    absolute = []
    relative = []
    for window in ("early", "near"):
        for cost in QUALIFY_COSTS:
            for tie in QUALIFY_TIES:
                branch = summary["windows"][window]["branches"][f"{cost}_{tie}"]
                fixed = branch["metrics"]["fixed_fixed"]
                current = branch["metrics"][candidate]
                absolute.append(current["mean_net_pct"] > 0)
                relative.append(current["mean_common_net_r"] - fixed["mean_common_net_r"] >= 0)
    ci = [
        summary["windows"][window]["branches"]["taker_stop_first"]["bootstrap"]
        ["delta_vs_fixed_common_r_ci"][candidate][0] >= 0
        for window in ("early", "near")
    ]
    return {
        "absolute_positive_all_8": all(absolute),
        "relative_nonnegative_all_8": all(relative),
        "main_ci_lower_nonnegative_both": all(ci),
        "qualified": all(absolute) and all(relative) and all(ci),
    }


def order_flip_checks(summary: dict) -> dict:
    flips = []
    for window in ("early", "near"):
        for cost in QUALIFY_COSTS:
            stop = summary["windows"][window]["branches"][f"{cost}_stop_first"]["metrics"]
            target = summary["windows"][window]["branches"][f"{cost}_target_first"]["metrics"]
            for candidate in SINGLE_COMPONENTS:
                absolute_stop = stop[candidate]["mean_net_pct"] > 0
                absolute_target = target[candidate]["mean_net_pct"] > 0
                relative_stop = stop[candidate]["mean_common_net_r"] - stop["fixed_fixed"]["mean_common_net_r"] >= 0
                relative_target = target[candidate]["mean_common_net_r"] - target["fixed_fixed"]["mean_common_net_r"] >= 0
                if absolute_stop != absolute_target or relative_stop != relative_target:
                    flips.append({
                        "window": window,
                        "cost": cost,
                        "candidate": candidate,
                        "absolute_positive": [absolute_stop, absolute_target],
                        "relative_nonnegative": [relative_stop, relative_target],
                    })
    return {"passed": not flips, "flips": flips}


def decide(summary: dict) -> tuple[str, list[str]]:
    measurement_ok = all(
        branch["measurement"]["passed"]
        for window in summary["windows"].values()
        for branch in window["branches"].values()
    )
    order_ok = summary["order_flip_check"]["passed"]
    if not measurement_ok or not order_ok:
        reasons = []
        if not measurement_ok:
            reasons.append("至少一个分支未通过会计恒等、共同事件集或政策无关删失闸门。")
        if not order_ok:
            reasons.append("stop-first与target-first使单组件政策的绝对收益或相对资格符号翻转。")
        return "measurement_insufficient", reasons
    qualified = [candidate for candidate, result in summary["qualification"].items() if result["qualified"]]
    if qualified:
        return "component_validation_eligible", [f"通过预注册资格：{', '.join(DISPLAY[item] for item in qualified)}。"]
    return "reject_current_atr_components", [
        "测量闭合且事件集一致，但两个单组件政策均未同时通过双窗绝对正收益、相对改善和主分支区块区间门槛。"
    ]


def render_report(summary: dict) -> str:
    lines = [
        "# ATR 出口四政策 2×2 失败机制归因",
        "",
        f"Taskboard：`CRYPTOTRADIN-134`。裁决：`{summary['decision']}`。",
        "",
        "## 白话结论",
        "",
        summary["plain_language"],
        "",
        "## 主结果：taker / stop-first",
        "",
        "| 窗口 | 政策 | mean net% | 胜率 | PF | mean own-R | mean common-R | TP/SL/TIME |",
        "|---|---|---:|---:|---:|---:|---:|---|",
    ]
    for window, label in (("early", "早窗"), ("near", "近窗")):
        metrics = summary["windows"][window]["branches"]["taker_stop_first"]["metrics"]
        for policy in POLICIES:
            item = metrics[policy]
            counts = item["status_counts"]
            pf = "n/a" if item["profit_factor"] is None else f"{item['profit_factor']:.3f}"
            lines.append(
                f"| {label} | {DISPLAY[policy]} | {item['mean_net_pct']:.4f}% | {item['win_rate_pct']:.2f}% | "
                f"{pf} | {item['mean_own_net_r']:.4f} | {item['mean_common_net_r']:.4f} | "
                f"{counts.get('TP', 0)}/{counts.get('SL', 0)}/{counts.get('TIME', 0)} |"
            )
    lines.extend(["", "## 组件主效应与交互", "", "| 窗口 | 单位 | TP边际 | SL边际 | 交互 |", "|---|---|---:|---:|---:|"])
    for window, label in (("early", "早窗"), ("near", "近窗")):
        effects = summary["windows"][window]["branches"]["taker_stop_first"]["factorial"]
        for unit in ("net_pct", "common_r"):
            item = effects[unit]
            lines.append(f"| {label} | {unit} | {item['tp_marginal']:.4f} | {item['sl_marginal']:.4f} | {item['interaction']:.4f} |")
    lines.extend(["", "## 单组件资格", ""])
    for candidate, result in summary["qualification"].items():
        lines.append(
            f"- `{DISPLAY[candidate]}`：qualified=`{result['qualified']}`；八分支绝对为正=`{result['absolute_positive_all_8']}`；"
            f"八分支相对不差=`{result['relative_nonnegative_all_8']}`；双窗主分支CI下界≥0=`{result['main_ci_lower_nonnegative_both']}`。"
        )
    lines.extend([
        "",
        "## 测量结论与边界",
        "",
        f"- 同根顺序翻号闸门：`{'pass' if summary['order_flip_check']['passed'] else 'fail'}`。",
        "- 四政策的逐分支会计恒等、共同事件集和删失检查见 `summary.json`；逐笔见 `trades.csv`。",
        "- MFE/MAE、首次触及和可达集合只是路径描述，不用于挑选参数或改变持仓期。",
        "- 两个窗口已烧且币池为current-survivor；即使通过也不能直接改生产。",
        "- 本轮若拒绝，只否定当前ATR20/1ATR SL/5/3ATR TP组件；不证明入场本身没有优势。",
        "",
        "## 裁决理由",
        "",
    ])
    lines.extend(f"- {reason}" for reason in summary["decision_reasons"])
    return "\n".join(lines) + "\n"


def write_trades(rows: list[dict]) -> None:
    fields = [
        "window", "exit_policy", "cost", "policy", "symbol", "signal_ms", "entry_ms", "exit_ms",
        "status", "entry_price", "atr20", "natr20_pct", "target", "stop", "gross_return_pct",
        "fee_pct", "slippage_pct", "total_cost_pct", "net_return_pct", "own_planned_risk_pct",
        "own_net_r", "own_cost_r", "common_planned_risk_pct", "gross_common_r", "net_common_r",
        "cost_common_r", "duration_hours", "mfe_48h_pct", "mae_48h_pct", "first_touch",
        "reachable_set", "ambiguous", "path_double_touch_bars", "uncaptured_pct", "path_complete_48h",
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
    fixed_checks = {}
    input_hashes = {}
    csv_rows = []
    for start, end in WINDOWS:
        meta_path = FROZEN / f"{start}_inputs.json"
        meta = read_json(meta_path)
        arrays = load_arrays(meta)
        market = Market(arrays)
        branches = {}
        for cost_name, tie_break in BRANCHES:
            source_path = REFERENCE / f"{start}_{cost_name}_{tie_break}_all_events_trades.json.gz"
            source_rows = read_json(source_path)["B"]
            rows_by_policy = {}
            for exit_policy in POLICIES:
                rows = enrich_and_simulate(
                    source_rows, arrays, market, ms(end), COST_BY_NAME[cost_name], tie_break, exit_policy
                )
                for row in rows:
                    add_path(row, market, ms(end), tie_break)
                rows_by_policy[exit_policy] = rows
            attach_common_r(rows_by_policy)
            fixed_checks[f"{start}_{cost_name}_{tie_break}"] = verify_fixed(
                rows_by_policy["fixed_fixed"], source_rows
            )
            measurement = measurement_checks(rows_by_policy)
            metrics = {policy: policy_metrics(rows_by_policy[policy]) for policy in POLICIES}
            branches[f"{cost_name}_{tie_break}"] = {
                "cost": cost_name,
                "tie_break": tie_break,
                "metrics": metrics,
                "factorial": factorial_effects(rows_by_policy),
                "bootstrap": paired_block_bootstrap(rows_by_policy, ms(start), ms(end)),
                "transitions_fixed_to_atr": transition_summary(
                    rows_by_policy["fixed_fixed"], rows_by_policy["atr_atr"]
                ),
                "measurement": measurement,
            }
            label = "early" if start == WINDOWS[0][0] else "near"
            for exit_policy, rows in rows_by_policy.items():
                for row in rows:
                    row["window"] = label
                    row["model"] = exit_policy
                    csv_rows.append(row)
            input_hashes[str(source_path.relative_to(ROOT))] = sha256(source_path)
        input_hashes[str(meta_path.relative_to(ROOT))] = sha256(meta_path)
        input_hashes[meta["archive"]] = sha256(ROOT / meta["archive"])
        label = "early" if start == WINDOWS[0][0] else "near"
        windows[label] = {"start": start, "end": end, "branches": branches}
        del market, arrays

    summary = {
        "experiment": "atr_exit_component_attribution_v1",
        "taskboard": "CRYPTOTRADIN-134",
        "policies": {policy: DISPLAY[policy] for policy in POLICIES},
        "configurations": len(POLICIES) * len(WINDOWS) * len(BRANCHES),
        "windows": windows,
        "fixed_replay_verification": fixed_checks,
        "limitations": ["burned_windows", "current_survivor_universe", "descriptive_all_events_risk_curve"],
    }
    summary["order_flip_check"] = order_flip_checks(summary)
    summary["qualification"] = {candidate: qualification(summary, candidate) for candidate in SINGLE_COMPONENTS}
    decision, reasons = decide(summary)
    summary["decision"] = decision
    summary["decision_reasons"] = reasons
    if decision == "component_validation_eligible":
        summary["plain_language"] = "至少一个单独的ATR止盈或ATR止损组件在两个窗口和关键成本/顺序分支都形成正收益与稳健改善，只获得独立验证资格，不能直接上线。"
    elif decision == "reject_current_atr_components":
        summary["plain_language"] = "把ATR止盈和ATR止损拆开后，没有任何一个单组件能在两个窗口稳定把交易变成正期望。因此应停止当前ATR组件路线；这不等于入场一定无效，也不应继续扫ATR参数。"
    else:
        summary["plain_language"] = "当前4h回放的会计、事件配对或同根顺序敏感性不足以支持策略判断，应先修复测量问题。"

    save_json(OUT / "summary.json", summary)
    write_trades(csv_rows)
    (OUT / "report.md").write_text(render_report(summary), encoding="utf-8")
    sources = [
        PROTOCOL,
        ROOT / "scripts/research_atr_exit_component_attribution.py",
        ROOT / "scripts/research_atr_adaptive_short_exit.py",
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
    verification = (
        "# Verification\n\n"
        f"- Protocol SHA256: `{sha256(PROTOCOL)}`\n"
        f"- Configurations: `{summary['configurations']}`.\n"
        f"- Fixed replay branches: `{len(fixed_checks)}`; all exact status/exit and numeric tolerance <=1e-9.\n"
        f"- Measurement branches passed: `{sum(branch['measurement']['passed'] for window in windows.values() for branch in window['branches'].values())}/{len(WINDOWS) * len(BRANCHES)}`.\n"
        f"- Order-flip gate: `{'pass' if summary['order_flip_check']['passed'] else 'fail'}`.\n"
        f"- Decision: `{decision}`.\n"
        "- No network or database writes; frozen archives and B all-events only.\n"
    )
    (OUT / "verification.md").write_text(verification, encoding="utf-8")
    print(json.dumps({"decision": decision, "qualification": summary["qualification"], "order_flip": summary["order_flip_check"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
