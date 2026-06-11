---
created: 2026-06-11 16:42:28 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: risk_off_no_core_entry_reclaim_ema_stop_sensitive
baseline_run_id: 7736c33f706e
variant_run_id: 86b55752f079
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
- baseline_run_id: `7736c33f706e`
- variant_run_id: `86b55752f079`
- symbols: `1000CATUSDT`, `1000SATSUSDT`, `1INCHUSDT`, `1MBABYDOGEUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACTUSDT`, `ACXUSDT`, `ADAUSDT`, `AEVOUSDT`, `AGLDUSDT`, `AIUSDT`, `ALGOUSDT`, `ALICEUSDT`, `ALTUSDT`, `AMPUSDT`, `ANKRUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARDRUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AVAUSDT`, `AVAXUSDT`, `AXLUSDT`, `AXSUSDT`, `BANANAUSDT`, `BATUSDT`, `BBUSDT`, `BCHUSDT`, `BEAMXUSDT`, `BLURUSDT`, `BNBUSDT`, `BOMEUSDT`, `BONKUSDT`, `BTCUSDT`, `BTTCUSDT`, `CAKEUSDT`, `CATIUSDT`, `CELOUSDT`, `CETUSUSDT`, `CFXUSDT`, `CHRUSDT`, `CHZUSDT`, `CKBUSDT`, `COMPUSDT`, `COSUSDT`, `COTIUSDT`, `COWUSDT`, `CRVUSDT`, `CTKUSDT`, `CTSIUSDT`, `CVCUSDT`, `CVXUSDT`, `DASHUSDT`, `DEXEUSDT`, `DGBUSDT`, `DIAUSDT`, `DODOUSDT`, `DOGEUSDT`, `DOGSUSDT`, `DOTUSDT`, `DYDXUSDT`, `DYMUSDT`, `EGLDUSDT`, `EIGENUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `FETUSDT`, `FIDAUSDT`, `FILUSDT`, `FLOKIUSDT`, `FLOWUSDT`, `FTTUSDT`, `GALAUSDT`, `GASUSDT`, `GLMRUSDT`, `GLMUSDT`, `GMTUSDT`, `GRTUSDT`, `GUSDT`, `HBARUSDT`, `HIGHUSDT`, `HIVEUSDT`, `HMSTRUSDT`, `HOTUSDT`, `ICPUSDT`, `IDUSDT`, `IMXUSDT`, `INJUSDT`, `IOTAUSDT`, `IOTXUSDT`, `IOUSDT`, `IQUSDT`, `JASMYUSDT`, `JSTUSDT`, `JTOUSDT`, `KAIAUSDT`, `KSMUSDT`, `LDOUSDT`, `LINKUSDT`, `LISTAUSDT`, `LPTUSDT`, `LQTYUSDT`, `LTCUSDT`, `LUMIAUSDT`, `LUNAUSDT`, `LUNCUSDT`, `MAGICUSDT`, `MANAUSDT`, `MANTAUSDT`, `MASKUSDT`, `MBOXUSDT`, `MEMEUSDT`, `METISUSDT`, `MEUSDT`, `MINAUSDT`, `MOVEUSDT`, `MOVRUSDT`, `NEARUSDT`, `NEIROUSDT`, `NEOUSDT`, `NOTUSDT`, `OGNUSDT`, `OGUSDT`, `ONEUSDT`, `OPUSDT`, `ORCAUSDT`, `ORDIUSDT`, `PENDLEUSDT`, `PENGUUSDT`, `PEOPLEUSDT`, `PEPEUSDT`, `PHAUSDT`, `PIXELUSDT`, `PNUTUSDT`, `POLUSDT`, `POLYXUSDT`, `PONDUSDT`, `POWRUSDT`, `PROMUSDT`, `PSGUSDT`, `PYRUSDT`, `PYTHUSDT`, `QKCUSDT`, `QNTUSDT`, `RADUSDT`, `RAREUSDT`, `RAYUSDT`, `RENDERUSDT`, `RONINUSDT`, `ROSEUSDT`, `RSRUSDT`, `RUNEUSDT`, `RVNUSDT`, `SAGAUSDT`, `SANDUSDT`, `SANTOSUSDT`, `SCRTUSDT`, `SCRUSDT`, `SEIUSDT`, `SHIBUSDT`, `SKLUSDT`, `SLPUSDT`, `SNXUSDT`, `SOLUSDT`, `SPELLUSDT`, `SSVUSDT`, `STEEMUSDT`, `STGUSDT`, `STORJUSDT`, `STRAXUSDT`, `STRKUSDT`, `STXUSDT`, `SUIUSDT`, `SUNUSDT`, `SUPERUSDT`, `SUSHIUSDT`, `SYNUSDT`, `TAOUSDT`, `THETAUSDT`, `THEUSDT`, `TIAUSDT`, `TLMUSDT`, `TNSRUSDT`, `TONUSDT`, `TRBUSDT`, `TRXUSDT`, `TURBOUSDT`, `TUSDT`, `UNIUSDT`, `USUALUSDT`, `VANAUSDT`, `VANRYUSDT`, `VELODROMEUSDT`, `VETUSDT`, `VTHOUSDT`, `WAXPUSDT`, `WBTCUSDT`, `WIFUSDT`, `WINUSDT`, `WLDUSDT`, `WUSDT`, `XAIUSDT`, `XLMUSDT`, `XRPUSDT`, `XTZUSDT`, `XVGUSDT`, `YFIUSDT`, `YGGUSDT`, `ZECUSDT`, `ZENUSDT`, `ZILUSDT`, `ZKUSDT`, `ZROUSDT`, `ZRXUSDT`
- universe_mode: dynamic
- time_periods_tested: `2024-07-01` -> `2025-01-01`
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
- baseline_universe_refreshes: 185
- variant_universe_refreshes: 185

## 指标对比

| Metric | Baseline | Variant | Delta |
|---|---:|---:|---:|
| closed_trades | 50.00 | 34.00 | -16.00 |
| stop_rate | 70.00% | 70.59% | 0.59% |
| profit_factor | 1.07 | 2.52 | 1.45 |
| avg_r | 0.08 | 0.73 | 0.64 |
| max_drawdown_pct | 14.53% | 9.02% | -5.51% |
| net_return_pct | 2.41% | 25.38% | 22.97% |
| sharpe | 0.32 | 2.46 | 2.14 |
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
    "trades": 297,
    "closed_trades": 50,
    "open_trades": 3,
    "win_rate": 30.0,
    "profit_factor": 1.0693450197338363,
    "avg_r": 0.08272742338966738,
    "net_return_pct": 2.408481118996031,
    "max_drawdown": 1452.9732821897996,
    "max_drawdown_pct": 14.529732821897998,
    "intrabar_max_drawdown": 1511.1816811809767,
    "intrabar_max_drawdown_pct": 15.111816811809767,
    "tp1_rate": 34.0,
    "tp2_rate": 30.0,
    "stop_rate": 70.0,
    "fee_drag": 60.65128164357609,
    "tail_max_loss": -118.56341433539528,
    "cagr": 4.834283014534124,
    "sharpe": 0.31651595018808737,
    "sortino": 0.34891110209225623,
    "exposure_pct": 85.05434782608695,
    "turnover": 5.258161804964617,
    "sample_sufficient": true,
    "sample_warning": ""
  },
  "variant": {
    "trades": 182,
    "closed_trades": 34,
    "open_trades": 1,
    "win_rate": 58.82352941176471,
    "profit_factor": 2.518122629724807,
    "avg_r": 0.7268226580206464,
    "net_return_pct": 25.379917528724285,
    "max_drawdown": 1239.551295060588,
    "max_drawdown_pct": 9.016904140370727,
    "intrabar_max_drawdown": 1173.3176269008345,
    "intrabar_max_drawdown_pct": 8.577862148118585,
    "tp1_rate": 55.88235294117647,
    "tp2_rate": 29.411764705882355,
    "stop_rate": 70.58823529411765,
    "fee_drag": 55.94418362381133,
    "tail_max_loss": -140.4616040142896,
    "cagr": 56.622595443149095,
    "sharpe": 2.4605649932016815,
    "sortino": 2.428294592975882,
    "exposure_pct": 48.641304347826086,
    "turnover": 4.428385940431582,
    "sample_sufficient": true,
    "sample_warning": ""
  }
}
```
