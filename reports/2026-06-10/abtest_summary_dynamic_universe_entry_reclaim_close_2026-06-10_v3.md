---
created: 2026-06-10 02:37:22 CST
tags:
  - crypto
  - trading-system
  - abtest-summary
experiment_id: entry_reclaim_close
mode: dynamic_universe
periods: 2
sufficient_periods: 1
unique_coverage_days: 516
overlap_periods: 0
universe_warnings: 1
verdict: retest
report_version: v3
---

# A/B 多时段汇总 entry_reclaim_close v3

- experiment_id: `entry_reclaim_close`
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
| 2025-01-01 -> 2025-06-01 | no | 17.00 -> 18.00 | 11.76% -> 11.11% | 0.33 -> 0.31 | -2.23 -> -2.14 | 14.49% -> 13.50% | -11.80% -> -11.36% | 88.24% -> 88.89% | retest |
| 2025-06-01 -> 2026-06-01 | yes | 49.00 -> 51.00 | 22.45% -> 31.37% | 0.73 -> 1.14 | -0.54 -> 0.37 | 24.24% -> 15.90% | -10.62% -> 5.34% | 77.55% -> 68.63% | retest |

## Universe Bias Checks

- Dynamic universe uses current Binance exchangeInfo as the symbol master; historic delisted symbols may be missing.

## Source Reports

- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-10\abtest_dynamic_universe_entry_reclaim_close_2025-01-01_2025-06-01_v1.md`
- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-10\abtest_dynamic_universe_entry_reclaim_close_2025-06-01_2026-06-01_v1.md`

## Decision Rule

- 汇总报告只给出 `candidate_keep_review`、`retest` 或 `reject_candidate`，不会自动修改默认配置。
- 至少需要多个充足样本时段共同改善净收益、Profit factor 和最大回撤，才会标记 `candidate_keep_review`。
- 时段存在重叠时，证据不视为完全独立，结论保持 `retest`。
- 任一 variant 样本不足时，结论应偏向 `retest`。

## Raw Summary

```json
{
  "experiment_id": "entry_reclaim_close",
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
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-10\\abtest_dynamic_universe_entry_reclaim_close_2025-01-01_2025-06-01_v1.md",
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
        "trades": 93,
        "closed_trades": 18,
        "open_trades": 1,
        "win_rate": 11.11111111111111,
        "profit_factor": 0.30517850857453244,
        "avg_r": -0.6152812468262404,
        "net_return_pct": -11.359042611254333,
        "max_drawdown": 1382.2111137329048,
        "max_drawdown_pct": 13.498430019088001,
        "intrabar_max_drawdown": 1296.7135661168886,
        "intrabar_max_drawdown_pct": 12.7865086064337,
        "tp1_rate": 11.11111111111111,
        "tp2_rate": 11.11111111111111,
        "stop_rate": 88.88888888888889,
        "fee_drag": 25.422258473503092,
        "tail_max_loss": -104.32545844903288,
        "cagr": -25.282730443616252,
        "sharpe": -2.1419844706035405,
        "sortino": -2.0434406898521957,
        "exposure_pct": 74.17218543046357,
        "turnover": 2.0627659006285324,
        "sample_sufficient": false,
        "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
      }
    },
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-10\\abtest_dynamic_universe_entry_reclaim_close_2025-06-01_2026-06-01_v1.md",
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
        "trades": 302,
        "closed_trades": 51,
        "open_trades": 3,
        "win_rate": 31.372549019607842,
        "profit_factor": 1.1420343723673843,
        "avg_r": 0.1287920796436081,
        "net_return_pct": 5.337048670007816,
        "max_drawdown": 1896.3142639521138,
        "max_drawdown_pct": 15.89697819960985,
        "intrabar_max_drawdown": 1893.595110689068,
        "intrabar_max_drawdown_pct": 15.90008367399503,
        "tp1_rate": 43.13725490196079,
        "tp2_rate": 31.372549019607842,
        "stop_rate": 68.62745098039215,
        "fee_drag": 94.57513428929525,
        "tail_max_loss": -127.01230435719472,
        "cagr": 5.337048670007816,
        "sharpe": 0.3680987497384412,
        "sortino": 0.44796182002664015,
        "exposure_pct": 88.08219178082192,
        "turnover": 8.235582796684122,
        "sample_sufficient": true,
        "sample_warning": ""
      }
    }
  ]
}
```
