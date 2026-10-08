# atr_reclaim prospective shadow maturity review v2

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
| decisions | 420 |
| opportunities | 72 |
| candidate-only rows | 210 |
| plan-linked decision rows | 210 |
| mature terminal rows | 0 |
| right-censored open rows | 210 |
| unknown plan rows | 0 |
| right-censored ratio | 100.00% |
| candidate observations | 50 |
| counterfactual outcomes | 150 |
| terminal counterfactual outcomes | 15 |

## Waiting Diagnostics

- open_plan_count: 4
- watching_plan_count: 4
- latest_scan: `741093cc2c86` at `2026-08-18T12:06:23+00:00`
- latest_daily_run: `20260818_120504_a5fbee24` status=`success`
- latest_4h_run: `20260818_201004_1a12f502` status=`success`
- next_trigger: Wait for plan-linked shadow decisions to reach terminal paper statuses.

### Open Plans

| Plan | Symbol | Status | Entry low | Entry high | Updated |
|---|---|---|---:|---:|---|
| `4a9a6cbaad0e` | `SOLUSDT` | `WATCHING` | 75.94465274308294 | 76.28056660986321 | 2026-08-18T20:10:04Z |
| `6360f05a90ec` | `BTCUSDT` | `WATCHING` | 64038.62190522268 | 64184.64430461345 | 2026-08-18T20:10:04Z |
| `9734a33dea2e` | `ONDOUSDT` | `WATCHING` | 0.394505 | 0.41156785714285715 | 2026-08-18T20:10:04Z |
| `ac939ee74e2c` | `ETHUSDT` | `WATCHING` | 1893.4206331314404 | 1896.8373504305791 | 2026-08-18T20:10:04Z |

## By Line

| Line | Count |
|---|---:|
| `atr_reclaim_0_35_shadow` | 140 |
| `reference_baseline` | 140 |
| `research_incumbent` | 140 |

## By Opportunity

| Opportunity | Rows | Lines | Maturity | Capacity | Scanner action |
|---|---:|---|---|---|---|
| `paper_plan:9734a33dea2e` | 207 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `right_censored_open:207` | `capacity_available:207` | `unknown:207` |
| `paper_plan:ac939ee74e2c` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `right_censored_open:3` | `capacity_available:3` | `unknown:3` |
| `scan_candidate:03db6f5625c0:BNBUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:03db6f5625c0:ETHUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:03db6f5625c0:EULUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:03db6f5625c0:MMTUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WAIT_PULLBACK:3` |
| `scan_candidate:03db6f5625c0:UNIUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WAIT_PULLBACK:3` |
| `scan_candidate:0bd63f946d48:BNBUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `REJECT:3` |
| `scan_candidate:0bd63f946d48:BTCUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `REJECT:3` |
| `scan_candidate:0bd63f946d48:EDENUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:0bd63f946d48:ETHUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `REJECT:3` |
| `scan_candidate:0bd63f946d48:SOLUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:3f882458ad8a:BNBUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:3f882458ad8a:BTCUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `REJECT:3` |
| `scan_candidate:3f882458ad8a:ETHUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `REJECT:3` |
| `scan_candidate:3f882458ad8a:GIGGLEUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:3f882458ad8a:MIRAUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `REJECT:3` |
| `scan_candidate:4ac624d4005e:BNBUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:4ac624d4005e:DOGEUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:4ac624d4005e:ETHUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `REJECT:3` |
| `scan_candidate:4ac624d4005e:SOLUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:4ac624d4005e:ZECUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `REJECT:3` |
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
| `scan_candidate:6ccdb7972935:BNBUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:6ccdb7972935:BTCUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:6ccdb7972935:ETHUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:6ccdb7972935:HEMIUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WAIT_PULLBACK:3` |
| `scan_candidate:6ccdb7972935:XPLUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WAIT_PULLBACK:3` |
| `scan_candidate:741093cc2c86:ACEUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:741093cc2c86:BTCUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:741093cc2c86:ETHUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:741093cc2c86:SOLUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:741093cc2c86:ZECUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
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
| `scan_candidate:b36a978be600:ACEUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:b36a978be600:BNBUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:b36a978be600:LINKUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:b36a978be600:PLUMEUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WAIT_PULLBACK:3` |
| `scan_candidate:b36a978be600:XPLUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:c453a9b4f0d0:BNBUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:c453a9b4f0d0:BTCUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:c453a9b4f0d0:ETHUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:c453a9b4f0d0:SOLUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:c453a9b4f0d0:TUTUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:d889ad7bd72e:BTCUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:d889ad7bd72e:ETHUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:d889ad7bd72e:PORTALUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:d889ad7bd72e:SOLUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:d889ad7bd72e:ZECUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:e6059958bb9f:BABYUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WAIT_PULLBACK:3` |
| `scan_candidate:e6059958bb9f:BNBUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:e6059958bb9f:BTCUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:e6059958bb9f:ETHUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:e6059958bb9f:TUTUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |

## By Stage

| Stage | Count |
|---|---:|
| `daily_import_candidate_context` | 210 |
| `decision_level_unknown` | 210 |

## By Capacity State

| Capacity state | Count |
|---|---:|
| `capacity_available` | 420 |

## By Scanner Action

| Scanner action | Count |
|---|---:|
| `BUY_CANDIDATE` | 9 |
| `REJECT` | 30 |
| `WAIT_PULLBACK` | 18 |
| `WATCH_ONLY` | 153 |
| `unknown` | 210 |

## Terminal Outcomes

| Plan status | Count |
|---|---:|
| none | 0 |

## Interpretation

- Candidate-only rows are useful for confirming that all three lines saw the same scan candidate, but they do not prove trade quality.
- Plan-linked rows can become maturity evidence only after the linked paper plan reaches a terminal status.
- Until mature terminal samples are sufficient, `atr_reclaim_0_35` remains a prospective shadow reference, not a paper deployment rule.
