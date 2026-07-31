---
created: 2026-07-31 11:42:23 +08:00
tags:
  - crypto
  - trading-system
  - atr-reclaim
  - execution-plan
status: active_plan_update
decision: accept_atr_reclaim_0_35_as_provisional_research_incumbent
paper_deployment: not_authorized
real_money_deployment: not_authorized
---

# atr_reclaim Execution Plan Update

## 1. Current Background

The project has finished the historical `atr_reclaim_0_35` review branch and moved to a prospective shadow observation framework.

The historical evidence is directionally promising: `atr_reclaim_0_35` improved portfolio-level net return, Profit Factor, Sharpe, and drawdown in reviewed windows. However, the mechanism is not clean enough for deployment. Same-key direct filtering did not clearly explain the improvement, and the benefit appears to be materially path-dependent through capacity release and variant-only trades.

The current project goal is therefore not to prove `0.35` through another historical window. The goal is to keep research moving while preserving a clean comparison structure that can later confirm or disprove whether `0.35` still adds forward value.

## 2. Current Difficulties

The main difficulty is evidence quality.

- The `2023-07-01 -> 2024-07-01` validation route is abandoned because the historical universe has a material gap and cannot provide clean validation without a larger historical-master reconstruction project.
- Recent historical windows have already been inspected during threshold sensitivity, A/B, attribution, and path reviews, so they are not clean independent validation windows.
- The `0.35` improvement may come from capacity/path effects rather than a stable direct entry-quality edge.
- Forward shadow evidence has started at candidate level, but there are no plan-linked or mature terminal samples yet.

As of `2026-07-31 11:42 +08:00`, automatic tasks are healthy:

- `CryptoTrading_DailyPaperUpdate`: last run `2026-07-30 20:05:01`, result `0`.
- `CryptoTrading_4H_PaperUpdate`: last run `2026-07-31 08:10:01`, result `0`; next run `2026-07-31 12:10:00`.
- latest database run: `20260731_001002_b39e3bc4`, `paper_4h_update`, status `success`.
- `paper_shadow_decisions`: 15 rows from the 2026-07-30 daily import, covering 5 scan candidates across `reference_baseline`, `atr_reclaim_0_35_shadow`, and `research_incumbent`.
- current maturity status: candidate context only; no plan-linked decision rows and no mature terminal outcomes.

## 3. Decisions

The formal decision is:

```text
accept_atr_reclaim_0_35_as_provisional_research_incumbent
```

Meaning:

- use `0.35` as the default research incumbent for future challenger studies;
- do not treat `0.35` as strictly validated;
- do not let `0.35` control paper orders without explicit user approval;
- do not authorize real-money deployment;
- freeze reclaim threshold tuning;
- do not run another near-window historical `0.35` A/B;
- do not repair the abandoned 2023-2024 historical validation branch for this project line.

The abandoned 2023-2024 artifacts remain diagnostic evidence only. They must not be used to keep, reject, or deploy `0.35`.

## 4. Required Comparison Lines

The plan must preserve these lines:

| Line | Definition | Purpose | Controls paper? |
|---|---|---|---|
| `reference_baseline` | Original strategy without `atr_reclaim_0_35` | Long-term reference for what the old system would have done | Existing paper behavior only |
| `atr_reclaim_0_35_shadow` | Original strategy plus `atr_reclaim_0_35` | Independent challenger-like line for checking `0.35` itself | No |
| `research_incumbent` | `reference_baseline + atr_reclaim_0_35` | Current default research benchmark | No, unless explicitly approved |
| `new_challenger` | `research_incumbent + one new factor` | Tests incremental value beyond `0.35` | No, unless explicitly approved |

Important clarification:

`atr_reclaim_0_35_shadow` remains an independent challenger-like comparison line even though `0.35` is also the research incumbent. This prevents future challenger results from hiding whether value came from `0.35`, from the new factor, or from path noise.

## 5. Next Plan

### Stage 1 - Continue Prospective Shadow Observation

Problem solved: historical evidence is contaminated or already observed.

Actions:

- wait for normal daily/import or entry-zone 4h updates to create more `paper_shadow_decisions`;
- do not manually manufacture samples;
- after normal runs, check `paper shadow-decisions`, `paper shadow-maturity`, `paper shadow-reconciliation`, and `db status`;
- require all three lines on the same opportunity before interpreting evidence.

Current status: candidate-level logging works, but attribution cannot start.

### Stage 2 - Verify Shadow Data Cleanliness

Problem solved: avoid interpreting malformed logs as strategy evidence.

Actions:

- confirm required lines are present;
- confirm `controls_paper=0` for shadow lines;
- separate candidate-only rows from plan-linked rows;
- reconcile opportunity IDs, active positions, capacity state, and terminal outcomes.

If reconciliation fails, fix logging before interpreting performance.

### Stage 3 - Wait For The Pre-Attribution Gate

Problem solved: avoid drawing conclusions from one or two early samples.

Minimum gate:

```text
complete opportunities >= 10
mature terminal opportunities >= 5
independent symbols >= 3
controls_paper rows = 0
incomplete opportunities = 0
```

Passing this gate only allows read-only attribution. It does not authorize paper or production deployment.

### Stage 4 - Attribute Forward `0.35` Value

Problem solved: distinguish direct filtering from capacity/path value.

Actions after the gate:

- compare `atr_reclaim_0_35_shadow vs reference_baseline`;
- separate avoided losers from missed winners;
- measure capacity release and follow-on trades;
- check concentration by symbol, month, and symbol-month;
- report right-censored ratio and sample maturity.

Possible conclusions:

```text
continue_as_research_incumbent
retest_more_forward_samples_needed
deprioritize_or_remove_from_incumbent
```

### Stage 5 - Start One New Challenger At A Time

Problem solved: continue system improvement without endless reclaim-threshold tuning.

Priority order:

1. Full-capacity candidate ranking and opportunity cost.
2. Capacity utilization and `max_active_positions` review.
3. `TIME_EXIT` and stale-slot exit behavior.
4. Execution quality, slippage, and state consistency.
5. Market-regime labels.
6. New entry filters only after the above are better understood.

Each new formal challenger must answer one question and compare mainly against `research_incumbent`, while `reference_baseline` and `atr_reclaim_0_35_shadow` continue as calibration lines.

## 6. Immediate Next Action

Do not change configuration now.

The next operational check should happen after the normal `2026-07-31 12:10 +08:00` 4h task, using:

```powershell
python main.py paper shadow-decisions --limit 30
python main.py paper shadow-maturity --no-obsidian
python main.py paper shadow-reconciliation --no-obsidian
python main.py db status
```

If the system still has only candidate-level rows, continue waiting. If plan-linked rows appear, inspect reconciliation first. If mature terminal opportunities are still below the gate, do not run attribution.

## 7. Plain-Language Summary

The project is keeping `0.35` as the best current research starting point, but it is not deployed. The old 2023-2024 validation route is closed because the data foundation is not clean enough. The clean path now is to keep observing forward shadow decisions, preserve the original strategy as a reference, preserve `0.35` as an independent shadow line, and only start attribution after enough real prospective samples mature.
