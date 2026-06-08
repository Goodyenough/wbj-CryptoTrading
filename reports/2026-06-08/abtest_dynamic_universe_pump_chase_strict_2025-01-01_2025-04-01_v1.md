---
created: 2026-06-08 23:26:46 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: pump_chase_strict
baseline_run_id: 0e45b2c869c6
variant_run_id: d09dfe156d16
changed_param: analysis.pump_chase_24h_pct, analysis.pump_chase_distance_pct, analysis.pump_chase_penalty
old_value: 20.0, 8.0, 8.0
new_value: 12.0, 6.0, 12.0
sample_sufficient: false
universe_mode: dynamic
verdict: retest
report_version: v1
---

# A/B 实验报告 pump_chase_strict v1

- experiment_id: `pump_chase_strict`
- description: Test stricter pump-chasing score penalties.
- baseline_run_id: `0e45b2c869c6`
- variant_run_id: `d09dfe156d16`
- symbols: `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1MBABYDOGEUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACHUSDT`, `ACTUSDT`, `ACXUSDT`, `ADAUSDT`, `AGLDUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALGOUSDT`, `AMPUSDT`, `ANIMEUSDT`, `ANKRUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AUDIOUSDT`, `AVAXUSDT`, `BANANAUSDT`
- universe_mode: dynamic
- time_periods_tested: `2025-01-01` -> `2025-04-01`
- changed_param: `analysis.pump_chase_24h_pct, analysis.pump_chase_distance_pct, analysis.pump_chase_penalty`
- old_value: `20.0, 8.0, 8.0`
- new_value: `12.0, 6.0, 12.0`
- sample_sufficient: false
- possible_over_filtering: false
- verdict: `retest`
- reason: Variant closed_trades is below 20, so the sample is insufficient for a keep decision.

## Dynamic Universe Metadata

- baseline_master_count: 60
- variant_master_count: 60
- baseline_source_limit: 60
- variant_source_limit: 60
- shared_master_expected: true (A/B runner builds the dynamic symbol master once before baseline and variant.)
- baseline_universe_refreshes: 91
- variant_universe_refreshes: 91

## 指标对比

| Metric | Baseline | Variant | Delta |
|---|---:|---:|---:|
| closed_trades | 5.00 | 5.00 | 0.00 |
| stop_rate | 100.00% | 100.00% | 0.00% |
| profit_factor | 0.00 | 0.00 | 0.00 |
| avg_r | -1.02 | -1.02 | 0.00 |
| max_drawdown_pct | 5.74% | 5.74% | 0.00% |
| net_return_pct | -5.13% | -5.13% | 0.00% |
| sharpe | -3.34 | -3.34 | 0.00 |
| first_trade_created_at | 2025-01-04T04:00:00+00:00 | 2025-01-04T04:00:00+00:00 | n/a |

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
    "trades": 7,
    "closed_trades": 5,
    "open_trades": 0,
    "win_rate": 0.0,
    "profit_factor": 0.0,
    "avg_r": -1.0224265038911926,
    "net_return_pct": -5.134578897213238,
    "max_drawdown": 577.7765036561323,
    "max_drawdown_pct": 5.740840744609944,
    "intrabar_max_drawdown": 540.6211118453539,
    "intrabar_max_drawdown_pct": 5.391565888271592,
    "tp1_rate": 0.0,
    "tp2_rate": 0.0,
    "stop_rate": 100.0,
    "fee_drag": 6.654926061944943,
    "tail_max_loss": -103.87799694393186,
    "cagr": -19.246756638515805,
    "sharpe": -3.3380459282465087,
    "sortino": -0.7560865649789468,
    "exposure_pct": 5.0,
    "turnover": 0.5115520732574516,
    "sample_sufficient": false,
    "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
  },
  "variant": {
    "trades": 7,
    "closed_trades": 5,
    "open_trades": 0,
    "win_rate": 0.0,
    "profit_factor": 0.0,
    "avg_r": -1.0224265038911926,
    "net_return_pct": -5.134578897213238,
    "max_drawdown": 577.7765036561323,
    "max_drawdown_pct": 5.740840744609944,
    "intrabar_max_drawdown": 540.6211118453539,
    "intrabar_max_drawdown_pct": 5.391565888271592,
    "tp1_rate": 0.0,
    "tp2_rate": 0.0,
    "stop_rate": 100.0,
    "fee_drag": 6.654926061944943,
    "tail_max_loss": -103.87799694393186,
    "cagr": -19.246756638515805,
    "sharpe": -3.3380459282465087,
    "sortino": -0.7560865649789468,
    "exposure_pct": 5.0,
    "turnover": 0.5115520732574516,
    "sample_sufficient": false,
    "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
  }
}
```
