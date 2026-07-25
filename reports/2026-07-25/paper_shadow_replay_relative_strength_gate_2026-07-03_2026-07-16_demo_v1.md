---
created: 2026-07-25 23:07:48 CST
tags:
  - crypto
  - trading-system
  - shadow-replay
account: demo
start_date: 2026-07-03
end_date: 2026-07-16
variant: relative_strength_gate
report_version: v1
---

# Paper Shadow Replay relative_strength_gate 2026-07-03 -> 2026-07-16 demo v1

This is an offline diagnostic replay. It does not modify settings, plans, events, or paper state.

## Summary

- opportunities: 53
- baseline_entries: 47
- variant_entries: 22
- filtered_loser: 4
- missed_winner: 2
- improved_path: 0
- worse_path: 0
- delayed_entry: 0
- kept_by_relative_strength: 22

## Decision Counts

| Decision | Count |
|---|---:|
| kept_by_relative_strength | 22 |
| filtered_unknown | 15 |
| no_baseline_entry | 5 |
| data_gap | 5 |
| filtered_loser | 4 |
| missed_winner | 2 |

## Replay Details

| Source | Symbol | ID | First Time | Baseline Entry | Variant Entry | Baseline Hit | Variant Hit | Baseline MFE_R | Variant MFE_R | Symbol Ret | Benchmark Ret | RS | Decision | Explanation |
|---|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| RECLAIM_PENDING | `ONDOUSDT` | `9734a33dea2e` | 2026-07-03 00:10 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | 1.21% | 1.92% | -0.72% | no_baseline_entry | price never closed back above entry_high |
| WATCH_ONLY | `ADAUSDT` | `0b0cbf231493:ADAUSDT` | 2026-07-03 20:06 | 2026-07-03 23:59 @ 0.173500 | 2026-07-03 23:59 @ 0.173500 | open_unknown | open_unknown | 0.79 | 0.79 | 10.03% | 2.55% | 7.48% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `BTCUSDT` | `0b0cbf231493:BTCUSDT` | 2026-07-03 20:06 | 2026-07-03 23:59 @ 61922.720000 | n/a @ n/a | open_unknown | no_variant_entry | 0.74 | n/a | 1.65% | 2.55% | -0.90% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| WATCH_ONLY | `SOLUSDT` | `0b0cbf231493:SOLUSDT` | 2026-07-03 20:06 | 2026-07-03 23:59 @ 81.210000 | n/a @ n/a | open_unknown | no_variant_entry | 0.28 | n/a | 1.26% | 2.55% | -1.30% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| WATCH_ONLY | `XRPUSDT` | `0b0cbf231493:XRPUSDT` | 2026-07-03 20:06 | 2026-07-03 23:59 @ 1.120100 | 2026-07-03 23:59 @ 1.120100 | open_unknown | open_unknown | 0.57 | 0.57 | 4.67% | 2.55% | 2.12% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `NEARUSDT` | `da040ac0b9ea:NEARUSDT` | 2026-07-04 20:06 | 2026-07-04 23:59 @ 2.037000 | n/a @ n/a | open_unknown | no_variant_entry | 0.28 | n/a | -2.80% | -0.62% | -2.18% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| WATCH_ONLY | `PEPEUSDT` | `da040ac0b9ea:PEPEUSDT` | 2026-07-04 20:06 | 2026-07-04 23:59 @ 0.000003 | n/a @ n/a | open_unknown | no_variant_entry | 0.36 | n/a | -2.53% | -0.62% | -1.91% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| WATCH_ONLY | `SOLUSDT` | `da040ac0b9ea:SOLUSDT` | 2026-07-04 20:06 | 2026-07-04 23:59 @ 82.230000 | n/a @ n/a | stop_first | no_variant_entry | 0.22 | n/a | -1.06% | -0.62% | -0.44% | filtered_loser | relative strength gate would avoid a baseline stop-first path |
| WATCH_ONLY | `TLMUSDT` | `da040ac0b9ea:TLMUSDT` | 2026-07-04 20:06 | 2026-07-05 15:59 @ 0.002878 | 2026-07-05 15:59 @ 0.002878 | open_unknown | open_unknown | 0.72 | 0.72 | 18.13% | -0.62% | 18.75% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `XLMUSDT` | `da040ac0b9ea:XLMUSDT` | 2026-07-04 20:06 | 2026-07-04 23:59 @ 0.211600 | n/a @ n/a | stop_first | no_variant_entry | 0.19 | n/a | -5.34% | -0.62% | -4.72% | filtered_loser | relative strength gate would avoid a baseline stop-first path |
| REJECT | `BTCUSDT` | `9a6e108e270f:BTCUSDT` | 2026-07-08 20:06 | 2026-07-09 03:59 @ 62277.980000 | 2026-07-09 03:59 @ 62277.980000 | near_tp1_first | near_tp1_first | 0.94 | 0.94 | 1.89% | 1.42% | 0.46% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| REJECT | `ETHUSDT` | `9a6e108e270f:ETHUSDT` | 2026-07-08 20:06 | 2026-07-09 15:59 @ 1753.310000 | n/a @ n/a | near_tp1_first | no_variant_entry | 1.38 | n/a | 0.96% | 1.42% | -0.46% | missed_winner | relative strength gate would skip a baseline near-TP1/TP1 path |
| REJECT | `SOLUSDT` | `9a6e108e270f:SOLUSDT` | 2026-07-08 20:06 | 2026-07-09 07:59 @ 77.830000 | n/a @ n/a | stop_first | no_variant_entry | 0.88 | n/a | 1.15% | 1.42% | -0.28% | filtered_loser | relative strength gate would avoid a baseline stop-first path |
| WATCH_ONLY | `TRXUSDT` | `9a6e108e270f:TRXUSDT` | 2026-07-08 20:06 | 2026-07-08 23:59 @ 0.328500 | n/a @ n/a | open_unknown | no_variant_entry | 0.73 | n/a | 0.91% | 1.42% | -0.51% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| WATCH_ONLY | `ZECUSDT` | `9a6e108e270f:ZECUSDT` | 2026-07-08 20:06 | 2026-07-09 15:59 @ 467.940000 | 2026-07-09 15:59 @ 467.940000 | near_tp1_first | near_tp1_first | 1.82 | 1.82 | 2.63% | 1.42% | 1.20% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| REJECT | `BNBUSDT` | `b2e95b25d9bb:BNBUSDT` | 2026-07-09 20:06 | 2026-07-09 23:59 @ 571.030000 | n/a @ n/a | open_unknown | no_variant_entry | 0.78 | n/a | 0.50% | 2.42% | -1.92% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| WATCH_ONLY | `BTCUSDT` | `b2e95b25d9bb:BTCUSDT` | 2026-07-09 20:06 | 2026-07-10 03:59 @ 63248.100000 | n/a @ n/a | open_unknown | no_variant_entry | 0.90 | n/a | 1.86% | 2.42% | -0.55% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| REJECT | `ETHUSDT` | `b2e95b25d9bb:ETHUSDT` | 2026-07-09 20:06 | 2026-07-10 03:59 @ 1748.510000 | 2026-07-10 03:59 @ 1748.510000 | near_tp1_first | near_tp1_first | 1.34 | 1.34 | 2.97% | 2.42% | 0.55% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `TRXUSDT` | `b2e95b25d9bb:TRXUSDT` | 2026-07-09 20:06 | 2026-07-09 23:59 @ 0.331500 | n/a @ n/a | open_unknown | no_variant_entry | 0.22 | n/a | -0.21% | 2.42% | -2.63% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| WATCH_ONLY | `ZECUSDT` | `b2e95b25d9bb:ZECUSDT` | 2026-07-09 20:06 | 2026-07-10 03:59 @ 485.410000 | 2026-07-10 03:59 @ 485.410000 | near_tp1_first | near_tp1_first | 0.73 | 0.73 | 7.45% | 2.42% | 5.04% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `BNBUSDT` | `26022241fbde:BNBUSDT` | 2026-07-10 20:05 | 2026-07-11 15:59 @ 576.920000 | 2026-07-11 15:59 @ 576.920000 | open_unknown | open_unknown | 0.36 | 0.36 | 1.05% | 0.77% | 0.28% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `BTCUSDT` | `26022241fbde:BTCUSDT` | 2026-07-10 20:05 | 2026-07-10 23:59 @ 64040.000000 | n/a @ n/a | open_unknown | no_variant_entry | 0.46 | n/a | 0.21% | 0.77% | -0.56% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| WATCH_ONLY | `ETHUSDT` | `26022241fbde:ETHUSDT` | 2026-07-10 20:05 | 2026-07-10 23:59 @ 1791.110000 | 2026-07-10 23:59 @ 1791.110000 | near_tp1_first | near_tp1_first | 1.50 | 1.50 | 1.32% | 0.77% | 0.56% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `SOLUSDT` | `26022241fbde:SOLUSDT` | 2026-07-10 20:05 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | 0.31% | 0.77% | -0.46% | no_baseline_entry | price never closed back above entry_high |
| WATCH_ONLY | `BNBUSDT` | `ebd75fd57197:BNBUSDT` | 2026-07-11 22:27 | 2026-07-11 23:59 @ 579.860000 | 2026-07-11 23:59 @ 579.860000 | open_unknown | open_unknown | 0.23 | 0.23 | 0.21% | 0.17% | 0.05% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `BTCUSDT` | `ebd75fd57197:BTCUSDT` | 2026-07-11 22:27 | 2026-07-11 23:59 @ 64175.750000 | n/a @ n/a | open_unknown | no_variant_entry | 0.42 | n/a | 0.00% | 0.17% | -0.17% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| WATCH_ONLY | `ETHUSDT` | `ebd75fd57197:ETHUSDT` | 2026-07-11 22:27 | 2026-07-11 23:59 @ 1814.830000 | 2026-07-11 23:59 @ 1814.830000 | near_tp1_first | near_tp1_first | 1.11 | 1.11 | 0.34% | 0.17% | 0.17% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `SOLUSDT` | `ebd75fd57197:SOLUSDT` | 2026-07-11 22:27 | 2026-07-11 23:59 @ 78.380000 | n/a @ n/a | stop_first | no_variant_entry | 0.01 | n/a | -1.17% | 0.17% | -1.34% | filtered_loser | relative strength gate would avoid a baseline stop-first path |
| WATCH_ONLY | `ZECUSDT` | `ebd75fd57197:ZECUSDT` | 2026-07-11 22:27 | 2026-07-11 23:59 @ 504.510000 | 2026-07-11 23:59 @ 504.510000 | near_tp1_first | near_tp1_first | 1.34 | 1.34 | 5.34% | 0.17% | 5.17% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `BNBUSDT` | `2b2031877823:BNBUSDT` | 2026-07-12 20:05 | 2026-07-12 23:59 @ 581.100000 | 2026-07-12 23:59 @ 581.100000 | open_unknown | open_unknown | 0.22 | 0.22 | -2.13% | -2.42% | 0.29% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `BTCUSDT` | `2b2031877823:BTCUSDT` | 2026-07-12 20:05 | 2026-07-12 23:59 @ 64176.000000 | n/a @ n/a | open_unknown | no_variant_entry | 0.56 | n/a | -2.43% | -2.42% | -0.01% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| WATCH_ONLY | `ETHUSDT` | `2b2031877823:ETHUSDT` | 2026-07-12 20:05 | 2026-07-12 23:59 @ 1820.930000 | 2026-07-12 23:59 @ 1820.930000 | open_unknown | open_unknown | 1.09 | 1.09 | -2.41% | -2.42% | 0.01% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| REJECT | `SOLUSDT` | `2b2031877823:SOLUSDT` | 2026-07-12 20:05 | 2026-07-12 23:59 @ 77.460000 | 2026-07-12 23:59 @ 77.460000 | stop_first | stop_first | 0.25 | 0.25 | -2.13% | -2.42% | 0.29% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `ZECUSDT` | `2b2031877823:ZECUSDT` | 2026-07-12 20:05 | 2026-07-12 23:59 @ 531.440000 | n/a @ n/a | open_unknown | no_variant_entry | 0.78 | n/a | -4.21% | -2.42% | -1.79% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| WATCH_ONLY | `DEXEUSDT` | `f58fa1439788:DEXEUSDT` | 2026-07-13 20:07 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | 1.40% | 4.46% | -3.06% | no_baseline_entry | price never closed back above entry_high |
| REJECT | `ETHUSDT` | `f58fa1439788:ETHUSDT` | 2026-07-13 20:07 | 2026-07-14 19:59 @ 1798.090000 | 2026-07-14 19:59 @ 1798.090000 | tp1_first | tp1_first | 1.79 | 1.79 | 5.53% | 4.46% | 1.07% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| REJECT | `TRXUSDT` | `f58fa1439788:TRXUSDT` | 2026-07-13 20:07 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | -0.12% | 4.46% | -4.58% | no_baseline_entry | price never closed back above entry_high |
| WATCH_ONLY | `WLDUSDT` | `f58fa1439788:WLDUSDT` | 2026-07-13 20:07 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | 1.25% | 4.46% | -3.21% | no_baseline_entry | price never closed back above entry_high |
| WATCH_ONLY | `ZECUSDT` | `f58fa1439788:ZECUSDT` | 2026-07-13 20:07 | 2026-07-13 23:59 @ 509.060000 | 2026-07-13 23:59 @ 509.060000 | near_tp1_first | near_tp1_first | 1.27 | 1.27 | 6.02% | 4.46% | 1.56% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| REJECT | `BNBUSDT` | `3ced75a34c7a:BNBUSDT` | 2026-07-14 20:06 | 2026-07-14 23:59 @ 582.870000 | n/a @ n/a | near_tp1_first | no_variant_entry | 0.10 | n/a | -0.20% | 2.04% | -2.24% | missed_winner | relative strength gate would skip a baseline near-TP1/TP1 path |
| WATCH_ONLY | `ETHUSDT` | `3ced75a34c7a:ETHUSDT` | 2026-07-14 20:06 | 2026-07-14 23:59 @ 1875.220000 | 2026-07-14 23:59 @ 1875.220000 | tp1_first | tp1_first | 0.47 | 0.47 | 3.03% | 2.04% | 0.98% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `NEARUSDT` | `3ced75a34c7a:NEARUSDT` | 2026-07-14 20:06 | 2026-07-14 23:59 @ 2.046000 | n/a @ n/a | open_unknown | no_variant_entry | 0.29 | n/a | 1.56% | 2.04% | -0.48% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| WATCH_ONLY | `SXTUSDT` | `3ced75a34c7a:SXTUSDT` | 2026-07-14 20:06 | 2026-07-14 23:59 @ 0.009230 | n/a @ n/a | open_unknown | no_variant_entry | 0.53 | n/a | -4.98% | 2.04% | -7.02% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| WATCH_ONLY | `ZECUSDT` | `3ced75a34c7a:ZECUSDT` | 2026-07-14 20:06 | 2026-07-14 23:59 @ 539.730000 | 2026-07-14 23:59 @ 539.730000 | tp1_first | tp1_first | 0.30 | 0.30 | 6.71% | 2.04% | 4.66% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `BNBUSDT` | `b91b23210b69:BNBUSDT` | 2026-07-15 20:06 | 2026-07-15 23:59 @ 581.730000 | 2026-07-15 23:59 @ 581.730000 | open_unknown | open_unknown | 0.15 | 0.15 | -0.39% | -1.85% | 1.46% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `BTCUSDT` | `b91b23210b69:BTCUSDT` | 2026-07-15 20:06 | 2026-07-15 23:59 @ 65427.610000 | 2026-07-15 23:59 @ 65427.610000 | open_unknown | open_unknown | 0.01 | 0.01 | -1.10% | -1.85% | 0.74% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `ETHUSDT` | `b91b23210b69:ETHUSDT` | 2026-07-15 20:06 | 2026-07-15 23:59 @ 1931.950000 | n/a @ n/a | open_unknown | no_variant_entry | 0.02 | n/a | -2.59% | -1.85% | -0.74% | filtered_unknown | relative strength gate would skip an inconclusive baseline path |
| WATCH_ONLY | `NEARUSDT` | `b91b23210b69:NEARUSDT` | 2026-07-15 20:06 | 2026-07-15 23:59 @ 2.078000 | 2026-07-15 23:59 @ 2.078000 | open_unknown | open_unknown | 0.04 | 0.04 | -0.48% | -1.85% | 1.37% | kept_by_relative_strength | symbol outperformed BTC/ETH benchmark during the confirmation window |
| WATCH_ONLY | `BTCUSDT` | `e4779384fba8:BTCUSDT` | 2026-07-16 20:06 | 2026-07-16 23:59 @ 64704.730000 | n/a @ n/a | open_unknown | no_variant_entry | n/a | n/a | n/a | n/a | n/a | data_gap | relative strength data unavailable |
| WATCH_ONLY | `ETHUSDT` | `e4779384fba8:ETHUSDT` | 2026-07-16 20:06 | n/a @ n/a | n/a @ n/a | no_baseline_entry | no_variant_entry | n/a | n/a | n/a | n/a | n/a | data_gap | relative strength data unavailable |
| WATCH_ONLY | `ONDOUSDT` | `e4779384fba8:ONDOUSDT` | 2026-07-16 20:06 | 2026-07-16 23:59 @ 0.384200 | n/a @ n/a | open_unknown | no_variant_entry | n/a | n/a | n/a | n/a | n/a | data_gap | relative strength data unavailable |
| WATCH_ONLY | `XRPUSDT` | `e4779384fba8:XRPUSDT` | 2026-07-16 20:06 | 2026-07-16 23:59 @ 1.114800 | n/a @ n/a | open_unknown | no_variant_entry | n/a | n/a | n/a | n/a | n/a | data_gap | relative strength data unavailable |
| WATCH_ONLY | `ZECUSDT` | `e4779384fba8:ZECUSDT` | 2026-07-16 20:06 | 2026-07-16 23:59 @ 555.830000 | n/a @ n/a | open_unknown | no_variant_entry | n/a | n/a | n/a | n/a | n/a | data_gap | relative strength data unavailable |

## Raw Summary

```json
{
  "variant": "relative_strength_gate",
  "opportunities": 53,
  "baseline_entries": 47,
  "variant_entries": 22,
  "decisions": {
    "no_baseline_entry": 5,
    "kept_by_relative_strength": 22,
    "filtered_unknown": 15,
    "filtered_loser": 4,
    "missed_winner": 2,
    "data_gap": 5
  },
  "relative_strength_window_bars": 6,
  "relative_strength_min_pct": 0.0
}
```
