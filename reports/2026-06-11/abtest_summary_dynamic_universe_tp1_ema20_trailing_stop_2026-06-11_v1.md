---
created: 2026-06-11 10:15:51 CST
tags:
  - crypto
  - trading-system
  - abtest-summary
experiment_id: tp1_ema20_trailing_stop
mode: dynamic_universe
periods: 2
sufficient_periods: 2
unique_coverage_days: 427
overlap_periods: 0
universe_warnings: 1
verdict: retest
report_version: v1
---

# A/B 多时段汇总 tp1_ema20_trailing_stop v1

- experiment_id: `tp1_ema20_trailing_stop`
- mode: `dynamic_universe`
- periods: 2
- sufficient_periods: 2
- total_period_days: 427
- unique_coverage_days: 427
- overlap_periods: 0
- universe_warnings: 1
- net_improved_periods: 2
- profit_factor_improved_periods: 2
- drawdown_improved_periods: 1
- variant_under_sample_periods: 0
- verdict: `retest`
- reason: Results are mixed or sample coverage is incomplete; continue cross-period testing.

## Period Results

| Period | Sample | Closed B -> V | Win B -> V | PF B -> V | Sharpe B -> V | MDD B -> V | Net B -> V | Stop B -> V | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 2024-07-01 -> 2025-01-01 | yes | 35.00 -> 49.00 | 34.29% -> 44.90% | 1.30 -> 1.41 | 0.78 -> 1.20 | 10.67% -> 10.54% | 7.14% -> 11.82% | 65.71% -> 79.59% | retest |
| 2025-01-01 -> 2025-09-01 | yes | 42.00 -> 53.00 | 19.05% -> 32.08% | 0.58 -> 0.75 | -1.03 -> -0.77 | 19.43% -> 19.78% | -13.17% -> -10.31% | 80.95% -> 86.79% | retest |

## Universe Bias Checks

- Dynamic universe uses current Binance exchangeInfo as the symbol master; historic delisted symbols may be missing.

## Source Reports

- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-11\abtest_dynamic_universe_tp1_ema20_trailing_stop_2024-07-01_2025-01-01_v1.md`
- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-11\abtest_dynamic_universe_tp1_ema20_trailing_stop_2025-01-01_2025-09-01_v1.md`

## Decision Rule

- 汇总报告只给出 `candidate_keep_review`、`retest` 或 `reject_candidate`，不会自动修改默认配置。
- 至少需要多个充足样本时段共同改善净收益、Profit factor 和最大回撤，才会标记 `candidate_keep_review`。
- 时段存在重叠时，证据不视为完全独立，结论保持 `retest`。
- 任一 variant 样本不足时，结论应偏向 `retest`。

## Raw Summary

```json
{
  "experiment_id": "tp1_ema20_trailing_stop",
  "mode": "dynamic_universe",
  "periods": 2,
  "sufficient_periods": 2,
  "total_period_days": 427,
  "unique_coverage_days": 427,
  "overlap_periods": 0,
  "universe_warnings": [
    "Dynamic universe uses current Binance exchangeInfo as the symbol master; historic delisted symbols may be missing."
  ],
  "net_improved_periods": 2,
  "profit_factor_improved_periods": 2,
  "drawdown_improved_periods": 1,
  "variant_under_sample_periods": 0,
  "verdict": "retest",
  "reason": "Results are mixed or sample coverage is incomplete; continue cross-period testing.",
  "records": [
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-11\\abtest_dynamic_universe_tp1_ema20_trailing_stop_2024-07-01_2025-01-01_v1.md",
      "start": "2024-07-01",
      "end": "2025-01-01",
      "sample_sufficient": true,
      "dynamic_metadata": {
        "baseline_master_count": "418",
        "variant_master_count": "418",
        "baseline_source_limit": "None",
        "variant_source_limit": "None",
        "baseline_universe_refreshes": "185",
        "variant_universe_refreshes": "185"
      },
      "baseline": {
        "trades": 178,
        "closed_trades": 35,
        "open_trades": 2,
        "win_rate": 34.285714285714285,
        "profit_factor": 1.3045231175786178,
        "avg_r": 0.24019530504725956,
        "net_return_pct": 7.141188711650748,
        "max_drawdown": 1067.1418735291263,
        "max_drawdown_pct": 10.671418735291264,
        "intrabar_max_drawdown": 1104.9997915491313,
        "intrabar_max_drawdown_pct": 11.049997915491312,
        "tp1_rate": 37.142857142857146,
        "tp2_rate": 34.285714285714285,
        "stop_rate": 65.71428571428571,
        "fee_drag": 40.61548958822572,
        "tail_max_loss": -117.19916034615537,
        "cagr": 14.663316853283082,
        "sharpe": 0.7773262810702322,
        "sortino": 0.8304264844304116,
        "exposure_pct": 85.05434782608695,
        "turnover": 3.488987406992759,
        "sample_sufficient": true,
        "sample_warning": ""
      },
      "variant": {
        "trades": 187,
        "closed_trades": 49,
        "open_trades": 1,
        "win_rate": 44.89795918367347,
        "profit_factor": 1.4149891020331626,
        "avg_r": 0.27069492185581046,
        "net_return_pct": 11.819734879999832,
        "max_drawdown": 1314.2337295588368,
        "max_drawdown_pct": 10.540172207842609,
        "intrabar_max_drawdown": 1236.0745727909143,
        "intrabar_max_drawdown_pct": 9.977526870173044,
        "tp1_rate": 42.857142857142854,
        "tp2_rate": 20.408163265306122,
        "stop_rate": 79.59183673469387,
        "fee_drag": 60.72060369496798,
        "tail_max_loss": -126.0206167075499,
        "cagr": 24.808985949617846,
        "sharpe": 1.1985507088119007,
        "sortino": 1.3169782647655341,
        "exposure_pct": 85.05434782608695,
        "turnover": 4.800345358799808,
        "sample_sufficient": true,
        "sample_warning": ""
      }
    },
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-11\\abtest_dynamic_universe_tp1_ema20_trailing_stop_2025-01-01_2025-09-01_v1.md",
      "start": "2025-01-01",
      "end": "2025-09-01",
      "sample_sufficient": true,
      "dynamic_metadata": {
        "baseline_master_count": "418",
        "variant_master_count": "418",
        "baseline_source_limit": "None",
        "variant_source_limit": "None",
        "baseline_universe_refreshes": "244",
        "variant_universe_refreshes": "244"
      },
      "baseline": {
        "trades": 271,
        "closed_trades": 42,
        "open_trades": 5,
        "win_rate": 19.047619047619047,
        "profit_factor": 0.5788303615775615,
        "avg_r": -0.32109130123569374,
        "net_return_pct": -13.169473352124028,
        "max_drawdown": 1999.7034664765688,
        "max_drawdown_pct": 19.428139493966125,
        "intrabar_max_drawdown": 1981.126720276632,
        "intrabar_max_drawdown_pct": 19.391240086382176,
        "tp1_rate": 30.952380952380953,
        "tp2_rate": 19.047619047619047,
        "stop_rate": 80.95238095238095,
        "fee_drag": 51.18942488974736,
        "tail_max_loss": -104.26307084075773,
        "cagr": -19.112304164922577,
        "sharpe": -1.0333162547884633,
        "sortino": -1.26161554956655,
        "exposure_pct": 87.72290809327846,
        "turnover": 4.471898425556106,
        "sample_sufficient": true,
        "sample_warning": ""
      },
      "variant": {
        "trades": 272,
        "closed_trades": 53,
        "open_trades": 4,
        "win_rate": 32.075471698113205,
        "profit_factor": 0.7507286876872792,
        "avg_r": -0.14227258787163016,
        "net_return_pct": -10.311962500816374,
        "max_drawdown": 2036.2491941919234,
        "max_drawdown_pct": 19.78319988560181,
        "intrabar_max_drawdown": 2017.4184566674558,
        "intrabar_max_drawdown_pct": 19.7464630846404,
        "tp1_rate": 28.30188679245283,
        "tp2_rate": 13.20754716981132,
        "stop_rate": 86.79245283018868,
        "fee_drag": 72.17806273428576,
        "tail_max_loss": -106.48236721520288,
        "cagr": -15.081067197160358,
        "sharpe": -0.7657707274278789,
        "sortino": -0.9256530332195974,
        "exposure_pct": 87.79149519890261,
        "turnover": 5.799481326780514,
        "sample_sufficient": true,
        "sample_warning": ""
      }
    }
  ]
}
```
