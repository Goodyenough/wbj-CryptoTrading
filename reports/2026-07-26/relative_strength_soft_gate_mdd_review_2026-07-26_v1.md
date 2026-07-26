# Relative Strength Soft Gate MDD Review

- Review time: `2026-07-26 00:55 +08:00`
- Experiment: `relative_strength_soft_gate_btc_eth_minus_0_5`
- Window: `2024-07-01 -> 2025-06-01`
- Baseline report: `reports/2026-07-26/backtest_dynamic_universe_2024-07-01_2025-06-01_v1.md`
- Variant report: `reports/2026-07-26/backtest_dynamic_universe_2024-07-01_2025-06-01_v2.md`
- A/B summary: `reports/2026-07-26/abtest_summary_dynamic_universe_relative_strength_soft_gate_btc_eth_minus_0_5_2026-07-26_v1.md`

## Question

Why did the variant improve net return, profit factor, Sharpe, and stop rate, but worsen max drawdown from `16.59%` to `18.96%` in the early walk-forward window?

## Headline

The drawdown deterioration is path-dependent. The variant created a much higher closed-PnL peak after a strong November 2024 winner cluster, then gave back more through December 2024 and May 2025. The rule is still economically positive in this window, but it increases path volatility by changing which candidates occupy capacity.

## Trade Set Reconciliation

| Bucket | Count | Net PnL |
|---|---:|---:|
| Baseline closed trades | 76 | -240.79 |
| Variant closed trades | 87 | 500.54 |
| Common trades | 45 | n/a |
| Variant-only trades | 42 | 565.32 |
| Baseline-only trades | 31 | -210.42 |
| Common-trade PnL delta | 33 changed | -34.41 |

Interpretation: the improvement mostly came from changing the selected trade set, not from better fills on the same trades. Variant-only trades added `+565.32`; removing baseline-only trades avoided a net losing bucket of `-210.42`; common trades were slightly worse by `-34.41`.

## Variant-Only Monthly Pattern

| Month | Variant-only trades | Net PnL |
|---|---:|---:|
| 2024-09 | 5 | -500.07 |
| 2024-10 | 3 | 260.64 |
| 2024-11 | 15 | 2,089.38 |
| 2024-12 | 9 | -364.83 |
| 2025-01 | 2 | -237.99 |
| 2025-05 | 8 | -681.81 |

The key driver is a large positive November cluster followed by December and May giveback. This makes max drawdown worse even though final net return is better.

## Closed-PnL Drawdown Proxy

This proxy uses closed trade PnL only. It does not fully reconstruct mark-to-market equity drawdown, but it identifies the trade-set path pressure.

| Arm | Final closed PnL | Max closed-PnL drawdown proxy | Worst point | Closed-PnL peak |
|---|---:|---:|---|---:|
| Baseline | -240.79 | 1,361.76 | 2025-04-25 04:00 UTC | 1,094.93 |
| Variant | 500.54 | 2,046.19 | 2025-05-23 16:00 UTC | 2,546.73 |

Interpretation: variant reached a much higher peak, then lost more absolute PnL from that peak. This explains why MDD can worsen while final net return improves.

## Worst Variant-Only Losses

| Created UTC | Symbol | Net PnL | Net R | Exit |
|---|---|---:|---:|---|
| 2024-12-03 08:00 | OPUSDT | -132.22 | -1.02 | Stop loss |
| 2024-12-06 00:00 | THETAUSDT | -131.77 | -1.02 | Stop loss |
| 2024-12-06 00:00 | TAOUSDT | -131.19 | -1.01 | Stop loss |
| 2024-12-15 00:00 | LDOUSDT | -126.72 | -1.01 | Stop loss |
| 2024-12-10 12:00 | BEAMXUSDT | -124.83 | -1.01 | Stop loss |
| 2024-12-11 00:00 | IOUSDT | -122.82 | -1.01 | Stop loss |
| 2025-01-15 16:00 | CRVUSDT | -121.33 | -1.01 | Stop loss |
| 2025-05-11 12:00 | SUIUSDT | -117.49 | -1.03 | Stop loss |
| 2025-05-18 04:00 | TRXUSDT | -116.74 | -1.07 | Stop loss |
| 2025-01-28 00:00 | TAOUSDT | -116.66 | -1.01 | Stop loss |

The losses are ordinary near-`-1R` stops, not single-trade tail blowups. The MDD issue is a cluster/timing problem.

## Best Variant-Only Winners

| Created UTC | Symbol | Net PnL | Net R | Exit |
|---|---|---:|---:|---|
| 2024-11-12 16:00 | DOTUSDT | 286.42 | 2.65 | TP2 |
| 2024-11-12 16:00 | GALAUSDT | 285.77 | 2.58 | TP2 |
| 2024-11-11 00:00 | XRPUSDT | 266.08 | 2.52 | TP2 |
| 2024-11-04 04:00 | RAYUSDT | 246.24 | 2.65 | TP2 |
| 2024-10-12 04:00 | SHIBUSDT | 240.55 | 2.68 | TP2 |

The same rule that changes capacity enough to catch these winners also admits later losing clusters. This supports `retest`, not `reject`.

## Conclusion

`retest`: the early-window MDD deterioration is not caused by a catastrophic new trade or a globally bad rule. It is caused by path dependence: variant-only winners lift the equity peak sharply in November, then variant-only stop clusters in December, January, and May create a larger peak-to-trough move.

## Next Action

Do not deploy the rule yet. The next useful test is threshold sensitivity on the same single dimension:

1. `relative_strength_soft_gate_btc_eth_minus_1_0`
2. `relative_strength_soft_gate_btc_eth_0_0`

Keep the experiment single-variable and compare whether a looser or harder threshold preserves the two-window PF/net improvement while reducing early-window MDD.
