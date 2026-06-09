---
created: 2026-06-09 12:59:00 CST
tags:
  - crypto
  - trading-system
  - abtest-summary
experiment_id: liquidity_50m
mode: dynamic_universe
periods: 2
sufficient_periods: 1
unique_coverage_days: 516
overlap_periods: 0
verdict: retest
report_version: v4
---

# A/B 多时段汇总 liquidity_50m v4

- experiment_id: `liquidity_50m`
- mode: `dynamic_universe`
- periods: 2
- sufficient_periods: 1
- total_period_days: 516
- unique_coverage_days: 516
- overlap_periods: 0
- net_improved_periods: 1
- profit_factor_improved_periods: 1
- drawdown_improved_periods: 1
- variant_under_sample_periods: 1
- verdict: `retest`
- reason: At least one variant period is below the closed-trade sample threshold.

## Period Results

| Period | Sample | Closed B -> V | Win B -> V | PF B -> V | Sharpe B -> V | MDD B -> V | Net B -> V | Stop B -> V | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 2025-01-01 -> 2025-06-01 | no | 14.00 -> 12.00 | 7.14% -> 8.33% | 0.20 -> 0.23 | -2.04 -> -1.74 | 12.67% -> 10.33% | -10.37% -> -8.51% | 92.86% -> 91.67% | retest |
| 2025-06-01 -> 2026-06-01 | yes | 36.00 -> 38.00 | 22.22% -> 23.68% | 0.72 -> 0.81 | -0.53 -> -0.29 | 19.70% -> 18.76% | -8.77% -> -5.53% | 77.78% -> 76.32% | retest |

## Source Reports

- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-09\abtest_dynamic_universe_liquidity_50m_2025-01-01_2025-06-01_v1.md`
- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-09\abtest_dynamic_universe_liquidity_50m_2025-06-01_2026-06-01_v2.md`

## Decision Rule

- 汇总报告只给出 `candidate_keep_review`、`retest` 或 `reject_candidate`，不会自动修改默认配置。
- 至少需要多个充足样本时段共同改善净收益、Profit factor 和最大回撤，才会标记 `candidate_keep_review`。
- 时段存在重叠时，证据不视为完全独立，结论保持 `retest`。
- 任一 variant 样本不足时，结论应偏向 `retest`。

## Raw Summary

```json
{
  "experiment_id": "liquidity_50m",
  "mode": "dynamic_universe",
  "periods": 2,
  "sufficient_periods": 1,
  "total_period_days": 516,
  "unique_coverage_days": 516,
  "overlap_periods": 0,
  "net_improved_periods": 1,
  "profit_factor_improved_periods": 1,
  "drawdown_improved_periods": 1,
  "variant_under_sample_periods": 1,
  "verdict": "retest",
  "reason": "At least one variant period is below the closed-trade sample threshold.",
  "records": [
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-09\\abtest_dynamic_universe_liquidity_50m_2025-01-01_2025-06-01_v1.md",
      "start": "2025-01-01",
      "end": "2025-06-01",
      "sample_sufficient": false,
      "baseline": {
        "trades": 36,
        "closed_trades": 14,
        "open_trades": 2,
        "win_rate": 7.142857142857142,
        "profit_factor": 0.1979925903647124,
        "avg_r": -0.7533967667591908,
        "net_return_pct": -10.367053377005908,
        "max_drawdown": 1297.893550917499,
        "max_drawdown_pct": 12.671338931788265,
        "intrabar_max_drawdown": 1272.2608957171942,
        "intrabar_max_drawdown_pct": 12.49892002224569,
        "tp1_rate": 14.285714285714285,
        "tp2_rate": 7.142857142857142,
        "stop_rate": 92.85714285714286,
        "fee_drag": 20.394301124180796,
        "tail_max_loss": -108.1494009784496,
        "cagr": -23.245476532179786,
        "sharpe": -2.0397468908027,
        "sortino": -1.8201616169203354,
        "exposure_pct": 81.56732891832229,
        "turnover": 1.781273802186134,
        "sample_sufficient": false,
        "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
      },
      "variant": {
        "trades": 22,
        "closed_trades": 12,
        "open_trades": 2,
        "win_rate": 8.333333333333332,
        "profit_factor": 0.2322653230432656,
        "avg_r": -0.7091446197628661,
        "net_return_pct": -8.50950715465798,
        "max_drawdown": 1052.998061705206,
        "max_drawdown_pct": 10.328369026221734,
        "intrabar_max_drawdown": 1028.265434925188,
        "intrabar_max_drawdown_pct": 10.138971240270497,
        "tp1_rate": 16.666666666666664,
        "tp2_rate": 8.333333333333332,
        "stop_rate": 91.66666666666666,
        "fee_drag": 17.853797725231892,
        "tail_max_loss": -108.1494009784496,
        "cagr": -19.343890181058075,
        "sharpe": -1.7353697172755467,
        "sortino": -1.5368823597749883,
        "exposure_pct": 81.56732891832229,
        "turnover": 1.5106622332579631,
        "sample_sufficient": false,
        "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
      }
    },
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-09\\abtest_dynamic_universe_liquidity_50m_2025-06-01_2026-06-01_v2.md",
      "start": "2025-06-01",
      "end": "2026-06-01",
      "sample_sufficient": true,
      "baseline": {
        "trades": 108,
        "closed_trades": 36,
        "open_trades": 3,
        "win_rate": 22.22222222222222,
        "profit_factor": 0.7179994838296895,
        "avg_r": -0.20958174963443865,
        "net_return_pct": -8.76788797919248,
        "max_drawdown": 2171.6792769355943,
        "max_drawdown_pct": 19.70399164754432,
        "intrabar_max_drawdown": 2110.812412188494,
        "intrabar_max_drawdown_pct": 19.312736393538373,
        "tp1_rate": 30.555555555555557,
        "tp2_rate": 22.22222222222222,
        "stop_rate": 77.77777777777779,
        "fee_drag": 64.39244878330089,
        "tail_max_loss": -111.99973871893869,
        "cagr": -8.76788797919248,
        "sharpe": -0.529723753959949,
        "sortino": -0.5835995953542635,
        "exposure_pct": 84.15525114155251,
        "turnover": 5.325953822470949,
        "sample_sufficient": true,
        "sample_warning": ""
      },
      "variant": {
        "trades": 60,
        "closed_trades": 38,
        "open_trades": 2,
        "win_rate": 23.684210526315788,
        "profit_factor": 0.8099007692548293,
        "avg_r": -0.1302316620463432,
        "net_return_pct": -5.532110055874506,
        "max_drawdown": 2117.6575195760306,
        "max_drawdown_pct": 18.760430876087522,
        "intrabar_max_drawdown": 2071.5771379365215,
        "intrabar_max_drawdown_pct": 18.48039113849247,
        "tp1_rate": 28.947368421052634,
        "tp2_rate": 23.684210526315788,
        "stop_rate": 76.31578947368422,
        "fee_drag": 63.14974974665476,
        "tail_max_loss": -113.30139114212052,
        "cagr": -5.532110055874506,
        "sharpe": -0.28500993555989385,
        "sortino": -0.3104918438106821,
        "exposure_pct": 84.15525114155251,
        "turnover": 5.281501860962036,
        "sample_sufficient": true,
        "sample_warning": ""
      }
    }
  ]
}
```
