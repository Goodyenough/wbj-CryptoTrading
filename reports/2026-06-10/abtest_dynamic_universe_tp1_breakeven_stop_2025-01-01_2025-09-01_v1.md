---
created: 2026-06-10 04:04:28 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: tp1_breakeven_stop
baseline_run_id: 73cadcfc0a45
variant_run_id: 1d313ac1b8eb
changed_param: analysis.tp1_move_stop_to_breakeven_enabled
old_value: False
new_value: True
sample_sufficient: true
universe_mode: dynamic
verdict: reject_candidate
report_version: v1
---

# A/B 实验报告 tp1_breakeven_stop v1

- experiment_id: `tp1_breakeven_stop`
- description: Move stop loss to breakeven after TP1 is hit.
- baseline_run_id: `73cadcfc0a45`
- variant_run_id: `1d313ac1b8eb`
- symbols: `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1INCHUSDT`, `1MBABYDOGEUSDT`, `AAVEUSDT`, `ACHUSDT`, `ACTUSDT`, `ACXUSDT`, `ADAUSDT`, `AGLDUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALGOUSDT`, `ALPINEUSDT`, `ALTUSDT`, `AMPUSDT`, `ANIMEUSDT`, `ANKRUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARDRUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ASRUSDT`, `ATMUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AUDIOUSDT`, `AUSDT`, `AVAXUSDT`, `AXLUSDT`, `AXSUSDT`, `BABYUSDT`, `BANANAS31USDT`, `BANANAUSDT`, `BBUSDT`, `BCHUSDT`, `BEAMXUSDT`, `BERAUSDT`, `BIOUSDT`, `BMTUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BTCUSDT`, `C98USDT`, `CAKEUSDT`, `CATIUSDT`, `CETUSUSDT`, `CFXUSDT`, `CGPTUSDT`, `CKBUSDT`, `COMPUSDT`, `COOKIEUSDT`, `COWUSDT`, `CRVUSDT`, `CTSIUSDT`, `CUSDT`, `CVCUSDT`, `CYBERUSDT`, `DEXEUSDT`, `DIAUSDT`, `DOGEUSDT`, `DOGSUSDT`, `DOLOUSDT`, `DOTUSDT`, `DUSDT`, `DYMUSDT`, `EDUUSDT`, `EIGENUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSUSDT`, `EPICUSDT`, `ERAUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `FETUSDT`, `FIDAUSDT`, `FILUSDT`, `FLOKIUSDT`, `FORMUSDT`, `FTTUSDT`, `GALAUSDT`, `GASUSDT`, `GLMUSDT`, `GMTUSDT`, `GMXUSDT`, `GNSUSDT`, `GPSUSDT`, `GRTUSDT`, `GTCUSDT`, `GUNUSDT`, `GUSDT`, `HBARUSDT`, `HEIUSDT`, `HFTUSDT`, `HIGHUSDT`, `HIVEUSDT`, `HMSTRUSDT`, `HOMEUSDT`, `HUMAUSDT`, `HYPERUSDT`, `ICPUSDT`, `IDUSDT`, `ILVUSDT`, `IMXUSDT`, `INITUSDT`, `INJUSDT`, `IOSTUSDT`, `IOTAUSDT`, `IOUSDT`, `IQUSDT`, `JASMYUSDT`, `JSTUSDT`, `JTOUSDT`, `JUVUSDT`, `KAIAUSDT`, `KAITOUSDT`, `KAVAUSDT`, `KERNELUSDT`, `KNCUSDT`, `LAUSDT`, `LAYERUSDT`, `LDOUSDT`, `LINKUSDT`, `LISTAUSDT`, `LPTUSDT`, `LTCUSDT`, `LUNAUSDT`, `MAGICUSDT`, `MASKUSDT`, `MAVUSDT`, `MBOXUSDT`, `MEMEUSDT`, `MEUSDT`, `MITOUSDT`, `MOVEUSDT`, `MUBARAKUSDT`, `NEARUSDT`, `NEIROUSDT`, `NEOUSDT`, `NEWTUSDT`, `NILUSDT`, `NMRUSDT`, `NOTUSDT`, `NXPCUSDT`, `OGNUSDT`, `OGUSDT`, `ONDOUSDT`, `ONTUSDT`, `OPUSDT`, `ORCAUSDT`, `ORDIUSDT`, `OSMOUSDT`, `PARTIUSDT`, `PENDLEUSDT`, `PENGUUSDT`, `PEOPLEUSDT`, `PEPEUSDT`, `PHAUSDT`, `PIXELUSDT`, `PLUMEUSDT`, `PNUTUSDT`, `POLUSDT`, `PONDUSDT`, `PORTALUSDT`, `PROMUSDT`, `PROVEUSDT`, `PUNDIXUSDT`, `PYTHUSDT`, `QTUMUSDT`, `RAREUSDT`, `RAYUSDT`, `REDUSDT`, `RENDERUSDT`, `RESOLVUSDT`, `REZUSDT`, `RLCUSDT`, `RONINUSDT`, `RPLUSDT`, `RSRUSDT`, `RUNEUSDT`, `RVNUSDT`, `SAGAUSDT`, `SAHARAUSDT`, `SANDUSDT`, `SEIUSDT`, `SHELLUSDT`, `SHIBUSDT`, `SIGNUSDT`, `SKLUSDT`, `SLPUSDT`, `SOLUSDT`, `SOLVUSDT`, `SOPHUSDT`, `SPELLUSDT`, `SPKUSDT`, `STEEMUSDT`, `STGUSDT`, `STORJUSDT`, `STOUSDT`, `STRAXUSDT`, `STXUSDT`, `SUIUSDT`, `SUSDT`, `SUSHIUSDT`, `SXTUSDT`, `SYNUSDT`, `TAOUSDT`, `TFUELUSDT`, `THEUSDT`, `TIAUSDT`, `TONUSDT`, `TOWNSUSDT`, `TRBUSDT`, `TREEUSDT`, `TRUMPUSDT`, `TRXUSDT`, `TSTUSDT`, `TURBOUSDT`, `TUSDT`, `TUTUSDT`, `UMAUSDT`, `UNIUSDT`, `USD1USDT`, `USUALUSDT`, `VANAUSDT`, `VETUSDT`, `VICUSDT`, `VIRTUALUSDT`, `VTHOUSDT`, `WBETHUSDT`, `WBTCUSDT`, `WCTUSDT`, `WIFUSDT`, `WLDUSDT`, `WUSDT`, `XAIUSDT`, `XLMUSDT`, `XRPUSDT`, `XTZUSDT`, `XVGUSDT`, `ZENUSDT`, `ZKUSDT`, `ZROUSDT`
- universe_mode: dynamic
- time_periods_tested: `2025-01-01` -> `2025-09-01`
- changed_param: `analysis.tp1_move_stop_to_breakeven_enabled`
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
- baseline_universe_refreshes: 244
- variant_universe_refreshes: 244

## 指标对比

| Metric | Baseline | Variant | Delta |
|---|---:|---:|---:|
| closed_trades | 42.00 | 48.00 | 6.00 |
| stop_rate | 80.95% | 83.33% | 2.38% |
| profit_factor | 0.58 | 0.55 | -0.03 |
| avg_r | -0.32 | -0.33 | -0.01 |
| max_drawdown_pct | 19.43% | 19.43% | 0.00% |
| net_return_pct | -13.17% | -14.90% | -1.74% |
| sharpe | -1.03 | -1.17 | -0.14 |
| first_trade_created_at | 2025-01-02T12:00:00+00:00 | 2025-01-02T12:00:00+00:00 | n/a |

## 样本规则

- closed_trades < 20 时，默认 verdict 为 `retest`。
- 交易数下降超过 50% 时，标记 possible_over_filtering=true。
- 自动报告不会直接写 `keep`；采用默认策略前需要跨时段复测和人工复盘。

## 变更明细

| changed_param | old_value | new_value |
|---|---:|---:|
| `analysis.tp1_move_stop_to_breakeven_enabled` | `False` | `True` |

## Raw Metrics

```json
{
  "baseline": {
    "trades": 271,
    "closed_trades": 42,
    "open_trades": 5,
    "win_rate": 19.047619047619047,
    "profit_factor": 0.5788303615775615,
    "avg_r": -0.32109130123569374,
    "net_return_pct": -13.169473352124028,
    "max_drawdown": 1999.7034664765688,
    "max_drawdown_pct": 19.428139493966125,
    "intrabar_max_drawdown": 1981.126720276632,
    "intrabar_max_drawdown_pct": 19.391240086382176,
    "tp1_rate": 30.952380952380953,
    "tp2_rate": 19.047619047619047,
    "stop_rate": 80.95238095238095,
    "fee_drag": 51.18942488974736,
    "tail_max_loss": -104.26307084075773,
    "cagr": -19.112304164922577,
    "sharpe": -1.0333162547884633,
    "sortino": -1.26161554956655,
    "exposure_pct": 87.72290809327846,
    "turnover": 4.471898425556106,
    "sample_sufficient": true,
    "sample_warning": ""
  },
  "variant": {
    "trades": 272,
    "closed_trades": 48,
    "open_trades": 4,
    "win_rate": 16.666666666666664,
    "profit_factor": 0.5463925435943584,
    "avg_r": -0.32669624758612753,
    "net_return_pct": -14.904833528143136,
    "max_drawdown": 2000.0471828521986,
    "max_drawdown_pct": 19.431478873931223,
    "intrabar_max_drawdown": 1981.4680478374012,
    "intrabar_max_drawdown_pct": 19.394580995679508,
    "tp1_rate": 29.166666666666668,
    "tp2_rate": 16.666666666666664,
    "stop_rate": 83.33333333333334,
    "fee_drag": 61.27072947351701,
    "tail_max_loss": -104.26307084075773,
    "cagr": -21.528291232047714,
    "sharpe": -1.1722595510678437,
    "sortino": -1.3562918873048335,
    "exposure_pct": 87.72290809327846,
    "turnover": 5.168674841906516,
    "sample_sufficient": true,
    "sample_warning": ""
  }
}
```
