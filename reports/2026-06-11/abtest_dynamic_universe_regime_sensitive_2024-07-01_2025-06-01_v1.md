---
created: 2026-06-11 16:01:16 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: regime_sensitive
baseline_run_id: 178af1892514
variant_run_id: fc7d3c17086b
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
- baseline_run_id: `178af1892514`
- variant_run_id: `fc7d3c17086b`
- symbols: `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1INCHUSDT`, `1MBABYDOGEUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACHUSDT`, `ACTUSDT`, `ACXUSDT`, `ADAUSDT`, `AEVOUSDT`, `AGLDUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALGOUSDT`, `ALICEUSDT`, `ALPINEUSDT`, `ALTUSDT`, `AMPUSDT`, `ANIMEUSDT`, `ANKRUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARDRUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ASRUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AUDIOUSDT`, `AVAUSDT`, `AVAXUSDT`, `AXLUSDT`, `AXSUSDT`, `BABYUSDT`, `BANANAUSDT`, `BATUSDT`, `BBUSDT`, `BCHUSDT`, `BEAMXUSDT`, `BERAUSDT`, `BIOUSDT`, `BLURUSDT`, `BMTUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BTCUSDT`, `BTTCUSDT`, `C98USDT`, `CAKEUSDT`, `CATIUSDT`, `CELOUSDT`, `CETUSUSDT`, `CFXUSDT`, `CGPTUSDT`, `CHRUSDT`, `CHZUSDT`, `CKBUSDT`, `COMPUSDT`, `COOKIEUSDT`, `COSUSDT`, `COTIUSDT`, `COWUSDT`, `CRVUSDT`, `CTKUSDT`, `CTSIUSDT`, `CVCUSDT`, `CVXUSDT`, `DASHUSDT`, `DEXEUSDT`, `DGBUSDT`, `DIAUSDT`, `DODOUSDT`, `DOGEUSDT`, `DOGSUSDT`, `DOTUSDT`, `DUSDT`, `DYDXUSDT`, `DYMUSDT`, `EGLDUSDT`, `EIGENUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `FETUSDT`, `FIDAUSDT`, `FILUSDT`, `FLOKIUSDT`, `FLOWUSDT`, `FORMUSDT`, `FTTUSDT`, `GALAUSDT`, `GASUSDT`, `GLMRUSDT`, `GLMUSDT`, `GMTUSDT`, `GPSUSDT`, `GRTUSDT`, `GUNUSDT`, `GUSDT`, `HBARUSDT`, `HEIUSDT`, `HIGHUSDT`, `HIVEUSDT`, `HMSTRUSDT`, `HOTUSDT`, `HUMAUSDT`, `HYPERUSDT`, `ICPUSDT`, `IDUSDT`, `IMXUSDT`, `INITUSDT`, `INJUSDT`, `IOSTUSDT`, `IOTAUSDT`, `IOTXUSDT`, `IOUSDT`, `IQUSDT`, `JASMYUSDT`, `JSTUSDT`, `JTOUSDT`, `JUVUSDT`, `KAIAUSDT`, `KAITOUSDT`, `KAVAUSDT`, `KERNELUSDT`, `KSMUSDT`, `LAYERUSDT`, `LDOUSDT`, `LINKUSDT`, `LISTAUSDT`, `LPTUSDT`, `LQTYUSDT`, `LTCUSDT`, `LUMIAUSDT`, `LUNAUSDT`, `LUNCUSDT`, `MAGICUSDT`, `MANAUSDT`, `MANTAUSDT`, `MASKUSDT`, `MBOXUSDT`, `MEMEUSDT`, `METISUSDT`, `MEUSDT`, `MINAUSDT`, `MOVEUSDT`, `MOVRUSDT`, `MUBARAKUSDT`, `NEARUSDT`, `NEIROUSDT`, `NEOUSDT`, `NILUSDT`, `NMRUSDT`, `NOTUSDT`, `NXPCUSDT`, `OGNUSDT`, `OGUSDT`, `ONDOUSDT`, `ONEUSDT`, `ONTUSDT`, `OPUSDT`, `ORCAUSDT`, `ORDIUSDT`, `OSMOUSDT`, `PARTIUSDT`, `PENDLEUSDT`, `PENGUUSDT`, `PEOPLEUSDT`, `PEPEUSDT`, `PHAUSDT`, `PIXELUSDT`, `PNUTUSDT`, `POLUSDT`, `POLYXUSDT`, `PONDUSDT`, `PORTALUSDT`, `POWRUSDT`, `PROMUSDT`, `PSGUSDT`, `PUNDIXUSDT`, `PYRUSDT`, `PYTHUSDT`, `QKCUSDT`, `QNTUSDT`, `QTUMUSDT`, `RADUSDT`, `RAREUSDT`, `RAYUSDT`, `REDUSDT`, `RENDERUSDT`, `REZUSDT`, `RONINUSDT`, `ROSEUSDT`, `RPLUSDT`, `RSRUSDT`, `RUNEUSDT`, `RVNUSDT`, `SAGAUSDT`, `SANDUSDT`, `SANTOSUSDT`, `SCRTUSDT`, `SCRUSDT`, `SEIUSDT`, `SHELLUSDT`, `SHIBUSDT`, `SIGNUSDT`, `SKLUSDT`, `SLPUSDT`, `SNXUSDT`, `SOLUSDT`, `SOLVUSDT`, `SOPHUSDT`, `SPELLUSDT`, `SSVUSDT`, `STEEMUSDT`, `STGUSDT`, `STORJUSDT`, `STOUSDT`, `STRAXUSDT`, `STRKUSDT`, `STXUSDT`, `SUIUSDT`, `SUNUSDT`, `SUPERUSDT`, `SUSDT`, `SUSHIUSDT`, `SXTUSDT`, `SYNUSDT`, `TAOUSDT`, `TFUELUSDT`, `THETAUSDT`, `THEUSDT`, `TIAUSDT`, `TLMUSDT`, `TNSRUSDT`, `TONUSDT`, `TRBUSDT`, `TRUMPUSDT`, `TRXUSDT`, `TSTUSDT`, `TURBOUSDT`, `TUSDT`, `TUTUSDT`, `UNIUSDT`, `USUALUSDT`, `VANAUSDT`, `VANRYUSDT`, `VELODROMEUSDT`, `VETUSDT`, `VICUSDT`, `VIRTUALUSDT`, `VTHOUSDT`, `WAXPUSDT`, `WBTCUSDT`, `WCTUSDT`, `WIFUSDT`, `WINUSDT`, `WLDUSDT`, `WUSDT`, `XAIUSDT`, `XLMUSDT`, `XRPUSDT`, `XTZUSDT`, `XVGUSDT`, `YFIUSDT`, `YGGUSDT`, `ZECUSDT`, `ZENUSDT`, `ZILUSDT`, `ZKUSDT`, `ZROUSDT`, `ZRXUSDT`
- universe_mode: dynamic
- time_periods_tested: `2024-07-01` -> `2025-06-01`
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
- baseline_universe_refreshes: 336
- variant_universe_refreshes: 336

## 指标对比

| Metric | Baseline | Variant | Delta |
|---|---:|---:|---:|
| closed_trades | 70.00 | 52.00 | -18.00 |
| stop_rate | 77.14% | 73.08% | -4.07% |
| profit_factor | 0.74 | 0.91 | 0.17 |
| avg_r | -0.18 | -0.03 | 0.15 |
| max_drawdown_pct | 26.15% | 18.73% | -7.42% |
| net_return_pct | -14.32% | -5.60% | 8.72% |
| sharpe | -0.69 | -0.25 | 0.43 |
| first_trade_created_at | 2024-07-01T20:00:00+00:00 | 2024-07-01T20:00:00+00:00 | n/a |

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
    "trades": 268,
    "closed_trades": 52,
    "open_trades": 3,
    "win_rate": 26.923076923076923,
    "profit_factor": 0.9102519918991828,
    "avg_r": -0.03041598140660157,
    "net_return_pct": -5.595101316812123,
    "max_drawdown": 2171.251555639963,
    "max_drawdown_pct": 18.7312322084563,
    "intrabar_max_drawdown": 2134.564109515233,
    "intrabar_max_drawdown_pct": 18.52793703933711,
    "tp1_rate": 28.846153846153843,
    "tp2_rate": 26.923076923076923,
    "stop_rate": 73.07692307692307,
    "fee_drag": 63.15067881366979,
    "tail_max_loss": -117.19916034615537,
    "cagr": -6.080616162082375,
    "sharpe": -0.2520247085630767,
    "sortino": -0.2646537302546678,
    "exposure_pct": 84.32835820895522,
    "turnover": 5.402176692522704,
    "sample_sufficient": true,
    "sample_warning": ""
  }
}
```
