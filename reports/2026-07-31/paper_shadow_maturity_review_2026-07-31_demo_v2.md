# atr_reclaim prospective shadow maturity review v2

## Scope

- This report is read-only. It does not change `config/settings.toml`, paper plans, paper events, snapshots, or strategy defaults.
- `reference_baseline` is the original strategy without `atr_reclaim_0_35`.
- `atr_reclaim_0_35_shadow` is the independent forward reference line for original strategy plus `0.35`.
- `research_incumbent` is the current research baseline, not an automatic paper deployment.

## Verdict

- verdict: `candidate_context_only`
- reason: Only candidate-level context exists; no plan-level decision outcomes can be reviewed yet.

## Maturity Summary

| Metric | Value |
|---|---:|
| decisions | 15 |
| opportunities | 5 |
| candidate-only rows | 15 |
| plan-linked decision rows | 0 |
| mature terminal rows | 0 |
| right-censored open rows | 0 |
| unknown plan rows | 0 |
| right-censored ratio | 0.00% |

## Waiting Diagnostics

- open_plan_count: 1
- watching_plan_count: 1
- latest_scan: `ac6f6d17c4a3` at `2026-07-30T12:06:00+00:00`
- latest_daily_run: `20260730_120502_4a73a4c7` status=`success`
- latest_4h_run: `20260730_201002_8208737e` status=`success`
- next_trigger: Wait for a WATCHING plan to touch entry_high during a 4h paper update.

### Open Plans

| Plan | Symbol | Status | Entry low | Entry high | Updated |
|---|---|---|---:|---:|---|
| `9734a33dea2e` | `ONDOUSDT` | `WATCHING` | 0.394505 | 0.41156785714285715 | 2026-07-30T12:06:01Z |

## By Line

| Line | Count |
|---|---:|
| `atr_reclaim_0_35_shadow` | 5 |
| `reference_baseline` | 5 |
| `research_incumbent` | 5 |

## By Opportunity

| Opportunity | Rows | Lines | Maturity | Capacity | Scanner action |
|---|---:|---|---|---|---|
| `scan_candidate:ac6f6d17c4a3:BNBUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:ac6f6d17c4a3:BTCUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:ac6f6d17c4a3:COTIUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:ac6f6d17c4a3:ETHUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:ac6f6d17c4a3:XRPUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |

## By Stage

| Stage | Count |
|---|---:|
| `daily_import_candidate_context` | 15 |

## By Capacity State

| Capacity state | Count |
|---|---:|
| `capacity_available` | 15 |

## By Scanner Action

| Scanner action | Count |
|---|---:|
| `WATCH_ONLY` | 15 |

## Terminal Outcomes

| Plan status | Count |
|---|---:|
| none | 0 |

## Interpretation

- Candidate-only rows are useful for confirming that all three lines saw the same scan candidate, but they do not prove trade quality.
- Plan-linked rows can become maturity evidence only after the linked paper plan reaches a terminal status.
- Until mature terminal samples are sufficient, `atr_reclaim_0_35` remains a prospective shadow reference, not a paper deployment rule.
