# Paper Shadow Decision-State Reconciliation v5

## Scope

- This report is read-only and does not change `config/settings.toml`, paper plans, events, snapshots, or strategy defaults.
- Required lines: `reference_baseline`, `atr_reclaim_0_35_shadow`, `research_incumbent`.
- The goal is state reconciliation, not strategy validation.

## Verdict

- verdict: `reconciliation_waiting_for_sample_threshold`
- reason: Three-line reconciliation is structurally clean, but the minimum pre-attribution sample gate has not been reached.

## Summary

| Metric | Value |
|---|---:|
| decisions | 495 |
| opportunities | 82 |
| complete opportunities | 82 |
| incomplete opportunities | 0 |
| controls_paper rows | 0 |
| mismatch opportunities | 0 |
| mature terminal opportunities | 1 |
| right-censored opportunities | 1 |
| independent symbols | 31 |
| candidate observations | 60 |
| counterfactual outcomes | 180 |
| terminal counterfactual outcomes | 125 |

## Pre-Attribution Gate

| Requirement | Current | Minimum |
|---|---:|---:|
| complete opportunities | 82 | 10 |
| mature terminal opportunities | 1 | 5 |
| independent symbols | 31 | 3 |
| controls_paper rows | 0 | 0 |
| incomplete opportunities | 0 | 0 |

## Run Context

- latest_daily_run: `20260820_120503_19950d20` status=`success`
- latest_4h_run: `20260821_081004_6bc7c423` status=`success`
- open_plan_count: 5
- watching_plan_count: 5

### Open Plans

| Plan | Symbol | Status | Entry low | Entry high | Updated |
|---|---|---|---:|---:|---|
| `0629b2ffa602` | `TRXUSDT` | `WATCHING` | 0.3342760165260081 | 0.3348137989281518 | 2026-08-21T08:10:04Z |
| `6c424aa918fb` | `SOLUSDT` | `WATCHING` | 76.63113721248224 | 76.9411808507807 | 2026-08-21T08:10:04Z |
| `7b4d014fe7e2` | `BTCUSDT` | `WATCHING` | 64260.66724337454 | 64428.49443849754 | 2026-08-21T08:10:04Z |
| `9734a33dea2e` | `ONDOUSDT` | `WATCHING` | 0.394505 | 0.41156785714285715 | 2026-08-21T08:10:04Z |
| `fd7033e6abc6` | `ETHUSDT` | `WATCHING` | 1910.6152808344302 | 1917.3911774794713 | 2026-08-21T08:10:04Z |

## By Line

| Line | Count |
|---|---:|
| `atr_reclaim_0_35_shadow` | 165 |
| `reference_baseline` | 165 |
| `research_incumbent` | 165 |

## By Stage

| Stage | Count |
|---|---:|
| `candidate_level` | 240 |
| `paper_4h_decision` | 255 |

## By Decision

| Decision | Count |
|---|---:|
| `candidate_registered` | 240 |
| `reject` | 255 |

## By Opportunity

| Opportunity | Rows | Symbols | Lines | Missing lines | Decisions | Accepted | Maturity | Plan status |
|---|---:|---|---|---|---|---|---|---|
| `paper_plan:9734a33dea2e` | 252 | `ONDOUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:reject,reference_baseline:reject,research_incumbent:reject` | `atr_reclaim_0_35_shadow:0,reference_baseline:0,research_incumbent:0` | `right_censored_open` | `WATCHING` |
| `paper_plan:ac939ee74e2c` | 3 | `ETHUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:reject,reference_baseline:reject,research_incumbent:reject` | `atr_reclaim_0_35_shadow:0,reference_baseline:0,research_incumbent:0` | `mature_terminal` | `ARCHIVED` |
| `scan_candidate:03db6f5625c0:BNBUSDT` | 3 | `BNBUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:03db6f5625c0:ETHUSDT` | 3 | `ETHUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:03db6f5625c0:EULUSDT` | 3 | `EULUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:03db6f5625c0:MMTUSDT` | 3 | `MMTUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:03db6f5625c0:UNIUSDT` | 3 | `UNIUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:0bd63f946d48:BNBUSDT` | 3 | `BNBUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:0bd63f946d48:BTCUSDT` | 3 | `BTCUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:0bd63f946d48:EDENUSDT` | 3 | `EDENUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:0bd63f946d48:ETHUSDT` | 3 | `ETHUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:0bd63f946d48:SOLUSDT` | 3 | `SOLUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:110604e1204a:ACEUSDT` | 3 | `ACEUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:110604e1204a:ALLOUSDT` | 3 | `ALLOUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:110604e1204a:BTCUSDT` | 3 | `BTCUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:110604e1204a:ETHUSDT` | 3 | `ETHUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:110604e1204a:SOLUSDT` | 3 | `SOLUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:3f882458ad8a:BNBUSDT` | 3 | `BNBUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:3f882458ad8a:BTCUSDT` | 3 | `BTCUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:3f882458ad8a:ETHUSDT` | 3 | `ETHUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:3f882458ad8a:GIGGLEUSDT` | 3 | `GIGGLEUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:3f882458ad8a:MIRAUSDT` | 3 | `MIRAUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:4ac624d4005e:BNBUSDT` | 3 | `BNBUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:4ac624d4005e:DOGEUSDT` | 3 | `DOGEUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:4ac624d4005e:ETHUSDT` | 3 | `ETHUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:4ac624d4005e:SOLUSDT` | 3 | `SOLUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:4ac624d4005e:ZECUSDT` | 3 | `ZECUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:5b204540bee0:BNBUSDT` | 3 | `BNBUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:5b204540bee0:BTCUSDT` | 3 | `BTCUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:5b204540bee0:MMTUSDT` | 3 | `MMTUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:5b204540bee0:MUBARAKUSDT` | 3 | `MUBARAKUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:5b204540bee0:TUTUSDT` | 3 | `TUTUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:65af47840f77:ADAUSDT` | 3 | `ADAUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:65af47840f77:BNBUSDT` | 3 | `BNBUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:65af47840f77:EULUSDT` | 3 | `EULUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:65af47840f77:XRPUSDT` | 3 | `XRPUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:65af47840f77:ZECUSDT` | 3 | `ZECUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:6a84e67a5013:PLUMEUSDT` | 3 | `PLUMEUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:6a84e67a5013:PUMPUSDT` | 3 | `PUMPUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:6a84e67a5013:TRUMPUSDT` | 3 | `TRUMPUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:6a84e67a5013:TRXUSDT` | 3 | `TRXUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:6a84e67a5013:WLDUSDT` | 3 | `WLDUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:6ccdb7972935:BNBUSDT` | 3 | `BNBUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:6ccdb7972935:BTCUSDT` | 3 | `BTCUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:6ccdb7972935:ETHUSDT` | 3 | `ETHUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:6ccdb7972935:HEMIUSDT` | 3 | `HEMIUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:6ccdb7972935:XPLUSDT` | 3 | `XPLUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:741093cc2c86:ACEUSDT` | 3 | `ACEUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:741093cc2c86:BTCUSDT` | 3 | `BTCUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:741093cc2c86:ETHUSDT` | 3 | `ETHUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:741093cc2c86:SOLUSDT` | 3 | `SOLUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:741093cc2c86:ZECUSDT` | 3 | `ZECUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
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
| `scan_candidate:b36a978be600:ACEUSDT` | 3 | `ACEUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:b36a978be600:BNBUSDT` | 3 | `BNBUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:b36a978be600:LINKUSDT` | 3 | `LINKUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:b36a978be600:PLUMEUSDT` | 3 | `PLUMEUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:b36a978be600:XPLUSDT` | 3 | `XPLUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:c453a9b4f0d0:BNBUSDT` | 3 | `BNBUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:c453a9b4f0d0:BTCUSDT` | 3 | `BTCUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:c453a9b4f0d0:ETHUSDT` | 3 | `ETHUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:c453a9b4f0d0:SOLUSDT` | 3 | `SOLUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:c453a9b4f0d0:TUTUSDT` | 3 | `TUTUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:d889ad7bd72e:BTCUSDT` | 3 | `BTCUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:d889ad7bd72e:ETHUSDT` | 3 | `ETHUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:d889ad7bd72e:PORTALUSDT` | 3 | `PORTALUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:d889ad7bd72e:SOLUSDT` | 3 | `SOLUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
| `scan_candidate:d889ad7bd72e:ZECUSDT` | 3 | `ZECUSDT` | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `none` | `atr_reclaim_0_35_shadow:candidate_registered,reference_baseline:candidate_registered,research_incumbent:candidate_registered` | `atr_reclaim_0_35_shadow:1,reference_baseline:1,research_incumbent:1` | `candidate_only_or_unknown_plan` | `none` |
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
