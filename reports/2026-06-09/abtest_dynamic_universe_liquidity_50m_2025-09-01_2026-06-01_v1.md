---
created: 2026-06-09 02:18:57 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: liquidity_50m
baseline_run_id: 0e425690504c
variant_run_id: b6a1661f9faa
changed_param: market.min_quote_volume, market.min_trades
old_value: 30000000.0, 30000
new_value: 50000000, 50000
sample_sufficient: false
universe_mode: dynamic
verdict: retest
report_version: v1
---

# A/B 实验报告 liquidity_50m v1

- experiment_id: `liquidity_50m`
- description: Test higher liquidity thresholds.
- baseline_run_id: `0e425690504c`
- variant_run_id: `b6a1661f9faa`
- symbols: `0GUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `2ZUSDT`, `AAVEUSDT`, `ACEUSDT`, `ADAUSDT`, `AEVOUSDT`, `AIGENSYNUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALCXUSDT`, `ALGOUSDT`, `ALICEUSDT`, `ALLOUSDT`, `ALPINEUSDT`, `ALTUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARKMUSDT`, `ARPAUSDT`, `ARUSDT`, `ASTERUSDT`, `ATOMUSDT`, `ATUSDT`, `AUCTIONUSDT`, `AUSDT`, `AVAXUSDT`, `AVNTUSDT`, `AWEUSDT`, `AXSUSDT`, `BABYUSDT`, `BANANAS31USDT`, `BARDUSDT`, `BATUSDT`, `BBUSDT`, `BCHUSDT`, `BELUSDT`, `BERAUSDT`, `BIOUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BREVUSDT`, `BROCCOLI714USDT`, `BTCUSDT`, `C98USDT`, `CAKEUSDT`, `CELOUSDT`, `CFGUSDT`, `CFXUSDT`, `CHIPUSDT`, `CHZUSDT`, `COSUSDT`, `COTIUSDT`, `COWUSDT`
- universe_mode: dynamic
- time_periods_tested: `2025-09-01` -> `2026-06-01`
- changed_param: `market.min_quote_volume, market.min_trades`
- old_value: `30000000.0, 30000`
- new_value: `50000000, 50000`
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
- baseline_universe_refreshes: 274
- variant_universe_refreshes: 274

## 指标对比

| Metric | Baseline | Variant | Delta |
|---|---:|---:|---:|
| closed_trades | 20.00 | 19.00 | -1.00 |
| stop_rate | 85.00% | 84.21% | -0.79% |
| profit_factor | 0.45 | 0.48 | 0.03 |
| avg_r | -0.48 | -0.45 | 0.03 |
| max_drawdown_pct | 18.06% | 15.99% | -2.08% |
| net_return_pct | -10.09% | -8.23% | 1.86% |
| sharpe | -1.09 | -0.89 | 0.20 |
| first_trade_created_at | 2025-09-05T08:00:00+00:00 | 2025-09-05T08:00:00+00:00 | n/a |

## 样本规则

- closed_trades < 20 时，默认 verdict 为 `retest`。
- 交易数下降超过 50% 时，标记 possible_over_filtering=true。
- 自动报告不会直接写 `keep`；采用默认策略前需要跨时段复测和人工复盘。

## 变更明细

| changed_param | old_value | new_value |
|---|---:|---:|
| `market.min_quote_volume` | `30000000.0` | `50000000` |
| `market.min_trades` | `30000` | `50000` |

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
```
