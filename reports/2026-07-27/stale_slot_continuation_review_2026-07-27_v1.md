---
created: 2026-07-27 00:50:07 CST
tags:
  - crypto
  - trading-system
  - stale-slot-continuation-review
experiment: stale_slot_continuation_review
source_run_id: 110c51eef593
replay_run_id: 8e24e6bda89b
verdict: stale_slot_continuation_weak_retest
---

# stale_slot_continuation_review

## Plain-language conclusion

Pre-TP1 stale slots show negative average continuation after the stale time, supporting further capacity replacement research but not deployment.

This report is diagnostic only. It does not compare blocked candidates, does not calculate replacement outcome, and does not change `config/settings.toml`, backtest behavior, paper state, strategy defaults, or saved backtest rows.

## Scope

| Field | Value |
|---|---:|
| source_run_id | `110c51eef593` |
| replay_run_id | `8e24e6bda89b` |
| window | `2025-06-01T00:00:00+00:00` -> `2026-06-01T00:00:00+00:00` |
| source_commit_hash | `b9cb5e23eeb069e2b6b2552e3d1e9d54f4c5f036` |
| stale_threshold | 42 bars = 168h |

## Sample Definition

A slot is included only if it was an entered position that reached the stale threshold while still pre-TP1 and still open. `forward_R_*` is incremental R from the stale-time close, not whole-trade R.

| Metric | Value |
|---|---:|
| total_entered_trades | 58 |
| eligible_pre_tp1_stale_slots | 26 |
| excluded_tp1_before_stale | 13 |
| excluded_closed_before_stale | 19 |
| excluded_insufficient_price_data | 0 |
| right_censored_count | 1 |

## Continuation R Summary

| Metric | n | mean | median | positive_pct | min | max |
|---|---:|---:|---:|---:|---:|---:|
| forward_R_24 | 26 | -0.282 | -0.262 | 26.923 | -1.340 | 1.224 |
| forward_R_42 | 26 | -0.132 | -0.548 | 26.923 | -1.340 | 2.924 |
| forward_R_60 | 26 | -0.191 | -0.504 | 30.769 | -2.048 | 2.924 |
| eventual_continuation_R | 26 | -0.129 | -0.916 | 38.462 | -2.048 | 2.924 |
| MFE_R_after_stale | 26 | 1.140 | 0.840 | 100.000 | 0.008 | 3.299 |
| MAE_R_after_stale | 26 | -1.334 | -1.043 | 0.000 | -4.645 | -0.088 |

## First Hit After Stale

| Outcome | Count |
|---|---:|
| `not_hit_by_end` | 1 |
| `stop` | 15 |
| `tp1` | 10 |

## First Observations

| # | Symbol | Stale Time | Status | forward_R_42 | eventual_R | MFE_R | MAE_R | First Hit | Censored |
|---:|---|---|---|---:|---:|---:|---:|---|---|
| 1 | `BTCUSDT` | `2025-06-15T16:00:00+00:00` | `STOPPED` | -0.948 | -0.968 | 0.483 | -0.981 | `stop` | false |
| 2 | `APTUSDT` | `2025-07-03T20:00:00+00:00` | `STOPPED` | -0.063 | -1.001 | 0.974 | -4.273 | `stop` | false |
| 3 | `WUSDT` | `2025-07-05T04:00:00+00:00` | `STOPPED` | 1.241 | 1.382 | 2.094 | -0.377 | `tp1` | false |
| 4 | `SEIUSDT` | `2025-07-04T20:00:00+00:00` | `STOPPED` | 2.172 | 1.493 | 2.572 | -0.308 | `tp1` | false |
| 5 | `BTCUSDT` | `2025-07-05T04:00:00+00:00` | `CLOSED` | 2.924 | 2.924 | 3.299 | -0.233 | `tp1` | false |
| 6 | `WIFUSDT` | `2025-07-06T00:00:00+00:00` | `STOPPED` | 0.950 | 0.950 | 2.449 | -0.236 | `tp1` | false |
| 7 | `TAOUSDT` | `2025-07-22T08:00:00+00:00` | `STOPPED` | -0.476 | -1.567 | 0.706 | -1.735 | `stop` | false |
| 8 | `LINKUSDT` | `2025-07-26T00:00:00+00:00` | `STOPPED` | -0.958 | 1.203 | 1.917 | -1.236 | `tp1` | false |
| 9 | `CRVUSDT` | `2025-07-28T16:00:00+00:00` | `STOPPED` | -0.473 | -1.157 | 0.479 | -1.235 | `stop` | false |
| 10 | `BCHUSDT` | `2025-08-13T16:00:00+00:00` | `STOPPED` | -1.116 | -1.903 | 0.540 | -2.312 | `stop` | false |
| 11 | `SEIUSDT` | `2025-08-15T20:00:00+00:00` | `STOPPED` | 0.208 | -1.256 | 1.109 | -1.332 | `stop` | false |
| 12 | `PENGUUSDT` | `2025-08-30T08:00:00+00:00` | `STOPPED` | -0.238 | -0.238 | 0.136 | -0.325 | `stop` | false |
| 13 | `ENAUSDT` | `2025-09-13T00:00:00+00:00` | `STOPPED` | -0.977 | -1.668 | 0.038 | -1.968 | `stop` | false |
| 14 | `BTCUSDT` | `2025-09-21T20:00:00+00:00` | `STOPPED` | -0.983 | -0.983 | 0.017 | -1.018 | `stop` | false |
| 15 | `SOLUSDT` | `2025-10-09T04:00:00+00:00` | `STOPPED` | -1.340 | -1.340 | 0.143 | -3.057 | `stop` | false |
| 16 | `LINKUSDT` | `2025-10-09T04:00:00+00:00` | `STOPPED` | -0.851 | -0.851 | 0.255 | -0.938 | `stop` | false |
| 17 | `PENGUUSDT` | `2025-10-09T12:00:00+00:00` | `STOPPED` | -0.865 | -0.865 | 0.166 | -4.645 | `stop` | false |
| 18 | `TRXUSDT` | `2026-01-23T12:00:00+00:00` | `STOPPED` | -0.983 | -0.983 | 0.008 | -0.962 | `stop` | false |
| 19 | `ROSEUSDT` | `2026-01-28T00:00:00+00:00` | `STOPPED` | -1.066 | -2.048 | 0.285 | -2.071 | `stop` | false |
| 20 | `TRXUSDT` | `2026-04-22T16:00:00+00:00` | `CLOSED` | -0.720 | 2.675 | 2.832 | -1.068 | `tp1` | false |
| 21 | `BNBUSDT` | `2026-04-22T12:00:00+00:00` | `STOPPED` | -0.470 | 0.835 | 1.324 | -0.912 | `tp1` | false |
| 22 | `AVAXUSDT` | `2026-04-22T20:00:00+00:00` | `STOPPED` | -0.621 | -1.038 | 1.492 | -1.130 | `stop` | false |
| 23 | `LINKUSDT` | `2026-04-22T20:00:00+00:00` | `STOPPED` | -0.637 | 0.626 | 1.389 | -0.817 | `tp1` | false |
| 24 | `DOGEUSDT` | `2026-04-23T00:00:00+00:00` | `CLOSED` | 2.378 | 2.378 | 2.944 | -0.088 | `tp1` | false |
| 25 | `ZBTUSDT` | `2026-05-06T12:00:00+00:00` | `ENTERED` | -0.388 | -1.217 | 0.145 | -1.295 | `not_hit_by_end` | true |
| 26 | `TRXUSDT` | `2026-05-18T00:00:00+00:00` | `STOPPED` | 0.866 | 1.265 | 1.848 | -0.125 | `tp1` | false |

## Decision

`stale_slot_continuation_weak_retest`

## Next Action

Proceed to `blocked_candidate_vs_stale_slot_review`, still as a diagnostic comparison only. Do not change `max_active_positions` or deploy replacement logic.

## Raw Summary

```json
{
  "source_run_id": "110c51eef593",
  "replay_run_id": "8e24e6bda89b",
  "report_date": "2026-07-27",
  "start_utc": "2025-06-01T00:00:00+00:00",
  "end_utc": "2026-06-01T00:00:00+00:00",
  "source_commit_hash": "b9cb5e23eeb069e2b6b2552e3d1e9d54f4c5f036",
  "stale_bars": 42,
  "stale_hours": 168,
  "total_entered_trades": 58,
  "eligible_pre_tp1_stale_slots": 26,
  "excluded_tp1_before_stale": 13,
  "excluded_closed_before_stale": 19,
  "excluded_insufficient_price_data": 0,
  "right_censored_count": 1,
  "first_hit_outcomes": {
    "not_hit_by_end": 1,
    "stop": 15,
    "tp1": 10
  },
  "forward_r_24_summary": {
    "n": 26,
    "mean": -0.2817617209475555,
    "median": -0.2623165158668908,
    "positive_pct": 26.923076923076923,
    "min": -1.340188998364123,
    "max": 1.2242828053330062
  },
  "forward_r_42_summary": {
    "n": 26,
    "mean": -0.1319978927248013,
    "median": -0.5480757989546478,
    "positive_pct": 26.923076923076923,
    "min": -1.340188998364123,
    "max": 2.9240866303594815
  },
  "forward_r_60_summary": {
    "n": 26,
    "mean": -0.19147494217114056,
    "median": -0.5043177044768581,
    "positive_pct": 30.76923076923077,
    "min": -2.0482265299347926,
    "max": 2.9240866303594815
  },
  "eventual_continuation_r_summary": {
    "n": 26,
    "mean": -0.12888278685385757,
    "median": -0.9162805632950137,
    "positive_pct": 38.46153846153847,
    "min": -2.0482265299347926,
    "max": 2.9240866303594815
  },
  "mfe_r_summary": {
    "n": 26,
    "mean": 1.1400348114750642,
    "median": 0.8396101526243487,
    "positive_pct": 100.0,
    "min": 0.007696741926552437,
    "max": 3.298609248951896
  },
  "mae_r_summary": {
    "n": 26,
    "mean": -1.3338010112793814,
    "median": -1.0428686737369022,
    "positive_pct": 0.0,
    "min": -4.645389863055026,
    "max": -0.08822792398340748
  },
  "verdict": "stale_slot_continuation_weak_retest",
  "reason": "Pre-TP1 stale slots show negative average continuation after the stale time, supporting further capacity replacement research but not deployment.",
  "observations": [
    {
      "trade_id": "af8d9ae15e1a",
      "symbol": "BTCUSDT",
      "entered_at_utc": "2025-06-08T16:00:00+00:00",
      "stale_time_utc": "2025-06-15T16:00:00+00:00",
      "closed_at_utc": "2025-06-22T20:00:00+00:00",
      "tp1_hit_at_utc": null,
      "final_status": "STOPPED",
      "entry_price": 105888.72504606054,
      "stop_loss": 98866.6761,
      "take_profit_1": 118919.42452389534,
      "stale_close": 105564.0,
      "risk_per_unit": 7022.048946060546,
      "forward_r_24": -0.2089233514703783,
      "forward_r_42": -0.9481264017299529,
      "forward_r_60": -0.9678358308671081,
      "eventual_continuation_r": -0.9678358308671081,
      "mfe_r_after_stale": 0.4825343750844868,
      "mae_r_after_stale": -0.9812435163764502,
      "first_hit_outcome_after_stale": "stop",
      "first_hit_time_utc": "2025-06-22T20:00:00+00:00",
      "right_censored": false,
      "horizon_24_censored": false,
      "horizon_42_censored": false,
      "horizon_60_censored": false
    },
    {
      "trade_id": "c5538b945895",
      "symbol": "APTUSDT",
      "entered_at_utc": "2025-06-26T20:00:00+00:00",
      "stale_time_utc": "2025-07-03T20:00:00+00:00",
      "closed_at_utc": "2025-10-11T00:00:00+00:00",
      "tp1_hit_at_utc": null,
      "final_status": "STOPPED",
      "entry_price": 4.7515796025,
      "stop_loss": 3.814905,
      "take_profit_1": 6.471687144052654,
      "stale_close": 4.749,
      "risk_per_unit": 0.9366746024999997,
      "forward_r_24": -0.30320027813501,
      "forward_r_42": -0.06298879017593444,
      "forward_r_60": 0.2658340466747102,
      "eventual_continuation_r": -1.0013188171182426,
      "mfe_r_after_stale": 0.9736572311941171,
      "mae_r_after_stale": -4.27256166583208,
      "first_hit_outcome_after_stale": "stop",
      "first_hit_time_utc": "2025-10-11T00:00:00+00:00",
      "right_censored": false,
      "horizon_24_censored": false,
      "horizon_42_censored": false,
      "horizon_60_censored": false
    },
    {
      "trade_id": "165449658820",
      "symbol": "WUSDT",
      "entered_at_utc": "2025-06-28T04:00:00+00:00",
      "stale_time_utc": "2025-07-05T04:00:00+00:00",
      "closed_at_utc": "2025-07-15T04:00:00+00:00",
      "tp1_hit_at_utc": "2025-07-13T12:00:00+00:00",
      "final_status": "STOPPED",
      "entry_price": 0.06753565094999998,
      "stop_loss": 0.058509,
      "take_profit_1": 0.0853291673520445,
      "stale_close": 0.0665,
      "risk_per_unit": 0.009026650949999986,
      "forward_r_24": -0.17725289355516807,
      "forward_r_42": 1.2407702548861734,
      "forward_r_60": 1.3816578795320698,
      "eventual_continuation_r": 1.3816578795320698,
      "mfe_r_after_stale": 2.093799805120417,
      "mae_r_after_stale": -0.3766623988047312,
      "first_hit_outcome_after_stale": "tp1",
      "first_hit_time_utc": "2025-07-13T12:00:00+00:00",
      "right_censored": false,
      "horizon_24_censored": false,
      "horizon_42_censored": false,
      "horizon_60_censored": false
    },
    {
      "trade_id": "055d9319a6fe",
      "symbol": "SEIUSDT",
      "entered_at_utc": "2025-06-27T20:00:00+00:00",
      "stale_time_utc": "2025-07-04T20:00:00+00:00",
      "closed_at_utc": "2025-07-14T00:00:00+00:00",
      "tp1_hit_at_utc": "2025-07-11T12:00:00+00:00",
      "final_status": "STOPPED",
      "entry_price": 0.27887306684999996,
      "stop_loss": 0.2418175,
      "take_profit_1": 0.3416787132021952,
      "stale_close": 0.26,
      "risk_per_unit": 0.03705556684999997,
      "forward_r_24": 0.008095949556361117,
      "forward_r_42": 2.172413130957139,
      "forward_r_60": 1.493452235299311,
      "eventual_continuation_r": 1.493452235299311,
      "mfe_r_after_stale": 2.571813309070998,
      "mae_r_after_stale": -0.3076460831417569,
      "first_hit_outcome_after_stale": "tp1",
      "first_hit_time_utc": "2025-07-11T12:00:00+00:00",
      "right_censored": false,
      "horizon_24_censored": false,
      "horizon_42_censored": false,
      "horizon_60_censored": false
    },
    {
      "trade_id": "299ae1c6986b",
      "symbol": "BTCUSDT",
      "entered_at_utc": "2025-06-28T04:00:00+00:00",
      "stale_time_utc": "2025-07-05T04:00:00+00:00",
      "closed_at_utc": "2025-07-11T08:00:00+00:00",
      "tp1_hit_at_utc": "2025-07-10T20:00:00+00:00",
      "final_status": "CLOSED",
      "entry_price": 107328.12814621799,
      "stop_loss": 104220.90955,
      "take_profit_1": 112731.24649500518,
      "stale_close": 108154.72,
      "risk_per_unit": 3107.2185962179938,
      "forward_r_24": 0.07134676661302049,
      "forward_r_42": 2.9240866303594815,
      "forward_r_60": 2.9240866303594815,
      "eventual_continuation_r": 2.9240866303594815,
      "mfe_r_after_stale": 3.298609248951896,
      "mae_r_after_stale": -0.23337592047196917,
      "first_hit_outcome_after_stale": "tp1",
      "first_hit_time_utc": "2025-07-10T20:00:00+00:00",
      "right_censored": false,
      "horizon_24_censored": false,
      "horizon_42_censored": false,
      "horizon_60_censored": false
    },
    {
      "trade_id": "81aed2c59363",
      "symbol": "WIFUSDT",
      "entered_at_utc": "2025-06-29T00:00:00+00:00",
      "stale_time_utc": "2025-07-06T00:00:00+00:00",
      "closed_at_utc": "2025-07-11T08:00:00+00:00",
      "tp1_hit_at_utc": "2025-07-10T20:00:00+00:00",
      "final_status": "STOPPED",
      "entry_price": 0.8298957404999998,
      "stop_loss": 0.73678,
      "take_profit_1": 1.004599480407024,
      "stale_close": 0.846,
      "risk_per_unit": 0.09311574049999982,
      "forward_r_24": 1.2242828053330062,
      "forward_r_42": 0.9504892882777439,
      "forward_r_60": 0.9504892882777439,
      "eventual_continuation_r": 0.9504892882777439,
      "mfe_r_after_stale": 2.448565610666013,
      "mae_r_after_stale": -0.2362651027835628,
      "first_hit_outcome_after_stale": "tp1",
      "first_hit_time_utc": "2025-07-10T20:00:00+00:00",
      "right_censored": false,
      "horizon_24_censored": false,
      "horizon_42_censored": false,
      "horizon_60_censored": false
    },
    {
      "trade_id": "f6bf4e8d500a",
      "symbol": "TAOUSDT",
      "entered_at_utc": "2025-07-15T08:00:00+00:00",
      "stale_time_utc": "2025-07-22T08:00:00+00:00",
      "closed_at_utc": "2025-07-30T12:00:00+00:00",
      "tp1_hit_at_utc": null,
      "final_status": "STOPPED",
      "entry_price": 406.16480875362015,
      "stop_loss": 367.8975,
      "take_profit_1": 469.96924400262014,
      "stale_close": 427.5,
      "risk_per_unit": 38.26730875362017,
      "forward_r_24": 0.023518769135152086,
      "forward_r_42": -0.4756017758441983,
      "forward_r_60": -1.5671443708287094,
      "eventual_continuation_r": -1.5671443708287094,
      "mfe_r_after_stale": 0.7055630740545804,
      "mae_r_after_stale": -1.7351625228601526,
      "first_hit_outcome_after_stale": "stop",
      "first_hit_time_utc": "2025-07-30T12:00:00+00:00",
      "right_censored": false,
      "horizon_24_censored": false,
      "horizon_42_censored": false,
      "horizon_60_censored": false
    },
    {
      "trade_id": "edd9beed2605",
      "symbol": "LINKUSDT",
      "entered_at_utc": "2025-07-19T00:00:00+00:00",
      "stale_time_utc": "2025-07-26T00:00:00+00:00",
      "closed_at_utc": "2025-08-12T00:00:00+00:00",
      "tp1_hit_at_utc": "2025-08-10T00:00:00+00:00",
      "final_status": "STOPPED",
      "entry_price": 17.642627920944726,
      "stop_loss": 15.33645,
      "take_profit_1": 21.611096479357336,
      "stale_close": 18.28,
      "risk_per_unit": 2.3061779209447266,
      "forward_r_24": -0.19512804971077868,
      "forward_r_42": -0.9582955330240407,
      "forward_r_60": -0.5073329292480221,
      "eventual_continuation_r": 1.2025892304665842,
      "mfe_r_after_stale": 1.9165910660480798,
      "mae_r_after_stale": -1.2358109815015912,
      "first_hit_outcome_after_stale": "tp1",
      "first_hit_time_utc": "2025-08-10T00:00:00+00:00",
      "right_censored": false,
      "horizon_24_censored": false,
      "horizon_42_censored": false,
      "horizon_60_censored": false
    },
    {
      "trade_id": "431fb87ee406",
      "symbol": "CRVUSDT",
      "entered_at_utc": "2025-07-21T16:00:00+00:00",
      "stale_time_utc": "2025-07-28T16:00:00+00:00",
      "closed_at_utc": "2025-08-25T20:00:00+00:00",
      "tp1_hit_at_utc": null,
      "final_status": "STOPPED",
      "entry_price": 0.9629600393999999,
      "stop_loss": 0.7918415,
      "take_profit_1": 1.2542363531715157,
      "stale_close": 0.989,
      "risk_per_unit": 0.17111853939999988,
      "forward_r_24": -0.4979004630283795,
      "forward_r_42": -0.47277168379103185,
      "forward_r_60": -0.40322924822720874,
      "eventual_continuation_r": -1.156802425932816,
      "mfe_r_after_stale": 0.4791999761540743,
      "mae_r_after_stale": -1.2354009141337972,
      "first_hit_outcome_after_stale": "stop",
      "first_hit_time_utc": "2025-08-25T20:00:00+00:00",
      "right_censored": false,
      "horizon_24_censored": false,
      "horizon_42_censored": false,
      "horizon_60_censored": false
    },
    {
      "trade_id": "9538bde4191d",
      "symbol": "BCHUSDT",
      "entered_at_utc": "2025-08-06T16:00:00+00:00",
      "stale_time_utc": "2025-08-13T16:00:00+00:00",
      "closed_at_utc": "2025-10-11T00:00:00+00:00",
      "tp1_hit_at_utc": null,
      "final_status": "STOPPED",
      "entry_price": 566.0281674410156,
      "stop_loss": 506.78249999999997,
      "take_profit_1": 672.1116602652379,
      "stale_close": 619.0,
      "risk_per_unit": 59.245667441015655,
      "forward_r_24": -0.5451875452691538,
      "forward_r_42": -1.1156933975941525,
      "forward_r_60": -0.501302479705694,
      "eventual_continuation_r": -1.9026586646564003,
      "mfe_r_after_stale": 0.5401238838579859,
      "mae_r_after_stale": -2.3124053777670026,
      "first_hit_outcome_after_stale": "stop",
      "first_hit_time_utc": "2025-10-11T00:00:00+00:00",
      "right_censored": false,
      "horizon_24_censored": false,
      "horizon_42_censored": false,
      "horizon_60_censored": false
    },
    {
      "trade_id": "caf9a9ed8a96",
      "symbol": "SEIUSDT",
      "entered_at_utc": "2025-08-08T20:00:00+00:00",
      "stale_time_utc": "2025-08-15T20:00:00+00:00",
      "closed_at_utc": "2025-08-26T00:00:00+00:00",
      "tp1_hit_at_utc": null,
      "final_status": "STOPPED",
      "entry_price": 0.30998161334999996,
      "stop_loss": 0.27491350000000003,
      "take_profit_1": 0.3755817114561339,
      "stale_close": 0.3187,
      "risk_per_unit": 0.03506811334999993,
      "forward_r_24": -0.40777785383769466,
      "forward_r_42": 0.208166316994069,
      "forward_r_60": -0.9353226297815666,
      "eventual_continuation_r": -1.2564523520339315,
      "mfe_r_after_stale": 1.10926982617387,
      "mae_r_after_stale": -1.3316941100853392,
      "first_hit_outcome_after_stale": "stop",
      "first_hit_time_utc": "2025-08-26T00:00:00+00:00",
      "right_censored": false,
      "horizon_24_censored": false,
      "horizon_42_censored": false,
      "horizon_60_censored": false
    },
    {
      "trade_id": "2bd86be332c1",
      "symbol": "PENGUUSDT",
      "entered_at_utc": "2025-08-23T08:00:00+00:00",
      "stale_time_utc": "2025-08-30T08:00:00+00:00",
      "closed_at_utc": "2025-09-01T04:00:00+00:00",
      "tp1_hit_at_utc": null,
      "final_status": "STOPPED",
      "entry_price": 0.03484458258449999,
      "stop_loss": 0.028195625000000002,
      "take_profit_1": 0.04677196563898836,
      "stale_close": 0.029748,
      "risk_per_unit": 0.006648957584499987,
      "forward_r_24": -0.237717056382585,
      "forward_r_42": -0.237717056382585,
      "forward_r_60": -0.237717056382585,
      "eventual_continuation_r": -0.237717056382585,
      "mfe_r_after_stale": 0.136261961139903,
      "mae_r_after_stale": -0.3250133532266337,
      "first_hit_outcome_after_stale": "stop",
      "first_hit_time_utc": "2025-09-01T04:00:00+00:00",
      "right_censored": false,
      "horizon_24_censored": false,
      "horizon_42_censored": false,
      "horizon_60_censored": false
    },
    {
      "trade_id": "10d7a06f95ff",
      "symbol": "ENAUSDT",
      "entered_at_utc": "2025-09-06T00:00:00+00:00",
      "stale_time_utc": "2025-09-13T00:00:00+00:00",
      "closed_at_utc": "2025-09-22T08:00:00+00:00",
      "tp1_hit_at_utc": null,
      "final_status": "STOPPED",
      "entry_price": 0.7069981248712413,
      "stop_loss": 0.5983875000000001,
      "take_profit_1": 0.8998410668174286,
      "stale_close": 0.779,
      "risk_per_unit": 0.10861062487124118,
      "forward_r_24": -0.7448626697057273,
      "forward_r_42": -0.9768841687982407,
      "forward_r_60": -1.6684453083188404,
      "eventual_continuation_r": -1.6684453083188404,
      "mfe_r_after_stale": 0.037749529614258065,
      "mae_r_after_stale": -1.9684998613483875,
      "first_hit_outcome_after_stale": "stop",
      "first_hit_time_utc": "2025-09-22T08:00:00+00:00",
      "right_censored": false,
      "horizon_24_censored": false,
      "horizon_42_censored": false,
      "horizon_60_censored": false
    },
    {
      "trade_id": "801e17aadd79",
      "symbol": "BTCUSDT",
      "entered_at_utc": "2025-09-14T20:00:00+00:00",
      "stale_time_utc": "2025-09-21T20:00:00+00:00",
      "closed_at_utc": "2025-09-23T04:00:00+00:00",
      "tp1_hit_at_utc": null,
      "final_status": "STOPPED",
      "entry_price": 115660.15781528388,
      "stop_loss": 111728.55,
      "take_profit_1": 123003.7752438071,
      "stale_close": 115480.05,
      "risk_per_unit": 3931.6078152838745,
      "forward_r_24": -0.9826078112323272,
      "forward_r_42": -0.9826078112323272,
      "forward_r_60": -0.9826078112323272,
      "eventual_continuation_r": -0.9826078112323272,
      "mfe_r_after_stale": 0.01662932903577756,
      "mae_r_after_stale": -1.0179168899914912,
      "first_hit_outcome_after_stale": "stop",
      "first_hit_time_utc": "2025-09-23T04:00:00+00:00",
      "right_censored": false,
      "horizon_24_censored": false,
      "horizon_42_censored": false,
      "horizon_60_censored": false
    },
    {
      "trade_id": "3796e72b5b4c",
      "symbol": "SOLUSDT",
      "entered_at_utc": "2025-10-02T04:00:00+00:00",
      "stale_time_utc": "2025-10-09T04:00:00+00:00",
      "closed_at_utc": "2025-10-11T00:00:00+00:00",
      "tp1_hit_at_utc": null,
      "final_status": "STOPPED",
      "entry_price": 220.00328187186128,
      "stop_loss": 201.22565,
      "take_profit_1": 253.36435561839022,
      "stale_close": 226.19,
      "risk_per_unit": 18.777631871861274,
      "forward_r_24": -1.340188998364123,
      "forward_r_42": -1.340188998364123,
      "forward_r_60": -1.340188998364123,
      "eventual_continuation_r": -1.340188998364123,
      "mfe_r_after_stale": 0.14272300246848754,
      "mae_r_after_stale": -3.0568284857056582,
      "first_hit_outcome_after_stale": "stop",
      "first_hit_time_utc": "2025-10-11T00:00:00+00:00",
      "right_censored": false,
      "horizon_24_censored": false,
      "horizon_42_censored": false,
      "horizon_60_censored": false
    },
    {
      "trade_id": "54d0ef55337d",
      "symbol": "LINKUSDT",
      "entered_at_utc": "2025-10-02T04:00:00+00:00",
      "stale_time_utc": "2025-10-09T04:00:00+00:00",
      "closed_at_utc": "2025-10-10T20:00:00+00:00",
      "tp1_hit_at_utc": null,
      "final_status": "STOPPED",
      "entry_price": 22.58984973151334,
      "stop_loss": 20.586499999999997,
      "take_profit_1": 26.162984035216965,
      "stale_close": 22.27,
      "risk_per_unit": 2.0033497315133424,
      "forward_r_24": -0.8506185780716008,
      "forward_r_42": -0.8506185780716008,
      "forward_r_60": -0.8506185780716008,
      "eventual_continuation_r": -0.8506185780716008,
      "mfe_r_after_stale": 0.2545736233556906,
      "mae_r_after_stale": -0.9384282586445033,
      "first_hit_outcome_after_stale": "stop",
      "first_hit_time_utc": "2025-10-10T20:00:00+00:00",
      "right_censored": false,
      "horizon_24_censored": false,
      "horizon_42_censored": false,
      "horizon_60_censored": false
    },
    {
      "trade_id": "017fea1ab0b5",
      "symbol": "PENGUUSDT",
      "entered_at_utc": "2025-10-02T12:00:00+00:00",
      "stale_time_utc": "2025-10-09T12:00:00+00:00",
      "closed_at_utc": "2025-10-11T00:00:00+00:00",
      "tp1_hit_at_utc": null,
      "final_status": "STOPPED",
      "entry_price": 0.031566143447238404,
      "stop_loss": 0.02617736,
      "take_profit_1": 0.04135028354410988,
      "stale_close": 0.030811,
      "risk_per_unit": 0.005388783447238404,
      "forward_r_24": -0.8647252957229195,
      "forward_r_42": -0.8647252957229195,
      "forward_r_60": -0.8647252957229195,
      "eventual_continuation_r": -0.8647252957229195,
      "mfe_r_after_stale": 0.16627129458304205,
      "mae_r_after_stale": -4.645389863055026,
      "first_hit_outcome_after_stale": "stop",
      "first_hit_time_utc": "2025-10-11T00:00:00+00:00",
      "right_censored": false,
      "horizon_24_censored": false,
      "horizon_42_censored": false,
      "horizon_60_censored": false
    },
    {
      "trade_id": "57ddf5cc601b",
      "symbol": "TRXUSDT",
      "entered_at_utc": "2026-01-16T12:00:00+00:00",
      "stale_time_utc": "2026-01-23T12:00:00+00:00",
      "closed_at_utc": "2026-01-24T16:00:00+00:00",
      "tp1_hit_at_utc": null,
      "final_status": "STOPPED",
      "entry_price": 0.3070150104614728,
      "stop_loss": 0.29402249999999996,
      "take_profit_1": 0.3301837837539259,
      "stale_close": 0.3065,
      "risk_per_unit": 0.012992510461472817,
      "forward_r_24": -0.9829911269166879,
      "forward_r_42": -0.9829911269166879,
      "forward_r_60": -0.9829911269166879,
      "eventual_continuation_r": -0.9829911269166879,
      "mfe_r_after_stale": 0.007696741926552437,
      "mae_r_after_stale": -0.9620927408191615,
      "first_hit_outcome_after_stale": "stop",
      "first_hit_time_utc": "2026-01-24T16:00:00+00:00",
      "right_censored": false,
      "horizon_24_censored": false,
      "horizon_42_censored": false,
      "horizon_60_censored": false
    },
    {
      "trade_id": "2d1ee7f56922",
      "symbol": "ROSEUSDT",
      "entered_at_utc": "2026-01-21T00:00:00+00:00",
      "stale_time_utc": "2026-01-28T00:00:00+00:00",
      "closed_at_utc": "2026-02-06T04:00:00+00:00",
      "tp1_hit_at_utc": null,
      "final_status": "STOPPED",
      "entry_price": 0.016517634689999998,
      "stop_loss": 0.01182,
      "take_profit_1": 0.025298312288683775,
      "stale_close": 0.02143,
      "risk_per_unit": 0.004697634689999997,
      "forward_r_24": -0.8472348879048326,
      "forward_r_42": -1.0664941679405053,
      "forward_r_60": -2.0482265299347926,
      "eventual_continuation_r": -2.0482265299347926,
      "mfe_r_after_stale": 0.28524993713378727,
      "mae_r_after_stale": -2.0712551405311608,
      "first_hit_outcome_after_stale": "stop",
      "first_hit_time_utc": "2026-02-06T04:00:00+00:00",
      "right_censored": false,
      "horizon_24_censored": false,
      "horizon_42_censored": false,
      "horizon_60_censored": false
    },
    {
      "trade_id": "c9cbcef3f5e6",
      "symbol": "TRXUSDT",
      "entered_at_utc": "2026-04-15T16:00:00+00:00",
      "stale_time_utc": "2026-04-22T16:00:00+00:00",
      "closed_at_utc": "2026-05-09T08:00:00+00:00",
      "tp1_hit_at_utc": "2026-05-03T08:00:00+00:00",
      "final_status": "CLOSED",
      "entry_price": 0.3222396806001747,
      "stop_loss": 0.313624,
      "take_profit_1": 0.33850376476244337,
      "stale_close": 0.329,
      "risk_per_unit": 0.008615680600174702,
      "forward_r_24": -0.60355069335957,
      "forward_r_42": -0.7196181343902558,
      "forward_r_60": 0.39462929950432657,
      "eventual_continuation_r": 2.674648286343603,
      "mfe_r_after_stale": 2.8320455611487283,
      "mae_r_after_stale": -1.0678204574823131,
      "first_hit_outcome_after_stale": "tp1",
      "first_hit_time_utc": "2026-05-03T08:00:00+00:00",
      "right_censored": false,
      "horizon_24_censored": false,
      "horizon_42_censored": false,
      "horizon_60_censored": false
    },
    {
      "trade_id": "aa18af0cc2c6",
      "symbol": "BNBUSDT",
      "entered_at_utc": "2026-04-15T12:00:00+00:00",
      "stale_time_utc": "2026-04-22T12:00:00+00:00",
      "closed_at_utc": "2026-05-15T16:00:00+00:00",
      "tp1_hit_at_utc": "2026-05-13T04:00:00+00:00",
      "final_status": "STOPPED",
      "entry_price": 615.9185379862191,
      "stop_loss": 580.2635,
      "take_profit_1": 680.8346745575873,
      "stale_close": 642.77,
      "risk_per_unit": 35.6550379862191,
      "forward_r_24": -0.2869159753511966,
      "forward_r_42": -0.46977933403055083,
      "forward_r_60": -0.7603413579443725,
      "eventual_continuation_r": 0.8353774571736912,
      "mfe_r_after_stale": 1.3240765587810341,
      "mae_r_after_stale": -0.9117926059303405,
      "first_hit_outcome_after_stale": "tp1",
      "first_hit_time_utc": "2026-05-13T04:00:00+00:00",
      "right_censored": false,
      "horizon_24_censored": false,
      "horizon_42_censored": false,
      "horizon_60_censored": false
    },
    {
      "trade_id": "092302e9ce81",
      "symbol": "AVAXUSDT",
      "entered_at_utc": "2026-04-15T20:00:00+00:00",
      "stale_time_utc": "2026-04-22T20:00:00+00:00",
      "closed_at_utc": "2026-05-28T08:00:00+00:00",
      "tp1_hit_at_utc": null,
      "final_status": "STOPPED",
      "entry_price": 9.463019144999997,
      "stop_loss": 8.7862,
      "take_profit_1": 10.61171795748248,
      "stale_close": 9.48,
      "risk_per_unit": 0.6768191449999978,
      "forward_r_24": 0.0,
      "forward_r_42": -0.6205498220650972,
      "forward_r_60": -0.4580248686670964,
      "eventual_continuation_r": -1.0380708128461746,
      "mfe_r_after_stale": 1.4922745721089243,
      "mae_r_after_stale": -1.1302871759042854,
      "first_hit_outcome_after_stale": "stop",
      "first_hit_time_utc": "2026-05-28T08:00:00+00:00",
      "right_censored": false,
      "horizon_24_censored": false,
      "horizon_42_censored": false,
      "horizon_60_censored": false
    },
    {
      "trade_id": "6be62d7c6c06",
      "symbol": "LINKUSDT",
      "entered_at_utc": "2026-04-15T20:00:00+00:00",
      "stale_time_utc": "2026-04-22T20:00:00+00:00",
      "closed_at_utc": "2026-05-08T04:00:00+00:00",
      "tp1_hit_at_utc": "2026-05-06T12:00:00+00:00",
      "final_status": "STOPPED",
      "entry_price": 9.171480483870994,
      "stop_loss": 8.55965,
      "take_profit_1": 10.214253297166012,
      "stale_close": 9.41,
      "risk_per_unit": 0.6118304838709943,
      "forward_r_24": 0.1307551717492851,
      "forward_r_42": -0.6374314622777653,
      "forward_r_60": -0.39226551524785536,
      "eventual_continuation_r": 0.6259323119633109,
      "mfe_r_after_stale": 1.3892736998361526,
      "mae_r_after_stale": -0.8172198234330312,
      "first_hit_outcome_after_stale": "tp1",
      "first_hit_time_utc": "2026-05-06T12:00:00+00:00",
      "right_censored": false,
      "horizon_24_censored": false,
      "horizon_42_censored": false,
      "horizon_60_censored": false
    },
    {
      "trade_id": "11d2a7d7cd65",
      "symbol": "DOGEUSDT",
      "entered_at_utc": "2026-04-16T00:00:00+00:00",
      "stale_time_utc": "2026-04-23T00:00:00+00:00",
      "closed_at_utc": "2026-04-29T12:00:00+00:00",
      "tp1_hit_at_utc": "2026-04-29T08:00:00+00:00",
      "final_status": "CLOSED",
      "entry_price": 0.09469629723195296,
      "stop_loss": 0.0891425,
      "take_profit_1": 0.10392883915497722,
      "stale_close": 0.09565,
      "risk_per_unit": 0.005553797231952956,
      "forward_r_24": 0.642803446164821,
      "forward_r_42": 2.378124069297105,
      "forward_r_60": 2.378124069297105,
      "eventual_continuation_r": 2.378124069297105,
      "mfe_r_after_stale": 2.9439317492422448,
      "mae_r_after_stale": -0.08822792398340748,
      "first_hit_outcome_after_stale": "tp1",
      "first_hit_time_utc": "2026-04-29T08:00:00+00:00",
      "right_censored": false,
      "horizon_24_censored": false,
      "horizon_42_censored": false,
      "horizon_60_censored": false
    },
    {
      "trade_id": "4293c40fe29d",
      "symbol": "ZBTUSDT",
      "entered_at_utc": "2026-04-29T12:00:00+00:00",
      "stale_time_utc": "2026-05-06T12:00:00+00:00",
      "closed_at_utc": null,
      "tp1_hit_at_utc": null,
      "final_status": "ENTERED",
      "entry_price": 0.17149840634999997,
      "stop_loss": 0.118988,
      "take_profit_1": 0.27412250000000005,
      "stale_close": 0.1879,
      "risk_per_unit": 0.05251040634999997,
      "forward_r_24": -0.19043844249359945,
      "forward_r_42": -0.38849442268694256,
      "forward_r_60": -0.5636977897810542,
      "eventual_continuation_r": -1.2169016475340997,
      "mfe_r_after_stale": 0.1447332162951354,
      "mae_r_after_stale": -1.2949814089564753,
      "first_hit_outcome_after_stale": "not_hit_by_end",
      "first_hit_time_utc": null,
      "right_censored": true,
      "horizon_24_censored": false,
      "horizon_42_censored": false,
      "horizon_60_censored": false
    },
    {
      "trade_id": "7de1ba038b8e",
      "symbol": "TRXUSDT",
      "entered_at_utc": "2026-05-11T00:00:00+00:00",
      "stale_time_utc": "2026-05-18T00:00:00+00:00",
      "closed_at_utc": "2026-05-27T16:00:00+00:00",
      "tp1_hit_at_utc": "2026-05-25T16:00:00+00:00",
      "final_status": "STOPPED",
      "entry_price": 0.35075652257558076,
      "stop_loss": 0.3387415,
      "take_profit_1": 0.372809944574682,
      "stale_close": 0.3553,
      "risk_per_unit": 0.012015022575580792,
      "forward_r_24": 0.8406143173236423,
      "forward_r_42": 0.8655830594223662,
      "forward_r_60": 1.2653957798481617,
      "eventual_continuation_r": 1.2653957798481617,
      "mfe_r_after_stale": 1.8476869153054318,
      "mae_r_after_stale": -0.12484371049361039,
      "first_hit_outcome_after_stale": "tp1",
      "first_hit_time_utc": "2026-05-25T16:00:00+00:00",
      "right_censored": false,
      "horizon_24_censored": false,
      "horizon_42_censored": false,
      "horizon_60_censored": false
    }
  ]
}
```
