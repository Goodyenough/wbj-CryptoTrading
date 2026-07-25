---
created: 2026-07-25 23:54:04 CST
tags:
  - crypto
  - trading-system
  - shadow-experiment
account: demo
start_date: 2026-06-19
end_date: 2026-07-02
experiment: relative_strength_soft_gate
report_version: v1
opportunity_set_hash: 6e1f8adbd43f8f1f
---

# Paper Shadow Experiment relative_strength_soft_gate 2026-06-19 -> 2026-07-02 demo v1

This is an offline diagnostic experiment. It uses a fixed opportunity set and does not modify settings, plans, events, snapshots, or paper state.

## Decision

- verdict: retest
- opportunity_set_hash: 6e1f8adbd43f8f1f
- opportunity_set_path: `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-07-25\paper_shadow_opportunity_set_2026-06-19_2026-07-02_demo_6e1f8adbd43f8f1f_v1.json`
- config_action: do_not_modify_settings_toml

## Variant Summary

| Variant | Opportunities | Accepted | Filtered | Accepted Loser | Accepted Winner Path | Filtered Loser | Missed Winner | Total Decision R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| alt_equal_hard_0 | 71 | 26 | 45 | 8 | 7 | 17 | 5 | 23.32 |
| btc_eth_hard_0 | 71 | 29 | 42 | 8 | 9 | 17 | 3 | 34.59 |
| btc_eth_soft_minus_0_5 | 71 | 38 | 33 | 11 | 10 | 14 | 2 | 34.08 |
| risk_off_hard_0 | 71 | 30 | 41 | 9 | 9 | 16 | 3 | 32.59 |

## Outcome Counts

### alt_equal_hard_0

| Outcome | Count |
|---|---:|
| accepted_loser | 8 |
| accepted_neutral | 3 |
| accepted_right_censored | 8 |
| accepted_winner_path | 7 |
| filtered_loser | 17 |
| filtered_neutral | 4 |
| filtered_right_censored | 19 |
| missed_winner | 5 |

### btc_eth_hard_0

| Outcome | Count |
|---|---:|
| accepted_loser | 8 |
| accepted_neutral | 5 |
| accepted_right_censored | 7 |
| accepted_winner_path | 9 |
| filtered_loser | 17 |
| filtered_neutral | 2 |
| filtered_right_censored | 20 |
| missed_winner | 3 |

### btc_eth_soft_minus_0_5

| Outcome | Count |
|---|---:|
| accepted_loser | 11 |
| accepted_neutral | 5 |
| accepted_right_censored | 12 |
| accepted_winner_path | 10 |
| filtered_loser | 14 |
| filtered_neutral | 2 |
| filtered_right_censored | 15 |
| missed_winner | 2 |

### risk_off_hard_0

| Outcome | Count |
|---|---:|
| accepted_loser | 9 |
| accepted_neutral | 5 |
| accepted_right_censored | 7 |
| accepted_winner_path | 9 |
| filtered_loser | 16 |
| filtered_neutral | 2 |
| filtered_right_censored | 20 |
| missed_winner | 3 |

## Detail Rows

| Variant | Source | Symbol | Time | Regime | Accepted | Outcome | PnL_R | MFE_R | MAE_R | Reason |
|---|---|---|---|---|---|---|---:|---:|---:|---|
| btc_eth_hard_0 | RECLAIM_PENDING | `ONDOUSDT` | 2026-06-19 00:10 | n/a | false | filtered_loser | 1.00 | -0.64 | -1.52 | btc_eth RS -2.03% >= 0.00% |
| btc_eth_soft_minus_0_5 | RECLAIM_PENDING | `ONDOUSDT` | 2026-06-19 00:10 | n/a | false | filtered_loser | 1.00 | -0.64 | -1.52 | btc_eth RS -2.03% >= -0.50% |
| risk_off_hard_0 | RECLAIM_PENDING | `ONDOUSDT` | 2026-06-19 00:10 | n/a | true | accepted_loser | -1.00 | -0.64 | -1.52 | non-RISK_OFF kept; RS=-2.03% |
| alt_equal_hard_0 | RECLAIM_PENDING | `ONDOUSDT` | 2026-06-19 00:10 | n/a | false | filtered_loser | 1.00 | -0.64 | -1.52 | alt_equal RS -1.40% >= 0.00% |
| btc_eth_hard_0 | REJECT | `ETHUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.63 | -3.21 | btc_eth RS 0.21% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `ETHUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.63 | -3.21 | btc_eth RS 0.21% >= -0.50% |
| risk_off_hard_0 | REJECT | `ETHUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.63 | -3.21 | btc_eth RS 0.21% >= 0.00% |
| alt_equal_hard_0 | REJECT | `ETHUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.63 | -3.21 | alt_equal RS 0.20% >= 0.00% |
| btc_eth_hard_0 | REJECT | `SOLUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_winner_path | 7.05 | 7.05 | -1.22 | btc_eth RS 2.17% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `SOLUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_winner_path | 7.05 | 7.05 | -1.22 | btc_eth RS 2.17% >= -0.50% |
| risk_off_hard_0 | REJECT | `SOLUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_winner_path | 7.05 | 7.05 | -1.22 | btc_eth RS 2.17% >= 0.00% |
| alt_equal_hard_0 | REJECT | `SOLUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_winner_path | 7.05 | 7.05 | -1.22 | alt_equal RS 2.17% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `WLDUSDT` | 2026-06-19 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.82 | -5.49 | btc_eth RS -1.90% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `WLDUSDT` | 2026-06-19 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.82 | -5.49 | btc_eth RS -1.90% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `WLDUSDT` | 2026-06-19 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.82 | -5.49 | btc_eth RS -1.90% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `WLDUSDT` | 2026-06-19 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.82 | -5.49 | alt_equal RS -1.91% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `XLMUSDT` | 2026-06-19 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.09 | -3.41 | btc_eth RS -4.76% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `XLMUSDT` | 2026-06-19 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.09 | -3.41 | btc_eth RS -4.76% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `XLMUSDT` | 2026-06-19 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.09 | -3.41 | btc_eth RS -4.76% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `XLMUSDT` | 2026-06-19 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.09 | -3.41 | alt_equal RS -4.77% >= 0.00% |
| btc_eth_hard_0 | REJECT | `XPLUSDT` | 2026-06-19 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.73 | -0.91 | btc_eth RS -6.09% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `XPLUSDT` | 2026-06-19 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.73 | -0.91 | btc_eth RS -6.09% >= -0.50% |
| risk_off_hard_0 | REJECT | `XPLUSDT` | 2026-06-19 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.73 | -0.91 | btc_eth RS -6.09% >= 0.00% |
| alt_equal_hard_0 | REJECT | `XPLUSDT` | 2026-06-19 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.73 | -0.91 | alt_equal RS -6.10% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-06-20 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.39 | -2.17 | btc_eth RS -0.33% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ETHUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.39 | -2.17 | btc_eth RS -0.33% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-06-20 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.39 | -2.17 | btc_eth RS -0.33% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-06-20 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.39 | -2.17 | alt_equal RS -1.40% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.99 | -1.15 | btc_eth RS 3.18% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `SOLUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.99 | -1.15 | btc_eth RS 3.18% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.99 | -1.15 | btc_eth RS 3.18% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.99 | -1.15 | alt_equal RS 2.12% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `TRXUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.21 | -0.81 | btc_eth RS 1.04% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `TRXUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.21 | -0.81 | btc_eth RS 1.04% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `TRXUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.21 | -0.81 | btc_eth RS 1.04% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `TRXUSDT` | 2026-06-20 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.21 | -0.81 | alt_equal RS -0.02% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `WLDUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.94 | -6.12 | btc_eth RS 4.60% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `WLDUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.94 | -6.12 | btc_eth RS 4.60% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `WLDUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.94 | -6.12 | btc_eth RS 4.60% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `WLDUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.94 | -6.12 | alt_equal RS 3.54% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-06-20 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.03 | -2.47 | btc_eth RS -4.38% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ZECUSDT` | 2026-06-20 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.03 | -2.47 | btc_eth RS -4.38% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-06-20 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.03 | -2.47 | btc_eth RS -4.38% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-06-20 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.03 | -2.47 | alt_equal RS -5.44% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BICOUSDT` | 2026-06-21 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.28 | -1.16 | btc_eth RS -32.65% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BICOUSDT` | 2026-06-21 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.28 | -1.16 | btc_eth RS -32.65% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BICOUSDT` | 2026-06-21 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.28 | -1.16 | btc_eth RS -32.65% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `BICOUSDT` | 2026-06-21 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.28 | -1.16 | alt_equal RS -31.06% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-06-21 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 2.20 | -3.69 | btc_eth RS -0.07% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ETHUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 2.20 | -3.69 | btc_eth RS -0.07% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-06-21 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 2.20 | -3.69 | btc_eth RS -0.07% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 2.20 | -3.69 | alt_equal RS 1.52% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `NEARUSDT` | 2026-06-21 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.28 | -2.53 | btc_eth RS -4.65% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `NEARUSDT` | 2026-06-21 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.28 | -2.53 | btc_eth RS -4.65% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `NEARUSDT` | 2026-06-21 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.28 | -2.53 | btc_eth RS -4.65% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `NEARUSDT` | 2026-06-21 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.28 | -2.53 | alt_equal RS -3.06% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-06-21 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 1.54 | -1.13 | btc_eth RS -2.23% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `SOLUSDT` | 2026-06-21 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 1.54 | -1.13 | btc_eth RS -2.23% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-06-21 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 1.54 | -1.13 | btc_eth RS -2.23% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-06-21 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 1.54 | -1.13 | alt_equal RS -0.64% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `TRXUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.78 | -0.85 | btc_eth RS 0.13% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `TRXUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.78 | -0.85 | btc_eth RS 0.13% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `TRXUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.78 | -0.85 | btc_eth RS 0.13% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `TRXUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.78 | -0.85 | alt_equal RS 1.72% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_loser | -1.00 | -0.03 | -2.35 | btc_eth RS 0.62% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BTCUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_loser | -1.00 | -0.03 | -2.35 | btc_eth RS 0.62% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_loser | -1.00 | -0.03 | -2.35 | btc_eth RS 0.62% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_loser | -1.00 | -0.03 | -2.35 | alt_equal RS 0.95% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.37 | -2.18 | btc_eth RS -0.62% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ETHUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.37 | -2.18 | btc_eth RS -0.62% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.37 | -2.18 | btc_eth RS -0.62% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.37 | -2.18 | alt_equal RS -0.30% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 1.41 | -1.24 | btc_eth RS -1.52% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `SOLUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 1.41 | -1.24 | btc_eth RS -1.52% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 1.41 | -1.24 | btc_eth RS -1.52% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 1.41 | -1.24 | alt_equal RS -1.20% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `SYNUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_winner_path | 2.88 | 2.88 | 0.01 | btc_eth RS 17.69% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `SYNUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_winner_path | 2.88 | 2.88 | 0.01 | btc_eth RS 17.69% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `SYNUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_winner_path | 2.88 | 2.88 | 0.01 | btc_eth RS 17.69% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `SYNUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_winner_path | 2.88 | 2.88 | 0.01 | alt_equal RS 18.02% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `WLDUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.07 | -5.62 | btc_eth RS -8.60% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `WLDUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.07 | -5.62 | btc_eth RS -8.60% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `WLDUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.07 | -5.62 | btc_eth RS -8.60% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `WLDUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.07 | -5.62 | alt_equal RS -8.28% >= 0.00% |
| btc_eth_hard_0 | REJECT | `BTCUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_loser | 1.00 | 0.31 | -2.80 | btc_eth RS -0.53% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `BTCUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_loser | 1.00 | 0.31 | -2.80 | btc_eth RS -0.53% >= -0.50% |
| risk_off_hard_0 | REJECT | `BTCUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_loser | 1.00 | 0.31 | -2.80 | btc_eth RS -0.53% >= 0.00% |
| alt_equal_hard_0 | REJECT | `BTCUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_loser | 1.00 | 0.31 | -2.80 | alt_equal RS -0.32% >= 0.00% |
| btc_eth_hard_0 | REJECT | `SUIUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_neutral | n/a | 1.03 | -0.73 | btc_eth RS -1.05% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `SUIUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_neutral | n/a | 1.03 | -0.73 | btc_eth RS -1.05% >= -0.50% |
| risk_off_hard_0 | REJECT | `SUIUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_neutral | n/a | 1.03 | -0.73 | btc_eth RS -1.05% >= 0.00% |
| alt_equal_hard_0 | REJECT | `SUIUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_neutral | n/a | 1.03 | -0.73 | alt_equal RS -0.84% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `SYNUSDT` | 2026-06-23 20:07 | RISK_OFF | true | accepted_winner_path | 4.80 | 4.80 | 0.59 | btc_eth RS 23.25% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `SYNUSDT` | 2026-06-23 20:07 | RISK_OFF | true | accepted_winner_path | 4.80 | 4.80 | 0.59 | btc_eth RS 23.25% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `SYNUSDT` | 2026-06-23 20:07 | RISK_OFF | true | accepted_winner_path | 4.80 | 4.80 | 0.59 | btc_eth RS 23.25% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `SYNUSDT` | 2026-06-23 20:07 | RISK_OFF | true | accepted_winner_path | 4.80 | 4.80 | 0.59 | alt_equal RS 23.46% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `TRXUSDT` | 2026-06-23 20:07 | RISK_OFF | true | accepted_loser | -1.00 | 0.13 | -1.35 | btc_eth RS 2.35% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `TRXUSDT` | 2026-06-23 20:07 | RISK_OFF | true | accepted_loser | -1.00 | 0.13 | -1.35 | btc_eth RS 2.35% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `TRXUSDT` | 2026-06-23 20:07 | RISK_OFF | true | accepted_loser | -1.00 | 0.13 | -1.35 | btc_eth RS 2.35% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `TRXUSDT` | 2026-06-23 20:07 | RISK_OFF | true | accepted_loser | -1.00 | 0.13 | -1.35 | alt_equal RS 2.56% >= 0.00% |
| btc_eth_hard_0 | REJECT | `WLDUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.66 | -4.97 | btc_eth RS -2.94% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `WLDUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.66 | -4.97 | btc_eth RS -2.94% >= -0.50% |
| risk_off_hard_0 | REJECT | `WLDUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.66 | -4.97 | btc_eth RS -2.94% >= 0.00% |
| alt_equal_hard_0 | REJECT | `WLDUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.66 | -4.97 | alt_equal RS -2.73% >= 0.00% |
| btc_eth_hard_0 | REJECT | `BNBUSDT` | 2026-06-24 20:06 | RISK_OFF | true | accepted_loser | -1.00 | -0.36 | -2.46 | btc_eth RS 0.75% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `BNBUSDT` | 2026-06-24 20:06 | RISK_OFF | true | accepted_loser | -1.00 | -0.36 | -2.46 | btc_eth RS 0.75% >= -0.50% |
| risk_off_hard_0 | REJECT | `BNBUSDT` | 2026-06-24 20:06 | RISK_OFF | true | accepted_loser | -1.00 | -0.36 | -2.46 | btc_eth RS 0.75% >= 0.00% |
| alt_equal_hard_0 | REJECT | `BNBUSDT` | 2026-06-24 20:06 | RISK_OFF | true | accepted_loser | -1.00 | -0.36 | -2.46 | alt_equal RS 0.06% >= 0.00% |
| btc_eth_hard_0 | REJECT | `BTCUSDT` | 2026-06-24 20:06 | RISK_OFF | true | accepted_loser | -1.00 | -0.38 | -2.81 | btc_eth RS 0.91% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `BTCUSDT` | 2026-06-24 20:06 | RISK_OFF | true | accepted_loser | -1.00 | -0.38 | -2.81 | btc_eth RS 0.91% >= -0.50% |
| risk_off_hard_0 | REJECT | `BTCUSDT` | 2026-06-24 20:06 | RISK_OFF | true | accepted_loser | -1.00 | -0.38 | -2.81 | btc_eth RS 0.91% >= 0.00% |
| alt_equal_hard_0 | REJECT | `BTCUSDT` | 2026-06-24 20:06 | RISK_OFF | true | accepted_loser | -1.00 | -0.38 | -2.81 | alt_equal RS 0.23% >= 0.00% |
| btc_eth_hard_0 | REJECT | `ETHUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 1.05 | -2.52 | btc_eth RS -0.91% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `ETHUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 1.05 | -2.52 | btc_eth RS -0.91% >= -0.50% |
| risk_off_hard_0 | REJECT | `ETHUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 1.05 | -2.52 | btc_eth RS -0.91% >= 0.00% |
| alt_equal_hard_0 | REJECT | `ETHUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 1.05 | -2.52 | alt_equal RS -1.59% >= 0.00% |
| btc_eth_hard_0 | REJECT | `SOLUSDT` | 2026-06-24 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 6.90 | -1.52 | btc_eth RS 0.56% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `SOLUSDT` | 2026-06-24 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 6.90 | -1.52 | btc_eth RS 0.56% >= -0.50% |
| risk_off_hard_0 | REJECT | `SOLUSDT` | 2026-06-24 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 6.90 | -1.52 | btc_eth RS 0.56% >= 0.00% |
| alt_equal_hard_0 | REJECT | `SOLUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 6.90 | -1.52 | alt_equal RS -0.12% >= 0.00% |
| btc_eth_hard_0 | REJECT | `XRPUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.03 | -2.60 | btc_eth RS -0.15% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `XRPUSDT` | 2026-06-24 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.03 | -2.60 | btc_eth RS -0.15% >= -0.50% |
| risk_off_hard_0 | REJECT | `XRPUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.03 | -2.60 | btc_eth RS -0.15% >= 0.00% |
| alt_equal_hard_0 | REJECT | `XRPUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.03 | -2.60 | alt_equal RS -0.83% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `AAVEUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_neutral | n/a | 1.26 | -0.06 | btc_eth RS 12.20% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `AAVEUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_neutral | n/a | 1.26 | -0.06 | btc_eth RS 12.20% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `AAVEUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_neutral | n/a | 1.26 | -0.06 | btc_eth RS 12.20% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `AAVEUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_neutral | n/a | 1.26 | -0.06 | alt_equal RS 9.39% >= 0.00% |
| btc_eth_hard_0 | REJECT | `BTCUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_neutral | n/a | 1.17 | -0.89 | btc_eth RS 0.32% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `BTCUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_neutral | n/a | 1.17 | -0.89 | btc_eth RS 0.32% >= -0.50% |
| risk_off_hard_0 | REJECT | `BTCUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_neutral | n/a | 1.17 | -0.89 | btc_eth RS 0.32% >= 0.00% |
| alt_equal_hard_0 | REJECT | `BTCUSDT` | 2026-06-25 20:08 | RISK_OFF | false | filtered_neutral | n/a | 1.17 | -0.89 | alt_equal RS -2.48% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `SYNUSDT` | 2026-06-25 20:08 | RISK_OFF | false | missed_winner | -1.92 | 1.92 | -0.57 | btc_eth RS -16.15% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `SYNUSDT` | 2026-06-25 20:08 | RISK_OFF | false | missed_winner | -1.92 | 1.92 | -0.57 | btc_eth RS -16.15% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `SYNUSDT` | 2026-06-25 20:08 | RISK_OFF | false | missed_winner | -1.92 | 1.92 | -0.57 | btc_eth RS -16.15% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `SYNUSDT` | 2026-06-25 20:08 | RISK_OFF | false | missed_winner | -1.92 | 1.92 | -0.57 | alt_equal RS -18.95% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `TRXUSDT` | 2026-06-25 20:08 | RISK_OFF | false | filtered_loser | 1.00 | -0.57 | -1.55 | btc_eth RS -1.93% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `TRXUSDT` | 2026-06-25 20:08 | RISK_OFF | false | filtered_loser | 1.00 | -0.57 | -1.55 | btc_eth RS -1.93% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `TRXUSDT` | 2026-06-25 20:08 | RISK_OFF | false | filtered_loser | 1.00 | -0.57 | -1.55 | btc_eth RS -1.93% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `TRXUSDT` | 2026-06-25 20:08 | RISK_OFF | false | filtered_loser | 1.00 | -0.57 | -1.55 | alt_equal RS -4.73% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `XPLUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_neutral | n/a | 1.26 | -0.56 | btc_eth RS 10.87% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `XPLUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_neutral | n/a | 1.26 | -0.56 | btc_eth RS 10.87% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `XPLUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_neutral | n/a | 1.26 | -0.56 | btc_eth RS 10.87% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `XPLUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_neutral | n/a | 1.26 | -0.56 | alt_equal RS 8.07% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `AAVEUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.76 | -0.14 | btc_eth RS 2.23% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `AAVEUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.76 | -0.14 | btc_eth RS 2.23% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `AAVEUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.76 | -0.14 | btc_eth RS 2.23% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `AAVEUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.76 | -0.14 | alt_equal RS 2.33% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `HEIUSDT` | 2026-06-26 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.09 | -0.55 | btc_eth RS -4.07% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `HEIUSDT` | 2026-06-26 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.09 | -0.55 | btc_eth RS -4.07% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `HEIUSDT` | 2026-06-26 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.09 | -0.55 | btc_eth RS -4.07% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `HEIUSDT` | 2026-06-26 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.09 | -0.55 | alt_equal RS -3.96% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-06-26 20:06 | RISK_OFF | false | missed_winner | -2.75 | 2.75 | 0.44 | btc_eth RS -0.16% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `SOLUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_winner_path | 2.75 | 2.75 | 0.44 | btc_eth RS -0.16% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-06-26 20:06 | RISK_OFF | false | missed_winner | -2.75 | 2.75 | 0.44 | btc_eth RS -0.16% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-06-26 20:06 | RISK_OFF | false | missed_winner | -2.75 | 2.75 | 0.44 | alt_equal RS -0.06% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `SYNUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_winner_path | 4.21 | 4.21 | -0.43 | btc_eth RS 0.42% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `SYNUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_winner_path | 4.21 | 4.21 | -0.43 | btc_eth RS 0.42% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `SYNUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_winner_path | 4.21 | 4.21 | -0.43 | btc_eth RS 0.42% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `SYNUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_winner_path | 4.21 | 4.21 | -0.43 | alt_equal RS 0.52% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `XPLUSDT` | 2026-06-26 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.39 | -0.76 | btc_eth RS -1.84% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `XPLUSDT` | 2026-06-26 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.39 | -0.76 | btc_eth RS -1.84% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `XPLUSDT` | 2026-06-26 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.39 | -0.76 | btc_eth RS -1.84% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `XPLUSDT` | 2026-06-26 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.39 | -0.76 | alt_equal RS -1.74% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `AAVEUSDT` | 2026-06-27 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.06 | -0.45 | btc_eth RS -5.83% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `AAVEUSDT` | 2026-06-27 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.06 | -0.45 | btc_eth RS -5.83% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `AAVEUSDT` | 2026-06-27 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.06 | -0.45 | btc_eth RS -5.83% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `AAVEUSDT` | 2026-06-27 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.06 | -0.45 | alt_equal RS -5.37% >= 0.00% |
| btc_eth_hard_0 | REJECT | `BNBUSDT` | 2026-06-27 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.07 | -0.64 | btc_eth RS -0.38% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `BNBUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.07 | -0.64 | btc_eth RS -0.38% >= -0.50% |
| risk_off_hard_0 | REJECT | `BNBUSDT` | 2026-06-27 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.07 | -0.64 | btc_eth RS -0.38% >= 0.00% |
| alt_equal_hard_0 | REJECT | `BNBUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.07 | -0.64 | alt_equal RS 0.07% >= 0.00% |
| btc_eth_hard_0 | REJECT | `BTCUSDT` | 2026-06-27 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 1.65 | -0.31 | btc_eth RS -0.01% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `BTCUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.65 | -0.31 | btc_eth RS -0.01% >= -0.50% |
| risk_off_hard_0 | REJECT | `BTCUSDT` | 2026-06-27 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 1.65 | -0.31 | btc_eth RS -0.01% >= 0.00% |
| alt_equal_hard_0 | REJECT | `BTCUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.65 | -0.31 | alt_equal RS 0.44% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.16 | -0.17 | btc_eth RS 0.52% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `SOLUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.16 | -0.17 | btc_eth RS 0.52% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.16 | -0.17 | btc_eth RS 0.52% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.16 | -0.17 | alt_equal RS 0.97% >= 0.00% |
| btc_eth_hard_0 | REJECT | `XRPUSDT` | 2026-06-27 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.70 | -0.32 | btc_eth RS -0.55% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `XRPUSDT` | 2026-06-27 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.70 | -0.32 | btc_eth RS -0.55% >= -0.50% |
| risk_off_hard_0 | REJECT | `XRPUSDT` | 2026-06-27 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.70 | -0.32 | btc_eth RS -0.55% >= 0.00% |
| alt_equal_hard_0 | REJECT | `XRPUSDT` | 2026-06-27 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.70 | -0.32 | alt_equal RS -0.10% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 2.05 | -0.32 | btc_eth RS -0.04% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BTCUSDT` | 2026-06-28 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 2.05 | -0.32 | btc_eth RS -0.04% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 2.05 | -0.32 | btc_eth RS -0.04% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 2.05 | -0.32 | alt_equal RS -0.73% >= 0.00% |
| btc_eth_hard_0 | REJECT | `ETHUSDT` | 2026-06-28 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.41 | -0.14 | btc_eth RS 0.04% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `ETHUSDT` | 2026-06-28 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.41 | -0.14 | btc_eth RS 0.04% >= -0.50% |
| risk_off_hard_0 | REJECT | `ETHUSDT` | 2026-06-28 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.41 | -0.14 | btc_eth RS 0.04% >= 0.00% |
| alt_equal_hard_0 | REJECT | `ETHUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 1.41 | -0.14 | alt_equal RS -0.66% >= 0.00% |
| btc_eth_hard_0 | REJECT | `NEARUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.77 | -0.55 | btc_eth RS -0.94% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `NEARUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.77 | -0.55 | btc_eth RS -0.94% >= -0.50% |
| risk_off_hard_0 | REJECT | `NEARUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.77 | -0.55 | btc_eth RS -0.94% >= 0.00% |
| alt_equal_hard_0 | REJECT | `NEARUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.77 | -0.55 | alt_equal RS -1.63% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-06-28 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.39 | -0.18 | btc_eth RS 2.61% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `SOLUSDT` | 2026-06-28 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.39 | -0.18 | btc_eth RS 2.61% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-06-28 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.39 | -0.18 | btc_eth RS 2.61% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-06-28 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.39 | -0.18 | alt_equal RS 1.92% >= 0.00% |
| btc_eth_hard_0 | REJECT | `XRPUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.85 | -0.26 | btc_eth RS -0.23% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `XRPUSDT` | 2026-06-28 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.85 | -0.26 | btc_eth RS -0.23% >= -0.50% |
| risk_off_hard_0 | REJECT | `XRPUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.85 | -0.26 | btc_eth RS -0.23% >= 0.00% |
| alt_equal_hard_0 | REJECT | `XRPUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.85 | -0.26 | alt_equal RS -0.92% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ACTUSDT` | 2026-06-29 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.60 | -0.51 | btc_eth RS -11.57% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ACTUSDT` | 2026-06-29 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.60 | -0.51 | btc_eth RS -11.57% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ACTUSDT` | 2026-06-29 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.60 | -0.51 | btc_eth RS -11.57% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ACTUSDT` | 2026-06-29 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.60 | -0.51 | alt_equal RS -12.11% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-06-29 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.36 | -0.86 | btc_eth RS -0.73% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `BTCUSDT` | 2026-06-29 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.36 | -0.86 | btc_eth RS -0.73% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-06-29 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.36 | -0.86 | btc_eth RS -0.73% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `BTCUSDT` | 2026-06-29 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.36 | -0.86 | alt_equal RS -1.27% >= 0.00% |
| btc_eth_hard_0 | REJECT | `ETHUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_winner_path | 3.53 | 3.53 | 0.04 | btc_eth RS 0.73% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `ETHUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_winner_path | 3.53 | 3.53 | 0.04 | btc_eth RS 0.73% >= -0.50% |
| risk_off_hard_0 | REJECT | `ETHUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_winner_path | 3.53 | 3.53 | 0.04 | btc_eth RS 0.73% >= 0.00% |
| alt_equal_hard_0 | REJECT | `ETHUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_winner_path | 3.53 | 3.53 | 0.04 | alt_equal RS 0.19% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_winner_path | 2.49 | 2.49 | 0.13 | btc_eth RS 0.61% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `SOLUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_winner_path | 2.49 | 2.49 | 0.13 | btc_eth RS 0.61% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_winner_path | 2.49 | 2.49 | 0.13 | btc_eth RS 0.61% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_winner_path | 2.49 | 2.49 | 0.13 | alt_equal RS 0.07% >= 0.00% |
| btc_eth_hard_0 | REJECT | `XRPUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.71 | -0.62 | btc_eth RS 0.21% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `XRPUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.71 | -0.62 | btc_eth RS 0.21% >= -0.50% |
| risk_off_hard_0 | REJECT | `XRPUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.71 | -0.62 | btc_eth RS 0.21% >= 0.00% |
| alt_equal_hard_0 | REJECT | `XRPUSDT` | 2026-06-29 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.71 | -0.62 | alt_equal RS -0.33% >= 0.00% |
| btc_eth_hard_0 | REJECT | `ETHUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 3.25 | 3.25 | 0.09 | btc_eth RS 0.24% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `ETHUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 3.25 | 3.25 | 0.09 | btc_eth RS 0.24% >= -0.50% |
| risk_off_hard_0 | REJECT | `ETHUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 3.25 | 3.25 | 0.09 | btc_eth RS 0.24% >= 0.00% |
| alt_equal_hard_0 | REJECT | `ETHUSDT` | 2026-06-30 20:06 | RISK_OFF | false | missed_winner | -3.25 | 3.25 | 0.09 | alt_equal RS -0.92% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 1.90 | 1.90 | 0.06 | btc_eth RS 2.61% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `SOLUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 1.90 | 1.90 | 0.06 | btc_eth RS 2.61% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 1.90 | 1.90 | 0.06 | btc_eth RS 2.61% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 1.90 | 1.90 | 0.06 | alt_equal RS 1.45% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `SYNUSDT` | 2026-06-30 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.02 | -0.45 | btc_eth RS -28.98% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `SYNUSDT` | 2026-06-30 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.02 | -0.45 | btc_eth RS -28.98% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `SYNUSDT` | 2026-06-30 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.02 | -0.45 | btc_eth RS -28.98% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `SYNUSDT` | 2026-06-30 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.02 | -0.45 | alt_equal RS -30.14% >= 0.00% |
| btc_eth_hard_0 | REJECT | `XRPUSDT` | 2026-06-30 20:06 | RISK_OFF | false | missed_winner | -2.25 | 2.25 | -0.08 | btc_eth RS -0.69% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `XRPUSDT` | 2026-06-30 20:06 | RISK_OFF | false | missed_winner | -2.25 | 2.25 | -0.08 | btc_eth RS -0.69% >= -0.50% |
| risk_off_hard_0 | REJECT | `XRPUSDT` | 2026-06-30 20:06 | RISK_OFF | false | missed_winner | -2.25 | 2.25 | -0.08 | btc_eth RS -0.69% >= 0.00% |
| alt_equal_hard_0 | REJECT | `XRPUSDT` | 2026-06-30 20:06 | RISK_OFF | false | missed_winner | -2.25 | 2.25 | -0.08 | alt_equal RS -1.86% >= 0.00% |
| btc_eth_hard_0 | REJECT | `ZECUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 2.39 | 2.39 | 0.23 | btc_eth RS 0.16% >= 0.00% |
| btc_eth_soft_minus_0_5 | REJECT | `ZECUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 2.39 | 2.39 | 0.23 | btc_eth RS 0.16% >= -0.50% |
| risk_off_hard_0 | REJECT | `ZECUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 2.39 | 2.39 | 0.23 | btc_eth RS 0.16% >= 0.00% |
| alt_equal_hard_0 | REJECT | `ZECUSDT` | 2026-06-30 20:06 | RISK_OFF | false | missed_winner | -2.39 | 2.39 | 0.23 | alt_equal RS -1.01% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ADAUSDT` | 2026-07-01 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.80 | 0.19 | btc_eth RS -0.05% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ADAUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.80 | 0.19 | btc_eth RS -0.05% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `ADAUSDT` | 2026-07-01 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.80 | 0.19 | btc_eth RS -0.05% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `ADAUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.80 | 0.19 | alt_equal RS 0.40% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `CELOUSDT` | 2026-07-01 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.34 | -0.40 | btc_eth RS -13.42% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `CELOUSDT` | 2026-07-01 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.34 | -0.40 | btc_eth RS -13.42% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `CELOUSDT` | 2026-07-01 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.34 | -0.40 | btc_eth RS -13.42% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `CELOUSDT` | 2026-07-01 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.34 | -0.40 | alt_equal RS -12.97% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.24 | 0.36 | btc_eth RS 0.84% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `SOLUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.24 | 0.36 | btc_eth RS 0.84% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.24 | 0.36 | btc_eth RS 0.84% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.24 | 0.36 | alt_equal RS 1.29% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `SYNUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.73 | -0.23 | btc_eth RS 1.92% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `SYNUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.73 | -0.23 | btc_eth RS 1.92% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `SYNUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.73 | -0.23 | btc_eth RS 1.92% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `SYNUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.73 | -0.23 | alt_equal RS 2.37% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `XLMUSDT` | 2026-07-01 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.17 | -0.04 | btc_eth RS -4.98% >= 0.00% |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `XLMUSDT` | 2026-07-01 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.17 | -0.04 | btc_eth RS -4.98% >= -0.50% |
| risk_off_hard_0 | WATCH_ONLY | `XLMUSDT` | 2026-07-01 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.17 | -0.04 | btc_eth RS -4.98% >= 0.00% |
| alt_equal_hard_0 | WATCH_ONLY | `XLMUSDT` | 2026-07-01 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.17 | -0.04 | alt_equal RS -4.53% >= 0.00% |
| btc_eth_hard_0 | WATCH_ONLY | `ADAUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.03 | -0.03 | btc_eth relative strength unavailable |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ADAUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.03 | -0.03 | btc_eth relative strength unavailable |
| risk_off_hard_0 | WATCH_ONLY | `ADAUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.03 | -0.03 | btc_eth relative strength unavailable |
| alt_equal_hard_0 | WATCH_ONLY | `ADAUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.03 | -0.03 | alt_equal relative strength unavailable |
| btc_eth_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.61 | 0.61 | btc_eth relative strength unavailable |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ETHUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.61 | 0.61 | btc_eth relative strength unavailable |
| risk_off_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.61 | 0.61 | btc_eth relative strength unavailable |
| alt_equal_hard_0 | WATCH_ONLY | `ETHUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.61 | 0.61 | alt_equal relative strength unavailable |
| btc_eth_hard_0 | WATCH_ONLY | `NEARUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.02 | 0.02 | btc_eth relative strength unavailable |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `NEARUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.02 | 0.02 | btc_eth relative strength unavailable |
| risk_off_hard_0 | WATCH_ONLY | `NEARUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.02 | 0.02 | btc_eth relative strength unavailable |
| alt_equal_hard_0 | WATCH_ONLY | `NEARUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.02 | 0.02 | alt_equal relative strength unavailable |
| btc_eth_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.09 | -0.09 | btc_eth relative strength unavailable |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `SOLUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.09 | -0.09 | btc_eth relative strength unavailable |
| risk_off_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.09 | -0.09 | btc_eth relative strength unavailable |
| alt_equal_hard_0 | WATCH_ONLY | `SOLUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.09 | -0.09 | alt_equal relative strength unavailable |
| btc_eth_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.17 | -0.17 | btc_eth relative strength unavailable |
| btc_eth_soft_minus_0_5 | WATCH_ONLY | `ZECUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.17 | -0.17 | btc_eth relative strength unavailable |
| risk_off_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.17 | -0.17 | btc_eth relative strength unavailable |
| alt_equal_hard_0 | WATCH_ONLY | `ZECUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.17 | -0.17 | alt_equal relative strength unavailable |

## Raw Summary

```json
{
  "experiment": "relative_strength_soft_gate",
  "opportunity_set_hash": "6e1f8adbd43f8f1f",
  "opportunities": 71,
  "summary": [
    {
      "variant": "alt_equal_hard_0",
      "opportunities": 71,
      "accepted": 26,
      "filtered": 45,
      "accepted_loser": 8,
      "accepted_winner_path": 7,
      "filtered_loser": 17,
      "missed_winner": 5,
      "total_decision_R": 23.318852036358333,
      "outcomes": {
        "filtered_loser": 17,
        "accepted_loser": 8,
        "accepted_winner_path": 7,
        "filtered_neutral": 4,
        "accepted_neutral": 3,
        "missed_winner": 5,
        "accepted_right_censored": 8,
        "filtered_right_censored": 19
      }
    },
    {
      "variant": "btc_eth_hard_0",
      "opportunities": 71,
      "accepted": 29,
      "filtered": 42,
      "accepted_loser": 8,
      "accepted_winner_path": 9,
      "filtered_loser": 17,
      "missed_winner": 3,
      "total_decision_R": 34.590939954144744,
      "outcomes": {
        "filtered_loser": 17,
        "accepted_loser": 8,
        "accepted_winner_path": 9,
        "filtered_neutral": 2,
        "accepted_neutral": 5,
        "missed_winner": 3,
        "accepted_right_censored": 7,
        "filtered_right_censored": 20
      }
    },
    {
      "variant": "btc_eth_soft_minus_0_5",
      "opportunities": 71,
      "accepted": 38,
      "filtered": 33,
      "accepted_loser": 11,
      "accepted_winner_path": 10,
      "filtered_loser": 14,
      "missed_winner": 2,
      "total_decision_R": 34.083627047130754,
      "outcomes": {
        "filtered_loser": 14,
        "accepted_loser": 11,
        "accepted_winner_path": 10,
        "filtered_neutral": 2,
        "accepted_neutral": 5,
        "missed_winner": 2,
        "accepted_right_censored": 12,
        "filtered_right_censored": 15
      }
    },
    {
      "variant": "risk_off_hard_0",
      "opportunities": 71,
      "accepted": 30,
      "filtered": 41,
      "accepted_loser": 9,
      "accepted_winner_path": 9,
      "filtered_loser": 16,
      "missed_winner": 3,
      "total_decision_R": 32.590939954144744,
      "outcomes": {
        "accepted_loser": 9,
        "accepted_winner_path": 9,
        "filtered_loser": 16,
        "filtered_neutral": 2,
        "accepted_neutral": 5,
        "missed_winner": 3,
        "accepted_right_censored": 7,
        "filtered_right_censored": 20
      }
    }
  ]
}
```
