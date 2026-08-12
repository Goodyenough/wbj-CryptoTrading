# Paper Shadow Decision-State Reconciliation v4

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
| decisions | 153 |
| opportunities | 31 |
| complete opportunities | 31 |
| incomplete opportunities | 0 |
| controls_paper rows | 0 |
| mismatch opportunities | 0 |
| mature terminal opportunities | 0 |
| right-censored opportunities | 1 |
| independent symbols | 17 |
| candidate observations | 10 |
| counterfactual outcomes | 30 |
| terminal counterfactual outcomes | 0 |

## Pre-Attribution Gate

| Requirement | Current | Minimum |
|---|---:|---:|
| complete opportunities | 31 | 10 |
| mature terminal opportunities | 0 | 5 |
| independent symbols | 17 | 3 |
| controls_paper rows | 0 | 0 |
| incomplete opportunities | 0 | 0 |

## Run Context

- latest_daily_run: `20260809_120503_3b3edf94` status=`success`
- latest_4h_run: `20260810_041003_adba9021` status=`success`
- open_plan_count: 1
- watching_plan_count: 1

### Open Plans

| Plan | Symbol | Status | Entry low | Entry high | Updated |
|---|---|---|---:|---:|---|
| `9734a33dea2e` | `ONDOUSDT` | `WATCHING` | 0.394505 | 0.41156785714285715 | 2026-08-10T04:10:03Z |

## By Line

| Line | Count |
|---|---:|
| `atr_reclaim_0_35_shadow` | 51 |
| `reference_baseline` | 51 |
| `research_incumbent` | 51 |

## By Stage

| Stage | Count |
|---|---:|
| `candidate_level` | 90 |
| `paper_4h_decision` | 63 |

## By Decision

| Decision | Count |
|---|---:|
| `candidate_registered` | 90 |
| `reject` | 63 |

## By Opportunity

| Opportunity | Rows | Symbols | Lines | Missing lines | Decisions | Accepted | Maturity | Plan status |
|---|---:|---|---|---|---|---|---|---|
| `paper_plan:9734a33dea2e` | 63 | `ONDOUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:reject,reference_baseline:reject,research_incumbent:reject` | `atr_reclaim_0_35_shadow:0,reference_baseline:0,research_incumbent:0` | `right_censored_open` | `WATCHING` |
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
| `scan_candidate:65af47840f77:ADAUSDT` | 3 | `ADAUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:65af47840f77:BNBUSDT` | 3 | `BNBUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:65af47840f77:EULUSDT` | 3 | `EULUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:65af47840f77:XRPUSDT` | 3 | `XRPUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:65af47840f77:ZECUSDT` | 3 | `ZECUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:ac6f6d17c4a3:BNBUSDT` | 3 | `BNBUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:ac6f6d17c4a3:BTCUSDT` | 3 | `BTCUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:ac6f6d17c4a3:COTIUSDT` | 3 | `COTIUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:ac6f6d17c4a3:ETHUSDT` | 3 | `ETHUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:ac6f6d17c4a3:XRPUSDT` | 3 | `XRPUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:af613d2bf39b:BNBUSDT` | 3 | `BNBUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:af613d2bf39b:BTCUSDT` | 3 | `BTCUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:af613d2bf39b:HEIUSDT` | 3 | `HEIUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:af613d2bf39b:TRXUSDT` | 3 | `TRXUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:af613d2bf39b:ZECUSDT` | 3 | `ZECUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:e6059958bb9f:BABYUSDT` | 3 | `BABYUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:e6059958bb9f:BNBUSDT` | 3 | `BNBUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:e6059958bb9f:BTCUSDT` | 3 | `BTCUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:e6059958bb9f:ETHUSDT` | 3 | `ETHUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:e6059958bb9f:TUTUSDT` | 3 | `TUTUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |

## Interpretation

- Empty shadow decisions mean the system is still waiting for prospective samples.
- Missing required lines block attribution because baseline, `0.35`, and incumbent would not share the same observation point.
- Mature terminal opportunities are required before direct filtering or path/capacity contribution can be interpreted.
- Any `controls_paper=1` row is a failure for this shadow phase unless explicitly approved later.
