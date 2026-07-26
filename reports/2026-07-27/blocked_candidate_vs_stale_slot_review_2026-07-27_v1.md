---
created: 2026-07-27 01:04:30 CST
tags:
  - crypto
  - trading-system
  - blocked-candidate-vs-stale-slot-review
experiment: blocked_candidate_vs_stale_slot_review
source_run_id: 110c51eef593
replay_run_id: e40da6f04438
verdict: replacement_edge_not_supported
---

# blocked_candidate_vs_stale_slot_review

## Plain-language conclusion

Rank-1 blocked candidates do not show a broad enough 42-bar net replacement edge over oldest eligible pre-TP1 stale slots.

This report is diagnostic only. It does not deploy replacement logic, does not change `max_active_positions`, and does not modify `config/settings.toml`, backtest behavior, paper state, strategy defaults, or saved backtest rows.

## Scope

| Field | Value |
|---|---:|
| source_run_id | `110c51eef593` |
| replay_run_id | `e40da6f04438` |
| window | `2025-06-01T00:00:00+00:00` -> `2026-06-01T00:00:00+00:00` |
| source_commit_hash | `b9cb5e23eeb069e2b6b2552e3d1e9d54f4c5f036` |
| stale_threshold | 42 bars |

## Sample Definition

Primary sample uses only `candidate_rank=1` blocked events. The replacement slot is the oldest active slot that is still pre-TP1 and has `holding_bars >= stale_bars`. Post-TP1 slots are excluded from V1 eligibility. Oracle is reported only as an upper bound.

| Metric | Value |
|---|---:|
| total_blocked_events | 512 |
| rank1_blocked_events | 46 |
| eligible_comparison_events | 42 |
| rank1_without_eligible_stale_slot | 4 |
| same_bar_stop_possible_events | 0 |
| same_bar_tp1_possible_events | 1 |
| right_censored_count | 0 |

## Net Replacement Delta R

`net_replacement_delta_R = candidate_R - selected_stale_slot_R`; each leg is normalized by its own per-unit risk, so this is a path-quality diagnostic rather than a full portfolio PnL simulation.

| Metric | n | mean | median | positive_pct | min | max |
|---|---:|---:|---:|---:|---:|---:|
| net_replacement_delta_R_24 | 42 | 0.436 | 0.145 | 59.524 | -1.528 | 3.445 |
| net_replacement_delta_R_42 | 42 | 0.309 | -0.223 | 42.857 | -1.595 | 3.545 |
| net_replacement_delta_R_60 | 42 | 0.176 | -0.432 | 45.238 | -1.918 | 3.522 |
| lowest_unrealized_slot_delta_R_42 | 42 | 0.221 | -0.276 | 35.714 | -1.017 | 3.545 |
| oracle_upper_bound_delta_R_42 | 42 | 0.756 | 0.434 | 78.571 | -0.570 | 4.428 |

## Robustness

| Metric | Value |
|---|---:|
| positive_n | 18 |
| top1_positive_contribution_share_pct | 14.657 |
| top3_positive_contribution_share_pct | 43.369 |
| 20pct_trimmed_mean_R_42 | 0.001 |

## First-Hit Pairs

| Candidate vs Stale Slot | Count |
|---|---:|
| `stop vs stop` | 27 |
| `stop vs tp1` | 6 |
| `tp1 vs stop` | 9 |

## Month Leave-One-Out

| Removed Month | Mean R42 |
|---|---:|
| 2025-07 | -0.054 |
| 2025-08 | 0.487 |
| 2025-09 | 0.355 |
| 2025-10 | 0.201 |
| 2026-04 | 0.332 |
| 2026-05 | 0.485 |

## First Events

| # | Time | Candidate | Slot | Slot Bars | Delta R42 | Candidate R42 | Slot R42 | Candidate Hit | Slot Hit | Same-bar Flags |
|---:|---|---|---|---:|---:|---:|---:|---|---|---|
| 1 | `2025-07-06T00:00:00+00:00` | `UNIUSDT` | `APTUSDT` | 55 | 1.334 | 1.742 | 0.408 | `tp1` | `stop` | none |
| 2 | `2025-07-06T12:00:00+00:00` | `XRPUSDT` | `APTUSDT` | 58 | 1.181 | 1.729 | 0.548 | `tp1` | `stop` | none |
| 3 | `2025-07-16T08:00:00+00:00` | `ENAUSDT` | `APTUSDT` | 117 | 1.267 | 1.569 | 0.302 | `tp1` | `stop` | none |
| 4 | `2025-07-20T20:00:00+00:00` | `PENGUUSDT` | `APTUSDT` | 144 | 2.066 | 1.502 | -0.564 | `tp1` | `stop` | none |
| 5 | `2025-07-21T08:00:00+00:00` | `PENGUUSDT` | `APTUSDT` | 147 | 2.114 | 1.502 | -0.612 | `tp1` | `stop` | tp1 |
| 6 | `2025-07-23T00:00:00+00:00` | `LDOUSDT` | `APTUSDT` | 157 | -0.052 | -1.000 | -0.948 | `stop` | `stop` | none |
| 7 | `2025-07-26T00:00:00+00:00` | `BNBUSDT` | `APTUSDT` | 175 | 0.031 | -0.528 | -0.559 | `stop` | `stop` | none |
| 8 | `2025-07-26T04:00:00+00:00` | `BNBUSDT` | `APTUSDT` | 176 | 0.184 | -0.383 | -0.567 | `stop` | `stop` | none |
| 9 | `2025-07-27T00:00:00+00:00` | `ETHUSDT` | `APTUSDT` | 181 | -0.271 | -1.000 | -0.729 | `stop` | `stop` | none |
| 10 | `2025-07-27T04:00:00+00:00` | `ETHUSDT` | `APTUSDT` | 182 | -0.280 | -1.000 | -0.720 | `stop` | `stop` | none |
| 11 | `2025-07-27T20:00:00+00:00` | `CFXUSDT` | `APTUSDT` | 186 | 3.506 | 2.824 | -0.682 | `tp1` | `stop` | none |
| 12 | `2025-07-28T00:00:00+00:00` | `CFXUSDT` | `APTUSDT` | 187 | 3.545 | 2.824 | -0.722 | `tp1` | `stop` | none |
| 13 | `2025-08-09T04:00:00+00:00` | `LTCUSDT` | `APTUSDT` | 260 | -0.256 | -0.340 | -0.084 | `stop` | `stop` | none |
| 14 | `2025-08-09T08:00:00+00:00` | `LTCUSDT` | `APTUSDT` | 261 | -0.280 | -0.447 | -0.167 | `stop` | `stop` | none |
| 15 | `2025-08-10T16:00:00+00:00` | `LTCUSDT` | `APTUSDT` | 269 | -0.315 | -0.076 | 0.239 | `stop` | `stop` | none |
| 16 | `2025-08-10T20:00:00+00:00` | `LTCUSDT` | `APTUSDT` | 270 | -0.369 | -0.250 | 0.120 | `stop` | `stop` | none |
| 17 | `2025-08-11T04:00:00+00:00` | `LTCUSDT` | `APTUSDT` | 272 | -0.504 | -0.679 | -0.175 | `stop` | `stop` | none |
| 18 | `2025-08-12T20:00:00+00:00` | `SOLUSDT` | `APTUSDT` | 282 | 2.179 | 1.643 | -0.536 | `tp1` | `stop` | none |
| 19 | `2025-08-13T20:00:00+00:00` | `TAOUSDT` | `APTUSDT` | 288 | -0.481 | -1.000 | -0.519 | `stop` | `stop` | none |
| 20 | `2025-08-14T00:00:00+00:00` | `TAOUSDT` | `APTUSDT` | 289 | -0.405 | -1.000 | -0.595 | `stop` | `stop` | none |
| 21 | `2025-08-23T20:00:00+00:00` | `LINKUSDT` | `APTUSDT` | 348 | -0.507 | -1.000 | -0.493 | `stop` | `stop` | none |
| 22 | `2025-08-24T00:00:00+00:00` | `LINKUSDT` | `APTUSDT` | 349 | -0.541 | -1.000 | -0.459 | `stop` | `stop` | none |
| 23 | `2025-08-24T20:00:00+00:00` | `LINKUSDT` | `APTUSDT` | 354 | -0.610 | -1.000 | -0.390 | `stop` | `stop` | none |
| 24 | `2025-09-18T16:00:00+00:00` | `PEPEUSDT` | `APTUSDT` | 503 | -0.384 | -1.000 | -0.616 | `stop` | `stop` | none |
| 25 | `2025-09-18T20:00:00+00:00` | `PEPEUSDT` | `APTUSDT` | 504 | -0.251 | -1.000 | -0.749 | `stop` | `stop` | none |
| 26 | `2025-09-19T00:00:00+00:00` | `PEPEUSDT` | `APTUSDT` | 505 | -0.195 | -1.000 | -0.805 | `stop` | `stop` | none |
| 27 | `2025-10-02T16:00:00+00:00` | `ADAUSDT` | `APTUSDT` | 587 | -0.410 | -0.522 | -0.112 | `stop` | `stop` | none |
| 28 | `2025-10-05T04:00:00+00:00` | `ADAUSDT` | `APTUSDT` | 602 | 0.558 | -1.000 | -1.558 | `stop` | `stop` | none |
| 29 | `2025-10-05T12:00:00+00:00` | `LTCUSDT` | `APTUSDT` | 604 | 3.439 | 1.595 | -1.844 | `tp1` | `stop` | none |
| 30 | `2025-10-05T20:00:00+00:00` | `BNBUSDT` | `APTUSDT` | 606 | 0.701 | -1.000 | -1.701 | `stop` | `stop` | none |
| 31 | `2025-10-06T00:00:00+00:00` | `BNBUSDT` | `APTUSDT` | 607 | 0.758 | -1.000 | -1.758 | `stop` | `stop` | none |
| 32 | `2025-10-08T12:00:00+00:00` | `FORMUSDT` | `APTUSDT` | 622 | 0.471 | -1.000 | -1.471 | `stop` | `stop` | none |
| 33 | `2025-10-09T04:00:00+00:00` | `BNBUSDT` | `APTUSDT` | 626 | 0.331 | -1.000 | -1.331 | `stop` | `stop` | none |
| 34 | `2025-10-09T08:00:00+00:00` | `BNBUSDT` | `APTUSDT` | 627 | 0.315 | -1.000 | -1.315 | `stop` | `stop` | none |
| 35 | `2025-10-09T12:00:00+00:00` | `BNBUSDT` | `APTUSDT` | 628 | 0.208 | -1.000 | -1.208 | `stop` | `stop` | none |
| 36 | `2026-04-30T20:00:00+00:00` | `APEUSDT` | `BNBUSDT` | 92 | -0.619 | 0.089 | 0.708 | `stop` | `tp1` | none |
| 37 | `2026-05-01T00:00:00+00:00` | `APEUSDT` | `BNBUSDT` | 93 | -0.458 | 0.149 | 0.607 | `stop` | `tp1` | none |
| 38 | `2026-05-01T16:00:00+00:00` | `APEUSDT` | `BNBUSDT` | 97 | -0.306 | 0.341 | 0.648 | `stop` | `tp1` | none |
| 39 | `2026-05-02T08:00:00+00:00` | `PENGUUSDT` | `BNBUSDT` | 101 | -0.570 | 0.379 | 0.950 | `stop` | `tp1` | none |
| 40 | `2026-05-08T20:00:00+00:00` | `TAOUSDT` | `BNBUSDT` | 140 | -1.595 | -0.677 | 0.918 | `stop` | `tp1` | none |

## Decision

`replacement_edge_not_supported`

## Next Action

Do not proceed to shadow replacement yet. Revisit capacity only if a stronger, pre-declared slot selection rule or broader walk-forward evidence appears.

## Raw Summary

```json
{
  "source_run_id": "110c51eef593",
  "replay_run_id": "e40da6f04438",
  "report_date": "2026-07-27",
  "start_utc": "2025-06-01T00:00:00+00:00",
  "end_utc": "2026-06-01T00:00:00+00:00",
  "source_commit_hash": "b9cb5e23eeb069e2b6b2552e3d1e9d54f4c5f036",
  "stale_bars": 42,
  "total_blocked_events": 512,
  "rank1_blocked_events": 46,
  "eligible_comparison_events": 42,
  "rank1_without_eligible_stale_slot": 4,
  "same_bar_stop_possible_events": 0,
  "same_bar_tp1_possible_events": 1,
  "right_censored_count": 0,
  "net_delta_r_24_summary": {
    "n": 42,
    "mean": 0.43558545902365525,
    "median": 0.14498185196782087,
    "positive_pct": 59.523809523809526,
    "min": -1.5276862855919346,
    "max": 3.445081430544437
  },
  "net_delta_r_42_summary": {
    "n": 42,
    "mean": 0.3094469476994779,
    "median": -0.2227823856257483,
    "positive_pct": 42.857142857142854,
    "min": -1.5951655252867416,
    "max": 3.545436452180673
  },
  "net_delta_r_60_summary": {
    "n": 42,
    "mean": 0.17591457716553738,
    "median": -0.43203328180343115,
    "positive_pct": 45.23809523809524,
    "min": -1.9183744123409228,
    "max": 3.5219491066913413
  },
  "lowest_unrealized_delta_r_42_summary": {
    "n": 42,
    "mean": 0.22135586582748168,
    "median": -0.2756289129767449,
    "positive_pct": 35.714285714285715,
    "min": -1.0171394598244237,
    "max": 3.545436452180673
  },
  "oracle_upper_bound_delta_r_42_summary": {
    "n": 42,
    "mean": 0.7564846992172173,
    "median": 0.4338111057501878,
    "positive_pct": 78.57142857142857,
    "min": -0.5701660766976773,
    "max": 4.428302405936089
  },
  "first_hit_pair_counts": {
    "stop vs stop": 27,
    "stop vs tp1": 6,
    "tp1 vs stop": 9
  },
  "month_leave_one_out_mean_r_42": {
    "2025-07": -0.05429033444244962,
    "2025-08": 0.48667789242324494,
    "2025-09": 0.35452121945746623,
    "2025-10": 0.20075760315655833,
    "2026-04": 0.3320958177282809,
    "2026-05": 0.48495270542155894
  },
  "top_contribution_share_r_42": {
    "positive_n": 18,
    "top1_share_pct": 14.656999406310167,
    "top3_share_pct": 43.36850895737347,
    "trimmed_mean_20pct": 0.0007945929765473087
  },
  "verdict": "replacement_edge_not_supported",
  "reason": "Rank-1 blocked candidates do not show a broad enough 42-bar net replacement edge over oldest eligible pre-TP1 stale slots.",
  "events": [
    {
      "event_id": "77e44fa92b9c",
      "decision_time_utc": "2025-07-06T00:00:00+00:00",
      "month": "2025-07",
      "candidate_symbol": "UNIUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 55,
      "eligible_stale_slots": 5,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": 1.7415987849159418,
      "stale_slot_r_42": 0.4078257262238523,
      "net_replacement_delta_r_42": 1.3337730586920895,
      "net_replacement_delta_r_24": 0.9983264061877499,
      "net_replacement_delta_r_60": 1.022031927651868,
      "lowest_unrealized_slot_delta_r_42": -0.40865069108675023,
      "oracle_upper_bound_delta_r_42": 1.3337730586920895,
      "candidate_first_hit": "tp1",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "a791e8103d4a",
      "decision_time_utc": "2025-07-06T12:00:00+00:00",
      "month": "2025-07",
      "candidate_symbol": "XRPUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 58,
      "eligible_stale_slots": 5,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": 1.728690635579612,
      "stale_slot_r_42": 0.5476821925466908,
      "net_replacement_delta_r_42": 1.181008443032921,
      "net_replacement_delta_r_24": 1.3337359774266393,
      "net_replacement_delta_r_60": 0.9375941352343921,
      "lowest_unrealized_slot_delta_r_42": -0.437750739535804,
      "oracle_upper_bound_delta_r_42": 1.181008443032921,
      "candidate_first_hit": "tp1",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "b93e70fb08d5",
      "decision_time_utc": "2025-07-16T08:00:00+00:00",
      "month": "2025-07",
      "candidate_symbol": "ENAUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 117,
      "eligible_stale_slots": 1,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": 1.569120862247298,
      "stale_slot_r_42": 0.3021326715218582,
      "net_replacement_delta_r_42": 1.2669881907254399,
      "net_replacement_delta_r_24": 1.4527517414137907,
      "net_replacement_delta_r_60": 2.068760757202174,
      "lowest_unrealized_slot_delta_r_42": 1.2669881907254399,
      "oracle_upper_bound_delta_r_42": 1.2669881907254399,
      "candidate_first_hit": "tp1",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "3a8b9ffa6f51",
      "decision_time_utc": "2025-07-20T20:00:00+00:00",
      "month": "2025-07",
      "candidate_symbol": "PENGUUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 144,
      "eligible_stale_slots": 1,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": 1.5024984583917806,
      "stale_slot_r_42": -0.5636962917439631,
      "net_replacement_delta_r_42": 2.0661947501357436,
      "net_replacement_delta_r_24": 2.235944201626823,
      "net_replacement_delta_r_60": 2.4932373953963207,
      "lowest_unrealized_slot_delta_r_42": 2.0661947501357436,
      "oracle_upper_bound_delta_r_42": 2.0661947501357436,
      "candidate_first_hit": "tp1",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "2076e1f3fabf",
      "decision_time_utc": "2025-07-21T08:00:00+00:00",
      "month": "2025-07",
      "candidate_symbol": "PENGUUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 147,
      "eligible_stale_slots": 1,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": true,
      "candidate_r_42": 1.5024984583917806,
      "stale_slot_r_42": -0.611738589335778,
      "net_replacement_delta_r_42": 2.1142370477275585,
      "net_replacement_delta_r_24": 2.43345142505984,
      "net_replacement_delta_r_60": 2.5007106416883804,
      "lowest_unrealized_slot_delta_r_42": 2.1142370477275585,
      "oracle_upper_bound_delta_r_42": 2.1142370477275585,
      "candidate_first_hit": "tp1",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "2aefa8b4e9c3",
      "decision_time_utc": "2025-07-23T00:00:00+00:00",
      "month": "2025-07",
      "candidate_symbol": "LDOUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 157,
      "eligible_stale_slots": 2,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -1.0,
      "stale_slot_r_42": -0.9480346724784824,
      "net_replacement_delta_r_42": -0.05196532752151761,
      "net_replacement_delta_r_24": 0.05700373145688509,
      "net_replacement_delta_r_60": 0.3270350201472447,
      "lowest_unrealized_slot_delta_r_42": -0.05196532752151761,
      "oracle_upper_bound_delta_r_42": 0.7822000611304583,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "d2c055788e00",
      "decision_time_utc": "2025-07-26T00:00:00+00:00",
      "month": "2025-07",
      "candidate_symbol": "BNBUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 175,
      "eligible_stale_slots": 3,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -0.5279469199297545,
      "stale_slot_r_42": -0.5594258652913559,
      "net_replacement_delta_r_42": 0.03147894536160134,
      "net_replacement_delta_r_24": 0.6162147097534958,
      "net_replacement_delta_r_60": -0.5868362407103915,
      "lowest_unrealized_slot_delta_r_42": 0.03147894536160134,
      "oracle_upper_bound_delta_r_42": 1.0269703694751593,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "b2bd5a7ae0a9",
      "decision_time_utc": "2025-07-26T04:00:00+00:00",
      "month": "2025-07",
      "candidate_symbol": "BNBUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 176,
      "eligible_stale_slots": 3,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -0.38324601680694603,
      "stale_slot_r_42": -0.5668991115834165,
      "net_replacement_delta_r_42": 0.18365309477647052,
      "net_replacement_delta_r_24": 0.6702363698489068,
      "net_replacement_delta_r_60": -0.4854136124610037,
      "lowest_unrealized_slot_delta_r_42": 0.18365309477647052,
      "oracle_upper_bound_delta_r_42": 1.093275375480792,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "d69ecfc1f2ac",
      "decision_time_utc": "2025-07-27T00:00:00+00:00",
      "month": "2025-07",
      "candidate_symbol": "ETHUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 181,
      "eligible_stale_slots": 3,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -1.0,
      "stale_slot_r_42": -0.7291753167824363,
      "net_replacement_delta_r_42": -0.2708246832175637,
      "net_replacement_delta_r_24": 0.5935408316768089,
      "net_replacement_delta_r_60": -0.4523178074533092,
      "lowest_unrealized_slot_delta_r_42": -0.2708246832175637,
      "oracle_upper_bound_delta_r_42": 0.5313985202697615,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "59a90687501a",
      "decision_time_utc": "2025-07-27T04:00:00+00:00",
      "month": "2025-07",
      "candidate_symbol": "ETHUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 182,
      "eligible_stale_slots": 3,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -1.0,
      "stale_slot_r_42": -0.7195668572640739,
      "net_replacement_delta_r_42": -0.2804331427359261,
      "net_replacement_delta_r_24": 0.7182721334961943,
      "net_replacement_delta_r_60": -0.31246134113046975,
      "lowest_unrealized_slot_delta_r_42": -0.2804331427359261,
      "oracle_upper_bound_delta_r_42": 0.6228604002397997,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "85a7a7bff100",
      "decision_time_utc": "2025-07-27T20:00:00+00:00",
      "month": "2025-07",
      "candidate_symbol": "CFXUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 186,
      "eligible_stale_slots": 3,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": 2.8237343816902967,
      "stale_slot_r_42": -0.6822006258037722,
      "net_replacement_delta_r_42": 3.505935007494069,
      "net_replacement_delta_r_24": 3.3116306039005066,
      "net_replacement_delta_r_60": 3.4707039892600715,
      "lowest_unrealized_slot_delta_r_42": 3.505935007494069,
      "oracle_upper_bound_delta_r_42": 4.428302405936089,
      "candidate_first_hit": "tp1",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "df1e3dd136b5",
      "decision_time_utc": "2025-07-28T00:00:00+00:00",
      "month": "2025-07",
      "candidate_symbol": "CFXUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 187,
      "eligible_stale_slots": 3,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": 2.8237343816902967,
      "stale_slot_r_42": -0.7217020704903765,
      "net_replacement_delta_r_42": 3.545436452180673,
      "net_replacement_delta_r_24": 3.445081430544437,
      "net_replacement_delta_r_60": 3.5219491066913413,
      "lowest_unrealized_slot_delta_r_42": 3.545436452180673,
      "oracle_upper_bound_delta_r_42": 4.423076012794944,
      "candidate_first_hit": "tp1",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "0703462e5235",
      "decision_time_utc": "2025-08-09T04:00:00+00:00",
      "month": "2025-08",
      "candidate_symbol": "LTCUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 260,
      "eligible_stale_slots": 3,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -0.33988933638931496,
      "stale_slot_r_42": -0.08434092243896477,
      "net_replacement_delta_r_42": -0.2555484139503502,
      "net_replacement_delta_r_24": 0.7580553719797036,
      "net_replacement_delta_r_60": -0.48412078565010885,
      "lowest_unrealized_slot_delta_r_42": 0.09314381279381856,
      "oracle_upper_bound_delta_r_42": 0.09314381279381856,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "26d375c62933",
      "decision_time_utc": "2025-08-09T08:00:00+00:00",
      "month": "2025-08",
      "candidate_symbol": "LTCUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 261,
      "eligible_stale_slots": 3,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -0.44683020217240155,
      "stale_slot_r_42": -0.16654663165162592,
      "net_replacement_delta_r_42": -0.2802835705207756,
      "net_replacement_delta_r_24": 0.9096079780087338,
      "net_replacement_delta_r_60": -0.5622812886079077,
      "lowest_unrealized_slot_delta_r_42": 0.14574147565714868,
      "oracle_upper_bound_delta_r_42": 0.14574147565714868,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "86ad5e782794",
      "decision_time_utc": "2025-08-10T16:00:00+00:00",
      "month": "2025-08",
      "candidate_symbol": "LTCUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 269,
      "eligible_stale_slots": 2,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -0.07617108484655374,
      "stale_slot_r_42": 0.2391438813459228,
      "net_replacement_delta_r_42": -0.31531496619247656,
      "net_replacement_delta_r_24": -0.10504399644011622,
      "net_replacement_delta_r_60": -0.6839884425071723,
      "lowest_unrealized_slot_delta_r_42": -0.31531496619247656,
      "oracle_upper_bound_delta_r_42": 0.4041976717371645,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "09e478e0c936",
      "decision_time_utc": "2025-08-10T20:00:00+00:00",
      "month": "2025-08",
      "candidate_symbol": "LTCUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 270,
      "eligible_stale_slots": 2,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -0.24956064393175476,
      "stale_slot_r_42": 0.11957194067296187,
      "net_replacement_delta_r_42": -0.36913258460471665,
      "net_replacement_delta_r_24": -0.19926162020630522,
      "net_replacement_delta_r_60": -0.7790054310776512,
      "lowest_unrealized_slot_delta_r_42": -0.36913258460471665,
      "oracle_upper_bound_delta_r_42": 0.3395046926088637,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "22f4818cab5c",
      "decision_time_utc": "2025-08-11T04:00:00+00:00",
      "month": "2025-08",
      "candidate_symbol": "LTCUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 272,
      "eligible_stale_slots": 2,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -0.6794006287297977,
      "stale_slot_r_42": -0.17508748455683654,
      "net_replacement_delta_r_42": -0.5043131441729611,
      "net_replacement_delta_r_24": -0.06343668430751596,
      "net_replacement_delta_r_60": -0.6306081118496002,
      "lowest_unrealized_slot_delta_r_42": -0.5043131441729611,
      "oracle_upper_bound_delta_r_42": 0.27140225078566516,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "42e4f0d3c6bc",
      "decision_time_utc": "2025-08-12T20:00:00+00:00",
      "month": "2025-08",
      "candidate_symbol": "SOLUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 282,
      "eligible_stale_slots": 2,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": 1.64291608764841,
      "stale_slot_r_42": -0.5359385198020248,
      "net_replacement_delta_r_42": 2.1788546074504347,
      "net_replacement_delta_r_24": 1.790245800263309,
      "net_replacement_delta_r_60": 1.7656908481608253,
      "lowest_unrealized_slot_delta_r_42": 2.1788546074504347,
      "oracle_upper_bound_delta_r_42": 2.5440457989039986,
      "candidate_first_hit": "tp1",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "a3037395d0df",
      "decision_time_utc": "2025-08-13T20:00:00+00:00",
      "month": "2025-08",
      "candidate_symbol": "TAOUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 288,
      "eligible_stale_slots": 3,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -1.0,
      "stale_slot_r_42": -0.5188568139916017,
      "net_replacement_delta_r_42": -0.48114318600839834,
      "net_replacement_delta_r_24": -0.821709695603709,
      "net_replacement_delta_r_60": -0.7619237252672281,
      "lowest_unrealized_slot_delta_r_42": -0.48114318600839834,
      "oracle_upper_bound_delta_r_42": -0.11523321475942838,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "94d16270a108",
      "decision_time_utc": "2025-08-14T00:00:00+00:00",
      "month": "2025-08",
      "candidate_symbol": "TAOUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 289,
      "eligible_stale_slots": 3,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -1.0,
      "stale_slot_r_42": -0.5946568835253548,
      "net_replacement_delta_r_42": -0.40534311647464516,
      "net_replacement_delta_r_24": -0.721354673967473,
      "net_replacement_delta_r_60": -0.6893264755729294,
      "lowest_unrealized_slot_delta_r_42": -0.40534311647464516,
      "oracle_upper_bound_delta_r_42": -0.06659841320791682,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "23b51ddbc640",
      "decision_time_utc": "2025-08-23T20:00:00+00:00",
      "month": "2025-08",
      "candidate_symbol": "LINKUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 348,
      "eligible_stale_slots": 4,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -1.0,
      "stale_slot_r_42": -0.4932342552759679,
      "net_replacement_delta_r_42": -0.5067657447240321,
      "net_replacement_delta_r_24": -0.5943094870024512,
      "net_replacement_delta_r_60": -0.4928868587530634,
      "lowest_unrealized_slot_delta_r_42": -0.3083245075898532,
      "oracle_upper_bound_delta_r_42": 0.3911926060316573,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "534f5faa2146",
      "decision_time_utc": "2025-08-24T00:00:00+00:00",
      "month": "2025-08",
      "candidate_symbol": "LINKUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 349,
      "eligible_stale_slots": 4,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -1.0,
      "stale_slot_r_42": -0.45907084365512074,
      "net_replacement_delta_r_42": -0.5409291563448793,
      "net_replacement_delta_r_24": -0.5814982076446334,
      "net_replacement_delta_r_60": -0.5494700092500908,
      "lowest_unrealized_slot_delta_r_42": -0.35916645627937105,
      "oracle_upper_bound_delta_r_42": 0.43966969355082486,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "05f49aa96b87",
      "decision_time_utc": "2025-08-24T20:00:00+00:00",
      "month": "2025-08",
      "candidate_symbol": "LINKUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 354,
      "eligible_stale_slots": 4,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -1.0,
      "stale_slot_r_42": -0.38967641380027646,
      "net_replacement_delta_r_42": -0.6103235861997236,
      "net_replacement_delta_r_24": -0.7021377549307471,
      "net_replacement_delta_r_60": -0.7170842475148675,
      "lowest_unrealized_slot_delta_r_42": -0.32527182381969244,
      "oracle_upper_bound_delta_r_42": 0.15736194858626606,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "c25266f69a80",
      "decision_time_utc": "2025-09-18T16:00:00+00:00",
      "month": "2025-09",
      "candidate_symbol": "PEPEUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 503,
      "eligible_stale_slots": 3,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -1.0,
      "stale_slot_r_42": -0.6160090157883833,
      "net_replacement_delta_r_42": -0.3839909842116167,
      "net_replacement_delta_r_24": -0.5270502703739106,
      "net_replacement_delta_r_60": -0.4363037082560369,
      "lowest_unrealized_slot_delta_r_42": -0.3839909842116167,
      "oracle_upper_bound_delta_r_42": 0.4279525179495507,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "6e982975e330",
      "decision_time_utc": "2025-09-18T20:00:00+00:00",
      "month": "2025-09",
      "candidate_symbol": "PEPEUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 504,
      "eligible_stale_slots": 3,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -1.0,
      "stale_slot_r_42": -0.7494598424323139,
      "net_replacement_delta_r_42": -0.2505401575676861,
      "net_replacement_delta_r_24": -0.47366993971633764,
      "net_replacement_delta_r_60": -0.42776285535082537,
      "lowest_unrealized_slot_delta_r_42": -0.09481691946298787,
      "oracle_upper_bound_delta_r_42": 0.5916775702440016,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "59bcf60188a8",
      "decision_time_utc": "2025-09-19T00:00:00+00:00",
      "month": "2025-09",
      "candidate_symbol": "PEPEUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 505,
      "eligible_stale_slots": 3,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -1.0,
      "stale_slot_r_42": -0.8049753863161895,
      "net_replacement_delta_r_42": -0.19502461368381052,
      "net_replacement_delta_r_24": -0.590039060549845,
      "net_replacement_delta_r_60": -0.5110361711766382,
      "lowest_unrealized_slot_delta_r_42": -0.0791646754765879,
      "oracle_upper_bound_delta_r_42": 0.48365279347240486,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "7d9c86b16b48",
      "decision_time_utc": "2025-10-02T16:00:00+00:00",
      "month": "2025-10",
      "candidate_symbol": "ADAUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 587,
      "eligible_stale_slots": 2,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -0.52214252924627,
      "stale_slot_r_42": -0.11209869438090116,
      "net_replacement_delta_r_42": -0.4100438348653689,
      "net_replacement_delta_r_24": -0.03763163594489444,
      "net_replacement_delta_r_60": 0.28977021131519365,
      "lowest_unrealized_slot_delta_r_42": -0.4100438348653689,
      "oracle_upper_bound_delta_r_42": -0.3179081856624687,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "9503a25c7de7",
      "decision_time_utc": "2025-10-05T04:00:00+00:00",
      "month": "2025-10",
      "candidate_symbol": "ADAUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 602,
      "eligible_stale_slots": 2,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -1.0,
      "stale_slot_r_42": -1.5577394712162067,
      "net_replacement_delta_r_42": 0.5577394712162067,
      "net_replacement_delta_r_24": -0.07763044152056056,
      "net_replacement_delta_r_60": 0.5577394712162067,
      "lowest_unrealized_slot_delta_r_42": 0.5577394712162067,
      "oracle_upper_bound_delta_r_42": 0.6189791446858879,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "1d627b9cef1a",
      "decision_time_utc": "2025-10-05T12:00:00+00:00",
      "month": "2025-10",
      "candidate_symbol": "LTCUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 604,
      "eligible_stale_slots": 2,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": 1.5953414705404345,
      "stale_slot_r_42": -1.8438580435407934,
      "net_replacement_delta_r_42": 3.4391995140812277,
      "net_replacement_delta_r_24": 0.08239920183310923,
      "net_replacement_delta_r_60": 3.4391995140812277,
      "lowest_unrealized_slot_delta_r_42": 3.177187098211085,
      "oracle_upper_bound_delta_r_42": 3.4391995140812277,
      "candidate_first_hit": "tp1",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "e93007d33ef6",
      "decision_time_utc": "2025-10-05T20:00:00+00:00",
      "month": "2025-10",
      "candidate_symbol": "BNBUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 606,
      "eligible_stale_slots": 2,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -1.0,
      "stale_slot_r_42": -1.7007987573785006,
      "net_replacement_delta_r_42": 0.7007987573785006,
      "net_replacement_delta_r_24": 1.1551753376564506,
      "net_replacement_delta_r_60": 0.7007987573785006,
      "lowest_unrealized_slot_delta_r_42": 0.4890118351325592,
      "oracle_upper_bound_delta_r_42": 0.7007987573785006,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "7d4b497db34e",
      "decision_time_utc": "2025-10-06T00:00:00+00:00",
      "month": "2025-10",
      "candidate_symbol": "BNBUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 607,
      "eligible_stale_slots": 2,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -1.0,
      "stale_slot_r_42": -1.7584495144886778,
      "net_replacement_delta_r_42": 0.7584495144886778,
      "net_replacement_delta_r_24": 1.3373221891335045,
      "net_replacement_delta_r_60": 0.7584495144886778,
      "lowest_unrealized_slot_delta_r_42": 0.47550873803611027,
      "oracle_upper_bound_delta_r_42": 0.7584495144886778,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "183488c087e9",
      "decision_time_utc": "2025-10-08T12:00:00+00:00",
      "month": "2025-10",
      "candidate_symbol": "FORMUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 622,
      "eligible_stale_slots": 2,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -1.0,
      "stale_slot_r_42": -1.4712633355509392,
      "net_replacement_delta_r_42": 0.47126333555093924,
      "net_replacement_delta_r_24": 0.47126333555093924,
      "net_replacement_delta_r_60": 0.47126333555093924,
      "lowest_unrealized_slot_delta_r_42": 0.198695247558891,
      "oracle_upper_bound_delta_r_42": 0.47126333555093924,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "2b487795afef",
      "decision_time_utc": "2025-10-09T04:00:00+00:00",
      "month": "2025-10",
      "candidate_symbol": "BNBUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 626,
      "eligible_stale_slots": 4,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -1.0,
      "stale_slot_r_42": -1.3314068692281007,
      "net_replacement_delta_r_42": 0.3314068692281007,
      "net_replacement_delta_r_24": 0.3314068692281007,
      "net_replacement_delta_r_60": 0.3314068692281007,
      "lowest_unrealized_slot_delta_r_42": -0.1596574609425404,
      "oracle_upper_bound_delta_r_42": 0.3314068692281007,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "022edf0ddc9b",
      "decision_time_utc": "2025-10-09T08:00:00+00:00",
      "month": "2025-10",
      "candidate_symbol": "BNBUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 627,
      "eligible_stale_slots": 4,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -1.0,
      "stale_slot_r_42": -1.3153927700308286,
      "net_replacement_delta_r_42": 0.31539277003082855,
      "net_replacement_delta_r_24": 0.31539277003082855,
      "net_replacement_delta_r_60": 0.31539277003082855,
      "lowest_unrealized_slot_delta_r_42": -0.30940665115177,
      "oracle_upper_bound_delta_r_42": 0.31539277003082855,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "3d007f9e12c8",
      "decision_time_utc": "2025-10-09T12:00:00+00:00",
      "month": "2025-10",
      "candidate_symbol": "BNBUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "5ef66652c15e",
      "selected_slot_symbol": "APTUSDT",
      "selected_slot_holding_bars": 628,
      "eligible_stale_slots": 5,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -1.0,
      "stale_slot_r_42": -1.2075645021025325,
      "net_replacement_delta_r_42": 0.20756450210253252,
      "net_replacement_delta_r_24": 0.20756450210253252,
      "net_replacement_delta_r_60": 0.20756450210253252,
      "lowest_unrealized_slot_delta_r_42": -0.4292060033191527,
      "oracle_upper_bound_delta_r_42": 0.20756450210253252,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    },
    {
      "event_id": "f88daf32d7d4",
      "decision_time_utc": "2026-04-30T20:00:00+00:00",
      "month": "2026-04",
      "candidate_symbol": "APEUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "1ea8a0eaeb9a",
      "selected_slot_symbol": "BNBUSDT",
      "selected_slot_holding_bars": 92,
      "eligible_stale_slots": 4,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": 0.08929855876402898,
      "stale_slot_r_42": 0.7084552822454752,
      "net_replacement_delta_r_42": -0.6191567234814461,
      "net_replacement_delta_r_24": 0.0816762099337966,
      "net_replacement_delta_r_60": -1.1355001933187798,
      "lowest_unrealized_slot_delta_r_42": -0.45737628448379636,
      "oracle_upper_bound_delta_r_42": -0.45737628448379636,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "tp1",
      "right_censored": false
    },
    {
      "event_id": "cb72349abdf4",
      "decision_time_utc": "2026-05-01T00:00:00+00:00",
      "month": "2026-05",
      "candidate_symbol": "APEUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "1ea8a0eaeb9a",
      "selected_slot_symbol": "BNBUSDT",
      "selected_slot_holding_bars": 93,
      "eligible_stale_slots": 4,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": 0.14886563596897845,
      "stale_slot_r_42": 0.6069268530400664,
      "net_replacement_delta_r_42": -0.458061217071088,
      "net_replacement_delta_r_24": -0.04072543913012974,
      "net_replacement_delta_r_60": -1.3854189035974347,
      "lowest_unrealized_slot_delta_r_42": -0.45690919033266447,
      "oracle_upper_bound_delta_r_42": -0.45690919033266447,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "tp1",
      "right_censored": false
    },
    {
      "event_id": "187e4086a082",
      "decision_time_utc": "2026-05-01T16:00:00+00:00",
      "month": "2026-05",
      "candidate_symbol": "APEUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "1ea8a0eaeb9a",
      "selected_slot_symbol": "BNBUSDT",
      "selected_slot_holding_bars": 97,
      "eligible_stale_slots": 4,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": 0.34131311616958016,
      "stale_slot_r_42": 0.6475943177770376,
      "net_replacement_delta_r_42": -0.3062812016074574,
      "net_replacement_delta_r_24": -0.0129317757401608,
      "net_replacement_delta_r_60": -1.2850399367474261,
      "lowest_unrealized_slot_delta_r_42": -0.5156366381107925,
      "oracle_upper_bound_delta_r_42": -0.3062812016074574,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "tp1",
      "right_censored": false
    },
    {
      "event_id": "113f2651fa4a",
      "decision_time_utc": "2026-05-02T08:00:00+00:00",
      "month": "2026-05",
      "candidate_symbol": "PENGUUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "1ea8a0eaeb9a",
      "selected_slot_symbol": "BNBUSDT",
      "selected_slot_holding_bars": 101,
      "eligible_stale_slots": 4,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": 0.37948934122915595,
      "stale_slot_r_42": 0.9496554179268333,
      "net_replacement_delta_r_42": -0.5701660766976773,
      "net_replacement_delta_r_24": 0.07329144869783877,
      "net_replacement_delta_r_60": -1.177246837255332,
      "lowest_unrealized_slot_delta_r_42": -0.8763852986644929,
      "oracle_upper_bound_delta_r_42": -0.5701660766976773,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "tp1",
      "right_censored": false
    },
    {
      "event_id": "0f89aa51711b",
      "decision_time_utc": "2026-05-08T20:00:00+00:00",
      "month": "2026-05",
      "candidate_symbol": "TAOUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "1ea8a0eaeb9a",
      "selected_slot_symbol": "BNBUSDT",
      "selected_slot_holding_bars": 140,
      "eligible_stale_slots": 3,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -0.6767911129458187,
      "stale_slot_r_42": 0.9183744123409229,
      "net_replacement_delta_r_42": -1.5951655252867416,
      "net_replacement_delta_r_24": -0.42728392243833224,
      "net_replacement_delta_r_60": -1.9183744123409228,
      "lowest_unrealized_slot_delta_r_42": -0.08833632564059724,
      "oracle_upper_bound_delta_r_42": -0.08833632564059724,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "tp1",
      "right_censored": false
    },
    {
      "event_id": "7db800d2d2d1",
      "decision_time_utc": "2026-05-12T04:00:00+00:00",
      "month": "2026-05",
      "candidate_symbol": "ONDOUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "1ea8a0eaeb9a",
      "selected_slot_symbol": "BNBUSDT",
      "selected_slot_holding_bars": 160,
      "eligible_stale_slots": 3,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -1.0,
      "stale_slot_r_42": 0.5276862855919348,
      "net_replacement_delta_r_42": -1.5276862855919346,
      "net_replacement_delta_r_24": -1.5276862855919346,
      "net_replacement_delta_r_60": -1.5276862855919346,
      "lowest_unrealized_slot_delta_r_42": -1.0171394598244237,
      "oracle_upper_bound_delta_r_42": 0.1524496695494657,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "tp1",
      "right_censored": false
    },
    {
      "event_id": "4a16b89cff1d",
      "decision_time_utc": "2026-05-14T16:00:00+00:00",
      "month": "2026-05",
      "candidate_symbol": "NEARUSDT",
      "candidate_rank": 1,
      "selected_slot_trade_id": "580141baa4ca",
      "selected_slot_symbol": "AVAXUSDT",
      "selected_slot_holding_bars": 173,
      "eligible_stale_slots": 2,
      "candidate_same_bar_stop_possible": false,
      "candidate_same_bar_tp1_possible": false,
      "candidate_r_42": -1.0,
      "stale_slot_r_42": -0.9958347144568486,
      "net_replacement_delta_r_42": -0.004165285543151431,
      "net_replacement_delta_r_24": 0.41839959329165244,
      "net_replacement_delta_r_60": 0.20120715556886792,
      "lowest_unrealized_slot_delta_r_42": -0.9371553139771123,
      "oracle_upper_bound_delta_r_42": -0.004165285543151431,
      "candidate_first_hit": "stop",
      "stale_slot_first_hit": "stop",
      "right_censored": false
    }
  ]
}
```
