---
created: 2026-07-29 23:50:00 CST
tags:
  - crypto
  - trading-system
  - experiment-card
  - atr-reclaim
experiment: atr_reclaim_0_35_n1_diagnostic_retest
status: gated_by_n0_conditional_pass
---

# atr_reclaim_0_35 N1 Diagnostic Retest Card

## 1. System Goal

当前系统级目标不是部署新规则，而是判断 `entry_reclaim_min_atr=0.35` 是否仍值得继续研究为单变量入场质量规则。

## 2. Single Question

在固定 baseline、固定 symbol master、固定窗口 `2023-07-01 -> 2024-07-01`、不叠加任何其他过滤器的前提下，`atr_reclaim_0_35` 是否还能改善组合级表现，并且改善是否至少部分来自直接过滤弱 reclaim，而不是主要来自容量路径偶然变化。

## 3. Roadmap Position

这是 Stage N0 后的 N1。N0 结论是 `n0_conditional_pass_with_universe_bias_warning`，因此 N1 只能叫 third-window diagnostic retest，不能叫 clean confirmatory validation。

## 4. Facts / Observations / Hypotheses / Decisions

- Fact: N0 报告 `reports/2026-07-29/atr_reclaim_n0_readiness_audit_2026-07-29_v1.md` 显示 `git_dirty=False`，固定 commit 为 `4910a67f103d2c6d116f585e04bf66eaad7e2915`。
- Fact: 固定 master 为 `reports/2026-06-09/dynamic_master_full.json`，`symbol_master_count=418`，但 `listing_dates_present=false`。
- Fact: 第三窗口本地 K 线完整覆盖符号为 207 个，部分覆盖 59 个，完全无历史 K 线 152 个；1h/4h/1d 覆盖率约 56.1%。
- Observation: 这些空 K 线符号很可能包含 2023-07-01 后才上市的当前交易对，因此不能简单视为缓存损坏，也不能忽略 survivor/listing-date bias。
- Hypothesis: 如果 `0.35 ATR` 是真实入场质量改善，第三窗口 diagnostic 应该在组合级和直接 filtered/retained 机会层都看到方向一致的改善。
- Decision: 可以准备 N1 diagnostic；但在补齐 listing-date 或历史 membership 证据前，不能把 N1 结果用于 keep 或部署。

## 5. Fixed Conditions

- Main test only: baseline vs fixed `atr_reclaim_0_35`。
- Variant only changes:
  - `analysis.entry_reclaim_min_atr_enabled=true`
  - `analysis.entry_reclaim_min_atr=0.35`
- Do not run neighboring thresholds as part of the main judgment.
- If `0.30` or `0.40` is later explored, it is a new exploratory hypothesis, not a rescue of `0.35`.
- Do not change `max_active_positions`。
- Do not enable capacity replacement。
- Do not add relative strength, MACD, trend, liquidity, or holding-time filters。
- Do not modify `config/settings.toml`。

## 6. Required Evidence

### Portfolio Layer

- Baseline vs variant trades / closed_trades / sample_sufficient。
- Net return, profit factor, Sharpe, Sortino if available, max drawdown, win rate, stop rate。
- Fee/slippage/capital/position rules must match frozen baseline snapshot。
- Report must clearly label the universe caveat from N0。

### Mechanism Layer

- Direct filtered vs retained opportunity metrics:
  - filtered loser count and R avoided。
  - missed winner count and R opportunity cost。
  - first-hit outcome split。
  - MFE/MAE or available proxy。
  - fixed-horizon R where available。
- Capacity-path trades added because slots were freed must not be interpreted as direct filter quality improvement。
- Cluster concentration by symbol, month, and symbol-month must be reported before judging mechanism。

## 7. Approval Criteria

Support the hypothesis only if all are true:

- Variant improves profit factor and net return without increasing max drawdown versus baseline。
- Closed-trade sample remains sufficient。
- Improvement is not dominated by one symbol-month or a very small winner cluster。
- Direct filtered opportunities show avoided loser R greater than missed winner R。
- Mechanism evidence and portfolio evidence point in the same direction。

Reject the hypothesis if any are true:

- Net return or profit factor worsens materially。
- Max drawdown worsens materially even if net return improves。
- Missed winner opportunity cost is greater than avoided loser benefit。
- Improvement is mainly from capacity-path replacement trades rather than direct filtering。
- Results are dominated by one symbol-month cluster。

Insufficient evidence if any are true:

- Sample is insufficient。
- Universe/listing-date caveat prevents clean interpretation。
- Opportunity alignment cannot separate direct filter effect from capacity-path effect。
- Portfolio improves but mechanism layer is weak or contradictory。

## 8. N1 Gate Decision

Current decision: prepare but do not yet run as confirmatory validation.

Recommended execution path:

1. Prefer first generating or fetching a listing-date enriched symbol master, then rerun N0。
2. If N1 is run before that, label it diagnostic only and keep production config frozen。
3. After N1, update experiment ledger with `keep / revert / retest` using the criteria above。

## 9. Production Permission

N1 does not permit production deployment. Even a strong diagnostic result can only move `atr_reclaim_0_35` from `retest_path_dependent` to `candidate_keep_review`, unless listing-date/historical-membership risk is resolved and mechanism evidence is clean.
