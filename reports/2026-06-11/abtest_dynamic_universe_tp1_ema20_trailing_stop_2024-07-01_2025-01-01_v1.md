---
created: 2026-06-11 10:15:32 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: tp1_ema20_trailing_stop
baseline_run_id: ec6edacdae47
variant_run_id: 7b1855f719a3
changed_param: analysis.tp1_ema_trailing_stop_enabled
old_value: False
new_value: True
sample_sufficient: true
universe_mode: dynamic
verdict: retest
report_version: v1
---

# A/B 实验报告 tp1_ema20_trailing_stop v1

- experiment_id: `tp1_ema20_trailing_stop`
- description: After TP1 hit, trail stop with 4h EMA20 instead of immediate breakeven.
- baseline_run_id: `ec6edacdae47`
- variant_run_id: `7b1855f719a3`
- symbols: `1000CATUSDT`, `1000SATSUSDT`, `1INCHUSDT`, `1MBABYDOGEUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACTUSDT`, `ACXUSDT`, `ADAUSDT`, `AEVOUSDT`, `AGLDUSDT`, `AIUSDT`, `ALGOUSDT`, `ALICEUSDT`, `ALTUSDT`, `AMPUSDT`, `ANKRUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARDRUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AVAUSDT`, `AVAXUSDT`, `AXLUSDT`, `AXSUSDT`, `BANANAUSDT`, `BATUSDT`, `BBUSDT`, `BCHUSDT`, `BEAMXUSDT`, `BLURUSDT`, `BNBUSDT`, `BOMEUSDT`, `BONKUSDT`, `BTCUSDT`, `BTTCUSDT`, `CAKEUSDT`, `CATIUSDT`, `CELOUSDT`, `CETUSUSDT`, `CFXUSDT`, `CHRUSDT`, `CHZUSDT`, `CKBUSDT`, `COMPUSDT`, `COSUSDT`, `COTIUSDT`, `COWUSDT`, `CRVUSDT`, `CTKUSDT`, `CTSIUSDT`, `CVCUSDT`, `CVXUSDT`, `DASHUSDT`, `DEXEUSDT`, `DGBUSDT`, `DIAUSDT`, `DODOUSDT`, `DOGEUSDT`, `DOGSUSDT`, `DOTUSDT`, `DYDXUSDT`, `DYMUSDT`, `EGLDUSDT`, `EIGENUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `FETUSDT`, `FIDAUSDT`, `FILUSDT`, `FLOKIUSDT`, `FLOWUSDT`, `FTTUSDT`, `GALAUSDT`, `GASUSDT`, `GLMRUSDT`, `GLMUSDT`, `GMTUSDT`, `GRTUSDT`, `GUSDT`, `HBARUSDT`, `HIGHUSDT`, `HIVEUSDT`, `HMSTRUSDT`, `HOTUSDT`, `ICPUSDT`, `IDUSDT`, `IMXUSDT`, `INJUSDT`, `IOTAUSDT`, `IOTXUSDT`, `IOUSDT`, `IQUSDT`, `JASMYUSDT`, `JSTUSDT`, `JTOUSDT`, `KAIAUSDT`, `KSMUSDT`, `LDOUSDT`, `LINKUSDT`, `LISTAUSDT`, `LPTUSDT`, `LQTYUSDT`, `LTCUSDT`, `LUMIAUSDT`, `LUNAUSDT`, `LUNCUSDT`, `MAGICUSDT`, `MANAUSDT`, `MANTAUSDT`, `MASKUSDT`, `MBOXUSDT`, `MEMEUSDT`, `METISUSDT`, `MEUSDT`, `MINAUSDT`, `MOVEUSDT`, `MOVRUSDT`, `NEARUSDT`, `NEIROUSDT`, `NEOUSDT`, `NOTUSDT`, `OGNUSDT`, `OGUSDT`, `ONEUSDT`, `OPUSDT`, `ORCAUSDT`, `ORDIUSDT`, `PENDLEUSDT`, `PENGUUSDT`, `PEOPLEUSDT`, `PEPEUSDT`, `PHAUSDT`, `PIXELUSDT`, `PNUTUSDT`, `POLUSDT`, `POLYXUSDT`, `PONDUSDT`, `POWRUSDT`, `PROMUSDT`, `PSGUSDT`, `PYRUSDT`, `PYTHUSDT`, `QKCUSDT`, `QNTUSDT`, `RADUSDT`, `RAREUSDT`, `RAYUSDT`, `RENDERUSDT`, `RONINUSDT`, `ROSEUSDT`, `RSRUSDT`, `RUNEUSDT`, `RVNUSDT`, `SAGAUSDT`, `SANDUSDT`, `SANTOSUSDT`, `SCRTUSDT`, `SCRUSDT`, `SEIUSDT`, `SHIBUSDT`, `SKLUSDT`, `SLPUSDT`, `SNXUSDT`, `SOLUSDT`, `SPELLUSDT`, `SSVUSDT`, `STEEMUSDT`, `STGUSDT`, `STORJUSDT`, `STRAXUSDT`, `STRKUSDT`, `STXUSDT`, `SUIUSDT`, `SUNUSDT`, `SUPERUSDT`, `SUSHIUSDT`, `SYNUSDT`, `TAOUSDT`, `THETAUSDT`, `THEUSDT`, `TIAUSDT`, `TLMUSDT`, `TNSRUSDT`, `TONUSDT`, `TRBUSDT`, `TRXUSDT`, `TURBOUSDT`, `TUSDT`, `UNIUSDT`, `USUALUSDT`, `VANAUSDT`, `VANRYUSDT`, `VELODROMEUSDT`, `VETUSDT`, `VTHOUSDT`, `WAXPUSDT`, `WBTCUSDT`, `WIFUSDT`, `WINUSDT`, `WLDUSDT`, `WUSDT`, `XAIUSDT`, `XLMUSDT`, `XRPUSDT`, `XTZUSDT`, `XVGUSDT`, `YFIUSDT`, `YGGUSDT`, `ZECUSDT`, `ZENUSDT`, `ZILUSDT`, `ZKUSDT`, `ZROUSDT`, `ZRXUSDT`
- universe_mode: dynamic
- time_periods_tested: `2024-07-01` -> `2025-01-01`
- changed_param: `analysis.tp1_ema_trailing_stop_enabled`
- old_value: `False`
- new_value: `True`
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
| closed_trades | 35.00 | 49.00 | 14.00 |
| stop_rate | 65.71% | 79.59% | 13.88% |
| profit_factor | 1.30 | 1.41 | 0.11 |
| avg_r | 0.24 | 0.27 | 0.03 |
| max_drawdown_pct | 10.67% | 10.54% | -0.13% |
| net_return_pct | 7.14% | 11.82% | 4.68% |
| sharpe | 0.78 | 1.20 | 0.42 |
| first_trade_created_at | 2024-07-01T20:00:00+00:00 | 2024-07-01T20:00:00+00:00 | n/a |

## 样本规则

- closed_trades < 20 时，默认 verdict 为 `retest`。
- 交易数下降超过 50% 时，标记 possible_over_filtering=true。
- 自动报告不会直接写 `keep`；采用默认策略前需要跨时段复测和人工复盘。

## 变更明细

| changed_param | old_value | new_value |
|---|---:|---:|
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
    "trades": 187,
    "closed_trades": 49,
    "open_trades": 1,
    "win_rate": 44.89795918367347,
    "profit_factor": 1.4149891020331626,
    "avg_r": 0.27069492185581046,
    "net_return_pct": 11.819734879999832,
    "max_drawdown": 1314.2337295588368,
    "max_drawdown_pct": 10.540172207842609,
    "intrabar_max_drawdown": 1236.0745727909143,
    "intrabar_max_drawdown_pct": 9.977526870173044,
    "tp1_rate": 42.857142857142854,
    "tp2_rate": 20.408163265306122,
    "stop_rate": 79.59183673469387,
    "fee_drag": 60.72060369496798,
    "tail_max_loss": -126.0206167075499,
    "cagr": 24.808985949617846,
    "sharpe": 1.1985507088119007,
    "sortino": 1.3169782647655341,
    "exposure_pct": 85.05434782608695,
    "turnover": 4.800345358799808,
    "sample_sufficient": true,
    "sample_warning": ""
  }
}
```
