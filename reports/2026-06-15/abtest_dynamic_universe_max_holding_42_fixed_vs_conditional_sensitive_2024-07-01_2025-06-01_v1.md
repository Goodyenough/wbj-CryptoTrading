---
created: 2026-06-15 23:56:22 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: max_holding_42_fixed_vs_conditional_sensitive
baseline_run_id: 5c8c378c16fd
variant_run_id: e562c08d5fca
changed_param: backtest.max_holding_bars_conditional
old_value: False
new_value: True
sample_sufficient: true
universe_mode: dynamic
verdict: reject_candidate
report_version: v1
---

# A/B 实验报告 max_holding_42_fixed_vs_conditional_sensitive v1

- experiment_id: `max_holding_42_fixed_vs_conditional_sensitive`
- description: Direct fixed-vs-conditional 42-bar exit comparison under the same sensitive strategy. Both arms use 42 bars; only conditional gating changes.
- baseline_run_id: `5c8c378c16fd`
- variant_run_id: `e562c08d5fca`
- symbols: `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1INCHUSDT`, `1MBABYDOGEUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACHUSDT`, `ACTUSDT`, `ACXUSDT`, `ADAUSDT`, `AEVOUSDT`, `AGLDUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALGOUSDT`, `ALICEUSDT`, `ALPINEUSDT`, `ALTUSDT`, `AMPUSDT`, `ANIMEUSDT`, `ANKRUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARDRUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ASRUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AUDIOUSDT`, `AVAUSDT`, `AVAXUSDT`, `AXLUSDT`, `AXSUSDT`, `BABYUSDT`, `BANANAUSDT`, `BATUSDT`, `BBUSDT`, `BCHUSDT`, `BEAMXUSDT`, `BERAUSDT`, `BIOUSDT`, `BLURUSDT`, `BMTUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BTCUSDT`, `BTTCUSDT`, `C98USDT`, `CAKEUSDT`, `CATIUSDT`, `CELOUSDT`, `CETUSUSDT`, `CFXUSDT`, `CGPTUSDT`, `CHRUSDT`, `CHZUSDT`, `CKBUSDT`, `COMPUSDT`, `COOKIEUSDT`, `COSUSDT`, `COTIUSDT`, `COWUSDT`, `CRVUSDT`, `CTKUSDT`, `CTSIUSDT`, `CVCUSDT`, `CVXUSDT`, `DASHUSDT`, `DEXEUSDT`, `DGBUSDT`, `DIAUSDT`, `DODOUSDT`, `DOGEUSDT`, `DOGSUSDT`, `DOTUSDT`, `DUSDT`, `DYDXUSDT`, `DYMUSDT`, `EGLDUSDT`, `EIGENUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `FETUSDT`, `FIDAUSDT`, `FILUSDT`, `FLOKIUSDT`, `FLOWUSDT`, `FORMUSDT`, `FTTUSDT`, `GALAUSDT`, `GASUSDT`, `GLMRUSDT`, `GLMUSDT`, `GMTUSDT`, `GPSUSDT`, `GRTUSDT`, `GUNUSDT`, `GUSDT`, `HBARUSDT`, `HEIUSDT`, `HIGHUSDT`, `HIVEUSDT`, `HMSTRUSDT`, `HOTUSDT`, `HUMAUSDT`, `HYPERUSDT`, `ICPUSDT`, `IDUSDT`, `IMXUSDT`, `INITUSDT`, `INJUSDT`, `IOSTUSDT`, `IOTAUSDT`, `IOTXUSDT`, `IOUSDT`, `IQUSDT`, `JASMYUSDT`, `JSTUSDT`, `JTOUSDT`, `JUVUSDT`, `KAIAUSDT`, `KAITOUSDT`, `KAVAUSDT`, `KERNELUSDT`, `KSMUSDT`, `LAYERUSDT`, `LDOUSDT`, `LINKUSDT`, `LISTAUSDT`, `LPTUSDT`, `LQTYUSDT`, `LTCUSDT`, `LUMIAUSDT`, `LUNAUSDT`, `LUNCUSDT`, `MAGICUSDT`, `MANAUSDT`, `MANTAUSDT`, `MASKUSDT`, `MBOXUSDT`, `MEMEUSDT`, `METISUSDT`, `MEUSDT`, `MINAUSDT`, `MOVEUSDT`, `MOVRUSDT`, `MUBARAKUSDT`, `NEARUSDT`, `NEIROUSDT`, `NEOUSDT`, `NILUSDT`, `NMRUSDT`, `NOTUSDT`, `NXPCUSDT`, `OGNUSDT`, `OGUSDT`, `ONDOUSDT`, `ONEUSDT`, `ONTUSDT`, `OPUSDT`, `ORCAUSDT`, `ORDIUSDT`, `OSMOUSDT`, `PARTIUSDT`, `PENDLEUSDT`, `PENGUUSDT`, `PEOPLEUSDT`, `PEPEUSDT`, `PHAUSDT`, `PIXELUSDT`, `PNUTUSDT`, `POLUSDT`, `POLYXUSDT`, `PONDUSDT`, `PORTALUSDT`, `POWRUSDT`, `PROMUSDT`, `PSGUSDT`, `PUNDIXUSDT`, `PYRUSDT`, `PYTHUSDT`, `QKCUSDT`, `QNTUSDT`, `QTUMUSDT`, `RADUSDT`, `RAREUSDT`, `RAYUSDT`, `REDUSDT`, `RENDERUSDT`, `REZUSDT`, `RONINUSDT`, `ROSEUSDT`, `RPLUSDT`, `RSRUSDT`, `RUNEUSDT`, `RVNUSDT`, `SAGAUSDT`, `SANDUSDT`, `SANTOSUSDT`, `SCRTUSDT`, `SCRUSDT`, `SEIUSDT`, `SHELLUSDT`, `SHIBUSDT`, `SIGNUSDT`, `SKLUSDT`, `SLPUSDT`, `SNXUSDT`, `SOLUSDT`, `SOLVUSDT`, `SOPHUSDT`, `SPELLUSDT`, `SSVUSDT`, `STEEMUSDT`, `STGUSDT`, `STORJUSDT`, `STOUSDT`, `STRAXUSDT`, `STRKUSDT`, `STXUSDT`, `SUIUSDT`, `SUNUSDT`, `SUPERUSDT`, `SUSDT`, `SUSHIUSDT`, `SXTUSDT`, `SYNUSDT`, `TAOUSDT`, `TFUELUSDT`, `THETAUSDT`, `THEUSDT`, `TIAUSDT`, `TLMUSDT`, `TNSRUSDT`, `TONUSDT`, `TRBUSDT`, `TRUMPUSDT`, `TRXUSDT`, `TSTUSDT`, `TURBOUSDT`, `TUSDT`, `TUTUSDT`, `UNIUSDT`, `USUALUSDT`, `VANAUSDT`, `VANRYUSDT`, `VELODROMEUSDT`, `VETUSDT`, `VICUSDT`, `VIRTUALUSDT`, `VTHOUSDT`, `WAXPUSDT`, `WBTCUSDT`, `WCTUSDT`, `WIFUSDT`, `WINUSDT`, `WLDUSDT`, `WUSDT`, `XAIUSDT`, `XLMUSDT`, `XRPUSDT`, `XTZUSDT`, `XVGUSDT`, `YFIUSDT`, `YGGUSDT`, `ZECUSDT`, `ZENUSDT`, `ZILUSDT`, `ZKUSDT`, `ZROUSDT`, `ZRXUSDT`
- universe_mode: dynamic
- time_periods_tested: `2024-07-01` -> `2025-06-01`
- changed_param: `backtest.max_holding_bars_conditional`
- old_value: `False`
- new_value: `True`
- sample_sufficient: true
- possible_over_filtering: false
- verdict: `reject_candidate`
- reason: Variant return is worse and max drawdown did not improve.

## Dynamic Universe Metadata

- baseline_master_count: 418
- variant_master_count: 418
- baseline_source_limit: None
- variant_source_limit: None
- shared_master_expected: true (A/B runner builds the dynamic symbol master once before baseline and variant.)
- baseline_universe_refreshes: 336
- variant_universe_refreshes: 336

## 指标对比

| Metric | Baseline | Variant | Delta |
|---|---:|---:|---:|
| closed_trades | 134.00 | 134.00 | 0.00 |
| stop_rate | 50.00% | 54.48% | 4.48% |
| profit_factor | 1.48 | 1.38 | -0.09 |
| avg_r | 0.23 | 0.22 | -0.02 |
| max_drawdown_pct | 20.66% | 21.04% | 0.37% |
| net_return_pct | 31.86% | 27.57% | -4.30% |
| sharpe | 1.31 | 1.21 | -0.10 |
| first_trade_created_at | 2024-07-24T00:00:00+00:00 | 2024-07-24T00:00:00+00:00 | n/a |

## 样本规则

- closed_trades < 20 时，默认 verdict 为 `retest`。
- 交易数下降超过 50% 时，标记 possible_over_filtering=true。
- 自动报告不会直接写 `keep`；采用默认策略前需要跨时段复测和人工复盘。

## 变更明细

| changed_param | old_value | new_value |
|---|---:|---:|
| `backtest.max_holding_bars_conditional` | `False` | `True` |

## Raw Metrics

```json
{
  "baseline": {
    "trades": 517,
    "closed_trades": 134,
    "open_trades": 1,
    "win_rate": 50.0,
    "profit_factor": 1.4772889936794513,
    "avg_r": 0.23463119542659508,
    "net_return_pct": 31.86163369853203,
    "max_drawdown": 3111.8035593343884,
    "max_drawdown_pct": 20.664890308577046,
    "intrabar_max_drawdown": 3032.612877964919,
    "intrabar_max_drawdown_pct": 20.317727161402804,
    "tp1_rate": 26.119402985074625,
    "tp2_rate": 15.671641791044777,
    "stop_rate": 50.0,
    "fee_drag": 213.29587140645714,
    "tail_max_loss": -154.51965211599236,
    "cagr": 35.16844836488411,
    "sharpe": 1.3113863698379893,
    "sortino": 1.3728979794973917,
    "exposure_pct": 49.45273631840796,
    "turnover": 16.396929485728936,
    "sample_sufficient": true,
    "sample_warning": ""
  },
  "variant": {
    "trades": 509,
    "closed_trades": 134,
    "open_trades": 2,
    "win_rate": 44.776119402985074,
    "profit_factor": 1.3834024649299093,
    "avg_r": 0.2192827966155529,
    "net_return_pct": 27.566124401278213,
    "max_drawdown": 3304.0871569578176,
    "max_drawdown_pct": 21.036699067084808,
    "intrabar_max_drawdown": 3321.1856934797997,
    "intrabar_max_drawdown_pct": 21.1935522642374,
    "tp1_rate": 28.35820895522388,
    "tp2_rate": 17.16417910447761,
    "stop_rate": 54.47761194029851,
    "fee_drag": 214.66713715208633,
    "tail_max_loss": -161.24764139223754,
    "cagr": 30.377965489741456,
    "sharpe": 1.2118979697287446,
    "sortino": 1.2714310148783572,
    "exposure_pct": 49.1044776119403,
    "turnover": 16.82072099965837,
    "sample_sufficient": true,
    "sample_warning": ""
  }
}
```
