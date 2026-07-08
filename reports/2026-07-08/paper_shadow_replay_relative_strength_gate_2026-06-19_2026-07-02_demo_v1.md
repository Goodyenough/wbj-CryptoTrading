---
created: 2026-07-08 17:13:52 CST
tags:
  - crypto
  - trading-system
  - shadow-replay
account: demo
start_date: 2026-06-19
end_date: 2026-07-02
variant: relative_strength_gate
report_version: v1
---

# Paper Shadow Replay relative_strength_gate 2026-06-19 -> 2026-07-02 demo v1

This is an offline diagnostic replay. It does not modify settings, plans, events, or paper state.

## Summary

- opportunities: 71
- baseline_entries: 61
- variant_entries: 27
- filtered_loser: 13
- missed_winner: 4
- improved_path: 0
- worse_path: 0
- delayed_entry: 0
- kept_by_relative_strength: 29

## Decision Counts

| Decision | Count |
|---|---:|
| kept_by_relative_strength | 29 |
| filtered_unknown | 15 |
| filtered_loser | 13 |
| no_baseline_entry | 5 |
| data_gap | 5 |
| missed_winner | 4 |

## Replay Details

| Source | Symbol | ID | First Time | Baseline Entry | Variant Entry | Baseline Hit | Variant Hit | Baseline MFE_R | Variant MFE_R | Symbol Ret | Benchmark Ret | RS | Decision | Explanation |
|---|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| RECLAIM_PENDING | `ONDOUSDT` | `9734a33dea2e` | 2026-06-19 00:10 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | -2.10% | -0.07% | -2.03% | no_baseline_entry | price never closed back above entry_high |
| REJECT | `ETHUSDT` | `a4116cc70ea1:ETHUSDT` | 2026-06-19 20:06 | 2026-06-19 23:59 @ 1707.860000 | 2026-06-19 23:59 @ 1707.860000 | stop_first | stop_first | 1.18 | 1.18 | 1.92% | 1.71% | 0.21% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| REJECT | `SOLUSDT` | `a4116cc70ea1:SOLUSDT` | 2026-06-19 20:06 | 2026-06-19 23:59 @ 69.330000 | 2026-06-19 23:59 @ 69.330000 | near_tp1_first | near_tp1_first | 1.94 | 1.94 | 3.88% | 1.71% | 2.17% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `WLDUSDT` | `a4116cc70ea1:WLDUSDT` | 2026-06-19 20:06 | 2026-06-19 23:59 @ 0.617900 | n/a @ n/a | stop_first | no_variant_entry | 0.67 | n/a | -0.19% | 1.71% | -1.90% | filtered_loser | relative strength gate would avoid a baseline stop-first path |
| WATCH_ONLY | `XLMUSDT` | `a4116cc70ea1:XLMUSDT` | 2026-06-19 20:06 | 2026-06-19 23:59 @ 0.222500 | n/a @ n/a | stop_first | no_variant_entry | 0.10 | n/a | -3.06% | 1.71% | -4.76% | filtered_loser | relative strength gate would avoid a baseline stop-first path |
| REJECT | `XPLUSDT` | `a4116cc70ea1:XPLUSDT` | 2026-06-19 20:06 | 2026-06-19 23:59 @ 0.100300 | n/a @ n/a | stop_first | no_variant_entry | 0.25 | n/a | -4.39% | 1.71% | -6.09% | filtered_loser | relative strength gate would avoid a baseline stop-first path |
| WATCH_ONLY | `ETHUSDT` | `4b508e31bdd5:ETHUSDT` | 2026-06-20 20:06 | 2026-06-20 23:59 @ 1740.630000 | n/a @ n/a | stop_first | no_variant_entry | 0.42 | n/a | -0.57% | -0.23% | -0.33% | filtered_loser | relative strength gate would avoid a baseline stop-first path |
| WATCH_ONLY | `SOLUSDT` | `4b508e31bdd5:SOLUSDT` | 2026-06-20 20:06 | 2026-06-21 07:59 @ 73.220000 | 2026-06-21 07:59 @ 73.220000 | stop_first | stop_first | 0.28 | 0.28 | 2.94% | -0.23% | 3.18% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `TRXUSDT` | `4b508e31bdd5:TRXUSDT` | 2026-06-20 20:06 | 2026-06-20 23:59 @ 0.324200 | 2026-06-20 23:59 @ 0.324200 | open_unknown | open_unknown | 0.94 | 0.94 | 0.80% | -0.23% | 1.04% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `WLDUSDT` | `4b508e31bdd5:WLDUSDT` | 2026-06-20 20:06 | 2026-06-20 23:59 @ 0.616700 | 2026-06-20 23:59 @ 0.616700 | stop_first | stop_first | 0.75 | 0.75 | 4.36% | -0.23% | 4.60% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `ZECUSDT` | `4b508e31bdd5:ZECUSDT` | 2026-06-20 20:06 | 2026-06-20 23:59 @ 475.650000 | n/a @ n/a | stop_first | no_variant_entry | 0.04 | n/a | -4.61% | -0.23% | -4.38% | filtered_loser | relative strength gate would avoid a baseline stop-first path |
| WATCH_ONLY | `BICOUSDT` | `87d1f0e4c969:BICOUSDT` | 2026-06-21 20:06 | 2026-06-21 23:59 @ 0.053200 | n/a @ n/a | stop_first | no_variant_entry | 0.01 | n/a | -31.77% | 0.88% | -32.65% | filtered_loser | relative strength gate would avoid a baseline stop-first path |
| WATCH_ONLY | `ETHUSDT` | `87d1f0e4c969:ETHUSDT` | 2026-06-21 20:06 | 2026-06-21 23:59 @ 1730.720000 | n/a @ n/a | stop_first | no_variant_entry | 0.59 | n/a | 0.81% | 0.88% | -0.07% | filtered_loser | relative strength gate would avoid a baseline stop-first path |
| WATCH_ONLY | `NEARUSDT` | `87d1f0e4c969:NEARUSDT` | 2026-06-21 20:06 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | -3.77% | 0.88% | -4.65% | no_baseline_entry | price never closed back above entry_high |
| WATCH_ONLY | `SOLUSDT` | `87d1f0e4c969:SOLUSDT` | 2026-06-21 20:06 | 2026-06-21 23:59 @ 74.140000 | n/a @ n/a | stop_first | no_variant_entry | 0.12 | n/a | -1.35% | 0.88% | -2.23% | filtered_loser | relative strength gate would avoid a baseline stop-first path |
| WATCH_ONLY | `TRXUSDT` | `87d1f0e4c969:TRXUSDT` | 2026-06-21 20:06 | 2026-06-21 23:59 @ 0.326800 | 2026-06-21 23:59 @ 0.326800 | open_unknown | open_unknown | 0.56 | 0.56 | 1.01% | 0.88% | 0.13% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `BTCUSDT` | `097536a10619:BTCUSDT` | 2026-06-22 20:06 | 2026-06-22 23:59 @ 64836.950000 | 2026-06-22 23:59 @ 64836.950000 | stop_first | stop_first | 0.01 | 0.01 | -3.62% | -4.25% | 0.62% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `ETHUSDT` | `097536a10619:ETHUSDT` | 2026-06-22 20:06 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | -4.87% | -4.25% | -0.62% | no_baseline_entry | price never closed back above entry_high |
| WATCH_ONLY | `SOLUSDT` | `097536a10619:SOLUSDT` | 2026-06-22 20:06 | 2026-06-29 23:59 @ 73.920000 | n/a @ n/a | near_tp1_first | no_variant_entry | 1.40 | n/a | -5.77% | -4.25% | -1.52% | missed_winner | relative strength gate would skip a baseline near-TP1/TP1 path |
| WATCH_ONLY | `SYNUSDT` | `097536a10619:SYNUSDT` | 2026-06-22 20:06 | 2026-06-23 03:59 @ 0.274000 | 2026-06-23 03:59 @ 0.274000 | tp1_first | tp1_first | 2.12 | 2.12 | 13.45% | -4.25% | 17.69% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `WLDUSDT` | `097536a10619:WLDUSDT` | 2026-06-22 20:06 | 2026-06-22 23:59 @ 0.636600 | n/a @ n/a | stop_first | no_variant_entry | 0.13 | n/a | -12.85% | -4.25% | -8.60% | filtered_loser | relative strength gate would avoid a baseline stop-first path |
| REJECT | `BTCUSDT` | `3b5de7642393:BTCUSDT` | 2026-06-23 20:07 | 2026-06-23 23:59 @ 62487.790000 | n/a @ n/a | stop_first | no_variant_entry | 0.51 | n/a | -3.58% | -3.05% | -0.53% | filtered_loser | relative strength gate would avoid a baseline stop-first path |
| REJECT | `SUIUSDT` | `3b5de7642393:SUIUSDT` | 2026-06-23 20:07 | 2026-06-23 23:59 @ 0.703500 | n/a @ n/a | stop_first | no_variant_entry | 0.19 | n/a | -4.09% | -3.05% | -1.05% | filtered_loser | relative strength gate would avoid a baseline stop-first path |
| WATCH_ONLY | `SYNUSDT` | `3b5de7642393:SYNUSDT` | 2026-06-23 20:07 | 2026-06-23 23:59 @ 0.274200 | 2026-06-23 23:59 @ 0.274200 | near_tp1_first | near_tp1_first | 0.68 | 0.68 | 20.20% | -3.05% | 23.25% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `TRXUSDT` | `3b5de7642393:TRXUSDT` | 2026-06-23 20:07 | 2026-06-24 19:59 @ 0.331500 | 2026-06-24 19:59 @ 0.331500 | stop_first | stop_first | 0.00 | 0.00 | -0.70% | -3.05% | 2.35% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| REJECT | `WLDUSDT` | `3b5de7642393:WLDUSDT` | 2026-06-23 20:07 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | -5.98% | -3.05% | -2.94% | no_baseline_entry | price never closed back above entry_high |
| REJECT | `BNBUSDT` | `170fe0098ac0:BNBUSDT` | 2026-06-24 20:06 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_baseline_entry | n/a | n/a | -1.31% | -2.06% | 0.75% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| REJECT | `BTCUSDT` | `170fe0098ac0:BTCUSDT` | 2026-06-24 20:06 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_baseline_entry | n/a | n/a | -1.15% | -2.06% | 0.91% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| REJECT | `ETHUSDT` | `170fe0098ac0:ETHUSDT` | 2026-06-24 20:06 | 2026-06-25 15:59 @ 1657.190000 | n/a @ n/a | stop_first | no_variant_entry | 0.04 | n/a | -2.97% | -2.06% | -0.91% | filtered_loser | relative strength gate would avoid a baseline stop-first path |
| REJECT | `SOLUSDT` | `170fe0098ac0:SOLUSDT` | 2026-06-24 20:06 | 2026-06-25 15:59 @ 69.450000 | 2026-06-25 15:59 @ 69.450000 | stop_first | stop_first | 0.00 | 0.00 | -1.50% | -2.06% | 0.56% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| REJECT | `XRPUSDT` | `170fe0098ac0:XRPUSDT` | 2026-06-24 20:06 | 2026-07-02 23:59 @ 1.093800 | n/a @ n/a | open_unknown | no_variant_entry | n/a | n/a | -2.21% | -2.06% | -0.15% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| WATCH_ONLY | `AAVEUSDT` | `71e06c148da7:AAVEUSDT` | 2026-06-25 20:08 | 2026-06-25 23:59 @ 82.180000 | 2026-06-25 23:59 @ 82.180000 | near_tp1_first | near_tp1_first | 1.34 | 1.34 | 13.17% | 0.97% | 12.20% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| REJECT | `BTCUSDT` | `71e06c148da7:BTCUSDT` | 2026-06-25 20:08 | 2026-06-26 07:59 @ 59794.000000 | 2026-06-26 07:59 @ 59794.000000 | stop_first | stop_first | 0.73 | 0.73 | 1.29% | 0.97% | 0.32% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `SYNUSDT` | `71e06c148da7:SYNUSDT` | 2026-06-25 20:08 | 2026-06-25 23:59 @ 0.392280 | n/a @ n/a | tp1_first | no_variant_entry | 1.73 | n/a | -15.18% | 0.97% | -16.15% | missed_winner | relative strength gate would skip a baseline near-TP1/TP1 path |
| WATCH_ONLY | `TRXUSDT` | `71e06c148da7:TRXUSDT` | 2026-06-25 20:08 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | -0.96% | 0.97% | -1.93% | no_baseline_entry | price never closed back above entry_high |
| WATCH_ONLY | `XPLUSDT` | `71e06c148da7:XPLUSDT` | 2026-06-25 20:08 | 2026-06-25 23:59 @ 0.094420 | 2026-06-25 23:59 @ 0.094420 | open_unknown | open_unknown | 1.18 | 1.18 | 11.84% | 0.97% | 10.87% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `AAVEUSDT` | `0e7ad0534e93:AAVEUSDT` | 2026-06-26 20:06 | 2026-06-26 23:59 @ 93.000000 | 2026-06-26 23:59 @ 93.000000 | open_unknown | open_unknown | 0.27 | 0.27 | 3.46% | 1.23% | 2.23% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `HEIUSDT` | `0e7ad0534e93:HEIUSDT` | 2026-06-26 20:06 | 2026-06-26 23:59 @ 0.165900 | n/a @ n/a | open_unknown | no_variant_entry | 0.04 | n/a | -2.83% | 1.23% | -4.07% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| WATCH_ONLY | `SOLUSDT` | `0e7ad0534e93:SOLUSDT` | 2026-06-26 20:06 | 2026-06-26 23:59 @ 72.070000 | n/a @ n/a | tp1_first | no_variant_entry | 0.49 | n/a | 1.07% | 1.23% | -0.16% | missed_winner | relative strength gate would skip a baseline near-TP1/TP1 path |
| WATCH_ONLY | `SYNUSDT` | `0e7ad0534e93:SYNUSDT` | 2026-06-26 20:06 | 2026-06-26 23:59 @ 0.332740 | 2026-06-26 23:59 @ 0.332740 | near_tp1_first | near_tp1_first | 2.75 | 2.75 | 1.65% | 1.23% | 0.42% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `XPLUSDT` | `0e7ad0534e93:XPLUSDT` | 2026-06-26 20:06 | 2026-06-26 23:59 @ 0.105600 | n/a @ n/a | open_unknown | no_variant_entry | 0.19 | n/a | -0.61% | 1.23% | -1.84% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| WATCH_ONLY | `AAVEUSDT` | `d505babb3397:AAVEUSDT` | 2026-06-27 20:06 | 2026-06-27 23:59 @ 96.220000 | n/a @ n/a | open_unknown | no_variant_entry | 0.01 | n/a | -7.38% | -1.55% | -5.83% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| REJECT | `BNBUSDT` | `d505babb3397:BNBUSDT` | 2026-06-27 20:06 | 2026-06-27 23:59 @ 565.460000 | n/a @ n/a | open_unknown | no_variant_entry | 0.05 | n/a | -1.93% | -1.55% | -0.38% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| REJECT | `BTCUSDT` | `d505babb3397:BTCUSDT` | 2026-06-27 20:06 | 2026-06-27 23:59 @ 60840.060000 | n/a @ n/a | open_unknown | no_variant_entry | 0.38 | n/a | -1.56% | -1.55% | -0.01% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| WATCH_ONLY | `SOLUSDT` | `d505babb3397:SOLUSDT` | 2026-06-27 20:06 | 2026-06-27 23:59 @ 72.840000 | 2026-06-27 23:59 @ 72.840000 | open_unknown | open_unknown | 1.02 | 1.02 | -1.03% | -1.55% | 0.52% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| REJECT | `XRPUSDT` | `d505babb3397:XRPUSDT` | 2026-06-27 20:06 | 2026-06-27 23:59 @ 1.075200 | n/a @ n/a | open_unknown | no_variant_entry | 0.46 | n/a | -2.10% | -1.55% | -0.55% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| WATCH_ONLY | `BTCUSDT` | `7426dc73980c:BTCUSDT` | 2026-06-28 20:05 | 2026-06-28 23:59 @ 59890.000000 | n/a @ n/a | open_unknown | no_variant_entry | 0.95 | n/a | -0.11% | -0.08% | -0.04% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| REJECT | `ETHUSDT` | `7426dc73980c:ETHUSDT` | 2026-06-28 20:05 | 2026-06-28 23:59 @ 1580.890000 | 2026-06-28 23:59 @ 1580.890000 | near_tp1_first | near_tp1_first | 1.57 | 1.57 | -0.04% | -0.08% | 0.04% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| REJECT | `NEARUSDT` | `7426dc73980c:NEARUSDT` | 2026-06-28 20:05 | 2026-06-28 23:59 @ 1.866000 | n/a @ n/a | stop_first | no_variant_entry | 0.36 | n/a | -1.02% | -0.08% | -0.94% | filtered_loser | relative strength gate would avoid a baseline stop-first path |
| WATCH_ONLY | `SOLUSDT` | `7426dc73980c:SOLUSDT` | 2026-06-28 20:05 | 2026-06-28 23:59 @ 72.090000 | 2026-06-28 23:59 @ 72.090000 | open_unknown | open_unknown | 1.44 | 1.44 | 2.54% | -0.08% | 2.61% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| REJECT | `XRPUSDT` | `7426dc73980c:XRPUSDT` | 2026-06-28 20:05 | 2026-06-28 23:59 @ 1.052600 | n/a @ n/a | open_unknown | no_variant_entry | 1.02 | n/a | -0.30% | -0.08% | -0.23% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| WATCH_ONLY | `ACTUSDT` | `ae9a993942c9:ACTUSDT` | 2026-06-29 20:06 | 2026-06-29 23:59 @ 0.012000 | n/a @ n/a | open_unknown | no_variant_entry | 0.34 | n/a | -13.25% | -1.68% | -11.57% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| WATCH_ONLY | `BTCUSDT` | `ae9a993942c9:BTCUSDT` | 2026-06-29 20:06 | 2026-07-02 11:59 @ 61058.000000 | n/a @ n/a | open_unknown | no_variant_entry | 0.38 | n/a | -2.41% | -1.68% | -0.73% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| REJECT | `ETHUSDT` | `ae9a993942c9:ETHUSDT` | 2026-06-29 20:06 | 2026-06-29 23:59 @ 1580.260000 | 2026-06-29 23:59 @ 1580.260000 | tp1_first | tp1_first | 2.63 | 2.63 | -0.95% | -1.68% | 0.73% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `SOLUSDT` | `ae9a993942c9:SOLUSDT` | 2026-06-29 20:06 | 2026-06-29 23:59 @ 73.920000 | 2026-06-29 23:59 @ 73.920000 | near_tp1_first | near_tp1_first | 0.83 | 0.83 | -1.07% | -1.68% | 0.61% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| REJECT | `XRPUSDT` | `ae9a993942c9:XRPUSDT` | 2026-06-29 20:06 | 2026-06-30 03:59 @ 1.075300 | 2026-06-30 03:59 @ 1.075300 | open_unknown | open_unknown | 0.63 | 0.63 | -1.47% | -1.68% | 0.21% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| REJECT | `ETHUSDT` | `ccf353f12660:ETHUSDT` | 2026-06-30 20:06 | 2026-07-01 03:59 @ 1580.530000 | 2026-07-01 03:59 @ 1580.530000 | near_tp1_first | near_tp1_first | 1.19 | 1.19 | 3.51% | 3.27% | 0.24% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `SOLUSDT` | `ccf353f12660:SOLUSDT` | 2026-06-30 20:06 | 2026-07-01 03:59 @ 73.750000 | 2026-07-01 03:59 @ 73.750000 | tp1_first | tp1_first | 1.79 | 1.79 | 5.88% | 3.27% | 2.61% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `SYNUSDT` | `ccf353f12660:SYNUSDT` | 2026-06-30 20:06 | 2026-06-30 23:59 @ 0.626840 | n/a @ n/a | open_unknown | no_variant_entry | 0.08 | n/a | -25.71% | 3.27% | -28.98% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| REJECT | `XRPUSDT` | `ccf353f12660:XRPUSDT` | 2026-06-30 20:06 | 2026-07-01 03:59 @ 1.044900 | n/a @ n/a | tp1_first | no_variant_entry | 1.47 | n/a | 2.57% | 3.27% | -0.69% | missed_winner | relative strength gate would skip a baseline near-TP1/TP1 path |
| REJECT | `ZECUSDT` | `ccf353f12660:ZECUSDT` | 2026-06-30 20:06 | 2026-06-30 23:59 @ 401.360000 | 2026-06-30 23:59 @ 401.360000 | near_tp1_first | near_tp1_first | 0.60 | 0.60 | 3.42% | 3.27% | 0.16% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `ADAUSDT` | `1bc2608a3ab4:ADAUSDT` | 2026-07-01 20:06 | 2026-07-01 23:59 @ 0.155300 | n/a @ n/a | open_unknown | no_variant_entry | 0.46 | n/a | 3.54% | 3.59% | -0.05% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| WATCH_ONLY | `CELOUSDT` | `1bc2608a3ab4:CELOUSDT` | 2026-07-01 20:06 | 2026-07-01 23:59 @ 0.068410 | n/a @ n/a | open_unknown | no_variant_entry | 0.20 | n/a | -9.82% | 3.59% | -13.42% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| WATCH_ONLY | `SOLUSDT` | `1bc2608a3ab4:SOLUSDT` | 2026-07-01 20:06 | 2026-07-01 23:59 @ 77.430000 | 2026-07-01 23:59 @ 77.430000 | open_unknown | open_unknown | 0.61 | 0.61 | 4.43% | 3.59% | 0.84% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `SYNUSDT` | `1bc2608a3ab4:SYNUSDT` | 2026-07-01 20:06 | 2026-07-02 07:59 @ 0.528530 | 2026-07-02 07:59 @ 0.528530 | open_unknown | open_unknown | 0.47 | 0.47 | 5.52% | 3.59% | 1.92% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `XLMUSDT` | `1bc2608a3ab4:XLMUSDT` | 2026-07-01 20:06 | 2026-07-01 23:59 @ 0.202300 | n/a @ n/a | open_unknown | no_variant_entry | 0.06 | n/a | -1.38% | 3.59% | -4.98% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| WATCH_ONLY | `ADAUSDT` | `ddf9572f5edf:ADAUSDT` | 2026-07-02 20:06 | 2026-07-02 23:59 @ 0.160800 | n/a @ n/a | open_unknown | no_variant_entry | n/a | n/a | n/a | n/a | n/a | data_gap | relative strength data unavailable |
| WATCH_ONLY | `ETHUSDT` | `ddf9572f5edf:ETHUSDT` | 2026-07-02 20:06 | 2026-07-02 23:59 @ 1697.050000 | n/a @ n/a | open_unknown | no_variant_entry | n/a | n/a | n/a | n/a | n/a | data_gap | relative strength data unavailable |
| WATCH_ONLY | `NEARUSDT` | `ddf9572f5edf:NEARUSDT` | 2026-07-02 20:06 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | n/a | n/a | n/a | data_gap | relative strength data unavailable |
| WATCH_ONLY | `SOLUSDT` | `ddf9572f5edf:SOLUSDT` | 2026-07-02 20:06 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | n/a | n/a | n/a | data_gap | relative strength data unavailable |
| WATCH_ONLY | `ZECUSDT` | `ddf9572f5edf:ZECUSDT` | 2026-07-02 20:06 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | n/a | n/a | n/a | data_gap | relative strength data unavailable |

## Raw Summary

```json
{
  "variant": "relative_strength_gate",
  "opportunities": 71,
  "baseline_entries": 61,
  "variant_entries": 27,
  "decisions": {
    "no_baseline_entry": 5,
    "kept_by_relative_strength": 29,
    "filtered_loser": 13,
    "missed_winner": 4,
    "filtered_unknown": 15,
    "data_gap": 5
  },
  "relative_strength_window_bars": 6,
  "relative_strength_min_pct": 0.0
}
```
