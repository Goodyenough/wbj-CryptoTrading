---
created: 2026-06-09 02:43:11 CST
tags:
  - crypto
  - trading-system
  - abtest-summary
experiment_id: liquidity_50m
mode: dynamic_universe
periods: 3
sufficient_periods: 2
verdict: retest
report_version: v2
---

# A/B 多时段汇总 liquidity_50m v2

- experiment_id: `liquidity_50m`
- mode: `dynamic_universe`
- periods: 3
- sufficient_periods: 2
- net_improved_periods: 2
- profit_factor_improved_periods: 2
- drawdown_improved_periods: 2
- variant_under_sample_periods: 1
- verdict: `retest`
- reason: At least one variant period is below the closed-trade sample threshold.

## Period Results

| Period | Sample | Closed B -> V | Win B -> V | PF B -> V | Sharpe B -> V | MDD B -> V | Net B -> V | Stop B -> V | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 2025-01-01 -> 2025-09-01 | yes | 33.00 -> 30.00 | 15.15% -> 20.00% | 0.43 -> 0.65 | -1.35 -> -0.63 | 19.84% -> 14.69% | -15.27% -> -8.13% | 84.85% -> 80.00% | retest |
| 2025-06-01 -> 2026-06-01 | yes | 36.00 -> 38.00 | 22.22% -> 23.68% | 0.72 -> 0.81 | -0.53 -> -0.29 | 19.70% -> 18.76% | -8.77% -> -5.53% | 77.78% -> 76.32% | retest |
| 2025-09-01 -> 2026-06-01 | no | 20.00 -> 19.00 | 15.00% -> 15.79% | 0.45 -> 0.48 | -1.09 -> -0.89 | 18.06% -> 15.99% | -10.09% -> -8.23% | 85.00% -> 84.21% | retest |

## Source Reports

- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-09\abtest_dynamic_universe_liquidity_50m_2025-01-01_2025-09-01_v1.md`
- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-09\abtest_dynamic_universe_liquidity_50m_2025-06-01_2026-06-01_v1.md`
- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-09\abtest_dynamic_universe_liquidity_50m_2025-09-01_2026-06-01_v1.md`

## Decision Rule

- 汇总报告只给出 `candidate_keep_review`、`retest` 或 `reject_candidate`，不会自动修改默认配置。
- 至少需要多个充足样本时段共同改善净收益、Profit factor 和最大回撤，才会标记 `candidate_keep_review`。
- 任一 variant 样本不足时，结论应偏向 `retest`。

## Raw Summary

```json
{
  "experiment_id": "liquidity_50m",
  "mode": "dynamic_universe",
  "periods": 3,
  "sufficient_periods": 2,
  "net_improved_periods": 2,
  "profit_factor_improved_periods": 2,
  "drawdown_improved_periods": 2,
  "variant_under_sample_periods": 1,
  "verdict": "retest",
  "reason": "At least one variant period is below the closed-trade sample threshold.",
  "records": [
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-09\\abtest_dynamic_universe_liquidity_50m_2025-01-01_2025-09-01_v1.md",
      "start": "2025-01-01",
      "end": "2025-09-01",
      "sample_sufficient": true,
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
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-09\\abtest_dynamic_universe_liquidity_50m_2025-09-01_2026-06-01_v1.md",
      "start": "2025-09-01",
      "end": "2026-06-01",
      "sample_sufficient": false,
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
