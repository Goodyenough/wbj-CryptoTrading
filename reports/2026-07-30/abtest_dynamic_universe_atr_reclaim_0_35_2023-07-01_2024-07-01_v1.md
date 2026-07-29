---
created: 2026-07-30 00:02:58 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: atr_reclaim_0_35
baseline_run_id: 86861b2dd032
variant_run_id: 0d78a8dc60e3
changed_param: analysis.entry_reclaim_min_atr_enabled, analysis.entry_reclaim_min_atr
old_value: False, 0.0
new_value: True, 0.35
sample_sufficient: true
universe_mode: dynamic
verdict: retest
report_version: v1
---

# A/B 实验报告 atr_reclaim_0_35 v1

- experiment_id: `atr_reclaim_0_35`
- description: Sensitivity test: require 4h reclaim close to exceed entry_high by at least 0.35 ATR before entering.
- baseline_run_id: `86861b2dd032`
- variant_run_id: `0d78a8dc60e3`
- symbols: `1000SATSUSDT`, `1INCHUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACHUSDT`, `ACMUSDT`, `ADAUSDT`, `ADXUSDT`, `AEVOUSDT`, `AGLDUSDT`, `AIUSDT`, `ALCXUSDT`, `ALGOUSDT`, `ALICEUSDT`, `ALTUSDT`, `AMPUSDT`, `ANKRUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ASRUSDT`, `ASTRUSDT`, `ATMUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AUDIOUSDT`, `AVAXUSDT`, `AXLUSDT`, `AXSUSDT`, `BANDUSDT`, `BBUSDT`, `BCHUSDT`, `BEAMXUSDT`, `BELUSDT`, `BICOUSDT`, `BLURUSDT`, `BNBUSDT`, `BNTUSDT`, `BOMEUSDT`, `BONKUSDT`, `BTCUSDT`, `BTTCUSDT`, `C98USDT`, `CAKEUSDT`, `CELOUSDT`, `CFXUSDT`, `CHRUSDT`, `CHZUSDT`, `CKBUSDT`, `COMPUSDT`, `COSUSDT`, `COTIUSDT`, `CRVUSDT`, `CTKUSDT`, `CTSIUSDT`, `CVCUSDT`, `CVXUSDT`, `CYBERUSDT`, `DCRUSDT`, `DEXEUSDT`, `DGBUSDT`, `DIAUSDT`, `DODOUSDT`, `DOGEUSDT`, `DOTUSDT`, `DUSKUSDT`, `DYDXUSDT`, `DYMUSDT`, `EDUUSDT`, `EGLDUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `FETUSDT`, `FIDAUSDT`, `FILUSDT`, `FLOKIUSDT`, `FLOWUSDT`, `FLUXUSDT`, `FTTUSDT`, `GALAUSDT`, `GASUSDT`, `GLMRUSDT`, `GLMUSDT`, `GMTUSDT`, `GMXUSDT`, `GRTUSDT`, `GTCUSDT`, `HBARUSDT`, `HIGHUSDT`, `HOTUSDT`, `ICPUSDT`, `ICXUSDT`, `IDUSDT`, `ILVUSDT`, `IMXUSDT`, `INJUSDT`, `IOSTUSDT`, `IOTAUSDT`, `IOTXUSDT`, `IOUSDT`, `IQUSDT`, `JASMYUSDT`, `JOEUSDT`, `JSTUSDT`, `JTOUSDT`, `KAVAUSDT`, `KNCUSDT`, `KSMUSDT`, `LAZIOUSDT`, `LDOUSDT`, `LINKUSDT`, `LISTAUSDT`, `LPTUSDT`, `LQTYUSDT`, `LSKUSDT`, `LTCUSDT`, `LUNAUSDT`, `LUNCUSDT`, `MAGICUSDT`, `MANAUSDT`, `MANTAUSDT`, `MASKUSDT`, `MAVUSDT`, `MBLUSDT`, `MBOXUSDT`, `MEMEUSDT`, `METISUSDT`, `MINAUSDT`, `MOVRUSDT`, `MTLUSDT`, `NEARUSDT`, `NEOUSDT`, `NFPUSDT`, `NMRUSDT`, `NOTUSDT`, `OGNUSDT`, `OGUSDT`, `ONEUSDT`, `ONGUSDT`, `ONTUSDT`, `OPUSDT`, `ORDIUSDT`, `OSMOUSDT`, `PENDLEUSDT`, `PEOPLEUSDT`, `PEPEUSDT`, `PHAUSDT`, `PIXELUSDT`, `POLYXUSDT`, `PONDUSDT`, `PORTALUSDT`, `POWRUSDT`, `PROMUSDT`, `PUNDIXUSDT`, `PYRUSDT`, `PYTHUSDT`, `QIUSDT`, `QTUMUSDT`, `QUICKUSDT`, `RADUSDT`, `RAREUSDT`, `RAYUSDT`, `REQUSDT`, `REZUSDT`, `RIFUSDT`, `RLCUSDT`, `RONINUSDT`, `ROSEUSDT`, `RPLUSDT`, `RSRUSDT`, `RUNEUSDT`, `RVNUSDT`, `SAGAUSDT`, `SANDUSDT`, `SANTOSUSDT`, `SCUSDT`, `SEIUSDT`, `SFPUSDT`, `SHIBUSDT`, `SKLUSDT`, `SLPUSDT`, `SNXUSDT`, `SOLUSDT`, `SPELLUSDT`, `SSVUSDT`, `STEEMUSDT`, `STGUSDT`, `STORJUSDT`, `STRAXUSDT`, `STRKUSDT`, `STXUSDT`, `SUIUSDT`, `SUPERUSDT`, `SUSHIUSDT`, `SYNUSDT`, `TAOUSDT`, `TFUELUSDT`, `THETAUSDT`, `TIAUSDT`, `TKOUSDT`, `TLMUSDT`, `TNSRUSDT`, `TRBUSDT`, `TRXUSDT`, `TUSDT`, `TWTUSDT`, `UMAUSDT`, `UNIUSDT`, `VANRYUSDT`, `VETUSDT`, `VTHOUSDT`, `WAXPUSDT`, `WIFUSDT`, `WINUSDT`, `WLDUSDT`, `WOOUSDT`, `WUSDT`, `XAIUSDT`, `XECUSDT`, `XLMUSDT`, `XNOUSDT`, `XRPUSDT`, `XVGUSDT`, `XVSUSDT`, `YFIUSDT`, `YGGUSDT`, `ZENUSDT`, `ZILUSDT`, `ZKUSDT`, `ZROUSDT`, `ZRXUSDT`
- universe_mode: dynamic
- time_periods_tested: `2023-07-01` -> `2024-07-01`
- changed_param: `analysis.entry_reclaim_min_atr_enabled, analysis.entry_reclaim_min_atr`
- old_value: `False, 0.0`
- new_value: `True, 0.35`
- sample_sufficient: true
- possible_over_filtering: false
- verdict: `retest`
- reason: Automatic report does not assign keep; review across additional time periods before adopting.

## Dynamic Universe Metadata

- baseline_master_count: 418
- variant_master_count: 418
- baseline_source_limit: None
- variant_source_limit: None
- shared_master_expected: true (A/B runner builds the dynamic symbol master once before baseline and variant.)
- baseline_universe_refreshes: 367
- variant_universe_refreshes: 367

## 指标对比

| Metric | Baseline | Variant | Delta |
|---|---:|---:|---:|
| closed_trades | 122.00 | 116.00 | -6.00 |
| stop_rate | 83.61% | 82.76% | -0.85% |
| profit_factor | 1.26 | 1.38 | 0.11 |
| avg_r | 0.19 | 0.26 | 0.07 |
| max_drawdown_pct | 21.85% | 21.08% | -0.78% |
| net_return_pct | 22.10% | 31.55% | 9.46% |
| sharpe | 0.93 | 1.24 | 0.31 |
| first_trade_created_at | 2023-07-01T04:00:00+00:00 | 2023-07-01T04:00:00+00:00 | n/a |

## 样本规则

- closed_trades < 20 时，默认 verdict 为 `retest`。
- 交易数下降超过 50% 时，标记 possible_over_filtering=true。
- 自动报告不会直接写 `keep`；采用默认策略前需要跨时段复测和人工复盘。

## 变更明细

| changed_param | old_value | new_value |
|---|---:|---:|
| `analysis.entry_reclaim_min_atr_enabled` | `False` | `True` |
| `analysis.entry_reclaim_min_atr` | `0.0` | `0.35` |

## Raw Metrics

```json
{
  "baseline": {
    "trades": 683,
    "closed_trades": 122,
    "open_trades": 0,
    "win_rate": 47.540983606557376,
    "profit_factor": 1.2635798959759066,
    "avg_r": 0.1891191941562675,
    "net_return_pct": 22.09735247462077,
    "max_drawdown": 3414.584641603162,
    "max_drawdown_pct": 21.854292960251513,
    "intrabar_max_drawdown": 3355.7861313902013,
    "intrabar_max_drawdown_pct": 21.5590987909307,
    "tp1_rate": 44.26229508196721,
    "tp2_rate": 16.39344262295082,
    "stop_rate": 83.60655737704919,
    "fee_drag": 216.23001693369324,
    "tail_max_loss": -157.89946311081437,
    "cagr": 22.03076802831059,
    "sharpe": 0.9322173028561375,
    "sortino": 1.0348535852135137,
    "exposure_pct": 78.18761384335154,
    "turnover": 16.68744881061567,
    "sample_sufficient": true,
    "sample_warning": ""
  },
  "variant": {
    "trades": 693,
    "closed_trades": 116,
    "open_trades": 0,
    "win_rate": 50.0,
    "profit_factor": 1.3764511119940768,
    "avg_r": 0.2584191380420014,
    "net_return_pct": 31.553588580632642,
    "max_drawdown": 3512.8246710303974,
    "max_drawdown_pct": 21.075029950917564,
    "intrabar_max_drawdown": 3411.769766112,
    "intrabar_max_drawdown_pct": 20.593609451027262,
    "tp1_rate": 45.689655172413794,
    "tp2_rate": 17.24137931034483,
    "stop_rate": 82.75862068965517,
    "fee_drag": 213.29155966148682,
    "tail_max_loss": -168.53844040324293,
    "cagr": 31.455052290028007,
    "sharpe": 1.2380625803515595,
    "sortino": 1.3422336263871641,
    "exposure_pct": 76.68488160291439,
    "turnover": 16.539603749125153,
    "sample_sufficient": true,
    "sample_warning": ""
  }
}
```
