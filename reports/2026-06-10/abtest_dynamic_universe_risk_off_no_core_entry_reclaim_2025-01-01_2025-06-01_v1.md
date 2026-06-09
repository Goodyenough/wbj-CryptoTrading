---
created: 2026-06-10 03:11:42 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: risk_off_no_core_entry_reclaim
baseline_run_id: e6133152fb7e
variant_run_id: c7be05461e78
changed_param: analysis.risk_off_core_buy_enabled, analysis.entry_reclaim_close_enabled
old_value: True, False
new_value: False, True
sample_sufficient: false
universe_mode: dynamic
verdict: retest
report_version: v1
---

# A/B 实验报告 risk_off_no_core_entry_reclaim v1

- experiment_id: `risk_off_no_core_entry_reclaim`
- description: Combine RISK_OFF core-buy pause with 4h entry reclaim confirmation.
- baseline_run_id: `e6133152fb7e`
- variant_run_id: `c7be05461e78`
- symbols: `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1MBABYDOGEUSDT`, `AAVEUSDT`, `ACHUSDT`, `ACTUSDT`, `ACXUSDT`, `ADAUSDT`, `AGLDUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALGOUSDT`, `ALPINEUSDT`, `AMPUSDT`, `ANIMEUSDT`, `ANKRUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARDRUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ASRUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AUDIOUSDT`, `AVAXUSDT`, `BABYUSDT`, `BANANAUSDT`, `BCHUSDT`, `BEAMXUSDT`, `BERAUSDT`, `BIOUSDT`, `BMTUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BTCUSDT`, `C98USDT`, `CAKEUSDT`, `CATIUSDT`, `CETUSUSDT`, `CFXUSDT`, `CGPTUSDT`, `CKBUSDT`, `COMPUSDT`, `COOKIEUSDT`, `COWUSDT`, `CRVUSDT`, `CVCUSDT`, `DEXEUSDT`, `DOGEUSDT`, `DOGSUSDT`, `DOTUSDT`, `DUSDT`, `DYMUSDT`, `EIGENUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `FETUSDT`, `FIDAUSDT`, `FILUSDT`, `FLOKIUSDT`, `FORMUSDT`, `FTTUSDT`, `GALAUSDT`, `GASUSDT`, `GLMUSDT`, `GMTUSDT`, `GPSUSDT`, `GRTUSDT`, `GUNUSDT`, `GUSDT`, `HBARUSDT`, `HEIUSDT`, `HIGHUSDT`, `HIVEUSDT`, `HUMAUSDT`, `HYPERUSDT`, `ICPUSDT`, `IDUSDT`, `IMXUSDT`, `INITUSDT`, `INJUSDT`, `IOSTUSDT`, `IOTAUSDT`, `IOUSDT`, `IQUSDT`, `JASMYUSDT`, `JSTUSDT`, `JTOUSDT`, `JUVUSDT`, `KAITOUSDT`, `KAVAUSDT`, `KERNELUSDT`, `LAYERUSDT`, `LDOUSDT`, `LINKUSDT`, `LISTAUSDT`, `LPTUSDT`, `LTCUSDT`, `LUNAUSDT`, `MAGICUSDT`, `MASKUSDT`, `MBOXUSDT`, `MEMEUSDT`, `MEUSDT`, `MOVEUSDT`, `MUBARAKUSDT`, `NEARUSDT`, `NEIROUSDT`, `NEOUSDT`, `NILUSDT`, `NMRUSDT`, `NOTUSDT`, `NXPCUSDT`, `OGUSDT`, `ONDOUSDT`, `ONTUSDT`, `OPUSDT`, `ORCAUSDT`, `ORDIUSDT`, `OSMOUSDT`, `PARTIUSDT`, `PENDLEUSDT`, `PENGUUSDT`, `PEOPLEUSDT`, `PEPEUSDT`, `PHAUSDT`, `PIXELUSDT`, `PNUTUSDT`, `POLUSDT`, `PORTALUSDT`, `PROMUSDT`, `PUNDIXUSDT`, `PYTHUSDT`, `QTUMUSDT`, `RAREUSDT`, `RAYUSDT`, `REDUSDT`, `RENDERUSDT`, `REZUSDT`, `RPLUSDT`, `RSRUSDT`, `RUNEUSDT`, `SAGAUSDT`, `SANDUSDT`, `SEIUSDT`, `SHELLUSDT`, `SHIBUSDT`, `SIGNUSDT`, `SKLUSDT`, `SOLUSDT`, `SOLVUSDT`, `SOPHUSDT`, `SPELLUSDT`, `STEEMUSDT`, `STGUSDT`, `STORJUSDT`, `STOUSDT`, `STRAXUSDT`, `STXUSDT`, `SUIUSDT`, `SUSDT`, `SUSHIUSDT`, `SXTUSDT`, `TAOUSDT`, `TFUELUSDT`, `THEUSDT`, `TIAUSDT`, `TONUSDT`, `TRBUSDT`, `TRUMPUSDT`, `TRXUSDT`, `TSTUSDT`, `TURBOUSDT`, `TUSDT`, `TUTUSDT`, `UNIUSDT`, `USUALUSDT`, `VANAUSDT`, `VETUSDT`, `VICUSDT`, `VIRTUALUSDT`, `VTHOUSDT`, `WBTCUSDT`, `WCTUSDT`, `WIFUSDT`, `WLDUSDT`, `WUSDT`, `XAIUSDT`, `XLMUSDT`, `XRPUSDT`, `XVGUSDT`, `ZENUSDT`, `ZROUSDT`
- universe_mode: dynamic
- time_periods_tested: `2025-01-01` -> `2025-06-01`
- changed_param: `analysis.risk_off_core_buy_enabled, analysis.entry_reclaim_close_enabled`
- old_value: `True, False`
- new_value: `False, True`
- sample_sufficient: false
- possible_over_filtering: false
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
| closed_trades | 17.00 | 15.00 | -2.00 |
| stop_rate | 88.24% | 86.67% | -1.57% |
| profit_factor | 0.33 | 0.41 | 0.09 |
| avg_r | -0.59 | -0.50 | 0.09 |
| max_drawdown_pct | 14.49% | 10.85% | -3.64% |
| net_return_pct | -11.80% | -8.17% | 3.63% |
| sharpe | -2.23 | -1.30 | 0.92 |
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

## Raw Metrics

```json
{
  "baseline": {
    "trades": 91,
    "closed_trades": 17,
    "open_trades": 3,
    "win_rate": 11.76470588235294,
    "profit_factor": 0.3267107639092419,
    "avg_r": -0.587579187250048,
    "net_return_pct": -11.797079538661093,
    "max_drawdown": 1491.3179874467587,
    "max_drawdown_pct": 14.48891516952118,
    "intrabar_max_drawdown": 1447.3663971714068,
    "intrabar_max_drawdown_pct": 14.166801655470952,
    "tp1_rate": 11.76470588235294,
    "tp2_rate": 11.76470588235294,
    "stop_rate": 88.23529411764706,
    "fee_drag": 21.27499693532945,
    "tail_max_loss": -104.26307084075773,
    "cagr": -26.17211747574988,
    "sharpe": -2.22676780806392,
    "sortino": -2.288121469885454,
    "exposure_pct": 81.56732891832229,
    "turnover": 1.8716336947181718,
    "sample_sufficient": false,
    "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
  },
  "variant": {
    "trades": 91,
    "closed_trades": 15,
    "open_trades": 1,
    "win_rate": 13.333333333333334,
    "profit_factor": 0.41286897495684083,
    "avg_r": -0.5001202170789691,
    "net_return_pct": -8.168417189682753,
    "max_drawdown": 1117.1414205881865,
    "max_drawdown_pct": 10.852894033469328,
    "intrabar_max_drawdown": 1023.9400768066625,
    "intrabar_max_drawdown_pct": 10.05176907608129,
    "tp1_rate": 20.0,
    "tp2_rate": 13.333333333333334,
    "stop_rate": 86.66666666666667,
    "fee_drag": 20.434937459527138,
    "tail_max_loss": -105.45388955456175,
    "cagr": -18.61511669669277,
    "sharpe": -1.3030347844364556,
    "sortino": -1.1076295689606377,
    "exposure_pct": 56.84326710816777,
    "turnover": 1.7585991029502606,
    "sample_sufficient": false,
    "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
  }
}
```
