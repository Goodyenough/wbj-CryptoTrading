---
created: 2026-07-25 23:54:22 CST
tags:
  - crypto
  - trading-system
  - shadow-experiment
account: demo
start_date: 2026-07-17
end_date: 2026-07-25
experiment: momentum_pullback_definition_ab
report_version: v1
opportunity_set_hash: d958282222b977b7
---

# Paper Shadow Experiment momentum_pullback_definition_ab 2026-07-17 -> 2026-07-25 demo v1

This is an offline diagnostic experiment. It uses a fixed opportunity set and does not modify settings, plans, events, snapshots, or paper state.

## Decision

- verdict: retest
- opportunity_set_hash: d958282222b977b7
- opportunity_set_path: `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-07-25\paper_shadow_opportunity_set_2026-07-17_2026-07-25_demo_d958282222b977b7_v1.json`
- config_action: do_not_modify_settings_toml

## Variant Summary

| Variant | Opportunities | Accepted | Filtered | Accepted Loser | Accepted Winner Path | Filtered Loser | Missed Winner | Total Decision R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| allow_minor_24h_pullback | 43 | 30 | 13 | 7 | 1 | 1 | 5 | -16.57 |
| current_24h_7d_positive | 43 | 22 | 21 | 4 | 1 | 4 | 5 | -10.57 |
| recent_high_atr_pullback | 43 | 15 | 28 | 4 | 0 | 4 | 6 | -15.81 |
| trend_support_atr_pullback | 43 | 23 | 20 | 7 | 3 | 1 | 3 | -7.41 |

## Outcome Counts

### allow_minor_24h_pullback

| Outcome | Count |
|---|---:|
| accepted_loser | 7 |
| accepted_neutral | 4 |
| accepted_right_censored | 18 |
| accepted_winner_path | 1 |
| filtered_loser | 1 |
| filtered_neutral | 3 |
| filtered_right_censored | 4 |
| missed_winner | 5 |

### current_24h_7d_positive

| Outcome | Count |
|---|---:|
| accepted_loser | 4 |
| accepted_neutral | 2 |
| accepted_right_censored | 15 |
| accepted_winner_path | 1 |
| filtered_loser | 4 |
| filtered_neutral | 5 |
| filtered_right_censored | 7 |
| missed_winner | 5 |

### recent_high_atr_pullback

| Outcome | Count |
|---|---:|
| accepted_loser | 4 |
| accepted_neutral | 2 |
| accepted_right_censored | 9 |
| filtered_loser | 4 |
| filtered_neutral | 5 |
| filtered_right_censored | 13 |
| missed_winner | 6 |

### trend_support_atr_pullback

| Outcome | Count |
|---|---:|
| accepted_loser | 7 |
| accepted_neutral | 4 |
| accepted_right_censored | 9 |
| accepted_winner_path | 3 |
| filtered_loser | 1 |
| filtered_neutral | 3 |
| filtered_right_censored | 13 |
| missed_winner | 3 |

## Detail Rows

| Variant | Source | Symbol | Time | Regime | Accepted | Outcome | PnL_R | MFE_R | MAE_R | Reason |
|---|---|---|---|---|---|---|---:|---:|---:|---|
| current_24h_7d_positive | RECLAIM_PENDING | `ONDOUSDT` | 2026-07-17 00:10 | n/a | false | filtered_neutral | n/a | 0.04 | -0.99 | pct_24h > 0 and pct_7d > 0 |
| allow_minor_24h_pullback | RECLAIM_PENDING | `ONDOUSDT` | 2026-07-17 00:10 | n/a | false | filtered_neutral | n/a | 0.04 | -0.99 | pct_24h >= -2 and pct_7d > 0 |
| recent_high_atr_pullback | RECLAIM_PENDING | `ONDOUSDT` | 2026-07-17 00:10 | n/a | false | filtered_neutral | n/a | 0.04 | -0.99 | recent high pullback is 0.25-2.5 ATR |
| trend_support_atr_pullback | RECLAIM_PENDING | `ONDOUSDT` | 2026-07-17 00:10 | n/a | false | filtered_neutral | n/a | 0.04 | -0.99 | pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR |
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
  "opportunity_set_hash": "d958282222b977b7",
  "opportunities": 43,
  "summary": [
    {
      "variant": "allow_minor_24h_pullback",
      "opportunities": 43,
      "accepted": 30,
      "filtered": 13,
      "accepted_loser": 7,
      "accepted_winner_path": 1,
      "filtered_loser": 1,
      "missed_winner": 5,
      "total_decision_R": -16.570280305594675,
      "outcomes": {
        "filtered_neutral": 3,
        "missed_winner": 5,
        "accepted_neutral": 4,
        "accepted_loser": 7,
        "filtered_right_censored": 4,
        "accepted_right_censored": 18,
        "accepted_winner_path": 1,
        "filtered_loser": 1
      }
    },
    {
      "variant": "current_24h_7d_positive",
      "opportunities": 43,
      "accepted": 22,
      "filtered": 21,
      "accepted_loser": 4,
      "accepted_winner_path": 1,
      "filtered_loser": 4,
      "missed_winner": 5,
      "total_decision_R": -10.570280305594675,
      "outcomes": {
        "filtered_neutral": 5,
        "missed_winner": 5,
        "accepted_neutral": 2,
        "filtered_loser": 4,
        "filtered_right_censored": 7,
        "accepted_loser": 4,
        "accepted_right_censored": 15,
        "accepted_winner_path": 1
      }
    },
    {
      "variant": "recent_high_atr_pullback",
      "opportunities": 43,
      "accepted": 15,
      "filtered": 28,
      "accepted_loser": 4,
      "accepted_winner_path": 0,
      "filtered_loser": 4,
      "missed_winner": 6,
      "total_decision_R": -15.813430849618083,
      "outcomes": {
        "filtered_neutral": 5,
        "missed_winner": 6,
        "accepted_neutral": 2,
        "filtered_loser": 4,
        "filtered_right_censored": 13,
        "accepted_right_censored": 9,
        "accepted_loser": 4
      }
    },
    {
      "variant": "trend_support_atr_pullback",
      "opportunities": 43,
      "accepted": 23,
      "filtered": 20,
      "accepted_loser": 7,
      "accepted_winner_path": 3,
      "filtered_loser": 1,
      "missed_winner": 3,
      "total_decision_R": -7.405785351748097,
      "outcomes": {
        "filtered_neutral": 3,
        "missed_winner": 3,
        "accepted_winner_path": 3,
        "accepted_neutral": 4,
        "accepted_loser": 7,
        "filtered_right_censored": 13,
        "accepted_right_censored": 9,
        "filtered_loser": 1
      }
    }
  ]
}
```
