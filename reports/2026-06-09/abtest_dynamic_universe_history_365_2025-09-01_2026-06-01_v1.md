---
created: 2026-06-09 02:07:07 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: history_365
baseline_run_id: 3ad4659b89d8
variant_run_id: 266ed68dc7a6
changed_param: analysis.min_history_days
old_value: 180
new_value: 365
sample_sufficient: true
universe_mode: dynamic
verdict: retest
report_version: v1
---

# A/B 实验报告 history_365 v1

- experiment_id: `history_365`
- description: Test min_history_days 365 versus baseline 180.
- baseline_run_id: `3ad4659b89d8`
- variant_run_id: `266ed68dc7a6`
- symbols: `0GUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `2ZUSDT`, `AAVEUSDT`, `ACEUSDT`, `ADAUSDT`, `AEVOUSDT`, `AIGENSYNUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALCXUSDT`, `ALGOUSDT`, `ALICEUSDT`, `ALLOUSDT`, `ALPINEUSDT`, `ALTUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARKMUSDT`, `ARPAUSDT`, `ARUSDT`, `ASTERUSDT`, `ATOMUSDT`, `ATUSDT`, `AUCTIONUSDT`, `AUSDT`, `AVAXUSDT`, `AVNTUSDT`, `AWEUSDT`, `AXSUSDT`, `BABYUSDT`, `BANANAS31USDT`, `BARDUSDT`, `BATUSDT`, `BBUSDT`, `BCHUSDT`, `BELUSDT`, `BERAUSDT`, `BIOUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BREVUSDT`, `BROCCOLI714USDT`, `BTCUSDT`, `C98USDT`, `CAKEUSDT`, `CELOUSDT`, `CFGUSDT`, `CFXUSDT`, `CHIPUSDT`, `CHZUSDT`, `COSUSDT`, `COTIUSDT`, `COWUSDT`
- universe_mode: dynamic
- time_periods_tested: `2025-09-01` -> `2026-06-01`
- changed_param: `analysis.min_history_days`
- old_value: `180`
- new_value: `365`
- sample_sufficient: true
- possible_over_filtering: false
- verdict: `retest`
- reason: Automatic report does not assign keep; review across additional time periods before adopting.

## Dynamic Universe Metadata

- baseline_master_count: 100
- variant_master_count: 100
- baseline_source_limit: 100
- variant_source_limit: 100
- shared_master_expected: true (A/B runner builds the dynamic symbol master once before baseline and variant.)
- baseline_universe_refreshes: 274
- variant_universe_refreshes: 274

## 指标对比

| Metric | Baseline | Variant | Delta |
|---|---:|---:|---:|
| closed_trades | 20.00 | 20.00 | 0.00 |
| stop_rate | 85.00% | 85.00% | 0.00% |
| profit_factor | 0.45 | 0.45 | 0.00 |
| avg_r | -0.48 | -0.48 | 0.00 |
| max_drawdown_pct | 18.06% | 18.06% | -0.00% |
| net_return_pct | -10.09% | -10.09% | 0.00% |
| sharpe | -1.09 | -1.09 | -0.00 |
| first_trade_created_at | 2025-09-05T08:00:00+00:00 | 2025-09-05T08:00:00+00:00 | n/a |

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
```
