# atr_reclaim prospective shadow maturity review v1

## Scope

- This report is read-only. It does not change `config/settings.toml`, paper plans, paper events, snapshots, or strategy defaults.
- `reference_baseline` is the original strategy without `atr_reclaim_0_35`.
- `atr_reclaim_0_35_shadow` is the independent forward reference line for original strategy plus `0.35`.
- `research_incumbent` is the current research baseline, not an automatic paper deployment.

## Verdict

- verdict: `decision_samples_not_mature`
- reason: Plan-level decisions exist, but all known plan-linked samples are still open or unresolved.

## Maturity Summary

| Metric | Value |
|---|---:|
| decisions | 177 |
| opportunities | 36 |
| candidate-only rows | 105 |
| plan-linked decision rows | 72 |
| mature terminal rows | 0 |
| right-censored open rows | 72 |
| unknown plan rows | 0 |
| right-censored ratio | 100.00% |
| candidate observations | 15 |
| counterfactual outcomes | 45 |
| terminal counterfactual outcomes | 0 |

## Waiting Diagnostics

- open_plan_count: 1
- watching_plan_count: 1
- latest_scan: `5b204540bee0` at `2026-08-10T12:06:38+00:00`
- latest_daily_run: `20260810_120503_f66b7c3d` status=`success`
- latest_4h_run: `20260810_161005_b40d7fd4` status=`success`
- next_trigger: Wait for plan-linked shadow decisions to reach terminal paper statuses.

### Open Plans

| Plan | Symbol | Status | Entry low | Entry high | Updated |
|---|---|---|---:|---:|---|
| `9734a33dea2e` | `ONDOUSDT` | `WATCHING` | 0.394505 | 0.41156785714285715 | 2026-08-10T16:10:05Z |

## By Line

| Line | Count |
|---|---:|
| `atr_reclaim_0_35_shadow` | 59 |
| `reference_baseline` | 59 |
| `research_incumbent` | 59 |

## By Opportunity

| Opportunity | Rows | Lines | Maturity | Capacity | Scanner action |
|---|---:|---|---|---|---|
| `paper_plan:9734a33dea2e` | 72 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `right_censored_open:72` | `capacity_available:72` | `unknown:72` |
| `scan_candidate:03db6f5625c0:BNBUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:03db6f5625c0:ETHUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:03db6f5625c0:EULUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:03db6f5625c0:MMTUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WAIT_PULLBACK:3` |
| `scan_candidate:03db6f5625c0:UNIUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WAIT_PULLBACK:3` |
| `scan_candidate:3f882458ad8a:BNBUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:3f882458ad8a:BTCUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `REJECT:3` |
| `scan_candidate:3f882458ad8a:ETHUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `REJECT:3` |
| `scan_candidate:3f882458ad8a:GIGGLEUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:3f882458ad8a:MIRAUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `REJECT:3` |
| `scan_candidate:5b204540bee0:BNBUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:5b204540bee0:BTCUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:5b204540bee0:MMTUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:5b204540bee0:MUBARAKUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:5b204540bee0:TUTUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:65af47840f77:ADAUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:65af47840f77:BNBUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:65af47840f77:EULUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `REJECT:3` |
| `scan_candidate:65af47840f77:XRPUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:65af47840f77:ZECUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `REJECT:3` |
| `scan_candidate:ac6f6d17c4a3:BNBUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:ac6f6d17c4a3:BTCUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:ac6f6d17c4a3:COTIUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:ac6f6d17c4a3:ETHUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:ac6f6d17c4a3:XRPUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:af613d2bf39b:BNBUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:af613d2bf39b:BTCUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:af613d2bf39b:HEIUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:af613d2bf39b:TRXUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:af613d2bf39b:ZECUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:e6059958bb9f:BABYUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WAIT_PULLBACK:3` |
| `scan_candidate:e6059958bb9f:BNBUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:e6059958bb9f:BTCUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:e6059958bb9f:ETHUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:e6059958bb9f:TUTUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |

## By Stage

| Stage | Count |
|---|---:|
| `daily_import_candidate_context` | 105 |
| `decision_level_unknown` | 72 |

## By Capacity State

| Capacity state | Count |
|---|---:|
| `capacity_available` | 177 |

## By Scanner Action

| Scanner action | Count |
|---|---:|
| `REJECT` | 15 |
| `WAIT_PULLBACK` | 9 |
| `WATCH_ONLY` | 81 |
| `unknown` | 72 |

## Terminal Outcomes

| Plan status | Count |
|---|---:|
| none | 0 |

## Interpretation

- Candidate-only rows are useful for confirming that all three lines saw the same scan candidate, but they do not prove trade quality.
- Plan-linked rows can become maturity evidence only after the linked paper plan reaches a terminal status.
- Until mature terminal samples are sufficient, `atr_reclaim_0_35` remains a prospective shadow reference, not a paper deployment rule.
