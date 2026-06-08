---
created: 2026-06-09 00:58:18 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: history_365
baseline_run_id: e1dd9a29fc50
variant_run_id: e92bd90fdc7d
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
- baseline_run_id: `e1dd9a29fc50`
- variant_run_id: `e92bd90fdc7d`
- symbols: `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1INCHUSDT`, `1MBABYDOGEUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACHUSDT`, `ACTUSDT`, `ACXUSDT`, `ADAUSDT`, `AEVOUSDT`, `AGLDUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALGOUSDT`, `ALPINEUSDT`, `ALTUSDT`, `AMPUSDT`, `ANIMEUSDT`, `ANKRUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARDRUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ASRUSDT`, `ATMUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AUDIOUSDT`, `AUSDT`, `AVAXUSDT`, `AXLUSDT`, `AXSUSDT`, `BABYUSDT`, `BANANAS31USDT`, `BANANAUSDT`, `BBUSDT`, `BCHUSDT`, `BEAMXUSDT`, `BERAUSDT`, `BIOUSDT`, `BMTUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BTCUSDT`, `C98USDT`, `CAKEUSDT`, `CATIUSDT`, `CETUSUSDT`, `CFXUSDT`, `CGPTUSDT`, `CKBUSDT`, `COMPUSDT`, `COOKIEUSDT`, `COWUSDT`
- universe_mode: dynamic
- time_periods_tested: `2025-01-01` -> `2025-09-01`
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
- baseline_universe_refreshes: 244
- variant_universe_refreshes: 244

## 指标对比

| Metric | Baseline | Variant | Delta |
|---|---:|---:|---:|
| closed_trades | 33.00 | 29.00 | -4.00 |
| stop_rate | 84.85% | 79.31% | -5.54% |
| profit_factor | 0.43 | 0.65 | 0.22 |
| avg_r | -0.47 | -0.26 | 0.21 |
| max_drawdown_pct | 19.84% | 15.99% | -3.85% |
| net_return_pct | -15.27% | -7.84% | 7.43% |
| sharpe | -1.35 | -0.69 | 0.66 |
| first_trade_created_at | 2025-01-02T12:00:00+00:00 | 2025-01-02T12:00:00+00:00 | n/a |

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
    "trades": 95,
    "closed_trades": 29,
    "open_trades": 2,
    "win_rate": 20.689655172413794,
    "profit_factor": 0.6537749086019617,
    "avg_r": -0.25976802029884577,
    "net_return_pct": -7.8398505279532955,
    "max_drawdown": 1637.6181040087813,
    "max_drawdown_pct": 15.988070841448218,
    "intrabar_max_drawdown": 1605.3854774347492,
    "intrabar_max_drawdown_pct": 15.771595869116409,
    "tp1_rate": 24.137931034482758,
    "tp2_rate": 20.689655172413794,
    "stop_rate": 79.3103448275862,
    "fee_drag": 36.9566451959728,
    "tail_max_loss": -108.1494009784496,
    "cagr": -11.541046087396879,
    "sharpe": -0.6893787123136389,
    "sortino": -0.7664379429405735,
    "exposure_pct": 88.54595336076817,
    "turnover": 3.114843867521111,
    "sample_sufficient": true,
    "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
  }
}
```
