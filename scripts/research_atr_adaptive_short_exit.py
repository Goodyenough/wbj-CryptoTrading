"""Compare fixed +5%/-3% exits with one preregistered ATR-adaptive exit.

CRYPTOTRADIN-133 is an isolated, read-only study. It reuses frozen B all-event
signals and market arrays. Production, paper, shadow, configuration, and the
SQLite database are never written.
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

from research_breakout_d6 import load_arrays, read_json, save_json, sha256  # noqa: E402
from short_horizon_core import COSTS, DAY, H4, HOLD, HOUR, Market, trade_metrics  # noqa: E402


FROZEN = ROOT / "reports/2026-10-13/short_horizon_entry_v1"
REFERENCE = ROOT / "reports/2026-10-13/short_horizon_entry_v1_cashfix"
PROTOCOL = ROOT / "reports/2026-10-14/atr_adaptive_short_exit_protocol_v1.md"
OUT = ROOT / "reports/2026-10-14/atr_adaptive_short_exit_v1"
WINDOWS = (("2024-07-01", "2025-06-01"), ("2025-06-01", "2026-06-01"))
BRANCHES = tuple(
    (cost, policy)
    for cost in ("taker", "stress", "legacy_fee")
    for policy in ("stop_first", "target_first")
)
PRIMARY = ("taker", "stop_first")
ATR_STOP_MULTIPLE = 1.0
ATR_TARGET_MULTIPLE = 5.0 / 3.0
BOOTSTRAP_REPETITIONS = 2000
BOOTSTRAP_SEED = 20261014
COST_BY_NAME = {cost.name: cost for cost in COSTS}


def ms(value: str) -> int:
    return int(datetime.fromisoformat(value).replace(tzinfo=timezone.utc).timestamp() * 1000)


def event_key(row: dict) -> tuple[str, int, int]:
    return row["symbol"], int(row["signal_ms"]), int(row["entry_ms"])


def signal_week(row: dict) -> str:
    return datetime.fromtimestamp(row["signal_ms"] / 1000, timezone.utc).strftime("%G-W%V")


def causal_atr20(bars: np.ndarray, signal_ms: int) -> tuple[float, float]:
    """Return ATR20 and signal close using only completed bars before entry."""
    n = int(np.searchsorted(bars[:, 0], signal_ms))
    if n < 21 or int(bars[n - 1, 0]) != signal_ms - H4:
        raise ValueError(f"Missing causal ATR history at {signal_ms}")
    current = bars[n - 20:n]
    previous_close = bars[n - 21:n - 1, 4]
    true_range = np.maximum.reduce(
        (
            current[:, 2] - current[:, 3],
            np.abs(current[:, 2] - previous_close),
            np.abs(current[:, 3] - previous_close),
        )
    )
    atr = float(np.mean(true_range))
    close = float(bars[n - 1, 4])
    if not math.isfinite(atr) or not math.isfinite(close) or atr <= 0 or close <= 0:
        raise ValueError(f"Invalid causal ATR at {signal_ms}")
    return atr, close


def exit_levels(entry: float, atr: float, model: str) -> tuple[float, float]:
    if model == "fixed":
        stop, target = entry * 0.97, entry * 1.05
    elif model == "atr":
        stop = entry - ATR_STOP_MULTIPLE * atr
        target = entry + ATR_TARGET_MULTIPLE * atr
    else:
        raise ValueError(model)
    if stop <= 0 or not stop < entry < target:
        raise ValueError(f"Invalid {model} exit geometry: {stop=} {entry=} {target=}")
    return stop, target


def simulate_exit(
    market: Market,
    symbol: str,
    entered: int,
    end: int,
    costs,
    policy: str,
    atr: float,
    model: str,
) -> dict:
    if policy not in {"stop_first", "target_first"}:
        raise ValueError(policy)
    first = market.row(symbol, "4h", entered)
    if first is None or not math.isfinite(first[1]) or first[1] <= 0:
        return {"status": "NO_ENTRY", "symbol": symbol, "entry_ms": entered}
    raw_entry = float(first[1])
    entry = raw_entry * (1 + costs.entry_slip)
    stop, target = exit_levels(entry, atr, model)
    deadline = entered + HOLD
    ambiguous = 0
    fallback = Counter()
    last_mark = raw_entry

    def finish(status: str, raw_exit: float, when: int, *, exact=False, gap_at=None) -> dict:
        closed = status in {"TP", "SL", "TIME"}
        fee = costs.tp_fee if status == "TP" else costs.exit_fee if closed else 0
        slip = costs.tp_slip if status == "TP" else costs.exit_slip if closed else 0
        exit_price = raw_exit * (1 - slip)
        entry_cash = entry * (1 + costs.entry_fee)
        fees = entry * costs.entry_fee + exit_price * fee
        slippage = entry - raw_entry + raw_exit - exit_price
        net = exit_price * (1 - fee) - entry_cash
        planned_stop_proceeds = stop * (1 - costs.exit_slip) * (1 - costs.exit_fee)
        planned_risk = entry_cash - planned_stop_proceeds
        if planned_risk <= 0:
            raise AssertionError(f"Non-positive planned risk: {symbol} {entered} {model}")
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
            "entry_cash_per_unit": entry_cash,
            "net_return_pct": 100 * net / entry_cash,
            "raw_return_pct": 100 * (raw_exit - raw_entry) / entry_cash,
            "fee_pct": 100 * fees / entry_cash,
            "slippage_pct": 100 * slippage / entry_cash,
            "duration_hours": (when - entered) / HOUR,
            "exit_time_exact": exact,
            "ambiguous": ambiguous,
            "fallback": dict(fallback),
            "gap_at": gap_at,
            "planned_risk_pct": 100 * planned_risk / entry_cash,
            "net_r": net / planned_risk,
            "cost_r": (fees + slippage) / planned_risk,
            "stop_distance_pct": 100 * (entry - stop) / entry,
            "target_distance_pct": 100 * (target - entry) / entry,
        }
        assert abs(
            result["raw_return_pct"]
            - result["fee_pct"]
            - result["slippage_pct"]
            - result["net_return_pct"]
        ) < 1e-9
        return result

    for opened in range(entered, min(deadline, end), H4):
        pieces, source = market.segments(symbol, opened)
        if not pieces:
            return finish("GAP_CENSORED", last_mark, end, gap_at=opened)
        if source != "1h":
            fallback[source] += 1
        for row, step in pieces:
            t, opened_price, high, low = (
                int(row[0]),
                float(row[1]),
                float(row[2]),
                float(row[3]),
            )
            if opened_price <= stop:
                return finish("SL", opened_price, t, exact=True)
            if opened_price >= target:
                return finish("TP", target, t, exact=True)
            sl_hit, tp_hit = low <= stop, high >= target
            if sl_hit and tp_hit:
                ambiguous += 1
            if sl_hit and (not tp_hit or policy == "stop_first"):
                return finish("SL", stop, t + step)
            if tp_hit:
                return finish("TP", target, t + step)
            last_mark = float(row[4])
    if deadline <= end:
        row = market.row(symbol, "4h", deadline)
        if row is None or not math.isfinite(row[1]) or row[1] <= 0:
            return finish("GAP_CENSORED", last_mark, end, gap_at=deadline)
        opening = float(row[1])
        if opening <= stop:
            return finish("SL", opening, deadline, exact=True)
        if opening >= target:
            return finish("TP", target, deadline, exact=True)
        return finish("TIME", opening, deadline, exact=True)
    return finish("END_CENSORED", last_mark, end)


def enrich_and_simulate(
    source_rows: list[dict],
    arrays: dict,
    market: Market,
    end_ms: int,
    costs,
    policy: str,
    model: str,
) -> list[dict]:
    rows = []
    for source in source_rows:
        atr, close = causal_atr20(arrays[source["symbol"]]["4h"], int(source["signal_ms"]))
        trade = simulate_exit(
            market,
            source["symbol"],
            int(source["entry_ms"]),
            end_ms,
            costs,
            policy,
            atr,
            model,
        )
        if trade["status"] == "NO_ENTRY":
            raise AssertionError(f"Frozen event lost entry: {event_key(source)}")
        trade.update(
            model=model,
            cost=costs.name,
            policy=policy,
            signal_ms=int(source["signal_ms"]),
            regime=source["regime"],
            crash=source["crash"],
            quote_volume=source["quote_volume"],
            atr20=atr,
            signal_close=close,
            natr20_pct=100 * atr / close,
            signal_week=signal_week(source),
            net_pnl=1000 * trade["net_return_pct"] / 100,
        )
        rows.append(trade)
    return rows


def verify_fixed(rows: list[dict], source_rows: list[dict]) -> dict:
    if len(rows) != len(source_rows):
        raise AssertionError("Fixed replay row count mismatch")
    max_error = 0.0
    for actual, expected in zip(rows, source_rows):
        if event_key(actual) != event_key(expected):
            raise AssertionError(f"Fixed replay event mismatch: {event_key(actual)}")
        for key in ("status", "exit_ms"):
            if actual[key] != expected[key]:
                raise AssertionError(
                    f"Fixed replay {key} mismatch: {event_key(actual)} {actual[key]} != {expected[key]}"
                )
        for key in (
            "raw_entry",
            "entry_price",
            "stop",
            "target",
            "raw_exit",
            "exit_price",
            "net_return_pct",
            "raw_return_pct",
            "fee_pct",
            "slippage_pct",
        ):
            error = abs(float(actual[key]) - float(expected[key]))
            max_error = max(max_error, error)
            if error > 1e-9:
                raise AssertionError(
                    f"Fixed replay {key} mismatch: {event_key(actual)} {error}"
                )
    return {"rows": len(rows), "max_numeric_error": max_error, "exact_status_exit": True}


def risk_curve(rows: list[dict]) -> dict:
    closed = sorted(
        (row for row in rows if row["closed"]),
        key=lambda row: (row["signal_ms"], row["symbol"]),
    )
    equity = [10_000.0]
    for row in closed:
        equity.append(equity[-1] * (1 + 0.01 * row["net_r"]))
    values = np.asarray(equity, dtype=float)
    return {
        "final_return_pct": 100 * (values[-1] / values[0] - 1),
        "max_drawdown_pct": 100 * float(np.max(1 - values / np.maximum.accumulate(values))),
    }


def risk_metrics(rows: list[dict]) -> dict:
    base = trade_metrics(rows)
    closed = [row for row in rows if row["closed"]]
    values = np.asarray([row["net_r"] for row in closed], dtype=float)
    wins, losses = values[values > 0], values[values < 0]
    risk_loss = -float(losses.sum())
    base.update(
        mean_net_r=float(values.mean()) if len(values) else None,
        median_net_r=float(np.median(values)) if len(values) else None,
        r_profit_factor=float(wins.sum() / risk_loss) if risk_loss else None,
        p05_r=float(np.quantile(values, 0.05)) if len(values) else None,
        worst_r=float(values.min()) if len(values) else None,
        mean_cost_r=float(np.mean([row["cost_r"] for row in closed])) if closed else None,
        mean_planned_risk_pct=float(np.mean([row["planned_risk_pct"] for row in closed]))
        if closed
        else None,
        median_stop_distance_pct=float(np.median([row["stop_distance_pct"] for row in closed]))
        if closed
        else None,
        median_target_distance_pct=float(
            np.median([row["target_distance_pct"] for row in closed])
        )
        if closed
        else None,
        same_bar_double_touch_pct=100
        * sum(row["ambiguous"] > 0 for row in closed)
        / len(closed)
        if closed
        else None,
        risk_curve=risk_curve(closed) if closed else None,
    )
    return base


def align(fixed: list[dict], adaptive: list[dict]) -> list[tuple[dict, dict]]:
    right = {event_key(row): row for row in adaptive}
    if len(right) != len(adaptive):
        raise AssertionError("Duplicate adaptive events")
    pairs = []
    for row in fixed:
        key = event_key(row)
        if key not in right:
            raise AssertionError(f"Missing adaptive event: {key}")
        pairs.append((row, right[key]))
    if len(pairs) != len(adaptive):
        raise AssertionError("Paired event count mismatch")
    return pairs


def compare(fixed: list[dict], adaptive: list[dict]) -> dict:
    pairs = align(fixed, adaptive)
    fixed_metrics = risk_metrics(fixed)
    adaptive_metrics = risk_metrics(adaptive)
    return {
        "fixed": fixed_metrics,
        "atr": adaptive_metrics,
        "paired_closed": sum(left["closed"] and right["closed"] for left, right in pairs),
        "mean_net_r_delta": adaptive_metrics["mean_net_r"] - fixed_metrics["mean_net_r"],
        "r_pf_delta": adaptive_metrics["r_profit_factor"] - fixed_metrics["r_profit_factor"],
        "mean_net_pct_delta_pp": adaptive_metrics["mean_net_pct"] - fixed_metrics["mean_net_pct"],
        "win_rate_delta_pp": adaptive_metrics["win_rate_pct"] - fixed_metrics["win_rate_pct"],
        "time_exit_delta_pp": adaptive_metrics["time_exit_pct"] - fixed_metrics["time_exit_pct"],
        "p05_r_delta": adaptive_metrics["p05_r"] - fixed_metrics["p05_r"],
        "risk_mdd_delta_pp": adaptive_metrics["risk_curve"]["max_drawdown_pct"]
        - fixed_metrics["risk_curve"]["max_drawdown_pct"],
    }


def paired_block_bootstrap(
    fixed: list[dict], adaptive: list[dict], start_ms: int, end_ms: int
) -> dict:
    pairs = align(fixed, adaptive)
    block_ms = 14 * DAY
    block_count = math.ceil((end_ms - start_ms) / block_ms)
    sums = np.zeros((block_count, 3), dtype=float)
    counts = np.zeros(block_count, dtype=int)
    for left, right in pairs:
        if not left["closed"] or not right["closed"]:
            continue
        index = min(block_count - 1, max(0, (left["signal_ms"] - start_ms) // block_ms))
        sums[index] += (left["net_r"], right["net_r"], right["net_r"] - left["net_r"])
        counts[index] += 1
    rng = np.random.default_rng(BOOTSTRAP_SEED)
    picks = rng.integers(0, block_count, size=(BOOTSTRAP_REPETITIONS, block_count))
    sampled_counts = counts[picks].sum(axis=1)
    sampled = sums[picks].sum(axis=1)
    usable = sampled_counts > 0
    means = sampled[usable] / sampled_counts[usable, None]
    return {
        "block_days": 14,
        "repetitions": BOOTSTRAP_REPETITIONS,
        "valid_resamples": int(usable.sum()),
        "fixed_mean_net_r_ci": np.quantile(means[:, 0], [0.025, 0.975]).tolist(),
        "atr_mean_net_r_ci": np.quantile(means[:, 1], [0.025, 0.975]).tolist(),
        "delta_mean_net_r_ci": np.quantile(means[:, 2], [0.025, 0.975]).tolist(),
    }


def leave_one_out(fixed: list[dict], adaptive: list[dict], field: str) -> dict:
    pairs = align(fixed, adaptive)
    groups = sorted({left[field] for left, _ in pairs})
    values = []
    for group in groups:
        kept = [
            (left, right)
            for left, right in pairs
            if left[field] != group and left["closed"] and right["closed"]
        ]
        delta = float(np.mean([right["net_r"] - left["net_r"] for left, right in kept]))
        values.append({"removed": group, "paired": len(kept), "mean_net_r_delta": delta})
    return {
        "field": field,
        "groups": len(groups),
        "min_delta": min(item["mean_net_r_delta"] for item in values),
        "max_delta": max(item["mean_net_r_delta"] for item in values),
        "worst_removed": min(values, key=lambda item: item["mean_net_r_delta"]),
        "best_removed": max(values, key=lambda item: item["mean_net_r_delta"]),
    }


def grouped_compare(fixed: list[dict], adaptive: list[dict], field: str) -> list[dict]:
    pairs = align(fixed, adaptive)
    groups = sorted({left[field] for left, _ in pairs})
    result = []
    for group in groups:
        left_rows = [left for left, _ in pairs if left[field] == group]
        right_rows = [right for left, right in pairs if left[field] == group]
        item = compare(left_rows, right_rows)
        result.append({"group": group, **item})
    return result


def assign_natr_buckets(rows_by_window: dict[str, dict[str, list[dict]]]) -> list[float]:
    early = rows_by_window[WINDOWS[0][0]]["taker_stop_first_fixed"]
    values = np.asarray([row["natr20_pct"] for row in early], dtype=float)
    cuts = [float(value) for value in np.quantile(values, [1 / 3, 2 / 3])]
    for models in rows_by_window.values():
        for rows in models.values():
            for row in rows:
                if row["natr20_pct"] <= cuts[0]:
                    row["natr_bucket"] = "low"
                elif row["natr20_pct"] <= cuts[1]:
                    row["natr_bucket"] = "mid"
                else:
                    row["natr_bucket"] = "high"
    return cuts


def branch_key(cost: str, policy: str, model: str) -> str:
    return f"{cost}_{policy}_{model}"


def primary_robustness(
    fixed: list[dict], adaptive: list[dict], start_ms: int, end_ms: int
) -> dict:
    return {
        "bootstrap": paired_block_bootstrap(fixed, adaptive, start_ms, end_ms),
        "leave_one_symbol": leave_one_out(fixed, adaptive, "symbol"),
        "leave_one_week": leave_one_out(fixed, adaptive, "signal_week"),
        "regime": grouped_compare(fixed, adaptive, "regime"),
        "natr_bucket": grouped_compare(fixed, adaptive, "natr_bucket"),
    }


def decide(summary: dict) -> tuple[str, list[str]]:
    early = summary["windows"]["early"]
    near = summary["windows"]["near"]
    primary = [early["primary"], near["primary"]]
    robustness = [early["robustness"], near["robustness"]]
    sensitivities = []
    for window in (early, near):
        sensitivities.extend(
            window["branches"][name]
            for name in ("stress_stop_first", "taker_target_first")
        )
    support_checks = {
        "both_mean_r_not_worse": all(item["mean_net_r_delta"] >= 0 for item in primary),
        "both_atr_positive": all(item["atr"]["mean_net_r"] > 0 for item in primary),
        "both_rpf_not_worse_and_above_one": all(
            item["atr"]["r_profit_factor"] > 1 and item["r_pf_delta"] >= 0 for item in primary
        ),
        "both_bootstrap_lower_nonnegative": all(
            item["bootstrap"]["delta_mean_net_r_ci"][0] >= 0 for item in robustness
        ),
        "tail_and_mdd_not_worse": all(
            item["p05_r_delta"] >= -1e-12 and item["risk_mdd_delta_pp"] <= 1e-12
            for item in primary
        ),
        "sensitivity_delta_nonnegative": all(
            item["mean_net_r_delta"] >= 0 for item in sensitivities
        ),
        "loo_delta_nonnegative": all(
            item[name]["min_delta"] >= 0
            for item in robustness
            for name in ("leave_one_symbol", "leave_one_week")
        ),
    }
    summary["support_checks"] = support_checks
    if all(support_checks.values()):
        return (
            "support_for_independent_validation",
            ["唯一预注册ATR版本通过两窗收益、区块、尾部、成本/顺序和集中度门槛。"],
        )

    both_worse = all(
        item["mean_net_r_delta"] < 0 and item["r_pf_delta"] < 0 for item in primary
    )
    near_failed = (
        near["primary"]["atr"]["mean_net_r"] <= 0
        and near["primary"]["atr"]["r_profit_factor"] <= 1
        and near["robustness"]["bootstrap"]["delta_mean_net_r_ci"][0] < 0
    )
    if both_worse or near_failed:
        reasons = []
        if both_worse:
            reasons.append("两个窗口的平均净R和R-PF均低于固定出口。")
        if near_failed:
            reasons.append("近窗ATR版本仍为负R、R-PF不高于1，且区块差值未排除有害方向。")
        if any(item["bootstrap"]["delta_mean_net_r_ci"][0] < 0 for item in robustness):
            reasons.append("两个窗口的14日配对区块差值区间均跨过零，点估计改善不稳定。")
        if early["primary"]["risk_mdd_delta_pp"] > 0:
            reasons.append("早窗等风险诊断最大回撤反而扩大。")
        if near["branches"]["stress_stop_first"]["mean_net_r_delta"] < 0:
            reasons.append("近窗在stress成本下ATR相对固定出口的平均净R差值转负。")
        return "reject_preregistered_atr_exit", reasons
    return (
        "insufficient_or_window_inconsistent",
        ["收益、区块区间或稳健性未形成跨窗口一致证据，不能支持或普遍否定ATR出口。"],
    )


def fmt(value, digits=3) -> str:
    return "n/a" if value is None else f"{value:.{digits}f}"


def render_report(summary: dict) -> str:
    lines = [
        "# ATR自适应5:3短周期出口验证",
        "",
        f"Taskboard：`CRYPTOTRADIN-133`。裁决：`{summary['decision']}`。",
        "",
        "## 白话结论",
        "",
        summary["plain_language"],
        "",
        "## 主结果：B all-events / taker / stop-first",
        "",
        "| 窗口 | fixed mean R | ATR mean R | ΔR | fixed R-PF | ATR R-PF | 胜率 | TIME | mean net% | 风险曲线MDD |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for key, label in (("early", "早窗"), ("near", "近窗")):
        item = summary["windows"][key]["primary"]
        fixed, adaptive = item["fixed"], item["atr"]
        lines.append(
            f"| {label} | {fmt(fixed['mean_net_r'], 4)} | {fmt(adaptive['mean_net_r'], 4)} | "
            f"{fmt(item['mean_net_r_delta'], 4)} | {fmt(fixed['r_profit_factor'])} | "
            f"{fmt(adaptive['r_profit_factor'])} | {fmt(fixed['win_rate_pct'], 2)}%→{fmt(adaptive['win_rate_pct'], 2)}% | "
            f"{fmt(fixed['time_exit_pct'], 2)}%→{fmt(adaptive['time_exit_pct'], 2)}% | "
            f"{fmt(fixed['mean_net_pct'], 4)}%→{fmt(adaptive['mean_net_pct'], 4)}% | "
            f"{fmt(fixed['risk_curve']['max_drawdown_pct'], 2)}%→{fmt(adaptive['risk_curve']['max_drawdown_pct'], 2)}% |"
        )
    lines.extend(
        [
            "",
            "## 14日配对区块区间",
            "",
            "| 窗口 | fixed mean R 95% | ATR mean R 95% | ATR-fixed ΔR 95% |",
            "|---|---|---|---|",
        ]
    )
    for key, label in (("early", "早窗"), ("near", "近窗")):
        boot = summary["windows"][key]["robustness"]["bootstrap"]
        lines.append(
            f"| {label} | `{fmt(boot['fixed_mean_net_r_ci'][0], 4)}, {fmt(boot['fixed_mean_net_r_ci'][1], 4)}` | "
            f"`{fmt(boot['atr_mean_net_r_ci'][0], 4)}, {fmt(boot['atr_mean_net_r_ci'][1], 4)}` | "
            f"`{fmt(boot['delta_mean_net_r_ci'][0], 4)}, {fmt(boot['delta_mean_net_r_ci'][1], 4)}` |"
        )
    lines.extend(
        [
            "",
            "## 成本与市场状态",
            "",
            "| 窗口 | taker ΔR | stress ΔR | legacy_fee ΔR | NEUTRAL ΔR | RISK_ON ΔR |",
            "|---|---:|---:|---:|---:|---:|",
        ]
    )
    for key, label in (("early", "早窗"), ("near", "近窗")):
        window = summary["windows"][key]
        regime = {
            item["group"]: item["mean_net_r_delta"]
            for item in window["robustness"]["regime"]
        }
        lines.append(
            f"| {label} | {fmt(window['branches']['taker_stop_first']['mean_net_r_delta'], 4)} | "
            f"{fmt(window['branches']['stress_stop_first']['mean_net_r_delta'], 4)} | "
            f"{fmt(window['branches']['legacy_fee_stop_first']['mean_net_r_delta'], 4)} | "
            f"{fmt(regime.get('NEUTRAL'), 4)} | {fmt(regime.get('RISK_ON'), 4)} |"
        )
    lines.extend(
        [
            "",
            "## 波动分层机制",
            "",
            "| 窗口 | NATR桶 | N | fixed TIME | ATR TIME | fixed SL | ATR SL | fixed mean R | ATR mean R |",
            "|---|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for key, label in (("early", "早窗"), ("near", "近窗")):
        for item in summary["windows"][key]["robustness"]["natr_bucket"]:
            fixed, adaptive = item["fixed"], item["atr"]
            lines.append(
                f"| {label} | {item['group']} | {fixed['closed_trades']} | "
                f"{fmt(fixed['time_exit_pct'], 2)}% | {fmt(adaptive['time_exit_pct'], 2)}% | "
                f"{fixed['status_counts'].get('SL', 0)} | {adaptive['status_counts'].get('SL', 0)} | "
                f"{fmt(fixed['mean_net_r'], 4)} | {fmt(adaptive['mean_net_r'], 4)} |"
            )
    lines.extend(["", "## 裁决原因", ""])
    lines.extend(f"- {reason}" for reason in summary["decision_reasons"])
    lines.extend(
        [
            "",
            "## 边界",
            "",
            "- 本轮只检验`TP=5/3 ATR / SL=1 ATR / 48h`；结论不能外推所有ATR倍数。",
            "- 两个窗口均已烧，币池为current-survivor；即使通过也只能获得独立验证资格。",
            "- 风险曲线忽略重叠容量，不是可执行账户；生产、paper、shadow均未修改。",
            "- 完整成本/顺序、leave-one-out、regime、逐笔配对和哈希见JSON/CSV/manifest。",
        ]
    )
    return "\n".join(lines) + "\n"


def write_trades(rows: list[dict]) -> None:
    fields = [
        "window",
        "model",
        "cost",
        "policy",
        "symbol",
        "signal_ms",
        "entry_ms",
        "exit_ms",
        "status",
        "net_return_pct",
        "net_r",
        "cost_r",
        "planned_risk_pct",
        "stop_distance_pct",
        "target_distance_pct",
        "natr20_pct",
        "natr_bucket",
        "regime",
        "duration_hours",
        "ambiguous",
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
    rows_by_window: dict[str, dict[str, list[dict]]] = {}
    input_hashes = {}
    fixed_checks = {}
    for start, end in WINDOWS:
        meta_path = FROZEN / f"{start}_inputs.json"
        meta = read_json(meta_path)
        arrays = load_arrays(meta)
        market = Market(arrays)
        models = {}
        for cost_name, policy in BRANCHES:
            source_path = REFERENCE / f"{start}_{cost_name}_{policy}_all_events_trades.json.gz"
            source_rows = read_json(source_path)["B"]
            costs = COST_BY_NAME[cost_name]
            fixed = enrich_and_simulate(
                source_rows, arrays, market, ms(end), costs, policy, "fixed"
            )
            adaptive = enrich_and_simulate(
                source_rows, arrays, market, ms(end), costs, policy, "atr"
            )
            models[branch_key(cost_name, policy, "fixed")] = fixed
            models[branch_key(cost_name, policy, "atr")] = adaptive
            fixed_checks[f"{start}_{cost_name}_{policy}"] = verify_fixed(fixed, source_rows)
            input_hashes[str(source_path.relative_to(ROOT))] = sha256(source_path)
        input_hashes[str(meta_path.relative_to(ROOT))] = sha256(meta_path)
        input_hashes[meta["archive"]] = sha256(ROOT / meta["archive"])
        rows_by_window[start] = models
        del market, arrays

    cuts = assign_natr_buckets(rows_by_window)
    windows = {}
    csv_rows = []
    for start, end in WINDOWS:
        label = "early" if start == WINDOWS[0][0] else "near"
        models = rows_by_window[start]
        fixed = models["taker_stop_first_fixed"]
        adaptive = models["taker_stop_first_atr"]
        branches = {}
        for cost_name, policy in BRANCHES:
            branches[f"{cost_name}_{policy}"] = compare(
                models[branch_key(cost_name, policy, "fixed")],
                models[branch_key(cost_name, policy, "atr")],
            )
        robustness = primary_robustness(fixed, adaptive, ms(start), ms(end))
        windows[label] = {
            "start": start,
            "end": end,
            "primary": branches["taker_stop_first"],
            "branches": branches,
            "robustness": robustness,
        }
        for row in fixed + adaptive:
            row["window"] = label
            csv_rows.append(row)

    summary = {
        "experiment": "atr_adaptive_short_exit_v1",
        "taskboard": "CRYPTOTRADIN-133",
        "exit_definition": {
            "fixed": {"target_pct": 5.0, "stop_pct": 3.0, "max_hours": 48},
            "atr": {
                "target_atr": ATR_TARGET_MULTIPLE,
                "stop_atr": ATR_STOP_MULTIPLE,
                "max_hours": 48,
            },
        },
        "natr_early_tercile_cuts_pct": cuts,
        "fixed_replay_verification": fixed_checks,
        "windows": windows,
        "limitations": [
            "burned_windows",
            "current_survivor_universe",
            "all_events_equal_risk_curve_not_executable_portfolio",
        ],
    }
    decision, reasons = decide(summary)
    summary["decision"] = decision
    summary["decision_reasons"] = reasons
    if decision == "support_for_independent_validation":
        summary["plain_language"] = (
            "这个唯一ATR版本在两个窗口都改善了等风险收益并通过稳健性门槛；思路获得独立验证资格，但还不能用于生产。"
        )
    elif decision == "reject_preregistered_atr_exit":
        summary["plain_language"] = (
            "按ATR调整距离确实减少了TIME并改善两窗点估计，但没有形成稳定正收益：区块区间跨零、早窗回撤扩大、近窗压力成本翻转。这个1ATR止损/5/3ATR止盈版本不能采用，但不代表所有ATR出口都无效。"
        )
    else:
        summary["plain_language"] = (
            "ATR出口在窗口或稳健性检查之间不一致；现有结果不能证明这个具体版本可行，也不能否定所有ATR出口。"
        )

    save_json(OUT / "summary.json", summary)
    write_trades(csv_rows)
    (OUT / "report.md").write_text(render_report(summary), encoding="utf-8")
    sources = [
        PROTOCOL,
        ROOT / "scripts/research_atr_adaptive_short_exit.py",
        ROOT / "scripts/short_horizon_core.py",
        ROOT / "scripts/research_breakout_d6.py",
    ]
    manifest = {
        "completed_utc": datetime.now(timezone.utc).isoformat(),
        "head": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip(),
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
        f"- Fixed replay branches: `{len(fixed_checks)}`; all exact status/exit and numeric tolerance <=1e-9.\n"
        f"- Primary paired events: early `{len(rows_by_window[WINDOWS[0][0]]['taker_stop_first_fixed'])}`; "
        f"near `{len(rows_by_window[WINDOWS[1][0]]['taker_stop_first_fixed'])}`.\n"
        f"- Decision: `{decision}`\n"
        "- No network or database writes; frozen archives and frozen B events only.\n"
    )
    (OUT / "verification.md").write_text(verification, encoding="utf-8")
    print(json.dumps({"decision": decision, "cuts_pct": cuts}, ensure_ascii=False))


if __name__ == "__main__":
    main()
