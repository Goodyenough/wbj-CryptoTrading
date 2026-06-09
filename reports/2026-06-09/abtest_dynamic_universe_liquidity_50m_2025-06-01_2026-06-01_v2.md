---
created: 2026-06-09 12:58:47 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: liquidity_50m
baseline_run_id: f0fd8b2b13cf
variant_run_id: 01e07460c41d
changed_param: market.min_quote_volume, market.min_trades
old_value: 30000000.0, 30000
new_value: 50000000, 50000
sample_sufficient: true
universe_mode: dynamic
verdict: retest
report_version: v2
---

# A/B 实验报告 liquidity_50m v2

- experiment_id: `liquidity_50m`
- description: Test higher liquidity thresholds.
- baseline_run_id: `f0fd8b2b13cf`
- variant_run_id: `01e07460c41d`
- symbols: `0GUSDT`, `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1INCHUSDT`, `2ZUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACHUSDT`, `ADAUSDT`, `AEVOUSDT`, `AIGENSYNUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALCXUSDT`, `ALGOUSDT`, `ALICEUSDT`, `ALLOUSDT`, `ALPINEUSDT`, `ALTUSDT`, `ANIMEUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ASRUSDT`, `ASTERUSDT`, `ATMUSDT`, `ATOMUSDT`, `ATUSDT`, `AUCTIONUSDT`, `AUSDT`, `AVAXUSDT`, `AVNTUSDT`, `AWEUSDT`, `AXLUSDT`, `AXSUSDT`, `BABYUSDT`, `BANANAS31USDT`, `BARDUSDT`, `BATUSDT`, `BBUSDT`, `BCHUSDT`, `BELUSDT`, `BERAUSDT`, `BIOUSDT`, `BMTUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BREVUSDT`, `BROCCOLI714USDT`, `BTCUSDT`, `C98USDT`, `CAKEUSDT`, `CELOUSDT`, `CFGUSDT`, `CFXUSDT`, `CHIPUSDT`, `CHZUSDT`, `CKBUSDT`, `COMPUSDT`, `COSUSDT`, `COTIUSDT`, `COWUSDT`
- universe_mode: dynamic
- time_periods_tested: `2025-06-01` -> `2026-06-01`
- changed_param: `market.min_quote_volume, market.min_trades`
- old_value: `30000000.0, 30000`
- new_value: `50000000, 50000`
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
- baseline_universe_refreshes: 366
- variant_universe_refreshes: 366

## 指标对比

| Metric | Baseline | Variant | Delta |
|---|---:|---:|---:|
| closed_trades | 36.00 | 38.00 | 2.00 |
| stop_rate | 77.78% | 76.32% | -1.46% |
| profit_factor | 0.72 | 0.81 | 0.09 |
| avg_r | -0.21 | -0.13 | 0.08 |
| max_drawdown_pct | 19.70% | 18.76% | -0.94% |
| net_return_pct | -8.77% | -5.53% | 3.24% |
| sharpe | -0.53 | -0.29 | 0.24 |
| first_trade_created_at | 2025-06-06T16:00:00+00:00 | 2025-06-06T16:00:00+00:00 | n/a |

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
}
```
