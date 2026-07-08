---
created: 2026-07-08 17:10:10 CST
tags:
  - crypto
  - trading-system
  - shadow-replay
account: demo
start_date: 2026-06-19
end_date: 2026-07-02
variant: entry_reclaim_confirm_1bar
report_version: v2
---

# Paper Shadow Replay entry_reclaim_confirm_1bar 2026-06-19 -> 2026-07-02 demo v2

This is an offline diagnostic replay. It does not modify settings, plans, events, or paper state.

## Summary

- opportunities: 71
- baseline_entries: 61
- variant_entries: 36
- filtered_loser: 11
- missed_winner: 3
- improved_path: 0
- worse_path: 0
- delayed_entry: 36

## Decision Counts

| Decision | Count |
|---|---:|
| delayed_entry | 36 |
| filtered_loser | 11 |
| filtered_unknown | 11 |
| no_baseline_entry | 10 |
| missed_winner | 3 |

## Replay Details

| Source | Symbol | ID | First Time | Baseline Entry | Variant Entry | Baseline Hit | Variant Hit | Baseline MFE_R | Variant MFE_R | Decision | Explanation |
|---|---|---|---|---|---|---|---|---:|---:|---|---|
| RECLAIM_PENDING | `ONDOUSDT` | `9734a33dea2e` | 2026-06-19 00:10 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| REJECT | `ETHUSDT` | `a4116cc70ea1:ETHUSDT` | 2026-06-19 20:06 | 2026-06-19 23:59 @ 1707.860000 | 2026-06-20 03:59 @ 1701.200000 | stop_first | stop_first | 1.18 | 1.44 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| REJECT | `SOLUSDT` | `a4116cc70ea1:SOLUSDT` | 2026-06-19 20:06 | 2026-06-19 23:59 @ 69.330000 | 2026-06-20 03:59 @ 68.970000 | near_tp1_first | near_tp1_first | 1.94 | 2.26 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `WLDUSDT` | `a4116cc70ea1:WLDUSDT` | 2026-06-19 20:06 | 2026-06-19 23:59 @ 0.617900 | 2026-06-20 03:59 @ 0.615300 | stop_first | stop_first | 0.67 | 0.75 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `XLMUSDT` | `a4116cc70ea1:XLMUSDT` | 2026-06-19 20:06 | 2026-06-19 23:59 @ 0.222500 | 2026-06-20 03:59 @ 0.218500 | stop_first | stop_first | 0.10 | 0.05 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| REJECT | `XPLUSDT` | `a4116cc70ea1:XPLUSDT` | 2026-06-19 20:06 | 2026-06-19 23:59 @ 0.100300 | 2026-06-20 03:59 @ 0.099900 | stop_first | stop_first | 0.25 | 0.11 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ETHUSDT` | `4b508e31bdd5:ETHUSDT` | 2026-06-20 20:06 | 2026-06-20 23:59 @ 1740.630000 | n/a @ n/a | stop_first | no_variant_entry | 0.42 | n/a | filtered_loser | 1-bar confirmation would avoid a baseline stop-first path |
| WATCH_ONLY | `SOLUSDT` | `4b508e31bdd5:SOLUSDT` | 2026-06-20 20:06 | 2026-06-21 07:59 @ 73.220000 | 2026-06-21 11:59 @ 73.630000 | stop_first | stop_first | 0.28 | 0.20 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `TRXUSDT` | `4b508e31bdd5:TRXUSDT` | 2026-06-20 20:06 | 2026-06-20 23:59 @ 0.324200 | 2026-06-21 03:59 @ 0.325600 | open_unknown | open_unknown | 0.94 | 0.71 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `WLDUSDT` | `4b508e31bdd5:WLDUSDT` | 2026-06-20 20:06 | 2026-06-20 23:59 @ 0.616700 | n/a @ n/a | stop_first | no_variant_entry | 0.75 | n/a | filtered_loser | 1-bar confirmation would avoid a baseline stop-first path |
| WATCH_ONLY | `ZECUSDT` | `4b508e31bdd5:ZECUSDT` | 2026-06-20 20:06 | 2026-06-20 23:59 @ 475.650000 | n/a @ n/a | stop_first | no_variant_entry | 0.04 | n/a | filtered_loser | 1-bar confirmation would avoid a baseline stop-first path |
| WATCH_ONLY | `BICOUSDT` | `87d1f0e4c969:BICOUSDT` | 2026-06-21 20:06 | 2026-06-21 23:59 @ 0.053200 | 2026-06-22 03:59 @ 0.047400 | stop_first | stop_first | 0.01 | 0.01 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ETHUSDT` | `87d1f0e4c969:ETHUSDT` | 2026-06-21 20:06 | 2026-06-21 23:59 @ 1730.720000 | 2026-06-22 03:59 @ 1734.140000 | stop_first | stop_first | 0.59 | 0.52 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `NEARUSDT` | `87d1f0e4c969:NEARUSDT` | 2026-06-21 20:06 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| WATCH_ONLY | `SOLUSDT` | `87d1f0e4c969:SOLUSDT` | 2026-06-21 20:06 | 2026-06-21 23:59 @ 74.140000 | 2026-06-22 03:59 @ 74.420000 | stop_first | stop_first | 0.12 | 0.08 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `TRXUSDT` | `87d1f0e4c969:TRXUSDT` | 2026-06-21 20:06 | 2026-06-21 23:59 @ 0.326800 | 2026-06-22 03:59 @ 0.327900 | open_unknown | open_unknown | 0.56 | 0.44 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BTCUSDT` | `097536a10619:BTCUSDT` | 2026-06-22 20:06 | 2026-06-22 23:59 @ 64836.950000 | n/a @ n/a | stop_first | no_variant_entry | 0.01 | n/a | filtered_loser | 1-bar confirmation would avoid a baseline stop-first path |
| WATCH_ONLY | `ETHUSDT` | `097536a10619:ETHUSDT` | 2026-06-22 20:06 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| WATCH_ONLY | `SOLUSDT` | `097536a10619:SOLUSDT` | 2026-06-22 20:06 | 2026-06-29 23:59 @ 73.920000 | 2026-06-30 03:59 @ 75.980000 | near_tp1_first | open_unknown | 1.40 | 0.81 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `SYNUSDT` | `097536a10619:SYNUSDT` | 2026-06-22 20:06 | 2026-06-23 03:59 @ 0.274000 | 2026-06-23 07:59 @ 0.283400 | tp1_first | tp1_first | 2.12 | 1.94 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `WLDUSDT` | `097536a10619:WLDUSDT` | 2026-06-22 20:06 | 2026-06-22 23:59 @ 0.636600 | n/a @ n/a | stop_first | no_variant_entry | 0.13 | n/a | filtered_loser | 1-bar confirmation would avoid a baseline stop-first path |
| REJECT | `BTCUSDT` | `3b5de7642393:BTCUSDT` | 2026-06-23 20:07 | 2026-06-23 23:59 @ 62487.790000 | n/a @ n/a | stop_first | no_variant_entry | 0.51 | n/a | filtered_loser | 1-bar confirmation would avoid a baseline stop-first path |
| REJECT | `SUIUSDT` | `3b5de7642393:SUIUSDT` | 2026-06-23 20:07 | 2026-06-23 23:59 @ 0.703500 | n/a @ n/a | stop_first | no_variant_entry | 0.19 | n/a | filtered_loser | 1-bar confirmation would avoid a baseline stop-first path |
| WATCH_ONLY | `SYNUSDT` | `3b5de7642393:SYNUSDT` | 2026-06-23 20:07 | 2026-06-23 23:59 @ 0.274200 | 2026-06-24 03:59 @ 0.306000 | near_tp1_first | tp1_first | 0.68 | 0.55 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `TRXUSDT` | `3b5de7642393:TRXUSDT` | 2026-06-23 20:07 | 2026-06-24 19:59 @ 0.331500 | n/a @ n/a | stop_first | no_variant_entry | 0.00 | n/a | filtered_loser | 1-bar confirmation would avoid a baseline stop-first path |
| REJECT | `WLDUSDT` | `3b5de7642393:WLDUSDT` | 2026-06-23 20:07 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| REJECT | `BNBUSDT` | `170fe0098ac0:BNBUSDT` | 2026-06-24 20:06 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| REJECT | `BTCUSDT` | `170fe0098ac0:BTCUSDT` | 2026-06-24 20:06 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| REJECT | `ETHUSDT` | `170fe0098ac0:ETHUSDT` | 2026-06-24 20:06 | 2026-06-25 15:59 @ 1657.190000 | n/a @ n/a | stop_first | no_variant_entry | 0.04 | n/a | filtered_loser | 1-bar confirmation would avoid a baseline stop-first path |
| REJECT | `SOLUSDT` | `170fe0098ac0:SOLUSDT` | 2026-06-24 20:06 | 2026-06-25 15:59 @ 69.450000 | n/a @ n/a | stop_first | no_variant_entry | 0.00 | n/a | filtered_loser | 1-bar confirmation would avoid a baseline stop-first path |
| REJECT | `XRPUSDT` | `170fe0098ac0:XRPUSDT` | 2026-06-24 20:06 | 2026-07-02 23:59 @ 1.093800 | n/a @ n/a | open_unknown | no_variant_entry | n/a | n/a | filtered_unknown | 1-bar confirmation would skip an inconclusive baseline path |
| WATCH_ONLY | `AAVEUSDT` | `71e06c148da7:AAVEUSDT` | 2026-06-25 20:08 | 2026-06-25 23:59 @ 82.180000 | n/a @ n/a | near_tp1_first | no_variant_entry | 1.34 | n/a | missed_winner | 1-bar confirmation would skip a baseline near-TP1/TP1 path |
| REJECT | `BTCUSDT` | `71e06c148da7:BTCUSDT` | 2026-06-25 20:08 | 2026-06-26 07:59 @ 59794.000000 | 2026-06-26 11:59 @ 60036.010000 | stop_first | stop_first | 0.73 | 0.50 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `SYNUSDT` | `71e06c148da7:SYNUSDT` | 2026-06-25 20:08 | 2026-06-25 23:59 @ 0.392280 | 2026-06-26 03:59 @ 0.402480 | tp1_first | tp1_first | 1.73 | 1.57 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `TRXUSDT` | `71e06c148da7:TRXUSDT` | 2026-06-25 20:08 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| WATCH_ONLY | `XPLUSDT` | `71e06c148da7:XPLUSDT` | 2026-06-25 20:08 | 2026-06-25 23:59 @ 0.094420 | 2026-06-26 03:59 @ 0.096280 | open_unknown | open_unknown | 1.18 | 0.91 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `AAVEUSDT` | `0e7ad0534e93:AAVEUSDT` | 2026-06-26 20:06 | 2026-06-26 23:59 @ 93.000000 | 2026-06-27 03:59 @ 95.130000 | open_unknown | open_unknown | 0.27 | 0.16 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `HEIUSDT` | `0e7ad0534e93:HEIUSDT` | 2026-06-26 20:06 | 2026-06-26 23:59 @ 0.165900 | n/a @ n/a | open_unknown | no_variant_entry | 0.04 | n/a | filtered_unknown | 1-bar confirmation would skip an inconclusive baseline path |
| WATCH_ONLY | `SOLUSDT` | `0e7ad0534e93:SOLUSDT` | 2026-06-26 20:06 | 2026-06-26 23:59 @ 72.070000 | 2026-06-27 03:59 @ 73.010000 | tp1_first | tp1_first | 0.49 | 0.35 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `SYNUSDT` | `0e7ad0534e93:SYNUSDT` | 2026-06-26 20:06 | 2026-06-26 23:59 @ 0.332740 | 2026-06-27 03:59 @ 0.339220 | near_tp1_first | near_tp1_first | 2.75 | 2.48 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `XPLUSDT` | `0e7ad0534e93:XPLUSDT` | 2026-06-26 20:06 | 2026-06-26 23:59 @ 0.105600 | 2026-06-27 03:59 @ 0.103200 | open_unknown | open_unknown | 0.19 | 0.32 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `AAVEUSDT` | `d505babb3397:AAVEUSDT` | 2026-06-27 20:06 | 2026-06-27 23:59 @ 96.220000 | 2026-06-28 03:59 @ 93.840000 | open_unknown | open_unknown | 0.01 | 0.09 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| REJECT | `BNBUSDT` | `d505babb3397:BNBUSDT` | 2026-06-27 20:06 | 2026-06-27 23:59 @ 565.460000 | n/a @ n/a | open_unknown | no_variant_entry | 0.05 | n/a | filtered_unknown | 1-bar confirmation would skip an inconclusive baseline path |
| REJECT | `BTCUSDT` | `d505babb3397:BTCUSDT` | 2026-06-27 20:06 | 2026-06-27 23:59 @ 60840.060000 | 2026-06-28 03:59 @ 60175.950000 | open_unknown | open_unknown | 0.38 | 0.69 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `SOLUSDT` | `d505babb3397:SOLUSDT` | 2026-06-27 20:06 | 2026-06-27 23:59 @ 72.840000 | n/a @ n/a | open_unknown | no_variant_entry | 1.02 | n/a | filtered_unknown | 1-bar confirmation would skip an inconclusive baseline path |
| REJECT | `XRPUSDT` | `d505babb3397:XRPUSDT` | 2026-06-27 20:06 | 2026-06-27 23:59 @ 1.075200 | 2026-06-28 03:59 @ 1.054400 | open_unknown | open_unknown | 0.46 | 0.96 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BTCUSDT` | `7426dc73980c:BTCUSDT` | 2026-06-28 20:05 | 2026-06-28 23:59 @ 59890.000000 | 2026-06-29 03:59 @ 59481.790000 | open_unknown | open_unknown | 0.95 | 1.35 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| REJECT | `ETHUSDT` | `7426dc73980c:ETHUSDT` | 2026-06-28 20:05 | 2026-06-28 23:59 @ 1580.890000 | n/a @ n/a | near_tp1_first | no_variant_entry | 1.57 | n/a | missed_winner | 1-bar confirmation would skip a baseline near-TP1/TP1 path |
| REJECT | `NEARUSDT` | `7426dc73980c:NEARUSDT` | 2026-06-28 20:05 | 2026-06-28 23:59 @ 1.866000 | n/a @ n/a | stop_first | no_variant_entry | 0.36 | n/a | filtered_loser | 1-bar confirmation would avoid a baseline stop-first path |
| WATCH_ONLY | `SOLUSDT` | `7426dc73980c:SOLUSDT` | 2026-06-28 20:05 | 2026-06-28 23:59 @ 72.090000 | n/a @ n/a | open_unknown | no_variant_entry | 1.44 | n/a | filtered_unknown | 1-bar confirmation would skip an inconclusive baseline path |
| REJECT | `XRPUSDT` | `7426dc73980c:XRPUSDT` | 2026-06-28 20:05 | 2026-06-28 23:59 @ 1.052600 | n/a @ n/a | open_unknown | no_variant_entry | 1.02 | n/a | filtered_unknown | 1-bar confirmation would skip an inconclusive baseline path |
| WATCH_ONLY | `ACTUSDT` | `ae9a993942c9:ACTUSDT` | 2026-06-29 20:06 | 2026-06-29 23:59 @ 0.012000 | 2026-06-30 03:59 @ 0.012680 | open_unknown | open_unknown | 0.34 | 0.16 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BTCUSDT` | `ae9a993942c9:BTCUSDT` | 2026-06-29 20:06 | 2026-07-02 11:59 @ 61058.000000 | n/a @ n/a | open_unknown | no_variant_entry | 0.38 | n/a | filtered_unknown | 1-bar confirmation would skip an inconclusive baseline path |
| REJECT | `ETHUSDT` | `ae9a993942c9:ETHUSDT` | 2026-06-29 20:06 | 2026-06-29 23:59 @ 1580.260000 | 2026-06-30 03:59 @ 1625.600000 | tp1_first | tp1_first | 2.63 | 0.99 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `SOLUSDT` | `ae9a993942c9:SOLUSDT` | 2026-06-29 20:06 | 2026-06-29 23:59 @ 73.920000 | 2026-06-30 03:59 @ 75.980000 | near_tp1_first | near_tp1_first | 0.83 | 0.41 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| REJECT | `XRPUSDT` | `ae9a993942c9:XRPUSDT` | 2026-06-29 20:06 | 2026-06-30 03:59 @ 1.075300 | n/a @ n/a | open_unknown | no_variant_entry | 0.63 | n/a | filtered_unknown | 1-bar confirmation would skip an inconclusive baseline path |
| REJECT | `ETHUSDT` | `ccf353f12660:ETHUSDT` | 2026-06-30 20:06 | 2026-07-01 03:59 @ 1580.530000 | 2026-07-01 07:59 @ 1572.010000 | near_tp1_first | near_tp1_first | 1.19 | 1.58 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `SOLUSDT` | `ccf353f12660:SOLUSDT` | 2026-06-30 20:06 | 2026-07-01 03:59 @ 73.750000 | 2026-07-01 07:59 @ 73.670000 | tp1_first | tp1_first | 1.79 | 1.83 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `SYNUSDT` | `ccf353f12660:SYNUSDT` | 2026-06-30 20:06 | 2026-06-30 23:59 @ 0.626840 | n/a @ n/a | open_unknown | no_variant_entry | 0.08 | n/a | filtered_unknown | 1-bar confirmation would skip an inconclusive baseline path |
| REJECT | `XRPUSDT` | `ccf353f12660:XRPUSDT` | 2026-06-30 20:06 | 2026-07-01 03:59 @ 1.044900 | n/a @ n/a | tp1_first | no_variant_entry | 1.47 | n/a | missed_winner | 1-bar confirmation would skip a baseline near-TP1/TP1 path |
| REJECT | `ZECUSDT` | `ccf353f12660:ZECUSDT` | 2026-06-30 20:06 | 2026-06-30 23:59 @ 401.360000 | 2026-07-01 03:59 @ 399.630000 | near_tp1_first | near_tp1_first | 0.60 | 0.68 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ADAUSDT` | `1bc2608a3ab4:ADAUSDT` | 2026-07-01 20:06 | 2026-07-01 23:59 @ 0.155300 | 2026-07-02 03:59 @ 0.153400 | open_unknown | open_unknown | 0.46 | 0.66 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `CELOUSDT` | `1bc2608a3ab4:CELOUSDT` | 2026-07-01 20:06 | 2026-07-01 23:59 @ 0.068410 | 2026-07-02 03:59 @ 0.069840 | open_unknown | open_unknown | 0.20 | -0.00 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `SOLUSDT` | `1bc2608a3ab4:SOLUSDT` | 2026-07-01 20:06 | 2026-07-01 23:59 @ 77.430000 | 2026-07-02 03:59 @ 77.000000 | open_unknown | open_unknown | 0.61 | 0.70 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `SYNUSDT` | `1bc2608a3ab4:SYNUSDT` | 2026-07-01 20:06 | 2026-07-02 07:59 @ 0.528530 | 2026-07-02 11:59 @ 0.497470 | open_unknown | open_unknown | 0.47 | 0.73 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `XLMUSDT` | `1bc2608a3ab4:XLMUSDT` | 2026-07-01 20:06 | 2026-07-01 23:59 @ 0.202300 | 2026-07-02 03:59 @ 0.203200 | open_unknown | open_unknown | 0.06 | 0.03 | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ADAUSDT` | `ddf9572f5edf:ADAUSDT` | 2026-07-02 20:06 | 2026-07-02 23:59 @ 0.160800 | n/a @ n/a | open_unknown | no_variant_entry | n/a | n/a | filtered_unknown | 1-bar confirmation would skip an inconclusive baseline path |
| WATCH_ONLY | `ETHUSDT` | `ddf9572f5edf:ETHUSDT` | 2026-07-02 20:06 | 2026-07-02 23:59 @ 1697.050000 | n/a @ n/a | open_unknown | no_variant_entry | n/a | n/a | filtered_unknown | 1-bar confirmation would skip an inconclusive baseline path |
| WATCH_ONLY | `NEARUSDT` | `ddf9572f5edf:NEARUSDT` | 2026-07-02 20:06 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| WATCH_ONLY | `SOLUSDT` | `ddf9572f5edf:SOLUSDT` | 2026-07-02 20:06 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| WATCH_ONLY | `ZECUSDT` | `ddf9572f5edf:ZECUSDT` | 2026-07-02 20:06 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | no_baseline_entry | price never closed back above entry_high |

## Raw Summary

```json
{
  "variant": "entry_reclaim_confirm_1bar",
  "opportunities": 71,
  "baseline_entries": 61,
  "variant_entries": 36,
  "decisions": {
    "no_baseline_entry": 10,
    "delayed_entry": 36,
    "filtered_loser": 11,
    "filtered_unknown": 11,
    "missed_winner": 3
  }
}
```
