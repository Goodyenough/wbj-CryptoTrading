---
created: 2026-06-09 23:51:51 CST
tags:
  - crypto
  - trading-system
  - abtest-summary
experiment_id: risk_off_no_core_top_n_3
mode: dynamic_universe
periods: 3
sufficient_periods: 2
unique_coverage_days: 516
overlap_periods: 2
universe_warnings: 1
verdict: retest
report_version: v1
---

# A/B 多时段汇总 risk_off_no_core_top_n_3 v1

- experiment_id: `risk_off_no_core_top_n_3`
- mode: `dynamic_universe`
- periods: 3
- sufficient_periods: 2
- total_period_days: 759
- unique_coverage_days: 516
- overlap_periods: 2
- universe_warnings: 1
- net_improved_periods: 2
- profit_factor_improved_periods: 2
- drawdown_improved_periods: 2
- variant_under_sample_periods: 1
- verdict: `retest`
- reason: Some periods overlap, so the evidence is not fully independent.

## Period Results

| Period | Sample | Closed B -> V | Win B -> V | PF B -> V | Sharpe B -> V | MDD B -> V | Net B -> V | Stop B -> V | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 2025-01-01 -> 2025-06-01 | no | 17.00 -> 13.00 | 11.76% -> 15.38% | 0.33 -> 0.49 | -2.23 -> -1.49 | 14.49% -> 11.46% | -11.80% -> -8.03% | 88.24% -> 84.62% | retest |
| 2025-01-01 -> 2025-09-01 | yes | 42.00 -> 35.00 | 19.05% -> 28.57% | 0.58 -> 1.00 | -1.03 -> 0.18 | 19.43% -> 15.96% | -13.17% -> 1.04% | 80.95% -> 71.43% | retest |
| 2025-06-01 -> 2026-06-01 | yes | 49.00 -> 46.00 | 22.45% -> 26.09% | 0.73 -> 0.88 | -0.54 -> -0.24 | 24.24% -> 21.38% | -10.62% -> -5.36% | 77.55% -> 73.91% | retest |

## Universe Bias Checks

- Dynamic universe uses current Binance exchangeInfo as the symbol master; historic delisted symbols may be missing.

## Source Reports

- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-09\abtest_dynamic_universe_risk_off_no_core_top_n_3_2025-01-01_2025-06-01_v1.md`
- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-09\abtest_dynamic_universe_risk_off_no_core_top_n_3_2025-01-01_2025-09-01_v1.md`
- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-09\abtest_dynamic_universe_risk_off_no_core_top_n_3_2025-06-01_2026-06-01_v1.md`

## Decision Rule

- 汇总报告只给出 `candidate_keep_review`、`retest` 或 `reject_candidate`，不会自动修改默认配置。
- 至少需要多个充足样本时段共同改善净收益、Profit factor 和最大回撤，才会标记 `candidate_keep_review`。
- 时段存在重叠时，证据不视为完全独立，结论保持 `retest`。
- 任一 variant 样本不足时，结论应偏向 `retest`。

## Raw Summary

```json
{
  "experiment_id": "risk_off_no_core_top_n_3",
  "mode": "dynamic_universe",
  "periods": 3,
  "sufficient_periods": 2,
  "total_period_days": 759,
  "unique_coverage_days": 516,
  "overlap_periods": 2,
  "universe_warnings": [
    "Dynamic universe uses current Binance exchangeInfo as the symbol master; historic delisted symbols may be missing."
  ],
  "net_improved_periods": 2,
  "profit_factor_improved_periods": 2,
  "drawdown_improved_periods": 2,
  "variant_under_sample_periods": 1,
  "verdict": "retest",
  "reason": "Some periods overlap, so the evidence is not fully independent.",
  "records": [
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-09\\abtest_dynamic_universe_risk_off_no_core_top_n_3_2025-01-01_2025-06-01_v1.md",
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
        "trades": 89,
        "closed_trades": 13,
        "open_trades": 4,
        "win_rate": 15.384615384615385,
        "profit_factor": 0.48803471650381675,
        "avg_r": -0.4187143662741381,
        "net_return_pct": -8.028673472946924,
        "max_drawdown": 1186.1364678973623,
        "max_drawdown_pct": 11.464479508308784,
        "intrabar_max_drawdown": 1173.152013713605,
        "intrabar_max_drawdown_pct": 11.43215217011969,
        "tp1_rate": 15.384615384615385,
        "tp2_rate": 15.384615384615385,
        "stop_rate": 84.61538461538461,
        "fee_drag": 19.23898815172922,
        "tail_max_loss": -105.36993946372326,
        "cagr": -18.315429605295684,
        "sharpe": -1.4931620823513791,
        "sortino": -1.317748584344828,
        "exposure_pct": 57.17439293598234,
        "turnover": 2.0544783799587045,
        "sample_sufficient": false,
        "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
      }
    },
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-09\\abtest_dynamic_universe_risk_off_no_core_top_n_3_2025-01-01_2025-09-01_v1.md",
      "start": "2025-01-01",
      "end": "2025-09-01",
      "sample_sufficient": true,
      "dynamic_metadata": {
        "baseline_master_count": "418",
        "variant_master_count": "418",
        "baseline_source_limit": "None",
        "variant_source_limit": "None",
        "baseline_universe_refreshes": "244",
        "variant_universe_refreshes": "244"
      },
      "baseline": {
        "trades": 271,
        "closed_trades": 42,
        "open_trades": 5,
        "win_rate": 19.047619047619047,
        "profit_factor": 0.5788303615775615,
        "avg_r": -0.32109130123569374,
        "net_return_pct": -13.169473352124028,
        "max_drawdown": 1999.7034664765688,
        "max_drawdown_pct": 19.428139493966125,
        "intrabar_max_drawdown": 1981.126720276632,
        "intrabar_max_drawdown_pct": 19.391240086382176,
        "tp1_rate": 30.952380952380953,
        "tp2_rate": 19.047619047619047,
        "stop_rate": 80.95238095238095,
        "fee_drag": 51.18942488974736,
        "tail_max_loss": -104.26307084075773,
        "cagr": -19.112304164922577,
        "sharpe": -1.0333162547884633,
        "sortino": -1.26161554956655,
        "exposure_pct": 87.72290809327846,
        "turnover": 4.471898425556106,
        "sample_sufficient": true,
        "sample_warning": ""
      },
      "variant": {
        "trades": 264,
        "closed_trades": 35,
        "open_trades": 5,
        "win_rate": 28.57142857142857,
        "profit_factor": 1.0005359068871378,
        "avg_r": 0.03758993204237669,
        "net_return_pct": 1.0396124611707247,
        "max_drawdown": 1651.6571092305949,
        "max_drawdown_pct": 15.963921181087215,
        "intrabar_max_drawdown": 1627.7618426066038,
        "intrabar_max_drawdown_pct": 15.862241946367217,
        "tp1_rate": 34.285714285714285,
        "tp2_rate": 28.57142857142857,
        "stop_rate": 71.42857142857143,
        "fee_drag": 49.78836076617317,
        "tail_max_loss": -110.93703354839087,
        "cagr": 1.5656260464253613,
        "sharpe": 0.17633875434996177,
        "sortino": 0.2060593397174128,
        "exposure_pct": 72.63374485596708,
        "turnover": 4.535413937732525,
        "sample_sufficient": true,
        "sample_warning": ""
      }
    },
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-09\\abtest_dynamic_universe_risk_off_no_core_top_n_3_2025-06-01_2026-06-01_v1.md",
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
        "trades": 291,
        "closed_trades": 46,
        "open_trades": 2,
        "win_rate": 26.08695652173913,
        "profit_factor": 0.8755086052495377,
        "avg_r": -0.0811716835723636,
        "net_return_pct": -5.358158509585786,
        "max_drawdown": 2534.7954083705954,
        "max_drawdown_pct": 21.38064313614943,
        "intrabar_max_drawdown": 2543.407131414604,
        "intrabar_max_drawdown_pct": 21.55519496108469,
        "tp1_rate": 30.434782608695656,
        "tp2_rate": 26.08695652173913,
        "stop_rate": 73.91304347826086,
        "fee_drag": 78.79849729583839,
        "tail_max_loss": -123.53066761796354,
        "cagr": -5.358158509585786,
        "sharpe": -0.2353828204806775,
        "sortino": -0.24951595577401595,
        "exposure_pct": 63.013698630136986,
        "turnover": 6.617967050728584,
        "sample_sufficient": true,
        "sample_warning": ""
      }
    }
  ]
}
```
