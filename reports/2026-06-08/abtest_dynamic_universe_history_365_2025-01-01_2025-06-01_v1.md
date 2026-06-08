---
created: 2026-06-08 23:52:58 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: history_365
baseline_run_id: c203a76b4772
variant_run_id: 5b18cca9384b
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
- baseline_run_id: `c203a76b4772`
- variant_run_id: `5b18cca9384b`
- symbols: `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1MBABYDOGEUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACHUSDT`, `ACTUSDT`, `ACXUSDT`, `ADAUSDT`, `AEVOUSDT`, `AGLDUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALGOUSDT`, `ALPINEUSDT`, `AMPUSDT`, `ANIMEUSDT`, `ANKRUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARDRUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ASRUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AUDIOUSDT`, `AVAXUSDT`, `BABYUSDT`, `BANANAUSDT`
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

- baseline_master_count: 60
- variant_master_count: 60
- baseline_source_limit: 60
- variant_source_limit: 60
- shared_master_expected: true (A/B runner builds the dynamic symbol master once before baseline and variant.)
- baseline_universe_refreshes: 152
- variant_universe_refreshes: 152

## 指标对比

| Metric | Baseline | Variant | Delta |
|---|---:|---:|---:|
| closed_trades | 11.00 | 11.00 | 0.00 |
| stop_rate | 90.91% | 90.91% | 0.00% |
| profit_factor | 0.25 | 0.24 | -0.00 |
| avg_r | -0.69 | -0.70 | -0.00 |
| max_drawdown_pct | 8.50% | 9.20% | 0.70% |
| net_return_pct | -7.74% | -7.77% | -0.03% |
| sharpe | -1.42 | -1.75 | -0.33 |
| first_trade_created_at | 2025-01-04T04:00:00+00:00 | 2025-01-04T04:00:00+00:00 | n/a |

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
    "trades": 17,
    "closed_trades": 11,
    "open_trades": 1,
    "win_rate": 9.090909090909092,
    "profit_factor": 0.2471083616510551,
    "avg_r": -0.6944041511181808,
    "net_return_pct": -7.736150206112402,
    "max_drawdown": 855.4466333542205,
    "max_drawdown_pct": 8.499796818532653,
    "intrabar_max_drawdown": 893.9794118879781,
    "intrabar_max_drawdown_pct": 8.91557654028702,
    "tp1_rate": 18.181818181818183,
    "tp2_rate": 9.090909090909092,
    "stop_rate": 90.9090909090909,
    "fee_drag": 12.568717303431935,
    "tail_max_loss": -103.87799694393186,
    "cagr": -17.686007410690685,
    "sharpe": -1.4187274002601735,
    "sortino": -0.6878280122759884,
    "exposure_pct": 16.777041942604857,
    "turnover": 1.0579992339016693,
    "sample_sufficient": false,
    "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
  },
  "variant": {
    "trades": 16,
    "closed_trades": 11,
    "open_trades": 1,
    "win_rate": 9.090909090909092,
    "profit_factor": 0.24418161327206594,
    "avg_r": -0.6952365376294275,
    "net_return_pct": -7.766238185871977,
    "max_drawdown": 925.9393188264348,
    "max_drawdown_pct": 9.200218657072343,
    "intrabar_max_drawdown": 952.4324222210635,
    "intrabar_max_drawdown_pct": 9.498523172731518,
    "tp1_rate": 9.090909090909092,
    "tp2_rate": 9.090909090909092,
    "stop_rate": 90.9090909090909,
    "fee_drag": 13.061646341038537,
    "tail_max_loss": -103.87799694393186,
    "cagr": -17.750878423076145,
    "sharpe": -1.7463981524330612,
    "sortino": -0.858549813973611,
    "exposure_pct": 16.55629139072848,
    "turnover": 1.0920500549970518,
    "sample_sufficient": false,
    "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
  }
}
```
