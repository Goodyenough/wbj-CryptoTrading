---
created: 2026-06-11 16:18:42 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: risk_off_no_core_entry_reclaim_ema_stop_sensitive
baseline_run_id: 05f9aba00146
variant_run_id: 463df2acd88e
changed_param: analysis.risk_off_core_buy_enabled, analysis.entry_reclaim_close_enabled, analysis.tp1_ema_trailing_stop_enabled, analysis.regime_btc_7d_drop_pct, analysis.regime_eth_7d_drop_pct, analysis.regime_require_both_trend
old_value: True, False, False, -5.0, -8.0, False
new_value: False, True, True, -3.0, -5.0, True
sample_sufficient: true
universe_mode: dynamic
verdict: retest
report_version: v1
---

# A/B 实验报告 risk_off_no_core_entry_reclaim_ema_stop_sensitive v1

- experiment_id: `risk_off_no_core_entry_reclaim_ema_stop_sensitive`
- description: Three-way combo (RISK_OFF core-buy pause + entry reclaim + TP1 EMA trailing stop) with tighter regime thresholds.
- baseline_run_id: `05f9aba00146`
- variant_run_id: `463df2acd88e`
- symbols: `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1INCHUSDT`, `1MBABYDOGEUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACHUSDT`, `ACTUSDT`, `ACXUSDT`, `ADAUSDT`, `AEVOUSDT`, `AGLDUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALGOUSDT`, `ALICEUSDT`, `ALPINEUSDT`, `ALTUSDT`, `AMPUSDT`, `ANIMEUSDT`, `ANKRUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARDRUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ASRUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AUDIOUSDT`, `AVAUSDT`, `AVAXUSDT`, `AXLUSDT`, `AXSUSDT`, `BABYUSDT`, `BANANAUSDT`, `BATUSDT`, `BBUSDT`, `BCHUSDT`, `BEAMXUSDT`, `BERAUSDT`, `BIOUSDT`, `BLURUSDT`, `BMTUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BTCUSDT`, `BTTCUSDT`, `C98USDT`, `CAKEUSDT`, `CATIUSDT`, `CELOUSDT`, `CETUSUSDT`, `CFXUSDT`, `CGPTUSDT`, `CHRUSDT`, `CHZUSDT`, `CKBUSDT`, `COMPUSDT`, `COOKIEUSDT`, `COSUSDT`, `COTIUSDT`, `COWUSDT`, `CRVUSDT`, `CTKUSDT`, `CTSIUSDT`, `CVCUSDT`, `CVXUSDT`, `DASHUSDT`, `DEXEUSDT`, `DGBUSDT`, `DIAUSDT`, `DODOUSDT`, `DOGEUSDT`, `DOGSUSDT`, `DOTUSDT`, `DUSDT`, `DYDXUSDT`, `DYMUSDT`, `EGLDUSDT`, `EIGENUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `FETUSDT`, `FIDAUSDT`, `FILUSDT`, `FLOKIUSDT`, `FLOWUSDT`, `FORMUSDT`, `FTTUSDT`, `GALAUSDT`, `GASUSDT`, `GLMRUSDT`, `GLMUSDT`, `GMTUSDT`, `GPSUSDT`, `GRTUSDT`, `GUNUSDT`, `GUSDT`, `HBARUSDT`, `HEIUSDT`, `HIGHUSDT`, `HIVEUSDT`, `HMSTRUSDT`, `HOTUSDT`, `HUMAUSDT`, `HYPERUSDT`, `ICPUSDT`, `IDUSDT`, `IMXUSDT`, `INITUSDT`, `INJUSDT`, `IOSTUSDT`, `IOTAUSDT`, `IOTXUSDT`, `IOUSDT`, `IQUSDT`, `JASMYUSDT`, `JSTUSDT`, `JTOUSDT`, `JUVUSDT`, `KAIAUSDT`, `KAITOUSDT`, `KAVAUSDT`, `KERNELUSDT`, `KSMUSDT`, `LAYERUSDT`, `LDOUSDT`, `LINKUSDT`, `LISTAUSDT`, `LPTUSDT`, `LQTYUSDT`, `LTCUSDT`, `LUMIAUSDT`, `LUNAUSDT`, `LUNCUSDT`, `MAGICUSDT`, `MANAUSDT`, `MANTAUSDT`, `MASKUSDT`, `MBOXUSDT`, `MEMEUSDT`, `METISUSDT`, `MEUSDT`, `MINAUSDT`, `MOVEUSDT`, `MOVRUSDT`, `MUBARAKUSDT`, `NEARUSDT`, `NEIROUSDT`, `NEOUSDT`, `NILUSDT`, `NMRUSDT`, `NOTUSDT`, `NXPCUSDT`, `OGNUSDT`, `OGUSDT`, `ONDOUSDT`, `ONEUSDT`, `ONTUSDT`, `OPUSDT`, `ORCAUSDT`, `ORDIUSDT`, `OSMOUSDT`, `PARTIUSDT`, `PENDLEUSDT`, `PENGUUSDT`, `PEOPLEUSDT`, `PEPEUSDT`, `PHAUSDT`, `PIXELUSDT`, `PNUTUSDT`, `POLUSDT`, `POLYXUSDT`, `PONDUSDT`, `PORTALUSDT`, `POWRUSDT`, `PROMUSDT`, `PSGUSDT`, `PUNDIXUSDT`, `PYRUSDT`, `PYTHUSDT`, `QKCUSDT`, `QNTUSDT`, `QTUMUSDT`, `RADUSDT`, `RAREUSDT`, `RAYUSDT`, `REDUSDT`, `RENDERUSDT`, `REZUSDT`, `RONINUSDT`, `ROSEUSDT`, `RPLUSDT`, `RSRUSDT`, `RUNEUSDT`, `RVNUSDT`, `SAGAUSDT`, `SANDUSDT`, `SANTOSUSDT`, `SCRTUSDT`, `SCRUSDT`, `SEIUSDT`, `SHELLUSDT`, `SHIBUSDT`, `SIGNUSDT`, `SKLUSDT`, `SLPUSDT`, `SNXUSDT`, `SOLUSDT`, `SOLVUSDT`, `SOPHUSDT`, `SPELLUSDT`, `SSVUSDT`, `STEEMUSDT`, `STGUSDT`, `STORJUSDT`, `STOUSDT`, `STRAXUSDT`, `STRKUSDT`, `STXUSDT`, `SUIUSDT`, `SUNUSDT`, `SUPERUSDT`, `SUSDT`, `SUSHIUSDT`, `SXTUSDT`, `SYNUSDT`, `TAOUSDT`, `TFUELUSDT`, `THETAUSDT`, `THEUSDT`, `TIAUSDT`, `TLMUSDT`, `TNSRUSDT`, `TONUSDT`, `TRBUSDT`, `TRUMPUSDT`, `TRXUSDT`, `TSTUSDT`, `TURBOUSDT`, `TUSDT`, `TUTUSDT`, `UNIUSDT`, `USUALUSDT`, `VANAUSDT`, `VANRYUSDT`, `VELODROMEUSDT`, `VETUSDT`, `VICUSDT`, `VIRTUALUSDT`, `VTHOUSDT`, `WAXPUSDT`, `WBTCUSDT`, `WCTUSDT`, `WIFUSDT`, `WINUSDT`, `WLDUSDT`, `WUSDT`, `XAIUSDT`, `XLMUSDT`, `XRPUSDT`, `XTZUSDT`, `XVGUSDT`, `YFIUSDT`, `YGGUSDT`, `ZECUSDT`, `ZENUSDT`, `ZILUSDT`, `ZKUSDT`, `ZROUSDT`, `ZRXUSDT`
- universe_mode: dynamic
- time_periods_tested: `2024-07-01` -> `2025-06-01`
- changed_param: `analysis.risk_off_core_buy_enabled, analysis.entry_reclaim_close_enabled, analysis.tp1_ema_trailing_stop_enabled, analysis.regime_btc_7d_drop_pct, analysis.regime_eth_7d_drop_pct, analysis.regime_require_both_trend`
- old_value: `True, False, False, -5.0, -8.0, False`
- new_value: `False, True, True, -3.0, -5.0, True`
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
- baseline_universe_refreshes: 336
- variant_universe_refreshes: 336

## 指标对比

| Metric | Baseline | Variant | Delta |
|---|---:|---:|---:|
| closed_trades | 70.00 | 49.00 | -21.00 |
| stop_rate | 77.14% | 75.51% | -1.63% |
| profit_factor | 0.74 | 1.58 | 0.84 |
| avg_r | -0.18 | 0.40 | 0.57 |
| max_drawdown_pct | 26.15% | 14.99% | -11.17% |
| net_return_pct | -14.32% | 17.98% | 32.30% |
| sharpe | -0.69 | 1.14 | 1.83 |
| first_trade_created_at | 2024-07-01T20:00:00+00:00 | 2024-07-24T00:00:00+00:00 | n/a |

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
| `analysis.regime_btc_7d_drop_pct` | `-5.0` | `-3.0` |
| `analysis.regime_eth_7d_drop_pct` | `-8.0` | `-5.0` |
| `analysis.regime_require_both_trend` | `False` | `True` |

## Raw Metrics

```json
{
  "baseline": {
    "trades": 492,
    "closed_trades": 70,
    "open_trades": 4,
    "win_rate": 22.857142857142858,
    "profit_factor": 0.744621462042217,
    "avg_r": -0.17863342094033235,
    "net_return_pct": -14.31962046215849,
    "max_drawdown": 3026.4428745376154,
    "max_drawdown_pct": 26.15478209165892,
    "intrabar_max_drawdown": 3009.8665110809106,
    "intrabar_max_drawdown_pct": 26.139663074418106,
    "tp1_rate": 28.57142857142857,
    "tp2_rate": 22.857142857142858,
    "stop_rate": 77.14285714285715,
    "fee_drag": 85.21402738474119,
    "tail_max_loss": -118.56341433539528,
    "cagr": -15.497266244211582,
    "sharpe": -0.6855581798888873,
    "sortino": -0.7551010210656071,
    "exposure_pct": 84.32835820895522,
    "turnover": 7.196186356542488,
    "sample_sufficient": true,
    "sample_warning": ""
  },
  "variant": {
    "trades": 274,
    "closed_trades": 49,
    "open_trades": 2,
    "win_rate": 46.93877551020408,
    "profit_factor": 1.5832904456174,
    "avg_r": 0.3953892660066838,
    "net_return_pct": 17.980933999154924,
    "max_drawdown": 2060.1233225206706,
    "max_drawdown_pct": 14.986015173823814,
    "intrabar_max_drawdown": 2048.6068289993564,
    "intrabar_max_drawdown_pct": 14.976905291422863,
    "tp1_rate": 44.89795918367347,
    "tp2_rate": 24.489795918367346,
    "stop_rate": 75.51020408163265,
    "fee_drag": 82.16914273575269,
    "tail_max_loss": -140.4616040142896,
    "cagr": 19.740961213005924,
    "sharpe": 1.1395631095575727,
    "sortino": 1.088732505721008,
    "exposure_pct": 53.53233830845772,
    "turnover": 6.8514216328733815,
    "sample_sufficient": true,
    "sample_warning": ""
  }
}
```
