"""Run the frozen, pre-holdout ZEC study without opening the production DB."""
from __future__ import annotations

import argparse
from collections import defaultdict
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import random
import subprocess
import sys
from statistics import mean

UTC = timezone.utc
CUTOFF_MS = 1782144000000
ROOT = Path(__file__).resolve().parents[2]
WINDOWS = (("development_2024", "2024-01-01", "2025-01-01"),
           ("validation_2025", "2025-01-01", "2026-01-01"))
COSTS = (("normal", 5.0, 3.0), ("stress", 10.0, 10.0))


def timestamp(value: str) -> int:
    return int(datetime.fromisoformat(value).replace(tzinfo=UTC).timestamp() * 1000)


def iso(value: int) -> str:
    return datetime.fromtimestamp(value / 1000, UTC).isoformat()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: list[dict]) -> None:
    fields = list(dict.fromkeys(key for row in rows for key in row))
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def monthly_rows(trades: list[dict], start_ms: int, end_ms: int) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for trade in trades:
        month = datetime.fromtimestamp(trade["exit_ms"] / 1000, UTC).strftime("%Y-%m")
        grouped[month].append(trade)
    year = datetime.fromtimestamp(start_ms / 1000, UTC).year
    rows = []
    for m in range(1, 13):
        month = f"{year}-{m:02d}"
        if not start_ms <= timestamp(month + "-01") < end_ms:
            continue
        batch = grouped[month]
        rows.append({"month": month, "trades": len(batch),
                     "net_pnl_usdt": sum(t["net_pnl_usdt"] for t in batch),
                     "net_r_sum": sum(t["net_pnl_usdt"] / t["initial_risk_usdt"] for t in batch),
                     "wins": sum(t["net_pnl_usdt"] > 0 for t in batch),
                     "fees_usdt": sum(t["fees_usdt"] for t in batch),
                     "funding_cost_usdt": sum(t["funding_cost_usdt"] for t in batch)})
    return rows


def monthly_bootstrap(months: list[dict], repetitions: int = 5000) -> list[float] | None:
    """Exploratory month-cluster CI; only 12 blocks, not a guarantee of stationarity."""
    if not months or not sum(m["trades"] for m in months):
        return None
    rng = random.Random(20261123)
    means = []
    for _ in range(repetitions):
        batch = rng.choices(months, k=len(months))
        count = sum(m["trades"] for m in batch)
        if count:
            means.append(sum(m["net_r_sum"] for m in batch) / count)
    means.sort()
    return [means[int((len(means) - 1) * q)] for q in (0.025, 0.975)] if means else None


def stats(trades: list[dict], curve: list[dict], final_equity: float, months: list[dict]) -> dict:
    pnls = [t["net_pnl_usdt"] for t in trades]
    wins, losses = [p for p in pnls if p > 0], [p for p in pnls if p < 0]
    peak, drawdown = 110.0, 0.0
    for point in curve:
        peak = max(peak, point["equity"])
        drawdown = max(drawdown, (peak - point["equity"]) / peak if peak > 0 else 0)
    streak = longest = 0
    for p in pnls:
        streak = streak + 1 if p < 0 else 0
        longest = max(longest, streak)
    by_side = {}
    for side in ("long", "short"):
        batch = [t for t in trades if str(t["side"]).lower() == side]
        by_side[side] = {"trades": len(batch), "net_pnl_usdt": sum(t["net_pnl_usdt"] for t in batch),
                         "mean_net_r": mean([t["net_pnl_usdt"] / t["initial_risk_usdt"] for t in batch]) if batch else None}
    reasons: dict[str, int] = defaultdict(int)
    for t in trades:
        reasons[t["exit_reason"]] += 1
    return {"trades": len(trades), "trades_per_month": len(trades) / len(months) if months else 0,
            "net_win_rate": len(wins) / len(trades) if trades else None,
            "average_net_win_usdt": mean(wins) if wins else None,
            "average_net_loss_usdt": mean(losses) if losses else None,
            "mean_net_r": mean([t["net_pnl_usdt"] / t["initial_risk_usdt"] for t in trades]) if trades else None,
            "profit_factor": sum(wins) / -sum(losses) if losses else None,
            "final_equity": final_equity, "net_pnl_usdt": final_equity - 110,
            "net_return_pct": (final_equity / 110 - 1) * 100,
            "max_drawdown_pct": drawdown * 100, "longest_losing_streak": longest,
            "mean_holding_hours": mean([(t["exit_ms"] - t["entry_ms"]) / 3600000 for t in trades]) if trades else None,
            "fees_usdt": sum(t["fees_usdt"] for t in trades),
            "funding_cost_usdt": sum(t["funding_cost_usdt"] for t in trades),
            "largest_win_usdt": max(wins) if wins else 0,
            "worst_net_trade_usdt": min(pnls) if pnls else None,
            "ambiguous_bars": sum(bool(t["ambiguous"]) for t in trades),
            "intrabar_funding_trades": sum(bool(t.get("funding_intrabar_order_assumed", False)) for t in trades),
            "target_clamped_to_bar_trades": sum(bool(t.get("target_clamped_to_bar", False)) for t in trades),
            "positive_months": sum(m["net_pnl_usdt"] > 0 for m in months),
            "monthly_cluster_mean_r_ci95": monthly_bootstrap(months),
            "exit_reasons": dict(reasons), "by_side": by_side}


def verdict(normal: dict, stress: dict) -> tuple[str, str]:
    n, s = normal["metrics"], stress["metrics"]
    if n["trades"] == 0:
        return "insufficient", "没有交易样本。"
    if n["mean_net_r"] <= 0 or n["net_pnl_usdt"] <= 0:
        return "reject", "时间顺序验证段在常规成本下没有正向净期望。"
    if s["trades"] < 100 or s["mean_net_r"] is None:
        return "insufficient", "成本压力情景没有足够交易，不能确认成本稳健性。"
    if s["net_pnl_usdt"] < 0 or (s["mean_net_r"] is not None and s["mean_net_r"] <= 0):
        return "reject", "常规成本下的优势未通过预注册成本压力条件。"
    if n["trades"] < 100 or any(n["by_side"][side]["trades"] < 30 for side in ("long", "short")):
        return "insufficient", "总体或单方向样本数未达到预注册最低要求。"
    if any(n["by_side"][side]["net_pnl_usdt"] <= 0 or n["by_side"][side]["mean_net_r"] <= 0
           for side in ("long", "short")):
        return "insufficient", "多空方向的净期望结论矛盾，不能确认双边策略有效。"
    if any(s["by_side"][side]["trades"] < 30 or s["by_side"][side]["net_pnl_usdt"] <= 0
           or s["by_side"][side]["mean_net_r"] <= 0 for side in ("long", "short")):
        return "insufficient", "压力成本下单方向样本或净期望不足，不能确认双边稳健性。"
    ci = n["monthly_cluster_mean_r_ci95"]
    if ci is None or ci[0] <= 0:
        return "insufficient", "月份分块区间仍包含零，不能确认稳定正期望。"
    total = n["net_pnl_usdt"]
    if max([m["net_pnl_usdt"] for m in normal["monthly"]], default=0) >= total:
        return "insufficient", "验证收益依赖单个月份，缺少跨月份证据。"
    if n["largest_win_usdt"] >= total:
        return "insufficient", "剔除最大盈利单后无净盈利，收益依赖单笔交易。"
    return "continue_research", "通过本轮统计筛选，但历史下单规则、盘口和强平验证仍未完成。"


def fmt(value: float | None, digits: int = 2) -> str:
    return "—" if value is None else f"{value:.{digits}f}"


def render_report(results: list[dict], decisions: list[dict], manifest: dict) -> str:
    lines = ["# ZEC 短线顺势多空：封存期之外的首次回测", "",
             "本轮仅验证预先固定的简单候选。所有 2026 年行情均未进入数据集；最近五个月没有用于选参、比较或查看表现。", "",
             "## 可以直接理解的结论", ""]
    for d in decisions:
        lines.append(f"- 净目标{d['target_pct'] * 100:.0f}%、最长{d['hold_hours']}小时：**{d['verdict']}**。{d['reason']}")
    lines += ["", "结论针对这套固定规则，不代表所有短线趋势交易均有效或无效；没有展示为上涨/下跌预测概率，也没有修改正式策略。", "",
              "## 试验与数据", "",
              "- Binance USD-M ZECUSDT 永续，5M 路径、15M 突破、1H EMA20方向；不等待回踩。",
              "- 2023-12仅预热；2024开发/诊断，2025按时间顺序验证。每个年段独立从110 USDT开始。",
              "- 封存起点：2026-06-23 00:00北京时间（2026-06-22 16:00 UTC）；本次额外保留整个2026年。",
              "- 目标为入场权益净增1%/2%；最长2H/4H。名义仓位至多入场权益1倍，单笔计划总风险上限5 USDT。",
              "- 常规：单边手续费5bps、滑点3bps；压力：各10bps。这是成本情景，不是用户实际费率。",
              "- 资金费保留原始毫秒时刻；结算标记价格由所在5M桶mark开盘代理，不能等同真实账单。",
              "- 五分钟执行延迟；跳空止损按更差价；同柱双触发止损优先。", "",
              "## 完整结果（不按收益挑选参数）", "",
              "| 年段 | 目标 | 最长持仓 | 成本 | 交易数 | 净盈利胜率 | 平均净R | PF | 净收益 | 最大回撤 | 最长连亏 |",
              "|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|"]
    for row in results:
        m = row["metrics"]
        lines.append(f"| {row['window']} | {row['target_pct']*100:.0f}% | {row['hold_hours']}H | {row['cost']} | {m['trades']} | {fmt(None if m['net_win_rate'] is None else m['net_win_rate']*100)}% | {fmt(m['mean_net_r'],4)} | {fmt(m['profit_factor'])} | {fmt(m['net_return_pct'])}% | {fmt(m['max_drawdown_pct'])}% | {m['longest_losing_streak']} |")
    lines += ["", "## 2025验证段分方向及不确定性", "",
              "| 目标/期限 | 成本 | 多头笔数/净盈亏USDT | 空头笔数/净盈亏USDT | 平均净R的月份分块95%区间 | 同柱歧义交易 |",
              "|---|---|---|---|---|---:|"]
    for row in results:
        if row["window"] != "validation_2025":
            continue
        m = row["metrics"]
        a, b, ci = m["by_side"]["long"], m["by_side"]["short"], m["monthly_cluster_mean_r_ci95"]
        ci_text = "—" if ci is None else f"[{ci[0]:.4f}, {ci[1]:.4f}]"
        lines.append(f"| {row['target_pct']*100:.0f}%/{row['hold_hours']}H | {row['cost']} | {a['trades']} / {a['net_pnl_usdt']:.2f} | {b['trades']} / {b['net_pnl_usdt']:.2f} | {ci_text} | {m['ambiguous_bars']} |")
    lines += ["", "## 结果的实际边界", "",
              "- 原系统现货4H runner未被当作永续多空基准。本轮不是原七条件规则的完整消融研究。",
              "- 使用连续数学数量，未重建历史最小下单量、最小名义、tick size、盘口、部分成交与完整强平制度；不证明110 USDT账户已经可实盘执行。",
              "- 止损是计划风险，跳空、资金费异常及实际成交可使亏损超过估计；最大回撤为5M采样的净清算权益，不含柱内更差路径。",
              "- 柱内资金费与未知柱内止盈止损采用固定先收资金费顺序；对收款方向并非一概保守，逐笔记录相关标记，不冒充逐笔成交重建。",
              "- 资金费使净目标越过整根柱区间时，使用区间内最不利可见价代理并记录target_clamped_to_bar，不能视为精确成交价格。技术复算保留修正前运行，交易参数没有改变。",
              "- 只有12个验证月份；月份分块区间是描述性不确定性估计，不能保证独立同分布或覆盖未来市场。",
              "- 2025年属于本轮按时间顺序保留的验证段；旧系统的其他研究可能已使用过这些历史年份，不能称为从未接触过的全新留出集。珍贵封存期仍未启封。",
              "- ZEC为用户预先指定币种，结论不能外推所有币；本次没有模型训练或校准的未来涨跌概率。",
              "- 验证结果不作为本轮调参依据；下一轮新假设须重新预注册，并继续避开封存期。", "",
              "## 复查文件", "",
              "- PROTOCOL.md：读行情前冻结的候选、边界与判断标准。",
              "- summary.json、monthly.csv：所有配置与逐月结果。",
              "- trades.csv：逐笔净盈亏、成本、资金费、止损与退出原因。",
              "- equity.csv：按小时与每笔退出保留的权益点（回撤指标用完整5M曲线计算）。",
              "- data_manifest.json、run_manifest.json：源URL、SHA256、实际时间范围与代码哈希。", "",
              "来源：[Binance官方归档格式](https://github.com/binance/binance-public-data)、[资金费字段说明](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History)。", ""]
    return "\n".join(lines)


def main() -> None:
    # The original project's editable venv may point at another worktree.
    # Always use the source whose bytes are frozen in this run's manifest.
    sys.path.insert(0, str(ROOT / "src"))
    from .data import load_dataset
    from .engine import run_replay, signals
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--download", action="store_true")
    args = parser.parse_args()
    cache, out = args.cache_dir.resolve(), args.output_dir.resolve()
    if cache == out or cache.is_relative_to(ROOT / "data") or out.is_relative_to(ROOT / "data"):
        raise ValueError("Use distinct isolated cache/output directories, never production data/.")
    out.mkdir(parents=True, exist_ok=True)
    files = [Path(__file__).parent / name for name in ("PROTOCOL.md", "engine.py", "data.py", "run.py")]
    files.append(ROOT / "src/crypto_trading_system/indicators.py")
    frozen_hashes = {str(p.relative_to(ROOT)).replace("\\", "/"): sha256(p) for p in files}
    save_json(out / "pre_run_manifest.json", {"frozen_at_utc": datetime.now(UTC).isoformat(),
              "cutoff_ms": CUTOFF_MS, "source_sha256": frozen_hashes})
    months = ["2023-12"] + [f"{y}-{m:02d}" for y in (2024, 2025) for m in range(1, 13)]
    print("Loading only frozen 2023-12..2025-12 USDM archives", flush=True)
    bars, funding, data_manifest = load_dataset(cache, months=months, cutoff_ms=CUTOFF_MS, download=args.download)
    save_json(out / "data_manifest.json", data_manifest)
    print(f"Validated bars={len(bars)} funding={len(funding)}; computing causal signals", flush=True)
    prepared = signals(bars, cutoff_ms=CUTOFF_MS)
    results, all_trades, all_months, sampled_equity = [], [], [], []
    import inspect
    accepts_prepared = "precomputed_signals" in inspect.signature(run_replay).parameters
    for window, start, end in WINDOWS:
        for target in (0.01, 0.02):
            for hours in (2, 4):
                for cost, fee, slip in COSTS:
                    tag = {"window": window, "target_pct": target, "hold_hours": hours, "cost": cost}
                    print(f"Replay {tag}", flush=True)
                    extra = {"precomputed_signals": prepared} if accepts_prepared else {}
                    result = run_replay(bars, funding, timestamp(start), timestamp(end), target, hours, fee, slip,
                                        cutoff_ms=CUTOFF_MS, initial_equity=110, **extra)
                    trades, curve = result["trades"], result["equity_curve"]
                    monthly = monthly_rows(trades, timestamp(start), timestamp(end))
                    metrics = stats(trades, curve, result["final_equity"], monthly)
                    results.append({**tag, "metrics": metrics, "monthly": monthly,
                                    "signal_count": result["signal_count"], "skip_counts": result["skip_counts"]})
                    for trade in trades:
                        all_trades.append({**tag, **trade, "entry_utc": iso(trade["entry_ms"]), "exit_utc": iso(trade["exit_ms"])})
                    all_months.extend({**tag, **m} for m in monthly)
                    exit_times = {t["exit_ms"] for t in trades}
                    selected = {p["time_ms"]: p for p in curve
                                if (p["time_ms"] + 1) % 3600000 == 0 or p["time_ms"] in exit_times
                                or p["time_ms"] == timestamp(start)}
                    # Open-price TIME/gap exits occur between sampled candle closes.
                    for trade in trades:
                        selected[trade["exit_ms"]] = {"time_ms": trade["exit_ms"], "equity": trade["equity_after"]}
                    sampled_equity.extend({**tag, **p, "time_utc": iso(p["time_ms"])}
                                          for _, p in sorted(selected.items()))
    decisions = []
    for target in (0.01, 0.02):
        for hours in (2, 4):
            pair = [r for r in results if r["window"] == "validation_2025" and r["target_pct"] == target and r["hold_hours"] == hours]
            decision, reason = verdict(next(r for r in pair if r["cost"] == "normal"), next(r for r in pair if r["cost"] == "stress"))
            decisions.append({"target_pct": target, "hold_hours": hours, "verdict": decision, "reason": reason})
    final_hashes = {str(p.relative_to(ROOT)).replace("\\", "/"): sha256(p) for p in files}
    if final_hashes != frozen_hashes:
        raise RuntimeError("Source changed during the frozen experiment; do not interpret partial results.")
    commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
    run_manifest = {"base_git_commit": commit, "generated_at_utc": datetime.now(UTC).isoformat(),
                    "cutoff_ms": CUTOFF_MS, "holdout_start_beijing": "2026-06-23T00:00:00+08:00",
                    "max_loaded_bar_close_ms": max(int(b[6]) for b in bars),
                    "max_loaded_funding_time_ms": max(f["time_ms"] for f in funding),
                    "all_2026_market_data_excluded": True,
                    "production_database_opened_by_this_runner": False,
                    "source_sha256": frozen_hashes,
                    "protocol": "All four predeclared candidates retained; no selection using 2025 validation."}
    save_json(out / "run_manifest.json", run_manifest)
    save_json(out / "summary.json", {"results": results, "decisions": decisions})
    write_csv(out / "trades.csv", all_trades)
    write_csv(out / "monthly.csv", all_months)
    write_csv(out / "equity.csv", sampled_equity)
    (out / "report.md").write_text(render_report(results, decisions, data_manifest), encoding="utf-8")
    (out / "PROTOCOL.md").write_bytes((Path(__file__).parent / "PROTOCOL.md").read_bytes())
    print(json.dumps({"output": str(out), "decisions": decisions}, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
