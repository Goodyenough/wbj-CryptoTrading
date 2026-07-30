# atr_reclaim prospective shadow maturity review v10

## Scope

- This report is read-only. It does not change `config/settings.toml`, paper plans, paper events, snapshots, or strategy defaults.
- `reference_baseline` is the original strategy without `atr_reclaim_0_35`.
- `atr_reclaim_0_35_shadow` is the independent forward reference line for original strategy plus `0.35`.
- `research_incumbent` is the current research baseline, not an automatic paper deployment.

## Verdict

- verdict: `no_shadow_samples_yet`
- reason: paper_shadow_decisions is empty for this account.

## Maturity Summary

| Metric | Value |
|---|---:|
| decisions | 0 |
| opportunities | 0 |
| candidate-only rows | 0 |
| plan-linked decision rows | 0 |
| mature terminal rows | 0 |
| right-censored open rows | 0 |
| unknown plan rows | 0 |
| right-censored ratio | 0.00% |

## Waiting Diagnostics

- open_plan_count: 1
- watching_plan_count: 1
- latest_scan: `3a77f1af8f42` at `2026-07-29T12:06:34+00:00`
- latest_daily_run: `20260729_120502_400dc662` status=`success`
- latest_4h_run: `20260730_111428_76a80af1` status=`success`
- next_trigger: Wait for the next daily scan/import candidate rows, or for a WATCHING plan to touch entry_high during a 4h paper update so plan-linked shadow decisions can be recorded.

### Open Plans

| Plan | Symbol | Status | Entry low | Entry high | Updated |
|---|---|---|---:|---:|---|
| `9734a33dea2e` | `ONDOUSDT` | `WATCHING` | 0.394505 | 0.41156785714285715 | 2026-07-30T11:14:28Z |

## By Line

| Line | Count |
|---|---:|
| none | 0 |

## By Opportunity

| Opportunity | Rows | Lines | Maturity | Capacity | Scanner action |
|---|---:|---|---|---|---|
| none | 0 |  |  |  |  |

## By Stage

| Stage | Count |
|---|---:|
| none | 0 |

## By Capacity State

| Capacity state | Count |
|---|---:|
| none | 0 |

## By Scanner Action

| Scanner action | Count |
|---|---:|
| none | 0 |

## Terminal Outcomes

| Plan status | Count |
|---|---:|
| none | 0 |

## Interpretation

- Candidate-only rows are useful for confirming that all three lines saw the same scan candidate, but they do not prove trade quality.
- Plan-linked rows can become maturity evidence only after the linked paper plan reaches a terminal status.
- Until mature terminal samples are sufficient, `atr_reclaim_0_35` remains a prospective shadow reference, not a paper deployment rule.
