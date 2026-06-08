---
created: 2026-06-09 02:26:34 CST
tags:
  - crypto
  - trading-system
  - abtest-summary
experiment_id: history_365
mode: dynamic_universe
periods: 3
sufficient_periods: 2
verdict: retest
report_version: v1
---

# A/B 多时段汇总 history_365 v1

- experiment_id: `history_365`
- mode: `dynamic_universe`
- periods: 3
- sufficient_periods: 2
- net_improved_periods: 1
- profit_factor_improved_periods: 1
- drawdown_improved_periods: 1
- variant_under_sample_periods: 1
- verdict: `retest`
- reason: At least one variant period is below the closed-trade sample threshold.

## Period Results

| Period | Sample | Closed B -> V | Win B -> V | PF B -> V | Sharpe B -> V | MDD B -> V | Net B -> V | Stop B -> V | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 2025-01-01 -> 2025-06-01 | no | 14.00 -> 13.00 | 7.14% -> 7.69% | 0.20 -> 0.21 | -2.04 -> -2.15 | 12.67% -> 11.66% | -10.37% -> -9.44% | 92.86% -> 92.31% | retest |
| 2025-01-01 -> 2025-09-01 | yes | 33.00 -> 29.00 | 15.15% -> 20.69% | 0.43 -> 0.65 | -1.35 -> -0.69 | 19.84% -> 15.99% | -15.27% -> -7.84% | 84.85% -> 79.31% | retest |
| 2025-09-01 -> 2026-06-01 | yes | 20.00 -> 20.00 | 15.00% -> 15.00% | 0.45 -> 0.45 | -1.09 -> -1.09 | 18.06% -> 18.06% | -10.09% -> -10.09% | 85.00% -> 85.00% | retest |

## Source Reports

- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-09\abtest_dynamic_universe_history_365_2025-01-01_2025-06-01_v1.md`
- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-09\abtest_dynamic_universe_history_365_2025-01-01_2025-09-01_v1.md`
- `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-09\abtest_dynamic_universe_history_365_2025-09-01_2026-06-01_v1.md`

## Decision Rule

- 汇总报告只给出 `candidate_keep_review`、`retest` 或 `reject_candidate`，不会自动修改默认配置。
- 至少需要多个充足样本时段共同改善净收益、Profit factor 和最大回撤，才会标记 `candidate_keep_review`。
- 任一 variant 样本不足时，结论应偏向 `retest`。

## Raw Summary

```json
{
  "experiment_id": "history_365",
  "mode": "dynamic_universe",
  "periods": 3,
  "sufficient_periods": 2,
  "net_improved_periods": 1,
  "profit_factor_improved_periods": 1,
  "drawdown_improved_periods": 1,
  "variant_under_sample_periods": 1,
  "verdict": "retest",
  "reason": "At least one variant period is below the closed-trade sample threshold.",
  "records": [
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-09\\abtest_dynamic_universe_history_365_2025-01-01_2025-06-01_v1.md",
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
        "trades": 33,
        "closed_trades": 13,
        "open_trades": 2,
        "win_rate": 7.6923076923076925,
        "profit_factor": 0.21407967896549948,
        "avg_r": -0.7333807512031822,
        "net_return_pct": -9.442371705046193,
        "max_drawdown": 1193.8501082922849,
        "max_drawdown_pct": 11.655562465218892,
        "intrabar_max_drawdown": 1158.6761244343452,
        "intrabar_max_drawdown_pct": 11.383042786068359,
        "tp1_rate": 7.6923076923076925,
        "tp2_rate": 7.6923076923076925,
        "stop_rate": 92.3076923076923,
        "fee_drag": 19.187079623919203,
        "tail_max_loss": -108.1494009784496,
        "cagr": -21.31745342325342,
        "sharpe": -2.1468719895714745,
        "sortino": -1.9292377720401066,
        "exposure_pct": 81.56732891832229,
        "turnover": 1.6120099183230596,
        "sample_sufficient": false,
        "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
      }
    },
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-09\\abtest_dynamic_universe_history_365_2025-01-01_2025-09-01_v1.md",
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
        "trades": 95,
        "closed_trades": 29,
        "open_trades": 2,
        "win_rate": 20.689655172413794,
        "profit_factor": 0.6537749086019617,
        "avg_r": -0.25976802029884577,
        "net_return_pct": -7.8398505279532955,
        "max_drawdown": 1637.6181040087813,
        "max_drawdown_pct": 15.988070841448218,
        "intrabar_max_drawdown": 1605.3854774347492,
        "intrabar_max_drawdown_pct": 15.771595869116409,
        "tp1_rate": 24.137931034482758,
        "tp2_rate": 20.689655172413794,
        "stop_rate": 79.3103448275862,
        "fee_drag": 36.9566451959728,
        "tail_max_loss": -108.1494009784496,
        "cagr": -11.541046087396879,
        "sharpe": -0.6893787123136389,
        "sortino": -0.7664379429405735,
        "exposure_pct": 88.54595336076817,
        "turnover": 3.114843867521111,
        "sample_sufficient": true,
        "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
      }
    },
    {
      "path": "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-09\\abtest_dynamic_universe_history_365_2025-09-01_2026-06-01_v1.md",
      "start": "2025-09-01",
      "end": "2026-06-01",
      "sample_sufficient": true,
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
        "trades": 35,
        "closed_trades": 20,
        "open_trades": 3,
        "win_rate": 15.0,
        "profit_factor": 0.45147171647807804,
        "avg_r": -0.4790107899968318,
        "net_return_pct": -10.087210136761993,
        "max_drawdown": 1922.8512378782762,
        "max_drawdown_pct": 18.063909579509176,
        "intrabar_max_drawdown": 1906.3776592002814,
        "intrabar_max_drawdown_pct": 17.98864220517264,
        "tp1_rate": 25.0,
        "tp2_rate": 15.0,
        "stop_rate": 85.0,
        "fee_drag": 41.58467837200188,
        "tail_max_loss": -112.37720364588355,
        "cagr": -13.251998343140226,
        "sharpe": -1.0856809535808845,
        "sortino": -1.020027187711169,
        "exposure_pct": 72.4053724053724,
        "turnover": 3.4492407292598326,
        "sample_sufficient": true,
        "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
      }
    }
  ]
}
```
