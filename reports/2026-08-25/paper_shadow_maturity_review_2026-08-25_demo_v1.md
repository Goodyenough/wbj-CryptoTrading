# atr_reclaim prospective shadow maturity review v1

## Scope

- This report is read-only. It does not change `config/settings.toml`, paper plans, paper events, snapshots, or strategy defaults.
- `reference_baseline` is the original strategy without `atr_reclaim_0_35`.
- `atr_reclaim_0_35_shadow` is the independent forward reference line for original strategy plus `0.35`.
- `research_incumbent` is the current research baseline, not an automatic paper deployment.

## Verdict

- verdict: `maturity_review_available`
- reason: At least one plan-linked shadow decision has reached a terminal paper status.

## Maturity Summary

| Metric | Value |
|---|---:|
| decisions | 615 |
| opportunities | 103 |
| candidate-only rows | 300 |
| plan-linked decision rows | 315 |
| mature terminal rows | 3 |
| right-censored open rows | 312 |
| unknown plan rows | 0 |
| right-censored ratio | 99.05% |
| candidate observations | 80 |
| counterfactual outcomes | 240 |
| terminal counterfactual outcomes | 137 |

## Waiting Diagnostics

- open_plan_count: 7
- watching_plan_count: 6
- latest_scan: `ed103f737b70` at `2026-08-24T12:07:11+00:00`
- latest_daily_run: `20260824_120503_b6999dcc` status=`success`
- latest_4h_run: `20260824_161003_3277f7a6` status=`success`
- next_trigger: Review direct filtering and capacity/path contribution once the sample reaches the pre-set threshold.

### Open Plans

| Plan | Symbol | Status | Entry low | Entry high | Updated |
|---|---|---|---:|---:|---|
| `0a265e9f2163` | `TAOUSDT` | `WATCHING` | 228.60382318459742 | 234.16752812834073 | 2026-08-24T16:10:03Z |
| `34a7cc973d13` | `BTCUSDT` | `WATCHING` | 76527.52156974994 | 76994.94152569854 | 2026-08-24T16:10:03Z |
| `56474a1c8879` | `TRXUSDT` | `WATCHING` | 0.33687782084620144 | 0.33763041002614913 | 2026-08-24T16:10:03Z |
| `9734a33dea2e` | `ONDOUSDT` | `WATCHING` | 0.394505 | 0.41156785714285715 | 2026-08-24T16:10:03Z |
| `bffd2fdd7e2b` | `ETHUSDT` | `WATCHING` | 2413.8617567754914 | 2441.032169436618 | 2026-08-24T16:10:03Z |
| `eb16fbac349f` | `SOLUSDT` | `WATCHING` | 93.1115473438544 | 94.44769595195051 | 2026-08-24T16:10:03Z |
| `ecdc3e95f224` | `UNIUSDT` | `ENTERED` | 4.237943717270133 | 4.357384747774584 | 2026-08-24T16:10:03Z |

## By Line

| Line | Count |
|---|---:|
| `atr_reclaim_0_35_shadow` | 205 |
| `reference_baseline` | 205 |
| `research_incumbent` | 205 |

## By Opportunity

| Opportunity | Rows | Lines | Maturity | Capacity | Scanner action |
|---|---:|---|---|---|---|
| `paper_plan:9734a33dea2e` | 309 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `right_censored_open:309` | `capacity_available:309` | `unknown:309` |
| `paper_plan:ac939ee74e2c` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `mature_terminal:3` | `capacity_available:3` | `unknown:3` |
| `paper_plan:ecdc3e95f224` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `right_censored_open:3` | `capacity_available:3` | `unknown:3` |
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
| `scan_candidate:110604e1204a:ACEUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:110604e1204a:ALLOUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:110604e1204a:BTCUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:110604e1204a:ETHUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:110604e1204a:SOLUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:2ee5c0fa058f:ETHUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:2ee5c0fa058f:LINKUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:2ee5c0fa058f:ONGUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:2ee5c0fa058f:TRXUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:2ee5c0fa058f:ZECUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:320bc0bceb6a:BTCUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:320bc0bceb6a:DOGEUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WAIT_PULLBACK:3` |
| `scan_candidate:320bc0bceb6a:ETHUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:320bc0bceb6a:SOLUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:320bc0bceb6a:UNIUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WAIT_PULLBACK:3` |
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
| `scan_candidate:6a84e67a5013:PLUMEUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WAIT_PULLBACK:3` |
| `scan_candidate:6a84e67a5013:PUMPUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:6a84e67a5013:TRUMPUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WAIT_PULLBACK:3` |
| `scan_candidate:6a84e67a5013:TRXUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:6a84e67a5013:WLDUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WAIT_PULLBACK:3` |
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
| `scan_candidate:dd4ccf80b821:ADAUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WAIT_PULLBACK:3` |
| `scan_candidate:dd4ccf80b821:ETHUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WAIT_PULLBACK:3` |
| `scan_candidate:dd4ccf80b821:LINKUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WAIT_PULLBACK:3` |
| `scan_candidate:dd4ccf80b821:SUIUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WAIT_PULLBACK:3` |
| `scan_candidate:dd4ccf80b821:XLMUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WAIT_PULLBACK:3` |
| `scan_candidate:e6059958bb9f:BABYUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WAIT_PULLBACK:3` |
| `scan_candidate:e6059958bb9f:BNBUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:e6059958bb9f:BTCUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:e6059958bb9f:ETHUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:e6059958bb9f:TUTUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:ed103f737b70:BTCUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:ed103f737b70:ETHUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:ed103f737b70:SOLUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:ed103f737b70:TAOUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:ed103f737b70:UNIUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `BUY_CANDIDATE:3` |

## By Stage

| Stage | Count |
|---|---:|
| `daily_import_candidate_context` | 300 |
| `decision_level_unknown` | 315 |

## By Capacity State

| Capacity state | Count |
|---|---:|
| `capacity_available` | 615 |

## By Scanner Action

| Scanner action | Count |
|---|---:|
| `BUY_CANDIDATE` | 48 |
| `REJECT` | 30 |
| `WAIT_PULLBACK` | 48 |
| `WATCH_ONLY` | 174 |
| `unknown` | 315 |

## Terminal Outcomes

| Plan status | Count |
|---|---:|
| `ARCHIVED` | 3 |

## Interpretation

- Candidate-only rows are useful for confirming that all three lines saw the same scan candidate, but they do not prove trade quality.
- Plan-linked rows can become maturity evidence only after the linked paper plan reaches a terminal status.
- Until mature terminal samples are sufficient, `atr_reclaim_0_35` remains a prospective shadow reference, not a paper deployment rule.
