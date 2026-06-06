---
created: 2026-06-06 20:33:28 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: pump_chase_strict
baseline_run_id: 60460911376a
variant_run_id: f588f42650a3
changed_param: analysis.pump_chase_24h_pct, analysis.pump_chase_distance_pct, analysis.pump_chase_penalty
old_value: 20.0, 8.0, 8.0
new_value: 12.0, 6.0, 12.0
sample_sufficient: false
verdict: retest
report_version: v2
---

# A/B 实验报告 pump_chase_strict v2

- experiment_id: `pump_chase_strict`
- description: Test stricter pump-chasing score penalties.
- baseline_run_id: `60460911376a`
- variant_run_id: `f588f42650a3`
- symbols: `BTCUSDT`, `ETHUSDT`, `SOLUSDT`, `BNBUSDT`, `XRPUSDT`, `DOGEUSDT`, `ADAUSDT`, `AVAXUSDT`, `TRXUSDT`, `LINKUSDT`, `NEARUSDT`, `ONDOUSDT`, `ZECUSDT`
- time_periods_tested: `2025-01-01` -> `2025-06-01`
- changed_param: `analysis.pump_chase_24h_pct, analysis.pump_chase_distance_pct, analysis.pump_chase_penalty`
- old_value: `20.0, 8.0, 8.0`
- new_value: `12.0, 6.0, 12.0`
- sample_sufficient: false
- possible_over_filtering: false
- verdict: `retest`
- reason: Variant closed_trades is below 20, so the sample is insufficient for a keep decision.

## 指标对比

| Metric | Baseline | Variant | Delta |
|---|---:|---:|---:|
| closed_trades | 18.00 | 18.00 | 0.00 |
| stop_rate | 77.78% | 77.78% | 0.00% |
| profit_factor | 0.72 | 0.72 | 0.00 |
| avg_r | -0.21 | -0.21 | 0.00 |
| max_drawdown_pct | 9.44% | 9.44% | 0.00% |
| net_return_pct | -4.34% | -4.34% | 0.00% |
| sharpe | -0.71 | -0.71 | 0.00 |
| first_trade_created_at | 2025-01-02T12:00:00+00:00 | 2025-01-02T12:00:00+00:00 | n/a |

## 样本规则

- closed_trades < 20 时，默认 verdict 为 `retest`。
- 交易数下降超过 50% 时，标记 possible_over_filtering=true。
- 自动报告不会直接写 `keep`；采用默认策略前需要跨时段复测和人工复盘。

## 变更明细

| changed_param | old_value | new_value |
|---|---:|---:|
| `analysis.pump_chase_24h_pct` | `20.0` | `12.0` |
| `analysis.pump_chase_distance_pct` | `8.0` | `6.0` |
| `analysis.pump_chase_penalty` | `8.0` | `12.0` |

## Raw Metrics

```json
{
  "baseline": {
    "trades": 56,
    "closed_trades": 18,
    "open_trades": 2,
    "win_rate": 22.22222222222222,
    "profit_factor": 0.7194442998005088,
    "avg_r": -0.21092171037369173,
    "net_return_pct": -4.337312186708864,
    "max_drawdown": 966.2559525448542,
    "max_drawdown_pct": 9.442730807022857,
    "intrabar_max_drawdown": 904.0642999685533,
    "intrabar_max_drawdown_pct": 8.891957878695973,
    "tp1_rate": 22.22222222222222,
    "tp2_rate": 22.22222222222222,
    "stop_rate": 77.77777777777779,
    "fee_drag": 25.66467923230345,
    "tail_max_loss": -106.95560225203097,
    "cagr": -10.163958969021113,
    "sharpe": -0.7131843222168059,
    "sortino": -0.7097460199845309,
    "exposure_pct": 82.45033112582782,
    "turnover": 2.248445096954121,
    "sample_sufficient": false,
    "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
  },
  "variant": {
    "trades": 56,
    "closed_trades": 18,
    "open_trades": 2,
    "win_rate": 22.22222222222222,
    "profit_factor": 0.7194442998005088,
    "avg_r": -0.21092171037369173,
    "net_return_pct": -4.337312186708864,
    "max_drawdown": 966.2559525448542,
    "max_drawdown_pct": 9.442730807022857,
    "intrabar_max_drawdown": 904.0642999685533,
    "intrabar_max_drawdown_pct": 8.891957878695973,
    "tp1_rate": 22.22222222222222,
    "tp2_rate": 22.22222222222222,
    "stop_rate": 77.77777777777779,
    "fee_drag": 25.66467923230345,
    "tail_max_loss": -106.95560225203097,
    "cagr": -10.163958969021113,
    "sharpe": -0.7131843222168059,
    "sortino": -0.7097460199845309,
    "exposure_pct": 82.45033112582782,
    "turnover": 2.248445096954121,
    "sample_sufficient": false,
    "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
  }
}
```
