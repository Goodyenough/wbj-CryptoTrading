---
created: 2026-07-26 00:37:46 CST
tags:
  - crypto
  - trading-system
  - abtest-summary
experiment_id: relative_strength_soft_gate_btc_eth_minus_0_5
mode: dynamic_universe
periods: 2
sufficient_periods: 2
unique_coverage_days: 700
overlap_periods: 0
universe_warnings: 1
verdict: retest
report_version: v1
---

# A/B 多时段汇总 relative_strength_soft_gate_btc_eth_minus_0_5 v1

- experiment_id: `relative_strength_soft_gate_btc_eth_minus_0_5`
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
| 2024-07-01 -> 2025-06-01 | yes | 76.00 -> 87.00 | 38.16% -> 43.68% | 0.95 -> 1.09 | -0.01 -> 0.39 | 16.59% -> 18.96% | -2.09% -> 5.63% | 89.47% -> 87.36% | retest |
| 2025-06-01 -> 2026-06-01 | yes | 57.00 -> 51.00 | 40.35% -> 41.18% | 1.11 -> 1.27 | 0.26 -> 0.54 | 20.75% -> 15.46% | 3.11% -> 7.88% | 85.96% -> 80.39% | retest |

## Universe Bias Checks

- Dynamic universe uses current Binance exchangeInfo as the symbol master; historic delisted symbols may be missing.

## Source Reports

- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-07-26\abtest_dynamic_universe_relative_strength_soft_gate_btc_eth_minus_0_5_2024-07-01_2025-06-01_v1.md`
- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-07-26\abtest_dynamic_universe_relative_strength_soft_gate_btc_eth_minus_0_5_2025-06-01_2026-06-01_v1.md`

## Decision Rule

- 汇总报告只给出 `candidate_keep_review`、`retest` 或 `reject_candidate`，不会自动修改默认配置。
- 至少需要多个充足样本时段共同改善净收益、Profit factor 和最大回撤，才会标记 `candidate_keep_review`。
- 时段存在重叠时，证据不视为完全独立，结论保持 `retest`。
- 任一 variant 样本不足时，结论应偏向 `retest`。

## Raw Summary

```json
{
  "experiment_id": "relative_strength_soft_gate_btc_eth_minus_0_5",
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
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-07-26\\abtest_dynamic_universe_relative_strength_soft_gate_btc_eth_minus_0_5_2024-07-01_2025-06-01_v1.md",
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
        "trades": 474,
        "closed_trades": 87,
        "open_trades": 2,
        "win_rate": 43.67816091954023,
        "profit_factor": 1.0920778401183997,
        "avg_r": 0.08482191050831794,
        "net_return_pct": 5.6258137621480575,
        "max_drawdown": 2471.139523396272,
        "max_drawdown_pct": 18.959586003333936,
        "intrabar_max_drawdown": 2424.6366249994517,
        "intrabar_max_drawdown_pct": 18.737600067152883,
        "tp1_rate": 40.229885057471265,
        "tp2_rate": 12.643678160919542,
        "stop_rate": 87.35632183908046,
        "fee_drag": 124.56767116685856,
        "tail_max_loss": -132.22189914178136,
        "cagr": 6.144801852640036,
        "sharpe": 0.3857557180163554,
        "sortino": 0.41071136803734715,
        "exposure_pct": 57.76119402985075,
        "turnover": 9.626472897378264,
        "sample_sufficient": true,
        "sample_warning": ""
      }
    },
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-07-26\\abtest_dynamic_universe_relative_strength_soft_gate_btc_eth_minus_0_5_2025-06-01_2026-06-01_v1.md",
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
        "trades": 380,
        "closed_trades": 51,
        "open_trades": 1,
        "win_rate": 41.17647058823529,
        "profit_factor": 1.2682894018580873,
        "avg_r": 0.17569164585978217,
        "net_return_pct": 7.878770480803743,
        "max_drawdown": 1845.1621148532795,
        "max_drawdown_pct": 15.456849345119839,
        "intrabar_max_drawdown": 1749.454955723053,
        "intrabar_max_drawdown_pct": 14.820525606852952,
        "tp1_rate": 41.17647058823529,
        "tp2_rate": 19.607843137254903,
        "stop_rate": 80.3921568627451,
        "fee_drag": 90.53990495196874,
        "tail_max_loss": -122.8148108181206,
        "cagr": 7.878770480803743,
        "sharpe": 0.5428414623245448,
        "sortino": 0.5415942447758602,
        "exposure_pct": 52.10045662100457,
        "turnover": 7.236542937845933,
        "sample_sufficient": true,
        "sample_warning": ""
      }
    }
  ]
}
```
