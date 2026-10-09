"""Validate frozen run cash/fees and render every prespecified result branch."""
from __future__ import annotations
import json
from math import isclose
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports/2026-10-09/atr_fixed_history"


def fmt(value):
    return "n/a" if value is None else f"{value:.2f}"


def main():
    rows = json.loads((OUT / "summary.json").read_text(encoding="utf-8"))
    assert len(rows) == 4
    checks = []
    for path in sorted(OUT.glob("20*_*.json")):
        if path.name.endswith("_inputs.json"):
            continue
        obj = json.loads(path.read_text(encoding="utf-8"))
        result = obj["result"]
        cash = result["initial_equity"]
        for t in result["trades"]:
            if not t["entered_at_utc"]:
                continue
            cash -= t["quantity"] * t["entry_price_filled"] + t["entry_fee"]
            if t["status"] in {"CLOSED", "STOPPED", "TIME_EXIT"}:
                cash += t["quantity"] * t["exit_price_filled"] - t["exit_fee"]
                assert isclose(t["net_pnl"], t["gross_pnl"] - t["entry_fee"] - t["exit_fee"], abs_tol=1e-8)
            if result["config_snapshot"]["entry_timing"] == "confirmation_close":
                assert not t["closed_at_utc"] or t["closed_at_utc"] > t["entered_at_utc"]
                at_entry = [e["event_type"] for e in t["events"] if e["event_time_utc"] == t["entered_at_utc"]]
                assert at_entry == ["ENTERED"]
        assert isclose(cash, result["cash"], abs_tol=1e-7)
        assert isclose(result["final_equity"], result["equity_curve"][-1]["equity"], abs_tol=1e-7)
        checks.append(dict(file=path.name, cash_error=cash-result["cash"], accounting_pass=True))
    assert len(checks) == 8
    verdicts = []
    for r in rows:
        b, v = r["metrics"]["baseline"], r["metrics"]["atr035"]
        support = (v["net_return_pct"] > b["net_return_pct"] and v["profit_factor"] > b["profit_factor"]
                   and v["max_drawdown_pct"] <= b["max_drawdown_pct"] and min(b["closed_trades"], v["closed_trades"]) >= 30
                   and r["attribution"]["delta_less_top3"] > 0 and not any(r["gap_affected"].values()))
        worse = v["net_return_pct"] < b["net_return_pct"] and (v["profit_factor"] < b["profit_factor"] or v["max_drawdown_pct"] > b["max_drawdown_pct"])
        verdicts.append(dict(start=r["start"], timing=r["timing"], support=support, worse=worse))
    support_all = all(x["support"] for x in verdicts)
    rejected = all(x["worse"] for x in verdicts if x["timing"] == "confirmation_close")
    verdict = "retest_supports_further_research" if support_all else "retest_reject_stable_improvement_in_frozen_windows" if rejected else "retest_insufficient_or_sensitive"
    validation = dict(verdict=verdict, branches=verdicts, checks=checks)
    (OUT / "validation.json").write_text(json.dumps(validation, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    lines = ["# 原规则 vs ATR 0.35：修复后固定历史诊断", "", f"裁决：`{verdict}`。旧窗口 diagnostic，不作为新的样本外证据。", "",
             "## 白话结论", "",
             "ATR 0.35 暂时不能认定为稳定有效的收益改进。较早窗口里，旧成交假设显示它大幅领先；按确认收盘价成交后，它反而比原规则少赚约3.22个百分点，虽然回撤更低。等待更强确认有代价，旧回测按更早的价格回填成交会掩盖这一点。组合路径也会随之改变，所以差值不能全部归因于单笔入场溢价。",
             "较近窗口同样反转：确认收盘价成交时，净收益从原规则的-1.51%变为ATR线的-10.20%，最大回撤从17.71%扩大到20.21%。因此更准确的说法是：ATR能挡掉部分亏损机会，也会漏掉赢家，但未必减少组合整体亏损或回撤。两个固定窗口均未支持稳定收益改善；这不是对所有未来行情的证明。",
             "保留 ATR 0.35 作为研究对照，维持 retest，生产配置冻结。此前候选极少 bug 的数据分级修复属于另一项工程验收，本次收益裁决不推翻它。", "",
             "## 技术证据", "",
             "较早窗口 legacy_same_bar 的净收益差为 +38.64pp，confirmation_close 变为 -3.22pp；后者 PF 1.12→1.04、MDD 17.23%→14.81%。至少一个预声明窗口已经发生方向反转，稳定改善的支持门槛未通过。其收盘模式 baseline-only 账目中，避免亏损2626.61 USDT、错失盈利3725.63 USDT；结合共同交易、新增交易与未平仓残差，最终少321.84 USDT。以下完整保留第二窗口及全部口径。", "",
             "## 所有预声明分支", "", "表中均为 baseline → ATR0.35；百分比变化用百分点理解。", "",
             "| 窗口 | 成交口径 | 平仓数 | 净收益% | PF | 最大回撤% |", "|---|---|---:|---:|---:|---:|"]
    for r in rows:
        b, v = r["metrics"]["baseline"], r["metrics"]["atr035"]
        vals = [f"{fmt(b[k])} → {fmt(v[k])}" for k in ("closed_trades", "net_return_pct", "profit_factor", "max_drawdown_pct")]
        lines.append(f"| {r['start']} 至 {r['end']} | {r['timing']} | " + " | ".join(vals) + " |")
    lines += ["", "## 机会配对账目", "", "金额为USDT；按 symbol + plan_created_at 配对。这里的避免亏损/错失盈利包含组合路径变化，不能解释为ATR过滤的纯因果效应。capacity causal contribution = n/a。", "",
              "| 窗口/口径 | 避免亏损 | 错失盈利 | 共同平仓差值 | variant-only净额 | 未平仓/混合状态残差 | 总权益差 | 去最大3贡献后 |", "|---|---:|---:|---:|---:|---:|---:|---:|"]
    for r in rows:
        a = r["attribution"]
        keys = ("avoided_losses", "missed_profits", "common_closed_delta", "variant_only_pnl", "open_or_mixed_status_residual", "final_equity_delta", "delta_less_top3")
        lines.append(f"| {r['start']} / {r['timing']} | " + " | ".join(fmt(a[k]) for k in keys) + " |")
    lines += ["", "## 完整指标", "", "历史字段 `trades` 统计全部计划；实际入场数为 closed_trades + open_trades。", ""]
    for r in rows:
        lines += [f"### {r['start']} — {r['end']} / {r['timing']}", "", "| 指标 | baseline | ATR0.35 |", "|---|---:|---:|"]
        for key, value in r["metrics"]["baseline"].items():
            if key in {"sample_warning", "sample_sufficient"}:
                continue
            lines.append(f"| {key} | {fmt(value)} | {fmt(r['metrics']['atr035'][key])} |")
        lines += ["", f"成交后4h缺口影响：baseline {len(r['gap_affected']['baseline'])} / ATR {len(r['gap_affected']['atr035'])} 笔。", "",
                  "最大三项正向配对贡献：" + "; ".join(f"{x[0][0]} {x[0][1]}: {x[1]:.2f}" for x in r["attribution"]["largest_3_positive_contributions"]), ""]
    lines += ["## 口径与复现", "",
              "- 预声明协议：`../atr_fixed_history_protocol_v1.md`。所有8个分支的完整交易/事件/权益和指标均在本目录JSON中；inputs含逐日币池、配置和各币各周期数据SHA256；manifest含代码/协议SHA256。",
              "- 使用旧run逐日币池，保留2026-07-26存续币选择偏差；没有新建历史master。数据来自只读本地缓存，禁止网络补数；基于closed bars，warmup至少240天。",
              "- legacy_same_bar仍有收盘确认后回填entry_high的前视成交假设，只作为诊断对照。confirmation_close按确认收盘价+滑点理想成交，从下一根检查退出；零延迟且沿用maker入场费用，不能视为实盘可成交或真实市价成本。",
              "- 所有分支保留仓位容量、排序和资金限制；期末持仓按市值计算，不强平。因此平仓收益归因与总权益存在明确残差。",
              "- 当前scanner与旧研究版本不同，不能把新旧报告差值全部归因于stop修复。UNKNOWN回退缺陷另行处理；本次不改生产配置。",
              "- 独立按同一缓存、240天warmup与旧regime参数逐4h重算：早窗 RISK_OFF/NEUTRAL/RISK_ON = 1217/397/396；近窗 = 1471/221/498；两窗口 UNKNOWN 均为0。",
              "- intrabar_max_drawdown是既有快照近似，收盘入场已排除入场前low；主裁决使用close-to-close max_drawdown_pct。",
              "- 核验：8个分支逐笔费用、现金、末期权益一致；收盘模式无入场当根止盈止损。详见validation.json。",
              "- 执行期间为兼容旧源码审计，最终源码将等价raw_entry条件表达式展开，并恢复legacy blocked-event标签。运行时实际replay源码已保存executed_replay.py.txt，hash对应manifest；变动不改变成交、筛选或收益。",
              "- 重算前先保留现有产物；脚本发现summary.json会拒绝覆盖。原始缓存未提交，复现需匹配inputs中的每组数据hash。", ""]
    (OUT / "report.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps(validation, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
