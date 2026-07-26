---
created: 2026-07-27 00:06:06 CST
tags:
  - crypto
  - trading-system
  - timing-audit
experiment: signal_fill_timing_audit
run_id: 110c51eef593
verdict: timing_audit_warn_same_bar_ambiguity
---

# signal_fill_timing_audit

## Plain-language conclusion

replay order is inspectable, but WATCHING entry and same-bar stop/TP evaluation can occur in one step_trade call; later capacity diagnostics must explicitly account for same-bar ambiguity.

This report is diagnostic only. It does not change `config/settings.toml`, backtest behavior, paper state, or strategy defaults.

## Scope

| Field | Value |
|---|---:|
| run_id | `110c51eef593` |
| window | `2025-06-01T00:00:00+00:00` -> `2026-06-01T00:00:00+00:00` |
| commit_hash | `b9cb5e23eeb069e2b6b2552e3d1e9d54f4c5f036` |
| symbols | 294 |
| max_active_positions | 5 |
| intrabar_policy | `n/a` |

## Timing Findings

| Question | Current replay behavior | Risk read |
|---|---|---|
| `signal_time` | 4h reclaim is evaluated with the current bar close at `bar_time = bar_close_ms`. | Signal depends on a closed 4h candle. |
| `decision_time` | Capacity is checked after entry-zone touch, reclaim confirmation, quantity sizing, cash sizing, and notional sizing. | Blocked events must be recorded after these earlier gates pass. |
| `fill_time` | Entry raw price is `entry_high`, then `entry_fill` adds entry slippage; event time is the same `bar_time`. | Audit warning: signal confirmation and event timestamp are same-bar, while raw fill price is not explicitly next-bar open. |
| exit/entry order | Existing active positions are advanced before WATCHING plans are processed. | Capacity snapshots must be taken after same-bar active exits/time exits. |
| WATCHING order | WATCHING plans sort by `(-score, created_index, symbol)`. | Multi-candidate events must use this order for primary sample selection. |
| same-bar entry risk | `step_trade` can move a WATCHING trade to ENTERED and then evaluate ENTERED/TP1_HIT stop/TP logic in the same call. | Same-bar entry/exit or TP1 outcomes need explicit ambiguity flags. |

## Run Evidence

| Metric | Value |
|---|---:|
| entered_trades | 58 |
| same_bar_entry_and_exit_trades | 1 |
| same_bar_entry_and_tp1_trades | 0 |
| persisted max-active skipped notes | 0 |

Persisted max-active skipped notes are expected to be incomplete because later plan notes can overwrite skipped-entry attempts. Stage 1 must export blocked events directly from replay rather than infer them from final trade notes.

## Cost And Fill Assumptions

| Field | Value |
|---|---:|
| maker_fee_bps | 4.00 |
| taker_fee_bps | 10.00 |
| entry_slippage_bps | 5.00 |
| stop_slippage_bps | 10.00 |
| entry_reclaim_close_enabled | True |
| entry_reclaim_min_atr_enabled | False |
| entry_reclaim_min_atr | 0.00 |

## Source Markers

| Behavior | Source marker |
|---|---|
| active exits before watching entries | `# First advance exits for active positions, then process existing condition plans.` |
| WATCHING sort order | `watching.sort(key=lambda item: (-item.score, item.created_index, item.paper.symbol))` |
| reclaim check | `def _entry_reclaim_close_satisfied(` |
| raw entry price | `raw_entry = item.paper.entry_high` |
| capacity check | `if len(_active_positions(all_trades)) >= settings.backtest.max_active_positions:` |
| same-call ENTERED evaluation | `if trade.status in {"ENTERED", "TP1_HIT"} and trade.entry_price is not None and trade.quantity:` |

## Decision

`timing_audit_warn_same_bar_ambiguity`

## Next Action

Proceed to design `blocked_entry_event_export`, but include explicit fields for same-bar ambiguity:

- `signal_time`
- `decision_time`
- `fill_time_assumption`
- `active_snapshot_after_exits`
- `same_bar_entry_exit_possible`
- `same_bar_entry_tp1_possible`

## Raw Summary

```json
{
  "run_id": "110c51eef593",
  "report_date": "2026-07-27",
  "start_utc": "2025-06-01T00:00:00+00:00",
  "end_utc": "2026-06-01T00:00:00+00:00",
  "commit_hash": "b9cb5e23eeb069e2b6b2552e3d1e9d54f4c5f036",
  "symbols_count": 294,
  "entry_reclaim_close_enabled": true,
  "entry_reclaim_min_atr_enabled": false,
  "entry_reclaim_min_atr": 0.0,
  "max_active_positions": 5,
  "intrabar_policy": null,
  "maker_fee_bps": 4.0,
  "taker_fee_bps": 10.0,
  "entry_slippage_bps": 5.0,
  "stop_slippage_bps": 10.0,
  "entered_trades": 58,
  "same_bar_entry_and_exit_trades": 1,
  "same_bar_entry_and_tp1_trades": 0,
  "blocked_notes_persisted": 0,
  "verdict": "timing_audit_warn_same_bar_ambiguity",
  "reason": "replay order is inspectable, but WATCHING entry and same-bar stop/TP evaluation can occur in one step_trade call; later capacity diagnostics must explicitly account for same-bar ambiguity."
}
```
