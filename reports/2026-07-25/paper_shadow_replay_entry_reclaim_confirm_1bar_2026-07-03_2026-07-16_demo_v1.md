---
created: 2026-07-25 23:07:24 CST
tags:
  - crypto
  - trading-system
  - shadow-replay
account: demo
start_date: 2026-07-03
end_date: 2026-07-16
variant: entry_reclaim_confirm_1bar
report_version: v1
---

# Paper Shadow Replay entry_reclaim_confirm_1bar 2026-07-03 -> 2026-07-16 demo v1

This is an offline diagnostic replay. It does not modify settings, plans, events, or paper state.

## Summary

- opportunities: 53
- baseline_entries: 47
- variant_entries: 37
- filtered_loser: 1
- missed_winner: 3
- improved_path: 0
- worse_path: 0
- delayed_entry: 37
- kept_by_relative_strength: 0

## Decision Counts

| Decision | Count |
|---|---:|
| delayed_entry | 37 |
| no_baseline_entry | 6 |
| filtered_unknown | 6 |
| missed_winner | 3 |
| filtered_loser | 1 |

## Replay Details

| Source | Symbol | ID | First Time | Baseline Entry | Variant Entry | Baseline Hit | Variant Hit | Baseline MFE_R | Variant MFE_R | Symbol Ret | Benchmark Ret | RS | Decision | Explanation |
|---|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| RECLAIM_PENDING | `ONDOUSDT` | `9734a33dea2e` | 2026-07-03 00:10 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | n/a | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| WATCH_ONLY | `ADAUSDT` | `0b0cbf231493:ADAUSDT` | 2026-07-03 20:06 | 2026-07-03 23:59 @ 0.173500 | 2026-07-04 03:59 @ 0.181100 | open_unknown | open_unknown | 0.79 | 0.46 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BTCUSDT` | `0b0cbf231493:BTCUSDT` | 2026-07-03 20:06 | 2026-07-03 23:59 @ 61922.720000 | 2026-07-04 03:59 @ 62210.000000 | open_unknown | open_unknown | 0.74 | 0.64 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `SOLUSDT` | `0b0cbf231493:SOLUSDT` | 2026-07-03 20:06 | 2026-07-03 23:59 @ 81.210000 | 2026-07-04 03:59 @ 82.480000 | open_unknown | open_unknown | 0.28 | 0.13 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `XRPUSDT` | `0b0cbf231493:XRPUSDT` | 2026-07-03 20:06 | 2026-07-03 23:59 @ 1.120100 | 2026-07-04 03:59 @ 1.131900 | open_unknown | open_unknown | 0.57 | 0.42 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `NEARUSDT` | `da040ac0b9ea:NEARUSDT` | 2026-07-04 20:06 | 2026-07-04 23:59 @ 2.037000 | 2026-07-05 03:59 @ 2.004000 | open_unknown | open_unknown | 0.28 | 0.46 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `PEPEUSDT` | `da040ac0b9ea:PEPEUSDT` | 2026-07-04 20:06 | 2026-07-04 23:59 @ 0.000003 | 2026-07-05 03:59 @ 0.000003 | open_unknown | open_unknown | 0.36 | 0.41 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `SOLUSDT` | `da040ac0b9ea:SOLUSDT` | 2026-07-04 20:06 | 2026-07-04 23:59 @ 82.230000 | 2026-07-05 03:59 @ 81.880000 | stop_first | stop_first | 0.22 | 0.29 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `TLMUSDT` | `da040ac0b9ea:TLMUSDT` | 2026-07-04 20:06 | 2026-07-05 15:59 @ 0.002878 | n/a @ n/a | open_unknown | no_variant_entry | 0.72 | n/a | n/a | n/a | n/a | filtered_unknown | 1-bar confirmation would skip an inconclusive baseline path |
| WATCH_ONLY | `XLMUSDT` | `da040ac0b9ea:XLMUSDT` | 2026-07-04 20:06 | 2026-07-04 23:59 @ 0.211600 | 2026-07-05 03:59 @ 0.209900 | stop_first | stop_first | 0.19 | 0.04 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| REJECT | `BTCUSDT` | `9a6e108e270f:BTCUSDT` | 2026-07-08 20:06 | 2026-07-09 03:59 @ 62277.980000 | 2026-07-09 07:59 @ 62290.000000 | near_tp1_first | near_tp1_first | 0.94 | 0.93 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| REJECT | `ETHUSDT` | `9a6e108e270f:ETHUSDT` | 2026-07-08 20:06 | 2026-07-09 15:59 @ 1753.310000 | n/a @ n/a | near_tp1_first | no_variant_entry | 1.38 | n/a | n/a | n/a | n/a | missed_winner | 1-bar confirmation would skip a baseline near-TP1/TP1 path |
| REJECT | `SOLUSDT` | `9a6e108e270f:SOLUSDT` | 2026-07-08 20:06 | 2026-07-09 07:59 @ 77.830000 | n/a @ n/a | stop_first | no_variant_entry | 0.88 | n/a | n/a | n/a | n/a | filtered_loser | 1-bar confirmation would avoid a baseline stop-first path |
| WATCH_ONLY | `TRXUSDT` | `9a6e108e270f:TRXUSDT` | 2026-07-08 20:06 | 2026-07-08 23:59 @ 0.328500 | 2026-07-09 03:59 @ 0.330100 | open_unknown | open_unknown | 0.73 | 0.41 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ZECUSDT` | `9a6e108e270f:ZECUSDT` | 2026-07-08 20:06 | 2026-07-09 15:59 @ 467.940000 | 2026-07-09 19:59 @ 467.880000 | near_tp1_first | near_tp1_first | 1.82 | 1.83 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| REJECT | `BNBUSDT` | `b2e95b25d9bb:BNBUSDT` | 2026-07-09 20:06 | 2026-07-09 23:59 @ 571.030000 | 2026-07-10 03:59 @ 570.260000 | open_unknown | open_unknown | 0.78 | 0.85 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BTCUSDT` | `b2e95b25d9bb:BTCUSDT` | 2026-07-09 20:06 | 2026-07-10 03:59 @ 63248.100000 | 2026-07-10 07:59 @ 63230.000000 | open_unknown | open_unknown | 0.90 | 0.91 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| REJECT | `ETHUSDT` | `b2e95b25d9bb:ETHUSDT` | 2026-07-09 20:06 | 2026-07-10 03:59 @ 1748.510000 | n/a @ n/a | near_tp1_first | no_variant_entry | 1.34 | n/a | n/a | n/a | n/a | missed_winner | 1-bar confirmation would skip a baseline near-TP1/TP1 path |
| WATCH_ONLY | `TRXUSDT` | `b2e95b25d9bb:TRXUSDT` | 2026-07-09 20:06 | 2026-07-09 23:59 @ 0.331500 | 2026-07-10 03:59 @ 0.331900 | open_unknown | open_unknown | 0.22 | 0.17 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ZECUSDT` | `b2e95b25d9bb:ZECUSDT` | 2026-07-09 20:06 | 2026-07-10 03:59 @ 485.410000 | 2026-07-10 07:59 @ 481.540000 | near_tp1_first | near_tp1_first | 0.73 | 0.89 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BNBUSDT` | `26022241fbde:BNBUSDT` | 2026-07-10 20:05 | 2026-07-11 15:59 @ 576.920000 | 2026-07-11 19:59 @ 579.390000 | open_unknown | open_unknown | 0.36 | 0.24 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BTCUSDT` | `26022241fbde:BTCUSDT` | 2026-07-10 20:05 | 2026-07-10 23:59 @ 64040.000000 | 2026-07-11 03:59 @ 63917.880000 | open_unknown | open_unknown | 0.46 | 0.51 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ETHUSDT` | `26022241fbde:ETHUSDT` | 2026-07-10 20:05 | 2026-07-10 23:59 @ 1791.110000 | 2026-07-11 03:59 @ 1792.680000 | near_tp1_first | near_tp1_first | 1.50 | 1.47 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `SOLUSDT` | `26022241fbde:SOLUSDT` | 2026-07-10 20:05 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | n/a | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| WATCH_ONLY | `BNBUSDT` | `ebd75fd57197:BNBUSDT` | 2026-07-11 22:27 | 2026-07-11 23:59 @ 579.860000 | 2026-07-12 03:59 @ 580.560000 | open_unknown | open_unknown | 0.23 | 0.19 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BTCUSDT` | `ebd75fd57197:BTCUSDT` | 2026-07-11 22:27 | 2026-07-11 23:59 @ 64175.750000 | 2026-07-12 03:59 @ 64286.000000 | open_unknown | open_unknown | 0.42 | 0.37 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ETHUSDT` | `ebd75fd57197:ETHUSDT` | 2026-07-11 22:27 | 2026-07-11 23:59 @ 1814.830000 | 2026-07-12 03:59 @ 1824.380000 | near_tp1_first | near_tp1_first | 1.11 | 0.95 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `SOLUSDT` | `ebd75fd57197:SOLUSDT` | 2026-07-11 22:27 | 2026-07-11 23:59 @ 78.380000 | 2026-07-12 03:59 @ 78.150000 | stop_first | stop_first | 0.01 | 0.07 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ZECUSDT` | `ebd75fd57197:ZECUSDT` | 2026-07-11 22:27 | 2026-07-11 23:59 @ 504.510000 | 2026-07-12 03:59 @ 515.390000 | near_tp1_first | near_tp1_first | 1.34 | 0.97 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BNBUSDT` | `2b2031877823:BNBUSDT` | 2026-07-12 20:05 | 2026-07-12 23:59 @ 581.100000 | 2026-07-13 03:59 @ 579.860000 | open_unknown | open_unknown | 0.22 | 0.30 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BTCUSDT` | `2b2031877823:BTCUSDT` | 2026-07-12 20:05 | 2026-07-12 23:59 @ 64176.000000 | 2026-07-13 03:59 @ 64228.590000 | open_unknown | open_unknown | 0.56 | 0.53 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ETHUSDT` | `2b2031877823:ETHUSDT` | 2026-07-12 20:05 | 2026-07-12 23:59 @ 1820.930000 | 2026-07-13 03:59 @ 1821.400000 | open_unknown | open_unknown | 1.09 | 1.08 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| REJECT | `SOLUSDT` | `2b2031877823:SOLUSDT` | 2026-07-12 20:05 | 2026-07-12 23:59 @ 77.460000 | 2026-07-13 03:59 @ 77.680000 | stop_first | stop_first | 0.25 | 0.16 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ZECUSDT` | `2b2031877823:ZECUSDT` | 2026-07-12 20:05 | 2026-07-12 23:59 @ 531.440000 | 2026-07-13 03:59 @ 539.010000 | open_unknown | open_unknown | 0.78 | 0.61 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `DEXEUSDT` | `f58fa1439788:DEXEUSDT` | 2026-07-13 20:07 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | n/a | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| REJECT | `ETHUSDT` | `f58fa1439788:ETHUSDT` | 2026-07-13 20:07 | 2026-07-14 19:59 @ 1798.090000 | 2026-07-14 23:59 @ 1875.220000 | tp1_first | tp1_first | 1.79 | 0.05 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| REJECT | `TRXUSDT` | `f58fa1439788:TRXUSDT` | 2026-07-13 20:07 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | n/a | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| WATCH_ONLY | `WLDUSDT` | `f58fa1439788:WLDUSDT` | 2026-07-13 20:07 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | n/a | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| WATCH_ONLY | `ZECUSDT` | `f58fa1439788:ZECUSDT` | 2026-07-13 20:07 | 2026-07-13 23:59 @ 509.060000 | n/a @ n/a | near_tp1_first | no_variant_entry | 1.27 | n/a | n/a | n/a | n/a | missed_winner | 1-bar confirmation would skip a baseline near-TP1/TP1 path |
| REJECT | `BNBUSDT` | `3ced75a34c7a:BNBUSDT` | 2026-07-14 20:06 | 2026-07-14 23:59 @ 582.870000 | 2026-07-15 03:59 @ 580.640000 | near_tp1_first | near_tp1_first | 0.10 | 0.17 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ETHUSDT` | `3ced75a34c7a:ETHUSDT` | 2026-07-14 20:06 | 2026-07-14 23:59 @ 1875.220000 | 2026-07-15 03:59 @ 1876.740000 | tp1_first | tp1_first | 0.47 | 0.46 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `NEARUSDT` | `3ced75a34c7a:NEARUSDT` | 2026-07-14 20:06 | 2026-07-14 23:59 @ 2.046000 | 2026-07-15 03:59 @ 2.023000 | open_unknown | open_unknown | 0.29 | 0.44 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `SXTUSDT` | `3ced75a34c7a:SXTUSDT` | 2026-07-14 20:06 | 2026-07-14 23:59 @ 0.009230 | 2026-07-15 03:59 @ 0.009510 | open_unknown | open_unknown | 0.53 | 0.04 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ZECUSDT` | `3ced75a34c7a:ZECUSDT` | 2026-07-14 20:06 | 2026-07-14 23:59 @ 539.730000 | 2026-07-15 03:59 @ 539.190000 | tp1_first | tp1_first | 0.30 | 0.55 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BNBUSDT` | `b91b23210b69:BNBUSDT` | 2026-07-15 20:06 | 2026-07-15 23:59 @ 581.730000 | 2026-07-16 03:59 @ 579.480000 | open_unknown | open_unknown | 0.15 | 0.25 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BTCUSDT` | `b91b23210b69:BTCUSDT` | 2026-07-15 20:06 | 2026-07-15 23:59 @ 65427.610000 | 2026-07-16 03:59 @ 64977.340000 | open_unknown | open_unknown | 0.01 | 0.02 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ETHUSDT` | `b91b23210b69:ETHUSDT` | 2026-07-15 20:06 | 2026-07-15 23:59 @ 1931.950000 | 2026-07-16 03:59 @ 1924.150000 | open_unknown | open_unknown | 0.02 | 0.03 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `NEARUSDT` | `b91b23210b69:NEARUSDT` | 2026-07-15 20:06 | 2026-07-15 23:59 @ 2.078000 | n/a @ n/a | open_unknown | no_variant_entry | 0.04 | n/a | n/a | n/a | n/a | filtered_unknown | 1-bar confirmation would skip an inconclusive baseline path |
| WATCH_ONLY | `BTCUSDT` | `e4779384fba8:BTCUSDT` | 2026-07-16 20:06 | 2026-07-16 23:59 @ 64704.730000 | n/a @ n/a | open_unknown | no_variant_entry | n/a | n/a | n/a | n/a | n/a | filtered_unknown | 1-bar confirmation would skip an inconclusive baseline path |
| WATCH_ONLY | `ETHUSDT` | `e4779384fba8:ETHUSDT` | 2026-07-16 20:06 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | n/a | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| WATCH_ONLY | `ONDOUSDT` | `e4779384fba8:ONDOUSDT` | 2026-07-16 20:06 | 2026-07-16 23:59 @ 0.384200 | n/a @ n/a | open_unknown | no_variant_entry | n/a | n/a | n/a | n/a | n/a | filtered_unknown | 1-bar confirmation would skip an inconclusive baseline path |
| WATCH_ONLY | `XRPUSDT` | `e4779384fba8:XRPUSDT` | 2026-07-16 20:06 | 2026-07-16 23:59 @ 1.114800 | n/a @ n/a | open_unknown | no_variant_entry | n/a | n/a | n/a | n/a | n/a | filtered_unknown | 1-bar confirmation would skip an inconclusive baseline path |
| WATCH_ONLY | `ZECUSDT` | `e4779384fba8:ZECUSDT` | 2026-07-16 20:06 | 2026-07-16 23:59 @ 555.830000 | n/a @ n/a | open_unknown | no_variant_entry | n/a | n/a | n/a | n/a | n/a | filtered_unknown | 1-bar confirmation would skip an inconclusive baseline path |

## Raw Summary

```json
{
  "variant": "entry_reclaim_confirm_1bar",
  "opportunities": 53,
  "baseline_entries": 47,
  "variant_entries": 37,
  "decisions": {
    "no_baseline_entry": 6,
    "delayed_entry": 37,
    "filtered_unknown": 6,
    "missed_winner": 3,
    "filtered_loser": 1
  },
  "relative_strength_window_bars": null,
  "relative_strength_min_pct": null
}
```
