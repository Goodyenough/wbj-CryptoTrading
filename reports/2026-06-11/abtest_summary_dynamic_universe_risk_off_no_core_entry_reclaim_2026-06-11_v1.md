---
created: 2026-06-11 00:43:28 CST
tags:
  - crypto
  - trading-system
  - abtest-summary
experiment_id: risk_off_no_core_entry_reclaim
mode: dynamic_universe
periods: 2
sufficient_periods: 2
unique_coverage_days: 700
overlap_periods: 0
universe_warnings: 1
verdict: candidate_keep_review
report_version: v1
---

# A/B 多时段汇总 risk_off_no_core_entry_reclaim v1

- experiment_id: `risk_off_no_core_entry_reclaim`
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
| 2024-07-01 -> 2025-06-01 | yes | 52.00 -> 41.00 | 26.92% -> 36.59% | 0.91 -> 1.40 | -0.25 -> 0.79 | 18.72% -> 14.31% | -5.59% -> 11.74% | 73.08% -> 63.41% | retest |
| 2025-06-01 -> 2026-06-01 | yes | 49.00 -> 46.00 | 22.45% -> 32.61% | 0.73 -> 1.20 | -0.54 -> 0.41 | 24.24% -> 14.46% | -10.62% -> 5.96% | 77.55% -> 67.39% | retest |

## Universe Bias Checks

- Dynamic universe uses current Binance exchangeInfo as the symbol master; historic delisted symbols may be missing.

## Source Reports

- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-10\abtest_dynamic_universe_risk_off_no_core_entry_reclaim_2024-07-01_2025-06-01_v1.md`
- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-11\abtest_dynamic_universe_risk_off_no_core_entry_reclaim_2025-06-01_2026-06-01_v1.md`

## Decision Rule

- 汇总报告只给出 `candidate_keep_review`、`retest` 或 `reject_candidate`，不会自动修改默认配置。
- 至少需要多个充足样本时段共同改善净收益、Profit factor 和最大回撤，才会标记 `candidate_keep_review`。
- 时段存在重叠时，证据不视为完全独立，结论保持 `retest`。
- 任一 variant 样本不足时，结论应偏向 `retest`。

## Raw Summary

```json
{
  "experiment_id": "risk_off_no_core_entry_reclaim",
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
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-10\\abtest_dynamic_universe_risk_off_no_core_entry_reclaim_2024-07-01_2025-06-01_v1.md",
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
        "trades": 268,
        "closed_trades": 52,
        "open_trades": 3,
        "win_rate": 26.923076923076923,
        "profit_factor": 0.9102519918991828,
        "avg_r": -0.03041598140660157,
        "net_return_pct": -5.58688262495367,
        "max_drawdown": 2170.411957751381,
        "max_drawdown_pct": 18.723989057393542,
        "intrabar_max_drawdown": 2134.121253145846,
        "intrabar_max_drawdown_pct": 18.524093062530373,
        "tp1_rate": 28.846153846153843,
        "tp2_rate": 26.923076923076923,
        "stop_rate": 73.07692307692307,
        "fee_drag": 63.157877648175145,
        "tail_max_loss": -117.19916034615537,
        "cagr": -6.07170748632806,
        "sharpe": -0.2514497640138396,
        "sortino": -0.26403429151851554,
        "exposure_pct": 84.32835820895522,
        "turnover": 5.40397640114904,
        "sample_sufficient": true,
        "sample_warning": ""
      },
      "variant": {
        "trades": 265,
        "closed_trades": 41,
        "open_trades": 1,
        "win_rate": 36.58536585365854,
        "profit_factor": 1.4004450874222993,
        "avg_r": 0.3319523108886942,
        "net_return_pct": 11.735156461759999,
        "max_drawdown": 1864.5398527686066,
        "max_drawdown_pct": 14.30984660000843,
        "intrabar_max_drawdown": 1816.5855395568287,
        "intrabar_max_drawdown_pct": 14.011199228431433,
        "tp1_rate": 41.46341463414634,
        "tp2_rate": 36.58536585365854,
        "stop_rate": 63.41463414634146,
        "fee_drag": 57.47981609713977,
        "tail_max_loss": -134.40618262785378,
        "cagr": 12.850983848070353,
        "sharpe": 0.7916951964875444,
        "sortino": 0.7641755461013752,
        "exposure_pct": 55.472636815920396,
        "turnover": 4.931602662337832,
        "sample_sufficient": true,
        "sample_warning": ""
      }
    },
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-11\\abtest_dynamic_universe_risk_off_no_core_entry_reclaim_2025-06-01_2026-06-01_v1.md",
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
        "trades": 302,
        "closed_trades": 49,
        "open_trades": 3,
        "win_rate": 22.448979591836736,
        "profit_factor": 0.7335465870648034,
        "avg_r": -0.19820595721035383,
        "net_return_pct": -10.621034473218582,
        "max_drawdown": 2722.4137887098896,
        "max_drawdown_pct": 24.239993862312907,
        "intrabar_max_drawdown": 2681.5476646191437,
        "intrabar_max_drawdown_pct": 23.993723782285777,
        "tp1_rate": 32.6530612244898,
        "tp2_rate": 22.448979591836736,
        "stop_rate": 77.55102040816327,
        "fee_drag": 81.52972337365311,
        "tail_max_loss": -114.93804751814146,
        "cagr": -10.621034473218582,
        "sharpe": -0.5445715158743036,
        "sortino": -0.655090699515348,
        "exposure_pct": 88.44748858447488,
        "turnover": 6.79780742067835,
        "sample_sufficient": true,
        "sample_warning": ""
      },
      "variant": {
        "trades": 295,
        "closed_trades": 46,
        "open_trades": 2,
        "win_rate": 32.608695652173914,
        "profit_factor": 1.2035621117782322,
        "avg_r": 0.1731014149881459,
        "net_return_pct": 5.964175449661768,
        "max_drawdown": 1728.0874477479192,
        "max_drawdown_pct": 14.458855015307304,
        "intrabar_max_drawdown": 1744.5480611850817,
        "intrabar_max_drawdown_pct": 14.621397706857206,
        "tp1_rate": 41.30434782608695,
        "tp2_rate": 32.608695652173914,
        "stop_rate": 67.3913043478261,
        "fee_drag": 78.40417238272816,
        "tail_max_loss": -127.19582036968083,
        "cagr": 5.964175449661768,
        "sharpe": 0.4074368697335161,
        "sortino": 0.4345880175063331,
        "exposure_pct": 62.694063926940636,
        "turnover": 6.906752392418545,
        "sample_sufficient": true,
        "sample_warning": ""
      }
    }
  ]
}
```
