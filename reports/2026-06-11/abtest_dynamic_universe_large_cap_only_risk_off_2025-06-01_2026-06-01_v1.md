---
created: 2026-06-11 23:21:03 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: large_cap_only_risk_off
baseline_run_id: 763dba3b3653
variant_run_id: 4f563eab44be
changed_param: analysis.risk_off_core_buy_enabled, analysis.risk_off_large_cap_buy_enabled
old_value: False, False
new_value: False, True
sample_sufficient: true
universe_mode: dynamic
verdict: reject_candidate
report_version: v1
---

# A/B 实验报告 large_cap_only_risk_off v1

- experiment_id: `large_cap_only_risk_off`
- description: RISK_OFF: pause altcoin only; allow BTC/ETH/BNB/SOL entry via risk_off_large_cap_buy_enabled. Baseline keeps both flags false (all paused).
- baseline_run_id: `763dba3b3653`
- variant_run_id: `4f563eab44be`
- symbols: `0GUSDT`, `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1INCHUSDT`, `2ZUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACHUSDT`, `ADAUSDT`, `AEVOUSDT`, `AIGENSYNUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALCXUSDT`, `ALGOUSDT`, `ALICEUSDT`, `ALLOUSDT`, `ALPINEUSDT`, `ALTUSDT`, `ANIMEUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ASRUSDT`, `ASTERUSDT`, `ATMUSDT`, `ATUSDT`, `AUCTIONUSDT`, `AUSDT`, `AVAXUSDT`, `AVNTUSDT`, `AXLUSDT`, `AXSUSDT`, `BABYUSDT`, `BANANAS31USDT`, `BARDUSDT`, `BATUSDT`, `BBUSDT`, `BCHUSDT`, `BERAUSDT`, `BIOUSDT`, `BMTUSDT`, `BNBUSDT`, `BOMEUSDT`, `BONKUSDT`, `BREVUSDT`, `BROCCOLI714USDT`, `BTCUSDT`, `C98USDT`, `CAKEUSDT`, `CELOUSDT`, `CFGUSDT`, `CFXUSDT`, `CHIPUSDT`, `CHZUSDT`, `CKBUSDT`, `COMPUSDT`, `COSUSDT`, `COTIUSDT`, `COWUSDT`, `CRVUSDT`, `CTSIUSDT`, `CUSDT`, `CYBERUSDT`, `DASHUSDT`, `DEXEUSDT`, `DIAUSDT`, `DOGEUSDT`, `DOGSUSDT`, `DOLOUSDT`, `DOTUSDT`, `DUSDT`, `DUSKUSDT`, `DYMUSDT`, `EDENUSDT`, `EDUUSDT`, `EIGENUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSOUSDT`, `ENSUSDT`, `EPICUSDT`, `ERAUSDT`, `ESPUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `EULUSDT`, `FETUSDT`, `FFUSDT`, `FIDAUSDT`, `FILUSDT`, `FLOKIUSDT`, `FLOWUSDT`, `FLUXUSDT`, `FOGOUSDT`, `FORMUSDT`, `FRAXUSDT`, `FUSDT`, `GALAUSDT`, `GENIUSUSDT`, `GIGGLEUSDT`, `GMTUSDT`, `GMXUSDT`, `GNSUSDT`, `GPSUSDT`, `GTCUSDT`, `GUNUSDT`, `HBARUSDT`, `HEIUSDT`, `HEMIUSDT`, `HFTUSDT`, `HIGHUSDT`, `HMSTRUSDT`, `HOLOUSDT`, `HOMEUSDT`, `HUMAUSDT`, `HYPERUSDT`, `ICPUSDT`, `ILVUSDT`, `INITUSDT`, `INJUSDT`, `IOUSDT`, `JASMYUSDT`, `JTOUSDT`, `JUVUSDT`, `KAIAUSDT`, `KAITOUSDT`, `KATUSDT`, `KERNELUSDT`, `KITEUSDT`, `KMNOUSDT`, `KNCUSDT`, `LAUSDT`, `LAYERUSDT`, `LDOUSDT`, `LINEAUSDT`, `LINKUSDT`, `LISTAUSDT`, `LPTUSDT`, `LSKUSDT`, `LTCUSDT`, `LUNAUSDT`, `LUNCUSDT`, `MAGICUSDT`, `MASKUSDT`, `MAVUSDT`, `MEGAUSDT`, `MEMEUSDT`, `METUSDT`, `MEUSDT`, `MINAUSDT`, `MIRAUSDT`, `MITOUSDT`, `MMTUSDT`, `MORPHOUSDT`, `MOVEUSDT`, `MOVRUSDT`, `MUBARAKUSDT`, `NEARUSDT`, `NEIROUSDT`, `NEOUSDT`, `NEWTUSDT`, `NIGHTUSDT`, `NILUSDT`, `NMRUSDT`, `NOMUSDT`, `NOTUSDT`, `NXPCUSDT`, `OGNUSDT`, `OGUSDT`, `ONDOUSDT`, `ONTUSDT`, `OPENUSDT`, `OPGUSDT`, `OPNUSDT`, `OPUSDT`, `ORCAUSDT`, `ORDIUSDT`, `OSMOUSDT`, `PARTIUSDT`, `PENDLEUSDT`, `PENGUUSDT`, `PEOPLEUSDT`, `PEPEUSDT`, `PIVXUSDT`, `PIXELUSDT`, `PLUMEUSDT`, `PNUTUSDT`, `POLUSDT`, `PONDUSDT`, `PORTALUSDT`, `PROVEUSDT`, `PUMPUSDT`, `PYRUSDT`, `PYTHUSDT`, `QTUMUSDT`, `RAREUSDT`, `RAYUSDT`, `REDUSDT`, `RENDERUSDT`, `RESOLVUSDT`, `REZUSDT`, `RLCUSDT`, `ROBOUSDT`, `RONINUSDT`, `ROSEUSDT`, `RVNUSDT`, `SAGAUSDT`, `SAHARAUSDT`, `SANDUSDT`, `SAPIENUSDT`, `SEIUSDT`, `SENTUSDT`, `SHIBUSDT`, `SIGNUSDT`, `SKLUSDT`, `SLPUSDT`, `SNXUSDT`, `SOLUSDT`, `SOLVUSDT`, `SOMIUSDT`, `SOPHUSDT`, `SPKUSDT`, `STOUSDT`, `STRKUSDT`, `SUIUSDT`, `SUNUSDT`, `SUPERUSDT`, `SUSDT`, `SUSHIUSDT`, `SXTUSDT`, `SYNUSDT`, `TAOUSDT`, `THEUSDT`, `TIAUSDT`, `TNSRUSDT`, `TONUSDT`, `TOWNSUSDT`, `TRBUSDT`, `TREEUSDT`, `TRUMPUSDT`, `TRXUSDT`, `TSTUSDT`, `TURBOUSDT`, `TURTLEUSDT`, `TUTUSDT`, `TWTUSDT`, `UMAUSDT`, `UNIUSDT`, `USD1USDT`, `USUALUSDT`, `VANAUSDT`, `VETUSDT`, `VICUSDT`, `VIRTUALUSDT`, `WALUSDT`, `WBETHUSDT`, `WBTCUSDT`, `WCTUSDT`, `WIFUSDT`, `WLDUSDT`, `WLFIUSDT`, `WUSDT`, `XAIUSDT`, `XAUTUSDT`, `XLMUSDT`, `XPLUSDT`, `XRPUSDT`, `XTZUSDT`, `YBUSDT`, `YGGUSDT`, `ZAMAUSDT`, `ZBTUSDT`, `ZECUSDT`, `ZENUSDT`, `ZILUSDT`, `ZKCUSDT`, `ZKPUSDT`, `ZKUSDT`, `ZROUSDT`, `币安人生USDT`
- universe_mode: dynamic
- time_periods_tested: `2025-06-01` -> `2026-06-01`
- changed_param: `analysis.risk_off_core_buy_enabled, analysis.risk_off_large_cap_buy_enabled`
- old_value: `False, False`
- new_value: `False, True`
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
| closed_trades | 57.00 | 76.00 | 19.00 |
| stop_rate | 85.96% | 84.21% | -1.75% |
| profit_factor | 1.11 | 0.95 | -0.16 |
| avg_r | 0.08 | -0.02 | -0.10 |
| max_drawdown_pct | 20.74% | 22.19% | 1.45% |
| net_return_pct | 3.12% | -3.12% | -6.24% |
| sharpe | 0.26 | -0.07 | -0.33 |
| first_trade_created_at | 2025-06-01T08:00:00+00:00 | 2025-06-01T08:00:00+00:00 | n/a |

## 样本规则

- closed_trades < 20 时，默认 verdict 为 `retest`。
- 交易数下降超过 50% 时，标记 possible_over_filtering=true。
- 自动报告不会直接写 `keep`；采用默认策略前需要跨时段复测和人工复盘。

## 变更明细

| changed_param | old_value | new_value |
|---|---:|---:|
| `analysis.risk_off_core_buy_enabled` | `False` | `False` |
| `analysis.risk_off_large_cap_buy_enabled` | `False` | `True` |

## Raw Metrics

```json
{
  "baseline": {
    "trades": 387,
    "closed_trades": 57,
    "open_trades": 1,
    "win_rate": 40.35087719298245,
    "profit_factor": 1.1085498859208813,
    "avg_r": 0.07746094957893503,
    "net_return_pct": 3.117817201675166,
    "max_drawdown": 2524.9843278450226,
    "max_drawdown_pct": 20.744549389630293,
    "intrabar_max_drawdown": 2469.365847187475,
    "intrabar_max_drawdown_pct": 20.44124950026346,
    "tp1_rate": 40.35087719298245,
    "tp2_rate": 14.035087719298245,
    "stop_rate": 85.96491228070175,
    "fee_drag": 105.13122209926844,
    "tail_max_loss": -123.90935785436643,
    "cagr": 3.117817201675166,
    "sharpe": 0.26457611778930706,
    "sortino": 0.264007827957292,
    "exposure_pct": 52.10045662100457,
    "turnover": 8.18605489886344,
    "sample_sufficient": true,
    "sample_warning": ""
  },
  "variant": {
    "trades": 413,
    "closed_trades": 76,
    "open_trades": 1,
    "win_rate": 34.21052631578947,
    "profit_factor": 0.9456643820417481,
    "avg_r": -0.018798658849066098,
    "net_return_pct": -3.121837342286604,
    "max_drawdown": 2497.9278879204594,
    "max_drawdown_pct": 22.191260552638685,
    "intrabar_max_drawdown": 2439.9981870467764,
    "intrabar_max_drawdown_pct": 21.858365785580666,
    "tp1_rate": 34.21052631578947,
    "tp2_rate": 15.789473684210526,
    "stop_rate": 84.21052631578947,
    "fee_drag": 139.14020859835287,
    "tail_max_loss": -116.04311366856561,
    "cagr": -3.121837342286604,
    "sharpe": -0.06537472141700082,
    "sortino": -0.07924087978814565,
    "exposure_pct": 89.63470319634703,
    "turnover": 10.986825943568814,
    "sample_sufficient": true,
    "sample_warning": ""
  }
}
```
