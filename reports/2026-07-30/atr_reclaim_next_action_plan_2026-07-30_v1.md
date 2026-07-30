---
created: 2026-07-30 12:25:00 +08:00
tags:
  - crypto
  - trading-system
  - atr-reclaim
  - research-plan
experiment: atr_reclaim_next_action_plan
atr_reclaim_0_35_status: experimental_candidate_unvalidated
---

# atr_reclaim Next Action Plan

## Current System Goal

Validate whether `atr_reclaim_0_35` has stable entry-quality value without relying on the abandoned `2023-07-01 -> 2024-07-01` window.

## Single Question

Can `atr_reclaim_0_35` be validated through cleaner evidence paths without introducing window-selection bias or changing production configuration?

## Current Decision State

- `2023-07-01 -> 2024-07-01` is abandoned as validation evidence.
- N0-N4 artifacts are frozen as diagnostic evidence.
- `atr_reclaim_0_35_status = experimental_candidate_unvalidated`.
- `config/settings.toml` remains unchanged.
- `max_active_positions` remains unchanged.
- No new filters are stacked.

## Stage A - Freeze Abandoned Window

Purpose: prevent the project from drifting back into low-value historical universe repair.

Actions:

- record `abandon_2023_2024_window_for_atr_reclaim_validation`;
- keep N0-N4 artifacts;
- mark prior third-window evidence as diagnostic only;
- block corrected N1 and path fork audit for this window.

Done when:

- decision report exists;
- TODO, experiment ledger, development plan, and experiment log are updated.

## Stage B - Candidate Recent-Window Eligibility Audit

Purpose: determine whether any recent historical window can be used as pre-registered auxiliary evidence.

Important constraint: this stage must not inspect new `atr_reclaim_0_35` A/B results.

Eligibility checks:

1. Window was not used to choose `0.35`.
2. Window result for `atr_reclaim_0_35` has not already been repeatedly inspected.
3. Start and end dates can be locked before A/B.
4. Point-in-time universe can be reliably generated or limitations are small.
5. Practical candidate symbols have complete 1h/4h/1d data.
6. No major unresolved rename, migration, or delisting gap affects likely selected symbols.
7. Baseline and variant can share identical universe and data.
8. Code, settings, max active positions, and metrics can be frozen.
9. Result will be reported once, regardless of direction.

Likely current stance:

`2024-07-01 -> 2026-06-01` and common subwindows have already been heavily observed in prior A/B and walk-forward work. They may be usable only as auxiliary context, not strong validation, unless the audit proves a genuinely unobserved slice exists.

Outputs:

- candidate-window eligibility table;
- decision: `eligible_for_pre_registered_auxiliary_ab` or `no_clean_recent_window_available`.

## Stage C - One-Time Pre-Registered A/B If Eligible

Purpose: obtain one auxiliary historical result without window shopping.

Run only if Stage B passes.

Fixed specification:

- one variable: `entry_reclaim_min_atr = 0.35`;
- no relative-strength filter;
- no capacity change;
- no exit-rule change;
- same symbol universe for baseline and variant;
- same fees, slippage, intrabar policy, and max active positions;
- report portfolio metrics, direct filtering, path contribution, and concentration.

Support criteria:

- net return, PF, and Sharpe improve;
- MDD does not materially worsen;
- direct filtering is not clearly negative;
- improvement is not dominated by a small symbol/month cluster;
- sample is sufficient.

Reject criteria:

- portfolio improvement disappears;
- direct filtering remains negative;
- improvement is mostly path/capacity accident;
- MDD materially worsens;
- sample or universe quality is insufficient.

Insufficient evidence:

- sample too small;
- universe caveats remain material;
- result depends on a few winners;
- baseline and variant cannot be strictly aligned.

## Stage D - Prospective Shadow Observation

Purpose: collect the cleanest evidence using future data and the actual point-in-time universe.

This stage should start immediately and does not require a historical window.

Rules:

- do not modify production or paper trading behavior;
- do not let `atr_reclaim_0_35` control entries;
- do not tune the threshold during observation;
- log both baseline and variant decisions for each raw entry opportunity;
- preserve point-in-time data, universe, position capacity, and rejection reason.

Required fields:

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

Evidence layers:

- signal layer: filtered losers, missed winners, kept winners, kept losers;
- portfolio path layer: whether released capacity leads to better or worse later trades.

Minimum review gate:

- at least 50 mature opportunities for interim review;
- preferably 100 mature opportunities for deployment review;
- right-censored ratio low enough to interpret;
- no threshold changes during the observation period.

## Stage E - Final Decision Gate

Allowed final statuses:

```text
keep_candidate_for_deployment_review
retest_more_data_needed
reject_or_deprioritize_candidate
```

Deployment review requires:

- prospective evidence supports the rule;
- direct filtering mechanism is not clearly negative;
- path/capacity contribution is explainable;
- risk metrics do not materially worsen;
- any historical A/B is used only according to its evidence grade;
- production configuration remains frozen until explicit approval.

## Immediate Next Actions

1. Complete Stage A records.
2. Produce candidate recent-window eligibility audit without running A/B.
3. Draft the prospective shadow observation schema and decide where it should be logged.
4. Only after those are complete, decide whether Stage C is worth running.

## Non-Goals

- Do not repair the abandoned 2023-2024 historical universe.
- Do not continue the 127-symbol mapping queue in this project line.
- Do not run corrected N1 on the abandoned window.
- Do not run path fork audit on the abandoned window.
- Do not deploy or reject `atr_reclaim_0_35` based on abandoned-window evidence.
