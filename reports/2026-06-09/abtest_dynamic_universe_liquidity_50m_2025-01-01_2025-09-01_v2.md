---
created: 2026-06-09 18:47:56 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: liquidity_50m
baseline_run_id: 1c1bd1b7b9ad
variant_run_id: 4dae110c062c
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
- baseline_run_id: `1c1bd1b7b9ad`
- variant_run_id: `4dae110c062c`
- symbols: `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1INCHUSDT`, `1MBABYDOGEUSDT`, `AAVEUSDT`, `ACHUSDT`, `ACTUSDT`, `ACXUSDT`, `ADAUSDT`, `AGLDUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALGOUSDT`, `ALPINEUSDT`, `ALTUSDT`, `AMPUSDT`, `ANIMEUSDT`, `ANKRUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARDRUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ASRUSDT`, `ATMUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AUDIOUSDT`, `AUSDT`, `AVAXUSDT`, `AXLUSDT`, `AXSUSDT`, `BABYUSDT`, `BANANAS31USDT`, `BANANAUSDT`, `BBUSDT`, `BCHUSDT`, `BEAMXUSDT`, `BERAUSDT`, `BIOUSDT`, `BMTUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BTCUSDT`, `C98USDT`, `CAKEUSDT`, `CATIUSDT`, `CETUSUSDT`, `CFXUSDT`, `CGPTUSDT`, `CKBUSDT`, `COMPUSDT`, `COOKIEUSDT`, `COWUSDT`, `CRVUSDT`, `CTSIUSDT`, `CUSDT`, `CVCUSDT`, `CYBERUSDT`, `DEXEUSDT`, `DIAUSDT`, `DOGEUSDT`, `DOGSUSDT`, `DOLOUSDT`, `DOTUSDT`, `DUSDT`, `DYMUSDT`, `EDUUSDT`, `EIGENUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSUSDT`, `EPICUSDT`, `ERAUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `FETUSDT`, `FIDAUSDT`, `FILUSDT`, `FLOKIUSDT`, `FORMUSDT`, `FTTUSDT`, `GALAUSDT`, `GASUSDT`, `GLMUSDT`, `GMTUSDT`, `GMXUSDT`, `GNSUSDT`, `GPSUSDT`, `GRTUSDT`, `GTCUSDT`, `GUNUSDT`, `GUSDT`, `HBARUSDT`, `HEIUSDT`, `HFTUSDT`, `HIGHUSDT`, `HIVEUSDT`, `HMSTRUSDT`, `HOMEUSDT`, `HUMAUSDT`, `HYPERUSDT`, `ICPUSDT`, `IDUSDT`, `ILVUSDT`, `IMXUSDT`, `INITUSDT`, `INJUSDT`, `IOSTUSDT`, `IOTAUSDT`, `IOUSDT`, `IQUSDT`, `JASMYUSDT`, `JSTUSDT`, `JTOUSDT`, `JUVUSDT`, `KAIAUSDT`, `KAITOUSDT`, `KAVAUSDT`, `KERNELUSDT`, `KNCUSDT`, `LAUSDT`, `LAYERUSDT`, `LDOUSDT`, `LINKUSDT`, `LISTAUSDT`, `LPTUSDT`, `LTCUSDT`, `LUNAUSDT`, `MAGICUSDT`, `MASKUSDT`, `MAVUSDT`, `MBOXUSDT`, `MEMEUSDT`, `MEUSDT`, `MITOUSDT`, `MOVEUSDT`, `MUBARAKUSDT`, `NEARUSDT`, `NEIROUSDT`, `NEOUSDT`, `NEWTUSDT`, `NILUSDT`, `NMRUSDT`, `NOTUSDT`, `NXPCUSDT`, `OGNUSDT`, `OGUSDT`, `ONDOUSDT`, `ONTUSDT`, `OPUSDT`, `ORCAUSDT`, `ORDIUSDT`, `OSMOUSDT`, `PARTIUSDT`, `PENDLEUSDT`, `PENGUUSDT`, `PEOPLEUSDT`, `PEPEUSDT`, `PHAUSDT`, `PIXELUSDT`, `PLUMEUSDT`, `PNUTUSDT`, `POLUSDT`, `PONDUSDT`, `PORTALUSDT`, `PROMUSDT`, `PROVEUSDT`, `PUNDIXUSDT`, `PYTHUSDT`, `QTUMUSDT`, `RAREUSDT`, `RAYUSDT`, `REDUSDT`, `RENDERUSDT`, `RESOLVUSDT`, `REZUSDT`, `RLCUSDT`, `RONINUSDT`, `RPLUSDT`, `RSRUSDT`, `RUNEUSDT`, `RVNUSDT`, `SAGAUSDT`, `SAHARAUSDT`, `SANDUSDT`, `SEIUSDT`, `SHELLUSDT`, `SHIBUSDT`, `SIGNUSDT`, `SKLUSDT`, `SLPUSDT`, `SOLUSDT`, `SOLVUSDT`, `SOPHUSDT`, `SPELLUSDT`, `SPKUSDT`, `STEEMUSDT`, `STGUSDT`, `STORJUSDT`, `STOUSDT`, `STRAXUSDT`, `STXUSDT`, `SUIUSDT`, `SUSDT`, `SUSHIUSDT`, `SXTUSDT`, `SYNUSDT`, `TAOUSDT`, `TFUELUSDT`, `THEUSDT`, `TIAUSDT`, `TONUSDT`, `TOWNSUSDT`, `TRBUSDT`, `TREEUSDT`, `TRUMPUSDT`, `TRXUSDT`, `TSTUSDT`, `TURBOUSDT`, `TUSDT`, `TUTUSDT`, `UMAUSDT`, `UNIUSDT`, `USD1USDT`, `USUALUSDT`, `VANAUSDT`, `VETUSDT`, `VICUSDT`, `VIRTUALUSDT`, `VTHOUSDT`, `WBETHUSDT`, `WBTCUSDT`, `WCTUSDT`, `WIFUSDT`, `WLDUSDT`, `WUSDT`, `XAIUSDT`, `XLMUSDT`, `XRPUSDT`, `XTZUSDT`, `XVGUSDT`, `ZENUSDT`, `ZKUSDT`, `ZROUSDT`
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
| closed_trades | 42.00 | 41.00 | -1.00 |
| stop_rate | 80.95% | 78.05% | -2.90% |
| profit_factor | 0.58 | 0.69 | 0.11 |
| avg_r | -0.32 | -0.22 | 0.10 |
| max_drawdown_pct | 19.43% | 18.81% | -0.62% |
| net_return_pct | -13.17% | -9.60% | 3.57% |
| sharpe | -1.03 | -0.73 | 0.30 |
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
    "trades": 242,
    "closed_trades": 41,
    "open_trades": 3,
    "win_rate": 21.951219512195124,
    "profit_factor": 0.6932260092037525,
    "avg_r": -0.21970034310578032,
    "net_return_pct": -9.59776918818559,
    "max_drawdown": 1935.714481507297,
    "max_drawdown_pct": 18.806453855619562,
    "intrabar_max_drawdown": 1895.257103627644,
    "intrabar_max_drawdown_pct": 18.550749503158087,
    "tp1_rate": 36.58536585365854,
    "tp2_rate": 21.951219512195124,
    "stop_rate": 78.04878048780488,
    "fee_drag": 53.44189123000119,
    "tail_max_loss": -104.26307084075773,
    "cagr": -14.063323299263597,
    "sharpe": -0.7321075653318526,
    "sortino": -0.8530579119083066,
    "exposure_pct": 88.54595336076817,
    "turnover": 4.703164184632447,
    "sample_sufficient": true,
    "sample_warning": ""
  }
}
```
