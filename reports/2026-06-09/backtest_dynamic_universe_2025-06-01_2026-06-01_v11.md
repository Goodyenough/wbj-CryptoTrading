---
created: 2026-06-09 17:08:16 CST
tags:
  - crypto
  - trading-system
  - backtest
backtest_run_id: 67ba6215cad9
report_version: v11
sample_sufficient: true
universe_mode: true
universe_type: dynamic
---

# 回测报告 2025-06-01 至 2026-06-01 v11

- 回测 ID：`67ba6215cad9`
- 交易对：`0GUSDT`, `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1INCHUSDT`, `2ZUSDT`, `AAVEUSDT`, `ACEUSDT`, `ADAUSDT`, `AEVOUSDT`, `AIUSDT`, `ALCXUSDT`, `ALGOUSDT`, `ALICEUSDT`, `ALLOUSDT`, `ALPINEUSDT`, `ALTUSDT`, `ANIMEUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARKMUSDT`, `ARUSDT`, `ASRUSDT`, `ASTERUSDT`, `ATUSDT`, `AUCTIONUSDT`, `AUSDT`, `AVAXUSDT`, `AVNTUSDT`, `AXLUSDT`, `AXSUSDT`, `BANANAS31USDT`, `BARDUSDT`, `BCHUSDT`, `BELUSDT`, `BERAUSDT`, `BIOUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BREVUSDT`, `BROCCOLI714USDT`, `BTCUSDT`, `CAKEUSDT`, `CFGUSDT`, `CFXUSDT`, `CHIPUSDT`, `CKBUSDT`, `COMPUSDT`, `COWUSDT`, `CRVUSDT`, `CTSIUSDT`, `CUSDT`, `CYBERUSDT`, `DASHUSDT`, `DCRUSDT`, `DIAUSDT`, `DOGEUSDT`, `DOGSUSDT`, `DOLOUSDT`, `DOTUSDT`, `DUSKUSDT`, `DYMUSDT`, `EDENUSDT`, `EIGENUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSOUSDT`, `EPICUSDT`, `ERAUSDT`, `ESPUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `EULUSDT`, `FETUSDT`, `FFUSDT`, `FILUSDT`, `FLOKIUSDT`, `FLOWUSDT`, `FLUXUSDT`, `FOGOUSDT`, `FORMUSDT`, `FUSDT`, `GENIUSUSDT`, `GIGGLEUSDT`, `GMXUSDT`, `HBARUSDT`, `HEMIUSDT`, `HFTUSDT`, `HIGHUSDT`, `HOLOUSDT`, `HUMAUSDT`, `HYPERUSDT`, `ICPUSDT`, `ILVUSDT`, `INJUSDT`, `IOUSDT`, `KAIAUSDT`, `KAITOUSDT`, `KATUSDT`, `KERNELUSDT`, `KITEUSDT`, `KNCUSDT`, `LAUSDT`, `LAYERUSDT`, `LDOUSDT`, `LINEAUSDT`, `LINKUSDT`, `LISTAUSDT`, `LPTUSDT`, `LTCUSDT`, `LUNAUSDT`, `LUNCUSDT`, `MAGICUSDT`, `MASKUSDT`, `MAVUSDT`, `MEGAUSDT`, `MEMEUSDT`, `METUSDT`, `MEUSDT`, `MINAUSDT`, `MIRAUSDT`, `MITOUSDT`, `MMTUSDT`, `MORPHOUSDT`, `MOVEUSDT`, `MOVRUSDT`, `NEARUSDT`, `NEIROUSDT`, `NEWTUSDT`, `NIGHTUSDT`, `NMRUSDT`, `NOMUSDT`, `NOTUSDT`, `NXPCUSDT`, `OGUSDT`, `ONDOUSDT`, `ONTUSDT`, `OPENUSDT`, `OPGUSDT`, `OPNUSDT`, `OPUSDT`, `ORCAUSDT`, `ORDIUSDT`, `PENDLEUSDT`, `PENGUUSDT`, `PEPEUSDT`, `PIXELUSDT`, `PLUMEUSDT`, `PNUTUSDT`, `POLUSDT`, `PORTALUSDT`, `PROVEUSDT`, `PUMPUSDT`, `PYRUSDT`, `PYTHUSDT`, `RAYUSDT`, `REDUSDT`, `RESOLVUSDT`, `REZUSDT`, `ROBOUSDT`, `RVNUSDT`, `SAGAUSDT`, `SAHARAUSDT`, `SAPIENUSDT`, `SEIUSDT`, `SENTUSDT`, `SHIBUSDT`, `SIGNUSDT`, `SKLUSDT`, `SLPUSDT`, `SNXUSDT`, `SOLUSDT`, `SOLVUSDT`, `SOMIUSDT`, `SOPHUSDT`, `SPKUSDT`, `STOUSDT`, `STRKUSDT`, `SUIUSDT`, `SUNUSDT`, `SUPERUSDT`, `SUSDT`, `SUSHIUSDT`, `TAOUSDT`, `THEUSDT`, `TNSRUSDT`, `TONUSDT`, `TOWNSUSDT`, `TRBUSDT`, `TREEUSDT`, `TRUMPUSDT`, `TRXUSDT`, `TSTUSDT`, `TURBOUSDT`, `TURTLEUSDT`, `TUTUSDT`, `TWTUSDT`, `UMAUSDT`, `UNIUSDT`, `USD1USDT`, `USUALUSDT`, `VANAUSDT`, `VICUSDT`, `VIRTUALUSDT`, `WALUSDT`, `WBETHUSDT`, `WCTUSDT`, `WIFUSDT`, `WLDUSDT`, `WLFIUSDT`, `WUSDT`, `XAUTUSDT`, `XLMUSDT`, `XPLUSDT`, `XRPUSDT`, `XTZUSDT`, `YBUSDT`, `YGGUSDT`, `ZAMAUSDT`, `ZBTUSDT`, `ZECUSDT`, `ZENUSDT`, `ZKCUSDT`, `ZKPUSDT`, `ZKUSDT`, `ZROUSDT`, `币安人生USDT`
- UTC 区间：2025-06-01T00:00:00+00:00 -> 2026-06-01T00:00:00+00:00
- 初始权益：10,000.00 USDT
- 最终权益：9,389.48 USDT
- 净收益：-6.11%
- 代码 commit：`c8c334766c9339fc96a1c4e2c656772fda1ade9a`
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
- Universe refreshes / Universe 刷新次数：366
- Selected symbols per refresh / 每次入选数量：min=4, avg=16.25, max=40
- Top selected symbols / 最常入选：`BTCUSDT`(366), `ETHUSDT`(366), `SOLUSDT`(366), `XRPUSDT`(360), `BNBUSDT`(344), `DOGEUSDT`(331), `SUIUSDT`(247), `TRXUSDT`(224), `ZECUSDT`(202), `PEPEUSDT`(200)
- Filter counts / 过滤统计：
```json
{
  "missing_1h": 11803,
  "insufficient_24h": 74,
  "reconstruct_error": 0,
  "low_quote_volume": 134937,
  "low_trades": 65,
  "stable_like": 135
}
```
> Warning / 警告：dynamic universe 的 symbol master 来自当前 Binance exchangeInfo；历史上曾交易但今天已退市的币不会进入 master list，因此仍有退市幸存者偏差。
> Runtime / 耗时提示：第一次完整运行需要缓存大量 1h/4h/1d K 线，可能很慢；缓存命中后后续回测会明显加快。

## 核心指标

| Metric（指标） | Value（数值） |
|---|---:|
| Trades（计划总数） | 240 |
| Closed trades（已结束交易） | 51 |
| Open trades（仍开放持仓） | 3 |
| Win rate（胜率） | 25.49% |
| Profit factor（盈利因子） | 0.85 |
| Avg R（平均R倍数） | -0.09 |
| Net return（净收益率） | -6.11% |
| Max drawdown（最大回撤） | 2,415.46 / 21.32% |
| Intrabar max drawdown（K线内最大回撤） | 2,385.66 / 21.14% |
| TP1 touched rate（第一止盈触达率） | 41.18% |
| TP2 close rate（第二止盈平仓率） | 25.49% |
| Stop rate（止损率） | 74.51% |
| Fee drag（手续费拖累） | 89.21 USDT |
| Tail max single loss（最大单笔亏损） | -115.02 USDT |
| CAGR（年化复合收益率） | -6.11% |
| Sharpe（夏普比率） | -0.26 |
| Sortino（索提诺比率） | -0.30 |
| Exposure（持仓暴露时间） | 86.12% |
| Turnover（换手率） | 7.59 |
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
| BTC buy-hold（买入并持有BTC） | -29.49% |
| ETH buy-hold（买入并持有ETH） | -20.22% |
| Cash（现金不交易） | 0.00% |
| Equal-weight symbols（等权持有本次币种） | -52.28% |

## 已结束交易

| Symbol（交易对） | Status（状态） | Created（创建时间） | Entry（入场价） | Exit（出场价） | Qty（数量） | Gross PnL（毛盈亏） | Net PnL（净盈亏） | Net R（净R倍数） | Fees（手续费） | Notes（备注） |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| `ETHUSDT` | STOPPED（已止损） | 2025-06-02T16:00:00+00:00 | 2,553.30 | 2,429.10 | 0.83 | -103.08 | -105.94 | -1.05 | 2.86 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-06-06T16:00:00+00:00 | 105,460.26 | 98,767.81 | 0.02 | -101.23 | -103.37 | -1.04 | 2.13 | Stop loss hit. |
| `TRXUSDT` | STOPPED（已止损） | 2025-06-08T00:00:00+00:00 | 0.28 | 0.26 | 5,242.92 | -101.50 | -103.46 | -1.03 | 1.96 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-06-08T12:00:00+00:00 | 2,522.31 | 2,343.42 | 0.56 | -101.05 | -102.94 | -1.03 | 1.89 | Stop loss hit. |
| `AVAXUSDT` | STOPPED（已止损） | 2025-06-10T00:00:00+00:00 | 21.79 | 19.25 | 40.19 | -102.00 | -103.12 | -1.02 | 1.12 | Stop loss hit. |
| `SOLUSDT` | STOPPED（已止损） | 2025-06-10T00:00:00+00:00 | 160.91 | 144.49 | 6.23 | -102.20 | -103.50 | -1.02 | 1.30 | Stop loss hit. |
| `BNBUSDT` | STOPPED（已止损） | 2025-06-10T12:00:00+00:00 | 660.52 | 636.16 | 4.12 | -100.51 | -104.22 | -1.06 | 3.71 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-06-24T16:00:00+00:00 | 105,613.24 | 96,630.27 | 0.01 | -94.30 | -95.76 | -1.03 | 1.46 | Stop loss hit. |
| `ETHUSDT` | CLOSED（已按TP2平仓） | 2025-06-29T08:00:00+00:00 | 2,449.05 | 2,734.86 | 0.92 | 263.19 | 261.28 | 2.77 | 1.91 | TP2 hit; paper trade closed. |
| `SEIUSDT` | STOPPED（已止损） | 2025-06-30T00:00:00+00:00 | 0.30 | 0.25 | 1,804.34 | -93.68 | -94.33 | -1.01 | 0.66 | Stop loss hit. |
| `SUIUSDT` | CLOSED（已按TP2平仓） | 2025-06-30T00:00:00+00:00 | 2.91 | 3.97 | 255.07 | 269.92 | 269.22 | 2.87 | 0.70 | TP2 hit; paper trade closed. |
| `PEPEUSDT` | CLOSED（已按TP2平仓） | 2025-06-30T20:00:00+00:00 | 0.00 | 0.00 | 94,733,341.21 | 250.84 | 250.00 | 2.63 | 0.85 | TP2 hit; paper trade closed. |
| `WIFUSDT` | CLOSED（已按TP2平仓） | 2025-07-07T00:00:00+00:00 | 0.88 | 1.08 | 1,225.26 | 246.38 | 245.42 | 2.52 | 0.96 | TP2 hit; paper trade closed. |
| `AAVEUSDT` | STOPPED（已止损） | 2025-07-10T04:00:00+00:00 | 296.13 | 273.05 | 4.50 | -103.79 | -105.55 | -1.03 | 1.76 | Stop loss hit. |
| `TRXUSDT` | CLOSED（已按TP2平仓） | 2025-07-13T00:00:00+00:00 | 0.30 | 0.34 | 7,322.68 | 290.52 | 288.64 | 2.69 | 1.87 | TP2 hit; paper trade closed. |
| `DOGEUSDT` | CLOSED（已按TP2平仓） | 2025-07-13T16:00:00+00:00 | 0.20 | 0.26 | 4,741.31 | 276.47 | 275.60 | 2.58 | 0.87 | TP2 hit; paper trade closed. |
| `PENGUUSDT` | CLOSED（已按TP2平仓） | 2025-07-19T08:00:00+00:00 | 0.03 | 0.04 | 30,306.49 | 260.42 | 259.54 | 2.33 | 0.88 | TP2 hit; paper trade closed. |
| `HBARUSDT` | STOPPED（已止损） | 2025-07-19T16:00:00+00:00 | 0.27 | 0.23 | 2,695.08 | -113.04 | -113.93 | -1.01 | 0.89 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-07-27T20:00:00+00:00 | 3,787.59 | 3,516.63 | 0.42 | -112.80 | -114.90 | -1.03 | 2.09 | Stop loss hit. |
| `CAKEUSDT` | STOPPED（已止损） | 2025-07-28T16:00:00+00:00 | 3.00 | 2.57 | 264.55 | -114.02 | -115.02 | -1.01 | 1.00 | Stop loss hit. |
| `CFXUSDT` | STOPPED（已止损） | 2025-07-30T00:00:00+00:00 | 0.21 | 0.18 | 3,740.09 | -109.24 | -110.21 | -1.02 | 0.97 | Stop loss hit. |
| `ENAUSDT` | STOPPED（已止损） | 2025-07-31T00:00:00+00:00 | 0.61 | 0.52 | 1,261.17 | -108.27 | -109.24 | -1.02 | 0.97 | Stop loss hit. |
| `LTCUSDT` | STOPPED（已止损） | 2025-08-08T00:00:00+00:00 | 121.19 | 113.35 | 14.16 | -111.03 | -113.32 | -1.04 | 2.29 | Stop loss hit. |
| `OPUSDT` | STOPPED（已止损） | 2025-08-14T08:00:00+00:00 | 0.83 | 0.71 | 925.09 | -108.58 | -109.54 | -1.01 | 0.96 | Stop loss hit. |
| `PENDLEUSDT` | STOPPED（已止损） | 2025-08-15T08:00:00+00:00 | 5.44 | 4.97 | 228.27 | -106.77 | -108.41 | -1.03 | 1.63 | Stop loss hit. |
| `WIFUSDT` | STOPPED（已止损） | 2025-08-23T00:00:00+00:00 | 0.94 | 0.78 | 674.78 | -105.89 | -106.67 | -1.01 | 0.78 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-08-24T12:00:00+00:00 | 4,691.33 | 4,137.00 | 0.19 | -103.05 | -104.17 | -1.02 | 1.12 | Stop loss hit. |
| `AVAXUSDT` | CLOSED（已按TP2平仓） | 2025-09-16T00:00:00+00:00 | 29.85 | 34.86 | 49.65 | 248.93 | 247.65 | 2.43 | 1.29 | TP2 hit; paper trade closed. |
| `BNBUSDT` | CLOSED（已按TP2平仓） | 2025-09-16T08:00:00+00:00 | 930.05 | 1,025.84 | 3.11 | 298.11 | 295.67 | 2.87 | 2.43 | TP2 hit; paper trade closed. |
| `XRPUSDT` | STOPPED（已止损） | 2025-09-16T12:00:00+00:00 | 3.04 | 2.91 | 822.72 | -109.84 | -113.23 | -1.05 | 3.39 | Stop loss hit. |
| `BIOUSDT` | STOPPED（已止损） | 2025-09-21T00:00:00+00:00 | 0.18 | 0.16 | 4,716.49 | -107.49 | -108.59 | -1.02 | 1.10 | Stop loss hit. |
| `BNBUSDT` | STOPPED（已止损） | 2025-09-21T12:00:00+00:00 | 1,025.08 | 958.33 | 1.57 | -104.60 | -106.74 | -1.04 | 2.14 | Stop loss hit. |
| `CAKEUSDT` | STOPPED（已止损） | 2025-09-21T12:00:00+00:00 | 2.89 | 2.59 | 354.34 | -105.31 | -106.63 | -1.02 | 1.33 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-10-01T12:00:00+00:00 | 4,306.31 | 3,902.60 | 0.26 | -102.97 | -104.41 | -1.02 | 1.43 | Stop loss hit. |
| `SOLUSDT` | STOPPED（已止损） | 2025-10-02T00:00:00+00:00 | 220.00 | 201.02 | 5.45 | -103.50 | -105.08 | -1.03 | 1.58 | Stop loss hit. |
| `LINKUSDT` | STOPPED（已止损） | 2025-10-02T00:00:00+00:00 | 22.59 | 20.57 | 51.21 | -103.64 | -105.16 | -1.03 | 1.52 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-10-26T16:00:00+00:00 | 4,060.46 | 3,757.68 | 0.33 | -98.84 | -100.59 | -1.03 | 1.76 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-11-27T16:00:00+00:00 | 2,996.52 | 2,797.38 | 0.48 | -96.23 | -98.16 | -1.03 | 1.93 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-11-30T04:00:00+00:00 | 91,152.21 | 88,714.33 | 0.04 | -99.68 | -104.80 | -1.09 | 5.12 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-12-03T08:00:00+00:00 | 93,325.63 | 82,482.85 | 0.01 | -93.23 | -94.26 | -1.02 | 1.03 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-12-07T20:00:00+00:00 | 3,107.08 | 2,861.04 | 0.38 | -93.54 | -95.10 | -1.03 | 1.56 | Stop loss hit. |
| `ETHUSDT` | CLOSED（已按TP2平仓） | 2025-12-31T00:00:00+00:00 | 2,984.10 | 3,318.38 | 0.78 | 261.48 | 259.50 | 2.82 | 1.97 | TP2 hit; paper trade closed. |
| `ETHUSDT` | STOPPED（已止损） | 2026-01-17T16:00:00+00:00 | 3,319.13 | 3,201.01 | 0.83 | -97.96 | -101.72 | -1.07 | 3.76 | Stop loss hit. |
| `BNBUSDT` | STOPPED（已止损） | 2026-01-18T00:00:00+00:00 | 944.78 | 908.92 | 2.72 | -97.65 | -101.16 | -1.06 | 3.50 | Stop loss hit. |
| `DASHUSDT` | STOPPED（已止损） | 2026-01-18T12:00:00+00:00 | 80.43 | 70.28 | 9.38 | -95.20 | -96.16 | -1.02 | 0.96 | Stop loss hit. |
| `SOLUSDT` | CLOSED（已按TP2平仓） | 2026-04-16T00:00:00+00:00 | 85.20 | 98.36 | 18.56 | 244.31 | 242.95 | 2.61 | 1.36 | TP2 hit; paper trade closed. |
| `BNBUSDT` | CLOSED（已按TP2平仓） | 2026-04-16T00:00:00+00:00 | 618.86 | 718.19 | 2.59 | 257.67 | 256.28 | 2.73 | 1.39 | TP2 hit; paper trade closed. |
| `DOGEUSDT` | CLOSED（已按TP2平仓） | 2026-04-16T00:00:00+00:00 | 0.09 | 0.11 | 16,900.90 | 237.40 | 236.02 | 2.53 | 1.38 | TP2 hit; paper trade closed. |
| `PEPEUSDT` | STOPPED（已止损） | 2026-05-11T00:00:00+00:00 | 0.00 | 0.00 | 301,821,903.05 | -100.66 | -102.40 | -1.03 | 1.74 | Stop loss hit. |
| `SOLUSDT` | STOPPED（已止损） | 2026-05-12T00:00:00+00:00 | 95.59 | 90.38 | 19.18 | -99.82 | -102.28 | -1.04 | 2.47 | Stop loss hit. |
| `XRPUSDT` | STOPPED（已止损） | 2026-05-12T04:00:00+00:00 | 1.46 | 1.39 | 1,309.85 | -99.64 | -102.23 | -1.05 | 2.59 | Stop loss hit. |

## 回测结束仍开放

| Symbol（交易对） | Status（状态） | Entry（入场价） | Qty（数量） | Unrealized Handling（未实现盈亏处理） | Notes（备注） |
|---|---|---:|---:|---|---|
| `ETHUSDT` | TP1_HIT（第一止盈已触达） | 1,990.26 | 0.50 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |
| `BTCUSDT` | TP1_HIT（第一止盈已触达） | 69,208.02 | 0.01 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |
| `ZBTUSDT` | ENTERED（已入场） | 0.17 | 1,813.24 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |

## 未入场/过期计划

| Symbol（交易对） | Status（状态） | Created（创建时间） | Entry Zone（入场区间） | Score（评分） | Notes（备注） |
|---|---|---|---:|---:|---|
| `XRPUSDT` | EXPIRED（观察计划过期） | 2025-06-10T00:00:00+00:00 | 2.25 - 2.27 | 63.43 | Backtest WATCHING plan expired before entry. |
| `SUIUSDT` | EXPIRED（观察计划过期） | 2025-06-10T00:00:00+00:00 | 3.38 - 3.42 | 51.55 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-06-10T00:00:00+00:00 | 0.70 - 0.71 | 48.97 | Backtest WATCHING plan expired before entry. |
| `PEPEUSDT` | INVALIDATED（未入场前失效） | 2025-06-10T04:00:00+00:00 | 0.00 - 0.00 | 53.69 | Plan invalidated before entry: current price is below stop loss. |
| `ENAUSDT` | INVALIDATED（未入场前失效） | 2025-06-10T08:00:00+00:00 | 0.34 - 0.34 | 59.20 | Plan invalidated before entry: current price is below stop loss. |
| `DOGEUSDT` | INVALIDATED（未入场前失效） | 2025-06-11T00:00:00+00:00 | 0.20 - 0.20 | 54.27 | Plan invalidated before entry: current price is below stop loss. |
| `UNIUSDT` | INVALIDATED（未入场前失效） | 2025-06-30T04:00:00+00:00 | 7.11 - 7.20 | 73.42 | Plan invalidated before entry: current price is below stop loss. |
| `DOGEUSDT` | EXPIRED（观察计划过期） | 2025-06-30T04:00:00+00:00 | 0.16 - 0.17 | 52.96 | Backtest WATCHING plan expired before entry. |
| `XRPUSDT` | EXPIRED（观察计划过期） | 2025-06-30T08:00:00+00:00 | 2.18 - 2.19 | 64.22 | Backtest WATCHING plan expired before entry. |
| `SOLUSDT` | EXPIRED（观察计划过期） | 2025-06-30T08:00:00+00:00 | 148.74 - 150.23 | 56.87 | Backtest WATCHING plan expired before entry. |
| `ARBUSDT` | EXPIRED（观察计划过期） | 2025-06-30T16:00:00+00:00 | 0.33 - 0.34 | 69.82 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-01T00:00:00+00:00 | 652.84 - 653.99 | 57.15 | Backtest WATCHING plan expired before entry. |
| `TRXUSDT` | EXPIRED（观察计划过期） | 2025-07-01T12:00:00+00:00 | 0.28 - 0.28 | 60.47 | Backtest WATCHING plan expired before entry. |
| `UNIUSDT` | EXPIRED（观察计划过期） | 2025-07-03T00:00:00+00:00 | 7.11 - 7.25 | 73.17 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-07-03T08:00:00+00:00 | 0.59 - 0.60 | 66.10 | Backtest WATCHING plan expired before entry. |
| `DOGEUSDT` | EXPIRED（观察计划过期） | 2025-07-03T08:00:00+00:00 | 0.17 - 0.17 | 65.98 | Backtest WATCHING plan expired before entry. |
| `XRPUSDT` | EXPIRED（观察计划过期） | 2025-07-03T12:00:00+00:00 | 2.23 - 2.25 | 71.85 | Backtest WATCHING plan expired before entry. |
| `SOLUSDT` | EXPIRED（观察计划过期） | 2025-07-03T12:00:00+00:00 | 151.60 - 153.27 | 69.74 | Backtest WATCHING plan expired before entry. |
| `WIFUSDT` | EXPIRED（观察计划过期） | 2025-07-03T16:00:00+00:00 | 0.86 - 0.88 | 69.72 | Backtest WATCHING plan expired before entry. |
| `LTCUSDT` | EXPIRED（观察计划过期） | 2025-07-04T00:00:00+00:00 | 87.66 - 88.60 | 68.21 | Backtest WATCHING plan expired before entry. |
| `PNUTUSDT` | EXPIRED（观察计划过期） | 2025-07-04T00:00:00+00:00 | 0.23 - 0.24 | 68.13 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-04T04:00:00+00:00 | 659.14 - 661.18 | 57.11 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-07-04T16:00:00+00:00 | 0.00 - 0.00 | 71.04 | Backtest WATCHING plan expired before entry. |
| `SOLUSDT` | EXPIRED（观察计划过期） | 2025-07-06T16:00:00+00:00 | 149.21 - 150.31 | 61.58 | Backtest WATCHING plan expired before entry. |
| `XRPUSDT` | EXPIRED（观察计划过期） | 2025-07-06T16:00:00+00:00 | 2.24 - 2.25 | 57.68 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-07T08:00:00+00:00 | 659.71 - 660.49 | 56.33 | Backtest WATCHING plan expired before entry. |
| `DOGEUSDT` | EXPIRED（观察计划过期） | 2025-07-07T12:00:00+00:00 | 0.17 - 0.17 | 59.67 | Backtest WATCHING plan expired before entry. |
| `UNIUSDT` | EXPIRED（观察计划过期） | 2025-07-07T12:00:00+00:00 | 7.29 - 7.39 | 55.05 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-07-08T20:00:00+00:00 | 0.00 - 0.00 | 84.85 | Backtest WATCHING plan expired before entry. |
| `SOLUSDT` | EXPIRED（观察计划过期） | 2025-07-09T20:00:00+00:00 | 152.10 - 153.56 | 67.53 | Backtest WATCHING plan expired before entry. |
| `XRPUSDT` | EXPIRED（观察计划过期） | 2025-07-10T00:00:00+00:00 | 2.33 - 2.35 | 71.60 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-10T12:00:00+00:00 | 665.56 - 666.92 | 59.24 | Backtest WATCHING plan expired before entry. |
| `LINKUSDT` | EXPIRED（观察计划过期） | 2025-07-12T00:00:00+00:00 | 14.76 - 15.01 | 69.45 | Backtest WATCHING plan expired before entry. |
| `TONUSDT` | EXPIRED（观察计划过期） | 2025-07-12T00:00:00+00:00 | 2.91 - 2.94 | 58.93 | Backtest WATCHING plan expired before entry. |
| `SHIBUSDT` | EXPIRED（观察计划过期） | 2025-07-12T08:00:00+00:00 | 0.00 - 0.00 | 66.79 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-07-12T16:00:00+00:00 | 0.00 - 0.00 | 75.65 | Backtest WATCHING plan expired before entry. |
| `HBARUSDT` | EXPIRED（观察计划过期） | 2025-07-13T00:00:00+00:00 | 0.19 - 0.20 | 79.39 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-07-13T08:00:00+00:00 | 2,901.59 - 2,932.21 | 68.11 | Backtest WATCHING plan expired before entry. |
| `SOLUSDT` | EXPIRED（观察计划过期） | 2025-07-13T12:00:00+00:00 | 160.85 - 162.55 | 53.07 | Backtest WATCHING plan expired before entry. |
| `UNIUSDT` | EXPIRED（观察计划过期） | 2025-07-13T16:00:00+00:00 | 8.44 - 8.60 | 66.08 | Backtest WATCHING plan expired before entry. |
| `WIFUSDT` | EXPIRED（观察计划过期） | 2025-07-14T16:00:00+00:00 | 1.00 - 1.01 | 71.24 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-07-14T16:00:00+00:00 | 21.09 - 21.43 | 68.12 | Backtest WATCHING plan expired before entry. |
| `PNUTUSDT` | EXPIRED（观察计划过期） | 2025-07-15T16:00:00+00:00 | 0.27 - 0.28 | 72.20 | Backtest WATCHING plan expired before entry. |
| `PEPEUSDT` | EXPIRED（观察计划过期） | 2025-07-15T16:00:00+00:00 | 0.00 - 0.00 | 71.30 | Backtest WATCHING plan expired before entry. |
| `NEIROUSDT` | EXPIRED（观察计划过期） | 2025-07-15T16:00:00+00:00 | 0.00 - 0.00 | 70.58 | Backtest WATCHING plan expired before entry. |
| `USUALUSDT` | EXPIRED（观察计划过期） | 2025-07-15T20:00:00+00:00 | 0.09 - 0.09 | 76.50 | Backtest WATCHING plan expired before entry. |
| `ENAUSDT` | EXPIRED（观察计划过期） | 2025-07-16T04:00:00+00:00 | 0.34 - 0.35 | 81.68 | Backtest WATCHING plan expired before entry. |
| `ARBUSDT` | EXPIRED（观察计划过期） | 2025-07-16T12:00:00+00:00 | 0.42 - 0.43 | 81.05 | Backtest WATCHING plan expired before entry. |
| `SUIUSDT` | EXPIRED（观察计划过期） | 2025-07-16T16:00:00+00:00 | 3.86 - 3.94 | 81.52 | Backtest WATCHING plan expired before entry. |
| `XLMUSDT` | EXPIRED（观察计划过期） | 2025-07-16T20:00:00+00:00 | 0.45 - 0.46 | 76.07 | Backtest WATCHING plan expired before entry. |
| `TRUMPUSDT` | EXPIRED（观察计划过期） | 2025-07-18T00:00:00+00:00 | 9.77 - 10.01 | 56.82 | Backtest WATCHING plan expired before entry. |
| `UNIUSDT` | EXPIRED（观察计划过期） | 2025-07-18T00:00:00+00:00 | 8.69 - 8.93 | 40.18 | Backtest WATCHING plan expired before entry. |
| `LINKUSDT` | EXPIRED（观察计划过期） | 2025-07-18T20:00:00+00:00 | 17.22 - 17.63 | 77.87 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-07-18T20:00:00+00:00 | 0.80 - 0.82 | 76.43 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-07-18T20:00:00+00:00 | 22.96 - 23.49 | 75.25 | Backtest WATCHING plan expired before entry. |
| `OPUSDT` | EXPIRED（观察计划过期） | 2025-07-19T00:00:00+00:00 | 0.73 - 0.75 | 75.52 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-07-19T20:00:00+00:00 | 3,472.71 - 3,527.19 | 71.70 | Backtest WATCHING plan expired before entry. |
| `XRPUSDT` | EXPIRED（观察计划过期） | 2025-07-20T00:00:00+00:00 | 3.33 - 3.42 | 73.72 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-07-20T20:00:00+00:00 | 0.00 - 0.00 | 70.99 | Backtest WATCHING plan expired before entry. |
| `SHIBUSDT` | INVALIDATED（未入场前失效） | 2025-07-21T04:00:00+00:00 | 0.00 - 0.00 | 69.27 | Plan invalidated before entry: current price is below stop loss. |
| `NEIROUSDT` | INVALIDATED（未入场前失效） | 2025-07-21T04:00:00+00:00 | 0.00 - 0.00 | 68.59 | Plan invalidated before entry: current price is below stop loss. |
| `ADAUSDT` | INVALIDATED（未入场前失效） | 2025-07-22T00:00:00+00:00 | 0.86 - 0.88 | 74.74 | Plan invalidated before entry: current price is below stop loss. |
| `LINKUSDT` | INVALIDATED（未入场前失效） | 2025-07-22T00:00:00+00:00 | 18.98 - 19.37 | 73.81 | Plan invalidated before entry: current price is below stop loss. |
| `UNIUSDT` | INVALIDATED（未入场前失效） | 2025-07-22T00:00:00+00:00 | 10.46 - 10.73 | 71.87 | Plan invalidated before entry: current price is below stop loss. |
| `FLOKIUSDT` | INVALIDATED（未入场前失效） | 2025-07-22T04:00:00+00:00 | 0.00 - 0.00 | 76.73 | Plan invalidated before entry: current price is below stop loss. |
| `TAOUSDT` | EXPIRED（观察计划过期） | 2025-07-22T16:00:00+00:00 | 429.87 - 440.88 | 64.80 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-23T00:00:00+00:00 | 759.88 - 769.08 | 72.70 | Backtest WATCHING plan expired before entry. |
| `CRVUSDT` | EXPIRED（观察计划过期） | 2025-07-23T04:00:00+00:00 | 0.97 - 0.99 | 71.48 | Backtest WATCHING plan expired before entry. |
| `WLDUSDT` | INVALIDATED（未入场前失效） | 2025-07-23T16:00:00+00:00 | 1.25 - 1.25 | 66.68 | Plan invalidated before entry: current price is below stop loss. |
| `WIFUSDT` | INVALIDATED（未入场前失效） | 2025-07-23T16:00:00+00:00 | 1.21 - 1.22 | 53.03 | Plan invalidated before entry: current price is below stop loss. |
| `CFXUSDT` | EXPIRED（观察计划过期） | 2025-07-24T08:00:00+00:00 | 0.18 - 0.18 | 57.69 | Backtest WATCHING plan expired before entry. |
| `ENAUSDT` | EXPIRED（观察计划过期） | 2025-07-24T12:00:00+00:00 | 0.48 - 0.48 | 62.68 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-07-24T16:00:00+00:00 | 3,675.13 - 3,734.05 | 66.35 | Backtest WATCHING plan expired before entry. |
| `UNIUSDT` | EXPIRED（观察计划过期） | 2025-07-24T16:00:00+00:00 | 10.36 - 10.39 | 65.65 | Backtest WATCHING plan expired before entry. |
| `LTCUSDT` | EXPIRED（观察计划过期） | 2025-07-24T20:00:00+00:00 | 110.47 - 113.09 | 40.55 | Backtest WATCHING plan expired before entry. |
| `LINKUSDT` | EXPIRED（观察计划过期） | 2025-07-24T20:00:00+00:00 | 18.22 - 18.40 | 37.97 | Backtest WATCHING plan expired before entry. |
| `BCHUSDT` | EXPIRED（观察计划过期） | 2025-07-25T00:00:00+00:00 | 510.37 - 514.54 | 36.35 | Backtest WATCHING plan expired before entry. |
| `SUIUSDT` | EXPIRED（观察计划过期） | 2025-07-25T20:00:00+00:00 | 3.81 - 3.85 | 41.41 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-07-26T04:00:00+00:00 | 0.00 - 0.00 | 66.86 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-26T08:00:00+00:00 | 775.08 - 784.43 | 59.80 | Backtest WATCHING plan expired before entry. |
| `CRVUSDT` | EXPIRED（观察计划过期） | 2025-07-27T16:00:00+00:00 | 1.04 - 1.05 | 64.71 | Backtest WATCHING plan expired before entry. |
| `SOLUSDT` | INVALIDATED（未入场前失效） | 2025-07-27T20:00:00+00:00 | 186.84 - 187.48 | 61.00 | Plan invalidated before entry: current price is below stop loss. |
| `PENGUUSDT` | INVALIDATED（未入场前失效） | 2025-07-28T00:00:00+00:00 | 0.04 - 0.04 | 81.80 | Plan invalidated before entry: current price is below stop loss. |
| `UNIUSDT` | INVALIDATED（未入场前失效） | 2025-07-28T12:00:00+00:00 | 10.67 - 10.81 | 62.59 | Plan invalidated before entry: current price is below stop loss. |
| `AVAXUSDT` | INVALIDATED（未入场前失效） | 2025-07-28T16:00:00+00:00 | 25.38 - 25.79 | 68.81 | Plan invalidated before entry: current price is below stop loss. |
| `TRXUSDT` | EXPIRED（观察计划过期） | 2025-07-29T16:00:00+00:00 | 0.33 - 0.33 | 72.81 | Backtest WATCHING plan expired before entry. |
| `CRVUSDT` | INVALIDATED（未入场前失效） | 2025-07-30T20:00:00+00:00 | 1.01 - 1.03 | 66.23 | Plan invalidated before entry: current price is below stop loss. |
| `TONUSDT` | EXPIRED（观察计划过期） | 2025-07-31T00:00:00+00:00 | 3.34 - 3.40 | 65.42 | Backtest WATCHING plan expired before entry. |
| `XRPUSDT` | INVALIDATED（未入场前失效） | 2025-07-31T04:00:00+00:00 | 3.15 - 3.15 | 40.70 | Plan invalidated before entry: current price is below stop loss. |
| `SUIUSDT` | INVALIDATED（未入场前失效） | 2025-07-31T04:00:00+00:00 | 3.78 - 3.85 | 35.53 | Plan invalidated before entry: current price is below stop loss. |
| `LINKUSDT` | INVALIDATED（未入场前失效） | 2025-07-31T08:00:00+00:00 | 18.04 - 18.08 | 47.35 | Plan invalidated before entry: current price is below stop loss. |
| `BNBUSDT` | INVALIDATED（未入场前失效） | 2025-07-31T08:00:00+00:00 | 795.60 - 804.81 | 38.20 | Plan invalidated before entry: current price is below stop loss. |
| `TRXUSDT` | EXPIRED（观察计划过期） | 2025-08-08T00:00:00+00:00 | 0.34 - 0.34 | 63.32 | Backtest WATCHING plan expired before entry. |
| `BCHUSDT` | EXPIRED（观察计划过期） | 2025-08-08T00:00:00+00:00 | 569.87 - 576.42 | 61.79 | Backtest WATCHING plan expired before entry. |
| `SOLUSDT` | EXPIRED（观察计划过期） | 2025-08-08T00:00:00+00:00 | 172.32 - 174.39 | 50.66 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-08-08T00:00:00+00:00 | 22.80 - 23.08 | 49.26 | Backtest WATCHING plan expired before entry. |
| `ENAUSDT` | EXPIRED（观察计划过期） | 2025-08-08T08:00:00+00:00 | 0.61 - 0.63 | 69.59 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-08-08T08:00:00+00:00 | 773.64 - 778.88 | 60.60 | Backtest WATCHING plan expired before entry. |
| `XRPUSDT` | EXPIRED（观察计划过期） | 2025-08-08T16:00:00+00:00 | 3.14 - 3.19 | 75.28 | Backtest WATCHING plan expired before entry. |
| `PENGUUSDT` | EXPIRED（观察计划过期） | 2025-08-08T16:00:00+00:00 | 0.04 - 0.04 | 67.03 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-08-08T16:00:00+00:00 | 0.76 - 0.77 | 65.29 | Backtest WATCHING plan expired before entry. |
| `SUIUSDT` | EXPIRED（观察计划过期） | 2025-08-08T16:00:00+00:00 | 3.65 - 3.72 | 63.32 | Backtest WATCHING plan expired before entry. |
| `SOLUSDT` | EXPIRED（观察计划过期） | 2025-08-11T04:00:00+00:00 | 179.54 - 181.92 | 72.49 | Backtest WATCHING plan expired before entry. |
| `TRXUSDT` | EXPIRED（观察计划过期） | 2025-08-11T04:00:00+00:00 | 0.34 - 0.34 | 58.58 | Backtest WATCHING plan expired before entry. |
| `UNIUSDT` | EXPIRED（观察计划过期） | 2025-08-11T08:00:00+00:00 | 10.81 - 11.03 | 70.67 | Backtest WATCHING plan expired before entry. |
| `DOGEUSDT` | EXPIRED（观察计划过期） | 2025-08-11T08:00:00+00:00 | 0.23 - 0.23 | 67.47 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-08-11T12:00:00+00:00 | 4,146.78 - 4,197.66 | 71.09 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-08-11T16:00:00+00:00 | 801.89 - 809.22 | 62.06 | Backtest WATCHING plan expired before entry. |
| `PENDLEUSDT` | EXPIRED（观察计划过期） | 2025-08-12T04:00:00+00:00 | 5.36 - 5.51 | 67.66 | Backtest WATCHING plan expired before entry. |
| `LINKUSDT` | EXPIRED（观察计划过期） | 2025-08-12T12:00:00+00:00 | 21.20 - 21.36 | 72.34 | Backtest WATCHING plan expired before entry. |
| `PEPEUSDT` | INVALIDATED（未入场前失效） | 2025-08-12T16:00:00+00:00 | 0.00 - 0.00 | 68.08 | Plan invalidated before entry: current price is below stop loss. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-08-12T16:00:00+00:00 | 0.79 - 0.81 | 65.38 | Backtest WATCHING plan expired before entry. |
| `SUIUSDT` | EXPIRED（观察计划过期） | 2025-08-14T08:00:00+00:00 | 3.92 - 3.99 | 73.83 | Backtest WATCHING plan expired before entry. |
| `ETHFIUSDT` | INVALIDATED（未入场前失效） | 2025-08-14T12:00:00+00:00 | 1.26 - 1.30 | 75.31 | Plan invalidated before entry: current price is below stop loss. |
| `NEARUSDT` | EXPIRED（观察计划过期） | 2025-08-14T12:00:00+00:00 | 2.86 - 2.91 | 66.97 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-08-15T08:00:00+00:00 | 24.58 - 25.09 | 67.53 | Backtest WATCHING plan expired before entry. |
| `ENAUSDT` | EXPIRED（观察计划过期） | 2025-08-15T08:00:00+00:00 | 0.73 - 0.74 | 42.46 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-08-15T20:00:00+00:00 | 0.91 - 0.93 | 73.08 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | INVALIDATED（未入场前失效） | 2025-08-17T04:00:00+00:00 | 4,376.86 - 4,430.92 | 37.85 | Plan invalidated before entry: current price is below stop loss. |
| `PEPEUSDT` | INVALIDATED（未入场前失效） | 2025-08-23T00:00:00+00:00 | 0.00 - 0.00 | 61.33 | Plan invalidated before entry: current price is below stop loss. |
| `SUIUSDT` | EXPIRED（观察计划过期） | 2025-08-23T00:00:00+00:00 | 3.68 - 3.74 | 60.68 | Backtest WATCHING plan expired before entry. |
| `LINKUSDT` | INVALIDATED（未入场前失效） | 2025-08-23T04:00:00+00:00 | 25.53 - 26.03 | 78.34 | Plan invalidated before entry: current price is below stop loss. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-08-23T04:00:00+00:00 | 861.81 - 871.06 | 71.00 | Backtest WATCHING plan expired before entry. |
| `PENGUUSDT` | EXPIRED（观察计划过期） | 2025-08-23T04:00:00+00:00 | 0.03 - 0.03 | 66.08 | Backtest WATCHING plan expired before entry. |
| `TRXUSDT` | INVALIDATED（未入场前失效） | 2025-08-23T04:00:00+00:00 | 0.36 - 0.36 | 65.71 | Plan invalidated before entry: current price is below stop loss. |
| `DOTUSDT` | EXPIRED（观察计划过期） | 2025-08-23T04:00:00+00:00 | 3.95 - 4.01 | 58.40 | Backtest WATCHING plan expired before entry. |
| `LTCUSDT` | INVALIDATED（未入场前失效） | 2025-08-23T08:00:00+00:00 | 118.50 - 120.04 | 55.73 | Plan invalidated before entry: current price is below stop loss. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-08-23T12:00:00+00:00 | 0.89 - 0.91 | 71.43 | Backtest WATCHING plan expired before entry. |
| `TRXUSDT` | EXPIRED（观察计划过期） | 2025-09-16T12:00:00+00:00 | 0.35 - 0.35 | 36.62 | Backtest WATCHING plan expired before entry. |
| `SUIUSDT` | EXPIRED（观察计划过期） | 2025-09-16T16:00:00+00:00 | 3.62 - 3.63 | 51.69 | Backtest WATCHING plan expired before entry. |
| `SOLUSDT` | EXPIRED（观察计划过期） | 2025-09-16T16:00:00+00:00 | 237.46 - 238.50 | 51.56 | Backtest WATCHING plan expired before entry. |
| `DOGEUSDT` | EXPIRED（观察计划过期） | 2025-09-16T16:00:00+00:00 | 0.26 - 0.27 | 35.42 | Backtest WATCHING plan expired before entry. |
| `PENGUUSDT` | EXPIRED（观察计划过期） | 2025-09-16T16:00:00+00:00 | 0.03 - 0.03 | 35.08 | Backtest WATCHING plan expired before entry. |
| `PEPEUSDT` | EXPIRED（观察计划过期） | 2025-09-16T20:00:00+00:00 | 0.00 - 0.00 | 36.57 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-09-17T08:00:00+00:00 | 0.88 - 0.88 | 50.38 | Backtest WATCHING plan expired before entry. |
| `HBARUSDT` | EXPIRED（观察计划过期） | 2025-09-18T00:00:00+00:00 | 0.24 - 0.24 | 64.91 | Backtest WATCHING plan expired before entry. |
| `LTCUSDT` | EXPIRED（观察计划过期） | 2025-09-18T00:00:00+00:00 | 115.27 - 116.23 | 60.92 | Backtest WATCHING plan expired before entry. |
| `LINKUSDT` | INVALIDATED（未入场前失效） | 2025-09-19T08:00:00+00:00 | 24.12 - 24.41 | 64.31 | Plan invalidated before entry: current price is below stop loss. |
| `NEARUSDT` | INVALIDATED（未入场前失效） | 2025-09-21T00:00:00+00:00 | 3.06 - 3.14 | 67.13 | Plan invalidated before entry: current price is below stop loss. |
| `SUIUSDT` | EXPIRED（观察计划过期） | 2025-10-02T00:00:00+00:00 | 3.42 - 3.46 | 66.79 | Backtest WATCHING plan expired before entry. |
| `XRPUSDT` | EXPIRED（观察计划过期） | 2025-10-02T00:00:00+00:00 | 2.91 - 2.94 | 65.83 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-10-02T00:00:00+00:00 | 0.84 - 0.84 | 64.07 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-10-02T04:00:00+00:00 | 1,013.18 - 1,021.09 | 65.73 | Backtest WATCHING plan expired before entry. |
| `PENGUUSDT` | EXPIRED（观察计划过期） | 2025-10-02T04:00:00+00:00 | 0.03 - 0.03 | 63.98 | Backtest WATCHING plan expired before entry. |
| `NEARUSDT` | EXPIRED（观察计划过期） | 2025-10-02T04:00:00+00:00 | 2.81 - 2.85 | 56.82 | Backtest WATCHING plan expired before entry. |
| `TRXUSDT` | EXPIRED（观察计划过期） | 2025-10-02T04:00:00+00:00 | 0.34 - 0.34 | 51.65 | Backtest WATCHING plan expired before entry. |
| `PEPEUSDT` | EXPIRED（观察计划过期） | 2025-10-02T12:00:00+00:00 | 0.00 - 0.00 | 55.97 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-10-02T20:00:00+00:00 | 30.34 - 30.77 | 55.07 | Backtest WATCHING plan expired before entry. |
| `ENAUSDT` | EXPIRED（观察计划过期） | 2025-10-03T04:00:00+00:00 | 0.60 - 0.61 | 55.01 | Backtest WATCHING plan expired before entry. |
| `SUIUSDT` | INVALIDATED（未入场前失效） | 2025-10-05T04:00:00+00:00 | 3.54 - 3.58 | 67.11 | Plan invalidated before entry: current price is below stop loss. |
| `DOGEUSDT` | EXPIRED（观察计划过期） | 2025-10-05T04:00:00+00:00 | 0.25 - 0.26 | 65.55 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | INVALIDATED（未入场前失效） | 2025-10-05T04:00:00+00:00 | 0.85 - 0.86 | 51.26 | Plan invalidated before entry: current price is below stop loss. |
| `XRPUSDT` | INVALIDATED（未入场前失效） | 2025-10-05T08:00:00+00:00 | 3.00 - 3.02 | 62.24 | Plan invalidated before entry: current price is below stop loss. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-10-05T12:00:00+00:00 | 1,131.18 - 1,149.27 | 72.89 | Backtest WATCHING plan expired before entry. |
| `PEPEUSDT` | INVALIDATED（未入场前失效） | 2025-10-05T16:00:00+00:00 | 0.00 - 0.00 | 54.73 | Plan invalidated before entry: current price is below stop loss. |
| `APTUSDT` | EXPIRED（观察计划过期） | 2025-10-05T20:00:00+00:00 | 5.26 - 5.38 | 76.12 | Backtest WATCHING plan expired before entry. |
| `PENGUUSDT` | EXPIRED（观察计划过期） | 2025-10-06T00:00:00+00:00 | 0.03 - 0.03 | 64.05 | Backtest WATCHING plan expired before entry. |
| `TRXUSDT` | EXPIRED（观察计划过期） | 2025-10-06T00:00:00+00:00 | 0.34 - 0.34 | 48.48 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | INVALIDATED（未入场前失效） | 2025-10-06T12:00:00+00:00 | 30.44 - 30.59 | 36.49 | Plan invalidated before entry: current price is below stop loss. |
| `FORMUSDT` | INVALIDATED（未入场前失效） | 2025-10-08T08:00:00+00:00 | 1.41 - 1.46 | 75.54 | Plan invalidated before entry: current price is below stop loss. |
| `BNBUSDT` | INVALIDATED（未入场前失效） | 2025-10-08T16:00:00+00:00 | 1,249.87 - 1,275.74 | 83.10 | Plan invalidated before entry: current price is below stop loss. |
| `DOGEUSDT` | INVALIDATED（未入场前失效） | 2025-10-08T16:00:00+00:00 | 0.25 - 0.25 | 47.37 | Plan invalidated before entry: current price is below stop loss. |
| `NEARUSDT` | INVALIDATED（未入场前失效） | 2025-10-08T20:00:00+00:00 | 2.97 - 3.00 | 60.40 | Plan invalidated before entry: current price is below stop loss. |
| `FLOKIUSDT` | INVALIDATED（未入场前失效） | 2025-10-08T20:00:00+00:00 | 0.00 - 0.00 | 54.13 | Plan invalidated before entry: current price is below stop loss. |
| `SUIUSDT` | INVALIDATED（未入场前失效） | 2025-10-08T20:00:00+00:00 | 3.54 - 3.55 | 49.80 | Plan invalidated before entry: current price is below stop loss. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2026-01-14T12:00:00+00:00 | 3,202.86 - 3,234.96 | 72.24 | Backtest WATCHING plan expired before entry. |
| `XRPUSDT` | EXPIRED（观察计划过期） | 2026-04-16T00:00:00+00:00 | 1.37 - 1.38 | 52.95 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2026-04-17T00:00:00+00:00 | 0.25 - 0.25 | 59.10 | Backtest WATCHING plan expired before entry. |
| `PEPEUSDT` | EXPIRED（观察计划过期） | 2026-04-17T08:00:00+00:00 | 0.00 - 0.00 | 70.27 | Backtest WATCHING plan expired before entry. |
| `AVNTUSDT` | EXPIRED（观察计划过期） | 2026-04-18T12:00:00+00:00 | 0.14 - 0.14 | 53.00 | Backtest WATCHING plan expired before entry. |
| `TRXUSDT` | EXPIRED（观察计划过期） | 2026-04-20T04:00:00+00:00 | 0.33 - 0.33 | 64.72 | Backtest WATCHING plan expired before entry. |
| `TREEUSDT` | EXPIRED（观察计划过期） | 2026-04-20T08:00:00+00:00 | 0.07 - 0.07 | 52.52 | Backtest WATCHING plan expired before entry. |
| `XRPUSDT` | EXPIRED（观察计划过期） | 2026-04-20T16:00:00+00:00 | 1.43 - 1.44 | 50.99 | Backtest WATCHING plan expired before entry. |
| `ORDIUSDT` | EXPIRED（观察计划过期） | 2026-04-21T04:00:00+00:00 | 4.88 - 4.91 | 63.16 | Backtest WATCHING plan expired before entry. |
| `DOGEUSDT` | EXPIRED（观察计划过期） | 2026-05-02T00:00:00+00:00 | 0.11 - 0.11 | 69.70 | Backtest WATCHING plan expired before entry. |
| `PEPEUSDT` | EXPIRED（观察计划过期） | 2026-05-05T00:00:00+00:00 | 0.00 - 0.00 | 63.13 | Backtest WATCHING plan expired before entry. |
| `LINKUSDT` | EXPIRED（观察计划过期） | 2026-05-05T00:00:00+00:00 | 9.27 - 9.35 | 60.10 | Backtest WATCHING plan expired before entry. |
| `DOGEUSDT` | EXPIRED（观察计划过期） | 2026-05-05T12:00:00+00:00 | 0.11 - 0.11 | 63.06 | Backtest WATCHING plan expired before entry. |
| `XRPUSDT` | EXPIRED（观察计划过期） | 2026-05-05T12:00:00+00:00 | 1.40 - 1.41 | 62.07 | Backtest WATCHING plan expired before entry. |
| `SUIUSDT` | EXPIRED（观察计划过期） | 2026-05-07T00:00:00+00:00 | 0.97 - 0.98 | 61.09 | Backtest WATCHING plan expired before entry. |
| `TAOUSDT` | EXPIRED（观察计划过期） | 2026-05-07T04:00:00+00:00 | 295.85 - 302.76 | 81.10 | Backtest WATCHING plan expired before entry. |
| `XRPUSDT` | EXPIRED（观察计划过期） | 2026-05-09T00:00:00+00:00 | 1.41 - 1.42 | 54.82 | Backtest WATCHING plan expired before entry. |
| `DOGEUSDT` | EXPIRED（观察计划过期） | 2026-05-09T00:00:00+00:00 | 0.11 - 0.11 | 36.06 | Backtest WATCHING plan expired before entry. |
| `ZECUSDT` | INVALIDATED（未入场前失效） | 2026-05-10T16:00:00+00:00 | 583.70 - 598.14 | 74.99 | Plan invalidated before entry: current price is below stop loss. |
| `TONUSDT` | INVALIDATED（未入场前失效） | 2026-05-10T16:00:00+00:00 | 2.36 - 2.43 | 48.69 | Plan invalidated before entry: current price is below stop loss. |
| `TAOUSDT` | INVALIDATED（未入场前失效） | 2026-05-11T00:00:00+00:00 | 312.93 - 318.17 | 70.55 | Plan invalidated before entry: current price is below stop loss. |

## 数据质量摘要

| Severity（严重程度） | Symbol（交易对） | Interval（周期） | Message（说明） |
|---|---|---|---|
| WARNING | `0GUSDT` | 1h | Large wick/range candle. |
| WARNING | `0GUSDT` | 1h | Large wick/range candle. |
| WARNING | `0GUSDT` | 1h | Large wick/range candle. |
| WARNING | `0GUSDT` | 1h | Large wick/range candle. |
| WARNING | `0GUSDT` | 1h | Large wick/range candle. |
| WARNING | `0GUSDT` | 4h | Large wick/range candle. |
| WARNING | `0GUSDT` | 4h | Large wick/range candle. |
| WARNING | `0GUSDT` | 4h | Large wick/range candle. |
| WARNING | `0GUSDT` | 4h | Large wick/range candle. |
| WARNING | `0GUSDT` | 4h | Large wick/range candle. |
| WARNING | `0GUSDT` | 4h | Large wick/range candle. |
| WARNING | `0GUSDT` | 4h | Large wick/range candle. |
| WARNING | `0GUSDT` | 1d | Large wick/range candle. |
| WARNING | `0GUSDT` | 1d | Large wick/range candle. |
| WARNING | `0GUSDT` | 1d | Large wick/range candle. |
| WARNING | `0GUSDT` | 1d | Large wick/range candle. |
| WARNING | `0GUSDT` | 1d | Large wick/range candle. |
| WARNING | `0GUSDT` | 1d | Large wick/range candle. |
| WARNING | `0GUSDT` | 1d | Large wick/range candle. |
| WARNING | `0GUSDT` | 1d | Large wick/range candle. |
| WARNING | `0GUSDT` | 1d | Large wick/range candle. |
| WARNING | `0GUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000CATUSDT` | 1h | Large wick/range candle. |
| WARNING | `1000CATUSDT` | 1h | Large wick/range candle. |
| WARNING | `1000CATUSDT` | 1h | Large wick/range candle. |
| WARNING | `1000CATUSDT` | 4h | Large wick/range candle. |
| WARNING | `1000CATUSDT` | 4h | Large wick/range candle. |
| WARNING | `1000CATUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000CATUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000CATUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000CATUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000CATUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000CATUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000CATUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000CATUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000CHEEMSUSDT` | 1h | Large wick/range candle. |
| WARNING | `1000CHEEMSUSDT` | 1h | Large wick/range candle. |
| WARNING | `1000CHEEMSUSDT` | 1h | Large wick/range candle. |
| WARNING | `1000CHEEMSUSDT` | 1h | Large wick/range candle. |
| WARNING | `1000CHEEMSUSDT` | 4h | Large wick/range candle. |
| WARNING | `1000CHEEMSUSDT` | 4h | Large wick/range candle. |
| WARNING | `1000CHEEMSUSDT` | 4h | Large wick/range candle. |
| WARNING | `1000CHEEMSUSDT` | 4h | Large wick/range candle. |
| WARNING | `1000CHEEMSUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000CHEEMSUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000CHEEMSUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000CHEEMSUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000CHEEMSUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000CHEEMSUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000SATSUSDT` | 1h | Large wick/range candle. |
| WARNING | `1000SATSUSDT` | 1h | Large wick/range candle. |
| WARNING | `1000SATSUSDT` | 1h | Large wick/range candle. |
| WARNING | `1000SATSUSDT` | 1h | Large wick/range candle. |
| WARNING | `1000SATSUSDT` | 4h | Large wick/range candle. |
| WARNING | `1000SATSUSDT` | 4h | Large wick/range candle. |
| WARNING | `1000SATSUSDT` | 4h | Large wick/range candle. |
| WARNING | `1000SATSUSDT` | 4h | Large wick/range candle. |
| WARNING | `1000SATSUSDT` | 4h | Large wick/range candle. |
| WARNING | `1000SATSUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000SATSUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000SATSUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000SATSUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000SATSUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000SATSUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000SATSUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000SATSUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000SATSUSDT` | 1d | Large wick/range candle. |
| WARNING | `1INCHUSDT` | 1h | Large wick/range candle. |
| WARNING | `1INCHUSDT` | 4h | Large wick/range candle. |
| WARNING | `1INCHUSDT` | 1d | Large wick/range candle. |
| WARNING | `1INCHUSDT` | 1d | Large wick/range candle. |
| WARNING | `1INCHUSDT` | 1d | Large wick/range candle. |
| WARNING | `1MBABYDOGEUSDT` | 1h | Large wick/range candle. |
| WARNING | `1MBABYDOGEUSDT` | 1h | Large wick/range candle. |
| WARNING | `1MBABYDOGEUSDT` | 4h | Large wick/range candle. |
| WARNING | `1MBABYDOGEUSDT` | 4h | Large wick/range candle. |
| WARNING | `1MBABYDOGEUSDT` | 1d | Large wick/range candle. |
| WARNING | `1MBABYDOGEUSDT` | 1d | Large wick/range candle. |
| WARNING | `1MBABYDOGEUSDT` | 1d | Large wick/range candle. |
| WARNING | `1MBABYDOGEUSDT` | 1d | Large wick/range candle. |
| INFO | n/a | n/a | Additional issues omitted: 5160. |

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
    "created_at_utc": "2026-06-09T09:08:16+00:00",
    "refresh_frequency": "daily",
    "max_symbols": 40,
    "master_count": 418,
    "source_limit": null,
    "source_limit_applied": false,
    "universe_refresh_count": 366,
    "selected_count_min": 4,
    "selected_count_avg": 16.25136612021858,
    "selected_count_max": 40,
    "top_selected_symbols": [
      {
        "symbol": "BTCUSDT",
        "days_selected": 366
      },
      {
        "symbol": "ETHUSDT",
        "days_selected": 366
      },
      {
        "symbol": "SOLUSDT",
        "days_selected": 366
      },
      {
        "symbol": "XRPUSDT",
        "days_selected": 360
      },
      {
        "symbol": "BNBUSDT",
        "days_selected": 344
      },
      {
        "symbol": "DOGEUSDT",
        "days_selected": 331
      },
      {
        "symbol": "SUIUSDT",
        "days_selected": 247
      },
      {
        "symbol": "TRXUSDT",
        "days_selected": 224
      },
      {
        "symbol": "ZECUSDT",
        "days_selected": 202
      },
      {
        "symbol": "PEPEUSDT",
        "days_selected": 200
      },
      {
        "symbol": "ADAUSDT",
        "days_selected": 193
      },
      {
        "symbol": "LINKUSDT",
        "days_selected": 152
      },
      {
        "symbol": "ENAUSDT",
        "days_selected": 142
      },
      {
        "symbol": "AVAXUSDT",
        "days_selected": 130
      },
      {
        "symbol": "UNIUSDT",
        "days_selected": 102
      },
      {
        "symbol": "LTCUSDT",
        "days_selected": 100
      },
      {
        "symbol": "PENGUUSDT",
        "days_selected": 93
      },
      {
        "symbol": "ASTERUSDT",
        "days_selected": 80
      },
      {
        "symbol": "TAOUSDT",
        "days_selected": 77
      },
      {
        "symbol": "PUMPUSDT",
        "days_selected": 65
      }
    ],
    "filter_counts": {
      "missing_1h": 11803,
      "insufficient_24h": 74,
      "reconstruct_error": 0,
      "low_quote_volume": 134937,
      "low_trades": 65,
      "stable_like": 135
    },
    "selection_by_day": [
      {
        "date_utc": "2025-06-01",
        "decision_time_utc": "2025-06-01T04:00:00+00:00",
        "selected_symbols": [
          "NEIROUSDT",
          "TAOUSDT",
          "VIRTUALUSDT",
          "SUIUSDT",
          "TRUMPUSDT",
          "PEPEUSDT",
          "BTCUSDT",
          "XRPUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "WIFUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "TRBUSDT",
          "LPTUSDT",
          "WCTUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 74,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 326,
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
      },
      {
        "date_utc": "2025-09-02",
        "decision_time_utc": "2025-09-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "TRUMPUSDT",
          "ADAUSDT",
          "LINKUSDT",
          "SUIUSDT",
          "TRXUSDT",
          "PLUMEUSDT",
          "FILUSDT",
          "PEPEUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "PENGUUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "POLUSDT",
          "UNIUSDT"
        ],
        "candidate_count": 21,
        "filter_counts": {
          "missing_1h": 58,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 337,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-03",
        "decision_time_utc": "2025-09-03T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "SOLUSDT",
          "PENGUUSDT",
          "AVAXUSDT",
          "XRPUSDT",
          "BTCUSDT",
          "LINKUSDT",
          "ARBUSDT",
          "ADAUSDT",
          "PLUMEUSDT",
          "ETHUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "WLFIUSDT",
          "BNBUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 57,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 342,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-04",
        "decision_time_utc": "2025-09-04T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BCHUSDT",
          "AVAXUSDT",
          "SOLUSDT",
          "SUIUSDT",
          "XRPUSDT",
          "WLFIUSDT",
          "LINKUSDT",
          "TRXUSDT",
          "BNBUSDT",
          "PEPEUSDT",
          "ADAUSDT",
          "SOMIUSDT",
          "PENGUUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 57,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 344,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-05",
        "decision_time_utc": "2025-09-05T00:00:00+00:00",
        "selected_symbols": [
          "SOMIUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "WLFIUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "LINKUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "SUIUSDT",
          "AVAXUSDT",
          "PEPEUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 57,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 346,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-06",
        "decision_time_utc": "2025-09-06T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "ENAUSDT",
          "SOMIUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "BCHUSDT",
          "PEPEUSDT",
          "SUIUSDT",
          "SOLUSDT",
          "ADAUSDT",
          "XRPUSDT",
          "ARBUSDT",
          "PENGUUSDT",
          "WLFIUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "LINKUSDT",
          "TRXUSDT",
          "REDUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 57,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 341,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-07",
        "decision_time_utc": "2025-09-07T00:00:00+00:00",
        "selected_symbols": [
          "SOMIUSDT",
          "NMRUSDT",
          "WLFIUSDT",
          "PYTHUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "SOLUSDT",
          "TRXUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "BIOUSDT",
          "BCHUSDT",
          "LINKUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 57,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 346,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-08",
        "decision_time_utc": "2025-09-08T00:00:00+00:00",
        "selected_symbols": [
          "SOMIUSDT",
          "NMRUSDT",
          "WLDUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "WLFIUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "SUIUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 57,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 347,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-09",
        "decision_time_utc": "2025-09-09T00:00:00+00:00",
        "selected_symbols": [
          "WLDUSDT",
          "ARKMUSDT",
          "PENGUUSDT",
          "BONKUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "SEIUSDT",
          "PEPEUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "SUIUSDT",
          "ETHUSDT",
          "LINKUSDT",
          "AVAXUSDT",
          "SOMIUSDT",
          "WLFIUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "LTCUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 56,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 339,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-10",
        "decision_time_utc": "2025-09-10T00:00:00+00:00",
        "selected_symbols": [
          "WLDUSDT",
          "OGUSDT",
          "KAITOUSDT",
          "ARKMUSDT",
          "AIUSDT",
          "ENAUSDT",
          "SOLUSDT",
          "DOLOUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "NEARUSDT",
          "TRXUSDT",
          "XRPUSDT",
          "WLFIUSDT",
          "PEPEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "SOMIUSDT",
          "LINKUSDT",
          "PENGUUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "LTCUSDT",
          "OPENUSDT"
        ],
        "candidate_count": 27,
        "filter_counts": {
          "missing_1h": 56,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 335,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-11",
        "decision_time_utc": "2025-09-11T00:00:00+00:00",
        "selected_symbols": [
          "PLUMEUSDT",
          "AVAXUSDT",
          "ONDOUSDT",
          "SOLUSDT",
          "1000SATSUSDT",
          "BTCUSDT",
          "LTCUSDT",
          "SUIUSDT",
          "ETHUSDT",
          "PYTHUSDT",
          "DOGEUSDT",
          "PENGUUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "XRPUSDT",
          "LINKUSDT",
          "PEPEUSDT",
          "WLDUSDT",
          "DOLOUSDT",
          "WLFIUSDT",
          "ENAUSDT",
          "TRXUSDT",
          "SOMIUSDT",
          "ARBUSDT",
          "OPENUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 55,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 337,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-12",
        "decision_time_utc": "2025-09-12T00:00:00+00:00",
        "selected_symbols": [
          "NMRUSDT",
          "ETHFIUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "LINKUSDT",
          "DOLOUSDT",
          "XRPUSDT",
          "TRXUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "ADAUSDT",
          "LINEAUSDT",
          "WLDUSDT",
          "SOMIUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "WLFIUSDT",
          "FORMUSDT",
          "PENGUUSDT",
          "LTCUSDT",
          "OPENUSDT",
          "ACEUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 53,
          "insufficient_24h": 2,
          "reconstruct_error": 0,
          "low_quote_volume": 338,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-13",
        "decision_time_utc": "2025-09-13T00:00:00+00:00",
        "selected_symbols": [
          "YGGUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "PEPEUSDT",
          "PUMPUSDT",
          "PENGUUSDT",
          "BONKUSDT",
          "WLFIUSDT",
          "XRPUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "LINKUSDT",
          "TRXUSDT",
          "SUIUSDT",
          "ONDOUSDT",
          "LTCUSDT",
          "WLDUSDT",
          "SOMIUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "LINEAUSDT",
          "HOLOUSDT",
          "OGUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 53,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 340,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-14",
        "decision_time_utc": "2025-09-14T00:00:00+00:00",
        "selected_symbols": [
          "SOMIUSDT",
          "LINEAUSDT",
          "PUMPUSDT",
          "YGGUSDT",
          "WLFIUSDT",
          "OPENUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "AVAXUSDT",
          "DOTUSDT",
          "ETHUSDT",
          "SUIUSDT",
          "TRUMPUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "SHIBUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "BONKUSDT",
          "LTCUSDT",
          "WLDUSDT",
          "LINKUSDT",
          "PENGUUSDT",
          "ENAUSDT",
          "TRXUSDT",
          "SEIUSDT"
        ],
        "candidate_count": 27,
        "filter_counts": {
          "missing_1h": 53,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 338,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-15",
        "decision_time_utc": "2025-09-15T00:00:00+00:00",
        "selected_symbols": [
          "PUMPUSDT",
          "MITOUSDT",
          "LINEAUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "WLFIUSDT",
          "XRPUSDT",
          "SOMIUSDT",
          "PEPEUSDT",
          "WLDUSDT",
          "BNBUSDT",
          "OPENUSDT",
          "AVAXUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "UNIUSDT",
          "TRXUSDT",
          "LTCUSDT",
          "ENAUSDT",
          "LINKUSDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 53,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 343,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-16",
        "decision_time_utc": "2025-09-16T00:00:00+00:00",
        "selected_symbols": [
          "PUMPUSDT",
          "WLFIUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "XRPUSDT",
          "SOMIUSDT",
          "MITOUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "ADAUSDT",
          "LINEAUSDT",
          "TRXUSDT",
          "WLDUSDT",
          "LINKUSDT",
          "ARBUSDT",
          "PENGUUSDT",
          "OPENUSDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 51,
          "insufficient_24h": 2,
          "reconstruct_error": 0,
          "low_quote_volume": 343,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-17",
        "decision_time_utc": "2025-09-17T00:00:00+00:00",
        "selected_symbols": [
          "SOMIUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "WLFIUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "PEPEUSDT",
          "SUIUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "PENGUUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "PUMPUSDT",
          "TRXUSDT",
          "ZKCUSDT",
          "ENAUSDT",
          "WLDUSDT",
          "LINEAUSDT",
          "LINKUSDT",
          "FORMUSDT",
          "AVNTUSDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 51,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 345,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-18",
        "decision_time_utc": "2025-09-18T00:00:00+00:00",
        "selected_symbols": [
          "DOGEUSDT",
          "AVAXUSDT",
          "SOLUSDT",
          "WLDUSDT",
          "ETHUSDT",
          "SUIUSDT",
          "PENGUUSDT",
          "PUMPUSDT",
          "BNBUSDT",
          "TSTUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "AVNTUSDT",
          "ADAUSDT",
          "PEPEUSDT",
          "BTCUSDT",
          "XRPUSDT",
          "LINKUSDT",
          "ENAUSDT",
          "HBARUSDT",
          "LTCUSDT",
          "TRXUSDT",
          "SOMIUSDT",
          "WLFIUSDT",
          "OPENUSDT",
          "WIFUSDT",
          "LINEAUSDT"
        ],
        "candidate_count": 27,
        "filter_counts": {
          "missing_1h": 50,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 340,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-19",
        "decision_time_utc": "2025-09-19T00:00:00+00:00",
        "selected_symbols": [
          "WUSDT",
          "NEARUSDT",
          "AVAXUSDT",
          "PENGUUSDT",
          "LINEAUSDT",
          "SUIUSDT",
          "SOLUSDT",
          "EIGENUSDT",
          "AVNTUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "LINKUSDT",
          "TRXUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "OPENUSDT",
          "XRPUSDT",
          "SOMIUSDT",
          "BCHUSDT",
          "PEPEUSDT",
          "LTCUSDT",
          "WLDUSDT",
          "PUMPUSDT",
          "ENAUSDT",
          "TSTUSDT",
          "WLFIUSDT"
        ],
        "candidate_count": 27,
        "filter_counts": {
          "missing_1h": 49,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 341,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-20",
        "decision_time_utc": "2025-09-20T00:00:00+00:00",
        "selected_symbols": [
          "TWTUSDT",
          "LINEAUSDT",
          "OPENUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "WLFIUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "NEARUSDT",
          "TRXUSDT",
          "LINKUSDT",
          "ENAUSDT",
          "PUMPUSDT",
          "PEPEUSDT",
          "AVNTUSDT",
          "DOTUSDT",
          "PENGUUSDT",
          "WLDUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 24,
        "filter_counts": {
          "missing_1h": 49,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 345,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-21",
        "decision_time_utc": "2025-09-21T00:00:00+00:00",
        "selected_symbols": [
          "AVNTUSDT",
          "SUNUSDT",
          "TWTUSDT",
          "CAKEUSDT",
          "BNBUSDT",
          "OPENUSDT",
          "BIOUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "NEARUSDT",
          "TRXUSDT",
          "WLFIUSDT",
          "SUIUSDT",
          "LINEAUSDT",
          "AVAXUSDT",
          "PUMPUSDT",
          "PEPEUSDT",
          "TUTUSDT"
        ],
        "candidate_count": 21,
        "filter_counts": {
          "missing_1h": 49,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 348,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-22",
        "decision_time_utc": "2025-09-22T00:00:00+00:00",
        "selected_symbols": [
          "AVNTUSDT",
          "LINEAUSDT",
          "WLFIUSDT",
          "THEUSDT",
          "OPENUSDT",
          "BARDUSDT",
          "BNBUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "PUMPUSDT",
          "AVAXUSDT",
          "TRXUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "LISTAUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 49,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 349,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-23",
        "decision_time_utc": "2025-09-23T00:00:00+00:00",
        "selected_symbols": [
          "TUTUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "MEUSDT",
          "SOLUSDT",
          "OPENUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "WLFIUSDT",
          "ADAUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "SUNUSDT",
          "LINKUSDT",
          "ENAUSDT",
          "WLDUSDT",
          "PUMPUSDT",
          "LINEAUSDT",
          "ARBUSDT",
          "TRUMPUSDT",
          "PENGUUSDT",
          "LTCUSDT",
          "UNIUSDT",
          "AAVEUSDT",
          "NEARUSDT",
          "SOMIUSDT",
          "HBARUSDT",
          "DOTUSDT",
          "SEIUSDT",
          "TONUSDT",
          "BONKUSDT",
          "AVNTUSDT"
        ],
        "candidate_count": 35,
        "filter_counts": {
          "missing_1h": 48,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 333,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-24",
        "decision_time_utc": "2025-09-24T00:00:00+00:00",
        "selected_symbols": [
          "BARDUSDT",
          "SIGNUSDT",
          "0GUSDT",
          "BNBUSDT",
          "LINEAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "PUMPUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "AVNTUSDT",
          "SOMIUSDT",
          "XRPUSDT",
          "ENAUSDT",
          "WLFIUSDT",
          "SUIUSDT",
          "TRXUSDT",
          "PEPEUSDT",
          "WLDUSDT",
          "ADAUSDT",
          "LINKUSDT",
          "NEARUSDT",
          "PENGUUSDT"
        ],
        "candidate_count": 24,
        "filter_counts": {
          "missing_1h": 47,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 345,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-25",
        "decision_time_utc": "2025-09-25T00:00:00+00:00",
        "selected_symbols": [
          "HEMIUSDT",
          "AVNTUSDT",
          "XRPUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "LINEAUSDT",
          "NEARUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "HOLOUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "TRXUSDT",
          "LINKUSDT",
          "PEPEUSDT",
          "PUMPUSDT",
          "WLFIUSDT",
          "0GUSDT",
          "ENAUSDT",
          "SIGNUSDT",
          "BARDUSDT"
        ],
        "candidate_count": 23,
        "filter_counts": {
          "missing_1h": 47,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 348,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-26",
        "decision_time_utc": "2025-09-26T00:00:00+00:00",
        "selected_symbols": [
          "SPKUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "HOLOUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "PUMPUSDT",
          "SUIUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "TRXUSDT",
          "WLFIUSDT",
          "ENAUSDT",
          "PEPEUSDT",
          "TUTUSDT",
          "LINKUSDT",
          "ARBUSDT",
          "LINEAUSDT",
          "PENGUUSDT",
          "ETHFIUSDT",
          "WLDUSDT",
          "NEARUSDT",
          "HBARUSDT",
          "AAVEUSDT",
          "HEMIUSDT",
          "0GUSDT",
          "LTCUSDT",
          "AVNTUSDT"
        ],
        "candidate_count": 30,
        "filter_counts": {
          "missing_1h": 46,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 341,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-27",
        "decision_time_utc": "2025-09-27T00:00:00+00:00",
        "selected_symbols": [
          "ALPINEUSDT",
          "SNXUSDT",
          "1000SATSUSDT",
          "LINEAUSDT",
          "WLFIUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "PUMPUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "AVNTUSDT",
          "LINKUSDT",
          "SUIUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "PEPEUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "XPLUSDT",
          "AVAXUSDT",
          "TRXUSDT",
          "HEMIUSDT",
          "0GUSDT"
        ],
        "candidate_count": 23,
        "filter_counts": {
          "missing_1h": 45,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 348,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-28",
        "decision_time_utc": "2025-09-28T00:00:00+00:00",
        "selected_symbols": [
          "XPLUSDT",
          "ALPINEUSDT",
          "AEVOUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "AVNTUSDT",
          "MIRAUSDT",
          "DOGEUSDT",
          "ZKCUSDT",
          "LINEAUSDT",
          "PUMPUSDT",
          "AVAXUSDT",
          "1000SATSUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 45,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 357,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-29",
        "decision_time_utc": "2025-09-29T00:00:00+00:00",
        "selected_symbols": [
          "FORMUSDT",
          "KAITOUSDT",
          "PUMPUSDT",
          "WLFIUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "XPLUSDT",
          "AVNTUSDT",
          "ZKCUSDT",
          "MIRAUSDT",
          "BARDUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 45,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 356,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-30",
        "decision_time_utc": "2025-09-30T00:00:00+00:00",
        "selected_symbols": [
          "ALPINEUSDT",
          "COWUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ETHUSDT",
          "SUPERUSDT",
          "SOLUSDT",
          "ZKCUSDT",
          "XPLUSDT",
          "AVAXUSDT",
          "XRPUSDT",
          "AVNTUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "PUMPUSDT",
          "WLFIUSDT",
          "TRXUSDT",
          "LINKUSDT",
          "ADAUSDT",
          "LINEAUSDT",
          "PEPEUSDT",
          "ENAUSDT",
          "MIRAUSDT"
        ],
        "candidate_count": 23,
        "filter_counts": {
          "missing_1h": 44,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 350,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-01",
        "decision_time_utc": "2025-10-01T00:00:00+00:00",
        "selected_symbols": [
          "AVNTUSDT",
          "BARDUSDT",
          "PUMPUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "XPLUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "SUIUSDT",
          "WLFIUSDT",
          "ADAUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "LINKUSDT",
          "ENAUSDT",
          "MIRAUSDT",
          "FFUSDT",
          "ALPINEUSDT"
        ],
        "candidate_count": 21,
        "filter_counts": {
          "missing_1h": 43,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 353,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-02",
        "decision_time_utc": "2025-10-02T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "PUMPUSDT",
          "PENGUUSDT",
          "SOMIUSDT",
          "APTUSDT",
          "SOLUSDT",
          "SUIUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "LTCUSDT",
          "NEARUSDT",
          "LINKUSDT",
          "ADAUSDT",
          "XRPUSDT",
          "PEPEUSDT",
          "WLFIUSDT",
          "FFUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "TRXUSDT",
          "XPLUSDT",
          "BARDUSDT",
          "AVNTUSDT",
          "EDENUSDT",
          "ALPINEUSDT"
        ],
        "candidate_count": 27,
        "filter_counts": {
          "missing_1h": 42,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 348,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-03",
        "decision_time_utc": "2025-10-03T00:00:00+00:00",
        "selected_symbols": [
          "ETHFIUSDT",
          "EIGENUSDT",
          "ZECUSDT",
          "ENAUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "APTUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "XRPUSDT",
          "PEPEUSDT",
          "LTCUSDT",
          "NEARUSDT",
          "DASHUSDT",
          "ADAUSDT",
          "SUIUSDT",
          "WLDUSDT",
          "BARDUSDT",
          "AVAXUSDT",
          "PUMPUSDT",
          "XPLUSDT",
          "PENGUUSDT",
          "LINKUSDT",
          "WLFIUSDT",
          "TRXUSDT",
          "AVNTUSDT",
          "SOMIUSDT"
        ],
        "candidate_count": 28,
        "filter_counts": {
          "missing_1h": 41,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 348,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-04",
        "decision_time_utc": "2025-10-04T00:00:00+00:00",
        "selected_symbols": [
          "OPENUSDT",
          "0GUSDT",
          "CAKEUSDT",
          "BNBUSDT",
          "AVNTUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "APTUSDT",
          "SOLUSDT",
          "SOMIUSDT",
          "NEARUSDT",
          "XPLUSDT",
          "XRPUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "LTCUSDT",
          "ZECUSDT",
          "SUIUSDT",
          "PUMPUSDT",
          "ADAUSDT",
          "PEPEUSDT",
          "2ZUSDT",
          "TRXUSDT",
          "LINKUSDT",
          "ENAUSDT",
          "PENGUUSDT",
          "WLFIUSDT",
          "WLDUSDT",
          "FORMUSDT"
        ],
        "candidate_count": 29,
        "filter_counts": {
          "missing_1h": 40,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 348,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-05",
        "decision_time_utc": "2025-10-05T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "SOMIUSDT",
          "FLOKIUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XPLUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "DOGEUSDT",
          "LINEAUSDT",
          "XRPUSDT",
          "APTUSDT",
          "PUMPUSDT",
          "AVAXUSDT",
          "PEPEUSDT",
          "ADAUSDT",
          "CAKEUSDT",
          "AVNTUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 40,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 359,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-06",
        "decision_time_utc": "2025-10-06T00:00:00+00:00",
        "selected_symbols": [
          "XPLUSDT",
          "ZECUSDT",
          "APTUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "PENGUUSDT",
          "BNBUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "TUTUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "PEPEUSDT",
          "PUMPUSDT",
          "AVAXUSDT",
          "TRXUSDT",
          "ENAUSDT",
          "NEARUSDT",
          "LTCUSDT",
          "LINKUSDT",
          "SOMIUSDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 40,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 356,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-07",
        "decision_time_utc": "2025-10-07T00:00:00+00:00",
        "selected_symbols": [
          "PLUMEUSDT",
          "STRKUSDT",
          "CAKEUSDT",
          "ALPINEUSDT",
          "XPLUSDT",
          "BONKUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "LINKUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "PEPEUSDT",
          "PENGUUSDT",
          "SOLUSDT",
          "ENAUSDT",
          "NEARUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "AVAXUSDT",
          "TRXUSDT",
          "FORMUSDT",
          "PUMPUSDT",
          "ZECUSDT",
          "APTUSDT",
          "LTCUSDT",
          "STOUSDT"
        ],
        "candidate_count": 27,
        "filter_counts": {
          "missing_1h": 39,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 351,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-08",
        "decision_time_utc": "2025-10-08T00:00:00+00:00",
        "selected_symbols": [
          "FORMUSDT",
          "CAKEUSDT",
          "BNBUSDT",
          "BROCCOLI714USDT",
          "PUMPUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "XPLUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "ASTERUSDT",
          "HEMIUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "SUIUSDT",
          "LINKUSDT",
          "ZECUSDT",
          "PEPEUSDT",
          "WLFIUSDT",
          "ENAUSDT",
          "TRXUSDT",
          "PENGUUSDT",
          "WLDUSDT",
          "NEARUSDT",
          "UNIUSDT",
          "FLOKIUSDT"
        ],
        "candidate_count": 28,
        "filter_counts": {
          "missing_1h": 39,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 351,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-09",
        "decision_time_utc": "2025-10-09T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "LISTAUSDT",
          "1000CHEEMSUSDT",
          "HEMIUSDT",
          "STOUSDT",
          "PENGUUSDT",
          "WLDUSDT",
          "SOLUSDT",
          "ENAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "FORMUSDT",
          "XPLUSDT",
          "LINKUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "TRUMPUSDT",
          "ADAUSDT",
          "XRPUSDT",
          "WLFIUSDT",
          "TRXUSDT",
          "ASTERUSDT",
          "PEPEUSDT",
          "CAKEUSDT",
          "MIRAUSDT",
          "PUMPUSDT"
        ],
        "candidate_count": 28,
        "filter_counts": {
          "missing_1h": 39,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 351,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-10",
        "decision_time_utc": "2025-10-10T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "1000CHEEMSUSDT",
          "ALICEUSDT",
          "LTCUSDT",
          "BTCUSDT",
          "XPLUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "MIRAUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "ASTERUSDT",
          "ZENUSDT",
          "CAKEUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "TRXUSDT",
          "PUMPUSDT",
          "LINKUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "PEPEUSDT",
          "PENGUUSDT",
          "NEARUSDT",
          "FORMUSDT"
        ],
        "candidate_count": 26,
        "filter_counts": {
          "missing_1h": 39,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 353,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-11",
        "decision_time_utc": "2025-10-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "TRXUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "DASHUSDT",
          "ZECUSDT",
          "SHIBUSDT",
          "ASTERUSDT",
          "NEARUSDT",
          "XRPUSDT",
          "XLMUSDT",
          "CAKEUSDT",
          "WLFIUSDT",
          "LTCUSDT",
          "DOGEUSDT",
          "ZENUSDT",
          "TAOUSDT",
          "LINKUSDT",
          "ETCUSDT",
          "ADAUSDT",
          "HBARUSDT",
          "MIRAUSDT",
          "FFUSDT",
          "XPLUSDT",
          "AVAXUSDT",
          "PEPEUSDT",
          "AAVEUSDT",
          "ONDOUSDT",
          "ARBUSDT",
          "CRVUSDT",
          "SEIUSDT",
          "UNIUSDT",
          "ENAUSDT",
          "FETUSDT",
          "OPUSDT",
          "LINEAUSDT",
          "BONKUSDT",
          "WLDUSDT"
        ],
        "candidate_count": 54,
        "filter_counts": {
          "missing_1h": 38,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 324,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-12",
        "decision_time_utc": "2025-10-12T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "FFUSDT",
          "ZENUSDT",
          "TRUMPUSDT",
          "BNBUSDT",
          "WLDUSDT",
          "FETUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ETCUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ONDOUSDT",
          "XRPUSDT",
          "BONKUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "TAOUSDT",
          "DOTUSDT",
          "TONUSDT",
          "HBARUSDT",
          "ARBUSDT",
          "SUIUSDT",
          "ASTERUSDT",
          "UNIUSDT",
          "ADAUSDT",
          "XPLUSDT",
          "LTCUSDT",
          "WBETHUSDT",
          "LINKUSDT",
          "PEPEUSDT",
          "SUSDT",
          "XLMUSDT",
          "ENAUSDT",
          "TRXUSDT",
          "PUMPUSDT",
          "NEARUSDT",
          "FILUSDT",
          "BNSOLUSDT",
          "PENGUUSDT"
        ],
        "candidate_count": 46,
        "filter_counts": {
          "missing_1h": 38,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 333,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-13",
        "decision_time_utc": "2025-10-13T00:00:00+00:00",
        "selected_symbols": [
          "SNXUSDT",
          "FORMUSDT",
          "CAKEUSDT",
          "TAOUSDT",
          "ASTERUSDT",
          "DASHUSDT",
          "FFUSDT",
          "PENGUUSDT",
          "BNBUSDT",
          "XPLUSDT",
          "WLFIUSDT",
          "PUMPUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "SOLUSDT",
          "UNIUSDT",
          "ENAUSDT",
          "PEPEUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "LINKUSDT",
          "WLDUSDT",
          "XRPUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "NEARUSDT",
          "LTCUSDT",
          "AVAXUSDT",
          "TRUMPUSDT",
          "ZENUSDT",
          "TRXUSDT",
          "ZECUSDT"
        ],
        "candidate_count": 32,
        "filter_counts": {
          "missing_1h": 38,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 348,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-14",
        "decision_time_utc": "2025-10-14T00:00:00+00:00",
        "selected_symbols": [
          "FFUSDT",
          "SNXUSDT",
          "TAOUSDT",
          "ENAUSDT",
          "WIFUSDT",
          "SOLUSDT",
          "FORMUSDT",
          "SUIUSDT",
          "BONKUSDT",
          "WLFIUSDT",
          "CAKEUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "NEARUSDT",
          "ETHUSDT",
          "TRUMPUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "XRPUSDT",
          "LINKUSDT",
          "ADAUSDT",
          "HBARUSDT",
          "BTCUSDT",
          "XPLUSDT",
          "BNBUSDT",
          "PENGUUSDT",
          "ASTERUSDT",
          "LTCUSDT",
          "ZECUSDT",
          "WLDUSDT",
          "PUMPUSDT",
          "TRXUSDT",
          "APTUSDT",
          "ZENUSDT",
          "FETUSDT",
          "DASHUSDT"
        ],
        "candidate_count": 36,
        "filter_counts": {
          "missing_1h": 37,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 344,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-15",
        "decision_time_utc": "2025-10-15T00:00:00+00:00",
        "selected_symbols": [
          "ALICEUSDT",
          "ASTERUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "TAOUSDT",
          "BNBUSDT",
          "SOLUSDT",
          "XPLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "EDENUSDT",
          "2ZUSDT",
          "SUIUSDT",
          "FORMUSDT",
          "ADAUSDT",
          "ZECUSDT",
          "TRXUSDT",
          "CAKEUSDT",
          "PEPEUSDT",
          "AVAXUSDT",
          "LINKUSDT",
          "ENAUSDT",
          "LTCUSDT",
          "PUMPUSDT",
          "BCHUSDT",
          "SNXUSDT",
          "WLFIUSDT",
          "FETUSDT",
          "FFUSDT",
          "PENGUUSDT",
          "NEARUSDT",
          "HBARUSDT",
          "WIFUSDT",
          "WLDUSDT"
        ],
        "candidate_count": 34,
        "filter_counts": {
          "missing_1h": 36,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 347,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-16",
        "decision_time_utc": "2025-10-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "2ZUSDT",
          "XRPUSDT",
          "XPLUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "ASTERUSDT",
          "ZECUSDT",
          "CAKEUSDT",
          "SUIUSDT",
          "TAOUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "LINKUSDT",
          "AVAXUSDT",
          "PEPEUSDT",
          "LTCUSDT",
          "PUMPUSDT",
          "ENSOUSDT",
          "YGGUSDT"
        ],
        "candidate_count": 23,
        "filter_counts": {
          "missing_1h": 35,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 359,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-17",
        "decision_time_utc": "2025-10-17T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "2ZUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "XPLUSDT",
          "ZECUSDT",
          "SUIUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "TAOUSDT",
          "AVAXUSDT",
          "LINKUSDT",
          "PEPEUSDT",
          "LTCUSDT",
          "PUMPUSDT",
          "ENAUSDT",
          "CAKEUSDT",
          "WLDUSDT",
          "YBUSDT",
          "BELUSDT"
        ],
        "candidate_count": 24,
        "filter_counts": {
          "missing_1h": 35,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 359,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-18",
        "decision_time_utc": "2025-10-18T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "ZECUSDT",
          "ZKCUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "PUMPUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "SUIUSDT",
          "TAOUSDT",
          "ADAUSDT",
          "XPLUSDT",
          "TRXUSDT",
          "LINKUSDT",
          "AVAXUSDT",
          "LTCUSDT",
          "PEPEUSDT",
          "AAVEUSDT",
          "PENGUUSDT",
          "BCHUSDT",
          "YBUSDT"
        ],
        "candidate_count": 24,
        "filter_counts": {
          "missing_1h": 34,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 359,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-19",
        "decision_time_utc": "2025-10-19T00:00:00+00:00",
        "selected_symbols": [
          "PUMPUSDT",
          "ENAUSDT",
          "SOLUSDT",
          "TAOUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "SUIUSDT",
          "XPLUSDT",
          "ZECUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 34,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 370,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-20",
        "decision_time_utc": "2025-10-20T00:00:00+00:00",
        "selected_symbols": [
          "TAOUSDT",
          "ZECUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "MORPHOUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "PEPEUSDT",
          "ADAUSDT",
          "LINKUSDT",
          "ASTERUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "TRXUSDT",
          "XPLUSDT",
          "PUMPUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 34,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 366,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-21",
        "decision_time_utc": "2025-10-21T00:00:00+00:00",
        "selected_symbols": [
          "AUCTIONUSDT",
          "FLOKIUSDT",
          "ZECUSDT",
          "LINKUSDT",
          "BIOUSDT",
          "XRPUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "SOLUSDT",
          "MORPHOUSDT",
          "BNBUSDT",
          "PEPEUSDT",
          "ADAUSDT",
          "WALUSDT",
          "ASTERUSDT",
          "TRXUSDT",
          "ZBTUSDT",
          "ENAUSDT",
          "XPLUSDT",
          "SUIUSDT",
          "TAOUSDT",
          "AVAXUSDT",
          "PUMPUSDT"
        ],
        "candidate_count": 24,
        "filter_counts": {
          "missing_1h": 34,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 360,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-22",
        "decision_time_utc": "2025-10-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "WALUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "ZECUSDT",
          "ASTERUSDT",
          "SUIUSDT",
          "ENAUSDT",
          "LINKUSDT",
          "AVNTUSDT",
          "TAOUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "XPLUSDT",
          "PEPEUSDT",
          "BCHUSDT",
          "AVAXUSDT",
          "CAKEUSDT",
          "PUMPUSDT",
          "LTCUSDT"
        ],
        "candidate_count": 23,
        "filter_counts": {
          "missing_1h": 34,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 361,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-23",
        "decision_time_utc": "2025-10-23T00:00:00+00:00",
        "selected_symbols": [
          "AVNTUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "SOLUSDT",
          "WALUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "ZECUSDT",
          "ASTERUSDT",
          "TRXUSDT",
          "SUIUSDT",
          "XPLUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "LINKUSDT",
          "TAOUSDT",
          "PEPEUSDT",
          "AVAXUSDT",
          "PUMPUSDT",
          "LTCUSDT"
        ],
        "candidate_count": 21,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 363,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-24",
        "decision_time_utc": "2025-10-24T00:00:00+00:00",
        "selected_symbols": [
          "YBUSDT",
          "ASTERUSDT",
          "WLFIUSDT",
          "WALUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "XPLUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "ADAUSDT",
          "ZECUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "BCHUSDT",
          "TAOUSDT",
          "LINKUSDT",
          "TURTLEUSDT",
          "TRXUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 363,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-25",
        "decision_time_utc": "2025-10-25T00:00:00+00:00",
        "selected_symbols": [
          "VIRTUALUSDT",
          "ZECUSDT",
          "AVNTUSDT",
          "PUMPUSDT",
          "XPLUSDT",
          "XRPUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SUIUSDT",
          "WALUSDT",
          "SOLUSDT",
          "PEPEUSDT",
          "LINKUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 366,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-26",
        "decision_time_utc": "2025-10-26T00:00:00+00:00",
        "selected_symbols": [
          "VIRTUALUSDT",
          "XRPUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ZECUSDT",
          "ASTERUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "DOGEUSDT",
          "SUIUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 31,
          "insufficient_24h": 2,
          "reconstruct_error": 0,
          "low_quote_volume": 374,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-27",
        "decision_time_utc": "2025-10-27T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "ZENUSDT",
          "PUMPUSDT",
          "VIRTUALUSDT",
          "BCHUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "BTCUSDT",
          "SUIUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "SOLUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "LINKUSDT",
          "PEPEUSDT",
          "TAOUSDT",
          "ASTERUSDT",
          "TRXUSDT",
          "GIGGLEUSDT",
          "XPLUSDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 31,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 365,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-28",
        "decision_time_utc": "2025-10-28T00:00:00+00:00",
        "selected_symbols": [
          "TRUMPUSDT",
          "ZECUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "TAOUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "ENSOUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "SUIUSDT",
          "ENAUSDT",
          "VIRTUALUSDT",
          "XPLUSDT",
          "PUMPUSDT",
          "GIGGLEUSDT",
          "TRXUSDT",
          "LINKUSDT",
          "LTCUSDT",
          "ADAUSDT",
          "PEPEUSDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 31,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 365,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-29",
        "decision_time_utc": "2025-10-29T00:00:00+00:00",
        "selected_symbols": [
          "EULUSDT",
          "HBARUSDT",
          "XPLUSDT",
          "TAOUSDT",
          "VIRTUALUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "ENSOUSDT",
          "BNBUSDT",
          "TRUMPUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "ZECUSDT",
          "ASTERUSDT",
          "SUIUSDT",
          "BCHUSDT",
          "LTCUSDT",
          "PUMPUSDT",
          "ZBTUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "LINKUSDT",
          "ENAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 31,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 362,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-30",
        "decision_time_utc": "2025-10-30T00:00:00+00:00",
        "selected_symbols": [
          "TRUMPUSDT",
          "PUMPUSDT",
          "ZECUSDT",
          "EULUSDT",
          "WLFIUSDT",
          "BTCUSDT",
          "HBARUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "TAOUSDT",
          "LINKUSDT",
          "LTCUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "VIRTUALUSDT",
          "TRXUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "GIGGLEUSDT",
          "ENAUSDT",
          "XPLUSDT",
          "ENSOUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 31,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 362,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-31",
        "decision_time_utc": "2025-10-31T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "ZECUSDT",
          "DOGEUSDT",
          "TRUMPUSDT",
          "ASTERUSDT",
          "SUIUSDT",
          "TRXUSDT",
          "HBARUSDT",
          "PUMPUSDT",
          "LINKUSDT",
          "TAOUSDT",
          "GIGGLEUSDT",
          "ADAUSDT",
          "XPLUSDT",
          "UNIUSDT",
          "VIRTUALUSDT",
          "PEPEUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "LTCUSDT",
          "ZBTUSDT",
          "PENGUUSDT"
        ],
        "candidate_count": 26,
        "filter_counts": {
          "missing_1h": 31,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 361,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-01",
        "decision_time_utc": "2025-11-01T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "TAOUSDT",
          "ASTERUSDT",
          "VIRTUALUSDT",
          "TRUMPUSDT",
          "BTCUSDT",
          "PUMPUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "LINKUSDT",
          "HBARUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "GIGGLEUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 31,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 369,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-02",
        "decision_time_utc": "2025-11-02T00:00:00+00:00",
        "selected_symbols": [
          "ZKUSDT",
          "DASHUSDT",
          "VIRTUALUSDT",
          "ZENUSDT",
          "ZBTUSDT",
          "LTCUSDT",
          "TAOUSDT",
          "ZECUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "SOLUSDT",
          "PUMPUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "TRUMPUSDT",
          "ASTERUSDT",
          "GIGGLEUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 31,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 369,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-03",
        "decision_time_utc": "2025-11-03T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "ICPUSDT",
          "DASHUSDT",
          "MINAUSDT",
          "ZKUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ZECUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "ZBTUSDT",
          "ZENUSDT",
          "BNBUSDT",
          "TAOUSDT",
          "DOGEUSDT",
          "VIRTUALUSDT",
          "XPLUSDT",
          "SUIUSDT",
          "PUMPUSDT",
          "GIGGLEUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 31,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 367,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-04",
        "decision_time_utc": "2025-11-04T00:00:00+00:00",
        "selected_symbols": [
          "DASHUSDT",
          "ZENUSDT",
          "ZECUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "XPLUSDT",
          "SOLUSDT",
          "ZBTUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "SUIUSDT",
          "TRUMPUSDT",
          "TAOUSDT",
          "LINKUSDT",
          "ADAUSDT",
          "PEPEUSDT",
          "AVAXUSDT",
          "VIRTUALUSDT",
          "LTCUSDT",
          "ZKUSDT",
          "PUMPUSDT",
          "ICPUSDT",
          "HBARUSDT",
          "ENAUSDT",
          "UNIUSDT",
          "WLDUSDT",
          "ASTERUSDT",
          "GIGGLEUSDT"
        ],
        "candidate_count": 30,
        "filter_counts": {
          "missing_1h": 30,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 356,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-05",
        "decision_time_utc": "2025-11-05T00:00:00+00:00",
        "selected_symbols": [
          "ZKUSDT",
          "GIGGLEUSDT",
          "ICPUSDT",
          "ASTERUSDT",
          "ZENUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ZECUSDT",
          "DASHUSDT",
          "SOLUSDT",
          "TRXUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "TAOUSDT",
          "ADAUSDT",
          "LINKUSDT",
          "PEPEUSDT",
          "XPLUSDT",
          "TRUMPUSDT",
          "AVAXUSDT",
          "VIRTUALUSDT",
          "LTCUSDT",
          "PUMPUSDT",
          "HBARUSDT",
          "ENAUSDT",
          "PENGUUSDT",
          "KITEUSDT",
          "AAVEUSDT",
          "NEARUSDT",
          "WLDUSDT",
          "ARBUSDT",
          "DCRUSDT"
        ],
        "candidate_count": 34,
        "filter_counts": {
          "missing_1h": 29,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 354,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-06",
        "decision_time_utc": "2025-11-06T00:00:00+00:00",
        "selected_symbols": [
          "GIGGLEUSDT",
          "XPLUSDT",
          "TRUMPUSDT",
          "ZKUSDT",
          "ICPUSDT",
          "ASTERUSDT",
          "PUMPUSDT",
          "ZECUSDT",
          "XRPUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "LTCUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "SUIUSDT",
          "LINKUSDT",
          "VIRTUALUSDT",
          "TRXUSDT",
          "DASHUSDT",
          "ZENUSDT",
          "TAOUSDT",
          "TURTLEUSDT",
          "KITEUSDT",
          "MMTUSDT"
        ],
        "candidate_count": 27,
        "filter_counts": {
          "missing_1h": 29,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 361,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-07",
        "decision_time_utc": "2025-11-07T00:00:00+00:00",
        "selected_symbols": [
          "FILUSDT",
          "ZECUSDT",
          "ICPUSDT",
          "DASHUSDT",
          "NEARUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "TAOUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ZENUSDT",
          "ZKUSDT",
          "SUIUSDT",
          "XPLUSDT",
          "TRUMPUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "VIRTUALUSDT",
          "LINKUSDT",
          "PEPEUSDT",
          "PUMPUSDT",
          "GIGGLEUSDT",
          "MMTUSDT",
          "ALCXUSDT"
        ],
        "candidate_count": 27,
        "filter_counts": {
          "missing_1h": 28,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 362,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-08",
        "decision_time_utc": "2025-11-08T00:00:00+00:00",
        "selected_symbols": [
          "FILUSDT",
          "STRKUSDT",
          "NEARUSDT",
          "XPLUSDT",
          "FETUSDT",
          "ARUSDT",
          "VIRTUALUSDT",
          "ICPUSDT",
          "ETCUSDT",
          "ZECUSDT",
          "DOTUSDT",
          "WLDUSDT",
          "LTCUSDT",
          "APTUSDT",
          "ASTERUSDT",
          "PUMPUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "SUIUSDT",
          "MMTUSDT",
          "ADAUSDT",
          "BCHUSDT",
          "PENGUUSDT",
          "HBARUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "ZENUSDT",
          "LINKUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "TRXUSDT",
          "TAOUSDT",
          "TRUMPUSDT",
          "DASHUSDT",
          "ZKUSDT",
          "GIGGLEUSDT",
          "SAPIENUSDT"
        ],
        "candidate_count": 40,
        "filter_counts": {
          "missing_1h": 28,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 350,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-09",
        "decision_time_utc": "2025-11-09T00:00:00+00:00",
        "selected_symbols": [
          "PYRUSDT",
          "0GUSDT",
          "MMTUSDT",
          "ICPUSDT",
          "NEARUSDT",
          "LTCUSDT",
          "ZECUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "FILUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "ASTERUSDT",
          "DASHUSDT",
          "FETUSDT",
          "XPLUSDT",
          "AAVEUSDT",
          "SUIUSDT",
          "SUSDT",
          "DOTUSDT",
          "VIRTUALUSDT",
          "TAOUSDT",
          "LINKUSDT",
          "TRXUSDT",
          "ARUSDT",
          "AVAXUSDT",
          "GIGGLEUSDT",
          "ADAUSDT",
          "ZKUSDT",
          "ORDIUSDT",
          "ZENUSDT",
          "FLUXUSDT"
        ],
        "candidate_count": 34,
        "filter_counts": {
          "missing_1h": 28,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 356,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-10",
        "decision_time_utc": "2025-11-10T00:00:00+00:00",
        "selected_symbols": [
          "KITEUSDT",
          "GIGGLEUSDT",
          "UNIUSDT",
          "ETHUSDT",
          "ASTERUSDT",
          "SOLUSDT",
          "ZENUSDT",
          "BTCUSDT",
          "NEARUSDT",
          "VIRTUALUSDT",
          "ZECUSDT",
          "XPLUSDT",
          "XRPUSDT",
          "LTCUSDT",
          "DOGEUSDT",
          "SAPIENUSDT",
          "FETUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ICPUSDT",
          "SUIUSDT",
          "FILUSDT",
          "DASHUSDT",
          "MMTUSDT",
          "ZKUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 28,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 365,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-11",
        "decision_time_utc": "2025-11-11T00:00:00+00:00",
        "selected_symbols": [
          "UNIUSDT",
          "WLFIUSDT",
          "TRUMPUSDT",
          "FUSDT",
          "HBARUSDT",
          "PUMPUSDT",
          "XRPUSDT",
          "STRKUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "ZECUSDT",
          "LINKUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "TRXUSDT",
          "PEPEUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ZKUSDT",
          "TAOUSDT",
          "SUIUSDT",
          "ASTERUSDT",
          "NEARUSDT",
          "VIRTUALUSDT",
          "ICPUSDT",
          "GIGGLEUSDT",
          "LTCUSDT",
          "FILUSDT",
          "FETUSDT",
          "XPLUSDT",
          "DASHUSDT",
          "ZENUSDT"
        ],
        "candidate_count": 34,
        "filter_counts": {
          "missing_1h": 28,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 356,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-12",
        "decision_time_utc": "2025-11-12T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "ZECUSDT",
          "SOLUSDT",
          "UNIUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "TRUMPUSDT",
          "TRXUSDT",
          "FILUSDT",
          "ICPUSDT",
          "LTCUSDT",
          "SUIUSDT",
          "PUMPUSDT",
          "MMTUSDT",
          "GIGGLEUSDT",
          "NEARUSDT",
          "KERNELUSDT",
          "ADAUSDT",
          "FETUSDT",
          "LINKUSDT",
          "ENAUSDT",
          "XPLUSDT",
          "STRKUSDT",
          "AVAXUSDT",
          "DASHUSDT",
          "CFXUSDT"
        ],
        "candidate_count": 29,
        "filter_counts": {
          "missing_1h": 27,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 361,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-13",
        "decision_time_utc": "2025-11-13T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "GIGGLEUSDT",
          "KERNELUSDT",
          "ICPUSDT",
          "ASTERUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "UNIUSDT",
          "LTCUSDT",
          "TRXUSDT",
          "PUMPUSDT",
          "TRUMPUSDT",
          "LINKUSDT",
          "SUIUSDT",
          "FILUSDT",
          "TAOUSDT",
          "MMTUSDT",
          "ADAUSDT",
          "VIRTUALUSDT",
          "ENAUSDT",
          "STRKUSDT",
          "ALLOUSDT"
        ],
        "candidate_count": 26,
        "filter_counts": {
          "missing_1h": 27,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 365,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-14",
        "decision_time_utc": "2025-11-14T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "UNIUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "TRXUSDT",
          "SUIUSDT",
          "LTCUSDT",
          "LINKUSDT",
          "GIGGLEUSDT",
          "ICPUSDT",
          "ADAUSDT",
          "PUMPUSDT",
          "MMTUSDT",
          "TAOUSDT",
          "AVAXUSDT",
          "TRUMPUSDT",
          "HBARUSDT",
          "XPLUSDT",
          "PEPEUSDT",
          "ALLOUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 25,
          "insufficient_24h": 2,
          "reconstruct_error": 0,
          "low_quote_volume": 366,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-15",
        "decision_time_utc": "2025-11-15T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "DASHUSDT",
          "STRKUSDT",
          "ZENUSDT",
          "METUSDT",
          "BTCUSDT",
          "ASTERUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "LTCUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "LINKUSDT",
          "AAVEUSDT",
          "UNIUSDT",
          "MMTUSDT",
          "ICPUSDT",
          "AVAXUSDT",
          "TAOUSDT",
          "PEPEUSDT",
          "HBARUSDT",
          "ENAUSDT",
          "GIGGLEUSDT",
          "FILUSDT",
          "PUMPUSDT"
        ],
        "candidate_count": 29,
        "filter_counts": {
          "missing_1h": 25,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 363,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-16",
        "decision_time_utc": "2025-11-16T00:00:00+00:00",
        "selected_symbols": [
          "DASHUSDT",
          "STRKUSDT",
          "ZECUSDT",
          "KITEUSDT",
          "ZENUSDT",
          "UNIUSDT",
          "ETHUSDT",
          "LTCUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "SOLUSDT",
          "NEARUSDT",
          "FILUSDT",
          "XRPUSDT",
          "ADAUSDT",
          "TRXUSDT",
          "MMTUSDT",
          "ICPUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 25,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 373,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-17",
        "decision_time_utc": "2025-11-17T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "STRKUSDT",
          "ZECUSDT",
          "KITEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DASHUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "UNIUSDT",
          "LINKUSDT",
          "ZENUSDT",
          "ICPUSDT",
          "LTCUSDT",
          "NEARUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 21,
        "filter_counts": {
          "missing_1h": 25,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 372,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-18",
        "decision_time_utc": "2025-11-18T00:00:00+00:00",
        "selected_symbols": [
          "ZENUSDT",
          "ICPUSDT",
          "XPLUSDT",
          "BTCUSDT",
          "UNIUSDT",
          "ETHUSDT",
          "FILUSDT",
          "ZECUSDT",
          "SOLUSDT",
          "KITEUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "STRKUSDT",
          "DASHUSDT",
          "LINKUSDT",
          "LTCUSDT",
          "PUMPUSDT",
          "AVAXUSDT",
          "NEARUSDT",
          "ENAUSDT",
          "BANANAS31USDT"
        ],
        "candidate_count": 26,
        "filter_counts": {
          "missing_1h": 25,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 367,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-19",
        "decision_time_utc": "2025-11-19T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "SOLUSDT",
          "ZENUSDT",
          "PUMPUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "BCHUSDT",
          "TAOUSDT",
          "STRKUSDT",
          "BTCUSDT",
          "ZECUSDT",
          "LTCUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "METUSDT",
          "LINKUSDT",
          "XPLUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "UNIUSDT",
          "TRXUSDT",
          "ICPUSDT",
          "NEARUSDT",
          "FILUSDT",
          "MMTUSDT",
          "AVAXUSDT",
          "DASHUSDT",
          "RESOLVUSDT"
        ],
        "candidate_count": 29,
        "filter_counts": {
          "missing_1h": 25,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 364,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-20",
        "decision_time_utc": "2025-11-20T00:00:00+00:00",
        "selected_symbols": [
          "TNSRUSDT",
          "STRKUSDT",
          "ZECUSDT",
          "FETUSDT",
          "NEARUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "ZENUSDT",
          "ADAUSDT",
          "SUIUSDT",
          "LINKUSDT",
          "XPLUSDT",
          "ICPUSDT",
          "UNIUSDT",
          "LTCUSDT"
        ],
        "candidate_count": 21,
        "filter_counts": {
          "missing_1h": 25,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 372,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-21",
        "decision_time_utc": "2025-11-21T00:00:00+00:00",
        "selected_symbols": [
          "TNSRUSDT",
          "DYMUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "ZECUSDT",
          "XRPUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "STRKUSDT",
          "TRXUSDT",
          "SUIUSDT",
          "LINKUSDT",
          "ADAUSDT",
          "NEARUSDT",
          "PEPEUSDT",
          "XPLUSDT",
          "AVAXUSDT",
          "FETUSDT",
          "UNIUSDT",
          "ALLOUSDT",
          "LTCUSDT",
          "DASHUSDT",
          "ZENUSDT",
          "TAOUSDT"
        ],
        "candidate_count": 26,
        "filter_counts": {
          "missing_1h": 25,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 367,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-22",
        "decision_time_utc": "2025-11-22T00:00:00+00:00",
        "selected_symbols": [
          "BCHUSDT",
          "WLFIUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ASTERUSDT",
          "SOLUSDT",
          "ZECUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "SUIUSDT",
          "STRKUSDT",
          "LINKUSDT",
          "PEPEUSDT",
          "LTCUSDT",
          "AVAXUSDT",
          "TAOUSDT",
          "UNIUSDT",
          "NEARUSDT",
          "XPLUSDT",
          "ENAUSDT",
          "PUMPUSDT",
          "DASHUSDT",
          "HBARUSDT",
          "PENGUUSDT",
          "WLDUSDT",
          "ALLOUSDT",
          "MMTUSDT",
          "DYMUSDT",
          "TNSRUSDT"
        ],
        "candidate_count": 32,
        "filter_counts": {
          "missing_1h": 25,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 361,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-23",
        "decision_time_utc": "2025-11-23T00:00:00+00:00",
        "selected_symbols": [
          "LAYERUSDT",
          "WLFIUSDT",
          "BCHUSDT",
          "MMTUSDT",
          "BTCUSDT",
          "ZECUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "TRXUSDT",
          "SUIUSDT",
          "STRKUSDT",
          "TNSRUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 25,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 377,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-24",
        "decision_time_utc": "2025-11-24T00:00:00+00:00",
        "selected_symbols": [
          "TNSRUSDT",
          "ZECUSDT",
          "HBARUSDT",
          "XRPUSDT",
          "BTCUSDT",
          "STRKUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "LINKUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "ASTERUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 25,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 379,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-25",
        "decision_time_utc": "2025-11-25T00:00:00+00:00",
        "selected_symbols": [
          "ALLOUSDT",
          "SUIUSDT",
          "XRPUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "LINKUSDT",
          "ZECUSDT",
          "WLFIUSDT",
          "TRXUSDT",
          "HBARUSDT",
          "STRKUSDT",
          "TNSRUSDT",
          "TAOUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 25,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 374,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-26",
        "decision_time_utc": "2025-11-26T00:00:00+00:00",
        "selected_symbols": [
          "METUSDT",
          "ENAUSDT",
          "XPLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SUIUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "ZECUSDT",
          "DOGEUSDT",
          "LINKUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "TRXUSDT",
          "TNSRUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 25,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 378,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-27",
        "decision_time_utc": "2025-11-27T00:00:00+00:00",
        "selected_symbols": [
          "BANANAS31USDT",
          "DASHUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "ZECUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "ALLOUSDT",
          "ASTERUSDT",
          "METUSDT",
          "SUIUSDT",
          "ENAUSDT",
          "PLUMEUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 25,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 376,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-28",
        "decision_time_utc": "2025-11-28T00:00:00+00:00",
        "selected_symbols": [
          "METUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "ZECUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 384,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2025-11-29",
        "decision_time_utc": "2025-11-29T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BCHUSDT",
          "METUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "ZECUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ATUSDT",
          "TRXUSDT",
          "ASTERUSDT",
          "SUIUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 380,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-30",
        "decision_time_utc": "2025-11-30T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "SAHARAUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 386,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-01",
        "decision_time_utc": "2025-12-01T00:00:00+00:00",
        "selected_symbols": [
          "GIGGLEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "ZECUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 386,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-02",
        "decision_time_utc": "2025-12-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "ZECUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "LINKUSDT",
          "LTCUSDT",
          "PEPEUSDT",
          "WLFIUSDT",
          "GIGGLEUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 378,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-03",
        "decision_time_utc": "2025-12-03T00:00:00+00:00",
        "selected_symbols": [
          "SUIUSDT",
          "ADAUSDT",
          "SOLUSDT",
          "LINKUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ASTERUSDT",
          "ZECUSDT",
          "TRXUSDT",
          "GIGGLEUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 379,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-04",
        "decision_time_utc": "2025-12-04T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "LINKUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "ASTERUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "XRPUSDT",
          "GIGGLEUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 377,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-05",
        "decision_time_utc": "2025-12-05T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "TRXUSDT",
          "SOLUSDT",
          "XPLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "ASTERUSDT",
          "LINKUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 382,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-06",
        "decision_time_utc": "2025-12-06T00:00:00+00:00",
        "selected_symbols": [
          "LUNCUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "ZECUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "TRXUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 383,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-07",
        "decision_time_utc": "2025-12-07T00:00:00+00:00",
        "selected_symbols": [
          "LUNAUSDT",
          "LUNCUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ZECUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 385,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-08",
        "decision_time_utc": "2025-12-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "ZECUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "LUNCUSDT",
          "TRXUSDT",
          "ATUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 382,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-09",
        "decision_time_utc": "2025-12-09T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "LUNCUSDT",
          "PEPEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ASTERUSDT",
          "DOGEUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 383,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-10",
        "decision_time_utc": "2025-12-10T00:00:00+00:00",
        "selected_symbols": [
          "LUNAUSDT",
          "LUNCUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "ZECUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "LINKUSDT",
          "PEPEUSDT",
          "SUIUSDT",
          "XRPUSDT",
          "ENAUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 377,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-11",
        "decision_time_utc": "2025-12-11T00:00:00+00:00",
        "selected_symbols": [
          "LUNAUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "ZECUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "LUNCUSDT",
          "ASTERUSDT",
          "ATUSDT",
          "TRXUSDT",
          "LINKUSDT",
          "PEPEUSDT",
          "ENAUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 376,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-12",
        "decision_time_utc": "2025-12-12T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "ATUSDT",
          "SUIUSDT",
          "TRXUSDT",
          "LUNAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 381,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-13",
        "decision_time_utc": "2025-12-13T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "ATUSDT",
          "LUNAUSDT",
          "SOLUSDT",
          "ZECUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "DOGEUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 383,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-14",
        "decision_time_utc": "2025-12-14T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "SOLUSDT",
          "ZECUSDT",
          "XRPUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 388,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-15",
        "decision_time_utc": "2025-12-15T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "TRXUSDT",
          "SOLUSDT",
          "ZECUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 385,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-16",
        "decision_time_utc": "2025-12-16T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "TRXUSDT",
          "DOGEUSDT",
          "SUIUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 383,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-17",
        "decision_time_utc": "2025-12-17T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "DOGEUSDT",
          "ZECUSDT",
          "TRXUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 384,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-18",
        "decision_time_utc": "2025-12-18T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "ZECUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "SUIUSDT",
          "TRXUSDT",
          "LINKUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 382,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-19",
        "decision_time_utc": "2025-12-19T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BCHUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "ASTERUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "UNIUSDT",
          "AVAXUSDT",
          "LINKUSDT",
          "PEPEUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 378,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-20",
        "decision_time_utc": "2025-12-20T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "BCHUSDT",
          "SUIUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "ASTERUSDT",
          "XRPUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 382,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2025-12-21",
        "decision_time_utc": "2025-12-21T00:00:00+00:00",
        "selected_symbols": [
          "UNIUSDT",
          "BTCUSDT",
          "XRPUSDT",
          "ETHUSDT",
          "ZECUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 388,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-22",
        "decision_time_utc": "2025-12-22T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "TRXUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "ZECUSDT",
          "BNBUSDT",
          "UNIUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 386,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-23",
        "decision_time_utc": "2025-12-23T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "ZECUSDT",
          "TRXUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 385,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-24",
        "decision_time_utc": "2025-12-24T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "ZECUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 387,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-25",
        "decision_time_utc": "2025-12-25T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 387,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2025-12-26",
        "decision_time_utc": "2025-12-26T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "ZECUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 387,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2025-12-27",
        "decision_time_utc": "2025-12-27T00:00:00+00:00",
        "selected_symbols": [
          "ATUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ZECUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 386,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2025-12-28",
        "decision_time_utc": "2025-12-28T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "FLOWUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 387,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2025-12-29",
        "decision_time_utc": "2025-12-29T00:00:00+00:00",
        "selected_symbols": [
          "UNIUSDT",
          "ZECUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 388,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2025-12-30",
        "decision_time_utc": "2025-12-30T00:00:00+00:00",
        "selected_symbols": [
          "ZBTUSDT",
          "BTCUSDT",
          "ZECUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 382,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2025-12-31",
        "decision_time_utc": "2025-12-31T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "ZECUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 387,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-01-01",
        "decision_time_utc": "2026-01-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "ZECUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BROCCOLI714USDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 386,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-01-02",
        "decision_time_utc": "2026-01-02T00:00:00+00:00",
        "selected_symbols": [
          "PEPEUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "BROCCOLI714USDT",
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "ZECUSDT",
          "XRPUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 385,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-03",
        "decision_time_utc": "2026-01-03T00:00:00+00:00",
        "selected_symbols": [
          "PEPEUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "SUIUSDT",
          "XRPUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "LINKUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ZECUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 383,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-01-04",
        "decision_time_utc": "2026-01-04T00:00:00+00:00",
        "selected_symbols": [
          "BCHUSDT",
          "ZECUSDT",
          "SUIUSDT",
          "BTCUSDT",
          "PEPEUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "TRXUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 384,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-05",
        "decision_time_utc": "2026-01-05T00:00:00+00:00",
        "selected_symbols": [
          "BROCCOLI714USDT",
          "BONKUSDT",
          "WIFUSDT",
          "PEPEUSDT",
          "PENGUUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "ASTERUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "SOLUSDT",
          "SUIUSDT",
          "ZECUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 379,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-01-06",
        "decision_time_utc": "2026-01-06T00:00:00+00:00",
        "selected_symbols": [
          "VIRTUALUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "UNIUSDT",
          "SOLUSDT",
          "LINKUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "PEPEUSDT",
          "BCHUSDT",
          "ZECUSDT",
          "ASTERUSDT",
          "TRXUSDT",
          "BROCCOLI714USDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 376,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-01-07",
        "decision_time_utc": "2026-01-07T00:00:00+00:00",
        "selected_symbols": [
          "BROCCOLI714USDT",
          "TAOUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "WIFUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "ASTERUSDT",
          "SUIUSDT",
          "ZECUSDT",
          "DOGEUSDT",
          "LINKUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 376,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-01-08",
        "decision_time_utc": "2026-01-08T00:00:00+00:00",
        "selected_symbols": [
          "BREVUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "TRXUSDT",
          "BNBUSDT",
          "ZECUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "SUIUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 2,
          "reconstruct_error": 0,
          "low_quote_volume": 384,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-01-09",
        "decision_time_utc": "2026-01-09T00:00:00+00:00",
        "selected_symbols": [
          "TAOUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ZECUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "TRXUSDT",
          "币安人生USDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 385,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-01-10",
        "decision_time_utc": "2026-01-10T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "TRXUSDT",
          "ZECUSDT",
          "PEPEUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "SUIUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 387,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-11",
        "decision_time_utc": "2026-01-11T00:00:00+00:00",
        "selected_symbols": [
          "币安人生USDT",
          "POLUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ZECUSDT",
          "SOLUSDT",
          "XRPUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 390,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-12",
        "decision_time_utc": "2026-01-12T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ZECUSDT",
          "BCHUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "DOGEUSDT",
          "币安人生USDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 388,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-13",
        "decision_time_utc": "2026-01-13T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "BCHUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "LTCUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 385,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-14",
        "decision_time_utc": "2026-01-14T00:00:00+00:00",
        "selected_symbols": [
          "DASHUSDT",
          "币安人生USDT",
          "PEPEUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "SUIUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "BREVUSDT",
          "LTCUSDT",
          "TRXUSDT",
          "ZECUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 19,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 380,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-01-15",
        "decision_time_utc": "2026-01-15T00:00:00+00:00",
        "selected_symbols": [
          "币安人生USDT",
          "DASHUSDT",
          "ICPUSDT",
          "ZENUSDT",
          "ZECUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "ASTERUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "PEPEUSDT",
          "LTCUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "BCHUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 19,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 379,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-01-16",
        "decision_time_utc": "2026-01-16T00:00:00+00:00",
        "selected_symbols": [
          "ZENUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "TRXUSDT",
          "DASHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "ZECUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "LTCUSDT",
          "ICPUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "ADAUSDT",
          "币安人生USDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 2,
          "reconstruct_error": 0,
          "low_quote_volume": 381,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-01-17",
        "decision_time_utc": "2026-01-17T00:00:00+00:00",
        "selected_symbols": [
          "DASHUSDT",
          "LTCUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "ZENUSDT",
          "ETHUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "ZECUSDT",
          "FOGOUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 387,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-18",
        "decision_time_utc": "2026-01-18T00:00:00+00:00",
        "selected_symbols": [
          "AXSUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BREVUSDT",
          "BNBUSDT",
          "SOLUSDT",
          "DASHUSDT",
          "XRPUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 392,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-19",
        "decision_time_utc": "2026-01-19T00:00:00+00:00",
        "selected_symbols": [
          "DASHUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "AXSUSDT",
          "TRXUSDT",
          "ZECUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 390,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-20",
        "decision_time_utc": "2026-01-20T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "ZECUSDT",
          "BREVUSDT",
          "ADAUSDT",
          "DASHUSDT",
          "TRXUSDT",
          "ASTERUSDT",
          "LTCUSDT",
          "PEPEUSDT",
          "LINKUSDT",
          "DUSKUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 383,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-01-21",
        "decision_time_utc": "2026-01-21T00:00:00+00:00",
        "selected_symbols": [
          "AXSUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BREVUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "ZECUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "DASHUSDT",
          "SUIUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 387,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-01-22",
        "decision_time_utc": "2026-01-22T00:00:00+00:00",
        "selected_symbols": [
          "AXSUSDT",
          "币安人生USDT",
          "ETHUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "XRPUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "SUIUSDT",
          "ZECUSDT",
          "BNBUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 387,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-01-23",
        "decision_time_utc": "2026-01-23T00:00:00+00:00",
        "selected_symbols": [
          "FOGOUSDT",
          "AXSUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ZECUSDT",
          "TRXUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 2,
          "reconstruct_error": 0,
          "low_quote_volume": 390,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-24",
        "decision_time_utc": "2026-01-24T00:00:00+00:00",
        "selected_symbols": [
          "AXSUSDT",
          "DASHUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "SENTUSDT",
          "ZECUSDT",
          "DOGEUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 391,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-01-25",
        "decision_time_utc": "2026-01-25T00:00:00+00:00",
        "selected_symbols": [
          "ENSOUSDT",
          "SOMIUSDT",
          "FOGOUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 395,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-01-26",
        "decision_time_utc": "2026-01-26T00:00:00+00:00",
        "selected_symbols": [
          "NOMUSDT",
          "ZKCUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "FOGOUSDT",
          "XRPUSDT",
          "ZKPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ZECUSDT",
          "SUIUSDT",
          "SOMIUSDT",
          "ENSOUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 388,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-01-27",
        "decision_time_utc": "2026-01-27T00:00:00+00:00",
        "selected_symbols": [
          "AXSUSDT",
          "ZECUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "ZKPUSDT",
          "XRPUSDT",
          "FOGOUSDT",
          "SUIUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 391,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-28",
        "decision_time_utc": "2026-01-28T00:00:00+00:00",
        "selected_symbols": [
          "PUMPUSDT",
          "ZECUSDT",
          "FOGOUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "ZKPUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 392,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-29",
        "decision_time_utc": "2026-01-29T00:00:00+00:00",
        "selected_symbols": [
          "WLDUSDT",
          "FOGOUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "ZECUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 393,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-30",
        "decision_time_utc": "2026-01-30T00:00:00+00:00",
        "selected_symbols": [
          "SENTUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "FOGOUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "WLDUSDT",
          "SUIUSDT",
          "ZECUSDT",
          "TRXUSDT",
          "AVAXUSDT",
          "PUMPUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 388,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-01-31",
        "decision_time_utc": "2026-01-31T00:00:00+00:00",
        "selected_symbols": [
          "SENTUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "TRXUSDT",
          "ZECUSDT",
          "ADAUSDT",
          "PEPEUSDT",
          "LINKUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 389,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-02-01",
        "decision_time_utc": "2026-02-01T00:00:00+00:00",
        "selected_symbols": [
          "SENTUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "ZECUSDT",
          "LINKUSDT",
          "AVAXUSDT",
          "LTCUSDT",
          "TRXUSDT",
          "PEPEUSDT",
          "ASTERUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 385,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-02-02",
        "decision_time_utc": "2026-02-02T00:00:00+00:00",
        "selected_symbols": [
          "ZKUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "ZECUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "SENTUSDT",
          "TRXUSDT",
          "ADAUSDT",
          "LINKUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 389,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-02-03",
        "decision_time_utc": "2026-02-03T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "SUIUSDT",
          "LINKUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "SENTUSDT",
          "ZECUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 390,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-02-04",
        "decision_time_utc": "2026-02-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "SENTUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "ZECUSDT",
          "SUIUSDT",
          "LINKUSDT",
          "ADAUSDT",
          "PEPEUSDT",
          "ZAMAUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 389,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-02-05",
        "decision_time_utc": "2026-02-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "SENTUSDT",
          "PEPEUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "ZECUSDT",
          "SUIUSDT",
          "TRXUSDT",
          "LINKUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 391,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-02-06",
        "decision_time_utc": "2026-02-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "SENTUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ZECUSDT",
          "SUIUSDT",
          "ADAUSDT",
          "TRXUSDT",
          "LINKUSDT",
          "AVAXUSDT",
          "PEPEUSDT",
          "LTCUSDT",
          "ASTERUSDT",
          "TRUMPUSDT",
          "NEARUSDT",
          "TAOUSDT",
          "AAVEUSDT",
          "UNIUSDT"
        ],
        "candidate_count": 21,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 382,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-02-07",
        "decision_time_utc": "2026-02-07T00:00:00+00:00",
        "selected_symbols": [
          "XRPUSDT",
          "ASTERUSDT",
          "ZECUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "HBARUSDT",
          "SUIUSDT",
          "BCHUSDT",
          "PEPEUSDT",
          "SOLUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "LINKUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "PUMPUSDT",
          "LTCUSDT",
          "TAOUSDT",
          "SENTUSDT",
          "TRXUSDT",
          "WLFIUSDT"
        ],
        "candidate_count": 21,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 382,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-02-08",
        "decision_time_utc": "2026-02-08T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "TRXUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ZECUSDT",
          "LINKUSDT",
          "SUIUSDT",
          "PEPEUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 391,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-02-09",
        "decision_time_utc": "2026-02-09T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "ZAMAUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "ZECUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 393,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-02-10",
        "decision_time_utc": "2026-02-10T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "ZAMAUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "ZECUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 394,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-02-11",
        "decision_time_utc": "2026-02-11T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ZAMAUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 396,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-02-12",
        "decision_time_utc": "2026-02-12T00:00:00+00:00",
        "selected_symbols": [
          "ZROUSDT",
          "ASTERUSDT",
          "BTCUSDT",
          "ZECUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "BERAUSDT",
          "DOGEUSDT",
          "TRXUSDT",
          "UNIUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 390,
          "low_trades": 1,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-02-13",
        "decision_time_utc": "2026-02-13T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ASTERUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "BERAUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 394,
          "low_trades": 1,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-02-14",
        "decision_time_utc": "2026-02-14T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 396,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-02-15",
        "decision_time_utc": "2026-02-15T00:00:00+00:00",
        "selected_symbols": [
          "PEPEUSDT",
          "ZECUSDT",
          "DOGEUSDT",
          "ZAMAUSDT",
          "XRPUSDT",
          "TAOUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 394,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-02-16",
        "decision_time_utc": "2026-02-16T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "ZECUSDT",
          "BNBUSDT",
          "ZAMAUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 395,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-02-17",
        "decision_time_utc": "2026-02-17T00:00:00+00:00",
        "selected_symbols": [
          "ZAMAUSDT",
          "TAOUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "PEPEUSDT",
          "DOGEUSDT",
          "ZECUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 394,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-02-18",
        "decision_time_utc": "2026-02-18T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "ZAMAUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "ZECUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 396,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-02-19",
        "decision_time_utc": "2026-02-19T00:00:00+00:00",
        "selected_symbols": [
          "WLFIUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "ZECUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 396,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-02-20",
        "decision_time_utc": "2026-02-20T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "TRXUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 397,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-02-21",
        "decision_time_utc": "2026-02-21T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 397,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-02-22",
        "decision_time_utc": "2026-02-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 399,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-02-23",
        "decision_time_utc": "2026-02-23T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 400,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-02-24",
        "decision_time_utc": "2026-02-24T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "USD1USDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 397,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-25",
        "decision_time_utc": "2026-02-25T00:00:00+00:00",
        "selected_symbols": [
          "ESPUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 397,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-02-26",
        "decision_time_utc": "2026-02-26T00:00:00+00:00",
        "selected_symbols": [
          "DOTUSDT",
          "UNIUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "LINKUSDT",
          "SUIUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "PEPEUSDT",
          "ZECUSDT",
          "ENSOUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 389,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-02-27",
        "decision_time_utc": "2026-02-27T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "ZECUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 396,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-02-28",
        "decision_time_utc": "2026-02-28T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 398,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-01",
        "decision_time_utc": "2026-03-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "SUIUSDT",
          "ZECUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 395,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-02",
        "decision_time_utc": "2026-03-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "SUIUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 397,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-03",
        "decision_time_utc": "2026-03-03T00:00:00+00:00",
        "selected_symbols": [
          "NEARUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 395,
          "low_trades": 1,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-04",
        "decision_time_utc": "2026-03-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "NEARUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 395,
          "low_trades": 1,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-05",
        "decision_time_utc": "2026-03-05T00:00:00+00:00",
        "selected_symbols": [
          "DOGEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ZECUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "PEPEUSDT",
          "ADAUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "ENSOUSDT",
          "NEARUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 11,
          "insufficient_24h": 2,
          "reconstruct_error": 0,
          "low_quote_volume": 390,
          "low_trades": 1,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-06",
        "decision_time_utc": "2026-03-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 398,
          "low_trades": 1,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-07",
        "decision_time_utc": "2026-03-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ROBOUSDT",
          "KITEUSDT",
          "OPNUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 398,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-08",
        "decision_time_utc": "2026-03-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 403,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-09",
        "decision_time_utc": "2026-03-09T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 401,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-10",
        "decision_time_utc": "2026-03-10T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SUIUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 400,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-11",
        "decision_time_utc": "2026-03-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "ZECUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "ADAUSDT",
          "SUIUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 398,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-12",
        "decision_time_utc": "2026-03-12T00:00:00+00:00",
        "selected_symbols": [
          "PIXELUSDT",
          "ICPUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 9,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 399,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-13",
        "decision_time_utc": "2026-03-13T00:00:00+00:00",
        "selected_symbols": [
          "OPNUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 9,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 400,
          "low_trades": 1,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-14",
        "decision_time_utc": "2026-03-14T00:00:00+00:00",
        "selected_symbols": [
          "TRUMPUSDT",
          "TAOUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "NIGHTUSDT",
          "SUIUSDT",
          "PEPEUSDT",
          "ADAUSDT",
          "OPNUSDT",
          "ZECUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 9,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 394,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-15",
        "decision_time_utc": "2026-03-15T00:00:00+00:00",
        "selected_symbols": [
          "OPNUSDT",
          "TRUMPUSDT",
          "BTCUSDT",
          "NIGHTUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 9,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 401,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-16",
        "decision_time_utc": "2026-03-16T00:00:00+00:00",
        "selected_symbols": [
          "TAOUSDT",
          "ZECUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "OPNUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "NIGHTUSDT",
          "DOGEUSDT",
          "TRUMPUSDT",
          "THEUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 9,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 396,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-17",
        "decision_time_utc": "2026-03-17T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "FETUSDT",
          "PEPEUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "SUIUSDT",
          "LINKUSDT",
          "NIGHTUSDT",
          "BNBUSDT",
          "OPNUSDT",
          "TAOUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 393,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-18",
        "decision_time_utc": "2026-03-18T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "OPNUSDT",
          "ASTERUSDT",
          "ZECUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "NIGHTUSDT",
          "PEPEUSDT",
          "TAOUSDT",
          "SUIUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 396,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-19",
        "decision_time_utc": "2026-03-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "OPNUSDT",
          "NIGHTUSDT",
          "DOGEUSDT",
          "ZECUSDT",
          "BNBUSDT",
          "PEPEUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 399,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-20",
        "decision_time_utc": "2026-03-20T00:00:00+00:00",
        "selected_symbols": [
          "OPNUSDT",
          "TAOUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "NIGHTUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ZECUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 400,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-21",
        "decision_time_utc": "2026-03-21T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "NIGHTUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "TAOUSDT",
          "BNBUSDT",
          "ZECUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 402,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-22",
        "decision_time_utc": "2026-03-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "NIGHTUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 405,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-23",
        "decision_time_utc": "2026-03-23T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "NIGHTUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 403,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-24",
        "decision_time_utc": "2026-03-24T00:00:00+00:00",
        "selected_symbols": [
          "NIGHTUSDT",
          "TAOUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "ZECUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "LINKUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 398,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-25",
        "decision_time_utc": "2026-03-25T00:00:00+00:00",
        "selected_symbols": [
          "TAOUSDT",
          "ZECUSDT",
          "BTCUSDT",
          "NIGHTUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 400,
          "low_trades": 1,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-26",
        "decision_time_utc": "2026-03-26T00:00:00+00:00",
        "selected_symbols": [
          "SAHARAUSDT",
          "BTCUSDT",
          "TAOUSDT",
          "ETHUSDT",
          "NIGHTUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "ROBOUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "ZECUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 398,
          "low_trades": 1,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-27",
        "decision_time_utc": "2026-03-27T00:00:00+00:00",
        "selected_symbols": [
          "ROBOUSDT",
          "NIGHTUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "TAOUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "KATUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 400,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-28",
        "decision_time_utc": "2026-03-28T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "NIGHTUSDT",
          "ROBOUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "TAOUSDT",
          "CFGUSDT",
          "BNBUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 401,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-29",
        "decision_time_utc": "2026-03-29T00:00:00+00:00",
        "selected_symbols": [
          "NIGHTUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "TAOUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 404,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-30",
        "decision_time_utc": "2026-03-30T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "NIGHTUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 405,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-03-31",
        "decision_time_utc": "2026-03-31T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "NIGHTUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "TAOUSDT",
          "TRXUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 402,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-04-01",
        "decision_time_utc": "2026-04-01T00:00:00+00:00",
        "selected_symbols": [
          "NIGHTUSDT",
          "ZECUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "TAOUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 402,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-04-02",
        "decision_time_utc": "2026-04-02T00:00:00+00:00",
        "selected_symbols": [
          "STOUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "ZECUSDT",
          "XRPUSDT",
          "NIGHTUSDT",
          "TAOUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 401,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-04-03",
        "decision_time_utc": "2026-04-03T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XPLUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "NIGHTUSDT",
          "KATUSDT",
          "ZECUSDT",
          "TAOUSDT",
          "DOGEUSDT",
          "UNIUSDT",
          "NOMUSDT",
          "SOLVUSDT",
          "STOUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 396,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-04-04",
        "decision_time_utc": "2026-04-04T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "NIGHTUSDT",
          "XRPUSDT",
          "STOUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 405,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-04-05",
        "decision_time_utc": "2026-04-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "STOUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 406,
          "low_trades": 2,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-06",
        "decision_time_utc": "2026-04-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "STOUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 406,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-04-07",
        "decision_time_utc": "2026-04-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "ZECUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "TAOUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 403,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-04-08",
        "decision_time_utc": "2026-04-08T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "PEPEUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "TAOUSDT",
          "AVAXUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 401,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-04-09",
        "decision_time_utc": "2026-04-09T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "ZECUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "TAOUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 403,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-04-10",
        "decision_time_utc": "2026-04-10T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "TAOUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 403,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-04-11",
        "decision_time_utc": "2026-04-11T00:00:00+00:00",
        "selected_symbols": [
          "DASHUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ZECUSDT",
          "SOLUSDT",
          "TAOUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 403,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-04-12",
        "decision_time_utc": "2026-04-12T00:00:00+00:00",
        "selected_symbols": [
          "币安人生USDT",
          "TAOUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "ZECUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 404,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-04-13",
        "decision_time_utc": "2026-04-13T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "ZECUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 405,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-04-14",
        "decision_time_utc": "2026-04-14T00:00:00+00:00",
        "selected_symbols": [
          "GIGGLEUSDT",
          "币安人生USDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ZECUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 402,
          "low_trades": 1,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-04-15",
        "decision_time_utc": "2026-04-15T00:00:00+00:00",
        "selected_symbols": [
          "币安人生USDT",
          "GIGGLEUSDT",
          "ENJUSDT",
          "ZAMAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "XAUTUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "BARDUSDT",
          "ZECUSDT",
          "PEPEUSDT",
          "TAOUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 395,
          "low_trades": 2,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-04-16",
        "decision_time_utc": "2026-04-16T00:00:00+00:00",
        "selected_symbols": [
          "ENJUSDT",
          "BARDUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "XAUTUSDT",
          "ZECUSDT",
          "币安人生USDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 401,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-04-17",
        "decision_time_utc": "2026-04-17T00:00:00+00:00",
        "selected_symbols": [
          "ORDIUSDT",
          "NEIROUSDT",
          "BIOUSDT",
          "PEPEUSDT",
          "SOLUSDT",
          "BARDUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "币安人生USDT",
          "XAUTUSDT",
          "ZECUSDT",
          "ENJUSDT",
          "SIGNUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 394,
          "low_trades": 1,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-04-18",
        "decision_time_utc": "2026-04-18T00:00:00+00:00",
        "selected_symbols": [
          "MOVRUSDT",
          "币安人生USDT",
          "BTCUSDT",
          "ETHUSDT",
          "XAUTUSDT",
          "XRPUSDT",
          "AVNTUSDT",
          "SOLUSDT",
          "TAOUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "PEPEUSDT",
          "ZECUSDT",
          "ADAUSDT",
          "ORDIUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 396,
          "low_trades": 1,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-04-19",
        "decision_time_utc": "2026-04-19T00:00:00+00:00",
        "selected_symbols": [
          "币安人生USDT",
          "BTCUSDT",
          "ETHUSDT",
          "AVNTUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "HIGHUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 403,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-04-20",
        "decision_time_utc": "2026-04-20T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "TREEUSDT",
          "ZECUSDT",
          "币安人生USDT",
          "AAVEUSDT",
          "TRXUSDT",
          "BNBUSDT",
          "HIGHUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 399,
          "low_trades": 1,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-04-21",
        "decision_time_utc": "2026-04-21T00:00:00+00:00",
        "selected_symbols": [
          "ORDIUSDT",
          "币安人生USDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 402,
          "low_trades": 1,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-04-22",
        "decision_time_utc": "2026-04-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "ZECUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "币安人生USDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 404,
          "low_trades": 1,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-04-23",
        "decision_time_utc": "2026-04-23T00:00:00+00:00",
        "selected_symbols": [
          "CHIPUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "ZECUSDT",
          "币安人生USDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 403,
          "low_trades": 1,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-04-24",
        "decision_time_utc": "2026-04-24T00:00:00+00:00",
        "selected_symbols": [
          "SPKUSDT",
          "ZECUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "CHIPUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 403,
          "low_trades": 1,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-04-25",
        "decision_time_utc": "2026-04-25T00:00:00+00:00",
        "selected_symbols": [
          "KATUSDT",
          "APEUSDT",
          "ZECUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "CHIPUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 404,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-04-26",
        "decision_time_utc": "2026-04-26T00:00:00+00:00",
        "selected_symbols": [
          "AXSUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "TRUMPUSDT",
          "CHIPUSDT",
          "APEUSDT",
          "KATUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 405,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-27",
        "decision_time_utc": "2026-04-27T00:00:00+00:00",
        "selected_symbols": [
          "ZBTUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "CHIPUSDT",
          "ORCAUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 407,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-28",
        "decision_time_utc": "2026-04-28T00:00:00+00:00",
        "selected_symbols": [
          "PENGUUSDT",
          "CHIPUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ORCAUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 404,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-04-29",
        "decision_time_utc": "2026-04-29T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "CHIPUSDT",
          "DOGEUSDT",
          "SOLUSDT",
          "TONUSDT",
          "XRPUSDT",
          "PENGUUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 405,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-30",
        "decision_time_utc": "2026-04-30T00:00:00+00:00",
        "selected_symbols": [
          "DOGEUSDT",
          "BTCUSDT",
          "TONUSDT",
          "ETHUSDT",
          "CHIPUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "PEPEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 404,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-05-01",
        "decision_time_utc": "2026-05-01T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "CHIPUSDT",
          "SOLUSDT",
          "PLUMEUSDT",
          "XRPUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 405,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-02",
        "decision_time_utc": "2026-05-02T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "CHIPUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 406,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-03",
        "decision_time_utc": "2026-05-03T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 409,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-04",
        "decision_time_utc": "2026-05-04T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "BTCUSDT",
          "TRXUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "CHIPUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 409,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-05",
        "decision_time_utc": "2026-05-05T00:00:00+00:00",
        "selected_symbols": [
          "TSTUSDT",
          "DASHUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ZECUSDT",
          "DOGEUSDT",
          "LINKUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "PEPEUSDT",
          "XRPUSDT",
          "CHIPUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 402,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-05-06",
        "decision_time_utc": "2026-05-06T00:00:00+00:00",
        "selected_symbols": [
          "DOGSUSDT",
          "ZECUSDT",
          "TONUSDT",
          "LUNCUSDT",
          "PENGUUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "PEPEUSDT",
          "XRPUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 402,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-07",
        "decision_time_utc": "2026-05-07T00:00:00+00:00",
        "selected_symbols": [
          "TONUSDT",
          "FILUSDT",
          "NEARUSDT",
          "ZECUSDT",
          "TAOUSDT",
          "SOLUSDT",
          "DASHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ETHUSDT",
          "SUIUSDT",
          "XRPUSDT",
          "IOUSDT",
          "PEPEUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 399,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-05-08",
        "decision_time_utc": "2026-05-08T00:00:00+00:00",
        "selected_symbols": [
          "DOGSUSDT",
          "NOTUSDT",
          "TONUSDT",
          "ZECUSDT",
          "VANAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "DOGEUSDT",
          "XRPUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 403,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-05-09",
        "decision_time_utc": "2026-05-09T00:00:00+00:00",
        "selected_symbols": [
          "CHIPUSDT",
          "ONDOUSDT",
          "STRKUSDT",
          "FILUSDT",
          "ZECUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "TONUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 402,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-05-10",
        "decision_time_utc": "2026-05-10T00:00:00+00:00",
        "selected_symbols": [
          "SUIUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "CHIPUSDT",
          "ZECUSDT",
          "XRPUSDT",
          "TONUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ONDOUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 403,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-11",
        "decision_time_utc": "2026-05-11T00:00:00+00:00",
        "selected_symbols": [
          "SUIUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "UNIUSDT",
          "DOGEUSDT",
          "TAOUSDT",
          "PEPEUSDT",
          "BNBUSDT",
          "TONUSDT",
          "CHIPUSDT",
          "ZECUSDT",
          "LAYERUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 400,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-05-12",
        "decision_time_utc": "2026-05-12T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "CHIPUSDT",
          "SUIUSDT",
          "DOGEUSDT",
          "ZECUSDT",
          "TONUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 403,
          "low_trades": 1,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-05-13",
        "decision_time_utc": "2026-05-13T00:00:00+00:00",
        "selected_symbols": [
          "SAGAUSDT",
          "CHIPUSDT",
          "BTCUSDT",
          "ZECUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "DOGEUSDT",
          "TONUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 403,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-05-14",
        "decision_time_utc": "2026-05-14T00:00:00+00:00",
        "selected_symbols": [
          "INJUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "CHIPUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "ZECUSDT",
          "SPKUSDT",
          "SUIUSDT",
          "SAGAUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 402,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-05-15",
        "decision_time_utc": "2026-05-15T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "XRPUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "SPKUSDT",
          "BNBUSDT",
          "TONUSDT",
          "SUIUSDT",
          "SAGAUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 403,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-05-16",
        "decision_time_utc": "2026-05-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "LAYERUSDT",
          "ZECUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 405,
          "low_trades": 1,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-05-17",
        "decision_time_utc": "2026-05-17T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "SPKUSDT",
          "ZECUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 407,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-05-18",
        "decision_time_utc": "2026-05-18T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 408,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-19",
        "decision_time_utc": "2026-05-19T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 407,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-05-20",
        "decision_time_utc": "2026-05-20T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ZECUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 408,
          "low_trades": 1,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-05-21",
        "decision_time_utc": "2026-05-21T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "XRPUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 409,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-05-22",
        "decision_time_utc": "2026-05-22T00:00:00+00:00",
        "selected_symbols": [
          "NEARUSDT",
          "SUIUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "XRPUSDT",
          "ZECUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 406,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-05-23",
        "decision_time_utc": "2026-05-23T00:00:00+00:00",
        "selected_symbols": [
          "NEARUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "ZECUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "WLDUSDT",
          "BNBUSDT",
          "ONDOUSDT",
          "DOGEUSDT",
          "EDENUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 2,
          "reconstruct_error": 0,
          "low_quote_volume": 403,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-05-24",
        "decision_time_utc": "2026-05-24T00:00:00+00:00",
        "selected_symbols": [
          "NEARUSDT",
          "ZECUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SAHARAUSDT",
          "SOLUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "MEGAUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 406,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-05-25",
        "decision_time_utc": "2026-05-25T00:00:00+00:00",
        "selected_symbols": [
          "ZECUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "NEARUSDT",
          "XRPUSDT",
          "SUIUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 410,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-05-26",
        "decision_time_utc": "2026-05-26T00:00:00+00:00",
        "selected_symbols": [
          "NEARUSDT",
          "TONUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "TRXUSDT",
          "BNBUSDT",
          "SOLUSDT",
          "ZECUSDT",
          "XRPUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 408,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-05-27",
        "decision_time_utc": "2026-05-27T00:00:00+00:00",
        "selected_symbols": [
          "WLDUSDT",
          "FETUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ZECUSDT",
          "SOLUSDT",
          "NEARUSDT",
          "TRXUSDT",
          "XRPUSDT",
          "OPGUSDT",
          "BNBUSDT",
          "SUIUSDT",
          "TAOUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 401,
          "low_trades": 2,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-05-28",
        "decision_time_utc": "2026-05-28T00:00:00+00:00",
        "selected_symbols": [
          "XLMUSDT",
          "ALTUSDT",
          "GENIUSUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "NEARUSDT",
          "OPGUSDT",
          "ZECUSDT",
          "XRPUSDT",
          "SUIUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "WLDUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 402,
          "low_trades": 1,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-05-29",
        "decision_time_utc": "2026-05-29T00:00:00+00:00",
        "selected_symbols": [
          "ALLOUSDT",
          "XLMUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ZECUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "OPGUSDT",
          "NEARUSDT",
          "BNBUSDT",
          "TRXUSDT",
          "GENIUSUSDT",
          "DOGEUSDT",
          "SUIUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 402,
          "low_trades": 1,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-05-30",
        "decision_time_utc": "2026-05-30T00:00:00+00:00",
        "selected_symbols": [
          "XLMUSDT",
          "ALLOUSDT",
          "HBARUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "NEARUSDT",
          "ZECUSDT",
          "TRXUSDT",
          "MEGAUSDT",
          "SUIUSDT",
          "GENIUSUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 403,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-05-31",
        "decision_time_utc": "2026-05-31T00:00:00+00:00",
        "selected_symbols": [
          "WLDUSDT",
          "FETUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "XRPUSDT",
          "XLMUSDT",
          "SOLUSDT",
          "HBARUSDT",
          "ZECUSDT",
          "NEARUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 406,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2026-06-01",
        "decision_time_utc": "2026-06-01T00:00:00+00:00",
        "selected_symbols": [
          "PORTALUSDT",
          "币安人生USDT",
          "XLMUSDT",
          "ZECUSDT",
          "NEARUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "SOLUSDT",
          "XRPUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 406,
          "low_trades": 1,
          "stable_like": 1
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
