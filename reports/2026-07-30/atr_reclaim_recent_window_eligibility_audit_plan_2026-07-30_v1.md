---
created: 2026-07-30 12:26:00 +08:00
tags:
  - crypto
  - trading-system
  - atr-reclaim
  - window-eligibility
experiment: atr_reclaim_recent_window_eligibility_audit_plan
status: pre_ab_no_results_inspected
---

# atr_reclaim Recent-Window Eligibility Audit Plan

## Purpose

Determine whether a cleaner recent historical window exists for one-time auxiliary `atr_reclaim_0_35` A/B evidence.

This is not an A/B run. This plan only audits candidate window eligibility before any new result inspection.

## Current Constraint

Many common recent windows have already been observed in prior A/B or walk-forward work, especially:

- `2024-07-01 -> 2025-06-01`
- `2025-06-01 -> 2026-06-01`
- `2024-07-01 -> 2026-06-01`
- smaller subwindows used by paper/shadow reviews around `2026-06-19 -> 2026-07-25`

These windows may be useful as context, but they should not automatically be treated as strong validation windows for `atr_reclaim_0_35`.

## Eligibility Checklist

| Check | Requirement | Pass/Fail |
|---|---|---|
| not_used_for_threshold_selection | Window was not used to choose `0.35` | pending |
| not_repeatedly_observed | `atr_reclaim_0_35` result in this window has not been repeatedly inspected | pending |
| dates_pre_locked | Start and end dates can be locked before A/B | pending |
| universe_clean | Point-in-time universe can be generated with small documented limitations | pending |
| kline_complete | Practical candidate symbols have complete 1h/4h/1d data | pending |
| rename_delist_clean | No major unresolved rename/migration/delisting issue affects likely selected symbols | pending |
| same_universe | Baseline and variant can use identical universe and data | pending |
| config_frozen | Settings, code, capacity, fees, slippage, and metrics are frozen | pending |
| one_time_result | Result will be reported once regardless of direction | pending |

## Candidate Window Triage

| Candidate Window | Prior Observation Risk | Data Completeness Risk | Current Evidence Grade | Next Action |
|---|---|---|---|---|
| `2024-07-01 -> 2025-06-01` | high | likely lower than current but must audit | auxiliary only unless proven unobserved | likely reject as strong validation |
| `2025-06-01 -> 2026-06-01` | high | likely better | auxiliary only unless proven unobserved | likely reject as strong validation |
| `2026-06-01 -> 2026-07-30` | medium/high due paper review overlap | high right-censor risk | prospective / interim only | do not use as completed A/B window yet |
| future locked window | none if registered before start | cleanest | prospective confirmation | prefer for final confirmation |

## Gate Outcomes

### `eligible_for_pre_registered_auxiliary_ab`

Use only if a candidate window passes all eligibility checks and no prior result contamination is found.

### `auxiliary_only_not_validation`

Use if the window is data-clean but has prior observation or threshold-selection contamination.

### `no_clean_recent_window_available`

Use if all recent windows are either already observed, too short, right-censored, or data-contaminated.

## Decision Rule

Do not run a new historical A/B unless the chosen window is locked and classified before inspecting new `atr_reclaim_0_35` results.

If no eligible recent window exists, skip historical A/B and make prospective shadow observation the main confirmation path.
