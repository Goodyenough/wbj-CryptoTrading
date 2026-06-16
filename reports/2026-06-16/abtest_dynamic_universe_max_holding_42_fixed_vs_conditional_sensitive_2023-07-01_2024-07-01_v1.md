---
created: 2026-06-16 10:01:06 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: max_holding_42_fixed_vs_conditional_sensitive
baseline_run_id: 6228ab0da9d5
variant_run_id: 769b52c120b5
changed_param: backtest.max_holding_bars_conditional
old_value: False
new_value: True
sample_sufficient: true
universe_mode: dynamic
verdict: reject_candidate
report_version: v1
---

# A/B 实验报告 max_holding_42_fixed_vs_conditional_sensitive v1

- experiment_id: `max_holding_42_fixed_vs_conditional_sensitive`
- description: Direct fixed-vs-conditional 42-bar exit comparison under the same sensitive strategy. Both arms use 42 bars; only conditional gating changes.
- baseline_run_id: `6228ab0da9d5`
- variant_run_id: `769b52c120b5`
- symbols: `1000SATSUSDT`, `1INCHUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACHUSDT`, `ACMUSDT`, `ADAUSDT`, `ADXUSDT`, `AEVOUSDT`, `AGLDUSDT`, `AIUSDT`, `ALCXUSDT`, `ALGOUSDT`, `ALICEUSDT`, `ALTUSDT`, `AMPUSDT`, `ANKRUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ASRUSDT`, `ASTRUSDT`, `ATMUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AUDIOUSDT`, `AVAXUSDT`, `AXLUSDT`, `AXSUSDT`, `BANDUSDT`, `BBUSDT`, `BCHUSDT`, `BEAMXUSDT`, `BELUSDT`, `BICOUSDT`, `BLURUSDT`, `BNBUSDT`, `BNTUSDT`, `BOMEUSDT`, `BONKUSDT`, `BTCUSDT`, `BTTCUSDT`, `C98USDT`, `CAKEUSDT`, `CELOUSDT`, `CFXUSDT`, `CHRUSDT`, `CHZUSDT`, `CKBUSDT`, `COMPUSDT`, `COSUSDT`, `COTIUSDT`, `CRVUSDT`, `CTSIUSDT`, `CVCUSDT`, `CVXUSDT`, `CYBERUSDT`, `DCRUSDT`, `DEXEUSDT`, `DGBUSDT`, `DIAUSDT`, `DODOUSDT`, `DOGEUSDT`, `DOTUSDT`, `DUSKUSDT`, `DYDXUSDT`, `DYMUSDT`, `EDUUSDT`, `EGLDUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `FETUSDT`, `FIDAUSDT`, `FILUSDT`, `FLOKIUSDT`, `FLOWUSDT`, `FLUXUSDT`, `FTTUSDT`, `GALAUSDT`, `GASUSDT`, `GLMRUSDT`, `GLMUSDT`, `GMTUSDT`, `GMXUSDT`, `GRTUSDT`, `GTCUSDT`, `HBARUSDT`, `HIGHUSDT`, `HOTUSDT`, `ICPUSDT`, `ICXUSDT`, `IDUSDT`, `ILVUSDT`, `IMXUSDT`, `INJUSDT`, `IOSTUSDT`, `IOTAUSDT`, `IOTXUSDT`, `IOUSDT`, `IQUSDT`, `JASMYUSDT`, `JOEUSDT`, `JSTUSDT`, `JTOUSDT`, `KAVAUSDT`, `KNCUSDT`, `KSMUSDT`, `LDOUSDT`, `LINKUSDT`, `LISTAUSDT`, `LPTUSDT`, `LQTYUSDT`, `LSKUSDT`, `LTCUSDT`, `LUNAUSDT`, `LUNCUSDT`, `MAGICUSDT`, `MANAUSDT`, `MANTAUSDT`, `MASKUSDT`, `MAVUSDT`, `MBLUSDT`, `MBOXUSDT`, `MEMEUSDT`, `MINAUSDT`, `MOVRUSDT`, `MTLUSDT`, `NEARUSDT`, `NEOUSDT`, `NFPUSDT`, `NMRUSDT`, `NOTUSDT`, `OGNUSDT`, `OGUSDT`, `ONEUSDT`, `ONGUSDT`, `ONTUSDT`, `OPUSDT`, `ORDIUSDT`, `OSMOUSDT`, `PENDLEUSDT`, `PEOPLEUSDT`, `PEPEUSDT`, `PHAUSDT`, `PIXELUSDT`, `POLYXUSDT`, `PONDUSDT`, `PORTALUSDT`, `POWRUSDT`, `PROMUSDT`, `PUNDIXUSDT`, `PYRUSDT`, `PYTHUSDT`, `QIUSDT`, `QTUMUSDT`, `QUICKUSDT`, `RADUSDT`, `RAREUSDT`, `RAYUSDT`, `REQUSDT`, `REZUSDT`, `RIFUSDT`, `RLCUSDT`, `RONINUSDT`, `ROSEUSDT`, `RPLUSDT`, `RSRUSDT`, `RUNEUSDT`, `RVNUSDT`, `SAGAUSDT`, `SANDUSDT`, `SANTOSUSDT`, `SCUSDT`, `SEIUSDT`, `SFPUSDT`, `SHIBUSDT`, `SKLUSDT`, `SLPUSDT`, `SNXUSDT`, `SOLUSDT`, `SPELLUSDT`, `SSVUSDT`, `STEEMUSDT`, `STGUSDT`, `STORJUSDT`, `STRAXUSDT`, `STRKUSDT`, `STXUSDT`, `SUIUSDT`, `SUPERUSDT`, `SUSHIUSDT`, `SYNUSDT`, `TAOUSDT`, `TFUELUSDT`, `THETAUSDT`, `TIAUSDT`, `TKOUSDT`, `TLMUSDT`, `TNSRUSDT`, `TRBUSDT`, `TRXUSDT`, `TUSDT`, `TWTUSDT`, `UMAUSDT`, `UNIUSDT`, `VANRYUSDT`, `VETUSDT`, `VTHOUSDT`, `WAXPUSDT`, `WIFUSDT`, `WINUSDT`, `WLDUSDT`, `WOOUSDT`, `WUSDT`, `XAIUSDT`, `XECUSDT`, `XLMUSDT`, `XNOUSDT`, `XRPUSDT`, `XVGUSDT`, `XVSUSDT`, `YFIUSDT`, `YGGUSDT`, `ZENUSDT`, `ZILUSDT`, `ZKUSDT`, `ZROUSDT`, `ZRXUSDT`
- universe_mode: dynamic
- time_periods_tested: `2023-07-01` -> `2024-07-01`
- changed_param: `backtest.max_holding_bars_conditional`
- old_value: `False`
- new_value: `True`
- sample_sufficient: true
- possible_over_filtering: false
- verdict: `reject_candidate`
- reason: Variant return is worse and max drawdown did not improve.

## Dynamic Universe Metadata

- baseline_master_count: 418
- variant_master_count: 418
- baseline_source_limit: None
- variant_source_limit: None
- shared_master_expected: true (A/B runner builds the dynamic symbol master once before baseline and variant.)
- baseline_universe_refreshes: 367
- variant_universe_refreshes: 367

## 指标对比

| Metric | Baseline | Variant | Delta |
|---|---:|---:|---:|
| closed_trades | 207.00 | 197.00 | -10.00 |
| stop_rate | 47.34% | 48.22% | 0.88% |
| profit_factor | 1.32 | 1.20 | -0.12 |
| avg_r | 0.17 | 0.12 | -0.06 |
| max_drawdown_pct | 19.81% | 20.69% | 0.89% |
| net_return_pct | 38.96% | 22.26% | -16.70% |
| sharpe | 1.40 | 0.89 | -0.50 |
| first_trade_created_at | 2023-07-01T04:00:00+00:00 | 2023-07-01T04:00:00+00:00 | n/a |

## 样本规则

- closed_trades < 20 时，默认 verdict 为 `retest`。
- 交易数下降超过 50% 时，标记 possible_over_filtering=true。
- 自动报告不会直接写 `keep`；采用默认策略前需要跨时段复测和人工复盘。

## 变更明细

| changed_param | old_value | new_value |
|---|---:|---:|
| `backtest.max_holding_bars_conditional` | `False` | `True` |

## Raw Metrics

```json
{
  "baseline": {
    "trades": 727,
    "closed_trades": 207,
    "open_trades": 0,
    "win_rate": 49.75845410628019,
    "profit_factor": 1.3226238318124162,
    "avg_r": 0.173378749223807,
    "net_return_pct": 38.9637111543071,
    "max_drawdown": 3432.2252335663325,
    "max_drawdown_pct": 19.80671235246925,
    "intrabar_max_drawdown": 3278.18757137837,
    "intrabar_max_drawdown_pct": 19.0874632132247,
    "tp1_rate": 26.08695652173913,
    "tp2_rate": 14.009661835748794,
    "stop_rate": 47.34299516908212,
    "fee_drag": 397.17951150617455,
    "tail_max_loss": -176.55376277979857,
    "cagr": 38.8388356381093,
    "sharpe": 1.3987912389492103,
    "sortino": 1.430726751637586,
    "exposure_pct": 69.30783242258653,
    "turnover": 30.372830526738106,
    "sample_sufficient": true,
    "sample_warning": ""
  },
  "variant": {
    "trades": 729,
    "closed_trades": 197,
    "open_trades": 0,
    "win_rate": 45.68527918781726,
    "profit_factor": 1.203062549891844,
    "avg_r": 0.11714919375969644,
    "net_return_pct": 22.25911814307615,
    "max_drawdown": 3190.052374697427,
    "max_drawdown_pct": 20.693174527303537,
    "intrabar_max_drawdown": 3053.016515807154,
    "intrabar_max_drawdown_pct": 19.981876018029734,
    "tp1_rate": 26.39593908629442,
    "tp2_rate": 13.19796954314721,
    "stop_rate": 48.223350253807105,
    "fee_drag": 354.82513520548747,
    "tail_max_loss": -157.0667600324707,
    "cagr": 22.192003446269105,
    "sharpe": 0.8941036748042459,
    "sortino": 0.8762455897303603,
    "exposure_pct": 69.30783242258653,
    "turnover": 27.37121664496888,
    "sample_sufficient": true,
    "sample_warning": ""
  }
}
```
