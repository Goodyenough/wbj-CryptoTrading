---
created: 2026-06-09 14:06:30 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: liquidity_50m
baseline_run_id: e745313c3727
variant_run_id: 838e78b04c3a
changed_param: market.min_quote_volume, market.min_trades
old_value: 30000000.0, 30000
new_value: 50000000, 50000
sample_sufficient: true
universe_mode: dynamic
verdict: retest
report_version: v3
---

# A/B 实验报告 liquidity_50m v3

- experiment_id: `liquidity_50m`
- description: Test higher liquidity thresholds.
- baseline_run_id: `e745313c3727`
- variant_run_id: `838e78b04c3a`
- symbols: `0GUSDT`, `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1INCHUSDT`, `2ZUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACHUSDT`, `ADAUSDT`, `AEVOUSDT`, `AIGENSYNUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALCXUSDT`, `ALGOUSDT`, `ALICEUSDT`, `ALLOUSDT`, `ALPINEUSDT`, `ALTUSDT`, `ANIMEUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ASRUSDT`, `ASTERUSDT`, `ATMUSDT`, `ATOMUSDT`, `ATUSDT`, `AUCTIONUSDT`, `AUSDT`, `AVAXUSDT`, `AVNTUSDT`, `AWEUSDT`, `AXLUSDT`, `AXSUSDT`, `BABYUSDT`, `BANANAS31USDT`, `BARDUSDT`, `BATUSDT`, `BBUSDT`, `BCHUSDT`, `BELUSDT`, `BERAUSDT`, `BIOUSDT`, `BMTUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BREVUSDT`, `BROCCOLI714USDT`, `BTCUSDT`, `C98USDT`, `CAKEUSDT`, `CELOUSDT`, `CFGUSDT`, `CFXUSDT`, `CHIPUSDT`, `CHZUSDT`, `CKBUSDT`, `COMPUSDT`, `COSUSDT`, `COTIUSDT`, `COWUSDT`, `CRVUSDT`, `CTSIUSDT`, `CUSDT`, `CYBERUSDT`, `DASHUSDT`, `DCRUSDT`, `DEXEUSDT`, `DIAUSDT`, `DOGEUSDT`, `DOGSUSDT`, `DOLOUSDT`, `DOTUSDT`, `DUSDT`, `DUSKUSDT`, `DYDXUSDT`, `DYMUSDT`, `EDENUSDT`, `EDUUSDT`, `EIGENUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSOUSDT`, `ENSUSDT`, `EPICUSDT`, `ERAUSDT`, `ESPUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `EULUSDT`, `FETUSDT`, `FFUSDT`, `FIDAUSDT`, `FILUSDT`, `FLOKIUSDT`, `FLOWUSDT`, `FLUXUSDT`, `FOGOUSDT`, `FORMUSDT`, `FRAXUSDT`, `FUSDT`, `GALAUSDT`
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

- baseline_master_count: 150
- variant_master_count: 150
- baseline_source_limit: 150
- variant_source_limit: 150
- shared_master_expected: true (A/B runner builds the dynamic symbol master once before baseline and variant.)
- baseline_universe_refreshes: 366
- variant_universe_refreshes: 366

## 指标对比

| Metric | Baseline | Variant | Delta |
|---|---:|---:|---:|
| closed_trades | 55.00 | 56.00 | 1.00 |
| stop_rate | 78.18% | 76.79% | -1.40% |
| profit_factor | 0.70 | 0.75 | 0.06 |
| avg_r | -0.22 | -0.18 | 0.05 |
| max_drawdown_pct | 26.71% | 24.92% | -1.79% |
| net_return_pct | -13.04% | -10.31% | 2.73% |
| sharpe | -0.65 | -0.48 | 0.17 |
| first_trade_created_at | 2025-06-02T16:00:00+00:00 | 2025-06-02T16:00:00+00:00 | n/a |

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
    "trades": 185,
    "closed_trades": 55,
    "open_trades": 3,
    "win_rate": 21.818181818181817,
    "profit_factor": 0.6971178307001836,
    "avg_r": -0.2241219405403126,
    "net_return_pct": -13.03576231812318,
    "max_drawdown": 3040.594745082548,
    "max_drawdown_pct": 26.712317955989878,
    "intrabar_max_drawdown": 2921.2848075155507,
    "intrabar_max_drawdown_pct": 25.96805481972579,
    "tp1_rate": 32.72727272727273,
    "tp2_rate": 21.818181818181817,
    "stop_rate": 78.18181818181819,
    "fee_drag": 90.95372387204374,
    "tail_max_loss": -116.33760689127996,
    "cagr": -13.03576231812318,
    "sharpe": -0.649847198418506,
    "sortino": -0.7333287352121214,
    "exposure_pct": 86.11872146118722,
    "turnover": 7.618009571618466,
    "sample_sufficient": true,
    "sample_warning": ""
  },
  "variant": {
    "trades": 120,
    "closed_trades": 56,
    "open_trades": 2,
    "win_rate": 23.214285714285715,
    "profit_factor": 0.7529602396706798,
    "avg_r": -0.17589781865354817,
    "net_return_pct": -10.306134421864677,
    "max_drawdown": 2839.947311838918,
    "max_drawdown_pct": 24.920342553022856,
    "intrabar_max_drawdown": 2780.0288582567027,
    "intrabar_max_drawdown_pct": 24.554384929008435,
    "tp1_rate": 33.92857142857143,
    "tp2_rate": 23.214285714285715,
    "stop_rate": 76.78571428571429,
    "fee_drag": 91.82453446977661,
    "tail_max_loss": -116.6667126115919,
    "cagr": -10.306134421864677,
    "sharpe": -0.4799191933924716,
    "sortino": -0.5539044248876623,
    "exposure_pct": 86.11872146118722,
    "turnover": 7.621200687701357,
    "sample_sufficient": true,
    "sample_warning": ""
  }
}
```
