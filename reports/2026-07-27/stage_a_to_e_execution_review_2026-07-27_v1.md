---
created: 2026-07-27 23:57:43 CST
tags:
  - crypto
  - trading-system
  - execution-review
experiment: stage_a_to_e_execution_review
verdict: atr_reclaim_retest_path_dependent_capacity_paused
---

# stage_a_to_e_execution_review

## Plain-language conclusion

这轮计划已经执行到可决策状态：容量 replacement 分支在 Stage A 被正式冻结；`atr_reclaim_0_35` 的正式 A/B、交易级归因和阈值敏感性证据已经存在且可复用，但结论仍是 `retest_path_dependent`，不能部署。

因此 Stage E 不启动 shadow/paper 观察。原因不是条件不够完整，而是前置 gate 没通过：当前没有稳定、可解释、可执行的 edge 可以拿去 shadow。

## System Goal

当前系统级目标不是继续叠加过滤器，而是确认 entry-quality 改善是否可解释、可复核、可跨路径维持。所有结论都不修改 `config/settings.toml`，不提高 `max_active_positions`，不部署 replacement。

## Stage A - Replacement Closure

问题：Stage 4 的否定结论是否被重复事件、少数 stale trade、same-bar 歧义或月份集中污染？

证据：

- 报告：`reports/2026-07-27/replacement_closure_audit_2026-07-27_v1.md`
- total_blocked_events：512
- eligible_comparison_events：42
- unique_stale_trades：3
- stale_trade_top1_share_pct：83.333%
- first_event_per_stale_trade_R42_median：-0.004
- cluster_bootstrap_R42_p05：-0.565

结论：`paused_no_stable_executable_edge`。

解释：Stage 4 的 comparison sample 高度集中在极少数 stale slots 上。去重和聚类后，R42 仍不能证明稳定 replacement edge。因此 Stage 5 shadow replacement 不应启动。

## Stage B - atr_reclaim_0_35 Formal Single-variable A/B

问题：`atr_reclaim_0_35` 在 capacity-neutral 的正式 dynamic-universe A/B 中是否优于 baseline？

证据：

- 汇总报告：`reports/2026-07-26/abtest_summary_dynamic_universe_atr_reclaim_0_35_2026-07-26_v1.md`
- 样本：两个非重叠窗口，`2024-07-01 -> 2025-06-01` 与 `2025-06-01 -> 2026-06-01`
- sufficient_periods：2
- overlap_periods：0

核心结果：

| Window | Closed B -> V | Win B -> V | PF B -> V | Sharpe B -> V | MDD B -> V | Net B -> V |
|---|---:|---:|---:|---:|---:|---:|
| 2024-07-01 -> 2025-06-01 | 76 -> 78 | 38.16% -> 48.72% | 0.95 -> 1.62 | -0.01 -> 0.93 | 16.59% -> 14.95% | -2.09% -> 18.20% |
| 2025-06-01 -> 2026-06-01 | 57 -> 53 | 40.35% -> 45.28% | 1.11 -> 1.31 | 0.26 -> 0.60 | 20.75% -> 15.27% | 3.11% -> 9.33% |

结论：报告级 A/B 支持 `candidate_keep_review`，但只能作为进入归因复核的条件，不是部署证据。

## Stage C - Trade-level Attribution

问题：改善来自广泛过滤亏损，还是少数赢家和路径变化？

证据：

- 交易级归因：`reports/2026-07-26/atr_reclaim_0_35_trade_attribution_review_2026-07-26_v1.md`
- 路径复盘：`reports/2026-07-26/atr_reclaim_0_35_path_replay_review_2026-07-26_v1.md`

核心结果：

| Attribution Path | Contribution |
|---|---:|
| removed baseline-only | +594.76 USDT |
| added variant-only | +3184.11 USDT |
| common trade delta | -43.72 USDT |
| total | +3735.15 USDT |

关键解释：

- 改善不是来自 common trades 普遍变好，common trade delta 反而小幅为负。
- 主要改善来自 variant-only 新增赢家。
- 近端窗口 top3 正贡献超过该窗口净改善，说明存在明显路径依赖和抵消项。
- 人工路径复盘显示 variant-only winners 的 reclaim margin 均超过 0.35 ATR，但 missed baseline winners 也有高质量 TP2 样本。

结论：`atr_reclaim_0_35` 保留为有价值候选，但状态是 `retest_path_dependent`，不能 keep。

## Stage D - Threshold Sensitivity

问题：`0.35 ATR` 是稳定阈值区间，还是单点偶然？

证据：

- 报告：`reports/2026-07-26/atr_reclaim_threshold_sensitivity_2026-07-26_v1.md`
- variants：`0.10`、`0.15`、`0.25`、`0.35`

核心结果：

| Variant | Early Net | Early PF | Early MDD | Near Net | Near PF | Near MDD | Verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| baseline | -2.09% | 0.95 | 16.59% | 3.11% | 1.11 | 20.75% | n/a |
| `atr_reclaim_0_10` | 8.25% | 1.18 | 18.35% | 1.99% | 1.08 | 18.62% | retest |
| `atr_reclaim_0_15` | 9.30% | 1.20 | 18.46% | 1.36% | 1.07 | 18.62% | retest |
| `atr_reclaim_0_25` | 6.32% | 1.34 | 19.21% | 7.20% | 1.24 | 15.01% | retest |
| `atr_reclaim_0_35` | 18.20% | 1.62 | 14.95% | 9.33% | 1.31 | 15.27% | candidate_keep_review |

结论：`0.35` 是当前阈值组里最强点，但曲线不是干净的单调稳定平台。结合 Stage C 的路径依赖，它不能直接 keep。

## Stage E - Shadow/Paper Gate

问题：是否具备进入 shadow/paper 观察的条件？

Gate 结果：不通过。

原因：

- Stage A 冻结 capacity replacement，不能进入 shadow replacement。
- Stage C 显示 `atr_reclaim_0_35` 的收益来源仍高度路径依赖。
- Stage D 说明 `0.35` 是当前最强点，但还不是稳定平台。

结论：Stage E 当前不执行。后续如果要重启 shadow，必须先有新的可解释机制：要么 `atr_reclaim_0_35` 在新窗口中继续呈现交易级稳定改善，要么 capacity 分支提出新的事前声明 slot-selection 规则。

## Final Decision

- capacity branch：`paused_no_stable_executable_edge`
- `atr_reclaim_0_35`：`retest_path_dependent`
- Stage 5 / Stage E：not started because gate failed
- production config：unchanged
- next research priority：capacity-neutral entry-quality retest, not replacement and not new stacked filters

