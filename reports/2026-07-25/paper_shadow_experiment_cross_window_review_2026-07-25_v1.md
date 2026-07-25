# Paper Shadow Experiment Cross-Window Review

- Account: `demo`
- Review time: `2026-07-25 23:55 +08:00`
- Strategy/config change: none
- Data source: generated `paper checkpoint` and `paper shadow-experiment` reports under `reports/2026-07-25/`

## Window Readiness

| Window | Checkpoint verdict | Opportunities | Mature | Right-censored | Right-censored ratio | Evidence status |
|---|---|---:|---:|---:|---:|---|
| `2026-06-19 -> 2026-07-02` | `formal_audit_ready` | 78 | 51 | 27 | 34.6% | usable comparison |
| `2026-07-03 -> 2026-07-25` | `formal_audit_ready` | 102 | 75 | 22 | 21.6% | main extended evidence |
| `2026-07-17 -> 2026-07-25` | `wait_for_more_data` | 50 | 23 | 22 | 44.0% | interim only |

The `2026-07-17 -> 2026-07-25` window overlaps with the extended window and has too much right-censoring, so it is useful for direction checks only. It must not be treated as an independent approval window.

## Experiment 1: `reclaim_quality_matrix`

Question: after a plan enters `RECLAIM_PENDING`, should the system require stronger reclaim confirmation before allowing entry?

| Variant | 06-19 -> 07-02 Total R | 07-03 -> 07-25 Total R | 07-17 -> 07-25 Total R | Missed winner pattern | Review |
|---|---:|---:|---:|---|---|
| `current_4h_close_reclaim` | 28.42 | 44.14 | 15.81 | 0 / 0 / 0 | baseline |
| `confirm_1bar` | 43.92 | 29.49 | 13.75 | 1 / 4 / 1 | mixed, opportunity cost visible |
| `atr_reclaim_0_25` | 32.42 | 48.14 | 17.81 | 0 / 0 / 0 | best current candidate |
| `quality_close` | 36.42 | 46.14 | 15.81 | 0 / 0 / 0 | stable but less strong than ATR variant |

Conclusion: `retest`. `atr_reclaim_0_25` is the cleanest candidate because it improves the main extended window and does not miss winners in any tested window. `confirm_1bar` is not preferred because it repeatedly introduces missed winners and underperforms in the main extended window.

## Experiment 2: `momentum_pullback_definition_ab`

Question: is the current momentum/pullback definition too loose or too strict, and can ATR-based pullback from trend support reduce bad entries?

| Variant | 06-19 -> 07-02 Total R | 07-03 -> 07-25 Total R | 07-17 -> 07-25 Total R | Missed winner pattern | Review |
|---|---:|---:|---:|---|---|
| `current_24h_7d_positive` | -17.02 | -15.29 | -10.57 | 9 / 11 / 5 | weak baseline |
| `allow_minor_24h_pullback` | -25.02 | 12.65 | -16.57 | 9 / 6 / 5 | unstable |
| `recent_high_atr_pullback` | -0.27 | -39.66 | -15.81 | 8 / 14 / 6 | reject as current candidate |
| `trend_support_atr_pullback` | 3.33 | 25.79 | -7.41 | 7 / 4 / 3 | best candidate, still not deployable |

Conclusion: `retest`. `trend_support_atr_pullback` is the best variant across the two usable windows because it turns Total Decision R positive and cuts missed winners in the main extended window. The recent `2026-07-17 -> 2026-07-25` slice is negative, but it is right-censored and overlapping, so it downgrades confidence rather than rejecting the variant.

## Experiment 3: `relative_strength_soft_gate`

Question: should weak relative strength versus BTC/ETH block or penalize entries, and should the gate be hard or soft?

| Variant | 06-19 -> 07-02 Total R | 07-03 -> 07-25 Total R | 07-17 -> 07-25 Total R | Missed winner pattern | Review |
|---|---:|---:|---:|---|---|
| `alt_equal_hard_0` | 23.32 | 45.55 | 13.81 | 5 / 2 / 0 | viable but stricter than needed |
| `btc_eth_hard_0` | 34.59 | 43.03 | 9.14 | 3 / 4 / 2 | defensive, may over-filter |
| `btc_eth_soft_minus_0_5` | 34.08 | 48.80 | 15.81 | 2 / 1 / 0 | best current candidate |
| `risk_off_hard_0` | 32.59 | 33.03 | 1.14 | 3 / 4 / 2 | weak relative to soft gate |

Conclusion: `retest`. `btc_eth_soft_minus_0_5` has the best main-window Total Decision R and the lowest missed-winner cost. A hard gate can filter more losers, but it also increases opportunity cost, so a soft gate is the stronger research direction.

## Overall Decision

No `settings.toml` change.

Best candidates for the next formal A/B design:

1. `relative_strength_soft_gate`: prioritize `btc_eth_soft_minus_0_5`.
2. `reclaim_quality_matrix`: prioritize `atr_reclaim_0_25`.
3. `momentum_pullback_definition_ab`: keep `trend_support_atr_pullback` as a secondary candidate.

The current evidence is enough to rank offline candidates, but not enough to deploy them. The next step should be a formal, single-variable dynamic-universe A/B or a later non-overlapping paper window after more data matures.
