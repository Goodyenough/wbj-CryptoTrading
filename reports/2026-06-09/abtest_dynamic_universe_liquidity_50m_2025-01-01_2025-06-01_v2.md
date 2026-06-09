---
created: 2026-06-09 14:37:52 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: liquidity_50m
baseline_run_id: c431a48d0643
variant_run_id: 41c97fd4dda5
changed_param: market.min_quote_volume, market.min_trades
old_value: 30000000.0, 30000
new_value: 50000000, 50000
sample_sufficient: false
universe_mode: dynamic
verdict: retest
report_version: v2
---

# A/B 实验报告 liquidity_50m v2

- experiment_id: `liquidity_50m`
- description: Test higher liquidity thresholds.
- baseline_run_id: `c431a48d0643`
- variant_run_id: `41c97fd4dda5`
- symbols: `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1MBABYDOGEUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACHUSDT`, `ACTUSDT`, `ACXUSDT`, `ADAUSDT`, `AEVOUSDT`, `AGLDUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALGOUSDT`, `ALPINEUSDT`, `AMPUSDT`, `ANIMEUSDT`, `ANKRUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARDRUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ASRUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AUDIOUSDT`, `AVAXUSDT`, `BABYUSDT`, `BANANAUSDT`, `BCHUSDT`, `BEAMXUSDT`, `BERAUSDT`, `BIOUSDT`, `BMTUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BTCUSDT`, `C98USDT`, `CAKEUSDT`, `CATIUSDT`, `CETUSUSDT`, `CFXUSDT`, `CGPTUSDT`, `CKBUSDT`, `COMPUSDT`, `COOKIEUSDT`, `COWUSDT`, `CRVUSDT`, `CVCUSDT`, `DEXEUSDT`, `DOGEUSDT`, `DOGSUSDT`, `DOTUSDT`, `DUSDT`, `DYDXUSDT`, `DYMUSDT`, `EGLDUSDT`, `EIGENUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `FETUSDT`, `FIDAUSDT`, `FILUSDT`, `FLOKIUSDT`, `FORMUSDT`, `FTTUSDT`, `GALAUSDT`, `GASUSDT`
- universe_mode: dynamic
- time_periods_tested: `2025-01-01` -> `2025-06-01`
- changed_param: `market.min_quote_volume, market.min_trades`
- old_value: `30000000.0, 30000`
- new_value: `50000000, 50000`
- sample_sufficient: false
- possible_over_filtering: false
- verdict: `retest`
- reason: Variant closed_trades is below 20, so the sample is insufficient for a keep decision.

## Dynamic Universe Metadata

- baseline_master_count: 150
- variant_master_count: 150
- baseline_source_limit: 150
- variant_source_limit: 150
- shared_master_expected: true (A/B runner builds the dynamic symbol master once before baseline and variant.)
- baseline_universe_refreshes: 152
- variant_universe_refreshes: 152

## 指标对比

| Metric | Baseline | Variant | Delta |
|---|---:|---:|---:|
| closed_trades | 19.00 | 16.00 | -3.00 |
| stop_rate | 89.47% | 87.50% | -1.97% |
| profit_factor | 0.29 | 0.35 | 0.06 |
| avg_r | -0.64 | -0.56 | 0.07 |
| max_drawdown_pct | 14.48% | 13.22% | -1.26% |
| net_return_pct | -11.23% | -9.09% | 2.14% |
| sharpe | -1.90 | -1.64 | 0.25 |
| first_trade_created_at | 2025-01-02T12:00:00+00:00 | 2025-01-02T12:00:00+00:00 | n/a |

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
    "trades": 71,
    "closed_trades": 19,
    "open_trades": 2,
    "win_rate": 10.526315789473683,
    "profit_factor": 0.2858130405717013,
    "avg_r": -0.6364200822044673,
    "net_return_pct": -11.225828888974299,
    "max_drawdown": 1490.0847844948985,
    "max_drawdown_pct": 14.475121436558029,
    "intrabar_max_drawdown": 1398.4557339298153,
    "intrabar_max_drawdown_pct": 13.711355582690537,
    "tp1_rate": 21.052631578947366,
    "tp2_rate": 10.526315789473683,
    "stop_rate": 89.47368421052632,
    "fee_drag": 27.00553390300852,
    "tail_max_loss": -108.73727506688915,
    "cagr": -25.011015340279762,
    "sharpe": -1.8957856901555281,
    "sortino": -1.8369508751256913,
    "exposure_pct": 81.56732891832229,
    "turnover": 2.2609745222643602,
    "sample_sufficient": false,
    "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
  },
  "variant": {
    "trades": 46,
    "closed_trades": 16,
    "open_trades": 2,
    "win_rate": 12.5,
    "profit_factor": 0.34727788284317357,
    "avg_r": -0.5638995421497967,
    "net_return_pct": -9.085559393015497,
    "max_drawdown": 1355.6073553493097,
    "max_drawdown_pct": 13.218848904267821,
    "intrabar_max_drawdown": 1275.9881670681207,
    "intrabar_max_drawdown_pct": 12.543842903894435,
    "tp1_rate": 18.75,
    "tp2_rate": 12.5,
    "stop_rate": 87.5,
    "fee_drag": 23.16039094761875,
    "tail_max_loss": -108.73727506688915,
    "cagr": -20.56596783449137,
    "sharpe": -1.6419457521957572,
    "sortino": -1.6040070181243393,
    "exposure_pct": 81.56732891832229,
    "turnover": 1.9618017736187412,
    "sample_sufficient": false,
    "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
  }
}
```
