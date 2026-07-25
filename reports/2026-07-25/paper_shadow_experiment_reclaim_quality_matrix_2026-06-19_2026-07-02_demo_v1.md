---
created: 2026-07-25 23:53:18 CST
tags:
  - crypto
  - trading-system
  - shadow-experiment
account: demo
start_date: 2026-06-19
end_date: 2026-07-02
experiment: reclaim_quality_matrix
report_version: v1
opportunity_set_hash: 6e1f8adbd43f8f1f
---

# Paper Shadow Experiment reclaim_quality_matrix 2026-06-19 -> 2026-07-02 demo v1

This is an offline diagnostic experiment. It uses a fixed opportunity set and does not modify settings, plans, events, snapshots, or paper state.

## Decision

- verdict: retest
- opportunity_set_hash: 6e1f8adbd43f8f1f
- opportunity_set_path: `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-07-25\paper_shadow_opportunity_set_2026-06-19_2026-07-02_demo_6e1f8adbd43f8f1f_v1.json`
- config_action: do_not_modify_settings_toml

## Variant Summary

| Variant | Opportunities | Accepted | Filtered | Accepted Loser | Accepted Winner Path | Filtered Loser | Missed Winner | Total Decision R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| atr_reclaim_0_25 | 71 | 58 | 13 | 16 | 12 | 9 | 0 | 32.42 |
| confirm_1bar | 71 | 36 | 35 | 8 | 11 | 17 | 1 | 43.92 |
| current_4h_close_reclaim | 71 | 61 | 10 | 18 | 12 | 7 | 0 | 28.42 |
| quality_close | 71 | 53 | 18 | 14 | 12 | 11 | 0 | 36.42 |

## Outcome Counts

### atr_reclaim_0_25

| Outcome | Count |
|---|---:|
| accepted_loser | 16 |
| accepted_neutral | 7 |
| accepted_right_censored | 23 |
| accepted_winner_path | 12 |
| filtered_loser | 9 |
| filtered_right_censored | 4 |

### confirm_1bar

| Outcome | Count |
|---|---:|
| accepted_loser | 8 |
| accepted_neutral | 5 |
| accepted_right_censored | 12 |
| accepted_winner_path | 11 |
| filtered_loser | 17 |
| filtered_neutral | 2 |
| filtered_right_censored | 15 |
| missed_winner | 1 |

### current_4h_close_reclaim

| Outcome | Count |
|---|---:|
| accepted_loser | 18 |
| accepted_neutral | 7 |
| accepted_right_censored | 24 |
| accepted_winner_path | 12 |
| filtered_loser | 7 |
| filtered_right_censored | 3 |

### quality_close

| Outcome | Count |
|---|---:|
| accepted_loser | 14 |
| accepted_neutral | 7 |
| accepted_right_censored | 20 |
| accepted_winner_path | 12 |
| filtered_loser | 11 |
| filtered_right_censored | 7 |

## Detail Rows

| Variant | Source | Symbol | Time | Regime | Accepted | Outcome | PnL_R | MFE_R | MAE_R | Reason |
|---|---|---|---|---|---|---|---:|---:|---:|---|
| current_4h_close_reclaim | RECLAIM_PENDING | `ONDOUSDT` | 2026-06-19 00:10 | n/a | false | filtered_loser | 1.00 | -0.64 | -1.52 | first 4h close >= entry_high |
| confirm_1bar | RECLAIM_PENDING | `ONDOUSDT` | 2026-06-19 00:10 | n/a | false | filtered_loser | 1.00 | -0.64 | -1.52 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | RECLAIM_PENDING | `ONDOUSDT` | 2026-06-19 00:10 | n/a | false | filtered_loser | 1.00 | -0.64 | -1.52 | atr_reclaim_0_25 condition not met |
| quality_close | RECLAIM_PENDING | `ONDOUSDT` | 2026-06-19 00:10 | n/a | false | filtered_loser | 1.00 | -0.64 | -1.52 | quality_close condition not met |
| current_4h_close_reclaim | REJECT | `ETHUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.63 | -3.21 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `ETHUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.63 | -3.21 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `ETHUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.63 | -3.21 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `ETHUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.63 | -3.21 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `SOLUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_winner_path | 7.05 | 7.05 | -1.22 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `SOLUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_winner_path | 7.05 | 7.05 | -1.22 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `SOLUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_winner_path | 7.05 | 7.05 | -1.22 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `SOLUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_winner_path | 7.05 | 7.05 | -1.22 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `WLDUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.82 | -5.49 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `WLDUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.82 | -5.49 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `WLDUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.82 | -5.49 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `WLDUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.82 | -5.49 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `XLMUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.09 | -3.41 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `XLMUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.09 | -3.41 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `XLMUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.09 | -3.41 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `XLMUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.09 | -3.41 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `XPLUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.73 | -0.91 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `XPLUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.73 | -0.91 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `XPLUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.73 | -0.91 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `XPLUSDT` | 2026-06-19 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.73 | -0.91 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ETHUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.39 | -2.17 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ETHUSDT` | 2026-06-20 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.39 | -2.17 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ETHUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.39 | -2.17 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ETHUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.39 | -2.17 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `SOLUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.99 | -1.15 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `SOLUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.99 | -1.15 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `SOLUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.99 | -1.15 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `SOLUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.99 | -1.15 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `TRXUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.21 | -0.81 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `TRXUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.21 | -0.81 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `TRXUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.21 | -0.81 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `TRXUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.21 | -0.81 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `WLDUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.94 | -6.12 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `WLDUSDT` | 2026-06-20 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.94 | -6.12 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `WLDUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.94 | -6.12 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `WLDUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.94 | -6.12 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ZECUSDT` | 2026-06-20 20:06 | RISK_OFF | true | accepted_loser | -1.00 | -0.03 | -2.47 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ZECUSDT` | 2026-06-20 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.03 | -2.47 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ZECUSDT` | 2026-06-20 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.03 | -2.47 | atr_reclaim_0_25 condition not met |
| quality_close | WATCH_ONLY | `ZECUSDT` | 2026-06-20 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.03 | -2.47 | quality_close condition not met |
| current_4h_close_reclaim | WATCH_ONLY | `BICOUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.28 | -1.16 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BICOUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.28 | -1.16 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BICOUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.28 | -1.16 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `BICOUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.28 | -1.16 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ETHUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 2.20 | -3.69 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ETHUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 2.20 | -3.69 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ETHUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 2.20 | -3.69 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ETHUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 2.20 | -3.69 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `NEARUSDT` | 2026-06-21 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.28 | -2.53 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `NEARUSDT` | 2026-06-21 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.28 | -2.53 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `NEARUSDT` | 2026-06-21 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.28 | -2.53 | atr_reclaim_0_25 condition not met |
| quality_close | WATCH_ONLY | `NEARUSDT` | 2026-06-21 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.28 | -2.53 | quality_close condition not met |
| current_4h_close_reclaim | WATCH_ONLY | `SOLUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.54 | -1.13 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `SOLUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.54 | -1.13 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `SOLUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.54 | -1.13 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `SOLUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.54 | -1.13 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `TRXUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.78 | -0.85 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `TRXUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.78 | -0.85 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `TRXUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.78 | -0.85 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `TRXUSDT` | 2026-06-21 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.78 | -0.85 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `BTCUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_loser | -1.00 | -0.03 | -2.35 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BTCUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.03 | -2.35 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BTCUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_loser | -1.00 | -0.03 | -2.35 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `BTCUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.03 | -2.35 | quality_close condition not met |
| current_4h_close_reclaim | WATCH_ONLY | `ETHUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.37 | -2.18 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ETHUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.37 | -2.18 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ETHUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.37 | -2.18 | atr_reclaim_0_25 condition not met |
| quality_close | WATCH_ONLY | `ETHUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.37 | -2.18 | quality_close condition not met |
| current_4h_close_reclaim | WATCH_ONLY | `SOLUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.41 | -1.24 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `SOLUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.41 | -1.24 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `SOLUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.41 | -1.24 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `SOLUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.41 | -1.24 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `SYNUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_winner_path | 2.88 | 2.88 | 0.01 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `SYNUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_winner_path | 2.88 | 2.88 | 0.01 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `SYNUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_winner_path | 2.88 | 2.88 | 0.01 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `SYNUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_winner_path | 2.88 | 2.88 | 0.01 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `WLDUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_loser | -1.00 | -0.07 | -5.62 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `WLDUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.07 | -5.62 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `WLDUSDT` | 2026-06-22 20:06 | RISK_OFF | true | accepted_loser | -1.00 | -0.07 | -5.62 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `WLDUSDT` | 2026-06-22 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.07 | -5.62 | quality_close condition not met |
| current_4h_close_reclaim | REJECT | `BTCUSDT` | 2026-06-23 20:07 | RISK_OFF | true | accepted_loser | -1.00 | 0.31 | -2.80 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `BTCUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_loser | 1.00 | 0.31 | -2.80 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `BTCUSDT` | 2026-06-23 20:07 | RISK_OFF | true | accepted_loser | -1.00 | 0.31 | -2.80 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `BTCUSDT` | 2026-06-23 20:07 | RISK_OFF | true | accepted_loser | -1.00 | 0.31 | -2.80 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `SUIUSDT` | 2026-06-23 20:07 | RISK_OFF | true | accepted_neutral | n/a | 1.03 | -0.73 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `SUIUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_neutral | n/a | 1.03 | -0.73 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `SUIUSDT` | 2026-06-23 20:07 | RISK_OFF | true | accepted_neutral | n/a | 1.03 | -0.73 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `SUIUSDT` | 2026-06-23 20:07 | RISK_OFF | true | accepted_neutral | n/a | 1.03 | -0.73 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `SYNUSDT` | 2026-06-23 20:07 | RISK_OFF | true | accepted_winner_path | 4.80 | 4.80 | 0.59 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `SYNUSDT` | 2026-06-23 20:07 | RISK_OFF | true | accepted_winner_path | 4.80 | 4.80 | 0.59 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `SYNUSDT` | 2026-06-23 20:07 | RISK_OFF | true | accepted_winner_path | 4.80 | 4.80 | 0.59 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `SYNUSDT` | 2026-06-23 20:07 | RISK_OFF | true | accepted_winner_path | 4.80 | 4.80 | 0.59 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `TRXUSDT` | 2026-06-23 20:07 | RISK_OFF | true | accepted_loser | -1.00 | 0.13 | -1.35 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `TRXUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_loser | 1.00 | 0.13 | -1.35 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `TRXUSDT` | 2026-06-23 20:07 | RISK_OFF | true | accepted_loser | -1.00 | 0.13 | -1.35 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `TRXUSDT` | 2026-06-23 20:07 | RISK_OFF | true | accepted_loser | -1.00 | 0.13 | -1.35 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `WLDUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.66 | -4.97 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `WLDUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.66 | -4.97 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `WLDUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.66 | -4.97 | atr_reclaim_0_25 condition not met |
| quality_close | REJECT | `WLDUSDT` | 2026-06-23 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.66 | -4.97 | quality_close condition not met |
| current_4h_close_reclaim | REJECT | `BNBUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.36 | -2.46 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `BNBUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.36 | -2.46 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `BNBUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.36 | -2.46 | atr_reclaim_0_25 condition not met |
| quality_close | REJECT | `BNBUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.36 | -2.46 | quality_close condition not met |
| current_4h_close_reclaim | REJECT | `BTCUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.38 | -2.81 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `BTCUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.38 | -2.81 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `BTCUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.38 | -2.81 | atr_reclaim_0_25 condition not met |
| quality_close | REJECT | `BTCUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | -0.38 | -2.81 | quality_close condition not met |
| current_4h_close_reclaim | REJECT | `ETHUSDT` | 2026-06-24 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.05 | -2.52 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `ETHUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 1.05 | -2.52 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `ETHUSDT` | 2026-06-24 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.05 | -2.52 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `ETHUSDT` | 2026-06-24 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.05 | -2.52 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `SOLUSDT` | 2026-06-24 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 6.90 | -1.52 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `SOLUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 6.90 | -1.52 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `SOLUSDT` | 2026-06-24 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 6.90 | -1.52 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `SOLUSDT` | 2026-06-24 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 6.90 | -1.52 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `XRPUSDT` | 2026-06-24 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.03 | -2.60 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `XRPUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.03 | -2.60 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `XRPUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.03 | -2.60 | atr_reclaim_0_25 condition not met |
| quality_close | REJECT | `XRPUSDT` | 2026-06-24 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.03 | -2.60 | quality_close condition not met |
| current_4h_close_reclaim | WATCH_ONLY | `AAVEUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_neutral | n/a | 1.26 | -0.06 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `AAVEUSDT` | 2026-06-25 20:08 | RISK_OFF | false | filtered_neutral | n/a | 1.26 | -0.06 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `AAVEUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_neutral | n/a | 1.26 | -0.06 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `AAVEUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_neutral | n/a | 1.26 | -0.06 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `BTCUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_neutral | n/a | 1.17 | -0.89 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `BTCUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_neutral | n/a | 1.17 | -0.89 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `BTCUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_neutral | n/a | 1.17 | -0.89 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `BTCUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_neutral | n/a | 1.17 | -0.89 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `SYNUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_winner_path | 1.92 | 1.92 | -0.57 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `SYNUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_winner_path | 1.92 | 1.92 | -0.57 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `SYNUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_winner_path | 1.92 | 1.92 | -0.57 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `SYNUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_winner_path | 1.92 | 1.92 | -0.57 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `TRXUSDT` | 2026-06-25 20:08 | RISK_OFF | false | filtered_loser | 1.00 | -0.57 | -1.55 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `TRXUSDT` | 2026-06-25 20:08 | RISK_OFF | false | filtered_loser | 1.00 | -0.57 | -1.55 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `TRXUSDT` | 2026-06-25 20:08 | RISK_OFF | false | filtered_loser | 1.00 | -0.57 | -1.55 | atr_reclaim_0_25 condition not met |
| quality_close | WATCH_ONLY | `TRXUSDT` | 2026-06-25 20:08 | RISK_OFF | false | filtered_loser | 1.00 | -0.57 | -1.55 | quality_close condition not met |
| current_4h_close_reclaim | WATCH_ONLY | `XPLUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_neutral | n/a | 1.26 | -0.56 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `XPLUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_neutral | n/a | 1.26 | -0.56 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `XPLUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_neutral | n/a | 1.26 | -0.56 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `XPLUSDT` | 2026-06-25 20:08 | RISK_OFF | true | accepted_neutral | n/a | 1.26 | -0.56 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `AAVEUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.76 | -0.14 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `AAVEUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.76 | -0.14 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `AAVEUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.76 | -0.14 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `AAVEUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.76 | -0.14 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `HEIUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.09 | -0.55 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `HEIUSDT` | 2026-06-26 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.09 | -0.55 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `HEIUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.09 | -0.55 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `HEIUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.09 | -0.55 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `SOLUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_winner_path | 2.75 | 2.75 | 0.44 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `SOLUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_winner_path | 2.75 | 2.75 | 0.44 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `SOLUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_winner_path | 2.75 | 2.75 | 0.44 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `SOLUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_winner_path | 2.75 | 2.75 | 0.44 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `SYNUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_winner_path | 4.21 | 4.21 | -0.43 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `SYNUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_winner_path | 4.21 | 4.21 | -0.43 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `SYNUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_winner_path | 4.21 | 4.21 | -0.43 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `SYNUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_winner_path | 4.21 | 4.21 | -0.43 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `XPLUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.39 | -0.76 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `XPLUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.39 | -0.76 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `XPLUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.39 | -0.76 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `XPLUSDT` | 2026-06-26 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.39 | -0.76 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `AAVEUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.06 | -0.45 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `AAVEUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.06 | -0.45 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `AAVEUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.06 | -0.45 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `AAVEUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.06 | -0.45 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `BNBUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.07 | -0.64 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `BNBUSDT` | 2026-06-27 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.07 | -0.64 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `BNBUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.07 | -0.64 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `BNBUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.07 | -0.64 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `BTCUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.65 | -0.31 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `BTCUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.65 | -0.31 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `BTCUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.65 | -0.31 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `BTCUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.65 | -0.31 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `SOLUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.16 | -0.17 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `SOLUSDT` | 2026-06-27 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 1.16 | -0.17 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `SOLUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.16 | -0.17 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `SOLUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.16 | -0.17 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `XRPUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.70 | -0.32 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `XRPUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.70 | -0.32 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `XRPUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.70 | -0.32 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `XRPUSDT` | 2026-06-27 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.70 | -0.32 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `BTCUSDT` | 2026-06-28 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 2.05 | -0.32 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BTCUSDT` | 2026-06-28 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 2.05 | -0.32 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BTCUSDT` | 2026-06-28 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 2.05 | -0.32 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `BTCUSDT` | 2026-06-28 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 2.05 | -0.32 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `ETHUSDT` | 2026-06-28 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.41 | -0.14 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `ETHUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 1.41 | -0.14 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `ETHUSDT` | 2026-06-28 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.41 | -0.14 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `ETHUSDT` | 2026-06-28 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.41 | -0.14 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `NEARUSDT` | 2026-06-28 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.77 | -0.55 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `NEARUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.77 | -0.55 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `NEARUSDT` | 2026-06-28 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.77 | -0.55 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `NEARUSDT` | 2026-06-28 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.77 | -0.55 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `SOLUSDT` | 2026-06-28 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.39 | -0.18 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `SOLUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 1.39 | -0.18 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `SOLUSDT` | 2026-06-28 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.39 | -0.18 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `SOLUSDT` | 2026-06-28 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.39 | -0.18 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `XRPUSDT` | 2026-06-28 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.85 | -0.26 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `XRPUSDT` | 2026-06-28 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.85 | -0.26 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `XRPUSDT` | 2026-06-28 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.85 | -0.26 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `XRPUSDT` | 2026-06-28 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.85 | -0.26 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ACTUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.60 | -0.51 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ACTUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.60 | -0.51 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ACTUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.60 | -0.51 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ACTUSDT` | 2026-06-29 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.60 | -0.51 | quality_close condition not met |
| current_4h_close_reclaim | WATCH_ONLY | `BTCUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.36 | -0.86 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BTCUSDT` | 2026-06-29 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.36 | -0.86 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BTCUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.36 | -0.86 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `BTCUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.36 | -0.86 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `ETHUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_winner_path | 3.53 | 3.53 | 0.04 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `ETHUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_winner_path | 3.53 | 3.53 | 0.04 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `ETHUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_winner_path | 3.53 | 3.53 | 0.04 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `ETHUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_winner_path | 3.53 | 3.53 | 0.04 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `SOLUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_winner_path | 2.49 | 2.49 | 0.13 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `SOLUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_winner_path | 2.49 | 2.49 | 0.13 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `SOLUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_winner_path | 2.49 | 2.49 | 0.13 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `SOLUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_winner_path | 2.49 | 2.49 | 0.13 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `XRPUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.71 | -0.62 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `XRPUSDT` | 2026-06-29 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.71 | -0.62 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `XRPUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.71 | -0.62 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `XRPUSDT` | 2026-06-29 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.71 | -0.62 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `ETHUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 3.25 | 3.25 | 0.09 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `ETHUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 3.25 | 3.25 | 0.09 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `ETHUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 3.25 | 3.25 | 0.09 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `ETHUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 3.25 | 3.25 | 0.09 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `SOLUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 1.90 | 1.90 | 0.06 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `SOLUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 1.90 | 1.90 | 0.06 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `SOLUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 1.90 | 1.90 | 0.06 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `SOLUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 1.90 | 1.90 | 0.06 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `SYNUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.02 | -0.45 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `SYNUSDT` | 2026-06-30 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.02 | -0.45 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `SYNUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.02 | -0.45 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `SYNUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.02 | -0.45 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `XRPUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 2.25 | 2.25 | -0.08 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `XRPUSDT` | 2026-06-30 20:06 | RISK_OFF | false | missed_winner | -2.25 | 2.25 | -0.08 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `XRPUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 2.25 | 2.25 | -0.08 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `XRPUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 2.25 | 2.25 | -0.08 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `ZECUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 2.39 | 2.39 | 0.23 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `ZECUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 2.39 | 2.39 | 0.23 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `ZECUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 2.39 | 2.39 | 0.23 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `ZECUSDT` | 2026-06-30 20:06 | RISK_OFF | true | accepted_winner_path | 2.39 | 2.39 | 0.23 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ADAUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.80 | 0.19 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ADAUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.80 | 0.19 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ADAUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.80 | 0.19 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ADAUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.80 | 0.19 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `CELOUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.34 | -0.40 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `CELOUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.34 | -0.40 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `CELOUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.34 | -0.40 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `CELOUSDT` | 2026-07-01 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.34 | -0.40 | quality_close condition not met |
| current_4h_close_reclaim | WATCH_ONLY | `SOLUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.24 | 0.36 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `SOLUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.24 | 0.36 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `SOLUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.24 | 0.36 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `SOLUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 1.24 | 0.36 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `SYNUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.73 | -0.23 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `SYNUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.73 | -0.23 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `SYNUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.73 | -0.23 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `SYNUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.73 | -0.23 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `XLMUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.17 | -0.04 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `XLMUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.17 | -0.04 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `XLMUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.17 | -0.04 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `XLMUSDT` | 2026-07-01 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.17 | -0.04 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ADAUSDT` | 2026-07-02 20:06 | RISK_OFF | true | accepted_right_censored | n/a | -0.03 | -0.03 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ADAUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.03 | -0.03 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ADAUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.03 | -0.03 | atr_reclaim_0_25 condition not met |
| quality_close | WATCH_ONLY | `ADAUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.03 | -0.03 | quality_close condition not met |
| current_4h_close_reclaim | WATCH_ONLY | `ETHUSDT` | 2026-07-02 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.61 | 0.61 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ETHUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.61 | 0.61 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ETHUSDT` | 2026-07-02 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.61 | 0.61 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ETHUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.61 | 0.61 | quality_close condition not met |
| current_4h_close_reclaim | WATCH_ONLY | `NEARUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.02 | 0.02 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `NEARUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.02 | 0.02 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `NEARUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.02 | 0.02 | atr_reclaim_0_25 condition not met |
| quality_close | WATCH_ONLY | `NEARUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | 0.02 | 0.02 | quality_close condition not met |
| current_4h_close_reclaim | WATCH_ONLY | `SOLUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.09 | -0.09 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `SOLUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.09 | -0.09 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `SOLUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.09 | -0.09 | atr_reclaim_0_25 condition not met |
| quality_close | WATCH_ONLY | `SOLUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.09 | -0.09 | quality_close condition not met |
| current_4h_close_reclaim | WATCH_ONLY | `ZECUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.17 | -0.17 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ZECUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.17 | -0.17 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ZECUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.17 | -0.17 | atr_reclaim_0_25 condition not met |
| quality_close | WATCH_ONLY | `ZECUSDT` | 2026-07-02 20:06 | RISK_OFF | false | filtered_right_censored | n/a | -0.17 | -0.17 | quality_close condition not met |

## Raw Summary

```json
{
  "experiment": "reclaim_quality_matrix",
  "opportunity_set_hash": "6e1f8adbd43f8f1f",
  "opportunities": 71,
  "summary": [
    {
      "variant": "atr_reclaim_0_25",
      "opportunities": 71,
      "accepted": 58,
      "filtered": 13,
      "accepted_loser": 16,
      "accepted_winner_path": 12,
      "filtered_loser": 9,
      "missed_winner": 0,
      "total_decision_R": 32.42294637145537,
      "outcomes": {
        "filtered_loser": 9,
        "accepted_loser": 16,
        "accepted_winner_path": 12,
        "accepted_neutral": 7,
        "accepted_right_censored": 23,
        "filtered_right_censored": 4
      }
    },
    {
      "variant": "confirm_1bar",
      "opportunities": 71,
      "accepted": 36,
      "filtered": 35,
      "accepted_loser": 8,
      "accepted_winner_path": 11,
      "filtered_loser": 17,
      "missed_winner": 1,
      "total_decision_R": 43.91665176797528,
      "outcomes": {
        "filtered_loser": 17,
        "accepted_loser": 8,
        "accepted_winner_path": 11,
        "accepted_neutral": 5,
        "filtered_neutral": 2,
        "accepted_right_censored": 12,
        "filtered_right_censored": 15,
        "missed_winner": 1
      }
    },
    {
      "variant": "current_4h_close_reclaim",
      "opportunities": 71,
      "accepted": 61,
      "filtered": 10,
      "accepted_loser": 18,
      "accepted_winner_path": 12,
      "filtered_loser": 7,
      "missed_winner": 0,
      "total_decision_R": 28.422946371455364,
      "outcomes": {
        "filtered_loser": 7,
        "accepted_loser": 18,
        "accepted_winner_path": 12,
        "accepted_neutral": 7,
        "accepted_right_censored": 24,
        "filtered_right_censored": 3
      }
    },
    {
      "variant": "quality_close",
      "opportunities": 71,
      "accepted": 53,
      "filtered": 18,
      "accepted_loser": 14,
      "accepted_winner_path": 12,
      "filtered_loser": 11,
      "missed_winner": 0,
      "total_decision_R": 36.42294637145537,
      "outcomes": {
        "filtered_loser": 11,
        "accepted_loser": 14,
        "accepted_winner_path": 12,
        "accepted_neutral": 7,
        "accepted_right_censored": 20,
        "filtered_right_censored": 7
      }
    }
  ]
}
```
