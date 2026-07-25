---
created: 2026-07-25 23:31:38 CST
tags:
  - crypto
  - trading-system
  - paper-checkpoint
account: demo
start_date: 2026-07-03
end_date: 2026-07-25
report_version: v1
verdict: formal_audit_ready
---

# Paper Checkpoint 2026-07-03 -> 2026-07-25 demo v1

This checkpoint decides whether the window is ready for a formal paper audit. It does not modify settings, plans, events, snapshots, or paper state.

## Decision

- verdict: formal_audit_ready
- reason: data link is usable, config hash is stable, and opportunity samples are sufficiently mature
- next_action: Run formal paper audit and both shadow replay reports before deciding whether any A/B should start.

## Data Link Gate

- data_link_verdict: partial_pass
- config_hash_stable: true
- config_hashes: be7ec39ec21f6a83
- stale_running_runs: 0
- duplicate_events: 0
- impossible_event_order: 0
- daily_success: 20/23
- paper_4h_success: 100/115
- note: expected paper_4h runs assume five scheduled updates per Beijing day (00:10, 04:10, 08:10, 12:10, 16:10)

## Sample Maturity Gate

- opportunities: 102
- mature: 75
- right_censored: 22
- right_censored_ratio: 21.6%
- open_unknown: 0
- entered_trades: 8

## Opportunity Classification

| Classification | Count |
|---|---:|
| neutral_or_unknown | 54 |
| avoided_loser | 22 |
| missed_winner | 19 |
| false_entry | 7 |

## Shadow Replay Snapshot

### entry_reclaim_confirm_1bar

| Decision | Count |
|---|---:|
| delayed_entry | 63 |
| no_baseline_entry | 15 |
| filtered_unknown | 9 |
| missed_winner | 4 |
| filtered_loser | 4 |

### relative_strength_gate

| Decision | Count |
|---|---:|
| kept_by_relative_strength | 43 |
| filtered_unknown | 25 |
| filtered_loser | 9 |
| no_baseline_entry | 8 |
| missed_winner | 5 |
| data_gap | 5 |

## Commands For Next Step

```powershell
python main.py paper audit --account demo --start-date 2026-07-03 --end-date 2026-07-25
python main.py paper shadow-replay --account demo --start-date 2026-07-03 --end-date 2026-07-25 --variant entry_reclaim_confirm_1bar
python main.py paper shadow-replay --account demo --start-date 2026-07-03 --end-date 2026-07-25 --variant relative_strength_gate
```

## Raw Summary

```json
{
  "verdict": "formal_audit_ready",
  "reason": "data link is usable, config hash is stable, and opportunity samples are sufficiently mature",
  "data_link_verdict": "partial_pass",
  "config_hash_stable": true,
  "opportunities": 102,
  "maturity": {
    "mature": 75,
    "right_censored": 22,
    "data_gap": 5
  },
  "classifications": {
    "avoided_loser": 22,
    "neutral_or_unknown": 54,
    "missed_winner": 19,
    "false_entry": 7
  },
  "entry_reclaim_confirm_1bar": {
    "filtered_unknown": 9,
    "delayed_entry": 63,
    "missed_winner": 4,
    "filtered_loser": 4,
    "no_baseline_entry": 15
  },
  "relative_strength_gate": {
    "filtered_unknown": 25,
    "kept_by_relative_strength": 43,
    "filtered_loser": 9,
    "missed_winner": 5,
    "no_baseline_entry": 8,
    "data_gap": 5
  }
}
```
