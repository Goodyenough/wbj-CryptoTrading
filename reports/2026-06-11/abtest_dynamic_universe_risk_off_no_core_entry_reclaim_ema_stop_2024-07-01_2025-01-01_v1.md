---
created: 2026-06-11 15:44:19 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: risk_off_no_core_entry_reclaim_ema_stop
baseline_run_id: fbe826b87404
variant_run_id: 684536a7843b
changed_param: analysis.risk_off_core_buy_enabled, analysis.entry_reclaim_close_enabled, analysis.tp1_ema_trailing_stop_enabled
old_value: True, False, False
new_value: False, True, True
sample_sufficient: true
universe_mode: dynamic
verdict: retest
report_version: v1
---

# A/B 实验报告 risk_off_no_core_entry_reclaim_ema_stop v1

- experiment_id: `risk_off_no_core_entry_reclaim_ema_stop`
- description: Combine RISK_OFF core-buy pause, 4h entry reclaim confirmation, and TP1 EMA20 trailing stop.
- baseline_run_id: `fbe826b87404`
- variant_run_id: `684536a7843b`
- symbols: `1000CATUSDT`, `1000SATSUSDT`, `1INCHUSDT`, `1MBABYDOGEUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACTUSDT`, `ACXUSDT`, `ADAUSDT`, `AEVOUSDT`, `AGLDUSDT`, `AIUSDT`, `ALGOUSDT`, `ALICEUSDT`, `ALTUSDT`, `AMPUSDT`, `ANKRUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARDRUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AVAUSDT`, `AVAXUSDT`, `AXLUSDT`, `AXSUSDT`, `BANANAUSDT`, `BATUSDT`, `BBUSDT`, `BCHUSDT`, `BEAMXUSDT`, `BLURUSDT`, `BNBUSDT`, `BOMEUSDT`, `BONKUSDT`, `BTCUSDT`, `BTTCUSDT`, `CAKEUSDT`, `CATIUSDT`, `CELOUSDT`, `CETUSUSDT`, `CFXUSDT`, `CHRUSDT`, `CHZUSDT`, `CKBUSDT`, `COMPUSDT`, `COSUSDT`, `COTIUSDT`, `COWUSDT`, `CRVUSDT`, `CTKUSDT`, `CTSIUSDT`, `CVCUSDT`, `CVXUSDT`, `DASHUSDT`, `DEXEUSDT`, `DGBUSDT`, `DIAUSDT`, `DODOUSDT`, `DOGEUSDT`, `DOGSUSDT`, `DOTUSDT`, `DYDXUSDT`, `DYMUSDT`, `EGLDUSDT`, `EIGENUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `FETUSDT`, `FIDAUSDT`, `FILUSDT`, `FLOKIUSDT`, `FLOWUSDT`, `FTTUSDT`, `GALAUSDT`, `GASUSDT`, `GLMRUSDT`, `GLMUSDT`, `GMTUSDT`, `GRTUSDT`, `GUSDT`, `HBARUSDT`, `HIGHUSDT`, `HIVEUSDT`, `HMSTRUSDT`, `HOTUSDT`, `ICPUSDT`, `IDUSDT`, `IMXUSDT`, `INJUSDT`, `IOTAUSDT`, `IOTXUSDT`, `IOUSDT`, `IQUSDT`, `JASMYUSDT`, `JSTUSDT`, `JTOUSDT`, `KAIAUSDT`, `KSMUSDT`, `LDOUSDT`, `LINKUSDT`, `LISTAUSDT`, `LPTUSDT`, `LQTYUSDT`, `LTCUSDT`, `LUMIAUSDT`, `LUNAUSDT`, `LUNCUSDT`, `MAGICUSDT`, `MANAUSDT`, `MANTAUSDT`, `MASKUSDT`, `MBOXUSDT`, `MEMEUSDT`, `METISUSDT`, `MEUSDT`, `MINAUSDT`, `MOVEUSDT`, `MOVRUSDT`, `NEARUSDT`, `NEIROUSDT`, `NEOUSDT`, `NOTUSDT`, `OGNUSDT`, `OGUSDT`, `ONEUSDT`, `OPUSDT`, `ORCAUSDT`, `ORDIUSDT`, `PENDLEUSDT`, `PENGUUSDT`, `PEOPLEUSDT`, `PEPEUSDT`, `PHAUSDT`, `PIXELUSDT`, `PNUTUSDT`, `POLUSDT`, `POLYXUSDT`, `PONDUSDT`, `POWRUSDT`, `PROMUSDT`, `PSGUSDT`, `PYRUSDT`, `PYTHUSDT`, `QKCUSDT`, `QNTUSDT`, `RADUSDT`, `RAREUSDT`, `RAYUSDT`, `RENDERUSDT`, `RONINUSDT`, `ROSEUSDT`, `RSRUSDT`, `RUNEUSDT`, `RVNUSDT`, `SAGAUSDT`, `SANDUSDT`, `SANTOSUSDT`, `SCRTUSDT`, `SCRUSDT`, `SEIUSDT`, `SHIBUSDT`, `SKLUSDT`, `SLPUSDT`, `SNXUSDT`, `SOLUSDT`, `SPELLUSDT`, `SSVUSDT`, `STEEMUSDT`, `STGUSDT`, `STORJUSDT`, `STRAXUSDT`, `STRKUSDT`, `STXUSDT`, `SUIUSDT`, `SUNUSDT`, `SUPERUSDT`, `SUSHIUSDT`, `SYNUSDT`, `TAOUSDT`, `THETAUSDT`, `THEUSDT`, `TIAUSDT`, `TLMUSDT`, `TNSRUSDT`, `TONUSDT`, `TRBUSDT`, `TRXUSDT`, `TURBOUSDT`, `TUSDT`, `UNIUSDT`, `USUALUSDT`, `VANAUSDT`, `VANRYUSDT`, `VELODROMEUSDT`, `VETUSDT`, `VTHOUSDT`, `WAXPUSDT`, `WBTCUSDT`, `WIFUSDT`, `WINUSDT`, `WLDUSDT`, `WUSDT`, `XAIUSDT`, `XLMUSDT`, `XRPUSDT`, `XTZUSDT`, `XVGUSDT`, `YFIUSDT`, `YGGUSDT`, `ZECUSDT`, `ZENUSDT`, `ZILUSDT`, `ZKUSDT`, `ZROUSDT`, `ZRXUSDT`
- universe_mode: dynamic
- time_periods_tested: `2024-07-01` -> `2025-01-01`
- changed_param: `analysis.risk_off_core_buy_enabled, analysis.entry_reclaim_close_enabled, analysis.tp1_ema_trailing_stop_enabled`
- old_value: `True, False, False`
- new_value: `False, True, True`
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
- baseline_universe_refreshes: 185
- variant_universe_refreshes: 185

## 指标对比

| Metric | Baseline | Variant | Delta |
|---|---:|---:|---:|
| closed_trades | 35.00 | 35.00 | 0.00 |
| stop_rate | 65.71% | 71.43% | 5.71% |
| profit_factor | 1.30 | 2.37 | 1.07 |
| avg_r | 0.24 | 0.68 | 0.44 |
| max_drawdown_pct | 10.67% | 9.02% | -1.65% |
| net_return_pct | 7.14% | 24.06% | 16.92% |
| sharpe | 0.78 | 2.34 | 1.57 |
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

## Raw Metrics

```json
{
  "baseline": {
    "trades": 178,
    "closed_trades": 35,
    "open_trades": 2,
    "win_rate": 34.285714285714285,
    "profit_factor": 1.3045231175786178,
    "avg_r": 0.24019530504725956,
    "net_return_pct": 7.141188711650748,
    "max_drawdown": 1067.1418735291263,
    "max_drawdown_pct": 10.671418735291264,
    "intrabar_max_drawdown": 1104.9997915491313,
    "intrabar_max_drawdown_pct": 11.049997915491312,
    "tp1_rate": 37.142857142857146,
    "tp2_rate": 34.285714285714285,
    "stop_rate": 65.71428571428571,
    "fee_drag": 40.61548958822572,
    "tail_max_loss": -117.19916034615537,
    "cagr": 14.663316853283082,
    "sharpe": 0.7773262810702322,
    "sortino": 0.8304264844304116,
    "exposure_pct": 85.05434782608695,
    "turnover": 3.488987406992759,
    "sample_sufficient": true,
    "sample_warning": ""
  },
  "variant": {
    "trades": 183,
    "closed_trades": 35,
    "open_trades": 1,
    "win_rate": 57.14285714285714,
    "profit_factor": 2.371781178573125,
    "avg_r": 0.6762582180727168,
    "net_return_pct": 24.059934274458605,
    "max_drawdown": 1226.5014623239476,
    "max_drawdown_pct": 9.016904140370709,
    "intrabar_max_drawdown": 1160.965093496994,
    "intrabar_max_drawdown_pct": 8.577862148118559,
    "tp1_rate": 54.285714285714285,
    "tp2_rate": 28.57142857142857,
    "stop_rate": 71.42857142857143,
    "fee_drag": 57.89936167107723,
    "tail_max_loss": -138.9828427515564,
    "cagr": 53.3686137643016,
    "sharpe": 2.342921200498839,
    "sortino": 2.3831612299885885,
    "exposure_pct": 52.264492753623195,
    "turnover": 4.570827731927035,
    "sample_sufficient": true,
    "sample_warning": ""
  }
}
```
