---
created: 2026-06-09 00:29:38 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: history_365
baseline_run_id: 54980e35da57
variant_run_id: 1bf4603379ae
changed_param: analysis.min_history_days
old_value: 180
new_value: 365
sample_sufficient: false
universe_mode: dynamic
verdict: retest
report_version: v1
---

# A/B 实验报告 history_365 v1

- experiment_id: `history_365`
- description: Test min_history_days 365 versus baseline 180.
- baseline_run_id: `54980e35da57`
- variant_run_id: `1bf4603379ae`
- symbols: `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1MBABYDOGEUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACHUSDT`, `ACTUSDT`, `ACXUSDT`, `ADAUSDT`, `AEVOUSDT`, `AGLDUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALGOUSDT`, `ALPINEUSDT`, `AMPUSDT`, `ANIMEUSDT`, `ANKRUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARDRUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ASRUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AUDIOUSDT`, `AVAXUSDT`, `BABYUSDT`, `BANANAUSDT`, `BCHUSDT`, `BEAMXUSDT`, `BERAUSDT`, `BIOUSDT`, `BMTUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BTCUSDT`, `C98USDT`, `CAKEUSDT`, `CATIUSDT`, `CETUSUSDT`, `CFXUSDT`, `CGPTUSDT`, `CKBUSDT`, `COMPUSDT`, `COOKIEUSDT`, `COWUSDT`
- universe_mode: dynamic
- time_periods_tested: `2025-01-01` -> `2025-06-01`
- changed_param: `analysis.min_history_days`
- old_value: `180`
- new_value: `365`
- sample_sufficient: false
- possible_over_filtering: false
- verdict: `retest`
- reason: Variant closed_trades is below 20, so the sample is insufficient for a keep decision.

## Dynamic Universe Metadata

- baseline_master_count: 100
- variant_master_count: 100
- baseline_source_limit: 100
- variant_source_limit: 100
- shared_master_expected: true (A/B runner builds the dynamic symbol master once before baseline and variant.)
- baseline_universe_refreshes: 152
- variant_universe_refreshes: 152

## 指标对比

| Metric | Baseline | Variant | Delta |
|---|---:|---:|---:|
| closed_trades | 14.00 | 13.00 | -1.00 |
| stop_rate | 92.86% | 92.31% | -0.55% |
| profit_factor | 0.20 | 0.21 | 0.02 |
| avg_r | -0.75 | -0.73 | 0.02 |
| max_drawdown_pct | 12.67% | 11.66% | -1.02% |
| net_return_pct | -10.37% | -9.44% | 0.92% |
| sharpe | -2.04 | -2.15 | -0.11 |
| first_trade_created_at | 2025-01-02T12:00:00+00:00 | 2025-01-02T12:00:00+00:00 | n/a |

## 样本规则

- closed_trades < 20 时，默认 verdict 为 `retest`。
- 交易数下降超过 50% 时，标记 possible_over_filtering=true。
- 自动报告不会直接写 `keep`；采用默认策略前需要跨时段复测和人工复盘。

## 变更明细

| changed_param | old_value | new_value |
|---|---:|---:|
| `analysis.min_history_days` | `180` | `365` |

## Raw Metrics

```json
{
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
}
```
