---
created: 2026-07-08 16:58:03 CST
tags:
  - crypto
  - trading-system
  - paper-audit
account: demo
start_date: 2026-06-19
end_date: 2026-07-02
report_version: v4
---

# Paper Opportunity Audit 2026-06-19 -> 2026-07-02 demo v4

本报告只解释 paper 阶段没有赚钱的来源，不证明策略长期盈利能力。

## Final Readout

- benchmark_context: BTC/ETH formal-window benchmark was broadly sideways; stopped trades point more toward entry quality.
- opportunity_verdict: review_entry_quality
- entered_trade_verdict: review_selection_and_entry
- mature_opportunities: 51
- right_censored_opportunities: 27
- defense_net_R: -14.42
- next_action: keep current settings while the next window collects more entered/TP1/reclaim evidence.

## BTC/ETH Benchmark

| Symbol | Status | Start | End | Return | High Return | Max Drawdown | Trend | Note |
|---|---|---:|---:|---:|---:|---:|---|---|
| `BTCUSDT` | ok | 62950.79 | 61612.93 | -2.13% | 3.00% | -9.96% | sideways | closed_4h_candles=84 fetched_from_api=0 |
| `ETHUSDT` | ok | 1705.39 | 1697.05 | -0.49% | 3.65% | -12.59% | sideways | closed_4h_candles=84 fetched_from_api=0 |

## Opportunity Audit Summary

| Classification | Count |
|---|---:|
| avoided_loser | 25 |
| missed_winner | 12 |
| false_entry | 7 |
| neutral_or_unknown | 34 |

### Opportunity Maturity

| Maturity Status | Count |
|---|---:|
| mature | 51 |
| right_censored | 27 |
| open_unknown | 0 |
| data_gap | 0 |

### Opportunity Funnel

| Stage | Count | Conversion | Mature | Right Censored | Dedupe Key | Note |
|---|---:|---:|---:|---:|---|---|
| scanned_candidates | 70 | n/a | 0 | 0 | scan_id+symbol | all scan candidates in the window |
| buy_candidates | 0 | 0.00% | 0 | 0 | scan_id+symbol | candidates allowed to become plans |
| watch_only_candidates | 47 | 67.14% | 0 | 0 | scan_id+symbol | defensive or lower-confidence candidates |
| reject_candidates | 23 | 32.86% | 0 | 0 | scan_id+symbol | rejected scan candidates |
| risk_off_blocked_candidates | 70 | 100.00% | 0 | 0 | scan_id+symbol | WATCH_ONLY/REJECT candidates tied to RISK_OFF evidence |
| reclaim_pending_plans | 1 | n/a | 51 | 27 | plan_id | deduped plans with reclaim pending events |
| reclaim_confirmed_or_entered_events | 0 | 0.00% | 0 | 0 | plan_id | plans with ENTERED or RECLAIM_CONFIRMED_ENTERED events |
| entered_plans | 0 | n/a | 0 | 0 | plan_id | paper plans that actually entered during the window |
| tp1_hit_plans | 0 | n/a | 0 | 0 | plan_id | entered plans that reached TP1 |
| stopped_plans | 0 | n/a | 0 | 0 | plan_id | entered plans currently marked STOPPED |

### Reclaim Reconciliation

| Metric | Value |
|---|---:|
| account_total_RECLAIM_PENDING_events | 111 |
| window_raw_RECLAIM_PENDING_events | 83 |
| deduped_reclaim_plans | 1 |
| excluded_reclaim_duplicate_events | 82 |
| scan_candidate_opportunities | 70 |
| entered_false_entries | 7 |
| final_classified_opportunities | 78 |

- dedupe_key: RECLAIM_PENDING: plan_id; WATCH_ONLY/REJECT: scan_id+symbol+action; false_entry: plan_id
- note: final opportunities combine deduped reclaim plans, scan WATCH_ONLY/REJECT candidates, and stopped entered trades classified as false_entry

### Counterfactual R Summary

| Metric | Value |
|---|---:|
| mature_avoided_loss_R | 25.00 |
| mature_missed_profit_R | 39.42 |
| mature_defense_net_R | -14.42 |

### Symbol Repeats

| Symbol | Opportunity Rows |
|---|---:|
| `SOLUSDT` | 12 |
| `ETHUSDT` | 9 |
| `BTCUSDT` | 7 |
| `SYNUSDT` | 6 |
| `ZECUSDT` | 5 |
| `XRPUSDT` | 5 |
| `WLDUSDT` | 4 |
| `TRXUSDT` | 4 |
| `ONDOUSDT` | 3 |
| `XPLUSDT` | 3 |
| `NEARUSDT` | 3 |
| `AAVEUSDT` | 3 |
| `TONUSDT` | 3 |
| `XLMUSDT` | 2 |
| `BNBUSDT` | 2 |
| `ADAUSDT` | 2 |
| `BICOUSDT` | 1 |
| `SUIUSDT` | 1 |
| `HEIUSDT` | 1 |
| `ACTUSDT` | 1 |
| `CELOUSDT` | 1 |

### Opportunity Details

| Source | Symbol | ID | First Time | Entry | Stop | TP1 | Max/Min After | Bars | Maturity | MFE_R | MAE_R | First Hit | Classification | Final | Explanation |
|---|---|---|---|---:|---:|---:|---:|---:|---|---:|---:|---|---|---|---|
| RECLAIM_PENDING | `ONDOUSDT` | `9734a33dea2e` | 2026-06-19 00:10 | 0.411568 | 0.338446 | 0.532217 | 0.364500 / 0.300400 | 82/42 | mature | -0.64 | -1.52 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| REJECT | `ETHUSDT` | `a4116cc70ea1:ETHUSDT` | 2026-06-19 20:06 | 1692.716500 | 1646.713150 | 1840.292300 | 1767.680000 / 1545.140000 | 79/42 | mature | 1.63 | -3.21 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| REJECT | `SOLUSDT` | `a4116cc70ea1:SOLUSDT` | 2026-06-19 20:06 | 68.534990 | 66.570082 | 75.709550 | 82.380000 / 66.130000 | 79/42 | mature | 7.05 | -1.22 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `WLDUSDT` | `a4116cc70ea1:WLDUSDT` | 2026-06-19 20:06 | 0.607116 | 0.562377 | 0.719286 | 0.643600 / 0.361500 | 79/42 | mature | 0.82 | -5.49 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `XLMUSDT` | `a4116cc70ea1:XLMUSDT` | 2026-06-19 20:06 | 0.217250 | 0.203537 | 0.250740 | 0.218500 / 0.170500 | 79/42 | mature | 0.09 | -3.41 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| REJECT | `XPLUSDT` | `a4116cc70ea1:XPLUSDT` | 2026-06-19 20:06 | 0.093078 | 0.083956 | 0.122584 | 0.108820 / 0.084800 | 79/42 | mature | 1.73 | -0.91 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ETHUSDT` | `4b508e31bdd5:ETHUSDT` | 2026-06-20 20:06 | 1733.825920 | 1646.713150 | 1900.467196 | 1767.680000 / 1545.140000 | 73/42 | mature | 0.39 | -2.17 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `SOLUSDT` | `4b508e31bdd5:SOLUSDT` | 2026-06-20 20:06 | 72.075580 | 66.901200 | 82.307201 | 82.380000 / 66.130000 | 73/42 | mature | 1.99 | -1.15 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `TRXUSDT` | `4b508e31bdd5:TRXUSDT` | 2026-06-20 20:06 | 0.322856 | 0.313526 | 0.340772 | 0.334100 / 0.315300 | 73/42 | mature | 1.21 | -0.81 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `WLDUSDT` | `4b508e31bdd5:WLDUSDT` | 2026-06-20 20:06 | 0.606013 | 0.566078 | 0.719286 | 0.643600 / 0.361500 | 73/42 | mature | 0.94 | -6.12 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `ZECUSDT` | `4b508e31bdd5:ZECUSDT` | 2026-06-20 20:06 | 472.232460 | 433.400000 | 544.113925 | 471.240000 / 376.410000 | 73/42 | mature | -0.03 | -2.47 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `BICOUSDT` | `87d1f0e4c969:BICOUSDT` | 2026-06-21 20:06 | 0.040970 | 0.018321 | 0.085822 | 0.047400 / 0.014750 | 67/42 | mature | 0.28 | -1.16 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `ETHUSDT` | `87d1f0e4c969:ETHUSDT` | 2026-06-21 20:06 | 1684.468500 | 1646.713150 | 1837.894350 | 1767.680000 / 1545.140000 | 67/42 | mature | 2.20 | -3.69 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `NEARUSDT` | `87d1f0e4c969:NEARUSDT` | 2026-06-21 20:06 | 2.229669 | 2.052740 | 2.556180 | 2.181000 / 1.782000 | 67/42 | mature | -0.28 | -2.53 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `SOLUSDT` | `87d1f0e4c969:SOLUSDT` | 2026-06-21 20:06 | 72.991227 | 66.901200 | 84.048075 | 82.380000 / 66.130000 | 67/42 | mature | 1.54 | -1.13 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `TRXUSDT` | `87d1f0e4c969:TRXUSDT` | 2026-06-21 20:06 | 0.325081 | 0.313526 | 0.347425 | 0.334100 / 0.315300 | 67/42 | mature | 0.78 | -0.85 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `BTCUSDT` | `097536a10619:BTCUSDT` | 2026-06-22 20:06 | 64546.575853 | 61923.985150 | 69333.351998 | 64472.000000 / 58381.990000 | 61/42 | mature | -0.03 | -2.35 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `ETHUSDT` | `097536a10619:ETHUSDT` | 2026-06-22 20:06 | 1773.083340 | 1668.294500 | 1979.546421 | 1734.590000 / 1545.140000 | 61/42 | mature | -0.37 | -2.18 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `SOLUSDT` | `097536a10619:SOLUSDT` | 2026-06-22 20:06 | 73.721280 | 67.600550 | 84.726744 | 82.380000 / 66.130000 | 61/42 | mature | 1.41 | -1.24 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `SYNUSDT` | `097536a10619:SYNUSDT` | 2026-06-22 20:06 | 0.257995 | 0.116624 | 0.495696 | 0.665800 / 0.259700 | 61/42 | mature | 2.88 | 0.01 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `WLDUSDT` | `097536a10619:WLDUSDT` | 2026-06-22 20:06 | 0.629082 | 0.581446 | 0.719286 | 0.625700 / 0.361500 | 61/42 | mature | -0.07 | -5.62 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| REJECT | `BTCUSDT` | `3b5de7642393:BTCUSDT` | 2026-06-23 20:07 | 62472.108000 | 61008.930000 | 66113.700350 | 62921.190000 / 58381.990000 | 55/42 | mature | 0.31 | -2.80 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| REJECT | `SUIUSDT` | `3b5de7642393:SUIUSDT` | 2026-06-23 20:07 | 0.701489 | 0.662905 | 0.807045 | 0.741200 / 0.673300 | 55/42 | mature | 1.03 | -0.73 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `SYNUSDT` | `3b5de7642393:SYNUSDT` | 2026-06-23 20:07 | 0.219023 | 0.125883 | 0.399336 | 0.665800 / 0.273800 | 55/42 | mature | 4.80 | 0.59 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `TRXUSDT` | `3b5de7642393:TRXUSDT` | 2026-06-23 20:07 | 0.330052 | 0.319140 | 0.350994 | 0.331500 / 0.315300 | 55/42 | mature | 0.13 | -1.35 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| REJECT | `WLDUSDT` | `3b5de7642393:WLDUSDT` | 2026-06-23 20:07 | 0.571710 | 0.529398 | 0.682868 | 0.543900 / 0.361500 | 55/42 | mature | -0.66 | -4.97 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| REJECT | `BNBUSDT` | `170fe0098ac0:BNBUSDT` | 2026-06-24 20:06 | 575.245000 | 562.011450 | 599.298450 | 570.470000 / 542.640000 | 49/42 | mature | -0.36 | -2.46 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| REJECT | `BTCUSDT` | `170fe0098ac0:BTCUSDT` | 2026-06-24 20:06 | 62462.996500 | 61008.930000 | 65294.715850 | 61911.040000 / 58381.990000 | 49/42 | mature | -0.38 | -2.81 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| REJECT | `ETHUSDT` | `170fe0098ac0:ETHUSDT` | 2026-06-24 20:06 | 1654.464500 | 1611.115250 | 1771.000500 | 1700.150000 / 1545.140000 | 49/42 | mature | 1.05 | -2.52 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| REJECT | `SOLUSDT` | `170fe0098ac0:SOLUSDT` | 2026-06-24 20:06 | 69.068000 | 67.137600 | 74.625000 | 82.380000 / 66.130000 | 49/42 | mature | 6.90 | -1.52 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| REJECT | `XRPUSDT` | `170fe0098ac0:XRPUSDT` | 2026-06-24 20:06 | 1.093090 | 1.066066 | 1.158080 | 1.093800 / 1.022700 | 49/42 | mature | 0.03 | -2.60 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `AAVEUSDT` | `71e06c148da7:AAVEUSDT` | 2026-06-25 20:08 | 81.695357 | 69.481900 | 102.355986 | 97.060000 / 80.910000 | 43/42 | mature | 1.26 | -0.06 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| REJECT | `BTCUSDT` | `71e06c148da7:BTCUSDT` | 2026-06-25 20:08 | 59780.571000 | 58216.159500 | 65294.715850 | 61612.930000 / 58381.990000 | 43/42 | mature | 1.17 | -0.89 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `SYNUSDT` | `71e06c148da7:SYNUSDT` | 2026-06-25 20:08 | 0.380653 | 0.231869 | 0.615186 | 0.665800 / 0.295710 | 43/42 | mature | 1.92 | -0.57 | tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `TRXUSDT` | `71e06c148da7:TRXUSDT` | 2026-06-25 20:08 | 0.329179 | 0.320223 | 0.346079 | 0.324100 / 0.315300 | 43/42 | mature | -0.57 | -1.55 | stop_first | avoided_loser | true | blocked candidate hit stop before reaching a near-TP1 path |
| WATCH_ONLY | `XPLUSDT` | `71e06c148da7:XPLUSDT` | 2026-06-25 20:08 | 0.093457 | 0.081263 | 0.114172 | 0.108820 / 0.086660 | 43/42 | mature | 1.26 | -0.56 | none | neutral_or_unknown | true | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `AAVEUSDT` | `0e7ad0534e93:AAVEUSDT` | 2026-06-26 20:06 | 85.395714 | 70.102450 | 110.345671 | 97.060000 / 83.210000 | 37/42 | right_censored | 0.76 | -0.14 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `HEIUSDT` | `0e7ad0534e93:HEIUSDT` | 2026-06-26 20:06 | 0.155325 | 0.086975 | 0.271702 | 0.161600 / 0.117900 | 37/42 | right_censored | 0.09 | -0.55 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `SOLUSDT` | `0e7ad0534e93:SOLUSDT` | 2026-06-26 20:06 | 68.231250 | 63.079400 | 75.756950 | 82.380000 / 70.500000 | 37/42 | mature | 2.75 | 0.44 | tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `SYNUSDT` | `0e7ad0534e93:SYNUSDT` | 2026-06-26 20:06 | 0.329902 | 0.250179 | 0.604283 | 0.665800 / 0.295710 | 37/42 | mature | 4.21 | -0.43 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `XPLUSDT` | `0e7ad0534e93:XPLUSDT` | 2026-06-26 20:06 | 0.101261 | 0.081952 | 0.132824 | 0.108820 / 0.086660 | 37/42 | right_censored | 0.39 | -0.76 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `AAVEUSDT` | `d505babb3397:AAVEUSDT` | 2026-06-27 20:06 | 93.366607 | 71.008650 | 131.559075 | 94.810000 / 83.210000 | 31/42 | right_censored | 0.06 | -0.45 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| REJECT | `BNBUSDT` | `d505babb3397:BNBUSDT` | 2026-06-27 20:06 | 560.585714 | 532.491000 | 605.762571 | 562.540000 / 542.640000 | 31/42 | right_censored | 0.07 | -0.64 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| REJECT | `BTCUSDT` | `d505babb3397:BTCUSDT` | 2026-06-27 20:06 | 58893.623000 | 57243.284850 | 65294.715850 | 61612.930000 / 58381.990000 | 31/42 | right_censored | 1.65 | -0.31 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `SOLUSDT` | `d505babb3397:SOLUSDT` | 2026-06-27 20:06 | 72.025430 | 63.079400 | 88.940950 | 82.380000 / 70.500000 | 31/42 | right_censored | 1.16 | -0.17 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| REJECT | `XRPUSDT` | `d505babb3397:XRPUSDT` | 2026-06-27 20:06 | 1.052691 | 0.994062 | 1.158080 | 1.093800 / 1.034000 | 31/42 | right_censored | 0.70 | -0.32 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `BTCUSDT` | `7426dc73980c:BTCUSDT` | 2026-06-28 20:05 | 58823.361500 | 57461.945000 | 64537.690000 | 61612.930000 / 58381.990000 | 25/42 | right_censored | 2.05 | -0.32 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| REJECT | `ETHUSDT` | `7426dc73980c:ETHUSDT` | 2026-06-28 20:05 | 1576.849821 | 1489.320000 | 1738.961500 | 1700.150000 / 1564.620000 | 25/42 | right_censored | 1.41 | -0.14 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| REJECT | `NEARUSDT` | `7426dc73980c:NEARUSDT` | 2026-06-28 20:05 | 1.849964 | 1.725720 | 2.138255 | 1.946000 / 1.782000 | 25/42 | right_censored | 0.77 | -0.55 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `SOLUSDT` | `7426dc73980c:SOLUSDT` | 2026-06-28 20:05 | 72.065550 | 64.665250 | 85.748243 | 82.380000 / 70.740000 | 25/42 | right_censored | 1.39 | -0.18 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| REJECT | `XRPUSDT` | `7426dc73980c:XRPUSDT` | 2026-06-28 20:05 | 1.047996 | 0.994062 | 1.138081 | 1.093800 / 1.034000 | 25/42 | right_censored | 0.85 | -0.26 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ACTUSDT` | `ae9a993942c9:ACTUSDT` | 2026-06-29 20:06 | 0.010812 | 0.007713 | 0.016756 | 0.012680 / 0.009240 | 19/42 | right_censored | 0.60 | -0.51 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `BTCUSDT` | `ae9a993942c9:BTCUSDT` | 2026-06-29 20:06 | 60669.464000 | 58016.509850 | 65531.776009 | 61612.930000 / 58381.990000 | 19/42 | right_censored | 0.36 | -0.86 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| REJECT | `ETHUSDT` | `ae9a993942c9:ETHUSDT` | 2026-06-29 20:06 | 1563.740000 | 1525.144450 | 1685.201650 | 1700.150000 / 1565.180000 | 19/42 | mature | 3.53 | 0.04 | tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `SOLUSDT` | `ae9a993942c9:SOLUSDT` | 2026-06-29 20:06 | 72.611638 | 68.693900 | 79.085295 | 82.380000 / 73.130000 | 19/42 | mature | 2.49 | 0.13 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| REJECT | `XRPUSDT` | `ae9a993942c9:XRPUSDT` | 2026-06-29 20:06 | 1.061876 | 1.016717 | 1.145636 | 1.093800 / 1.034000 | 19/42 | right_censored | 0.71 | -0.62 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| REJECT | `ETHUSDT` | `ccf353f12660:ETHUSDT` | 2026-06-30 20:06 | 1566.336000 | 1525.144450 | 1652.237300 | 1700.150000 / 1569.890000 | 13/42 | mature | 3.25 | 0.09 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `SOLUSDT` | `ccf353f12660:SOLUSDT` | 2026-06-30 20:06 | 73.409570 | 68.693900 | 82.135631 | 82.380000 / 73.670000 | 13/42 | mature | 1.90 | 0.06 | tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `SYNUSDT` | `ccf353f12660:SYNUSDT` | 2026-06-30 20:06 | 0.596452 | 0.262414 | 1.157145 | 0.603220 / 0.447610 | 13/42 | right_censored | 0.02 | -0.45 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| REJECT | `XRPUSDT` | `ccf353f12660:XRPUSDT` | 2026-06-30 20:06 | 1.040412 | 1.016717 | 1.084450 | 1.093800 / 1.038600 | 13/42 | mature | 2.25 | -0.08 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| REJECT | `ZECUSDT` | `ccf353f12660:ZECUSDT` | 2026-06-30 20:06 | 388.278214 | 362.509550 | 426.805250 | 449.800000 / 394.210000 | 13/42 | mature | 2.39 | 0.23 | near_tp1_first | missed_winner | true | blocked candidate reached a near-TP1 path before stop |
| WATCH_ONLY | `ADAUSDT` | `1bc2608a3ab4:ADAUSDT` | 2026-07-01 20:06 | 0.151140 | 0.139082 | 0.172492 | 0.160800 / 0.153400 | 7/42 | right_censored | 0.80 | 0.19 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `CELOUSDT` | `1bc2608a3ab4:CELOUSDT` | 2026-07-01 20:06 | 0.066002 | 0.054746 | 0.104475 | 0.069840 / 0.061500 | 7/42 | right_censored | 0.34 | -0.40 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `SOLUSDT` | `1bc2608a3ab4:SOLUSDT` | 2026-07-01 20:06 | 74.802405 | 68.693900 | 85.456003 | 82.380000 / 77.000000 | 7/42 | right_censored | 1.24 | 0.36 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `SYNUSDT` | `1bc2608a3ab4:SYNUSDT` | 2026-07-01 20:06 | 0.485392 | 0.323090 | 0.803716 | 0.603220 / 0.447610 | 7/42 | right_censored | 0.73 | -0.23 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `XLMUSDT` | `1bc2608a3ab4:XLMUSDT` | 2026-07-01 20:06 | 0.197882 | 0.166268 | 0.253850 | 0.203200 / 0.196700 | 7/42 | right_censored | 0.17 | -0.04 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ADAUSDT` | `ddf9572f5edf:ADAUSDT` | 2026-07-02 20:06 | 0.160380 | 0.139870 | 0.200098 | 0.159700 / 0.159700 | 1/42 | right_censored | -0.03 | -0.03 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ETHUSDT` | `ddf9572f5edf:ETHUSDT` | 2026-07-02 20:06 | 1634.325474 | 1526.947000 | 1822.239784 | 1700.150000 / 1700.150000 | 1/42 | right_censored | 0.61 | 0.61 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `NEARUSDT` | `ddf9572f5edf:NEARUSDT` | 2026-07-02 20:06 | 1.936094 | 1.697155 | 2.357707 | 1.940000 / 1.940000 | 1/42 | right_censored | 0.02 | 0.02 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `SOLUSDT` | `ddf9572f5edf:SOLUSDT` | 2026-07-02 20:06 | 81.766250 | 70.821500 | 101.189750 | 80.830000 / 80.830000 | 1/42 | right_censored | -0.09 | -0.09 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
| WATCH_ONLY | `ZECUSDT` | `ddf9572f5edf:ZECUSDT` | 2026-07-02 20:06 | 444.115920 | 380.210000 | 558.186520 | 433.070000 / 433.070000 | 1/42 | right_censored | -0.17 | -0.17 | none | neutral_or_unknown | false | no decisive missed winner or avoided loser evidence |
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
| `WLDUSDT` | `616e1bbfd4c6` | ENTERED | 2026-06-11 11:36 | n/a | 0.458300 | 0.316875 | 0.713862 | 1.38 | -0.70 | false | false | -60.03 | open_unknown | trade is still open or not terminal |

## Raw Classification Counts

```json
{
  "opportunities": {
    "avoided_loser": 25,
    "missed_winner": 12,
    "neutral_or_unknown": 34,
    "false_entry": 7
  },
  "opportunity_maturity": {
    "mature": 51,
    "right_censored": 27
  },
  "opportunity_r": {
    "avoided_loss_R": 25.0,
    "missed_profit_R": 39.42294637145537,
    "defense_net_R": -14.422946371455367
  },
  "entered_trades": {
    "entry_issue": 5,
    "selection_issue": 2,
    "open_unknown": 1
  }
}
```
