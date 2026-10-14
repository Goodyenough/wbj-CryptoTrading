"""Diagnose whether fixed +5%/-3%/48h exits fit a stable NATR20 range.

This is the preregistered CRYPTOTRADIN-132 read-only diagnostic. It reuses
frozen short-horizon B all-events inputs and never writes the database or
production configuration.
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

from research_breakout_d6 import (  # noqa: E402
    full_path_quality,
    load_arrays,
    natr20,
    path_summary,
    read_json,
    save_json,
    sha256,
)
from short_horizon_core import DAY, H4, Market, trade_metrics  # noqa: E402


FROZEN = ROOT / "reports/2026-10-13/short_horizon_entry_v1"
REFERENCE = ROOT / "reports/2026-10-13/short_horizon_entry_v1_cashfix"
PROTOCOL = ROOT / "reports/2026-10-14/fixed_exit_volatility_fit_protocol_v1.md"
OUT = ROOT / "reports/2026-10-14/fixed_exit_volatility_fit_v1"
WINDOWS = (("2024-07-01", "2025-06-01"), ("2025-06-01", "2026-06-01"))
BRANCHES = tuple(
    (cost, policy)
    for cost in ("taker", "stress", "legacy_fee")
    for policy in ("stop_first", "target_first")
)
PRIMARY = ("taker", "stop_first")
SELECTORS = (
    ("low",),
    ("mid",),
    ("high",),
    ("low", "mid"),
    ("mid", "high"),
)
BOOTSTRAP_REPETITIONS = 2000
BOOTSTRAP_SEED = 20261014


def ms(value: str) -> int:
    return int(datetime.fromisoformat(value).replace(tzinfo=timezone.utc).timestamp() * 1000)


def week(row: dict) -> str:
    return datetime.fromtimestamp(row["entry_ms"] / 1000, timezone.utc).strftime("%G-W%V")


def bucket(value: float, cuts: tuple[float, float]) -> str:
    if value <= cuts[0]:
        return "low"
    if value <= cuts[1]:
        return "mid"
    return "high"


def early_cuts(rows: list[dict]) -> tuple[float, float]:
    values = np.asarray([row["natr20_pct"] for row in rows if row.get("closed")], dtype=float)
    if not len(values) or not np.isfinite(values).all():
        raise ValueError("No finite closed-trade NATR20 values")
    return tuple(float(value) for value in np.quantile(values, [1 / 3, 2 / 3]))


def enrich(rows: list[dict], arrays: dict, market: Market, end_ms: int, policy: str) -> list[dict]:
    answer = []
    for raw in rows:
        row = dict(raw)
        signal = int(row["signal_ms"])
        bars = arrays[row["symbol"]]["4h"]
        n = int(np.searchsorted(bars[:, 0], signal))
        if n < 21 or int(bars[n - 1, 0]) != signal - H4:
            raise ValueError(f"Missing causal signal history: {row['symbol']} {signal}")
        value = natr20(bars, n)
        if not math.isfinite(value) or value <= 0:
            raise ValueError(f"Invalid NATR20: {row['symbol']} {signal}")
        row.update(
            natr20_pct=value,
            tp_atr=5.0 / value,
            sl_atr=3.0 / value,
            signal_week=week(row),
        )
        row.update(full_path_quality(market, row, end_ms, policy))
        answer.append(row)
    return answer


def apply_cuts(rows: list[dict], cuts: tuple[float, float]) -> None:
    for row in rows:
        row["natr_bucket"] = bucket(row["natr20_pct"], cuts)


def selector_name(labels: tuple[str, ...] | None) -> str | None:
    return "+".join(labels) if labels else None


def select_rows(rows: list[dict], labels: tuple[str, ...] | None) -> list[dict]:
    return list(rows) if labels is None else [row for row in rows if row["natr_bucket"] in labels]


def sequence_mdd(rows: list[dict]) -> float | None:
    closed = sorted((row for row in rows if row["closed"]), key=lambda row: (row["entry_ms"], row["symbol"]))
    if not closed:
        return None
    equity = 10_000.0 + np.cumsum([row["net_pnl"] for row in closed])
    equity = np.concatenate(([10_000.0], equity))
    return 100 * float(np.max(1 - equity / np.maximum.accumulate(equity)))


def metrics(rows: list[dict]) -> dict:
    result = trade_metrics(rows)
    closed = [row for row in rows if row["closed"]]
    natr = np.asarray([row["natr20_pct"] for row in closed], dtype=float)
    tp_atr = np.asarray([row["tp_atr"] for row in closed], dtype=float)
    sl_atr = np.asarray([row["sl_atr"] for row in closed], dtype=float)
    result.update(
        symbols=len({row["symbol"] for row in closed}),
        weeks=len({row["signal_week"] for row in closed}),
        diagnostic_sequence_mdd_pct=sequence_mdd(closed),
        same_bar_double_touch_pct=(
            100 * sum(row.get("ambiguous", 0) > 0 for row in closed) / len(closed) if closed else None
        ),
        natr20_mean_pct=float(natr.mean()) if len(natr) else None,
        natr20_median_pct=float(np.median(natr)) if len(natr) else None,
        tp_atr_median=float(np.median(tp_atr)) if len(tp_atr) else None,
        sl_atr_median=float(np.median(sl_atr)) if len(sl_atr) else None,
        path=path_summary(closed),
    )
    return result


def compare(baseline_rows: list[dict], chosen_rows: list[dict]) -> dict:
    base = metrics(baseline_rows)
    chosen = metrics(chosen_rows)
    base_n = base["closed_trades"]
    chosen_n = chosen["closed_trades"]
    return {
        "baseline": base,
        "selected": chosen,
        "retention_pct": 100 * chosen_n / base_n if base_n else None,
        "win_rate_delta_pp": chosen["win_rate_pct"] - base["win_rate_pct"] if chosen_n else None,
        "mean_net_delta_pp": chosen["mean_net_pct"] - base["mean_net_pct"] if chosen_n else None,
        "pf_delta": chosen["profit_factor"] - base["profit_factor"]
        if chosen_n and chosen["profit_factor"] is not None and base["profit_factor"] is not None
        else None,
        "tail_p05_delta_pp": chosen["tail_p05_pct"] - base["tail_p05_pct"] if chosen_n else None,
        "sequence_mdd_delta_pp": chosen["diagnostic_sequence_mdd_pct"] - base["diagnostic_sequence_mdd_pct"]
        if chosen_n else None,
    }


def pf_not_worse(result: dict) -> bool:
    selected = result["selected"]
    baseline = result["baseline"]
    if selected["profit_factor"] is None:
        return bool(selected["avg_win_pct"] is not None and selected["avg_loss_pct"] is None)
    if baseline["profit_factor"] is None:
        return False
    return selected["profit_factor"] >= baseline["profit_factor"]


def early_qualifies(result: dict) -> bool:
    selected = result["selected"]
    return bool(
        selected["closed_trades"]
        and result["retention_pct"] >= 30
        and result["win_rate_delta_pp"] >= 5
        and result["mean_net_delta_pp"] >= 0
        and pf_not_worse(result)
        and result["tail_p05_delta_pp"] >= -1e-12
    )


def choose_selector(rows: list[dict]) -> tuple[tuple[str, ...] | None, list[dict]]:
    results = []
    for order, labels in enumerate(SELECTORS):
        result = compare(rows, select_rows(rows, labels))
        result.update(selector=selector_name(labels), labels=list(labels), early_qualifies=early_qualifies(result))
        results.append(result)
    qualified = [result for result in results if result["early_qualifies"]]
    if not qualified:
        return None, results
    qualified.sort(
        key=lambda item: (
            -item["selected"]["mean_net_pct"],
            -(item["selected"]["profit_factor"] if item["selected"]["profit_factor"] is not None else 1e12),
            -item["win_rate_delta_pp"],
            -item["retention_pct"],
            [selector_name(value) for value in SELECTORS].index(item["selector"]),
        )
    )
    return tuple(qualified[0]["labels"]), results


def block_bootstrap(rows: list[dict], labels: tuple[str, ...], start_ms: int, end_ms: int) -> dict:
    days = (end_ms - start_ms) // DAY
    data = np.zeros((days, 6), dtype=float)
    for row in rows:
        if not row["closed"]:
            continue
        index = (int(row["entry_ms"]) - start_ms) // DAY
        if not 0 <= index < days:
            continue
        chosen = row["natr_bucket"] in labels
        data[index, 0] += row["net_return_pct"]
        data[index, 1] += 1
        data[index, 2] += int(row["net_return_pct"] > 0)
        if chosen:
            data[index, 3] += row["net_return_pct"]
            data[index, 4] += 1
            data[index, 5] += int(row["net_return_pct"] > 0)
    rng = np.random.default_rng(BOOTSTRAP_SEED + start_ms // DAY)
    blocks = math.ceil(days / 14)
    begins = rng.integers(0, max(1, days - 14 + 1), size=(BOOTSTRAP_REPETITIONS, blocks))
    indices = (begins[:, :, None] + np.arange(min(14, days))).reshape(BOOTSTRAP_REPETITIONS, -1)[:, :days]
    samples = data[indices].sum(axis=1)
    samples = samples[(samples[:, 1] > 0) & (samples[:, 4] > 0)]
    base_net = samples[:, 0] / samples[:, 1]
    selected_net = samples[:, 3] / samples[:, 4]
    base_win = 100 * samples[:, 2] / samples[:, 1]
    selected_win = 100 * samples[:, 5] / samples[:, 4]
    q = lambda values: np.quantile(values, [0.025, 0.975]).tolist()
    return {
        "valid_resamples": len(samples),
        "block_days": 14,
        "baseline_mean_net_ci": q(base_net),
        "selected_mean_net_ci": q(selected_net),
        "mean_net_delta_ci": q(selected_net - base_net),
        "win_rate_delta_ci": q(selected_win - base_win),
    }


def leave_one_out(rows: list[dict], labels: tuple[str, ...], dimension: str) -> dict:
    key = (lambda row: row["symbol"]) if dimension == "symbol" else (lambda row: row["signal_week"])
    outputs = []
    for removed in sorted({key(row) for row in rows if row["closed"]}):
        remaining = [row for row in rows if key(row) != removed]
        result = compare(remaining, select_rows(remaining, labels))
        outputs.append(
            {
                "removed": removed,
                "retention_pct": result["retention_pct"],
                "win_rate_delta_pp": result["win_rate_delta_pp"],
                "mean_net_delta_pp": result["mean_net_delta_pp"],
            }
        )
    def span(name: str):
        values = [row[name] for row in outputs if row[name] is not None]
        return [min(values), max(values)] if values else None
    return {
        "dimension": dimension,
        "cases": len(outputs),
        "retention_pct_range": span("retention_pct"),
        "win_rate_delta_pp_range": span("win_rate_delta_pp"),
        "mean_net_delta_pp_range": span("mean_net_delta_pp"),
        "robust_nonnegative": all(
            row["win_rate_delta_pp"] >= 0 and row["mean_net_delta_pp"] >= 0 for row in outputs
        ),
        "rows": outputs,
    }


def regime_groups(rows: list[dict], labels: tuple[str, ...]) -> list[dict]:
    result = []
    for regime in sorted({row["regime"] for row in rows if row["closed"]}):
        group = [row for row in rows if row["regime"] == regime]
        result.append({"regime": regime, **compare(group, select_rows(group, labels))})
    return result


def selector_test(result: dict, *, require_positive: bool) -> bool:
    selected = result["selected"]
    return bool(
        result["retention_pct"] >= 30
        and result["win_rate_delta_pp"] >= 5
        and result["mean_net_delta_pp"] >= 0
        and pf_not_worse(result)
        and result["tail_p05_delta_pp"] >= -1e-12
        and (not require_positive or selected["mean_net_pct"] > 0)
    )


def decide(early: dict, near: dict, sensitivities: dict, robustness: dict) -> tuple[str, list[str]]:
    reasons = []
    if early["selector"] is None:
        both_lack = all(
            item["win_rate_delta_pp"] < 5 or item["mean_net_delta_pp"] < 0
            for item in early["selector_candidates"]
        )
        return ("reject_no_early_qualifier" if both_lack else "insufficient_no_early_qualifier", [
            "早窗五个预注册连续选择器均未同时通过胜率、净期望、PF、尾损和保留率门槛。"
        ])
    if not selector_test(near["primary"], require_positive=True):
        reasons.append("早窗选择器原样应用近窗后未通过主门槛。")
    for name in ("early_taker_target_first", "early_stress_stop_first", "near_taker_target_first", "near_stress_stop_first"):
        item = sensitivities[name]
        if item["win_rate_delta_pp"] < 0 or item["mean_net_delta_pp"] < 0:
            reasons.append(f"敏感性分支 {name} 方向反转。")
    for window in ("early", "near"):
        boot = robustness[window]["bootstrap"]
        if boot["mean_net_delta_ci"][0] < 0 or boot["win_rate_delta_ci"][0] < 0:
            reasons.append(f"{window} 14日区块区间跨越有害方向。")
        for dimension in ("symbol", "week"):
            if not robustness[window][f"leave_one_{dimension}"]["robust_nonnegative"]:
                reasons.append(f"{window} {dimension} leave-one-out 发生方向反转。")
        shares = robustness[window]["selected_regime_shares_pct"]
        if shares and max(shares.values()) >= 80:
            reasons.append(f"{window} 选择样本至少80%集中在单一regime。")
    if not reasons:
        return "support_filter_experiment_qualification", ["全部预注册支持门槛通过；仅获得后续固定过滤实验资格。"]
    if (
        early["primary"]["win_rate_delta_pp"] >= 5
        and near["primary"]["win_rate_delta_pp"] >= 5
        and (early["primary"]["mean_net_delta_pp"] < 0 or near["primary"]["mean_net_delta_pp"] < 0)
    ):
        return "reject_win_rate_bought_with_worse_expectancy", reasons
    return "insufficient_or_window_inconsistent", reasons


def load_branch(start: str, cost: str, policy: str) -> list[dict]:
    path = REFERENCE / f"{start}_{cost}_{policy}_all_events_trades.json.gz"
    return read_json(path)["B"]


def fmt(value, digits=3) -> str:
    return "n/a" if value is None else f"{value:.{digits}f}"


def render_report(summary: dict) -> str:
    lines = [
        "# 固定5%/3%短周期出口的波动适配诊断",
        "",
        f"Taskboard：`CRYPTOTRADIN-132`。裁决：`{summary['decision']}`。",
        "",
        "## 白话结论",
        "",
        summary["plain_language"],
        "",
        "## 主结果：taker / stop-first / B all-events",
        "",
        f"早窗NATR三分位固定切点：`{fmt(summary['cuts_pct'][0])}% / {fmt(summary['cuts_pct'][1])}%`；早窗选择器：`{summary['selector'] or '无'}`。",
        "",
        "| 窗口 | 样本 | 选择样本 | 保留率 | 胜率 baseline→selected | 净期望 baseline→selected | PF baseline→selected | P05 baseline→selected |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for key, label in (("early", "早窗"), ("near", "近窗")):
        result = summary["windows"][key]["primary"]
        base, chosen = result["baseline"], result["selected"]
        lines.append(
            f"| {label} | {base['closed_trades']} | {chosen['closed_trades']} | {fmt(result['retention_pct'], 2)}% | "
            f"{fmt(base['win_rate_pct'], 2)}%→{fmt(chosen['win_rate_pct'], 2)}% | "
            f"{fmt(base['mean_net_pct'], 4)}%→{fmt(chosen['mean_net_pct'], 4)}% | "
            f"{fmt(base['profit_factor'], 3)}→{fmt(chosen['profit_factor'], 3)} | "
            f"{fmt(base['tail_p05_pct'], 3)}%→{fmt(chosen['tail_p05_pct'], 3)}% |"
        )
    lines.extend([
        "",
        "## 早窗预注册选择器",
        "",
        "| 选择器 | 保留率 | 胜率变化 | 净期望变化 | PF变化 | P05变化 | 通过 |",
        "|---|---:|---:|---:|---:|---:|---|",
    ])
    for candidate in summary["selector_candidates"]:
        lines.append(
            f"| {candidate['selector']} | {fmt(candidate['retention_pct'], 2)}% | "
            f"{fmt(candidate['win_rate_delta_pp'], 3)}pp | {fmt(candidate['mean_net_delta_pp'], 4)}pp | "
            f"{fmt(candidate['pf_delta'], 3)} | {fmt(candidate['tail_p05_delta_pp'], 3)}pp | "
            f"{'是' if candidate['early_qualifies'] else '否'} |"
        )
    lines.extend(["", "## NATR分组", "", "| 窗口 | 分组 | N | 胜率 | 净期望 | PF | TP/SL/TIME | 同根双触发 |", "|---|---|---:|---:|---:|---:|---|---:|"])
    for key, label in (("early", "早窗"), ("near", "近窗")):
        for group in summary["windows"][key]["buckets"]:
            m = group["metrics"]
            counts = m["status_counts"]
            lines.append(
                f"| {label} | {group['bucket']} | {m['closed_trades']} | {fmt(m['win_rate_pct'], 2)}% | "
                f"{fmt(m['mean_net_pct'], 4)}% | {fmt(m['profit_factor'], 3)} | "
                f"{counts.get('TP', 0)}/{counts.get('SL', 0)}/{counts.get('TIME', 0)} | {fmt(m['same_bar_double_touch_pct'], 2)}% |"
            )
    lines.extend(["", "## 裁决原因", ""])
    lines.extend(f"- {reason}" for reason in summary["decision_reasons"])
    lines.extend([
        "",
        "## 边界",
        "",
        "- 两个窗口均已烧，币池为current-survivor；结果不能直接升级生产。",
        "- 主样本是all-events，诊断性交易序列回撤不是可执行组合MDD。",
        "- 未修改入场、`+5%/-3%/48h`、成本、生产配置、paper或shadow。",
        "- 成本/同根分支和逐笔路径见`summary.json`与`trades.csv`；因早窗无候选过闸，按协议未继续运行候选bootstrap、leave-one-out和regime稳健性。",
    ])
    return "\n".join(lines) + "\n"


def write_csv(rows: list[dict]) -> None:
    fields = [
        "window", "symbol", "signal_ms", "entry_ms", "exit_ms", "status", "net_return_pct",
        "raw_return_pct", "fee_pct", "slippage_pct", "regime", "natr20_pct", "natr_bucket",
        "tp_atr", "sl_atr", "ambiguous", "signal_week", "mfe_48h_pct", "mae_48h_pct",
        "favorable_first", "sl_then_target_48h",
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
    source_files = [PROTOCOL, ROOT / "scripts/diagnose_fixed_exit_volatility_fit.py", ROOT / "scripts/short_horizon_core.py", ROOT / "scripts/research_breakout_d6.py"]
    windows: dict[str, dict] = {}
    all_primary_rows = []
    enriched_by_window: dict[str, dict] = {}
    input_hashes = {}
    for start, end in WINDOWS:
        meta_path = FROZEN / f"{start}_inputs.json"
        meta = read_json(meta_path)
        arrays = load_arrays(meta)
        market = Market(arrays)
        branches = {}
        for cost, policy in BRANCHES:
            path = REFERENCE / f"{start}_{cost}_{policy}_all_events_trades.json.gz"
            input_hashes[str(path.relative_to(ROOT))] = sha256(path)
            branches[f"{cost}_{policy}"] = enrich(read_json(path)["B"], arrays, market, ms(end), policy)
        input_hashes[str(meta_path.relative_to(ROOT))] = sha256(meta_path)
        input_hashes[meta["archive"]] = sha256(ROOT / meta["archive"])
        enriched_by_window[start] = branches
        del market, arrays

    early_rows = enriched_by_window[WINDOWS[0][0]]["taker_stop_first"]
    cuts = early_cuts(early_rows)
    for branches in enriched_by_window.values():
        for rows in branches.values():
            apply_cuts(rows, cuts)
    selector, candidates = choose_selector(early_rows)

    for start, end in WINDOWS:
        key = "early" if start == WINDOWS[0][0] else "near"
        branches = enriched_by_window[start]
        primary_rows = branches["taker_stop_first"]
        chosen = select_rows(primary_rows, selector) if selector else []
        primary = compare(primary_rows, chosen)
        buckets = [
            {"bucket": label, "metrics": metrics(select_rows(primary_rows, (label,)))}
            for label in ("low", "mid", "high")
        ]
        windows[key] = {
            "start": start,
            "end": end,
            "primary": primary,
            "buckets": buckets,
            "branches": {
                branch: compare(rows, select_rows(rows, selector) if selector else [])
                for branch, rows in branches.items()
            },
        }
        for row in primary_rows:
            row["window"] = key
        all_primary_rows.extend(primary_rows)

    early = {"selector": selector_name(selector), "selector_candidates": candidates, "primary": windows["early"]["primary"]}
    near = {"primary": windows["near"]["primary"]}
    if selector:
        sensitivities = {
            "early_taker_target_first": windows["early"]["branches"]["taker_target_first"],
            "early_stress_stop_first": windows["early"]["branches"]["stress_stop_first"],
            "near_taker_target_first": windows["near"]["branches"]["taker_target_first"],
            "near_stress_stop_first": windows["near"]["branches"]["stress_stop_first"],
        }
        robustness = {}
        for key, (start, end) in zip(("early", "near"), WINDOWS):
            rows = enriched_by_window[start]["taker_stop_first"]
            selected = select_rows(rows, selector)
            counts = Counter(row["regime"] for row in selected if row["closed"])
            total = sum(counts.values())
            robustness[key] = {
                "bootstrap": block_bootstrap(rows, selector, ms(start), ms(end)),
                "leave_one_symbol": leave_one_out(rows, selector, "symbol"),
                "leave_one_week": leave_one_out(rows, selector, "week"),
                "regime_groups": regime_groups(rows, selector),
                "selected_regime_shares_pct": {name: 100 * count / total for name, count in counts.items()},
            }
        decision, reasons = decide(early, near, sensitivities, robustness)
    else:
        sensitivities = {}
        robustness = {}
        decision, reasons = decide(early, near, sensitivities, robustness)

    if decision == "support_filter_experiment_qualification":
        plain = "固定5%/3%出口显示出跨窗口稳定的波动适配区间，但只获得后续固定过滤实验资格，不能直接采用。"
    elif decision.startswith("reject"):
        plain = "预注册波动适配规则没有形成可用优势；不能靠NATR过滤稳定提高胜率而不牺牲净期望。"
    else:
        plain = "早窗与近窗或稳健性检查不一致；现有数据不能证明按NATR筛选能可靠改善固定5%/3%策略。"
    summary = {
        "experiment": "fixed_exit_volatility_fit_v1",
        "taskboard": "CRYPTOTRADIN-132",
        "decision": decision,
        "decision_reasons": reasons,
        "plain_language": plain,
        "cuts_pct": list(cuts),
        "selector": selector_name(selector),
        "selector_candidates": candidates,
        "windows": windows,
        "sensitivities": sensitivities,
        "robustness": robustness,
        "limitations": ["burned_windows", "current_survivor_universe", "all_events_not_executable_portfolio"],
    }
    save_json(OUT / "summary.json", summary)
    write_csv(all_primary_rows)
    (OUT / "report.md").write_text(render_report(summary), encoding="utf-8")
    manifest = {
        "completed_utc": datetime.now(timezone.utc).isoformat(),
        "head": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip(),
        "source_sha256": {str(path.relative_to(ROOT)): sha256(path) for path in source_files},
        "input_sha256": input_hashes,
        "outputs": {},
    }
    for name in ("summary.json", "trades.csv", "report.md"):
        manifest["outputs"][name] = sha256(OUT / name)
    save_json(OUT / "run_manifest.json", manifest)
    verification = (
        "# Verification\n\n"
        f"- Protocol SHA256: `{sha256(PROTOCOL)}`\n"
        f"- Early cuts: `{cuts[0]:.8f}% / {cuts[1]:.8f}%`\n"
        f"- Selector: `{selector_name(selector) or 'none'}`\n"
        f"- Decision: `{decision}`\n"
        "- No network or database writes; frozen archives and frozen B outcomes only.\n"
    )
    (OUT / "verification.md").write_text(verification, encoding="utf-8")
    print(json.dumps({"decision": decision, "selector": selector_name(selector), "cuts_pct": cuts}, ensure_ascii=False))


if __name__ == "__main__":
    main()
