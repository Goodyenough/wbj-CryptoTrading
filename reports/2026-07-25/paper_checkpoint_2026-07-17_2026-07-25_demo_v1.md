---
created: 2026-07-25 23:51:51 CST
tags:
  - crypto
  - trading-system
  - paper-checkpoint
account: demo
start_date: 2026-07-17
end_date: 2026-07-25
report_version: v1
verdict: wait_for_more_data
---

# Paper Checkpoint 2026-07-17 -> 2026-07-25 demo v1

This checkpoint decides whether the window is ready for a formal paper audit. It does not modify settings, plans, events, snapshots, or paper state.

## Decision

- verdict: wait_for_more_data
- reason: right-censored ratio 44.0% > allowed 40.0%
- next_action: Treat the window as interim; avoid over-interpreting open or immature paths.

## Data Link Gate

- data_link_verdict: partial_pass
- config_hash_stable: true
- config_hashes: be7ec39ec21f6a83
- stale_running_runs: 0
- duplicate_events: 0
- impossible_event_order: 0
- daily_success: 9/9
- paper_4h_success: 44/45
- note: expected paper_4h runs assume five scheduled updates per Beijing day (00:10, 04:10, 08:10, 12:10, 16:10)

## Sample Maturity Gate

- opportunities: 50
- mature: 23
- right_censored: 22
- right_censored_ratio: 44.0%
- open_unknown: 0
- entered_trades: 8

## Opportunity Classification

| Classification | Count |
|---|---:|
| neutral_or_unknown | 29 |
| avoided_loser | 8 |
| false_entry | 7 |
| missed_winner | 6 |

## Shadow Replay Snapshot

### entry_reclaim_confirm_1bar

| Decision | Count |
|---|---:|
| delayed_entry | 22 |
| no_baseline_entry | 12 |
| filtered_unknown | 7 |
| missed_winner | 1 |
| filtered_loser | 1 |

### relative_strength_gate

| Decision | Count |
|---|---:|
| kept_by_relative_strength | 19 |
| filtered_unknown | 10 |
| no_baseline_entry | 5 |
| data_gap | 5 |
| missed_winner | 2 |
| filtered_loser | 2 |

## Commands For Next Step

```powershell
python main.py paper audit --account demo --start-date 2026-07-17 --end-date 2026-07-25
python main.py paper shadow-replay --account demo --start-date 2026-07-17 --end-date 2026-07-25 --variant entry_reclaim_confirm_1bar
python main.py paper shadow-replay --account demo --start-date 2026-07-17 --end-date 2026-07-25 --variant relative_strength_gate
```

## Raw Summary

```json
{
  "verdict": "wait_for_more_data",
  "reason": "right-censored ratio 44.0% > allowed 40.0%",
  "data_link_verdict": "partial_pass",
  "config_hash_stable": true,
  "opportunities": 50,
  "maturity": {
    "mature": 23,
    "right_censored": 22,
    "data_gap": 5
  },
  "classifications": {
    "neutral_or_unknown": 29,
    "missed_winner": 6,
    "avoided_loser": 8,
    "false_entry": 7
  },
  "entry_reclaim_confirm_1bar": {
    "filtered_unknown": 7,
    "delayed_entry": 22,
    "missed_winner": 1,
    "no_baseline_entry": 12,
    "filtered_loser": 1
  },
  "relative_strength_gate": {
    "kept_by_relative_strength": 19,
    "missed_winner": 2,
    "filtered_unknown": 10,
    "filtered_loser": 2,
    "no_baseline_entry": 5,
    "data_gap": 5
  }
}
```
