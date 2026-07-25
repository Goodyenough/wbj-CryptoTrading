---
created: 2026-07-25 23:39:12 CST
tags:
  - crypto
  - trading-system
  - shadow-experiment
account: demo
start_date: 2026-07-03
end_date: 2026-07-25
experiment: relative_strength_soft_gate
report_version: v3
opportunity_set_hash: 9468fbe1bab35767
---

# Paper Shadow Experiment relative_strength_soft_gate 2026-07-03 -> 2026-07-25 demo v3

This is an offline diagnostic experiment. It uses a fixed opportunity set and does not modify settings, plans, events, snapshots, or paper state.

## Decision

- verdict: retest
- opportunity_set_hash: 9468fbe1bab35767
- opportunity_set_path: `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-07-25\paper_shadow_opportunity_set_2026-07-03_2026-07-25_demo_9468fbe1bab35767_v3.json`
- config_action: do_not_modify_settings_toml

## Variant Summary

| Variant | Opportunities | Accepted | Filtered | Accepted Loser | Accepted Winner Path | Filtered Loser | Missed Winner | Total Decision R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| alt_equal_hard_0 | 95 | 51 | 44 | 9 | 17 | 13 | 2 | 45.55 |
| btc_eth_hard_0 | 95 | 43 | 52 | 5 | 15 | 17 | 4 | 43.03 |
| btc_eth_soft_minus_0_5 | 95 | 60 | 35 | 11 | 18 | 11 | 1 | 48.80 |
| risk_off_hard_0 | 95 | 52 | 43 | 10 | 15 | 12 | 4 | 33.03 |

## Outcome Counts

### alt_equal_hard_0

| Outcome | Count |
|---|---:|
| accepted_loser | 9 |
| accepted_neutral | 12 |
| accepted_right_censored | 13 |
| accepted_winner_path | 17 |
| filtered_loser | 13 |
| filtered_neutral | 20 |
| filtered_right_censored | 9 |
| missed_winner | 2 |

### btc_eth_hard_0

| Outcome | Count |
|---|---:|
| accepted_loser | 5 |
| accepted_neutral | 11 |
| accepted_right_censored | 12 |
| accepted_winner_path | 15 |
| filtered_loser | 17 |
| filtered_neutral | 21 |
| filtered_right_censored | 10 |
| missed_winner | 4 |

### btc_eth_soft_minus_0_5

| Outcome | Count |
|---|---:|
| accepted_loser | 11 |
| accepted_neutral | 14 |
| accepted_right_censored | 17 |
| accepted_winner_path | 18 |
| filtered_loser | 11 |
| filtered_neutral | 18 |
| filtered_right_censored | 5 |
| missed_winner | 1 |

### risk_off_hard_0

| Outcome | Count |
|---|---:|
| accepted_loser | 10 |
| accepted_neutral | 11 |
| accepted_right_censored | 16 |
| accepted_winner_path | 15 |
| filtered_loser | 12 |
| filtered_neutral | 21 |
| filtered_right_censored | 6 |
| missed_winner | 4 |

## Detail Rows

| Variant | Source | Symbol | Time | Regime | Accepted | Outcome | PnL_R | MFE_R | MAE_R | Reason |
|---|---|---|---|---|---|---|---:|---:|---:|---|
| btc_eth_hard_0 | RECLAIM_PENDING | `ONDOUSDT` | 2026-07-03 00:10 | n/a | false | filtered_loser | 1.00 | 0.04 | -1.43 | btc_eth RS -0.72% >= 0.00% |
| btc_eth_soft_minus_0_5 | RECLAIM_PENDING | `ONDOUSDT` | 2026-07-03 00:10 | n/a | false | filtered_loser | 1.00 | 0.04 | -1.43 | btc_eth RS -0.72% >= -0.50% |
| risk_off_hard_0 | RECLAIM_PENDING | `ONDOUSDT` | 2026-07-03 00:10 | n/a | true | accepted_loser | -1.00 | 0.04 | -1.43 | non-RISK_OFF kept; RS=-0.72% |
| alt_equal_hard_0 | RECLAIM_PENDING | `ONDOUSDT` | 2026-07-03 00:10 | n/a | false | filtered_loser | 1.00 | 0.04 | -1.43 | alt_equal RS -4.24% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ADAUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.83 | -0.39 | btc_eth RS 7.48% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ADAUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.83 | -0.39 | btc_eth RS 7.48% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ADAUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.83 | -0.39 | btc_eth RS 7.48% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ADAUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.83 | -0.39 | alt_equal RS 5.55% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-03 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.14 | 0.05 | btc_eth RS -0.90% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BTCUSDT` | 2026-07-03 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.14 | 0.05 | btc_eth RS -0.90% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-03 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.14 | 0.05 | btc_eth RS -0.90% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-03 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.14 | 0.05 | alt_equal RS -2.83% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-03 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.35 | -0.69 | btc_eth RS -1.30% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `SOLUSDT` | 2026-07-03 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.35 | -0.69 | btc_eth RS -1.30% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-03 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.35 | -0.69 | btc_eth RS -1.30% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-03 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.35 | -0.69 | alt_equal RS -3.22% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `XRPUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.52 | -0.46 | btc_eth RS 2.12% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `XRPUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.52 | -0.46 | btc_eth RS 2.12% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `XRPUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.52 | -0.46 | btc_eth RS 2.12% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `XRPUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.52 | -0.46 | alt_equal RS 0.19% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `NEARUSDT` | 2026-07-04 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.50 | -0.96 | btc_eth RS -2.18% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `NEARUSDT` | 2026-07-04 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.50 | -0.96 | btc_eth RS -2.18% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `NEARUSDT` | 2026-07-04 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.50 | -0.96 | btc_eth RS -2.18% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `NEARUSDT` | 2026-07-04 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.50 | -0.96 | alt_equal RS -2.02% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `PEPEUSDT` | 2026-07-04 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.60 | -0.25 | btc_eth RS -1.91% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `PEPEUSDT` | 2026-07-04 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.60 | -0.25 | btc_eth RS -1.91% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `PEPEUSDT` | 2026-07-04 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.60 | -0.25 | btc_eth RS -1.91% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `PEPEUSDT` | 2026-07-04 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.60 | -0.25 | alt_equal RS -1.74% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-04 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.14 | -1.28 | btc_eth RS -0.44% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `SOLUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.14 | -1.28 | btc_eth RS -0.44% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-04 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.14 | -1.28 | btc_eth RS -0.44% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-04 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.14 | -1.28 | alt_equal RS -0.28% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `TLMUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.46 | -0.78 | btc_eth RS 18.75% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `TLMUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.46 | -0.78 | btc_eth RS 18.75% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `TLMUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.46 | -0.78 | btc_eth RS 18.75% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `TLMUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.46 | -0.78 | alt_equal RS 18.91% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `XLMUSDT` | 2026-07-04 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.48 | -1.94 | btc_eth RS -4.72% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `XLMUSDT` | 2026-07-04 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.48 | -1.94 | btc_eth RS -4.72% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `XLMUSDT` | 2026-07-04 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.48 | -1.94 | btc_eth RS -4.72% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `XLMUSDT` | 2026-07-04 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.48 | -1.94 | alt_equal RS -4.56% >= 0.00% |
| btc_eth_hard_0 | REJECT | `BTCUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.01 | 3.01 | 0.01 | btc_eth RS 0.46% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `BTCUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.01 | 3.01 | 0.01 | btc_eth RS 0.46% >= -0.50% |
| risk_off_hard_0 | REJECT | `BTCUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.01 | 3.01 | 0.01 | btc_eth RS 0.46% >= 0.00% |
| alt_equal_hard_0 | REJECT | `BTCUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.01 | 3.01 | 0.01 | alt_equal RS 0.67% >= 0.00% |
| btc_eth_hard_0 | REJECT | `ETHUSDT` | 2026-07-08 20:06 | RISK_OFF | false | missed_winner | -3.55 | 3.55 | -0.41 | btc_eth RS -0.46% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `ETHUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.55 | 3.55 | -0.41 | btc_eth RS -0.46% >= -0.50% |
| risk_off_hard_0 | REJECT | `ETHUSDT` | 2026-07-08 20:06 | RISK_OFF | false | missed_winner | -3.55 | 3.55 | -0.41 | btc_eth RS -0.46% >= 0.00% |
| alt_equal_hard_0 | REJECT | `ETHUSDT` | 2026-07-08 20:06 | RISK_OFF | false | missed_winner | -3.55 | 3.55 | -0.41 | alt_equal RS -0.26% >= 0.00% |
| btc_eth_hard_0 | REJECT | `SOLUSDT` | 2026-07-08 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.77 | -1.94 | btc_eth RS -0.28% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `SOLUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.77 | -1.94 | btc_eth RS -0.28% >= -0.50% |
| risk_off_hard_0 | REJECT | `SOLUSDT` | 2026-07-08 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.77 | -1.94 | btc_eth RS -0.28% >= 0.00% |
| alt_equal_hard_0 | REJECT | `SOLUSDT` | 2026-07-08 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.77 | -1.94 | alt_equal RS -0.07% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `TRXUSDT` | 2026-07-08 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.77 | -0.95 | btc_eth RS -0.51% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `TRXUSDT` | 2026-07-08 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.77 | -0.95 | btc_eth RS -0.51% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `TRXUSDT` | 2026-07-08 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.77 | -0.95 | btc_eth RS -0.51% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `TRXUSDT` | 2026-07-08 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.77 | -0.95 | alt_equal RS -0.30% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.02 | 3.02 | -0.26 | btc_eth RS 1.20% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ZECUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.02 | 3.02 | -0.26 | btc_eth RS 1.20% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.02 | 3.02 | -0.26 | btc_eth RS 1.20% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.02 | 3.02 | -0.26 | alt_equal RS 1.41% >= 0.00% |
| btc_eth_hard_0 | REJECT | `BNBUSDT` | 2026-07-09 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.37 | -0.28 | btc_eth RS -1.92% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `BNBUSDT` | 2026-07-09 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.37 | -0.28 | btc_eth RS -1.92% >= -0.50% |
| risk_off_hard_0 | REJECT | `BNBUSDT` | 2026-07-09 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.37 | -0.28 | btc_eth RS -1.92% >= 0.00% |
| alt_equal_hard_0 | REJECT | `BNBUSDT` | 2026-07-09 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.37 | -0.28 | alt_equal RS -0.08% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-09 20:06 | RISK_OFF | false | missed_winner | -1.67 | 1.67 | -0.27 | btc_eth RS -0.55% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BTCUSDT` | 2026-07-09 20:06 | RISK_OFF | false | missed_winner | -1.67 | 1.67 | -0.27 | btc_eth RS -0.55% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-09 20:06 | RISK_OFF | false | missed_winner | -1.67 | 1.67 | -0.27 | btc_eth RS -0.55% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 1.67 | 1.67 | -0.27 | alt_equal RS 1.29% >= 0.00% |
| btc_eth_hard_0 | REJECT | `ETHUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 3.37 | 3.37 | -0.02 | btc_eth RS 0.55% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `ETHUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 3.37 | 3.37 | -0.02 | btc_eth RS 0.55% >= -0.50% |
| risk_off_hard_0 | REJECT | `ETHUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 3.37 | 3.37 | -0.02 | btc_eth RS 0.55% >= 0.00% |
| alt_equal_hard_0 | REJECT | `ETHUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 3.37 | 3.37 | -0.02 | alt_equal RS 2.39% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `TRXUSDT` | 2026-07-09 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.19 | -1.03 | btc_eth RS -2.63% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `TRXUSDT` | 2026-07-09 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.19 | -1.03 | btc_eth RS -2.63% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `TRXUSDT` | 2026-07-09 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.19 | -1.03 | btc_eth RS -2.63% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `TRXUSDT` | 2026-07-09 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.19 | -1.03 | alt_equal RS -0.79% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 3.54 | 3.54 | 0.25 | btc_eth RS 5.04% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ZECUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 3.54 | 3.54 | 0.25 | btc_eth RS 5.04% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 3.54 | 3.54 | 0.25 | btc_eth RS 5.04% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 3.54 | 3.54 | 0.25 | alt_equal RS 6.88% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BNBUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.24 | -0.62 | btc_eth RS 0.28% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BNBUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.24 | -0.62 | btc_eth RS 0.28% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BNBUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.24 | -0.62 | btc_eth RS 0.28% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `BNBUSDT` | 2026-07-10 20:05 | RISK_OFF | false | filtered_neutral | n/a | 0.24 | -0.62 | alt_equal RS -0.32% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-10 20:05 | RISK_OFF | false | filtered_neutral | n/a | 0.91 | -0.47 | btc_eth RS -0.56% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BTCUSDT` | 2026-07-10 20:05 | RISK_OFF | false | filtered_neutral | n/a | 0.91 | -0.47 | btc_eth RS -0.56% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-10 20:05 | RISK_OFF | false | filtered_neutral | n/a | 0.91 | -0.47 | btc_eth RS -0.56% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-10 20:05 | RISK_OFF | false | filtered_neutral | n/a | 0.91 | -0.47 | alt_equal RS -1.15% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_winner_path | 1.74 | 1.74 | -0.06 | btc_eth RS 0.56% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ETHUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_winner_path | 1.74 | 1.74 | -0.06 | btc_eth RS 0.56% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_winner_path | 1.74 | 1.74 | -0.06 | btc_eth RS 0.56% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-10 20:05 | RISK_OFF | false | missed_winner | -1.74 | 1.74 | -0.06 | alt_equal RS -0.04% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-10 20:05 | RISK_OFF | false | filtered_loser | 1.00 | -0.20 | -1.32 | btc_eth RS -0.46% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `SOLUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_loser | -1.00 | -0.20 | -1.32 | btc_eth RS -0.46% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-10 20:05 | RISK_OFF | false | filtered_loser | 1.00 | -0.20 | -1.32 | btc_eth RS -0.46% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-10 20:05 | RISK_OFF | false | filtered_loser | 1.00 | -0.20 | -1.32 | alt_equal RS -1.06% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BNBUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_neutral | n/a | 0.14 | -0.68 | btc_eth RS 0.05% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BNBUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_neutral | n/a | 0.14 | -0.68 | btc_eth RS 0.05% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BNBUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_neutral | n/a | 0.14 | -0.68 | btc_eth RS 0.05% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `BNBUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_neutral | n/a | 0.14 | -0.68 | alt_equal RS 1.78% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-11 22:27 | RISK_OFF | false | filtered_neutral | n/a | 0.80 | -0.54 | btc_eth RS -0.17% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BTCUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_neutral | n/a | 0.80 | -0.54 | btc_eth RS -0.17% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-11 22:27 | RISK_OFF | false | filtered_neutral | n/a | 0.80 | -0.54 | btc_eth RS -0.17% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_neutral | n/a | 0.80 | -0.54 | alt_equal RS 1.57% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.56 | 1.56 | -0.18 | btc_eth RS 0.17% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ETHUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.56 | 1.56 | -0.18 | btc_eth RS 0.17% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.56 | 1.56 | -0.18 | btc_eth RS 0.17% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.56 | 1.56 | -0.18 | alt_equal RS 1.91% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-11 22:27 | RISK_OFF | false | filtered_loser | 1.00 | 0.43 | -1.84 | btc_eth RS -1.34% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `SOLUSDT` | 2026-07-11 22:27 | RISK_OFF | false | filtered_loser | 1.00 | 0.43 | -1.84 | btc_eth RS -1.34% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-11 22:27 | RISK_OFF | false | filtered_loser | 1.00 | 0.43 | -1.84 | btc_eth RS -1.34% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_loser | -1.00 | 0.43 | -1.84 | alt_equal RS 0.40% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.50 | 1.50 | -0.45 | btc_eth RS 5.17% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ZECUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.50 | 1.50 | -0.45 | btc_eth RS 5.17% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.50 | 1.50 | -0.45 | btc_eth RS 5.17% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.50 | 1.50 | -0.45 | alt_equal RS 6.91% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BNBUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.18 | -0.90 | btc_eth RS 0.29% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BNBUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.18 | -0.90 | btc_eth RS 0.29% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BNBUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.18 | -0.90 | btc_eth RS 0.29% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `BNBUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.18 | -0.90 | alt_equal RS 0.46% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-12 20:05 | RISK_OFF | false | filtered_neutral | n/a | 1.01 | -0.73 | btc_eth RS -0.01% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BTCUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.01 | -0.73 | btc_eth RS -0.01% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-12 20:05 | RISK_OFF | false | filtered_neutral | n/a | 1.01 | -0.73 | btc_eth RS -0.01% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.01 | -0.73 | alt_equal RS 0.16% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.38 | -0.31 | btc_eth RS 0.01% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ETHUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.38 | -0.31 | btc_eth RS 0.01% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.38 | -0.31 | btc_eth RS 0.01% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.38 | -0.31 | alt_equal RS 0.17% >= 0.00% |
| btc_eth_hard_0 | REJECT | `SOLUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_loser | -1.00 | 0.59 | -1.28 | btc_eth RS 0.29% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `SOLUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_loser | -1.00 | 0.59 | -1.28 | btc_eth RS 0.29% >= -0.50% |
| risk_off_hard_0 | REJECT | `SOLUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_loser | -1.00 | 0.59 | -1.28 | btc_eth RS 0.29% >= 0.00% |
| alt_equal_hard_0 | REJECT | `SOLUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_loser | -1.00 | 0.59 | -1.28 | alt_equal RS 0.46% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-12 20:05 | RISK_OFF | false | filtered_neutral | n/a | 1.21 | -0.66 | btc_eth RS -1.79% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ZECUSDT` | 2026-07-12 20:05 | RISK_OFF | false | filtered_neutral | n/a | 1.21 | -0.66 | btc_eth RS -1.79% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-12 20:05 | RISK_OFF | false | filtered_neutral | n/a | 1.21 | -0.66 | btc_eth RS -1.79% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-12 20:05 | RISK_OFF | false | filtered_neutral | n/a | 1.21 | -0.66 | alt_equal RS -1.63% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `DEXEUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.12 | -4.06 | btc_eth RS -3.06% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `DEXEUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.12 | -4.06 | btc_eth RS -3.06% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `DEXEUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.12 | -4.06 | btc_eth RS -3.06% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `DEXEUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.12 | -4.06 | alt_equal RS -1.55% >= 0.00% |
| btc_eth_hard_0 | REJECT | `ETHUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_winner_path | 4.19 | 4.19 | -0.27 | btc_eth RS 1.07% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `ETHUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_winner_path | 4.19 | 4.19 | -0.27 | btc_eth RS 1.07% >= -0.50% |
| risk_off_hard_0 | REJECT | `ETHUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_winner_path | 4.19 | 4.19 | -0.27 | btc_eth RS 1.07% >= 0.00% |
| alt_equal_hard_0 | REJECT | `ETHUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_winner_path | 4.19 | 4.19 | -0.27 | alt_equal RS 2.58% >= 0.00% |
| btc_eth_hard_0 | REJECT | `TRXUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_neutral | n/a | 0.58 | -0.94 | btc_eth RS -4.58% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `TRXUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_neutral | n/a | 0.58 | -0.94 | btc_eth RS -4.58% >= -0.50% |
| risk_off_hard_0 | REJECT | `TRXUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_neutral | n/a | 0.58 | -0.94 | btc_eth RS -4.58% >= 0.00% |
| alt_equal_hard_0 | REJECT | `TRXUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_neutral | n/a | 0.58 | -0.94 | alt_equal RS -3.07% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `WLDUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.14 | -1.64 | btc_eth RS -3.21% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `WLDUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.14 | -1.64 | btc_eth RS -3.21% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `WLDUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.14 | -1.64 | btc_eth RS -3.21% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `WLDUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.14 | -1.64 | alt_equal RS -1.70% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_winner_path | 3.37 | 3.37 | -1.38 | btc_eth RS 1.56% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ZECUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_winner_path | 3.37 | 3.37 | -1.38 | btc_eth RS 1.56% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_winner_path | 3.37 | 3.37 | -1.38 | btc_eth RS 1.56% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_winner_path | 3.37 | 3.37 | -1.38 | alt_equal RS 3.08% >= 0.00% |
| btc_eth_hard_0 | REJECT | `BNBUSDT` | 2026-07-14 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.34 | -0.37 | btc_eth RS -2.24% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `BNBUSDT` | 2026-07-14 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.34 | -0.37 | btc_eth RS -2.24% >= -0.50% |
| risk_off_hard_0 | REJECT | `BNBUSDT` | 2026-07-14 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.34 | -0.37 | btc_eth RS -2.24% >= 0.00% |
| alt_equal_hard_0 | REJECT | `BNBUSDT` | 2026-07-14 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.34 | -0.37 | alt_equal RS -0.87% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 1.77 | 1.77 | 0.32 | btc_eth RS 0.98% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ETHUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 1.77 | 1.77 | 0.32 | btc_eth RS 0.98% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 1.77 | 1.77 | 0.32 | btc_eth RS 0.98% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 1.77 | 1.77 | 0.32 | alt_equal RS 2.35% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `NEARUSDT` | 2026-07-14 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.59 | -1.29 | btc_eth RS -0.48% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `NEARUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.59 | -1.29 | btc_eth RS -0.48% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `NEARUSDT` | 2026-07-14 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.59 | -1.29 | btc_eth RS -0.48% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `NEARUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.59 | -1.29 | alt_equal RS 0.89% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `SXTUSDT` | 2026-07-14 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.47 | -1.44 | btc_eth RS -7.02% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `SXTUSDT` | 2026-07-14 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.47 | -1.44 | btc_eth RS -7.02% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `SXTUSDT` | 2026-07-14 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.47 | -1.44 | btc_eth RS -7.02% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `SXTUSDT` | 2026-07-14 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.47 | -1.44 | alt_equal RS -5.66% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 4.03 | 4.03 | -1.40 | btc_eth RS 4.66% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ZECUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 4.03 | 4.03 | -1.40 | btc_eth RS 4.66% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 4.03 | 4.03 | -1.40 | btc_eth RS 4.66% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 4.03 | 4.03 | -1.40 | alt_equal RS 6.03% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BNBUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.09 | -0.70 | btc_eth RS 1.46% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BNBUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.09 | -0.70 | btc_eth RS 1.46% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BNBUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.09 | -0.70 | btc_eth RS 1.46% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `BNBUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.09 | -0.70 | alt_equal RS 0.73% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.65 | -0.45 | btc_eth RS 0.74% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BTCUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.65 | -0.45 | btc_eth RS 0.74% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.65 | -0.45 | btc_eth RS 0.74% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.65 | -0.45 | alt_equal RS 0.01% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-15 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.70 | -0.19 | btc_eth RS -0.74% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ETHUSDT` | 2026-07-15 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.70 | -0.19 | btc_eth RS -0.74% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-15 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.70 | -0.19 | btc_eth RS -0.74% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-15 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.70 | -0.19 | alt_equal RS -1.48% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `NEARUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.03 | -1.20 | btc_eth RS 1.37% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `NEARUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.03 | -1.20 | btc_eth RS 1.37% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `NEARUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.03 | -1.20 | btc_eth RS 1.37% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `NEARUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.03 | -1.20 | alt_equal RS 0.63% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.77 | -0.41 | btc_eth RS 0.39% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BTCUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.77 | -0.41 | btc_eth RS 0.39% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.77 | -0.41 | btc_eth RS 0.39% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.77 | -0.41 | alt_equal RS 0.05% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-16 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.34 | -0.36 | btc_eth RS -0.39% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ETHUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.34 | -0.36 | btc_eth RS -0.39% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-16 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.34 | -0.36 | btc_eth RS -0.39% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-16 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.34 | -0.36 | alt_equal RS -0.73% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ONDOUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.61 | -0.44 | btc_eth RS 0.71% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ONDOUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.61 | -0.44 | btc_eth RS 0.71% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ONDOUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.61 | -0.44 | btc_eth RS 0.71% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ONDOUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.61 | -0.44 | alt_equal RS 0.37% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `XRPUSDT` | 2026-07-16 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.58 | -0.40 | btc_eth RS -0.52% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `XRPUSDT` | 2026-07-16 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.58 | -0.40 | btc_eth RS -0.52% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `XRPUSDT` | 2026-07-16 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.58 | -0.40 | btc_eth RS -0.52% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `XRPUSDT` | 2026-07-16 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.58 | -0.40 | alt_equal RS -0.86% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.16 | -1.12 | btc_eth RS 0.16% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ZECUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.16 | -1.12 | btc_eth RS 0.16% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.16 | -1.12 | btc_eth RS 0.16% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-16 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.16 | -1.12 | alt_equal RS -0.18% >= 0.00% |
| btc_eth_hard_0 | REJECT | `BTCUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_winner_path | 2.57 | 2.57 | 0.59 | btc_eth RS 0.17% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `BTCUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_winner_path | 2.57 | 2.57 | 0.59 | btc_eth RS 0.17% >= -0.50% |
| risk_off_hard_0 | REJECT | `BTCUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_winner_path | 2.57 | 2.57 | 0.59 | btc_eth RS 0.17% >= 0.00% |
| alt_equal_hard_0 | REJECT | `BTCUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_winner_path | 2.57 | 2.57 | 0.59 | alt_equal RS 0.49% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-17 20:06 | RISK_OFF | false | missed_winner | -2.03 | 2.03 | -0.02 | btc_eth RS -0.17% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ETHUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_winner_path | 2.03 | 2.03 | -0.02 | btc_eth RS -0.17% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-17 20:06 | RISK_OFF | false | missed_winner | -2.03 | 2.03 | -0.02 | btc_eth RS -0.17% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_winner_path | 2.03 | 2.03 | -0.02 | alt_equal RS 0.16% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ONDOUSDT` | 2026-07-17 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.53 | -0.54 | btc_eth RS -10.94% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ONDOUSDT` | 2026-07-17 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.53 | -0.54 | btc_eth RS -10.94% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ONDOUSDT` | 2026-07-17 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.53 | -0.54 | btc_eth RS -10.94% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ONDOUSDT` | 2026-07-17 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.53 | -0.54 | alt_equal RS -10.62% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.01 | -2.46 | btc_eth RS 1.58% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ZECUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.01 | -2.46 | btc_eth RS 1.58% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.01 | -2.46 | btc_eth RS 1.58% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.01 | -2.46 | alt_equal RS 1.90% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-18 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.86 | -0.12 | btc_eth RS -0.37% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BTCUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.86 | -0.12 | btc_eth RS -0.37% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-18 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.86 | -0.12 | btc_eth RS -0.37% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-18 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.86 | -0.12 | alt_equal RS -0.20% >= 0.00% |
| btc_eth_hard_0 | REJECT | `SOLUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_winner_path | 2.73 | 2.73 | -0.11 | btc_eth RS 0.57% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `SOLUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_winner_path | 2.73 | 2.73 | -0.11 | btc_eth RS 0.57% >= -0.50% |
| risk_off_hard_0 | REJECT | `SOLUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_winner_path | 2.73 | 2.73 | -0.11 | btc_eth RS 0.57% >= 0.00% |
| alt_equal_hard_0 | REJECT | `SOLUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_winner_path | 2.73 | 2.73 | -0.11 | alt_equal RS 0.74% >= 0.00% |
| btc_eth_hard_0 | REJECT | `XRPUSDT` | 2026-07-18 20:05 | RISK_OFF | false | missed_winner | -3.31 | 3.31 | 0.43 | btc_eth RS -0.04% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `XRPUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_winner_path | 3.31 | 3.31 | 0.43 | btc_eth RS -0.04% >= -0.50% |
| risk_off_hard_0 | REJECT | `XRPUSDT` | 2026-07-18 20:05 | RISK_OFF | false | missed_winner | -3.31 | 3.31 | 0.43 | btc_eth RS -0.04% >= 0.00% |
| alt_equal_hard_0 | REJECT | `XRPUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_winner_path | 3.31 | 3.31 | 0.43 | alt_equal RS 0.13% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-18 20:05 | RISK_OFF | false | filtered_loser | 1.00 | 0.39 | -2.28 | btc_eth RS -1.82% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ZECUSDT` | 2026-07-18 20:05 | RISK_OFF | false | filtered_loser | 1.00 | 0.39 | -2.28 | btc_eth RS -1.82% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-18 20:05 | RISK_OFF | false | filtered_loser | 1.00 | 0.39 | -2.28 | btc_eth RS -1.82% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-18 20:05 | RISK_OFF | false | filtered_loser | 1.00 | 0.39 | -2.28 | alt_equal RS -1.65% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BANKUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.24 | -0.27 | btc_eth RS 84.69% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BANKUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.24 | -0.27 | btc_eth RS 84.69% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BANKUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.24 | -0.27 | btc_eth RS 84.69% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `BANKUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.24 | -0.27 | alt_equal RS 85.22% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-19 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.73 | -0.18 | btc_eth RS -0.06% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BTCUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.73 | -0.18 | btc_eth RS -0.06% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-19 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.73 | -0.18 | btc_eth RS -0.06% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.73 | -0.18 | alt_equal RS 0.47% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.78 | -0.15 | btc_eth RS 0.06% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ETHUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.78 | -0.15 | btc_eth RS 0.06% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.78 | -0.15 | btc_eth RS 0.06% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.78 | -0.15 | alt_equal RS 0.58% >= 0.00% |
| btc_eth_hard_0 | REJECT | `SOLUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.60 | -0.62 | btc_eth RS 0.41% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `SOLUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.60 | -0.62 | btc_eth RS 0.41% >= -0.50% |
| risk_off_hard_0 | REJECT | `SOLUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.60 | -0.62 | btc_eth RS 0.41% >= 0.00% |
| alt_equal_hard_0 | REJECT | `SOLUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.60 | -0.62 | alt_equal RS 0.93% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-19 20:05 | RISK_OFF | false | filtered_loser | 1.00 | -0.15 | -1.99 | btc_eth RS -2.71% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ZECUSDT` | 2026-07-19 20:05 | RISK_OFF | false | filtered_loser | 1.00 | -0.15 | -1.99 | btc_eth RS -2.71% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-19 20:05 | RISK_OFF | false | filtered_loser | 1.00 | -0.15 | -1.99 | btc_eth RS -2.71% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-19 20:05 | RISK_OFF | false | filtered_loser | 1.00 | -0.15 | -1.99 | alt_equal RS -2.18% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BANKUSDT` | 2026-07-20 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.33 | -0.61 | btc_eth RS -46.59% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BANKUSDT` | 2026-07-20 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.33 | -0.61 | btc_eth RS -46.59% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BANKUSDT` | 2026-07-20 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.33 | -0.61 | btc_eth RS -46.59% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `BANKUSDT` | 2026-07-20 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.33 | -0.61 | alt_equal RS -47.35% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.67 | -0.32 | btc_eth RS 0.05% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BTCUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.67 | -0.32 | btc_eth RS 0.05% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.67 | -0.32 | btc_eth RS 0.05% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-20 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.67 | -0.32 | alt_equal RS -0.71% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-20 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.75 | -0.30 | btc_eth RS -0.05% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ETHUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.75 | -0.30 | btc_eth RS -0.05% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-20 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.75 | -0.30 | btc_eth RS -0.05% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-20 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.75 | -0.30 | alt_equal RS -0.80% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-20 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.41 | -0.89 | btc_eth RS -1.11% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `SOLUSDT` | 2026-07-20 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.41 | -0.89 | btc_eth RS -1.11% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-20 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.41 | -0.89 | btc_eth RS -1.11% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-20 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.41 | -0.89 | alt_equal RS -1.86% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `XRPUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.25 | -0.44 | btc_eth RS 2.20% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `XRPUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.25 | -0.44 | btc_eth RS 2.20% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `XRPUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.25 | -0.44 | btc_eth RS 2.20% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `XRPUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.25 | -0.44 | alt_equal RS 1.44% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BANKUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_winner_path | 2.55 | 2.55 | 0.02 | btc_eth RS 12.20% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BANKUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_winner_path | 2.55 | 2.55 | 0.02 | btc_eth RS 12.20% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BANKUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_winner_path | 2.55 | 2.55 | 0.02 | btc_eth RS 12.20% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `BANKUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_winner_path | 2.55 | 2.55 | 0.02 | alt_equal RS 11.70% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-21 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.26 | -0.47 | btc_eth RS -0.76% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BTCUSDT` | 2026-07-21 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.26 | -0.47 | btc_eth RS -0.76% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-21 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.26 | -0.47 | btc_eth RS -0.76% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-21 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.26 | -0.47 | alt_equal RS -1.26% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.32 | -0.57 | btc_eth RS 0.76% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ETHUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.32 | -0.57 | btc_eth RS 0.76% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.32 | -0.57 | btc_eth RS 0.76% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.32 | -0.57 | alt_equal RS 0.27% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.16 | -0.98 | btc_eth RS 0.60% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `SOLUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.16 | -0.98 | btc_eth RS 0.60% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.16 | -0.98 | btc_eth RS 0.60% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.16 | -0.98 | alt_equal RS 0.11% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BANKUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_winner_path | 2.62 | 2.62 | 1.10 | btc_eth RS 41.27% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BANKUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_winner_path | 2.62 | 2.62 | 1.10 | btc_eth RS 41.27% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BANKUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_winner_path | 2.62 | 2.62 | 1.10 | non-RISK_OFF kept; RS=41.27% |
| alt_equal_hard_0 | WATCH_ONLY | `BANKUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_winner_path | 2.62 | 2.62 | 1.10 | alt_equal RS 41.97% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.00 | -0.53 | btc_eth RS 0.41% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BTCUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.00 | -0.53 | btc_eth RS 0.41% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.00 | -0.53 | non-RISK_OFF kept; RS=0.41% |
| alt_equal_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.00 | -0.53 | alt_equal RS 1.10% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-22 20:05 | NEUTRAL | false | filtered_right_censored | n/a | 0.09 | -0.63 | btc_eth RS -0.41% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ETHUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.09 | -0.63 | btc_eth RS -0.41% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.09 | -0.63 | non-RISK_OFF kept; RS=-0.41% |
| alt_equal_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.09 | -0.63 | alt_equal RS 0.29% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-22 20:05 | NEUTRAL | false | filtered_loser | 1.00 | 0.08 | -1.13 | btc_eth RS -0.60% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `SOLUSDT` | 2026-07-22 20:05 | NEUTRAL | false | filtered_loser | 1.00 | 0.08 | -1.13 | btc_eth RS -0.60% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_loser | -1.00 | 0.08 | -1.13 | non-RISK_OFF kept; RS=-0.60% |
| alt_equal_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_loser | -1.00 | 0.08 | -1.13 | alt_equal RS 0.10% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `XRPUSDT` | 2026-07-22 20:05 | NEUTRAL | false | filtered_right_censored | n/a | 0.10 | -0.69 | btc_eth RS -1.29% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `XRPUSDT` | 2026-07-22 20:05 | NEUTRAL | false | filtered_right_censored | n/a | 0.10 | -0.69 | btc_eth RS -1.29% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `XRPUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.10 | -0.69 | non-RISK_OFF kept; RS=-1.29% |
| alt_equal_hard_0 | WATCH_ONLY | `XRPUSDT` | 2026-07-22 20:05 | NEUTRAL | false | filtered_right_censored | n/a | 0.10 | -0.69 | alt_equal RS -0.59% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BANKUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.94 | 0.23 | btc_eth RS 18.20% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BANKUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.94 | 0.23 | btc_eth RS 18.20% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BANKUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.94 | 0.23 | non-RISK_OFF kept; RS=18.20% |
| alt_equal_hard_0 | WATCH_ONLY | `BANKUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.94 | 0.23 | alt_equal RS 19.02% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | 0.07 | -1.05 | btc_eth RS 0.22% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BTCUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | 0.07 | -1.05 | btc_eth RS 0.22% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | 0.07 | -1.05 | non-RISK_OFF kept; RS=0.22% |
| alt_equal_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | 0.07 | -1.05 | alt_equal RS 1.04% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | -0.51 | -1.08 | btc_eth RS -0.22% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ETHUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | -0.51 | -1.08 | btc_eth RS -0.22% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | -0.51 | -1.08 | non-RISK_OFF kept; RS=-0.22% |
| alt_equal_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | -0.51 | -1.08 | alt_equal RS 0.60% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | -0.89 | -1.99 | btc_eth RS -1.53% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `SOLUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | -0.89 | -1.99 | btc_eth RS -1.53% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | -0.89 | -1.99 | non-RISK_OFF kept; RS=-1.53% |
| alt_equal_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | -0.89 | -1.99 | alt_equal RS -0.71% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `XRPUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | -0.50 | -1.08 | btc_eth RS -0.40% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `XRPUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | -0.50 | -1.08 | btc_eth RS -0.40% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `XRPUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | -0.50 | -1.08 | non-RISK_OFF kept; RS=-0.40% |
| alt_equal_hard_0 | WATCH_ONLY | `XRPUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | -0.50 | -1.08 | alt_equal RS 0.42% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BANKUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.43 | 0.24 | btc_eth RS 8.20% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BANKUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.43 | 0.24 | btc_eth RS 8.20% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BANKUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.43 | 0.24 | non-RISK_OFF kept; RS=8.20% |
| alt_equal_hard_0 | WATCH_ONLY | `BANKUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.43 | 0.24 | alt_equal RS 8.26% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BNBUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | -0.06 | -0.14 | btc_eth RS 0.90% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BNBUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | -0.06 | -0.14 | btc_eth RS 0.90% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BNBUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | -0.06 | -0.14 | non-RISK_OFF kept; RS=0.90% |
| alt_equal_hard_0 | WATCH_ONLY | `BNBUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | -0.06 | -0.14 | alt_equal RS 0.96% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | -0.59 | -0.76 | btc_eth RS 0.09% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BTCUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | -0.59 | -0.76 | btc_eth RS 0.09% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | -0.59 | -0.76 | non-RISK_OFF kept; RS=0.09% |
| alt_equal_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | -0.59 | -0.76 | alt_equal RS 0.14% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.28 | -0.46 | btc_eth RS -0.09% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ETHUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | -0.28 | -0.46 | btc_eth RS -0.09% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | -0.28 | -0.46 | non-RISK_OFF kept; RS=-0.09% |
| alt_equal_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.28 | -0.46 | alt_equal RS -0.03% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `VANAUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | 0.07 | -0.86 | btc_eth RS -8.39% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `VANAUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | 0.07 | -0.86 | btc_eth RS -8.39% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `VANAUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.07 | -0.86 | non-RISK_OFF kept; RS=-8.39% |
| alt_equal_hard_0 | WATCH_ONLY | `VANAUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | 0.07 | -0.86 | alt_equal RS -8.33% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BANKUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | btc_eth relative strength unavailable |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BANKUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | btc_eth relative strength unavailable |
| risk_off_hard_0 | WATCH_ONLY | `BANKUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | btc_eth relative strength unavailable |
| alt_equal_hard_0 | WATCH_ONLY | `BANKUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | alt_equal relative strength unavailable |
| btc_eth_hard_0 | REJECT | `BNBUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | btc_eth relative strength unavailable |
| btc_eth_soft_minus_0_5 | REJECT | `BNBUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | btc_eth relative strength unavailable |
| risk_off_hard_0 | REJECT | `BNBUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | btc_eth relative strength unavailable |
| alt_equal_hard_0 | REJECT | `BNBUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | alt_equal relative strength unavailable |
| btc_eth_hard_0 | REJECT | `BTCUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | btc_eth relative strength unavailable |
| btc_eth_soft_minus_0_5 | REJECT | `BTCUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | btc_eth relative strength unavailable |
| risk_off_hard_0 | REJECT | `BTCUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | btc_eth relative strength unavailable |
| alt_equal_hard_0 | REJECT | `BTCUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | alt_equal relative strength unavailable |
| btc_eth_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | btc_eth relative strength unavailable |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ETHUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | btc_eth relative strength unavailable |
| risk_off_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | btc_eth relative strength unavailable |
| alt_equal_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | alt_equal relative strength unavailable |
| btc_eth_hard_0 | REJECT | `XRPUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | btc_eth relative strength unavailable |
| btc_eth_soft_minus_0_5 | REJECT | `XRPUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | btc_eth relative strength unavailable |
| risk_off_hard_0 | REJECT | `XRPUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | btc_eth relative strength unavailable |
| alt_equal_hard_0 | REJECT | `XRPUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | alt_equal relative strength unavailable |

## Raw Summary

```json
{
  "experiment": "relative_strength_soft_gate",
  "opportunity_set_hash": "9468fbe1bab35767",
  "opportunities": 95,
  "summary": [
    {
      "variant": "alt_equal_hard_0",
      "opportunities": 95,
      "accepted": 51,
      "filtered": 44,
      "accepted_loser": 9,
      "accepted_winner_path": 17,
      "filtered_loser": 13,
      "missed_winner": 2,
      "total_decision_R": 45.54695864339728,
      "outcomes": {
        "filtered_loser": 13,
        "accepted_neutral": 12,
        "filtered_neutral": 20,
        "accepted_winner_path": 17,
        "missed_winner": 2,
        "accepted_loser": 9,
        "filtered_right_censored": 9,
        "accepted_right_censored": 13
      }
    },
    {
      "variant": "btc_eth_hard_0",
      "opportunities": 95,
      "accepted": 43,
      "filtered": 52,
      "accepted_loser": 5,
      "accepted_winner_path": 15,
      "filtered_loser": 17,
      "missed_winner": 4,
      "total_decision_R": 43.02591902380618,
      "outcomes": {
        "filtered_loser": 17,
        "accepted_neutral": 11,
        "filtered_neutral": 21,
        "accepted_winner_path": 15,
        "missed_winner": 4,
        "accepted_loser": 5,
        "filtered_right_censored": 10,
        "accepted_right_censored": 12
      }
    },
    {
      "variant": "btc_eth_soft_minus_0_5",
      "opportunities": 95,
      "accepted": 60,
      "filtered": 35,
      "accepted_loser": 11,
      "accepted_winner_path": 18,
      "filtered_loser": 11,
      "missed_winner": 1,
      "total_decision_R": 48.80396812267222,
      "outcomes": {
        "filtered_loser": 11,
        "accepted_neutral": 14,
        "filtered_neutral": 18,
        "accepted_loser": 11,
        "accepted_winner_path": 18,
        "missed_winner": 1,
        "accepted_right_censored": 17,
        "filtered_right_censored": 5
      }
    },
    {
      "variant": "risk_off_hard_0",
      "opportunities": 95,
      "accepted": 52,
      "filtered": 43,
      "accepted_loser": 10,
      "accepted_winner_path": 15,
      "filtered_loser": 12,
      "missed_winner": 4,
      "total_decision_R": 33.02591902380618,
      "outcomes": {
        "accepted_loser": 10,
        "accepted_neutral": 11,
        "filtered_neutral": 21,
        "filtered_loser": 12,
        "accepted_winner_path": 15,
        "missed_winner": 4,
        "filtered_right_censored": 6,
        "accepted_right_censored": 16
      }
    }
  ]
}
```
