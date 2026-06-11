---
created: 2026-06-11 10:51:52 CST
tags:
  - crypto
  - trading-system
  - abtest-summary
experiment_id: risk_off_no_core_entry_reclaim_ema_stop
mode: dynamic_universe
periods: 2
sufficient_periods: 2
unique_coverage_days: 700
overlap_periods: 0
universe_warnings: 1
verdict: candidate_keep_review
report_version: v1
---

# A/B 多时段汇总 risk_off_no_core_entry_reclaim_ema_stop v1

- experiment_id: `risk_off_no_core_entry_reclaim_ema_stop`
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
| 2024-07-01 -> 2025-06-01 | yes | 52.00 -> 50.00 | 26.92% -> 46.00% | 0.91 -> 1.53 | -0.25 -> 1.07 | 18.72% -> 14.99% | -5.59% -> 16.74% | 73.08% -> 76.00% | retest |
| 2025-06-01 -> 2026-06-01 | yes | 49.00 -> 64.00 | 22.45% -> 39.06% | 0.73 -> 1.05 | -0.54 -> 0.16 | 24.24% -> 18.68% | -10.62% -> 1.21% | 77.55% -> 84.38% | retest |

## Universe Bias Checks

- Dynamic universe uses current Binance exchangeInfo as the symbol master; historic delisted symbols may be missing.

## Source Reports

- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-11\abtest_dynamic_universe_risk_off_no_core_entry_reclaim_ema_stop_2024-07-01_2025-06-01_v1.md`
- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-11\abtest_dynamic_universe_risk_off_no_core_entry_reclaim_ema_stop_2025-06-01_2026-06-01_v1.md`

## Decision Rule

- 汇总报告只给出 `candidate_keep_review`、`retest` 或 `reject_candidate`，不会自动修改默认配置。
- 至少需要多个充足样本时段共同改善净收益、Profit factor 和最大回撤，才会标记 `candidate_keep_review`。
- 时段存在重叠时，证据不视为完全独立，结论保持 `retest`。
- 任一 variant 样本不足时，结论应偏向 `retest`。

## Raw Summary

```json
{
  "experiment_id": "risk_off_no_core_entry_reclaim_ema_stop",
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
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-11\\abtest_dynamic_universe_risk_off_no_core_entry_reclaim_ema_stop_2024-07-01_2025-06-01_v1.md",
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
        "trades": 275,
        "closed_trades": 50,
        "open_trades": 2,
        "win_rate": 46.0,
        "profit_factor": 1.5332795743713263,
        "avg_r": 0.36662282588341233,
        "net_return_pct": 16.738846268750795,
        "max_drawdown": 2038.4346155806052,
        "max_drawdown_pct": 14.986015173823777,
        "intrabar_max_drawdown": 2027.0393661859052,
        "intrabar_max_drawdown_pct": 14.976905291422815,
        "tp1_rate": 44.0,
        "tp2_rate": 24.0,
        "stop_rate": 76.0,
        "fee_drag": 83.84822786834879,
        "tail_max_loss": -138.9828427515564,
        "cagr": 18.36810261438655,
        "sharpe": 1.0701707559513816,
        "sortino": 1.039700208686137,
        "exposure_pct": 55.52238805970149,
        "turnover": 6.968354023808108,
        "sample_sufficient": true,
        "sample_warning": ""
      }
    },
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-11\\abtest_dynamic_universe_risk_off_no_core_entry_reclaim_ema_stop_2025-06-01_2026-06-01_v1.md",
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
        "trades": 305,
        "closed_trades": 64,
        "open_trades": 2,
        "win_rate": 39.0625,
        "profit_factor": 1.054075407061724,
        "avg_r": 0.03359222353431476,
        "net_return_pct": 1.2103012830104065,
        "max_drawdown": 2270.662236349366,
        "max_drawdown_pct": 18.682218162324542,
        "intrabar_max_drawdown": 2167.5497208433044,
        "intrabar_max_drawdown_pct": 18.039613460900206,
        "tp1_rate": 35.9375,
        "tp2_rate": 15.625,
        "stop_rate": 84.375,
        "fee_drag": 122.08300070147759,
        "tail_max_loss": -124.71346354298379,
        "cagr": 1.2103012830104065,
        "sharpe": 0.1562306021917604,
        "sortino": 0.1505456009625278,
        "exposure_pct": 47.89954337899543,
        "turnover": 9.610120695475208,
        "sample_sufficient": true,
        "sample_warning": ""
      }
    }
  ]
}
```
