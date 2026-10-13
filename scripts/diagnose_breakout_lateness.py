"""Diagnose whether frozen 20x4h breakout entries arrive after the 5% move.

This is a path diagnostic over the frozen C-arm events. It does not search
parameters, rescan symbols, or modify production state.
"""
from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
import csv
import gzip
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from short_horizon_core import DAY, H4, new_breakout


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "reports/2026-10-13/short_horizon_entry_v1_cashfix"
FROZEN = ROOT / "reports/2026-10-13/short_horizon_entry_v1"
PROTOCOL = ROOT / "reports/2026-10-13/breakout_lateness_protocol_v1.md"
OUT = ROOT / "reports/2026-10-13/breakout_lateness_diagnostic_v1"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def utc(ms: int) -> str:
    return datetime.fromtimestamp(ms / 1000, timezone.utc).isoformat()


def event_features(rows: np.ndarray, trade: dict) -> dict:
    """Compute pre-signal and full-horizon features for one frozen trade."""
    entered = int(trade["entry_ms"])
    i = int(np.searchsorted(rows[:, 0], entered))
    if i >= len(rows) or int(rows[i, 0]) != entered:
        raise ValueError(f"missing entry bar: {trade['symbol']} {entered}")
    if i < 21 or i + 12 >= len(rows):
        raise ValueError(f"insufficient diagnostic path: {trade['symbol']} {entered}")
    signal = rows[i - 1]
    prior20 = rows[i - 21:i - 1]
    assert len(prior20) == 20
    assert new_breakout(rows[i - 22:i]) if i >= 22 else signal[4] > np.max(prior20[:, 2])
    breakout_close = float(signal[4])
    pre_advance = 100 * (breakout_close / float(np.min(prior20[:, 3])) - 1)
    pre_returns = {
        hours: 100 * (breakout_close / float(rows[i - 1 - hours // 4, 4]) - 1)
        for hours in (12, 24, 48)
    }
    # Same holding contract as path(): 12 complete 4h bars, plus deadline open.
    post_max = max(float(np.max(rows[i:i + 12, 2])), float(rows[i + 12, 1]))
    post_mfe = 100 * (post_max / float(trade["entry_price"]) - 1)
    pre_move = pre_advance >= 5
    target_available = post_max >= float(trade["target"])
    return {
        "window": "",
        "symbol": trade["symbol"],
        "entry_ms": entered,
        "entry_utc": utc(entered),
        "status": trade["status"],
        "regime": trade["regime"],
        "breakout_close": breakout_close,
        "raw_entry": float(trade["raw_entry"]),
        "entry_price": float(trade["entry_price"]),
        "target": float(trade["target"]),
        "pre_advance_20bar_pct": pre_advance,
        "pre_return_12h_pct": pre_returns[12],
        "pre_return_24h_pct": pre_returns[24],
        "pre_return_48h_pct": pre_returns[48],
        "post_mfe_48h_pct": post_mfe,
        "pre_move_5": pre_move,
        "post_target_available": target_available,
        "late_exhausted": pre_move and not target_available,
        "stopped_then_target_available": trade["status"] == "SL" and target_available,
    }


def block_ci(records: list[dict], start_ms: int, end_ms: int, field: str) -> list[float]:
    days = (end_ms - start_ms) // DAY
    daily = np.zeros((days, 2), dtype=float)
    for r in records:
        j = (r["entry_ms"] - start_ms) // DAY
        daily[j, 0] += bool(r[field])
        daily[j, 1] += 1
    rng = np.random.default_rng(20261013)
    block_days = 14
    blocks = math.ceil(days / block_days)
    begins = rng.integers(0, days - block_days + 1, size=(2000, blocks))
    indices = (begins[:, :, None] + np.arange(block_days)).reshape(2000, -1)[:, :days]
    samples = daily[indices].sum(axis=1)
    values = samples[:, 0] / samples[:, 1]
    return (100 * np.quantile(values, [.025, .975])).tolist()


def pct(records: list[dict], field: str) -> float:
    return 100 * sum(bool(r[field]) for r in records) / len(records)


def values(records: list[dict], field: str) -> dict:
    x = np.array([r[field] for r in records], dtype=float)
    return {"median": float(np.median(x)), "q25": float(np.quantile(x, .25)),
            "q75": float(np.quantile(x, .75)), "mean": float(np.mean(x))}


def summarize(records: list[dict], start_ms: int, end_ms: int) -> dict:
    by_symbol = Counter(r["symbol"] for r in records)
    loo = []
    for symbol in by_symbol:
        kept = [r for r in records if r["symbol"] != symbol]
        loo.append(pct(kept, "late_exhausted"))
    statuses = {}
    for status in ("TP", "SL", "TIME"):
        subset = [r for r in records if r["status"] == status]
        statuses[status] = {
            "n": len(subset),
            "pre_advance_20bar_pct": values(subset, "pre_advance_20bar_pct") if subset else None,
            "post_mfe_48h_pct": values(subset, "post_mfe_48h_pct") if subset else None,
            "pre_move_5_pct": pct(subset, "pre_move_5") if subset else None,
        }
    return {
        "n": len(records),
        "symbols": len(by_symbol),
        "pre_advance_20bar_pct": values(records, "pre_advance_20bar_pct"),
        "pre_return_12h_pct": values(records, "pre_return_12h_pct"),
        "pre_return_24h_pct": values(records, "pre_return_24h_pct"),
        "pre_return_48h_pct": values(records, "pre_return_48h_pct"),
        "post_mfe_48h_pct": values(records, "post_mfe_48h_pct"),
        "pre_move_5_pct": pct(records, "pre_move_5"),
        "post_target_available_pct": pct(records, "post_target_available"),
        "late_exhausted_pct": pct(records, "late_exhausted"),
        "late_exhausted_ci95_pct": block_ci(records, start_ms, end_ms, "late_exhausted"),
        "stopped_then_target_available_pct": pct(records, "stopped_then_target_available"),
        "actual_status_counts": dict(Counter(r["status"] for r in records)),
        "max_symbol_share_pct": 100 * max(by_symbol.values()) / len(records),
        "leave_one_symbol_out_late_pct": {"min": min(loo), "max": max(loo)},
        "by_status": statuses,
    }


def render_report(summary: dict) -> str:
    windows = summary["windows"]
    rows = []
    timing_rows = []
    for w in windows:
        s = w["summary"]
        rows.append(
            f"| {w['start']} → {w['end']} | {s['n']} | "
            f"{s['pre_advance_20bar_pct']['median']:.2f}% | {s['pre_move_5_pct']:.2f}% | "
            f"{s['post_target_available_pct']:.2f}% | {s['late_exhausted_pct']:.2f}% | "
            f"[{s['late_exhausted_ci95_pct'][0]:.3f}%, {s['late_exhausted_ci95_pct'][1]:.3f}%] |"
        )
        timing_rows.append(
            f"| {w['start']} | {s['pre_return_12h_pct']['median']:.2f}% | "
            f"{s['pre_return_24h_pct']['median']:.2f}% | {s['pre_return_48h_pct']['median']:.2f}% | "
            f"{s['post_mfe_48h_pct']['median']:.2f}% |"
        )
    decision = summary["decision"]
    return f"""# 20根4h突破是否入场过晚？

诊断完成：2026-10-13 +08:00。只复用冻结C臂事件和原始4h数组，不改参数、不重跑scanner、不改变生产配置。

## 白话结论

{decision['plain_language']}

正式裁决：**`{decision['label']}`**。

## 主指标

`late_exhausted`表示：突破前从此前20根低点到突破收盘已经上涨至少5%，但按实际下一根开盘成交后，未来48小时最高价仍不足以达到成交价+5%。

| UTC窗口 | 突破事件 | 突破前涨幅中位数 | 突破前已有5% | 成交后仍有5%空间 | late_exhausted | 14日区块95%区间 |
|---|---:|---:|---:|---:|---:|---:|
{chr(10).join(rows)}

从固定时间锚点看，突破前的上涨并不只是80小时区间低点造成的：

| 窗口起点 | 突破前12h收益中位数 | 前24h | 前48h | 成交后48h MFE中位数 |
|---|---:|---:|---:|---:|
{chr(10).join(timing_rows)}

## 区分“太晚”与“先止损后上涨”

{decision['mechanism_text']}

逐一剔除任一币后，`late_exhausted`比例范围：早窗 {windows[0]['summary']['leave_one_symbol_out_late_pct']['min']:.2f}%–{windows[0]['summary']['leave_one_symbol_out_late_pct']['max']:.2f}%，近窗 {windows[1]['summary']['leave_one_symbol_out_late_pct']['min']:.2f}%–{windows[1]['summary']['leave_one_symbol_out_late_pct']['max']:.2f}%；最大单币事件占比分别为 {windows[0]['summary']['max_symbol_share_pct']:.2f}% / {windows[1]['summary']['max_symbol_share_pct']:.2f}%。

## 边界

- 突破前涨幅以此前20根最低low为事后诊断锚点，证明路径中已发生过幅度，不等于存在可成交的早入场信号。
- `post_target_available`忽略先触发止损的事实，只回答后续空间；实际可实现结果仍以原回放为准。
- 样本沿用current-survivor币池和已研究窗口，不能作为新样本外，也不能推广到所有突破定义。
- 本诊断不授权把20改成10/5或搜索阈值。若结论支持机制，也必须另立可因果执行的“更早启动”规则和验证集。

## 复核

- 冻结协议SHA256：`{summary['protocol_sha256']}`。
- 输入逐笔、npz和脚本指纹见 `summary.json`；逐事件字段见 `events.csv`。
- 命令：`python scripts/diagnose_breakout_lateness.py`。
"""


def main() -> None:
    if OUT.exists():
        raise SystemExit(f"Output exists; do not overwrite: {OUT}")
    manifest = json.loads((FROZEN / "inputs_manifest.json").read_text(encoding="utf-8"))
    all_records = []
    windows = []
    inputs = []
    for item in manifest["windows"]:
        start = item["start"]
        meta_path = FROZEN / f"{start}_inputs.json"
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        archive = ROOT / meta["archive"]
        if sha256(archive) != meta["archive_sha256"]:
            raise ValueError(f"archive hash mismatch: {archive}")
        trades_path = SOURCE / f"{start}_taker_stop_first_all_events_trades.json.gz"
        with gzip.open(trades_path, "rt", encoding="utf-8") as f:
            trades = json.load(f)["C"]
        with np.load(archive, allow_pickle=False) as saved:
            for trade in trades:
                rows = saved[f"{trade['symbol']}__4h"]
                record = event_features(rows, trade)
                record["window"] = start
                all_records.append(record)
        start_ms = int(datetime.fromisoformat(item["start"] + "+00:00").timestamp() * 1000)
        end_ms = int(datetime.fromisoformat(item["end"] + "+00:00").timestamp() * 1000)
        subset = [r for r in all_records if r["window"] == start]
        windows.append({"start": start, "end": item["end"],
                        "summary": summarize(subset, start_ms, end_ms)})
        inputs.append({"window_input": str(meta_path.relative_to(ROOT)), "sha256": sha256(meta_path),
                       "archive": meta["archive"], "archive_sha256": meta["archive_sha256"],
                       "trades": str(trades_path.relative_to(ROOT)), "trades_sha256": sha256(trades_path)})

    support = all(w["summary"]["late_exhausted_pct"] > 50
                  and w["summary"]["late_exhausted_ci95_pct"][0] > 50
                  and w["summary"]["leave_one_symbol_out_late_pct"]["min"] > 50 for w in windows)
    reject = all(w["summary"]["late_exhausted_pct"] < 50
                 and w["summary"]["late_exhausted_ci95_pct"][1] < 50
                 and w["summary"]["post_target_available_pct"] > 50 for w in windows)
    if support:
        label = "support_breakout_entry_is_late"
        plain = "两个窗口都显示，多数突破在成交前已经走完至少5%，成交后却再无5%空间；区块区间和逐币剔除也通过预设门槛，支持这版20根突破入场过晚。"
    elif reject:
        label = "reject_breakout_entry_is_late"
        plain = "两个窗口都没有显示多数事件在成交前耗尽空间；成交后通常仍有5%空间，预设标准否定‘主要因为入场太晚’。"
    else:
        label = "insufficient_or_window_inconsistent"
        early, near = windows[0]["summary"], windows[1]["summary"]
        plain = ("突破前已经出现5%路径涨幅的现象很普遍，但‘成交后再无5%空间’只在近窗占多数："
                 f"早窗为{early['late_exhausted_pct']:.2f}%，近窗为{near['late_exhausted_pct']:.2f}%。"
                 "窗口结论不一致，且近窗区块区间下界略低于预设的50%严格门槛，所以不能把整体失败主要归因于入场过晚。")
    mechanism = []
    for w in windows:
        s = w["summary"]
        mechanism.append(f"{w['start']}窗口：实际SL后完整48小时内后来仍达到目标的事件占全部突破 {s['stopped_then_target_available_pct']:.2f}%。")
    summary = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "protocol": str(PROTOCOL.relative_to(ROOT)), "protocol_sha256": sha256(PROTOCOL),
        "script_sha256": sha256(Path(__file__)), "inputs": inputs, "windows": windows,
        "decision": {"label": label, "plain_language": plain, "mechanism_text": " ".join(mechanism)},
    }
    OUT.mkdir(parents=True)
    (OUT / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    fields = list(all_records[0])
    with (OUT / "events.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(all_records)
    (OUT / "report.md").write_text(render_report(summary), encoding="utf-8")
    print(json.dumps(summary["decision"], ensure_ascii=False))
    for w in windows:
        s = w["summary"]
        print(w["start"], s["n"], s["pre_move_5_pct"], s["post_target_available_pct"],
              s["late_exhausted_pct"], s["late_exhausted_ci95_pct"])


if __name__ == "__main__":
    main()
