---
created: 2026-07-30 14:45:00 +08:00
tags:
  - crypto
  - trading-system
  - atr-reclaim
  - research-plan
status: approved_plan
decision: accept_atr_reclaim_0_35_as_provisional_research_incumbent
---

# atr_reclaim Incumbent + Challenger Plan

## 1. Current Background

The project has been testing entry-quality improvements around reclaim behavior. The current strategy already includes symbol selection, entry confirmation, exits, position sizing, and capacity constraints.

`atr_reclaim_0_35` means a buy entry is only allowed after the 4h close reclaims the entry level by at least `0.35 * ATR`.

Historical portfolio results are promising:

| Window | Reference baseline net | `0.35` net | Change | Notes |
|---|---:|---:|---:|---|
| `2024-07-01 -> 2025-06-01` | `-2.09%` | `18.20%` | `+20.29 pp` | PF and MDD also improved. |
| `2025-06-01 -> 2026-06-01` | `3.11%` | `9.33%` | `+6.21 pp` | PF, Sharpe, and MDD improved. |
| `2023-07-01 -> 2024-07-01` | `22.10%` | `31.55%` | `+9.46 pp` | Diagnostic only because historical universe is not validation-clean. |

So `0.35` is currently one of the strongest observed candidates.

## 2. Current Difficulties

The difficulty is not that `0.35` performed badly. The difficulty is that its mechanism is not fully established.

Known issues:

- Recent historical windows have been repeatedly observed, so they cannot provide strong independent validation.
- The `2023-2024` window has historical universe gaps and is diagnostic only.
- Trade-level attribution showed that direct filtering was not clearly positive.
- Improvement appears plausibly driven by capacity release, delayed entry paths, and variant-only winners.
- If `0.35` is treated as fully validated, later research may confuse path effects with a stable entry-quality edge.
- If `0.35` is ignored entirely, the project may waste time proving an already useful candidate instead of moving to larger system bottlenecks.

## 3. Decision

Adopt the following formal status:

```text
decision:
accept_atr_reclaim_0_35_as_provisional_research_incumbent

reference_baseline:
original_strategy_without_atr_reclaim_0_35

atr_reclaim_0_35_shadow:
original_strategy_plus_atr_reclaim_0_35
tracked independently for forward comparison

research_incumbent:
reference_baseline_plus_atr_reclaim_0_35

paper_deployment:
pending_shadow_or_explicit_user_approval

real_money_deployment:
not_authorized

parameter_tuning:
frozen

historical_validation_status:
promising_but_not_independently_validated

mechanism_status:
direct_filter_advantage_unconfirmed
capacity_path_advantage_plausible_but_unconfirmed
```

This means `0.35` becomes the default research reference for new challenger studies, but it does not automatically control paper trades.

## 4. Lines To Preserve

The project must preserve three separate lines:

| Line | Definition | Purpose | Controls paper? |
|---|---|---|---|
| Reference baseline | Original strategy without `0.35` | Long-term calibration and attribution | No change |
| `atr_reclaim_0_35_shadow` | Original strategy + `0.35` | Keep measuring `0.35` itself against the original baseline | No, unless separately approved |
| New challenger | Research incumbent + one new factor | Test incremental value beyond `0.35` | No, unless separately approved |

The `0.35` line must remain independently visible. Do not collapse it into the only baseline, because future results must still answer whether `0.35` itself continues to add value.

## 5. Comparison Framework

### Daily Research Comparison

```text
new challenger vs research incumbent
```

Question answered:

Does the new factor add value after accepting `0.35` as the current research incumbent?

### Long-Term Calibration

```text
atr_reclaim_0_35_shadow vs reference baseline
```

Question answered:

Does `0.35` continue to justify its incumbent status in forward data?

### Full-System Sanity Check

```text
new challenger vs reference baseline
```

Question answered:

Is the full researched stack better than the original strategy, or only better than a narrow intermediate baseline?

## 6. Next Research Priorities

### Priority 1: Full-Capacity Candidate Ranking And Opportunity Cost

Problem:

The best historical evidence for `0.35` may come from path and capacity changes. That means the system may be leaving value on the table when positions are full.

Question:

When the system is at capacity, can candidate ranking identify better opportunities than the positions currently occupying slots?

Output:

- event-level blocked-candidate dataset;
- rank quality review;
- stale-slot opportunity cost review;
- one predefined challenger at most.

### Priority 2: Capacity Utilization / `max_active_positions`

Problem:

Raising capacity can increase opportunity capture, but may also dilute quality and increase drawdown.

Question:

Does a capacity change improve risk-adjusted return after `0.35` is the research incumbent?

Constraint:

Do not change production or paper capacity without explicit approval.

### Priority 3: `TIME_EXIT` And Exit Rules

Problem:

Long pre-TP1 holds can consume capacity and block later candidates.

Question:

Can exit logic reduce stale capacity usage without cutting off eventual winners?

Output:

- forward continuation after `TIME_EXIT`;
- stale-slot outcome distribution;
- direct comparison against research incumbent.

### Priority 4: Execution Quality / Slippage / State Consistency

Problem:

If backtest, paper, and shadow decisions diverge materially, strategy optimization may target behavior that cannot be executed.

Question:

Do paper/shadow signals match the theoretical decision state closely enough to trust subsequent challenger tests?

Output:

- decision-state reconciliation;
- slippage and fill assumption review;
- missed/extra signal audit.

### Priority 5: Market Regime Adaptation

Problem:

The same entry rule may behave differently in trend, chop, crash, and high-volatility regimes.

Question:

Can market-state labels explain when the incumbent works or fails?

Constraint:

Start as labels only. Do not convert every label into a hard filter.

### Priority 6: New Entry Filters

Problem:

Additional entry filters can easily overfit and reduce opportunity count.

Question:

After ranking, capacity, exits, and execution are better understood, does any new entry factor add stable value beyond `0.35`?

Constraint:

Only one new entry challenger at a time.

## 7. Operating Rules

- Stop tuning reclaim threshold values for now.
- Keep `entry_reclaim_min_atr=0.35` frozen for research incumbent studies.
- Do not deploy `0.35` to paper without explicit user approval.
- Do not authorize real-money deployment.
- Maintain reference baseline forward logs.
- Maintain independent `atr_reclaim_0_35_shadow` forward logs.
- Run at most `1-2` formal challengers at the same time.
- Separate facts, observations, hypotheses, and decisions in every follow-up experiment.
- A challenger can only be promoted after predefined evidence gates are met.

## 8. Evidence Gates

### Supports A Challenger

- Improves net return and profit factor versus research incumbent.
- Does not materially worsen max drawdown or tail loss.
- Improvement is not dominated by one symbol, one month, or one path event.
- Sample is sufficient and right-censoring is acceptable.
- Mechanism matches the stated hypothesis.

### Rejects A Challenger

- Net/PF/Sharpe deteriorate versus research incumbent.
- Drawdown or tail loss materially worsens.
- Benefit comes only from a small number of isolated path trades.
- It breaks execution consistency or reduces trade count too aggressively.

### Insufficient Evidence

- Sample is too small.
- Outcome maturity is too low.
- Right-censored ratio is too high.
- Results are directionally mixed across windows or regimes.
- Data quality or universe alignment is unresolved.

## 9. Immediate Next Step

Create the prospective shadow observation MVP for:

```text
reference baseline
atr_reclaim_0_35_shadow
at most one new challenger after explicit approval
```

The MVP should log:

- decision timestamp;
- symbol;
- reference baseline decision;
- `atr_reclaim_0_35_shadow` decision;
- research incumbent decision;
- challenger decision, if active;
- reclaim margin in ATR;
- capacity state;
- active positions;
- reject reason;
- decision-time signal snapshot;
- later matured outcome;
- direct-filter contribution;
- path/capacity contribution.

## 10. Plain-Language Summary

We accept `0.35` as the best current research version, but not as a fully proven rule and not as an automatically deployed paper strategy.

The original strategy remains the reference baseline. `0.35` remains an independent shadow line. New ideas must beat the `0.35` incumbent, while the system continues checking whether `0.35` itself still beats the original strategy in forward data.
