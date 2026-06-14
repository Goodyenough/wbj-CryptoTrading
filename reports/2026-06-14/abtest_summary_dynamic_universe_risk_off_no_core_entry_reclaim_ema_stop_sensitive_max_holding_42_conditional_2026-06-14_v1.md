---
created: 2026-06-14 22:44:29 CST
tags:
  - crypto
  - trading-system
  - abtest-summary
experiment_id: risk_off_no_core_entry_reclaim_ema_stop_sensitive_max_holding_42_conditional
mode: dynamic_universe
periods: 2
sufficient_periods: 2
unique_coverage_days: 700
overlap_periods: 0
universe_warnings: 1
verdict: retest
report_version: v1
---

# A/B 多时段汇总 risk_off_no_core_entry_reclaim_ema_stop_sensitive_max_holding_42_conditional v1

- experiment_id: `risk_off_no_core_entry_reclaim_ema_stop_sensitive_max_holding_42_conditional`
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
| 2024-07-01 -> 2025-06-01 | yes | 76.00 -> 134.00 | 39.47% -> 44.78% | 1.04 -> 1.38 | 0.23 -> 1.21 | 18.03% -> 21.04% | 2.37% -> 27.57% | 84.21% -> 54.48% | retest |
| 2025-06-01 -> 2026-06-01 | yes | 57.00 -> 110.00 | 40.35% -> 49.09% | 1.11 -> 1.64 | 0.26 -> 1.42 | 20.74% -> 12.40% | 3.12% -> 30.75% | 85.96% -> 47.27% | retest |

## Universe Bias Checks

- Dynamic universe uses current Binance exchangeInfo as the symbol master; historic delisted symbols may be missing.

## Source Reports

- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-14\abtest_dynamic_universe_risk_off_no_core_entry_reclaim_ema_stop_sensitive_max_holding_42_conditional_2024-07-01_2025-06-01_v1.md`
- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-14\abtest_dynamic_universe_risk_off_no_core_entry_reclaim_ema_stop_sensitive_max_holding_42_conditional_2025-06-01_2026-06-01_v1.md`

## Decision Rule

- 汇总报告只给出 `candidate_keep_review`、`retest` 或 `reject_candidate`，不会自动修改默认配置。
- 至少需要多个充足样本时段共同改善净收益、Profit factor 和最大回撤，才会标记 `candidate_keep_review`。
- 时段存在重叠时，证据不视为完全独立，结论保持 `retest`。
- 任一 variant 样本不足时，结论应偏向 `retest`。

## Raw Summary

```json
{
  "experiment_id": "risk_off_no_core_entry_reclaim_ema_stop_sensitive_max_holding_42_conditional",
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
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-14\\abtest_dynamic_universe_risk_off_no_core_entry_reclaim_ema_stop_sensitive_max_holding_42_conditional_2024-07-01_2025-06-01_v1.md",
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
        "trades": 485,
        "closed_trades": 76,
        "open_trades": 2,
        "win_rate": 39.473684210526315,
        "profit_factor": 1.0411923323301147,
        "avg_r": 0.05373777931702029,
        "net_return_pct": 2.3729263053924754,
        "max_drawdown": 2212.1967817971527,
        "max_drawdown_pct": 18.028416779537018,
        "intrabar_max_drawdown": 2197.2914025629125,
        "intrabar_max_drawdown_pct": 18.003671158121552,
        "tp1_rate": 35.526315789473685,
        "tp2_rate": 15.789473684210526,
        "stop_rate": 84.21052631578947,
        "fee_drag": 102.77647716231616,
        "tail_max_loss": -127.503998102125,
        "cagr": 2.5881546347458206,
        "sharpe": 0.2271908474647652,
        "sortino": 0.2296661576935706,
        "exposure_pct": 60.447761194029844,
        "turnover": 7.968600046919312,
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
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-14\\abtest_dynamic_universe_risk_off_no_core_entry_reclaim_ema_stop_sensitive_max_holding_42_conditional_2025-06-01_2026-06-01_v1.md",
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
        "trades": 387,
        "closed_trades": 57,
        "open_trades": 1,
        "win_rate": 40.35087719298245,
        "profit_factor": 1.1085498859208813,
        "avg_r": 0.07746094957893503,
        "net_return_pct": 3.117817201675166,
        "max_drawdown": 2524.9843278450226,
        "max_drawdown_pct": 20.744549389630293,
        "intrabar_max_drawdown": 2469.365847187475,
        "intrabar_max_drawdown_pct": 20.44124950026346,
        "tp1_rate": 40.35087719298245,
        "tp2_rate": 14.035087719298245,
        "stop_rate": 85.96491228070175,
        "fee_drag": 105.13122209926844,
        "tail_max_loss": -123.90935785436643,
        "cagr": 3.117817201675166,
        "sharpe": 0.26457611778930706,
        "sortino": 0.264007827957292,
        "exposure_pct": 52.10045662100457,
        "turnover": 8.18605489886344,
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
