---
created: 2026-07-25 23:37:11 CST
tags:
  - crypto
  - trading-system
  - shadow-experiment
account: demo
start_date: 2026-07-03
end_date: 2026-07-25
experiment: reclaim_quality_matrix
report_version: v2
opportunity_set_hash: 9468fbe1bab35767
---

# Paper Shadow Experiment reclaim_quality_matrix 2026-07-03 -> 2026-07-25 demo v2

This is an offline diagnostic experiment. It uses a fixed opportunity set and does not modify settings, plans, events, snapshots, or paper state.

## Decision

- verdict: retest
- opportunity_set_hash: 9468fbe1bab35767
- opportunity_set_path: `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-07-25\paper_shadow_opportunity_set_2026-07-03_2026-07-25_demo_9468fbe1bab35767_v2.json`
- config_action: do_not_modify_settings_toml

## Variant Summary

| Variant | Opportunities | Accepted | Filtered | Accepted Loser | Accepted Winner Path | Filtered Loser | Missed Winner | Total Decision R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| atr_reclaim_0_25 | 95 | 77 | 18 | 13 | 19 | 9 | 0 | 48.14 |
| confirm_1bar | 95 | 63 | 32 | 10 | 15 | 12 | 4 | 29.49 |
| current_4h_close_reclaim | 95 | 80 | 15 | 15 | 19 | 7 | 0 | 44.14 |
| quality_close | 95 | 78 | 17 | 14 | 19 | 8 | 0 | 46.14 |

## Outcome Counts

### atr_reclaim_0_25

| Outcome | Count |
|---|---:|
| accepted_loser | 13 |
| accepted_neutral | 27 |
| accepted_right_censored | 18 |
| accepted_winner_path | 19 |
| filtered_loser | 9 |
| filtered_neutral | 5 |
| filtered_right_censored | 4 |

### confirm_1bar

| Outcome | Count |
|---|---:|
| accepted_loser | 10 |
| accepted_neutral | 24 |
| accepted_right_censored | 14 |
| accepted_winner_path | 15 |
| filtered_loser | 12 |
| filtered_neutral | 8 |
| filtered_right_censored | 8 |
| missed_winner | 4 |

### current_4h_close_reclaim

| Outcome | Count |
|---|---:|
| accepted_loser | 15 |
| accepted_neutral | 27 |
| accepted_right_censored | 19 |
| accepted_winner_path | 19 |
| filtered_loser | 7 |
| filtered_neutral | 5 |
| filtered_right_censored | 3 |

### quality_close

| Outcome | Count |
|---|---:|
| accepted_loser | 14 |
| accepted_neutral | 26 |
| accepted_right_censored | 19 |
| accepted_winner_path | 19 |
| filtered_loser | 8 |
| filtered_neutral | 6 |
| filtered_right_censored | 3 |

## Detail Rows

| Variant | Source | Symbol | Time | Regime | Accepted | Outcome | PnL_R | MFE_R | MAE_R | Reason |
|---|---|---|---|---|---|---|---:|---:|---:|---|
| current_4h_close_reclaim | RECLAIM_PENDING | `ONDOUSDT` | 2026-07-03 00:10 | n/a | true | accepted_loser | -1.00 | 0.04 | -1.43 | first 4h close >= entry_high |
| confirm_1bar | RECLAIM_PENDING | `ONDOUSDT` | 2026-07-03 00:10 | n/a | false | filtered_loser | 1.00 | 0.04 | -1.43 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | RECLAIM_PENDING | `ONDOUSDT` | 2026-07-03 00:10 | n/a | false | filtered_loser | 1.00 | 0.04 | -1.43 | atr_reclaim_0_25 condition not met |
| quality_close | RECLAIM_PENDING | `ONDOUSDT` | 2026-07-03 00:10 | n/a | false | filtered_loser | 1.00 | 0.04 | -1.43 | quality_close condition not met |
| current_4h_close_reclaim | WATCH_ONLY | `ADAUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.83 | -0.39 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ADAUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.83 | -0.39 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ADAUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.83 | -0.39 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ADAUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.83 | -0.39 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `BTCUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.14 | 0.05 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BTCUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.14 | 0.05 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BTCUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.14 | 0.05 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `BTCUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.14 | 0.05 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `SOLUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.35 | -0.69 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `SOLUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.35 | -0.69 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `SOLUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.35 | -0.69 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `SOLUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.35 | -0.69 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `XRPUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.52 | -0.46 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `XRPUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.52 | -0.46 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `XRPUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.52 | -0.46 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `XRPUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.52 | -0.46 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `NEARUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.50 | -0.96 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `NEARUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.50 | -0.96 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `NEARUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.50 | -0.96 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `NEARUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.50 | -0.96 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `PEPEUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.60 | -0.25 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `PEPEUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.60 | -0.25 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `PEPEUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.60 | -0.25 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `PEPEUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.60 | -0.25 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `SOLUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.14 | -1.28 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `SOLUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.14 | -1.28 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `SOLUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.14 | -1.28 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `SOLUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.14 | -1.28 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `TLMUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.46 | -0.78 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `TLMUSDT` | 2026-07-04 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.46 | -0.78 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `TLMUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.46 | -0.78 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `TLMUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.46 | -0.78 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `XLMUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.48 | -1.94 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `XLMUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.48 | -1.94 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `XLMUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.48 | -1.94 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `XLMUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.48 | -1.94 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `BTCUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.01 | 3.01 | 0.01 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `BTCUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.01 | 3.01 | 0.01 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `BTCUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.01 | 3.01 | 0.01 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `BTCUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.01 | 3.01 | 0.01 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `ETHUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.55 | 3.55 | -0.41 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `ETHUSDT` | 2026-07-08 20:06 | RISK_OFF | false | missed_winner | -3.55 | 3.55 | -0.41 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `ETHUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.55 | 3.55 | -0.41 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `ETHUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.55 | 3.55 | -0.41 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `SOLUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.77 | -1.94 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `SOLUSDT` | 2026-07-08 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.77 | -1.94 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `SOLUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.77 | -1.94 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `SOLUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.77 | -1.94 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `TRXUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.77 | -0.95 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `TRXUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.77 | -0.95 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `TRXUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.77 | -0.95 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `TRXUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.77 | -0.95 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ZECUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.02 | 3.02 | -0.26 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ZECUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.02 | 3.02 | -0.26 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ZECUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.02 | 3.02 | -0.26 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ZECUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.02 | 3.02 | -0.26 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `BNBUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.37 | -0.28 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `BNBUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.37 | -0.28 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `BNBUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.37 | -0.28 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `BNBUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.37 | -0.28 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `BTCUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 1.67 | 1.67 | -0.27 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BTCUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 1.67 | 1.67 | -0.27 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BTCUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 1.67 | 1.67 | -0.27 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `BTCUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 1.67 | 1.67 | -0.27 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `ETHUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 3.37 | 3.37 | -0.02 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `ETHUSDT` | 2026-07-09 20:06 | RISK_OFF | false | missed_winner | -3.37 | 3.37 | -0.02 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `ETHUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 3.37 | 3.37 | -0.02 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `ETHUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 3.37 | 3.37 | -0.02 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `TRXUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.19 | -1.03 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `TRXUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.19 | -1.03 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `TRXUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.19 | -1.03 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `TRXUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.19 | -1.03 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ZECUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 3.54 | 3.54 | 0.25 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ZECUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 3.54 | 3.54 | 0.25 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ZECUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 3.54 | 3.54 | 0.25 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ZECUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 3.54 | 3.54 | 0.25 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `BNBUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.24 | -0.62 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BNBUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.24 | -0.62 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BNBUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.24 | -0.62 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `BNBUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.24 | -0.62 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `BTCUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.91 | -0.47 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BTCUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.91 | -0.47 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BTCUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.91 | -0.47 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `BTCUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.91 | -0.47 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ETHUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_winner_path | 1.74 | 1.74 | -0.06 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ETHUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_winner_path | 1.74 | 1.74 | -0.06 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ETHUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_winner_path | 1.74 | 1.74 | -0.06 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ETHUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_winner_path | 1.74 | 1.74 | -0.06 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `SOLUSDT` | 2026-07-10 20:05 | RISK_OFF | false | filtered_loser | 1.00 | -0.20 | -1.32 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `SOLUSDT` | 2026-07-10 20:05 | RISK_OFF | false | filtered_loser | 1.00 | -0.20 | -1.32 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `SOLUSDT` | 2026-07-10 20:05 | RISK_OFF | false | filtered_loser | 1.00 | -0.20 | -1.32 | atr_reclaim_0_25 condition not met |
| quality_close | WATCH_ONLY | `SOLUSDT` | 2026-07-10 20:05 | RISK_OFF | false | filtered_loser | 1.00 | -0.20 | -1.32 | quality_close condition not met |
| current_4h_close_reclaim | WATCH_ONLY | `BNBUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_neutral | n/a | 0.14 | -0.68 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BNBUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_neutral | n/a | 0.14 | -0.68 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BNBUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_neutral | n/a | 0.14 | -0.68 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `BNBUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_neutral | n/a | 0.14 | -0.68 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `BTCUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_neutral | n/a | 0.80 | -0.54 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BTCUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_neutral | n/a | 0.80 | -0.54 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BTCUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_neutral | n/a | 0.80 | -0.54 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `BTCUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_neutral | n/a | 0.80 | -0.54 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ETHUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.56 | 1.56 | -0.18 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ETHUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.56 | 1.56 | -0.18 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ETHUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.56 | 1.56 | -0.18 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ETHUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.56 | 1.56 | -0.18 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `SOLUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_loser | -1.00 | 0.43 | -1.84 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `SOLUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_loser | -1.00 | 0.43 | -1.84 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `SOLUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_loser | -1.00 | 0.43 | -1.84 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `SOLUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_loser | -1.00 | 0.43 | -1.84 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ZECUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.50 | 1.50 | -0.45 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ZECUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.50 | 1.50 | -0.45 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ZECUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.50 | 1.50 | -0.45 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ZECUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.50 | 1.50 | -0.45 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `BNBUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.18 | -0.90 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BNBUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.18 | -0.90 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BNBUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.18 | -0.90 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `BNBUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.18 | -0.90 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `BTCUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.01 | -0.73 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BTCUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.01 | -0.73 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BTCUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.01 | -0.73 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `BTCUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.01 | -0.73 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ETHUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.38 | -0.31 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ETHUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.38 | -0.31 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ETHUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.38 | -0.31 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ETHUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.38 | -0.31 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `SOLUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_loser | -1.00 | 0.59 | -1.28 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `SOLUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_loser | -1.00 | 0.59 | -1.28 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `SOLUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_loser | -1.00 | 0.59 | -1.28 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `SOLUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_loser | -1.00 | 0.59 | -1.28 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ZECUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.21 | -0.66 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ZECUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.21 | -0.66 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ZECUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.21 | -0.66 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ZECUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.21 | -0.66 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `DEXEUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.12 | -4.06 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `DEXEUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.12 | -4.06 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `DEXEUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.12 | -4.06 | atr_reclaim_0_25 condition not met |
| quality_close | WATCH_ONLY | `DEXEUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.12 | -4.06 | quality_close condition not met |
| current_4h_close_reclaim | REJECT | `ETHUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_winner_path | 4.19 | 4.19 | -0.27 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `ETHUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_winner_path | 4.19 | 4.19 | -0.27 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `ETHUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_winner_path | 4.19 | 4.19 | -0.27 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `ETHUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_winner_path | 4.19 | 4.19 | -0.27 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `TRXUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_neutral | n/a | 0.58 | -0.94 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `TRXUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_neutral | n/a | 0.58 | -0.94 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `TRXUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_neutral | n/a | 0.58 | -0.94 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `TRXUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_neutral | n/a | 0.58 | -0.94 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `WLDUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.14 | -1.64 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `WLDUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.14 | -1.64 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `WLDUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.14 | -1.64 | atr_reclaim_0_25 condition not met |
| quality_close | WATCH_ONLY | `WLDUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.14 | -1.64 | quality_close condition not met |
| current_4h_close_reclaim | WATCH_ONLY | `ZECUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_winner_path | 3.37 | 3.37 | -1.38 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ZECUSDT` | 2026-07-13 20:07 | RISK_OFF | false | missed_winner | -3.37 | 3.37 | -1.38 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ZECUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_winner_path | 3.37 | 3.37 | -1.38 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ZECUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_winner_path | 3.37 | 3.37 | -1.38 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `BNBUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.34 | -0.37 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `BNBUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.34 | -0.37 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `BNBUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.34 | -0.37 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `BNBUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.34 | -0.37 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ETHUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 1.77 | 1.77 | 0.32 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ETHUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 1.77 | 1.77 | 0.32 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ETHUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 1.77 | 1.77 | 0.32 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ETHUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 1.77 | 1.77 | 0.32 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `NEARUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.59 | -1.29 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `NEARUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.59 | -1.29 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `NEARUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.59 | -1.29 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `NEARUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.59 | -1.29 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `SXTUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.47 | -1.44 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `SXTUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.47 | -1.44 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `SXTUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.47 | -1.44 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `SXTUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.47 | -1.44 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ZECUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 4.03 | 4.03 | -1.40 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ZECUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 4.03 | 4.03 | -1.40 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ZECUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 4.03 | 4.03 | -1.40 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ZECUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 4.03 | 4.03 | -1.40 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `BNBUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.09 | -0.70 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BNBUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.09 | -0.70 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BNBUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.09 | -0.70 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `BNBUSDT` | 2026-07-15 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.09 | -0.70 | quality_close condition not met |
| current_4h_close_reclaim | WATCH_ONLY | `BTCUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.65 | -0.45 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BTCUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.65 | -0.45 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BTCUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.65 | -0.45 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `BTCUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.65 | -0.45 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ETHUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.70 | -0.19 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ETHUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.70 | -0.19 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ETHUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.70 | -0.19 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ETHUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.70 | -0.19 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `NEARUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.03 | -1.20 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `NEARUSDT` | 2026-07-15 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.03 | -1.20 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `NEARUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.03 | -1.20 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `NEARUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.03 | -1.20 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `BTCUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.77 | -0.41 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BTCUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.77 | -0.41 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BTCUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.77 | -0.41 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `BTCUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.77 | -0.41 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ETHUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.34 | -0.36 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ETHUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.34 | -0.36 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ETHUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.34 | -0.36 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ETHUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.34 | -0.36 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ONDOUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.61 | -0.44 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ONDOUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.61 | -0.44 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ONDOUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.61 | -0.44 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ONDOUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.61 | -0.44 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `XRPUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.58 | -0.40 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `XRPUSDT` | 2026-07-16 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.58 | -0.40 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `XRPUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.58 | -0.40 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `XRPUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.58 | -0.40 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ZECUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.16 | -1.12 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ZECUSDT` | 2026-07-16 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.16 | -1.12 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ZECUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.16 | -1.12 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ZECUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.16 | -1.12 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `BTCUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_winner_path | 2.57 | 2.57 | 0.59 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `BTCUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_winner_path | 2.57 | 2.57 | 0.59 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `BTCUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_winner_path | 2.57 | 2.57 | 0.59 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `BTCUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_winner_path | 2.57 | 2.57 | 0.59 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ETHUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_winner_path | 2.03 | 2.03 | -0.02 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ETHUSDT` | 2026-07-17 20:06 | RISK_OFF | false | missed_winner | -2.03 | 2.03 | -0.02 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ETHUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_winner_path | 2.03 | 2.03 | -0.02 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ETHUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_winner_path | 2.03 | 2.03 | -0.02 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ONDOUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.53 | -0.54 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ONDOUSDT` | 2026-07-17 20:06 | RISK_OFF | false | filtered_neutral | n/a | 0.53 | -0.54 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ONDOUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.53 | -0.54 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ONDOUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.53 | -0.54 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ZECUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.01 | -2.46 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ZECUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.01 | -2.46 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ZECUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.01 | -2.46 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ZECUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.01 | -2.46 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `BTCUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.86 | -0.12 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BTCUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.86 | -0.12 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BTCUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.86 | -0.12 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `BTCUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.86 | -0.12 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `SOLUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_winner_path | 2.73 | 2.73 | -0.11 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `SOLUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_winner_path | 2.73 | 2.73 | -0.11 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `SOLUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_winner_path | 2.73 | 2.73 | -0.11 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `SOLUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_winner_path | 2.73 | 2.73 | -0.11 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `XRPUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_winner_path | 3.31 | 3.31 | 0.43 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `XRPUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_winner_path | 3.31 | 3.31 | 0.43 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `XRPUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_winner_path | 3.31 | 3.31 | 0.43 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `XRPUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_winner_path | 3.31 | 3.31 | 0.43 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ZECUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_loser | -1.00 | 0.39 | -2.28 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ZECUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_loser | -1.00 | 0.39 | -2.28 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ZECUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_loser | -1.00 | 0.39 | -2.28 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ZECUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_loser | -1.00 | 0.39 | -2.28 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `BANKUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.24 | -0.27 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BANKUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.24 | -0.27 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BANKUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.24 | -0.27 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `BANKUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.24 | -0.27 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `BTCUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.73 | -0.18 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BTCUSDT` | 2026-07-19 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.73 | -0.18 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BTCUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.73 | -0.18 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `BTCUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.73 | -0.18 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ETHUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.78 | -0.15 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ETHUSDT` | 2026-07-19 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.78 | -0.15 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ETHUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.78 | -0.15 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ETHUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.78 | -0.15 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | REJECT | `SOLUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.60 | -0.62 | first 4h close >= entry_high |
| confirm_1bar | REJECT | `SOLUSDT` | 2026-07-19 20:05 | RISK_OFF | false | filtered_right_censored | n/a | 0.60 | -0.62 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `SOLUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.60 | -0.62 | close >= entry_high + 0.25 ATR |
| quality_close | REJECT | `SOLUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.60 | -0.62 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ZECUSDT` | 2026-07-19 20:05 | RISK_OFF | false | filtered_loser | 1.00 | -0.15 | -1.99 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ZECUSDT` | 2026-07-19 20:05 | RISK_OFF | false | filtered_loser | 1.00 | -0.15 | -1.99 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ZECUSDT` | 2026-07-19 20:05 | RISK_OFF | false | filtered_loser | 1.00 | -0.15 | -1.99 | atr_reclaim_0_25 condition not met |
| quality_close | WATCH_ONLY | `ZECUSDT` | 2026-07-19 20:05 | RISK_OFF | false | filtered_loser | 1.00 | -0.15 | -1.99 | quality_close condition not met |
| current_4h_close_reclaim | WATCH_ONLY | `BANKUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.33 | -0.61 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BANKUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.33 | -0.61 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BANKUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.33 | -0.61 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `BANKUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.33 | -0.61 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `BTCUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.67 | -0.32 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BTCUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.67 | -0.32 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BTCUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.67 | -0.32 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `BTCUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.67 | -0.32 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ETHUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.75 | -0.30 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ETHUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.75 | -0.30 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ETHUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.75 | -0.30 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ETHUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.75 | -0.30 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `SOLUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.41 | -0.89 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `SOLUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.41 | -0.89 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `SOLUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.41 | -0.89 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `SOLUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.41 | -0.89 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `XRPUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.25 | -0.44 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `XRPUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.25 | -0.44 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `XRPUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.25 | -0.44 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `XRPUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.25 | -0.44 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `BANKUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_winner_path | 2.55 | 2.55 | 0.02 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BANKUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_winner_path | 2.55 | 2.55 | 0.02 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BANKUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_winner_path | 2.55 | 2.55 | 0.02 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `BANKUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_winner_path | 2.55 | 2.55 | 0.02 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `BTCUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.26 | -0.47 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BTCUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.26 | -0.47 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BTCUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.26 | -0.47 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `BTCUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.26 | -0.47 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ETHUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.32 | -0.57 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ETHUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.32 | -0.57 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ETHUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.32 | -0.57 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ETHUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.32 | -0.57 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `SOLUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.16 | -0.98 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `SOLUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.16 | -0.98 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `SOLUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.16 | -0.98 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `SOLUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.16 | -0.98 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `BANKUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_winner_path | 2.62 | 2.62 | 1.10 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BANKUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_winner_path | 2.62 | 2.62 | 1.10 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BANKUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_winner_path | 2.62 | 2.62 | 1.10 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `BANKUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_winner_path | 2.62 | 2.62 | 1.10 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `BTCUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.00 | -0.53 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BTCUSDT` | 2026-07-22 20:05 | NEUTRAL | false | filtered_right_censored | n/a | 0.00 | -0.53 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BTCUSDT` | 2026-07-22 20:05 | NEUTRAL | false | filtered_right_censored | n/a | 0.00 | -0.53 | atr_reclaim_0_25 condition not met |
| quality_close | WATCH_ONLY | `BTCUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.00 | -0.53 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ETHUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.09 | -0.63 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ETHUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.09 | -0.63 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ETHUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.09 | -0.63 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `ETHUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.09 | -0.63 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `SOLUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_loser | -1.00 | 0.08 | -1.13 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `SOLUSDT` | 2026-07-22 20:05 | NEUTRAL | false | filtered_loser | 1.00 | 0.08 | -1.13 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `SOLUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_loser | -1.00 | 0.08 | -1.13 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `SOLUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_loser | -1.00 | 0.08 | -1.13 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `XRPUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.10 | -0.69 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `XRPUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.10 | -0.69 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `XRPUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.10 | -0.69 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `XRPUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.10 | -0.69 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `BANKUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.94 | 0.23 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BANKUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.94 | 0.23 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BANKUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.94 | 0.23 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `BANKUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.94 | 0.23 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `BTCUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | 0.07 | -1.05 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BTCUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | 0.07 | -1.05 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BTCUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | 0.07 | -1.05 | atr_reclaim_0_25 condition not met |
| quality_close | WATCH_ONLY | `BTCUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | 0.07 | -1.05 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `ETHUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | -0.51 | -1.08 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ETHUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | -0.51 | -1.08 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ETHUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | -0.51 | -1.08 | atr_reclaim_0_25 condition not met |
| quality_close | WATCH_ONLY | `ETHUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | -0.51 | -1.08 | quality_close condition not met |
| current_4h_close_reclaim | WATCH_ONLY | `SOLUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | -0.89 | -1.99 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `SOLUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | -0.89 | -1.99 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `SOLUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | -0.89 | -1.99 | atr_reclaim_0_25 condition not met |
| quality_close | WATCH_ONLY | `SOLUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | -0.89 | -1.99 | quality_close condition not met |
| current_4h_close_reclaim | WATCH_ONLY | `XRPUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | -0.50 | -1.08 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `XRPUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | -0.50 | -1.08 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `XRPUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | -0.50 | -1.08 | atr_reclaim_0_25 condition not met |
| quality_close | WATCH_ONLY | `XRPUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | -0.50 | -1.08 | quality_close condition not met |
| current_4h_close_reclaim | WATCH_ONLY | `BANKUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.43 | 0.24 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BANKUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.43 | 0.24 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BANKUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.43 | 0.24 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `BANKUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.43 | 0.24 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `BNBUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.06 | -0.14 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BNBUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.06 | -0.14 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BNBUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.06 | -0.14 | atr_reclaim_0_25 condition not met |
| quality_close | WATCH_ONLY | `BNBUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.06 | -0.14 | quality_close condition not met |
| current_4h_close_reclaim | WATCH_ONLY | `BTCUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.59 | -0.76 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BTCUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.59 | -0.76 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BTCUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.59 | -0.76 | atr_reclaim_0_25 condition not met |
| quality_close | WATCH_ONLY | `BTCUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.59 | -0.76 | quality_close condition not met |
| current_4h_close_reclaim | WATCH_ONLY | `ETHUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.28 | -0.46 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ETHUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.28 | -0.46 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ETHUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.28 | -0.46 | atr_reclaim_0_25 condition not met |
| quality_close | WATCH_ONLY | `ETHUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.28 | -0.46 | quality_close condition not met |
| current_4h_close_reclaim | WATCH_ONLY | `VANAUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.07 | -0.86 | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `VANAUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | 0.07 | -0.86 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `VANAUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.07 | -0.86 | close >= entry_high + 0.25 ATR |
| quality_close | WATCH_ONLY | `VANAUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.07 | -0.86 | close reclaimed with body >= 35% range and close in upper 65% |
| current_4h_close_reclaim | WATCH_ONLY | `BANKUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `BANKUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `BANKUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | missing 4h path |
| quality_close | WATCH_ONLY | `BANKUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | missing 4h path |
| current_4h_close_reclaim | REJECT | `BNBUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | first 4h close >= entry_high |
| confirm_1bar | REJECT | `BNBUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `BNBUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | missing 4h path |
| quality_close | REJECT | `BNBUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | missing 4h path |
| current_4h_close_reclaim | REJECT | `BTCUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | first 4h close >= entry_high |
| confirm_1bar | REJECT | `BTCUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `BTCUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | missing 4h path |
| quality_close | REJECT | `BTCUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | missing 4h path |
| current_4h_close_reclaim | WATCH_ONLY | `ETHUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | first 4h close >= entry_high |
| confirm_1bar | WATCH_ONLY | `ETHUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | WATCH_ONLY | `ETHUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | missing 4h path |
| quality_close | WATCH_ONLY | `ETHUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | missing 4h path |
| current_4h_close_reclaim | REJECT | `XRPUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | first 4h close >= entry_high |
| confirm_1bar | REJECT | `XRPUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | REJECT | `XRPUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | missing 4h path |
| quality_close | REJECT | `XRPUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | missing 4h path |

## Raw Summary

```json
{
  "experiment": "reclaim_quality_matrix",
  "opportunity_set_hash": "9468fbe1bab35767",
  "opportunities": 95,
  "summary": [
    {
      "variant": "atr_reclaim_0_25",
      "opportunities": 95,
      "accepted": 77,
      "filtered": 18,
      "accepted_loser": 13,
      "accepted_winner_path": 19,
      "filtered_loser": 9,
      "missed_winner": 0,
      "total_decision_R": 48.13786778393428,
      "outcomes": {
        "filtered_loser": 9,
        "accepted_neutral": 27,
        "accepted_loser": 13,
        "accepted_winner_path": 19,
        "accepted_right_censored": 18,
        "filtered_right_censored": 4,
        "filtered_neutral": 5
      }
    },
    {
      "variant": "confirm_1bar",
      "opportunities": 95,
      "accepted": 63,
      "filtered": 32,
      "accepted_loser": 10,
      "accepted_winner_path": 15,
      "filtered_loser": 12,
      "missed_winner": 4,
      "total_decision_R": 29.494528104596252,
      "outcomes": {
        "filtered_loser": 12,
        "accepted_neutral": 24,
        "accepted_loser": 10,
        "filtered_neutral": 8,
        "accepted_winner_path": 15,
        "missed_winner": 4,
        "accepted_right_censored": 14,
        "filtered_right_censored": 8
      }
    },
    {
      "variant": "current_4h_close_reclaim",
      "opportunities": 95,
      "accepted": 80,
      "filtered": 15,
      "accepted_loser": 15,
      "accepted_winner_path": 19,
      "filtered_loser": 7,
      "missed_winner": 0,
      "total_decision_R": 44.13786778393428,
      "outcomes": {
        "accepted_loser": 15,
        "accepted_neutral": 27,
        "accepted_winner_path": 19,
        "filtered_loser": 7,
        "accepted_right_censored": 19,
        "filtered_right_censored": 3,
        "filtered_neutral": 5
      }
    },
    {
      "variant": "quality_close",
      "opportunities": 95,
      "accepted": 78,
      "filtered": 17,
      "accepted_loser": 14,
      "accepted_winner_path": 19,
      "filtered_loser": 8,
      "missed_winner": 0,
      "total_decision_R": 46.13786778393428,
      "outcomes": {
        "filtered_loser": 8,
        "accepted_neutral": 26,
        "accepted_loser": 14,
        "accepted_winner_path": 19,
        "filtered_neutral": 6,
        "accepted_right_censored": 19,
        "filtered_right_censored": 3
      }
    }
  ]
}
```
