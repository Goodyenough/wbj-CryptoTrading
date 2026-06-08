---
created: 2026-06-09 01:10:14 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: pump_chase_strict
baseline_run_id: b2fdfa8e6ff9
variant_run_id: 242cf3ed27a4
changed_param: analysis.pump_chase_24h_pct, analysis.pump_chase_distance_pct, analysis.pump_chase_penalty
old_value: 20.0, 8.0, 8.0
new_value: 12.0, 6.0, 12.0
sample_sufficient: true
universe_mode: dynamic
verdict: retest
report_version: v1
---

# A/B 实验报告 pump_chase_strict v1

- experiment_id: `pump_chase_strict`
- description: Test stricter pump-chasing score penalties.
- baseline_run_id: `b2fdfa8e6ff9`
- variant_run_id: `242cf3ed27a4`
- symbols: `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1INCHUSDT`, `1MBABYDOGEUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACHUSDT`, `ACTUSDT`, `ACXUSDT`, `ADAUSDT`, `AEVOUSDT`, `AGLDUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALGOUSDT`, `ALPINEUSDT`, `ALTUSDT`, `AMPUSDT`, `ANIMEUSDT`, `ANKRUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARDRUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ASRUSDT`, `ATMUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AUDIOUSDT`, `AUSDT`, `AVAXUSDT`, `AXLUSDT`, `AXSUSDT`, `BABYUSDT`, `BANANAS31USDT`, `BANANAUSDT`, `BBUSDT`, `BCHUSDT`, `BEAMXUSDT`, `BERAUSDT`, `BIOUSDT`, `BMTUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BTCUSDT`, `C98USDT`, `CAKEUSDT`, `CATIUSDT`, `CETUSUSDT`, `CFXUSDT`, `CGPTUSDT`, `CKBUSDT`, `COMPUSDT`, `COOKIEUSDT`, `COWUSDT`
- universe_mode: dynamic
- time_periods_tested: `2025-01-01` -> `2025-09-01`
- changed_param: `analysis.pump_chase_24h_pct, analysis.pump_chase_distance_pct, analysis.pump_chase_penalty`
- old_value: `20.0, 8.0, 8.0`
- new_value: `12.0, 6.0, 12.0`
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
| closed_trades | 33.00 | 33.00 | 0.00 |
| stop_rate | 84.85% | 84.85% | 0.00% |
| profit_factor | 0.43 | 0.43 | 0.00 |
| avg_r | -0.47 | -0.47 | 0.00 |
| max_drawdown_pct | 19.84% | 19.84% | 0.00% |
| net_return_pct | -15.27% | -15.27% | 0.00% |
| sharpe | -1.35 | -1.35 | 0.00 |
| first_trade_created_at | 2025-01-02T12:00:00+00:00 | 2025-01-02T12:00:00+00:00 | n/a |

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
  }
}
```
