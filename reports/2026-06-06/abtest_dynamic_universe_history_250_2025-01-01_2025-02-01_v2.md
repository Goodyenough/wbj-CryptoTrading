---
created: 2026-06-06 23:47:03 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: history_250
baseline_run_id: 8b15c912c927
variant_run_id: 4e5b430ce360
changed_param: analysis.min_history_days
old_value: 180
new_value: 250
sample_sufficient: false
universe_mode: dynamic
verdict: retest
report_version: v2
---

# A/B 实验报告 history_250 v2

- experiment_id: `history_250`
- description: Test min_history_days 250 versus baseline 180.
- baseline_run_id: `8b15c912c927`
- variant_run_id: `4e5b430ce360`
- symbols: `1000SATSUSDT`, `1MBABYDOGEUSDT`, `AAVEUSDT`, `ACHUSDT`, `ACTUSDT`, `ADAUSDT`, `AGLDUSDT`, `AIUSDT`, `AIXBTUSDT`
- universe_mode: dynamic
- time_periods_tested: `2025-01-01` -> `2025-02-01`
- changed_param: `analysis.min_history_days`
- old_value: `180`
- new_value: `250`
- sample_sufficient: false
- possible_over_filtering: false
- verdict: `retest`
- reason: Variant closed_trades is below 20, so the sample is insufficient for a keep decision.

## Dynamic Universe Metadata

- baseline_master_count: 20
- variant_master_count: 20
- baseline_source_limit: 20
- variant_source_limit: 20
- shared_master_expected: true (A/B runner builds the dynamic symbol master once before baseline and variant.)
- baseline_universe_refreshes: 32
- variant_universe_refreshes: 32

## 指标对比

| Metric | Baseline | Variant | Delta |
|---|---:|---:|---:|
| closed_trades | 3.00 | 3.00 | 0.00 |
| stop_rate | 100.00% | 100.00% | 0.00% |
| profit_factor | 0.00 | 0.00 | 0.00 |
| avg_r | -1.02 | -1.02 | 0.00 |
| max_drawdown_pct | 3.46% | 3.46% | 0.00% |
| net_return_pct | -3.08% | -3.08% | 0.00% |
| sharpe | -6.10 | -6.10 | 0.00 |
| first_trade_created_at | 2025-01-04T04:00:00+00:00 | 2025-01-04T04:00:00+00:00 | n/a |

## 样本规则

- closed_trades < 20 时，默认 verdict 为 `retest`。
- 交易数下降超过 50% 时，标记 possible_over_filtering=true。
- 自动报告不会直接写 `keep`；采用默认策略前需要跨时段复测和人工复盘。

## 变更明细

| changed_param | old_value | new_value |
|---|---:|---:|
| `analysis.min_history_days` | `180` | `250` |

## Raw Metrics

```json
{
  "baseline": {
    "trades": 3,
    "closed_trades": 3,
    "open_trades": 0,
    "win_rate": 0.0,
    "profit_factor": 0.0,
    "avg_r": -1.0209655914347386,
    "net_return_pct": -3.0772943863704105,
    "max_drawdown": 347.11505443724127,
    "max_drawdown_pct": 3.4575328383735373,
    "intrabar_max_drawdown": 334.89266076107197,
    "intrabar_max_drawdown_pct": 3.3398544866823503,
    "tp1_rate": 0.0,
    "tp2_rate": 0.0,
    "stop_rate": 100.0,
    "fee_drag": 3.7366586821624113,
    "tail_max_loss": -103.37503580332037,
    "cagr": -30.789569348903324,
    "sharpe": -6.100720333001323,
    "sortino": -2.6633005165607546,
    "exposure_pct": 14.516129032258066,
    "turnover": 0.2886179615798065,
    "sample_sufficient": false,
    "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
  },
  "variant": {
    "trades": 3,
    "closed_trades": 3,
    "open_trades": 0,
    "win_rate": 0.0,
    "profit_factor": 0.0,
    "avg_r": -1.0209655914347386,
    "net_return_pct": -3.0772943863704105,
    "max_drawdown": 347.11505443724127,
    "max_drawdown_pct": 3.4575328383735373,
    "intrabar_max_drawdown": 334.89266076107197,
    "intrabar_max_drawdown_pct": 3.3398544866823503,
    "tp1_rate": 0.0,
    "tp2_rate": 0.0,
    "stop_rate": 100.0,
    "fee_drag": 3.7366586821624113,
    "tail_max_loss": -103.37503580332037,
    "cagr": -30.789569348903324,
    "sharpe": -6.100720333001323,
    "sortino": -2.6633005165607546,
    "exposure_pct": 14.516129032258066,
    "turnover": 0.2886179615798065,
    "sample_sufficient": false,
    "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
  }
}
```
