---
created: 2026-07-30 00:57:53 +08:00
tags:
  - crypto
  - trading-system
  - universe-audit
  - atr-reclaim
experiment: atr_reclaim_stage_n2_gate_decision
verdict: third_window_diagnostic_only_do_not_rerun_n1
---

# atr_reclaim Stage N2 Gate Decision

## System Goal

降低 `atr_reclaim_0_35` 第三历史窗口研究中的 universe / data substrate 偏差，避免在样本底座不干净时继续解释组合改善。

## Single Question

`2023-07-01 -> 2024-07-01` 第三窗口是否具备资格作为 `atr_reclaim_0_35` 的验证窗口？

## Roadmap Position

这是 N2 数据有效性前置检查。只有第三窗口通过 N2 与重跑 N0 后，才允许进入修正 universe 上的 N1；如果仍然出现“组合改善、直接机制失败”，才进入路径分叉审计。

## Facts

- N2-A 使用 `reports/2026-06-09/dynamic_master_full.json` 中的 418 个 current master symbols，补齐 Binance first available 1d kline listing date。
- N2-A 结果：`listing_dates_count=418`，`listed_after_window=152`，`listed_inside_window=49`，`full_window_coverage=208`，`partial_window_coverage=9`。
- N2-B 使用 Binance public-data `data/spot/monthly/klines/*/1d/` 审计窗口内历史 USDT symbol membership。
- N2-B 结果：窗口内存在 1d monthly data 的历史 USDT symbols 为 `413` 个，其中 `266` 个在 current master 中，`147` 个不在 current master 中。
- 使用 listing-enriched master 重跑 N0 后，N0 verdict 为 `n0_conditional_pass_with_alignment_warning`。
- N0 的 kline cache coverage 仍约为 `56.1%`，空历史 K 线 symbol 为 `152` 个，partial symbols 为 `59` 个。

## Observations

- 当前 master 的 listing date 能解释大量无历史 K 线样本：很多 current master symbols 是窗口之后才上市。
- 但 N2-B 暴露了更关键的问题：第三窗口内真实存在过的许多 Binance USDT symbols 已经不在 current master 中。
- 因此，当前第三窗口的 baseline / variant 都是在“当前存活币集合”上回看历史，不是完整 historical membership。

## Hypothesis

当前 N1 中 `atr_reclaim_0_35` 的组合层改善，可能受到 survivor-biased universe 的影响。这个偏差方向无法仅靠 current master listing date 修正来证明无害。

## Decision

`third_window_diagnostic_only_do_not_rerun_n1`

第三窗口不升级为 clean confirmatory validation，也不在当前修正条件下重跑 N1。原因是 historical membership gap 达到 `147 / 413 = 35.6%`，超过可以视为轻微 universe limitation 的范围。

## Gate Outcome

| Step | Outcome |
|---|---|
| 1. 补 listing date 和 earliest K-line | 完成 |
| 2. 审计未来上市币 | 完成；current master 中 `152` 个 symbol 在窗口后上市 |
| 3. 尽量补历史退市币和 historical membership | 完成第一层 public-data 审计；发现 `147` 个 historical symbols 缺失于 current master |
| 4. 重跑 N0 | 完成；N0 本身为 conditional pass，但必须受 N2-B 限制 |
| 5. 判断第三窗口资格 | 不合格，只能 diagnostic |
| 6. 合格后用修正后的 universe 重跑 N1 | gate failed，不执行 |
| 7. 若仍然“组合改善、直接机制失败”，再做路径分叉审计 | gate failed，不执行 |

## Consequence For atr_reclaim_0_35

`atr_reclaim_0_35` 仍是一个有观察价值的候选，但第三窗口证据降级：当前不能用该窗口支持 keep，也不能据此部署、叠加过滤器、提高 `max_active_positions` 或继续做路径分叉深挖。

## Next Action

优先构建 historical symbol membership dataset：

```text
symbol
listing_time
delisting_time
first_kline_time
last_kline_time
tradable_from
tradable_to
source
confidence
```

在这个 dataset 可用于动态构造历史 universe 前，不继续把第三窗口作为 `atr_reclaim_0_35` 的验证证据。

## Source Reports

- `reports/2026-07-30/atr_reclaim_stage_n2_universe_audit_2026-07-30_v2.md`
- `reports/2026-07-30/atr_reclaim_n0_readiness_audit_2026-07-30_v1.md`
- `reports/2026-07-30/atr_reclaim_0_35_n1_diagnostic_retest_review_2026-07-30_v1.md`
