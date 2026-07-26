---
created: 2026-07-26 18:10:00 CST
tags:
  - crypto
  - trading-system
  - abtest-review
experiment_family: atr_reclaim_threshold_sensitivity
verdict: candidate_keep_review
best_candidate: atr_reclaim_0_35
report_version: v1
---

# ATR reclaim threshold sensitivity v1

## Background

`atr_reclaim_0_25` improved net return, profit factor, Sharpe, and win rate in both walk-forward windows, but its early-window max drawdown worsened. This sensitivity test checks whether the drawdown issue came from the `0.25 ATR` threshold, or from the reclaim-margin mechanism itself.

## Experiments

- Baseline: current default strategy, with `entry_reclaim_close_enabled=true` and no ATR reclaim margin.
- Variants: `atr_reclaim_0_10`, `atr_reclaim_0_15`, `atr_reclaim_0_25`, `atr_reclaim_0_35`.
- Symbol universe: fixed `reports/2026-06-09/dynamic_master_full.json`, dynamic universe replay, master_count=418.
- Periods: `2024-07-01 -> 2025-06-01` and `2025-06-01 -> 2026-06-01`.
- Default config: `config/settings.toml` was not changed.

## Summary

| Variant | Early Net | Early PF | Early MDD | Early Stop | Near Net | Near PF | Near MDD | Near Stop | Verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| baseline | -2.09% | 0.95 | 16.59% | 89.47% | 3.11% | 1.11 | 20.75% | 85.96% | n/a |
| `atr_reclaim_0_10` | 8.25% | 1.18 | 18.35% | 82.50% | 1.99% | 1.08 | 18.62% | 85.19% | retest |
| `atr_reclaim_0_15` | 9.30% | 1.20 | 18.46% | 84.00% | 1.36% | 1.07 | 18.62% | 86.54% | retest |
| `atr_reclaim_0_25` | 6.32% | 1.34 | 19.21% | 78.48% | 7.20% | 1.24 | 15.01% | 87.04% | retest |
| `atr_reclaim_0_35` | 18.20% | 1.62 | 14.95% | 76.92% | 9.33% | 1.31 | 15.27% | 84.91% | candidate_keep_review |

## Interpretation

The sensitivity curve is not monotonic at the low thresholds. `0.10` and `0.15` improve the early window but degrade near-window net return and profit factor. These thresholds are too weak to reliably separate strong reclaim from ordinary noise.

`0.25` is better balanced than `0.10` and `0.15`, but it still worsens early-window max drawdown. It confirms that reclaim margin has value, but it does not solve the path-risk problem.

`0.35` is the strongest threshold in this set. It improves net return, profit factor, Sharpe, win rate, max drawdown, and stop rate in both non-overlapping windows. It is the first ATR reclaim threshold that clears the automatic `candidate_keep_review` rule.

## Decision

`candidate_keep_review` for `atr_reclaim_0_35`; do not deploy yet.

Reason: both sufficient, non-overlapping windows improved net return, profit factor, and max drawdown, but the rule still needs manual path/source review before changing default strategy settings.

## Next Action

Review `atr_reclaim_0_35` trade-level attribution before keep:

- Compare variant-only, baseline-only, and common trades.
- Check whether improvement comes from broad loser filtering or a small number of large winners.
- Inspect MDD timing and stop clusters in both windows.
- If the improvement is broad-based, prepare a keep review for `entry_reclaim_min_atr_enabled=true` and `entry_reclaim_min_atr=0.35`.

