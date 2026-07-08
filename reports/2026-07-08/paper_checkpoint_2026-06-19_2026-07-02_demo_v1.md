---
created: 2026-07-08 17:18:28 CST
tags:
  - crypto
  - trading-system
  - paper-checkpoint
account: demo
start_date: 2026-06-19
end_date: 2026-07-02
report_version: v1
verdict: formal_audit_ready
---

# Paper Checkpoint 2026-06-19 -> 2026-07-02 demo v1

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
- daily_success: 14/14
- paper_4h_success: 69/70
- note: expected paper_4h runs assume five scheduled updates per Beijing day (00:10, 04:10, 08:10, 12:10, 16:10)

## Sample Maturity Gate

- opportunities: 78
- mature: 51
- right_censored: 27
- right_censored_ratio: 34.6%
- open_unknown: 0
- entered_trades: 8

## Opportunity Classification

| Classification | Count |
|---|---:|
| neutral_or_unknown | 34 |
| avoided_loser | 25 |
| missed_winner | 12 |
| false_entry | 7 |

## Shadow Replay Snapshot

### entry_reclaim_confirm_1bar

| Decision | Count |
|---|---:|
| delayed_entry | 36 |
| filtered_loser | 11 |
| filtered_unknown | 11 |
| no_baseline_entry | 10 |
| missed_winner | 3 |

### relative_strength_gate

| Decision | Count |
|---|---:|
| kept_by_relative_strength | 29 |
| filtered_unknown | 15 |
| filtered_loser | 13 |
| no_baseline_entry | 5 |
| data_gap | 5 |
| missed_winner | 4 |

## Commands For Next Step

```powershell
python main.py paper audit --account demo --start-date 2026-06-19 --end-date 2026-07-02
python main.py paper shadow-replay --account demo --start-date 2026-06-19 --end-date 2026-07-02 --variant entry_reclaim_confirm_1bar
python main.py paper shadow-replay --account demo --start-date 2026-06-19 --end-date 2026-07-02 --variant relative_strength_gate
```

## Raw Summary

```json
{
  "verdict": "formal_audit_ready",
  "reason": "data link is usable, config hash is stable, and opportunity samples are sufficiently mature",
  "data_link_verdict": "partial_pass",
  "config_hash_stable": true,
  "opportunities": 78,
  "maturity": {
    "mature": 51,
    "right_censored": 27
  },
  "classifications": {
    "avoided_loser": 25,
    "missed_winner": 12,
    "neutral_or_unknown": 34,
    "false_entry": 7
  },
  "entry_reclaim_confirm_1bar": {
    "no_baseline_entry": 10,
    "delayed_entry": 36,
    "filtered_loser": 11,
    "filtered_unknown": 11,
    "missed_winner": 3
  },
  "relative_strength_gate": {
    "no_baseline_entry": 5,
    "kept_by_relative_strength": 29,
    "filtered_loser": 13,
    "missed_winner": 4,
    "filtered_unknown": 15,
    "data_gap": 5
  }
}
```
