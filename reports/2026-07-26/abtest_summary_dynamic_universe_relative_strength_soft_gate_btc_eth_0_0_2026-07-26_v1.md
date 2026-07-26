---
created: 2026-07-26 12:18:22 CST
tags:
  - crypto
  - trading-system
  - abtest-summary
experiment_id: relative_strength_soft_gate_btc_eth_0_0
mode: dynamic_universe
periods: 2
sufficient_periods: 2
unique_coverage_days: 700
overlap_periods: 0
universe_warnings: 1
verdict: retest
report_version: v1
---

# A/B 多时段汇总 relative_strength_soft_gate_btc_eth_0_0 v1

- experiment_id: `relative_strength_soft_gate_btc_eth_0_0`
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
| 2024-07-01 -> 2025-06-01 | yes | 76.00 -> 82.00 | 38.16% -> 39.02% | 0.95 -> 1.02 | -0.01 -> 0.13 | 16.59% -> 20.58% | -2.09% -> 0.41% | 89.47% -> 84.15% | retest |
| 2025-06-01 -> 2026-06-01 | yes | 57.00 -> 51.00 | 40.35% -> 43.14% | 1.11 -> 1.35 | 0.26 -> 0.68 | 20.75% -> 14.19% | 3.11% -> 10.67% | 85.96% -> 80.39% | retest |

## Universe Bias Checks

- Dynamic universe uses current Binance exchangeInfo as the symbol master; historic delisted symbols may be missing.

## Source Reports

- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-07-26\abtest_dynamic_universe_relative_strength_soft_gate_btc_eth_0_0_2024-07-01_2025-06-01_v1.md`
- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-07-26\abtest_dynamic_universe_relative_strength_soft_gate_btc_eth_0_0_2025-06-01_2026-06-01_v1.md`

## Decision Rule

- 汇总报告只给出 `candidate_keep_review`、`retest` 或 `reject_candidate`，不会自动修改默认配置。
- 至少需要多个充足样本时段共同改善净收益、Profit factor 和最大回撤，才会标记 `candidate_keep_review`。
- 时段存在重叠时，证据不视为完全独立，结论保持 `retest`。
- 任一 variant 样本不足时，结论应偏向 `retest`。

## Raw Summary

```json
{
  "experiment_id": "relative_strength_soft_gate_btc_eth_0_0",
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
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-07-26\\abtest_dynamic_universe_relative_strength_soft_gate_btc_eth_0_0_2024-07-01_2025-06-01_v1.md",
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
        "trades": 470,
        "closed_trades": 82,
        "open_trades": 1,
        "win_rate": 39.02439024390244,
        "profit_factor": 1.0166140177773986,
        "avg_r": 0.04000966139840584,
        "net_return_pct": 0.4087427371820995,
        "max_drawdown": 2599.403303257035,
        "max_drawdown_pct": 20.576057085808124,
        "intrabar_max_drawdown": 2527.939444627342,
        "intrabar_max_drawdown_pct": 20.147087888195664,
        "tp1_rate": 34.146341463414636,
        "tp2_rate": 15.853658536585366,
        "stop_rate": 84.14634146341463,
        "fee_drag": 118.26255587511683,
        "tail_max_loss": -127.04353417714013,
        "cagr": 0.44542797042645965,
        "sharpe": 0.12610289516436943,
        "sortino": 0.12384156736372436,
        "exposure_pct": 53.6318407960199,
        "turnover": 9.191455481513316,
        "sample_sufficient": true,
        "sample_warning": ""
      }
    },
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-07-26\\abtest_dynamic_universe_relative_strength_soft_gate_btc_eth_0_0_2025-06-01_2026-06-01_v1.md",
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
        "trades": 361,
        "closed_trades": 51,
        "open_trades": 1,
        "win_rate": 43.13725490196079,
        "profit_factor": 1.3502844705939774,
        "avg_r": 0.22201660162700917,
        "net_return_pct": 10.671198676711535,
        "max_drawdown": 1770.4839242166836,
        "max_drawdown_pct": 14.18860702922134,
        "intrabar_max_drawdown": 1688.3507421761515,
        "intrabar_max_drawdown_pct": 13.663930276180892,
        "tp1_rate": 43.13725490196079,
        "tp2_rate": 19.607843137254903,
        "stop_rate": 80.3921568627451,
        "fee_drag": 90.24641263603885,
        "tail_max_loss": -126.25830839542141,
        "cagr": 10.671198676711535,
        "sharpe": 0.6783713448020497,
        "sortino": 0.6892409055380946,
        "exposure_pct": 49.45205479452055,
        "turnover": 7.311623877080637,
        "sample_sufficient": true,
        "sample_warning": ""
      }
    }
  ]
}
```
