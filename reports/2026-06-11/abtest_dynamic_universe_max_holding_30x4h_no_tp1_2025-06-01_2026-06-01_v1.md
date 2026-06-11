---
created: 2026-06-11 21:27:56 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: max_holding_30x4h_no_tp1
baseline_run_id: c17998697a29
variant_run_id: baa1cb413fec
changed_param: backtest.max_holding_bars_without_tp1
old_value: 0
new_value: 30
sample_sufficient: true
universe_mode: dynamic
verdict: retest
report_version: v1
---

# A/B 实验报告 max_holding_30x4h_no_tp1 v1

- experiment_id: `max_holding_30x4h_no_tp1`
- description: Force-close an entered position if TP1 has not been touched after 30 closed 4h bars.
- baseline_run_id: `c17998697a29`
- variant_run_id: `baa1cb413fec`
- symbols: `0GUSDT`, `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1INCHUSDT`, `2ZUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACHUSDT`, `ADAUSDT`, `AEVOUSDT`, `AIGENSYNUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALCXUSDT`, `ALGOUSDT`, `ALICEUSDT`, `ALLOUSDT`, `ALPINEUSDT`, `ALTUSDT`, `ANIMEUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ASRUSDT`, `ASTERUSDT`, `ATMUSDT`, `ATUSDT`, `AUCTIONUSDT`, `AUSDT`, `AVAXUSDT`, `AVNTUSDT`, `AWEUSDT`, `AXLUSDT`, `AXSUSDT`, `BABYUSDT`, `BANANAS31USDT`, `BARDUSDT`, `BATUSDT`, `BBUSDT`, `BCHUSDT`, `BELUSDT`, `BERAUSDT`, `BIOUSDT`, `BMTUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BREVUSDT`, `BROCCOLI714USDT`, `BTCUSDT`, `C98USDT`, `CAKEUSDT`, `CELOUSDT`, `CFGUSDT`, `CFXUSDT`, `CHIPUSDT`, `CHZUSDT`, `CKBUSDT`, `COMPUSDT`, `COSUSDT`, `COTIUSDT`, `COWUSDT`, `CRVUSDT`, `CTSIUSDT`, `CUSDT`, `CYBERUSDT`, `DASHUSDT`, `DCRUSDT`, `DEXEUSDT`, `DIAUSDT`, `DOGEUSDT`, `DOGSUSDT`, `DOLOUSDT`, `DOTUSDT`, `DUSDT`, `DUSKUSDT`, `DYMUSDT`, `EDENUSDT`, `EDUUSDT`, `EIGENUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSOUSDT`, `ENSUSDT`, `EPICUSDT`, `ERAUSDT`, `ESPUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `EULUSDT`, `FETUSDT`, `FFUSDT`, `FIDAUSDT`, `FILUSDT`, `FLOKIUSDT`, `FLOWUSDT`, `FLUXUSDT`, `FOGOUSDT`, `FORMUSDT`, `FRAXUSDT`, `FUSDT`, `GALAUSDT`, `GENIUSUSDT`, `GIGGLEUSDT`, `GMTUSDT`, `GMXUSDT`, `GNSUSDT`, `GPSUSDT`, `GTCUSDT`, `GUNUSDT`, `HAEDALUSDT`, `HBARUSDT`, `HEIUSDT`, `HEMIUSDT`, `HFTUSDT`, `HIGHUSDT`, `HMSTRUSDT`, `HOLOUSDT`, `HOMEUSDT`, `HUMAUSDT`, `HYPERUSDT`, `ICPUSDT`, `ILVUSDT`, `INITUSDT`, `INJUSDT`, `IOUSDT`, `JASMYUSDT`, `JTOUSDT`, `JUVUSDT`, `KAIAUSDT`, `KAITOUSDT`, `KATUSDT`, `KERNELUSDT`, `KITEUSDT`, `KMNOUSDT`, `KNCUSDT`, `LAUSDT`, `LAYERUSDT`, `LDOUSDT`, `LINEAUSDT`, `LINKUSDT`, `LISTAUSDT`, `LPTUSDT`, `LSKUSDT`, `LTCUSDT`, `LUNAUSDT`, `LUNCUSDT`, `MAGICUSDT`, `MASKUSDT`, `MAVUSDT`, `MEGAUSDT`, `MEMEUSDT`, `METUSDT`, `MEUSDT`, `MINAUSDT`, `MIRAUSDT`, `MITOUSDT`, `MMTUSDT`, `MORPHOUSDT`, `MOVEUSDT`, `MOVRUSDT`, `MUBARAKUSDT`, `NEARUSDT`, `NEIROUSDT`, `NEOUSDT`, `NEWTUSDT`, `NIGHTUSDT`, `NILUSDT`, `NMRUSDT`, `NOMUSDT`, `NOTUSDT`, `NXPCUSDT`, `OGNUSDT`, `OGUSDT`, `ONDOUSDT`, `ONTUSDT`, `OPENUSDT`, `OPGUSDT`, `OPNUSDT`, `OPUSDT`, `ORCAUSDT`, `ORDIUSDT`, `OSMOUSDT`, `PARTIUSDT`, `PENDLEUSDT`, `PENGUUSDT`, `PEOPLEUSDT`, `PEPEUSDT`, `PIVXUSDT`, `PIXELUSDT`, `PLUMEUSDT`, `PNUTUSDT`, `POLUSDT`, `PONDUSDT`, `PORTALUSDT`, `PROVEUSDT`, `PUMPUSDT`, `PYRUSDT`, `PYTHUSDT`, `QTUMUSDT`, `RAREUSDT`, `RAYUSDT`, `REDUSDT`, `RENDERUSDT`, `RESOLVUSDT`, `REZUSDT`, `RLCUSDT`, `ROBOUSDT`, `RONINUSDT`, `ROSEUSDT`, `RVNUSDT`, `SAGAUSDT`, `SAHARAUSDT`, `SANDUSDT`, `SAPIENUSDT`, `SEIUSDT`, `SENTUSDT`, `SHIBUSDT`, `SIGNUSDT`, `SKLUSDT`, `SLPUSDT`, `SNXUSDT`, `SOLUSDT`, `SOLVUSDT`, `SOMIUSDT`, `SOPHUSDT`, `SPKUSDT`, `STOUSDT`, `STRKUSDT`, `SUIUSDT`, `SUNUSDT`, `SUPERUSDT`, `SUSDT`, `SUSHIUSDT`, `SXTUSDT`, `SYNUSDT`, `TAOUSDT`, `THEUSDT`, `TIAUSDT`, `TNSRUSDT`, `TONUSDT`, `TOWNSUSDT`, `TRBUSDT`, `TREEUSDT`, `TRUMPUSDT`, `TRXUSDT`, `TSTUSDT`, `TURBOUSDT`, `TURTLEUSDT`, `TUTUSDT`, `TWTUSDT`, `UMAUSDT`, `UNIUSDT`, `USD1USDT`, `USUALUSDT`, `VANAUSDT`, `VETUSDT`, `VICUSDT`, `VIRTUALUSDT`, `WALUSDT`, `WBETHUSDT`, `WBTCUSDT`, `WCTUSDT`, `WIFUSDT`, `WLDUSDT`, `WLFIUSDT`, `WUSDT`, `XAIUSDT`, `XAUTUSDT`, `XLMUSDT`, `XPLUSDT`, `XRPUSDT`, `XTZUSDT`, `XVGUSDT`, `YBUSDT`, `YGGUSDT`, `ZAMAUSDT`, `ZBTUSDT`, `ZECUSDT`, `ZENUSDT`, `ZILUSDT`, `ZKCUSDT`, `ZKPUSDT`, `ZKUSDT`, `ZROUSDT`, `币安人生USDT`
- universe_mode: dynamic
- time_periods_tested: `2025-06-01` -> `2026-06-01`
- changed_param: `backtest.max_holding_bars_without_tp1`
- old_value: `0`
- new_value: `30`
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
- baseline_universe_refreshes: 366
- variant_universe_refreshes: 366

## 指标对比

| Metric | Baseline | Variant | Delta |
|---|---:|---:|---:|
| closed_trades | 63.00 | 111.00 | 48.00 |
| stop_rate | 84.13% | 31.53% | -52.60% |
| profit_factor | 1.11 | 1.56 | 0.45 |
| avg_r | 0.08 | 0.24 | 0.16 |
| max_drawdown_pct | 20.85% | 11.84% | -9.01% |
| net_return_pct | 3.32% | 27.28% | 23.96% |
| sharpe | 0.28 | 1.44 | 1.16 |
| first_trade_created_at | 2025-06-08T00:00:00+00:00 | 2025-06-08T00:00:00+00:00 | n/a |

## 样本规则

- closed_trades < 20 时，默认 verdict 为 `retest`。
- 交易数下降超过 50% 时，标记 possible_over_filtering=true。
- 自动报告不会直接写 `keep`；采用默认策略前需要跨时段复测和人工复盘。

## 变更明细

| changed_param | old_value | new_value |
|---|---:|---:|
| `backtest.max_holding_bars_without_tp1` | `0` | `30` |

## Raw Metrics

```json
{
  "baseline": {
    "trades": 308,
    "closed_trades": 63,
    "open_trades": 2,
    "win_rate": 41.269841269841265,
    "profit_factor": 1.1067194860994791,
    "avg_r": 0.0803636344384486,
    "net_return_pct": 3.320892123838104,
    "max_drawdown": 2657.8960314637516,
    "max_drawdown_pct": 20.85037229078044,
    "intrabar_max_drawdown": 2561.207072517758,
    "intrabar_max_drawdown_pct": 20.303640208510377,
    "tp1_rate": 39.682539682539684,
    "tp2_rate": 15.873015873015872,
    "stop_rate": 84.12698412698413,
    "fee_drag": 117.76390073886442,
    "tail_max_loss": -130.48872126250012,
    "cagr": 3.320892123838104,
    "sharpe": 0.276482977042147,
    "sortino": 0.28139413258075346,
    "exposure_pct": 50.502283105022826,
    "turnover": 9.393084296312866,
    "sample_sufficient": true,
    "sample_warning": ""
  },
  "variant": {
    "trades": 337,
    "closed_trades": 111,
    "open_trades": 0,
    "win_rate": 46.846846846846844,
    "profit_factor": 1.560411758926206,
    "avg_r": 0.24194742201035424,
    "net_return_pct": 27.278727170143966,
    "max_drawdown": 1620.144342069223,
    "max_drawdown_pct": 11.839424020096654,
    "intrabar_max_drawdown": 1481.7254881077988,
    "intrabar_max_drawdown_pct": 10.973682511359586,
    "tp1_rate": 18.01801801801802,
    "tp2_rate": 14.414414414414415,
    "stop_rate": 31.53153153153153,
    "fee_drag": 250.50877125521055,
    "tail_max_loss": -140.24924806679505,
    "cagr": 27.278727170143966,
    "sharpe": 1.4364225475710881,
    "sortino": 1.3356537089697036,
    "exposure_pct": 34.93150684931507,
    "turnover": 19.142876259129917,
    "sample_sufficient": true,
    "sample_warning": ""
  }
}
```
