---
created: 2026-07-26 11:54:02 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: relative_strength_soft_gate_btc_eth_minus_1_0
baseline_run_id: e6a285634eae
variant_run_id: c2156ff9cdf8
changed_param: analysis.relative_strength_soft_gate_enabled, analysis.relative_strength_min_pct
old_value: False, -0.5
new_value: True, -1.0
sample_sufficient: true
universe_mode: dynamic
verdict: reject_candidate
report_version: v1
---

# A/B 实验报告 relative_strength_soft_gate_btc_eth_minus_1_0 v1

- experiment_id: `relative_strength_soft_gate_btc_eth_minus_1_0`
- description: Sensitivity test: soft gate BUY_CANDIDATE entries when 24h return underperforms the BTC/ETH average by more than 1.0 percentage point.
- baseline_run_id: `e6a285634eae`
- variant_run_id: `c2156ff9cdf8`
- symbols: `0GUSDT`, `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1INCHUSDT`, `2ZUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACHUSDT`, `ADAUSDT`, `AEVOUSDT`, `AIGENSYNUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALCXUSDT`, `ALGOUSDT`, `ALICEUSDT`, `ALLOUSDT`, `ALPINEUSDT`, `ALTUSDT`, `ANIMEUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ASRUSDT`, `ASTERUSDT`, `ATMUSDT`, `ATUSDT`, `AUCTIONUSDT`, `AUSDT`, `AVAXUSDT`, `AVNTUSDT`, `AWEUSDT`, `AXLUSDT`, `AXSUSDT`, `BABYUSDT`, `BANANAS31USDT`, `BARDUSDT`, `BATUSDT`, `BBUSDT`, `BCHUSDT`, `BELUSDT`, `BERAUSDT`, `BIOUSDT`, `BMTUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BREVUSDT`, `BROCCOLI714USDT`, `BTCUSDT`, `C98USDT`, `CAKEUSDT`, `CELOUSDT`, `CFGUSDT`, `CFXUSDT`, `CHIPUSDT`, `CHZUSDT`, `CKBUSDT`, `COMPUSDT`, `COSUSDT`, `COTIUSDT`, `COWUSDT`, `CRVUSDT`, `CTSIUSDT`, `CUSDT`, `CYBERUSDT`, `DASHUSDT`, `DCRUSDT`, `DEXEUSDT`, `DIAUSDT`, `DOGEUSDT`, `DOGSUSDT`, `DOLOUSDT`, `DOTUSDT`, `DUSDT`, `DUSKUSDT`, `DYMUSDT`, `EDENUSDT`, `EDUUSDT`, `EIGENUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSOUSDT`, `ENSUSDT`, `EPICUSDT`, `ERAUSDT`, `ESPUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `EULUSDT`, `FETUSDT`, `FFUSDT`, `FIDAUSDT`, `FILUSDT`, `FLOKIUSDT`, `FLOWUSDT`, `FLUXUSDT`, `FOGOUSDT`, `FORMUSDT`, `FRAXUSDT`, `FUSDT`, `GALAUSDT`, `GENIUSUSDT`, `GIGGLEUSDT`, `GMTUSDT`, `GMXUSDT`, `GNSUSDT`, `GPSUSDT`, `GTCUSDT`, `GUNUSDT`, `HAEDALUSDT`, `HBARUSDT`, `HEIUSDT`, `HEMIUSDT`, `HFTUSDT`, `HIGHUSDT`, `HMSTRUSDT`, `HOLOUSDT`, `HOMEUSDT`, `HUMAUSDT`, `HYPERUSDT`, `ICPUSDT`, `ILVUSDT`, `INITUSDT`, `INJUSDT`, `IOUSDT`, `JASMYUSDT`, `JTOUSDT`, `JUVUSDT`, `KAIAUSDT`, `KAITOUSDT`, `KATUSDT`, `KERNELUSDT`, `KITEUSDT`, `KMNOUSDT`, `KNCUSDT`, `LAUSDT`, `LAYERUSDT`, `LDOUSDT`, `LINEAUSDT`, `LINKUSDT`, `LISTAUSDT`, `LPTUSDT`, `LSKUSDT`, `LTCUSDT`, `LUNAUSDT`, `LUNCUSDT`, `MAGICUSDT`, `MASKUSDT`, `MAVUSDT`, `MEGAUSDT`, `MEMEUSDT`, `METUSDT`, `MEUSDT`, `MINAUSDT`, `MIRAUSDT`, `MITOUSDT`, `MMTUSDT`, `MORPHOUSDT`, `MOVEUSDT`, `MOVRUSDT`, `MUBARAKUSDT`, `NEARUSDT`, `NEIROUSDT`, `NEOUSDT`, `NEWTUSDT`, `NIGHTUSDT`, `NILUSDT`, `NMRUSDT`, `NOMUSDT`, `NOTUSDT`, `NXPCUSDT`, `OGNUSDT`, `OGUSDT`, `ONDOUSDT`, `ONTUSDT`, `OPENUSDT`, `OPGUSDT`, `OPNUSDT`, `OPUSDT`, `ORCAUSDT`, `ORDIUSDT`, `OSMOUSDT`, `PARTIUSDT`, `PENDLEUSDT`, `PENGUUSDT`, `PEOPLEUSDT`, `PEPEUSDT`, `PIVXUSDT`, `PIXELUSDT`, `PLUMEUSDT`, `PNUTUSDT`, `POLUSDT`, `PONDUSDT`, `PORTALUSDT`, `PROVEUSDT`, `PUMPUSDT`, `PYRUSDT`, `PYTHUSDT`, `QTUMUSDT`, `RAREUSDT`, `RAYUSDT`, `REDUSDT`, `RENDERUSDT`, `RESOLVUSDT`, `REZUSDT`, `RLCUSDT`, `ROBOUSDT`, `RONINUSDT`, `ROSEUSDT`, `RVNUSDT`, `SAGAUSDT`, `SAHARAUSDT`, `SANDUSDT`, `SAPIENUSDT`, `SEIUSDT`, `SENTUSDT`, `SHIBUSDT`, `SIGNUSDT`, `SKLUSDT`, `SLPUSDT`, `SNXUSDT`, `SOLUSDT`, `SOLVUSDT`, `SOMIUSDT`, `SOPHUSDT`, `SPKUSDT`, `STOUSDT`, `STRKUSDT`, `SUIUSDT`, `SUNUSDT`, `SUPERUSDT`, `SUSDT`, `SUSHIUSDT`, `SXTUSDT`, `SYNUSDT`, `TAOUSDT`, `THEUSDT`, `TIAUSDT`, `TNSRUSDT`, `TONUSDT`, `TOWNSUSDT`, `TRBUSDT`, `TREEUSDT`, `TRUMPUSDT`, `TRXUSDT`, `TSTUSDT`, `TURBOUSDT`, `TURTLEUSDT`, `TUTUSDT`, `TWTUSDT`, `UMAUSDT`, `UNIUSDT`, `USD1USDT`, `USUALUSDT`, `VANAUSDT`, `VETUSDT`, `VICUSDT`, `VIRTUALUSDT`, `WALUSDT`, `WBETHUSDT`, `WBTCUSDT`, `WCTUSDT`, `WIFUSDT`, `WLDUSDT`, `WLFIUSDT`, `WUSDT`, `XAIUSDT`, `XAUTUSDT`, `XLMUSDT`, `XPLUSDT`, `XRPUSDT`, `XTZUSDT`, `XVGUSDT`, `YBUSDT`, `YGGUSDT`, `ZAMAUSDT`, `ZBTUSDT`, `ZECUSDT`, `ZENUSDT`, `ZILUSDT`, `ZKCUSDT`, `ZKPUSDT`, `ZKUSDT`, `ZROUSDT`, `币安人生USDT`
- universe_mode: dynamic
- time_periods_tested: `2025-06-01` -> `2026-06-01`
- changed_param: `analysis.relative_strength_soft_gate_enabled, analysis.relative_strength_min_pct`
- old_value: `False, -0.5`
- new_value: `True, -1.0`
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
- baseline_universe_refreshes: 366
- variant_universe_refreshes: 366

## 指标对比

| Metric | Baseline | Variant | Delta |
|---|---:|---:|---:|
| closed_trades | 57.00 | 57.00 | 0.00 |
| stop_rate | 85.96% | 85.96% | 0.00% |
| profit_factor | 1.11 | 1.03 | -0.08 |
| avg_r | 0.08 | 0.03 | -0.05 |
| max_drawdown_pct | 20.75% | 20.93% | 0.18% |
| net_return_pct | 3.11% | 0.25% | -2.86% |
| sharpe | 0.26 | 0.10 | -0.17 |
| first_trade_created_at | 2025-06-01T08:00:00+00:00 | 2025-06-01T08:00:00+00:00 | n/a |

## 样本规则

- closed_trades < 20 时，默认 verdict 为 `retest`。
- 交易数下降超过 50% 时，标记 possible_over_filtering=true。
- 自动报告不会直接写 `keep`；采用默认策略前需要跨时段复测和人工复盘。

## 变更明细

| changed_param | old_value | new_value |
|---|---:|---:|
| `analysis.relative_strength_soft_gate_enabled` | `False` | `True` |
| `analysis.relative_strength_min_pct` | `-0.5` | `-1.0` |

## Raw Metrics

```json
{
  "baseline": {
    "trades": 389,
    "closed_trades": 57,
    "open_trades": 1,
    "win_rate": 40.35087719298245,
    "profit_factor": 1.1084402273665406,
    "avg_r": 0.07747588342292856,
    "net_return_pct": 3.1141295724147033,
    "max_drawdown": 2525.3293105807606,
    "max_drawdown_pct": 20.747383669162712,
    "intrabar_max_drawdown": 2469.7095471564644,
    "intrabar_max_drawdown_pct": 20.444094626200286,
    "tp1_rate": 40.35087719298245,
    "tp2_rate": 14.035087719298245,
    "stop_rate": 85.96491228070175,
    "fee_drag": 105.0726162312896,
    "tail_max_loss": -123.90935785436643,
    "cagr": 3.1141295724147033,
    "sharpe": 0.26428487207953116,
    "sortino": 0.2641862069291116,
    "exposure_pct": 52.10045662100457,
    "turnover": 8.181889958857594,
    "sample_sufficient": true,
    "sample_warning": ""
  },
  "variant": {
    "trades": 387,
    "closed_trades": 57,
    "open_trades": 1,
    "win_rate": 38.59649122807017,
    "profit_factor": 1.0301679985231726,
    "avg_r": 0.029710948777821836,
    "net_return_pct": 0.2509088382968816,
    "max_drawdown": 2482.4837684757786,
    "max_drawdown_pct": 20.929637994809788,
    "intrabar_max_drawdown": 2381.0646697268166,
    "intrabar_max_drawdown_pct": 20.307933053411034,
    "tp1_rate": 36.84210526315789,
    "tp2_rate": 14.035087719298245,
    "stop_rate": 85.96491228070175,
    "fee_drag": 103.91967576860448,
    "tail_max_loss": -122.02867322892455,
    "cagr": 0.2509088382968816,
    "sharpe": 0.09927196192124407,
    "sortino": 0.09431462675431587,
    "exposure_pct": 52.10045662100457,
    "turnover": 8.033368062715407,
    "sample_sufficient": true,
    "sample_warning": ""
  }
}
```
