---
created: 2026-07-30 19:32:00 +08:00
tags:
  - crypto
  - trading-system
  - atr-reclaim
  - execution-plan
status: approved_plan
decision: accept_atr_reclaim_0_35_as_provisional_research_incumbent
paper_deployment: not_authorized
real_money_deployment: not_authorized
---

# atr_reclaim Global Execution Plan

## 1. Background

The project has been testing whether an ATR-based reclaim requirement can improve entry quality. The strongest observed reclaim threshold is `atr_reclaim_0_35`: a buy entry is allowed only when the 4h close reclaims the entry level by at least `0.35 * ATR`.

Historical portfolio results are promising. In the already reviewed windows, `0.35` improved net return, Profit Factor, Sharpe, and drawdown in several portfolio-level comparisons. However, the trade-level mechanism was not clean: same-key direct filtering did not clearly add value, and part of the improvement appears to come from path changes, capacity release, and variant-only winners.

Therefore the project is no longer treating `0.35` as a rule that must be proven from scratch before any other research can continue. It is also not treating it as a fully validated deployable rule.

## 2. Current Difficulties

The main difficulty is evidence quality, not performance direction.

Known constraints:

- The `2023-07-01 -> 2024-07-01` window has a material historical universe gap, including 127 standard-like missing symbols. It is abandoned as validation evidence.
- Recent historical windows have already been inspected during threshold sensitivity, A/B, attribution, and path reviews, so they cannot serve as clean independent confirmation.
- The direct filtering mechanism for `0.35` is still unconfirmed.
- The portfolio improvement may depend on capacity path effects rather than a stable entry-quality edge.
- `paper_shadow_decisions` currently has no forward samples, so prospective evidence has not started producing conclusions.

The practical issue is that continuing to repair old historical windows would consume a lot of effort and may still leave residual survivor-bias and point-in-time universe uncertainty. That would pull the project away from the main goal: improving the trading system in a controlled, explainable way.

## 3. Formal Decisions

```text
decision:
accept_atr_reclaim_0_35_as_provisional_research_incumbent

meaning:
- use 0.35 as the default research incumbent for future challenger studies;
- do not treat 0.35 as strictly validated;
- do not let 0.35 control paper orders unless explicitly approved;
- do not authorize real-money deployment;
- freeze reclaim threshold tuning;
- stop 2023-2024 historical universe repair for this validation branch.
```

The abandoned 2023-2024 work remains useful as diagnostic evidence. It shows that current-master historical backtests can have universe bias and that portfolio-level improvements can hide mechanism-level weakness. It must not be used to keep, reject, or deploy `0.35`.

## 4. Required Comparison Lines

The plan must preserve three separate lines:

| Line | Definition | Main question | Controls paper? |
|---|---|---|---|
| `reference_baseline` | original strategy without `atr_reclaim_0_35` | What would the original system have done? | Existing paper behavior only |
| `atr_reclaim_0_35_shadow` | original strategy plus `atr_reclaim_0_35` | Does `0.35` itself continue to add forward value? | No |
| `research_incumbent` | reference baseline plus `atr_reclaim_0_35` | What is the current default research benchmark? | No, unless explicitly approved |
| `new_challenger` | research incumbent plus one new factor | Does the new factor add incremental value beyond `0.35`? | No, unless explicitly approved |

Important clarification:

`atr_reclaim_0_35_shadow` must remain an independent challenger-like line against the original baseline. Even though `0.35` is the research incumbent, the project still needs a visible forward comparison:

```text
atr_reclaim_0_35_shadow vs reference_baseline
```

Without this line, later results could not tell whether gains came from `0.35`, from a later challenger, or from path noise.

## 5. Evidence Framework

### Daily Research Comparison

```text
new_challenger vs research_incumbent
```

Purpose: test whether a new factor adds incremental value after accepting `0.35` as the current research baseline.

### Long-Term Calibration

```text
atr_reclaim_0_35_shadow vs reference_baseline
```

Purpose: keep checking whether `0.35` still deserves incumbent status in forward data.

### Full-System Check

```text
new_challenger vs reference_baseline
```

Purpose: confirm whether the full researched stack beats the original system, not just an intermediate benchmark.

## 6. Next Execution Stages

### Stage 1 - Keep Prospective Shadow Observation Running

Problem solved: historical evidence is contaminated or already observed.

Action:

- wait for normal daily/import or entry-zone 4h updates to create `paper_shadow_decisions`;
- do not manually manufacture samples;
- check `paper_shadow_maturity` and `paper_shadow_reconciliation` after normal runs;
- require all three lines on the same opportunity: `reference_baseline`, `atr_reclaim_0_35_shadow`, and `research_incumbent`.

Minimum gate before attribution:

```text
complete opportunities >= 10
mature terminal opportunities >= 5
independent symbols >= 3
controls_paper rows = 0
incomplete opportunities = 0
```

Passing this gate only allows read-only attribution. It does not authorize deployment.

### Stage 2 - Confirm Shadow Data Cleanliness

Problem solved: avoid interpreting bad shadow logs as strategy evidence.

Action:

- verify no required line is missing;
- verify `atr_reclaim_0_35_shadow` never has `controls_paper=1`;
- verify opportunity IDs, capacity state, active positions, and terminal outcomes can be reconciled;
- separate candidate-only rows from plan-linked decision rows.

Decision:

- if reconciliation fails, fix logging before interpreting performance;
- if reconciliation passes but sample is immature, continue waiting;
- if reconciliation passes and sample gate is met, start attribution.

### Stage 3 - Attribute `0.35` Forward Value

Problem solved: distinguish direct filtering value from capacity/path value.

Action:

- compare `atr_reclaim_0_35_shadow vs reference_baseline`;
- split direct filtered opportunities into avoided losers and missed winners;
- measure capacity release and follow-on trades;
- check concentration by symbol, month, and symbol-month;
- report right-censored ratio and sample maturity.

Possible conclusions:

```text
continue_as_research_incumbent
retest_more_forward_samples_needed
deprioritize_or_remove_from_incumbent
```

No conclusion here automatically changes paper or production configuration.

### Stage 4 - Start One New Challenger At A Time

Problem solved: continue system improvement without endlessly retuning reclaim thresholds.

Priority order:

1. Full-capacity candidate ranking and opportunity cost.
2. Capacity utilization and `max_active_positions` review.
3. `TIME_EXIT` and stale-slot exit behavior.
4. Execution quality, slippage, and state consistency.
5. Market-regime labels.
6. New entry filters only after the above are better understood.

Rule:

Only one formal new challenger should be active at a time, or at most two if they answer clearly different questions. Do not launch many variants and then pick the best-looking result.

### Stage 5 - Deployment Review

Problem solved: keep research progress separate from trading authorization.

Deployment review requires:

- mature prospective evidence;
- clean reconciliation;
- no paper-control leakage from shadow lines;
- stable improvement not dominated by one or two trades;
- drawdown and capacity behavior acceptable;
- explicit user approval.

Allowed statuses:

```text
keep_for_paper_deployment_review
continue_shadow_observation
retest_more_data_needed
deprioritize_candidate
```

Real-money deployment remains out of scope unless explicitly requested and separately reviewed.

## 7. Immediate Next Actions

1. Do not run a new near-window historical `0.35` A/B.
2. Do not repair the abandoned 2023-2024 validation window.
3. Do not change `config/settings.toml`.
4. After the next normal daily/cycle run, check:

```powershell
python main.py paper shadow-decisions --limit 20
python main.py paper shadow-maturity --no-obsidian
python main.py paper shadow-reconciliation --no-obsidian
python main.py db status
```

5. If shadow rows are still absent, continue waiting for normal scan/import or entry-zone 4h decision.
6. If shadow rows appear, first verify reconciliation before interpreting performance.
7. Only after the pre-attribution sample gate is met, begin read-only direct-filtering and capacity-path attribution.

## 8. Plain-Language Summary

The project is keeping `0.35` as the best current research version, but not deploying it. The old 2023-2024 validation route is closed because the data universe is not reliable enough. The clean path now is to observe future paper/shadow decisions in real time, while keeping the original strategy, the `0.35` shadow line, and later challengers separated. The next real work is not another backtest; it is waiting for clean forward samples and then checking whether `0.35` helps because it filters bad entries or because it changes capacity paths.
