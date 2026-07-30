---
created: 2026-07-30 12:25:00 +08:00
tags:
  - crypto
  - trading-system
  - atr-reclaim
  - research-decision
experiment: atr_reclaim_2023_2024_window_abandonment_decision
decision: abandon_2023_2024_window_for_atr_reclaim_validation
atr_reclaim_0_35_status: experimental_candidate_unvalidated
---

# atr_reclaim 2023-2024 Window Abandonment Decision

## Decision

`abandon_2023_2024_window_for_atr_reclaim_validation`

The window `2023-07-01 -> 2024-07-01` is abandoned as validation evidence for `atr_reclaim_0_35`.

This does not delete or invalidate prior work. It freezes N0-N4 as diagnostic evidence and stops further engineering on this historical window for the current atr reclaim validation path.

## System Goal

Keep `atr_reclaim_0_35` research focused on clean, explainable evidence instead of spending disproportionate effort repairing a historical universe that may remain unreliable.

## Reason

N2-N4 showed that this window has a material historical universe problem:

- N2 historical USDT symbols in window: `413`
- Present in current master: `266`
- Missing from current master: `147`
- N3 standard-like historical gap after excluding obvious nonstandard assets: `127`
- N3 standard gap ratio: `32.32%`
- N4 verdict: `historical_master_mvp_built_validation_blocked`

Fixing this window would require point-in-time universe reconstruction, delisting and migration mapping, multi-interval kline repair, and renewed path audits. That work is outside the current main strategy-validation line and may still not produce a clean confirmatory window.

## Stop Conditions

No further engineering work will be performed on the `2023-07-01 -> 2024-07-01` validation window unless a future independent project explicitly requires historical-master reconstruction.

Specifically, the current project will not:

- repair this window's historical universe;
- continue source-backed mapping for the 127 blocking symbols;
- rerun corrected N1 on this window;
- run a full path fork audit on this window;
- use this window to keep, reject, or deploy `atr_reclaim_0_35`.

## Artifact Status

The following artifacts remain useful as diagnostic records:

- N0 readiness audits;
- N1 diagnostic retest and mechanism review;
- N2 universe and data substrate audit;
- N3 historical membership dataset classification;
- N4 historical master MVP and review queue.

They may be cited to show:

- current exchangeInfo creates survivor-bias risk in historical dynamic-universe backtests;
- historical windows require universe audit before validation;
- the observed `atr_reclaim_0_35` improvement was path-dependent;
- `2023-2024` should not be treated as clean validation evidence.

They must not be used as evidence that `atr_reclaim_0_35` is valid, invalid, deployable, or rejected.

## Strategy Status

`atr_reclaim_0_35_status = experimental_candidate_unvalidated`

This means:

- not `keep`;
- not `rejected`;
- not deployed;
- still eligible for future validation through cleaner evidence paths.

## Next Direction

The research line now moves to:

```text
freeze diagnostic artifacts
-> pre-register cleaner recent-window A/B only if eligible
-> start prospective shadow observation immediately
-> keep atr_reclaim_0_35 undeployed
```

Near-term historical A/B, if any, is auxiliary evidence only unless the candidate window passes a strict pre-registration and contamination audit.

Prospective shadow observation becomes the cleanest confirmation path.
