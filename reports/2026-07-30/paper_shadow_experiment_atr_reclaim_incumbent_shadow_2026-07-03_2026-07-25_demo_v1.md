---
created: 2026-07-30 18:00:09 CST
tags:
  - crypto
  - trading-system
  - shadow-experiment
account: demo
start_date: 2026-07-03
end_date: 2026-07-25
experiment: atr_reclaim_incumbent_shadow
report_version: v1
opportunity_set_hash: 9468fbe1bab35767
---

# Paper Shadow Experiment atr_reclaim_incumbent_shadow 2026-07-03 -> 2026-07-25 demo v1

This is an offline diagnostic experiment. It uses a fixed opportunity set and does not modify settings, plans, events, snapshots, or paper state.

## Incumbent Framework

| Line | Definition | Controls paper? | Purpose |
|---|---|---|---|
| reference_baseline | Original strategy without `atr_reclaim_0_35` | no | Long-term calibration reference. |
| atr_reclaim_0_35_shadow | Original strategy plus frozen `0.35 ATR` reclaim requirement | no | Independent forward comparison line. |
| research_incumbent | Same decision rule as `atr_reclaim_0_35_shadow` for this MVP | no | Current research reference for future challengers. |

Capacity/path fields are explicit placeholders in this offline MVP. They require live decision-state logging before they can be treated as complete path attribution.

## Decision

- verdict: retest
- opportunity_set_hash: 9468fbe1bab35767
- opportunity_set_path: `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-07-30\paper_shadow_opportunity_set_2026-07-03_2026-07-25_demo_9468fbe1bab35767_v1.json`
- config_action: do_not_modify_settings_toml

## Variant Summary

| Variant | Opportunities | Accepted | Filtered | Accepted Loser | Accepted Winner Path | Filtered Loser | Missed Winner | Total Decision R | Direct Filter R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| atr_reclaim_0_35_shadow | 95 | 75 | 20 | 12 | 19 | 10 | 0 | 50.14 | 10.00 |
| reference_baseline | 95 | 80 | 15 | 15 | 19 | 7 | 0 | 44.14 | n/a |
| research_incumbent | 95 | 75 | 20 | 12 | 19 | 10 | 0 | 50.14 | n/a |

## Outcome Counts

### atr_reclaim_0_35_shadow

| Outcome | Count |
|---|---:|
| accepted_loser | 12 |
| accepted_neutral | 27 |
| accepted_right_censored | 17 |
| accepted_winner_path | 19 |
| filtered_loser | 10 |
| filtered_neutral | 5 |
| filtered_right_censored | 5 |

### reference_baseline

| Outcome | Count |
|---|---:|
| accepted_loser | 15 |
| accepted_neutral | 27 |
| accepted_right_censored | 19 |
| accepted_winner_path | 19 |
| filtered_loser | 7 |
| filtered_neutral | 5 |
| filtered_right_censored | 3 |

### research_incumbent

| Outcome | Count |
|---|---:|
| accepted_loser | 12 |
| accepted_neutral | 27 |
| accepted_right_censored | 17 |
| accepted_winner_path | 19 |
| filtered_loser | 10 |
| filtered_neutral | 5 |
| filtered_right_censored | 5 |

## Detail Rows

| Variant | Source | Symbol | Time | Regime | Accepted | Outcome | PnL_R | MFE_R | MAE_R | Reclaim Margin ATR | Capacity State | Active Positions | Direct Filter R | Path/Capacity R | Reason |
|---|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|---:|---:|---|
| reference_baseline | RECLAIM_PENDING | `ONDOUSDT` | 2026-07-03 00:10 | n/a | true | accepted_loser | -1.00 | 0.04 | -1.43 | n/a | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | RECLAIM_PENDING | `ONDOUSDT` | 2026-07-03 00:10 | n/a | false | filtered_loser | 1.00 | 0.04 | -1.43 | n/a | not_available_in_offline_opportunity_set | n/a | 1.00 | n/a | atr_reclaim_0_35_shadow: atr_reclaim_0_35_shadow condition not met |
| research_incumbent | RECLAIM_PENDING | `ONDOUSDT` | 2026-07-03 00:10 | n/a | false | filtered_loser | 1.00 | 0.04 | -1.43 | n/a | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: atr_reclaim_0_35_shadow condition not met |
| reference_baseline | WATCH_ONLY | `ADAUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.83 | -0.39 | 0.25 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `ADAUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.83 | -0.39 | 0.25 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `ADAUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.83 | -0.39 | 0.25 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `BTCUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.14 | 0.05 | 0.74 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `BTCUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.14 | 0.05 | 0.74 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `BTCUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.14 | 0.05 | 0.74 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `SOLUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.35 | -0.69 | 1.07 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `SOLUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.35 | -0.69 | 1.07 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `SOLUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.35 | -0.69 | 1.07 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `XRPUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.52 | -0.46 | -0.19 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `XRPUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.52 | -0.46 | -0.19 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `XRPUSDT` | 2026-07-03 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.52 | -0.46 | -0.19 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `NEARUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.50 | -0.96 | -0.12 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `NEARUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.50 | -0.96 | -0.12 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `NEARUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.50 | -0.96 | -0.12 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `PEPEUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.60 | -0.25 | 0.16 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `PEPEUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.60 | -0.25 | 0.16 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `PEPEUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.60 | -0.25 | 0.16 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `SOLUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.14 | -1.28 | 0.42 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `SOLUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.14 | -1.28 | 0.42 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `SOLUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.14 | -1.28 | 0.42 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `TLMUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.46 | -0.78 | 0.75 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `TLMUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.46 | -0.78 | 0.75 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `TLMUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.46 | -0.78 | 0.75 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `XLMUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.48 | -1.94 | 0.46 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `XLMUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.48 | -1.94 | 0.46 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `XLMUSDT` | 2026-07-04 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.48 | -1.94 | 0.46 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | REJECT | `BTCUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.01 | 3.01 | 0.01 | 0.41 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | REJECT | `BTCUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.01 | 3.01 | 0.01 | 0.41 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | REJECT | `BTCUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.01 | 3.01 | 0.01 | 0.41 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | REJECT | `ETHUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.55 | 3.55 | -0.41 | -0.17 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | REJECT | `ETHUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.55 | 3.55 | -0.41 | -0.17 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | REJECT | `ETHUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.55 | 3.55 | -0.41 | -0.17 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | REJECT | `SOLUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.77 | -1.94 | -0.16 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | REJECT | `SOLUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.77 | -1.94 | -0.16 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | REJECT | `SOLUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.77 | -1.94 | -0.16 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `TRXUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.77 | -0.95 | 0.23 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `TRXUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.77 | -0.95 | 0.23 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `TRXUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.77 | -0.95 | 0.23 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `ZECUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.02 | 3.02 | -0.26 | -0.09 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `ZECUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.02 | 3.02 | -0.26 | -0.09 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `ZECUSDT` | 2026-07-08 20:06 | RISK_OFF | true | accepted_winner_path | 3.02 | 3.02 | -0.26 | -0.09 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | REJECT | `BNBUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.37 | -0.28 | 0.60 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | REJECT | `BNBUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.37 | -0.28 | 0.60 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | REJECT | `BNBUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.37 | -0.28 | 0.60 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `BTCUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 1.67 | 1.67 | -0.27 | -0.24 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `BTCUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 1.67 | 1.67 | -0.27 | -0.24 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `BTCUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 1.67 | 1.67 | -0.27 | -0.24 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | REJECT | `ETHUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 3.37 | 3.37 | -0.02 | -0.19 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | REJECT | `ETHUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 3.37 | 3.37 | -0.02 | -0.19 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | REJECT | `ETHUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 3.37 | 3.37 | -0.02 | -0.19 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `TRXUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.19 | -1.03 | 0.08 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `TRXUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.19 | -1.03 | 0.08 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `TRXUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.19 | -1.03 | 0.08 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `ZECUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 3.54 | 3.54 | 0.25 | -0.09 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `ZECUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 3.54 | 3.54 | 0.25 | -0.09 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `ZECUSDT` | 2026-07-09 20:06 | RISK_OFF | true | accepted_winner_path | 3.54 | 3.54 | 0.25 | -0.09 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `BNBUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.24 | -0.62 | -0.28 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `BNBUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.24 | -0.62 | -0.28 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `BNBUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.24 | -0.62 | -0.28 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `BTCUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.91 | -0.47 | 0.81 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `BTCUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.91 | -0.47 | 0.81 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `BTCUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.91 | -0.47 | 0.81 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `ETHUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_winner_path | 1.74 | 1.74 | -0.06 | 0.77 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `ETHUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_winner_path | 1.74 | 1.74 | -0.06 | 0.77 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `ETHUSDT` | 2026-07-10 20:05 | RISK_OFF | true | accepted_winner_path | 1.74 | 1.74 | -0.06 | 0.77 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `SOLUSDT` | 2026-07-10 20:05 | RISK_OFF | false | filtered_loser | 1.00 | -0.20 | -1.32 | -0.21 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `SOLUSDT` | 2026-07-10 20:05 | RISK_OFF | false | filtered_loser | 1.00 | -0.20 | -1.32 | -0.21 | not_available_in_offline_opportunity_set | n/a | 1.00 | n/a | atr_reclaim_0_35_shadow: atr_reclaim_0_35_shadow condition not met |
| research_incumbent | WATCH_ONLY | `SOLUSDT` | 2026-07-10 20:05 | RISK_OFF | false | filtered_loser | 1.00 | -0.20 | -1.32 | -0.21 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: atr_reclaim_0_35_shadow condition not met |
| reference_baseline | WATCH_ONLY | `BNBUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_neutral | n/a | 0.14 | -0.68 | 0.63 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `BNBUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_neutral | n/a | 0.14 | -0.68 | 0.63 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `BNBUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_neutral | n/a | 0.14 | -0.68 | 0.63 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `BTCUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_neutral | n/a | 0.80 | -0.54 | 0.61 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `BTCUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_neutral | n/a | 0.80 | -0.54 | 0.61 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `BTCUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_neutral | n/a | 0.80 | -0.54 | 0.61 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `ETHUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.56 | 1.56 | -0.18 | 0.66 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `ETHUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.56 | 1.56 | -0.18 | 0.66 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `ETHUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.56 | 1.56 | -0.18 | 0.66 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `SOLUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_loser | -1.00 | 0.43 | -1.84 | 0.83 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `SOLUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_loser | -1.00 | 0.43 | -1.84 | 0.83 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `SOLUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_loser | -1.00 | 0.43 | -1.84 | 0.83 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `ZECUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.50 | 1.50 | -0.45 | 0.51 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `ZECUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.50 | 1.50 | -0.45 | 0.51 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `ZECUSDT` | 2026-07-11 22:27 | RISK_OFF | true | accepted_winner_path | 1.50 | 1.50 | -0.45 | 0.51 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `BNBUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.18 | -0.90 | 0.36 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `BNBUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.18 | -0.90 | 0.36 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `BNBUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 0.18 | -0.90 | 0.36 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `BTCUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.01 | -0.73 | -0.35 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `BTCUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.01 | -0.73 | -0.35 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `BTCUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.01 | -0.73 | -0.35 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `ETHUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.38 | -0.31 | -0.11 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `ETHUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.38 | -0.31 | -0.11 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `ETHUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.38 | -0.31 | -0.11 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | REJECT | `SOLUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_loser | -1.00 | 0.59 | -1.28 | -0.24 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | REJECT | `SOLUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_loser | -1.00 | 0.59 | -1.28 | -0.24 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | REJECT | `SOLUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_loser | -1.00 | 0.59 | -1.28 | -0.24 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `ZECUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.21 | -0.66 | 0.77 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `ZECUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.21 | -0.66 | 0.77 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `ZECUSDT` | 2026-07-12 20:05 | RISK_OFF | true | accepted_neutral | n/a | 1.21 | -0.66 | 0.77 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `DEXEUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.12 | -4.06 | 0.25 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `DEXEUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.12 | -4.06 | 0.25 | not_available_in_offline_opportunity_set | n/a | 1.00 | n/a | atr_reclaim_0_35_shadow: atr_reclaim_0_35_shadow condition not met |
| research_incumbent | WATCH_ONLY | `DEXEUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.12 | -4.06 | 0.25 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: atr_reclaim_0_35_shadow condition not met |
| reference_baseline | REJECT | `ETHUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_winner_path | 4.19 | 4.19 | -0.27 | -0.22 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | REJECT | `ETHUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_winner_path | 4.19 | 4.19 | -0.27 | -0.22 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | REJECT | `ETHUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_winner_path | 4.19 | 4.19 | -0.27 | -0.22 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | REJECT | `TRXUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_neutral | n/a | 0.58 | -0.94 | -0.56 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | REJECT | `TRXUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_neutral | n/a | 0.58 | -0.94 | -0.56 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | REJECT | `TRXUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_neutral | n/a | 0.58 | -0.94 | -0.56 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `WLDUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.14 | -1.64 | 0.15 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `WLDUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.14 | -1.64 | 0.15 | not_available_in_offline_opportunity_set | n/a | 1.00 | n/a | atr_reclaim_0_35_shadow: atr_reclaim_0_35_shadow condition not met |
| research_incumbent | WATCH_ONLY | `WLDUSDT` | 2026-07-13 20:07 | RISK_OFF | false | filtered_loser | 1.00 | -0.14 | -1.64 | 0.15 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: atr_reclaim_0_35_shadow condition not met |
| reference_baseline | WATCH_ONLY | `ZECUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_winner_path | 3.37 | 3.37 | -1.38 | 0.46 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `ZECUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_winner_path | 3.37 | 3.37 | -1.38 | 0.46 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `ZECUSDT` | 2026-07-13 20:07 | RISK_OFF | true | accepted_winner_path | 3.37 | 3.37 | -1.38 | 0.46 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | REJECT | `BNBUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.34 | -0.37 | 0.98 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | REJECT | `BNBUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.34 | -0.37 | 0.98 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | REJECT | `BNBUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_neutral | n/a | 1.34 | -0.37 | 0.98 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `ETHUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 1.77 | 1.77 | 0.32 | -0.24 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `ETHUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 1.77 | 1.77 | 0.32 | -0.24 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `ETHUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 1.77 | 1.77 | 0.32 | -0.24 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `NEARUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.59 | -1.29 | -0.05 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `NEARUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.59 | -1.29 | -0.05 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `NEARUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.59 | -1.29 | -0.05 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `SXTUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.47 | -1.44 | 0.75 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `SXTUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.47 | -1.44 | 0.75 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `SXTUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.47 | -1.44 | 0.75 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `ZECUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 4.03 | 4.03 | -1.40 | 0.51 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `ZECUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 4.03 | 4.03 | -1.40 | 0.51 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `ZECUSDT` | 2026-07-14 20:06 | RISK_OFF | true | accepted_winner_path | 4.03 | 4.03 | -1.40 | 0.51 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `BNBUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.09 | -0.70 | -0.18 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `BNBUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.09 | -0.70 | -0.18 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `BNBUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.09 | -0.70 | -0.18 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `BTCUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.65 | -0.45 | 0.47 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `BTCUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.65 | -0.45 | 0.47 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `BTCUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.65 | -0.45 | 0.47 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `ETHUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.70 | -0.19 | 1.09 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `ETHUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.70 | -0.19 | 1.09 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `ETHUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.70 | -0.19 | 1.09 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `NEARUSDT` | 2026-07-15 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.03 | -1.20 | 0.25 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `NEARUSDT` | 2026-07-15 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.03 | -1.20 | 0.25 | not_available_in_offline_opportunity_set | n/a | 1.00 | n/a | atr_reclaim_0_35_shadow: atr_reclaim_0_35_shadow condition not met |
| research_incumbent | WATCH_ONLY | `NEARUSDT` | 2026-07-15 20:06 | RISK_OFF | false | filtered_loser | 1.00 | 0.03 | -1.20 | 0.25 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: atr_reclaim_0_35_shadow condition not met |
| reference_baseline | WATCH_ONLY | `BTCUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.77 | -0.41 | -0.01 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `BTCUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.77 | -0.41 | -0.01 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `BTCUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.77 | -0.41 | -0.01 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `ETHUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.34 | -0.36 | -0.18 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `ETHUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.34 | -0.36 | -0.18 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `ETHUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.34 | -0.36 | -0.18 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `ONDOUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.61 | -0.44 | 0.25 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `ONDOUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.61 | -0.44 | 0.25 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `ONDOUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.61 | -0.44 | 0.25 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `XRPUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.58 | -0.40 | -0.22 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `XRPUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.58 | -0.40 | -0.22 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `XRPUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.58 | -0.40 | -0.22 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `ZECUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.16 | -1.12 | -0.09 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `ZECUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.16 | -1.12 | -0.09 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `ZECUSDT` | 2026-07-16 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 0.16 | -1.12 | -0.09 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | REJECT | `BTCUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_winner_path | 2.57 | 2.57 | 0.59 | 0.27 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | REJECT | `BTCUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_winner_path | 2.57 | 2.57 | 0.59 | 0.27 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | REJECT | `BTCUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_winner_path | 2.57 | 2.57 | 0.59 | 0.27 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `ETHUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_winner_path | 2.03 | 2.03 | -0.02 | -0.21 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `ETHUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_winner_path | 2.03 | 2.03 | -0.02 | -0.21 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `ETHUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_winner_path | 2.03 | 2.03 | -0.02 | -0.21 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `ONDOUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.53 | -0.54 | 0.25 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `ONDOUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.53 | -0.54 | 0.25 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `ONDOUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_neutral | n/a | 0.53 | -0.54 | 0.25 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `ZECUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.01 | -2.46 | 0.09 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `ZECUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.01 | -2.46 | 0.09 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `ZECUSDT` | 2026-07-17 20:06 | RISK_OFF | true | accepted_loser | -1.00 | 1.01 | -2.46 | 0.09 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `BTCUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.86 | -0.12 | -0.34 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `BTCUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.86 | -0.12 | -0.34 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `BTCUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.86 | -0.12 | -0.34 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | REJECT | `SOLUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_winner_path | 2.73 | 2.73 | -0.11 | 1.40 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | REJECT | `SOLUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_winner_path | 2.73 | 2.73 | -0.11 | 1.40 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | REJECT | `SOLUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_winner_path | 2.73 | 2.73 | -0.11 | 1.40 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | REJECT | `XRPUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_winner_path | 3.31 | 3.31 | 0.43 | 1.08 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | REJECT | `XRPUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_winner_path | 3.31 | 3.31 | 0.43 | 1.08 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | REJECT | `XRPUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_winner_path | 3.31 | 3.31 | 0.43 | 1.08 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `ZECUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_loser | -1.00 | 0.39 | -2.28 | -0.11 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `ZECUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_loser | -1.00 | 0.39 | -2.28 | -0.11 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `ZECUSDT` | 2026-07-18 20:05 | RISK_OFF | true | accepted_loser | -1.00 | 0.39 | -2.28 | -0.11 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `BANKUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.24 | -0.27 | 0.75 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `BANKUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.24 | -0.27 | 0.75 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `BANKUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.24 | -0.27 | 0.75 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `BTCUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.73 | -0.18 | -0.28 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `BTCUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.73 | -0.18 | -0.28 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `BTCUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.73 | -0.18 | -0.28 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `ETHUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.78 | -0.15 | -0.03 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `ETHUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.78 | -0.15 | -0.03 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `ETHUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.78 | -0.15 | -0.03 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | REJECT | `SOLUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.60 | -0.62 | -0.31 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | REJECT | `SOLUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.60 | -0.62 | -0.31 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | REJECT | `SOLUSDT` | 2026-07-19 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.60 | -0.62 | -0.31 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `ZECUSDT` | 2026-07-19 20:05 | RISK_OFF | false | filtered_loser | 1.00 | -0.15 | -1.99 | -0.15 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `ZECUSDT` | 2026-07-19 20:05 | RISK_OFF | false | filtered_loser | 1.00 | -0.15 | -1.99 | -0.15 | not_available_in_offline_opportunity_set | n/a | 1.00 | n/a | atr_reclaim_0_35_shadow: atr_reclaim_0_35_shadow condition not met |
| research_incumbent | WATCH_ONLY | `ZECUSDT` | 2026-07-19 20:05 | RISK_OFF | false | filtered_loser | 1.00 | -0.15 | -1.99 | -0.15 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: atr_reclaim_0_35_shadow condition not met |
| reference_baseline | WATCH_ONLY | `BANKUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.33 | -0.61 | 0.75 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `BANKUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.33 | -0.61 | 0.75 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `BANKUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.33 | -0.61 | 0.75 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `BTCUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.67 | -0.32 | -0.13 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `BTCUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.67 | -0.32 | -0.13 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `BTCUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.67 | -0.32 | -0.13 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `ETHUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.75 | -0.30 | 0.01 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `ETHUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.75 | -0.30 | 0.01 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `ETHUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.75 | -0.30 | 0.01 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `SOLUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.41 | -0.89 | -0.22 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `SOLUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.41 | -0.89 | -0.22 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `SOLUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 0.41 | -0.89 | -0.22 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `XRPUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.25 | -0.44 | -0.34 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `XRPUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.25 | -0.44 | -0.34 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `XRPUSDT` | 2026-07-20 20:05 | RISK_OFF | true | accepted_right_censored | n/a | 1.25 | -0.44 | -0.34 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `BANKUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_winner_path | 2.55 | 2.55 | 0.02 | -0.01 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `BANKUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_winner_path | 2.55 | 2.55 | 0.02 | -0.01 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `BANKUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_winner_path | 2.55 | 2.55 | 0.02 | -0.01 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `BTCUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.26 | -0.47 | 0.90 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `BTCUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.26 | -0.47 | 0.90 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `BTCUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.26 | -0.47 | 0.90 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `ETHUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.32 | -0.57 | 0.86 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `ETHUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.32 | -0.57 | 0.86 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `ETHUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.32 | -0.57 | 0.86 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `SOLUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.16 | -0.98 | 0.49 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `SOLUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.16 | -0.98 | 0.49 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `SOLUSDT` | 2026-07-21 20:06 | RISK_OFF | true | accepted_right_censored | n/a | 0.16 | -0.98 | 0.49 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `BANKUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_winner_path | 2.62 | 2.62 | 1.10 | 0.60 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `BANKUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_winner_path | 2.62 | 2.62 | 1.10 | 0.60 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `BANKUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_winner_path | 2.62 | 2.62 | 1.10 | 0.60 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `BTCUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.00 | -0.53 | -0.23 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `BTCUSDT` | 2026-07-22 20:05 | NEUTRAL | false | filtered_right_censored | n/a | 0.00 | -0.53 | -0.23 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: atr_reclaim_0_35_shadow condition not met |
| research_incumbent | WATCH_ONLY | `BTCUSDT` | 2026-07-22 20:05 | NEUTRAL | false | filtered_right_censored | n/a | 0.00 | -0.53 | -0.23 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: atr_reclaim_0_35_shadow condition not met |
| reference_baseline | WATCH_ONLY | `ETHUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.09 | -0.63 | -0.01 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `ETHUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.09 | -0.63 | -0.01 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `ETHUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.09 | -0.63 | -0.01 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `SOLUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_loser | -1.00 | 0.08 | -1.13 | -0.26 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `SOLUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_loser | -1.00 | 0.08 | -1.13 | -0.26 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `SOLUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_loser | -1.00 | 0.08 | -1.13 | -0.26 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `XRPUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.10 | -0.69 | 0.14 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `XRPUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.10 | -0.69 | 0.14 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `XRPUSDT` | 2026-07-22 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.10 | -0.69 | 0.14 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `BANKUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.94 | 0.23 | 0.75 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `BANKUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.94 | 0.23 | 0.75 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `BANKUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.94 | 0.23 | 0.75 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `BTCUSDT` | 2026-07-23 20:05 | NEUTRAL | true | accepted_loser | -1.00 | 0.07 | -1.05 | 0.34 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `BTCUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | 0.07 | -1.05 | 0.34 | not_available_in_offline_opportunity_set | n/a | 1.00 | n/a | atr_reclaim_0_35_shadow: atr_reclaim_0_35_shadow condition not met |
| research_incumbent | WATCH_ONLY | `BTCUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | 0.07 | -1.05 | 0.34 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: atr_reclaim_0_35_shadow condition not met |
| reference_baseline | WATCH_ONLY | `ETHUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | -0.51 | -1.08 | -0.21 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `ETHUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | -0.51 | -1.08 | -0.21 | not_available_in_offline_opportunity_set | n/a | 1.00 | n/a | atr_reclaim_0_35_shadow: atr_reclaim_0_35_shadow condition not met |
| research_incumbent | WATCH_ONLY | `ETHUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | -0.51 | -1.08 | -0.21 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: atr_reclaim_0_35_shadow condition not met |
| reference_baseline | WATCH_ONLY | `SOLUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | -0.89 | -1.99 | -0.27 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `SOLUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | -0.89 | -1.99 | -0.27 | not_available_in_offline_opportunity_set | n/a | 1.00 | n/a | atr_reclaim_0_35_shadow: atr_reclaim_0_35_shadow condition not met |
| research_incumbent | WATCH_ONLY | `SOLUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | -0.89 | -1.99 | -0.27 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: atr_reclaim_0_35_shadow condition not met |
| reference_baseline | WATCH_ONLY | `XRPUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | -0.50 | -1.08 | -0.27 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `XRPUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | -0.50 | -1.08 | -0.27 | not_available_in_offline_opportunity_set | n/a | 1.00 | n/a | atr_reclaim_0_35_shadow: atr_reclaim_0_35_shadow condition not met |
| research_incumbent | WATCH_ONLY | `XRPUSDT` | 2026-07-23 20:05 | NEUTRAL | false | filtered_loser | 1.00 | -0.50 | -1.08 | -0.27 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: atr_reclaim_0_35_shadow condition not met |
| reference_baseline | WATCH_ONLY | `BANKUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.43 | 0.24 | 0.75 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `BANKUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.43 | 0.24 | 0.75 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: close >= entry_high + 0.35 ATR |
| research_incumbent | WATCH_ONLY | `BANKUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.43 | 0.24 | 0.75 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: close >= entry_high + 0.35 ATR |
| reference_baseline | WATCH_ONLY | `BNBUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.06 | -0.14 | -0.12 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `BNBUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.06 | -0.14 | -0.12 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: atr_reclaim_0_35_shadow condition not met |
| research_incumbent | WATCH_ONLY | `BNBUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.06 | -0.14 | -0.12 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: atr_reclaim_0_35_shadow condition not met |
| reference_baseline | WATCH_ONLY | `BTCUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.59 | -0.76 | 0.00 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `BTCUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.59 | -0.76 | 0.00 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: atr_reclaim_0_35_shadow condition not met |
| research_incumbent | WATCH_ONLY | `BTCUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.59 | -0.76 | 0.00 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: atr_reclaim_0_35_shadow condition not met |
| reference_baseline | WATCH_ONLY | `ETHUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.28 | -0.46 | 0.24 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `ETHUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.28 | -0.46 | 0.24 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: atr_reclaim_0_35_shadow condition not met |
| research_incumbent | WATCH_ONLY | `ETHUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | -0.28 | -0.46 | 0.24 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: atr_reclaim_0_35_shadow condition not met |
| reference_baseline | WATCH_ONLY | `VANAUSDT` | 2026-07-24 20:05 | NEUTRAL | true | accepted_right_censored | n/a | 0.07 | -0.86 | 0.25 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `VANAUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | 0.07 | -0.86 | 0.25 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: atr_reclaim_0_35_shadow condition not met |
| research_incumbent | WATCH_ONLY | `VANAUSDT` | 2026-07-24 20:05 | NEUTRAL | false | filtered_right_censored | n/a | 0.07 | -0.86 | 0.25 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: atr_reclaim_0_35_shadow condition not met |
| reference_baseline | WATCH_ONLY | `BANKUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | 0.75 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `BANKUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | 0.75 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: missing 4h path |
| research_incumbent | WATCH_ONLY | `BANKUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | 0.75 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: missing 4h path |
| reference_baseline | REJECT | `BNBUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | 1.83 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | REJECT | `BNBUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | 1.83 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: missing 4h path |
| research_incumbent | REJECT | `BNBUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | 1.83 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: missing 4h path |
| reference_baseline | REJECT | `BTCUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | 0.02 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | REJECT | `BTCUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | 0.02 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: missing 4h path |
| research_incumbent | REJECT | `BTCUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | 0.02 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: missing 4h path |
| reference_baseline | WATCH_ONLY | `ETHUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | -0.16 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | WATCH_ONLY | `ETHUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | -0.16 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: missing 4h path |
| research_incumbent | WATCH_ONLY | `ETHUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | -0.16 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: missing 4h path |
| reference_baseline | REJECT | `XRPUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | -0.23 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | reference baseline: first 4h close >= entry_high |
| atr_reclaim_0_35_shadow | REJECT | `XRPUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | -0.23 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | atr_reclaim_0_35_shadow: missing 4h path |
| research_incumbent | REJECT | `XRPUSDT` | 2026-07-25 20:05 | NEUTRAL | false | filtered_neutral | n/a | n/a | n/a | -0.23 | not_available_in_offline_opportunity_set | n/a | n/a | n/a | research_incumbent: missing 4h path |

## Raw Summary

```json
{
  "experiment": "atr_reclaim_incumbent_shadow",
  "opportunity_set_hash": "9468fbe1bab35767",
  "opportunities": 95,
  "summary": [
    {
      "variant": "atr_reclaim_0_35_shadow",
      "opportunities": 95,
      "accepted": 75,
      "filtered": 20,
      "accepted_loser": 12,
      "accepted_winner_path": 19,
      "filtered_loser": 10,
      "missed_winner": 0,
      "total_decision_R": 50.13786778393428,
      "direct_filter_R": 10.0,
      "outcomes": {
        "filtered_loser": 10,
        "accepted_neutral": 27,
        "accepted_loser": 12,
        "accepted_winner_path": 19,
        "accepted_right_censored": 17,
        "filtered_right_censored": 5,
        "filtered_neutral": 5
      }
    },
    {
      "variant": "reference_baseline",
      "opportunities": 95,
      "accepted": 80,
      "filtered": 15,
      "accepted_loser": 15,
      "accepted_winner_path": 19,
      "filtered_loser": 7,
      "missed_winner": 0,
      "total_decision_R": 44.13786778393428,
      "direct_filter_R": null,
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
      "variant": "research_incumbent",
      "opportunities": 95,
      "accepted": 75,
      "filtered": 20,
      "accepted_loser": 12,
      "accepted_winner_path": 19,
      "filtered_loser": 10,
      "missed_winner": 0,
      "total_decision_R": 50.13786778393428,
      "direct_filter_R": null,
      "outcomes": {
        "filtered_loser": 10,
        "accepted_neutral": 27,
        "accepted_loser": 12,
        "accepted_winner_path": 19,
        "accepted_right_censored": 17,
        "filtered_right_censored": 5,
        "filtered_neutral": 5
      }
    }
  ]
}
```
