---
created: 2026-06-10 03:44:06 CST
tags:
  - crypto
  - trading-system
  - abtest-summary
experiment_id: risk_off_no_core_entry_reclaim
mode: dynamic_universe
periods: 3
sufficient_periods: 2
unique_coverage_days: 516
overlap_periods: 2
universe_warnings: 1
verdict: retest
report_version: v1
---

# A/B 多时段汇总 risk_off_no_core_entry_reclaim v1

- experiment_id: `risk_off_no_core_entry_reclaim`
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
| 2025-01-01 -> 2025-06-01 | no | 17.00 -> 15.00 | 11.76% -> 13.33% | 0.33 -> 0.41 | -2.23 -> -1.30 | 14.49% -> 10.85% | -11.80% -> -8.17% | 88.24% -> 86.67% | retest |
| 2025-01-01 -> 2025-09-01 | yes | 42.00 -> 38.00 | 19.05% -> 28.95% | 0.58 -> 1.03 | -1.03 -> 0.10 | 19.43% -> 15.11% | -13.17% -> -0.03% | 80.95% -> 71.05% | retest |
| 2025-06-01 -> 2026-06-01 | yes | 49.00 -> 46.00 | 22.45% -> 32.61% | 0.73 -> 1.20 | -0.54 -> 0.41 | 24.24% -> 14.46% | -10.62% -> 5.96% | 77.55% -> 67.39% | retest |

## Universe Bias Checks

- Dynamic universe uses current Binance exchangeInfo as the symbol master; historic delisted symbols may be missing.

## Source Reports

- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-10\abtest_dynamic_universe_risk_off_no_core_entry_reclaim_2025-01-01_2025-06-01_v1.md`
- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-10\abtest_dynamic_universe_risk_off_no_core_entry_reclaim_2025-01-01_2025-09-01_v1.md`
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
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-10\\abtest_dynamic_universe_risk_off_no_core_entry_reclaim_2025-01-01_2025-09-01_v1.md",
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
        "trades": 269,
        "closed_trades": 38,
        "open_trades": 4,
        "win_rate": 28.947368421052634,
        "profit_factor": 1.0253876650457328,
        "avg_r": 0.04947363396163098,
        "net_return_pct": -0.025332629522578642,
        "max_drawdown": 1555.3354725851896,
        "max_drawdown_pct": 15.10989634738954,
        "intrabar_max_drawdown": 1537.8609090133668,
        "intrabar_max_drawdown_pct": 15.09680407934028,
        "tp1_rate": 44.73684210526316,
        "tp2_rate": 28.947368421052634,
        "stop_rate": 71.05263157894737,
        "fee_drag": 53.6237796287557,
        "tail_max_loss": -111.19650825724824,
        "cagr": -0.03804864918312001,
        "sharpe": 0.1023901459022063,
        "sortino": 0.11445620851995147,
        "exposure_pct": 72.35939643347051,
        "turnover": 4.8549285337607655,
        "sample_sufficient": true,
        "sample_warning": ""
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
