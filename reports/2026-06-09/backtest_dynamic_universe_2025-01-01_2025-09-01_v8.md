---
created: 2026-06-09 18:47:56 CST
tags:
  - crypto
  - trading-system
  - backtest
backtest_run_id: 4dae110c062c
report_version: v8
sample_sufficient: true
universe_mode: true
universe_type: dynamic
---

# 回测报告 2025-01-01 至 2025-09-01 v8

- 回测 ID：`4dae110c062c`
- 交易对：`1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1INCHUSDT`, `AAVEUSDT`, `ACHUSDT`, `ACTUSDT`, `ACXUSDT`, `ADAUSDT`, `AGLDUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALGOUSDT`, `ALPINEUSDT`, `ALTUSDT`, `AMPUSDT`, `ANIMEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ASRUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AUSDT`, `AVAXUSDT`, `AXLUSDT`, `BABYUSDT`, `BANANAS31USDT`, `BCHUSDT`, `BERAUSDT`, `BIOUSDT`, `BMTUSDT`, `BNBUSDT`, `BOMEUSDT`, `BONKUSDT`, `BTCUSDT`, `CAKEUSDT`, `CETUSUSDT`, `CFXUSDT`, `CGPTUSDT`, `CKBUSDT`, `COMPUSDT`, `COOKIEUSDT`, `COWUSDT`, `CRVUSDT`, `CTSIUSDT`, `CUSDT`, `CVCUSDT`, `CYBERUSDT`, `DIAUSDT`, `DOGEUSDT`, `DOLOUSDT`, `DOTUSDT`, `DUSDT`, `EIGENUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSUSDT`, `EPICUSDT`, `ERAUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `FETUSDT`, `FIDAUSDT`, `FILUSDT`, `FLOKIUSDT`, `FORMUSDT`, `GALAUSDT`, `GASUSDT`, `GLMUSDT`, `GMTUSDT`, `GMXUSDT`, `GPSUSDT`, `GUNUSDT`, `GUSDT`, `HAEDALUSDT`, `HBARUSDT`, `HFTUSDT`, `HIGHUSDT`, `HIVEUSDT`, `HUMAUSDT`, `HYPERUSDT`, `ICPUSDT`, `ILVUSDT`, `INITUSDT`, `INJUSDT`, `IOTAUSDT`, `IOUSDT`, `IQUSDT`, `JASMYUSDT`, `JSTUSDT`, `JTOUSDT`, `JUVUSDT`, `KAIAUSDT`, `KAITOUSDT`, `KERNELUSDT`, `KNCUSDT`, `LAUSDT`, `LAYERUSDT`, `LDOUSDT`, `LINKUSDT`, `LISTAUSDT`, `LPTUSDT`, `LTCUSDT`, `MAGICUSDT`, `MASKUSDT`, `MAVUSDT`, `MEMEUSDT`, `MEUSDT`, `MITOUSDT`, `MOVEUSDT`, `MUBARAKUSDT`, `NEARUSDT`, `NEIROUSDT`, `NEWTUSDT`, `NILUSDT`, `NMRUSDT`, `NOTUSDT`, `NXPCUSDT`, `ONDOUSDT`, `ONTUSDT`, `OPUSDT`, `ORCAUSDT`, `PARTIUSDT`, `PENDLEUSDT`, `PENGUUSDT`, `PEOPLEUSDT`, `PEPEUSDT`, `PHAUSDT`, `PLUMEUSDT`, `PNUTUSDT`, `POLUSDT`, `PONDUSDT`, `PORTALUSDT`, `PROMUSDT`, `PROVEUSDT`, `PUNDIXUSDT`, `PYTHUSDT`, `QTUMUSDT`, `RADUSDT`, `RAREUSDT`, `RAYUSDT`, `REDUSDT`, `RENDERUSDT`, `RESOLVUSDT`, `REZUSDT`, `RSRUSDT`, `RUNEUSDT`, `RVNUSDT`, `SAGAUSDT`, `SAHARAUSDT`, `SANDUSDT`, `SEIUSDT`, `SHELLUSDT`, `SHIBUSDT`, `SIGNUSDT`, `SKLUSDT`, `SLPUSDT`, `SOLUSDT`, `SOLVUSDT`, `SOPHUSDT`, `SPELLUSDT`, `SPKUSDT`, `STEEMUSDT`, `STGUSDT`, `STOUSDT`, `SUIUSDT`, `SUSDT`, `SUSHIUSDT`, `SXTUSDT`, `TAOUSDT`, `THEUSDT`, `TIAUSDT`, `TONUSDT`, `TOWNSUSDT`, `TRBUSDT`, `TREEUSDT`, `TRUMPUSDT`, `TRXUSDT`, `TSTUSDT`, `TURBOUSDT`, `TUSDT`, `TUTUSDT`, `UMAUSDT`, `UNIUSDT`, `USUALUSDT`, `VANAUSDT`, `VETUSDT`, `VICUSDT`, `VIRTUALUSDT`, `VTHOUSDT`, `WBTCUSDT`, `WCTUSDT`, `WIFUSDT`, `WLDUSDT`, `WUSDT`, `XAIUSDT`, `XLMUSDT`, `XRPUSDT`, `XTZUSDT`, `ZENUSDT`, `ZROUSDT`
- UTC 区间：2025-01-01T00:00:00+00:00 -> 2025-09-01T00:00:00+00:00
- 初始权益：10,000.00 USDT
- 最终权益：9,040.22 USDT
- 净收益：-9.60%
- 代码 commit：`487bb3124157fa2d8023c75b3f7d062cc9729849`
- 样本是否充分：true
- 样本提示：样本数量未触发警告。
- Universe mode：dynamic

## 回测假设

- 决策在 4h bar 收盘后做，新 WATCHING 条件计划最早从下一根 bar 成交。
- WATCHING 是条件计划，不是真实提交交易所的限价单；不预留现金，成交时检查现金、名义仓位和活跃风险。
- intrabar 默认 stop_first；同 bar 同时触发止损和止盈时按止损优先。
- 入场成交价取 entry_high + 滑点；TP1 是 TP1 touched，不减仓，不代表已兑现利润。
- 使用固定 stop/TP，不实现动态支撑退出；4h K 线裁决成交，未使用 5m/15m 还原真实路径。
- 24h ticker 字段由 1h K 线重建，与实时 Binance /ticker/24hr 存在粒度差异。
- 未处理 tick size、step size、min notional、历史费率变化、BNB 折扣和 VIP 费率。
- 只覆盖本次手动输入、快照选中或动态 universe 选中且可获取历史数据的 symbols，不代表完整历史市场 universe。

## Dynamic Universe / 历史动态 Universe

- Source / 来源：Binance current exchangeInfo tradable USDT spot symbols
- Master symbols / Master 币种数：418
- Source limit / 调试截断：None
- Source limit applied / 是否截断：false
- Refresh frequency / 刷新频率：daily
- Universe refreshes / Universe 刷新次数：244
- Selected symbols per refresh / 每次入选数量：min=7, avg=22.80, max=40
- Top selected symbols / 最常入选：`BTCUSDT`(244), `ETHUSDT`(244), `SOLUSDT`(244), `SUIUSDT`(243), `XRPUSDT`(243), `PEPEUSDT`(242), `DOGEUSDT`(241), `BNBUSDT`(239), `TRXUSDT`(231), `ADAUSDT`(221)
- Filter counts / 过滤统计：
```json
{
  "missing_1h": 21197,
  "insufficient_24h": 63,
  "reconstruct_error": 0,
  "low_quote_volume": 75003,
  "low_trades": 7,
  "stable_like": 0
}
```
> Warning / 警告：dynamic universe 的 symbol master 来自当前 Binance exchangeInfo；历史上曾交易但今天已退市的币不会进入 master list，因此仍有退市幸存者偏差。
> Runtime / 耗时提示：第一次完整运行需要缓存大量 1h/4h/1d K 线，可能很慢；缓存命中后后续回测会明显加快。

## 核心指标

| Metric（指标） | Value（数值） |
|---|---:|
| Trades（计划总数） | 242 |
| Closed trades（已结束交易） | 41 |
| Open trades（仍开放持仓） | 3 |
| Win rate（胜率） | 21.95% |
| Profit factor（盈利因子） | 0.69 |
| Avg R（平均R倍数） | -0.22 |
| Net return（净收益率） | -9.60% |
| Max drawdown（最大回撤） | 1,935.71 / 18.81% |
| Intrabar max drawdown（K线内最大回撤） | 1,895.26 / 18.55% |
| TP1 touched rate（第一止盈触达率） | 36.59% |
| TP2 close rate（第二止盈平仓率） | 21.95% |
| Stop rate（止损率） | 78.05% |
| Fee drag（手续费拖累） | 53.44 USDT |
| Tail max single loss（最大单笔亏损） | -104.26 USDT |
| CAGR（年化复合收益率） | -14.06% |
| Sharpe（夏普比率） | -0.73 |
| Sortino（索提诺比率） | -0.85 |
| Exposure（持仓暴露时间） | 88.55% |
| Turnover（换手率） | 4.70 |
| Sample sufficient（样本是否充分） | true |

## 术语速查

- PnL（Profit and Loss，盈亏）：交易赚了或亏了多少钱。
- Gross PnL（毛盈亏）：未扣手续费和滑点前的盈亏。
- Net PnL（净盈亏）：扣除手续费和滑点后的真实模拟盈亏。
- R / Net R（风险倍数）：以单笔预设亏损风险为单位衡量结果，-1R 约等于亏掉一笔计划风险。
- Drawdown（回撤）：账户从阶段高点跌到低点的幅度，用来衡量过程中的最大压力。
- Profit factor（盈利因子）：总盈利除以总亏损，大于 1 才说明已闭合交易整体赚钱。
- Sharpe（夏普比率）：单位波动获得的收益，样本少时容易失真。
- Sortino（索提诺比率）：只惩罚下行波动的风险收益指标，样本少时也要谨慎看。
- Exposure（持仓暴露时间）：回测期间有仓位在市场里的时间比例。
- Turnover（换手率）：交易名义金额相对初始资金的规模。

## Benchmark

| Benchmark（基准） | Return（收益率） |
|---|---:|
| BTC buy-hold（买入并持有BTC） | 15.24% |
| ETH buy-hold（买入并持有ETH） | 30.77% |
| Cash（现金不交易） | 0.00% |
| Equal-weight symbols（等权持有本次币种） | -40.24% |

## 已结束交易

| Symbol（交易对） | Status（状态） | Created（创建时间） | Entry（入场价） | Exit（出场价） | Qty（数量） | Gross PnL（毛盈亏） | Net PnL（净盈亏） | Net R（净R倍数） | Fees（手续费） | Notes（备注） |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| `ETHUSDT` | STOPPED（已止损） | 2025-01-02T12:00:00+00:00 | 3,483.33 | 3,252.17 | 0.44 | -102.21 | -104.26 | -1.03 | 2.05 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-01-02T12:00:00+00:00 | 97,071.70 | 90,067.34 | 0.01 | -101.92 | -103.80 | -1.03 | 1.88 | Stop loss hit. |
| `WLDUSDT` | STOPPED（已止损） | 2025-01-04T00:00:00+00:00 | 2.42 | 2.05 | 271.01 | -101.54 | -102.36 | -1.01 | 0.82 | Stop loss hit. |
| `LINKUSDT` | STOPPED（已止损） | 2025-01-04T04:00:00+00:00 | 23.17 | 19.36 | 26.55 | -101.42 | -102.18 | -1.01 | 0.76 | Stop loss hit. |
| `HBARUSDT` | STOPPED（已止损） | 2025-01-04T08:00:00+00:00 | 0.31 | 0.26 | 2,186.42 | -101.82 | -102.66 | -1.01 | 0.84 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-01-14T20:00:00+00:00 | 96,875.83 | 87,829.92 | 0.01 | -96.30 | -97.65 | -1.02 | 1.35 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-01-16T08:00:00+00:00 | 3,396.15 | 2,873.32 | 0.18 | -96.13 | -96.91 | -1.01 | 0.78 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-02-20T08:00:00+00:00 | 2,739.78 | 2,563.79 | 0.55 | -96.06 | -98.06 | -1.04 | 2.00 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-03-06T08:00:00+00:00 | 90,332.96 | 80,197.22 | 0.01 | -93.07 | -94.14 | -1.02 | 1.07 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-03-20T00:00:00+00:00 | 86,570.94 | 79,837.72 | 0.01 | -92.68 | -94.25 | -1.03 | 1.58 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-03-20T04:00:00+00:00 | 1,991.87 | 1,842.38 | 0.62 | -92.59 | -94.22 | -1.03 | 1.63 | Stop loss hit. |
| `BTCUSDT` | CLOSED（已按TP2平仓） | 2025-04-12T08:00:00+00:00 | 83,637.41 | 108,712.75 | 0.01 | 248.92 | 248.16 | 2.77 | 0.76 | TP2 hit; paper trade closed. |
| `ETHUSDT` | CLOSED（已按TP2平仓） | 2025-04-25T20:00:00+00:00 | 1,781.57 | 2,078.51 | 0.79 | 234.02 | 232.80 | 2.56 | 1.22 | TP2 hit; paper trade closed. |
| `TRXUSDT` | CLOSED（已按TP2平仓） | 2025-05-11T00:00:00+00:00 | 0.26 | 0.30 | 5,829.69 | 252.65 | 251.33 | 2.67 | 1.32 | TP2 hit; paper trade closed. |
| `SUIUSDT` | STOPPED（已止损） | 2025-05-11T04:00:00+00:00 | 3.98 | 3.52 | 201.56 | -94.49 | -95.52 | -1.02 | 1.03 | Stop loss hit. |
| `XRPUSDT` | STOPPED（已止损） | 2025-05-11T04:00:00+00:00 | 2.38 | 2.13 | 385.09 | -94.61 | -95.80 | -1.02 | 1.19 | Stop loss hit. |
| `ACTUSDT` | STOPPED（已止损） | 2025-05-11T04:00:00+00:00 | 0.06 | 0.05 | 8,656.48 | -93.92 | -94.58 | -1.01 | 0.66 | Stop loss hit. |
| `NEIROUSDT` | STOPPED（已止损） | 2025-05-19T12:00:00+00:00 | 0.00 | 0.00 | 582,466.17 | -95.11 | -95.47 | -1.01 | 0.37 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-05-29T08:00:00+00:00 | 2,683.68 | 2,469.35 | 0.43 | -92.83 | -94.36 | -1.03 | 1.53 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-06-02T16:00:00+00:00 | 2,553.30 | 2,429.10 | 0.74 | -92.28 | -94.84 | -1.05 | 2.56 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-06-06T16:00:00+00:00 | 105,460.26 | 98,767.81 | 0.01 | -91.18 | -93.10 | -1.04 | 1.92 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-06-08T12:00:00+00:00 | 2,522.31 | 2,343.42 | 0.51 | -91.52 | -93.24 | -1.03 | 1.72 | Stop loss hit. |
| `XRPUSDT` | STOPPED（已止损） | 2025-06-10T00:00:00+00:00 | 2.27 | 2.11 | 591.93 | -93.81 | -95.60 | -1.03 | 1.79 | Stop loss hit. |
| `AVAXUSDT` | STOPPED（已止损） | 2025-06-10T00:00:00+00:00 | 21.79 | 19.25 | 36.34 | -92.21 | -93.23 | -1.02 | 1.02 | Stop loss hit. |
| `BNBUSDT` | STOPPED（已止损） | 2025-06-10T12:00:00+00:00 | 660.52 | 636.16 | 3.72 | -90.69 | -94.04 | -1.06 | 3.35 | Stop loss hit. |
| `ETHUSDT` | CLOSED（已按TP2平仓） | 2025-06-29T08:00:00+00:00 | 2,449.05 | 2,734.86 | 0.84 | 239.40 | 237.66 | 2.77 | 1.74 | TP2 hit; paper trade closed. |
| `SUIUSDT` | CLOSED（已按TP2平仓） | 2025-06-30T00:00:00+00:00 | 2.91 | 3.97 | 232.24 | 245.76 | 245.12 | 2.87 | 0.64 | TP2 hit; paper trade closed. |
| `WIFUSDT` | CLOSED（已按TP2平仓） | 2025-07-07T00:00:00+00:00 | 0.88 | 1.08 | 1,121.21 | 225.46 | 224.58 | 2.52 | 0.88 | TP2 hit; paper trade closed. |
| `BONKUSDT` | CLOSED（已按TP2平仓） | 2025-07-08T20:00:00+00:00 | 0.00 | 0.00 | 19,967,749.79 | 240.46 | 240.01 | 2.67 | 0.45 | TP2 hit; paper trade closed. |
| `AAVEUSDT` | STOPPED（已止损） | 2025-07-10T04:00:00+00:00 | 296.13 | 273.05 | 4.06 | -93.71 | -95.31 | -1.03 | 1.59 | Stop loss hit. |
| `SEIUSDT` | STOPPED（已止损） | 2025-07-13T16:00:00+00:00 | 0.33 | 0.27 | 1,735.19 | -97.09 | -97.78 | -1.01 | 0.70 | Stop loss hit. |
| `DOGEUSDT` | CLOSED（已按TP2平仓） | 2025-07-13T16:00:00+00:00 | 0.20 | 0.26 | 4,305.79 | 251.07 | 250.28 | 2.58 | 0.79 | TP2 hit; paper trade closed. |
| `SUIUSDT` | STOPPED（已止损） | 2025-07-16T16:00:00+00:00 | 3.94 | 3.37 | 174.55 | -99.84 | -100.71 | -1.01 | 0.86 | Stop loss hit. |
| `PENGUUSDT` | CLOSED（已按TP2平仓） | 2025-07-19T08:00:00+00:00 | 0.03 | 0.04 | 27,617.06 | 237.31 | 236.51 | 2.33 | 0.80 | TP2 hit; paper trade closed. |
| `HBARUSDT` | STOPPED（已止损） | 2025-07-19T16:00:00+00:00 | 0.27 | 0.23 | 2,460.64 | -103.21 | -104.02 | -1.01 | 0.82 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-07-27T20:00:00+00:00 | 3,787.59 | 3,516.63 | 0.37 | -101.44 | -103.32 | -1.03 | 1.88 | Stop loss hit. |
| `CFXUSDT` | STOPPED（已止损） | 2025-07-30T00:00:00+00:00 | 0.21 | 0.18 | 3,365.63 | -98.30 | -99.18 | -1.02 | 0.88 | Stop loss hit. |
| `ENAUSDT` | STOPPED（已止损） | 2025-07-31T00:00:00+00:00 | 0.61 | 0.52 | 1,132.18 | -97.20 | -98.07 | -1.02 | 0.87 | Stop loss hit. |
| `LTCUSDT` | STOPPED（已止损） | 2025-08-08T00:00:00+00:00 | 121.19 | 113.35 | 12.63 | -99.03 | -101.08 | -1.04 | 2.04 | Stop loss hit. |
| `OPUSDT` | STOPPED（已止损） | 2025-08-14T08:00:00+00:00 | 0.83 | 0.71 | 837.66 | -98.32 | -99.19 | -1.01 | 0.87 | Stop loss hit. |
| `WIFUSDT` | STOPPED（已止损） | 2025-08-23T00:00:00+00:00 | 0.94 | 0.78 | 608.98 | -95.57 | -96.27 | -1.01 | 0.70 | Stop loss hit. |

## 回测结束仍开放

| Symbol（交易对） | Status（状态） | Entry（入场价） | Qty（数量） | Unrealized Handling（未实现盈亏处理） | Notes（备注） |
|---|---|---:|---:|---|---|
| `BTCUSDT` | TP1_HIT（第一止盈已触达） | 105,613.24 | 0.01 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |
| `TRXUSDT` | TP1_HIT（第一止盈已触达） | 0.34 | 7,699.03 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |
| `ETHUSDT` | ENTERED（已入场） | 4,691.33 | 0.17 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |

## 未入场/过期计划

| Symbol（交易对） | Status（状态） | Created（创建时间） | Entry Zone（入场区间） | Score（评分） | Notes（备注） |
|---|---|---|---:|---:|---|
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-01-04T00:00:00+00:00 | 708.65 - 712.23 | 63.55 | Backtest WATCHING plan expired before entry. |
| `PEPEUSDT` | EXPIRED（观察计划过期） | 2025-01-04T04:00:00+00:00 | 0.00 - 0.00 | 75.52 | Backtest WATCHING plan expired before entry. |
| `AAVEUSDT` | EXPIRED（观察计划过期） | 2025-01-04T04:00:00+00:00 | 333.84 - 340.27 | 68.79 | Backtest WATCHING plan expired before entry. |
| `TRXUSDT` | EXPIRED（观察计划过期） | 2025-01-04T04:00:00+00:00 | 0.26 - 0.27 | 59.14 | Backtest WATCHING plan expired before entry. |
| `XRPUSDT` | EXPIRED（观察计划过期） | 2025-01-04T08:00:00+00:00 | 2.37 - 2.41 | 74.40 | Backtest WATCHING plan expired before entry. |
| `LTCUSDT` | EXPIRED（观察计划过期） | 2025-01-04T08:00:00+00:00 | 107.79 - 109.22 | 68.81 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-01-04T12:00:00+00:00 | 40.15 - 40.76 | 72.48 | Backtest WATCHING plan expired before entry. |
| `DOTUSDT` | EXPIRED（观察计划过期） | 2025-01-04T12:00:00+00:00 | 7.45 - 7.57 | 72.30 | Backtest WATCHING plan expired before entry. |
| `UNIUSDT` | EXPIRED（观察计划过期） | 2025-01-04T12:00:00+00:00 | 14.45 - 14.67 | 68.26 | Backtest WATCHING plan expired before entry. |
| `XLMUSDT` | EXPIRED（观察计划过期） | 2025-01-05T00:00:00+00:00 | 0.44 - 0.45 | 72.26 | Backtest WATCHING plan expired before entry. |
| `DOGEUSDT` | INVALIDATED（未入场前失效） | 2025-01-07T04:00:00+00:00 | 0.38 - 0.39 | 73.22 | Plan invalidated before entry: current price is below stop loss. |
| `SANDUSDT` | INVALIDATED（未入场前失效） | 2025-01-07T08:00:00+00:00 | 0.67 - 0.68 | 80.12 | Plan invalidated before entry: current price is below stop loss. |
| `ADAUSDT` | INVALIDATED（未入场前失效） | 2025-01-07T08:00:00+00:00 | 1.08 - 1.09 | 74.60 | Plan invalidated before entry: current price is below stop loss. |
| `GALAUSDT` | INVALIDATED（未入场前失效） | 2025-01-07T08:00:00+00:00 | 0.04 - 0.04 | 70.23 | Plan invalidated before entry: current price is below stop loss. |
| `XRPUSDT` | INVALIDATED（未入场前失效） | 2025-01-07T12:00:00+00:00 | 2.41 - 2.43 | 66.76 | Plan invalidated before entry: current price is below stop loss. |
| `BNBUSDT` | INVALIDATED（未入场前失效） | 2025-01-07T12:00:00+00:00 | 720.61 - 725.08 | 65.66 | Plan invalidated before entry: current price is below stop loss. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-04-22T16:00:00+00:00 | 1,657.99 - 1,682.01 | 65.88 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-05-11T04:00:00+00:00 | 641.66 - 649.35 | 65.46 | Backtest WATCHING plan expired before entry. |
| `SOLUSDT` | EXPIRED（观察计划过期） | 2025-05-11T08:00:00+00:00 | 167.41 - 170.67 | 77.05 | Backtest WATCHING plan expired before entry. |
| `LINKUSDT` | EXPIRED（观察计划过期） | 2025-05-11T08:00:00+00:00 | 15.99 - 16.35 | 74.79 | Backtest WATCHING plan expired before entry. |
| `HBARUSDT` | EXPIRED（观察计划过期） | 2025-05-11T12:00:00+00:00 | 0.20 - 0.21 | 74.49 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-05-11T12:00:00+00:00 | 0.78 - 0.80 | 71.00 | Backtest WATCHING plan expired before entry. |
| `LTCUSDT` | EXPIRED（观察计划过期） | 2025-05-11T12:00:00+00:00 | 99.34 - 101.50 | 69.24 | Backtest WATCHING plan expired before entry. |
| `SHIBUSDT` | EXPIRED（观察计划过期） | 2025-05-11T16:00:00+00:00 | 0.00 - 0.00 | 79.55 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-05-11T16:00:00+00:00 | 23.58 - 24.13 | 77.80 | Backtest WATCHING plan expired before entry. |
| `DOGEUSDT` | EXPIRED（观察计划过期） | 2025-05-12T16:00:00+00:00 | 0.23 - 0.23 | 86.14 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-05-12T16:00:00+00:00 | 2,424.67 - 2,480.54 | 82.20 | Backtest WATCHING plan expired before entry. |
| `PEPEUSDT` | INVALIDATED（未入场前失效） | 2025-05-14T08:00:00+00:00 | 0.00 - 0.00 | 82.71 | Plan invalidated before entry: current price is below stop loss. |
| `SOLUSDT` | EXPIRED（观察计划过期） | 2025-05-14T12:00:00+00:00 | 175.96 - 179.61 | 79.17 | Backtest WATCHING plan expired before entry. |
| `LINKUSDT` | INVALIDATED（未入场前失效） | 2025-05-14T12:00:00+00:00 | 16.88 - 17.16 | 71.72 | Plan invalidated before entry: current price is below stop loss. |
| `ENAUSDT` | EXPIRED（观察计划过期） | 2025-05-14T16:00:00+00:00 | 0.41 - 0.41 | 72.07 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | INVALIDATED（未入场前失效） | 2025-05-14T16:00:00+00:00 | 0.00 - 0.00 | 70.42 | Plan invalidated before entry: current price is below stop loss. |
| `ADAUSDT` | INVALIDATED（未入场前失效） | 2025-05-14T16:00:00+00:00 | 0.78 - 0.80 | 48.83 | Plan invalidated before entry: current price is below stop loss. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-05-15T16:00:00+00:00 | 655.00 - 657.37 | 57.38 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | INVALIDATED（未入场前失效） | 2025-05-16T04:00:00+00:00 | 2,558.21 - 2,589.09 | 56.00 | Plan invalidated before entry: current price is below stop loss. |
| `LTCUSDT` | EXPIRED（观察计划过期） | 2025-05-16T04:00:00+00:00 | 100.45 - 101.20 | 49.28 | Backtest WATCHING plan expired before entry. |
| `DOGEUSDT` | EXPIRED（观察计划过期） | 2025-05-16T08:00:00+00:00 | 0.22 - 0.23 | 37.66 | Backtest WATCHING plan expired before entry. |
| `TAOUSDT` | INVALIDATED（未入场前失效） | 2025-05-16T08:00:00+00:00 | 435.87 - 443.83 | 37.35 | Plan invalidated before entry: current price is below stop loss. |
| `WIFUSDT` | INVALIDATED（未入场前失效） | 2025-05-16T12:00:00+00:00 | 1.05 - 1.06 | 62.36 | Plan invalidated before entry: current price is below stop loss. |
| `PEPEUSDT` | EXPIRED（观察计划过期） | 2025-05-18T08:00:00+00:00 | 0.00 - 0.00 | 56.08 | Backtest WATCHING plan expired before entry. |
| `WIFUSDT` | EXPIRED（观察计划过期） | 2025-05-18T08:00:00+00:00 | 0.97 - 0.99 | 48.66 | Backtest WATCHING plan expired before entry. |
| `SOLUSDT` | INVALIDATED（未入场前失效） | 2025-05-18T16:00:00+00:00 | 170.86 - 172.99 | 65.07 | Plan invalidated before entry: current price is below stop loss. |
| `ETHFIUSDT` | EXPIRED（观察计划过期） | 2025-05-19T00:00:00+00:00 | 1.32 - 1.36 | 64.63 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-05-19T20:00:00+00:00 | 2,490.90 - 2,526.38 | 63.32 | Backtest WATCHING plan expired before entry. |
| `DOGEUSDT` | EXPIRED（观察计划过期） | 2025-05-20T04:00:00+00:00 | 0.22 - 0.23 | 64.45 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-05-20T04:00:00+00:00 | 647.50 - 652.06 | 59.89 | Backtest WATCHING plan expired before entry. |
| `ENAUSDT` | EXPIRED（观察计划过期） | 2025-05-20T04:00:00+00:00 | 0.37 - 0.39 | 54.07 | Backtest WATCHING plan expired before entry. |
| `LTCUSDT` | EXPIRED（观察计划过期） | 2025-05-22T08:00:00+00:00 | 97.60 - 99.03 | 53.36 | Backtest WATCHING plan expired before entry. |
| `LINKUSDT` | EXPIRED（观察计划过期） | 2025-05-22T12:00:00+00:00 | 16.03 - 16.32 | 68.11 | Backtest WATCHING plan expired before entry. |
| `SOLUSDT` | EXPIRED（观察计划过期） | 2025-05-22T12:00:00+00:00 | 171.84 - 174.53 | 67.62 | Backtest WATCHING plan expired before entry. |
| `UNIUSDT` | EXPIRED（观察计划过期） | 2025-05-22T12:00:00+00:00 | 6.18 - 6.37 | 67.12 | Backtest WATCHING plan expired before entry. |
| `AAVEUSDT` | EXPIRED（观察计划过期） | 2025-05-22T12:00:00+00:00 | 250.49 - 255.71 | 61.35 | Backtest WATCHING plan expired before entry. |
| `PNUTUSDT` | INVALIDATED（未入场前失效） | 2025-05-22T20:00:00+00:00 | 0.35 - 0.36 | 63.84 | Plan invalidated before entry: current price is below stop loss. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-05-23T00:00:00+00:00 | 2,583.29 - 2,627.72 | 66.04 | Backtest WATCHING plan expired before entry. |
| `DOGEUSDT` | EXPIRED（观察计划过期） | 2025-05-23T08:00:00+00:00 | 0.24 - 0.24 | 70.51 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-05-23T08:00:00+00:00 | 0.78 - 0.80 | 62.94 | Backtest WATCHING plan expired before entry. |
| `PEPEUSDT` | EXPIRED（观察计划过期） | 2025-05-23T12:00:00+00:00 | 0.00 - 0.00 | 75.74 | Backtest WATCHING plan expired before entry. |
| `AAVEUSDT` | EXPIRED（观察计划过期） | 2025-05-26T00:00:00+00:00 | 262.41 - 268.18 | 67.85 | Backtest WATCHING plan expired before entry. |
| `BTCUSDT` | EXPIRED（观察计划过期） | 2025-05-26T00:00:00+00:00 | 108,507.12 - 109,215.13 | 59.20 | Backtest WATCHING plan expired before entry. |
| `WLDUSDT` | EXPIRED（观察计划过期） | 2025-05-26T00:00:00+00:00 | 1.39 - 1.43 | 57.01 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-05-26T00:00:00+00:00 | 669.24 - 671.45 | 55.44 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-05-26T04:00:00+00:00 | 2,552.13 - 2,567.98 | 60.57 | Backtest WATCHING plan expired before entry. |
| `WIFUSDT` | EXPIRED（观察计划过期） | 2025-05-26T04:00:00+00:00 | 1.11 - 1.14 | 53.45 | Backtest WATCHING plan expired before entry. |
| `SOLUSDT` | EXPIRED（观察计划过期） | 2025-05-26T04:00:00+00:00 | 175.18 - 177.37 | 52.46 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-05-26T12:00:00+00:00 | 0.76 - 0.77 | 51.23 | Backtest WATCHING plan expired before entry. |
| `DOGEUSDT` | EXPIRED（观察计划过期） | 2025-05-26T12:00:00+00:00 | 0.22 - 0.22 | 42.54 | Backtest WATCHING plan expired before entry. |
| `PEPEUSDT` | EXPIRED（观察计划过期） | 2025-05-26T16:00:00+00:00 | 0.00 - 0.00 | 65.75 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | INVALIDATED（未入场前失效） | 2025-05-29T04:00:00+00:00 | 682.33 - 685.73 | 61.22 | Plan invalidated before entry: current price is below stop loss. |
| `UNIUSDT` | INVALIDATED（未入场前失效） | 2025-05-29T16:00:00+00:00 | 6.74 - 6.81 | 68.39 | Plan invalidated before entry: current price is below stop loss. |
| `SOLUSDT` | EXPIRED（观察计划过期） | 2025-06-10T00:00:00+00:00 | 159.22 - 160.83 | 52.36 | Backtest WATCHING plan expired before entry. |
| `SUIUSDT` | EXPIRED（观察计划过期） | 2025-06-10T00:00:00+00:00 | 3.38 - 3.42 | 51.55 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-06-10T00:00:00+00:00 | 0.70 - 0.71 | 48.97 | Backtest WATCHING plan expired before entry. |
| `PEPEUSDT` | INVALIDATED（未入场前失效） | 2025-06-10T04:00:00+00:00 | 0.00 - 0.00 | 53.69 | Plan invalidated before entry: current price is below stop loss. |
| `ENAUSDT` | INVALIDATED（未入场前失效） | 2025-06-10T08:00:00+00:00 | 0.34 - 0.34 | 59.20 | Plan invalidated before entry: current price is below stop loss. |
| `DOGEUSDT` | INVALIDATED（未入场前失效） | 2025-06-11T00:00:00+00:00 | 0.20 - 0.20 | 54.27 | Plan invalidated before entry: current price is below stop loss. |
| `SEIUSDT` | EXPIRED（观察计划过期） | 2025-06-30T00:00:00+00:00 | 0.29 - 0.30 | 85.32 | Backtest WATCHING plan expired before entry. |
| `UNIUSDT` | INVALIDATED（未入场前失效） | 2025-06-30T04:00:00+00:00 | 7.11 - 7.20 | 73.42 | Plan invalidated before entry: current price is below stop loss. |
| `DOGEUSDT` | EXPIRED（观察计划过期） | 2025-06-30T04:00:00+00:00 | 0.16 - 0.17 | 52.96 | Backtest WATCHING plan expired before entry. |
| `XRPUSDT` | EXPIRED（观察计划过期） | 2025-06-30T08:00:00+00:00 | 2.18 - 2.19 | 64.22 | Backtest WATCHING plan expired before entry. |
| `SOLUSDT` | EXPIRED（观察计划过期） | 2025-06-30T08:00:00+00:00 | 148.74 - 150.23 | 56.87 | Backtest WATCHING plan expired before entry. |
| `ARBUSDT` | EXPIRED（观察计划过期） | 2025-06-30T16:00:00+00:00 | 0.33 - 0.34 | 69.82 | Backtest WATCHING plan expired before entry. |
| `PEPEUSDT` | EXPIRED（观察计划过期） | 2025-06-30T20:00:00+00:00 | 0.00 - 0.00 | 61.28 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-01T00:00:00+00:00 | 652.84 - 653.99 | 57.15 | Backtest WATCHING plan expired before entry. |
| `UNIUSDT` | EXPIRED（观察计划过期） | 2025-07-03T00:00:00+00:00 | 7.11 - 7.25 | 73.17 | Backtest WATCHING plan expired before entry. |
| `SEIUSDT` | INVALIDATED（未入场前失效） | 2025-07-03T04:00:00+00:00 | 0.28 - 0.28 | 36.66 | Plan invalidated before entry: current price is below stop loss. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-07-03T08:00:00+00:00 | 0.59 - 0.60 | 66.10 | Backtest WATCHING plan expired before entry. |
| `DOGEUSDT` | EXPIRED（观察计划过期） | 2025-07-03T08:00:00+00:00 | 0.17 - 0.17 | 65.98 | Backtest WATCHING plan expired before entry. |
| `XRPUSDT` | EXPIRED（观察计划过期） | 2025-07-03T12:00:00+00:00 | 2.23 - 2.25 | 71.85 | Backtest WATCHING plan expired before entry. |
| `SOLUSDT` | EXPIRED（观察计划过期） | 2025-07-03T12:00:00+00:00 | 151.60 - 153.27 | 69.74 | Backtest WATCHING plan expired before entry. |
| `WIFUSDT` | EXPIRED（观察计划过期） | 2025-07-03T16:00:00+00:00 | 0.86 - 0.88 | 69.72 | Backtest WATCHING plan expired before entry. |
| `LTCUSDT` | EXPIRED（观察计划过期） | 2025-07-04T00:00:00+00:00 | 87.66 - 88.60 | 68.21 | Backtest WATCHING plan expired before entry. |
| `PNUTUSDT` | EXPIRED（观察计划过期） | 2025-07-04T00:00:00+00:00 | 0.23 - 0.24 | 68.13 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-04T04:00:00+00:00 | 659.14 - 661.18 | 57.11 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-07-04T16:00:00+00:00 | 0.00 - 0.00 | 71.04 | Backtest WATCHING plan expired before entry. |
| `PEPEUSDT` | EXPIRED（观察计划过期） | 2025-07-06T12:00:00+00:00 | 0.00 - 0.00 | 37.59 | Backtest WATCHING plan expired before entry. |
| `SOLUSDT` | EXPIRED（观察计划过期） | 2025-07-06T16:00:00+00:00 | 149.21 - 150.31 | 61.58 | Backtest WATCHING plan expired before entry. |
| `XRPUSDT` | EXPIRED（观察计划过期） | 2025-07-06T16:00:00+00:00 | 2.24 - 2.25 | 57.68 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-07T08:00:00+00:00 | 659.71 - 660.49 | 56.33 | Backtest WATCHING plan expired before entry. |
| `DOGEUSDT` | EXPIRED（观察计划过期） | 2025-07-07T12:00:00+00:00 | 0.17 - 0.17 | 59.67 | Backtest WATCHING plan expired before entry. |
| `UNIUSDT` | EXPIRED（观察计划过期） | 2025-07-07T12:00:00+00:00 | 7.29 - 7.39 | 55.05 | Backtest WATCHING plan expired before entry. |
| `PEPEUSDT` | EXPIRED（观察计划过期） | 2025-07-09T16:00:00+00:00 | 0.00 - 0.00 | 54.92 | Backtest WATCHING plan expired before entry. |
| `SOLUSDT` | EXPIRED（观察计划过期） | 2025-07-09T20:00:00+00:00 | 152.10 - 153.56 | 67.53 | Backtest WATCHING plan expired before entry. |
| `XRPUSDT` | EXPIRED（观察计划过期） | 2025-07-10T00:00:00+00:00 | 2.33 - 2.35 | 71.60 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-10T12:00:00+00:00 | 665.56 - 666.92 | 59.24 | Backtest WATCHING plan expired before entry. |
| `LINKUSDT` | EXPIRED（观察计划过期） | 2025-07-12T00:00:00+00:00 | 14.76 - 15.01 | 69.45 | Backtest WATCHING plan expired before entry. |
| `TONUSDT` | EXPIRED（观察计划过期） | 2025-07-12T00:00:00+00:00 | 2.91 - 2.94 | 58.93 | Backtest WATCHING plan expired before entry. |
| `SHIBUSDT` | EXPIRED（观察计划过期） | 2025-07-12T08:00:00+00:00 | 0.00 - 0.00 | 66.79 | Backtest WATCHING plan expired before entry. |
| `HBARUSDT` | EXPIRED（观察计划过期） | 2025-07-13T00:00:00+00:00 | 0.19 - 0.20 | 79.39 | Backtest WATCHING plan expired before entry. |
| `TRXUSDT` | EXPIRED（观察计划过期） | 2025-07-13T00:00:00+00:00 | 0.30 - 0.30 | 63.87 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-07-13T08:00:00+00:00 | 2,901.59 - 2,932.21 | 68.11 | Backtest WATCHING plan expired before entry. |
| `SOLUSDT` | EXPIRED（观察计划过期） | 2025-07-13T12:00:00+00:00 | 160.85 - 162.55 | 53.07 | Backtest WATCHING plan expired before entry. |
| `UNIUSDT` | EXPIRED（观察计划过期） | 2025-07-13T16:00:00+00:00 | 8.44 - 8.60 | 66.08 | Backtest WATCHING plan expired before entry. |
| `WIFUSDT` | EXPIRED（观察计划过期） | 2025-07-14T16:00:00+00:00 | 1.00 - 1.01 | 71.24 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-07-14T16:00:00+00:00 | 21.09 - 21.43 | 68.12 | Backtest WATCHING plan expired before entry. |
| `PNUTUSDT` | EXPIRED（观察计划过期） | 2025-07-15T16:00:00+00:00 | 0.27 - 0.28 | 72.20 | Backtest WATCHING plan expired before entry. |
| `PEPEUSDT` | EXPIRED（观察计划过期） | 2025-07-15T16:00:00+00:00 | 0.00 - 0.00 | 71.30 | Backtest WATCHING plan expired before entry. |
| `NEIROUSDT` | EXPIRED（观察计划过期） | 2025-07-15T16:00:00+00:00 | 0.00 - 0.00 | 70.58 | Backtest WATCHING plan expired before entry. |
| `ENAUSDT` | EXPIRED（观察计划过期） | 2025-07-16T04:00:00+00:00 | 0.34 - 0.35 | 81.68 | Backtest WATCHING plan expired before entry. |
| `XRPUSDT` | EXPIRED（观察计划过期） | 2025-07-16T04:00:00+00:00 | 2.86 - 2.91 | 72.56 | Backtest WATCHING plan expired before entry. |
| `ARBUSDT` | EXPIRED（观察计划过期） | 2025-07-16T12:00:00+00:00 | 0.42 - 0.43 | 81.05 | Backtest WATCHING plan expired before entry. |
| `XLMUSDT` | EXPIRED（观察计划过期） | 2025-07-16T20:00:00+00:00 | 0.45 - 0.46 | 76.07 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-07-17T00:00:00+00:00 | 0.74 - 0.75 | 75.72 | Backtest WATCHING plan expired before entry. |
| `TRUMPUSDT` | EXPIRED（观察计划过期） | 2025-07-18T00:00:00+00:00 | 9.77 - 10.01 | 56.82 | Backtest WATCHING plan expired before entry. |
| `UNIUSDT` | EXPIRED（观察计划过期） | 2025-07-18T00:00:00+00:00 | 8.69 - 8.93 | 40.18 | Backtest WATCHING plan expired before entry. |
| `LINKUSDT` | EXPIRED（观察计划过期） | 2025-07-18T20:00:00+00:00 | 17.22 - 17.63 | 77.87 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-07-18T20:00:00+00:00 | 22.96 - 23.49 | 75.25 | Backtest WATCHING plan expired before entry. |
| `SOLUSDT` | EXPIRED（观察计划过期） | 2025-07-18T20:00:00+00:00 | 173.19 - 176.38 | 73.20 | Backtest WATCHING plan expired before entry. |
| `NEIROUSDT` | EXPIRED（观察计划过期） | 2025-07-19T12:00:00+00:00 | 0.00 - 0.00 | 64.93 | Backtest WATCHING plan expired before entry. |
| `XRPUSDT` | EXPIRED（观察计划过期） | 2025-07-20T00:00:00+00:00 | 3.33 - 3.42 | 73.72 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-07-20T04:00:00+00:00 | 0.00 - 0.00 | 71.27 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-20T20:00:00+00:00 | 735.86 - 743.53 | 66.54 | Backtest WATCHING plan expired before entry. |
| `SHIBUSDT` | INVALIDATED（未入场前失效） | 2025-07-21T04:00:00+00:00 | 0.00 - 0.00 | 69.27 | Plan invalidated before entry: current price is below stop loss. |
| `BCHUSDT` | EXPIRED（观察计划过期） | 2025-07-21T04:00:00+00:00 | 524.83 - 532.49 | 65.47 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | INVALIDATED（未入场前失效） | 2025-07-22T00:00:00+00:00 | 0.86 - 0.88 | 74.74 | Plan invalidated before entry: current price is below stop loss. |
| `LINKUSDT` | INVALIDATED（未入场前失效） | 2025-07-22T00:00:00+00:00 | 18.98 - 19.37 | 73.81 | Plan invalidated before entry: current price is below stop loss. |
| `UNIUSDT` | INVALIDATED（未入场前失效） | 2025-07-22T00:00:00+00:00 | 10.46 - 10.73 | 71.87 | Plan invalidated before entry: current price is below stop loss. |
| `TAOUSDT` | EXPIRED（观察计划过期） | 2025-07-22T16:00:00+00:00 | 429.87 - 440.88 | 64.80 | Backtest WATCHING plan expired before entry. |
| `FLOKIUSDT` | INVALIDATED（未入场前失效） | 2025-07-22T20:00:00+00:00 | 0.00 - 0.00 | 80.66 | Plan invalidated before entry: current price is below stop loss. |
| `CRVUSDT` | EXPIRED（观察计划过期） | 2025-07-23T04:00:00+00:00 | 0.97 - 0.99 | 71.48 | Backtest WATCHING plan expired before entry. |
| `SOLUSDT` | EXPIRED（观察计划过期） | 2025-07-23T08:00:00+00:00 | 193.89 - 197.99 | 73.02 | Backtest WATCHING plan expired before entry. |
| `WLDUSDT` | INVALIDATED（未入场前失效） | 2025-07-23T16:00:00+00:00 | 1.25 - 1.25 | 66.68 | Plan invalidated before entry: current price is below stop loss. |
| `CFXUSDT` | EXPIRED（观察计划过期） | 2025-07-24T08:00:00+00:00 | 0.18 - 0.18 | 57.69 | Backtest WATCHING plan expired before entry. |
| `ENAUSDT` | EXPIRED（观察计划过期） | 2025-07-24T12:00:00+00:00 | 0.48 - 0.48 | 62.68 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-07-24T16:00:00+00:00 | 3,675.13 - 3,734.05 | 66.35 | Backtest WATCHING plan expired before entry. |
| `UNIUSDT` | EXPIRED（观察计划过期） | 2025-07-24T16:00:00+00:00 | 10.36 - 10.39 | 65.65 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-24T20:00:00+00:00 | 773.74 - 781.29 | 63.68 | Backtest WATCHING plan expired before entry. |
| `LTCUSDT` | EXPIRED（观察计划过期） | 2025-07-24T20:00:00+00:00 | 110.47 - 113.09 | 40.55 | Backtest WATCHING plan expired before entry. |
| `LINKUSDT` | EXPIRED（观察计划过期） | 2025-07-24T20:00:00+00:00 | 18.22 - 18.40 | 37.97 | Backtest WATCHING plan expired before entry. |
| `BCHUSDT` | EXPIRED（观察计划过期） | 2025-07-25T20:00:00+00:00 | 526.06 - 538.32 | 69.21 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-07-26T08:00:00+00:00 | 0.00 - 0.00 | 63.27 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-07-26T12:00:00+00:00 | 24.07 - 24.39 | 59.61 | Backtest WATCHING plan expired before entry. |
| `CRVUSDT` | EXPIRED（观察计划过期） | 2025-07-27T16:00:00+00:00 | 1.04 - 1.05 | 64.71 | Backtest WATCHING plan expired before entry. |
| `TRXUSDT` | EXPIRED（观察计划过期） | 2025-07-27T16:00:00+00:00 | 0.32 - 0.32 | 54.06 | Backtest WATCHING plan expired before entry. |
| `SOLUSDT` | INVALIDATED（未入场前失效） | 2025-07-27T20:00:00+00:00 | 186.84 - 187.48 | 61.00 | Plan invalidated before entry: current price is below stop loss. |
| `PENGUUSDT` | INVALIDATED（未入场前失效） | 2025-07-28T00:00:00+00:00 | 0.04 - 0.04 | 81.80 | Plan invalidated before entry: current price is below stop loss. |
| `UNIUSDT` | INVALIDATED（未入场前失效） | 2025-07-28T12:00:00+00:00 | 10.67 - 10.81 | 62.59 | Plan invalidated before entry: current price is below stop loss. |
| `CAKEUSDT` | EXPIRED（观察计划过期） | 2025-07-28T16:00:00+00:00 | 2.93 - 3.00 | 70.30 | Backtest WATCHING plan expired before entry. |
| `CRVUSDT` | INVALIDATED（未入场前失效） | 2025-07-30T20:00:00+00:00 | 1.01 - 1.03 | 66.23 | Plan invalidated before entry: current price is below stop loss. |
| `TONUSDT` | EXPIRED（观察计划过期） | 2025-07-31T00:00:00+00:00 | 3.34 - 3.40 | 65.42 | Backtest WATCHING plan expired before entry. |
| `XRPUSDT` | INVALIDATED（未入场前失效） | 2025-07-31T04:00:00+00:00 | 3.15 - 3.15 | 40.70 | Plan invalidated before entry: current price is below stop loss. |
| `LINKUSDT` | INVALIDATED（未入场前失效） | 2025-07-31T08:00:00+00:00 | 18.04 - 18.08 | 47.35 | Plan invalidated before entry: current price is below stop loss. |
| `BNBUSDT` | INVALIDATED（未入场前失效） | 2025-07-31T08:00:00+00:00 | 795.60 - 804.81 | 38.20 | Plan invalidated before entry: current price is below stop loss. |
| `TRXUSDT` | EXPIRED（观察计划过期） | 2025-07-31T16:00:00+00:00 | 0.33 - 0.33 | 58.45 | Backtest WATCHING plan expired before entry. |
| `BCHUSDT` | EXPIRED（观察计划过期） | 2025-08-08T00:00:00+00:00 | 569.87 - 576.42 | 61.79 | Backtest WATCHING plan expired before entry. |
| `SOLUSDT` | EXPIRED（观察计划过期） | 2025-08-08T00:00:00+00:00 | 172.32 - 174.39 | 50.66 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-08-08T00:00:00+00:00 | 22.80 - 23.08 | 49.26 | Backtest WATCHING plan expired before entry. |
| `ENAUSDT` | EXPIRED（观察计划过期） | 2025-08-08T08:00:00+00:00 | 0.61 - 0.63 | 69.59 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-08-08T08:00:00+00:00 | 773.64 - 778.88 | 60.60 | Backtest WATCHING plan expired before entry. |
| `XRPUSDT` | EXPIRED（观察计划过期） | 2025-08-08T16:00:00+00:00 | 3.14 - 3.19 | 75.28 | Backtest WATCHING plan expired before entry. |
| `PENGUUSDT` | EXPIRED（观察计划过期） | 2025-08-08T16:00:00+00:00 | 0.04 - 0.04 | 67.03 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-08-08T16:00:00+00:00 | 0.76 - 0.77 | 65.29 | Backtest WATCHING plan expired before entry. |
| `SUIUSDT` | EXPIRED（观察计划过期） | 2025-08-08T16:00:00+00:00 | 3.65 - 3.72 | 63.32 | Backtest WATCHING plan expired before entry. |
| `CRVUSDT` | EXPIRED（观察计划过期） | 2025-08-09T00:00:00+00:00 | 0.93 - 0.95 | 54.65 | Backtest WATCHING plan expired before entry. |
| `SOLUSDT` | EXPIRED（观察计划过期） | 2025-08-11T04:00:00+00:00 | 179.54 - 181.92 | 72.49 | Backtest WATCHING plan expired before entry. |
| `UNIUSDT` | EXPIRED（观察计划过期） | 2025-08-11T08:00:00+00:00 | 10.81 - 11.03 | 70.67 | Backtest WATCHING plan expired before entry. |
| `DOGEUSDT` | EXPIRED（观察计划过期） | 2025-08-11T08:00:00+00:00 | 0.23 - 0.23 | 67.47 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-08-11T12:00:00+00:00 | 4,146.78 - 4,197.66 | 71.09 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-08-11T16:00:00+00:00 | 801.89 - 809.22 | 62.06 | Backtest WATCHING plan expired before entry. |
| `PENDLEUSDT` | EXPIRED（观察计划过期） | 2025-08-12T04:00:00+00:00 | 5.36 - 5.51 | 67.66 | Backtest WATCHING plan expired before entry. |
| `LINKUSDT` | EXPIRED（观察计划过期） | 2025-08-12T12:00:00+00:00 | 21.20 - 21.36 | 72.34 | Backtest WATCHING plan expired before entry. |
| `PEPEUSDT` | INVALIDATED（未入场前失效） | 2025-08-12T16:00:00+00:00 | 0.00 - 0.00 | 68.08 | Plan invalidated before entry: current price is below stop loss. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-08-12T16:00:00+00:00 | 0.79 - 0.81 | 65.38 | Backtest WATCHING plan expired before entry. |
| `SUIUSDT` | EXPIRED（观察计划过期） | 2025-08-12T16:00:00+00:00 | 3.77 - 3.82 | 63.57 | Backtest WATCHING plan expired before entry. |
| `ETHFIUSDT` | INVALIDATED（未入场前失效） | 2025-08-14T12:00:00+00:00 | 1.26 - 1.30 | 75.31 | Plan invalidated before entry: current price is below stop loss. |
| `NEARUSDT` | EXPIRED（观察计划过期） | 2025-08-14T12:00:00+00:00 | 2.86 - 2.91 | 66.97 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-08-15T08:00:00+00:00 | 24.58 - 25.09 | 67.53 | Backtest WATCHING plan expired before entry. |
| `ENAUSDT` | EXPIRED（观察计划过期） | 2025-08-15T08:00:00+00:00 | 0.73 - 0.74 | 42.46 | Backtest WATCHING plan expired before entry. |
| `PENDLEUSDT` | EXPIRED（观察计划过期） | 2025-08-15T08:00:00+00:00 | 5.27 - 5.44 | 39.90 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-08-15T20:00:00+00:00 | 0.91 - 0.93 | 73.08 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | INVALIDATED（未入场前失效） | 2025-08-17T04:00:00+00:00 | 4,376.86 - 4,430.92 | 37.85 | Plan invalidated before entry: current price is below stop loss. |
| `PEPEUSDT` | INVALIDATED（未入场前失效） | 2025-08-23T00:00:00+00:00 | 0.00 - 0.00 | 61.33 | Plan invalidated before entry: current price is below stop loss. |
| `SUIUSDT` | EXPIRED（观察计划过期） | 2025-08-23T00:00:00+00:00 | 3.68 - 3.74 | 60.68 | Backtest WATCHING plan expired before entry. |
| `LINKUSDT` | INVALIDATED（未入场前失效） | 2025-08-23T04:00:00+00:00 | 25.53 - 26.03 | 78.34 | Plan invalidated before entry: current price is below stop loss. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-08-23T04:00:00+00:00 | 861.81 - 871.06 | 71.00 | Backtest WATCHING plan expired before entry. |
| `PENGUUSDT` | EXPIRED（观察计划过期） | 2025-08-23T04:00:00+00:00 | 0.03 - 0.03 | 66.08 | Backtest WATCHING plan expired before entry. |
| `DOTUSDT` | EXPIRED（观察计划过期） | 2025-08-23T04:00:00+00:00 | 3.95 - 4.01 | 58.40 | Backtest WATCHING plan expired before entry. |
| `LTCUSDT` | INVALIDATED（未入场前失效） | 2025-08-23T08:00:00+00:00 | 118.50 - 120.04 | 55.73 | Plan invalidated before entry: current price is below stop loss. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-08-23T12:00:00+00:00 | 0.89 - 0.91 | 71.43 | Backtest WATCHING plan expired before entry. |

## 数据质量摘要

| Severity（严重程度） | Symbol（交易对） | Interval（周期） | Message（说明） |
|---|---|---|---|
| ERROR | `0GUSDT` | 1h | No klines available for requested range. |
| ERROR | `0GUSDT` | 4h | No klines available for requested range. |
| ERROR | `0GUSDT` | 1d | No klines available for requested range. |
| WARNING | `1000CATUSDT` | 1h | Large wick/range candle. |
| WARNING | `1000CATUSDT` | 4h | Large wick/range candle. |
| WARNING | `1000CATUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000CATUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000CATUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000CATUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000CATUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000CATUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000CATUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000CHEEMSUSDT` | 1h | Large wick/range candle. |
| WARNING | `1000CHEEMSUSDT` | 1h | Large wick/range candle. |
| WARNING | `1000CHEEMSUSDT` | 4h | Large wick/range candle. |
| WARNING | `1000CHEEMSUSDT` | 4h | Large wick/range candle. |
| WARNING | `1000CHEEMSUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000CHEEMSUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000CHEEMSUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000SATSUSDT` | 1h | Large wick/range candle. |
| WARNING | `1000SATSUSDT` | 4h | Large wick/range candle. |
| WARNING | `1000SATSUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000SATSUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000SATSUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000SATSUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000SATSUSDT` | 1d | Large wick/range candle. |
| WARNING | `1INCHUSDT` | 1d | Large wick/range candle. |
| WARNING | `1MBABYDOGEUSDT` | 1h | Large wick/range candle. |
| WARNING | `1MBABYDOGEUSDT` | 1h | Large wick/range candle. |
| WARNING | `1MBABYDOGEUSDT` | 4h | Large wick/range candle. |
| WARNING | `1MBABYDOGEUSDT` | 4h | Large wick/range candle. |
| WARNING | `1MBABYDOGEUSDT` | 4h | Large wick/range candle. |
| WARNING | `1MBABYDOGEUSDT` | 1d | Large wick/range candle. |
| WARNING | `1MBABYDOGEUSDT` | 1d | Large wick/range candle. |
| WARNING | `1MBABYDOGEUSDT` | 1d | Large wick/range candle. |
| WARNING | `1MBABYDOGEUSDT` | 1d | Large wick/range candle. |
| WARNING | `1MBABYDOGEUSDT` | 1d | Large wick/range candle. |
| ERROR | `2ZUSDT` | 1h | No klines available for requested range. |
| ERROR | `2ZUSDT` | 4h | No klines available for requested range. |
| ERROR | `2ZUSDT` | 1d | No klines available for requested range. |
| WARNING | `AAVEUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACEUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACEUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACEUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACHUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACHUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACHUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACHUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACHUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACHUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACHUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACMUSDT` | 1h | Large wick/range candle. |
| WARNING | `ACMUSDT` | 1h | Large wick/range candle. |
| WARNING | `ACMUSDT` | 1h | Large wick/range candle. |
| WARNING | `ACMUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACMUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACMUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACMUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACMUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACMUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACTUSDT` | 1h | Large wick/range candle. |
| WARNING | `ACTUSDT` | 1h | Large wick/range candle. |
| WARNING | `ACTUSDT` | 1h | Large wick/range candle. |
| WARNING | `ACTUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACTUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACTUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACTUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACTUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACTUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACTUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACTUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACTUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACTUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACTUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACTUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACTUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACTUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACTUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACTUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACTUSDT` | 1d | Large wick/range candle. |
| INFO | n/a | n/a | Additional issues omitted: 2293. |

## 原始配置快照

```json
{
  "backtest": {
    "maker_fee_bps": 4.0,
    "taker_fee_bps": 10.0,
    "entry_slippage_bps": 5.0,
    "stop_slippage_bps": 10.0,
    "intrabar_policy": "stop_first",
    "primary_interval": "4h",
    "execution_interval": "4h",
    "initial_equity": 10000.0,
    "max_open_plans": 10,
    "max_active_positions": 5,
    "total_active_risk_pct": 0.05,
    "risk_per_trade_pct": 0.01,
    "max_position_notional_pct": 1.0,
    "allow_leverage": false,
    "watch_expiry_bars": 18,
    "warmup_1h_bars": 200,
    "warmup_4h_bars": 100,
    "warmup_1d_bars": 80
  },
  "analysis": {
    "risk_reward_min": 2.0,
    "risk_per_trade_pct": 0.01,
    "min_history_days": 180,
    "market_regime_filter_enabled": true,
    "data_quality_filter_enabled": true,
    "strict_data_quality_for_buy": true,
    "pump_chase_24h_pct": 20.0,
    "pump_chase_distance_pct": 8.0,
    "pump_chase_penalty": 8.0,
    "high_volatility_range_pct": 35.0,
    "high_volatility_penalty": 6.0,
    "validation_pool_multiplier": 2,
    "validation_pool_max": 10
  },
  "market_top_n": 5,
  "universe_mode": false,
  "universe_snapshot": null,
  "dynamic_universe_mode": true,
  "dynamic_universe_summary": {
    "mode": "dynamic_universe",
    "source": "Binance current exchangeInfo tradable USDT spot symbols",
    "created_at_utc": "2026-06-09T10:47:56+00:00",
    "refresh_frequency": "daily",
    "max_symbols": 40,
    "master_count": 418,
    "source_limit": null,
    "source_limit_applied": false,
    "universe_refresh_count": 244,
    "selected_count_min": 7,
    "selected_count_avg": 22.80327868852459,
    "selected_count_max": 40,
    "top_selected_symbols": [
      {
        "symbol": "BTCUSDT",
        "days_selected": 244
      },
      {
        "symbol": "ETHUSDT",
        "days_selected": 244
      },
      {
        "symbol": "SOLUSDT",
        "days_selected": 244
      },
      {
        "symbol": "SUIUSDT",
        "days_selected": 243
      },
      {
        "symbol": "XRPUSDT",
        "days_selected": 243
      },
      {
        "symbol": "PEPEUSDT",
        "days_selected": 242
      },
      {
        "symbol": "DOGEUSDT",
        "days_selected": 241
      },
      {
        "symbol": "BNBUSDT",
        "days_selected": 239
      },
      {
        "symbol": "TRXUSDT",
        "days_selected": 231
      },
      {
        "symbol": "ADAUSDT",
        "days_selected": 221
      },
      {
        "symbol": "ENAUSDT",
        "days_selected": 177
      },
      {
        "symbol": "TRUMPUSDT",
        "days_selected": 163
      },
      {
        "symbol": "LINKUSDT",
        "days_selected": 146
      },
      {
        "symbol": "WIFUSDT",
        "days_selected": 142
      },
      {
        "symbol": "AVAXUSDT",
        "days_selected": 141
      },
      {
        "symbol": "LTCUSDT",
        "days_selected": 141
      },
      {
        "symbol": "HBARUSDT",
        "days_selected": 110
      },
      {
        "symbol": "UNIUSDT",
        "days_selected": 105
      },
      {
        "symbol": "AAVEUSDT",
        "days_selected": 103
      },
      {
        "symbol": "PENGUUSDT",
        "days_selected": 95
      }
    ],
    "filter_counts": {
      "missing_1h": 21197,
      "insufficient_24h": 63,
      "reconstruct_error": 0,
      "low_quote_volume": 75003,
      "low_trades": 7,
      "stable_like": 0
    },
    "selection_by_day": [
      {
        "date_utc": "2025-01-01",
        "decision_time_utc": "2025-01-01T04:00:00+00:00",
        "selected_symbols": [
          "PENGUUSDT",
          "PEPEUSDT",
          "THEUSDT",
          "PNUTUSDT",
          "NEIROUSDT",
          "XRPUSDT",
          "LTCUSDT",
          "WIFUSDT",
          "FLOKIUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "WLDUSDT",
          "SUIUSDT",
          "ETHUSDT",
          "MOVEUSDT",
          "SOLUSDT",
          "SHIBUSDT",
          "TRXUSDT",
          "BNBUSDT",
          "USUALUSDT",
          "ADAUSDT",
          "PHAUSDT",
          "HBARUSDT",
          "LINKUSDT",
          "AAVEUSDT",
          "ENAUSDT",
          "UNIUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 28,
        "filter_counts": {
          "missing_1h": 122,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 268,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-02",
        "decision_time_utc": "2025-01-02T00:00:00+00:00",
        "selected_symbols": [
          "XLMUSDT",
          "PENGUUSDT",
          "XRPUSDT",
          "HBARUSDT",
          "ADAUSDT",
          "LINKUSDT",
          "CRVUSDT",
          "ENAUSDT",
          "ACTUSDT",
          "SUIUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "USUALUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "ETHUSDT",
          "LTCUSDT",
          "PEPEUSDT",
          "PNUTUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "PHAUSDT",
          "WIFUSDT",
          "CVCUSDT"
        ],
        "candidate_count": 24,
        "filter_counts": {
          "missing_1h": 122,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 272,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-03",
        "decision_time_utc": "2025-01-03T00:00:00+00:00",
        "selected_symbols": [
          "AIUSDT",
          "SOLUSDT",
          "WIFUSDT",
          "ACTUSDT",
          "ENAUSDT",
          "PEPEUSDT",
          "BONKUSDT",
          "USUALUSDT",
          "TAOUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "GALAUSDT",
          "SHIBUSDT",
          "ADAUSDT",
          "UNIUSDT",
          "CRVUSDT",
          "FETUSDT",
          "TRXUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ALGOUSDT",
          "WLDUSDT",
          "XLMUSDT",
          "PNUTUSDT",
          "SUIUSDT",
          "VANAUSDT",
          "LINKUSDT",
          "NEIROUSDT",
          "BNBUSDT",
          "AGLDUSDT",
          "HBARUSDT",
          "PENGUUSDT",
          "PHAUSDT",
          "LTCUSDT"
        ],
        "candidate_count": 36,
        "filter_counts": {
          "missing_1h": 122,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 260,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-04",
        "decision_time_utc": "2025-01-04T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "SUIUSDT",
          "NEIROUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "BONKUSDT",
          "GALAUSDT",
          "SANDUSDT",
          "PNUTUSDT",
          "AGLDUSDT",
          "FLOKIUSDT",
          "HBARUSDT",
          "DOTUSDT",
          "FETUSDT",
          "ETHUSDT",
          "WIFUSDT",
          "LTCUSDT",
          "LINKUSDT",
          "CRVUSDT",
          "SOLUSDT",
          "AVAXUSDT",
          "PEPEUSDT",
          "SHIBUSDT",
          "ALGOUSDT",
          "NEARUSDT",
          "TAOUSDT",
          "UNIUSDT",
          "AAVEUSDT",
          "WLDUSDT",
          "XLMUSDT",
          "BTCUSDT",
          "XRPUSDT",
          "PHAUSDT",
          "USUALUSDT",
          "TRXUSDT",
          "BNBUSDT",
          "ACTUSDT",
          "PENGUUSDT",
          "ZENUSDT"
        ],
        "candidate_count": 39,
        "filter_counts": {
          "missing_1h": 121,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 257,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-05",
        "decision_time_utc": "2025-01-05T00:00:00+00:00",
        "selected_symbols": [
          "PENGUUSDT",
          "SUIUSDT",
          "STGUSDT",
          "ARBUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "AVAXUSDT",
          "MOVEUSDT",
          "BIOUSDT",
          "PEPEUSDT",
          "XLMUSDT",
          "ADAUSDT",
          "TAOUSDT",
          "TRXUSDT",
          "LINKUSDT",
          "BNBUSDT",
          "PHAUSDT",
          "HBARUSDT",
          "PNUTUSDT",
          "USUALUSDT",
          "UNIUSDT",
          "AAVEUSDT",
          "NEIROUSDT",
          "SHIBUSDT",
          "RSRUSDT",
          "WLDUSDT",
          "GALAUSDT"
        ],
        "candidate_count": 31,
        "filter_counts": {
          "missing_1h": 121,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 266,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-06",
        "decision_time_utc": "2025-01-06T00:00:00+00:00",
        "selected_symbols": [
          "HIVEUSDT",
          "ACTUSDT",
          "STGUSDT",
          "MOVEUSDT",
          "FETUSDT",
          "STEEMUSDT",
          "BIOUSDT",
          "USUALUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "PNUTUSDT",
          "ARBUSDT",
          "ETHUSDT",
          "PHAUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "PENGUUSDT",
          "AVAXUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "HBARUSDT",
          "BNBUSDT",
          "NEIROUSDT",
          "XLMUSDT",
          "LINKUSDT"
        ],
        "candidate_count": 28,
        "filter_counts": {
          "missing_1h": 121,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 269,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-07",
        "decision_time_utc": "2025-01-07T00:00:00+00:00",
        "selected_symbols": [
          "HIVEUSDT",
          "WLDUSDT",
          "SANDUSDT",
          "PENGUUSDT",
          "BTCUSDT",
          "RENDERUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "XRPUSDT",
          "HBARUSDT",
          "AVAXUSDT",
          "GALAUSDT",
          "BONKUSDT",
          "LINKUSDT",
          "INJUSDT",
          "NEARUSDT",
          "FILUSDT",
          "PEPEUSDT",
          "XLMUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "DOTUSDT",
          "BIOUSDT",
          "FLOKIUSDT",
          "ENAUSDT",
          "SHIBUSDT",
          "ARBUSDT",
          "PNUTUSDT",
          "RUNEUSDT",
          "UNIUSDT",
          "USUALUSDT",
          "WIFUSDT",
          "LTCUSDT",
          "TAOUSDT",
          "ACTUSDT",
          "FETUSDT",
          "MOVEUSDT"
        ],
        "candidate_count": 43,
        "filter_counts": {
          "missing_1h": 121,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 254,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-08",
        "decision_time_utc": "2025-01-08T00:00:00+00:00",
        "selected_symbols": [
          "GUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "ADAUSDT",
          "PEPEUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "TRXUSDT",
          "ACTUSDT",
          "HBARUSDT",
          "WLDUSDT",
          "ENAUSDT",
          "LINKUSDT",
          "XLMUSDT",
          "APTUSDT",
          "PENGUUSDT",
          "USUALUSDT",
          "AVAXUSDT",
          "PNUTUSDT",
          "HIVEUSDT",
          "SHIBUSDT",
          "BIOUSDT",
          "WIFUSDT",
          "NEIROUSDT",
          "FETUSDT",
          "LTCUSDT",
          "DOTUSDT",
          "GALAUSDT",
          "TAOUSDT",
          "FILUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "SANDUSDT",
          "NEARUSDT",
          "RENDERUSDT",
          "AAVEUSDT",
          "SEIUSDT"
        ],
        "candidate_count": 44,
        "filter_counts": {
          "missing_1h": 121,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 253,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-09",
        "decision_time_utc": "2025-01-09T00:00:00+00:00",
        "selected_symbols": [
          "STEEMUSDT",
          "GASUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "PHAUSDT",
          "XLMUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "PEPEUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "ENAUSDT",
          "LINKUSDT",
          "HBARUSDT",
          "WLDUSDT",
          "ACTUSDT",
          "PENGUUSDT",
          "AVAXUSDT",
          "USUALUSDT",
          "NEIROUSDT",
          "WIFUSDT",
          "PNUTUSDT",
          "BIOUSDT",
          "FETUSDT",
          "APTUSDT",
          "SHIBUSDT",
          "DOTUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "LTCUSDT",
          "TAOUSDT",
          "GALAUSDT",
          "NEARUSDT",
          "RUNEUSDT",
          "RENDERUSDT",
          "FILUSDT",
          "MOVEUSDT"
        ],
        "candidate_count": 50,
        "filter_counts": {
          "missing_1h": 121,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 247,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-10",
        "decision_time_utc": "2025-01-10T00:00:00+00:00",
        "selected_symbols": [
          "GASUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "LTCUSDT",
          "WIFUSDT",
          "PENGUUSDT",
          "LINKUSDT",
          "HBARUSDT",
          "RUNEUSDT",
          "FETUSDT",
          "WLDUSDT",
          "USUALUSDT",
          "ACTUSDT",
          "XLMUSDT",
          "NEIROUSDT",
          "BIOUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "PNUTUSDT",
          "SHIBUSDT",
          "TAOUSDT",
          "GALAUSDT",
          "APTUSDT",
          "MOVEUSDT",
          "NEARUSDT",
          "FILUSDT",
          "STEEMUSDT"
        ],
        "candidate_count": 36,
        "filter_counts": {
          "missing_1h": 120,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 261,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-11",
        "decision_time_utc": "2025-01-11T00:00:00+00:00",
        "selected_symbols": [
          "IQUSDT",
          "SUIUSDT",
          "UNIUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "XLMUSDT",
          "XRPUSDT",
          "APTUSDT",
          "RUNEUSDT",
          "PEPEUSDT",
          "HBARUSDT",
          "ETHUSDT",
          "GALAUSDT",
          "ADAUSDT",
          "SOLUSDT",
          "LINKUSDT",
          "TRXUSDT",
          "FETUSDT",
          "WLDUSDT",
          "SHIBUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "AAVEUSDT",
          "TAOUSDT",
          "WIFUSDT",
          "LTCUSDT",
          "AVAXUSDT",
          "USUALUSDT",
          "NEIROUSDT",
          "PENGUUSDT",
          "ARBUSDT",
          "BIOUSDT",
          "ACTUSDT",
          "PNUTUSDT"
        ],
        "candidate_count": 34,
        "filter_counts": {
          "missing_1h": 117,
          "insufficient_24h": 3,
          "reconstruct_error": 0,
          "low_quote_volume": 264,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-12",
        "decision_time_utc": "2025-01-12T00:00:00+00:00",
        "selected_symbols": [
          "XRPUSDT",
          "HIVEUSDT",
          "XLMUSDT",
          "ADAUSDT",
          "HBARUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "SUIUSDT",
          "WLDUSDT",
          "USUALUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "CGPTUSDT",
          "RUNEUSDT",
          "LINKUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 117,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 282,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-13",
        "decision_time_utc": "2025-01-13T00:00:00+00:00",
        "selected_symbols": [
          "PROMUSDT",
          "PNUTUSDT",
          "BTCUSDT",
          "XRPUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "ENAUSDT",
          "TRXUSDT",
          "HBARUSDT",
          "USUALUSDT",
          "XLMUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 117,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 285,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-14",
        "decision_time_utc": "2025-01-14T00:00:00+00:00",
        "selected_symbols": [
          "PROMUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "SOLUSDT",
          "PNUTUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "WLDUSDT",
          "LINKUSDT",
          "AAVEUSDT",
          "WIFUSDT",
          "HBARUSDT",
          "FETUSDT",
          "PENGUUSDT",
          "USUALUSDT",
          "AVAXUSDT",
          "RUNEUSDT",
          "SHIBUSDT",
          "XLMUSDT",
          "TAOUSDT",
          "GALAUSDT",
          "NEARUSDT",
          "APTUSDT",
          "CGPTUSDT",
          "ACTUSDT",
          "ARBUSDT",
          "LTCUSDT",
          "NEIROUSDT",
          "FILUSDT",
          "DOTUSDT",
          "SEIUSDT",
          "CRVUSDT",
          "BIOUSDT",
          "UNIUSDT"
        ],
        "candidate_count": 42,
        "filter_counts": {
          "missing_1h": 117,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 259,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-15",
        "decision_time_utc": "2025-01-15T00:00:00+00:00",
        "selected_symbols": [
          "AIXBTUSDT",
          "CGPTUSDT",
          "COOKIEUSDT",
          "GALAUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "PNUTUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BIOUSDT",
          "LINKUSDT",
          "ENAUSDT",
          "SOLUSDT",
          "HBARUSDT",
          "PEPEUSDT",
          "WLDUSDT",
          "WIFUSDT",
          "XLMUSDT",
          "PENGUUSDT",
          "BNBUSDT",
          "USUALUSDT",
          "SUIUSDT",
          "TRXUSDT",
          "RUNEUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 117,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 276,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-16",
        "decision_time_utc": "2025-01-16T00:00:00+00:00",
        "selected_symbols": [
          "ZENUSDT",
          "AIXBTUSDT",
          "XRPUSDT",
          "ALGOUSDT",
          "XLMUSDT",
          "ENAUSDT",
          "LTCUSDT",
          "WIFUSDT",
          "HBARUSDT",
          "SOLUSDT",
          "PENGUUSDT",
          "CRVUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "ETHUSDT",
          "CGPTUSDT",
          "TAOUSDT",
          "COOKIEUSDT",
          "ADAUSDT",
          "RUNEUSDT",
          "LINKUSDT",
          "AVAXUSDT",
          "WLDUSDT",
          "UNIUSDT",
          "TRXUSDT",
          "NEIROUSDT",
          "AAVEUSDT",
          "FILUSDT",
          "BTCUSDT",
          "USUALUSDT",
          "JASMYUSDT",
          "GALAUSDT",
          "SUIUSDT",
          "DOTUSDT",
          "ARBUSDT",
          "SHIBUSDT",
          "BIOUSDT",
          "NEARUSDT",
          "FETUSDT",
          "APTUSDT"
        ],
        "candidate_count": 42,
        "filter_counts": {
          "missing_1h": 117,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 259,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-17",
        "decision_time_utc": "2025-01-17T00:00:00+00:00",
        "selected_symbols": [
          "HBARUSDT",
          "LTCUSDT",
          "XRPUSDT",
          "PHAUSDT",
          "SOLUSDT",
          "LINKUSDT",
          "ALGOUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "XLMUSDT",
          "PEPEUSDT",
          "IOTAUSDT",
          "AIXBTUSDT",
          "TRXUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "WIFUSDT",
          "PNUTUSDT",
          "WLDUSDT",
          "SHIBUSDT",
          "DOTUSDT",
          "APTUSDT",
          "USUALUSDT",
          "FILUSDT",
          "FETUSDT",
          "CRVUSDT",
          "GALAUSDT",
          "ZENUSDT",
          "CGPTUSDT",
          "ARBUSDT",
          "NEARUSDT",
          "RUNEUSDT",
          "TAOUSDT",
          "PENGUUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 39,
        "filter_counts": {
          "missing_1h": 116,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 262,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-18",
        "decision_time_utc": "2025-01-18T00:00:00+00:00",
        "selected_symbols": [
          "SPELLUSDT",
          "BONKUSDT",
          "RUNEUSDT",
          "AMPUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "LTCUSDT",
          "CRVUSDT",
          "NEARUSDT",
          "SHIBUSDT",
          "FLOKIUSDT",
          "LINKUSDT",
          "VETUSDT",
          "PNUTUSDT",
          "NEIROUSDT",
          "TAOUSDT",
          "SANDUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "WLDUSDT",
          "GALAUSDT",
          "TIAUSDT",
          "SOLUSDT",
          "WIFUSDT",
          "ENAUSDT",
          "UNIUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "MOVEUSDT",
          "APTUSDT",
          "FETUSDT",
          "HBARUSDT",
          "XRPUSDT",
          "DOTUSDT",
          "SUIUSDT",
          "FILUSDT",
          "AVAXUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 46,
        "filter_counts": {
          "missing_1h": 115,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 256,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-19",
        "decision_time_utc": "2025-01-19T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "RAYUSDT",
          "JTOUSDT",
          "FIDAUSDT",
          "SUIUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "BONKUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "LTCUSDT",
          "HBARUSDT",
          "ENAUSDT",
          "PNUTUSDT",
          "XLMUSDT",
          "WIFUSDT",
          "LINKUSDT",
          "USUALUSDT",
          "SHIBUSDT",
          "SOLVUSDT",
          "PENGUUSDT",
          "WLDUSDT",
          "NEIROUSDT",
          "AIXBTUSDT",
          "SPELLUSDT",
          "AVAXUSDT",
          "RUNEUSDT",
          "TAOUSDT",
          "UNIUSDT",
          "AAVEUSDT",
          "FILUSDT",
          "CRVUSDT",
          "ARBUSDT",
          "ACTUSDT",
          "NEARUSDT",
          "FLOKIUSDT"
        ],
        "candidate_count": 47,
        "filter_counts": {
          "missing_1h": 115,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 256,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-20",
        "decision_time_utc": "2025-01-20T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "COWUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "LINKUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "ENAUSDT",
          "SHIBUSDT",
          "HBARUSDT",
          "BONKUSDT",
          "WIFUSDT",
          "LTCUSDT",
          "PNUTUSDT",
          "AIXBTUSDT",
          "AVAXUSDT",
          "XLMUSDT",
          "WLDUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "PENGUUSDT",
          "NEIROUSDT",
          "APTUSDT",
          "OPUSDT",
          "TAOUSDT",
          "FETUSDT",
          "DOTUSDT",
          "NEARUSDT",
          "RAYUSDT",
          "FLOKIUSDT",
          "SUSDT",
          "FIDAUSDT",
          "CRVUSDT",
          "FILUSDT",
          "GALAUSDT"
        ],
        "candidate_count": 69,
        "filter_counts": {
          "missing_1h": 114,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 234,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-21",
        "decision_time_utc": "2025-01-21T00:00:00+00:00",
        "selected_symbols": [
          "RAYUSDT",
          "LDOUSDT",
          "AAVEUSDT",
          "AIXBTUSDT",
          "XRPUSDT",
          "ALGOUSDT",
          "HBARUSDT",
          "ETHUSDT",
          "TRXUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "LINKUSDT",
          "CRVUSDT",
          "INJUSDT",
          "XLMUSDT",
          "SOLUSDT",
          "LTCUSDT",
          "ADAUSDT",
          "TONUSDT",
          "DOGEUSDT",
          "NEARUSDT",
          "FILUSDT",
          "ACTUSDT",
          "DOTUSDT",
          "PEPEUSDT",
          "ENSUSDT",
          "SUIUSDT",
          "AVAXUSDT",
          "SANDUSDT",
          "UNIUSDT",
          "BNBUSDT",
          "FETUSDT",
          "WIFUSDT",
          "SHIBUSDT",
          "BONKUSDT",
          "SEIUSDT",
          "PNUTUSDT",
          "WLDUSDT",
          "APTUSDT",
          "VETUSDT"
        ],
        "candidate_count": 67,
        "filter_counts": {
          "missing_1h": 114,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 237,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-22",
        "decision_time_utc": "2025-01-22T00:00:00+00:00",
        "selected_symbols": [
          "SUSDT",
          "TRUMPUSDT",
          "WLDUSDT",
          "AAVEUSDT",
          "FETUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "LINKUSDT",
          "ENAUSDT",
          "SUIUSDT",
          "VETUSDT",
          "SOLUSDT",
          "RUNEUSDT",
          "XRPUSDT",
          "WIFUSDT",
          "ETHUSDT",
          "TAOUSDT",
          "LDOUSDT",
          "TRXUSDT",
          "RAYUSDT",
          "GMTUSDT",
          "DOTUSDT",
          "FLOKIUSDT",
          "ARBUSDT",
          "SHIBUSDT",
          "NEARUSDT",
          "AVAXUSDT",
          "PEPEUSDT",
          "BNBUSDT",
          "APTUSDT",
          "SOLVUSDT",
          "NEIROUSDT",
          "ADAUSDT",
          "LTCUSDT",
          "HBARUSDT",
          "AIXBTUSDT",
          "PNUTUSDT",
          "PENGUUSDT",
          "CRVUSDT"
        ],
        "candidate_count": 45,
        "filter_counts": {
          "missing_1h": 114,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 259,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-23",
        "decision_time_utc": "2025-01-23T00:00:00+00:00",
        "selected_symbols": [
          "AIXBTUSDT",
          "WLDUSDT",
          "SOLUSDT",
          "TRXUSDT",
          "ACTUSDT",
          "BTCUSDT",
          "RAYUSDT",
          "TRUMPUSDT",
          "PENGUUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "PEPEUSDT",
          "VTHOUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "BONKUSDT",
          "LINKUSDT",
          "HBARUSDT",
          "AAVEUSDT",
          "LTCUSDT",
          "WIFUSDT",
          "XLMUSDT",
          "SUSDT",
          "AVAXUSDT",
          "PNUTUSDT",
          "VETUSDT",
          "FETUSDT"
        ],
        "candidate_count": 30,
        "filter_counts": {
          "missing_1h": 114,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 274,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-24",
        "decision_time_utc": "2025-01-24T00:00:00+00:00",
        "selected_symbols": [
          "ETCUSDT",
          "ETHUSDT",
          "BIOUSDT",
          "BTCUSDT",
          "RAYUSDT",
          "SOLUSDT",
          "TRUMPUSDT",
          "XRPUSDT",
          "PEPEUSDT",
          "ARBUSDT",
          "LINKUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "SUIUSDT",
          "HBARUSDT",
          "BNBUSDT",
          "WLDUSDT",
          "LTCUSDT",
          "ACTUSDT",
          "ENAUSDT",
          "AIXBTUSDT",
          "XLMUSDT",
          "WIFUSDT",
          "RUNEUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "PENGUUSDT",
          "BONKUSDT",
          "TAOUSDT",
          "FETUSDT",
          "VTHOUSDT",
          "PNUTUSDT",
          "SHIBUSDT",
          "NEARUSDT",
          "APTUSDT",
          "FLOKIUSDT",
          "PONDUSDT"
        ],
        "candidate_count": 38,
        "filter_counts": {
          "missing_1h": 113,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 266,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-25",
        "decision_time_utc": "2025-01-25T00:00:00+00:00",
        "selected_symbols": [
          "HIVEUSDT",
          "LDOUSDT",
          "SPELLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "TRUMPUSDT",
          "XRPUSDT",
          "LTCUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "PEPEUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "HBARUSDT",
          "ADAUSDT",
          "LINKUSDT",
          "WLDUSDT",
          "NEARUSDT",
          "AAVEUSDT",
          "WIFUSDT",
          "NEIROUSDT",
          "AVAXUSDT",
          "AIXBTUSDT",
          "BONKUSDT",
          "PNUTUSDT",
          "ANIMEUSDT",
          "RUNEUSDT"
        ],
        "candidate_count": 29,
        "filter_counts": {
          "missing_1h": 113,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 276,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-26",
        "decision_time_utc": "2025-01-26T00:00:00+00:00",
        "selected_symbols": [
          "RUNEUSDT",
          "LTCUSDT",
          "SOLUSDT",
          "AVAXUSDT",
          "TRUMPUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "HBARUSDT",
          "ENAUSDT",
          "PEPEUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "WIFUSDT",
          "TRXUSDT",
          "ANIMEUSDT",
          "LINKUSDT",
          "WLDUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 113,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 285,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-27",
        "decision_time_utc": "2025-01-27T00:00:00+00:00",
        "selected_symbols": [
          "SPELLUSDT",
          "SKLUSDT",
          "PENGUUSDT",
          "TAOUSDT",
          "LDOUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "TRUMPUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "BNBUSDT",
          "RUNEUSDT",
          "HBARUSDT",
          "LINKUSDT",
          "ENAUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "LTCUSDT",
          "VTHOUSDT",
          "AVAXUSDT",
          "WLDUSDT",
          "AIXBTUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 113,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 280,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-28",
        "decision_time_utc": "2025-01-28T00:00:00+00:00",
        "selected_symbols": [
          "ACHUSDT",
          "CFXUSDT",
          "TRUMPUSDT",
          "XRPUSDT",
          "BTCUSDT",
          "SUIUSDT",
          "MOVEUSDT",
          "TAOUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "ACTUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "LINKUSDT",
          "ALGOUSDT",
          "HBARUSDT",
          "ENAUSDT",
          "XLMUSDT",
          "LTCUSDT",
          "AVAXUSDT",
          "WLDUSDT",
          "WIFUSDT",
          "SPELLUSDT",
          "AIXBTUSDT",
          "AAVEUSDT",
          "PENGUUSDT",
          "RUNEUSDT",
          "APTUSDT",
          "BONKUSDT",
          "SHIBUSDT",
          "OPUSDT",
          "ARBUSDT",
          "NEARUSDT",
          "RAYUSDT",
          "DOTUSDT",
          "FLOKIUSDT",
          "FETUSDT"
        ],
        "candidate_count": 49,
        "filter_counts": {
          "missing_1h": 113,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 256,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-29",
        "decision_time_utc": "2025-01-29T00:00:00+00:00",
        "selected_symbols": [
          "SPELLUSDT",
          "MOVEUSDT",
          "BTCUSDT",
          "XRPUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "TRUMPUSDT",
          "DOGEUSDT",
          "TAOUSDT",
          "PEPEUSDT",
          "SUIUSDT",
          "WIFUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "LINKUSDT",
          "TRXUSDT",
          "WLDUSDT",
          "HBARUSDT",
          "ENAUSDT",
          "FLOKIUSDT",
          "ACHUSDT",
          "LTCUSDT",
          "RUNEUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "PENGUUSDT",
          "DUSDT"
        ],
        "candidate_count": 27,
        "filter_counts": {
          "missing_1h": 113,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 278,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-30",
        "decision_time_utc": "2025-01-30T00:00:00+00:00",
        "selected_symbols": [
          "SKLUSDT",
          "ACTUSDT",
          "ACHUSDT",
          "WIFUSDT",
          "PEPEUSDT",
          "PNUTUSDT",
          "FLOKIUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "WLDUSDT",
          "AIXBTUSDT",
          "LTCUSDT",
          "UNIUSDT",
          "LINKUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "HBARUSDT",
          "DOGEUSDT",
          "SOLUSDT",
          "ADAUSDT",
          "XRPUSDT",
          "APTUSDT",
          "SUIUSDT",
          "AAVEUSDT",
          "TRUMPUSDT",
          "AVAXUSDT",
          "MOVEUSDT",
          "BNBUSDT",
          "SHIBUSDT",
          "FETUSDT",
          "TRXUSDT",
          "TAOUSDT",
          "SPELLUSDT",
          "PENGUUSDT",
          "RUNEUSDT"
        ],
        "candidate_count": 35,
        "filter_counts": {
          "missing_1h": 113,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 270,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-31",
        "decision_time_utc": "2025-01-31T00:00:00+00:00",
        "selected_symbols": [
          "USUALUSDT",
          "JASMYUSDT",
          "ACHUSDT",
          "LTCUSDT",
          "SUIUSDT",
          "ENAUSDT",
          "XLMUSDT",
          "AAVEUSDT",
          "RUNEUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "BTCUSDT",
          "XRPUSDT",
          "LINKUSDT",
          "DOGEUSDT",
          "WLDUSDT",
          "AIXBTUSDT",
          "ADAUSDT",
          "HBARUSDT",
          "TRUMPUSDT",
          "BNBUSDT",
          "TAOUSDT",
          "WIFUSDT",
          "PENGUUSDT",
          "SPELLUSDT"
        ],
        "candidate_count": 27,
        "filter_counts": {
          "missing_1h": 113,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 278,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-01",
        "decision_time_utc": "2025-02-01T00:00:00+00:00",
        "selected_symbols": [
          "QTUMUSDT",
          "NEIROUSDT",
          "VTHOUSDT",
          "LDOUSDT",
          "PEPEUSDT",
          "SUSDT",
          "FLOKIUSDT",
          "AAVEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "LINKUSDT",
          "ACHUSDT",
          "DOTUSDT",
          "GALAUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "TRUMPUSDT",
          "ARBUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "TRXUSDT",
          "ENAUSDT",
          "JASMYUSDT",
          "WIFUSDT",
          "SHIBUSDT",
          "LTCUSDT",
          "PENGUUSDT",
          "BNBUSDT",
          "USUALUSDT",
          "ADAUSDT",
          "WLDUSDT",
          "AVAXUSDT",
          "HBARUSDT",
          "RUNEUSDT",
          "TAOUSDT",
          "APTUSDT",
          "UNIUSDT",
          "PNUTUSDT"
        ],
        "candidate_count": 38,
        "filter_counts": {
          "missing_1h": 113,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 267,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-02",
        "decision_time_utc": "2025-02-02T00:00:00+00:00",
        "selected_symbols": [
          "ARPAUSDT",
          "ACHUSDT",
          "VTHOUSDT",
          "QTUMUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "TRUMPUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "SUIUSDT",
          "LTCUSDT",
          "TRXUSDT",
          "BNBUSDT",
          "LINKUSDT",
          "PENGUUSDT",
          "WIFUSDT",
          "ENAUSDT",
          "NEIROUSDT",
          "ADAUSDT",
          "TAOUSDT",
          "ARBUSDT",
          "WLDUSDT",
          "HBARUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "LDOUSDT",
          "RUNEUSDT"
        ],
        "candidate_count": 30,
        "filter_counts": {
          "missing_1h": 113,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 275,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-03",
        "decision_time_utc": "2025-02-03T00:00:00+00:00",
        "selected_symbols": [
          "RUNEUSDT",
          "TRUMPUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "SUIUSDT",
          "TRXUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "LINKUSDT",
          "WIFUSDT",
          "LTCUSDT",
          "AVAXUSDT",
          "HBARUSDT",
          "ENAUSDT",
          "SHIBUSDT",
          "WLDUSDT",
          "TAOUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "LDOUSDT",
          "XLMUSDT",
          "FETUSDT",
          "NEARUSDT",
          "DOTUSDT",
          "USUALUSDT",
          "CRVUSDT",
          "NEIROUSDT",
          "ARBUSDT",
          "FILUSDT",
          "OPUSDT",
          "IOUSDT",
          "PENGUUSDT",
          "UNIUSDT",
          "PNUTUSDT",
          "FLOKIUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 53,
        "filter_counts": {
          "missing_1h": 113,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 252,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-04",
        "decision_time_utc": "2025-02-04T00:00:00+00:00",
        "selected_symbols": [
          "ACTUSDT",
          "ENAUSDT",
          "SOLUSDT",
          "MASKUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "SHIBUSDT",
          "LINKUSDT",
          "PENDLEUSDT",
          "RUNEUSDT",
          "APTUSDT",
          "ETHUSDT",
          "UNIUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "XLMUSDT",
          "USUALUSDT",
          "RAYUSDT",
          "TRXUSDT",
          "PNUTUSDT",
          "SANDUSDT",
          "SUIUSDT",
          "TRUMPUSDT",
          "PEPEUSDT",
          "BNBUSDT",
          "ALGOUSDT",
          "ICPUSDT",
          "FETUSDT",
          "TIAUSDT",
          "LTCUSDT",
          "DOTUSDT",
          "NEARUSDT",
          "INJUSDT",
          "BONKUSDT",
          "1000SATSUSDT",
          "POLUSDT",
          "SEIUSDT",
          "AIXBTUSDT",
          "LDOUSDT",
          "ATOMUSDT"
        ],
        "candidate_count": 71,
        "filter_counts": {
          "missing_1h": 113,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 234,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-05",
        "decision_time_utc": "2025-02-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "TRUMPUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "LINKUSDT",
          "ENAUSDT",
          "HBARUSDT",
          "WIFUSDT",
          "LTCUSDT",
          "RUNEUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "SHIBUSDT",
          "TAOUSDT",
          "APTUSDT",
          "ARBUSDT",
          "LDOUSDT",
          "WLDUSDT",
          "XLMUSDT",
          "DOTUSDT",
          "UNIUSDT",
          "NEARUSDT",
          "PNUTUSDT",
          "OPUSDT",
          "ACTUSDT",
          "ACHUSDT",
          "FLOKIUSDT",
          "AIXBTUSDT",
          "RAYUSDT",
          "NEIROUSDT",
          "FETUSDT",
          "ETHFIUSDT",
          "FILUSDT"
        ],
        "candidate_count": 42,
        "filter_counts": {
          "missing_1h": 113,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 263,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-06",
        "decision_time_utc": "2025-02-06T00:00:00+00:00",
        "selected_symbols": [
          "TRUMPUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "LTCUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "SUIUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "LINKUSDT",
          "ENAUSDT",
          "WIFUSDT",
          "HBARUSDT",
          "RUNEUSDT",
          "ACTUSDT",
          "AAVEUSDT",
          "SHIBUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "TAOUSDT",
          "LDOUSDT"
        ],
        "candidate_count": 24,
        "filter_counts": {
          "missing_1h": 113,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 281,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-07",
        "decision_time_utc": "2025-02-07T00:00:00+00:00",
        "selected_symbols": [
          "TRXUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "TRUMPUSDT",
          "SUIUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "PEPEUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "LTCUSDT",
          "LINKUSDT",
          "HBARUSDT",
          "WIFUSDT",
          "RUNEUSDT",
          "APTUSDT",
          "TAOUSDT",
          "USUALUSDT",
          "NEARUSDT",
          "AAVEUSDT",
          "SHIBUSDT",
          "AVAXUSDT",
          "LDOUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 112,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 280,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-08",
        "decision_time_utc": "2025-02-08T00:00:00+00:00",
        "selected_symbols": [
          "PENDLEUSDT",
          "USUALUSDT",
          "XRPUSDT",
          "ENAUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "HBARUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "LTCUSDT",
          "DOGEUSDT",
          "TRUMPUSDT",
          "PEPEUSDT",
          "BERAUSDT",
          "SHIBUSDT",
          "ADAUSDT",
          "TRXUSDT",
          "LINKUSDT",
          "APTUSDT",
          "WLDUSDT",
          "WIFUSDT",
          "AVAXUSDT",
          "RUNEUSDT",
          "TAOUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 26,
        "filter_counts": {
          "missing_1h": 112,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 279,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-09",
        "decision_time_utc": "2025-02-09T00:00:00+00:00",
        "selected_symbols": [
          "MEUSDT",
          "CAKEUSDT",
          "PEPEUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "SOLUSDT",
          "WIFUSDT",
          "TRUMPUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "LTCUSDT",
          "TRXUSDT",
          "BERAUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 112,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 289,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-10",
        "decision_time_utc": "2025-02-10T00:00:00+00:00",
        "selected_symbols": [
          "TAOUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "CAKEUSDT",
          "BNBUSDT",
          "LTCUSDT",
          "XRPUSDT",
          "TRUMPUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "MEUSDT",
          "BERAUSDT",
          "ENAUSDT",
          "LINKUSDT",
          "WIFUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 110,
          "insufficient_24h": 2,
          "reconstruct_error": 0,
          "low_quote_volume": 287,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-11",
        "decision_time_utc": "2025-02-11T00:00:00+00:00",
        "selected_symbols": [
          "LTCUSDT",
          "COOKIEUSDT",
          "RUNEUSDT",
          "SUIUSDT",
          "AIXBTUSDT",
          "TRXUSDT",
          "TAOUSDT",
          "APTUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "WLDUSDT",
          "LINKUSDT",
          "AVAXUSDT",
          "SOLUSDT",
          "WIFUSDT",
          "BERAUSDT",
          "TRUMPUSDT",
          "BNBUSDT",
          "PEPEUSDT",
          "HBARUSDT",
          "NEARUSDT",
          "ENAUSDT",
          "TSTUSDT"
        ],
        "candidate_count": 27,
        "filter_counts": {
          "missing_1h": 110,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 281,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-12",
        "decision_time_utc": "2025-02-12T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "BERAUSDT",
          "TAOUSDT",
          "CAKEUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "1000CHEEMSUSDT",
          "AIXBTUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "LTCUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "TRUMPUSDT",
          "TRXUSDT",
          "ENAUSDT",
          "PNUTUSDT",
          "LINKUSDT",
          "WIFUSDT",
          "HBARUSDT",
          "APTUSDT",
          "WLDUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "TSTUSDT"
        ],
        "candidate_count": 27,
        "filter_counts": {
          "missing_1h": 109,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 281,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-13",
        "decision_time_utc": "2025-02-13T00:00:00+00:00",
        "selected_symbols": [
          "CAKEUSDT",
          "THEUSDT",
          "SUSDT",
          "BNBUSDT",
          "LDOUSDT",
          "SUIUSDT",
          "DOTUSDT",
          "ETHUSDT",
          "SHIBUSDT",
          "RUNEUSDT",
          "NEARUSDT",
          "TSTUSDT",
          "PEPEUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "LTCUSDT",
          "AAVEUSDT",
          "LINKUSDT",
          "HBARUSDT",
          "WLDUSDT",
          "SOLUSDT",
          "ENAUSDT",
          "TRXUSDT",
          "TRUMPUSDT",
          "BERAUSDT",
          "WIFUSDT",
          "TAOUSDT",
          "PNUTUSDT",
          "AIXBTUSDT",
          "LAYERUSDT"
        ],
        "candidate_count": 34,
        "filter_counts": {
          "missing_1h": 109,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 275,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-14",
        "decision_time_utc": "2025-02-14T00:00:00+00:00",
        "selected_symbols": [
          "TRUMPUSDT",
          "XRPUSDT",
          "LTCUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "ADAUSDT",
          "CAKEUSDT",
          "SUIUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "THEUSDT",
          "ENAUSDT",
          "RUNEUSDT",
          "NOTUSDT",
          "SUSDT",
          "LAYERUSDT",
          "WIFUSDT",
          "PENGUUSDT",
          "TAOUSDT",
          "APTUSDT",
          "HBARUSDT",
          "TSTUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 108,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 284,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-15",
        "decision_time_utc": "2025-02-15T00:00:00+00:00",
        "selected_symbols": [
          "TRUMPUSDT",
          "WIFUSDT",
          "PNUTUSDT",
          "XRPUSDT",
          "ENAUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "LINKUSDT",
          "SUIUSDT",
          "XLMUSDT",
          "AVAXUSDT",
          "HBARUSDT",
          "TAOUSDT",
          "BNBUSDT",
          "LTCUSDT",
          "TSTUSDT",
          "CAKEUSDT",
          "ADAUSDT",
          "TRXUSDT",
          "JUVUSDT"
        ],
        "candidate_count": 23,
        "filter_counts": {
          "missing_1h": 108,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 287,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-16",
        "decision_time_utc": "2025-02-16T00:00:00+00:00",
        "selected_symbols": [
          "LTCUSDT",
          "CAKEUSDT",
          "XRPUSDT",
          "TRUMPUSDT",
          "BTCUSDT",
          "TRXUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "TSTUSDT",
          "PEPEUSDT",
          "WIFUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 108,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 295,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-17",
        "decision_time_utc": "2025-02-17T00:00:00+00:00",
        "selected_symbols": [
          "GLMUSDT",
          "CAKEUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "TRUMPUSDT",
          "TRXUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "LTCUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "PEPEUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 108,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 297,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-18",
        "decision_time_utc": "2025-02-18T00:00:00+00:00",
        "selected_symbols": [
          "SUSDT",
          "BERAUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "PEPEUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "LINKUSDT",
          "XRPUSDT",
          "TRUMPUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "LTCUSDT",
          "SUIUSDT",
          "TRXUSDT",
          "CAKEUSDT",
          "WIFUSDT",
          "ARKUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 108,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 290,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-19",
        "decision_time_utc": "2025-02-19T00:00:00+00:00",
        "selected_symbols": [
          "ACHUSDT",
          "LTCUSDT",
          "TAOUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "TRUMPUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "LINKUSDT",
          "SUSDT",
          "ENAUSDT",
          "TSTUSDT",
          "WIFUSDT",
          "CAKEUSDT",
          "AVAXUSDT",
          "WLDUSDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 108,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 288,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-20",
        "decision_time_utc": "2025-02-20T00:00:00+00:00",
        "selected_symbols": [
          "SUSDT",
          "APTUSDT",
          "TAOUSDT",
          "CAKEUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "BERAUSDT",
          "LTCUSDT",
          "TRUMPUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "HBARUSDT",
          "ADAUSDT",
          "FLOKIUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "PEPEUSDT",
          "ENAUSDT",
          "TSTUSDT"
        ],
        "candidate_count": 21,
        "filter_counts": {
          "missing_1h": 108,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 289,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-21",
        "decision_time_utc": "2025-02-21T00:00:00+00:00",
        "selected_symbols": [
          "BERAUSDT",
          "SUSDT",
          "TIAUSDT",
          "TSTUSDT",
          "SEIUSDT",
          "TAOUSDT",
          "NEARUSDT",
          "SUIUSDT",
          "SOLUSDT",
          "ENAUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "ETHUSDT",
          "PEPEUSDT",
          "HBARUSDT",
          "XRPUSDT",
          "TRXUSDT",
          "FLOKIUSDT",
          "TRUMPUSDT",
          "LTCUSDT",
          "BNBUSDT",
          "CAKEUSDT",
          "DOGEUSDT",
          "APTUSDT"
        ],
        "candidate_count": 24,
        "filter_counts": {
          "missing_1h": 107,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 286,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-22",
        "decision_time_utc": "2025-02-22T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "JTOUSDT",
          "SOLUSDT",
          "AIXBTUSDT",
          "XRPUSDT",
          "LTCUSDT",
          "DOGEUSDT",
          "SUSDT",
          "SUIUSDT",
          "TRUMPUSDT",
          "BNBUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "NEIROUSDT",
          "BERAUSDT",
          "WIFUSDT",
          "TAOUSDT",
          "AVAXUSDT",
          "TSTUSDT",
          "LINKUSDT",
          "APTUSDT",
          "WLDUSDT",
          "DOTUSDT",
          "SEIUSDT",
          "HBARUSDT",
          "CAKEUSDT",
          "AAVEUSDT",
          "RUNEUSDT",
          "LDOUSDT",
          "UNIUSDT",
          "NEARUSDT",
          "ARKMUSDT",
          "KAITOUSDT"
        ],
        "candidate_count": 36,
        "filter_counts": {
          "missing_1h": 107,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 275,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-23",
        "decision_time_utc": "2025-02-23T00:00:00+00:00",
        "selected_symbols": [
          "TSTUSDT",
          "PNUTUSDT",
          "RUNEUSDT",
          "NEIROUSDT",
          "WIFUSDT",
          "SEIUSDT",
          "KAITOUSDT",
          "ETHUSDT",
          "PEPEUSDT",
          "SUIUSDT",
          "AVAXUSDT",
          "TRUMPUSDT",
          "BNBUSDT",
          "CAKEUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "XRPUSDT",
          "ADAUSDT",
          "SUSDT",
          "LTCUSDT",
          "TRXUSDT",
          "BERAUSDT",
          "ENAUSDT",
          "TAOUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 107,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 286,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-24",
        "decision_time_utc": "2025-02-24T00:00:00+00:00",
        "selected_symbols": [
          "GLMUSDT",
          "SUSDT",
          "ETHUSDT",
          "RUNEUSDT",
          "LTCUSDT",
          "TRXUSDT",
          "BTCUSDT",
          "KAITOUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "PNUTUSDT",
          "PEPEUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "TSTUSDT",
          "DOGEUSDT",
          "TRUMPUSDT",
          "ENAUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 107,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 292,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-25",
        "decision_time_utc": "2025-02-25T00:00:00+00:00",
        "selected_symbols": [
          "VANAUSDT",
          "KAITOUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "TRUMPUSDT",
          "BNBUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "SUSDT",
          "RUNEUSDT",
          "LTCUSDT",
          "HBARUSDT",
          "ADAUSDT",
          "TAOUSDT",
          "ENAUSDT",
          "WIFUSDT",
          "SEIUSDT",
          "LINKUSDT",
          "BERAUSDT",
          "TSTUSDT",
          "AVAXUSDT",
          "WLDUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "PNUTUSDT",
          "SHIBUSDT",
          "RAYUSDT"
        ],
        "candidate_count": 31,
        "filter_counts": {
          "missing_1h": 107,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 280,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-26",
        "decision_time_utc": "2025-02-26T00:00:00+00:00",
        "selected_symbols": [
          "PNUTUSDT",
          "ACTUSDT",
          "VANAUSDT",
          "ENAUSDT",
          "RUNEUSDT",
          "TSTUSDT",
          "COWUSDT",
          "OPUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "XRPUSDT",
          "DOTUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "APTUSDT",
          "UNIUSDT",
          "ETHUSDT",
          "WLDUSDT",
          "TRUMPUSDT",
          "SEIUSDT",
          "BNBUSDT",
          "SHIBUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "KAITOUSDT",
          "HBARUSDT",
          "ARBUSDT",
          "ADAUSDT",
          "LTCUSDT",
          "SUSDT",
          "LINKUSDT",
          "AVAXUSDT",
          "TAOUSDT",
          "WIFUSDT",
          "AAVEUSDT",
          "RAYUSDT",
          "NEARUSDT",
          "BERAUSDT",
          "XLMUSDT",
          "FETUSDT"
        ],
        "candidate_count": 40,
        "filter_counts": {
          "missing_1h": 107,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 271,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-27",
        "decision_time_utc": "2025-02-27T00:00:00+00:00",
        "selected_symbols": [
          "KAITOUSDT",
          "PNUTUSDT",
          "TSTUSDT",
          "LTCUSDT",
          "RUNEUSDT",
          "BERAUSDT",
          "ACTUSDT",
          "WIFUSDT",
          "ENAUSDT",
          "TIAUSDT",
          "APTUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "DOTUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "TRUMPUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "VANAUSDT",
          "SUSDT",
          "ADAUSDT",
          "TAOUSDT",
          "HBARUSDT",
          "LINKUSDT",
          "AVAXUSDT",
          "SEIUSDT",
          "AAVEUSDT",
          "UNIUSDT",
          "RAYUSDT"
        ],
        "candidate_count": 33,
        "filter_counts": {
          "missing_1h": 107,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 278,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-28",
        "decision_time_utc": "2025-02-28T00:00:00+00:00",
        "selected_symbols": [
          "BERAUSDT",
          "BTCUSDT",
          "APTUSDT",
          "SOLUSDT",
          "DOTUSDT",
          "WLDUSDT",
          "ETHUSDT",
          "LTCUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "HBARUSDT",
          "KAITOUSDT",
          "SUIUSDT",
          "RUNEUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "PEPEUSDT",
          "TRUMPUSDT",
          "WIFUSDT",
          "TSTUSDT",
          "PNUTUSDT",
          "SUSDT",
          "ADAUSDT",
          "TAOUSDT",
          "ENAUSDT",
          "LINKUSDT"
        ],
        "candidate_count": 27,
        "filter_counts": {
          "missing_1h": 106,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 284,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-01",
        "decision_time_utc": "2025-03-01T00:00:00+00:00",
        "selected_symbols": [
          "PNUTUSDT",
          "CKBUSDT",
          "SOLUSDT",
          "WIFUSDT",
          "ACTUSDT",
          "BERAUSDT",
          "HBARUSDT",
          "VANAUSDT",
          "APTUSDT",
          "NEIROUSDT",
          "BTCUSDT",
          "TRUMPUSDT",
          "RUNEUSDT",
          "ETHUSDT",
          "TRXUSDT",
          "SUIUSDT",
          "XRPUSDT",
          "LTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "PEPEUSDT",
          "KAITOUSDT",
          "ADAUSDT",
          "SUSDT",
          "AVAXUSDT",
          "LINKUSDT",
          "SHELLUSDT",
          "TAOUSDT",
          "WLDUSDT",
          "NEARUSDT",
          "ENAUSDT",
          "DOTUSDT",
          "SHIBUSDT",
          "TSTUSDT",
          "AAVEUSDT",
          "UNIUSDT",
          "WBTCUSDT"
        ],
        "candidate_count": 37,
        "filter_counts": {
          "missing_1h": 105,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 275,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-02",
        "decision_time_utc": "2025-03-02T00:00:00+00:00",
        "selected_symbols": [
          "HBARUSDT",
          "KAITOUSDT",
          "SUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "XRPUSDT",
          "TRUMPUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "PNUTUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "LTCUSDT",
          "RUNEUSDT",
          "SHELLUSDT",
          "WIFUSDT",
          "NEIROUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 105,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 293,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-03",
        "decision_time_utc": "2025-03-03T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "XRPUSDT",
          "TRUMPUSDT",
          "SOLUSDT",
          "WIFUSDT",
          "RAYUSDT",
          "ENAUSDT",
          "LINKUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "ETHUSDT",
          "ALGOUSDT",
          "SUIUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "XLMUSDT",
          "RUNEUSDT",
          "DOTUSDT",
          "SHIBUSDT",
          "WLDUSDT",
          "NEARUSDT",
          "PNUTUSDT",
          "APTUSDT",
          "HBARUSDT",
          "TRXUSDT",
          "TAOUSDT",
          "NEIROUSDT",
          "LTCUSDT",
          "BNBUSDT",
          "SUSDT",
          "BERAUSDT",
          "ACTUSDT",
          "KAITOUSDT",
          "SHELLUSDT"
        ],
        "candidate_count": 35,
        "filter_counts": {
          "missing_1h": 105,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 278,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-04",
        "decision_time_utc": "2025-03-04T00:00:00+00:00",
        "selected_symbols": [
          "LAYERUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "TRUMPUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "LTCUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "HBARUSDT",
          "WIFUSDT",
          "PNUTUSDT",
          "RUNEUSDT",
          "LINKUSDT",
          "AVAXUSDT",
          "KAITOUSDT",
          "ENAUSDT",
          "SUSDT",
          "XLMUSDT",
          "BCHUSDT",
          "WLDUSDT",
          "NEARUSDT",
          "SHIBUSDT",
          "TAOUSDT",
          "DOTUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "BERAUSDT",
          "ARBUSDT",
          "REDUSDT"
        ],
        "candidate_count": 34,
        "filter_counts": {
          "missing_1h": 105,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 279,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-05",
        "decision_time_utc": "2025-03-05T00:00:00+00:00",
        "selected_symbols": [
          "AAVEUSDT",
          "SOLVUSDT",
          "ADAUSDT",
          "HBARUSDT",
          "PNUTUSDT",
          "TRXUSDT",
          "XRPUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "LINKUSDT",
          "TRUMPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "SHIBUSDT",
          "LTCUSDT",
          "WIFUSDT",
          "AVAXUSDT",
          "SUSDT",
          "WLDUSDT",
          "KAITOUSDT",
          "NEARUSDT",
          "RUNEUSDT",
          "TAOUSDT",
          "APTUSDT",
          "DOTUSDT",
          "BERAUSDT",
          "UNIUSDT",
          "OPUSDT",
          "ARBUSDT",
          "LAYERUSDT"
        ],
        "candidate_count": 34,
        "filter_counts": {
          "missing_1h": 104,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 279,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-06",
        "decision_time_utc": "2025-03-06T00:00:00+00:00",
        "selected_symbols": [
          "BCHUSDT",
          "APTUSDT",
          "LINKUSDT",
          "KAITOUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "SUIUSDT",
          "SUSDT",
          "BERAUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "TAOUSDT",
          "HBARUSDT",
          "SOLUSDT",
          "TRUMPUSDT",
          "BNBUSDT",
          "WLDUSDT",
          "PEPEUSDT",
          "WIFUSDT",
          "LTCUSDT",
          "TRXUSDT",
          "ENAUSDT",
          "PNUTUSDT"
        ],
        "candidate_count": 27,
        "filter_counts": {
          "missing_1h": 104,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 287,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-07",
        "decision_time_utc": "2025-03-07T00:00:00+00:00",
        "selected_symbols": [
          "REZUSDT",
          "ENAUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "LINKUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "NEARUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "TRUMPUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "LTCUSDT",
          "PEPEUSDT",
          "AAVEUSDT",
          "TRXUSDT",
          "AVAXUSDT",
          "HBARUSDT",
          "SUSDT",
          "WIFUSDT",
          "PNUTUSDT",
          "KAITOUSDT",
          "REDUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 104,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 289,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-08",
        "decision_time_utc": "2025-03-08T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "PEPEUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "ADAUSDT",
          "TRXUSDT",
          "SUIUSDT",
          "TRUMPUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "LINKUSDT",
          "LTCUSDT",
          "HBARUSDT",
          "AVAXUSDT",
          "WIFUSDT",
          "NEARUSDT",
          "AAVEUSDT",
          "REDUSDT",
          "PNUTUSDT",
          "SUSDT",
          "BCHUSDT",
          "REZUSDT",
          "RUNEUSDT",
          "DOTUSDT",
          "GPSUSDT"
        ],
        "candidate_count": 27,
        "filter_counts": {
          "missing_1h": 104,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 287,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-09",
        "decision_time_utc": "2025-03-09T00:00:00+00:00",
        "selected_symbols": [
          "KAITOUSDT",
          "RUNEUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "ADAUSDT",
          "TRXUSDT",
          "DOGEUSDT",
          "TRUMPUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "BNBUSDT",
          "LTCUSDT",
          "PNUTUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 104,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 298,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-10",
        "decision_time_utc": "2025-03-10T00:00:00+00:00",
        "selected_symbols": [
          "RAREUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "TRUMPUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "LTCUSDT",
          "ENAUSDT",
          "WIFUSDT",
          "HBARUSDT",
          "LINKUSDT",
          "RUNEUSDT",
          "SUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 104,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 294,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-11",
        "decision_time_utc": "2025-03-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "PEPEUSDT",
          "SUIUSDT",
          "TRXUSDT",
          "ENAUSDT",
          "TRUMPUSDT",
          "LTCUSDT",
          "RUNEUSDT",
          "LINKUSDT",
          "AVAXUSDT",
          "HBARUSDT",
          "WIFUSDT",
          "SUSDT",
          "TAOUSDT",
          "NEARUSDT",
          "SHIBUSDT",
          "PNUTUSDT",
          "RAREUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 104,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 289,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-12",
        "decision_time_utc": "2025-03-12T00:00:00+00:00",
        "selected_symbols": [
          "AUCTIONUSDT",
          "TAOUSDT",
          "PEPEUSDT",
          "RUNEUSDT",
          "XRPUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "SOLUSDT",
          "AVAXUSDT",
          "SUIUSDT",
          "NEARUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "PNUTUSDT",
          "WLDUSDT",
          "RAREUSDT",
          "WIFUSDT",
          "HBARUSDT",
          "LINKUSDT",
          "SHIBUSDT",
          "LTCUSDT",
          "TRUMPUSDT",
          "AAVEUSDT",
          "TRXUSDT",
          "ENAUSDT",
          "SUSDT",
          "RADUSDT",
          "ARKMUSDT"
        ],
        "candidate_count": 29,
        "filter_counts": {
          "missing_1h": 104,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 285,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-13",
        "decision_time_utc": "2025-03-13T00:00:00+00:00",
        "selected_symbols": [
          "VICUSDT",
          "REDUSDT",
          "TIAUSDT",
          "PEPEUSDT",
          "AVAXUSDT",
          "WIFUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "LINKUSDT",
          "ADAUSDT",
          "HBARUSDT",
          "TRUMPUSDT",
          "LTCUSDT",
          "TRXUSDT",
          "AAVEUSDT",
          "ENAUSDT",
          "RAREUSDT",
          "TAOUSDT"
        ],
        "candidate_count": 23,
        "filter_counts": {
          "missing_1h": 104,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 291,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-14",
        "decision_time_utc": "2025-03-14T00:00:00+00:00",
        "selected_symbols": [
          "LAYERUSDT",
          "SUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "PNUTUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "TRUMPUSDT",
          "SOLUSDT",
          "TRXUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "SUIUSDT",
          "WIFUSDT",
          "HBARUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "LTCUSDT",
          "LINKUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 21,
        "filter_counts": {
          "missing_1h": 103,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 293,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-15",
        "decision_time_utc": "2025-03-15T00:00:00+00:00",
        "selected_symbols": [
          "RAREUSDT",
          "PNUTUSDT",
          "TRUMPUSDT",
          "SOLUSDT",
          "SUSDT",
          "SUIUSDT",
          "WIFUSDT",
          "BTCUSDT",
          "XRPUSDT",
          "PEPEUSDT",
          "LINKUSDT",
          "ADAUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "NEARUSDT",
          "HBARUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 103,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 296,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-16",
        "decision_time_utc": "2025-03-16T00:00:00+00:00",
        "selected_symbols": [
          "REDUSDT",
          "TONUSDT",
          "NOTUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "BTCUSDT",
          "XRPUSDT",
          "ETHUSDT",
          "TRUMPUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "PEPEUSDT",
          "SUIUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 103,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 300,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-17",
        "decision_time_utc": "2025-03-17T00:00:00+00:00",
        "selected_symbols": [
          "AUCTIONUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "TRUMPUSDT",
          "TRXUSDT",
          "SUIUSDT",
          "REDUSDT",
          "SUSDT",
          "TONUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 103,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 300,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-18",
        "decision_time_utc": "2025-03-18T00:00:00+00:00",
        "selected_symbols": [
          "CAKEUSDT",
          "PEPEUSDT",
          "TSTUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "TRXUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "LTCUSDT",
          "TRUMPUSDT",
          "ADAUSDT",
          "SUSDT",
          "AUCTIONUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 103,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 298,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-19",
        "decision_time_utc": "2025-03-19T00:00:00+00:00",
        "selected_symbols": [
          "AUCTIONUSDT",
          "TRXUSDT",
          "CAKEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "TRUMPUSDT",
          "API3USDT",
          "TSTUSDT",
          "LTCUSDT",
          "SUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 102,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 298,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-20",
        "decision_time_utc": "2025-03-20T00:00:00+00:00",
        "selected_symbols": [
          "XRPUSDT",
          "SUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "UNIUSDT",
          "SUIUSDT",
          "BTCUSDT",
          "LINKUSDT",
          "NEARUSDT",
          "WIFUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AUCTIONUSDT",
          "TRUMPUSDT",
          "HBARUSDT",
          "LTCUSDT",
          "AVAXUSDT",
          "PEPEUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "CAKEUSDT",
          "BMTUSDT"
        ],
        "candidate_count": 23,
        "filter_counts": {
          "missing_1h": 100,
          "insufficient_24h": 2,
          "reconstruct_error": 0,
          "low_quote_volume": 293,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-21",
        "decision_time_utc": "2025-03-21T00:00:00+00:00",
        "selected_symbols": [
          "AUCTIONUSDT",
          "BNBUSDT",
          "PEPEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "TRXUSDT",
          "SOLUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "TRUMPUSDT",
          "CAKEUSDT",
          "LTCUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 100,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 304,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-22",
        "decision_time_utc": "2025-03-22T00:00:00+00:00",
        "selected_symbols": [
          "ORCAUSDT",
          "ZROUSDT",
          "CAKEUSDT",
          "LAYERUSDT",
          "AUCTIONUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "PEPEUSDT",
          "SUIUSDT",
          "TRXUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "TRUMPUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 100,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 302,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-23",
        "decision_time_utc": "2025-03-23T00:00:00+00:00",
        "selected_symbols": [
          "API3USDT",
          "PNUTUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "CAKEUSDT",
          "TRXUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "ORCAUSDT",
          "PEPEUSDT",
          "SUIUSDT",
          "TRUMPUSDT",
          "ACXUSDT",
          "AUCTIONUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 100,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 303,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-24",
        "decision_time_utc": "2025-03-24T00:00:00+00:00",
        "selected_symbols": [
          "PNUTUSDT",
          "WUSDT",
          "TRUMPUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "PEPEUSDT",
          "XRPUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "AUCTIONUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 100,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 304,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-25",
        "decision_time_utc": "2025-03-25T00:00:00+00:00",
        "selected_symbols": [
          "FORMUSDT",
          "BERAUSDT",
          "SUSDT",
          "ENAUSDT",
          "PEPEUSDT",
          "WLDUSDT",
          "SOLUSDT",
          "AVAXUSDT",
          "WIFUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SUIUSDT",
          "LINKUSDT",
          "TRUMPUSDT",
          "ADAUSDT",
          "AUCTIONUSDT",
          "BNBUSDT",
          "LTCUSDT",
          "XRPUSDT",
          "TRXUSDT",
          "PNUTUSDT",
          "CAKEUSDT"
        ],
        "candidate_count": 23,
        "filter_counts": {
          "missing_1h": 99,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 295,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-26",
        "decision_time_utc": "2025-03-26T00:00:00+00:00",
        "selected_symbols": [
          "MOVEUSDT",
          "LAYERUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "SOLUSDT",
          "ENAUSDT",
          "BTCUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "SUSDT",
          "PEPEUSDT",
          "TRUMPUSDT",
          "PNUTUSDT",
          "TRXUSDT",
          "NILUSDT",
          "1000SATSUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 98,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 300,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-27",
        "decision_time_utc": "2025-03-27T00:00:00+00:00",
        "selected_symbols": [
          "PEPEUSDT",
          "SUIUSDT",
          "PARTIUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "SHIBUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "TRXUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "TRUMPUSDT",
          "1000SATSUSDT",
          "CAKEUSDT",
          "WIFUSDT",
          "ENAUSDT",
          "SUSDT",
          "PNUTUSDT",
          "LTCUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 98,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 300,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-28",
        "decision_time_utc": "2025-03-28T00:00:00+00:00",
        "selected_symbols": [
          "NILUSDT",
          "BERAUSDT",
          "TONUSDT",
          "SUIUSDT",
          "ORCAUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "CAKEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "TRXUSDT",
          "XRPUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "TRUMPUSDT",
          "PARTIUSDT",
          "1000SATSUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 94,
          "insufficient_24h": 4,
          "reconstruct_error": 0,
          "low_quote_volume": 301,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-29",
        "decision_time_utc": "2025-03-29T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "ADAUSDT",
          "TRUMPUSDT",
          "TRXUSDT",
          "TONUSDT",
          "LTCUSDT",
          "BERAUSDT",
          "LINKUSDT",
          "SUSDT",
          "TUTUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 94,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 307,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-30",
        "decision_time_utc": "2025-03-30T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "MUBARAKUSDT",
          "TRUMPUSDT",
          "BERAUSDT",
          "TUTUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 94,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 310,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-31",
        "decision_time_utc": "2025-03-31T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SUIUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "MUBARAKUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 94,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 314,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-01",
        "decision_time_utc": "2025-04-01T00:00:00+00:00",
        "selected_symbols": [
          "TONUSDT",
          "PEPEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "TRXUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "TRUMPUSDT",
          "LTCUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 93,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 311,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-02",
        "decision_time_utc": "2025-04-02T00:00:00+00:00",
        "selected_symbols": [
          "PEPEUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "SUIUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "TRUMPUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "PNUTUSDT",
          "TRXUSDT",
          "TONUSDT",
          "GUNUSDT",
          "COMPUSDT",
          "MASKUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 93,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 307,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-03",
        "decision_time_utc": "2025-04-03T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "TRUMPUSDT",
          "ADAUSDT",
          "TRXUSDT",
          "LINKUSDT",
          "AVAXUSDT",
          "GUNUSDT",
          "ENAUSDT",
          "LTCUSDT",
          "PNUTUSDT",
          "WIFUSDT",
          "SUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 93,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 305,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-04",
        "decision_time_utc": "2025-04-04T00:00:00+00:00",
        "selected_symbols": [
          "RAREUSDT",
          "ACTUSDT",
          "BTCUSDT",
          "XRPUSDT",
          "ETHUSDT",
          "TRUMPUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "LINKUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 93,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 310,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-05",
        "decision_time_utc": "2025-04-05T00:00:00+00:00",
        "selected_symbols": [
          "PEPEUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "BTCUSDT",
          "SUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "FILUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "ENAUSDT",
          "TRXUSDT",
          "LINKUSDT",
          "TRUMPUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 93,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 310,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-06",
        "decision_time_utc": "2025-04-06T00:00:00+00:00",
        "selected_symbols": [
          "GUNUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "PEPEUSDT",
          "SUIUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 93,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 316,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-07",
        "decision_time_utc": "2025-04-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "GUNUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "TRUMPUSDT",
          "TRXUSDT",
          "LTCUSDT",
          "LINKUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 93,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 310,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-08",
        "decision_time_utc": "2025-04-08T00:00:00+00:00",
        "selected_symbols": [
          "TAOUSDT",
          "HBARUSDT",
          "SUIUSDT",
          "TONUSDT",
          "ENAUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "PEPEUSDT",
          "ADAUSDT",
          "XRPUSDT",
          "AAVEUSDT",
          "DOGEUSDT",
          "LINKUSDT",
          "BNBUSDT",
          "LTCUSDT",
          "TRXUSDT",
          "SHIBUSDT",
          "TRUMPUSDT",
          "SUSDT",
          "NEARUSDT",
          "GUNUSDT",
          "BERAUSDT",
          "DOTUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 93,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 300,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-09",
        "decision_time_utc": "2025-04-09T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "TRXUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "TRUMPUSDT",
          "HBARUSDT",
          "LTCUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 93,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 311,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-10",
        "decision_time_utc": "2025-04-10T00:00:00+00:00",
        "selected_symbols": [
          "SUSDT",
          "PENDLEUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "LINKUSDT",
          "HBARUSDT",
          "SOLUSDT",
          "ENAUSDT",
          "CRVUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "NEARUSDT",
          "LTCUSDT",
          "TRUMPUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "BERAUSDT"
        ],
        "candidate_count": 21,
        "filter_counts": {
          "missing_1h": 93,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 304,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-11",
        "decision_time_utc": "2025-04-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "PEPEUSDT",
          "ADAUSDT",
          "TRUMPUSDT",
          "ENAUSDT",
          "HBARUSDT",
          "LINKUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 92,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 311,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-12",
        "decision_time_utc": "2025-04-12T00:00:00+00:00",
        "selected_symbols": [
          "ORCAUSDT",
          "BABYUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "CRVUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "AVAXUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "TRUMPUSDT",
          "HBARUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 89,
          "insufficient_24h": 3,
          "reconstruct_error": 0,
          "low_quote_volume": 310,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-13",
        "decision_time_utc": "2025-04-13T00:00:00+00:00",
        "selected_symbols": [
          "JASMYUSDT",
          "BABYUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "TRUMPUSDT",
          "PEPEUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "GUNUSDT",
          "ORCAUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 89,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 313,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-14",
        "decision_time_utc": "2025-04-14T00:00:00+00:00",
        "selected_symbols": [
          "TRXUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "BABYUSDT",
          "BNBUSDT",
          "TRUMPUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 89,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 317,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-15",
        "decision_time_utc": "2025-04-15T00:00:00+00:00",
        "selected_symbols": [
          "VTHOUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "AVAXUSDT",
          "XRPUSDT",
          "PEPEUSDT",
          "SUIUSDT",
          "TRXUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "TRUMPUSDT",
          "BABYUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 88,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 314,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-16",
        "decision_time_utc": "2025-04-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "TRUMPUSDT",
          "KERNELUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 87,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 318,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-17",
        "decision_time_utc": "2025-04-17T00:00:00+00:00",
        "selected_symbols": [
          "KERNELUSDT",
          "CRVUSDT",
          "WCTUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "PEPEUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "TRUMPUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 87,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 317,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-18",
        "decision_time_utc": "2025-04-18T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "SUIUSDT",
          "ETHUSDT",
          "PEPEUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "TRXUSDT",
          "DOGEUSDT",
          "TRUMPUSDT",
          "WCTUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 87,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 320,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-19",
        "decision_time_utc": "2025-04-19T00:00:00+00:00",
        "selected_symbols": [
          "MEMEUSDT",
          "TUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "PEPEUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "SUIUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 87,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 320,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-20",
        "decision_time_utc": "2025-04-20T00:00:00+00:00",
        "selected_symbols": [
          "HIGHUSDT",
          "GMTUSDT",
          "TRUMPUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "PEPEUSDT",
          "XRPUSDT",
          "TRXUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "MEMEUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 87,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 318,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-21",
        "decision_time_utc": "2025-04-21T00:00:00+00:00",
        "selected_symbols": [
          "MAGICUSDT",
          "TAOUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "PEPEUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "WCTUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "TRUMPUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 87,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 318,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-22",
        "decision_time_utc": "2025-04-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SUIUSDT",
          "ENJUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "MAGICUSDT",
          "TRXUSDT",
          "TRUMPUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "TAOUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 87,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 317,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-23",
        "decision_time_utc": "2025-04-23T00:00:00+00:00",
        "selected_symbols": [
          "SUIUSDT",
          "CRVUSDT",
          "PEPEUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "TRUMPUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "XRPUSDT",
          "TAOUSDT",
          "LINKUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "MAGICUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 86,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 315,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-24",
        "decision_time_utc": "2025-04-24T00:00:00+00:00",
        "selected_symbols": [
          "TURBOUSDT",
          "TRUMPUSDT",
          "SUIUSDT",
          "PNUTUSDT",
          "WIFUSDT",
          "LINKUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "ADAUSDT",
          "XRPUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "TRXUSDT",
          "TAOUSDT",
          "LTCUSDT",
          "BONKUSDT",
          "ACTUSDT",
          "HYPERUSDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 86,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 310,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-25",
        "decision_time_utc": "2025-04-25T00:00:00+00:00",
        "selected_symbols": [
          "SUIUSDT",
          "ONDOUSDT",
          "TAOUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "WIFUSDT",
          "XRPUSDT",
          "TRUMPUSDT",
          "PEPEUSDT",
          "BNBUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 85,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 318,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-26",
        "decision_time_utc": "2025-04-26T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "PENGUUSDT",
          "WIFUSDT",
          "WLDUSDT",
          "INITUSDT",
          "TRUMPUSDT",
          "SUIUSDT",
          "BTCUSDT",
          "PEPEUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "ENAUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "TRXUSDT",
          "LINKUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 85,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 314,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-27",
        "decision_time_utc": "2025-04-27T00:00:00+00:00",
        "selected_symbols": [
          "TURBOUSDT",
          "VIRTUALUSDT",
          "TRUMPUSDT",
          "WLDUSDT",
          "INITUSDT",
          "TRXUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "PEPEUSDT",
          "WIFUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "LAYERUSDT",
          "BONKUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 85,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 315,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-28",
        "decision_time_utc": "2025-04-28T00:00:00+00:00",
        "selected_symbols": [
          "PENGUUSDT",
          "JSTUSDT",
          "XRPUSDT",
          "BTCUSDT",
          "SUIUSDT",
          "ETHUSDT",
          "TRUMPUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "BONKUSDT",
          "TRXUSDT",
          "PEPEUSDT",
          "BNBUSDT",
          "WLDUSDT",
          "ADAUSDT",
          "INITUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 85,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 317,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-29",
        "decision_time_utc": "2025-04-29T00:00:00+00:00",
        "selected_symbols": [
          "VIRTUALUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "TAOUSDT",
          "XRPUSDT",
          "ETHUSDT",
          "PEPEUSDT",
          "SOLUSDT",
          "SUIUSDT",
          "TRUMPUSDT",
          "TRXUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "WIFUSDT",
          "PENGUUSDT",
          "AVAXUSDT",
          "WLDUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 84,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 315,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-30",
        "decision_time_utc": "2025-04-30T00:00:00+00:00",
        "selected_symbols": [
          "INITUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "SUIUSDT",
          "XRPUSDT",
          "TRUMPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "BONKUSDT",
          "VIRTUALUSDT",
          "SIGNUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 84,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 319,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-01",
        "decision_time_utc": "2025-05-01T00:00:00+00:00",
        "selected_symbols": [
          "VIRTUALUSDT",
          "PUNDIXUSDT",
          "WLDUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "TRUMPUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "TRXUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "SIGNUSDT",
          "BONKUSDT",
          "LAYERUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 84,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 317,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-02",
        "decision_time_utc": "2025-05-02T00:00:00+00:00",
        "selected_symbols": [
          "AIXBTUSDT",
          "SUSDT",
          "VIRTUALUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "ADAUSDT",
          "SUIUSDT",
          "XRPUSDT",
          "TRUMPUSDT",
          "PEPEUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "WLDUSDT",
          "TRXUSDT",
          "MOVEUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 84,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 317,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-03",
        "decision_time_utc": "2025-05-03T00:00:00+00:00",
        "selected_symbols": [
          "TURBOUSDT",
          "VIRTUALUSDT",
          "TRUMPUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "SUSDT",
          "SUIUSDT",
          "XRPUSDT",
          "TRXUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 83,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 320,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-04",
        "decision_time_utc": "2025-05-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "TRUMPUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "XRPUSDT",
          "STOUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 83,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 323,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-05",
        "decision_time_utc": "2025-05-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "SUIUSDT",
          "XRPUSDT",
          "TRXUSDT",
          "TRUMPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "ADAUSDT",
          "VIRTUALUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 83,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 323,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-06",
        "decision_time_utc": "2025-05-06T00:00:00+00:00",
        "selected_symbols": [
          "PARTIUSDT",
          "SUIUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "TRUMPUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "VIRTUALUSDT",
          "TRXUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "LTCUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 83,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 321,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-07",
        "decision_time_utc": "2025-05-07T00:00:00+00:00",
        "selected_symbols": [
          "LTCUSDT",
          "BTCUSDT",
          "PENGUUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "ADAUSDT",
          "SOLUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "TURBOUSDT",
          "PEPEUSDT",
          "TRUMPUSDT",
          "VIRTUALUSDT",
          "TRXUSDT",
          "LAYERUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 82,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 319,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-08",
        "decision_time_utc": "2025-05-08T00:00:00+00:00",
        "selected_symbols": [
          "KAITOUSDT",
          "PEPEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "SUIUSDT",
          "XRPUSDT",
          "TRXUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "TRUMPUSDT",
          "LTCUSDT",
          "ADAUSDT",
          "VIRTUALUSDT",
          "PENGUUSDT",
          "LAYERUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 82,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 320,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-09",
        "decision_time_utc": "2025-05-09T00:00:00+00:00",
        "selected_symbols": [
          "VIRTUALUSDT",
          "PNUTUSDT",
          "PEPEUSDT",
          "ENAUSDT",
          "PENGUUSDT",
          "ETHUSDT",
          "UNIUSDT",
          "SUIUSDT",
          "WIFUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "DOGEUSDT",
          "TRUMPUSDT",
          "ADAUSDT",
          "TAOUSDT",
          "LINKUSDT",
          "SOLUSDT",
          "IOUSDT",
          "WLDUSDT",
          "AVAXUSDT",
          "TIAUSDT",
          "XRPUSDT",
          "BTCUSDT",
          "BCHUSDT",
          "LTCUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "LAYERUSDT",
          "KAITOUSDT"
        ],
        "candidate_count": 29,
        "filter_counts": {
          "missing_1h": 81,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 307,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-10",
        "decision_time_utc": "2025-05-10T00:00:00+00:00",
        "selected_symbols": [
          "MUBARAKUSDT",
          "PNUTUSDT",
          "NEIROUSDT",
          "PEOPLEUSDT",
          "TRUMPUSDT",
          "PEPEUSDT",
          "TIAUSDT",
          "ETHUSDT",
          "BONKUSDT",
          "EIGENUSDT",
          "WIFUSDT",
          "ENAUSDT",
          "FLOKIUSDT",
          "SOLUSDT",
          "BERAUSDT",
          "BNBUSDT",
          "DOTUSDT",
          "WLDUSDT",
          "LTCUSDT",
          "NEARUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "SHIBUSDT",
          "BTCUSDT",
          "SUSDT",
          "HBARUSDT",
          "UNIUSDT",
          "XRPUSDT",
          "PENGUUSDT",
          "TRXUSDT",
          "AAVEUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "TAOUSDT",
          "LINKUSDT",
          "VIRTUALUSDT",
          "SXTUSDT",
          "LAYERUSDT"
        ],
        "candidate_count": 38,
        "filter_counts": {
          "missing_1h": 81,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 299,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-11",
        "decision_time_utc": "2025-05-11T00:00:00+00:00",
        "selected_symbols": [
          "ETHFIUSDT",
          "KAITOUSDT",
          "ARBUSDT",
          "WIFUSDT",
          "DOGEUSDT",
          "OPUSDT",
          "UNIUSDT",
          "XAIUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "SHIBUSDT",
          "PEPEUSDT",
          "NEIROUSDT",
          "AVAXUSDT",
          "DOTUSDT",
          "WLDUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "INITUSDT",
          "LINKUSDT",
          "HBARUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "TRUMPUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "LTCUSDT",
          "PENGUUSDT",
          "VIRTUALUSDT",
          "TRXUSDT",
          "BNBUSDT",
          "LAYERUSDT",
          "PNUTUSDT",
          "1000CATUSDT",
          "ACTUSDT",
          "MUBARAKUSDT"
        ],
        "candidate_count": 36,
        "filter_counts": {
          "missing_1h": 81,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 301,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-12",
        "decision_time_utc": "2025-05-12T00:00:00+00:00",
        "selected_symbols": [
          "PARTIUSDT",
          "INITUSDT",
          "PNUTUSDT",
          "MUBARAKUSDT",
          "NEIROUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "SOLUSDT",
          "PEPEUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "TRUMPUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "WLDUSDT",
          "RUNEUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "ETHFIUSDT",
          "LINKUSDT",
          "WIFUSDT",
          "ARBUSDT",
          "SHIBUSDT",
          "AVAXUSDT",
          "LTCUSDT",
          "OPUSDT",
          "UNIUSDT",
          "BONKUSDT",
          "VIRTUALUSDT"
        ],
        "candidate_count": 30,
        "filter_counts": {
          "missing_1h": 81,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 307,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-13",
        "decision_time_utc": "2025-05-13T00:00:00+00:00",
        "selected_symbols": [
          "ACTUSDT",
          "WIFUSDT",
          "FIDAUSDT",
          "XRPUSDT",
          "RUNEUSDT",
          "INITUSDT",
          "FLOKIUSDT",
          "TSTUSDT",
          "BOMEUSDT",
          "NEIROUSDT",
          "HBARUSDT",
          "TRXUSDT",
          "BTCUSDT",
          "LTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BONKUSDT",
          "BNBUSDT",
          "VIRTUALUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "PEPEUSDT",
          "SUIUSDT",
          "XLMUSDT",
          "TRUMPUSDT",
          "WLDUSDT",
          "NEARUSDT",
          "PNUTUSDT",
          "AVAXUSDT",
          "SUSDT",
          "ENAUSDT",
          "SHIBUSDT",
          "LINKUSDT",
          "MUBARAKUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "TAOUSDT",
          "PENGUUSDT",
          "UNIUSDT",
          "OPUSDT"
        ],
        "candidate_count": 42,
        "filter_counts": {
          "missing_1h": 81,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 295,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-14",
        "decision_time_utc": "2025-05-14T00:00:00+00:00",
        "selected_symbols": [
          "PEOPLEUSDT",
          "ETHFIUSDT",
          "NEIROUSDT",
          "MUBARAKUSDT",
          "BOMEUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "PNUTUSDT",
          "INITUSDT",
          "KAITOUSDT",
          "PEPEUSDT",
          "SOLUSDT",
          "RUNEUSDT",
          "TRUMPUSDT",
          "DOGEUSDT",
          "ARBUSDT",
          "BTCUSDT",
          "PENGUUSDT",
          "LINKUSDT",
          "SUIUSDT",
          "XRPUSDT",
          "SHIBUSDT",
          "AVAXUSDT",
          "WIFUSDT",
          "BONKUSDT",
          "VIRTUALUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "WLDUSDT",
          "LTCUSDT",
          "HBARUSDT"
        ],
        "candidate_count": 32,
        "filter_counts": {
          "missing_1h": 81,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 305,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-15",
        "decision_time_utc": "2025-05-15T00:00:00+00:00",
        "selected_symbols": [
          "PENGUUSDT",
          "ETHUSDT",
          "1000SATSUSDT",
          "PEOPLEUSDT",
          "BTCUSDT",
          "NEIROUSDT",
          "SOLUSDT",
          "TRXUSDT",
          "XRPUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "TRUMPUSDT",
          "ADAUSDT",
          "PNUTUSDT",
          "WIFUSDT",
          "ENAUSDT",
          "BONKUSDT",
          "ETHFIUSDT",
          "LTCUSDT",
          "AVAXUSDT",
          "LINKUSDT",
          "ONDOUSDT"
        ],
        "candidate_count": 24,
        "filter_counts": {
          "missing_1h": 81,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 313,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-16",
        "decision_time_utc": "2025-05-16T00:00:00+00:00",
        "selected_symbols": [
          "ETHFIUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "NEIROUSDT",
          "TRXUSDT",
          "TRUMPUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "WIFUSDT",
          "PNUTUSDT",
          "AVAXUSDT",
          "LINKUSDT",
          "PENGUUSDT",
          "LTCUSDT",
          "BONKUSDT",
          "VIRTUALUSDT",
          "TAOUSDT",
          "PEOPLEUSDT",
          "1000SATSUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 80,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 312,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-17",
        "decision_time_utc": "2025-05-17T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "WIFUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "PEPEUSDT",
          "SUIUSDT",
          "NXPCUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "TRUMPUSDT",
          "NEIROUSDT",
          "ETHFIUSDT",
          "ADAUSDT",
          "PNUTUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 80,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 320,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-18",
        "decision_time_utc": "2025-05-18T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "SUIUSDT",
          "XRPUSDT",
          "PEPEUSDT",
          "TRUMPUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "NEIROUSDT",
          "NXPCUSDT",
          "ENAUSDT",
          "WIFUSDT",
          "PNUTUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 80,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 322,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-19",
        "decision_time_utc": "2025-05-19T00:00:00+00:00",
        "selected_symbols": [
          "NEIROUSDT",
          "PEOPLEUSDT",
          "VIRTUALUSDT",
          "PNUTUSDT",
          "PEPEUSDT",
          "WIFUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "ETHFIUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "TRUMPUSDT",
          "SUIUSDT",
          "LTCUSDT",
          "XRPUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "LINKUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "NXPCUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 80,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 316,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-20",
        "decision_time_utc": "2025-05-20T00:00:00+00:00",
        "selected_symbols": [
          "AAVEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "PEPEUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "NEIROUSDT",
          "BNBUSDT",
          "TRUMPUSDT",
          "TRXUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "WIFUSDT",
          "NXPCUSDT",
          "VIRTUALUSDT",
          "PNUTUSDT",
          "LINKUSDT",
          "LTCUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 21,
        "filter_counts": {
          "missing_1h": 80,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 317,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-21",
        "decision_time_utc": "2025-05-21T00:00:00+00:00",
        "selected_symbols": [
          "TRUMPUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "TRXUSDT",
          "PEPEUSDT",
          "XRPUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "NEIROUSDT",
          "LTCUSDT",
          "LINKUSDT",
          "NXPCUSDT",
          "WIFUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 80,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 319,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-22",
        "decision_time_utc": "2025-05-22T00:00:00+00:00",
        "selected_symbols": [
          "INITUSDT",
          "WIFUSDT",
          "PNUTUSDT",
          "TAOUSDT",
          "WLDUSDT",
          "BTCUSDT",
          "PEPEUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "ETHUSDT",
          "NEIROUSDT",
          "ETHFIUSDT",
          "ADAUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "UNIUSDT",
          "LINKUSDT",
          "LTCUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "VIRTUALUSDT",
          "TRUMPUSDT",
          "TRXUSDT",
          "NXPCUSDT",
          "AAVEUSDT",
          "SXTUSDT"
        ],
        "candidate_count": 28,
        "filter_counts": {
          "missing_1h": 78,
          "insufficient_24h": 2,
          "reconstruct_error": 0,
          "low_quote_volume": 310,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-23",
        "decision_time_utc": "2025-05-23T00:00:00+00:00",
        "selected_symbols": [
          "WLDUSDT",
          "LISTAUSDT",
          "COOKIEUSDT",
          "PEPEUSDT",
          "NEIROUSDT",
          "BONKUSDT",
          "AVAXUSDT",
          "RUNEUSDT",
          "WIFUSDT",
          "ETHUSDT",
          "PNUTUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "TRUMPUSDT",
          "LINKUSDT",
          "TRXUSDT",
          "AAVEUSDT",
          "LTCUSDT",
          "BNBUSDT",
          "UNIUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "NXPCUSDT",
          "HAEDALUSDT",
          "CETUSUSDT"
        ],
        "candidate_count": 28,
        "filter_counts": {
          "missing_1h": 77,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 312,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-24",
        "decision_time_utc": "2025-05-24T00:00:00+00:00",
        "selected_symbols": [
          "SAGAUSDT",
          "COOKIEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "NXPCUSDT",
          "SOLUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "XRPUSDT",
          "TRUMPUSDT",
          "WIFUSDT",
          "BNBUSDT",
          "WLDUSDT",
          "ADAUSDT",
          "TRXUSDT",
          "NEIROUSDT",
          "PNUTUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "FETUSDT",
          "BONKUSDT",
          "VIRTUALUSDT",
          "LINKUSDT",
          "AAVEUSDT",
          "UNIUSDT",
          "LTCUSDT",
          "ETHFIUSDT",
          "TIAUSDT",
          "SHIBUSDT",
          "NEARUSDT",
          "CRVUSDT"
        ],
        "candidate_count": 32,
        "filter_counts": {
          "missing_1h": 77,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 309,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-25",
        "decision_time_utc": "2025-05-25T00:00:00+00:00",
        "selected_symbols": [
          "NXPCUSDT",
          "WLDUSDT",
          "BTCUSDT",
          "TRUMPUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "WIFUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "NEIROUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 77,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 324,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-26",
        "decision_time_utc": "2025-05-26T00:00:00+00:00",
        "selected_symbols": [
          "NEIROUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "AAVEUSDT",
          "SOLUSDT",
          "PEPEUSDT",
          "ADAUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "TRXUSDT",
          "WLDUSDT",
          "BNBUSDT",
          "TRUMPUSDT",
          "WIFUSDT",
          "NXPCUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 77,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 325,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-27",
        "decision_time_utc": "2025-05-27T00:00:00+00:00",
        "selected_symbols": [
          "UNIUSDT",
          "VIRTUALUSDT",
          "BTCUSDT",
          "PEPEUSDT",
          "ETHUSDT",
          "FETUSDT",
          "WIFUSDT",
          "SOLUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "TRXUSDT",
          "TRUMPUSDT",
          "WLDUSDT",
          "ADAUSDT",
          "NEIROUSDT",
          "AAVEUSDT",
          "COOKIEUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 76,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 321,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-28",
        "decision_time_utc": "2025-05-28T00:00:00+00:00",
        "selected_symbols": [
          "TRBUSDT",
          "WCTUSDT",
          "AIXBTUSDT",
          "VIRTUALUSDT",
          "CAKEUSDT",
          "ETHFIUSDT",
          "ETHUSDT",
          "PNUTUSDT",
          "SUIUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "SOLUSDT",
          "WLDUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "XRPUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "TRUMPUSDT",
          "WIFUSDT",
          "ADAUSDT",
          "HUMAUSDT",
          "UNIUSDT"
        ],
        "candidate_count": 24,
        "filter_counts": {
          "missing_1h": 76,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 318,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-29",
        "decision_time_utc": "2025-05-29T00:00:00+00:00",
        "selected_symbols": [
          "TONUSDT",
          "UNIUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "NEIROUSDT",
          "PEPEUSDT",
          "SOLUSDT",
          "WCTUSDT",
          "XRPUSDT",
          "WIFUSDT",
          "SUIUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "TRUMPUSDT",
          "TRXUSDT",
          "TRBUSDT",
          "ENAUSDT",
          "WLDUSDT",
          "VIRTUALUSDT",
          "ADAUSDT",
          "RENDERUSDT"
        ],
        "candidate_count": 21,
        "filter_counts": {
          "missing_1h": 74,
          "insufficient_24h": 2,
          "reconstruct_error": 0,
          "low_quote_volume": 321,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-30",
        "decision_time_utc": "2025-05-30T00:00:00+00:00",
        "selected_symbols": [
          "TRBUSDT",
          "WCTUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "PEPEUSDT",
          "SOLUSDT",
          "TONUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "UNIUSDT",
          "TRXUSDT",
          "TRUMPUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "WIFUSDT",
          "AVAXUSDT",
          "ETHFIUSDT",
          "VIRTUALUSDT",
          "NEIROUSDT",
          "LINKUSDT",
          "LTCUSDT",
          "AAVEUSDT",
          "NEARUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 74,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 319,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-31",
        "decision_time_utc": "2025-05-31T00:00:00+00:00",
        "selected_symbols": [
          "LPTUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "PEPEUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "TRBUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "TRUMPUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "UNIUSDT",
          "LINKUSDT",
          "WLDUSDT",
          "PNUTUSDT",
          "VIRTUALUSDT",
          "LTCUSDT",
          "AAVEUSDT",
          "WIFUSDT",
          "AVAXUSDT",
          "LDOUSDT",
          "NEIROUSDT",
          "ARBUSDT",
          "NEARUSDT",
          "ETHFIUSDT",
          "SHIBUSDT",
          "WCTUSDT"
        ],
        "candidate_count": 30,
        "filter_counts": {
          "missing_1h": 74,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 314,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-01",
        "decision_time_utc": "2025-06-01T00:00:00+00:00",
        "selected_symbols": [
          "TAOUSDT",
          "NEIROUSDT",
          "VIRTUALUSDT",
          "TRUMPUSDT",
          "BTCUSDT",
          "XRPUSDT",
          "ETHUSDT",
          "SUIUSDT",
          "SOLUSDT",
          "PEPEUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "WIFUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "TRBUSDT",
          "LPTUSDT",
          "WCTUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 74,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 325,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-02",
        "decision_time_utc": "2025-06-02T00:00:00+00:00",
        "selected_symbols": [
          "MASKUSDT",
          "BTCUSDT",
          "SUIUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "WCTUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 74,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 332,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-03",
        "decision_time_utc": "2025-06-03T00:00:00+00:00",
        "selected_symbols": [
          "SOPHUSDT",
          "WIFUSDT",
          "PEPEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "AUSDT",
          "SUIUSDT",
          "TRXUSDT",
          "VIRTUALUSDT",
          "WCTUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 74,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 329,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-04",
        "decision_time_utc": "2025-06-04T00:00:00+00:00",
        "selected_symbols": [
          "SOPHUSDT",
          "ENAUSDT",
          "XRPUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "WIFUSDT",
          "UNIUSDT",
          "SOLUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "TRUMPUSDT",
          "TAOUSDT",
          "ADAUSDT",
          "VIRTUALUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 74,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 328,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-05",
        "decision_time_utc": "2025-06-05T00:00:00+00:00",
        "selected_symbols": [
          "LPTUSDT",
          "TRBUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "TRXUSDT",
          "XRPUSDT",
          "PEPEUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "UNIUSDT",
          "WIFUSDT",
          "VIRTUALUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 74,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 328,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-06",
        "decision_time_utc": "2025-06-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "TRXUSDT",
          "SOLUSDT",
          "PEPEUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "TRUMPUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "WIFUSDT",
          "LPTUSDT",
          "AVAXUSDT",
          "VIRTUALUSDT",
          "LINKUSDT",
          "UNIUSDT",
          "AAVEUSDT",
          "RVNUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 74,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 324,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-07",
        "decision_time_utc": "2025-06-07T00:00:00+00:00",
        "selected_symbols": [
          "HUMAUSDT",
          "VIRTUALUSDT",
          "SUIUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "TRUMPUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "WIFUSDT",
          "MASKUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 74,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 328,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-08",
        "decision_time_utc": "2025-06-08T00:00:00+00:00",
        "selected_symbols": [
          "ANIMEUSDT",
          "HUMAUSDT",
          "ENAUSDT",
          "PEPEUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "TRXUSDT",
          "SOLUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "MASKUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 74,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 331,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-09",
        "decision_time_utc": "2025-06-09T00:00:00+00:00",
        "selected_symbols": [
          "ANIMEUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "PEPEUSDT",
          "HUMAUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "SUIUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 74,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 334,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-10",
        "decision_time_utc": "2025-06-10T00:00:00+00:00",
        "selected_symbols": [
          "ANIMEUSDT",
          "WIFUSDT",
          "ETHUSDT",
          "VIRTUALUSDT",
          "PEPEUSDT",
          "ENAUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "SUIUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "HUMAUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 74,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 328,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-11",
        "decision_time_utc": "2025-06-11T00:00:00+00:00",
        "selected_symbols": [
          "UNIUSDT",
          "AXLUSDT",
          "COMPUSDT",
          "NEIROUSDT",
          "AAVEUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "LINKUSDT",
          "PEPEUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "TRUMPUSDT",
          "WIFUSDT",
          "RVNUSDT"
        ],
        "candidate_count": 21,
        "filter_counts": {
          "missing_1h": 74,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 323,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-12",
        "decision_time_utc": "2025-06-12T00:00:00+00:00",
        "selected_symbols": [
          "KAIAUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "PEPEUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "UNIUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "WIFUSDT",
          "AAVEUSDT",
          "TRUMPUSDT",
          "LINKUSDT",
          "VIRTUALUSDT",
          "NEIROUSDT",
          "AVAXUSDT",
          "ANIMEUSDT",
          "WLDUSDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 73,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 322,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-13",
        "decision_time_utc": "2025-06-13T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "PEPEUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "UNIUSDT",
          "ADAUSDT",
          "VIRTUALUSDT",
          "ENAUSDT",
          "WIFUSDT",
          "AAVEUSDT",
          "LINKUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 72,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 328,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-14",
        "decision_time_utc": "2025-06-14T00:00:00+00:00",
        "selected_symbols": [
          "UNIUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "VIRTUALUSDT",
          "PEPEUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "TRUMPUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "WIFUSDT",
          "LINKUSDT",
          "NXPCUSDT",
          "OPUSDT",
          "NEIROUSDT",
          "WLDUSDT",
          "SHIBUSDT"
        ],
        "candidate_count": 23,
        "filter_counts": {
          "missing_1h": 72,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 323,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-15",
        "decision_time_utc": "2025-06-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "SUIUSDT",
          "XRPUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "TRUMPUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 72,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 337,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-16",
        "decision_time_utc": "2025-06-16T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "ETHUSDT",
          "SUIUSDT",
          "BTCUSDT",
          "PEPEUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 72,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 337,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-17",
        "decision_time_utc": "2025-06-17T00:00:00+00:00",
        "selected_symbols": [
          "XRPUSDT",
          "BTCUSDT",
          "UNIUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "TRXUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "TRUMPUSDT",
          "WIFUSDT",
          "ALTUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 72,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 331,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-18",
        "decision_time_utc": "2025-06-18T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "PEPEUSDT",
          "SUIUSDT",
          "TRXUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "UNIUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "WIFUSDT",
          "TAOUSDT",
          "ENAUSDT",
          "WLDUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 71,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 330,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-19",
        "decision_time_utc": "2025-06-19T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "PEPEUSDT",
          "UNIUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 71,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 336,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-20",
        "decision_time_utc": "2025-06-20T00:00:00+00:00",
        "selected_symbols": [
          "BCHUSDT",
          "RAYUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "UNIUSDT",
          "XRPUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "SUIUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 71,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 335,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-21",
        "decision_time_utc": "2025-06-21T00:00:00+00:00",
        "selected_symbols": [
          "SEIUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "UNIUSDT",
          "SUIUSDT",
          "PNUTUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 71,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 334,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-22",
        "decision_time_utc": "2025-06-22T00:00:00+00:00",
        "selected_symbols": [
          "SEIUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "UNIUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 71,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 335,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-23",
        "decision_time_utc": "2025-06-23T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "UNIUSDT",
          "BCHUSDT",
          "AAVEUSDT",
          "LINKUSDT",
          "ENAUSDT",
          "SEIUSDT",
          "VIRTUALUSDT",
          "TRUMPUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 71,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 328,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-24",
        "decision_time_utc": "2025-06-24T00:00:00+00:00",
        "selected_symbols": [
          "MOVEUSDT",
          "VIRTUALUSDT",
          "SEIUSDT",
          "WIFUSDT",
          "SUIUSDT",
          "TAOUSDT",
          "PEPEUSDT",
          "AAVEUSDT",
          "ENAUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "LINKUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "UNIUSDT",
          "XRPUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "TRUMPUSDT",
          "BNBUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 21,
        "filter_counts": {
          "missing_1h": 71,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 326,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-25",
        "decision_time_utc": "2025-06-25T00:00:00+00:00",
        "selected_symbols": [
          "SEIUSDT",
          "APTUSDT",
          "BANANAS31USDT",
          "WIFUSDT",
          "ETHUSDT",
          "LINKUSDT",
          "BTCUSDT",
          "UNIUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "PEPEUSDT",
          "AAVEUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "TRUMPUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 70,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 329,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-26",
        "decision_time_utc": "2025-06-26T00:00:00+00:00",
        "selected_symbols": [
          "BANANAS31USDT",
          "BCHUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "SEIUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "PEPEUSDT",
          "SUIUSDT",
          "DOGEUSDT",
          "UNIUSDT",
          "APTUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "NEWTUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 70,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 332,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-27",
        "decision_time_utc": "2025-06-27T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "SEIUSDT",
          "UNIUSDT",
          "TRXUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "NEWTUSDT",
          "BANANAS31USDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 69,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 334,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-28",
        "decision_time_utc": "2025-06-28T00:00:00+00:00",
        "selected_symbols": [
          "BANANAS31USDT",
          "SEIUSDT",
          "SUIUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "XRPUSDT",
          "ETHUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "APTUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 69,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 338,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-29",
        "decision_time_utc": "2025-06-29T00:00:00+00:00",
        "selected_symbols": [
          "PENGUUSDT",
          "SOLUSDT",
          "PEPEUSDT",
          "SUIUSDT",
          "XRPUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SEIUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 69,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 341,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-30",
        "decision_time_utc": "2025-06-30T00:00:00+00:00",
        "selected_symbols": [
          "ARBUSDT",
          "SAHARAUSDT",
          "PEPEUSDT",
          "ETHUSDT",
          "NEWTUSDT",
          "SUIUSDT",
          "SEIUSDT",
          "UNIUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "SOLUSDT",
          "ADAUSDT",
          "XRPUSDT",
          "PENGUUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 69,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 335,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-01",
        "decision_time_utc": "2025-07-01T00:00:00+00:00",
        "selected_symbols": [
          "HFTUSDT",
          "PENGUUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "SEIUSDT",
          "ARBUSDT",
          "NEWTUSDT",
          "ADAUSDT",
          "WIFUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 69,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 333,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-02",
        "decision_time_utc": "2025-07-02T00:00:00+00:00",
        "selected_symbols": [
          "HFTUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "PENGUUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "NEWTUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "UNIUSDT",
          "MAVUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 69,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 335,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-03",
        "decision_time_utc": "2025-07-03T00:00:00+00:00",
        "selected_symbols": [
          "NEIROUSDT",
          "WIFUSDT",
          "UNIUSDT",
          "ETHUSDT",
          "PEPEUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "PENGUUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "HFTUSDT",
          "SEIUSDT",
          "NEWTUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 69,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 331,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-04",
        "decision_time_utc": "2025-07-04T00:00:00+00:00",
        "selected_symbols": [
          "PENGUUSDT",
          "BONKUSDT",
          "SUIUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "ADAUSDT",
          "UNIUSDT",
          "SOLUSDT",
          "LTCUSDT",
          "PEPEUSDT",
          "WIFUSDT",
          "TRXUSDT",
          "NEWTUSDT",
          "BNBUSDT",
          "NEIROUSDT",
          "PNUTUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 69,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 331,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-05",
        "decision_time_utc": "2025-07-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "UNIUSDT",
          "PENGUUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "NEWTUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 69,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 337,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-06",
        "decision_time_utc": "2025-07-06T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "PEPEUSDT",
          "XRPUSDT",
          "NEWTUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 69,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 342,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-07",
        "decision_time_utc": "2025-07-07T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "DOGEUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "PEPEUSDT",
          "TONUSDT",
          "XRPUSDT",
          "WIFUSDT",
          "BTCUSDT",
          "UNIUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "NEWTUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 69,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 336,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-08",
        "decision_time_utc": "2025-07-08T00:00:00+00:00",
        "selected_symbols": [
          "VICUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "NEWTUSDT",
          "SUIUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 69,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 338,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-09",
        "decision_time_utc": "2025-07-09T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "PEPEUSDT",
          "UNIUSDT",
          "XRPUSDT",
          "VICUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "BONKUSDT",
          "NEWTUSDT",
          "BNBUSDT",
          "SAHARAUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 69,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 336,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-10",
        "decision_time_utc": "2025-07-10T00:00:00+00:00",
        "selected_symbols": [
          "BANANAS31USDT",
          "MAGICUSDT",
          "NEIROUSDT",
          "WIFUSDT",
          "XLMUSDT",
          "PEPEUSDT",
          "ETHUSDT",
          "UNIUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "XRPUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "TRUMPUSDT",
          "AAVEUSDT",
          "SAHARAUSDT",
          "BNBUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 68,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 329,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-11",
        "decision_time_utc": "2025-07-11T00:00:00+00:00",
        "selected_symbols": [
          "HYPERUSDT",
          "BANANAS31USDT",
          "PENGUUSDT",
          "PNUTUSDT",
          "WLDUSDT",
          "SEIUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "BONKUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "WIFUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "NEIROUSDT",
          "BTCUSDT",
          "TRUMPUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "LINKUSDT",
          "AVAXUSDT",
          "XLMUSDT",
          "BNBUSDT",
          "UNIUSDT",
          "AAVEUSDT",
          "TRXUSDT",
          "SAHARAUSDT",
          "LAUSDT"
        ],
        "candidate_count": 28,
        "filter_counts": {
          "missing_1h": 68,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 322,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-12",
        "decision_time_utc": "2025-07-12T00:00:00+00:00",
        "selected_symbols": [
          "1INCHUSDT",
          "PENGUUSDT",
          "XLMUSDT",
          "PORTALUSDT",
          "XRPUSDT",
          "SEIUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "TAOUSDT",
          "ETHUSDT",
          "UNIUSDT",
          "TRXUSDT",
          "SOLUSDT",
          "HBARUSDT",
          "RESOLVUSDT",
          "PEPEUSDT",
          "ARBUSDT",
          "TRUMPUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "WIFUSDT",
          "LINKUSDT",
          "NEIROUSDT",
          "BONKUSDT",
          "TONUSDT",
          "WLDUSDT",
          "LTCUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "PNUTUSDT",
          "SHIBUSDT",
          "ALTUSDT",
          "HYPERUSDT",
          "REZUSDT",
          "VICUSDT",
          "BANANAS31USDT"
        ],
        "candidate_count": 38,
        "filter_counts": {
          "missing_1h": 68,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 312,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-13",
        "decision_time_utc": "2025-07-13T00:00:00+00:00",
        "selected_symbols": [
          "KNCUSDT",
          "BONKUSDT",
          "XLMUSDT",
          "XRPUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "HBARUSDT",
          "SOLUSDT",
          "TRXUSDT",
          "PEPEUSDT",
          "SUIUSDT",
          "DOGEUSDT",
          "PENGUUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "SEIUSDT",
          "ENAUSDT",
          "UNIUSDT",
          "TRUMPUSDT",
          "WIFUSDT",
          "BANANAS31USDT"
        ],
        "candidate_count": 21,
        "filter_counts": {
          "missing_1h": 68,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 329,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-14",
        "decision_time_utc": "2025-07-14T00:00:00+00:00",
        "selected_symbols": [
          "PENGUUSDT",
          "HBARUSDT",
          "XLMUSDT",
          "ALGOUSDT",
          "AUCTIONUSDT",
          "ENAUSDT",
          "XRPUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "WIFUSDT",
          "SUIUSDT",
          "AVAXUSDT",
          "SOLUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "TRUMPUSDT",
          "1INCHUSDT",
          "BANANAS31USDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 68,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 328,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-15",
        "decision_time_utc": "2025-07-15T00:00:00+00:00",
        "selected_symbols": [
          "TURBOUSDT",
          "SUIUSDT",
          "UNIUSDT",
          "XRPUSDT",
          "SEIUSDT",
          "ALGOUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "SOLUSDT",
          "BONKUSDT",
          "WIFUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "XLMUSDT",
          "PENGUUSDT",
          "HBARUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "LINKUSDT",
          "WLDUSDT",
          "ENAUSDT",
          "TRUMPUSDT",
          "AVAXUSDT",
          "PNUTUSDT",
          "NEIROUSDT",
          "USUALUSDT"
        ],
        "candidate_count": 28,
        "filter_counts": {
          "missing_1h": 68,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 322,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-16",
        "decision_time_utc": "2025-07-16T00:00:00+00:00",
        "selected_symbols": [
          "THEUSDT",
          "BONKUSDT",
          "SEIUSDT",
          "PENGUUSDT",
          "ARBUSDT",
          "ETHUSDT",
          "CRVUSDT",
          "SUIUSDT",
          "ENAUSDT",
          "PEPEUSDT",
          "WIFUSDT",
          "AVAXUSDT",
          "NEIROUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "SOLUSDT",
          "UNIUSDT",
          "WLDUSDT",
          "XRPUSDT",
          "LINKUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "XLMUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "HBARUSDT",
          "LTCUSDT",
          "TRUMPUSDT"
        ],
        "candidate_count": 28,
        "filter_counts": {
          "missing_1h": 68,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 322,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-17",
        "decision_time_utc": "2025-07-17T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "FLOKIUSDT",
          "CRVUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "NEIROUSDT",
          "PEPEUSDT",
          "XRPUSDT",
          "ETHFIUSDT",
          "TRUMPUSDT",
          "BTCUSDT",
          "PNUTUSDT",
          "LINKUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "REZUSDT",
          "WLDUSDT",
          "APTUSDT",
          "HBARUSDT",
          "SUIUSDT",
          "XLMUSDT",
          "WIFUSDT",
          "PENGUUSDT",
          "LTCUSDT",
          "ARBUSDT",
          "UNIUSDT",
          "AVAXUSDT",
          "SEIUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 32,
        "filter_counts": {
          "missing_1h": 68,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 318,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-18",
        "decision_time_utc": "2025-07-18T00:00:00+00:00",
        "selected_symbols": [
          "HBARUSDT",
          "XRPUSDT",
          "LDOUSDT",
          "ALGOUSDT",
          "XLMUSDT",
          "CRVUSDT",
          "ADAUSDT",
          "LINKUSDT",
          "ONDOUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "LTCUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "SUIUSDT",
          "ENAUSDT",
          "ARBUSDT",
          "PEPEUSDT",
          "TRUMPUSDT",
          "VIRTUALUSDT",
          "BONKUSDT",
          "PENGUUSDT",
          "UNIUSDT",
          "FLOKIUSDT",
          "ETHFIUSDT",
          "WIFUSDT",
          "NEIROUSDT",
          "SEIUSDT",
          "AAVEUSDT",
          "PNUTUSDT",
          "WLDUSDT"
        ],
        "candidate_count": 34,
        "filter_counts": {
          "missing_1h": 67,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 316,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-19",
        "decision_time_utc": "2025-07-19T00:00:00+00:00",
        "selected_symbols": [
          "EPICUSDT",
          "SUSHIUSDT",
          "UNIUSDT",
          "ETCUSDT",
          "DOGEUSDT",
          "PENGUUSDT",
          "ETHUSDT",
          "TRXUSDT",
          "NEIROUSDT",
          "OPUSDT",
          "BTCUSDT",
          "XRPUSDT",
          "FLOKIUSDT",
          "ENAUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "WLDUSDT",
          "BCHUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "ADAUSDT",
          "SHIBUSDT",
          "AAVEUSDT",
          "LDOUSDT",
          "LTCUSDT",
          "ARBUSDT",
          "SEIUSDT",
          "BONKUSDT",
          "HBARUSDT",
          "XLMUSDT",
          "TRUMPUSDT",
          "LINKUSDT",
          "WIFUSDT",
          "ERAUSDT",
          "APTUSDT",
          "CRVUSDT",
          "AVAXUSDT",
          "PNUTUSDT",
          "DOTUSDT",
          "VIRTUALUSDT"
        ],
        "candidate_count": 44,
        "filter_counts": {
          "missing_1h": 66,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 307,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-20",
        "decision_time_utc": "2025-07-20T00:00:00+00:00",
        "selected_symbols": [
          "XTZUSDT",
          "LTCUSDT",
          "ENAUSDT",
          "WIFUSDT",
          "ETCUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "LINKUSDT",
          "HBARUSDT",
          "XRPUSDT",
          "BTCUSDT",
          "FLOKIUSDT",
          "BONKUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "PENGUUSDT",
          "UNIUSDT",
          "XLMUSDT",
          "ERAUSDT",
          "CRVUSDT",
          "EPICUSDT"
        ],
        "candidate_count": 26,
        "filter_counts": {
          "missing_1h": 66,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 326,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-21",
        "decision_time_utc": "2025-07-21T00:00:00+00:00",
        "selected_symbols": [
          "CFXUSDT",
          "CKBUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "WIFUSDT",
          "PNUTUSDT",
          "ETHUSDT",
          "LDOUSDT",
          "BCHUSDT",
          "WLDUSDT",
          "TRUMPUSDT",
          "PEPEUSDT",
          "LINKUSDT",
          "UNIUSDT",
          "SOLUSDT",
          "XTZUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "LTCUSDT",
          "ARBUSDT",
          "SHIBUSDT",
          "XRPUSDT",
          "BTCUSDT",
          "SUIUSDT",
          "ETHFIUSDT",
          "NEIROUSDT",
          "ERAUSDT",
          "AVAXUSDT",
          "HBARUSDT",
          "AAVEUSDT",
          "ETCUSDT",
          "TRXUSDT",
          "BONKUSDT",
          "PENGUUSDT",
          "XLMUSDT",
          "FLOKIUSDT",
          "CRVUSDT",
          "APTUSDT"
        ],
        "candidate_count": 38,
        "filter_counts": {
          "missing_1h": 66,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 314,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-22",
        "decision_time_utc": "2025-07-22T00:00:00+00:00",
        "selected_symbols": [
          "SPKUSDT",
          "UMAUSDT",
          "DIAUSDT",
          "PENGUUSDT",
          "SOLUSDT",
          "FLOKIUSDT",
          "TAOUSDT",
          "ENAUSDT",
          "BONKUSDT",
          "XRPUSDT",
          "TRUMPUSDT",
          "PNUTUSDT",
          "ADAUSDT",
          "VIRTUALUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SUIUSDT",
          "WIFUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "XLMUSDT",
          "UNIUSDT",
          "PEPEUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "LINKUSDT",
          "TRXUSDT",
          "WLDUSDT",
          "CFXUSDT",
          "HBARUSDT",
          "ERAUSDT",
          "ARBUSDT",
          "LTCUSDT",
          "BCHUSDT",
          "SEIUSDT",
          "NEIROUSDT",
          "AAVEUSDT",
          "SHIBUSDT"
        ],
        "candidate_count": 38,
        "filter_counts": {
          "missing_1h": 66,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 314,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-23",
        "decision_time_utc": "2025-07-23T00:00:00+00:00",
        "selected_symbols": [
          "CUSDT",
          "SPKUSDT",
          "PENGUUSDT",
          "WLDUSDT",
          "SOLUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "LAUSDT",
          "LTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "CRVUSDT",
          "WIFUSDT",
          "ADAUSDT",
          "FLOKIUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "AVAXUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "HBARUSDT",
          "TRXUSDT",
          "LINKUSDT",
          "ENAUSDT",
          "APTUSDT",
          "PNUTUSDT",
          "TAOUSDT",
          "TONUSDT",
          "VIRTUALUSDT",
          "DOTUSDT",
          "UNIUSDT",
          "TRUMPUSDT",
          "ERAUSDT",
          "XLMUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "NEARUSDT",
          "NEIROUSDT",
          "SHIBUSDT",
          "CFXUSDT"
        ],
        "candidate_count": 40,
        "filter_counts": {
          "missing_1h": 66,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 312,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-24",
        "decision_time_utc": "2025-07-24T00:00:00+00:00",
        "selected_symbols": [
          "SPKUSDT",
          "SAHARAUSDT",
          "NEWTUSDT",
          "SLPUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "PENGUUSDT",
          "XRPUSDT",
          "CUSDT",
          "SOLUSDT",
          "ERAUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "PEPEUSDT",
          "LAUSDT",
          "TRXUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "ENAUSDT",
          "WIFUSDT",
          "LTCUSDT",
          "UNIUSDT",
          "WLDUSDT",
          "HBARUSDT",
          "TRUMPUSDT",
          "XLMUSDT",
          "AVAXUSDT",
          "FLOKIUSDT",
          "APTUSDT",
          "LINKUSDT",
          "CRVUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "CAKEUSDT",
          "PNUTUSDT",
          "SEIUSDT",
          "CFXUSDT",
          "SHIBUSDT",
          "DOTUSDT"
        ],
        "candidate_count": 42,
        "filter_counts": {
          "missing_1h": 66,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 310,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-25",
        "decision_time_utc": "2025-07-25T00:00:00+00:00",
        "selected_symbols": [
          "ERAUSDT",
          "NEWTUSDT",
          "KERNELUSDT",
          "HYPERUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "BTCUSDT",
          "XRPUSDT",
          "TRXUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "CFXUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "CRVUSDT",
          "PEPEUSDT",
          "PENGUUSDT",
          "UNIUSDT",
          "HBARUSDT",
          "WIFUSDT",
          "LTCUSDT",
          "LINKUSDT",
          "TRUMPUSDT",
          "BCHUSDT",
          "XLMUSDT",
          "FLOKIUSDT",
          "LAUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "WLDUSDT",
          "AAVEUSDT",
          "DOTUSDT",
          "SEIUSDT",
          "SAHARAUSDT",
          "SPKUSDT"
        ],
        "candidate_count": 37,
        "filter_counts": {
          "missing_1h": 66,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 315,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-26",
        "decision_time_utc": "2025-07-26T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "SPKUSDT",
          "HYPERUSDT",
          "CRVUSDT",
          "HBARUSDT",
          "BCHUSDT",
          "BONKUSDT",
          "SUIUSDT",
          "PENGUUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "WIFUSDT",
          "UNIUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "XRPUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "LINKUSDT",
          "ADAUSDT",
          "LTCUSDT",
          "ERAUSDT",
          "XLMUSDT",
          "AVAXUSDT",
          "TRUMPUSDT"
        ],
        "candidate_count": 27,
        "filter_counts": {
          "missing_1h": 66,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 325,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-27",
        "decision_time_utc": "2025-07-27T00:00:00+00:00",
        "selected_symbols": [
          "CKBUSDT",
          "HBARUSDT",
          "PENGUUSDT",
          "SUIUSDT",
          "CRVUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "ERAUSDT",
          "BTCUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "PEPEUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 66,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 333,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-28",
        "decision_time_utc": "2025-07-28T00:00:00+00:00",
        "selected_symbols": [
          "ASRUSDT",
          "CAKEUSDT",
          "ERAUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "ETHUSDT",
          "SUIUSDT",
          "WIFUSDT",
          "BCHUSDT",
          "HBARUSDT",
          "BTCUSDT",
          "LINKUSDT",
          "AVAXUSDT",
          "XRPUSDT",
          "PENGUUSDT",
          "SOLUSDT",
          "PEPEUSDT",
          "UNIUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "TRXUSDT",
          "CRVUSDT"
        ],
        "candidate_count": 23,
        "filter_counts": {
          "missing_1h": 66,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 328,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-29",
        "decision_time_utc": "2025-07-29T00:00:00+00:00",
        "selected_symbols": [
          "ASRUSDT",
          "BANANAS31USDT",
          "1000CATUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "OPUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "ERAUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "ENAUSDT",
          "BONKUSDT",
          "PEPEUSDT",
          "PENGUUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "CAKEUSDT",
          "HBARUSDT",
          "WIFUSDT",
          "UNIUSDT",
          "LINKUSDT",
          "BCHUSDT",
          "CRVUSDT",
          "LTCUSDT",
          "TRUMPUSDT",
          "ARBUSDT",
          "WLDUSDT"
        ],
        "candidate_count": 30,
        "filter_counts": {
          "missing_1h": 66,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 322,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-30",
        "decision_time_utc": "2025-07-30T00:00:00+00:00",
        "selected_symbols": [
          "TRXUSDT",
          "ETHUSDT",
          "CFXUSDT",
          "BTCUSDT",
          "ERAUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "ENAUSDT",
          "PEPEUSDT",
          "BONKUSDT",
          "PENGUUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "UNIUSDT",
          "LINKUSDT",
          "HBARUSDT",
          "CRVUSDT",
          "LTCUSDT",
          "BANANAS31USDT",
          "CUSDT"
        ],
        "candidate_count": 23,
        "filter_counts": {
          "missing_1h": 65,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 328,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-31",
        "decision_time_utc": "2025-07-31T00:00:00+00:00",
        "selected_symbols": [
          "CFXUSDT",
          "ENAUSDT",
          "SPKUSDT",
          "CRVUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ERAUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "TRXUSDT",
          "LTCUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "PENGUUSDT",
          "PEPEUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "TONUSDT",
          "AVAXUSDT",
          "UNIUSDT",
          "HBARUSDT",
          "LINKUSDT",
          "WIFUSDT"
        ],
        "candidate_count": 24,
        "filter_counts": {
          "missing_1h": 65,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 329,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-01",
        "decision_time_utc": "2025-08-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "TONUSDT",
          "ERAUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "PENGUUSDT",
          "SUIUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "PEPEUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "HBARUSDT",
          "UNIUSDT",
          "CFXUSDT",
          "AVAXUSDT",
          "LINKUSDT",
          "SUSDT",
          "LTCUSDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 65,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 331,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-02",
        "decision_time_utc": "2025-08-02T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "PENGUUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "PEPEUSDT",
          "TONUSDT",
          "ADAUSDT",
          "LTCUSDT",
          "HBARUSDT",
          "LINKUSDT",
          "BONKUSDT",
          "UNIUSDT",
          "AVAXUSDT",
          "XLMUSDT",
          "TREEUSDT",
          "WIFUSDT",
          "NEARUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "SEIUSDT",
          "APTUSDT"
        ],
        "candidate_count": 27,
        "filter_counts": {
          "missing_1h": 65,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 326,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-03",
        "decision_time_utc": "2025-08-03T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "PENGUUSDT",
          "PEPEUSDT",
          "ADAUSDT",
          "LTCUSDT",
          "BONKUSDT",
          "HBARUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 65,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 338,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-04",
        "decision_time_utc": "2025-08-04T00:00:00+00:00",
        "selected_symbols": [
          "CFXUSDT",
          "ENAUSDT",
          "XRPUSDT",
          "HBARUSDT",
          "PENGUUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "SUIUSDT",
          "SOLUSDT",
          "ETCUSDT",
          "PEPEUSDT",
          "BNBUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 65,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 338,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-05",
        "decision_time_utc": "2025-08-05T00:00:00+00:00",
        "selected_symbols": [
          "MAGICUSDT",
          "SPKUSDT",
          "LTCUSDT",
          "ETHUSDT",
          "UNIUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "PEPEUSDT",
          "PENGUUSDT",
          "XLMUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "CRVUSDT",
          "TRXUSDT",
          "BONKUSDT",
          "HBARUSDT",
          "TONUSDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 65,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 331,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-06",
        "decision_time_utc": "2025-08-06T00:00:00+00:00",
        "selected_symbols": [
          "ILVUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "LTCUSDT",
          "TRXUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "PEPEUSDT",
          "PENGUUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "CRVUSDT",
          "UNIUSDT",
          "LINKUSDT",
          "SPKUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 63,
          "insufficient_24h": 2,
          "reconstruct_error": 0,
          "low_quote_volume": 334,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-07",
        "decision_time_utc": "2025-08-07T00:00:00+00:00",
        "selected_symbols": [
          "PENGUUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "TRXUSDT",
          "LTCUSDT",
          "TOWNSUSDT",
          "PROVEUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 63,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 340,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-08",
        "decision_time_utc": "2025-08-08T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "XRPUSDT",
          "LINKUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "UNIUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "SOLUSDT",
          "BONKUSDT",
          "HBARUSDT",
          "PEPEUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "PENGUUSDT",
          "LTCUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "CFXUSDT",
          "TRXUSDT",
          "TSTUSDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 63,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 333,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-09",
        "decision_time_utc": "2025-08-09T00:00:00+00:00",
        "selected_symbols": [
          "MAGICUSDT",
          "LINKUSDT",
          "PENDLEUSDT",
          "PEPEUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "APTUSDT",
          "UNIUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "XLMUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "TREEUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "PENGUUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "LTCUSDT",
          "TRXUSDT",
          "HBARUSDT",
          "BONKUSDT",
          "CRVUSDT"
        ],
        "candidate_count": 24,
        "filter_counts": {
          "missing_1h": 63,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 331,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-10",
        "decision_time_utc": "2025-08-10T00:00:00+00:00",
        "selected_symbols": [
          "PROVEUSDT",
          "LDOUSDT",
          "ENAUSDT",
          "MAGICUSDT",
          "LINKUSDT",
          "ETHUSDT",
          "TREEUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "BONKUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "PENGUUSDT",
          "SUIUSDT",
          "AVAXUSDT",
          "XRPUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "UNIUSDT",
          "LTCUSDT",
          "TRXUSDT",
          "GMXUSDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 63,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 333,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-11",
        "decision_time_utc": "2025-08-11T00:00:00+00:00",
        "selected_symbols": [
          "RAYUSDT",
          "BIOUSDT",
          "ENAUSDT",
          "LDOUSDT",
          "BTCUSDT",
          "PENGUUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "LTCUSDT",
          "XRPUSDT",
          "BONKUSDT",
          "BNBUSDT",
          "LINKUSDT",
          "TRXUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "PROVEUSDT",
          "TREEUSDT",
          "ADAUSDT",
          "UNIUSDT",
          "GMXUSDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 63,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 333,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-12",
        "decision_time_utc": "2025-08-12T00:00:00+00:00",
        "selected_symbols": [
          "PROVEUSDT",
          "BIOUSDT",
          "BANANAS31USDT",
          "LDOUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ZROUSDT",
          "TRXUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "UNIUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "TREEUSDT",
          "PEPEUSDT",
          "ADAUSDT",
          "LINKUSDT",
          "LTCUSDT",
          "PENGUUSDT",
          "BONKUSDT",
          "AVAXUSDT",
          "PENDLEUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "XLMUSDT",
          "HBARUSDT",
          "CRVUSDT",
          "WIFUSDT",
          "TRUMPUSDT",
          "SEIUSDT",
          "ETHFIUSDT"
        ],
        "candidate_count": 33,
        "filter_counts": {
          "missing_1h": 63,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 322,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-13",
        "decision_time_utc": "2025-08-13T00:00:00+00:00",
        "selected_symbols": [
          "LINKUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "LTCUSDT",
          "PEPEUSDT",
          "AVAXUSDT",
          "TREEUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "BCHUSDT",
          "XRPUSDT",
          "UNIUSDT",
          "HBARUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "LDOUSDT",
          "ENAUSDT",
          "TRXUSDT",
          "BONKUSDT",
          "PENGUUSDT",
          "PROVEUSDT",
          "CYBERUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 63,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 330,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-14",
        "decision_time_utc": "2025-08-14T00:00:00+00:00",
        "selected_symbols": [
          "SKLUSDT",
          "ARBUSDT",
          "ETHFIUSDT",
          "OPUSDT",
          "SEIUSDT",
          "ADAUSDT",
          "SOLUSDT",
          "BONKUSDT",
          "ETHUSDT",
          "NEARUSDT",
          "BTCUSDT",
          "CRVUSDT",
          "DOGEUSDT",
          "UNIUSDT",
          "WLDUSDT",
          "SUIUSDT",
          "TRUMPUSDT",
          "APTUSDT",
          "WIFUSDT",
          "TRXUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "LINKUSDT",
          "AAVEUSDT",
          "XRPUSDT",
          "PEPEUSDT",
          "HBARUSDT",
          "ENAUSDT",
          "PENGUUSDT",
          "LTCUSDT",
          "TONUSDT",
          "BCHUSDT",
          "LDOUSDT",
          "PROVEUSDT"
        ],
        "candidate_count": 34,
        "filter_counts": {
          "missing_1h": 62,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 321,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-15",
        "decision_time_utc": "2025-08-15T00:00:00+00:00",
        "selected_symbols": [
          "SKLUSDT",
          "ADAUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "SUIUSDT",
          "ENAUSDT",
          "PEPEUSDT",
          "LINKUSDT",
          "UNIUSDT",
          "TRUMPUSDT",
          "ARBUSDT",
          "LTCUSDT",
          "AVAXUSDT",
          "PENGUUSDT",
          "BONKUSDT",
          "RAYUSDT",
          "HBARUSDT",
          "SEIUSDT",
          "WIFUSDT",
          "XLMUSDT",
          "AAVEUSDT",
          "LDOUSDT",
          "WLDUSDT",
          "NEARUSDT",
          "PROVEUSDT",
          "OPUSDT",
          "DOTUSDT",
          "CRVUSDT",
          "ETHFIUSDT",
          "APTUSDT",
          "TAOUSDT",
          "PENDLEUSDT",
          "BCHUSDT",
          "TONUSDT",
          "CFXUSDT"
        ],
        "candidate_count": 40,
        "filter_counts": {
          "missing_1h": 62,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 316,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-16",
        "decision_time_utc": "2025-08-16T00:00:00+00:00",
        "selected_symbols": [
          "ALPINEUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "TRUMPUSDT",
          "XRPUSDT",
          "ENAUSDT",
          "TRXUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "AVAXUSDT",
          "PEPEUSDT",
          "LINKUSDT",
          "ARBUSDT",
          "UNIUSDT",
          "LTCUSDT",
          "PENGUUSDT",
          "PROVEUSDT",
          "SEIUSDT",
          "HBARUSDT",
          "BONKUSDT",
          "WIFUSDT",
          "SKLUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 62,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 331,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-17",
        "decision_time_utc": "2025-08-17T00:00:00+00:00",
        "selected_symbols": [
          "CTSIUSDT",
          "PROVEUSDT",
          "LINKUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "UNIUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "ENAUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 62,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 341,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-18",
        "decision_time_utc": "2025-08-18T00:00:00+00:00",
        "selected_symbols": [
          "LINKUSDT",
          "ARBUSDT",
          "ADAUSDT",
          "SEIUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "TRXUSDT",
          "XRPUSDT",
          "PROVEUSDT",
          "TRUMPUSDT",
          "SUIUSDT",
          "ENAUSDT",
          "PEPEUSDT",
          "LTCUSDT",
          "UNIUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 62,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 337,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-19",
        "decision_time_utc": "2025-08-19T00:00:00+00:00",
        "selected_symbols": [
          "POLUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "TOWNSUSDT",
          "LINKUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "PROVEUSDT",
          "TRXUSDT",
          "ENAUSDT",
          "ARBUSDT",
          "PEPEUSDT",
          "UNIUSDT",
          "AVAXUSDT",
          "BIOUSDT",
          "PENGUUSDT",
          "SEIUSDT",
          "LTCUSDT",
          "HBARUSDT"
        ],
        "candidate_count": 23,
        "filter_counts": {
          "missing_1h": 61,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 333,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-20",
        "decision_time_utc": "2025-08-20T00:00:00+00:00",
        "selected_symbols": [
          "API3USDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "PROVEUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "LINKUSDT",
          "TRXUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "TOWNSUSDT",
          "ENAUSDT",
          "PEPEUSDT",
          "PENGUUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "UNIUSDT",
          "BIOUSDT",
          "LTCUSDT",
          "SEIUSDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 61,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 335,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-21",
        "decision_time_utc": "2025-08-21T00:00:00+00:00",
        "selected_symbols": [
          "MEMEUSDT",
          "BIOUSDT",
          "LINKUSDT",
          "CFXUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "PENGUUSDT",
          "ARBUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "UNIUSDT",
          "ADAUSDT",
          "XRPUSDT",
          "BTCUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "TRXUSDT",
          "LTCUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 61,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 337,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-22",
        "decision_time_utc": "2025-08-22T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "API3USDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "LINKUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "SUIUSDT",
          "ENAUSDT",
          "PEPEUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 61,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 342,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-23",
        "decision_time_utc": "2025-08-23T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "MEMEUSDT",
          "ENAUSDT",
          "LDOUSDT",
          "PENGUUSDT",
          "ARBUSDT",
          "ETHUSDT",
          "ETHFIUSDT",
          "ETCUSDT",
          "AAVEUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "UNIUSDT",
          "SUIUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "SEIUSDT",
          "ADAUSDT",
          "XRPUSDT",
          "LINKUSDT",
          "DOTUSDT",
          "WIFUSDT",
          "NEARUSDT",
          "HBARUSDT",
          "BNBUSDT",
          "XLMUSDT",
          "BTCUSDT",
          "LTCUSDT",
          "TRUMPUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 31,
        "filter_counts": {
          "missing_1h": 61,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 326,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-24",
        "decision_time_utc": "2025-08-24T00:00:00+00:00",
        "selected_symbols": [
          "BOMEUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "SOLUSDT",
          "AAVEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "LINKUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "SUIUSDT",
          "TRXUSDT",
          "MEMEUSDT",
          "PEPEUSDT",
          "BIOUSDT",
          "PENGUUSDT",
          "UNIUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 61,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 337,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-25",
        "decision_time_utc": "2025-08-25T00:00:00+00:00",
        "selected_symbols": [
          "MEMEUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "PLUMEUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "SUIUSDT",
          "LINKUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "ENAUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "UNIUSDT",
          "PENGUUSDT",
          "AAVEUSDT",
          "LTCUSDT",
          "WIFUSDT",
          "SEIUSDT",
          "BIOUSDT"
        ],
        "candidate_count": 23,
        "filter_counts": {
          "missing_1h": 61,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 334,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-26",
        "decision_time_utc": "2025-08-26T00:00:00+00:00",
        "selected_symbols": [
          "ONTUSDT",
          "SPKUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "LINKUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "ENAUSDT",
          "BIOUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "LTCUSDT",
          "UNIUSDT",
          "PENGUUSDT",
          "AAVEUSDT",
          "HBARUSDT",
          "PLUMEUSDT",
          "MEMEUSDT",
          "WIFUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 61,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 332,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-27",
        "decision_time_utc": "2025-08-27T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "AAVEUSDT",
          "LINKUSDT",
          "BTCUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "TRXUSDT",
          "BNBUSDT",
          "PENGUUSDT",
          "PEPEUSDT",
          "LTCUSDT",
          "PLUMEUSDT",
          "AVAXUSDT",
          "UNIUSDT",
          "ARBUSDT",
          "ENAUSDT",
          "BIOUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 61,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 337,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-28",
        "decision_time_utc": "2025-08-28T00:00:00+00:00",
        "selected_symbols": [
          "NMRUSDT",
          "LPTUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "LINKUSDT",
          "BIOUSDT",
          "TRXUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "PEPEUSDT",
          "ARBUSDT",
          "UNIUSDT",
          "XLMUSDT",
          "PENGUUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 21,
        "filter_counts": {
          "missing_1h": 60,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 336,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-29",
        "decision_time_utc": "2025-08-29T00:00:00+00:00",
        "selected_symbols": [
          "PYTHUSDT",
          "ENAUSDT",
          "SOLUSDT",
          "DOLOUSDT",
          "LINKUSDT",
          "BTCUSDT",
          "LPTUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ARBUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "AVAXUSDT",
          "XRPUSDT",
          "PEPEUSDT",
          "ADAUSDT",
          "PLUMEUSDT",
          "TRXUSDT",
          "NMRUSDT",
          "BIOUSDT",
          "AAVEUSDT",
          "TREEUSDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 60,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 335,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-30",
        "decision_time_utc": "2025-08-30T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "WUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "PYTHUSDT",
          "LINKUSDT",
          "BONKUSDT",
          "SUIUSDT",
          "TRXUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "PEPEUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "PENGUUSDT",
          "PLUMEUSDT",
          "HBARUSDT",
          "UNIUSDT",
          "LTCUSDT"
        ],
        "candidate_count": 23,
        "filter_counts": {
          "missing_1h": 59,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 335,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-31",
        "decision_time_utc": "2025-08-31T00:00:00+00:00",
        "selected_symbols": [
          "DOLOUSDT",
          "SKLUSDT",
          "CFXUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "LINKUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "PYTHUSDT",
          "PLUMEUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 59,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 343,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-01",
        "decision_time_utc": "2025-09-01T00:00:00+00:00",
        "selected_symbols": [
          "DOLOUSDT",
          "POLUSDT",
          "ETHUSDT",
          "TRUMPUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "LINKUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "PLUMEUSDT",
          "FORMUSDT",
          "ADAUSDT",
          "SUIUSDT",
          "MITOUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 59,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 341,
          "low_trades": 1,
          "stable_like": 0
        }
      }
    ],
    "limitations": [
      "Symbol master is built from current Binance exchangeInfo.",
      "Symbols that traded historically but are delisted today are not in the master list.",
      "First full run can be slow because 1h/4h/1d klines are cached for many symbols."
    ]
  }
}
```
