---
created: 2026-06-11 16:09:41 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: regime_sensitive
baseline_run_id: f068158d4815
variant_run_id: ecb735800fbd
changed_param: analysis.regime_btc_7d_drop_pct, analysis.regime_eth_7d_drop_pct, analysis.regime_require_both_trend
old_value: -5.0, -8.0, False
new_value: -3.0, -5.0, True
sample_sufficient: true
universe_mode: dynamic
verdict: retest
report_version: v1
---

# A/B 实验报告 regime_sensitive v1

- experiment_id: `regime_sensitive`
- description: Test tighter RISK_OFF thresholds: BTC 7d drop -3% (vs -5%), ETH -5% (vs -8%), require both BTC+ETH trend ok.
- baseline_run_id: `f068158d4815`
- variant_run_id: `ecb735800fbd`
- symbols: `0GUSDT`, `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1INCHUSDT`, `2ZUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACHUSDT`, `ADAUSDT`, `AEVOUSDT`, `AIGENSYNUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALCXUSDT`, `ALGOUSDT`, `ALICEUSDT`, `ALLOUSDT`, `ALPINEUSDT`, `ALTUSDT`, `ANIMEUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ASRUSDT`, `ASTERUSDT`, `ATMUSDT`, `ATUSDT`, `AUCTIONUSDT`, `AUSDT`, `AVAXUSDT`, `AVNTUSDT`, `AXLUSDT`, `AXSUSDT`, `BABYUSDT`, `BANANAS31USDT`, `BARDUSDT`, `BATUSDT`, `BBUSDT`, `BCHUSDT`, `BERAUSDT`, `BIOUSDT`, `BMTUSDT`, `BNBUSDT`, `BOMEUSDT`, `BONKUSDT`, `BREVUSDT`, `BROCCOLI714USDT`, `BTCUSDT`, `C98USDT`, `CAKEUSDT`, `CELOUSDT`, `CFGUSDT`, `CFXUSDT`, `CHIPUSDT`, `CHZUSDT`, `CKBUSDT`, `COMPUSDT`, `COSUSDT`, `COTIUSDT`, `COWUSDT`, `CRVUSDT`, `CTSIUSDT`, `CUSDT`, `CYBERUSDT`, `DASHUSDT`, `DEXEUSDT`, `DIAUSDT`, `DOGEUSDT`, `DOGSUSDT`, `DOLOUSDT`, `DOTUSDT`, `DUSDT`, `DUSKUSDT`, `DYMUSDT`, `EDENUSDT`, `EDUUSDT`, `EIGENUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSOUSDT`, `ENSUSDT`, `EPICUSDT`, `ERAUSDT`, `ESPUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `EULUSDT`, `FETUSDT`, `FFUSDT`, `FIDAUSDT`, `FILUSDT`, `FLOKIUSDT`, `FLOWUSDT`, `FLUXUSDT`, `FOGOUSDT`, `FORMUSDT`, `FRAXUSDT`, `FUSDT`, `GALAUSDT`, `GENIUSUSDT`, `GIGGLEUSDT`, `GMTUSDT`, `GMXUSDT`, `GNSUSDT`, `GPSUSDT`, `GTCUSDT`, `GUNUSDT`, `HBARUSDT`, `HEIUSDT`, `HEMIUSDT`, `HFTUSDT`, `HIGHUSDT`, `HMSTRUSDT`, `HOLOUSDT`, `HOMEUSDT`, `HUMAUSDT`, `HYPERUSDT`, `ICPUSDT`, `ILVUSDT`, `INITUSDT`, `INJUSDT`, `IOUSDT`, `JASMYUSDT`, `JTOUSDT`, `JUVUSDT`, `KAIAUSDT`, `KAITOUSDT`, `KATUSDT`, `KERNELUSDT`, `KITEUSDT`, `KMNOUSDT`, `KNCUSDT`, `LAUSDT`, `LAYERUSDT`, `LDOUSDT`, `LINEAUSDT`, `LINKUSDT`, `LISTAUSDT`, `LPTUSDT`, `LSKUSDT`, `LTCUSDT`, `LUNAUSDT`, `LUNCUSDT`, `MAGICUSDT`, `MASKUSDT`, `MAVUSDT`, `MEGAUSDT`, `MEMEUSDT`, `METUSDT`, `MEUSDT`, `MINAUSDT`, `MIRAUSDT`, `MITOUSDT`, `MMTUSDT`, `MORPHOUSDT`, `MOVEUSDT`, `MOVRUSDT`, `MUBARAKUSDT`, `NEARUSDT`, `NEIROUSDT`, `NEOUSDT`, `NEWTUSDT`, `NIGHTUSDT`, `NILUSDT`, `NMRUSDT`, `NOMUSDT`, `NOTUSDT`, `NXPCUSDT`, `OGNUSDT`, `OGUSDT`, `ONDOUSDT`, `ONTUSDT`, `OPENUSDT`, `OPGUSDT`, `OPNUSDT`, `OPUSDT`, `ORCAUSDT`, `ORDIUSDT`, `OSMOUSDT`, `PARTIUSDT`, `PENDLEUSDT`, `PENGUUSDT`, `PEOPLEUSDT`, `PEPEUSDT`, `PIVXUSDT`, `PIXELUSDT`, `PLUMEUSDT`, `PNUTUSDT`, `POLUSDT`, `PONDUSDT`, `PORTALUSDT`, `PROVEUSDT`, `PUMPUSDT`, `PYRUSDT`, `PYTHUSDT`, `QTUMUSDT`, `RAREUSDT`, `RAYUSDT`, `REDUSDT`, `RENDERUSDT`, `RESOLVUSDT`, `REZUSDT`, `RLCUSDT`, `ROBOUSDT`, `RONINUSDT`, `ROSEUSDT`, `RVNUSDT`, `SAGAUSDT`, `SAHARAUSDT`, `SANDUSDT`, `SAPIENUSDT`, `SEIUSDT`, `SENTUSDT`, `SHIBUSDT`, `SIGNUSDT`, `SKLUSDT`, `SLPUSDT`, `SNXUSDT`, `SOLUSDT`, `SOLVUSDT`, `SOMIUSDT`, `SOPHUSDT`, `SPKUSDT`, `STOUSDT`, `STRKUSDT`, `SUIUSDT`, `SUNUSDT`, `SUPERUSDT`, `SUSDT`, `SUSHIUSDT`, `SXTUSDT`, `SYNUSDT`, `TAOUSDT`, `THEUSDT`, `TIAUSDT`, `TNSRUSDT`, `TONUSDT`, `TOWNSUSDT`, `TRBUSDT`, `TREEUSDT`, `TRUMPUSDT`, `TRXUSDT`, `TSTUSDT`, `TURBOUSDT`, `TURTLEUSDT`, `TUTUSDT`, `TWTUSDT`, `UMAUSDT`, `UNIUSDT`, `USD1USDT`, `USUALUSDT`, `VANAUSDT`, `VETUSDT`, `VICUSDT`, `VIRTUALUSDT`, `WALUSDT`, `WBETHUSDT`, `WBTCUSDT`, `WCTUSDT`, `WIFUSDT`, `WLDUSDT`, `WLFIUSDT`, `WUSDT`, `XAIUSDT`, `XAUTUSDT`, `XLMUSDT`, `XPLUSDT`, `XRPUSDT`, `XTZUSDT`, `YBUSDT`, `YGGUSDT`, `ZAMAUSDT`, `ZBTUSDT`, `ZECUSDT`, `ZENUSDT`, `ZILUSDT`, `ZKCUSDT`, `ZKPUSDT`, `ZKUSDT`, `ZROUSDT`, `币安人生USDT`
- universe_mode: dynamic
- time_periods_tested: `2025-06-01` -> `2026-06-01`
- changed_param: `analysis.regime_btc_7d_drop_pct, analysis.regime_eth_7d_drop_pct, analysis.regime_require_both_trend`
- old_value: `-5.0, -8.0, False`
- new_value: `-3.0, -5.0, True`
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
| closed_trades | 56.00 | 49.00 | -7.00 |
| stop_rate | 80.36% | 77.55% | -2.81% |
| profit_factor | 0.66 | 0.73 | 0.06 |
| avg_r | -0.28 | -0.20 | 0.07 |
| max_drawdown_pct | 22.61% | 24.24% | 1.63% |
| net_return_pct | -14.17% | -10.88% | 3.29% |
| sharpe | -0.73 | -0.57 | 0.16 |
| first_trade_created_at | 2025-06-01T08:00:00+00:00 | 2025-06-02T16:00:00+00:00 | n/a |

## 样本规则

- closed_trades < 20 时，默认 verdict 为 `retest`。
- 交易数下降超过 50% 时，标记 possible_over_filtering=true。
- 自动报告不会直接写 `keep`；采用默认策略前需要跨时段复测和人工复盘。

## 变更明细

| changed_param | old_value | new_value |
|---|---:|---:|
| `analysis.regime_btc_7d_drop_pct` | `-5.0` | `-3.0` |
| `analysis.regime_eth_7d_drop_pct` | `-8.0` | `-5.0` |
| `analysis.regime_require_both_trend` | `False` | `True` |

## Raw Metrics

```json
{
  "baseline": {
    "trades": 385,
    "closed_trades": 56,
    "open_trades": 2,
    "win_rate": 19.642857142857142,
    "profit_factor": 0.6629085989490314,
    "avg_r": -0.2770615806679856,
    "net_return_pct": -14.172516770093624,
    "max_drawdown": 2395.804202791831,
    "max_drawdown_pct": 22.606937554487807,
    "intrabar_max_drawdown": 2319.9385592926146,
    "intrabar_max_drawdown_pct": 22.077585459941453,
    "tp1_rate": 25.0,
    "tp2_rate": 19.642857142857142,
    "stop_rate": 80.35714285714286,
    "fee_drag": 90.09969221777382,
    "tail_max_loss": -108.56851994287817,
    "cagr": -14.172516770093624,
    "sharpe": -0.7290522028119927,
    "sortino": -0.8404180853657471,
    "exposure_pct": 88.67579908675799,
    "turnover": 7.474030755914036,
    "sample_sufficient": true,
    "sample_warning": ""
  },
  "variant": {
    "trades": 302,
    "closed_trades": 49,
    "open_trades": 3,
    "win_rate": 22.448979591836736,
    "profit_factor": 0.7261226020000187,
    "avg_r": -0.2033760597415057,
    "net_return_pct": -10.881749618474746,
    "max_drawdown": 2714.4726081179215,
    "max_drawdown_pct": 24.23999386231287,
    "intrabar_max_drawdown": 2673.7256890036006,
    "intrabar_max_drawdown_pct": 23.99372378228574,
    "tp1_rate": 34.69387755102041,
    "tp2_rate": 22.448979591836736,
    "stop_rate": 77.55102040816327,
    "fee_drag": 81.12675966507629,
    "tail_max_loss": -114.60277747358965,
    "cagr": -10.881749618474746,
    "sharpe": -0.5706966136248354,
    "sortino": -0.6828742911135459,
    "exposure_pct": 88.03652968036529,
    "turnover": 6.7575775247752246,
    "sample_sufficient": true,
    "sample_warning": ""
  }
}
```
