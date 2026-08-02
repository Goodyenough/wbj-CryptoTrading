# Paper Shadow Decision-State Reconciliation v5

## Scope

- This report is read-only and does not change `config/settings.toml`, paper plans, events, snapshots, or strategy defaults.
- Required lines: `reference_baseline`, `atr_reclaim_0_35_shadow`, `research_incumbent`.
- The goal is state reconciliation, not strategy validation.

## Verdict

- verdict: `reconciliation_waiting_for_terminal_outcomes`
- reason: All opportunities have the required lines, but no plan-linked opportunity is mature terminal yet.

## Summary

| Metric | Value |
|---|---:|
| decisions | 87 |
| opportunities | 16 |
| complete opportunities | 16 |
| incomplete opportunities | 0 |
| controls_paper rows | 0 |
| mismatch opportunities | 0 |
| mature terminal opportunities | 0 |
| right-censored opportunities | 1 |
| independent symbols | 11 |

## Pre-Attribution Gate

| Requirement | Current | Minimum |
|---|---:|---:|
| complete opportunities | 16 | 10 |
| mature terminal opportunities | 0 | 5 |
| independent symbols | 11 | 3 |
| controls_paper rows | 0 | 0 |
| incomplete opportunities | 0 | 0 |

## Run Context

- latest_daily_run: `20260801_120503_ca7e4bfc` status=`success`
- latest_4h_run: `20260802_081002_5dfb626b` status=`success`
- open_plan_count: 1
- watching_plan_count: 1

### Open Plans

| Plan | Symbol | Status | Entry low | Entry high | Updated |
|---|---|---|---:|---:|---|
| `9734a33dea2e` | `ONDOUSDT` | `WATCHING` | 0.394505 | 0.41156785714285715 | 2026-08-02T08:10:02Z |

## By Line

| Line | Count |
|---|---:|
| `atr_reclaim_0_35_shadow` | 29 |
| `reference_baseline` | 29 |
| `research_incumbent` | 29 |

## By Stage

| Stage | Count |
|---|---:|
| `candidate_level` | 45 |
| `paper_4h_decision` | 42 |

## By Decision

| Decision | Count |
|---|---:|
| `candidate_registered` | 45 |
| `reject` | 42 |

## By Opportunity

| Opportunity | Rows | Symbols | Lines | Missing lines | Decisions | Accepted | Maturity | Plan status |
|---|---:|---|---|---|---|---|---|---|
| `paper_plan:9734a33dea2e` | 42 | `ONDOUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:reject,reference_baseline:reject,research_incumbent:reject` | `atr_reclaim_0_35_shadow:0,reference_baseline:0,research_incumbent:0` | `right_censored_open` | `WATCHING` |
| `scan_candidate:03db6f5625c0:BNBUSDT` | 3 | `BNBUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:03db6f5625c0:ETHUSDT` | 3 | `ETHUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:03db6f5625c0:EULUSDT` | 3 | `EULUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:03db6f5625c0:MMTUSDT` | 3 | `MMTUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:03db6f5625c0:UNIUSDT` | 3 | `UNIUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:3f882458ad8a:BNBUSDT` | 3 | `BNBUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:3f882458ad8a:BTCUSDT` | 3 | `BTCUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:3f882458ad8a:ETHUSDT` | 3 | `ETHUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:3f882458ad8a:GIGGLEUSDT` | 3 | `GIGGLEUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:3f882458ad8a:MIRAUSDT` | 3 | `MIRAUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:ac6f6d17c4a3:BNBUSDT` | 3 | `BNBUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:ac6f6d17c4a3:BTCUSDT` | 3 | `BTCUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:ac6f6d17c4a3:COTIUSDT` | 3 | `COTIUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:ac6f6d17c4a3:ETHUSDT` | 3 | `ETHUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:ac6f6d17c4a3:XRPUSDT` | 3 | `XRPUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |

## Interpretation

- Empty shadow decisions mean the system is still waiting for prospective samples.
- Missing required lines block attribution because baseline, `0.35`, and incumbent would not share the same observation point.
- Mature terminal opportunities are required before direct filtering or path/capacity contribution can be interpreted.
- Any `controls_paper=1` row is a failure for this shadow phase unless explicitly approved later.
