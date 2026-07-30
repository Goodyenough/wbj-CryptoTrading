---
created: 2026-07-30 12:26:00 +08:00
tags:
  - crypto
  - trading-system
  - atr-reclaim
  - prospective-shadow
experiment: atr_reclaim_prospective_shadow_observation_plan
status: schema_plan_not_enabled
---

# atr_reclaim Prospective Shadow Observation Plan

## Purpose

Collect clean future evidence for `atr_reclaim_0_35` without changing live or paper trading behavior.

This is the primary clean confirmation path because it records the actual point-in-time universe, signals, capacity state, and outcomes.

## Rules

- Do not modify `config/settings.toml`.
- Do not let `atr_reclaim_0_35` control live or paper entries.
- Do not tune the `0.35` threshold during observation.
- Record baseline and variant decisions at the same decision time.
- Preserve point-in-time universe and capacity state.
- Evaluate only after the predeclared sample or time gate.

## Observation Row Schema

```text
observation_id
decision_time_utc
symbol
source_signal_id
baseline_accept
variant_accept
variant_reject_reason
reclaim_margin_atr
entry_high
entry_close
atr_4h
market_regime
current_universe_hash
active_positions_at_decision
capacity_available
baseline_eventual_outcome
variant_direct_filter_outcome
baseline_r
mfe_r
mae_r
first_hit
right_censored
variant_path_replacement_trade_id
variant_path_replacement_r
notes
```

## Evidence Layers

### Signal Layer

Answers whether the filter itself improves decision quality:

- filtered loser;
- missed winner;
- kept winner;
- kept loser;
- right-censored / unknown.

### Portfolio Path Layer

Answers whether released capacity creates better or worse later trades:

- baseline-only occupied slot;
- variant-released slot;
- replacement trade id;
- replacement R;
- capacity state at decision;
- path contribution by symbol and month.

## Minimum Review Gates

### Interim Review

- at least 50 mature opportunities;
- right-censored ratio low enough to interpret;
- no threshold changes;
- report signal layer and path layer separately.

### Deployment Review

- preferably at least 100 mature opportunities;
- direct filtering is not clearly negative;
- path contribution is explainable and not dominated by a tiny cluster;
- risk metrics do not materially worsen;
- user explicitly approves any production config change.

## Status

This is a schema and research plan only. No shadow logger is enabled by this document.

Implementation should be a separate step after confirming where to store observations and how to link them to existing paper-trading runs.
