---
created: 2026-07-26 15:45:00 CST
tags:
  - crypto
  - trading-system
  - abtest-review
experiment_id: atr_reclaim_0_25
verdict: retest
report_version: v1
---

# atr_reclaim_0_25 formal A/B review v1

## Experiment

- Experiment: `atr_reclaim_0_25`
- Change tested: keep the current `entry_reclaim_close_enabled=true` baseline, but require the reclaim close to exceed `entry_high` by at least `0.25 * ATR`.
- Changed params: `analysis.entry_reclaim_min_atr_enabled: false -> true`, `analysis.entry_reclaim_min_atr: 0.0 -> 0.25`
- Symbol universe: fixed `reports/2026-06-09/dynamic_master_full.json`, dynamic universe replay, master_count=418.
- Periods: `2024-07-01 -> 2025-06-01` and `2025-06-01 -> 2026-06-01`.
- Default config: `config/settings.toml` was not changed.

## Results

| Period | Closed B -> V | Win B -> V | PF B -> V | Sharpe B -> V | MDD B -> V | Net B -> V | Stop B -> V |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2024-07-01 -> 2025-06-01 | 76 -> 79 | 38.16% -> 43.04% | 0.95 -> 1.34 | -0.01 -> 0.41 | 16.59% -> 19.21% | -2.09% -> 6.32% | 89.47% -> 78.48% |
| 2025-06-01 -> 2026-06-01 | 57 -> 54 | 40.35% -> 44.44% | 1.11 -> 1.24 | 0.26 -> 0.50 | 20.75% -> 15.01% | 3.11% -> 7.20% | 85.96% -> 87.04% |

## Interpretation

This is a valuable entry-quality candidate. Net return, profit factor, Sharpe, and win rate improved in both non-overlapping windows. The near window also improved max drawdown materially.

The rule still cannot be kept directly. The early window max drawdown deteriorated from `16.59%` to `19.21%`, and the near-window stop rate was slightly worse. That means the ATR reclaim threshold improves average trade quality, but does not yet prove stable drawdown control.

The result is stronger than the relative-strength family because the core profitability metrics improved in both windows. The main unresolved issue is path risk: stricter reclaim can delay entries into later bars, which may improve confirmation but can also enter after a short-term move has already stretched.

## Decision

`retest`: keep as a high-value candidate, but do not deploy to `settings.toml`.

Reason: two-window PF/net/Sharpe improvements are promising, but early-window MDD worsened and near-window stop rate did not improve.

## Next Action

Run threshold sensitivity within the same reclaim-quality dimension before combining with other filters:

- `atr_reclaim_0_10`
- `atr_reclaim_0_15`
- `atr_reclaim_0_35`

The goal is to find whether the early-window MDD deterioration is caused by the `0.25 ATR` threshold being too strict, or by the reclaim-margin mechanism itself.

