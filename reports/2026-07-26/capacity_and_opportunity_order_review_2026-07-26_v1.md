---
created: 2026-07-26 23:48:30 CST
tags:
  - crypto
  - trading-system
  - backtest
  - capacity-review
experiment: capacity_and_opportunity_order_review
verdict: retest_capacity_real_but_not_actionable
---

# capacity_and_opportunity_order_review

## Research frame

- System goal: keep strategy changes explainable before adding more filters or changing production settings.
- Single question: did `max_active_positions=5` and score ordering cause high-quality opportunities to be blocked by lower-quality long-held positions?
- Roadmap position: follow-up to `atr_reclaim_0_35` trade attribution and path replay.
- Fixed scope: no new parameter experiment, no `settings.toml` change, no production decision.

## Plain-language conclusion

Capacity is a real constraint, but the evidence is not clean enough to change the strategy.

The strongest warning sign is that several important opportunities appeared while the opposite run was already full. For example, when baseline missed `ALPINEUSDT`, all 5 baseline slots were occupied and all 5 later finished around `-1R`. That is a clear example of low-quality slot occupation.

But this pattern is not one-sided. When variant missed baseline winners such as `UNIUSDT` and `LINKUSDT` in July 2025, variant was also full, but the active positions were mostly profitable. That means the system was often choosing between good opportunities, not simply letting bad trades block good trades.

So the decision is: do not raise `max_active_positions`, do not change score sorting, and do not deploy `atr_reclaim_0_35` based on this review. The next useful work is to define a measurable replacement-quality diagnostic before any capacity or ordering experiment.

## Facts

- Backtest runs reviewed:
  - baseline: `110c51eef593`
  - variant: `54da79435459`
- Window: `2025-06-01 -> 2026-06-01`
- Entry ordering in replay: WATCHING plans are sorted by `(-score, created_index, symbol)`.
- Capacity check happens after entry-zone touch and reclaim confirmation.
- `backtest_trades.payload_json.notes` does not retain each skipped max-active attempt, so this review reconstructs active slots at key event times instead of claiming exact skipped-entry counts.

## Key event capacity table

| Case | Opposite run active slots | Candidate score / R | Lower-score blockers | Negative blockers | Blocker final net / R | Read |
|---|---:|---:|---:|---:|---:|---|
| variant winner `CFXUSDT` 2025-07-27 | 5 | 68.4 / 3.34 | 1 | 4 | -286 / -2.60 | capacity mixed |
| variant winner `ALPINEUSDT` 2025-08-14 | 5 | 73.4 / 2.85 | 5 | 5 | -572 / -5.11 | capacity bad |
| variant winner `ENAUSDT` 2025-07-24 | 5 | 62.7 / 2.90 | 0 | 4 | -286 / -2.60 | capacity mixed |
| variant winner `LINKUSDT` 2025-06-26 | 4 | 53.9 / 2.87 | 0 | 1 | +447 / +4.38 | not capacity |
| variant winner `ADAUSDT` 2025-07-17 | 5 | 75.7 / 2.44 | 5 | 2 | +268 / +2.37 | capacity mixed |
| missed baseline `BTCUSDT` 2025-06-28 | 1 | 59.1 / 3.16 | 0 | 1 | -101 / -1.01 | not capacity |
| missed baseline `UNIUSDT` 2025-07-16 | 5 | 72.4 / 2.47 | 4 | 1 | +692 / +6.48 | capacity mixed |
| missed baseline `LINKUSDT` 2025-07-13 | 5 | 64.3 / 2.57 | 4 | 1 | +546 / +5.20 | capacity mixed |
| missed baseline `UNIUSDT` 2025-06-08 | 2 | 51.5 / 2.77 | 1 | 0 | +365 / +3.63 | not capacity |
| missed baseline `BONKUSDT` 2025-07-10 | 4 | 65.5 / 2.44 | 4 | 1 | +442 / +4.38 | not capacity |

## Occupancy over the full near window

| Run | 4h bars sampled | Bars at 5 active slots | Bars at 4+ active slots | Average active slots | Max active slots |
|---|---:|---:|---:|---:|---:|
| baseline | 2191 | 613 (28.0%) | 34.6% | 1.97 | 5 |
| variant | 2191 | 663 (30.3%) | 33.5% | 1.97 | 5 |

Interpretation: both runs are capacity-constrained during a meaningful share of the year. Variant did not simply create more capacity overall; it changed which path filled the same capacity.

## Long-held negative slot occupation

| Run | Negative trades held 240h+ | Slot-hours occupied | Final net PnL | Final R |
|---|---:|---:|---:|---:|
| baseline | 9 | 7876h | -977.91 | -9.17 |
| variant | 10 | 8760h | -1128.39 | -10.18 |

Examples:

| Run | Symbol | Hold hours | Score | Final R | Note |
|---|---|---:|---:|---:|---|
| baseline | `APTUSDT` | 2548 | 63.2 | -1.01 | long slot occupation ending at stop |
| baseline | `BCHUSDT` | 1568 | 61.6 | -1.02 | long slot occupation ending at stop |
| baseline | `CRVUSDT` | 844 | 71.9 | -1.01 | high score did not imply good slot use |
| variant | `APTUSDT` | 2548 | 63.2 | -1.01 | shared long loser |
| variant | `BCHUSDT` | 1568 | 61.6 | -1.02 | shared long loser |
| variant | `LTCUSDT` | 1100 | 73.6 | -1.02 | high score long loser |

## Observations

- Capacity explains some `atr_reclaim_0_35` variant winners, especially `ALPINEUSDT`; it does not explain all of them.
- Score ordering is not enough to rank future slot value. Several high-score active positions later lost around `-1R`, while some lower-score or moderate-score missed opportunities reached TP2.
- The issue is not just `max_active_positions=5`; it is also stale slot retention. Long-held trades that never reach TP1 can occupy capacity for weeks or months.
- The same problem appears in both baseline and variant, so it should be treated as a system-level portfolio management question, not an ATR reclaim rule justification.

## Hypotheses

- A future capacity experiment should not start by raising `max_active_positions`. Higher capacity may simply allow more long-held losers.
- The more plausible research direction is replacement quality: when the portfolio is full, should a stale, negative-progress, pre-TP1 position be replaced by a fresh higher-quality opportunity?
- That replacement question must be tested independently from `atr_reclaim_0_35`; otherwise capacity effects and entry-gate effects remain confounded.

## Decision

`retest_capacity_real_but_not_actionable`

Capacity and opportunity ordering are real contributors to path dependence, but the current evidence is mixed. There is no approval to change production config, raise capacity, alter score ordering, or deploy `atr_reclaim_0_35`.

## Next action

Define a diagnostic-only `slot_replacement_quality_review`:

- For each time the portfolio is full and a fresh opportunity becomes entry-ready, compare the fresh opportunity against each active slot.
- Measure active slot age, unrealized R, TP1 status, score, and eventual outcome.
- Approval criterion for a future experiment: replacement candidates must show consistently better forward R than the stale slots they would replace, across more than a few isolated July/August 2025 cases.
