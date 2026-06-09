---
created: 2026-06-09 12:41:43 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: liquidity_50m
baseline_run_id: b8929f6a4f08
variant_run_id: 7b80538b60e9
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
- baseline_run_id: `b8929f6a4f08`
- variant_run_id: `7b80538b60e9`
- symbols: `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1MBABYDOGEUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACHUSDT`, `ACTUSDT`, `ACXUSDT`, `ADAUSDT`, `AEVOUSDT`, `AGLDUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALGOUSDT`, `ALPINEUSDT`, `AMPUSDT`, `ANIMEUSDT`, `ANKRUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARDRUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ASRUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AUDIOUSDT`, `AVAXUSDT`, `BABYUSDT`, `BANANAUSDT`, `BCHUSDT`, `BEAMXUSDT`, `BERAUSDT`, `BIOUSDT`, `BMTUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BTCUSDT`, `C98USDT`, `CAKEUSDT`, `CATIUSDT`, `CETUSUSDT`, `CFXUSDT`, `CGPTUSDT`, `CKBUSDT`, `COMPUSDT`, `COOKIEUSDT`, `COWUSDT`
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
| closed_trades | 14.00 | 12.00 | -2.00 |
| stop_rate | 92.86% | 91.67% | -1.19% |
| profit_factor | 0.20 | 0.23 | 0.03 |
| avg_r | -0.75 | -0.71 | 0.04 |
| max_drawdown_pct | 12.67% | 10.33% | -2.34% |
| net_return_pct | -10.37% | -8.51% | 1.86% |
| sharpe | -2.04 | -1.74 | 0.30 |
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
    "trades": 22,
    "closed_trades": 12,
    "open_trades": 2,
    "win_rate": 8.333333333333332,
    "profit_factor": 0.2322653230432656,
    "avg_r": -0.7091446197628661,
    "net_return_pct": -8.50950715465798,
    "max_drawdown": 1052.998061705206,
    "max_drawdown_pct": 10.328369026221734,
    "intrabar_max_drawdown": 1028.265434925188,
    "intrabar_max_drawdown_pct": 10.138971240270497,
    "tp1_rate": 16.666666666666664,
    "tp2_rate": 8.333333333333332,
    "stop_rate": 91.66666666666666,
    "fee_drag": 17.853797725231892,
    "tail_max_loss": -108.1494009784496,
    "cagr": -19.343890181058075,
    "sharpe": -1.7353697172755467,
    "sortino": -1.5368823597749883,
    "exposure_pct": 81.56732891832229,
    "turnover": 1.5106622332579631,
    "sample_sufficient": false,
    "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
  }
}
```
