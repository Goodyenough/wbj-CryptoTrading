---
created: 2026-06-09 15:03:05 CST
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
universe_warnings: 2
verdict: retest
report_version: v7
---

# A/B 多时段汇总 liquidity_50m v7

- experiment_id: `liquidity_50m`
- mode: `dynamic_universe`
- periods: 2
- sufficient_periods: 1
- total_period_days: 516
- unique_coverage_days: 516
- overlap_periods: 0
- universe_warnings: 2
- net_improved_periods: 1
- profit_factor_improved_periods: 1
- drawdown_improved_periods: 1
- variant_under_sample_periods: 1
- verdict: `retest`
- reason: At least one variant period is below the closed-trade sample threshold.

## Period Results

| Period | Sample | Closed B -> V | Win B -> V | PF B -> V | Sharpe B -> V | MDD B -> V | Net B -> V | Stop B -> V | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 2025-01-01 -> 2025-06-01 | no | 19.00 -> 16.00 | 10.53% -> 12.50% | 0.29 -> 0.35 | -1.90 -> -1.64 | 14.48% -> 13.22% | -11.23% -> -9.09% | 89.47% -> 87.50% | retest |
| 2025-06-01 -> 2026-06-01 | yes | 55.00 -> 56.00 | 21.82% -> 23.21% | 0.70 -> 0.75 | -0.65 -> -0.48 | 26.71% -> 24.92% | -13.04% -> -10.31% | 78.18% -> 76.79% | retest |

## Universe Bias Checks

- Dynamic universe uses current Binance exchangeInfo as the symbol master; historic delisted symbols may be missing.
- 2/2 periods used source_limit; rerun with a larger or uncapped master before keep review.

## Source Reports

- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-09\abtest_dynamic_universe_liquidity_50m_2025-01-01_2025-06-01_v2.md`
- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-09\abtest_dynamic_universe_liquidity_50m_2025-06-01_2026-06-01_v4.md`

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
  "universe_warnings": [
    "Dynamic universe uses current Binance exchangeInfo as the symbol master; historic delisted symbols may be missing.",
    "2/2 periods used source_limit; rerun with a larger or uncapped master before keep review."
  ],
  "net_improved_periods": 1,
  "profit_factor_improved_periods": 1,
  "drawdown_improved_periods": 1,
  "variant_under_sample_periods": 1,
  "verdict": "retest",
  "reason": "At least one variant period is below the closed-trade sample threshold.",
  "records": [
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-09\\abtest_dynamic_universe_liquidity_50m_2025-01-01_2025-06-01_v2.md",
      "start": "2025-01-01",
      "end": "2025-06-01",
      "sample_sufficient": false,
      "dynamic_metadata": {
        "baseline_master_count": "150",
        "variant_master_count": "150",
        "baseline_source_limit": "150",
        "variant_source_limit": "150",
        "baseline_universe_refreshes": "152",
        "variant_universe_refreshes": "152"
      },
      "baseline": {
        "trades": 71,
        "closed_trades": 19,
        "open_trades": 2,
        "win_rate": 10.526315789473683,
        "profit_factor": 0.2858130405717013,
        "avg_r": -0.6364200822044673,
        "net_return_pct": -11.225828888974299,
        "max_drawdown": 1490.0847844948985,
        "max_drawdown_pct": 14.475121436558029,
        "intrabar_max_drawdown": 1398.4557339298153,
        "intrabar_max_drawdown_pct": 13.711355582690537,
        "tp1_rate": 21.052631578947366,
        "tp2_rate": 10.526315789473683,
        "stop_rate": 89.47368421052632,
        "fee_drag": 27.00553390300852,
        "tail_max_loss": -108.73727506688915,
        "cagr": -25.011015340279762,
        "sharpe": -1.8957856901555281,
        "sortino": -1.8369508751256913,
        "exposure_pct": 81.56732891832229,
        "turnover": 2.2609745222643602,
        "sample_sufficient": false,
        "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
      },
      "variant": {
        "trades": 46,
        "closed_trades": 16,
        "open_trades": 2,
        "win_rate": 12.5,
        "profit_factor": 0.34727788284317357,
        "avg_r": -0.5638995421497967,
        "net_return_pct": -9.085559393015497,
        "max_drawdown": 1355.6073553493097,
        "max_drawdown_pct": 13.218848904267821,
        "intrabar_max_drawdown": 1275.9881670681207,
        "intrabar_max_drawdown_pct": 12.543842903894435,
        "tp1_rate": 18.75,
        "tp2_rate": 12.5,
        "stop_rate": 87.5,
        "fee_drag": 23.16039094761875,
        "tail_max_loss": -108.73727506688915,
        "cagr": -20.56596783449137,
        "sharpe": -1.6419457521957572,
        "sortino": -1.6040070181243393,
        "exposure_pct": 81.56732891832229,
        "turnover": 1.9618017736187412,
        "sample_sufficient": false,
        "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
      }
    },
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-09\\abtest_dynamic_universe_liquidity_50m_2025-06-01_2026-06-01_v4.md",
      "start": "2025-06-01",
      "end": "2026-06-01",
      "sample_sufficient": true,
      "dynamic_metadata": {
        "baseline_master_count": "150",
        "variant_master_count": "150",
        "baseline_source_limit": "150",
        "variant_source_limit": "150",
        "baseline_universe_refreshes": "366",
        "variant_universe_refreshes": "366"
      },
      "baseline": {
        "trades": 185,
        "closed_trades": 55,
        "open_trades": 3,
        "win_rate": 21.818181818181817,
        "profit_factor": 0.6971178307001836,
        "avg_r": -0.2241219405403126,
        "net_return_pct": -13.03576231812318,
        "max_drawdown": 3040.594745082548,
        "max_drawdown_pct": 26.712317955989878,
        "intrabar_max_drawdown": 2921.2848075155507,
        "intrabar_max_drawdown_pct": 25.96805481972579,
        "tp1_rate": 32.72727272727273,
        "tp2_rate": 21.818181818181817,
        "stop_rate": 78.18181818181819,
        "fee_drag": 90.95372387204374,
        "tail_max_loss": -116.33760689127996,
        "cagr": -13.03576231812318,
        "sharpe": -0.649847198418506,
        "sortino": -0.7333287352121214,
        "exposure_pct": 86.11872146118722,
        "turnover": 7.618009571618466,
        "sample_sufficient": true,
        "sample_warning": ""
      },
      "variant": {
        "trades": 120,
        "closed_trades": 56,
        "open_trades": 2,
        "win_rate": 23.214285714285715,
        "profit_factor": 0.7529602396706798,
        "avg_r": -0.17589781865354817,
        "net_return_pct": -10.306134421864677,
        "max_drawdown": 2839.947311838918,
        "max_drawdown_pct": 24.920342553022856,
        "intrabar_max_drawdown": 2780.0288582567027,
        "intrabar_max_drawdown_pct": 24.554384929008435,
        "tp1_rate": 33.92857142857143,
        "tp2_rate": 23.214285714285715,
        "stop_rate": 76.78571428571429,
        "fee_drag": 91.82453446977661,
        "tail_max_loss": -116.6667126115919,
        "cagr": -10.306134421864677,
        "sharpe": -0.4799191933924716,
        "sortino": -0.5539044248876623,
        "exposure_pct": 86.11872146118722,
        "turnover": 7.621200687701357,
        "sample_sufficient": true,
        "sample_warning": ""
      }
    }
  ]
}
```
