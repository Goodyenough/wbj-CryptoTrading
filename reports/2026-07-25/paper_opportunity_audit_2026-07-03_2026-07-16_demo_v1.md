---
created: 2026-07-25 23:07:14 CST
tags:
  - crypto
  - trading-system
  - paper-audit
account: demo
start_date: 2026-07-03
end_date: 2026-07-16
report_version: v1
---

# Paper Opportunity Audit 2026-07-03 -> 2026-07-16 demo v1

本报告只解释 paper 阶段没有赚钱的来源，不证明策略长期盈利能力。

## Final Readout

- benchmark_context: BTC/ETH formal-window benchmark rose; strategy losses or inactivity need selection/entry/defense review.
- opportunity_verdict: review_defense_rules
- entered_trade_verdict: review_selection_and_entry
- mature_opportunities: 36
- right_censored_opportunities: 24
- defense_net_R: -24.35
- data_link_verdict: partial_pass
- next_action: keep current settings while the next window collects more entered/TP1/reclaim evidence.

## Data Link Health

| Run Type | Expected | Observed | Success | Failed | Running | Success Rate | Latest Started |
|---|---:|---:|---:|---:|---:|---:|---|
| daily_full | 14 | 11 | 11 | 0 | 0 | 78.57% | 2026-07-16 20:05 |
| paper_4h_update | 70 | 57 | 56 | 1 | 0 | 80.00% | 2026-07-16 16:10 |

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
| `BTCUSDT` | ok | 61479.60 | 64704.73 | 5.25% | 6.42% | -3.65% | up | closed_4h_candles=84 fetched_from_api=0 |
| `ETHUSDT` | ok | 1700.15 | 1881.88 | 10.69% | 13.63% | -4.26% | up | closed_4h_candles=84 fetched_from_api=0 |

## Opportunity Audit Summary

| Classification | Count |
|---|---:|
| avoided_loser | 7 |
| missed_winner | 11 |
| false_entry | 7 |
| neutral_or_unknown | 35 |

### Opportunity Maturity

| Maturity Status | Count |
|---|---:|
| mature | 36 |
| right_censored | 24 |
| open_unknown | 0 |
| data_gap | 0 |

### Opportunity Funnel

| Stage | Count | Conversion | Mature | Right Censored | Dedupe Key | Note |
|---|---:|---:|---:|---:|---|---|
| scanned_candidates | 55 | n/a | 0 | 0 | scan_id+symbol | all scan candidates in the window |
| buy_candidates | 0 | 0.00% | 0 | 0 | scan_id+symbol | candidates allowed to become plans |
| watch_only_candidates | 43 | 78.18% | 0 | 0 | scan_id+symbol | defensive or lower-confidence candidates |
| reject_candidates | 9 | 16.36% | 0 | 0 | scan_id+symbol | rejected scan candidates |
| risk_off_blocked_candidates | 52 | 94.55% | 0 | 0 | scan_id+symbol | WATCH_ONLY/REJECT candidates tied to RISK_OFF evidence |
| reclaim_pending_plans | 1 | n/a | 36 | 24 | plan_id | deduped plans with reclaim pending events |
| reclaim_confirmed_or_entered_events | 0 | 0.00% | 0 | 0 | plan_id | plans with ENTERED or RECLAIM_CONFIRMED_ENTERED events |
| entered_plans | 0 | n/a | 0 | 0 | plan_id | paper plans that actually entered during the window |
| tp1_hit_plans | 0 | n/a | 0 | 0 | plan_id | entered plans that reached TP1 |
| stopped_plans | 0 | n/a | 0 | 0 | plan_id | entered plans currently marked STOPPED |

### Reclaim Reconciliation

| Metric | Value |
|---|---:|
| account_total_RECLAIM_PENDING_events | 208 |
| window_raw_RECLAIM_PENDING_events | 67 |
| deduped_reclaim_plans | 1 |
| excluded_reclaim_duplicate_events | 66 |
| scan_candidate_opportunities | 52 |
| entered_false_entries | 7 |
| final_classified_opportunities | 60 |

- dedupe_key: RECLAIM_PENDING: plan_id; WATCH_ONLY/REJECT: scan_id+symbol+action; false_entry: plan_id
- note: final opportunities combine deduped reclaim plans, scan WATCH_ONLY/REJECT candidates, and stopped entered trades classified as false_entry

### Counterfactual R Summary

| Metric | Value |
|---|---:|
| mature_avoided_loss_R | 7.00 |
| mature_missed_profit_R | 31.35 |
| mature_defense_net_R | -24.35 |

### Symbol Repeats

| Symbol | Opportunity Rows |
|---|---:|
| `ETHUSDT` | 9 |
| `ZECUSDT` | 9 |
| `BTCUSDT` | 8 |
| `SOLUSDT` | 6 |
| `BNBUSDT` | 6 |
| `ONDOUSDT` | 4 |
| `NEARUSDT` | 3 |
| `TRXUSDT` | 3 |
| `TONUSDT` | 3 |
| `XRPUSDT` | 2 |
| `ADAUSDT` | 1 |
| `PEPEUSDT` | 1 |
| `TLMUSDT` | 1 |
| `XLMUSDT` | 1 |
| `DEXEUSDT` | 1 |
| `WLDUSDT` | 1 |
| `SXTUSDT` | 1 |

### Opportunity Details

| Source | Symbol | ID | First Time | Entry | Stop | TP1 | Max/Min After | Bars | Maturity | MFE_R | MAE_R | First Hit | Classification | Final | Explanation |
|---|---|---|---|---:|---:|---:|---:|---:|---|---:|---:|---|---|---|---|
| RECLAIM_PENDING | `ONDOUSDT` | `9734a33dea2e` | 2026-07-03 00:10 | 0.411568 | 0.338446 | 0.532217 | 0.373700 / 0.307100 | 66/42 | mature | -0.52 | -1.43 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `ADAUSDT` | `0b0cbf231493:ADAUSDT` | 2026-07-03 20:06 | 0.168925 | 0.139870 | 0.221875 | 0.193100 / 0.157600 | 79/42 | mature | 0.83 | -0.39 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `BTCUSDT` | `0b0cbf231493:BTCUSDT` | 2026-07-03 20:06 | 61481.078566 | 56933.187150 | 69814.781365 | 65427.610000 / 61704.010000 | 79/42 | mature | 0.87 | 0.05 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `SOLUSDT` | `0b0cbf231493:SOLUSDT` | 2026-07-03 20:06 | 79.760221 | 71.166250 | 95.335747 | 82.740000 / 74.970000 | 79/42 | mature | 0.35 | -0.56 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `XRPUSDT` | `0b0cbf231493:XRPUSDT` | 2026-07-03 20:06 | 1.115938 | 1.006670 | 1.320822 | 1.172400 / 1.066200 | 79/42 | mature | 0.52 | -0.46 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `NEARUSDT` | `da040ac0b9ea:NEARUSDT` | 2026-07-04 20:06 | 1.977916 | 1.774970 | 2.348984 | 2.080000 / 1.855000 | 73/42 | mature | 0.50 | -0.61 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `PEPEUSDT` | `da040ac0b9ea:PEPEUSDT` | 2026-07-04 20:06 | 0.000003 | 0.000002 | 0.000003 | 0.000003 / 0.000003 | 73/42 | mature | 0.41 | -0.25 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `SOLUSDT` | `da040ac0b9ea:SOLUSDT` | 2026-07-04 20:06 | 81.268862 | 75.441150 | 91.569652 | 82.110000 / 74.970000 | 73/42 | mature | 0.14 | -1.08 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `TLMUSDT` | `da040ac0b9ea:TLMUSDT` | 2026-07-04 20:06 | 0.002859 | 0.000883 | 0.006072 | 0.003773 / 0.001535 | 73/42 | mature | 0.46 | -0.67 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `XLMUSDT` | `da040ac0b9ea:XLMUSDT` | 2026-07-04 20:06 | 0.203342 | 0.189711 | 0.226240 | 0.209900 / 0.178800 | 73/42 | mature | 0.48 | -1.80 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| REJECT | `BTCUSDT` | `9a6e108e270f:BTCUSDT` | 2026-07-08 20:06 | 61955.039500 | 60387.237400 | 64376.500000 | 65427.610000 / 61974.340000 | 49/42 | mature | 2.21 | 0.01 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| REJECT | `ETHUSDT` | `9a6e108e270f:ETHUSDT` | 2026-07-08 20:06 | 1752.862860 | 1699.302300 | 1834.109046 | 1931.950000 / 1730.700000 | 49/42 | mature | 3.34 | -0.41 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| REJECT | `SOLUSDT` | `9a6e108e270f:SOLUSDT` | 2026-07-08 20:06 | 77.772620 | 75.724353 | 83.560100 | 79.360000 / 74.970000 | 49/42 | mature | 0.77 | -1.37 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `TRXUSDT` | `9a6e108e270f:TRXUSDT` | 2026-07-08 20:06 | 0.327605 | 0.321504 | 0.338979 | 0.332200 / 0.323200 | 49/42 | mature | 0.75 | -0.72 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ZECUSDT` | `9a6e108e270f:ZECUSDT` | 2026-07-08 20:06 | 467.157280 | 431.164050 | 538.290353 | 575.920000 / 457.790000 | 49/42 | mature | 3.02 | -0.26 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| REJECT | `BNBUSDT` | `b2e95b25d9bb:BNBUSDT` | 2026-07-09 20:06 | 565.044000 | 551.994000 | 590.502650 | 582.870000 / 566.290000 | 43/42 | mature | 1.37 | 0.10 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `BTCUSDT` | `b2e95b25d9bb:BTCUSDT` | 2026-07-09 20:06 | 62891.831160 | 60621.391600 | 67210.751088 | 65427.610000 / 62288.230000 | 43/42 | mature | 1.12 | -0.27 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| REJECT | `ETHUSDT` | `b2e95b25d9bb:ETHUSDT` | 2026-07-09 20:06 | 1746.162820 | 1687.738400 | 1849.777500 | 1931.950000 / 1745.160000 | 43/42 | mature | 3.18 | -0.02 | tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `TRXUSDT` | `b2e95b25d9bb:TRXUSDT` | 2026-07-09 20:06 | 0.330664 | 0.322095 | 0.346884 | 0.332200 / 0.323200 | 43/42 | mature | 0.18 | -0.87 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ZECUSDT` | `b2e95b25d9bb:ZECUSDT` | 2026-07-09 20:06 | 467.839320 | 437.340000 | 526.013612 | 575.920000 / 481.540000 | 43/42 | mature | 3.54 | 0.45 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `BNBUSDT` | `26022241fbde:BNBUSDT` | 2026-07-10 20:05 | 576.857731 | 551.994000 | 622.598355 | 582.870000 / 566.290000 | 37/42 | right_censored | 0.24 | -0.43 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `BTCUSDT` | `26022241fbde:BTCUSDT` | 2026-07-10 20:05 | 63795.385986 | 60621.391600 | 69571.176796 | 65427.610000 / 62288.230000 | 37/42 | right_censored | 0.51 | -0.47 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ETHUSDT` | `26022241fbde:ETHUSDT` | 2026-07-10 20:05 | 1780.742579 | 1687.738400 | 1946.891611 | 1931.950000 / 1774.920000 | 37/42 | mature | 1.63 | -0.06 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `SOLUSDT` | `26022241fbde:SOLUSDT` | 2026-07-10 20:05 | 79.427570 | 75.145650 | 87.464194 | 78.380000 / 74.970000 | 37/42 | mature | -0.24 | -1.04 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `BNBUSDT` | `ebd75fd57197:BNBUSDT` | 2026-07-11 22:27 | 579.221913 | 553.215400 | 628.423025 | 582.870000 / 566.290000 | 31/42 | right_censored | 0.14 | -0.50 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `BTCUSDT` | `ebd75fd57197:BTCUSDT` | 2026-07-11 22:27 | 64048.963749 | 60766.620000 | 70240.370289 | 65427.610000 / 62288.230000 | 31/42 | right_censored | 0.42 | -0.54 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ETHUSDT` | `ebd75fd57197:ETHUSDT` | 2026-07-11 22:27 | 1792.482555 | 1696.101050 | 1971.024644 | 1931.950000 / 1774.920000 | 31/42 | right_censored | 1.45 | -0.18 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `SOLUSDT` | `ebd75fd57197:SOLUSDT` | 2026-07-11 22:27 | 77.656032 | 75.559350 | 83.321300 | 78.150000 / 74.970000 | 31/42 | mature | 0.24 | -1.28 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `ZECUSDT` | `ebd75fd57197:ZECUSDT` | 2026-07-11 22:27 | 498.819971 | 447.308200 | 589.370340 | 575.920000 / 495.570000 | 31/42 | mature | 1.50 | -0.06 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `BNBUSDT` | `2b2031877823:BNBUSDT` | 2026-07-12 20:05 | 579.278039 | 559.499700 | 615.782490 | 582.870000 / 566.290000 | 25/42 | right_censored | 0.18 | -0.66 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `BTCUSDT` | `2b2031877823:BTCUSDT` | 2026-07-12 20:05 | 64134.269490 | 61621.196150 | 68882.376973 | 65427.610000 / 62288.230000 | 25/42 | right_censored | 0.51 | -0.73 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ETHUSDT` | `2b2031877823:ETHUSDT` | 2026-07-12 20:05 | 1805.557117 | 1706.010150 | 1988.537247 | 1931.950000 / 1774.920000 | 25/42 | right_censored | 1.27 | -0.31 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| REJECT | `SOLUSDT` | `2b2031877823:SOLUSDT` | 2026-07-12 20:05 | 77.060490 | 74.515250 | 83.321300 | 78.070000 / 74.970000 | 25/42 | right_censored | 0.40 | -0.82 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ZECUSDT` | `2b2031877823:ZECUSDT` | 2026-07-12 20:05 | 510.898404 | 457.246850 | 606.327449 | 575.920000 / 495.570000 | 25/42 | right_censored | 1.21 | -0.29 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `DEXEUSDT` | `f58fa1439788:DEXEUSDT` | 2026-07-13 20:07 | 43.877821 | 33.490000 | 61.379007 | 42.635000 / 32.893000 | 19/42 | mature | -0.12 | -1.06 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| REJECT | `ETHUSDT` | `f58fa1439788:ETHUSDT` | 2026-07-13 20:07 | 1785.079220 | 1747.380150 | 1849.165500 | 1931.950000 / 1774.920000 | 19/42 | mature | 3.90 | -0.27 | tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| REJECT | `TRXUSDT` | `f58fa1439788:TRXUSDT` | 2026-07-13 20:07 | 0.328290 | 0.321405 | 0.341557 | 0.328100 / 0.323200 | 19/42 | right_censored | -0.03 | -0.74 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `WLDUSDT` | `f58fa1439788:WLDUSDT` | 2026-07-13 20:07 | 0.421996 | 0.373808 | 0.502414 | 0.415300 / 0.388700 | 19/42 | right_censored | -0.14 | -0.69 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ZECUSDT` | `f58fa1439788:ZECUSDT` | 2026-07-13 20:07 | 504.612500 | 483.458796 | 547.060950 | 575.920000 / 495.570000 | 19/42 | mature | 3.37 | -0.43 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| REJECT | `BNBUSDT` | `3ced75a34c7a:BNBUSDT` | 2026-07-14 20:06 | 565.890500 | 553.934450 | 586.208960 | 581.870000 / 575.800000 | 13/42 | right_censored | 1.34 | 0.83 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ETHUSDT` | `3ced75a34c7a:ETHUSDT` | 2026-07-14 20:06 | 1803.153280 | 1723.947000 | 1946.389132 | 1931.950000 / 1870.040000 | 13/42 | mature | 1.63 | 0.84 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `NEARUSDT` | `3ced75a34c7a:NEARUSDT` | 2026-07-14 20:06 | 1.986693 | 1.829145 | 2.255819 | 2.080000 / 2.007000 | 13/42 | right_censored | 0.59 | 0.13 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `SXTUSDT` | `3ced75a34c7a:SXTUSDT` | 2026-07-14 20:06 | 0.008801 | 0.007289 | 0.011247 | 0.009510 / 0.008190 | 13/42 | right_censored | 0.47 | -0.40 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ZECUSDT` | `3ced75a34c7a:ZECUSDT` | 2026-07-14 20:06 | 501.362092 | 482.861377 | 547.060950 | 575.920000 / 539.190000 | 13/42 | mature | 4.03 | 2.04 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `BNBUSDT` | `b91b23210b69:BNBUSDT` | 2026-07-15 20:06 | 579.151336 | 553.934450 | 626.446830 | 581.460000 / 575.800000 | 7/42 | right_censored | 0.09 | -0.13 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `BTCUSDT` | `b91b23210b69:BTCUSDT` | 2026-07-15 20:06 | 64393.142414 | 60897.595450 | 70894.803520 | 64977.340000 / 64238.000000 | 7/42 | right_censored | 0.17 | -0.04 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ETHUSDT` | `b91b23210b69:ETHUSDT` | 2026-07-15 20:06 | 1853.120662 | 1723.947000 | 2089.021948 | 1924.150000 / 1875.590000 | 7/42 | right_censored | 0.55 | 0.17 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `NEARUSDT` | `b91b23210b69:NEARUSDT` | 2026-07-15 20:06 | 2.060196 | 1.829145 | 2.460842 | 2.068000 / 2.028000 | 7/42 | right_censored | 0.03 | -0.14 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `BTCUSDT` | `e4779384fba8:BTCUSDT` | 2026-07-16 20:06 | 64171.611287 | 60897.595450 | 70180.334318 | 64271.840000 / 64271.840000 | 1/42 | right_censored | 0.03 | 0.03 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ETHUSDT` | `e4779384fba8:ETHUSDT` | 2026-07-16 20:06 | 1887.525640 | 1723.947000 | 2191.548141 | 1875.590000 / 1875.590000 | 1/42 | right_censored | -0.07 | -0.07 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ONDOUSDT` | `e4779384fba8:ONDOUSDT` | 2026-07-16 20:06 | 0.370866 | 0.300721 | 0.498034 | 0.375900 / 0.375900 | 1/42 | right_censored | 0.07 | 0.07 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `XRPUSDT` | `e4779384fba8:XRPUSDT` | 2026-07-16 20:06 | 1.113230 | 1.037698 | 1.257472 | 1.097300 / 1.097300 | 1/42 | right_censored | -0.21 | -0.21 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ZECUSDT` | `e4779384fba8:ZECUSDT` | 2026-07-16 20:06 | 549.272890 | 483.044000 | 678.616820 | 547.070000 / 547.070000 | 1/42 | right_censored | -0.03 | -0.03 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
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
| `WLDUSDT` | `616e1bbfd4c6` | ENTERED | 2026-06-11 11:36 | n/a | 0.458300 | 0.316875 | 0.713862 | 1.38 | -0.70 | false | false | -81.53 | open_unknown | trade is still open or not terminal |

## Raw Classification Counts

```json
{
  "opportunities": {
    "avoided_loser": 7,
    "neutral_or_unknown": 35,
    "missed_winner": 11,
    "false_entry": 7
  },
  "opportunity_maturity": {
    "mature": 36,
    "right_censored": 24
  },
  "opportunity_r": {
    "avoided_loss_R": 7.0,
    "missed_profit_R": 31.34943576294271,
    "defense_net_R": -24.34943576294271
  },
  "entered_trades": {
    "entry_issue": 5,
    "selection_issue": 2,
    "open_unknown": 1
  }
}
```
