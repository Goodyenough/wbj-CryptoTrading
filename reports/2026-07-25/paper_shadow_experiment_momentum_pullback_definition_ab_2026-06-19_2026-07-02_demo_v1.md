---
created: 2026-07-25 23:52:42 CST
tags:
  - crypto
  - trading-system
  - shadow-experiment
account: demo
start_date: 2026-06-19
end_date: 2026-07-02
experiment: momentum_pullback_definition_ab
report_version: v1
opportunity_set_hash: 6e1f8adbd43f8f1f
---

# Paper Shadow Experiment momentum_pullback_definition_ab 2026-06-19 -> 2026-07-02 demo v1

This is an offline diagnostic experiment. It uses a fixed opportunity set and does not modify settings, plans, events, snapshots, or paper state.

## Decision

- verdict: retest
- opportunity_set_hash: 6e1f8adbd43f8f1f
- opportunity_set_path: `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-07-25\paper_shadow_opportunity_set_2026-06-19_2026-07-02_demo_6e1f8adbd43f8f1f_v1.json`
- config_action: do_not_modify_settings_toml

## Variant Summary

| Variant | Opportunities | Accepted | Filtered | Accepted Loser | Accepted Winner Path | Filtered Loser | Missed Winner | Total Decision R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| allow_minor_24h_pullback | 71 | 33 | 38 | 12 | 3 | 13 | 9 | -25.02 |
| current_24h_7d_positive | 71 | 29 | 42 | 8 | 3 | 17 | 9 | -17.02 |
| recent_high_atr_pullback | 71 | 23 | 48 | 5 | 4 | 20 | 8 | -0.27 |
| trend_support_atr_pullback | 71 | 31 | 40 | 11 | 5 | 14 | 7 | 3.33 |

## Outcome Counts

### allow_minor_24h_pullback

| Outcome | Count |
|---|---:|
| accepted_loser | 12 |
| accepted_neutral | 3 |
| accepted_right_censored | 15 |
| accepted_winner_path | 3 |
| filtered_loser | 13 |
| filtered_neutral | 4 |
| filtered_right_censored | 12 |
| missed_winner | 9 |

### current_24h_7d_positive

| Outcome | Count |
|---|---:|
| accepted_loser | 8 |
| accepted_neutral | 3 |
| accepted_right_censored | 15 |
| accepted_winner_path | 3 |
| filtered_loser | 17 |
| filtered_neutral | 4 |
| filtered_right_censored | 12 |
| missed_winner | 9 |

### recent_high_atr_pullback

| Outcome | Count |
|---|---:|
| accepted_loser | 5 |
| accepted_neutral | 2 |
| accepted_right_censored | 12 |
| accepted_winner_path | 4 |
| filtered_loser | 20 |
| filtered_neutral | 5 |
| filtered_right_censored | 15 |
| missed_winner | 8 |

### trend_support_atr_pullback

| Outcome | Count |
|---|---:|
| accepted_loser | 11 |
| accepted_neutral | 2 |
| accepted_right_censored | 13 |
| accepted_winner_path | 5 |
| filtered_loser | 14 |
| filtered_neutral | 5 |
| filtered_right_censored | 14 |
| missed_winner | 7 |

## Detail Rows

| Variant | Source | Symbol | Time | Regime | Accepted | Outcome | PnL_R | MFE_R | MAE_R | Reason |
|---|---|---|---|---|---|---|---:|---:|---:|---|
| current_24h_7d_positive | RECLAIM_PENDING | `ONDOUSDT` | 2026-06-19 00:10 | n/a | false | filtered_loser | 1.00 | -0.64 | -1.52 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | RECLAIM_PENDING | `ONDOUSDT` | 2026-06-19 00:10 | n/a | false | filtered_loser | 1.00 | -0.64 | -1.52 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | RECLAIM_PENDING | `ONDOUSDT` | 2026-06-19 00:10 | n/a | false | filtered_loser | 1.00 | -0.64 | -1.52 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | RECLAIM_PENDING | `ONDOUSDT` | 2026-06-19 00:10 | n/a | false | filtered_loser | 1.00 | -0.64 | -1.52 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `ETHUSDT` | 2026-06-19 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 1.63 | -3.21 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `ETHUSDT` | 2026-06-19 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 1.63 | -3.21 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `ETHUSDT` | 2026-06-19 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 1.63 | -3.21 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `ETHUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.63 | -3.21 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `SOLUSDT` | 2026-06-19 20:06 | RISK_OFF | false | missed_winner | -7.05 | 7.05 | -1.22 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `SOLUSDT` | 2026-06-19 20:06 | RISK_OFF | false | missed_winner | -7.05 | 7.05 | -1.22 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `SOLUSDT` | 2026-06-19 20:06 | RISK_OFF | false | missed_winner | -7.05 | 7.05 | -1.22 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `SOLUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_winner_path | 7.05 | 7.05 | -1.22 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `WLDUSDT` | 2026-06-19 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.82 | -5.49 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `WLDUSDT` | 2026-06-19 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.82 | -5.49 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `WLDUSDT` | 2026-06-19 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.82 | -5.49 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `WLDUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.82 | -5.49 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `XLMUSDT` | 2026-06-19 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.09 | -3.41 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `XLMUSDT` | 2026-06-19 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.09 | -3.41 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `XLMUSDT` | 2026-06-19 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.09 | -3.41 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `XLMUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.09 | -3.41 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `XPLUSDT` | 2026-06-19 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.73 | -0.91 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `XPLUSDT` | 2026-06-19 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.73 | -0.91 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `XPLUSDT` | 2026-06-19 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.73 | -0.91 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `XPLUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.73 | -0.91 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ETHUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.39 | -2.17 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ETHUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.39 | -2.17 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-06-20 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.39 | -2.17 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.39 | -2.17 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `SOLUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.99 | -1.15 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `SOLUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.99 | -1.15 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-06-20 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 1.99 | -1.15 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.99 | -1.15 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `TRXUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.21 | -0.81 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `TRXUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.21 | -0.81 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `TRXUSDT` | 2026-06-20 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.21 | -0.81 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `TRXUSDT` | 2026-06-20 20:06 | RISK_OFF | false | filtered_neutral | n/a | 1.21 | -0.81 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `WLDUSDT` | 2026-06-20 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.94 | -6.12 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `WLDUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.94 | -6.12 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `WLDUSDT` | 2026-06-20 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.94 | -6.12 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `WLDUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.94 | -6.12 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ZECUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | -0.03 | -2.47 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ZECUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | -0.03 | -2.47 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ZECUSDT` | 2026-06-20 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.03 | -2.47 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ZECUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | -0.03 | -2.47 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BICOUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.28 | -1.16 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BICOUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.28 | -1.16 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BICOUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.28 | -1.16 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BICOUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.28 | -1.16 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ETHUSDT` | 2026-06-21 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 2.20 | -3.69 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ETHUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 2.20 | -3.69 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-06-21 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 2.20 | -3.69 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 2.20 | -3.69 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `NEARUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_loser | -1.00 | -0.28 | -2.53 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `NEARUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_loser | -1.00 | -0.28 | -2.53 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `NEARUSDT` | 2026-06-21 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.28 | -2.53 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `NEARUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_loser | -1.00 | -0.28 | -2.53 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `SOLUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.54 | -1.13 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `SOLUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.54 | -1.13 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.54 | -1.13 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-06-21 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 1.54 | -1.13 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `TRXUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.78 | -0.85 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `TRXUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.78 | -0.85 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `TRXUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.78 | -0.85 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `TRXUSDT` | 2026-06-21 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.78 | -0.85 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BTCUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.03 | -2.35 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BTCUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.03 | -2.35 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.03 | -2.35 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.03 | -2.35 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ETHUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.37 | -2.18 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ETHUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.37 | -2.18 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_loser | -1.00 | -0.37 | -2.18 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.37 | -2.18 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `SOLUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.41 | -1.24 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `SOLUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.41 | -1.24 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.41 | -1.24 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 1.41 | -1.24 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `SYNUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_winner_path | 2.88 | 2.88 | 0.01 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `SYNUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_winner_path | 2.88 | 2.88 | 0.01 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `SYNUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_winner_path | 2.88 | 2.88 | 0.01 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `SYNUSDT` | 2026-06-22 20:06 | RISK_OFF | false | missed_winner | -2.88 | 2.88 | 0.01 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `WLDUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_loser | -1.00 | -0.07 | -5.62 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `WLDUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_loser | -1.00 | -0.07 | -5.62 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `WLDUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.07 | -5.62 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `WLDUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_loser | -1.00 | -0.07 | -5.62 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `BTCUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_loser | 1.00 | 0.31 | -2.80 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `BTCUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_loser | 1.00 | 0.31 | -2.80 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `BTCUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_loser | 1.00 | 0.31 | -2.80 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `BTCUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_loser | 1.00 | 0.31 | -2.80 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `SUIUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_neutral | n/a | 1.03 | -0.73 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `SUIUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_neutral | n/a | 1.03 | -0.73 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `SUIUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_neutral | n/a | 1.03 | -0.73 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `SUIUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_neutral | n/a | 1.03 | -0.73 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `SYNUSDT` | 2026-06-23 20:07 | RISK_OFF | false | missed_winner | -4.80 | 4.80 | 0.59 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `SYNUSDT` | 2026-06-23 20:07 | RISK_OFF | false | missed_winner | -4.80 | 4.80 | 0.59 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `SYNUSDT` | 2026-06-23 20:07 | RISK_OFF | true | accepted_winner_path | 4.80 | 4.80 | 0.59 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `SYNUSDT` | 2026-06-23 20:07 | RISK_OFF | true | accepted_winner_path | 4.80 | 4.80 | 0.59 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `TRXUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_loser | 1.00 | 0.13 | -1.35 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `TRXUSDT` | 2026-06-23 20:07 | RISK_OFF | true | accepted_loser | -1.00 | 0.13 | -1.35 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `TRXUSDT` | 2026-06-23 20:07 | RISK_OFF | true | accepted_loser | -1.00 | 0.13 | -1.35 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `TRXUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_loser | 1.00 | 0.13 | -1.35 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `WLDUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.66 | -4.97 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `WLDUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.66 | -4.97 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `WLDUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.66 | -4.97 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `WLDUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.66 | -4.97 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `BNBUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.36 | -2.46 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `BNBUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.36 | -2.46 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `BNBUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.36 | -2.46 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `BNBUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.36 | -2.46 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `BTCUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.38 | -2.81 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `BTCUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.38 | -2.81 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `BTCUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.38 | -2.81 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `BTCUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.38 | -2.81 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `ETHUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 1.05 | -2.52 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `ETHUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 1.05 | -2.52 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `ETHUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 1.05 | -2.52 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `ETHUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 1.05 | -2.52 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `SOLUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 6.90 | -1.52 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `SOLUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 6.90 | -1.52 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `SOLUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 6.90 | -1.52 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `SOLUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 6.90 | -1.52 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `XRPUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.03 | -2.60 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `XRPUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.03 | -2.60 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `XRPUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.03 | -2.60 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `XRPUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.03 | -2.60 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `AAVEUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_neutral | n/a | 1.26 | -0.06 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `AAVEUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_neutral | n/a | 1.26 | -0.06 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `AAVEUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_neutral | n/a | 1.26 | -0.06 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `AAVEUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_neutral | n/a | 1.26 | -0.06 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `BTCUSDT` | 2026-06-25 20:08 | RISK_OFF | false | filtered_neutral | n/a | 1.17 | -0.89 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `BTCUSDT` | 2026-06-25 20:08 | RISK_OFF | false | filtered_neutral | n/a | 1.17 | -0.89 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `BTCUSDT` | 2026-06-25 20:08 | RISK_OFF | false | filtered_neutral | n/a | 1.17 | -0.89 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `BTCUSDT` | 2026-06-25 20:08 | RISK_OFF | false | filtered_neutral | n/a | 1.17 | -0.89 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `SYNUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_winner_path | 1.92 | 1.92 | -0.57 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `SYNUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_winner_path | 1.92 | 1.92 | -0.57 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `SYNUSDT` | 2026-06-25 20:08 | RISK_OFF | false | missed_winner | -1.92 | 1.92 | -0.57 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `SYNUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_winner_path | 1.92 | 1.92 | -0.57 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `TRXUSDT` | 2026-06-25 20:08 | RISK_OFF | false | filtered_loser | 1.00 | -0.57 | -1.55 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `TRXUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_loser | -1.00 | -0.57 | -1.55 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `TRXUSDT` | 2026-06-25 20:08 | RISK_OFF | false | filtered_loser | 1.00 | -0.57 | -1.55 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `TRXUSDT` | 2026-06-25 20:08 | RISK_OFF | false | filtered_loser | 1.00 | -0.57 | -1.55 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `XPLUSDT` | 2026-06-25 20:08 | RISK_OFF | false | filtered_neutral | n/a | 1.26 | -0.56 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `XPLUSDT` | 2026-06-25 20:08 | RISK_OFF | false | filtered_neutral | n/a | 1.26 | -0.56 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `XPLUSDT` | 2026-06-25 20:08 | RISK_OFF | false | filtered_neutral | n/a | 1.26 | -0.56 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `XPLUSDT` | 2026-06-25 20:08 | RISK_OFF | false | filtered_neutral | n/a | 1.26 | -0.56 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `AAVEUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.76 | -0.14 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `AAVEUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.76 | -0.14 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `AAVEUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.76 | -0.14 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `AAVEUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.76 | -0.14 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `HEIUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.09 | -0.55 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `HEIUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.09 | -0.55 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `HEIUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.09 | -0.55 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `HEIUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.09 | -0.55 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `SOLUSDT` | 2026-06-26 20:06 | RISK_OFF | false | missed_winner | -2.75 | 2.75 | 0.44 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `SOLUSDT` | 2026-06-26 20:06 | RISK_OFF | false | missed_winner | -2.75 | 2.75 | 0.44 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-06-26 20:06 | RISK_OFF | false | missed_winner | -2.75 | 2.75 | 0.44 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-06-26 20:06 | RISK_OFF | false | missed_winner | -2.75 | 2.75 | 0.44 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `SYNUSDT` | 2026-06-26 20:06 | RISK_OFF | false | missed_winner | -4.21 | 4.21 | -0.43 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `SYNUSDT` | 2026-06-26 20:06 | RISK_OFF | false | missed_winner | -4.21 | 4.21 | -0.43 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `SYNUSDT` | 2026-06-26 20:06 | RISK_OFF | false | missed_winner | -4.21 | 4.21 | -0.43 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `SYNUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_winner_path | 4.21 | 4.21 | -0.43 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `XPLUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.39 | -0.76 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `XPLUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.39 | -0.76 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `XPLUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.39 | -0.76 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `XPLUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.39 | -0.76 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `AAVEUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.06 | -0.45 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `AAVEUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.06 | -0.45 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `AAVEUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.06 | -0.45 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `AAVEUSDT` | 2026-06-27 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.06 | -0.45 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `BNBUSDT` | 2026-06-27 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.07 | -0.64 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `BNBUSDT` | 2026-06-27 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.07 | -0.64 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `BNBUSDT` | 2026-06-27 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.07 | -0.64 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `BNBUSDT` | 2026-06-27 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.07 | -0.64 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `BTCUSDT` | 2026-06-27 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 1.65 | -0.31 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `BTCUSDT` | 2026-06-27 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 1.65 | -0.31 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `BTCUSDT` | 2026-06-27 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 1.65 | -0.31 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `BTCUSDT` | 2026-06-27 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 1.65 | -0.31 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `SOLUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.16 | -0.17 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `SOLUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.16 | -0.17 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.16 | -0.17 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.16 | -0.17 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `XRPUSDT` | 2026-06-27 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.70 | -0.32 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `XRPUSDT` | 2026-06-27 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.70 | -0.32 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `XRPUSDT` | 2026-06-27 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.70 | -0.32 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `XRPUSDT` | 2026-06-27 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.70 | -0.32 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BTCUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 2.05 | -0.32 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BTCUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 2.05 | -0.32 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 2.05 | -0.32 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 2.05 | -0.32 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `ETHUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 1.41 | -0.14 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `ETHUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 1.41 | -0.14 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `ETHUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 1.41 | -0.14 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `ETHUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 1.41 | -0.14 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `NEARUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.77 | -0.55 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `NEARUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.77 | -0.55 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `NEARUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.77 | -0.55 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `NEARUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.77 | -0.55 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `SOLUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 1.39 | -0.18 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `SOLUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 1.39 | -0.18 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-06-28 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.39 | -0.18 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 1.39 | -0.18 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `XRPUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.85 | -0.26 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `XRPUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.85 | -0.26 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `XRPUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.85 | -0.26 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `XRPUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.85 | -0.26 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ACTUSDT` | 2026-06-29 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.60 | -0.51 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ACTUSDT` | 2026-06-29 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.60 | -0.51 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ACTUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.60 | -0.51 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ACTUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.60 | -0.51 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `BTCUSDT` | 2026-06-29 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.36 | -0.86 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `BTCUSDT` | 2026-06-29 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.36 | -0.86 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-06-29 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.36 | -0.86 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `BTCUSDT` | 2026-06-29 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.36 | -0.86 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `ETHUSDT` | 2026-06-29 20:06 | RISK_OFF | false | missed_winner | -3.53 | 3.53 | 0.04 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `ETHUSDT` | 2026-06-29 20:06 | RISK_OFF | false | missed_winner | -3.53 | 3.53 | 0.04 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `ETHUSDT` | 2026-06-29 20:06 | RISK_OFF | false | missed_winner | -3.53 | 3.53 | 0.04 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `ETHUSDT` | 2026-06-29 20:06 | RISK_OFF | false | missed_winner | -3.53 | 3.53 | 0.04 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `SOLUSDT` | 2026-06-29 20:06 | RISK_OFF | false | missed_winner | -2.49 | 2.49 | 0.13 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `SOLUSDT` | 2026-06-29 20:06 | RISK_OFF | false | missed_winner | -2.49 | 2.49 | 0.13 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_winner_path | 2.49 | 2.49 | 0.13 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-06-29 20:06 | RISK_OFF | false | missed_winner | -2.49 | 2.49 | 0.13 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `XRPUSDT` | 2026-06-29 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.71 | -0.62 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `XRPUSDT` | 2026-06-29 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.71 | -0.62 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `XRPUSDT` | 2026-06-29 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.71 | -0.62 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `XRPUSDT` | 2026-06-29 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.71 | -0.62 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `ETHUSDT` | 2026-06-30 20:06 | RISK_OFF | false | missed_winner | -3.25 | 3.25 | 0.09 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `ETHUSDT` | 2026-06-30 20:06 | RISK_OFF | false | missed_winner | -3.25 | 3.25 | 0.09 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `ETHUSDT` | 2026-06-30 20:06 | RISK_OFF | false | missed_winner | -3.25 | 3.25 | 0.09 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `ETHUSDT` | 2026-06-30 20:06 | RISK_OFF | false | missed_winner | -3.25 | 3.25 | 0.09 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `SOLUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 1.90 | 1.90 | 0.06 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `SOLUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 1.90 | 1.90 | 0.06 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 1.90 | 1.90 | 0.06 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 1.90 | 1.90 | 0.06 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `SYNUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.02 | -0.45 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `SYNUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.02 | -0.45 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `SYNUSDT` | 2026-06-30 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.02 | -0.45 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `SYNUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.02 | -0.45 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `XRPUSDT` | 2026-06-30 20:06 | RISK_OFF | false | missed_winner | -2.25 | 2.25 | -0.08 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `XRPUSDT` | 2026-06-30 20:06 | RISK_OFF | false | missed_winner | -2.25 | 2.25 | -0.08 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `XRPUSDT` | 2026-06-30 20:06 | RISK_OFF | false | missed_winner | -2.25 | 2.25 | -0.08 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `XRPUSDT` | 2026-06-30 20:06 | RISK_OFF | false | missed_winner | -2.25 | 2.25 | -0.08 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | REJECT | `ZECUSDT` | 2026-06-30 20:06 | RISK_OFF | false | missed_winner | -2.39 | 2.39 | 0.23 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | REJECT | `ZECUSDT` | 2026-06-30 20:06 | RISK_OFF | false | missed_winner | -2.39 | 2.39 | 0.23 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | REJECT | `ZECUSDT` | 2026-06-30 20:06 | RISK_OFF | false | missed_winner | -2.39 | 2.39 | 0.23 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | REJECT | `ZECUSDT` | 2026-06-30 20:06 | RISK_OFF | false | missed_winner | -2.39 | 2.39 | 0.23 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ADAUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.80 | 0.19 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ADAUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.80 | 0.19 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ADAUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.80 | 0.19 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ADAUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.80 | 0.19 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `CELOUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.34 | -0.40 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `CELOUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.34 | -0.40 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `CELOUSDT` | 2026-07-01 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.34 | -0.40 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `CELOUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.34 | -0.40 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `SOLUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.24 | 0.36 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.24 | 0.36 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.24 | 0.36 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.24 | 0.36 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `SYNUSDT` | 2026-07-01 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.73 | -0.23 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `SYNUSDT` | 2026-07-01 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.73 | -0.23 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `SYNUSDT` | 2026-07-01 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.73 | -0.23 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `SYNUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.73 | -0.23 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `XLMUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.17 | -0.04 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `XLMUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.17 | -0.04 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `XLMUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.17 | -0.04 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `XLMUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.17 | -0.04 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ADAUSDT` | 2026-07-02 20:06 | RISK_OFF | true | accepted_right_censored | n/a | -0.03 | -0.03 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ADAUSDT` | 2026-07-02 20:06 | RISK_OFF | true | accepted_right_censored | n/a | -0.03 | -0.03 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ADAUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.03 | -0.03 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ADAUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.03 | -0.03 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ETHUSDT` | 2026-07-02 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.61 | 0.61 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-02 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.61 | 0.61 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-02 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.61 | 0.61 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ETHUSDT` | 2026-07-02 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.61 | 0.61 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `NEARUSDT` | 2026-07-02 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.02 | 0.02 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `NEARUSDT` | 2026-07-02 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.02 | 0.02 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `NEARUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.02 | 0.02 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `NEARUSDT` | 2026-07-02 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.02 | 0.02 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `SOLUSDT` | 2026-07-02 20:06 | RISK_OFF | true | accepted_right_censored | n/a | -0.09 | -0.09 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-02 20:06 | RISK_OFF | true | accepted_right_censored | n/a | -0.09 | -0.09 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.09 | -0.09 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `SOLUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.09 | -0.09 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
| current_24h_7d_positive | WATCH_ONLY | `ZECUSDT` | 2026-07-02 20:06 | RISK_OFF | true | accepted_right_censored | n/a | -0.17 | -0.17 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-02 20:06 | RISK_OFF | true | accepted_right_censored | n/a | -0.17 | -0.17 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-02 20:06 | RISK_OFF | true | accepted_right_censored | n/a | -0.17 | -0.17 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | WATCH_ONLY | `ZECUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.17 | -0.17 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |

## Raw Summary

```json
{
  "experiment": "momentum_pullback_definition_ab",
  "opportunity_set_hash": "6e1f8adbd43f8f1f",
  "opportunities": 71,
  "summary": [
    {
      "variant": "allow_minor_24h_pullback",
      "opportunities": 71,
      "accepted": 33,
      "filtered": 38,
      "accepted_loser": 12,
      "accepted_winner_path": 3,
      "filtered_loser": 13,
      "missed_winner": 9,
      "total_decision_R": -25.016094296782267,
      "outcomes": {
        "filtered_loser": 13,
        "missed_winner": 9,
        "filtered_neutral": 4,
        "accepted_loser": 12,
        "accepted_neutral": 3,
        "accepted_winner_path": 3,
        "accepted_right_censored": 15,
        "filtered_right_censored": 12
      }
    },
    {
      "variant": "current_24h_7d_positive",
      "opportunities": 71,
      "accepted": 29,
      "filtered": 42,
      "accepted_loser": 8,
      "accepted_winner_path": 3,
      "filtered_loser": 17,
      "missed_winner": 9,
      "total_decision_R": -17.016094296782267,
      "outcomes": {
        "filtered_loser": 17,
        "missed_winner": 9,
        "filtered_neutral": 4,
        "accepted_loser": 8,
        "accepted_neutral": 3,
        "accepted_winner_path": 3,
        "accepted_right_censored": 15,
        "filtered_right_censored": 12
      }
    },
    {
      "variant": "recent_high_atr_pullback",
      "opportunities": 71,
      "accepted": 23,
      "filtered": 48,
      "accepted_loser": 5,
      "accepted_winner_path": 4,
      "filtered_loser": 20,
      "missed_winner": 8,
      "total_decision_R": -0.26874394727505924,
      "outcomes": {
        "filtered_loser": 20,
        "missed_winner": 8,
        "filtered_neutral": 5,
        "accepted_loser": 5,
        "accepted_neutral": 2,
        "accepted_winner_path": 4,
        "accepted_right_censored": 12,
        "filtered_right_censored": 15
      }
    },
    {
      "variant": "trend_support_atr_pullback",
      "opportunities": 71,
      "accepted": 31,
      "filtered": 40,
      "accepted_loser": 11,
      "accepted_winner_path": 5,
      "filtered_loser": 14,
      "missed_winner": 7,
      "total_decision_R": 3.3271423724366986,
      "outcomes": {
        "filtered_loser": 14,
        "accepted_loser": 11,
        "accepted_winner_path": 5,
        "accepted_neutral": 2,
        "filtered_neutral": 5,
        "missed_winner": 7,
        "accepted_right_censored": 13,
        "filtered_right_censored": 14
      }
    }
  ]
}
```
