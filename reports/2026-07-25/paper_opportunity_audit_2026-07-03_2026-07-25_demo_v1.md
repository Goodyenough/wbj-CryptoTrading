---
created: 2026-07-25 23:32:00 CST
tags:
  - crypto
  - trading-system
  - paper-audit
account: demo
start_date: 2026-07-03
end_date: 2026-07-25
report_version: v1
---

# Paper Opportunity Audit 2026-07-03 -> 2026-07-25 demo v1

本报告只解释 paper 阶段没有赚钱的来源，不证明策略长期盈利能力。

## Final Readout

- benchmark_context: BTC/ETH formal-window benchmark rose; strategy losses or inactivity need selection/entry/defense review.
- opportunity_verdict: review_entry_quality
- entered_trade_verdict: review_selection_and_entry
- mature_opportunities: 75
- right_censored_opportunities: 22
- defense_net_R: -30.14
- data_link_verdict: partial_pass
- next_action: keep current settings while the next window collects more entered/TP1/reclaim evidence.

## Data Link Health

| Run Type | Expected | Observed | Success | Failed | Running | Success Rate | Latest Started |
|---|---:|---:|---:|---:|---:|---:|---|
| daily_full | 23 | 20 | 20 | 0 | 0 | 86.96% | 2026-07-25 20:05 |
| paper_4h_update | 115 | 102 | 100 | 2 | 0 | 86.96% | 2026-07-25 16:10 |

| Check | Value |
|---|---|
| verdict | partial_pass |
| config_hash_stable | true |
| config_hashes | be7ec39ec21f6a83 |
| stale_running_runs | 0 |
| duplicate_events | 0 |
| impossible_event_order | 0 |
| note | expected paper_4h runs assume five scheduled updates per Beijing day (00:10, 04:10, 08:10, 12:10, 16:10) |

## BTC/ETH Benchmark

| Symbol | Status | Start | End | Return | High Return | Max Drawdown | Trend | Note |
|---|---|---:|---:|---:|---:|---:|---|---|
| `BTCUSDT` | ok | 61479.60 | 64064.01 | 4.20% | 8.45% | -4.01% | up | closed_4h_candles=137 fetched_from_api=138 |
| `ETHUSDT` | ok | 1700.15 | 1857.75 | 9.27% | 14.29% | -5.35% | up | closed_4h_candles=137 fetched_from_api=138 |

## Opportunity Audit Summary

| Classification | Count |
|---|---:|
| avoided_loser | 22 |
| missed_winner | 19 |
| false_entry | 7 |
| neutral_or_unknown | 54 |

### Opportunity Maturity

| Maturity Status | Count |
|---|---:|
| mature | 75 |
| right_censored | 22 |
| open_unknown | 0 |
| data_gap | 5 |

### Opportunity Funnel

| Stage | Count | Conversion | Mature | Right Censored | Dedupe Key | Note |
|---|---:|---:|---:|---:|---|---|
| scanned_candidates | 100 | n/a | 0 | 0 | scan_id+symbol | all scan candidates in the window |
| buy_candidates | 0 | 0.00% | 0 | 0 | scan_id+symbol | candidates allowed to become plans |
| watch_only_candidates | 78 | 78.00% | 0 | 0 | scan_id+symbol | defensive or lower-confidence candidates |
| reject_candidates | 16 | 16.00% | 0 | 0 | scan_id+symbol | rejected scan candidates |
| risk_off_blocked_candidates | 74 | 74.00% | 0 | 0 | scan_id+symbol | WATCH_ONLY/REJECT candidates tied to RISK_OFF evidence |
| reclaim_pending_plans | 1 | n/a | 75 | 22 | plan_id | deduped plans with reclaim pending events |
| reclaim_confirmed_or_entered_events | 0 | 0.00% | 0 | 0 | plan_id | plans with ENTERED or RECLAIM_CONFIRMED_ENTERED events |
| entered_plans | 0 | n/a | 0 | 0 | plan_id | paper plans that actually entered during the window |
| tp1_hit_plans | 0 | n/a | 0 | 0 | plan_id | entered plans that reached TP1 |
| stopped_plans | 0 | n/a | 0 | 0 | plan_id | entered plans currently marked STOPPED |

### Reclaim Reconciliation

| Metric | Value |
|---|---:|
| account_total_RECLAIM_PENDING_events | 208 |
| window_raw_RECLAIM_PENDING_events | 117 |
| deduped_reclaim_plans | 1 |
| excluded_reclaim_duplicate_events | 116 |
| scan_candidate_opportunities | 94 |
| entered_false_entries | 7 |
| final_classified_opportunities | 102 |

- dedupe_key: RECLAIM_PENDING: plan_id; WATCH_ONLY/REJECT: scan_id+symbol+action; false_entry: plan_id
- note: final opportunities combine deduped reclaim plans, scan WATCH_ONLY/REJECT candidates, and stopped entered trades classified as false_entry

### Counterfactual R Summary

| Metric | Value |
|---|---:|
| mature_avoided_loss_R | 22.00 |
| mature_missed_profit_R | 52.14 |
| mature_defense_net_R | -30.14 |

### Symbol Repeats

| Symbol | Opportunity Rows |
|---|---:|
| `BTCUSDT` | 17 |
| `ETHUSDT` | 17 |
| `SOLUSDT` | 12 |
| `ZECUSDT` | 12 |
| `BNBUSDT` | 8 |
| `XRPUSDT` | 7 |
| `BANKUSDT` | 7 |
| `ONDOUSDT` | 5 |
| `NEARUSDT` | 3 |
| `TRXUSDT` | 3 |
| `TONUSDT` | 3 |
| `ADAUSDT` | 1 |
| `PEPEUSDT` | 1 |
| `TLMUSDT` | 1 |
| `XLMUSDT` | 1 |
| `DEXEUSDT` | 1 |
| `WLDUSDT` | 1 |
| `SXTUSDT` | 1 |
| `VANAUSDT` | 1 |

### Opportunity Details

| Source | Symbol | ID | First Time | Entry | Stop | TP1 | Max/Min After | Bars | Maturity | MFE_R | MAE_R | First Hit | Classification | Final | Explanation |
|---|---|---|---|---:|---:|---:|---:|---:|---|---:|---:|---|---|---|---|
| RECLAIM_PENDING | `ONDOUSDT` | `9734a33dea2e` | 2026-07-03 00:10 | 0.411568 | 0.338446 | 0.532217 | 0.414500 / 0.307100 | 119/42 | mature | 0.04 | -1.43 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `ADAUSDT` | `0b0cbf231493:ADAUSDT` | 2026-07-03 20:06 | 0.168925 | 0.139870 | 0.221875 | 0.193100 / 0.157600 | 131/42 | mature | 0.83 | -0.39 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `BTCUSDT` | `0b0cbf231493:BTCUSDT` | 2026-07-03 20:06 | 61481.078566 | 56933.187150 | 69814.781365 | 66676.540000 / 61704.010000 | 131/42 | mature | 1.14 | 0.05 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `SOLUSDT` | `0b0cbf231493:SOLUSDT` | 2026-07-03 20:06 | 79.760221 | 71.166250 | 95.335747 | 82.740000 / 73.790000 | 131/42 | mature | 0.35 | -0.69 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `XRPUSDT` | `0b0cbf231493:XRPUSDT` | 2026-07-03 20:06 | 1.115938 | 1.006670 | 1.320822 | 1.172400 / 1.066200 | 131/42 | mature | 0.52 | -0.46 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `NEARUSDT` | `da040ac0b9ea:NEARUSDT` | 2026-07-04 20:06 | 1.977916 | 1.774970 | 2.348984 | 2.080000 / 1.784000 | 125/42 | mature | 0.50 | -0.96 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `PEPEUSDT` | `da040ac0b9ea:PEPEUSDT` | 2026-07-04 20:06 | 0.000003 | 0.000002 | 0.000003 | 0.000003 / 0.000003 | 125/42 | mature | 0.60 | -0.25 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `SOLUSDT` | `da040ac0b9ea:SOLUSDT` | 2026-07-04 20:06 | 81.268862 | 75.441150 | 91.569652 | 82.110000 / 73.790000 | 125/42 | mature | 0.14 | -1.28 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `TLMUSDT` | `da040ac0b9ea:TLMUSDT` | 2026-07-04 20:06 | 0.002859 | 0.000883 | 0.006072 | 0.003773 / 0.001318 | 125/42 | mature | 0.46 | -0.78 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `XLMUSDT` | `da040ac0b9ea:XLMUSDT` | 2026-07-04 20:06 | 0.203342 | 0.189711 | 0.226240 | 0.209900 / 0.176900 | 125/42 | mature | 0.48 | -1.94 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| REJECT | `BTCUSDT` | `9a6e108e270f:BTCUSDT` | 2026-07-08 20:06 | 61955.039500 | 60387.237400 | 64376.500000 | 66676.540000 / 61974.340000 | 101/42 | mature | 3.01 | 0.01 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| REJECT | `ETHUSDT` | `9a6e108e270f:ETHUSDT` | 2026-07-08 20:06 | 1752.862860 | 1699.302300 | 1834.109046 | 1943.030000 / 1730.700000 | 101/42 | mature | 3.55 | -0.41 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| REJECT | `SOLUSDT` | `9a6e108e270f:SOLUSDT` | 2026-07-08 20:06 | 77.772620 | 75.724353 | 83.560100 | 79.360000 / 73.790000 | 101/42 | mature | 0.77 | -1.94 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `TRXUSDT` | `9a6e108e270f:TRXUSDT` | 2026-07-08 20:06 | 0.327605 | 0.321504 | 0.338979 | 0.332300 / 0.321800 | 101/42 | mature | 0.77 | -0.95 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ZECUSDT` | `9a6e108e270f:ZECUSDT` | 2026-07-08 20:06 | 467.157280 | 431.164050 | 538.290353 | 575.920000 / 457.790000 | 101/42 | mature | 3.02 | -0.26 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| REJECT | `BNBUSDT` | `b2e95b25d9bb:BNBUSDT` | 2026-07-09 20:06 | 565.044000 | 551.994000 | 590.502650 | 582.870000 / 561.410000 | 95/42 | mature | 1.37 | -0.28 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `BTCUSDT` | `b2e95b25d9bb:BTCUSDT` | 2026-07-09 20:06 | 62891.831160 | 60621.391600 | 67210.751088 | 66676.540000 / 62288.230000 | 95/42 | mature | 1.67 | -0.27 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| REJECT | `ETHUSDT` | `b2e95b25d9bb:ETHUSDT` | 2026-07-09 20:06 | 1746.162820 | 1687.738400 | 1849.777500 | 1943.030000 / 1745.160000 | 95/42 | mature | 3.37 | -0.02 | tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `TRXUSDT` | `b2e95b25d9bb:TRXUSDT` | 2026-07-09 20:06 | 0.330664 | 0.322095 | 0.346884 | 0.332300 / 0.321800 | 95/42 | mature | 0.19 | -1.03 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `ZECUSDT` | `b2e95b25d9bb:ZECUSDT` | 2026-07-09 20:06 | 467.839320 | 437.340000 | 526.013612 | 575.920000 / 475.390000 | 95/42 | mature | 3.54 | 0.25 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `BNBUSDT` | `26022241fbde:BNBUSDT` | 2026-07-10 20:05 | 576.857731 | 551.994000 | 622.598355 | 582.870000 / 561.410000 | 89/42 | mature | 0.24 | -0.62 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `BTCUSDT` | `26022241fbde:BTCUSDT` | 2026-07-10 20:05 | 63795.385986 | 60621.391600 | 69571.176796 | 66676.540000 / 62288.230000 | 89/42 | mature | 0.91 | -0.47 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ETHUSDT` | `26022241fbde:ETHUSDT` | 2026-07-10 20:05 | 1780.742579 | 1687.738400 | 1946.891611 | 1943.030000 / 1774.920000 | 89/42 | mature | 1.74 | -0.06 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `SOLUSDT` | `26022241fbde:SOLUSDT` | 2026-07-10 20:05 | 79.427570 | 75.145650 | 87.464194 | 78.560000 / 73.790000 | 89/42 | mature | -0.20 | -1.32 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `BNBUSDT` | `ebd75fd57197:BNBUSDT` | 2026-07-11 22:27 | 579.221913 | 553.215400 | 628.423025 | 582.870000 / 561.410000 | 83/42 | mature | 0.14 | -0.68 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `BTCUSDT` | `ebd75fd57197:BTCUSDT` | 2026-07-11 22:27 | 64048.963749 | 60766.620000 | 70240.370289 | 66676.540000 / 62288.230000 | 83/42 | mature | 0.80 | -0.54 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ETHUSDT` | `ebd75fd57197:ETHUSDT` | 2026-07-11 22:27 | 1792.482555 | 1696.101050 | 1971.024644 | 1943.030000 / 1774.920000 | 83/42 | mature | 1.56 | -0.18 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `SOLUSDT` | `ebd75fd57197:SOLUSDT` | 2026-07-11 22:27 | 77.656032 | 75.559350 | 83.321300 | 78.560000 / 73.790000 | 83/42 | mature | 0.43 | -1.84 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `ZECUSDT` | `ebd75fd57197:ZECUSDT` | 2026-07-11 22:27 | 498.819971 | 447.308200 | 589.370340 | 575.920000 / 475.390000 | 83/42 | mature | 1.50 | -0.45 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `BNBUSDT` | `2b2031877823:BNBUSDT` | 2026-07-12 20:05 | 579.278039 | 559.499700 | 615.782490 | 582.870000 / 561.410000 | 77/42 | mature | 0.18 | -0.90 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `BTCUSDT` | `2b2031877823:BTCUSDT` | 2026-07-12 20:05 | 64134.269490 | 61621.196150 | 68882.376973 | 66676.540000 / 62288.230000 | 77/42 | mature | 1.01 | -0.73 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ETHUSDT` | `2b2031877823:ETHUSDT` | 2026-07-12 20:05 | 1805.557117 | 1706.010150 | 1988.537247 | 1943.030000 / 1774.920000 | 77/42 | mature | 1.38 | -0.31 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| REJECT | `SOLUSDT` | `2b2031877823:SOLUSDT` | 2026-07-12 20:05 | 77.060490 | 74.515250 | 83.321300 | 78.560000 / 73.790000 | 77/42 | mature | 0.59 | -1.28 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `ZECUSDT` | `2b2031877823:ZECUSDT` | 2026-07-12 20:05 | 510.898404 | 457.246850 | 606.327449 | 575.920000 / 475.390000 | 77/42 | mature | 1.21 | -0.66 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `DEXEUSDT` | `f58fa1439788:DEXEUSDT` | 2026-07-13 20:07 | 43.877821 | 33.490000 | 61.379007 | 42.635000 / 1.668000 | 71/42 | mature | -0.12 | -4.06 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| REJECT | `ETHUSDT` | `f58fa1439788:ETHUSDT` | 2026-07-13 20:07 | 1785.079220 | 1747.380150 | 1849.165500 | 1943.030000 / 1774.920000 | 71/42 | mature | 4.19 | -0.27 | tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| REJECT | `TRXUSDT` | `f58fa1439788:TRXUSDT` | 2026-07-13 20:07 | 0.328290 | 0.321405 | 0.341557 | 0.332300 / 0.321800 | 71/42 | mature | 0.58 | -0.94 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `WLDUSDT` | `f58fa1439788:WLDUSDT` | 2026-07-13 20:07 | 0.421996 | 0.373808 | 0.502414 | 0.415300 / 0.342800 | 71/42 | mature | -0.14 | -1.64 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `ZECUSDT` | `f58fa1439788:ZECUSDT` | 2026-07-13 20:07 | 504.612500 | 483.458796 | 547.060950 | 575.920000 / 475.390000 | 71/42 | mature | 3.37 | -1.38 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| REJECT | `BNBUSDT` | `3ced75a34c7a:BNBUSDT` | 2026-07-14 20:06 | 565.890500 | 553.934450 | 586.208960 | 581.870000 / 561.410000 | 65/42 | mature | 1.34 | -0.37 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ETHUSDT` | `3ced75a34c7a:ETHUSDT` | 2026-07-14 20:06 | 1803.153280 | 1723.947000 | 1946.389132 | 1943.030000 / 1828.520000 | 65/42 | mature | 1.77 | 0.32 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `NEARUSDT` | `3ced75a34c7a:NEARUSDT` | 2026-07-14 20:06 | 1.986693 | 1.829145 | 2.255819 | 2.080000 / 1.784000 | 65/42 | mature | 0.59 | -1.29 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `SXTUSDT` | `3ced75a34c7a:SXTUSDT` | 2026-07-14 20:06 | 0.008801 | 0.007289 | 0.011247 | 0.009510 / 0.006620 | 65/42 | mature | 0.47 | -1.44 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `ZECUSDT` | `3ced75a34c7a:ZECUSDT` | 2026-07-14 20:06 | 501.362092 | 482.861377 | 547.060950 | 575.920000 / 475.390000 | 65/42 | mature | 4.03 | -1.40 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `BNBUSDT` | `b91b23210b69:BNBUSDT` | 2026-07-15 20:06 | 579.151336 | 553.934450 | 626.446830 | 581.460000 / 561.410000 | 59/42 | mature | 0.09 | -0.70 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `BTCUSDT` | `b91b23210b69:BTCUSDT` | 2026-07-15 20:06 | 64393.142414 | 60897.595450 | 70894.803520 | 66676.540000 / 62828.110000 | 59/42 | mature | 0.65 | -0.45 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ETHUSDT` | `b91b23210b69:ETHUSDT` | 2026-07-15 20:06 | 1853.120662 | 1723.947000 | 2089.021948 | 1943.030000 / 1828.520000 | 59/42 | mature | 0.70 | -0.19 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `NEARUSDT` | `b91b23210b69:NEARUSDT` | 2026-07-15 20:06 | 2.060196 | 1.829145 | 2.460842 | 2.068000 / 1.784000 | 59/42 | mature | 0.03 | -1.20 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `BTCUSDT` | `e4779384fba8:BTCUSDT` | 2026-07-16 20:06 | 64171.611287 | 60897.595450 | 70180.334318 | 66676.540000 / 62828.110000 | 53/42 | mature | 0.77 | -0.41 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ETHUSDT` | `e4779384fba8:ETHUSDT` | 2026-07-16 20:06 | 1887.525640 | 1723.947000 | 2191.548141 | 1943.030000 / 1828.520000 | 53/42 | mature | 0.34 | -0.36 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ONDOUSDT` | `e4779384fba8:ONDOUSDT` | 2026-07-16 20:06 | 0.370866 | 0.300721 | 0.498034 | 0.413700 / 0.340000 | 53/42 | mature | 0.61 | -0.44 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `XRPUSDT` | `e4779384fba8:XRPUSDT` | 2026-07-16 20:06 | 1.113230 | 1.037698 | 1.257472 | 1.157000 / 1.083100 | 53/42 | mature | 0.58 | -0.40 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ZECUSDT` | `e4779384fba8:ZECUSDT` | 2026-07-16 20:06 | 549.272890 | 483.044000 | 678.616820 | 559.720000 / 475.390000 | 53/42 | mature | 0.16 | -1.12 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| REJECT | `BTCUSDT` | `b69201a6f091:BTCUSDT` | 2026-07-17 20:06 | 63113.201000 | 61726.010000 | 65404.779500 | 66676.540000 / 63931.670000 | 47/42 | mature | 2.57 | 0.59 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `ETHUSDT` | `b69201a6f091:ETHUSDT` | 2026-07-17 20:06 | 1842.791840 | 1793.428900 | 1936.787400 | 1943.030000 / 1841.930000 | 47/42 | mature | 2.03 | -0.02 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `ONDOUSDT` | `b69201a6f091:ONDOUSDT` | 2026-07-17 20:06 | 0.377193 | 0.308699 | 0.494946 | 0.413700 / 0.340000 | 47/42 | mature | 0.53 | -0.54 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ZECUSDT` | `b69201a6f091:ZECUSDT` | 2026-07-17 20:06 | 535.163000 | 510.908743 | 586.234100 | 559.720000 / 475.390000 | 47/42 | mature | 1.01 | -2.46 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `BTCUSDT` | `ae0bdfd19b79:BTCUSDT` | 2026-07-18 20:05 | 64334.405940 | 61599.496600 | 69462.335650 | 66676.540000 / 64003.200000 | 41/42 | right_censored | 0.86 | -0.12 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| REJECT | `SOLUSDT` | `ae0bdfd19b79:SOLUSDT` | 2026-07-18 20:05 | 73.969000 | 72.289150 | 78.644800 | 78.560000 / 73.790000 | 41/42 | mature | 2.73 | -0.11 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| REJECT | `XRPUSDT` | `ae0bdfd19b79:XRPUSDT` | 2026-07-18 20:05 | 1.077720 | 1.053753 | 1.124549 | 1.157000 / 1.088000 | 41/42 | mature | 3.31 | 0.43 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `ZECUSDT` | `ae0bdfd19b79:ZECUSDT` | 2026-07-18 20:05 | 547.367190 | 515.746000 | 606.504228 | 559.720000 / 475.390000 | 41/42 | mature | 0.39 | -2.28 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `BANKUSDT` | `3b1acc678d5c:BANKUSDT` | 2026-07-19 20:05 | 0.170080 | 0.046394 | 0.385687 | 0.324000 / 0.137300 | 35/42 | right_censored | 1.24 | -0.27 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `BTCUSDT` | `3b1acc678d5c:BTCUSDT` | 2026-07-19 20:05 | 64541.741766 | 61599.496600 | 70194.622550 | 66676.540000 / 64003.200000 | 35/42 | right_censored | 0.73 | -0.18 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ETHUSDT` | `3b1acc678d5c:ETHUSDT` | 2026-07-19 20:05 | 1869.777257 | 1776.004250 | 2046.474002 | 1943.030000 / 1856.020000 | 35/42 | right_censored | 0.78 | -0.15 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| REJECT | `SOLUSDT` | `3b1acc678d5c:SOLUSDT` | 2026-07-19 20:05 | 76.203982 | 72.289150 | 83.562612 | 78.560000 / 73.790000 | 35/42 | right_censored | 0.60 | -0.62 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ZECUSDT` | `3b1acc678d5c:ZECUSDT` | 2026-07-19 20:05 | 556.715150 | 515.746000 | 630.462718 | 550.680000 / 475.390000 | 35/42 | mature | -0.15 | -1.99 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `BANKUSDT` | `db791a7e6ebe:BANKUSDT` | 2026-07-20 20:05 | 0.258696 | 0.060676 | 0.598490 | 0.324000 / 0.137300 | 29/42 | right_censored | 0.33 | -0.61 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `BTCUSDT` | `db791a7e6ebe:BTCUSDT` | 2026-07-20 20:05 | 64853.902358 | 62153.500000 | 69867.819703 | 66676.540000 / 64003.200000 | 29/42 | right_censored | 0.67 | -0.32 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ETHUSDT` | `db791a7e6ebe:ETHUSDT` | 2026-07-20 20:05 | 1880.912767 | 1797.940200 | 2031.506734 | 1943.030000 / 1856.020000 | 29/42 | right_censored | 0.75 | -0.30 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `SOLUSDT` | `db791a7e6ebe:SOLUSDT` | 2026-07-20 20:05 | 77.059865 | 73.382500 | 83.756750 | 78.560000 / 73.790000 | 29/42 | right_censored | 0.41 | -0.89 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `XRPUSDT` | `db791a7e6ebe:XRPUSDT` | 2026-07-20 20:05 | 1.105908 | 1.064883 | 1.184812 | 1.157000 / 1.088000 | 29/42 | right_censored | 1.25 | -0.44 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `BANKUSDT` | `eea62e96754a:BANKUSDT` | 2026-07-21 20:06 | 0.139116 | 0.066658 | 0.337604 | 0.324000 / 0.140700 | 23/42 | mature | 2.55 | 0.02 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `BTCUSDT` | `eea62e96754a:BTCUSDT` | 2026-07-21 20:06 | 65638.118827 | 62153.500000 | 72061.977464 | 66556.160000 / 64003.200000 | 23/42 | right_censored | 0.26 | -0.47 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ETHUSDT` | `eea62e96754a:ETHUSDT` | 2026-07-21 20:06 | 1911.557399 | 1813.887350 | 2086.201163 | 1943.030000 / 1856.020000 | 23/42 | right_censored | 0.32 | -0.57 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `SOLUSDT` | `eea62e96754a:SOLUSDT` | 2026-07-21 20:06 | 77.804141 | 73.717400 | 85.167953 | 78.470000 / 73.790000 | 23/42 | right_censored | 0.16 | -0.98 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `BANKUSDT` | `f9373c9091c9:BANKUSDT` | 2026-07-22 20:05 | 0.143867 | 0.075155 | 0.337604 | 0.324000 / 0.219200 | 17/42 | mature | 2.62 | 1.10 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `BTCUSDT` | `f9373c9091c9:BTCUSDT` | 2026-07-22 20:05 | 66098.141171 | 62153.500000 | 73453.771215 | 66114.490000 / 64003.200000 | 17/42 | right_censored | 0.00 | -0.53 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ETHUSDT` | `f9373c9091c9:ETHUSDT` | 2026-07-22 20:05 | 1924.464388 | 1815.492900 | 2123.004755 | 1934.250000 / 1856.020000 | 17/42 | right_censored | 0.09 | -0.63 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `SOLUSDT` | `f9373c9091c9:SOLUSDT` | 2026-07-22 20:05 | 77.682350 | 74.239450 | 84.277727 | 77.970000 / 73.790000 | 17/42 | mature | 0.08 | -1.13 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `XRPUSDT` | `f9373c9091c9:XRPUSDT` | 2026-07-22 20:05 | 1.135428 | 1.066853 | 1.260849 | 1.142100 / 1.088000 | 17/42 | right_censored | 0.10 | -0.69 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `BANKUSDT` | `8140da228bbb:BANKUSDT` | 2026-07-23 20:05 | 0.223752 | 0.116722 | 0.420165 | 0.324000 / 0.248700 | 11/42 | right_censored | 0.94 | 0.23 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `BTCUSDT` | `8140da228bbb:BTCUSDT` | 2026-07-23 20:05 | 65410.071545 | 64065.434250 | 67768.312677 | 65499.950000 / 64003.200000 | 11/42 | mature | 0.07 | -1.05 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `ETHUSDT` | `8140da228bbb:ETHUSDT` | 2026-07-23 20:05 | 1931.657760 | 1861.718950 | 2054.324682 | 1895.980000 / 1856.020000 | 11/42 | mature | -0.51 | -1.08 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `SOLUSDT` | `8140da228bbb:SOLUSDT` | 2026-07-23 20:05 | 77.923070 | 75.845000 | 81.699343 | 76.070000 / 73.790000 | 11/42 | mature | -0.89 | -1.99 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `XRPUSDT` | `8140da228bbb:XRPUSDT` | 2026-07-23 20:05 | 1.136399 | 1.091676 | 1.220277 | 1.113900 / 1.088000 | 11/42 | mature | -0.50 | -1.08 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `BANKUSDT` | `77ed2c36cc7b:BANKUSDT` | 2026-07-24 20:05 | 0.261904 | 0.116722 | 0.519203 | 0.324000 / 0.297000 | 5/42 | right_censored | 0.43 | 0.24 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `BNBUSDT` | `77ed2c36cc7b:BNBUSDT` | 2026-07-24 20:05 | 566.358000 | 555.254350 | 586.284430 | 565.740000 / 564.810000 | 5/42 | right_censored | -0.06 | -0.14 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `BTCUSDT` | `77ed2c36cc7b:BTCUSDT` | 2026-07-24 20:05 | 65007.607000 | 63680.250000 | 67319.860500 | 64225.320000 / 64003.200000 | 5/42 | right_censored | -0.59 | -0.76 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ETHUSDT` | `77ed2c36cc7b:ETHUSDT` | 2026-07-24 20:05 | 1876.512500 | 1831.774950 | 1946.667750 | 1863.830000 / 1856.020000 | 5/42 | right_censored | -0.28 | -0.46 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `VANAUSDT` | `77ed2c36cc7b:VANAUSDT` | 2026-07-24 20:05 | 1.255571 | 1.129795 | 1.466667 | 1.264000 / 1.148000 | 5/42 | right_censored | 0.07 | -0.86 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `BANKUSDT` | `6769789d22f7:BANKUSDT` | 2026-07-25 20:05 | 0.303064 | 0.181437 | 0.505401 | n/a / n/a | 0/42 | data_gap | n/a | n/a | none | neutral_or_unknown | false | insufficient post-block price path |
| REJECT | `BNBUSDT` | `6769789d22f7:BNBUSDT` | 2026-07-25 20:05 | 558.703000 | 547.660000 | 578.402500 | n/a / n/a | 0/42 | data_gap | n/a | n/a | none | neutral_or_unknown | false | insufficient post-block price path |
| REJECT | `BTCUSDT` | `6769789d22f7:BTCUSDT` | 2026-07-25 20:05 | 64067.950000 | 62783.653750 | 66621.369250 | n/a / n/a | 0/42 | data_gap | n/a | n/a | none | neutral_or_unknown | false | insufficient post-block price path |
| WATCH_ONLY | `ETHUSDT` | `6769789d22f7:ETHUSDT` | 2026-07-25 20:05 | 1861.442500 | 1820.368650 | 1946.667750 | n/a / n/a | 0/42 | data_gap | n/a | n/a | none | neutral_or_unknown | false | insufficient post-block price path |
| REJECT | `XRPUSDT` | `6769789d22f7:XRPUSDT` | 2026-07-25 20:05 | 1.092320 | 1.068725 | 1.158777 | n/a / n/a | 0/42 | data_gap | n/a | n/a | none | neutral_or_unknown | false | insufficient post-block price path |
| ENTERED_TRADE | `ZECUSDT` | `1b124f8886a4` | 2026-05-19 22:53 | 553.890000 | 489.022950 | 668.523622 | 553.890000 / 489.022950 | 0/42 | mature | 0.00 | -1.00 | stop_first | false_entry | true | entry failed before producing meaningful favorable excursion |
| ENTERED_TRADE | `TONUSDT` | `da78b42d2554` | 2026-05-19 23:14 | 1.971000 | 1.831115 | 2.266911 | 1.971000 / 1.831115 | 0/42 | mature | 0.00 | -1.00 | stop_first | false_entry | true | entry failed before producing meaningful favorable excursion |
| ENTERED_TRADE | `ONDOUSDT` | `2ed171ff8ada` | 2026-05-19 23:14 | 0.361900 | 0.328202 | 0.419142 | 0.384000 / 0.324400 | 0/42 | mature | 0.66 | -1.11 | stop_first | false_entry | true | trade reached full risk without strong upside follow-through |
| ENTERED_TRADE | `TONUSDT` | `195cc3f0d481` | 2026-05-19 23:14 | 1.971000 | 1.831115 | 2.256882 | 1.971000 / 1.831115 | 0/42 | mature | 0.00 | -1.00 | stop_first | false_entry | true | entry failed before producing meaningful favorable excursion |
| ENTERED_TRADE | `ONDOUSDT` | `5d1c3b7ddf56` | 2026-05-19 23:25 | 0.361100 | 0.328202 | 0.418468 | 0.384000 / 0.324400 | 0/42 | mature | 0.70 | -1.12 | stop_first | false_entry | true | trade reached full risk without strong upside follow-through |
| ENTERED_TRADE | `TONUSDT` | `136c277b7ecb` | 2026-05-19 23:37 | 1.977000 | 1.831115 | 2.266768 | 1.977000 / 1.831115 | 0/42 | mature | 0.00 | -1.00 | stop_first | false_entry | true | entry failed before producing meaningful favorable excursion |
| ENTERED_TRADE | `ZECUSDT` | `bf97525097f3` | 2026-06-03 20:11 | 597.810000 | 518.760100 | 730.619727 | 597.810000 / 518.760100 | 0/42 | mature | 0.00 | -1.00 | stop_first | false_entry | true | entry failed before producing meaningful favorable excursion |

## Entered Trades Review

| Attribution | Count |
|---|---:|
| entry_issue | 5 |
| selection_issue | 2 |
| exit_issue | 0 |
| market_issue | 0 |
| risk_rule_issue | 0 |
| open_unknown | 1 |

| Symbol | Plan | Status | Entered | Regime | Entry | Stop | TP1 | MFE_R | MAE_R | Near TP1 | TP1 Hit | PnL | Attribution | Explanation |
|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|---:|---|---|
| `ZECUSDT` | `1b124f8886a4` | STOPPED | 2026-05-19 22:53 | n/a | 553.890000 | 489.022950 | 668.523622 | 0.00 | -1.00 | false | false | -100.00 | entry_issue | entry failed before producing meaningful favorable excursion |
| `TONUSDT` | `da78b42d2554` | STOPPED | 2026-05-19 23:14 | n/a | 1.971000 | 1.831115 | 2.266911 | 0.00 | -1.00 | false | false | -100.00 | entry_issue | entry failed before producing meaningful favorable excursion |
| `ONDOUSDT` | `2ed171ff8ada` | STOPPED | 2026-05-19 23:14 | n/a | 0.361900 | 0.328202 | 0.419142 | 0.66 | -1.11 | false | false | -100.00 | selection_issue | trade reached full risk without strong upside follow-through |
| `TONUSDT` | `195cc3f0d481` | STOPPED | 2026-05-19 23:14 | n/a | 1.971000 | 1.831115 | 2.256882 | 0.00 | -1.00 | false | false | -100.00 | entry_issue | entry failed before producing meaningful favorable excursion |
| `ONDOUSDT` | `5d1c3b7ddf56` | STOPPED | 2026-05-19 23:25 | n/a | 0.361100 | 0.328202 | 0.418468 | 0.70 | -1.12 | false | false | -100.00 | selection_issue | trade reached full risk without strong upside follow-through |
| `TONUSDT` | `136c277b7ecb` | STOPPED | 2026-05-19 23:37 | n/a | 1.977000 | 1.831115 | 2.266768 | 0.00 | -1.00 | false | false | -100.00 | entry_issue | entry failed before producing meaningful favorable excursion |
| `ZECUSDT` | `bf97525097f3` | STOPPED | 2026-06-03 20:11 | n/a | 597.810000 | 518.760100 | 730.619727 | 0.00 | -1.00 | false | false | -100.00 | entry_issue | entry failed before producing meaningful favorable excursion |
| `WLDUSDT` | `616e1bbfd4c6` | ENTERED | 2026-06-11 11:36 | n/a | 0.458300 | 0.316875 | 0.713862 | 1.38 | -0.82 | false | false | -81.53 | open_unknown | trade is still open or not terminal |

## Raw Classification Counts

```json
{
  "opportunities": {
    "avoided_loser": 22,
    "neutral_or_unknown": 54,
    "missed_winner": 19,
    "false_entry": 7
  },
  "opportunity_maturity": {
    "mature": 75,
    "right_censored": 22,
    "data_gap": 5
  },
  "opportunity_r": {
    "avoided_loss_R": 22.0,
    "missed_profit_R": 52.13786778393428,
    "defense_net_R": -30.137867783934283
  },
  "entered_trades": {
    "entry_issue": 5,
    "selection_issue": 2,
    "open_unknown": 1
  }
}
```
