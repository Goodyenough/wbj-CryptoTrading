---
created: 2026-07-27 23:56:58 CST
tags:
  - crypto
  - trading-system
  - replacement-closure-audit
experiment: replacement_closure_audit
source_run_id: 110c51eef593
replay_run_id: e40da6f04438
verdict: paused_no_stable_executable_edge
---

# replacement_closure_audit

## Plain-language conclusion

Stage 4 remains too concentrated and unstable after de-duplication and robustness checks, so capacity replacement should be frozen until a new pre-declared mechanism exists.

This is a closure appendix for Stage 4 only. It does not introduce a trading rule, does not proceed to Stage 5 shadow replacement, does not raise `max_active_positions`, and does not modify production config.

## Scope

| Field | Value |
|---|---:|
| source_run_id | `110c51eef593` |
| replay_run_id | `e40da6f04438` |
| window | `2025-06-01T00:00:00+00:00` -> `2026-06-01T00:00:00+00:00` |
| stage1_json | `reports\2026-07-27\blocked_entry_event_export_2026-07-27_v1.json` |
| stage4_report | `reports\2026-07-27\blocked_candidate_vs_stale_slot_review_2026-07-27_v1.md` |

## Event Uniqueness

| Metric | Value |
|---|---:|
| total_blocked_events | 512 |
| unique_blocked_timestamps | 293 |
| rank1_blocked_events | 46 |
| unique_rank1_timestamps | 46 |
| eligible_comparison_events | 42 |
| unique_comparison_timestamps | 42 |
| unique_comparison_candidates | 18 |
| unique_stale_trades | 3 |
| stale_trade_top1_share_pct | 83.333 |
| stale_trade_top3_share_pct | 100.000 |

## Stale Trade Concentration

| Stale Trade ID | Comparison Events |
|---|---:|
| `5ef66652c15e` | 35 |
| `1ea8a0eaeb9a` | 6 |
| `580141baa4ca` | 1 |

## Robustness Summaries

| Check | Metric | n | mean | median | positive_pct | min | max |
|---|---|---:|---:|---:|---:|---:|---:|
| first_event_per_stale_trade | `net_replacement_delta_r_24` | 3 | 0.499 | 0.418 | 100.000 | 0.082 | 0.998 |
| first_event_per_stale_trade | `net_replacement_delta_r_42` | 3 | 0.237 | -0.004 | 33.333 | -0.619 | 1.334 |
| first_event_per_stale_trade | `net_replacement_delta_r_60` | 3 | 0.029 | 0.201 | 66.667 | -1.136 | 1.022 |
| exclude_2025_07 | `net_replacement_delta_r_24` | 30 | 0.014 | -0.039 | 43.333 | -1.528 | 1.790 |
| exclude_2025_07 | `net_replacement_delta_r_42` | 30 | -0.054 | -0.311 | 30.000 | -1.595 | 3.439 |
| exclude_2025_07 | `net_replacement_delta_r_60` | 30 | -0.237 | -0.502 | 36.667 | -1.918 | 3.439 |
| exclude_same_bar_ambiguous | `net_replacement_delta_r_24` | 41 | 0.387 | 0.082 | 58.537 | -1.528 | 3.445 |
| exclude_same_bar_ambiguous | `net_replacement_delta_r_42` | 41 | 0.265 | -0.251 | 41.463 | -1.595 | 3.545 |
| exclude_same_bar_ambiguous | `net_replacement_delta_r_60` | 41 | 0.119 | -0.436 | 43.902 | -1.918 | 3.522 |

## Cluster Bootstrap

| Metric | Value |
|---|---:|
| clusters | 3 |
| iterations | 5000 |
| mean | -0.111 |
| p05 | -0.565 |
| p50 | -0.111 |
| p95 | 0.343 |

## Winner Contribution

| Metric | Value |
|---|---:|
| positive_n | 18 |
| top1_positive_contribution_share_pct | 14.657 |
| top3_positive_contribution_share_pct | 43.369 |
| 20pct_trimmed_mean_R_42 | 0.001 |

## Decision

`paused_no_stable_executable_edge`

## Next Action

Freeze the current capacity replacement branch. Resume capacity research only with a new pre-declared slot-selection mechanism or broader walk-forward evidence; otherwise move back to capacity-neutral `atr_reclaim_0_35` entry-quality attribution.

## Raw Summary

```json
{
  "source_run_id": "110c51eef593",
  "replay_run_id": "e40da6f04438",
  "report_date": "2026-07-27",
  "stage1_json_path": "reports\\2026-07-27\\blocked_entry_event_export_2026-07-27_v1.json",
  "stage4_report_path": "reports\\2026-07-27\\blocked_candidate_vs_stale_slot_review_2026-07-27_v1.md",
  "start_utc": "2025-06-01T00:00:00+00:00",
  "end_utc": "2026-06-01T00:00:00+00:00",
  "total_blocked_events": 512,
  "unique_blocked_timestamps": 293,
  "rank1_blocked_events": 46,
  "unique_rank1_timestamps": 46,
  "eligible_comparison_events": 42,
  "unique_comparison_timestamps": 42,
  "unique_comparison_candidates": 18,
  "unique_stale_trades": 3,
  "stale_trade_duplicate_counts": {
    "5ef66652c15e": 35,
    "1ea8a0eaeb9a": 6,
    "580141baa4ca": 1
  },
  "stale_trade_top1_share_pct": 83.33333333333334,
  "stale_trade_top3_share_pct": 100.0,
  "first_event_per_stale_trade_summaries": {
    "net_replacement_delta_r_24": {
      "n": 3,
      "mean": 0.499467403137733,
      "median": 0.41839959329165244,
      "positive_pct": 100.0,
      "min": 0.0816762099337966,
      "max": 0.9983264061877499
    },
    "net_replacement_delta_r_42": {
      "n": 3,
      "mean": 0.23681701655583065,
      "median": -0.004165285543151431,
      "positive_pct": 33.33333333333333,
      "min": -0.6191567234814461,
      "max": 1.3337730586920895
    },
    "net_replacement_delta_r_60": {
      "n": 3,
      "mean": 0.02924629663398533,
      "median": 0.20120715556886792,
      "positive_pct": 66.66666666666666,
      "min": -1.1355001933187798,
      "max": 1.022031927651868
    }
  },
  "exclude_2025_07_summaries": {
    "net_replacement_delta_r_24": {
      "n": 30,
      "mean": 0.014279990553381427,
      "median": -0.03917853753751209,
      "positive_pct": 43.333333333333336,
      "min": -1.5276862855919346,
      "max": 1.790245800263309
    },
    "net_replacement_delta_r_42": {
      "n": 30,
      "mean": -0.05429033444244962,
      "median": -0.310798083899967,
      "positive_pct": 30.0,
      "min": -1.5951655252867416,
      "max": 3.4391995140812277
    },
    "net_replacement_delta_r_60": {
      "n": 30,
      "mean": -0.23721939101880166,
      "median": -0.5019615149648509,
      "positive_pct": 36.666666666666664,
      "min": -1.9183744123409228,
      "max": 3.4391995140812277
    }
  },
  "exclude_same_bar_ambiguous_summaries": {
    "net_replacement_delta_r_24": {
      "n": 41,
      "mean": 0.3868570208276507,
      "median": 0.08239920183310923,
      "positive_pct": 58.536585365853654,
      "min": -1.5276862855919346,
      "max": 3.445081430544437
    },
    "net_replacement_delta_r_42": {
      "n": 41,
      "mean": 0.26542767696708564,
      "median": -0.2505401575676861,
      "positive_pct": 41.46341463414634,
      "min": -1.5951655252867416,
      "max": 3.545436452180673
    },
    "net_replacement_delta_r_60": {
      "n": 41,
      "mean": 0.11921223412839486,
      "median": -0.4363037082560369,
      "positive_pct": 43.90243902439025,
      "min": -1.9183744123409228,
      "max": 3.5219491066913413
    }
  },
  "cluster_bootstrap_mean_r_42": {
    "clusters": 3,
    "iterations": 5000,
    "mean": -0.11125092268712455,
    "p05": -0.5654458762628666,
    "p50": -0.11125092268712455,
    "p95": 0.3429440308886174
  },
  "top_contribution_share_r_42": {
    "positive_n": 18,
    "top1_share_pct": 14.656999406310167,
    "top3_share_pct": 43.36850895737347,
    "trimmed_mean_20pct": 0.0007945929765473087
  },
  "verdict": "paused_no_stable_executable_edge",
  "reason": "Stage 4 remains too concentrated and unstable after de-duplication and robustness checks, so capacity replacement should be frozen until a new pre-declared mechanism exists."
}
```
