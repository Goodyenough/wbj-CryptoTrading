"""Run the preregistered D6 versus C20 short-horizon breakout study.

This harness reuses the frozen inputs and eligibility frames from the prior
short-horizon entry study. It performs no network or database writes and does
not touch production configuration.

Usage: python scripts/research_breakout_d6.py
"""
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime, timezone
import gzip
import hashlib
import json
import math
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from short_horizon_core import (  # noqa: E402
    COSTS,
    DAY,
    H4,
    HOLD,
    Market,
    account_metrics,
    bootstrap,
    new_breakout,
    replay,
    trade_metrics,
    utc,
)


FROZEN = ROOT / "reports/2026-10-13/short_horizon_entry_v1"
REFERENCE = ROOT / "reports/2026-10-13/short_horizon_entry_v1_cashfix"
PROTOCOL = ROOT / "reports/2026-10-13/breakout_d6_protocol_v1.md"
OUT = ROOT / "reports/2026-10-13/breakout_d6_v1"
ARMS = ("C20", "D6")
PRIMARY_COST = "taker"
PRIMARY_POLICY = "stop_first"


def read_json(path: Path):
    if path.suffix == ".gz":
        with gzip.open(path, "rt", encoding="utf-8") as stream:
            return json.load(stream)
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(
        value,
        ensure_ascii=False,
        indent=2,
        allow_nan=False,
        default=lambda x: x.item() if isinstance(x, np.generic) else str(x),
    ) + "\n"
    if path.suffix == ".gz":
        with gzip.open(path, "wt", encoding="utf-8") as stream:
            stream.write(text)
    else:
        path.write_text(text, encoding="utf-8")


def sha256(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def ms(value: str) -> int:
    dt = datetime.fromisoformat(value)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return int(dt.timestamp() * 1000)


def source_hashes() -> dict[str, str]:
    names = (
        "scripts/research_breakout_d6.py",
        "scripts/short_horizon_core.py",
        "reports/2026-10-13/breakout_d6_protocol_v1.md",
    )
    return {name: sha256(ROOT / name) for name in names}


def load_arrays(meta: dict) -> dict[str, dict[str, np.ndarray]]:
    archive = ROOT / meta["archive"]
    if sha256(archive) != meta["archive_sha256"]:
        raise ValueError(f"Frozen archive hash mismatch: {archive}")
    arrays: dict[str, dict[str, np.ndarray]] = defaultdict(dict)
    with np.load(archive, allow_pickle=False) as saved:
        for key in saved.files:
            symbol, interval = key.split("__")
            arrays[symbol][interval] = saved[key]
    return dict(arrays)


def natr20(rows: np.ndarray, n: int) -> float:
    """Mean true range of the latest 20 closed bars, divided by signal close."""
    if n < 21:
        return float("nan")
    bars = rows[n - 20:n]
    previous_close = rows[n - 21:n - 1, 4]
    true_range = np.maximum.reduce(
        (bars[:, 2] - bars[:, 3], np.abs(bars[:, 2] - previous_close),
         np.abs(bars[:, 3] - previous_close))
    )
    return float(100 * np.mean(true_range) / bars[-1, 4])


def bucket(value: float, cuts: tuple[float, float]) -> str:
    if value <= cuts[0]:
        return "low"
    if value <= cuts[1]:
        return "mid"
    return "high"


def build_frames(start: str, arrays: dict[str, dict[str, np.ndarray]]):
    source_path = FROZEN / f"{start}_features.json.gz"
    source = read_json(source_path)
    frames: dict[int, dict] = {}
    event_map: dict[str, list[dict]] = {arm: [] for arm in ARMS}
    recomputed_c20 = 0
    for raw_now, raw_frame in source.items():
        now = int(raw_now)
        frame = {}
        for symbol, raw_feature in raw_frame.items():
            feature = dict(raw_feature)
            rows = arrays[symbol]["4h"]
            n = int(np.searchsorted(rows[:, 0], now))
            if n < 1 or int(rows[n - 1, 0]) != now - H4:
                raise ValueError(f"Missing signal bar: {symbol} {utc(now)}")
            d6 = new_breakout(rows[max(0, n - 8):n], 6)
            c20 = new_breakout(rows[max(0, n - 22):n], 20)
            if c20 != bool(feature["breakout"]):
                raise AssertionError(f"C20 mismatch: {symbol} {utc(now)}")
            recomputed_c20 += int(c20)
            feature["breakout_6"] = d6
            feature["breakout_20"] = c20
            feature["natr20_pct"] = natr20(rows, n)
            frame[symbol] = feature
            if d6:
                event_map["D6"].append({"symbol": symbol, "signal_ms": now,
                                         "natr20_pct": feature["natr20_pct"],
                                         "regime": feature["regime"]})
            if c20:
                event_map["C20"].append({"symbol": symbol, "signal_ms": now,
                                          "natr20_pct": feature["natr20_pct"],
                                          "regime": feature["regime"]})
        frames[now] = frame

    union = {(e["symbol"], e["signal_ms"]): e["natr20_pct"]
             for arm in ARMS for e in event_map[arm]}
    values = np.array([v for v in union.values() if math.isfinite(v)], dtype=float)
    if not len(values):
        raise ValueError(f"No breakout events in {start}")
    cuts = tuple(float(v) for v in np.quantile(values, [1 / 3, 2 / 3]))
    for feature_frame in frames.values():
        for feature in feature_frame.values():
            feature["natr_bucket"] = bucket(feature["natr20_pct"], cuts)
    for events in event_map.values():
        for event in events:
            event["natr_bucket"] = bucket(event["natr20_pct"], cuts)
    checks = {
        "source_features": str(source_path.relative_to(ROOT)),
        "source_features_sha256": sha256(source_path),
        "eligible_frames": len(frames),
        "recomputed_c20_events": recomputed_c20,
        "natr_tercile_cuts_pct": list(cuts),
    }
    return frames, event_map, checks


def event_density(events: list[dict], start_ms: int, end_ms: int) -> dict:
    by_symbol: dict[str, list[int]] = defaultdict(list)
    for event in events:
        by_symbol[event["symbol"]].append(int(event["signal_ms"]))
    intervals = []
    for times in by_symbol.values():
        times.sort()
        intervals.extend((b - a) / 3_600_000 for a, b in zip(times, times[1:]))
    days = (end_ms - start_ms) / DAY
    weeks = {datetime.fromtimestamp(e["signal_ms"] / 1000, timezone.utc).strftime("%G-W%V")
             for e in events}
    return {
        "events": len(events),
        "symbols": len(by_symbol),
        "signal_weeks": len(weeks),
        "events_per_30d": 30 * len(events) / days,
        "mean_inter_event_hours_same_symbol": float(np.mean(intervals)) if intervals else None,
        "median_inter_event_hours_same_symbol": float(np.median(intervals)) if intervals else None,
    }


def event_overlap(event_map: dict[str, list[dict]]) -> dict:
    sets = {arm: {(e["symbol"], e["signal_ms"]) for e in event_map[arm]} for arm in ARMS}
    overlap = sets["D6"] & sets["C20"]
    return {
        "same_symbol_time_events": len(overlap),
        "pct_of_d6": 100 * len(overlap) / len(sets["D6"]) if sets["D6"] else None,
        "pct_of_c20": 100 * len(overlap) / len(sets["C20"]) if sets["C20"] else None,
    }


def benchmark_48h(arrays: dict[str, dict[str, np.ndarray]], entered: int) -> dict:
    values = {}
    for symbol in ("BTCUSDT", "ETHUSDT"):
        rows = arrays[symbol]["4h"]
        i = int(np.searchsorted(rows[:, 0], entered))
        j = int(np.searchsorted(rows[:, 0], entered + HOLD))
        if (i >= len(rows) or j >= len(rows) or int(rows[i, 0]) != entered
                or int(rows[j, 0]) != entered + HOLD):
            values[symbol] = None
        else:
            values[symbol] = float(100 * (rows[j, 1] / rows[i, 1] - 1))
    btc, eth = values["BTCUSDT"], values["ETHUSDT"]
    if btc is None or eth is None:
        label = "incomplete"
    elif btc > 0 and eth > 0:
        label = "both_up"
    elif btc <= 0 and eth <= 0:
        label = "both_down"
    else:
        label = "mixed"
    return {"btc_48h_pct": btc, "eth_48h_pct": eth, "btc_eth_48h": label}


def full_path_quality(market: Market, trade: dict, end: int, policy: str) -> dict:
    """Inspect the complete 48h path without stopping at the simulated exit."""
    entered = int(trade["entry_ms"])
    deadline = entered + HOLD
    if deadline > end:
        return {"path_complete_48h": False}
    stop, target = float(trade["stop"]), float(trade["target"])
    maximum, minimum = float(trade["raw_entry"]), float(trade["raw_entry"])
    stop_order = None
    target_order = None

    def record(kind: str, order: tuple[int, int]):
        nonlocal stop_order, target_order
        if kind == "stop" and stop_order is None:
            stop_order = order
        if kind == "target" and target_order is None:
            target_order = order

    for opened in range(entered, deadline, H4):
        pieces, _source = market.segments(trade["symbol"], opened)
        if not pieces:
            return {"path_complete_48h": False}
        for row, _step in pieces:
            t, opening = int(row[0]), float(row[1])
            high, low = float(row[2]), float(row[3])
            maximum, minimum = max(maximum, high), min(minimum, low)
            if opening <= stop:
                record("stop", (t, 0))
            elif opening >= target:
                record("target", (t, 0))
            sl, tp = low <= stop, high >= target
            if sl and tp:
                first, second = (("stop", "target") if policy == "stop_first"
                                 else ("target", "stop"))
                record(first, (t, 1))
                record(second, (t, 2))
            elif sl:
                record("stop", (t, 1))
            elif tp:
                record("target", (t, 1))

    deadline_row = market.row(trade["symbol"], "4h", deadline)
    if deadline_row is None:
        return {"path_complete_48h": False}
    deadline_open = float(deadline_row[1])
    maximum, minimum = max(maximum, deadline_open), min(minimum, deadline_open)
    if deadline_open <= stop:
        record("stop", (deadline, 0))
    elif deadline_open >= target:
        record("target", (deadline, 0))
    favorable = target_order is not None and (stop_order is None or target_order < stop_order)
    sl_then_target = stop_order is not None and target_order is not None and stop_order < target_order
    entry = float(trade["entry_price"])
    return {
        "path_complete_48h": True,
        "mfe_48h_pct": 100 * (maximum / entry - 1),
        "mae_48h_pct": 100 * (minimum / entry - 1),
        "favorable_first": favorable,
        "target_available_48h": target_order is not None,
        "stop_available_48h": stop_order is not None,
        "sl_then_target_48h": sl_then_target,
    }


def path_summary(rows: list[dict]) -> dict:
    complete = [row for row in rows if row.get("path_complete_48h")]
    if not complete:
        return {"complete": 0}
    mfe = np.array([row["mfe_48h_pct"] for row in complete])
    mae = np.array([row["mae_48h_pct"] for row in complete])
    pct = lambda key: 100 * sum(bool(row[key]) for row in complete) / len(complete)
    return {
        "complete": len(complete),
        "favorable_first_pct": pct("favorable_first"),
        "target_available_48h_pct": pct("target_available_48h"),
        "stop_available_48h_pct": pct("stop_available_48h"),
        "sl_then_target_48h_pct": pct("sl_then_target_48h"),
        "mfe_48h_median_pct": float(np.median(mfe)),
        "mfe_48h_mean_pct": float(np.mean(mfe)),
        "mae_48h_median_pct": float(np.median(mae)),
        "mae_48h_mean_pct": float(np.mean(mae)),
    }


def group_summaries(rows: list[dict]) -> list[dict]:
    groups: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for row in rows:
        dt = datetime.fromtimestamp(row["entry_ms"] / 1000, timezone.utc)
        dimensions = {
            "regime": row["regime"],
            "natr_bucket": row["natr_bucket"],
            "btc_eth_48h": row["btc_eth_48h"],
            "symbol": row["symbol"],
            "week": dt.strftime("%G-W%V"),
        }
        for name, label in dimensions.items():
            groups[name, str(label)].append(row)
    return [
        {"dimension": name, "label": label, **trade_metrics(group),
         "path": path_summary(group)}
        for (name, label), group in sorted(groups.items())
    ]


def contribution_removal(d6: list[dict], c20: list[dict], dimension: str) -> dict:
    def label(row):
        if dimension == "symbol":
            return row["symbol"]
        return datetime.fromtimestamp(row["entry_ms"] / 1000, timezone.utc).strftime("%G-W%V")

    contributions = Counter()
    for row in d6:
        if row["closed"]:
            contributions[label(row)] += row["net_return_pct"]
    removed = max(contributions, key=contributions.get) if contributions else None
    result = {"removed": removed, "d6_contribution_pct_points": contributions.get(removed) if removed else None}
    for arm, rows in (("D6", d6), ("C20", c20)):
        kept = [row for row in rows if removed is None or label(row) != removed]
        result[arm] = trade_metrics(kept)
    return result


def annotate_trades(rows: list[dict], frames: dict[int, dict], arrays: dict,
                    market: Market, end: int, policy: str,
                    quality_cache: dict[tuple, dict]) -> None:
    benchmark_cache = {}
    for row in rows:
        feature = frames[int(row["signal_ms"])][row["symbol"]]
        row["natr20_pct"] = feature["natr20_pct"]
        row["natr_bucket"] = feature["natr_bucket"]
        benchmark_cache.setdefault(row["entry_ms"], benchmark_48h(arrays, row["entry_ms"]))
        row.update(benchmark_cache[row["entry_ms"]])
        key = (row["symbol"], row["entry_ms"], policy)
        if key not in quality_cache:
            quality_cache[key] = full_path_quality(market, row, end, policy)
        row.update(quality_cache[key])


def bootstrap_named(c20: list[dict], d6: list[dict], start: int, end: int) -> dict:
    result = bootstrap(c20, d6, start, end)
    return {
        "c20_ci": result["b_ci"],
        "d6_ci": result["c_ci"],
        "d6_minus_c20_ci": result["delta_ci"],
        "valid_resamples": result["valid_resamples"],
        "block_days": result.get("block_days"),
    }


def verify_reference(start: str, cost: str, policy: str, layer: str,
                     rows: list[dict]) -> int:
    path = REFERENCE / f"{start}_{cost}_{policy}_{layer}_trades.json.gz"
    reference = read_json(path)["C"]
    if len(rows) != len(reference):
        raise AssertionError(f"C20 count mismatch: {start} {cost} {policy} {layer}")
    exact = ("symbol", "signal_ms", "entry_ms", "exit_ms", "status", "closed")
    numeric = ("raw_entry", "entry_price", "raw_exit", "exit_price", "net_return_pct",
               "cash_invested", "quantity", "net_pnl")
    for current, old in zip(rows, reference):
        if any(current[key] != old[key] for key in exact):
            raise AssertionError(f"C20 event mismatch: {start} {cost} {policy} {layer}")
        if any(not np.isclose(current[key], old[key], rtol=1e-12, atol=1e-12)
               for key in numeric):
            raise AssertionError(f"C20 ledger mismatch: {start} {cost} {policy} {layer}")
    return len(rows)


def find_branch(summary: dict, cost: str, policy: str) -> dict:
    return next(branch for branch in summary["branches"]
                if branch["cost"] == cost and branch["policy"] == policy)


def decide(summaries: list[dict]) -> dict:
    window_flags = []
    for summary in summaries:
        primary = find_branch(summary, PRIMARY_COST, PRIMARY_POLICY)["layers"]
        stress = find_branch(summary, "stress", PRIMARY_POLICY)["layers"]["all_events"]
        main = primary["all_events"]
        d6, c20 = main["D6"]["metrics"], main["C20"]["metrics"]
        d6_path, c20_path = main["D6"]["path"], main["C20"]["path"]
        delta_ci = main["bootstrap"]["d6_minus_c20_ci"]
        concentration = main["concentration"]
        symbol_only = primary["symbol_only"]
        path_not_worse = (
            d6_path["favorable_first_pct"] >= c20_path["favorable_first_pct"]
            and d6_path["mfe_48h_median_pct"] >= c20_path["mfe_48h_median_pct"]
        )
        concentration_ok = all(
            item["D6"]["mean_net_pct"] > 0
            and item["D6"]["mean_net_pct"] > item["C20"]["mean_net_pct"]
            for item in concentration.values()
        )
        qualify = all((
            d6["mean_net_pct"] > 0,
            d6["profit_factor"] is not None and d6["profit_factor"] > 1,
            d6["mean_net_pct"] > c20["mean_net_pct"],
            delta_ci is not None and delta_ci[0] > 0,
            path_not_worse,
            stress["D6"]["metrics"]["mean_net_pct"] > 0,
            stress["D6"]["metrics"]["mean_net_pct"] > stress["C20"]["metrics"]["mean_net_pct"],
            symbol_only["D6"]["metrics"]["mean_net_pct"] > 0,
            symbol_only["D6"]["metrics"]["mean_net_pct"] > symbol_only["C20"]["metrics"]["mean_net_pct"],
            concentration_ok,
        ))
        reject_net = d6["mean_net_pct"] <= 0 and d6["mean_net_pct"] <= c20["mean_net_pct"]
        reject_path = (
            d6_path["favorable_first_pct"] <= c20_path["favorable_first_pct"]
            and d6_path["mfe_48h_median_pct"] <= c20_path["mfe_48h_median_pct"]
        )
        window_flags.append({
            "start": summary["start"],
            "qualify": qualify,
            "reject_net": reject_net,
            "reject_path": reject_path,
            "path_improved": (d6_path["favorable_first_pct"] > c20_path["favorable_first_pct"]
                              and d6_path["mfe_48h_median_pct"] > c20_path["mfe_48h_median_pct"]),
            "d6_net_positive": d6["mean_net_pct"] > 0,
        })

    if all(flag["qualify"] for flag in window_flags):
        label = "development_qualified"
        route = "consider_squeeze_only_after_unused_validation"
        plain = "D6在两个开发窗口的净收益和路径质量均通过全部严格门槛；这只授予进入未使用数据或自然前向验证的资格，不代表可以改生产。"
    elif all(flag["reject_net"] for flag in window_flags) or all(flag["reject_path"] for flag in window_flags):
        label = "reject_d6"
        route = "stop_this_d6_definition"
        plain = "D6没有在两个窗口同时改善净期望或入场后路径，否定这一个‘6根4h首次突破＋固定出口’定义；结论不能外推所有更早动能信号。"
    else:
        label = "insufficient"
        if all(flag["path_improved"] and not flag["d6_net_positive"] for flag in window_flags):
            route = "exit_matching_priority"
            plain = "D6的路径质量在两个窗口都改善，但成本后净收益仍未转正；证据不足，下一研究方向应优先检查退出匹配，而不是叠加收缩条件。"
        else:
            route = "no_automatic_next_experiment"
            plain = "净收益、路径质量或窗口稳定性没有同时满足开发资格，也未形成双窗明确否定；按预注册规则归为证据不足，不自动启动下一项实验。"
    return {"label": label, "route": route, "plain_language": plain,
            "window_flags": window_flags}


def fmt(value, digits=3) -> str:
    return "n/a" if value is None else f"{value:.{digits}f}"


def render_report(summaries: list[dict], decision: dict, manifest: dict) -> str:
    result_rows = []
    path_rows = []
    density_rows = []
    sensitivity_rows = []
    regime_rows = []
    for summary in summaries:
        primary = find_branch(summary, PRIMARY_COST, PRIMARY_POLICY)["layers"]
        main = primary["all_events"]
        for arm in ("C20", "D6"):
            metrics = main[arm]["metrics"]
            path = main[arm]["path"]
            density = summary["events"]["density"][arm]
            result_rows.append(
                f"| {summary['start']} | {arm} | {metrics['closed_trades']} | "
                f"{fmt(metrics['mean_net_pct'], 4)}% | {fmt(metrics['profit_factor'])} | "
                f"{fmt(metrics['win_rate_pct'], 2)}% | {metrics['status_counts'].get('TP', 0)} / "
                f"{metrics['status_counts'].get('SL', 0)} / {metrics['status_counts'].get('TIME', 0)} |"
            )
            path_rows.append(
                f"| {summary['start']} | {arm} | {fmt(path['favorable_first_pct'], 2)}% | "
                f"{fmt(path['mfe_48h_median_pct'], 3)}% | {fmt(path['mae_48h_median_pct'], 3)}% | "
                f"{fmt(path['sl_then_target_48h_pct'], 2)}% |"
            )
            density_rows.append(
                f"| {summary['start']} | {arm} | {density['events']} | "
                f"{fmt(density['events_per_30d'], 1)} | {density['signal_weeks']} | "
                f"{fmt(density['median_inter_event_hours_same_symbol'], 1)} |"
            )
        for cost, layer in (("stress", "all_events"), ("taker", "symbol_only"), ("taker", "portfolio")):
            detail = find_branch(summary, cost, PRIMARY_POLICY)["layers"][layer]
            for arm in ("C20", "D6"):
                metric = detail[arm]["metrics"]
                account = detail[arm]["account"]
                sensitivity_rows.append(
                    f"| {summary['start']} | {cost} | {layer} | {arm} | "
                    f"{fmt(metric['mean_net_pct'], 4)}% | "
                    f"{fmt(account['net_return_pct'], 3) + '%' if account else 'n/a'} |"
                )
        for arm in ("C20", "D6"):
            for group in main[arm]["groups"]:
                if group["dimension"] == "regime":
                    regime_rows.append(
                        f"| {summary['start']} | {group['label']} | {arm} | "
                        f"{group['closed_trades']} | {fmt(group['mean_net_pct'], 4)}% | "
                        f"{fmt(group['profit_factor'])} |"
                    )

    ci_rows = []
    concentration_rows = []
    for summary in summaries:
        main = find_branch(summary, PRIMARY_COST, PRIMARY_POLICY)["layers"]["all_events"]
        ci = main["bootstrap"]
        ci_rows.append(
            f"| {summary['start']} | [{fmt(ci['c20_ci'][0])}, {fmt(ci['c20_ci'][1])}] | "
            f"[{fmt(ci['d6_ci'][0])}, {fmt(ci['d6_ci'][1])}] | "
            f"[{fmt(ci['d6_minus_c20_ci'][0])}, {fmt(ci['d6_minus_c20_ci'][1])}] |"
        )
        for dimension, item in main["concentration"].items():
            concentration_rows.append(
                f"| {summary['start']} | {dimension} | {item['removed']} | "
                f"{fmt(item['C20']['mean_net_pct'], 4)}% | {fmt(item['D6']['mean_net_pct'], 4)}% |"
            )

    return f"""# D6 vs C20：更早局部突破诊断

完成时间：{manifest['completed_utc']}。Taskboard：`CRYPTOTRADIN-126`。

## 白话结论

{decision['plain_language']}

正式裁决：**`{decision['label']}`**；后续路由：**`{decision['route']}`**。

这次只改变突破窗口：D6约24小时，C20约80小时。两边都使用已收盘信号、下一根4h开盘、相同成本和`+5%/-3%/48h`出口；没有加入收缩、放量、防追高、冷却或1h触发。

## 主结果：taker / stop-first / all-events

| 窗口起点 | 入场 | 闭合交易 | 平均净收益 | PF | 净盈利胜率 | TP / SL / TIME |
|---|---|---:|---:|---:|---:|---:|
{chr(10).join(result_rows)}

| 窗口起点 | 入场 | favorable-first | 48h MFE中位 | 48h MAE中位 | 先SL后达目标 |
|---|---|---:|---:|---:|---:|
{chr(10).join(path_rows)}

`favorable-first`按主口径的stop-first细粒度顺序判断目标是否先于止损；`先SL后达目标`继续观察完整48小时，因此不等于实际可实现收益。

## 不确定性

| 窗口起点 | C20均值95%区间 | D6均值95%区间 | D6-C20 95%区间 |
|---|---|---|---|
{chr(10).join(ci_rows)}

采用固定种子`20261013`的2,000次14日移动区块bootstrap。旧窗口只能用于开发诊断，区间不能消除重复研究和幸存者偏差。

## 信号密度与重叠

| 窗口起点 | 入场 | 事件数 | 每30日事件 | 有信号周 | 同币相邻事件中位小时 |
|---|---|---:|---:|---:|---:|
{chr(10).join(density_rows)}

精确同币同signal-time重叠：早窗 {summaries[0]['events']['overlap']['same_symbol_time_events']} 个，近窗 {summaries[1]['events']['overlap']['same_symbol_time_events']} 个。完整比例见`summary.json`。

## 成本、同币占用与组合敏感性

| 窗口起点 | 成本 | 层次 | 入场 | 平均净收益 | 账户净收益 |
|---|---|---|---|---:|---:|
{chr(10).join(sensitivity_rows)}

## Regime分层

| 窗口起点 | Regime | 入场 | 交易数 | 平均净收益 | PF |
|---|---|---|---:|---:|---:|
{chr(10).join(regime_rows)}

NATR三分位、BTC/ETH同期48小时、symbol和week的完整分层见各窗口主诊断JSON。

## 集中度

移除D6净贡献最高的一个标签后，对D6和C20同时应用相同剔除：

| 窗口起点 | 维度 | 移除标签 | C20净期望 | D6净期望 |
|---|---|---|---:|---:|
{chr(10).join(concentration_rows)}

## 裁决边界

- `development_qualified`也不允许改生产，只能进入真正未使用数据或自然前向验证。
- `reject_d6`只否定6根4h首次收盘突破与当前固定出口的组合，不外推10根、1h、reclaim或成交量触发。
- `insufficient`是兜底，不表述为接近成功；本实验不会自动启动下一项。
- 两个窗口的历史币池继承current-survivor偏差；组合层未实施历史`LOT_SIZE / MIN_NOTIONAL`，仍是研究近似。

## 复核

- C20全部36个成本×顺序×层次导出与既有cash-fix结果逐笔、逐金额一致。
- 运行与输入SHA256、逐分支核验计数见`run_manifest.json`和`verification.md`。
- 命令：`python scripts/research_breakout_d6.py`。
"""


def render_verification(manifest: dict, summaries: list[dict]) -> str:
    lines = [
        "# D6 vs C20 验证记录",
        "",
        f"- 协议SHA256：`{manifest['protocol_sha256']}`。",
        f"- 源码运行前后指纹一致：`{manifest['source_stable']}`。",
        f"- C20与既有cash-fix逐笔一致记录：{manifest['reference_trades_checked']}笔（跨全部分支/层次计数，允许同一事件在不同分支重复计数）。",
        "- 两窗C20信号均从冻结4h数组独立重算，并与冻结feature标记逐事件一致。",
        "- D6/C20均使用同一回放器、同一资格frame、同一成本和同一资金约束；未读取网络、未写业务数据库。",
        "- 生产配置、paper状态机和业务数据库未修改。",
        "",
        "## 窗口检查",
        "",
    ]
    for summary in summaries:
        checks = summary["checks"]
        lines.append(
            f"- `{summary['start']}`：eligible_frames={checks['eligible_frames']}，"
            f"recomputed_c20_events={checks['recomputed_c20_events']}，"
            f"D6_events={summary['events']['density']['D6']['events']}，"
            f"C20_events={summary['events']['density']['C20']['events']}。"
        )
    return "\n".join(lines) + "\n"


def main() -> None:
    if OUT.exists():
        raise SystemExit(f"Output exists; preserve the one-attempt result: {OUT}")
    frozen_manifest_path = FROZEN / "inputs_manifest.json"
    frozen_manifest = read_json(frozen_manifest_path)
    initial_sources = source_hashes()
    run_manifest = {
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "protocol": str(PROTOCOL.relative_to(ROOT)),
        "protocol_sha256": sha256(PROTOCOL),
        "source_sha256": initial_sources,
        "frozen_manifest": str(frozen_manifest_path.relative_to(ROOT)),
        "frozen_manifest_sha256": sha256(frozen_manifest_path),
        "attempt_budget": 1,
        "windows": [],
    }
    OUT.mkdir(parents=True)
    save_json(OUT / "run_manifest.json", run_manifest)
    summaries = []
    reference_trades_checked = 0

    for window in frozen_manifest["windows"]:
        meta_path = FROZEN / f"{window['start']}_inputs.json"
        if sha256(meta_path) != window["input_sha256"]:
            raise ValueError(f"Frozen input metadata mismatch: {meta_path}")
        meta = read_json(meta_path)
        arrays = load_arrays(meta)
        market = Market(arrays)
        start_ms, end_ms = ms(meta["start"]), ms(meta["end"])
        frames, events, checks = build_frames(meta["start"], arrays)
        density = {arm: event_density(events[arm], start_ms, end_ms) for arm in ARMS}
        overlap = event_overlap(events)
        save_json(OUT / f"{meta['start']}_event_index.json.gz", events)
        quality_cache = {}
        summary = {
            "start": meta["start"],
            "end": meta["end"],
            "checks": checks,
            "events": {"density": density, "overlap": overlap},
            "branches": [],
        }

        for costs in COSTS:
            for policy in ("stop_first", "target_first"):
                print(f"REPLAY {meta['start']} {costs.name} {policy}", flush=True)
                branch = {"cost": costs.name, "policy": policy, "layers": {}}
                for layer in ("all_events", "symbol_only", "portfolio"):
                    results = {
                        arm: replay(market, frames, start_ms, end_ms, arm, layer, costs, policy)
                        for arm in ARMS
                    }
                    for arm in ARMS:
                        annotate_trades(results[arm]["trades"], frames, arrays, market,
                                        end_ms, policy, quality_cache)
                    reference_trades_checked += verify_reference(
                        meta["start"], costs.name, policy, layer, results["C20"]["trades"]
                    )
                    details = {}
                    for arm in ARMS:
                        details[arm] = {
                            "metrics": trade_metrics(results[arm]["trades"]),
                            "path": path_summary(results[arm]["trades"]),
                            "counts": results[arm]["counts"],
                            "account": account_metrics(results[arm], start_ms, end_ms)
                            if layer == "portfolio" else None,
                        }
                    details["bootstrap"] = bootstrap_named(
                        results["C20"]["trades"], results["D6"]["trades"], start_ms, end_ms
                    )
                    if costs.name == PRIMARY_COST and policy == PRIMARY_POLICY and layer == "all_events":
                        for arm in ARMS:
                            details[arm]["groups"] = group_summaries(results[arm]["trades"])
                        details["concentration"] = {
                            dimension: contribution_removal(
                                results["D6"]["trades"], results["C20"]["trades"], dimension
                            )
                            for dimension in ("symbol", "week")
                        }
                        save_json(
                            OUT / f"{meta['start']}_primary_diagnostics.json.gz",
                            {arm: {"groups": details[arm]["groups"],
                                   "blocks": results[arm]["blocks"]} for arm in ARMS},
                        )
                    branch["layers"][layer] = details
                    prefix = f"{meta['start']}_{costs.name}_{policy}_{layer}"
                    save_json(OUT / f"{prefix}_trades.json.gz",
                              {arm: results[arm]["trades"] for arm in ARMS})
                summary["branches"].append(branch)
                save_json(OUT / f"{meta['start']}_summary.json", summary)
        summaries.append(summary)
        run_manifest["windows"].append({
            "start": meta["start"],
            "input_metadata": str(meta_path.relative_to(ROOT)),
            "input_metadata_sha256": sha256(meta_path),
            "archive": meta["archive"],
            "archive_sha256": meta["archive_sha256"],
            "feature_sha256": checks["source_features_sha256"],
        })
        del market, arrays, frames, quality_cache

    decision = decide(summaries)
    run_manifest["completed_utc"] = datetime.now(timezone.utc).isoformat()
    run_manifest["reference_trades_checked"] = reference_trades_checked
    run_manifest["source_stable"] = source_hashes() == initial_sources
    if not run_manifest["source_stable"]:
        raise AssertionError("Research source changed during run")
    save_json(OUT / "summary.json", {"decision": decision, "windows": summaries})
    save_json(OUT / "run_manifest.json", run_manifest)
    (OUT / "report.md").write_text(
        render_report(summaries, decision, run_manifest), encoding="utf-8"
    )
    (OUT / "verification.md").write_text(
        render_verification(run_manifest, summaries), encoding="utf-8"
    )
    print(json.dumps(decision, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
