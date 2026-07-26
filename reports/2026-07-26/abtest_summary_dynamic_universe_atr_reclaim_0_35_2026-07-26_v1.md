---
created: 2026-07-26 18:04:30 CST
tags:
  - crypto
  - trading-system
  - abtest-summary
experiment_id: atr_reclaim_0_35
mode: dynamic_universe
periods: 2
sufficient_periods: 2
unique_coverage_days: 700
overlap_periods: 0
universe_warnings: 1
verdict: candidate_keep_review
report_version: v1
---

# A/B 多时段汇总 atr_reclaim_0_35 v1

- experiment_id: `atr_reclaim_0_35`
- mode: `dynamic_universe`
- periods: 2
- sufficient_periods: 2
- total_period_days: 700
- unique_coverage_days: 700
- overlap_periods: 0
- universe_warnings: 1
- net_improved_periods: 2
- profit_factor_improved_periods: 2
- drawdown_improved_periods: 2
- variant_under_sample_periods: 0
- verdict: `candidate_keep_review`
- reason: All sufficient periods improved net return, Profit factor, and max drawdown; manual review is still required.

## Period Results

| Period | Sample | Closed B -> V | Win B -> V | PF B -> V | Sharpe B -> V | MDD B -> V | Net B -> V | Stop B -> V | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 2024-07-01 -> 2025-06-01 | yes | 76.00 -> 78.00 | 38.16% -> 48.72% | 0.95 -> 1.62 | -0.01 -> 0.93 | 16.59% -> 14.95% | -2.09% -> 18.20% | 89.47% -> 76.92% | retest |
| 2025-06-01 -> 2026-06-01 | yes | 57.00 -> 53.00 | 40.35% -> 45.28% | 1.11 -> 1.31 | 0.26 -> 0.60 | 20.75% -> 15.27% | 3.11% -> 9.33% | 85.96% -> 84.91% | retest |

## Universe Bias Checks

- Dynamic universe uses current Binance exchangeInfo as the symbol master; historic delisted symbols may be missing.

## Source Reports

- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-07-26\abtest_dynamic_universe_atr_reclaim_0_35_2024-07-01_2025-06-01_v1.md`
- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-07-26\abtest_dynamic_universe_atr_reclaim_0_35_2025-06-01_2026-06-01_v1.md`

## Decision Rule

- 汇总报告只给出 `candidate_keep_review`、`retest` 或 `reject_candidate`，不会自动修改默认配置。
- 至少需要多个充足样本时段共同改善净收益、Profit factor 和最大回撤，才会标记 `candidate_keep_review`。
- 时段存在重叠时，证据不视为完全独立，结论保持 `retest`。
- 任一 variant 样本不足时，结论应偏向 `retest`。

## Raw Summary

```json
{
  "experiment_id": "atr_reclaim_0_35",
  "mode": "dynamic_universe",
  "periods": 2,
  "sufficient_periods": 2,
  "total_period_days": 700,
  "unique_coverage_days": 700,
  "overlap_periods": 0,
  "universe_warnings": [
    "Dynamic universe uses current Binance exchangeInfo as the symbol master; historic delisted symbols may be missing."
  ],
  "net_improved_periods": 2,
  "profit_factor_improved_periods": 2,
  "drawdown_improved_periods": 2,
  "variant_under_sample_periods": 0,
  "verdict": "candidate_keep_review",
  "reason": "All sufficient periods improved net return, Profit factor, and max drawdown; manual review is still required.",
  "records": [
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-07-26\\abtest_dynamic_universe_atr_reclaim_0_35_2024-07-01_2025-06-01_v1.md",
      "start": "2024-07-01",
      "end": "2025-06-01",
      "sample_sufficient": true,
      "dynamic_metadata": {
        "baseline_master_count": "418",
        "variant_master_count": "418",
        "baseline_source_limit": "None",
        "variant_source_limit": "None",
        "baseline_universe_refreshes": "336",
        "variant_universe_refreshes": "336"
      },
      "baseline": {
        "trades": 491,
        "closed_trades": 76,
        "open_trades": 2,
        "win_rate": 38.15789473684211,
        "profit_factor": 0.9497022392762177,
        "avg_r": -0.008733834521892258,
        "net_return_pct": -2.085381747848458,
        "max_drawdown": 1913.5674696124388,
        "max_drawdown_pct": 16.590752201409874,
        "intrabar_max_drawdown": 1898.8721286879845,
        "intrabar_max_drawdown_pct": 16.55447336667667,
        "tp1_rate": 38.15789473684211,
        "tp2_rate": 10.526315789473683,
        "stop_rate": 89.47368421052632,
        "fee_drag": 101.23230923887559,
        "tail_max_loss": -115.29716538521697,
        "cagr": -2.2699971791179663,
        "sharpe": -0.01397676540932231,
        "sortino": -0.014062573304631853,
        "exposure_pct": 58.05970149253732,
        "turnover": 7.729736834412474,
        "sample_sufficient": true,
        "sample_warning": ""
      },
      "variant": {
        "trades": 494,
        "closed_trades": 78,
        "open_trades": 3,
        "win_rate": 48.717948717948715,
        "profit_factor": 1.6247248711653803,
        "avg_r": 0.36183866973669176,
        "net_return_pct": 18.20432087132291,
        "max_drawdown": 1946.0032710449304,
        "max_drawdown_pct": 14.95480300437003,
        "intrabar_max_drawdown": 1945.0476308704729,
        "intrabar_max_drawdown_pct": 14.992080020911361,
        "tp1_rate": 46.15384615384615,
        "tp2_rate": 23.076923076923077,
        "stop_rate": 76.92307692307693,
        "fee_drag": 105.89483149822686,
        "tail_max_loss": -132.30367416650486,
        "cagr": 19.988004701576934,
        "sharpe": 0.9252802389224751,
        "sortino": 0.9168365488139123,
        "exposure_pct": 58.10945273631841,
        "turnover": 8.632422613030549,
        "sample_sufficient": true,
        "sample_warning": ""
      }
    },
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-07-26\\abtest_dynamic_universe_atr_reclaim_0_35_2025-06-01_2026-06-01_v1.md",
      "start": "2025-06-01",
      "end": "2026-06-01",
      "sample_sufficient": true,
      "dynamic_metadata": {
        "baseline_master_count": "418",
        "variant_master_count": "418",
        "baseline_source_limit": "None",
        "variant_source_limit": "None",
        "baseline_universe_refreshes": "366",
        "variant_universe_refreshes": "366"
      },
      "baseline": {
        "trades": 389,
        "closed_trades": 57,
        "open_trades": 1,
        "win_rate": 40.35087719298245,
        "profit_factor": 1.1084402273665406,
        "avg_r": 0.07747588342292856,
        "net_return_pct": 3.1141295724147033,
        "max_drawdown": 2525.3293105807606,
        "max_drawdown_pct": 20.747383669162712,
        "intrabar_max_drawdown": 2469.7095471564644,
        "intrabar_max_drawdown_pct": 20.444094626200286,
        "tp1_rate": 40.35087719298245,
        "tp2_rate": 14.035087719298245,
        "stop_rate": 85.96491228070175,
        "fee_drag": 105.0726162312896,
        "tail_max_loss": -123.90935785436643,
        "cagr": 3.1141295724147033,
        "sharpe": 0.26428487207953116,
        "sortino": 0.2641862069291116,
        "exposure_pct": 52.10045662100457,
        "turnover": 8.181889958857594,
        "sample_sufficient": true,
        "sample_warning": ""
      },
      "variant": {
        "trades": 391,
        "closed_trades": 53,
        "open_trades": 1,
        "win_rate": 45.28301886792453,
        "profit_factor": 1.3055013700143936,
        "avg_r": 0.20720624210252425,
        "net_return_pct": 9.325520715913749,
        "max_drawdown": 1868.0687015803978,
        "max_drawdown_pct": 15.270875195966363,
        "intrabar_max_drawdown": 1807.0190831415784,
        "intrabar_max_drawdown_pct": 14.88533037369763,
        "tp1_rate": 43.39622641509434,
        "tp2_rate": 15.09433962264151,
        "stop_rate": 84.90566037735849,
        "fee_drag": 97.08803424170499,
        "tail_max_loss": -125.52757514928477,
        "cagr": 9.325520715913749,
        "sharpe": 0.601985904511637,
        "sortino": 0.6112667042681229,
        "exposure_pct": 52.054794520547944,
        "turnover": 7.470896191334832,
        "sample_sufficient": true,
        "sample_warning": ""
      }
    }
  ]
}
```
