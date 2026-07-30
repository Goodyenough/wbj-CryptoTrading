---
created: 2026-07-30 19:27:49 +08:00
tags:
  - crypto
  - trading-system
  - atr-reclaim
  - prospective-shadow
  - runbook
status: active_runbook
---

# atr_reclaim Prospective Shadow Observation Runbook

## Purpose

This runbook defines what to do after normal `daily` or `paper cycle` jobs run while `atr_reclaim_0_35` is in prospective shadow observation.

The goal is to collect clean forward evidence without changing paper trading behavior.

## Current State

```text
reference_baseline:
original_strategy_without_atr_reclaim_0_35

atr_reclaim_0_35_shadow:
original_strategy_plus_atr_reclaim_0_35

research_incumbent:
reference_baseline_plus_atr_reclaim_0_35

paper_deployment:
not authorized

real_money_deployment:
not authorized
```

## Hard Rules

- Do not modify `config/settings.toml`.
- Do not let `atr_reclaim_0_35` control paper entries.
- Do not tune the `0.35` threshold during observation.
- Do not manually run `daily` just to manufacture shadow samples.
- Do not run a new near-window historical `0.35` A/B.
- Do not reopen the abandoned `2023-07-01 -> 2024-07-01` historical repair branch.

## Normal Check After A Daily Or 4h Cycle

Run:

```powershell
python main.py paper shadow-decisions --limit 20
python main.py paper shadow-maturity --no-obsidian
python main.py paper shadow-reconciliation --no-obsidian
python main.py db status
```

Then inspect the generated reports in `reports/YYYY-MM-DD/`.

## Decision Tree

### Case 1: No Shadow Rows Yet

Signal:

```text
paper_shadow_decisions = []
maturity verdict = no_shadow_samples_yet
reconciliation verdict = no_shadow_samples_yet
```

Action:

```text
continue_waiting
```

Do not change strategy, do not deploy `0.35`, and do not force sample creation.

### Case 2: Candidate Rows Exist, No Plan-Linked Rows

Signal:

```text
maturity verdict = candidate_context_only
```

Meaning:

The same scan candidates are being observed by the three lines, but there is no entry-zone decision outcome yet.

Action:

```text
continue_waiting_for_plan_linked_decisions
```

### Case 3: Plan-Linked Rows Exist, Not Mature

Signal:

```text
maturity verdict = decision_samples_not_mature
right_censored_open rows > 0
mature terminal rows = 0
```

Action:

```text
continue_waiting_for_terminal_outcomes
```

Do not infer signal quality from open/right-censored rows.

### Case 4: Reconciliation Is Structurally Incomplete

Signal:

```text
reconciliation verdict = reconciliation_incomplete_missing_lines
```

Action:

```text
pause_attribution_and_debug_logging
```

Check whether every opportunity has all required lines:

```text
reference_baseline
atr_reclaim_0_35_shadow
research_incumbent
```

### Case 5: Shadow Accidentally Controls Paper

Signal:

```text
controls_paper rows > 0
reconciliation verdict = reconciliation_failed_controls_paper
```

Action:

```text
stop_and_debug_immediately
```

This violates the current research boundary.

### Case 6: Structurally Clean But Too Small

Signal:

```text
reconciliation verdict = reconciliation_waiting_for_sample_threshold
```

Default pre-attribution gate:

```text
complete opportunities >= 10
mature terminal opportunities >= 5
independent symbols >= 3
controls_paper rows = 0
incomplete opportunities = 0
```

Action:

```text
continue_collecting_samples
```

Do not start direct filtering or path/capacity attribution yet.

### Case 7: Ready For Attribution

Signal:

```text
reconciliation verdict = reconciliation_ready_for_attribution
```

Action:

```text
start_read_only_attribution_review
```

Allowed next analysis:

- direct filtering contribution;
- missed winners vs avoided losers;
- capacity/path contribution;
- symbol/month concentration;
- right-censoring and sample maturity.

Still not allowed:

- deploy `atr_reclaim_0_35`;
- modify `settings.toml`;
- tune the reclaim threshold;
- start a new combined challenger without an approved single-variable card.

## Minimum Deployment Boundary

Passing the pre-attribution gate is not deployment approval.

Before any paper deployment decision, the project still needs:

- attribution review showing direct filtering is not clearly negative;
- path/capacity benefit not dominated by a tiny cluster;
- no material drawdown or tail-risk deterioration;
- enough mature forward samples;
- explicit user approval.

## Current Next Action

As of this runbook:

```text
paper_shadow_decisions = []
current action = wait_for_normal_daily_or_entry_zone_4h_trigger
```
