---
created: 2026-07-26 11:42:41 CST
tags:
  - crypto
  - trading-system
  - abtest
experiment_id: relative_strength_soft_gate_btc_eth_minus_1_0
baseline_run_id: 8ecf90a9d098
variant_run_id: 35b200959728
changed_param: analysis.relative_strength_soft_gate_enabled, analysis.relative_strength_min_pct
old_value: False, -0.5
new_value: True, -1.0
sample_sufficient: true
universe_mode: dynamic
verdict: retest
report_version: v1
---

# A/B 实验报告 relative_strength_soft_gate_btc_eth_minus_1_0 v1

- experiment_id: `relative_strength_soft_gate_btc_eth_minus_1_0`
- description: Sensitivity test: soft gate BUY_CANDIDATE entries when 24h return underperforms the BTC/ETH average by more than 1.0 percentage point.
- baseline_run_id: `8ecf90a9d098`
- variant_run_id: `35b200959728`
- symbols: `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1INCHUSDT`, `1MBABYDOGEUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACHUSDT`, `ACTUSDT`, `ACXUSDT`, `ADAUSDT`, `AEVOUSDT`, `AGLDUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALGOUSDT`, `ALICEUSDT`, `ALPINEUSDT`, `ALTUSDT`, `AMPUSDT`, `ANIMEUSDT`, `ANKRUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARDRUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ASRUSDT`, `ASTRUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AUDIOUSDT`, `AVAUSDT`, `AVAXUSDT`, `AXLUSDT`, `AXSUSDT`, `BABYUSDT`, `BANANAUSDT`, `BATUSDT`, `BBUSDT`, `BCHUSDT`, `BEAMXUSDT`, `BERAUSDT`, `BIOUSDT`, `BLURUSDT`, `BMTUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BTCUSDT`, `BTTCUSDT`, `C98USDT`, `CAKEUSDT`, `CATIUSDT`, `CELOUSDT`, `CETUSUSDT`, `CFXUSDT`, `CGPTUSDT`, `CHRUSDT`, `CHZUSDT`, `CKBUSDT`, `COMPUSDT`, `COOKIEUSDT`, `COSUSDT`, `COTIUSDT`, `COWUSDT`, `CRVUSDT`, `CTKUSDT`, `CTSIUSDT`, `CVCUSDT`, `CVXUSDT`, `DASHUSDT`, `DEXEUSDT`, `DGBUSDT`, `DIAUSDT`, `DODOUSDT`, `DOGEUSDT`, `DOGSUSDT`, `DOTUSDT`, `DUSDT`, `DYDXUSDT`, `DYMUSDT`, `EGLDUSDT`, `EIGENUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `FETUSDT`, `FIDAUSDT`, `FILUSDT`, `FLOKIUSDT`, `FLOWUSDT`, `FORMUSDT`, `FTTUSDT`, `GALAUSDT`, `GASUSDT`, `GLMRUSDT`, `GLMUSDT`, `GMTUSDT`, `GPSUSDT`, `GRTUSDT`, `GUNUSDT`, `GUSDT`, `HAEDALUSDT`, `HBARUSDT`, `HEIUSDT`, `HIGHUSDT`, `HIVEUSDT`, `HMSTRUSDT`, `HOTUSDT`, `HUMAUSDT`, `HYPERUSDT`, `ICPUSDT`, `IDUSDT`, `IMXUSDT`, `INITUSDT`, `INJUSDT`, `IOSTUSDT`, `IOTAUSDT`, `IOTXUSDT`, `IOUSDT`, `IQUSDT`, `JASMYUSDT`, `JSTUSDT`, `JTOUSDT`, `JUVUSDT`, `KAIAUSDT`, `KAITOUSDT`, `KAVAUSDT`, `KERNELUSDT`, `KSMUSDT`, `LAYERUSDT`, `LDOUSDT`, `LINKUSDT`, `LISTAUSDT`, `LPTUSDT`, `LQTYUSDT`, `LTCUSDT`, `LUMIAUSDT`, `LUNAUSDT`, `LUNCUSDT`, `MAGICUSDT`, `MANAUSDT`, `MANTAUSDT`, `MASKUSDT`, `MBOXUSDT`, `MEMEUSDT`, `METISUSDT`, `MEUSDT`, `MINAUSDT`, `MOVEUSDT`, `MOVRUSDT`, `MUBARAKUSDT`, `NEARUSDT`, `NEIROUSDT`, `NEOUSDT`, `NILUSDT`, `NMRUSDT`, `NOTUSDT`, `NXPCUSDT`, `OGNUSDT`, `OGUSDT`, `ONDOUSDT`, `ONEUSDT`, `ONTUSDT`, `OPUSDT`, `ORCAUSDT`, `ORDIUSDT`, `OSMOUSDT`, `PARTIUSDT`, `PENDLEUSDT`, `PENGUUSDT`, `PEOPLEUSDT`, `PEPEUSDT`, `PHAUSDT`, `PIXELUSDT`, `PNUTUSDT`, `POLUSDT`, `POLYXUSDT`, `PONDUSDT`, `PORTALUSDT`, `POWRUSDT`, `PROMUSDT`, `PSGUSDT`, `PUNDIXUSDT`, `PYRUSDT`, `PYTHUSDT`, `QKCUSDT`, `QNTUSDT`, `QTUMUSDT`, `RADUSDT`, `RAREUSDT`, `RAYUSDT`, `REDUSDT`, `RENDERUSDT`, `REZUSDT`, `RONINUSDT`, `ROSEUSDT`, `RPLUSDT`, `RSRUSDT`, `RUNEUSDT`, `RVNUSDT`, `SAGAUSDT`, `SANDUSDT`, `SANTOSUSDT`, `SCRTUSDT`, `SCRUSDT`, `SEIUSDT`, `SHELLUSDT`, `SHIBUSDT`, `SIGNUSDT`, `SKLUSDT`, `SLPUSDT`, `SNXUSDT`, `SOLUSDT`, `SOLVUSDT`, `SOPHUSDT`, `SPELLUSDT`, `SSVUSDT`, `STEEMUSDT`, `STGUSDT`, `STORJUSDT`, `STOUSDT`, `STRAXUSDT`, `STRKUSDT`, `STXUSDT`, `SUIUSDT`, `SUNUSDT`, `SUPERUSDT`, `SUSDT`, `SUSHIUSDT`, `SXTUSDT`, `SYNUSDT`, `TAOUSDT`, `TFUELUSDT`, `THETAUSDT`, `THEUSDT`, `TIAUSDT`, `TLMUSDT`, `TNSRUSDT`, `TONUSDT`, `TRBUSDT`, `TRUMPUSDT`, `TRXUSDT`, `TSTUSDT`, `TURBOUSDT`, `TUSDT`, `TUTUSDT`, `UNIUSDT`, `USUALUSDT`, `VANAUSDT`, `VANRYUSDT`, `VELODROMEUSDT`, `VETUSDT`, `VICUSDT`, `VIRTUALUSDT`, `VTHOUSDT`, `WAXPUSDT`, `WBTCUSDT`, `WCTUSDT`, `WIFUSDT`, `WINUSDT`, `WLDUSDT`, `WUSDT`, `XAIUSDT`, `XLMUSDT`, `XRPUSDT`, `XTZUSDT`, `XVGUSDT`, `YFIUSDT`, `YGGUSDT`, `ZECUSDT`, `ZENUSDT`, `ZILUSDT`, `ZKUSDT`, `ZROUSDT`, `ZRXUSDT`
- universe_mode: dynamic
- time_periods_tested: `2024-07-01` -> `2025-06-01`
- changed_param: `analysis.relative_strength_soft_gate_enabled, analysis.relative_strength_min_pct`
- old_value: `False, -0.5`
- new_value: `True, -1.0`
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
| closed_trades | 76.00 | 79.00 | 3.00 |
| stop_rate | 89.47% | 87.34% | -2.13% |
| profit_factor | 0.95 | 1.04 | 0.09 |
| avg_r | -0.01 | 0.06 | 0.07 |
| max_drawdown_pct | 16.59% | 18.62% | 2.03% |
| net_return_pct | -2.09% | 2.99% | 5.08% |
| sharpe | -0.01 | 0.26 | 0.27 |
| first_trade_created_at | 2024-07-24T00:00:00+00:00 | 2024-07-24T00:00:00+00:00 | n/a |

## 样本规则

- closed_trades < 20 时，默认 verdict 为 `retest`。
- 交易数下降超过 50% 时，标记 possible_over_filtering=true。
- 自动报告不会直接写 `keep`；采用默认策略前需要跨时段复测和人工复盘。

## 变更明细

| changed_param | old_value | new_value |
|---|---:|---:|
| `analysis.relative_strength_soft_gate_enabled` | `False` | `True` |
| `analysis.relative_strength_min_pct` | `-0.5` | `-1.0` |

## Raw Metrics

```json
{
  "baseline": {
    "trades": 491,
    "closed_trades": 76,
    "open_trades": 2,
    "win_rate": 38.15789473684211,
    "profit_factor": 0.9497022392762177,
    "avg_r": -0.008733834521892258,
    "net_return_pct": -2.085381747848458,
    "max_drawdown": 1913.5674696124388,
    "max_drawdown_pct": 16.590752201409874,
    "intrabar_max_drawdown": 1898.8721286879845,
    "intrabar_max_drawdown_pct": 16.55447336667667,
    "tp1_rate": 38.15789473684211,
    "tp2_rate": 10.526315789473683,
    "stop_rate": 89.47368421052632,
    "fee_drag": 101.23230923887559,
    "tail_max_loss": -115.29716538521697,
    "cagr": -2.2699971791179663,
    "sharpe": -0.01397676540932231,
    "sortino": -0.014062573304631853,
    "exposure_pct": 58.05970149253732,
    "turnover": 7.729736834412474,
    "sample_sufficient": true,
    "sample_warning": ""
  },
  "variant": {
    "trades": 483,
    "closed_trades": 79,
    "open_trades": 1,
    "win_rate": 41.77215189873418,
    "profit_factor": 1.039748080127218,
    "avg_r": 0.06097564566538683,
    "net_return_pct": 2.993237000031268,
    "max_drawdown": 2323.262787017122,
    "max_drawdown_pct": 18.621186947708953,
    "intrabar_max_drawdown": 2235.8228329920294,
    "intrabar_max_drawdown_pct": 18.122159092245553,
    "tp1_rate": 37.9746835443038,
    "tp2_rate": 12.658227848101266,
    "stop_rate": 87.34177215189874,
    "fee_drag": 105.89867124979895,
    "tail_max_loss": -126.45687698629807,
    "cagr": 3.26561988587335,
    "sharpe": 0.2590689761777293,
    "sortino": 0.27716623587750855,
    "exposure_pct": 60.0,
    "turnover": 8.095881586251908,
    "sample_sufficient": true,
    "sample_warning": ""
  }
}
```
