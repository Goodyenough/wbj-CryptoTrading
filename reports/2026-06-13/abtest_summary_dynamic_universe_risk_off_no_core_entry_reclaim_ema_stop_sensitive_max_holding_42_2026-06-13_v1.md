---
created: 2026-06-13 23:35:43 CST
tags:
  - crypto
  - trading-system
  - abtest-summary
experiment_id: risk_off_no_core_entry_reclaim_ema_stop_sensitive_max_holding_42
mode: dynamic_universe
periods: 2
sufficient_periods: 2
unique_coverage_days: 700
overlap_periods: 0
universe_warnings: 1
verdict: retest
report_version: v1
---

# A/B 多时段汇总 risk_off_no_core_entry_reclaim_ema_stop_sensitive_max_holding_42 v1

- experiment_id: `risk_off_no_core_entry_reclaim_ema_stop_sensitive_max_holding_42`
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
| 2024-07-01 -> 2025-06-01 | yes | 76.00 -> 134.00 | 39.47% -> 50.00% | 1.04 -> 1.48 | 0.23 -> 1.31 | 18.03% -> 20.66% | 2.37% -> 31.86% | 84.21% -> 50.00% | retest |
| 2025-06-01 -> 2026-06-01 | yes | 57.00 -> 110.00 | 40.35% -> 47.27% | 1.11 -> 1.31 | 0.26 -> 0.86 | 20.74% -> 11.05% | 3.12% -> 15.95% | 85.96% -> 45.45% | retest |

## Universe Bias Checks

- Dynamic universe uses current Binance exchangeInfo as the symbol master; historic delisted symbols may be missing.

## Source Reports

- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-13\abtest_dynamic_universe_risk_off_no_core_entry_reclaim_ema_stop_sensitive_max_holding_42_2024-07-01_2025-06-01_v1.md`
- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-13\abtest_dynamic_universe_risk_off_no_core_entry_reclaim_ema_stop_sensitive_max_holding_42_2025-06-01_2026-06-01_v1.md`

## Decision Rule

- 汇总报告只给出 `candidate_keep_review`、`retest` 或 `reject_candidate`，不会自动修改默认配置。
- 至少需要多个充足样本时段共同改善净收益、Profit factor 和最大回撤，才会标记 `candidate_keep_review`。
- 时段存在重叠时，证据不视为完全独立，结论保持 `retest`。
- 任一 variant 样本不足时，结论应偏向 `retest`。

## Raw Summary

```json
{
  "experiment_id": "risk_off_no_core_entry_reclaim_ema_stop_sensitive_max_holding_42",
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
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-13\\abtest_dynamic_universe_risk_off_no_core_entry_reclaim_ema_stop_sensitive_max_holding_42_2024-07-01_2025-06-01_v1.md",
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
      }
    },
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-13\\abtest_dynamic_universe_risk_off_no_core_entry_reclaim_ema_stop_sensitive_max_holding_42_2025-06-01_2026-06-01_v1.md",
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
      }
    }
  ]
}
```
