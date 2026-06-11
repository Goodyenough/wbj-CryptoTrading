---
created: 2026-06-11 15:25:59 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: risk_off_no_core_entry_reclaim_ema_stop_daily_trend
baseline_run_id: c8843b0f8ec3
variant_run_id: 88ebcb325767
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
- baseline_run_id: `c8843b0f8ec3`
- variant_run_id: `88ebcb325767`
- symbols: `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1INCHUSDT`, `1MBABYDOGEUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACHUSDT`, `ACTUSDT`, `ACXUSDT`, `ADAUSDT`, `AEVOUSDT`, `AGLDUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALGOUSDT`, `ALICEUSDT`, `ALPINEUSDT`, `ALTUSDT`, `AMPUSDT`, `ANIMEUSDT`, `ANKRUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARDRUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ASRUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AUDIOUSDT`, `AVAUSDT`, `AVAXUSDT`, `AXLUSDT`, `AXSUSDT`, `BABYUSDT`, `BANANAUSDT`, `BATUSDT`, `BBUSDT`, `BCHUSDT`, `BEAMXUSDT`, `BERAUSDT`, `BIOUSDT`, `BLURUSDT`, `BMTUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BTCUSDT`, `BTTCUSDT`, `C98USDT`, `CAKEUSDT`, `CATIUSDT`, `CELOUSDT`, `CETUSUSDT`, `CFXUSDT`, `CGPTUSDT`, `CHRUSDT`, `CHZUSDT`, `CKBUSDT`, `COMPUSDT`, `COOKIEUSDT`, `COSUSDT`, `COTIUSDT`, `COWUSDT`, `CRVUSDT`, `CTKUSDT`, `CTSIUSDT`, `CVCUSDT`, `CVXUSDT`, `DASHUSDT`, `DEXEUSDT`, `DGBUSDT`, `DIAUSDT`, `DODOUSDT`, `DOGEUSDT`, `DOGSUSDT`, `DOTUSDT`, `DUSDT`, `DYDXUSDT`, `DYMUSDT`, `EGLDUSDT`, `EIGENUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `FETUSDT`, `FIDAUSDT`, `FILUSDT`, `FLOKIUSDT`, `FLOWUSDT`, `FORMUSDT`, `FTTUSDT`, `GALAUSDT`, `GASUSDT`, `GLMRUSDT`, `GLMUSDT`, `GMTUSDT`, `GPSUSDT`, `GRTUSDT`, `GUNUSDT`, `GUSDT`, `HBARUSDT`, `HEIUSDT`, `HIGHUSDT`, `HIVEUSDT`, `HMSTRUSDT`, `HOTUSDT`, `HUMAUSDT`, `HYPERUSDT`, `ICPUSDT`, `IDUSDT`, `IMXUSDT`, `INITUSDT`, `INJUSDT`, `IOSTUSDT`, `IOTAUSDT`, `IOTXUSDT`, `IOUSDT`, `IQUSDT`, `JASMYUSDT`, `JSTUSDT`, `JTOUSDT`, `JUVUSDT`, `KAIAUSDT`, `KAITOUSDT`, `KAVAUSDT`, `KERNELUSDT`, `KSMUSDT`, `LAYERUSDT`, `LDOUSDT`, `LINKUSDT`, `LISTAUSDT`, `LPTUSDT`, `LQTYUSDT`, `LTCUSDT`, `LUMIAUSDT`, `LUNAUSDT`, `LUNCUSDT`, `MAGICUSDT`, `MANAUSDT`, `MANTAUSDT`, `MASKUSDT`, `MBOXUSDT`, `MEMEUSDT`, `METISUSDT`, `MEUSDT`, `MINAUSDT`, `MOVEUSDT`, `MOVRUSDT`, `MUBARAKUSDT`, `NEARUSDT`, `NEIROUSDT`, `NEOUSDT`, `NILUSDT`, `NMRUSDT`, `NOTUSDT`, `NXPCUSDT`, `OGNUSDT`, `OGUSDT`, `ONDOUSDT`, `ONEUSDT`, `ONTUSDT`, `OPUSDT`, `ORCAUSDT`, `ORDIUSDT`, `OSMOUSDT`, `PARTIUSDT`, `PENDLEUSDT`, `PENGUUSDT`, `PEOPLEUSDT`, `PEPEUSDT`, `PHAUSDT`, `PIXELUSDT`, `PNUTUSDT`, `POLUSDT`, `POLYXUSDT`, `PONDUSDT`, `PORTALUSDT`, `POWRUSDT`, `PROMUSDT`, `PSGUSDT`, `PUNDIXUSDT`, `PYRUSDT`, `PYTHUSDT`, `QKCUSDT`, `QNTUSDT`, `QTUMUSDT`, `RADUSDT`, `RAREUSDT`, `RAYUSDT`, `REDUSDT`, `RENDERUSDT`, `REZUSDT`, `RONINUSDT`, `ROSEUSDT`, `RPLUSDT`, `RSRUSDT`, `RUNEUSDT`, `RVNUSDT`, `SAGAUSDT`, `SANDUSDT`, `SANTOSUSDT`, `SCRTUSDT`, `SCRUSDT`, `SEIUSDT`, `SHELLUSDT`, `SHIBUSDT`, `SIGNUSDT`, `SKLUSDT`, `SLPUSDT`, `SNXUSDT`, `SOLUSDT`, `SOLVUSDT`, `SOPHUSDT`, `SPELLUSDT`, `SSVUSDT`, `STEEMUSDT`, `STGUSDT`, `STORJUSDT`, `STOUSDT`, `STRAXUSDT`, `STRKUSDT`, `STXUSDT`, `SUIUSDT`, `SUNUSDT`, `SUPERUSDT`, `SUSDT`, `SUSHIUSDT`, `SXTUSDT`, `SYNUSDT`, `TAOUSDT`, `TFUELUSDT`, `THETAUSDT`, `THEUSDT`, `TIAUSDT`, `TLMUSDT`, `TNSRUSDT`, `TONUSDT`, `TRBUSDT`, `TRUMPUSDT`, `TRXUSDT`, `TSTUSDT`, `TURBOUSDT`, `TUSDT`, `TUTUSDT`, `UNIUSDT`, `USUALUSDT`, `VANAUSDT`, `VANRYUSDT`, `VELODROMEUSDT`, `VETUSDT`, `VICUSDT`, `VIRTUALUSDT`, `VTHOUSDT`, `WAXPUSDT`, `WBTCUSDT`, `WCTUSDT`, `WIFUSDT`, `WINUSDT`, `WLDUSDT`, `WUSDT`, `XAIUSDT`, `XLMUSDT`, `XRPUSDT`, `XTZUSDT`, `XVGUSDT`, `YFIUSDT`, `YGGUSDT`, `ZECUSDT`, `ZENUSDT`, `ZILUSDT`, `ZKUSDT`, `ZROUSDT`, `ZRXUSDT`
- universe_mode: dynamic
- time_periods_tested: `2024-07-01` -> `2025-06-01`
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
- baseline_universe_refreshes: 336
- variant_universe_refreshes: 336

## 指标对比

| Metric | Baseline | Variant | Delta |
|---|---:|---:|---:|
| closed_trades | 52.00 | 53.00 | 1.00 |
| stop_rate | 73.08% | 81.13% | 8.06% |
| profit_factor | 0.91 | 1.50 | 0.59 |
| avg_r | -0.03 | 0.31 | 0.35 |
| max_drawdown_pct | 18.72% | 15.30% | -3.43% |
| net_return_pct | -5.59% | 15.37% | 20.96% |
| sharpe | -0.25 | 1.05 | 1.30 |
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
| `analysis.daily_trend_required` | `False` | `True` |

## Raw Metrics

```json
{
  "baseline": {
    "trades": 268,
    "closed_trades": 52,
    "open_trades": 3,
    "win_rate": 26.923076923076923,
    "profit_factor": 0.9102519918991828,
    "avg_r": -0.03041598140660157,
    "net_return_pct": -5.58688262495367,
    "max_drawdown": 2170.411957751381,
    "max_drawdown_pct": 18.723989057393542,
    "intrabar_max_drawdown": 2134.121253145846,
    "intrabar_max_drawdown_pct": 18.524093062530373,
    "tp1_rate": 28.846153846153843,
    "tp2_rate": 26.923076923076923,
    "stop_rate": 73.07692307692307,
    "fee_drag": 63.157877648175145,
    "tail_max_loss": -117.19916034615537,
    "cagr": -6.07170748632806,
    "sharpe": -0.2514497640138396,
    "sortino": -0.26403429151851554,
    "exposure_pct": 84.32835820895522,
    "turnover": 5.40397640114904,
    "sample_sufficient": true,
    "sample_warning": ""
  },
  "variant": {
    "trades": 268,
    "closed_trades": 53,
    "open_trades": 2,
    "win_rate": 49.056603773584904,
    "profit_factor": 1.4981781737549311,
    "avg_r": 0.31499070906468973,
    "net_return_pct": 15.37097287079716,
    "max_drawdown": 2074.770861929788,
    "max_drawdown_pct": 15.295226013073576,
    "intrabar_max_drawdown": 2018.135499746404,
    "intrabar_max_drawdown_pct": 14.981950118122944,
    "tp1_rate": 45.28301886792453,
    "tp2_rate": 18.867924528301888,
    "stop_rate": 81.13207547169812,
    "fee_drag": 86.12444854029667,
    "tail_max_loss": -139.8757929975153,
    "cagr": 16.85772855229184,
    "sharpe": 1.049395119190653,
    "sortino": 1.0293310377148268,
    "exposure_pct": 54.02985074626866,
    "turnover": 6.984955492060005,
    "sample_sufficient": true,
    "sample_warning": ""
  }
}
```
