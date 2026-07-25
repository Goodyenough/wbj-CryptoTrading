---
created: 2026-07-25 23:54:52 CST
tags:
  - crypto
  - trading-system
  - shadow-experiment
account: demo
start_date: 2026-07-17
end_date: 2026-07-25
experiment: reclaim_quality_matrix
report_version: v1
opportunity_set_hash: d958282222b977b7
---

# Paper Shadow Experiment reclaim_quality_matrix 2026-07-17 -> 2026-07-25 demo v1

This is an offline diagnostic experiment. It uses a fixed opportunity set and does not modify settings, plans, events, snapshots, or paper state.

## Decision

- verdict: retest
- opportunity_set_hash: d958282222b977b7
- opportunity_set_path: `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-07-25\paper_shadow_opportunity_set_2026-07-17_2026-07-25_demo_d958282222b977b7_v1.json`
- config_action: do_not_modify_settings_toml

## Variant Summary

| Variant | Opportunities | Accepted | Filtered | Accepted Loser | Accepted Winner Path | Filtered Loser | Missed Winner | Total Decision R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| atr_reclaim_0_25 | 43 | 28 | 15 | 3 | 6 | 5 | 0 | 17.81 |
| confirm_1bar | 43 | 22 | 21 | 3 | 5 | 5 | 1 | 13.75 |
| current_4h_close_reclaim | 43 | 31 | 12 | 4 | 6 | 4 | 0 | 15.81 |
| quality_close | 43 | 30 | 13 | 4 | 6 | 4 | 0 | 15.81 |

## Outcome Counts

### atr_reclaim_0_25

| Outcome | Count |
|---|---:|
| accepted_loser | 3 |
| accepted_neutral | 1 |
| accepted_right_censored | 18 |
| accepted_winner_path | 6 |
| filtered_loser | 5 |
| filtered_neutral | 6 |
| filtered_right_censored | 4 |

### confirm_1bar

| Outcome | Count |
|---|---:|
| accepted_loser | 3 |
| accepted_right_censored | 14 |
| accepted_winner_path | 5 |
| filtered_loser | 5 |
| filtered_neutral | 7 |
| filtered_right_censored | 8 |
| missed_winner | 1 |

### current_4h_close_reclaim

| Outcome | Count |
|---|---:|
| accepted_loser | 4 |
| accepted_neutral | 2 |
| accepted_right_censored | 19 |
| accepted_winner_path | 6 |
| filtered_loser | 4 |
| filtered_neutral | 5 |
| filtered_right_censored | 3 |

### quality_close

| Outcome | Count |
|---|---:|
| accepted_loser | 4 |
| accepted_neutral | 1 |
| accepted_right_censored | 19 |
| accepted_winner_path | 6 |
| filtered_loser | 4 |
| filtered_neutral | 6 |
| filtered_right_censored | 3 |

## Detail Rows

| Variant | Source | Symbol | Time | Regime | Accepted | Outcome | PnL_R | MFE_R | MAE_R | Reason |
|---|---|---|---|---|---|---|---:|---:|---:|---|
| current_4h_close_reclaim | RECLAIM_PENDING | `ONDOUSDT` | 2026-07-17 00:10 | n/a | true | accepted_neutral | n/a | 0.04 | -0.99 | first 4h close >= entry_high |
| confirm_1bar | RECLAIM_PENDING | `ONDOUSDT` | 2026-07-17 00:10 | n/a | false | filtered_neutral | n/a | 0.04 | -0.99 | next 4h candle confirms close >= entry_high and low > stop |
| atr_reclaim_0_25 | RECLAIM_PENDING | `ONDOUSDT` | 2026-07-17 00:10 | n/a | false | filtered_neutral | n/a | 0.04 | -0.99 | atr_reclaim_0_25 condition not met |
| quality_close | RECLAIM_PENDING | `ONDOUSDT` | 2026-07-17 00:10 | n/a | false | filtered_neutral | n/a | 0.04 | -0.99 | quality_close condition not met |
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
  "opportunity_set_hash": "d958282222b977b7",
  "opportunities": 43,
  "summary": [
    {
      "variant": "atr_reclaim_0_25",
      "opportunities": 43,
      "accepted": 28,
      "filtered": 15,
      "accepted_loser": 3,
      "accepted_winner_path": 6,
      "filtered_loser": 5,
      "missed_winner": 0,
      "total_decision_R": 17.813430849618083,
      "outcomes": {
        "filtered_neutral": 6,
        "accepted_winner_path": 6,
        "accepted_neutral": 1,
        "accepted_loser": 3,
        "accepted_right_censored": 18,
        "filtered_loser": 5,
        "filtered_right_censored": 4
      }
    },
    {
      "variant": "confirm_1bar",
      "opportunities": 43,
      "accepted": 22,
      "filtered": 21,
      "accepted_loser": 3,
      "accepted_winner_path": 5,
      "filtered_loser": 5,
      "missed_winner": 1,
      "total_decision_R": 13.752158972375758,
      "outcomes": {
        "filtered_neutral": 7,
        "accepted_winner_path": 5,
        "missed_winner": 1,
        "accepted_loser": 3,
        "accepted_right_censored": 14,
        "filtered_right_censored": 8,
        "filtered_loser": 5
      }
    },
    {
      "variant": "current_4h_close_reclaim",
      "opportunities": 43,
      "accepted": 31,
      "filtered": 12,
      "accepted_loser": 4,
      "accepted_winner_path": 6,
      "filtered_loser": 4,
      "missed_winner": 0,
      "total_decision_R": 15.813430849618083,
      "outcomes": {
        "accepted_neutral": 2,
        "accepted_winner_path": 6,
        "accepted_loser": 4,
        "accepted_right_censored": 19,
        "filtered_loser": 4,
        "filtered_right_censored": 3,
        "filtered_neutral": 5
      }
    },
    {
      "variant": "quality_close",
      "opportunities": 43,
      "accepted": 30,
      "filtered": 13,
      "accepted_loser": 4,
      "accepted_winner_path": 6,
      "filtered_loser": 4,
      "missed_winner": 0,
      "total_decision_R": 15.813430849618083,
      "outcomes": {
        "filtered_neutral": 6,
        "accepted_winner_path": 6,
        "accepted_neutral": 1,
        "accepted_loser": 4,
        "accepted_right_censored": 19,
        "filtered_loser": 4,
        "filtered_right_censored": 3
      }
    }
  ]
}
```
