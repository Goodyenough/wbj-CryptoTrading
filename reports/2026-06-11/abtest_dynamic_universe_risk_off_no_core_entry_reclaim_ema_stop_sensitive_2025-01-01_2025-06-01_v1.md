---
created: 2026-06-11 16:46:51 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: risk_off_no_core_entry_reclaim_ema_stop_sensitive
baseline_run_id: 3b16409ab913
variant_run_id: 6ca838301cfb
changed_param: analysis.risk_off_core_buy_enabled, analysis.entry_reclaim_close_enabled, analysis.tp1_ema_trailing_stop_enabled, analysis.regime_btc_7d_drop_pct, analysis.regime_eth_7d_drop_pct, analysis.regime_require_both_trend
old_value: True, False, False, -5.0, -8.0, False
new_value: False, True, True, -3.0, -5.0, True
sample_sufficient: false
universe_mode: dynamic
verdict: retest
report_version: v1
---

# A/B 实验报告 risk_off_no_core_entry_reclaim_ema_stop_sensitive v1

- experiment_id: `risk_off_no_core_entry_reclaim_ema_stop_sensitive`
- description: Three-way combo (RISK_OFF core-buy pause + entry reclaim + TP1 EMA trailing stop) with tighter regime thresholds.
- baseline_run_id: `3b16409ab913`
- variant_run_id: `6ca838301cfb`
- symbols: `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1MBABYDOGEUSDT`, `AAVEUSDT`, `ACHUSDT`, `ACTUSDT`, `ACXUSDT`, `ADAUSDT`, `AGLDUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALGOUSDT`, `ALPINEUSDT`, `AMPUSDT`, `ANIMEUSDT`, `ANKRUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARDRUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ASRUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AUDIOUSDT`, `AVAXUSDT`, `BABYUSDT`, `BANANAUSDT`, `BCHUSDT`, `BEAMXUSDT`, `BERAUSDT`, `BIOUSDT`, `BMTUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BTCUSDT`, `C98USDT`, `CAKEUSDT`, `CATIUSDT`, `CETUSUSDT`, `CFXUSDT`, `CGPTUSDT`, `CKBUSDT`, `COMPUSDT`, `COOKIEUSDT`, `COWUSDT`, `CRVUSDT`, `CVCUSDT`, `DEXEUSDT`, `DOGEUSDT`, `DOGSUSDT`, `DOTUSDT`, `DUSDT`, `DYMUSDT`, `EIGENUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `FETUSDT`, `FIDAUSDT`, `FILUSDT`, `FLOKIUSDT`, `FORMUSDT`, `FTTUSDT`, `GALAUSDT`, `GASUSDT`, `GLMUSDT`, `GMTUSDT`, `GPSUSDT`, `GRTUSDT`, `GUNUSDT`, `GUSDT`, `HBARUSDT`, `HEIUSDT`, `HIGHUSDT`, `HIVEUSDT`, `HUMAUSDT`, `HYPERUSDT`, `ICPUSDT`, `IDUSDT`, `IMXUSDT`, `INITUSDT`, `INJUSDT`, `IOSTUSDT`, `IOTAUSDT`, `IOUSDT`, `IQUSDT`, `JASMYUSDT`, `JSTUSDT`, `JTOUSDT`, `JUVUSDT`, `KAITOUSDT`, `KAVAUSDT`, `KERNELUSDT`, `LAYERUSDT`, `LDOUSDT`, `LINKUSDT`, `LISTAUSDT`, `LPTUSDT`, `LTCUSDT`, `LUNAUSDT`, `MAGICUSDT`, `MASKUSDT`, `MBOXUSDT`, `MEMEUSDT`, `MEUSDT`, `MOVEUSDT`, `MUBARAKUSDT`, `NEARUSDT`, `NEIROUSDT`, `NEOUSDT`, `NILUSDT`, `NMRUSDT`, `NOTUSDT`, `NXPCUSDT`, `OGUSDT`, `ONDOUSDT`, `ONTUSDT`, `OPUSDT`, `ORCAUSDT`, `ORDIUSDT`, `OSMOUSDT`, `PARTIUSDT`, `PENDLEUSDT`, `PENGUUSDT`, `PEOPLEUSDT`, `PEPEUSDT`, `PHAUSDT`, `PIXELUSDT`, `PNUTUSDT`, `POLUSDT`, `PORTALUSDT`, `PROMUSDT`, `PUNDIXUSDT`, `PYTHUSDT`, `QTUMUSDT`, `RAREUSDT`, `RAYUSDT`, `REDUSDT`, `RENDERUSDT`, `REZUSDT`, `RPLUSDT`, `RSRUSDT`, `RUNEUSDT`, `SAGAUSDT`, `SANDUSDT`, `SEIUSDT`, `SHELLUSDT`, `SHIBUSDT`, `SIGNUSDT`, `SKLUSDT`, `SOLUSDT`, `SOLVUSDT`, `SOPHUSDT`, `SPELLUSDT`, `STEEMUSDT`, `STGUSDT`, `STORJUSDT`, `STOUSDT`, `STRAXUSDT`, `STXUSDT`, `SUIUSDT`, `SUSDT`, `SUSHIUSDT`, `SXTUSDT`, `TAOUSDT`, `TFUELUSDT`, `THEUSDT`, `TIAUSDT`, `TONUSDT`, `TRBUSDT`, `TRUMPUSDT`, `TRXUSDT`, `TSTUSDT`, `TURBOUSDT`, `TUSDT`, `TUTUSDT`, `UNIUSDT`, `USUALUSDT`, `VANAUSDT`, `VETUSDT`, `VICUSDT`, `VIRTUALUSDT`, `VTHOUSDT`, `WBTCUSDT`, `WCTUSDT`, `WIFUSDT`, `WLDUSDT`, `WUSDT`, `XAIUSDT`, `XLMUSDT`, `XRPUSDT`, `XVGUSDT`, `ZENUSDT`, `ZROUSDT`
- universe_mode: dynamic
- time_periods_tested: `2025-01-01` -> `2025-06-01`
- changed_param: `analysis.risk_off_core_buy_enabled, analysis.entry_reclaim_close_enabled, analysis.tp1_ema_trailing_stop_enabled, analysis.regime_btc_7d_drop_pct, analysis.regime_eth_7d_drop_pct, analysis.regime_require_both_trend`
- old_value: `True, False, False, -5.0, -8.0, False`
- new_value: `False, True, True, -3.0, -5.0, True`
- sample_sufficient: false
- possible_over_filtering: true
- verdict: `retest`
- reason: Variant closed_trades is below 20, so the sample is insufficient for a keep decision.

## Dynamic Universe Metadata

- baseline_master_count: 418
- variant_master_count: 418
- baseline_source_limit: None
- variant_source_limit: None
- shared_master_expected: true (A/B runner builds the dynamic symbol master once before baseline and variant.)
- baseline_universe_refreshes: 152
- variant_universe_refreshes: 152

## 指标对比

| Metric | Baseline | Variant | Delta |
|---|---:|---:|---:|
| closed_trades | 24.00 | 15.00 | -9.00 |
| stop_rate | 95.83% | 86.67% | -9.17% |
| profit_factor | 0.11 | 0.53 | 0.43 |
| avg_r | -0.86 | -0.36 | 0.51 |
| max_drawdown_pct | 22.25% | 10.02% | -12.23% |
| net_return_pct | -19.67% | -6.50% | 13.17% |
| sharpe | -2.86 | -1.08 | 1.78 |
| first_trade_created_at | 2025-01-02T12:00:00+00:00 | 2025-01-03T00:00:00+00:00 | n/a |

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
    "trades": 203,
    "closed_trades": 24,
    "open_trades": 4,
    "win_rate": 4.166666666666666,
    "profit_factor": 0.1082483991403431,
    "avg_r": -0.8619061785587236,
    "net_return_pct": -19.666624562573396,
    "max_drawdown": 2292.2600381542106,
    "max_drawdown_pct": 22.246649429258326,
    "intrabar_max_drawdown": 2252.835874551729,
    "intrabar_max_drawdown_pct": 22.028790659933982,
    "tp1_rate": 12.5,
    "tp2_rate": 4.166666666666666,
    "stop_rate": 95.83333333333334,
    "fee_drag": 26.530315911094494,
    "tail_max_loss": -104.26307084075773,
    "cagr": -41.10032680739369,
    "sharpe": -2.85978178454428,
    "sortino": -3.062929017490437,
    "exposure_pct": 81.56732891832229,
    "turnover": 2.245105379834868,
    "sample_sufficient": true,
    "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
  },
  "variant": {
    "trades": 92,
    "closed_trades": 15,
    "open_trades": 2,
    "win_rate": 20.0,
    "profit_factor": 0.5349977935487055,
    "avg_r": -0.35667071187155486,
    "net_return_pct": -6.495133198075942,
    "max_drawdown": 1031.1680844442435,
    "max_drawdown_pct": 10.017673452011712,
    "intrabar_max_drawdown": 969.5329182606492,
    "intrabar_max_drawdown_pct": 9.51766731936928,
    "tp1_rate": 20.0,
    "tp2_rate": 13.333333333333334,
    "stop_rate": 86.66666666666667,
    "fee_drag": 21.640515928918326,
    "tail_max_loss": -105.45388955456175,
    "cagr": -14.984145195659915,
    "sharpe": -1.0777393896301497,
    "sortino": -0.9211294493478516,
    "exposure_pct": 56.84326710816777,
    "turnover": 2.0083020031807743,
    "sample_sufficient": false,
    "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
  }
}
```
