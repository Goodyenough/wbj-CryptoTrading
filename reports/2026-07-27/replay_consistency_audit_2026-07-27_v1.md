---
created: 2026-07-27 00:35:42 CST
tags:
  - crypto
  - trading-system
  - replay-consistency-audit
experiment: replay_consistency_audit
source_run_id: 110c51eef593
replay_run_id: 1e3cbb13c14a
verdict: replay_consistency_pass_with_ordering_limit
---

# replay_consistency_audit

## Plain-language conclusion

Source/replay entered trades, final equity, active path, and prior blocked-event signatures match. Candidate ordering is accepted only indirectly because the original source run did not persist blocked candidate ordering.

This report is diagnostic only. It does not change `config/settings.toml`, backtest behavior, paper state, strategy defaults, or saved backtest rows.

## Scope

| Field | Value |
|---|---:|
| source_run_id | `110c51eef593` |
| replay_run_id | `1e3cbb13c14a` |
| window | `2025-06-01T00:00:00+00:00` -> `2026-06-01T00:00:00+00:00` |
| source_commit_hash | `b9cb5e23eeb069e2b6b2552e3d1e9d54f4c5f036` |
| blocked_events_json | `reports\2026-07-27\blocked_entry_event_export_2026-07-27_v1.json` |

## Consistency Checks

| Check | Source | Replay | Mismatches |
|---|---:|---:|---:|
| trades | 389 | 389 | 0 |
| entered_trades | 58 | 58 | 0 |
| closed_trades | 388 | 388 | 0 |
| active_count_path | 2190 points | 2190 points | 0 |
| open_plan_path | 2190 points | 2190 points | 0 |
| final_equity_delta | n/a | n/a | 0.0000000000 |
| blocked_event_repeat | 512 | 512 | 0 |

## Candidate Ordering Evidence

source run did not persist blocked candidate order directly; current source marker and repeated blocked-event signatures match the prior export.

Important limitation: the original source run did not persist blocked candidate ordering directly. Ordering is therefore verified by replay source marker plus repeat blocked-event signatures, not by an independently persisted source ordering table.

## Mismatch Examples

```json
{
  "entered_mismatch_examples": [],
  "active_path_mismatch_examples": [],
  "blocked_event_mismatch_examples": []
}
```

## Decision

`replay_consistency_pass_with_ordering_limit`

## Next Action

Proceed to `stale_slot_continuation_review`. Do not calculate replacement outcome until stale-slot continuation value is reviewed independently.

## Raw Summary

```json
{
  "source_run_id": "110c51eef593",
  "replay_run_id": "1e3cbb13c14a",
  "report_date": "2026-07-27",
  "start_utc": "2025-06-01T00:00:00+00:00",
  "end_utc": "2026-06-01T00:00:00+00:00",
  "source_commit_hash": "b9cb5e23eeb069e2b6b2552e3d1e9d54f4c5f036",
  "source_trade_count": 389,
  "replay_trade_count": 389,
  "source_entered_trades": 58,
  "replay_entered_trades": 58,
  "source_closed_trades": 388,
  "replay_closed_trades": 388,
  "entered_signature_mismatches": 0,
  "active_path_points": 2190,
  "active_path_mismatches": 0,
  "open_plan_path_mismatches": 0,
  "final_equity_delta": 0.0,
  "blocked_events_json": "reports\\2026-07-27\\blocked_entry_event_export_2026-07-27_v1.json",
  "blocked_events_reference_count": 512,
  "blocked_events_replay_count": 512,
  "blocked_event_signature_mismatches": 0,
  "candidate_ordering_evidence": "source run did not persist blocked candidate order directly; current source marker and repeated blocked-event signatures match the prior export.",
  "ordering_directly_persisted_in_source": false,
  "verdict": "replay_consistency_pass_with_ordering_limit",
  "reason": "Source/replay entered trades, final equity, active path, and prior blocked-event signatures match. Candidate ordering is accepted only indirectly because the original source run did not persist blocked candidate ordering.",
  "entered_mismatch_examples": [],
  "active_path_mismatch_examples": [],
  "blocked_event_mismatch_examples": []
}
```
