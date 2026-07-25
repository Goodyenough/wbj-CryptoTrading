---
created: 2026-07-25 23:55:13 CST
tags:
  - crypto
  - trading-system
  - shadow-experiment
account: demo
start_date: 2026-07-17
end_date: 2026-07-25
experiment: relative_strength_soft_gate
report_version: v1
opportunity_set_hash: d958282222b977b7
---

# Paper Shadow Experiment relative_strength_soft_gate 2026-07-17 -> 2026-07-25 demo v1

This is an offline diagnostic experiment. It uses a fixed opportunity set and does not modify settings, plans, events, snapshots, or paper state.

## Decision

- verdict: retest
- opportunity_set_hash: d958282222b977b7
- opportunity_set_path: `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-07-25\paper_shadow_opportunity_set_2026-07-17_2026-07-25_demo_d958282222b977b7_v1.json`
- config_action: do_not_modify_settings_toml

## Variant Summary

| Variant | Opportunities | Accepted | Filtered | Accepted Loser | Accepted Winner Path | Filtered Loser | Missed Winner | Total Decision R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| alt_equal_hard_0 | 43 | 25 | 18 | 5 | 6 | 3 | 0 | 13.81 |
| btc_eth_hard_0 | 43 | 19 | 24 | 2 | 4 | 6 | 2 | 9.14 |
| btc_eth_soft_minus_0_5 | 43 | 28 | 15 | 4 | 6 | 4 | 0 | 15.81 |
| risk_off_hard_0 | 43 | 27 | 16 | 6 | 4 | 2 | 2 | 1.14 |

## Outcome Counts

### alt_equal_hard_0

| Outcome | Count |
|---|---:|
| accepted_loser | 5 |
| accepted_neutral | 1 |
| accepted_right_censored | 13 |
| accepted_winner_path | 6 |
| filtered_loser | 3 |
| filtered_neutral | 6 |
| filtered_right_censored | 9 |

### btc_eth_hard_0

| Outcome | Count |
|---|---:|
| accepted_loser | 2 |
| accepted_neutral | 1 |
| accepted_right_censored | 12 |
| accepted_winner_path | 4 |
| filtered_loser | 6 |
| filtered_neutral | 6 |
| filtered_right_censored | 10 |
| missed_winner | 2 |

### btc_eth_soft_minus_0_5

| Outcome | Count |
|---|---:|
| accepted_loser | 4 |
| accepted_neutral | 1 |
| accepted_right_censored | 17 |
| accepted_winner_path | 6 |
| filtered_loser | 4 |
| filtered_neutral | 6 |
| filtered_right_censored | 5 |

### risk_off_hard_0

| Outcome | Count |
|---|---:|
| accepted_loser | 6 |
| accepted_neutral | 1 |
| accepted_right_censored | 16 |
| accepted_winner_path | 4 |
| filtered_loser | 2 |
| filtered_neutral | 6 |
| filtered_right_censored | 6 |
| missed_winner | 2 |

## Detail Rows

| Variant | Source | Symbol | Time | Regime | Accepted | Outcome | PnL_R | MFE_R | MAE_R | Reason |
|---|---|---|---|---|---|---|---:|---:|---:|---|
| btc_eth_hard_0 | RECLAIM_PENDING | `ONDOUSDT` | 2026-07-17 00:10 | n/a | true | accepted_neutral | n/a | 0.04 | -0.99 | btc_eth RS 0.80% >= 0.00% |
| btc_eth_soft_minus_0_5 | RECLAIM_PENDING | `ONDOUSDT` | 2026-07-17 00:10 | n/a | true | accepted_neutral | n/a | 0.04 | -0.99 | btc_eth RS 0.80% >= -0.50% |
| risk_off_hard_0 | RECLAIM_PENDING | `ONDOUSDT` | 2026-07-17 00:10 | n/a | true | accepted_neutral | n/a | 0.04 | -0.99 | non-RISK_OFF kept; RS=0.80% |
| alt_equal_hard_0 | RECLAIM_PENDING | `ONDOUSDT` | 2026-07-17 00:10 | n/a | true | accepted_neutral | n/a | 0.04 | -0.99 | alt_equal RS 0.07% >= 0.00% |
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
  "opportunity_set_hash": "d958282222b977b7",
  "opportunities": 43,
  "summary": [
    {
      "variant": "alt_equal_hard_0",
      "opportunities": 43,
      "accepted": 25,
      "filtered": 18,
      "accepted_loser": 5,
      "accepted_winner_path": 6,
      "filtered_loser": 3,
      "missed_winner": 0,
      "total_decision_R": 13.813430849618083,
      "outcomes": {
        "accepted_neutral": 1,
        "accepted_winner_path": 6,
        "filtered_neutral": 6,
        "accepted_loser": 5,
        "filtered_right_censored": 9,
        "filtered_loser": 3,
        "accepted_right_censored": 13
      }
    },
    {
      "variant": "btc_eth_hard_0",
      "opportunities": 43,
      "accepted": 19,
      "filtered": 24,
      "accepted_loser": 2,
      "accepted_winner_path": 4,
      "filtered_loser": 6,
      "missed_winner": 2,
      "total_decision_R": 9.136395631114814,
      "outcomes": {
        "accepted_neutral": 1,
        "accepted_winner_path": 4,
        "missed_winner": 2,
        "filtered_neutral": 6,
        "accepted_loser": 2,
        "filtered_right_censored": 10,
        "filtered_loser": 6,
        "accepted_right_censored": 12
      }
    },
    {
      "variant": "btc_eth_soft_minus_0_5",
      "opportunities": 43,
      "accepted": 28,
      "filtered": 15,
      "accepted_loser": 4,
      "accepted_winner_path": 6,
      "filtered_loser": 4,
      "missed_winner": 0,
      "total_decision_R": 15.813430849618083,
      "outcomes": {
        "accepted_neutral": 1,
        "accepted_winner_path": 6,
        "filtered_neutral": 6,
        "accepted_loser": 4,
        "accepted_right_censored": 17,
        "filtered_loser": 4,
        "filtered_right_censored": 5
      }
    },
    {
      "variant": "risk_off_hard_0",
      "opportunities": 43,
      "accepted": 27,
      "filtered": 16,
      "accepted_loser": 6,
      "accepted_winner_path": 4,
      "filtered_loser": 2,
      "missed_winner": 2,
      "total_decision_R": 1.1363956311148145,
      "outcomes": {
        "accepted_neutral": 1,
        "accepted_winner_path": 4,
        "missed_winner": 2,
        "filtered_neutral": 6,
        "accepted_loser": 6,
        "filtered_right_censored": 6,
        "filtered_loser": 2,
        "accepted_right_censored": 16
      }
    }
  ]
}
```
