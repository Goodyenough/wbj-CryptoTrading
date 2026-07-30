---
created: 2026-07-30 14:08:40 +08:00
tags:
  - crypto
  - trading-system
  - atr-reclaim
  - window-eligibility
experiment: atr_reclaim_recent_window_eligibility_audit
status: completed_no_ab_run
verdict: no_clean_recent_window_available_for_strong_historical_validation
---

# atr_reclaim Recent-Window Eligibility Audit

## System Goal

Validate whether `atr_reclaim_0_35` has a real, repeatable entry-quality edge before any deployment or production configuration change.

## Single Question

Is there a recent historical window that is clean enough to use for a pre-registered one-time `atr_reclaim_0_35` A/B validation?

## Roadmap Fit

This audit follows the formal decision to abandon `2023-07-01 -> 2024-07-01` as validation evidence because its historical universe has a material missing-symbol gap.

The purpose is not to continue validating `0.35` immediately. The purpose is to decide whether a cleaner historical validation site exists, or whether the main evidence path should move to prospective shadow observation.

## Evidence Boundaries

This audit did not run a new A/B test and did not inspect any new `atr_reclaim_0_35` performance result.

It only reviewed existing project artifacts, ledgers, reports, and prior window usage.

## Facts

- `2023-07-01 -> 2024-07-01` was abandoned for `atr_reclaim_0_35` validation after N2-N4 found a material historical universe gap.
- N3 found `127` standard-like historical gaps, equal to `32.32%` of the historical standard universe.
- `atr_reclaim_0_35_status` is `experimental_candidate_unvalidated`.
- `2024-07-01 -> 2025-06-01` and `2025-06-01 -> 2026-06-01` were already used in ATR reclaim threshold sensitivity, formal A/B, trade attribution, path replay, and capacity/opportunity reviews.
- `2026-06-19 -> 2026-07-02`, `2026-07-03 -> 2026-07-25`, and `2026-07-17 -> 2026-07-25` were already used in paper/shadow audits and fixed opportunity shadow experiments.

## Observations

- The two main recent historical windows are likely better from a data-availability perspective than 2023-2024, but they are not clean validation windows because the ATR reclaim family has already been repeatedly inspected there.
- The June-July 2026 paper windows are closer to prospective data, but they are short, partially right-censored in earlier cuts, and already used for entry-quality shadow experiments.
- Using any of these observed windows as the next decisive validation would create window-selection and result-contamination risk.

## Hypothesis

If a clean recent historical validation window exists, it should be date-locked before A/B, should not have been used to select or favor `0.35`, and should pass an N0-style data/universe audit before any performance result is viewed.

## Candidate Window Gate

| Candidate window | Prior observation risk | Data/universe risk | Gate result | Evidence grade | Reason |
|---|---:|---:|---|---|---|
| `2024-07-01 -> 2025-06-01` | high | moderate | fail | auxiliary/context only | Window already appears in ATR reclaim threshold sensitivity and `atr_reclaim_0_35` A/B artifacts. |
| `2025-06-01 -> 2026-06-01` | high | low/moderate | fail | auxiliary/context only | Window already appears in ATR reclaim threshold sensitivity, attribution, path replay, and capacity review artifacts. |
| `2024-07-01 -> 2026-06-01` | high | moderate | fail | auxiliary/context only | Composite of already observed subwindows; not independent. |
| `2026-06-19 -> 2026-07-02` | high | high | fail | diagnostic only | Already used in paper opportunity audit and shadow replay; short and not a full mature validation window. |
| `2026-07-03 -> 2026-07-25` | high | medium/high | fail | diagnostic only | Already used for entry-quality fixed opportunity shadow experiments; not independent for `0.35`. |
| `2026-07-17 -> 2026-07-25` | high | high | fail | interim direction only | Already observed and too short; prior review noted high right-censor risk. |
| Future pre-locked window | low if registered before start | lowest if logged live | pass for setup | prospective confirmation | Cleanest route if baseline/variant decisions are logged before outcome maturity. |

## Decision

`no_clean_recent_window_available_for_strong_historical_validation`

Current recent historical windows should not be used as decisive validation evidence for `atr_reclaim_0_35`.

## Consequences

- Do not run another near-window historical A/B for `atr_reclaim_0_35` now.
- Do not deploy `atr_reclaim_0_35`.
- Do not change `config/settings.toml`.
- Keep existing 2024-2026 reports as auxiliary diagnostic context only.
- Move the main validation path to prospective shadow observation.

## Next Action

Design and implement a prospective shadow observation schema for `atr_reclaim_0_35`.

The shadow log should record, at decision time:

- baseline decision;
- `atr_reclaim_0_35` variant decision;
- raw signal and reclaim margin;
- capacity state;
- whether a trade was directly filtered;
- whether a path/capacity change created a later variant-only or baseline-only opportunity;
- enough candle/outcome data to mature the observation after a pre-declared holding horizon.

## Approval Criteria For Any Future Historical A/B

A future historical A/B may only be considered if all of the following are true before performance inspection:

- window dates are locked in advance;
- the window was not used to select `0.35`;
- no prior `atr_reclaim_0_35` result in that window has been inspected;
- N0-style universe and kline completeness audit passes;
- baseline and variant use the same universe, data, fees, slippage, code commit, capacity, and metrics;
- the result is reported once regardless of direction.

No currently reviewed recent window satisfies these conditions.
