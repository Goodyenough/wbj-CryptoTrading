# Paper Shadow Decision-State Reconciliation v1

## Scope

- This report is read-only and does not change `config/settings.toml`, paper plans, events, snapshots, or strategy defaults.
- Required lines: `reference_baseline`, `atr_reclaim_0_35_shadow`, `research_incumbent`.
- The goal is state reconciliation, not strategy validation.

## Verdict

- verdict: `no_shadow_samples_yet`
- reason: paper_shadow_decisions is empty, so no three-line reconciliation can be performed.

## Summary

| Metric | Value |
|---|---:|
| decisions | 0 |
| opportunities | 0 |
| complete opportunities | 0 |
| incomplete opportunities | 0 |
| controls_paper rows | 0 |
| mismatch opportunities | 0 |
| mature terminal opportunities | 0 |
| right-censored opportunities | 0 |

## Run Context

- latest_daily_run: `20260729_120502_400dc662` status=`success`
- latest_4h_run: `20260730_104051_53df384d` status=`success`
- open_plan_count: 1
- watching_plan_count: 1

### Open Plans

| Plan | Symbol | Status | Entry low | Entry high | Updated |
|---|---|---|---:|---:|---|
| `9734a33dea2e` | `ONDOUSDT` | `WATCHING` | 0.394505 | 0.41156785714285715 | 2026-07-30T10:40:51Z |

## By Line

| Line | Count |
|---|---:|
| none | 0 |

## By Stage

| Stage | Count |
|---|---:|
| none | 0 |

## By Decision

| Decision | Count |
|---|---:|
| none | 0 |

## By Opportunity

| Opportunity | Rows | Lines | Missing lines | Decisions | Accepted | Maturity | Plan status |
|---|---:|---|---|---|---|---|---|
| none | 0 |  |  |  |  |  |  |

## Interpretation

- Empty shadow decisions mean the system is still waiting for prospective samples.
- Missing required lines block attribution because baseline, `0.35`, and incumbent would not share the same observation point.
- Mature terminal opportunities are required before direct filtering or path/capacity contribution can be interpreted.
- Any `controls_paper=1` row is a failure for this shadow phase unless explicitly approved later.
