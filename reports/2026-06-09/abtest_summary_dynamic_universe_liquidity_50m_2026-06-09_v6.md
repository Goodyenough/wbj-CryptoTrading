---
created: 2026-06-09 14:07:19 CST
tags:
  - crypto
  - trading-system
  - abtest-summary
experiment_id: liquidity_50m
mode: dynamic_universe
periods: 6
sufficient_periods: 4
unique_coverage_days: 516
overlap_periods: 5
universe_warnings: 2
verdict: retest
report_version: v6
---

# A/B 多时段汇总 liquidity_50m v6

- experiment_id: `liquidity_50m`
- mode: `dynamic_universe`
- periods: 6
- sufficient_periods: 4
- total_period_days: 1762
- unique_coverage_days: 516
- overlap_periods: 5
- universe_warnings: 2
- net_improved_periods: 4
- profit_factor_improved_periods: 4
- drawdown_improved_periods: 4
- variant_under_sample_periods: 2
- verdict: `retest`
- reason: Some periods overlap, so the evidence is not fully independent.

## Period Results

| Period | Sample | Closed B -> V | Win B -> V | PF B -> V | Sharpe B -> V | MDD B -> V | Net B -> V | Stop B -> V | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 2025-01-01 -> 2025-06-01 | no | 14.00 -> 12.00 | 7.14% -> 8.33% | 0.20 -> 0.23 | -2.04 -> -1.74 | 12.67% -> 10.33% | -10.37% -> -8.51% | 92.86% -> 91.67% | retest |
| 2025-01-01 -> 2025-09-01 | yes | 33.00 -> 30.00 | 15.15% -> 20.00% | 0.43 -> 0.65 | -1.35 -> -0.63 | 19.84% -> 14.69% | -15.27% -> -8.13% | 84.85% -> 80.00% | retest |
| 2025-06-01 -> 2026-06-01 | yes | 36.00 -> 38.00 | 22.22% -> 23.68% | 0.72 -> 0.81 | -0.53 -> -0.29 | 19.70% -> 18.76% | -8.77% -> -5.53% | 77.78% -> 76.32% | retest |
| 2025-06-01 -> 2026-06-01 | yes | 36.00 -> 38.00 | 22.22% -> 23.68% | 0.72 -> 0.81 | -0.53 -> -0.29 | 19.70% -> 18.76% | -8.77% -> -5.53% | 77.78% -> 76.32% | retest |
| 2025-06-01 -> 2026-06-01 | yes | 55.00 -> 56.00 | 21.82% -> 23.21% | 0.70 -> 0.75 | -0.65 -> -0.48 | 26.71% -> 24.92% | -13.04% -> -10.31% | 78.18% -> 76.79% | retest |
| 2025-09-01 -> 2026-06-01 | no | 20.00 -> 19.00 | 15.00% -> 15.79% | 0.45 -> 0.48 | -1.09 -> -0.89 | 18.06% -> 15.99% | -10.09% -> -8.23% | 85.00% -> 84.21% | retest |

## Universe Bias Checks

- Dynamic universe uses current Binance exchangeInfo as the symbol master; historic delisted symbols may be missing.
- 6/6 periods used source_limit; rerun with a larger or uncapped master before keep review.

## Source Reports

- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-09\abtest_dynamic_universe_liquidity_50m_2025-01-01_2025-06-01_v1.md`
- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-09\abtest_dynamic_universe_liquidity_50m_2025-01-01_2025-09-01_v1.md`
- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-09\abtest_dynamic_universe_liquidity_50m_2025-06-01_2026-06-01_v1.md`
- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-09\abtest_dynamic_universe_liquidity_50m_2025-06-01_2026-06-01_v2.md`
- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-09\abtest_dynamic_universe_liquidity_50m_2025-06-01_2026-06-01_v3.md`
- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-09\abtest_dynamic_universe_liquidity_50m_2025-09-01_2026-06-01_v1.md`

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
  "periods": 6,
  "sufficient_periods": 4,
  "total_period_days": 1762,
  "unique_coverage_days": 516,
  "overlap_periods": 5,
  "universe_warnings": [
    "Dynamic universe uses current Binance exchangeInfo as the symbol master; historic delisted symbols may be missing.",
    "6/6 periods used source_limit; rerun with a larger or uncapped master before keep review."
  ],
  "net_improved_periods": 4,
  "profit_factor_improved_periods": 4,
  "drawdown_improved_periods": 4,
  "variant_under_sample_periods": 2,
  "verdict": "retest",
  "reason": "Some periods overlap, so the evidence is not fully independent.",
  "records": [
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-09\\abtest_dynamic_universe_liquidity_50m_2025-01-01_2025-06-01_v1.md",
      "start": "2025-01-01",
      "end": "2025-06-01",
      "sample_sufficient": false,
      "dynamic_metadata": {
        "baseline_master_count": "100",
        "variant_master_count": "100",
        "baseline_source_limit": "100",
        "variant_source_limit": "100",
        "baseline_universe_refreshes": "152",
        "variant_universe_refreshes": "152"
      },
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
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-09\\abtest_dynamic_universe_liquidity_50m_2025-01-01_2025-09-01_v1.md",
      "start": "2025-01-01",
      "end": "2025-09-01",
      "sample_sufficient": true,
      "dynamic_metadata": {
        "baseline_master_count": "100",
        "variant_master_count": "100",
        "baseline_source_limit": "100",
        "variant_source_limit": "100",
        "baseline_universe_refreshes": "244",
        "variant_universe_refreshes": "244"
      },
      "baseline": {
        "trades": 108,
        "closed_trades": 33,
        "open_trades": 3,
        "win_rate": 15.151515151515152,
        "profit_factor": 0.43115800770552987,
        "avg_r": -0.465503443901505,
        "net_return_pct": -15.270931447235615,
        "max_drawdown": 2032.3298832070068,
        "max_drawdown_pct": 19.841643217283078,
        "intrabar_max_drawdown": 2002.4190905666137,
        "intrabar_max_drawdown_pct": 19.672125543009255,
        "tp1_rate": 27.27272727272727,
        "tp2_rate": 15.151515151515152,
        "stop_rate": 84.84848484848484,
        "fee_drag": 48.05279488339604,
        "tail_max_loss": -108.1494009784496,
        "cagr": -22.03484138384406,
        "sharpe": -1.3451865578209627,
        "sortino": -1.4477309180821338,
        "exposure_pct": 87.79149519890261,
        "turnover": 3.9369289196597093,
        "sample_sufficient": true,
        "sample_warning": ""
      },
      "variant": {
        "trades": 60,
        "closed_trades": 30,
        "open_trades": 3,
        "win_rate": 20.0,
        "profit_factor": 0.6484928567521694,
        "avg_r": -0.26478528698685116,
        "net_return_pct": -8.134084586517588,
        "max_drawdown": 1498.1520334023226,
        "max_drawdown_pct": 14.694677626762392,
        "intrabar_max_drawdown": 1462.2485417241187,
        "intrabar_max_drawdown_pct": 14.418160337896571,
        "tp1_rate": 30.0,
        "tp2_rate": 20.0,
        "stop_rate": 80.0,
        "fee_drag": 38.96778575047144,
        "tail_max_loss": -108.1494009784496,
        "cagr": -11.964913252062793,
        "sharpe": -0.6302215820477526,
        "sortino": -0.6837326501217234,
        "exposure_pct": 88.54595336076817,
        "turnover": 3.397006683907528,
        "sample_sufficient": true,
        "sample_warning": ""
      }
    },
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-09\\abtest_dynamic_universe_liquidity_50m_2025-06-01_2026-06-01_v1.md",
      "start": "2025-06-01",
      "end": "2026-06-01",
      "sample_sufficient": true,
      "dynamic_metadata": {
        "baseline_master_count": "100",
        "variant_master_count": "100",
        "baseline_source_limit": "100",
        "variant_source_limit": "100",
        "baseline_universe_refreshes": "366",
        "variant_universe_refreshes": "366"
      },
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
    },
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-09\\abtest_dynamic_universe_liquidity_50m_2025-06-01_2026-06-01_v2.md",
      "start": "2025-06-01",
      "end": "2026-06-01",
      "sample_sufficient": true,
      "dynamic_metadata": {
        "baseline_master_count": "100",
        "variant_master_count": "100",
        "baseline_source_limit": "100",
        "variant_source_limit": "100",
        "baseline_universe_refreshes": "366",
        "variant_universe_refreshes": "366"
      },
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
    },
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-09\\abtest_dynamic_universe_liquidity_50m_2025-06-01_2026-06-01_v3.md",
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
    },
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-09\\abtest_dynamic_universe_liquidity_50m_2025-09-01_2026-06-01_v1.md",
      "start": "2025-09-01",
      "end": "2026-06-01",
      "sample_sufficient": false,
      "dynamic_metadata": {
        "baseline_master_count": "100",
        "variant_master_count": "100",
        "baseline_source_limit": "100",
        "variant_source_limit": "100",
        "baseline_universe_refreshes": "274",
        "variant_universe_refreshes": "274"
      },
      "baseline": {
        "trades": 37,
        "closed_trades": 20,
        "open_trades": 3,
        "win_rate": 15.0,
        "profit_factor": 0.45147171647802614,
        "avg_r": -0.47901078999689306,
        "net_return_pct": -10.087210136766556,
        "max_drawdown": 1922.8512378842643,
        "max_drawdown_pct": 18.06390957955602,
        "intrabar_max_drawdown": 1906.3776592061222,
        "intrabar_max_drawdown_pct": 17.98864220521859,
        "tp1_rate": 25.0,
        "tp2_rate": 15.0,
        "stop_rate": 85.0,
        "fee_drag": 41.58467837208483,
        "tail_max_loss": -112.37720364593433,
        "cagr": -13.25199834314611,
        "sharpe": -1.0856809535779242,
        "sortino": -1.0200271877072418,
        "exposure_pct": 72.4053724053724,
        "turnover": 3.4492407292658624,
        "sample_sufficient": true,
        "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
      },
      "variant": {
        "trades": 24,
        "closed_trades": 19,
        "open_trades": 2,
        "win_rate": 15.789473684210526,
        "profit_factor": 0.478928572171142,
        "avg_r": -0.44754341509220685,
        "net_return_pct": -8.231610576280524,
        "max_drawdown": 1695.3305461087984,
        "max_drawdown_pct": 15.988375751971482,
        "intrabar_max_drawdown": 1686.8520057245642,
        "intrabar_max_drawdown_pct": 15.968315933244122,
        "tp1_rate": 31.57894736842105,
        "tp2_rate": 15.789473684210526,
        "stop_rate": 84.21052631578947,
        "fee_drag": 37.06316534112992,
        "tail_max_loss": -108.51336896732407,
        "cagr": -10.850107395008624,
        "sharpe": -0.8851230644756023,
        "sortino": -0.7943386750613117,
        "exposure_pct": 72.4053724053724,
        "turnover": 3.1131614378323174,
        "sample_sufficient": false,
        "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
      }
    }
  ]
}
```
