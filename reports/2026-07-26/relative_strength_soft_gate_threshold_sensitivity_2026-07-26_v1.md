# Relative Strength Soft Gate Threshold Sensitivity

- Review time: `2026-07-26 12:20 +08:00`
- Experiment family: `relative_strength_soft_gate`
- Dynamic master: `reports/2026-06-09/dynamic_master_full.json`
- Windows:
  - `2024-07-01 -> 2025-06-01`
  - `2025-06-01 -> 2026-06-01`
- Strategy/config deployment: none
- `settings.toml`: unchanged

## Question

Can a different relative-strength threshold keep the PF/net-return improvement from `-0.5` while reducing the early-window MDD deterioration?

## Summary

| Threshold | Summary verdict | Net improved periods | PF improved periods | MDD improved periods | Main issue |
|---:|---|---:|---:|---:|---|
| `-1.0` | `retest` | 1 / 2 | 1 / 2 | 0 / 2 | Too loose; near window degrades |
| `-0.5` | `retest` | 2 / 2 | 2 / 2 | 1 / 2 | Best balance, but early MDD worsens |
| `0.0` | `retest` | 2 / 2 | 2 / 2 | 1 / 2 | Strong near window, worst early MDD |

## Window Results

### Threshold `-1.0`

| Period | Closed B -> V | Win B -> V | PF B -> V | Sharpe B -> V | MDD B -> V | Net B -> V | Stop B -> V | Verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `2024-07-01 -> 2025-06-01` | 76 -> 79 | 38.16% -> 41.77% | 0.95 -> 1.04 | -0.01 -> 0.26 | 16.59% -> 18.62% | -2.09% -> 2.99% | 89.47% -> 87.34% | `retest` |
| `2025-06-01 -> 2026-06-01` | 57 -> 57 | 40.35% -> 38.60% | 1.11 -> 1.03 | 0.26 -> 0.10 | 20.75% -> 20.93% | 3.11% -> 0.25% | 85.96% -> 85.96% | `reject_candidate` |

Interpretation: `-1.0` is too loose. It does not filter enough weak relative-strength entries, and the near window gets worse across PF, Sharpe, MDD, and net return.

### Threshold `-0.5`

| Period | Closed B -> V | Win B -> V | PF B -> V | Sharpe B -> V | MDD B -> V | Net B -> V | Stop B -> V | Verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `2024-07-01 -> 2025-06-01` | 76 -> 87 | 38.16% -> 43.68% | 0.95 -> 1.09 | -0.01 -> 0.39 | 16.59% -> 18.96% | -2.09% -> 5.63% | 89.47% -> 87.36% | `retest` |
| `2025-06-01 -> 2026-06-01` | 57 -> 51 | 40.35% -> 41.18% | 1.11 -> 1.27 | 0.26 -> 0.54 | 20.75% -> 15.46% | 3.11% -> 7.88% | 85.96% -> 80.39% | `retest` |

Interpretation: `-0.5` remains the best balanced threshold. It improves net return and PF in both windows and improves near-window MDD, but early-window MDD still worsens.

### Threshold `0.0`

| Period | Closed B -> V | Win B -> V | PF B -> V | Sharpe B -> V | MDD B -> V | Net B -> V | Stop B -> V | Verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `2024-07-01 -> 2025-06-01` | 76 -> 82 | 38.16% -> 39.02% | 0.95 -> 1.02 | -0.01 -> 0.13 | 16.59% -> 20.58% | -2.09% -> 0.41% | 89.47% -> 84.15% | `retest` |
| `2025-06-01 -> 2026-06-01` | 57 -> 51 | 40.35% -> 43.14% | 1.11 -> 1.35 | 0.26 -> 0.68 | 20.75% -> 14.19% | 3.11% -> 10.67% | 85.96% -> 80.39% | `retest` |

Interpretation: `0.0` is stronger in the near window, but it makes early-window MDD materially worse (`20.58%`) and early net improvement is much smaller than `-0.5`.

## Decision

`retest`: the threshold sensitivity test does not produce a deployable relative-strength gate.

Best current threshold if this family is revisited: `-0.5`.

Reason: `-0.5` is the only threshold with broad PF/net improvement and less severe early MDD deterioration than `0.0`, while `-1.0` fails the near window. However, none of the tested thresholds solves the early-window MDD issue.

## Next Action

Do not deploy `relative_strength_soft_gate` yet.

Move the next formal single-variable A/B to `reclaim_quality_matrix / atr_reclaim_0_25`, because the relative-strength threshold family has been tested enough to show value but not enough stability for keep.
