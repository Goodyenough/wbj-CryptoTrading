---
created: 2026-07-30 18:57:42 +08:00
tags:
  - crypto
  - paper-trading
  - time-exit
  - max-holding-42
status: review_complete
verdict: defer_keep_review_insufficient_forward_evidence
---

# Paper Max Holding 42 Forward Review

## Background

`max_holding_bars_without_tp1=42` means: after a paper trade enters, if it still has not touched TP1 after 42 closed 4h bars, the system would force a defensive `TIME_EXIT`.

Historical A/B results made fixed 42 bars a candidate, but the project rule is that a backtest improvement alone is not enough to change default production settings. The 5-day database stability gate has now passed, so the next step is to review the available paper evidence.

## Question

Does current paper evidence support writing fixed `max_holding_bars_without_tp1=42` into default `config/settings.toml`?

## Evidence Used

- Report: `reports/2026-07-30/paper_4h_dashboard_1840_demo_v1.md`
- Database: `data/crypto_trading.db`
- Health gate: `python main.py db stability --days 5` passed for `2026-07-25 -> 2026-07-29`
- Event checks:
  - `python main.py paper db-events --plan-id 2ed171ff8ada --limit 50`
  - `python main.py paper db-events --plan-id 5d1c3b7ddf56 --limit 50`
  - `python main.py paper db-events --plan-id 616e1bbfd4c6 --limit 50`

## Current Paper Samples

| Symbol | Plan | First observed >=168h | PnL at first observation | Max PnL after | Min PnL after | Final outcome |
|---|---|---:|---:|---:|---:|---|
| `ONDOUSDT` | `2ed171ff8ada` | 596.9h | `15.73` | `65.58` | `-99.71` | `STOPPED` |
| `ONDOUSDT` | `5d1c3b7ddf56` | 596.7h | `18.54` | `69.61` | `-99.70` | `STOPPED` |
| `WLDUSDT` | `616e1bbfd4c6` | 176.5h | `120.13` | `132.65` | `-98.50` | `STOPPED` |

Event review found no `TP1_HIT` before the final `STOPPED` event for these three plans.

## Interpretation

Plain-language reading:

The three available paper examples all support the idea that very long pre-TP1 holds can waste time and later turn into stop losses. In these cases, a 42-bar defensive exit would probably have avoided the full stop outcome.

Technical reading:

- Mature over-42h samples: `3`
- Terminal outcome after threshold: `3/3 STOPPED`
- Same-symbol concentration: `2/3` samples are `ONDOUSDT`
- Independent symbol count: `2`
- Right-censoring among these over-threshold rows: `0/3`
- Sample limitation: the first ONDO observation only appears after roughly `597h`, so the dashboard cannot reconstruct the exact 168h mark for those legacy rows.

## Decision

`defer_keep_review_insufficient_forward_evidence`

Do not write `max_holding_bars_without_tp1=42` into default `config/settings.toml` yet.

Reason:

The available paper evidence is directionally supportive, but the sample is too small and too concentrated. It shows that the rule remains a valuable candidate, not that it is ready for default deployment.

## Next Action

- Keep default settings unchanged.
- Continue daily + 4h paper observation.
- Re-run this review after at least `5` independent symbols or `8-10` terminal over-42h pre-TP1 cases are available.
- If future samples remain mostly `STOPPED` after the 42-bar threshold without cutting delayed TP1 winners, then reopen the keep review for fixed `max_holding_bars_without_tp1=42`.
