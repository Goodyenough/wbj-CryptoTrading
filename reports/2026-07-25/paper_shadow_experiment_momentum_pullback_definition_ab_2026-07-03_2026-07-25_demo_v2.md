---
created: 2026-07-25 23:36:38 CST
tags:
  - crypto
  - trading-system
  - shadow-experiment
account: demo
start_date: 2026-07-03
end_date: 2026-07-25
experiment: momentum_pullback_definition_ab
report_version: v2
opportunity_set_hash: 9468fbe1bab35767
---

# Paper Shadow Experiment momentum_pullback_definition_ab 2026-07-03 -> 2026-07-25 demo v2

This is an offline diagnostic experiment. It uses a fixed opportunity set and does not modify settings, plans, events, snapshots, or paper state.

## Decision

- verdict: retest
- opportunity_set_hash: 9468fbe1bab35767
- opportunity_set_path: `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-07-25\paper_shadow_opportunity_set_2026-07-03_2026-07-25_demo_9468fbe1bab35767_v2.json`
- config_action: do_not_modify_settings_toml

## Variant Summary

| Variant | Opportunities | Accepted | Filtered | Accepted Loser | Accepted Winner Path | Filtered Loser | Missed Winner | Total Decision R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| allow_minor_24h_pullback | 95 | 71 | 24 | 14 | 13 | 8 | 6 | 12.65 |
| current_24h_7d_positive | 95 | 53 | 42 | 10 | 8 | 12 | 11 | -15.29 |
| recent_high_atr_pullback | 95 | 44 | 51 | 13 | 5 | 9 | 14 | -39.66 |
| trend_support_atr_pullback | 95 | 47 | 48 | 14 | 15 | 8 | 4 | 25.79 |

## Outcome Counts

### allow_minor_24h_pullback

| Outcome | Count |
|---|---:|
| accepted_loser | 14 |
| accepted_neutral | 26 |
| accepted_right_censored | 18 |
| accepted_winner_path | 13 |
| filtered_loser | 8 |
| filtered_neutral | 6 |
| filtered_right_censored | 4 |
| missed_winner | 6 |

### current_24h_7d_positive

| Outcome | Count |
|---|---:|
| accepted_loser | 10 |
| accepted_neutral | 20 |
| accepted_right_censored | 15 |
| accepted_winner_path | 8 |
| filtered_loser | 12 |
| filtered_neutral | 12 |
| filtered_right_censored | 7 |
| missed_winner | 11 |

### recent_high_atr_pullback

| Outcome | Count |
|---|---:|
| accepted_loser | 13 |
| accepted_neutral | 17 |
| accepted_right_censored | 9 |
| accepted_winner_path | 5 |
| filtered_loser | 9 |
| filtered_neutral | 15 |
| filtered_right_censored | 13 |
| missed_winner | 14 |

### trend_support_atr_pullback

| Outcome | Count |
|---|---:|
| accepted_loser | 14 |
| accepted_neutral | 9 |
| accepted_right_censored | 9 |
| accepted_winner_path | 15 |
| filtered_loser | 8 |
| filtered_neutral | 23 |
| filtered_right_censored | 13 |
| missed_winner | 4 |

## Detail Rows

| Variant | Source | Symbol | Time | Regime | Accepted | Outcome | PnL_R | MFE_R | MAE_R | Reason |
|---|---|---|---|---|---|---|---:|---:|---:|---|
| current_24h_7d_positive | RECLAIM_PENDING | `ONDOUSDT` | 2026-07-03 00:10 | n/a | false | filtered_loser | 1.00 | 0.04 | -1.43 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | RECLAIM_PENDING | `ONDOUSDT` | 2026-07-03 00:10 | n/a | false | filtered_loser | 1.00 | 0.04 | -1.43 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | RECLAIM_PENDING | `ONDOUSDT` | 2026-07-03 00:10 | n/a | false | filtered_loser | 1.00 | 0.04 | -1.43 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | RECLAIM_PENDING | `ONDOUSDT` | 2026-07-03 00:10 | n/a | false | filtered_loser | 1.00 | 0.04 | -1.43 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ADAUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.83 | -0.39 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ADAUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.83 | -0.39 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ADAUSDT` | 2026-07-03 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.83 | -0.39 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ADAUSDT` | 2026-07-03 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.83 | -0.39 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BTCUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.14 | 0.05 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.14 | 0.05 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-03 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.14 | 0.05 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-03 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.14 | 0.05 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `SOLUSDT` | 2026-07-03 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.35 | -0.69 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.35 | -0.69 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.35 | -0.69 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-03 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.35 | -0.69 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `XRPUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.52 | -0.46 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `XRPUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.52 | -0.46 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `XRPUSDT` | 2026-07-03 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.52 | -0.46 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `XRPUSDT` | 2026-07-03 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.52 | -0.46 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `NEARUSDT` | 2026-07-04 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.50 | -0.96 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `NEARUSDT` | 2026-07-04 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.50 | -0.96 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `NEARUSDT` | 2026-07-04 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.50 | -0.96 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `NEARUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.50 | -0.96 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `PEPEUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.60 | -0.25 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `PEPEUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.60 | -0.25 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `PEPEUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.60 | -0.25 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `PEPEUSDT` | 2026-07-04 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.60 | -0.25 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `SOLUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.14 | -1.28 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.14 | -1.28 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.14 | -1.28 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.14 | -1.28 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `TLMUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.46 | -0.78 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `TLMUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.46 | -0.78 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `TLMUSDT` | 2026-07-04 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.46 | -0.78 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `TLMUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.46 | -0.78 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `XLMUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.48 | -1.94 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `XLMUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.48 | -1.94 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `XLMUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.48 | -1.94 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `XLMUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.48 | -1.94 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `BTCUSDT` | 2026-07-08 20:06 | RISK_OFF | false | missed_winner | -3.01 | 3.01 | 0.01 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `BTCUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.01 | 3.01 | 0.01 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `BTCUSDT` | 2026-07-08 20:06 | RISK_OFF | false | missed_winner | -3.01 | 3.01 | 0.01 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `BTCUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.01 | 3.01 | 0.01 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `ETHUSDT` | 2026-07-08 20:06 | RISK_OFF | false | missed_winner | -3.55 | 3.55 | -0.41 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `ETHUSDT` | 2026-07-08 20:06 | RISK_OFF | false | missed_winner | -3.55 | 3.55 | -0.41 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `ETHUSDT` | 2026-07-08 20:06 | RISK_OFF | false | missed_winner | -3.55 | 3.55 | -0.41 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `ETHUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.55 | 3.55 | -0.41 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `SOLUSDT` | 2026-07-08 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.77 | -1.94 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `SOLUSDT` | 2026-07-08 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.77 | -1.94 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `SOLUSDT` | 2026-07-08 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.77 | -1.94 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `SOLUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.77 | -1.94 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `TRXUSDT` | 2026-07-08 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.77 | -0.95 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `TRXUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.77 | -0.95 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `TRXUSDT` | 2026-07-08 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.77 | -0.95 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `TRXUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.77 | -0.95 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ZECUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.02 | 3.02 | -0.26 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.02 | 3.02 | -0.26 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-08 20:06 | RISK_OFF | false | missed_winner | -3.02 | 3.02 | -0.26 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.02 | 3.02 | -0.26 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `BNBUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.37 | -0.28 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `BNBUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.37 | -0.28 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `BNBUSDT` | 2026-07-09 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.37 | -0.28 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `BNBUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.37 | -0.28 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BTCUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 1.67 | 1.67 | -0.27 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 1.67 | 1.67 | -0.27 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 1.67 | 1.67 | -0.27 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 1.67 | 1.67 | -0.27 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `ETHUSDT` | 2026-07-09 20:06 | RISK_OFF | false | missed_winner | -3.37 | 3.37 | -0.02 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `ETHUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 3.37 | 3.37 | -0.02 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `ETHUSDT` | 2026-07-09 20:06 | RISK_OFF | false | missed_winner | -3.37 | 3.37 | -0.02 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `ETHUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 3.37 | 3.37 | -0.02 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `TRXUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.19 | -1.03 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `TRXUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.19 | -1.03 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `TRXUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.19 | -1.03 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `TRXUSDT` | 2026-07-09 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.19 | -1.03 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ZECUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 3.54 | 3.54 | 0.25 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 3.54 | 3.54 | 0.25 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-09 20:06 | RISK_OFF | false | missed_winner | -3.54 | 3.54 | 0.25 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 3.54 | 3.54 | 0.25 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BNBUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.24 | -0.62 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BNBUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.24 | -0.62 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BNBUSDT` | 2026-07-10 20:05 | RISK_OFF | false | filtered_neutral | n/a | 0.24 | -0.62 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BNBUSDT` | 2026-07-10 20:05 | RISK_OFF | false | filtered_neutral | n/a | 0.24 | -0.62 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BTCUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.91 | -0.47 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.91 | -0.47 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.91 | -0.47 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-10 20:05 | RISK_OFF | false | filtered_neutral | n/a | 0.91 | -0.47 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ETHUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_winner_path | 1.74 | 1.74 | -0.06 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_winner_path | 1.74 | 1.74 | -0.06 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_winner_path | 1.74 | 1.74 | -0.06 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_winner_path | 1.74 | 1.74 | -0.06 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `SOLUSDT` | 2026-07-10 20:05 | RISK_OFF | false | filtered_loser | 1.00 | -0.20 | -1.32 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-10 20:05 | RISK_OFF | false | filtered_loser | 1.00 | -0.20 | -1.32 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-10 20:05 | RISK_OFF | false | filtered_loser | 1.00 | -0.20 | -1.32 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-10 20:05 | RISK_OFF | false | filtered_loser | 1.00 | -0.20 | -1.32 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BNBUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_neutral | n/a | 0.14 | -0.68 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BNBUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_neutral | n/a | 0.14 | -0.68 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BNBUSDT` | 2026-07-11 22:27 | RISK_OFF | false | filtered_neutral | n/a | 0.14 | -0.68 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BNBUSDT` | 2026-07-11 22:27 | RISK_OFF | false | filtered_neutral | n/a | 0.14 | -0.68 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BTCUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_neutral | n/a | 0.80 | -0.54 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_neutral | n/a | 0.80 | -0.54 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_neutral | n/a | 0.80 | -0.54 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-11 22:27 | RISK_OFF | false | filtered_neutral | n/a | 0.80 | -0.54 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ETHUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.56 | 1.56 | -0.18 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.56 | 1.56 | -0.18 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.56 | 1.56 | -0.18 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-11 22:27 | RISK_OFF | false | missed_winner | -1.56 | 1.56 | -0.18 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `SOLUSDT` | 2026-07-11 22:27 | RISK_OFF | false | filtered_loser | 1.00 | 0.43 | -1.84 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-11 22:27 | RISK_OFF | false | filtered_loser | 1.00 | 0.43 | -1.84 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-11 22:27 | RISK_OFF | false | filtered_loser | 1.00 | 0.43 | -1.84 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-11 22:27 | RISK_OFF | false | filtered_loser | 1.00 | 0.43 | -1.84 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ZECUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.50 | 1.50 | -0.45 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.50 | 1.50 | -0.45 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.50 | 1.50 | -0.45 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.50 | 1.50 | -0.45 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BNBUSDT` | 2026-07-12 20:05 | RISK_OFF | false | filtered_neutral | n/a | 0.18 | -0.90 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BNBUSDT` | 2026-07-12 20:05 | RISK_OFF | false | filtered_neutral | n/a | 0.18 | -0.90 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BNBUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.18 | -0.90 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BNBUSDT` | 2026-07-12 20:05 | RISK_OFF | false | filtered_neutral | n/a | 0.18 | -0.90 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BTCUSDT` | 2026-07-12 20:05 | RISK_OFF | false | filtered_neutral | n/a | 1.01 | -0.73 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.01 | -0.73 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.01 | -0.73 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-12 20:05 | RISK_OFF | false | filtered_neutral | n/a | 1.01 | -0.73 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ETHUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.38 | -0.31 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.38 | -0.31 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.38 | -0.31 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-12 20:05 | RISK_OFF | false | filtered_neutral | n/a | 1.38 | -0.31 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `SOLUSDT` | 2026-07-12 20:05 | RISK_OFF | false | filtered_loser | 1.00 | 0.59 | -1.28 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `SOLUSDT` | 2026-07-12 20:05 | RISK_OFF | false | filtered_loser | 1.00 | 0.59 | -1.28 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `SOLUSDT` | 2026-07-12 20:05 | RISK_OFF | false | filtered_loser | 1.00 | 0.59 | -1.28 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `SOLUSDT` | 2026-07-12 20:05 | RISK_OFF | false | filtered_loser | 1.00 | 0.59 | -1.28 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ZECUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.21 | -0.66 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.21 | -0.66 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.21 | -0.66 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.21 | -0.66 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `DEXEUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_loser | -1.00 | -0.12 | -4.06 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `DEXEUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_loser | -1.00 | -0.12 | -4.06 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `DEXEUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_loser | -1.00 | -0.12 | -4.06 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `DEXEUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_loser | -1.00 | -0.12 | -4.06 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `ETHUSDT` | 2026-07-13 20:07 | RISK_OFF | false | missed_winner | -4.19 | 4.19 | -0.27 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `ETHUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_winner_path | 4.19 | 4.19 | -0.27 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `ETHUSDT` | 2026-07-13 20:07 | RISK_OFF | false | missed_winner | -4.19 | 4.19 | -0.27 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `ETHUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_winner_path | 4.19 | 4.19 | -0.27 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `TRXUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_neutral | n/a | 0.58 | -0.94 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `TRXUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_neutral | n/a | 0.58 | -0.94 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `TRXUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_neutral | n/a | 0.58 | -0.94 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `TRXUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_neutral | n/a | 0.58 | -0.94 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `WLDUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.14 | -1.64 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `WLDUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_loser | -1.00 | -0.14 | -1.64 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `WLDUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_loser | -1.00 | -0.14 | -1.64 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `WLDUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_loser | -1.00 | -0.14 | -1.64 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ZECUSDT` | 2026-07-13 20:07 | RISK_OFF | false | missed_winner | -3.37 | 3.37 | -1.38 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_winner_path | 3.37 | 3.37 | -1.38 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-13 20:07 | RISK_OFF | false | missed_winner | -3.37 | 3.37 | -1.38 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_winner_path | 3.37 | 3.37 | -1.38 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `BNBUSDT` | 2026-07-14 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.34 | -0.37 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `BNBUSDT` | 2026-07-14 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.34 | -0.37 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `BNBUSDT` | 2026-07-14 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.34 | -0.37 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `BNBUSDT` | 2026-07-14 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.34 | -0.37 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ETHUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 1.77 | 1.77 | 0.32 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 1.77 | 1.77 | 0.32 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 1.77 | 1.77 | 0.32 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 1.77 | 1.77 | 0.32 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `NEARUSDT` | 2026-07-14 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.59 | -1.29 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `NEARUSDT` | 2026-07-14 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.59 | -1.29 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `NEARUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.59 | -1.29 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `NEARUSDT` | 2026-07-14 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.59 | -1.29 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `SXTUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.47 | -1.44 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `SXTUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.47 | -1.44 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `SXTUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.47 | -1.44 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `SXTUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.47 | -1.44 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ZECUSDT` | 2026-07-14 20:06 | RISK_OFF | false | missed_winner | -4.03 | 4.03 | -1.40 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 4.03 | 4.03 | -1.40 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-14 20:06 | RISK_OFF | false | missed_winner | -4.03 | 4.03 | -1.40 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 4.03 | 4.03 | -1.40 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BNBUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.09 | -0.70 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BNBUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.09 | -0.70 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BNBUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.09 | -0.70 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BNBUSDT` | 2026-07-15 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.09 | -0.70 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BTCUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.65 | -0.45 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.65 | -0.45 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.65 | -0.45 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-15 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.65 | -0.45 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ETHUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.70 | -0.19 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.70 | -0.19 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.70 | -0.19 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-15 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.70 | -0.19 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `NEARUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.03 | -1.20 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `NEARUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.03 | -1.20 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `NEARUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.03 | -1.20 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `NEARUSDT` | 2026-07-15 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.03 | -1.20 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BTCUSDT` | 2026-07-16 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.77 | -0.41 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.77 | -0.41 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.77 | -0.41 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-16 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.77 | -0.41 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ETHUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.34 | -0.36 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.34 | -0.36 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.34 | -0.36 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-16 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.34 | -0.36 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ONDOUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.61 | -0.44 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ONDOUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.61 | -0.44 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ONDOUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.61 | -0.44 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ONDOUSDT` | 2026-07-16 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.61 | -0.44 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `XRPUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.58 | -0.40 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `XRPUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.58 | -0.40 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `XRPUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.58 | -0.40 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `XRPUSDT` | 2026-07-16 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.58 | -0.40 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ZECUSDT` | 2026-07-16 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.16 | -1.12 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-16 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.16 | -1.12 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.16 | -1.12 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.16 | -1.12 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `BTCUSDT` | 2026-07-17 20:06 | RISK_OFF | false | missed_winner | -2.57 | 2.57 | 0.59 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `BTCUSDT` | 2026-07-17 20:06 | RISK_OFF | false | missed_winner | -2.57 | 2.57 | 0.59 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `BTCUSDT` | 2026-07-17 20:06 | RISK_OFF | false | missed_winner | -2.57 | 2.57 | 0.59 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `BTCUSDT` | 2026-07-17 20:06 | RISK_OFF | false | missed_winner | -2.57 | 2.57 | 0.59 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ETHUSDT` | 2026-07-17 20:06 | RISK_OFF | false | missed_winner | -2.03 | 2.03 | -0.02 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-17 20:06 | RISK_OFF | false | missed_winner | -2.03 | 2.03 | -0.02 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-17 20:06 | RISK_OFF | false | missed_winner | -2.03 | 2.03 | -0.02 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_winner_path | 2.03 | 2.03 | -0.02 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ONDOUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.53 | -0.54 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ONDOUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.53 | -0.54 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ONDOUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.53 | -0.54 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ONDOUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.53 | -0.54 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ZECUSDT` | 2026-07-17 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 1.01 | -2.46 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.01 | -2.46 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-17 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 1.01 | -2.46 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.01 | -2.46 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BTCUSDT` | 2026-07-18 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.86 | -0.12 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-18 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.86 | -0.12 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-18 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.86 | -0.12 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-18 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.86 | -0.12 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `SOLUSDT` | 2026-07-18 20:05 | RISK_OFF | false | missed_winner | -2.73 | 2.73 | -0.11 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `SOLUSDT` | 2026-07-18 20:05 | RISK_OFF | false | missed_winner | -2.73 | 2.73 | -0.11 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `SOLUSDT` | 2026-07-18 20:05 | RISK_OFF | false | missed_winner | -2.73 | 2.73 | -0.11 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `SOLUSDT` | 2026-07-18 20:05 | RISK_OFF | false | missed_winner | -2.73 | 2.73 | -0.11 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `XRPUSDT` | 2026-07-18 20:05 | RISK_OFF | false | missed_winner | -3.31 | 3.31 | 0.43 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `XRPUSDT` | 2026-07-18 20:05 | RISK_OFF | false | missed_winner | -3.31 | 3.31 | 0.43 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `XRPUSDT` | 2026-07-18 20:05 | RISK_OFF | false | missed_winner | -3.31 | 3.31 | 0.43 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `XRPUSDT` | 2026-07-18 20:05 | RISK_OFF | false | missed_winner | -3.31 | 3.31 | 0.43 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ZECUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_loser | -1.00 | 0.39 | -2.28 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_loser | -1.00 | 0.39 | -2.28 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-18 20:05 | RISK_OFF | false | filtered_loser | 1.00 | 0.39 | -2.28 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_loser | -1.00 | 0.39 | -2.28 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BANKUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.24 | -0.27 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BANKUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.24 | -0.27 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BANKUSDT` | 2026-07-19 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 1.24 | -0.27 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BANKUSDT` | 2026-07-19 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 1.24 | -0.27 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BTCUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.73 | -0.18 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.73 | -0.18 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-19 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.73 | -0.18 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-19 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.73 | -0.18 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ETHUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.78 | -0.15 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.78 | -0.15 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-19 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.78 | -0.15 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-19 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.78 | -0.15 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `SOLUSDT` | 2026-07-19 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.60 | -0.62 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `SOLUSDT` | 2026-07-19 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.60 | -0.62 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `SOLUSDT` | 2026-07-19 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.60 | -0.62 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `SOLUSDT` | 2026-07-19 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.60 | -0.62 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ZECUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_loser | -1.00 | -0.15 | -1.99 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_loser | -1.00 | -0.15 | -1.99 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-19 20:05 | RISK_OFF | false | filtered_loser | 1.00 | -0.15 | -1.99 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_loser | -1.00 | -0.15 | -1.99 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BANKUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.33 | -0.61 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BANKUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.33 | -0.61 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BANKUSDT` | 2026-07-20 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.33 | -0.61 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BANKUSDT` | 2026-07-20 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.33 | -0.61 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BTCUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.67 | -0.32 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.67 | -0.32 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.67 | -0.32 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-20 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.67 | -0.32 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ETHUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.75 | -0.30 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.75 | -0.30 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-20 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.75 | -0.30 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.75 | -0.30 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `SOLUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.41 | -0.89 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.41 | -0.89 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-20 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.41 | -0.89 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-20 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.41 | -0.89 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `XRPUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.25 | -0.44 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `XRPUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.25 | -0.44 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `XRPUSDT` | 2026-07-20 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 1.25 | -0.44 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `XRPUSDT` | 2026-07-20 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 1.25 | -0.44 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BANKUSDT` | 2026-07-21 20:06 | RISK_OFF | false | missed_winner | -2.55 | 2.55 | 0.02 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BANKUSDT` | 2026-07-21 20:06 | RISK_OFF | false | missed_winner | -2.55 | 2.55 | 0.02 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BANKUSDT` | 2026-07-21 20:06 | RISK_OFF | false | missed_winner | -2.55 | 2.55 | 0.02 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BANKUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_winner_path | 2.55 | 2.55 | 0.02 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BTCUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.26 | -0.47 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.26 | -0.47 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-21 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.26 | -0.47 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-21 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.26 | -0.47 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ETHUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.32 | -0.57 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.32 | -0.57 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.32 | -0.57 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.32 | -0.57 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `SOLUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.16 | -0.98 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.16 | -0.98 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.16 | -0.98 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.16 | -0.98 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BANKUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_winner_path | 2.62 | 2.62 | 1.10 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BANKUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_winner_path | 2.62 | 2.62 | 1.10 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BANKUSDT` | 2026-07-22 20:05 | NEUTRAL | false | missed_winner | -2.62 | 2.62 | 1.10 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BANKUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_winner_path | 2.62 | 2.62 | 1.10 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BTCUSDT` | 2026-07-22 20:05 | NEUTRAL | false | filtered_right_censored | n/a | 0.00 | -0.53 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.00 | -0.53 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.00 | -0.53 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-22 20:05 | NEUTRAL | false | filtered_right_censored | n/a | 0.00 | -0.53 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ETHUSDT` | 2026-07-22 20:05 | NEUTRAL | false | filtered_right_censored | n/a | 0.09 | -0.63 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-22 20:05 | NEUTRAL | false | filtered_right_censored | n/a | 0.09 | -0.63 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.09 | -0.63 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-22 20:05 | NEUTRAL | false | filtered_right_censored | n/a | 0.09 | -0.63 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `SOLUSDT` | 2026-07-22 20:05 | NEUTRAL | false | filtered_loser | 1.00 | 0.08 | -1.13 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-22 20:05 | NEUTRAL | false | filtered_loser | 1.00 | 0.08 | -1.13 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_loser | -1.00 | 0.08 | -1.13 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-22 20:05 | NEUTRAL | false | filtered_loser | 1.00 | 0.08 | -1.13 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `XRPUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.10 | -0.69 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `XRPUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.10 | -0.69 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `XRPUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.10 | -0.69 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `XRPUSDT` | 2026-07-22 20:05 | NEUTRAL | false | filtered_right_censored | n/a | 0.10 | -0.69 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BANKUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.94 | 0.23 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BANKUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.94 | 0.23 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BANKUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.94 | 0.23 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BANKUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.94 | 0.23 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BTCUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | 0.07 | -1.05 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | 0.07 | -1.05 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | 0.07 | -1.05 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | 0.07 | -1.05 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ETHUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | -0.51 | -1.08 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | -0.51 | -1.08 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | -0.51 | -1.08 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | -0.51 | -1.08 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `SOLUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | -0.89 | -1.99 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | -0.89 | -1.99 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | -0.89 | -1.99 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | -0.89 | -1.99 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `XRPUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | -0.50 | -1.08 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `XRPUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | -0.50 | -1.08 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `XRPUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | -0.50 | -1.08 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `XRPUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | -0.50 | -1.08 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BANKUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.43 | 0.24 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BANKUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.43 | 0.24 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BANKUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.43 | 0.24 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BANKUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.43 | 0.24 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BNBUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.06 | -0.14 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BNBUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | -0.06 | -0.14 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BNBUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.06 | -0.14 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BNBUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | -0.06 | -0.14 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BTCUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.59 | -0.76 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | -0.59 | -0.76 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.59 | -0.76 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | -0.59 | -0.76 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ETHUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.28 | -0.46 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.28 | -0.46 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.28 | -0.46 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | -0.28 | -0.46 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `VANAUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.07 | -0.86 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `VANAUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.07 | -0.86 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `VANAUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.07 | -0.86 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `VANAUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.07 | -0.86 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BANKUSDT` | 2026-07-25 20:05 | NEUTRAL | true | accepted_neutral | n/a | n/a | n/a | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BANKUSDT` | 2026-07-25 20:05 | NEUTRAL | true | accepted_neutral | n/a | n/a | n/a | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BANKUSDT` | 2026-07-25 20:05 | NEUTRAL | true | accepted_neutral | n/a | n/a | n/a | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BANKUSDT` | 2026-07-25 20:05 | NEUTRAL | true | accepted_neutral | n/a | n/a | n/a | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `BNBUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `BNBUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `BNBUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `BNBUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `BTCUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `BTCUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `BTCUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `BTCUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ETHUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-25 20:05 | NEUTRAL | true | accepted_neutral | n/a | n/a | n/a | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-25 20:05 | NEUTRAL | true | accepted_neutral | n/a | n/a | n/a | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `XRPUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `XRPUSDT` | 2026-07-25 20:05 | NEUTRAL | true | accepted_neutral | n/a | n/a | n/a | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `XRPUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `XRPUSDT` | 2026-07-25 20:05 | NEUTRAL | true | accepted_neutral | n/a | n/a | n/a | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |

## Raw Summary

```json
{
  "experiment": "momentum_pullback_definition_ab",
  "opportunity_set_hash": "9468fbe1bab35767",
  "opportunities": 95,
  "summary": [
    {
      "variant": "allow_minor_24h_pullback",
      "opportunities": 95,
      "accepted": 71,
      "filtered": 24,
      "accepted_loser": 14,
      "accepted_winner_path": 13,
      "filtered_loser": 8,
      "missed_winner": 6,
      "total_decision_R": 12.653142748358759,
      "outcomes": {
        "filtered_loser": 8,
        "accepted_neutral": 26,
        "filtered_neutral": 6,
        "accepted_loser": 14,
        "accepted_winner_path": 13,
        "missed_winner": 6,
        "filtered_right_censored": 4,
        "accepted_right_censored": 18
      }
    },
    {
      "variant": "current_24h_7d_positive",
      "opportunities": 95,
      "accepted": 53,
      "filtered": 42,
      "accepted_loser": 10,
      "accepted_winner_path": 8,
      "filtered_loser": 12,
      "missed_winner": 11,
      "total_decision_R": -15.290554385006416,
      "outcomes": {
        "filtered_loser": 12,
        "accepted_neutral": 20,
        "filtered_neutral": 12,
        "accepted_loser": 10,
        "missed_winner": 11,
        "accepted_winner_path": 8,
        "filtered_right_censored": 7,
        "accepted_right_censored": 15
      }
    },
    {
      "variant": "recent_high_atr_pullback",
      "opportunities": 95,
      "accepted": 44,
      "filtered": 51,
      "accepted_loser": 13,
      "accepted_winner_path": 5,
      "filtered_loser": 9,
      "missed_winner": 14,
      "total_decision_R": -39.66463049739776,
      "outcomes": {
        "filtered_loser": 9,
        "filtered_neutral": 15,
        "accepted_neutral": 17,
        "accepted_loser": 13,
        "missed_winner": 14,
        "accepted_winner_path": 5,
        "filtered_right_censored": 13,
        "accepted_right_censored": 9
      }
    },
    {
      "variant": "trend_support_atr_pullback",
      "opportunities": 95,
      "accepted": 47,
      "filtered": 48,
      "accepted_loser": 14,
      "accepted_winner_path": 15,
      "filtered_loser": 8,
      "missed_winner": 4,
      "total_decision_R": 25.794661237484874,
      "outcomes": {
        "filtered_loser": 8,
        "filtered_neutral": 23,
        "accepted_neutral": 9,
        "accepted_loser": 14,
        "accepted_winner_path": 15,
        "missed_winner": 4,
        "filtered_right_censored": 13,
        "accepted_right_censored": 9
      }
    }
  ]
}
```
