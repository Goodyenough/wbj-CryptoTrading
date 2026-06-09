---
created: 2026-06-09 21:25:21 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: risk_off_no_core_top_n_3
baseline_run_id: e6133152fb7e
variant_run_id: 2ec5278f62cb
changed_param: analysis.risk_off_core_buy_enabled, market.top_n
old_value: True, 5
new_value: False, 3
sample_sufficient: false
universe_mode: dynamic
verdict: retest
report_version: v1
---

# A/B 实验报告 risk_off_no_core_top_n_3 v1

- experiment_id: `risk_off_no_core_top_n_3`
- description: Combine RISK_OFF core-buy pause with lower candidate capacity.
- baseline_run_id: `e6133152fb7e`
- variant_run_id: `2ec5278f62cb`
- symbols: `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1MBABYDOGEUSDT`, `AAVEUSDT`, `ACHUSDT`, `ACTUSDT`, `ACXUSDT`, `ADAUSDT`, `AGLDUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALGOUSDT`, `ALPINEUSDT`, `AMPUSDT`, `ANIMEUSDT`, `ANKRUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARDRUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ASRUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AUDIOUSDT`, `AVAXUSDT`, `BABYUSDT`, `BANANAUSDT`, `BCHUSDT`, `BEAMXUSDT`, `BERAUSDT`, `BIOUSDT`, `BMTUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BTCUSDT`, `C98USDT`, `CAKEUSDT`, `CATIUSDT`, `CETUSUSDT`, `CFXUSDT`, `CGPTUSDT`, `CKBUSDT`, `COMPUSDT`, `COOKIEUSDT`, `COWUSDT`, `CRVUSDT`, `CVCUSDT`, `DEXEUSDT`, `DOGEUSDT`, `DOGSUSDT`, `DOTUSDT`, `DUSDT`, `DYMUSDT`, `EIGENUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `FETUSDT`, `FIDAUSDT`, `FILUSDT`, `FLOKIUSDT`, `FORMUSDT`, `FTTUSDT`, `GALAUSDT`, `GASUSDT`, `GLMUSDT`, `GMTUSDT`, `GPSUSDT`, `GRTUSDT`, `GUNUSDT`, `GUSDT`, `HBARUSDT`, `HEIUSDT`, `HIGHUSDT`, `HIVEUSDT`, `HUMAUSDT`, `HYPERUSDT`, `ICPUSDT`, `IDUSDT`, `IMXUSDT`, `INITUSDT`, `INJUSDT`, `IOSTUSDT`, `IOTAUSDT`, `IOUSDT`, `IQUSDT`, `JASMYUSDT`, `JSTUSDT`, `JTOUSDT`, `JUVUSDT`, `KAITOUSDT`, `KAVAUSDT`, `KERNELUSDT`, `LAYERUSDT`, `LDOUSDT`, `LINKUSDT`, `LISTAUSDT`, `LPTUSDT`, `LTCUSDT`, `LUNAUSDT`, `MAGICUSDT`, `MASKUSDT`, `MBOXUSDT`, `MEMEUSDT`, `MEUSDT`, `MOVEUSDT`, `MUBARAKUSDT`, `NEARUSDT`, `NEIROUSDT`, `NEOUSDT`, `NILUSDT`, `NMRUSDT`, `NOTUSDT`, `NXPCUSDT`, `OGUSDT`, `ONDOUSDT`, `ONTUSDT`, `OPUSDT`, `ORCAUSDT`, `ORDIUSDT`, `OSMOUSDT`, `PARTIUSDT`, `PENDLEUSDT`, `PENGUUSDT`, `PEOPLEUSDT`, `PEPEUSDT`, `PHAUSDT`, `PIXELUSDT`, `PNUTUSDT`, `POLUSDT`, `PORTALUSDT`, `PROMUSDT`, `PUNDIXUSDT`, `PYTHUSDT`, `QTUMUSDT`, `RAREUSDT`, `RAYUSDT`, `REDUSDT`, `RENDERUSDT`, `REZUSDT`, `RPLUSDT`, `RSRUSDT`, `RUNEUSDT`, `SAGAUSDT`, `SANDUSDT`, `SEIUSDT`, `SHELLUSDT`, `SHIBUSDT`, `SIGNUSDT`, `SKLUSDT`, `SOLUSDT`, `SOLVUSDT`, `SOPHUSDT`, `SPELLUSDT`, `STEEMUSDT`, `STGUSDT`, `STORJUSDT`, `STOUSDT`, `STRAXUSDT`, `STXUSDT`, `SUIUSDT`, `SUSDT`, `SUSHIUSDT`, `SXTUSDT`, `TAOUSDT`, `TFUELUSDT`, `THEUSDT`, `TIAUSDT`, `TONUSDT`, `TRBUSDT`, `TRUMPUSDT`, `TRXUSDT`, `TSTUSDT`, `TURBOUSDT`, `TUSDT`, `TUTUSDT`, `UNIUSDT`, `USUALUSDT`, `VANAUSDT`, `VETUSDT`, `VICUSDT`, `VIRTUALUSDT`, `VTHOUSDT`, `WBTCUSDT`, `WCTUSDT`, `WIFUSDT`, `WLDUSDT`, `WUSDT`, `XAIUSDT`, `XLMUSDT`, `XRPUSDT`, `XVGUSDT`, `ZENUSDT`, `ZROUSDT`
- universe_mode: dynamic
- time_periods_tested: `2025-01-01` -> `2025-06-01`
- changed_param: `analysis.risk_off_core_buy_enabled, market.top_n`
- old_value: `True, 5`
- new_value: `False, 3`
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
| closed_trades | 17.00 | 13.00 | -4.00 |
| stop_rate | 88.24% | 84.62% | -3.62% |
| profit_factor | 0.33 | 0.49 | 0.16 |
| avg_r | -0.59 | -0.42 | 0.17 |
| max_drawdown_pct | 14.49% | 11.46% | -3.02% |
| net_return_pct | -11.80% | -8.03% | 3.77% |
| sharpe | -2.23 | -1.49 | 0.73 |
| first_trade_created_at | 2025-01-02T12:00:00+00:00 | 2025-01-03T00:00:00+00:00 | n/a |

## 样本规则

- closed_trades < 20 时，默认 verdict 为 `retest`。
- 交易数下降超过 50% 时，标记 possible_over_filtering=true。
- 自动报告不会直接写 `keep`；采用默认策略前需要跨时段复测和人工复盘。

## 变更明细

| changed_param | old_value | new_value |
|---|---:|---:|
| `analysis.risk_off_core_buy_enabled` | `True` | `False` |
| `market.top_n` | `5` | `3` |

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
    "trades": 89,
    "closed_trades": 13,
    "open_trades": 4,
    "win_rate": 15.384615384615385,
    "profit_factor": 0.48803471650381675,
    "avg_r": -0.4187143662741381,
    "net_return_pct": -8.028673472946924,
    "max_drawdown": 1186.1364678973623,
    "max_drawdown_pct": 11.464479508308784,
    "intrabar_max_drawdown": 1173.152013713605,
    "intrabar_max_drawdown_pct": 11.43215217011969,
    "tp1_rate": 15.384615384615385,
    "tp2_rate": 15.384615384615385,
    "stop_rate": 84.61538461538461,
    "fee_drag": 19.23898815172922,
    "tail_max_loss": -105.36993946372326,
    "cagr": -18.315429605295684,
    "sharpe": -1.4931620823513791,
    "sortino": -1.317748584344828,
    "exposure_pct": 57.17439293598234,
    "turnover": 2.0544783799587045,
    "sample_sufficient": false,
    "sample_warning": "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"
  }
}
```
