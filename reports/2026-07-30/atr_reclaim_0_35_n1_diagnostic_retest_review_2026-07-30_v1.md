---
created: 2026-07-30 00:18:00 CST
tags:
  - crypto
  - trading-system
  - atr-reclaim
  - diagnostic-retest
experiment: atr_reclaim_0_35_n1_diagnostic_retest
verdict: retest_path_dependent
baseline_run_id: 86861b2dd032
variant_run_id: 0d78a8dc60e3
---

# atr_reclaim_0_35 N1 Diagnostic Retest Review

## Plain-language conclusion

`atr_reclaim_0_35` 在第三窗口的组合层结果继续变好，但机制层没有通过。更严格的 0.35 ATR reclaim 不是稳定地“直接过滤亏损”：它确实避开了一批亏损，但错过的赢家更大；最终收益改善主要来自路径变化、延后入场、容量释放后的新增赢家，以及少数月份/币种贡献。因此结论不是 keep，而是 `retest_path_dependent`。

This is a diagnostic retest only. Stage N0 already found `listing_dates_present=false` and third-window universe coverage caveats, so this result must not be called clean confirmatory validation.

## Scope

| Field | Value |
|---|---|
| Main question | baseline vs fixed `atr_reclaim_0_35` in third window |
| Window | `2023-07-01 -> 2024-07-01` |
| Symbol master | `reports/2026-06-09/dynamic_master_full.json` |
| N0 report | `reports/2026-07-29/atr_reclaim_n0_readiness_audit_2026-07-29_v1.md` |
| A/B report | `reports/2026-07-30/abtest_dynamic_universe_atr_reclaim_0_35_2023-07-01_2024-07-01_v1.md` |
| Baseline run | `86861b2dd032` |
| Variant run | `0d78a8dc60e3` |
| Baseline backtest report | `reports/2026-07-29/backtest_dynamic_universe_2023-07-01_2024-07-01_v1.md` |
| Variant backtest report | `reports/2026-07-30/backtest_dynamic_universe_2023-07-01_2024-07-01_v1.md` |
| Cross-midnight artifact | Baseline report was written before Beijing midnight; A/B and variant reports after midnight. |

## Portfolio Layer

| Metric | Baseline | Variant | Delta |
|---|---:|---:|---:|
| trades | 683 | 693 | +10 |
| closed_trades | 122 | 116 | -6 |
| win_rate | 47.54% | 50.00% | +2.46 pp |
| profit_factor | 1.264 | 1.376 | +0.113 |
| avg_r | 0.189 | 0.258 | +0.069 |
| net_return_pct | 22.10% | 31.55% | +9.46 pp |
| max_drawdown_pct | 21.85% | 21.08% | -0.78 pp |
| sharpe | 0.932 | 1.238 | +0.306 |
| sortino | 1.035 | 1.342 | +0.307 |
| stop_rate | 83.61% | 82.76% | -0.85 pp |
| exposure_pct | 78.19% | 76.68% | -1.50 pp |
| fee_drag | 216.23 | 213.29 | -2.94 |

Portfolio verdict: supportive. The variant improves net return, PF, Sharpe, Sortino, win rate, stop rate, and drawdown while retaining sufficient sample.

## Mechanism Layer

### Opportunity-path decomposition

Opportunity key used here is approximate: `(symbol, created_at_utc)`. N0 already warned that there is no strict stable opportunity id shared by baseline and variant.

| Bucket | Count | Closed | Net PnL | Sum R | Wins | Losses | Interpretation |
|---|---:|---:|---:|---:|---:|---:|---|
| same key: baseline entered, variant did not | 50 | 50 | +1,335.62 | +13.282 | 26 | 24 | Direct strict filtering was net harmful. |
| same key: variant entered, baseline did not | 36 | 36 | +1,609.43 | +13.716 | 19 | 17 | Path/capacity-timing added value. |
| same key: both entered, baseline | 51 | 51 | -1,275.50 | -7.758 | 19 | 32 | Shared opportunities were weak. |
| same key: both entered, variant | 51 | 51 | -1,180.08 | -5.246 | 19 | 32 | Same-key delta was only +95.43 PnL. |
| baseline-only entered | 21 | 21 | +2,149.62 | +17.548 | 13 | 8 | Removing these was net harmful. |
| variant-only entered | 29 | 29 | +2,726.00 | +21.507 | 20 | 9 | Main positive contribution came from added path trades. |

Strict direct-filter test:

| Component | Count | PnL Impact |
|---|---:|---:|
| avoided losers from same-key baseline-entered / variant-not-entered | 24 | +3,141.55 |
| missed winners from same-key baseline-entered / variant-not-entered | 26 | -4,477.17 |
| net direct-filter effect | 50 | -1,335.62 |

This fails the N1 mechanism criterion. The direct filter missed more winner value than it avoided loser value.

### Contribution reconciliation

| Component | PnL Delta |
|---|---:|
| Remove same-key baseline-entered / variant-not-entered trades | -1,335.62 |
| Add same-key variant-entered / baseline-not-entered trades | +1,609.43 |
| Delta among same-key trades where both entered | +95.43 |
| Remove baseline-only entered trades | -2,149.62 |
| Add variant-only entered trades | +2,726.00 |
| Total explained delta | +945.62 |

The total explained delta matches portfolio net PnL delta: 3155.36 - 2209.74 = +945.62.

## Cluster Concentration

### Symbol contribution

| Rank | Symbol | PnL Contribution |
|---:|---|---:|
| 1 | DOTUSDT | +627.22 |
| 2 | FETUSDT | +388.31 |
| 3 | ETCUSDT | +368.61 |
| 4 | APTUSDT | +354.97 |
| 5 | NEARUSDT | +332.50 |
| Bottom 1 | FILUSDT | -728.82 |
| Bottom 2 | ATOMUSDT | -481.67 |
| Bottom 3 | UNIUSDT | -213.40 |

### Month contribution

| Month | PnL Contribution |
|---|---:|
| 2023-12 | +936.23 |
| 2023-11 | +742.67 |
| 2023-10 | +396.29 |
| 2024-01 | +70.91 |
| 2024-02 | -830.94 |
| 2024-03 | -355.19 |
| 2024-06 | -203.85 |

### Top symbol-months

| Rank | Symbol-month | PnL Contribution |
|---:|---|---:|
| 1 | FETUSDT 2024-03 | +388.31 |
| 2 | ETCUSDT 2024-03 | +368.61 |
| 3 | NEARUSDT 2023-11 | +364.99 |
| 4 | BTCUSDT 2023-12 | +358.86 |
| 5 | DOTUSDT 2023-12 | +324.16 |
| Bottom 1 | ETHUSDT 2024-03 | -385.97 |
| Bottom 2 | UNIUSDT 2024-03 | -369.29 |
| Bottom 3 | ATOMUSDT 2024-03 | -353.66 |

Concentration verdict: not clean. Positive result depends heavily on 2023-11/12 and a handful of path-added winners, while 2024-02/03 are strongly negative.

## MFE / MAE Approximation

Approximation uses 4h kline high/low from entered time to closed time and normalizes by entry-to-stop risk.

| Bucket | n | Avg MFE R | Median MFE R | Avg MAE R | Median MAE R |
|---|---:|---:|---:|---:|---:|
| filtered baseline-entered trades | 21 | 1.928 | 1.987 | -0.522 | -0.478 |
| added variant-entered trades | 29 | 1.885 | 1.996 | -0.481 | -0.289 |

MFE/MAE does not show a decisive quality gap. Added trades have slightly better MAE, but filtered trades had comparable MFE and were net profitable.

## Decision Against N1 Criteria

| Criterion | Result |
|---|---|
| Portfolio improves PF and net return | Pass |
| Max drawdown does not worsen | Pass |
| Sample sufficient | Pass |
| Direct filtered opportunities avoided loser R greater than missed winner R | Fail |
| Improvement not dominated by path/capacity changes | Fail |
| Cluster concentration acceptable | Fail / weak |
| Universe caveat resolved | Fail |

## Final Verdict

`retest_path_dependent`

`atr_reclaim_0_35` remains a valuable candidate, but N1 does not justify keep or deployment. The third-window diagnostic supports that the rule can improve portfolio outcomes, but the mechanism is still path-dependent: direct filtering is net harmful, and the benefit comes mostly from added/delayed/path trades plus favorable clusters.

## Next Action

Do not deploy. Do not add more filters on top. Do not tune neighboring thresholds using this same third window.

Best next action is to fix the research substrate:

1. Build or fetch a listing-date enriched symbol master / historical membership evidence.
2. Rerun Stage N0.
3. Only if N0 passes or the caveat is explicitly accepted, rerun N1 with strict opportunity IDs or a better opportunity-alignment export.
