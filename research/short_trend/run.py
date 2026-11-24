"""Run the single frozen event study offline; never qualify an unknown account.

No strategy, cost, year, universe or cutoff overrides exist. Data prefetch is a
separate bounded operation. This command reads only explicitly approved caches.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import csv
from datetime import datetime, timezone
import gzip
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

from .preflight import EFFECTIVE_END_MS, utc_ms, validate_protocol

ROOT = Path(__file__).resolve().parents[2]
EXPECTED_PROTOCOL_SHA256 = "240e2a60cdbfc3eda09615063114cb04a2277ff9d034a5286e021cfced5e8462"
PROTOCOL_COMMIT = "9ecc35d67096bc469834eddf149eb90cc51036a6"
ORDERS = {"primary": "funding_first", "alternative": "price_first"}


def canonical_digest(value: dict) -> str:
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


def locked_protocol() -> dict:
    config = json.loads((Path(__file__).with_name("protocol.json")).read_bytes())
    validate_protocol(config)
    if canonical_digest(config) != EXPECTED_PROTOCOL_SHA256:
        raise ValueError("Frozen protocol differs; do not run a changed strategy")
    return config


def iso(value: int) -> str:
    return datetime.fromtimestamp(value / 1000, timezone.utc).isoformat()


def save_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
                    encoding="utf-8")


def write_csv(path: Path, rows: list[dict]) -> None:
    fields = list(dict.fromkeys(key for row in rows for key in row))
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def validate_event_bounds(event: dict, start: int, end: int) -> None:
    if not start <= event["decision_ms"] < event["entry_ms"] < event["deadline_ms"] < end <= EFFECTIVE_END_MS:
        raise AssertionError("Event crosses its frozen time segment")
    for arm in ("signal", "mirror"):
        trade = event[arm]
        if not event["entry_ms"] <= trade["exit_ms"] <= event["deadline_ms"]:
            raise AssertionError("Trade exit is outside the complete frozen horizon")
        for funding in trade.get("funding_events", []):
            if not event["entry_ms"] < funding["time_ms"] <= trade["exit_ms"]:
                raise AssertionError("Funding attribution is outside the held interval")


def flat_event(event: dict) -> dict:
    row = {key: value for key, value in event.items()
           if not isinstance(value, (dict, list, tuple))}
    row["decision_utc"] = iso(event["decision_ms"])
    row["entry_utc"] = iso(event["entry_ms"])
    for arm in ("signal", "mirror"):
        for key, value in event[arm].items():
            if not isinstance(value, (dict, list, tuple)):
                row[f"{arm}_{key}"] = value
    for key, value in event.get("direction_hits", {}).items():
        if not isinstance(value, (dict, list, tuple)):
            row[f"direction_hit_{key}"] = value
    return row


def monthly_events(events: list[dict]) -> list[dict]:
    grouped = defaultdict(list)
    for event in events:
        month = datetime.fromtimestamp(event["entry_ms"] / 1000, timezone.utc).strftime("%Y-%m")
        grouped[(event["symbol"], event["cost_regime"], event["funding_order"], month)].append(event)
    rows = []
    for (symbol, cost, order, month), batch in sorted(grouped.items()):
        n = len(batch)
        rows.append({"symbol": symbol, "cost_regime": cost, "funding_order": order,
                     "month": month, "events": n,
                     "net_wins": sum(e["signal"]["net_pnl_usdt"] > 0 for e in batch),
                     "mean_net_R": sum(e["signal"]["net_R"] for e in batch) / n,
                     "mean_delta_R": sum(e["delta_R"] for e in batch) / n,
                     "fee_usdt_sum_diagnostic_not_account_pnl": sum(e["signal"]["fee_usdt"] for e in batch),
                     "funding_usdt_sum_diagnostic_not_account_pnl": sum(e["signal"]["funding_usdt"] for e in batch)})
    return rows


def format_number(value, digits=4) -> str:
    return "—" if value is None else f"{value:.{digits}f}"


def brief_metrics(events: list[dict]) -> dict:
    if not events:
        return {"n": 0, "win_pct": None, "mean_R": None, "delta_R": None, "pf": None}
    pnl = [e["signal"]["net_pnl_usdt"] for e in events]
    positive = sum(max(p, 0) for p in pnl)
    negative = -sum(min(p, 0) for p in pnl)
    return {"n": len(events), "win_pct": 100 * sum(p > 0 for p in pnl) / len(pnl),
            "mean_R": sum(e["signal"]["net_R"] for e in events) / len(events),
            "delta_R": sum(e["delta_R"] for e in events) / len(events),
            "pf": positive / negative if negative else None}


def render_report(events: list[dict], summary: dict, manifest: dict) -> str:
    lines = ["# 短期趋势48H：已知旧年份的固定规则回测", "",
             "## 可以直接理解的结果", "",
             f"- 事件层判定：**{summary.get('event_verdict', '见summary.json')}**。",
             f"- 总体判定：**{summary.get('overall_verdict', 'INSUFFICIENT_EXECUTION_EVIDENCE')}**。",
             "- 账户层未评估：缺历史下单/保证金证据，没有真实账户65%胜率或资金曲线结论。",
             "- 事件可重叠、固定参考权益110USDT；不能把所有事件利润相加当成账户收益。", "",
             "## 范围与证据含义", "",
             "BTC/ETH/SOL为固定主池，ZEC仅探索；2023-12预热，2024和2025逐年评估。",
             "这些年份和同类规则已有项目研究接触，只是固定规格的历史复核，不是全新独立确认。",
             "本次回放仅打开明确命名、校验通过的2023-12至2025-12官方归档；无2026市场行。",
             "此前审计的三项读取边界失误仍保留记录，不能因本次边界校验通过而宣称过去零暴露。", "",
             "1H首次48H突破，不等回踩；Wilder ATR14固定止损，+5min市价参考，4H退出。",
             "目标净账户1%，计划风险1.5%（≤5USDT），名义≤2E；两方向使用共同风险预算。",
             "正常fee/slip单边5/3bps，压力10/10bps；资金费按原始毫秒，mark为同桶历史open代理。", "",
             "## 全部预定情景", "",
             "| 样本 | 成本 | 资金费柱内顺序 | 年份 | 事件数 | 事件净盈利率 | 平均净R | 相对随机方向ΔR | PF |",
             "|---|---|---|---|---:|---:|---:|---:|---:|"]
    primary = set(manifest["primary_symbols"])
    for label, allowed in (("主池", primary), ("ZEC探索", {"ZECUSDT"})):
        for cost in ("normal", "stress"):
            for order in ORDERS:
                for year in (2024, 2025, "pooled"):
                    batch = [e for e in events if e["symbol"] in allowed and e["cost_regime"] == cost
                             and e["funding_order"] == order and (year == "pooled" or e["year"] == year)]
                    m = brief_metrics(batch)
                    lines.append(f"| {label} | {cost} | {order} | {year} | {m['n']} | {format_number(m['win_pct'],2)}% | {format_number(m['mean_R'])} | {format_number(m['delta_R'])} | {format_number(m['pf'],3)} |")
    lines += ["", "## 主池正常成本：平均值的95%区间", "",
              "| 资金费顺序 | 周块方法 | 平均净R区间 | ΔR区间 |",
              "|---|---|---|---|"]
    for order in ORDERS:
        normal = summary.get("scenarios", {}).get(order, {}).get("normal", {})
        for method, value in normal.get("pooled", {}).get("bootstrap", {}).items():
            def ci_text(key):
                interval = value[key]["ci95"]
                return "—" if interval is None else "[" + ", ".join(format_number(x) for x in interval) + "]"
            lines.append(f"| {order} | {method} | {ci_text('net_R')} | {ci_text('delta_R')} |")
    lines += ["", "## 主池正常成本：目标兑现与盈亏", "",
              "| 资金费顺序 | 净1%目标达标率 | 平均盈利USDT | 平均亏损USDT | 打平胜率 | 4H方向命中 | TIME占比 |",
              "|---|---:|---:|---:|---:|---:|---:|"]
    for order in ORDERS:
        metrics = summary.get("scenarios", {}).get(order, {}).get("normal", {}).get("pooled", {}).get("metrics", {})
        if metrics:
            percent = lambda key: format_number(None if metrics.get(key) is None else 100 * metrics[key], 2) + "%"
            direction_hit = metrics.get("direction_hit_rates", {}).get("4h", {}).get("hit_rate")
            lines.append(f"| {order} | {percent('target_achieved_rate')} | {format_number(metrics.get('avg_win_usdt'))} | {format_number(metrics.get('avg_loss_usdt'))} | {percent('breakeven_net_win_rate')} | {format_number(None if direction_hit is None else direction_hit*100,2)}% | {percent('time_exit_rate')} |")
    lines += ["", "## 不确定性与账户限制", "",
              "主周块与固定4周循环移动块各10000次、种子20261124；包含零事件周、跨币共同抽块。",
              "净R与配对Δ的区间、逐币/方向/年度和剔除任一币检查在summary.json中完整保存。",
              "资金费先发生/触价先发生两种预先规定情景全部报告，结论冲突按证据不足，不选较好者。",
              "事件盈利率不是单仓、合法最小单后的账户胜率，不能据此宣布65%目标达标。",
              "没有新参数比较、换币或近期数据补证；本轮不修改正式策略或自动下单。", "",
              "## 可追溯文件", "",
              "- pre_run_manifest.json：协议/实现Git与文件哈希，在策略计算之前保存。",
              "- data_manifest.json：全部官方旧归档URL、checksum及时间范围。",
              "- events.csv / events.jsonl.gz：逐事件及两臂完整账目；skips.csv：逐信号跳过原因。",
              "- monthly.csv：逐月事件诊断；summary.json：完整统计及门槛裁决。",
              "- audit.json：独立逐事件PnL、风险、时界和数据范围对账。",
              "- PROTOCOL.md / protocol.json：未改动的冻结协议副本。", ""]
    return "\n".join(lines)


def run(cache_root: Path, output: Path) -> None:
    from .data import load_symbol
    from .engine import event_pairs
    from .stats import summarize_events
    from .audit import audit_event_batch
    import numpy as np

    config = locked_protocol()
    output = output.resolve()
    if not output.is_relative_to((ROOT / "reports").resolve()) or output.exists():
        raise ValueError("Output must be a new directory under this worktree's reports/")
    if subprocess.run(["git", "diff", "--quiet", "HEAD"], cwd=ROOT).returncode:
        raise ValueError("Commit the reviewed implementation before running")
    source_files = sorted(p for p in Path(__file__).parent.iterdir()
                          if p.is_file() and p.suffix in {".py", ".json", ".md"})
    relative_files = [str(p.relative_to(ROOT)).replace("\\", "/") for p in source_files]
    subprocess.run(["git", "ls-files", "--error-unmatch", "--", *relative_files],
                   cwd=ROOT, check=True, capture_output=True)
    commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, check=True,
                            capture_output=True, text=True).stdout.strip()
    manifest = {"started_utc": datetime.now(timezone.utc).isoformat(),
                "protocol_commit": PROTOCOL_COMMIT, "implementation_commit": commit,
                "protocol_sha256": canonical_digest(config),
                "source_sha256_LF": {str(p.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(
                    p.read_bytes().replace(b"\r\n", b"\n")).hexdigest() for p in source_files},
                "primary_symbols": config["primary_symbols"],
                "exploratory_symbols": config["exploratory_symbols"],
                "data_role": config["purpose"], "effective_exclusive_end_ms": EFFECTIVE_END_MS,
                "python_version": sys.version, "numpy_version": np.__version__,
                "cache_only_during_strategy_run": True, "historical_account_evaluated": False,
                "parameter_search": False, "attempt": 1}
    output.mkdir(parents=True)
    save_json(output / "pre_run_manifest.json", manifest)
    shutil.copyfile(Path(__file__).with_name("PROTOCOL.md"), output / "PROTOCOL.md")
    shutil.copyfile(Path(__file__).with_name("protocol.json"), output / "protocol.json")
    all_events, skip_rows, dataset_manifests, audits = [], [], [], []
    for symbol in config["primary_symbols"] + config["exploratory_symbols"]:
        print(f"Loading checked historical cache: {symbol}", flush=True)
        dataset = load_symbol(symbol, cache_root, download=False)
        bars, funding = dataset["bars"], dataset["funding"]
        dataset_manifests.append(dataset["manifest"])
        for segment in config["segments"]:
            start, end = utc_ms(segment["start_utc"]), utc_ms(segment["end_utc"])
            year = datetime.fromtimestamp(start / 1000, timezone.utc).year
            for cost_name, costs in config["cost_regimes"].items():
                for order_name, engine_order in ORDERS.items():
                    replay = event_pairs(symbol, bars, funding, start, end,
                                         costs["fee_bps_per_side"], costs["slippage_bps_per_side"],
                                         order=engine_order)
                    for event in replay["events"]:
                        validate_event_bounds(event, start, end)
                        event.update(year=year, cost_regime=cost_name, funding_order=order_name)
                        all_events.append(event)
                    audits.append(dict(symbol=symbol, year=year, cost_regime=cost_name,
                                       funding_order=order_name,
                                       **audit_event_batch(replay["events"], bars, config)))
                    for skipped in replay.get("skip_records", []):
                        skip_rows.append(dict(symbol=symbol, year=year, cost_regime=cost_name,
                                              funding_order=order_name, **skipped))
                    print(f"Replayed {symbol} {year} {cost_name}/{order_name}: "
                          f"{len(replay['events'])} events", flush=True)
        del dataset, bars, funding
    save_json(output / "data_manifest.json", dataset_manifests)
    save_json(output / "audit.json", {
        "batches": audits, "violations": 0,
        "events_audited": sum(row["events_audited"] for row in audits),
        "arithmetic_and_path_assertions": sum(row["arithmetic_and_path_assertions"] for row in audits),
        "max_source_close_ms": max(row["bars"]["max_close_time_ms"] for row in dataset_manifests),
        "max_funding_ms": max(row["funding"]["max_time_ms"] for row in dataset_manifests),
        "account_execution_proven": False})
    with gzip.open(output / "events.jsonl.gz", "wt", encoding="utf-8") as stream:
        for event in all_events:
            stream.write(json.dumps(event, ensure_ascii=False, allow_nan=False) + "\n")
    write_csv(output / "events.csv", [flat_event(e) for e in all_events])
    write_csv(output / "skips.csv", skip_rows)
    write_csv(output / "monthly.csv", monthly_events(all_events))
    print("All frozen scenarios complete; starting calendar-block statistics", flush=True)
    summary = summarize_events(all_events, config, data_quality_ok=True,
                               account_status="NOT_EVALUATED_UNKNOWN_METADATA")
    save_json(output / "summary.json", summary)
    (output / "report.md").write_text(render_report(all_events, summary, manifest), encoding="utf-8")
    manifest["completed_utc"] = datetime.now(timezone.utc).isoformat()
    manifest["events_total_all_scenarios"] = len(all_events)
    save_json(output / "run_manifest.json", manifest)
    print(json.dumps({"output": str(output), "events": len(all_events),
                      "event_verdict": summary.get("event_verdict"),
                      "overall_verdict": summary.get("overall_verdict")}, ensure_ascii=False), flush=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    run(args.cache_root, args.output)


if __name__ == "__main__":
    main()
