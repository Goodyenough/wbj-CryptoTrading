---
created: 2026-07-25 23:07:09 CST
tags:
  - crypto
  - trading-system
  - paper-checkpoint
account: demo
start_date: 2026-07-03
end_date: 2026-07-16
report_version: v1
verdict: formal_audit_ready
---

# Paper Checkpoint 2026-07-03 -> 2026-07-16 demo v1

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
- daily_success: 11/14
- paper_4h_success: 56/70
- note: expected paper_4h runs assume five scheduled updates per Beijing day (00:10, 04:10, 08:10, 12:10, 16:10)

## Sample Maturity Gate

- opportunities: 60
- mature: 36
- right_censored: 24
- right_censored_ratio: 40.0%
- open_unknown: 0
- entered_trades: 8

## Opportunity Classification

| Classification | Count |
|---|---:|
| neutral_or_unknown | 35 |
| missed_winner | 11 |
| avoided_loser | 7 |
| false_entry | 7 |

## Shadow Replay Snapshot

### entry_reclaim_confirm_1bar

| Decision | Count |
|---|---:|
| delayed_entry | 37 |
| no_baseline_entry | 6 |
| filtered_unknown | 6 |
| missed_winner | 3 |
| filtered_loser | 1 |

### relative_strength_gate

| Decision | Count |
|---|---:|
| kept_by_relative_strength | 22 |
| filtered_unknown | 15 |
| no_baseline_entry | 5 |
| data_gap | 5 |
| filtered_loser | 4 |
| missed_winner | 2 |

## Commands For Next Step

```powershell
python main.py paper audit --account demo --start-date 2026-07-03 --end-date 2026-07-16
python main.py paper shadow-replay --account demo --start-date 2026-07-03 --end-date 2026-07-16 --variant entry_reclaim_confirm_1bar
python main.py paper shadow-replay --account demo --start-date 2026-07-03 --end-date 2026-07-16 --variant relative_strength_gate
```

## Raw Summary

```json
{
  "verdict": "formal_audit_ready",
  "reason": "data link is usable, config hash is stable, and opportunity samples are sufficiently mature",
  "data_link_verdict": "partial_pass",
  "config_hash_stable": true,
  "opportunities": 60,
  "maturity": {
    "mature": 36,
    "right_censored": 24
  },
  "classifications": {
    "avoided_loser": 7,
    "neutral_or_unknown": 35,
    "missed_winner": 11,
    "false_entry": 7
  },
  "entry_reclaim_confirm_1bar": {
    "no_baseline_entry": 6,
    "delayed_entry": 37,
    "filtered_unknown": 6,
    "missed_winner": 3,
    "filtered_loser": 1
  },
  "relative_strength_gate": {
    "no_baseline_entry": 5,
    "kept_by_relative_strength": 22,
    "filtered_unknown": 15,
    "filtered_loser": 4,
    "missed_winner": 2,
    "data_gap": 5
  }
}
```
