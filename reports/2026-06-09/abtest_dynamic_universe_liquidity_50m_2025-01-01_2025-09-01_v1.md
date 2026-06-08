---
created: 2026-06-09 01:20:53 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: liquidity_50m
baseline_run_id: 20a46ab54c7e
variant_run_id: 713c3fd7cd6a
changed_param: market.min_quote_volume, market.min_trades
old_value: 30000000.0, 30000
new_value: 50000000, 50000
sample_sufficient: true
universe_mode: dynamic
verdict: retest
report_version: v1
---

# A/B 实验报告 liquidity_50m v1

- experiment_id: `liquidity_50m`
- description: Test higher liquidity thresholds.
- baseline_run_id: `20a46ab54c7e`
- variant_run_id: `713c3fd7cd6a`
- symbols: `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1INCHUSDT`, `1MBABYDOGEUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACHUSDT`, `ACTUSDT`, `ACXUSDT`, `ADAUSDT`, `AEVOUSDT`, `AGLDUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALGOUSDT`, `ALPINEUSDT`, `ALTUSDT`, `AMPUSDT`, `ANIMEUSDT`, `ANKRUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARDRUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ASRUSDT`, `ATMUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AUDIOUSDT`, `AUSDT`, `AVAXUSDT`, `AXLUSDT`, `AXSUSDT`, `BABYUSDT`, `BANANAS31USDT`, `BANANAUSDT`, `BBUSDT`, `BCHUSDT`, `BEAMXUSDT`, `BERAUSDT`, `BIOUSDT`, `BMTUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BTCUSDT`, `C98USDT`, `CAKEUSDT`, `CATIUSDT`, `CETUSUSDT`, `CFXUSDT`, `CGPTUSDT`, `CKBUSDT`, `COMPUSDT`, `COOKIEUSDT`, `COWUSDT`
- universe_mode: dynamic
- time_periods_tested: `2025-01-01` -> `2025-09-01`
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
- baseline_universe_refreshes: 244
- variant_universe_refreshes: 244

## 指标对比

| Metric | Baseline | Variant | Delta |
|---|---:|---:|---:|
| closed_trades | 33.00 | 30.00 | -3.00 |
| stop_rate | 84.85% | 80.00% | -4.85% |
| profit_factor | 0.43 | 0.65 | 0.22 |
| avg_r | -0.47 | -0.26 | 0.20 |
| max_drawdown_pct | 19.84% | 14.69% | -5.15% |
| net_return_pct | -15.27% | -8.13% | 7.14% |
| sharpe | -1.35 | -0.63 | 0.71 |
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
    "trades": 108,
    "closed_trades": 33,
    "open_trades": 3,
    "win_rate": 15.151515151515152,
    "profit_factor": 0.43115800770552987,
    "avg_r": -0.465503443901505,
    "net_return_pct": -15.270931447235615,
    "max_drawdown": 2032.3298832070068,
    "max_drawdown_pct": 19.841643217283078,
    "intrabar_max_drawdown": 2002.4190905666137,
    "intrabar_max_drawdown_pct": 19.672125543009255,
    "tp1_rate": 27.27272727272727,
    "tp2_rate": 15.151515151515152,
    "stop_rate": 84.84848484848484,
    "fee_drag": 48.05279488339604,
    "tail_max_loss": -108.1494009784496,
    "cagr": -22.03484138384406,
    "sharpe": -1.3451865578209627,
    "sortino": -1.4477309180821338,
    "exposure_pct": 87.79149519890261,
    "turnover": 3.9369289196597093,
    "sample_sufficient": true,
    "sample_warning": ""
  },
  "variant": {
    "trades": 60,
    "closed_trades": 30,
    "open_trades": 3,
    "win_rate": 20.0,
    "profit_factor": 0.6484928567521694,
    "avg_r": -0.26478528698685116,
    "net_return_pct": -8.134084586517588,
    "max_drawdown": 1498.1520334023226,
    "max_drawdown_pct": 14.694677626762392,
    "intrabar_max_drawdown": 1462.2485417241187,
    "intrabar_max_drawdown_pct": 14.418160337896571,
    "tp1_rate": 30.0,
    "tp2_rate": 20.0,
    "stop_rate": 80.0,
    "fee_drag": 38.96778575047144,
    "tail_max_loss": -108.1494009784496,
    "cagr": -11.964913252062793,
    "sharpe": -0.6302215820477526,
    "sortino": -0.6837326501217234,
    "exposure_pct": 88.54595336076817,
    "turnover": 3.397006683907528,
    "sample_sufficient": true,
    "sample_warning": ""
  }
}
```
