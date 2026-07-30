---
created: 2026-07-30 19:12:00 +08:00
tags:
  - crypto
  - paper-trading
  - execution-quality
  - state-consistency
status: precheck_complete
verdict: execution_precheck_pass_shadow_reconciliation_waiting_for_samples
---

# Paper Execution State Consistency Precheck

## Background

The incumbent/challenger plan lists execution quality, slippage, and state consistency as a required check before trusting later challenger experiments. The immediate risk is that backtest, paper, and shadow decision states may diverge, causing research to optimize behavior that cannot be executed or observed in paper trading.

This precheck is read-only. It does not run a new A/B, does not modify `config/settings.toml`, and does not change paper plan state.

## Question

Is the current paper database and shadow logging chain clean enough to continue prospective observation?

## Evidence Used

- `python main.py db status`
- `python main.py db stability --days 5`
- `python main.py paper shadow-decisions --limit 5`
- `reports/2026-07-30/paper_shadow_maturity_review_2026-07-30_demo_v8.md`
- Read-only SQLite checks on `paper_plans`, `paper_events`, `paper_snapshots`, and `paper_shadow_decisions`

## Database And Run Health

| Check | Result |
|---|---|
| schema version | `2` |
| tables/indexes | OK |
| foreign keys | OK |
| UTC timestamps | OK |
| latest run | `20260730_104051_53df384d`, `paper_4h_update`, `success` |
| 5-day daily stability | pass |
| stable config hash | `be7ec39ec21f6a83` |
| ready for 4h task | `true` |

## Paper State Counts

| Metric | Value |
|---|---:|
| paper plans | 25 |
| paper snapshots | 534 |
| shadow decisions | 0 |
| duplicate event groups | 0 |
| events without plan | 0 |
| snapshots without plan | 0 |

## Plan Status

| Status | Count |
|---|---:|
| `ARCHIVED` | 13 |
| `STOPPED` | 8 |
| `INVALIDATED` | 3 |
| `WATCHING` | 1 |

Current open plan:

| Plan | Symbol | Status | Entry low | Entry high | Updated |
|---|---|---|---:|---:|---|
| `9734a33dea2e` | `ONDOUSDT` | `WATCHING` | 0.394505 | 0.41156785714285715 | `2026-07-30T10:40:51Z` |

## Event Type Counts

| Event type | Count |
|---|---:|
| `RECLAIM_PENDING_SET` | 231 |
| `WATCHLIST_ADDED` | 25 |
| `ARCHIVED` | 13 |
| `ENTERED` | 8 |
| `STOPPED` | 8 |
| `INVALIDATED` | 3 |
| `RECLAIM_PENDING` | 3 |
| `API_DELAY_SKIPPED` | 1 |

## Execution / State Interpretation

Clean findings:

- The paper database health checks pass.
- Five consecutive daily runs are ready and use a stable config hash.
- Paper events and snapshots are linked to known plans.
- No duplicate event groups were found.
- The latest successful 4h update generated downstream reports.
- One transient Binance/SSL issue was captured as `API_DELAY_SKIPPED`, which preserved auditability without changing trade status.

Blocking limitation:

- `paper_shadow_decisions` is still empty, so direct state reconciliation between `reference_baseline`, `atr_reclaim_0_35_shadow`, and `research_incumbent` cannot yet be evaluated.
- Slippage/fill quality cannot be concluded from this precheck because the current paper engine uses simulated paper prices rather than exchange execution fills.

## Decision

`execution_precheck_pass_shadow_reconciliation_waiting_for_samples`

The paper data chain is clean enough to continue prospective observation, but not enough to validate `atr_reclaim_0_35` or any future challenger. The next evidence gate is still the first daily/import candidate-level rows or plan-linked 4h shadow decision rows.

## Next Action

- Keep `config/settings.toml` unchanged.
- Do not start a new challenger until shadow rows begin accumulating.
- After the next normal daily scan/import or entry-zone 4h update, run `python main.py paper shadow-maturity --no-obsidian` and inspect whether `paper_shadow_decisions` now contains candidate-level or plan-linked rows.
- Once rows exist, start a proper decision-state reconciliation report: reference baseline vs `atr_reclaim_0_35_shadow` vs research incumbent.
