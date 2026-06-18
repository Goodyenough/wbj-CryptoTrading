---
report_type: paper_review
experiment_id: reclaim_pending_opportunity_cost_review
verdict: keep_observing
reason: 当前 RECLAIM_PENDING 样本集中在 ONDOUSDT 单一计划，8 次拦截价格均低于 entry_low，未显示真实入场机会被 reclaim_close 错过。
next_action: 继续让 4h update 收集更多 RECLAIM_PENDING 后续路径，三周复盘时按 plan 级别重新汇总。
---

# RECLAIM_PENDING Opportunity Cost Review v1

## Summary

本次复盘只读 SQLite 结构化 paper 数据与已生成报告，不修改 `settings.toml`，不新增或修改 paper plan。

结论：当前没有证据说明 `entry_reclaim_close` 造成了明显机会成本。现有 `RECLAIM_PENDING` 全部来自 ONDOUSDT 的同一个 WATCHING plan（`9734a33dea2e`），8 次事件价格均低于原计划 `entry_low=0.394505`，没有一次落在 `entry_low` 到 `entry_high` 的计划入场区间内，也没有一次 4h close 重新站上 `entry_high=0.411568`。

## Evidence Scope

- 数据源：`data/crypto_trading.db`
- plan：`9734a33dea2e`
- symbol：`ONDOUSDT`
- 观察窗口：2026-06-11 20:47:37 CST -> 2026-06-18 20:07:19 CST
- 事件数：8 次 `RECLAIM_PENDING` / `RECLAIM_PENDING_SET`
- 当前状态：`WATCHING`
- 当前价格：0.360800

限制：本地 `kline_cache` 的 ONDOUSDT 4h 数据只覆盖到 2026-06-01，因此本报告没有做 6/11 之后逐根 4h K 线回放；判断基于 paper events、snapshots 和事件中记录的最近已收 4h close。

## Plan Parameters

| Field | Value |
|---|---:|
| entry_low | 0.394505 |
| entry_high | 0.411568 |
| planned_entry_mid | 0.403036 |
| stop | 0.338446 |
| tp1 | 0.532217 |
| tp2 | 0.596808 |
| latest_price | 0.360800 |

## Event Statistics

| Metric | Value |
|---|---:|
| RECLAIM_PENDING events | 8 |
| event price min | 0.345700 |
| event price max | 0.384000 |
| event price avg | 0.363388 |
| below entry_low | 8 |
| inside entry zone | 0 |
| above entry_high | 0 |
| max event price vs entry_low | -2.66% |
| latest vs planned_entry_mid | -10.48% |
| latest vs entry_low | -8.54% |
| latest vs stop | +6.60% |
| latest vs tp1 | -32.21% |

## Event Path

| Time CST | Event price | Recorded 4h close | Classification |
|---|---:|---:|---|
| 2026-06-11 20:47:37 | 0.345700 | 0.349100 | below_entry_low |
| 2026-06-11 23:06:26 | 0.346200 | 0.349100 | below_entry_low |
| 2026-06-12 20:06:50 | 0.367000 | 0.366200 | below_entry_low |
| 2026-06-13 20:06:37 | 0.367200 | 0.367200 | below_entry_low |
| 2026-06-14 20:06:28 | 0.355500 | 0.356500 | below_entry_low |
| 2026-06-15 20:06:35 | 0.380700 | 0.383200 | below_entry_low |
| 2026-06-16 20:06:52 | 0.384000 | 0.384700 | below_entry_low |
| 2026-06-18 20:07:19 | 0.360800 | 0.362300 | below_entry_low |

## Interpretation

这批样本更像“价格跌破计划入场区间后仍未恢复”的等待案例，而不是“价格已经回到计划入场区间但因为 4h close 未 reclaim 而错过”的案例。按照当前 paper 逻辑，即使没有 `entry_reclaim_close` 过滤，价格低于 `entry_low` 时也不应触发正式入场；因此这 8 次事件不能算明确机会成本。

如果把第一条事件价格 0.345700 当成激进反事实入场价，到 2026-06-18 20:07 CST 的最新价格 0.360800，账面约为 +4.37%。但这不是系统定义的计划入场，因为它低于 `entry_low`，且距离 TP1 仍约 -32.21%，不能作为“错过高质量交易”的证据。

## Verdict

`keep_observing`

一句话原因：当前 ONDOUSDT 样本显示 `entry_reclaim_close` 没有错过已恢复到计划入场区间的机会；它主要是在阻止低于 entry_low 的弱反弹/低位等待被误解成入场。

## Next Action

继续让 4h update 收集更多路径。三周复盘时按 plan 级别重新统计：

- 拦截后重新站上 `entry_high` 并入场的次数
- 拦截后跌破 stop / invalidated 的次数
- 拦截后一直低于 entry_low 或 entry_high 的次数
- 拦截后如果按激进入场价计算的最大有利/不利 excursion
