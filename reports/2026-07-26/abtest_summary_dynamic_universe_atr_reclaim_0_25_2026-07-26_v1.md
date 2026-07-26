---
created: 2026-07-26 15:40:08 CST
tags:
  - crypto
  - trading-system
  - abtest-summary
experiment_id: atr_reclaim_0_25
mode: dynamic_universe
periods: 2
sufficient_periods: 2
unique_coverage_days: 700
overlap_periods: 0
universe_warnings: 1
verdict: retest
report_version: v1
---

# A/B 多时段汇总 atr_reclaim_0_25 v1

- experiment_id: `atr_reclaim_0_25`
- mode: `dynamic_universe`
- periods: 2
- sufficient_periods: 2
- total_period_days: 700
- unique_coverage_days: 700
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
| 2024-07-01 -> 2025-06-01 | yes | 76.00 -> 79.00 | 38.16% -> 43.04% | 0.95 -> 1.34 | -0.01 -> 0.41 | 16.59% -> 19.21% | -2.09% -> 6.32% | 89.47% -> 78.48% | retest |
| 2025-06-01 -> 2026-06-01 | yes | 57.00 -> 54.00 | 40.35% -> 44.44% | 1.11 -> 1.24 | 0.26 -> 0.50 | 20.75% -> 15.01% | 3.11% -> 7.20% | 85.96% -> 87.04% | retest |

## Universe Bias Checks

- Dynamic universe uses current Binance exchangeInfo as the symbol master; historic delisted symbols may be missing.

## Source Reports

- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-07-26\abtest_dynamic_universe_atr_reclaim_0_25_2024-07-01_2025-06-01_v1.md`
- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-07-26\abtest_dynamic_universe_atr_reclaim_0_25_2025-06-01_2026-06-01_v1.md`

## Decision Rule

- 汇总报告只给出 `candidate_keep_review`、`retest` 或 `reject_candidate`，不会自动修改默认配置。
- 至少需要多个充足样本时段共同改善净收益、Profit factor 和最大回撤，才会标记 `candidate_keep_review`。
- 时段存在重叠时，证据不视为完全独立，结论保持 `retest`。
- 任一 variant 样本不足时，结论应偏向 `retest`。

## Raw Summary

```json
{
  "experiment_id": "atr_reclaim_0_25",
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
  "drawdown_improved_periods": 1,
  "variant_under_sample_periods": 0,
  "verdict": "retest",
  "reason": "Results are mixed or sample coverage is incomplete; continue cross-period testing.",
  "records": [
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-07-26\\abtest_dynamic_universe_atr_reclaim_0_25_2024-07-01_2025-06-01_v1.md",
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
        "trades": 491,
        "closed_trades": 79,
        "open_trades": 4,
        "win_rate": 43.037974683544306,
        "profit_factor": 1.3416857466069145,
        "avg_r": 0.2417059599177341,
        "net_return_pct": 6.320378038301344,
        "max_drawdown": 2447.523966683355,
        "max_drawdown_pct": 19.209520618361005,
        "intrabar_max_drawdown": 2434.0643264975406,
        "intrabar_max_drawdown_pct": 19.193290690007846,
        "tp1_rate": 39.24050632911392,
        "tp2_rate": 21.518987341772153,
        "stop_rate": 78.48101265822784,
        "fee_drag": 105.6489974765393,
        "tail_max_loss": -131.54495423056085,
        "cagr": 6.905507710678793,
        "sharpe": 0.4130429596091996,
        "sortino": 0.36930134028547257,
        "exposure_pct": 51.592039800995025,
        "turnover": 8.677213768179799,
        "sample_sufficient": true,
        "sample_warning": ""
      }
    },
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-07-26\\abtest_dynamic_universe_atr_reclaim_0_25_2025-06-01_2026-06-01_v1.md",
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
        "trades": 390,
        "closed_trades": 54,
        "open_trades": 1,
        "win_rate": 44.44444444444444,
        "profit_factor": 1.2390824180094262,
        "avg_r": 0.16861157946971297,
        "net_return_pct": 7.20350091758597,
        "max_drawdown": 1782.910484010008,
        "max_drawdown_pct": 15.01286802029666,
        "intrabar_max_drawdown": 1710.0378406198652,
        "intrabar_max_drawdown_pct": 14.534365154882781,
        "tp1_rate": 42.592592592592595,
        "tp2_rate": 12.962962962962962,
        "stop_rate": 87.03703703703704,
        "fee_drag": 109.80907633363817,
        "tail_max_loss": -121.22499351113062,
        "cagr": 7.20350091758597,
        "sharpe": 0.49766640808971846,
        "sortino": 0.491031472642839,
        "exposure_pct": 52.054794520547944,
        "turnover": 8.351773535894994,
        "sample_sufficient": true,
        "sample_warning": ""
      }
    }
  ]
}
```
