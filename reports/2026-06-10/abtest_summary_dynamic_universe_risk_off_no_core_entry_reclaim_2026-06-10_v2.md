---
created: 2026-06-10 03:44:06 CST
tags:
  - crypto
  - trading-system
  - abtest-summary
experiment_id: risk_off_no_core_entry_reclaim
mode: dynamic_universe
periods: 2
sufficient_periods: 1
unique_coverage_days: 516
overlap_periods: 0
universe_warnings: 1
verdict: retest
report_version: v2
---

# A/B 多时段汇总 risk_off_no_core_entry_reclaim v2

- experiment_id: `risk_off_no_core_entry_reclaim`
- mode: `dynamic_universe`
- periods: 2
- sufficient_periods: 1
- total_period_days: 516
- unique_coverage_days: 516
- overlap_periods: 0
- universe_warnings: 1
- net_improved_periods: 1
- profit_factor_improved_periods: 1
- drawdown_improved_periods: 1
- variant_under_sample_periods: 1
- verdict: `retest`
- reason: At least one variant period is below the closed-trade sample threshold.

## Period Results

| Period | Sample | Closed B -> V | Win B -> V | PF B -> V | Sharpe B -> V | MDD B -> V | Net B -> V | Stop B -> V | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 2025-01-01 -> 2025-06-01 | no | 17.00 -> 15.00 | 11.76% -> 13.33% | 0.33 -> 0.41 | -2.23 -> -1.30 | 14.49% -> 10.85% | -11.80% -> -8.17% | 88.24% -> 86.67% | retest |
| 2025-06-01 -> 2026-06-01 | yes | 49.00 -> 46.00 | 22.45% -> 32.61% | 0.73 -> 1.20 | -0.54 -> 0.41 | 24.24% -> 14.46% | -10.62% -> 5.96% | 77.55% -> 67.39% | retest |

## Universe Bias Checks

- Dynamic universe uses current Binance exchangeInfo as the symbol master; historic delisted symbols may be missing.

## Source Reports

- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-10\abtest_dynamic_universe_risk_off_no_core_entry_reclaim_2025-01-01_2025-06-01_v1.md`
- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-10\abtest_dynamic_universe_risk_off_no_core_entry_reclaim_2025-06-01_2026-06-01_v1.md`

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
  "sufficient_periods": 1,
  "total_period_days": 516,
  "unique_coverage_days": 516,
  "overlap_periods": 0,
  "universe_warnings": [
    "Dynamic universe uses current Binance exchangeInfo as the symbol master; historic delisted symbols may be missing."
  ],
  "net_improved_periods": 1,
  "profit_factor_improved_periods": 1,
  "drawdown_improved_periods": 1,
  "variant_under_sample_periods": 1,
  "verdict": "retest",
  "reason": "At least one variant period is below the closed-trade sample threshold.",
  "records": [
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-10\\abtest_dynamic_universe_risk_off_no_core_entry_reclaim_2025-01-01_2025-06-01_v1.md",
      "start": "2025-01-01",
      "end": "2025-06-01",
      "sample_sufficient": false,
      "dynamic_metadata": {
        "baseline_master_count": "418",
        "variant_master_count": "418",
        "baseline_source_limit": "None",
        "variant_source_limit": "None",
        "baseline_universe_refreshes": "152",
        "variant_universe_refreshes": "152"
      },
      "baseline": {
        "trades": 91,
        "closed_trades": 17,
        "open_trades": 3,
        "win_rate": 11.76470588235294,
        "profit_factor": 0.3267107639092419,
        "avg_r": -0.587579187250048,
        "net_return_pct": -11.797079538661093,
        "max_drawdown": 1491.3179874467587,
        "max_drawdown_pct": 14.48891516952118,
        "intrabar_max_drawdown": 1447.3663971714068,
        "intrabar_max_drawdown_pct": 14.166801655470952,
        "tp1_rate": 11.76470588235294,
        "tp2_rate": 11.76470588235294,
        "stop_rate": 88.23529411764706,
        "fee_drag": 21.27499693532945,
        "tail_max_loss": -104.26307084075773,
        "cagr": -26.17211747574988,
        "sharpe": -2.22676780806392,
        "sortino": -2.288121469885454,
        "exposure_pct": 81.56732891832229,
        "turnover": 1.8716336947181718,
        "sample_sufficient": false,
        "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
      },
      "variant": {
        "trades": 91,
        "closed_trades": 15,
        "open_trades": 1,
        "win_rate": 13.333333333333334,
        "profit_factor": 0.41286897495684083,
        "avg_r": -0.5001202170789691,
        "net_return_pct": -8.168417189682753,
        "max_drawdown": 1117.1414205881865,
        "max_drawdown_pct": 10.852894033469328,
        "intrabar_max_drawdown": 1023.9400768066625,
        "intrabar_max_drawdown_pct": 10.05176907608129,
        "tp1_rate": 20.0,
        "tp2_rate": 13.333333333333334,
        "stop_rate": 86.66666666666667,
        "fee_drag": 20.434937459527138,
        "tail_max_loss": -105.45388955456175,
        "cagr": -18.61511669669277,
        "sharpe": -1.3030347844364556,
        "sortino": -1.1076295689606377,
        "exposure_pct": 56.84326710816777,
        "turnover": 1.7585991029502606,
        "sample_sufficient": false,
        "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
      }
    },
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-10\\abtest_dynamic_universe_risk_off_no_core_entry_reclaim_2025-06-01_2026-06-01_v1.md",
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
