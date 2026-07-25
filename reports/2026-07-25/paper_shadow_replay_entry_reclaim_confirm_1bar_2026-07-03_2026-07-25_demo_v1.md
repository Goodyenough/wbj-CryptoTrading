---
created: 2026-07-25 23:39:43 CST
tags:
  - crypto
  - trading-system
  - shadow-replay
account: demo
start_date: 2026-07-03
end_date: 2026-07-25
variant: entry_reclaim_confirm_1bar
report_version: v1
---

# Paper Shadow Replay entry_reclaim_confirm_1bar 2026-07-03 -> 2026-07-25 demo v1

This is an offline diagnostic replay. It does not modify settings, plans, events, or paper state.

## Summary

- opportunities: 95
- baseline_entries: 80
- variant_entries: 63
- filtered_loser: 4
- missed_winner: 4
- improved_path: 0
- worse_path: 0
- delayed_entry: 63
- kept_by_relative_strength: 0
- missed_winner_total_R: 5.68
- filtered_loser_avoided_stop_R: 4
- baseline_mfe_avg_R: 0.62
- variant_mfe_avg_R: 0.54
- baseline_stop_first_rate: 16.84%
- baseline_tp1_or_near_tp1_rate: 22.11%

## Decision Counts

| Decision | Count |
|---|---:|
| delayed_entry | 63 |
| no_baseline_entry | 15 |
| filtered_unknown | 9 |
| missed_winner | 4 |
| filtered_loser | 4 |

## Stratified Counts

### By Source

| Source | Count |
|---|---:|
| WATCH_ONLY | 78 |
| REJECT | 16 |
| RECLAIM_PENDING | 1 |

### By Baseline First Hit

| Baseline First Hit | Count |
|---|---:|
| open_unknown | 43 |
| near_tp1_first | 18 |
| stop_first | 16 |
| no_baseline_entry | 15 |
| tp1_first | 3 |

### Decision By Source

| Decision / Source | Count |
|---|---:|
| delayed_entry / WATCH_ONLY | 54 |
| no_baseline_entry / WATCH_ONLY | 12 |
| delayed_entry / REJECT | 9 |
| filtered_unknown / WATCH_ONLY | 7 |
| filtered_loser / WATCH_ONLY | 3 |
| no_baseline_entry / REJECT | 3 |
| missed_winner / REJECT | 2 |
| missed_winner / WATCH_ONLY | 2 |
| filtered_unknown / RECLAIM_PENDING | 1 |
| filtered_loser / REJECT | 1 |
| filtered_unknown / REJECT | 1 |

## Replay Details

| Source | Symbol | ID | First Time | Entry Low | Entry High | Baseline Entry | Variant Entry | Baseline Hit | Variant Hit | Baseline MFE_R | Variant MFE_R | Symbol Ret | Benchmark Ret | RS | Decision | Explanation |
|---|---|---|---|---:|---:|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| RECLAIM_PENDING | `ONDOUSDT` | `9734a33dea2e` | 2026-07-03 00:10 | 0.394505 | 0.411568 | 2026-07-22 23:59 @ 0.413700 | n/a @ n/a | open_unknown | no_variant_entry | 0.10 | n/a | n/a | n/a | n/a | filtered_unknown | 1-bar confirmation would skip an inconclusive baseline path |
| WATCH_ONLY | `ADAUSDT` | `0b0cbf231493:ADAUSDT` | 2026-07-03 20:06 | 0.165485 | 0.168925 | 2026-07-03 23:59 @ 0.173500 | 2026-07-04 03:59 @ 0.181100 | open_unknown | open_unknown | 0.79 | 0.46 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BTCUSDT` | `0b0cbf231493:BTCUSDT` | 2026-07-03 20:06 | 60973.025211 | 61481.078566 | 2026-07-03 23:59 @ 61922.720000 | 2026-07-04 03:59 @ 62210.000000 | open_unknown | open_unknown | 1.01 | 0.90 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `SOLUSDT` | `0b0cbf231493:SOLUSDT` | 2026-07-03 20:06 | 78.685277 | 79.760221 | 2026-07-03 23:59 @ 81.210000 | 2026-07-04 03:59 @ 82.480000 | open_unknown | open_unknown | 0.28 | 0.13 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `XRPUSDT` | `0b0cbf231493:XRPUSDT` | 2026-07-03 20:06 | 1.106837 | 1.115938 | 2026-07-03 23:59 @ 1.120100 | 2026-07-04 03:59 @ 1.131900 | open_unknown | open_unknown | 0.57 | 0.42 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `NEARUSDT` | `da040ac0b9ea:NEARUSDT` | 2026-07-04 20:06 | 1.954700 | 1.977916 | 2026-07-04 23:59 @ 2.037000 | 2026-07-05 03:59 @ 2.004000 | open_unknown | open_unknown | 0.28 | 0.46 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `PEPEUSDT` | `da040ac0b9ea:PEPEUSDT` | 2026-07-04 20:06 | 0.000003 | 0.000003 | 2026-07-04 23:59 @ 0.000003 | 2026-07-05 03:59 @ 0.000003 | open_unknown | open_unknown | 0.42 | 0.47 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `SOLUSDT` | `da040ac0b9ea:SOLUSDT` | 2026-07-04 20:06 | 80.365773 | 81.268862 | 2026-07-04 23:59 @ 82.230000 | 2026-07-05 03:59 @ 81.880000 | stop_first | stop_first | 0.22 | 0.29 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `TLMUSDT` | `da040ac0b9ea:TLMUSDT` | 2026-07-04 20:06 | 0.002365 | 0.002859 | 2026-07-05 15:59 @ 0.002878 | n/a @ n/a | open_unknown | no_variant_entry | 0.72 | n/a | n/a | n/a | n/a | filtered_unknown | 1-bar confirmation would skip an inconclusive baseline path |
| WATCH_ONLY | `XLMUSDT` | `da040ac0b9ea:XLMUSDT` | 2026-07-04 20:06 | 0.200432 | 0.203342 | 2026-07-04 23:59 @ 0.211600 | 2026-07-05 03:59 @ 0.209900 | stop_first | stop_first | 0.19 | 0.04 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| REJECT | `BTCUSDT` | `9a6e108e270f:BTCUSDT` | 2026-07-08 20:06 | 61429.453680 | 61955.039500 | 2026-07-09 03:59 @ 62277.980000 | 2026-07-09 07:59 @ 62290.000000 | near_tp1_first | near_tp1_first | 0.94 | 0.93 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| REJECT | `ETHUSDT` | `9a6e108e270f:ETHUSDT` | 2026-07-08 20:06 | 1735.612904 | 1752.862860 | 2026-07-09 15:59 @ 1753.310000 | n/a @ n/a | near_tp1_first | no_variant_entry | 1.38 | n/a | n/a | n/a | n/a | missed_winner | 1-bar confirmation would skip a baseline near-TP1/TP1 path |
| REJECT | `SOLUSDT` | `9a6e108e270f:SOLUSDT` | 2026-07-08 20:06 | 77.053800 | 77.772620 | 2026-07-09 07:59 @ 77.830000 | n/a @ n/a | stop_first | no_variant_entry | 0.88 | n/a | n/a | n/a | n/a | filtered_loser | 1-bar confirmation would avoid a baseline stop-first path |
| WATCH_ONLY | `TRXUSDT` | `9a6e108e270f:TRXUSDT` | 2026-07-08 20:06 | 0.327053 | 0.327605 | 2026-07-08 23:59 @ 0.328500 | 2026-07-09 03:59 @ 0.330100 | open_unknown | open_unknown | 0.73 | 0.41 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ZECUSDT` | `9a6e108e270f:ZECUSDT` | 2026-07-08 20:06 | 466.588355 | 467.157280 | 2026-07-09 15:59 @ 467.940000 | 2026-07-09 19:59 @ 467.880000 | near_tp1_first | near_tp1_first | 1.82 | 1.83 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| REJECT | `BNBUSDT` | `b2e95b25d9bb:BNBUSDT` | 2026-07-09 20:06 | 561.520800 | 565.044000 | 2026-07-09 23:59 @ 571.030000 | 2026-07-10 03:59 @ 570.260000 | open_unknown | open_unknown | 0.78 | 0.85 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BTCUSDT` | `b2e95b25d9bb:BTCUSDT` | 2026-07-09 20:06 | 62743.858366 | 62891.831160 | 2026-07-10 03:59 @ 63248.100000 | 2026-07-10 07:59 @ 63230.000000 | near_tp1_first | near_tp1_first | 1.21 | 1.22 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| REJECT | `ETHUSDT` | `b2e95b25d9bb:ETHUSDT` | 2026-07-09 20:06 | 1737.340047 | 1746.162820 | 2026-07-10 03:59 @ 1748.510000 | n/a @ n/a | near_tp1_first | no_variant_entry | 1.34 | n/a | n/a | n/a | n/a | missed_winner | 1-bar confirmation would skip a baseline near-TP1/TP1 path |
| WATCH_ONLY | `TRXUSDT` | `b2e95b25d9bb:TRXUSDT` | 2026-07-09 20:06 | 0.330052 | 0.330664 | 2026-07-09 23:59 @ 0.331500 | 2026-07-10 03:59 @ 0.331900 | stop_first | stop_first | 0.22 | 0.17 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ZECUSDT` | `b2e95b25d9bb:ZECUSDT` | 2026-07-09 20:06 | 465.956421 | 467.839320 | 2026-07-10 03:59 @ 485.410000 | 2026-07-10 07:59 @ 481.540000 | near_tp1_first | near_tp1_first | 0.73 | 0.89 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BNBUSDT` | `26022241fbde:BNBUSDT` | 2026-07-10 20:05 | 574.199839 | 576.857731 | 2026-07-11 15:59 @ 576.920000 | 2026-07-11 19:59 @ 579.390000 | open_unknown | open_unknown | 0.36 | 0.24 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BTCUSDT` | `26022241fbde:BTCUSDT` | 2026-07-10 20:05 | 63413.920678 | 63795.385986 | 2026-07-10 23:59 @ 64040.000000 | 2026-07-11 03:59 @ 63917.880000 | open_unknown | open_unknown | 0.85 | 0.92 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ETHUSDT` | `26022241fbde:ETHUSDT` | 2026-07-10 20:05 | 1767.503029 | 1780.742579 | 2026-07-10 23:59 @ 1791.110000 | 2026-07-11 03:59 @ 1792.680000 | near_tp1_first | near_tp1_first | 1.50 | 1.47 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `SOLUSDT` | `26022241fbde:SOLUSDT` | 2026-07-10 20:05 | 79.076093 | 79.427570 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | n/a | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| WATCH_ONLY | `BNBUSDT` | `ebd75fd57197:BNBUSDT` | 2026-07-11 22:27 | 577.347303 | 579.221913 | 2026-07-11 23:59 @ 579.860000 | 2026-07-12 03:59 @ 580.560000 | open_unknown | open_unknown | 0.23 | 0.19 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BTCUSDT` | `ebd75fd57197:BTCUSDT` | 2026-07-11 22:27 | 63800.109777 | 64048.963749 | 2026-07-11 23:59 @ 64175.750000 | 2026-07-12 03:59 @ 64286.000000 | open_unknown | open_unknown | 0.82 | 0.76 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ETHUSDT` | `ebd75fd57197:ETHUSDT` | 2026-07-11 22:27 | 1783.001941 | 1792.482555 | 2026-07-11 23:59 @ 1814.830000 | 2026-07-12 03:59 @ 1824.380000 | near_tp1_first | near_tp1_first | 1.11 | 0.95 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `SOLUSDT` | `ebd75fd57197:SOLUSDT` | 2026-07-11 22:27 | 77.140004 | 77.656032 | 2026-07-11 23:59 @ 78.380000 | 2026-07-12 03:59 @ 78.150000 | stop_first | stop_first | 0.01 | 0.07 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ZECUSDT` | `ebd75fd57197:ZECUSDT` | 2026-07-11 22:27 | 490.504522 | 498.819971 | 2026-07-11 23:59 @ 504.510000 | 2026-07-12 03:59 @ 515.390000 | near_tp1_first | near_tp1_first | 1.34 | 0.97 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BNBUSDT` | `2b2031877823:BNBUSDT` | 2026-07-12 20:05 | 577.243221 | 579.278039 | 2026-07-12 23:59 @ 581.100000 | 2026-07-13 03:59 @ 579.860000 | stop_first | stop_first | 0.22 | 0.30 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BTCUSDT` | `2b2031877823:BTCUSDT` | 2026-07-12 20:05 | 63948.910025 | 64134.269490 | 2026-07-12 23:59 @ 64176.000000 | 2026-07-13 03:59 @ 64228.590000 | open_unknown | open_unknown | 1.09 | 1.05 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ETHUSDT` | `2b2031877823:ETHUSDT` | 2026-07-12 20:05 | 1794.814581 | 1805.557117 | 2026-07-12 23:59 @ 1820.930000 | 2026-07-13 03:59 @ 1821.400000 | near_tp1_first | near_tp1_first | 1.17 | 1.17 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| REJECT | `SOLUSDT` | `2b2031877823:SOLUSDT` | 2026-07-12 20:05 | 76.982471 | 77.060490 | 2026-07-12 23:59 @ 77.460000 | 2026-07-13 03:59 @ 77.680000 | stop_first | stop_first | 0.25 | 0.16 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ZECUSDT` | `2b2031877823:ZECUSDT` | 2026-07-12 20:05 | 502.982361 | 510.898404 | 2026-07-12 23:59 @ 531.440000 | 2026-07-13 03:59 @ 539.010000 | open_unknown | open_unknown | 0.78 | 0.61 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `DEXEUSDT` | `f58fa1439788:DEXEUSDT` | 2026-07-13 20:07 | 41.694850 | 43.877821 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | n/a | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| REJECT | `ETHUSDT` | `f58fa1439788:ETHUSDT` | 2026-07-13 20:07 | 1777.537980 | 1785.079220 | 2026-07-14 19:59 @ 1798.090000 | 2026-07-14 23:59 @ 1875.220000 | tp1_first | tp1_first | 1.79 | 0.05 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| REJECT | `TRXUSDT` | `f58fa1439788:TRXUSDT` | 2026-07-13 20:07 | 0.327955 | 0.328290 | 2026-07-21 23:59 @ 0.328600 | 2026-07-22 03:59 @ 0.329500 | open_unknown | open_unknown | 0.53 | 0.36 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `WLDUSDT` | `f58fa1439788:WLDUSDT` | 2026-07-13 20:07 | 0.411357 | 0.421996 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | n/a | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| WATCH_ONLY | `ZECUSDT` | `f58fa1439788:ZECUSDT` | 2026-07-13 20:07 | 495.499020 | 504.612500 | 2026-07-13 23:59 @ 509.060000 | n/a @ n/a | near_tp1_first | no_variant_entry | 1.27 | n/a | n/a | n/a | n/a | missed_winner | 1-bar confirmation would skip a baseline near-TP1/TP1 path |
| REJECT | `BNBUSDT` | `3ced75a34c7a:BNBUSDT` | 2026-07-14 20:06 | 563.494740 | 565.890500 | 2026-07-14 23:59 @ 582.870000 | 2026-07-15 03:59 @ 580.640000 | near_tp1_first | near_tp1_first | 0.10 | 0.17 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ETHUSDT` | `3ced75a34c7a:ETHUSDT` | 2026-07-14 20:06 | 1793.035475 | 1803.153280 | 2026-07-14 23:59 @ 1875.220000 | 2026-07-15 03:59 @ 1876.740000 | tp1_first | tp1_first | 0.47 | 0.46 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `NEARUSDT` | `3ced75a34c7a:NEARUSDT` | 2026-07-14 20:06 | 1.956047 | 1.986693 | 2026-07-14 23:59 @ 2.046000 | 2026-07-15 03:59 @ 2.023000 | stop_first | stop_first | 0.29 | 0.44 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `SXTUSDT` | `3ced75a34c7a:SXTUSDT` | 2026-07-14 20:06 | 0.008416 | 0.008801 | 2026-07-14 23:59 @ 0.009230 | 2026-07-15 03:59 @ 0.009510 | stop_first | stop_first | 0.53 | 0.04 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ZECUSDT` | `3ced75a34c7a:ZECUSDT` | 2026-07-14 20:06 | 493.483590 | 501.362092 | 2026-07-14 23:59 @ 539.730000 | 2026-07-15 03:59 @ 539.190000 | tp1_first | tp1_first | 0.30 | 0.55 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BNBUSDT` | `b91b23210b69:BNBUSDT` | 2026-07-15 20:06 | 577.059151 | 579.151336 | 2026-07-15 23:59 @ 581.730000 | 2026-07-16 03:59 @ 579.480000 | open_unknown | open_unknown | 0.15 | 0.25 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BTCUSDT` | `b91b23210b69:BTCUSDT` | 2026-07-15 20:06 | 64066.853866 | 64393.142414 | 2026-07-15 23:59 @ 65427.610000 | 2026-07-16 03:59 @ 64977.340000 | open_unknown | open_unknown | 0.34 | 0.49 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ETHUSDT` | `b91b23210b69:ETHUSDT` | 2026-07-15 20:06 | 1838.156637 | 1853.120662 | 2026-07-15 23:59 @ 1931.950000 | 2026-07-16 03:59 @ 1924.150000 | open_unknown | open_unknown | 0.12 | 0.16 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `NEARUSDT` | `b91b23210b69:NEARUSDT` | 2026-07-15 20:06 | 2.019225 | 2.060196 | 2026-07-15 23:59 @ 2.078000 | n/a @ n/a | stop_first | no_variant_entry | 0.04 | n/a | n/a | n/a | n/a | filtered_loser | 1-bar confirmation would avoid a baseline stop-first path |
| WATCH_ONLY | `BTCUSDT` | `e4779384fba8:BTCUSDT` | 2026-07-16 20:06 | 63812.072192 | 64171.611287 | 2026-07-16 23:59 @ 64704.730000 | 2026-07-17 03:59 @ 64271.840000 | open_unknown | open_unknown | 0.59 | 0.80 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ETHUSDT` | `e4779384fba8:ETHUSDT` | 2026-07-16 20:06 | 1872.102454 | 1887.525640 | 2026-07-20 19:59 @ 1893.200000 | 2026-07-20 23:59 @ 1902.340000 | open_unknown | open_unknown | 0.37 | 0.30 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ONDOUSDT` | `e4779384fba8:ONDOUSDT` | 2026-07-16 20:06 | 0.362117 | 0.370866 | 2026-07-16 23:59 @ 0.384200 | 2026-07-17 03:59 @ 0.375900 | open_unknown | open_unknown | 0.46 | 0.62 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `XRPUSDT` | `e4779384fba8:XRPUSDT` | 2026-07-16 20:06 | 1.108682 | 1.113230 | 2026-07-16 23:59 @ 1.114800 | n/a @ n/a | open_unknown | no_variant_entry | 0.65 | n/a | n/a | n/a | n/a | filtered_unknown | 1-bar confirmation would skip an inconclusive baseline path |
| WATCH_ONLY | `ZECUSDT` | `e4779384fba8:ZECUSDT` | 2026-07-16 20:06 | 547.196990 | 549.272890 | 2026-07-16 23:59 @ 555.830000 | n/a @ n/a | stop_first | no_variant_entry | 0.18 | n/a | n/a | n/a | n/a | filtered_loser | 1-bar confirmation would avoid a baseline stop-first path |
| REJECT | `BTCUSDT` | `b69201a6f091:BTCUSDT` | 2026-07-17 20:06 | 62791.332000 | 63113.201000 | 2026-07-17 23:59 @ 63452.000000 | 2026-07-18 03:59 @ 64160.800000 | near_tp1_first | tp1_first | 0.96 | 0.62 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ETHUSDT` | `b69201a6f091:ETHUSDT` | 2026-07-17 20:06 | 1830.265114 | 1842.791840 | 2026-07-18 03:59 @ 1843.760000 | n/a @ n/a | near_tp1_first | no_variant_entry | 1.69 | n/a | n/a | n/a | n/a | missed_winner | 1-bar confirmation would skip a baseline near-TP1/TP1 path |
| WATCH_ONLY | `ONDOUSDT` | `b69201a6f091:ONDOUSDT` | 2026-07-17 20:06 | 0.364370 | 0.377193 | 2026-07-17 23:59 @ 0.378000 | n/a @ n/a | open_unknown | no_variant_entry | 0.65 | n/a | n/a | n/a | n/a | filtered_unknown | 1-bar confirmation would skip an inconclusive baseline path |
| WATCH_ONLY | `ZECUSDT` | `b69201a6f091:ZECUSDT` | 2026-07-17 20:06 | 524.647200 | 535.163000 | 2026-07-17 23:59 @ 543.780000 | 2026-07-18 03:59 @ 546.180000 | stop_first | stop_first | 0.76 | 0.64 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BTCUSDT` | `ae0bdfd19b79:BTCUSDT` | 2026-07-18 20:05 | 64106.479960 | 64334.405940 | 2026-07-19 03:59 @ 64552.790000 | 2026-07-19 07:59 @ 64834.220000 | open_unknown | open_unknown | 0.81 | 0.66 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| REJECT | `SOLUSDT` | `ae0bdfd19b79:SOLUSDT` | 2026-07-18 20:05 | 73.536780 | 73.969000 | 2026-07-18 23:59 @ 74.970000 | 2026-07-19 03:59 @ 75.440000 | near_tp1_first | near_tp1_first | 1.10 | 0.93 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| REJECT | `XRPUSDT` | `ae0bdfd19b79:XRPUSDT` | 2026-07-18 20:05 | 1.071940 | 1.077720 | 2026-07-18 23:59 @ 1.086400 | 2026-07-19 03:59 @ 1.093500 | near_tp1_first | near_tp1_first | 1.05 | 0.68 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ZECUSDT` | `ae0bdfd19b79:ZECUSDT` | 2026-07-18 20:05 | 544.630295 | 547.367190 | 2026-07-18 23:59 @ 557.230000 | 2026-07-19 03:59 @ 557.080000 | stop_first | stop_first | 0.28 | 0.28 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BANKUSDT` | `3b1acc678d5c:BANKUSDT` | 2026-07-19 20:05 | 0.148902 | 0.170080 | 2026-07-20 03:59 @ 0.230000 | 2026-07-20 07:59 @ 0.225800 | open_unknown | open_unknown | 0.60 | 0.63 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BTCUSDT` | `3b1acc678d5c:BTCUSDT` | 2026-07-19 20:05 | 64387.335401 | 64541.741766 | 2026-07-19 23:59 @ 64585.320000 | n/a @ n/a | open_unknown | no_variant_entry | 0.79 | n/a | n/a | n/a | n/a | filtered_unknown | 1-bar confirmation would skip an inconclusive baseline path |
| WATCH_ONLY | `ETHUSDT` | `3b1acc678d5c:ETHUSDT` | 2026-07-19 20:05 | 1862.544411 | 1869.777257 | 2026-07-19 23:59 @ 1870.910000 | n/a @ n/a | open_unknown | no_variant_entry | 0.90 | n/a | n/a | n/a | n/a | filtered_unknown | 1-bar confirmation would skip an inconclusive baseline path |
| REJECT | `SOLUSDT` | `3b1acc678d5c:SOLUSDT` | 2026-07-19 20:05 | 75.889959 | 76.203982 | 2026-07-19 23:59 @ 76.210000 | n/a @ n/a | open_unknown | no_variant_entry | 0.68 | n/a | n/a | n/a | n/a | filtered_unknown | 1-bar confirmation would skip an inconclusive baseline path |
| WATCH_ONLY | `ZECUSDT` | `3b1acc678d5c:ZECUSDT` | 2026-07-19 20:05 | 551.254662 | 556.715150 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | n/a | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| WATCH_ONLY | `BANKUSDT` | `db791a7e6ebe:BANKUSDT` | 2026-07-20 20:05 | 0.221199 | 0.258696 | 2026-07-20 23:59 @ 0.299600 | 2026-07-21 03:59 @ 0.281100 | open_unknown | open_unknown | 0.17 | 0.26 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BTCUSDT` | `db791a7e6ebe:BTCUSDT` | 2026-07-20 20:05 | 64595.977444 | 64853.902358 | 2026-07-20 23:59 @ 65598.750000 | 2026-07-21 03:59 @ 65142.000000 | open_unknown | open_unknown | 0.39 | 0.61 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ETHUSDT` | `db791a7e6ebe:ETHUSDT` | 2026-07-20 20:05 | 1870.678656 | 1880.912767 | 2026-07-20 23:59 @ 1902.340000 | 2026-07-21 03:59 @ 1898.460000 | open_unknown | open_unknown | 0.52 | 0.58 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `SOLUSDT` | `db791a7e6ebe:SOLUSDT` | 2026-07-20 20:05 | 76.621302 | 77.059865 | 2026-07-20 23:59 @ 77.760000 | 2026-07-21 03:59 @ 77.630000 | open_unknown | open_unknown | 0.26 | 0.29 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `XRPUSDT` | `db791a7e6ebe:XRPUSDT` | 2026-07-20 20:05 | 1.103812 | 1.105908 | 2026-07-20 23:59 @ 1.112600 | 2026-07-21 03:59 @ 1.116700 | open_unknown | open_unknown | 1.09 | 0.92 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BANKUSDT` | `eea62e96754a:BANKUSDT` | 2026-07-21 20:06 | 0.134681 | 0.139116 | 2026-07-21 23:59 @ 0.164800 | 2026-07-22 03:59 @ 0.169400 | near_tp1_first | near_tp1_first | 1.43 | 1.32 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BTCUSDT` | `eea62e96754a:BTCUSDT` | 2026-07-21 20:06 | 65274.532816 | 65638.118827 | 2026-07-21 23:59 @ 66676.540000 | 2026-07-22 03:59 @ 66444.760000 | open_unknown | open_unknown | 0.02 | 0.07 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ETHUSDT` | `eea62e96754a:ETHUSDT` | 2026-07-21 20:06 | 1897.759843 | 1911.557399 | 2026-07-21 23:59 @ 1931.810000 | 2026-07-22 03:59 @ 1923.390000 | open_unknown | open_unknown | 0.21 | 0.30 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `SOLUSDT` | `eea62e96754a:SOLUSDT` | 2026-07-21 20:06 | 77.264361 | 77.804141 | 2026-07-21 23:59 @ 78.140000 | 2026-07-22 03:59 @ 77.870000 | stop_first | stop_first | 0.16 | 0.24 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BANKUSDT` | `f9373c9091c9:BANKUSDT` | 2026-07-22 20:05 | 0.135211 | 0.143867 | 2026-07-22 23:59 @ 0.184600 | 2026-07-23 03:59 @ 0.219200 | near_tp1_first | near_tp1_first | 1.12 | 0.70 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BTCUSDT` | `f9373c9091c9:BTCUSDT` | 2026-07-22 20:05 | 65742.372972 | 66098.141171 | 2026-07-23 07:59 @ 66114.490000 | n/a @ n/a | open_unknown | no_variant_entry | 0.05 | n/a | n/a | n/a | n/a | filtered_unknown | 1-bar confirmation would skip an inconclusive baseline path |
| WATCH_ONLY | `ETHUSDT` | `f9373c9091c9:ETHUSDT` | 2026-07-22 20:05 | 1911.529315 | 1924.464388 | 2026-07-22 23:59 @ 1943.030000 | 2026-07-23 03:59 @ 1925.130000 | open_unknown | open_unknown | 0.11 | 0.15 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `SOLUSDT` | `f9373c9091c9:SOLUSDT` | 2026-07-22 20:05 | 77.488735 | 77.682350 | 2026-07-22 23:59 @ 78.470000 | n/a @ n/a | stop_first | no_variant_entry | 0.08 | n/a | n/a | n/a | n/a | filtered_loser | 1-bar confirmation would avoid a baseline stop-first path |
| WATCH_ONLY | `XRPUSDT` | `f9373c9091c9:XRPUSDT` | 2026-07-22 20:05 | 1.127609 | 1.135428 | 2026-07-22 23:59 @ 1.151300 | 2026-07-23 03:59 @ 1.137300 | open_unknown | open_unknown | 0.07 | 0.11 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BANKUSDT` | `8140da228bbb:BANKUSDT` | 2026-07-23 20:05 | 0.211988 | 0.223752 | 2026-07-23 23:59 @ 0.257000 | 2026-07-24 03:59 @ 0.248700 | open_unknown | open_unknown | 0.56 | 0.65 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BTCUSDT` | `8140da228bbb:BTCUSDT` | 2026-07-23 20:05 | 65189.382573 | 65410.071545 | 2026-07-24 11:59 @ 65456.700000 | 2026-07-24 15:59 @ 65499.950000 | stop_first | stop_first | 0.25 | 0.01 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `ETHUSDT` | `8140da228bbb:ETHUSDT` | 2026-07-23 20:05 | 1920.183962 | 1931.657760 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | n/a | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| WATCH_ONLY | `SOLUSDT` | `8140da228bbb:SOLUSDT` | 2026-07-23 20:05 | 77.669826 | 77.923070 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | n/a | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| WATCH_ONLY | `XRPUSDT` | `8140da228bbb:XRPUSDT` | 2026-07-23 20:05 | 1.132686 | 1.136399 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | n/a | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| WATCH_ONLY | `BANKUSDT` | `77ed2c36cc7b:BANKUSDT` | 2026-07-24 20:05 | 0.239862 | 0.261904 | 2026-07-24 23:59 @ 0.299800 | 2026-07-25 03:59 @ 0.297000 | open_unknown | open_unknown | 0.19 | 0.21 | n/a | n/a | n/a | delayed_entry | baseline and variant both enter; compare first-hit path and R |
| WATCH_ONLY | `BNBUSDT` | `77ed2c36cc7b:BNBUSDT` | 2026-07-24 20:05 | 564.837420 | 566.358000 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | n/a | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| WATCH_ONLY | `BTCUSDT` | `77ed2c36cc7b:BTCUSDT` | 2026-07-24 20:05 | 64779.300000 | 65007.607000 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | n/a | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| WATCH_ONLY | `ETHUSDT` | `77ed2c36cc7b:ETHUSDT` | 2026-07-24 20:05 | 1863.389340 | 1876.512500 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | n/a | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| WATCH_ONLY | `VANAUSDT` | `77ed2c36cc7b:VANAUSDT` | 2026-07-24 20:05 | 1.228600 | 1.255571 | 2026-07-25 15:59 @ 1.264000 | n/a @ n/a | open_unknown | no_variant_entry | 0.51 | n/a | n/a | n/a | n/a | filtered_unknown | 1-bar confirmation would skip an inconclusive baseline path |
| WATCH_ONLY | `BANKUSDT` | `6769789d22f7:BANKUSDT` | 2026-07-25 20:05 | 0.275786 | 0.303064 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | n/a | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| REJECT | `BNBUSDT` | `6769789d22f7:BNBUSDT` | 2026-07-25 20:05 | 557.112000 | 558.703000 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | n/a | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| REJECT | `BTCUSDT` | `6769789d22f7:BTCUSDT` | 2026-07-25 20:05 | 63867.229500 | 64067.950000 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | n/a | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| WATCH_ONLY | `ETHUSDT` | `6769789d22f7:ETHUSDT` | 2026-07-25 20:05 | 1851.786180 | 1861.442500 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | n/a | n/a | n/a | no_baseline_entry | price never closed back above entry_high |
| REJECT | `XRPUSDT` | `6769789d22f7:XRPUSDT` | 2026-07-25 20:05 | 1.087170 | 1.092320 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | n/a | n/a | n/a | no_baseline_entry | price never closed back above entry_high |

## Raw Summary

```json
{
  "variant": "entry_reclaim_confirm_1bar",
  "opportunities": 95,
  "baseline_entries": 80,
  "variant_entries": 63,
  "decisions": {
    "filtered_unknown": 9,
    "delayed_entry": 63,
    "missed_winner": 4,
    "filtered_loser": 4,
    "no_baseline_entry": 15
  },
  "r_summary": {
    "baseline_mfe_total_R": 49.94002606624423,
    "baseline_mfe_avg_R": 0.6242503258280528,
    "baseline_mfe_median_R": 0.5429910671192875,
    "variant_mfe_total_R": 33.878412281267444,
    "variant_mfe_avg_R": 0.5377525758931341,
    "variant_mfe_median_R": 0.46282146443697264,
    "filtered_loser_count": 4,
    "filtered_loser_avoided_stop_R": 4,
    "missed_winner_total_R": 5.679948965795694,
    "missed_winner_avg_R": 1.4199872414489234,
    "tp1_or_near_tp1_rate_pct": 22.105263157894736,
    "stop_first_rate_pct": 16.842105263157894
  },
  "by_source": {
    "RECLAIM_PENDING": 1,
    "WATCH_ONLY": 78,
    "REJECT": 16
  },
  "by_baseline_first_hit": {
    "open_unknown": 43,
    "stop_first": 16,
    "near_tp1_first": 18,
    "no_baseline_entry": 15,
    "tp1_first": 3
  },
  "decision_by_source": {
    "filtered_unknown / RECLAIM_PENDING": 1,
    "delayed_entry / WATCH_ONLY": 54,
    "filtered_unknown / WATCH_ONLY": 7,
    "delayed_entry / REJECT": 9,
    "missed_winner / REJECT": 2,
    "filtered_loser / REJECT": 1,
    "no_baseline_entry / WATCH_ONLY": 12,
    "missed_winner / WATCH_ONLY": 2,
    "filtered_loser / WATCH_ONLY": 3,
    "filtered_unknown / REJECT": 1,
    "no_baseline_entry / REJECT": 3
  },
  "relative_strength_window_bars": null,
  "relative_strength_min_pct": null
}
```
