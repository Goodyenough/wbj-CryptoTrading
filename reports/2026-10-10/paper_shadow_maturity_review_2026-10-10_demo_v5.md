# atr_reclaim prospective shadow maturity review v5

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
| decisions | 1539 |
| opportunities | 179 |
| candidate-only rows | 450 |
| plan-linked decision rows | 1089 |
| mature terminal rows | 231 |
| right-censored open rows | 858 |
| unknown plan rows | 0 |
| right-censored ratio | 78.79% |
| candidate observations | 130 |
| counterfactual outcomes | 390 |
| terminal counterfactual outcomes | 248 |

## Waiting Diagnostics

- open_plan_count: 13
- watching_plan_count: 10
- latest_scan: `c6386143eeed` at `2026-10-09T12:07:41+00:00`
- latest_daily_run: `20261009_120503_060f1481` status=`success`
- latest_4h_run: `20261010_081003_289c6c6c` status=`success`
- next_trigger: Review direct filtering and capacity/path contribution once the sample reaches the pre-set threshold.

### Open Plans

| Plan | Symbol | Status | Entry low | Entry high | Updated |
|---|---|---|---:|---:|---|
| `307336166337` | `ENAUSDT` | `WATCHING` | 0.16739583725893095 | 0.17167171383126842 | 2026-10-10T08:10:03Z |
| `56474a1c8879` | `TRXUSDT` | `ENTERED` | 0.33687782084620144 | 0.33763041002614913 | 2026-10-10T08:10:03Z |
| `6602caabf17a` | `PEPEUSDT` | `WATCHING` | 3.880658555256357e-06 | 3.931759999999999e-06 | 2026-10-10T08:10:03Z |
| `8be03a0ebd7e` | `LTCUSDT` | `WATCHING` | 59.488823247349856 | 60.46708308118748 | 2026-10-10T08:10:03Z |
| `94043786e3ef` | `SUIUSDT` | `WATCHING` | 0.7927911328654246 | 0.8047887154345555 | 2026-10-10T08:10:03Z |
| `94119a9f7aee` | `AAVEUSDT` | `TP1_HIT` | 144.29942228999548 | 147.61739949101343 | 2026-10-10T08:10:03Z |
| `9734a33dea2e` | `ONDOUSDT` | `WATCHING` | 0.394505 | 0.41156785714285715 | 2026-10-10T08:10:03Z |
| `cf227f0cc559` | `BNBUSDT` | `WATCHING` | 741.3499526224628 | 747.7567121980666 | 2026-10-10T08:10:03Z |
| `d058835e1b0f` | `SOLUSDT` | `ENTERED` | 102.90071170390547 | 104.5983210617819 | 2026-10-10T08:10:03Z |
| `d7619461e7f7` | `XRPUSDT` | `WATCHING` | 1.5244605364070274 | 1.5545527010050173 | 2026-10-10T08:10:03Z |

## By Line

| Line | Count |
|---|---:|
| `atr_reclaim_0_35_shadow` | 513 |
| `reference_baseline` | 513 |
| `research_incumbent` | 513 |

## By Opportunity

| Opportunity | Rows | Lines | Maturity | Capacity | Scanner action |
|---|---:|---|---|---|---|
| `paper_plan:0a265e9f2163` | 9 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `mature_terminal:9` | `capacity_available:9` | `unknown:9` |
| `paper_plan:172fa3911e40` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `mature_terminal:3` | `at_capacity:3` | `unknown:3` |
| `paper_plan:2d74b7ff6191` | 6 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `mature_terminal:6` | `at_capacity:6` | `unknown:6` |
| `paper_plan:307336166337` | 30 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `right_censored_open:30` | `at_capacity:30` | `unknown:30` |
| `paper_plan:39a6ae4b393e` | 12 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `mature_terminal:12` | `capacity_available:12` | `unknown:12` |
| `paper_plan:4f2f0f1fa0e7` | 9 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `mature_terminal:9` | `at_capacity:6,capacity_available:3` | `unknown:9` |
| `paper_plan:549cfdd6bdc4` | 6 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `mature_terminal:6` | `at_capacity:6` | `unknown:6` |
| `paper_plan:56474a1c8879` | 27 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `right_censored_open:27` | `capacity_available:27` | `unknown:27` |
| `paper_plan:5ff6dab72dfa` | 27 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `mature_terminal:27` | `at_capacity:24,capacity_available:3` | `unknown:27` |
| `paper_plan:6602caabf17a` | 123 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `right_censored_open:123` | `at_capacity:93,capacity_available:30` | `unknown:123` |
| `paper_plan:67ed9d733634` | 111 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `mature_terminal:111` | `at_capacity:90,capacity_available:21` | `unknown:111` |
| `paper_plan:8be03a0ebd7e` | 6 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `right_censored_open:6` | `at_capacity:6` | `unknown:6` |
| `paper_plan:94043786e3ef` | 6 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `right_censored_open:6` | `at_capacity:6` | `unknown:6` |
| `paper_plan:94119a9f7aee` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `right_censored_open:3` | `at_capacity:3` | `unknown:3` |
| `paper_plan:9734a33dea2e` | 459 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `right_censored_open:459` | `at_capacity:93,capacity_available:366` | `unknown:459` |
| `paper_plan:ac939ee74e2c` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `mature_terminal:3` | `capacity_available:3` | `unknown:3` |
| `paper_plan:ae8588dfe3b4` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `mature_terminal:3` | `at_capacity:3` | `unknown:3` |
| `paper_plan:b7c8dda9f475` | 12 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `mature_terminal:12` | `capacity_available:12` | `unknown:12` |
| `paper_plan:bffd2fdd7e2b` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `mature_terminal:3` | `capacity_available:3` | `unknown:3` |
| `paper_plan:c8d6065215ab` | 18 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `mature_terminal:18` | `capacity_available:18` | `unknown:18` |
| `paper_plan:cf227f0cc559` | 54 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `right_censored_open:54` | `at_capacity:30,capacity_available:24` | `unknown:54` |
| `paper_plan:d058835e1b0f` | 6 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `right_censored_open:6` | `capacity_available:6` | `unknown:6` |
| `paper_plan:d6075516aea8` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `mature_terminal:3` | `capacity_available:3` | `unknown:3` |
| `paper_plan:d7619461e7f7` | 39 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `right_censored_open:39` | `at_capacity:9,capacity_available:30` | `unknown:39` |
| `paper_plan:e83962372405` | 39 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `right_censored_open:39` | `at_capacity:9,capacity_available:30` | `unknown:39` |
| `paper_plan:ecdc3e95f224` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `mature_terminal:3` | `capacity_available:3` | `unknown:3` |
| `paper_plan:ed61c745d8b8` | 39 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `right_censored_open:39` | `at_capacity:9,capacity_available:30` | `unknown:39` |
| `paper_plan:f5274549c775` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `mature_terminal:3` | `capacity_available:3` | `unknown:3` |
| `paper_plan:fb831c92566e` | 27 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `right_censored_open:27` | `at_capacity:24,capacity_available:3` | `unknown:27` |
| `scan_candidate:03db6f5625c0:BNBUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:03db6f5625c0:ETHUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:03db6f5625c0:EULUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:03db6f5625c0:MMTUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WAIT_PULLBACK:3` |
| `scan_candidate:03db6f5625c0:UNIUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WAIT_PULLBACK:3` |
| `scan_candidate:05233b4f12a0:BNBUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:05233b4f12a0:ENAUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:05233b4f12a0:ETHUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:05233b4f12a0:PEPEUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:05233b4f12a0:SOLUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WAIT_PULLBACK:3` |
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
| `scan_candidate:1480a9add8c9:BTCUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:1480a9add8c9:ETHUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:1480a9add8c9:SOLUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:1480a9add8c9:XRPUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:1480a9add8c9:ZECUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:1be61ae78f1e:DASHUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `WAIT_PULLBACK:3` |
| `scan_candidate:1be61ae78f1e:NEARUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `WATCH_ONLY:3` |
| `scan_candidate:1be61ae78f1e:SUIUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:1be61ae78f1e:TAOUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `WAIT_PULLBACK:3` |
| `scan_candidate:1be61ae78f1e:WLDUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `WATCH_ONLY:3` |
| `scan_candidate:1f452162056b:AVAXUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `WATCH_ONLY:3` |
| `scan_candidate:1f452162056b:LTCUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:1f452162056b:PEPEUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `WAIT_PULLBACK:3` |
| `scan_candidate:1f452162056b:TAOUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `WATCH_ONLY:3` |
| `scan_candidate:1f452162056b:ZECUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `WATCH_ONLY:3` |
| `scan_candidate:23537861af20:ADAUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:23537861af20:BNBUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:23537861af20:DOGEUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:23537861af20:ENAUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:23537861af20:SUIUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `BUY_CANDIDATE:3` |
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
| `scan_candidate:637752924d13:BMTUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `WAIT_PULLBACK:3` |
| `scan_candidate:637752924d13:BTCUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:637752924d13:ETHUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:637752924d13:LINKUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:637752924d13:SOLUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `BUY_CANDIDATE:3` |
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
| `scan_candidate:6d047ae7c4f5:BNBUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:6d047ae7c4f5:BTCUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:6d047ae7c4f5:ETHUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:6d047ae7c4f5:SOLUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:6d047ae7c4f5:ZROUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:6da7db425dbd:BNBUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `WATCH_ONLY:3` |
| `scan_candidate:6da7db425dbd:NEARUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `WATCH_ONLY:3` |
| `scan_candidate:6da7db425dbd:SUIUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:6da7db425dbd:UNIUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `WATCH_ONLY:3` |
| `scan_candidate:6da7db425dbd:ZECUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `WATCH_ONLY:3` |
| `scan_candidate:741093cc2c86:ACEUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:741093cc2c86:BTCUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:741093cc2c86:ETHUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:741093cc2c86:SOLUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:741093cc2c86:ZECUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:75c59fd5991f:AAVEUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:75c59fd5991f:DOGEUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:75c59fd5991f:HBARUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `BUY_CANDIDATE:3` |
| `scan_candidate:75c59fd5991f:UNIUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `WAIT_PULLBACK:3` |
| `scan_candidate:75c59fd5991f:XRPUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `at_capacity:3` | `BUY_CANDIDATE:3` |
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
| `scan_candidate:c6386143eeed:OGNUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:c6386143eeed:ONDOUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:c6386143eeed:QNTUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:c6386143eeed:RLCUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
| `scan_candidate:c6386143eeed:STRKUSDT` | 3 | `atr_reclaim_0_35_shadow,reference_baseline,research_incumbent` | `candidate_only_no_plan_link:3` | `capacity_available:3` | `WATCH_ONLY:3` |
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
| `daily_import_candidate_context` | 450 |
| `decision_level_unknown` | 1089 |

## By Capacity State

| Capacity state | Count |
|---|---:|
| `at_capacity` | 540 |
| `capacity_available` | 999 |

## By Scanner Action

| Scanner action | Count |
|---|---:|
| `BUY_CANDIDATE` | 120 |
| `REJECT` | 30 |
| `WAIT_PULLBACK` | 66 |
| `WATCH_ONLY` | 234 |
| `unknown` | 1089 |

## Terminal Outcomes

| Plan status | Count |
|---|---:|
| `ARCHIVED` | 54 |
| `CLOSED` | 21 |
| `STOPPED` | 156 |

## Interpretation

- Candidate-only rows are useful for confirming that all three lines saw the same scan candidate, but they do not prove trade quality.
- Plan-linked rows can become maturity evidence only after the linked paper plan reaches a terminal status.
- Until mature terminal samples are sufficient, `atr_reclaim_0_35` remains a prospective shadow reference, not a paper deployment rule.
