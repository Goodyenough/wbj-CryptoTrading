---
created: 2026-06-11 15:34:47 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: risk_off_no_core_entry_reclaim_ema_stop_daily_trend
baseline_run_id: a8cf291fe2e8
variant_run_id: a29439383caa
changed_param: analysis.risk_off_core_buy_enabled, analysis.entry_reclaim_close_enabled, analysis.tp1_ema_trailing_stop_enabled, analysis.daily_trend_required
old_value: True, False, False, False
new_value: False, True, True, True
sample_sufficient: true
universe_mode: dynamic
verdict: retest
report_version: v1
---

# A/B 实验报告 risk_off_no_core_entry_reclaim_ema_stop_daily_trend v1

- experiment_id: `risk_off_no_core_entry_reclaim_ema_stop_daily_trend`
- description: Combine RISK_OFF core-buy pause, 4h entry reclaim confirmation, TP1 EMA20 trailing stop, and daily trend confirmation (only applies in RISK_ON).
- baseline_run_id: `a8cf291fe2e8`
- variant_run_id: `a29439383caa`
- symbols: `0GUSDT`, `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1INCHUSDT`, `2ZUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACHUSDT`, `ADAUSDT`, `AEVOUSDT`, `AIGENSYNUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALCXUSDT`, `ALGOUSDT`, `ALICEUSDT`, `ALLOUSDT`, `ALPINEUSDT`, `ALTUSDT`, `ANIMEUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ASRUSDT`, `ASTERUSDT`, `ATMUSDT`, `ATUSDT`, `AUCTIONUSDT`, `AUSDT`, `AVAXUSDT`, `AVNTUSDT`, `AXLUSDT`, `AXSUSDT`, `BABYUSDT`, `BANANAS31USDT`, `BARDUSDT`, `BATUSDT`, `BBUSDT`, `BCHUSDT`, `BERAUSDT`, `BIOUSDT`, `BMTUSDT`, `BNBUSDT`, `BOMEUSDT`, `BONKUSDT`, `BREVUSDT`, `BROCCOLI714USDT`, `BTCUSDT`, `C98USDT`, `CAKEUSDT`, `CELOUSDT`, `CFGUSDT`, `CFXUSDT`, `CHIPUSDT`, `CHZUSDT`, `CKBUSDT`, `COMPUSDT`, `COSUSDT`, `COTIUSDT`, `COWUSDT`, `CRVUSDT`, `CTSIUSDT`, `CUSDT`, `CYBERUSDT`, `DASHUSDT`, `DEXEUSDT`, `DIAUSDT`, `DOGEUSDT`, `DOGSUSDT`, `DOLOUSDT`, `DOTUSDT`, `DUSDT`, `DUSKUSDT`, `DYMUSDT`, `EDENUSDT`, `EDUUSDT`, `EIGENUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSOUSDT`, `ENSUSDT`, `EPICUSDT`, `ERAUSDT`, `ESPUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `EULUSDT`, `FETUSDT`, `FFUSDT`, `FIDAUSDT`, `FILUSDT`, `FLOKIUSDT`, `FLOWUSDT`, `FLUXUSDT`, `FOGOUSDT`, `FORMUSDT`, `FRAXUSDT`, `FUSDT`, `GALAUSDT`, `GENIUSUSDT`, `GIGGLEUSDT`, `GMTUSDT`, `GMXUSDT`, `GNSUSDT`, `GPSUSDT`, `GTCUSDT`, `GUNUSDT`, `HBARUSDT`, `HEIUSDT`, `HEMIUSDT`, `HFTUSDT`, `HIGHUSDT`, `HMSTRUSDT`, `HOLOUSDT`, `HOMEUSDT`, `HUMAUSDT`, `HYPERUSDT`, `ICPUSDT`, `ILVUSDT`, `INITUSDT`, `INJUSDT`, `IOUSDT`, `JASMYUSDT`, `JTOUSDT`, `JUVUSDT`, `KAIAUSDT`, `KAITOUSDT`, `KATUSDT`, `KERNELUSDT`, `KITEUSDT`, `KMNOUSDT`, `KNCUSDT`, `LAUSDT`, `LAYERUSDT`, `LDOUSDT`, `LINEAUSDT`, `LINKUSDT`, `LISTAUSDT`, `LPTUSDT`, `LSKUSDT`, `LTCUSDT`, `LUNAUSDT`, `LUNCUSDT`, `MAGICUSDT`, `MASKUSDT`, `MAVUSDT`, `MEGAUSDT`, `MEMEUSDT`, `METUSDT`, `MEUSDT`, `MINAUSDT`, `MIRAUSDT`, `MITOUSDT`, `MMTUSDT`, `MORPHOUSDT`, `MOVEUSDT`, `MOVRUSDT`, `MUBARAKUSDT`, `NEARUSDT`, `NEIROUSDT`, `NEOUSDT`, `NEWTUSDT`, `NIGHTUSDT`, `NILUSDT`, `NMRUSDT`, `NOMUSDT`, `NOTUSDT`, `NXPCUSDT`, `OGNUSDT`, `OGUSDT`, `ONDOUSDT`, `ONTUSDT`, `OPENUSDT`, `OPGUSDT`, `OPNUSDT`, `OPUSDT`, `ORCAUSDT`, `ORDIUSDT`, `OSMOUSDT`, `PARTIUSDT`, `PENDLEUSDT`, `PENGUUSDT`, `PEOPLEUSDT`, `PEPEUSDT`, `PIVXUSDT`, `PIXELUSDT`, `PLUMEUSDT`, `PNUTUSDT`, `POLUSDT`, `PONDUSDT`, `PORTALUSDT`, `PROVEUSDT`, `PUMPUSDT`, `PYRUSDT`, `PYTHUSDT`, `QTUMUSDT`, `RAREUSDT`, `RAYUSDT`, `REDUSDT`, `RENDERUSDT`, `RESOLVUSDT`, `REZUSDT`, `RLCUSDT`, `ROBOUSDT`, `RONINUSDT`, `ROSEUSDT`, `RVNUSDT`, `SAGAUSDT`, `SAHARAUSDT`, `SANDUSDT`, `SAPIENUSDT`, `SEIUSDT`, `SENTUSDT`, `SHIBUSDT`, `SIGNUSDT`, `SKLUSDT`, `SLPUSDT`, `SNXUSDT`, `SOLUSDT`, `SOLVUSDT`, `SOMIUSDT`, `SOPHUSDT`, `SPKUSDT`, `STOUSDT`, `STRKUSDT`, `SUIUSDT`, `SUNUSDT`, `SUPERUSDT`, `SUSDT`, `SUSHIUSDT`, `SXTUSDT`, `SYNUSDT`, `TAOUSDT`, `THEUSDT`, `TIAUSDT`, `TNSRUSDT`, `TONUSDT`, `TOWNSUSDT`, `TRBUSDT`, `TREEUSDT`, `TRUMPUSDT`, `TRXUSDT`, `TSTUSDT`, `TURBOUSDT`, `TURTLEUSDT`, `TUTUSDT`, `TWTUSDT`, `UMAUSDT`, `UNIUSDT`, `USD1USDT`, `USUALUSDT`, `VANAUSDT`, `VETUSDT`, `VICUSDT`, `VIRTUALUSDT`, `WALUSDT`, `WBETHUSDT`, `WBTCUSDT`, `WCTUSDT`, `WIFUSDT`, `WLDUSDT`, `WLFIUSDT`, `WUSDT`, `XAIUSDT`, `XAUTUSDT`, `XLMUSDT`, `XPLUSDT`, `XRPUSDT`, `XTZUSDT`, `YBUSDT`, `YGGUSDT`, `ZAMAUSDT`, `ZBTUSDT`, `ZECUSDT`, `ZENUSDT`, `ZILUSDT`, `ZKCUSDT`, `ZKPUSDT`, `ZKUSDT`, `ZROUSDT`, `币安人生USDT`
- universe_mode: dynamic
- time_periods_tested: `2025-06-01` -> `2026-06-01`
- changed_param: `analysis.risk_off_core_buy_enabled, analysis.entry_reclaim_close_enabled, analysis.tp1_ema_trailing_stop_enabled, analysis.daily_trend_required`
- old_value: `True, False, False, False`
- new_value: `False, True, True, True`
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
| closed_trades | 49.00 | 61.00 | 12.00 |
| stop_rate | 77.55% | 91.80% | 14.25% |
| profit_factor | 0.73 | 0.81 | 0.08 |
| avg_r | -0.20 | -0.13 | 0.07 |
| max_drawdown_pct | 24.24% | 20.47% | -3.77% |
| net_return_pct | -10.62% | -7.82% | 2.80% |
| sharpe | -0.54 | -0.40 | 0.14 |
| first_trade_created_at | 2025-06-02T00:00:00+00:00 | 2025-06-02T00:00:00+00:00 | n/a |

## 样本规则

- closed_trades < 20 时，默认 verdict 为 `retest`。
- 交易数下降超过 50% 时，标记 possible_over_filtering=true。
- 自动报告不会直接写 `keep`；采用默认策略前需要跨时段复测和人工复盘。

## 变更明细

| changed_param | old_value | new_value |
|---|---:|---:|
| `analysis.risk_off_core_buy_enabled` | `True` | `False` |
| `analysis.entry_reclaim_close_enabled` | `False` | `True` |
| `analysis.tp1_ema_trailing_stop_enabled` | `False` | `True` |
| `analysis.daily_trend_required` | `False` | `True` |

## Raw Metrics

```json
{
  "baseline": {
    "trades": 302,
    "closed_trades": 49,
    "open_trades": 3,
    "win_rate": 22.448979591836736,
    "profit_factor": 0.7335465870648034,
    "avg_r": -0.19820595721035383,
    "net_return_pct": -10.621034473218582,
    "max_drawdown": 2722.4137887098896,
    "max_drawdown_pct": 24.239993862312907,
    "intrabar_max_drawdown": 2681.5476646191437,
    "intrabar_max_drawdown_pct": 23.993723782285777,
    "tp1_rate": 32.6530612244898,
    "tp2_rate": 22.448979591836736,
    "stop_rate": 77.55102040816327,
    "fee_drag": 81.52972337365311,
    "tail_max_loss": -114.93804751814146,
    "cagr": -10.621034473218582,
    "sharpe": -0.5445715158743036,
    "sortino": -0.655090699515348,
    "exposure_pct": 88.44748858447488,
    "turnover": 6.79780742067835,
    "sample_sufficient": true,
    "sample_warning": ""
  },
  "variant": {
    "trades": 286,
    "closed_trades": 61,
    "open_trades": 1,
    "win_rate": 36.0655737704918,
    "profit_factor": 0.8118018551068245,
    "avg_r": -0.1267799844714314,
    "net_return_pct": -7.81945024368097,
    "max_drawdown": 2326.123020916659,
    "max_drawdown_pct": 20.465844069995768,
    "intrabar_max_drawdown": 2287.7949731789577,
    "intrabar_max_drawdown_pct": 20.23588134463539,
    "tp1_rate": 34.42622950819672,
    "tp2_rate": 8.19672131147541,
    "stop_rate": 91.80327868852459,
    "fee_drag": 112.83168755987427,
    "tail_max_loss": -117.16873672219305,
    "cagr": -7.81945024368097,
    "sharpe": -0.4022152222937021,
    "sortino": -0.371750184533703,
    "exposure_pct": 51.46118721461187,
    "turnover": 8.569683657016816,
    "sample_sufficient": true,
    "sample_warning": ""
  }
}
```
