---
created: 2026-06-16 00:06:32 CST
tags:
  - crypto
  - trading-system
  - abtest-summary
experiment_id: max_holding_42_fixed_vs_conditional_sensitive
mode: dynamic_universe
periods: 2
sufficient_periods: 2
unique_coverage_days: 700
overlap_periods: 0
universe_warnings: 1
verdict: retest
report_version: v1
---

# A/B 多时段汇总 max_holding_42_fixed_vs_conditional_sensitive v1

- experiment_id: `max_holding_42_fixed_vs_conditional_sensitive`
- mode: `dynamic_universe`
- periods: 2
- sufficient_periods: 2
- total_period_days: 700
- unique_coverage_days: 700
- overlap_periods: 0
- universe_warnings: 1
- net_improved_periods: 1
- profit_factor_improved_periods: 1
- drawdown_improved_periods: 0
- variant_under_sample_periods: 0
- verdict: `retest`
- reason: Results are mixed or sample coverage is incomplete; continue cross-period testing.

## Period Results

| Period | Sample | Closed B -> V | Win B -> V | PF B -> V | Sharpe B -> V | MDD B -> V | Net B -> V | Stop B -> V | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 2024-07-01 -> 2025-06-01 | yes | 134.00 -> 134.00 | 50.00% -> 44.78% | 1.48 -> 1.38 | 1.31 -> 1.21 | 20.66% -> 21.04% | 31.86% -> 27.57% | 50.00% -> 54.48% | reject_candidate |
| 2025-06-01 -> 2026-06-01 | yes | 110.00 -> 110.00 | 47.27% -> 49.09% | 1.31 -> 1.64 | 0.86 -> 1.42 | 11.05% -> 12.40% | 15.95% -> 30.75% | 45.45% -> 47.27% | retest |

## Universe Bias Checks

- Dynamic universe uses current Binance exchangeInfo as the symbol master; historic delisted symbols may be missing.

## Source Reports

- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-15\abtest_dynamic_universe_max_holding_42_fixed_vs_conditional_sensitive_2024-07-01_2025-06-01_v1.md`
- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-16\abtest_dynamic_universe_max_holding_42_fixed_vs_conditional_sensitive_2025-06-01_2026-06-01_v1.md`

## Decision Rule

- 汇总报告只给出 `candidate_keep_review`、`retest` 或 `reject_candidate`，不会自动修改默认配置。
- 至少需要多个充足样本时段共同改善净收益、Profit factor 和最大回撤，才会标记 `candidate_keep_review`。
- 时段存在重叠时，证据不视为完全独立，结论保持 `retest`。
- 任一 variant 样本不足时，结论应偏向 `retest`。

## Raw Summary

```json
{
  "experiment_id": "max_holding_42_fixed_vs_conditional_sensitive",
  "mode": "dynamic_universe",
  "periods": 2,
  "sufficient_periods": 2,
  "total_period_days": 700,
  "unique_coverage_days": 700,
  "overlap_periods": 0,
  "universe_warnings": [
    "Dynamic universe uses current Binance exchangeInfo as the symbol master; historic delisted symbols may be missing."
  ],
  "net_improved_periods": 1,
  "profit_factor_improved_periods": 1,
  "drawdown_improved_periods": 0,
  "variant_under_sample_periods": 0,
  "verdict": "retest",
  "reason": "Results are mixed or sample coverage is incomplete; continue cross-period testing.",
  "records": [
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-15\\abtest_dynamic_universe_max_holding_42_fixed_vs_conditional_sensitive_2024-07-01_2025-06-01_v1.md",
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
        "trades": 517,
        "closed_trades": 134,
        "open_trades": 1,
        "win_rate": 50.0,
        "profit_factor": 1.4772889936794513,
        "avg_r": 0.23463119542659508,
        "net_return_pct": 31.86163369853203,
        "max_drawdown": 3111.8035593343884,
        "max_drawdown_pct": 20.664890308577046,
        "intrabar_max_drawdown": 3032.612877964919,
        "intrabar_max_drawdown_pct": 20.317727161402804,
        "tp1_rate": 26.119402985074625,
        "tp2_rate": 15.671641791044777,
        "stop_rate": 50.0,
        "fee_drag": 213.29587140645714,
        "tail_max_loss": -154.51965211599236,
        "cagr": 35.16844836488411,
        "sharpe": 1.3113863698379893,
        "sortino": 1.3728979794973917,
        "exposure_pct": 49.45273631840796,
        "turnover": 16.396929485728936,
        "sample_sufficient": true,
        "sample_warning": ""
      },
      "variant": {
        "trades": 509,
        "closed_trades": 134,
        "open_trades": 2,
        "win_rate": 44.776119402985074,
        "profit_factor": 1.3834024649299093,
        "avg_r": 0.2192827966155529,
        "net_return_pct": 27.566124401278213,
        "max_drawdown": 3304.0871569578176,
        "max_drawdown_pct": 21.036699067084808,
        "intrabar_max_drawdown": 3321.1856934797997,
        "intrabar_max_drawdown_pct": 21.1935522642374,
        "tp1_rate": 28.35820895522388,
        "tp2_rate": 17.16417910447761,
        "stop_rate": 54.47761194029851,
        "fee_drag": 214.66713715208633,
        "tail_max_loss": -161.24764139223754,
        "cagr": 30.377965489741456,
        "sharpe": 1.2118979697287446,
        "sortino": 1.2714310148783572,
        "exposure_pct": 49.1044776119403,
        "turnover": 16.82072099965837,
        "sample_sufficient": true,
        "sample_warning": ""
      }
    },
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-16\\abtest_dynamic_universe_max_holding_42_fixed_vs_conditional_sensitive_2025-06-01_2026-06-01_v1.md",
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
        "trades": 420,
        "closed_trades": 110,
        "open_trades": 0,
        "win_rate": 47.27272727272727,
        "profit_factor": 1.3059024523904943,
        "avg_r": 0.13993761855138268,
        "net_return_pct": 15.952179063721816,
        "max_drawdown": 1440.2376078873458,
        "max_drawdown_pct": 11.048617413575347,
        "intrabar_max_drawdown": 1378.523343873545,
        "intrabar_max_drawdown_pct": 10.633205341510301,
        "tp1_rate": 23.636363636363637,
        "tp2_rate": 10.0,
        "stop_rate": 45.45454545454545,
        "fee_drag": 226.2909522685009,
        "tail_max_loss": -136.29446478019682,
        "cagr": 15.952179063721816,
        "sharpe": 0.8622627060204072,
        "sortino": 0.8119790621570393,
        "exposure_pct": 41.0958904109589,
        "turnover": 16.81189338134064,
        "sample_sufficient": true,
        "sample_warning": ""
      },
      "variant": {
        "trades": 412,
        "closed_trades": 110,
        "open_trades": 0,
        "win_rate": 49.09090909090909,
        "profit_factor": 1.6407641522492014,
        "avg_r": 0.24936555757028067,
        "net_return_pct": 30.751258496645704,
        "max_drawdown": 1661.6492219931952,
        "max_drawdown_pct": 12.395966795962835,
        "intrabar_max_drawdown": 1582.5345183775153,
        "intrabar_max_drawdown_pct": 11.89526286058767,
        "tp1_rate": 30.909090909090907,
        "tp2_rate": 12.727272727272727,
        "stop_rate": 47.27272727272727,
        "fee_drag": 236.41352153652204,
        "tail_max_loss": -139.7047391114886,
        "cagr": 30.751258496645704,
        "sharpe": 1.4189399641399831,
        "sortino": 1.3478753836075588,
        "exposure_pct": 41.41552511415525,
        "turnover": 17.701298877378118,
        "sample_sufficient": true,
        "sample_warning": ""
      }
    }
  ]
}
```
