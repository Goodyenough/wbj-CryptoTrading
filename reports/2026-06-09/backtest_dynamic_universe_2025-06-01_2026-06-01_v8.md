---
created: 2026-06-09 14:50:42 CST
tags:
  - crypto
  - trading-system
  - backtest
backtest_run_id: f78c745ccefc
report_version: v8
sample_sufficient: true
universe_mode: true
universe_type: dynamic
---

# 回测报告 2025-06-01 至 2026-06-01 v8

- 回测 ID：`f78c745ccefc`
- 交易对：`0GUSDT`, `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1INCHUSDT`, `2ZUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACHUSDT`, `ADAUSDT`, `AEVOUSDT`, `AIGENSYNUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALCXUSDT`, `ALGOUSDT`, `ALICEUSDT`, `ALLOUSDT`, `ALPINEUSDT`, `ALTUSDT`, `ANIMEUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ASRUSDT`, `ASTERUSDT`, `ATMUSDT`, `ATOMUSDT`, `ATUSDT`, `AUCTIONUSDT`, `AUSDT`, `AVAXUSDT`, `AVNTUSDT`, `AWEUSDT`, `AXLUSDT`, `AXSUSDT`, `BABYUSDT`, `BANANAS31USDT`, `BARDUSDT`, `BATUSDT`, `BBUSDT`, `BCHUSDT`, `BELUSDT`, `BERAUSDT`, `BIOUSDT`, `BMTUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BREVUSDT`, `BROCCOLI714USDT`, `BTCUSDT`, `C98USDT`, `CAKEUSDT`, `CELOUSDT`, `CFGUSDT`, `CFXUSDT`, `CHIPUSDT`, `CHZUSDT`, `CKBUSDT`, `COMPUSDT`, `COSUSDT`, `COTIUSDT`, `COWUSDT`, `CRVUSDT`, `CTSIUSDT`, `CUSDT`, `CYBERUSDT`, `DASHUSDT`, `DCRUSDT`, `DEXEUSDT`, `DIAUSDT`, `DOGEUSDT`, `DOGSUSDT`, `DOLOUSDT`, `DOTUSDT`, `DUSDT`, `DUSKUSDT`, `DYDXUSDT`, `DYMUSDT`, `EDENUSDT`, `EDUUSDT`, `EIGENUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSOUSDT`, `ENSUSDT`, `EPICUSDT`, `ERAUSDT`, `ESPUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `EULUSDT`, `FETUSDT`, `FFUSDT`, `FIDAUSDT`, `FILUSDT`, `FLOKIUSDT`, `FLOWUSDT`, `FLUXUSDT`, `FOGOUSDT`, `FORMUSDT`, `FRAXUSDT`, `FUSDT`, `GALAUSDT`
- UTC 区间：2025-06-01T00:00:00+00:00 -> 2026-06-01T00:00:00+00:00
- 初始权益：10,000.00 USDT
- 最终权益：8,696.42 USDT
- 净收益：-13.04%
- 代码 commit：`c330af5b5b1c8691611578c246f5405ead0ece2d`
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
- Master symbols / Master 币种数：150
- Source limit / 调试截断：150
- Source limit applied / 是否截断：true
- Refresh frequency / 刷新频率：daily
- Universe refreshes / Universe 刷新次数：366
- Selected symbols per refresh / 每次入选数量：min=3, avg=10.37, max=35
- Top selected symbols / 最常入选：`BNBUSDT`(366), `BTCUSDT`(366), `ETHUSDT`(366), `DOGEUSDT`(361), `ADAUSDT`(288), `AVAXUSDT`(226), `ENAUSDT`(199), `AAVEUSDT`(132), `BCHUSDT`(122), `ASTERUSDT`(111)
- Filter counts / 过滤统计：
```json
{
  "missing_1h": 3908,
  "insufficient_24h": 24,
  "reconstruct_error": 0,
  "low_quote_volume": 47156,
  "low_trades": 16,
  "stable_like": 2
}
```
> Warning / 警告：dynamic universe 的 symbol master 来自当前 Binance exchangeInfo；历史上曾交易但今天已退市的币不会进入 master list，因此仍有退市幸存者偏差。
> Runtime / 耗时提示：第一次完整运行需要缓存大量 1h/4h/1d K 线，可能很慢；缓存命中后后续回测会明显加快。

## 核心指标

| Metric（指标） | Value（数值） |
|---|---:|
| Trades（计划总数） | 185 |
| Closed trades（已结束交易） | 55 |
| Open trades（仍开放持仓） | 3 |
| Win rate（胜率） | 21.82% |
| Profit factor（盈利因子） | 0.70 |
| Avg R（平均R倍数） | -0.22 |
| Net return（净收益率） | -13.04% |
| Max drawdown（最大回撤） | 3,040.59 / 26.71% |
| Intrabar max drawdown（K线内最大回撤） | 2,921.28 / 25.97% |
| TP1 touched rate（第一止盈触达率） | 32.73% |
| TP2 close rate（第二止盈平仓率） | 21.82% |
| Stop rate（止损率） | 78.18% |
| Fee drag（手续费拖累） | 90.95 USDT |
| Tail max single loss（最大单笔亏损） | -116.34 USDT |
| CAGR（年化复合收益率） | -13.04% |
| Sharpe（夏普比率） | -0.65 |
| Sortino（索提诺比率） | -0.73 |
| Exposure（持仓暴露时间） | 86.12% |
| Turnover（换手率） | 7.62 |
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
| Equal-weight symbols（等权持有本次币种） | -56.92% |

## 已结束交易

| Symbol（交易对） | Status（状态） | Created（创建时间） | Entry（入场价） | Exit（出场价） | Qty（数量） | Gross PnL（毛盈亏） | Net PnL（净盈亏） | Net R（净R倍数） | Fees（手续费） | Notes（备注） |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| `ETHUSDT` | STOPPED（已止损） | 2025-06-02T16:00:00+00:00 | 2,553.30 | 2,429.10 | 0.83 | -103.08 | -105.94 | -1.05 | 2.86 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-06-06T16:00:00+00:00 | 105,460.26 | 98,767.81 | 0.02 | -101.23 | -103.37 | -1.04 | 2.13 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-06-08T12:00:00+00:00 | 2,522.31 | 2,343.42 | 0.56 | -101.05 | -102.94 | -1.03 | 1.89 | Stop loss hit. |
| `AVAXUSDT` | STOPPED（已止损） | 2025-06-10T00:00:00+00:00 | 21.79 | 19.25 | 40.07 | -101.70 | -102.82 | -1.02 | 1.12 | Stop loss hit. |
| `ADAUSDT` | STOPPED（已止损） | 2025-06-10T00:00:00+00:00 | 0.71 | 0.64 | 1,492.10 | -101.98 | -103.36 | -1.02 | 1.38 | Stop loss hit. |
| `ENAUSDT` | STOPPED（已止损） | 2025-06-10T08:00:00+00:00 | 0.34 | 0.30 | 2,737.12 | -102.39 | -103.59 | -1.02 | 1.20 | Stop loss hit. |
| `BNBUSDT` | STOPPED（已止损） | 2025-06-10T12:00:00+00:00 | 660.52 | 636.16 | 4.10 | -99.86 | -103.55 | -1.06 | 3.69 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-06-24T16:00:00+00:00 | 105,613.24 | 96,630.27 | 0.01 | -94.31 | -95.77 | -1.03 | 1.46 | Stop loss hit. |
| `ETHUSDT` | CLOSED（已按TP2平仓） | 2025-06-29T08:00:00+00:00 | 2,449.05 | 2,734.86 | 0.92 | 263.22 | 261.31 | 2.77 | 1.91 | TP2 hit; paper trade closed. |
| `DOGEUSDT` | CLOSED（已按TP2平仓） | 2025-06-30T04:00:00+00:00 | 0.17 | 0.20 | 8,658.98 | 256.72 | 255.47 | 2.72 | 1.25 | TP2 hit; paper trade closed. |
| `AAVEUSDT` | CLOSED（已按TP2平仓） | 2025-06-30T08:00:00+00:00 | 269.57 | 322.83 | 4.62 | 246.20 | 245.11 | 2.62 | 1.10 | TP2 hit; paper trade closed. |
| `ARBUSDT` | CLOSED（已按TP2平仓） | 2025-06-30T16:00:00+00:00 | 0.34 | 0.45 | 2,118.73 | 240.68 | 240.00 | 2.53 | 0.67 | TP2 hit; paper trade closed. |
| `BONKUSDT` | CLOSED（已按TP2平仓） | 2025-07-08T20:00:00+00:00 | 0.00 | 0.00 | 22,062,197.82 | 265.68 | 265.19 | 2.67 | 0.50 | TP2 hit; paper trade closed. |
| `FETUSDT` | STOPPED（已止损） | 2025-07-11T16:00:00+00:00 | 0.73 | 0.65 | 1,369.39 | -104.36 | -105.64 | -1.02 | 1.29 | Stop loss hit. |
| `DOGEUSDT` | CLOSED（已按TP2平仓） | 2025-07-13T16:00:00+00:00 | 0.20 | 0.26 | 4,696.34 | 273.84 | 272.98 | 2.58 | 0.86 | TP2 hit; paper trade closed. |
| `COMPUSDT` | STOPPED（已止损） | 2025-07-15T00:00:00+00:00 | 48.95 | 44.40 | 23.98 | -109.18 | -110.71 | -1.02 | 1.53 | Stop loss hit. |
| `APTUSDT` | STOPPED（已止损） | 2025-07-16T12:00:00+00:00 | 5.10 | 4.71 | 278.95 | -109.57 | -111.45 | -1.03 | 1.88 | Stop loss hit. |
| `AAVEUSDT` | STOPPED（已止损） | 2025-07-18T04:00:00+00:00 | 329.07 | 301.27 | 4.12 | -114.55 | -116.34 | -1.03 | 1.78 | Stop loss hit. |
| `FLOKIUSDT` | STOPPED（已止损） | 2025-07-22T04:00:00+00:00 | 0.00 | 0.00 | 10,164,546.42 | -112.54 | -114.45 | -1.03 | 1.91 | Stop loss hit. |
| `ENSUSDT` | STOPPED（已止损） | 2025-07-23T04:00:00+00:00 | 28.80 | 25.73 | 35.17 | -107.94 | -109.25 | -1.02 | 1.31 | Stop loss hit. |
| `BNBUSDT` | STOPPED（已止损） | 2025-07-23T16:00:00+00:00 | 783.39 | 732.83 | 2.16 | -109.40 | -111.67 | -1.04 | 2.26 | Stop loss hit. |
| `ENAUSDT` | STOPPED（已止损） | 2025-07-31T00:00:00+00:00 | 0.61 | 0.52 | 1,202.38 | -103.22 | -104.15 | -1.02 | 0.92 | Stop loss hit. |
| `CFXUSDT` | STOPPED（已止损） | 2025-07-31T08:00:00+00:00 | 0.21 | 0.18 | 3,342.62 | -104.07 | -104.94 | -1.01 | 0.88 | Stop loss hit. |
| `BCHUSDT` | STOPPED（已止损） | 2025-08-08T00:00:00+00:00 | 576.71 | 532.94 | 2.35 | -102.74 | -104.54 | -1.03 | 1.79 | Stop loss hit. |
| `AVAXUSDT` | CLOSED（已按TP2平仓） | 2025-08-08T00:00:00+00:00 | 23.09 | 28.40 | 51.43 | 273.01 | 271.95 | 2.68 | 1.06 | TP2 hit; paper trade closed. |
| `CRVUSDT` | STOPPED（已止损） | 2025-08-08T04:00:00+00:00 | 0.95 | 0.86 | 1,116.40 | -102.52 | -103.90 | -1.02 | 1.38 | Stop loss hit. |
| `DOTUSDT` | STOPPED（已止损） | 2025-08-12T16:00:00+00:00 | 4.05 | 3.76 | 341.02 | -99.84 | -101.68 | -1.03 | 1.83 | Stop loss hit. |
| `ETHFIUSDT` | STOPPED（已止损） | 2025-08-13T08:00:00+00:00 | 1.23 | 1.13 | 1,003.71 | -101.97 | -103.59 | -1.03 | 1.62 | Stop loss hit. |
| `ENAUSDT` | STOPPED（已止损） | 2025-08-15T08:00:00+00:00 | 0.74 | 0.67 | 1,360.12 | -100.26 | -101.57 | -1.02 | 1.31 | Stop loss hit. |
| `FLOKIUSDT` | STOPPED（已止损） | 2025-08-23T00:00:00+00:00 | 0.00 | 0.00 | 5,577,742.19 | -97.26 | -98.03 | -1.01 | 0.77 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-08-24T12:00:00+00:00 | 4,691.33 | 4,137.00 | 0.17 | -94.42 | -95.45 | -1.02 | 1.02 | Stop loss hit. |
| `AVAXUSDT` | CLOSED（已按TP2平仓） | 2025-09-16T00:00:00+00:00 | 29.85 | 34.86 | 46.90 | 235.15 | 233.94 | 2.43 | 1.21 | TP2 hit; paper trade closed. |
| `BNBUSDT` | CLOSED（已按TP2平仓） | 2025-09-16T08:00:00+00:00 | 930.05 | 1,025.84 | 2.94 | 281.41 | 279.11 | 2.87 | 2.30 | TP2 hit; paper trade closed. |
| `DOGEUSDT` | STOPPED（已止损） | 2025-09-16T16:00:00+00:00 | 0.27 | 0.25 | 7,227.90 | -99.23 | -101.83 | -1.05 | 2.60 | Stop loss hit. |
| `AAVEUSDT` | STOPPED（已止损） | 2025-09-18T04:00:00+00:00 | 309.62 | 284.85 | 4.15 | -102.86 | -104.56 | -1.03 | 1.70 | Stop loss hit. |
| `ETHFIUSDT` | STOPPED（已止损） | 2025-09-19T00:00:00+00:00 | 1.60 | 1.39 | 491.15 | -101.47 | -102.47 | -1.02 | 1.00 | Stop loss hit. |
| `BNBUSDT` | STOPPED（已止损） | 2025-09-21T12:00:00+00:00 | 1,025.08 | 958.33 | 1.47 | -98.25 | -100.26 | -1.04 | 2.01 | Stop loss hit. |
| `CAKEUSDT` | STOPPED（已止损） | 2025-09-21T12:00:00+00:00 | 2.89 | 2.59 | 331.47 | -98.51 | -99.75 | -1.02 | 1.24 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-10-01T12:00:00+00:00 | 4,306.31 | 3,902.60 | 0.24 | -96.62 | -97.96 | -1.02 | 1.35 | Stop loss hit. |
| `ADAUSDT` | STOPPED（已止损） | 2025-10-02T00:00:00+00:00 | 0.85 | 0.77 | 1,224.34 | -97.36 | -98.71 | -1.02 | 1.35 | Stop loss hit. |
| `AAVEUSDT` | STOPPED（已止损） | 2025-10-02T00:00:00+00:00 | 287.76 | 261.85 | 3.74 | -96.99 | -98.40 | -1.02 | 1.41 | Stop loss hit. |
| `DOGEUSDT` | STOPPED（已止损） | 2025-10-02T00:00:00+00:00 | 0.25 | 0.22 | 3,985.74 | -96.83 | -98.11 | -1.02 | 1.28 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-10-26T16:00:00+00:00 | 4,060.46 | 3,757.68 | 0.31 | -92.60 | -94.25 | -1.03 | 1.65 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-11-27T16:00:00+00:00 | 2,996.52 | 2,797.38 | 0.45 | -90.04 | -91.85 | -1.03 | 1.81 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-11-30T04:00:00+00:00 | 91,152.21 | 88,714.33 | 0.04 | -93.27 | -98.06 | -1.09 | 4.79 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-12-03T08:00:00+00:00 | 93,325.63 | 82,482.85 | 0.01 | -87.24 | -88.20 | -1.02 | 0.96 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-12-07T20:00:00+00:00 | 3,107.08 | 2,861.04 | 0.36 | -87.53 | -88.99 | -1.03 | 1.46 | Stop loss hit. |
| `ETHUSDT` | CLOSED（已按TP2平仓） | 2025-12-31T00:00:00+00:00 | 2,984.10 | 3,318.38 | 0.73 | 244.67 | 242.83 | 2.82 | 1.85 | TP2 hit; paper trade closed. |
| `ETHUSDT` | STOPPED（已止损） | 2026-01-17T16:00:00+00:00 | 3,319.13 | 3,201.01 | 0.78 | -91.67 | -95.18 | -1.07 | 3.51 | Stop loss hit. |
| `BNBUSDT` | STOPPED（已止损） | 2026-01-18T00:00:00+00:00 | 944.78 | 908.92 | 2.55 | -91.38 | -94.66 | -1.06 | 3.28 | Stop loss hit. |
| `DASHUSDT` | STOPPED（已止损） | 2026-01-18T12:00:00+00:00 | 80.43 | 70.28 | 8.77 | -89.08 | -89.98 | -1.02 | 0.90 | Stop loss hit. |
| `BNBUSDT` | CLOSED（已按TP2平仓） | 2026-04-16T00:00:00+00:00 | 618.86 | 718.19 | 2.42 | 240.44 | 239.15 | 2.73 | 1.29 | TP2 hit; paper trade closed. |
| `DOGEUSDT` | CLOSED（已按TP2平仓） | 2026-04-16T00:00:00+00:00 | 0.09 | 0.11 | 15,813.41 | 222.12 | 220.83 | 2.53 | 1.29 | TP2 hit; paper trade closed. |
| `AVAXUSDT` | STOPPED（已止损） | 2026-04-17T00:00:00+00:00 | 9.63 | 9.06 | 158.36 | -89.15 | -91.19 | -1.04 | 2.04 | Stop loss hit. |
| `DOGEUSDT` | STOPPED（已止损） | 2026-05-02T00:00:00+00:00 | 0.11 | 0.10 | 8,811.35 | -89.02 | -90.27 | -1.02 | 1.24 | Stop loss hit. |

## 回测结束仍开放

| Symbol（交易对） | Status（状态） | Entry（入场价） | Qty（数量） | Unrealized Handling（未实现盈亏处理） | Notes（备注） |
|---|---|---:|---:|---|---|
| `ETHUSDT` | TP1_HIT（第一止盈已触达） | 1,990.26 | 0.46 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |
| `BTCUSDT` | TP1_HIT（第一止盈已触达） | 69,208.02 | 0.01 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |
| `ALICEUSDT` | ENTERED（已入场） | 0.15 | 2,328.14 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |

## 未入场/过期计划

| Symbol（交易对） | Status（状态） | Created（创建时间） | Entry Zone（入场区间） | Score（评分） | Notes（备注） |
|---|---|---|---:|---:|---|
| `FETUSDT` | INVALIDATED（未入场前失效） | 2025-06-10T04:00:00+00:00 | 0.79 - 0.79 | 53.90 | Plan invalidated before entry: current price is below stop loss. |
| `DOGEUSDT` | INVALIDATED（未入场前失效） | 2025-06-11T00:00:00+00:00 | 0.20 - 0.20 | 54.27 | Plan invalidated before entry: current price is below stop loss. |
| `CRVUSDT` | INVALIDATED（未入场前失效） | 2025-06-11T04:00:00+00:00 | 0.69 - 0.71 | 67.61 | Plan invalidated before entry: current price is below stop loss. |
| `BCHUSDT` | INVALIDATED（未入场前失效） | 2025-06-12T20:00:00+00:00 | 429.90 - 433.00 | 60.69 | Plan invalidated before entry: current price is below stop loss. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-06-30T00:00:00+00:00 | 648.87 - 649.59 | 56.89 | Backtest WATCHING plan expired before entry. |
| `BCHUSDT` | EXPIRED（观察计划过期） | 2025-07-01T00:00:00+00:00 | 499.10 - 504.88 | 64.61 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-07-03T00:00:00+00:00 | 18.43 - 18.57 | 61.42 | Backtest WATCHING plan expired before entry. |
| `ENAUSDT` | EXPIRED（观察计划过期） | 2025-07-03T04:00:00+00:00 | 0.28 - 0.28 | 62.81 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-03T04:00:00+00:00 | 656.07 - 657.93 | 62.47 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-07-03T08:00:00+00:00 | 0.59 - 0.60 | 66.10 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-07-04T16:00:00+00:00 | 0.00 - 0.00 | 71.04 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-06T12:00:00+00:00 | 657.05 - 658.15 | 45.07 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-07-07T00:00:00+00:00 | 0.58 - 0.58 | 49.98 | Backtest WATCHING plan expired before entry. |
| `FLOKIUSDT` | EXPIRED（观察计划过期） | 2025-07-08T12:00:00+00:00 | 0.00 - 0.00 | 60.98 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-09T20:00:00+00:00 | 662.59 - 663.99 | 61.84 | Backtest WATCHING plan expired before entry. |
| `BCHUSDT` | EXPIRED（观察计划过期） | 2025-07-11T00:00:00+00:00 | 508.00 - 512.65 | 65.30 | Backtest WATCHING plan expired before entry. |
| `APTUSDT` | EXPIRED（观察计划过期） | 2025-07-12T00:00:00+00:00 | 4.76 - 4.84 | 57.90 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-07-13T00:00:00+00:00 | 20.31 - 20.70 | 57.91 | Backtest WATCHING plan expired before entry. |
| `ARKUSDT` | EXPIRED（观察计划过期） | 2025-07-13T04:00:00+00:00 | 0.45 - 0.46 | 62.46 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-07-13T08:00:00+00:00 | 2,901.59 - 2,932.21 | 68.11 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-13T16:00:00+00:00 | 686.16 - 689.46 | 57.50 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-07-14T12:00:00+00:00 | 0.72 - 0.74 | 74.57 | Backtest WATCHING plan expired before entry. |
| `AAVEUSDT` | EXPIRED（观察计划过期） | 2025-07-14T16:00:00+00:00 | 310.43 - 316.01 | 71.35 | Backtest WATCHING plan expired before entry. |
| `ETHFIUSDT` | EXPIRED（观察计划过期） | 2025-07-15T16:00:00+00:00 | 1.14 - 1.16 | 70.39 | Backtest WATCHING plan expired before entry. |
| `ENAUSDT` | EXPIRED（观察计划过期） | 2025-07-15T16:00:00+00:00 | 0.34 - 0.35 | 70.16 | Backtest WATCHING plan expired before entry. |
| `DOTUSDT` | EXPIRED（观察计划过期） | 2025-07-15T20:00:00+00:00 | 3.94 - 3.96 | 55.86 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-07-16T04:00:00+00:00 | 21.28 - 21.74 | 71.69 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-07-16T12:00:00+00:00 | 3,041.39 - 3,079.50 | 79.73 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-16T20:00:00+00:00 | 692.57 - 697.70 | 66.79 | Backtest WATCHING plan expired before entry. |
| `ARBUSDT` | EXPIRED（观察计划过期） | 2025-07-17T04:00:00+00:00 | 0.42 - 0.43 | 71.97 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-07-18T16:00:00+00:00 | 0.79 - 0.82 | 76.32 | Backtest WATCHING plan expired before entry. |
| `ENAUSDT` | EXPIRED（观察计划过期） | 2025-07-19T00:00:00+00:00 | 0.38 - 0.39 | 74.86 | Backtest WATCHING plan expired before entry. |
| `FILUSDT` | EXPIRED（观察计划过期） | 2025-07-19T00:00:00+00:00 | 2.71 - 2.76 | 68.72 | Backtest WATCHING plan expired before entry. |
| `CAKEUSDT` | EXPIRED（观察计划过期） | 2025-07-19T00:00:00+00:00 | 2.58 - 2.64 | 68.50 | Backtest WATCHING plan expired before entry. |
| `GALAUSDT` | EXPIRED（观察计划过期） | 2025-07-19T00:00:00+00:00 | 0.02 - 0.02 | 68.16 | Backtest WATCHING plan expired before entry. |
| `CRVUSDT` | EXPIRED（观察计划过期） | 2025-07-19T16:00:00+00:00 | 0.93 - 0.96 | 71.91 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-07-19T20:00:00+00:00 | 3,472.71 - 3,527.19 | 71.70 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-20T00:00:00+00:00 | 726.59 - 735.19 | 59.00 | Backtest WATCHING plan expired before entry. |
| `ARBUSDT` | EXPIRED（观察计划过期） | 2025-07-20T08:00:00+00:00 | 0.46 - 0.47 | 64.42 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-07-20T20:00:00+00:00 | 0.00 - 0.00 | 70.99 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | INVALIDATED（未入场前失效） | 2025-07-21T20:00:00+00:00 | 0.86 - 0.87 | 76.27 | Plan invalidated before entry: current price is below stop loss. |
| `AVAXUSDT` | INVALIDATED（未入场前失效） | 2025-07-22T04:00:00+00:00 | 24.98 - 25.44 | 74.03 | Plan invalidated before entry: current price is below stop loss. |
| `ANIMEUSDT` | INVALIDATED（未入场前失效） | 2025-07-22T04:00:00+00:00 | 0.02 - 0.02 | 57.18 | Plan invalidated before entry: current price is below stop loss. |
| `CRVUSDT` | EXPIRED（观察计划过期） | 2025-07-23T00:00:00+00:00 | 0.96 - 0.99 | 63.77 | Backtest WATCHING plan expired before entry. |
| `DOTUSDT` | INVALIDATED（未入场前失效） | 2025-07-23T00:00:00+00:00 | 4.44 - 4.53 | 63.59 | Plan invalidated before entry: current price is below stop loss. |
| `FILUSDT` | INVALIDATED（未入场前失效） | 2025-07-23T00:00:00+00:00 | 2.86 - 2.92 | 62.95 | Plan invalidated before entry: current price is below stop loss. |
| `ETCUSDT` | INVALIDATED（未入场前失效） | 2025-07-23T00:00:00+00:00 | 23.89 - 24.31 | 59.54 | Plan invalidated before entry: current price is below stop loss. |
| `BCHUSDT` | INVALIDATED（未入场前失效） | 2025-07-23T12:00:00+00:00 | 524.76 - 529.88 | 48.45 | Plan invalidated before entry: current price is below stop loss. |
| `CFXUSDT` | EXPIRED（观察计划过期） | 2025-07-24T08:00:00+00:00 | 0.18 - 0.18 | 57.69 | Backtest WATCHING plan expired before entry. |
| `ENAUSDT` | EXPIRED（观察计划过期） | 2025-07-24T12:00:00+00:00 | 0.48 - 0.48 | 62.68 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-07-24T16:00:00+00:00 | 3,675.13 - 3,734.05 | 66.35 | Backtest WATCHING plan expired before entry. |
| `BCHUSDT` | EXPIRED（观察计划过期） | 2025-07-24T16:00:00+00:00 | 520.12 - 523.27 | 60.23 | Backtest WATCHING plan expired before entry. |
| `ETCUSDT` | EXPIRED（观察计划过期） | 2025-07-24T20:00:00+00:00 | 22.65 - 22.78 | 40.21 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-07-26T00:00:00+00:00 | 0.00 - 0.00 | 66.50 | Backtest WATCHING plan expired before entry. |
| `CAKEUSDT` | EXPIRED（观察计划过期） | 2025-07-26T00:00:00+00:00 | 2.69 - 2.75 | 64.55 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-07-26T00:00:00+00:00 | 24.02 - 24.08 | 46.51 | Backtest WATCHING plan expired before entry. |
| `ARBUSDT` | EXPIRED（观察计划过期） | 2025-07-26T00:00:00+00:00 | 0.44 - 0.44 | 45.35 | Backtest WATCHING plan expired before entry. |
| `CRVUSDT` | EXPIRED（观察计划过期） | 2025-07-26T04:00:00+00:00 | 1.00 - 1.03 | 68.04 | Backtest WATCHING plan expired before entry. |
| `CFXUSDT` | EXPIRED（观察计划过期） | 2025-07-27T12:00:00+00:00 | 0.18 - 0.19 | 68.36 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-07-27T20:00:00+00:00 | 3,750.11 - 3,785.70 | 64.48 | Backtest WATCHING plan expired before entry. |
| `CRVUSDT` | INVALIDATED（未入场前失效） | 2025-07-29T08:00:00+00:00 | 1.02 - 1.03 | 50.75 | Plan invalidated before entry: current price is below stop loss. |
| `CKBUSDT` | INVALIDATED（未入场前失效） | 2025-07-30T00:00:00+00:00 | 0.01 - 0.01 | 57.54 | Plan invalidated before entry: current price is below stop loss. |
| `BIOUSDT` | INVALIDATED（未入场前失效） | 2025-07-30T08:00:00+00:00 | 0.07 - 0.07 | 60.16 | Plan invalidated before entry: current price is below stop loss. |
| `CRVUSDT` | INVALIDATED（未入场前失效） | 2025-07-30T16:00:00+00:00 | 1.01 - 1.02 | 60.26 | Plan invalidated before entry: current price is below stop loss. |
| `BCHUSDT` | INVALIDATED（未入场前失效） | 2025-07-30T16:00:00+00:00 | 570.12 - 571.01 | 50.29 | Plan invalidated before entry: current price is below stop loss. |
| `ETHUSDT` | INVALIDATED（未入场前失效） | 2025-07-31T00:00:00+00:00 | 3,801.12 - 3,821.43 | 61.37 | Plan invalidated before entry: current price is below stop loss. |
| `ENAUSDT` | EXPIRED（观察计划过期） | 2025-08-08T08:00:00+00:00 | 0.61 - 0.63 | 69.59 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-08-08T08:00:00+00:00 | 773.64 - 778.88 | 60.60 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-08-08T16:00:00+00:00 | 0.76 - 0.77 | 65.29 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-08-10T04:00:00+00:00 | 0.00 - 0.00 | 63.87 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-08-10T08:00:00+00:00 | 4,043.50 - 4,095.99 | 74.86 | Backtest WATCHING plan expired before entry. |
| `AAVEUSDT` | EXPIRED（观察计划过期） | 2025-08-10T08:00:00+00:00 | 291.23 - 295.48 | 73.60 | Backtest WATCHING plan expired before entry. |
| `ETCUSDT` | EXPIRED（观察计划过期） | 2025-08-10T16:00:00+00:00 | 22.51 - 22.94 | 69.36 | Backtest WATCHING plan expired before entry. |
| `ARBUSDT` | EXPIRED（观察计划过期） | 2025-08-11T08:00:00+00:00 | 0.45 - 0.46 | 68.68 | Backtest WATCHING plan expired before entry. |
| `DOGEUSDT` | EXPIRED（观察计划过期） | 2025-08-11T08:00:00+00:00 | 0.23 - 0.23 | 67.47 | Backtest WATCHING plan expired before entry. |
| `ENSUSDT` | EXPIRED（观察计划过期） | 2025-08-11T08:00:00+00:00 | 28.93 - 29.29 | 62.29 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-08-11T16:00:00+00:00 | 801.89 - 809.22 | 62.06 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-08-12T16:00:00+00:00 | 0.79 - 0.81 | 65.38 | Backtest WATCHING plan expired before entry. |
| `ENAUSDT` | INVALIDATED（未入场前失效） | 2025-08-13T12:00:00+00:00 | 0.78 - 0.80 | 72.65 | Plan invalidated before entry: current price is below stop loss. |
| `BONKUSDT` | INVALIDATED（未入场前失效） | 2025-08-13T20:00:00+00:00 | 0.00 - 0.00 | 62.03 | Plan invalidated before entry: current price is below stop loss. |
| `FLOKIUSDT` | INVALIDATED（未入场前失效） | 2025-08-14T00:00:00+00:00 | 0.00 - 0.00 | 67.88 | Plan invalidated before entry: current price is below stop loss. |
| `APTUSDT` | EXPIRED（观察计划过期） | 2025-08-14T08:00:00+00:00 | 4.85 - 4.94 | 69.05 | Backtest WATCHING plan expired before entry. |
| `BERAUSDT` | EXPIRED（观察计划过期） | 2025-08-15T08:00:00+00:00 | 2.12 - 2.15 | 56.07 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-08-15T20:00:00+00:00 | 0.91 - 0.93 | 73.08 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | INVALIDATED（未入场前失效） | 2025-08-17T04:00:00+00:00 | 4,376.86 - 4,430.92 | 37.85 | Plan invalidated before entry: current price is below stop loss. |
| `CRVUSDT` | INVALIDATED（未入场前失效） | 2025-08-23T00:00:00+00:00 | 0.91 - 0.92 | 61.26 | Plan invalidated before entry: current price is below stop loss. |
| `FILUSDT` | INVALIDATED（未入场前失效） | 2025-08-23T00:00:00+00:00 | 2.51 - 2.54 | 59.24 | Plan invalidated before entry: current price is below stop loss. |
| `APTUSDT` | INVALIDATED（未入场前失效） | 2025-08-23T00:00:00+00:00 | 4.63 - 4.69 | 53.21 | Plan invalidated before entry: current price is below stop loss. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-08-23T04:00:00+00:00 | 861.81 - 871.06 | 71.00 | Backtest WATCHING plan expired before entry. |
| `DOTUSDT` | EXPIRED（观察计划过期） | 2025-08-23T04:00:00+00:00 | 3.95 - 4.01 | 58.40 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-08-23T12:00:00+00:00 | 0.89 - 0.91 | 71.43 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-09-16T20:00:00+00:00 | 0.00 - 0.00 | 49.30 | Backtest WATCHING plan expired before entry. |
| `DOTUSDT` | EXPIRED（观察计划过期） | 2025-09-16T20:00:00+00:00 | 4.26 - 4.29 | 49.19 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-09-17T08:00:00+00:00 | 0.88 - 0.88 | 50.38 | Backtest WATCHING plan expired before entry. |
| `BCHUSDT` | EXPIRED（观察计划过期） | 2025-09-18T00:00:00+00:00 | 599.74 - 604.08 | 65.77 | Backtest WATCHING plan expired before entry. |
| `ARBUSDT` | EXPIRED（观察计划过期） | 2025-09-18T00:00:00+00:00 | 0.51 - 0.52 | 46.78 | Backtest WATCHING plan expired before entry. |
| `BIOUSDT` | INVALIDATED（未入场前失效） | 2025-09-21T00:00:00+00:00 | 0.18 - 0.18 | 73.51 | Plan invalidated before entry: current price is below stop loss. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-10-02T00:00:00+00:00 | 1,011.09 - 1,019.11 | 63.44 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-10-02T20:00:00+00:00 | 30.34 - 30.77 | 55.07 | Backtest WATCHING plan expired before entry. |
| `ARBUSDT` | EXPIRED（观察计划过期） | 2025-10-03T04:00:00+00:00 | 0.44 - 0.44 | 55.25 | Backtest WATCHING plan expired before entry. |
| `ENAUSDT` | EXPIRED（观察计划过期） | 2025-10-03T04:00:00+00:00 | 0.60 - 0.61 | 55.01 | Backtest WATCHING plan expired before entry. |
| `DOTUSDT` | EXPIRED（观察计划过期） | 2025-10-03T08:00:00+00:00 | 4.13 - 4.18 | 62.79 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-10-03T16:00:00+00:00 | 0.00 - 0.00 | 54.75 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-10-05T12:00:00+00:00 | 1,131.18 - 1,149.27 | 72.89 | Backtest WATCHING plan expired before entry. |
| `EIGENUSDT` | EXPIRED（观察计划过期） | 2025-10-05T12:00:00+00:00 | 1.85 - 1.90 | 69.67 | Backtest WATCHING plan expired before entry. |
| `APTUSDT` | EXPIRED（观察计划过期） | 2025-10-05T20:00:00+00:00 | 5.26 - 5.38 | 76.12 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | INVALIDATED（未入场前失效） | 2025-10-06T12:00:00+00:00 | 30.44 - 30.59 | 36.49 | Plan invalidated before entry: current price is below stop loss. |
| `FLOKIUSDT` | EXPIRED（观察计划过期） | 2025-10-06T20:00:00+00:00 | 0.00 - 0.00 | 58.67 | Backtest WATCHING plan expired before entry. |
| `DOTUSDT` | INVALIDATED（未入场前失效） | 2025-10-07T00:00:00+00:00 | 4.25 - 4.31 | 70.97 | Plan invalidated before entry: current price is below stop loss. |
| `BONKUSDT` | INVALIDATED（未入场前失效） | 2025-10-07T00:00:00+00:00 | 0.00 - 0.00 | 62.93 | Plan invalidated before entry: current price is below stop loss. |
| `ARBUSDT` | INVALIDATED（未入场前失效） | 2025-10-07T00:00:00+00:00 | 0.45 - 0.46 | 61.41 | Plan invalidated before entry: current price is below stop loss. |
| `API3USDT` | INVALIDATED（未入场前失效） | 2025-10-08T00:00:00+00:00 | 0.85 - 0.88 | 64.48 | Plan invalidated before entry: current price is below stop loss. |
| `FORMUSDT` | INVALIDATED（未入场前失效） | 2025-10-08T08:00:00+00:00 | 1.41 - 1.46 | 75.54 | Plan invalidated before entry: current price is below stop loss. |
| `BNBUSDT` | INVALIDATED（未入场前失效） | 2025-10-08T16:00:00+00:00 | 1,249.87 - 1,275.74 | 83.10 | Plan invalidated before entry: current price is below stop loss. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2026-01-14T12:00:00+00:00 | 3,202.86 - 3,234.96 | 72.24 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2026-04-17T00:00:00+00:00 | 0.25 - 0.25 | 59.10 | Backtest WATCHING plan expired before entry. |
| `AVNTUSDT` | EXPIRED（观察计划过期） | 2026-04-18T12:00:00+00:00 | 0.14 - 0.14 | 53.00 | Backtest WATCHING plan expired before entry. |
| `BOMEUSDT` | EXPIRED（观察计划过期） | 2026-04-20T00:00:00+00:00 | 0.00 - 0.00 | 78.60 | Backtest WATCHING plan expired before entry. |
| `ENJUSDT` | EXPIRED（观察计划过期） | 2026-04-20T00:00:00+00:00 | 0.06 - 0.06 | 48.52 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2026-04-21T12:00:00+00:00 | 9.37 - 9.47 | 48.53 | Backtest WATCHING plan expired before entry. |
| `ENJUSDT` | EXPIRED（观察计划过期） | 2026-04-25T00:00:00+00:00 | 0.06 - 0.06 | 50.06 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2026-05-05T00:00:00+00:00 | 0.25 - 0.25 | 48.99 | Backtest WATCHING plan expired before entry. |
| `BCHUSDT` | EXPIRED（观察计划过期） | 2026-05-07T00:00:00+00:00 | 458.71 - 463.32 | 56.00 | Backtest WATCHING plan expired before entry. |
| `ENAUSDT` | EXPIRED（观察计划过期） | 2026-05-07T04:00:00+00:00 | 0.11 - 0.11 | 72.32 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2026-05-07T08:00:00+00:00 | 9.47 - 9.56 | 61.12 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2026-05-11T00:00:00+00:00 | 0.27 - 0.28 | 71.95 | Backtest WATCHING plan expired before entry. |
| `APTUSDT` | EXPIRED（观察计划过期） | 2026-05-11T04:00:00+00:00 | 1.11 - 1.12 | 70.27 | Backtest WATCHING plan expired before entry. |

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
| INFO | n/a | n/a | Additional issues omitted: 1771. |

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
    "created_at_utc": "2026-06-09T06:50:42+00:00",
    "refresh_frequency": "daily",
    "max_symbols": 40,
    "master_count": 150,
    "source_limit": 150,
    "source_limit_applied": true,
    "universe_refresh_count": 366,
    "selected_count_min": 3,
    "selected_count_avg": 10.366120218579235,
    "selected_count_max": 35,
    "top_selected_symbols": [
      {
        "symbol": "BNBUSDT",
        "days_selected": 366
      },
      {
        "symbol": "BTCUSDT",
        "days_selected": 366
      },
      {
        "symbol": "ETHUSDT",
        "days_selected": 366
      },
      {
        "symbol": "DOGEUSDT",
        "days_selected": 361
      },
      {
        "symbol": "ADAUSDT",
        "days_selected": 288
      },
      {
        "symbol": "AVAXUSDT",
        "days_selected": 226
      },
      {
        "symbol": "ENAUSDT",
        "days_selected": 199
      },
      {
        "symbol": "AAVEUSDT",
        "days_selected": 132
      },
      {
        "symbol": "BCHUSDT",
        "days_selected": 122
      },
      {
        "symbol": "ASTERUSDT",
        "days_selected": 111
      },
      {
        "symbol": "ARBUSDT",
        "days_selected": 103
      },
      {
        "symbol": "BONKUSDT",
        "days_selected": 97
      },
      {
        "symbol": "DOTUSDT",
        "days_selected": 68
      },
      {
        "symbol": "APTUSDT",
        "days_selected": 61
      },
      {
        "symbol": "FETUSDT",
        "days_selected": 58
      },
      {
        "symbol": "CRVUSDT",
        "days_selected": 52
      },
      {
        "symbol": "DASHUSDT",
        "days_selected": 51
      },
      {
        "symbol": "ETHFIUSDT",
        "days_selected": 50
      },
      {
        "symbol": "FILUSDT",
        "days_selected": 47
      },
      {
        "symbol": "AVNTUSDT",
        "days_selected": 36
      }
    ],
    "filter_counts": {
      "missing_1h": 3908,
      "insufficient_24h": 24,
      "reconstruct_error": 0,
      "low_quote_volume": 47156,
      "low_trades": 16,
      "stable_like": 2
    },
    "selection_by_day": [
      {
        "date_utc": "2025-06-01",
        "decision_time_utc": "2025-06-01T04:00:00+00:00",
        "selected_symbols": [
          "ETHFIUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 117,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-02",
        "decision_time_utc": "2025-06-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 120,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-03",
        "decision_time_utc": "2025-06-03T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "AUSDT",
          "AVAXUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 117,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-04",
        "decision_time_utc": "2025-06-04T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "FETUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "AAVEUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AUSDT",
          "ETHFIUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 115,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-05",
        "decision_time_utc": "2025-06-05T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "COMPUSDT",
          "ENAUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ETHFIUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 116,
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
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ETHFIUSDT",
          "CAKEUSDT",
          "FETUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 114,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-07",
        "decision_time_utc": "2025-06-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHFIUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "COMPUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "ANIMEUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 115,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-08",
        "decision_time_utc": "2025-06-08T00:00:00+00:00",
        "selected_symbols": [
          "ANIMEUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 118,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-09",
        "decision_time_utc": "2025-06-09T00:00:00+00:00",
        "selected_symbols": [
          "ANIMEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 118,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-10",
        "decision_time_utc": "2025-06-10T00:00:00+00:00",
        "selected_symbols": [
          "ANIMEUSDT",
          "AAVEUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "FETUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 116,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-11",
        "decision_time_utc": "2025-06-11T00:00:00+00:00",
        "selected_symbols": [
          "AXLUSDT",
          "COMPUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "ETHFIUSDT",
          "EIGENUSDT",
          "CRVUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "FETUSDT",
          "BNBUSDT",
          "ANIMEUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 109,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-12",
        "decision_time_utc": "2025-06-12T00:00:00+00:00",
        "selected_symbols": [
          "AUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ANIMEUSDT",
          "FETUSDT",
          "BCHUSDT",
          "ETHFIUSDT",
          "ARBUSDT",
          "CAKEUSDT",
          "EIGENUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 110,
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
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ETHFIUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 117,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-14",
        "decision_time_utc": "2025-06-14T00:00:00+00:00",
        "selected_symbols": [
          "BCHUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "FETUSDT",
          "ETHFIUSDT",
          "CRVUSDT",
          "DOTUSDT",
          "BONKUSDT",
          "APTUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 110,
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
          "DOGEUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 120,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-16",
        "decision_time_utc": "2025-06-16T00:00:00+00:00",
        "selected_symbols": [
          "BCHUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 121,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-17",
        "decision_time_utc": "2025-06-17T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "ETHFIUSDT",
          "ALTUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 115,
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
          "ALTUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "EIGENUSDT",
          "FETUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 113,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-19",
        "decision_time_utc": "2025-06-19T00:00:00+00:00",
        "selected_symbols": [
          "ALTUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 117,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-20",
        "decision_time_utc": "2025-06-20T00:00:00+00:00",
        "selected_symbols": [
          "BCHUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "FETUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 116,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-21",
        "decision_time_utc": "2025-06-21T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AAVEUSDT",
          "BCHUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 117,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-22",
        "decision_time_utc": "2025-06-22T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "ENAUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 117,
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
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BCHUSDT",
          "AAVEUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "DOTUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 115,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-24",
        "decision_time_utc": "2025-06-24T00:00:00+00:00",
        "selected_symbols": [
          "BANANAS31USDT",
          "FETUSDT",
          "ETHFIUSDT",
          "AAVEUSDT",
          "ENAUSDT",
          "ARBUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 113,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-25",
        "decision_time_utc": "2025-06-25T00:00:00+00:00",
        "selected_symbols": [
          "APTUSDT",
          "BANANAS31USDT",
          "ETHUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "FORMUSDT",
          "FETUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 113,
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
          "BNBUSDT",
          "DOGEUSDT",
          "APTUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "ENAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 115,
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
          "BCHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "ENAUSDT",
          "BANANAS31USDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 116,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-28",
        "decision_time_utc": "2025-06-28T00:00:00+00:00",
        "selected_symbols": [
          "BANANAS31USDT",
          "BTCUSDT",
          "ETHUSDT",
          "AAVEUSDT",
          "BCHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "APTUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 117,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-29",
        "decision_time_utc": "2025-06-29T00:00:00+00:00",
        "selected_symbols": [
          "BANANAS31USDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 120,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-30",
        "decision_time_utc": "2025-06-30T00:00:00+00:00",
        "selected_symbols": [
          "ARBUSDT",
          "AAVEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 119,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-01",
        "decision_time_utc": "2025-07-01T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ARBUSDT",
          "ADAUSDT",
          "BANANAS31USDT",
          "BCHUSDT",
          "AAVEUSDT",
          "ENAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 115,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-02",
        "decision_time_utc": "2025-07-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 119,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-03",
        "decision_time_utc": "2025-07-03T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 117,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-04",
        "decision_time_utc": "2025-07-04T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 116,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-05",
        "decision_time_utc": "2025-07-05T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "ENAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 117,
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
          "DOGEUSDT",
          "BNBUSDT",
          "BMTUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 120,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-07",
        "decision_time_utc": "2025-07-07T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "FLOKIUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 118,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-08",
        "decision_time_utc": "2025-07-08T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "FLOKIUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 118,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-09",
        "decision_time_utc": "2025-07-09T00:00:00+00:00",
        "selected_symbols": [
          "BANANAS31USDT",
          "FLOKIUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 117,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-10",
        "decision_time_utc": "2025-07-10T00:00:00+00:00",
        "selected_symbols": [
          "BANANAS31USDT",
          "ETHFIUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "FLOKIUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 113,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-11",
        "decision_time_utc": "2025-07-11T00:00:00+00:00",
        "selected_symbols": [
          "BANANAS31USDT",
          "BONKUSDT",
          "ARBUSDT",
          "FLOKIUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "ETHFIUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "FETUSDT",
          "APTUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 110,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-12",
        "decision_time_utc": "2025-07-12T00:00:00+00:00",
        "selected_symbols": [
          "1INCHUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "CRVUSDT",
          "ETHUSDT",
          "ARBUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "DOTUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "FETUSDT",
          "FLOKIUSDT",
          "ETHFIUSDT",
          "ALTUSDT",
          "BANANAS31USDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 106,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-13",
        "decision_time_utc": "2025-07-13T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "ARKUSDT",
          "BANANAS31USDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 115,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-14",
        "decision_time_utc": "2025-07-14T00:00:00+00:00",
        "selected_symbols": [
          "ALGOUSDT",
          "AUCTIONUSDT",
          "ENAUSDT",
          "FETUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "1INCHUSDT",
          "BANANAS31USDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 112,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-15",
        "decision_time_utc": "2025-07-15T00:00:00+00:00",
        "selected_symbols": [
          "CRVUSDT",
          "ALGOUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "COMPUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "DOGEUSDT",
          "BANANAS31USDT",
          "ADAUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "FETUSDT",
          "DOTUSDT",
          "ETHFIUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 108,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-16",
        "decision_time_utc": "2025-07-16T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "ETHFIUSDT",
          "ARBUSDT",
          "ETHUSDT",
          "CRVUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "FETUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "APTUSDT",
          "BNBUSDT",
          "ALGOUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 111,
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
          "BOMEUSDT",
          "ETHUSDT",
          "COWUSDT",
          "ENSUSDT",
          "DOGEUSDT",
          "ETHFIUSDT",
          "BERAUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "FETUSDT",
          "APTUSDT",
          "DOTUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 106,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-18",
        "decision_time_utc": "2025-07-18T00:00:00+00:00",
        "selected_symbols": [
          "ALGOUSDT",
          "CRVUSDT",
          "ADAUSDT",
          "ETHUSDT",
          "BOMEUSDT",
          "AVAXUSDT",
          "AIXBTUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "EIGENUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "ARBUSDT",
          "DOTUSDT",
          "BONKUSDT",
          "APTUSDT",
          "FLOKIUSDT",
          "ETHFIUSDT",
          "AAVEUSDT",
          "FETUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 106,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-19",
        "decision_time_utc": "2025-07-19T00:00:00+00:00",
        "selected_symbols": [
          "EPICUSDT",
          "ETCUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "FLOKIUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "FILUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "CAKEUSDT",
          "ERAUSDT",
          "APTUSDT",
          "CRVUSDT",
          "AVAXUSDT",
          "DOTUSDT",
          "ETHFIUSDT",
          "FETUSDT",
          "ALGOUSDT",
          "GALAUSDT"
        ],
        "candidate_count": 24,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 103,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-20",
        "decision_time_utc": "2025-07-20T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "ETCUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "FLOKIUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "BNBUSDT",
          "ERAUSDT",
          "CRVUSDT",
          "CUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "EPICUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 111,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-21",
        "decision_time_utc": "2025-07-21T00:00:00+00:00",
        "selected_symbols": [
          "CFXUSDT",
          "EPICUSDT",
          "DIAUSDT",
          "CKBUSDT",
          "ACHUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "CUSDT",
          "ETHUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ARBUSDT",
          "BTCUSDT",
          "ETHFIUSDT",
          "FILUSDT",
          "ERAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "FETUSDT",
          "ETCUSDT",
          "DOTUSDT",
          "BONKUSDT",
          "FLOKIUSDT",
          "CRVUSDT",
          "APTUSDT"
        ],
        "candidate_count": 26,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 102,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-22",
        "decision_time_utc": "2025-07-22T00:00:00+00:00",
        "selected_symbols": [
          "DIAUSDT",
          "ANIMEUSDT",
          "FLOKIUSDT",
          "ENAUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "FETUSDT",
          "ETHUSDT",
          "CUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "CAKEUSDT",
          "ETHFIUSDT",
          "CFXUSDT",
          "ERAUSDT",
          "ARBUSDT",
          "BCHUSDT",
          "DOTUSDT",
          "AAVEUSDT",
          "CRVUSDT",
          "ETCUSDT",
          "EPICUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 103,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-23",
        "decision_time_utc": "2025-07-23T00:00:00+00:00",
        "selected_symbols": [
          "CUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "CRVUSDT",
          "DIAUSDT",
          "ENSUSDT",
          "ADAUSDT",
          "FLOKIUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "APTUSDT",
          "DOTUSDT",
          "ERAUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "ETCUSDT",
          "BCHUSDT",
          "FILUSDT",
          "ETHFIUSDT",
          "FETUSDT",
          "CFXUSDT"
        ],
        "candidate_count": 24,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 104,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-24",
        "decision_time_utc": "2025-07-24T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "CUSDT",
          "ERAUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "FLOKIUSDT",
          "APTUSDT",
          "CRVUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "CAKEUSDT",
          "CFXUSDT",
          "DOTUSDT",
          "FETUSDT",
          "ENSUSDT",
          "ETHFIUSDT",
          "BCHUSDT",
          "ETCUSDT",
          "FILUSDT",
          "BERAUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 103,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-25",
        "decision_time_utc": "2025-07-25T00:00:00+00:00",
        "selected_symbols": [
          "ERAUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "CFXUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "CRVUSDT",
          "ENSUSDT",
          "BCHUSDT",
          "FLOKIUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "DOTUSDT",
          "CUSDT",
          "ARBUSDT",
          "FETUSDT",
          "CAKEUSDT",
          "ETHFIUSDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 106,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-26",
        "decision_time_utc": "2025-07-26T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "CRVUSDT",
          "BCHUSDT",
          "BONKUSDT",
          "CFXUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "FLOKIUSDT",
          "DOGEUSDT",
          "CAKEUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "APTUSDT",
          "ADAUSDT",
          "ERAUSDT",
          "DOTUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 110,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-27",
        "decision_time_utc": "2025-07-27T00:00:00+00:00",
        "selected_symbols": [
          "CKBUSDT",
          "CRVUSDT",
          "ENSUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "ERAUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "CFXUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 115,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-28",
        "decision_time_utc": "2025-07-28T00:00:00+00:00",
        "selected_symbols": [
          "ASRUSDT",
          "ALTUSDT",
          "ATMUSDT",
          "CAKEUSDT",
          "ERAUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "ETHUSDT",
          "BCHUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "CRVUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 112,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-29",
        "decision_time_utc": "2025-07-29T00:00:00+00:00",
        "selected_symbols": [
          "ASRUSDT",
          "ATMUSDT",
          "BANANAS31USDT",
          "CUSDT",
          "1000CATUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "CFXUSDT",
          "ERAUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "CAKEUSDT",
          "BCHUSDT",
          "CRVUSDT",
          "ARBUSDT",
          "FLOKIUSDT",
          "AAVEUSDT",
          "FETUSDT",
          "APTUSDT",
          "DOTUSDT"
        ],
        "candidate_count": 24,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 104,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-30",
        "decision_time_utc": "2025-07-30T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "CKBUSDT",
          "ETHUSDT",
          "CFXUSDT",
          "BTCUSDT",
          "ERAUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "CRVUSDT",
          "ARBUSDT",
          "CAKEUSDT",
          "APTUSDT",
          "BCHUSDT",
          "AAVEUSDT",
          "FLOKIUSDT",
          "DOTUSDT",
          "BANANAS31USDT",
          "CUSDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 106,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-31",
        "decision_time_utc": "2025-07-31T00:00:00+00:00",
        "selected_symbols": [
          "CFXUSDT",
          "ENAUSDT",
          "CRVUSDT",
          "BCHUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ERAUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "FLOKIUSDT",
          "APTUSDT",
          "DOTUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 111,
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
          "ERAUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "CFXUSDT",
          "AVAXUSDT",
          "CRVUSDT",
          "FLOKIUSDT",
          "AAVEUSDT",
          "BCHUSDT",
          "APTUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 112,
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
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "CRVUSDT",
          "CFXUSDT",
          "DOTUSDT",
          "FLOKIUSDT",
          "BCHUSDT",
          "ETHFIUSDT",
          "FILUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 110,
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
          "DOGEUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "APTUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 119,
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
          "ETHUSDT",
          "DOGEUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "ETCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 119,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-05",
        "decision_time_utc": "2025-08-05T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "CRVUSDT",
          "BONKUSDT",
          "CFXUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 117,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-06",
        "decision_time_utc": "2025-08-06T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "CRVUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "APTUSDT",
          "CFXUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 116,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-07",
        "decision_time_utc": "2025-08-07T00:00:00+00:00",
        "selected_symbols": [
          "CFXUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "CRVUSDT",
          "AVAXUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 118,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-08",
        "decision_time_utc": "2025-08-08T00:00:00+00:00",
        "selected_symbols": [
          "ASRUSDT",
          "BIOUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "FLOKIUSDT",
          "AAVEUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "CRVUSDT",
          "BCHUSDT",
          "CFXUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 113,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-09",
        "decision_time_utc": "2025-08-09T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "APTUSDT",
          "ASRUSDT",
          "ARBUSDT",
          "ETCUSDT",
          "BTCUSDT",
          "DOTUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "CRVUSDT",
          "CFXUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 111,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-10",
        "decision_time_utc": "2025-08-10T00:00:00+00:00",
        "selected_symbols": [
          "COWUSDT",
          "ALPINEUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "ARBUSDT",
          "ETHFIUSDT",
          "DOGEUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "ETCUSDT",
          "CRVUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "BIOUSDT",
          "CFXUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 111,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-11",
        "decision_time_utc": "2025-08-11T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "ENAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BONKUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "ENSUSDT",
          "AAVEUSDT",
          "APTUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 115,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-12",
        "decision_time_utc": "2025-08-12T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "BANANAS31USDT",
          "BTCUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "CRVUSDT",
          "ETHFIUSDT",
          "APTUSDT",
          "DOTUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 111,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-13",
        "decision_time_utc": "2025-08-13T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "DOTUSDT",
          "BCHUSDT",
          "CRVUSDT",
          "APTUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "BONKUSDT",
          "ETHFIUSDT",
          "BIOUSDT",
          "CYBERUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 111,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-14",
        "decision_time_utc": "2025-08-14T00:00:00+00:00",
        "selected_symbols": [
          "ARBUSDT",
          "EIGENUSDT",
          "ALPINEUSDT",
          "ETHFIUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "CRVUSDT",
          "DOGEUSDT",
          "APTUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "FLOKIUSDT",
          "DOTUSDT",
          "ENAUSDT",
          "BCHUSDT",
          "CYBERUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 21,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 109,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-15",
        "decision_time_utc": "2025-08-15T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BERAUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "AAVEUSDT",
          "DOTUSDT",
          "CRVUSDT",
          "ETHFIUSDT",
          "APTUSDT",
          "BCHUSDT",
          "CFXUSDT",
          "ENSUSDT",
          "FLOKIUSDT",
          "ETCUSDT",
          "FETUSDT",
          "EIGENUSDT",
          "FILUSDT",
          "ALGOUSDT"
        ],
        "candidate_count": 24,
        "filter_counts": {
          "missing_1h": 21,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 104,
          "low_trades": 1,
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
          "ENAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "AAVEUSDT",
          "DOTUSDT",
          "CRVUSDT",
          "APTUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 21,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 115,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-17",
        "decision_time_utc": "2025-08-17T00:00:00+00:00",
        "selected_symbols": [
          "CTSIUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "ALPINEUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 21,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 119,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-18",
        "decision_time_utc": "2025-08-18T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "CYBERUSDT",
          "ARBUSDT",
          "ADAUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "ASRUSDT",
          "ENAUSDT",
          "CTSIUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 21,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 116,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-19",
        "decision_time_utc": "2025-08-19T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "BIOUSDT",
          "CRVUSDT",
          "AAVEUSDT",
          "DOTUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 21,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 115,
          "low_trades": 1,
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
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "BIOUSDT",
          "CRVUSDT",
          "BONKUSDT",
          "AAVEUSDT",
          "APTUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 21,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 115,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-21",
        "decision_time_utc": "2025-08-21T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "CFXUSDT",
          "ETHUSDT",
          "ARBUSDT",
          "DOGEUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "CRVUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "API3USDT",
          "AVAXUSDT",
          "ENAUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 21,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 115,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-22",
        "decision_time_utc": "2025-08-22T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "ASRUSDT",
          "API3USDT",
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 21,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 117,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-23",
        "decision_time_utc": "2025-08-23T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "BBUSDT",
          "ENAUSDT",
          "ARBUSDT",
          "ETHUSDT",
          "ETHFIUSDT",
          "ETCUSDT",
          "AAVEUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "FLOKIUSDT",
          "DOTUSDT",
          "BNBUSDT",
          "CRVUSDT",
          "APTUSDT",
          "BTCUSDT",
          "BCHUSDT",
          "FILUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 21,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 109,
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
          "AAVEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "DOTUSDT",
          "BIOUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 21,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 117,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-25",
        "decision_time_utc": "2025-08-25T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "CRVUSDT",
          "AAVEUSDT",
          "DOTUSDT",
          "BONKUSDT",
          "BOMEUSDT",
          "ETHFIUSDT",
          "FILUSDT",
          "ETCUSDT",
          "BIOUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 21,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 112,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-26",
        "decision_time_utc": "2025-08-26T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "BIOUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "DOTUSDT",
          "BONKUSDT",
          "CRVUSDT",
          "FILUSDT",
          "ETHFIUSDT",
          "APTUSDT",
          "FLOKIUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 21,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 112,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-27",
        "decision_time_utc": "2025-08-27T00:00:00+00:00",
        "selected_symbols": [
          "BERAUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "ENAUSDT",
          "EDUUSDT",
          "BCHUSDT",
          "BIOUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 21,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 116,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-28",
        "decision_time_utc": "2025-08-28T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "CKBUSDT",
          "AVAXUSDT",
          "BERAUSDT",
          "BIOUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 116,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-29",
        "decision_time_utc": "2025-08-29T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "DOLOUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ARBUSDT",
          "BNBUSDT",
          "DOTUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BIOUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 118,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-30",
        "decision_time_utc": "2025-08-30T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BONKUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "BCHUSDT",
          "DOTUSDT",
          "BIOUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 117,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-31",
        "decision_time_utc": "2025-08-31T00:00:00+00:00",
        "selected_symbols": [
          "DOLOUSDT",
          "CFXUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BONKUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "ARBUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 119,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-01",
        "decision_time_utc": "2025-09-01T00:00:00+00:00",
        "selected_symbols": [
          "DOLOUSDT",
          "AXSUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "FORMUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 119,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-02",
        "decision_time_utc": "2025-09-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "FORMUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "FILUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "AAVEUSDT",
          "DOTUSDT",
          "BIOUSDT",
          "APTUSDT",
          "DOLOUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 114,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-03",
        "decision_time_utc": "2025-09-03T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "BCHUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "ADAUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 119,
          "low_trades": 0,
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
          "AAVEUSDT",
          "ARBUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 120,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-05",
        "decision_time_utc": "2025-09-05T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 120,
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
          "ETHUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "BCHUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 118,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-07",
        "decision_time_utc": "2025-09-07T00:00:00+00:00",
        "selected_symbols": [
          "DOLOUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "BIOUSDT",
          "BCHUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 121,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-08",
        "decision_time_utc": "2025-09-08T00:00:00+00:00",
        "selected_symbols": [
          "DOGEUSDT",
          "DOTUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "DOLOUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 121,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-09",
        "decision_time_utc": "2025-09-09T00:00:00+00:00",
        "selected_symbols": [
          "ARKMUSDT",
          "BONKUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "DOTUSDT",
          "BCHUSDT",
          "DOLOUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 116,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-10",
        "decision_time_utc": "2025-09-10T00:00:00+00:00",
        "selected_symbols": [
          "ARKMUSDT",
          "AIUSDT",
          "ENAUSDT",
          "DOLOUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "DOTUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "AAVEUSDT",
          "BCHUSDT",
          "EIGENUSDT",
          "FETUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 113,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-11",
        "decision_time_utc": "2025-09-11T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "1000SATSUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "DOLOUSDT",
          "BONKUSDT",
          "ENAUSDT",
          "DOTUSDT",
          "ARBUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 117,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-12",
        "decision_time_utc": "2025-09-12T00:00:00+00:00",
        "selected_symbols": [
          "ETHFIUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "DOLOUSDT",
          "BIOUSDT",
          "ARKMUSDT",
          "ARBUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "FORMUSDT",
          "ACEUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 114,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-13",
        "decision_time_utc": "2025-09-13T00:00:00+00:00",
        "selected_symbols": [
          "DOGEUSDT",
          "ETHUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "ETHFIUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 119,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-14",
        "decision_time_utc": "2025-09-14T00:00:00+00:00",
        "selected_symbols": [
          "EIGENUSDT",
          "BIOUSDT",
          "DOGEUSDT",
          "ETHFIUSDT",
          "AVAXUSDT",
          "DOTUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "ENAUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 117,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-15",
        "decision_time_utc": "2025-09-15T00:00:00+00:00",
        "selected_symbols": [
          "DOLOUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BIOUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "ARBUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 119,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-16",
        "decision_time_utc": "2025-09-16T00:00:00+00:00",
        "selected_symbols": [
          "CUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "DOTUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 19,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 119,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-17",
        "decision_time_utc": "2025-09-17T00:00:00+00:00",
        "selected_symbols": [
          "BNBUSDT",
          "BTCUSDT",
          "BONKUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "DOTUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "FORMUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "AVNTUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 19,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 118,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-18",
        "decision_time_utc": "2025-09-18T00:00:00+00:00",
        "selected_symbols": [
          "EIGENUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "CRVUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "ETHFIUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "AVNTUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "DOTUSDT",
          "ENAUSDT",
          "BCHUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 19,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 115,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-19",
        "decision_time_utc": "2025-09-19T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "BROCCOLI714USDT",
          "EIGENUSDT",
          "AVNTUSDT",
          "BTCUSDT",
          "CRVUSDT",
          "ETHUSDT",
          "DOTUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "ENAUSDT",
          "ARBUSDT",
          "ETHFIUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 18,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 115,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-20",
        "decision_time_utc": "2025-09-20T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AVNTUSDT",
          "DOTUSDT",
          "ARBUSDT",
          "BARDUSDT",
          "BONKUSDT",
          "ETHFIUSDT",
          "APTUSDT",
          "BCHUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 18,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 116,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-21",
        "decision_time_utc": "2025-09-21T00:00:00+00:00",
        "selected_symbols": [
          "AVNTUSDT",
          "BROCCOLI714USDT",
          "CAKEUSDT",
          "BNBUSDT",
          "BARDUSDT",
          "BIOUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "FORMUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 18,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 119,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-22",
        "decision_time_utc": "2025-09-22T00:00:00+00:00",
        "selected_symbols": [
          "AVNTUSDT",
          "AEVOUSDT",
          "DEXEUSDT",
          "EDUUSDT",
          "BARDUSDT",
          "BNBUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "CAKEUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 18,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 119,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-23",
        "decision_time_utc": "2025-09-23T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "EIGENUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "DOTUSDT",
          "BONKUSDT",
          "APTUSDT",
          "BBUSDT",
          "ETHFIUSDT",
          "CAKEUSDT",
          "CRVUSDT",
          "ETCUSDT",
          "AVNTUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 113,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-24",
        "decision_time_utc": "2025-09-24T00:00:00+00:00",
        "selected_symbols": [
          "BARDUSDT",
          "0GUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "AVNTUSDT",
          "ENAUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 120,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-25",
        "decision_time_utc": "2025-09-25T00:00:00+00:00",
        "selected_symbols": [
          "BBUSDT",
          "ETHFIUSDT",
          "AVNTUSDT",
          "EIGENUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "0GUSDT",
          "ENAUSDT",
          "BARDUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 119,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-26",
        "decision_time_utc": "2025-09-26T00:00:00+00:00",
        "selected_symbols": [
          "1000SATSUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "BARDUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "ARBUSDT",
          "ETHFIUSDT",
          "AAVEUSDT",
          "0GUSDT",
          "BONKUSDT",
          "DOTUSDT",
          "EIGENUSDT",
          "APTUSDT",
          "CRVUSDT",
          "AWEUSDT",
          "AVNTUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 113,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-27",
        "decision_time_utc": "2025-09-27T00:00:00+00:00",
        "selected_symbols": [
          "ALPINEUSDT",
          "1000SATSUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ETHFIUSDT",
          "ENAUSDT",
          "AVNTUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "EIGENUSDT",
          "0GUSDT",
          "BARDUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 117,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-28",
        "decision_time_utc": "2025-09-28T00:00:00+00:00",
        "selected_symbols": [
          "ALPINEUSDT",
          "AEVOUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "AVNTUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "1000SATSUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 123,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-29",
        "decision_time_utc": "2025-09-29T00:00:00+00:00",
        "selected_symbols": [
          "FORMUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AVNTUSDT",
          "BARDUSDT",
          "ALPINEUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 122,
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
          "AVAXUSDT",
          "AVNTUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "0GUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 16,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 122,
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
          "BTCUSDT",
          "ETHUSDT",
          "APTUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "FFUSDT",
          "ALPINEUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 122,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-02",
        "decision_time_utc": "2025-10-02T00:00:00+00:00",
        "selected_symbols": [
          "DASHUSDT",
          "APTUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "0GUSDT",
          "BTCUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "FFUSDT",
          "ENAUSDT",
          "EIGENUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "BARDUSDT",
          "AVNTUSDT",
          "EDENUSDT",
          "ALPINEUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 117,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-03",
        "decision_time_utc": "2025-10-03T00:00:00+00:00",
        "selected_symbols": [
          "C98USDT",
          "ETHFIUSDT",
          "CAKEUSDT",
          "EIGENUSDT",
          "FORMUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "APTUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DASHUSDT",
          "DOTUSDT",
          "ARBUSDT",
          "ADAUSDT",
          "BARDUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "AVNTUSDT",
          "AAVEUSDT",
          "ALPINEUSDT",
          "FFUSDT",
          "EDENUSDT"
        ],
        "candidate_count": 23,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 112,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-04",
        "decision_time_utc": "2025-10-04T00:00:00+00:00",
        "selected_symbols": [
          "0GUSDT",
          "CAKEUSDT",
          "BNBUSDT",
          "AVNTUSDT",
          "EIGENUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "FFUSDT",
          "APTUSDT",
          "ETHFIUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "2ZUSDT",
          "ENAUSDT",
          "AAVEUSDT",
          "FORMUSDT",
          "BONKUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 117,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-05",
        "decision_time_utc": "2025-10-05T00:00:00+00:00",
        "selected_symbols": [
          "FLOKIUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "EIGENUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ETHFIUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "CAKEUSDT",
          "AVNTUSDT",
          "BONKUSDT",
          "ENAUSDT",
          "FORMUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 121,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-06",
        "decision_time_utc": "2025-10-06T00:00:00+00:00",
        "selected_symbols": [
          "CELOUSDT",
          "EDENUSDT",
          "APTUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "AVNTUSDT",
          "CAKEUSDT",
          "BONKUSDT",
          "FLOKIUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 122,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-07",
        "decision_time_utc": "2025-10-07T00:00:00+00:00",
        "selected_symbols": [
          "CAKEUSDT",
          "ALPINEUSDT",
          "BONKUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "DOTUSDT",
          "ARBUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "EIGENUSDT",
          "ENAUSDT",
          "CELOUSDT",
          "AVAXUSDT",
          "FORMUSDT",
          "FLOKIUSDT",
          "AVNTUSDT",
          "APTUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 118,
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
          "API3USDT",
          "BROCCOLI714USDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "EIGENUSDT",
          "ENAUSDT",
          "FLOKIUSDT",
          "BONKUSDT",
          "ARBUSDT",
          "AVNTUSDT",
          "AAVEUSDT",
          "DOTUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 117,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-09",
        "decision_time_utc": "2025-10-09T00:00:00+00:00",
        "selected_symbols": [
          "1000CHEEMSUSDT",
          "ENAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "FORMUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ASTERUSDT",
          "CAKEUSDT",
          "FFUSDT",
          "APTUSDT",
          "AVNTUSDT",
          "BROCCOLI714USDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 122,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-10",
        "decision_time_utc": "2025-10-10T00:00:00+00:00",
        "selected_symbols": [
          "1000CHEEMSUSDT",
          "ALICEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "CAKEUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "FFUSDT",
          "APTUSDT",
          "FETUSDT",
          "DOTUSDT",
          "FORMUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 121,
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
          "BCHUSDT",
          "BNBUSDT",
          "1000CHEEMSUSDT",
          "DASHUSDT",
          "ASTERUSDT",
          "ALGOUSDT",
          "CAKEUSDT",
          "DOGEUSDT",
          "ETCUSDT",
          "ADAUSDT",
          "FFUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "EIGENUSDT",
          "ARBUSDT",
          "CRVUSDT",
          "ENAUSDT",
          "FETUSDT",
          "AVNTUSDT",
          "ARKMUSDT",
          "BONKUSDT",
          "GALAUSDT",
          "FLOKIUSDT",
          "DOTUSDT",
          "APTUSDT",
          "BNSOLUSDT",
          "ALICEUSDT",
          "FILUSDT",
          "DYDXUSDT",
          "ENSUSDT",
          "FORMUSDT",
          "ETHFIUSDT",
          "ATOMUSDT"
        ],
        "candidate_count": 35,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 102,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-12",
        "decision_time_utc": "2025-10-12T00:00:00+00:00",
        "selected_symbols": [
          "FFUSDT",
          "AVNTUSDT",
          "BNBUSDT",
          "FETUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ETCUSDT",
          "BTCUSDT",
          "DASHUSDT",
          "ETHUSDT",
          "BONKUSDT",
          "DOGEUSDT",
          "DOTUSDT",
          "ARBUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "FILUSDT",
          "BNSOLUSDT",
          "APTUSDT",
          "CAKEUSDT",
          "FORMUSDT",
          "CRVUSDT",
          "BCHUSDT",
          "ETHFIUSDT",
          "EIGENUSDT",
          "FLOKIUSDT"
        ],
        "candidate_count": 27,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 110,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-13",
        "decision_time_utc": "2025-10-13T00:00:00+00:00",
        "selected_symbols": [
          "FORMUSDT",
          "CAKEUSDT",
          "ASTERUSDT",
          "DASHUSDT",
          "FFUSDT",
          "EIGENUSDT",
          "BNBUSDT",
          "CRVUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BONKUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "ETHFIUSDT",
          "ARBUSDT",
          "ETCUSDT",
          "AVNTUSDT",
          "BTCUSDT",
          "DOTUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "FILUSDT",
          "FETUSDT",
          "EDENUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 112,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-14",
        "decision_time_utc": "2025-10-14T00:00:00+00:00",
        "selected_symbols": [
          "FFUSDT",
          "ALICEUSDT",
          "BATUSDT",
          "ENAUSDT",
          "CRVUSDT",
          "EDENUSDT",
          "FORMUSDT",
          "BONKUSDT",
          "CAKEUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "2ZUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "FILUSDT",
          "DOTUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "ETHFIUSDT",
          "ASTERUSDT",
          "APTUSDT",
          "FETUSDT",
          "DASHUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 112,
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
          "BNBUSDT",
          "DOGEUSDT",
          "EDENUSDT",
          "2ZUSDT",
          "FORMUSDT",
          "ADAUSDT",
          "CAKEUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "BCHUSDT",
          "FETUSDT",
          "FFUSDT",
          "ARBUSDT",
          "CRVUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "DOTUSDT",
          "EULUSDT",
          "FILUSDT"
        ],
        "candidate_count": 23,
        "filter_counts": {
          "missing_1h": 11,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 115,
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
          "BNBUSDT",
          "2ZUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "CAKEUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "DASHUSDT",
          "FORMUSDT",
          "FETUSDT",
          "CRVUSDT",
          "FFUSDT",
          "EULUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "ENSOUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 11,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 120,
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
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "CAKEUSDT",
          "ARBUSDT",
          "FETUSDT",
          "FORMUSDT",
          "DOTUSDT",
          "CRVUSDT",
          "FFUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "BELUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 11,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 120,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-18",
        "decision_time_utc": "2025-10-18T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BCHUSDT",
          "CAKEUSDT",
          "ARBUSDT",
          "DOTUSDT",
          "BONKUSDT",
          "FFUSDT",
          "CRVUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 11,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 123,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-19",
        "decision_time_utc": "2025-10-19T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 11,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 131,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-20",
        "decision_time_utc": "2025-10-20T00:00:00+00:00",
        "selected_symbols": [
          "FETUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ASTERUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 11,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 130,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-21",
        "decision_time_utc": "2025-10-21T00:00:00+00:00",
        "selected_symbols": [
          "AVNTUSDT",
          "AUCTIONUSDT",
          "FLOKIUSDT",
          "BIOUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ASTERUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "CAKEUSDT",
          "FETUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 11,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 125,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-22",
        "decision_time_utc": "2025-10-22T00:00:00+00:00",
        "selected_symbols": [
          "FFUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "ENAUSDT",
          "AVNTUSDT",
          "ADAUSDT",
          "BCHUSDT",
          "AVAXUSDT",
          "CAKEUSDT",
          "FLOKIUSDT",
          "FETUSDT",
          "AAVEUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 11,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 123,
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
          "DOGEUSDT",
          "ASTERUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "CAKEUSDT",
          "AAVEUSDT",
          "FFUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 11,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 127,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-24",
        "decision_time_utc": "2025-10-24T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVNTUSDT",
          "BCHUSDT",
          "CAKEUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 11,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 128,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-25",
        "decision_time_utc": "2025-10-25T00:00:00+00:00",
        "selected_symbols": [
          "AVNTUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "CAKEUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 11,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 129,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-26",
        "decision_time_utc": "2025-10-26T00:00:00+00:00",
        "selected_symbols": [
          "AIXBTUSDT",
          "EDENUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "AVNTUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 131,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-27",
        "decision_time_utc": "2025-10-27T00:00:00+00:00",
        "selected_symbols": [
          "FFUSDT",
          "DASHUSDT",
          "AIXBTUSDT",
          "BCHUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "AVNTUSDT",
          "EULUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 126,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-28",
        "decision_time_utc": "2025-10-28T00:00:00+00:00",
        "selected_symbols": [
          "DIAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "ENSOUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "FFUSDT",
          "EULUSDT",
          "1000CHEEMSUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 126,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-29",
        "decision_time_utc": "2025-10-29T00:00:00+00:00",
        "selected_symbols": [
          "EULUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ENSOUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 129,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-30",
        "decision_time_utc": "2025-10-30T00:00:00+00:00",
        "selected_symbols": [
          "EULUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "ENAUSDT",
          "BCHUSDT",
          "ENSOUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 128,
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
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "BCHUSDT",
          "ARBUSDT",
          "DOTUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 128,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-01",
        "decision_time_utc": "2025-11-01T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 130,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-02",
        "decision_time_utc": "2025-11-02T00:00:00+00:00",
        "selected_symbols": [
          "DASHUSDT",
          "FILUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 132,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-03",
        "decision_time_utc": "2025-11-03T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "DASHUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "FILUSDT",
          "ENAUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 131,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-04",
        "decision_time_utc": "2025-11-04T00:00:00+00:00",
        "selected_symbols": [
          "DASHUSDT",
          "0GUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "DOTUSDT",
          "FILUSDT",
          "BCHUSDT",
          "BONKUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 123,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-05",
        "decision_time_utc": "2025-11-05T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DASHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "FILUSDT",
          "DOTUSDT",
          "BONKUSDT",
          "BCHUSDT",
          "CAKEUSDT",
          "CRVUSDT",
          "APTUSDT",
          "DCRUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 120,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-06",
        "decision_time_utc": "2025-11-06T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "ETHUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "DASHUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 129,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-07",
        "decision_time_utc": "2025-11-07T00:00:00+00:00",
        "selected_symbols": [
          "FILUSDT",
          "ARUSDT",
          "DASHUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "AAVEUSDT",
          "ALCXUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 127,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-08",
        "decision_time_utc": "2025-11-08T00:00:00+00:00",
        "selected_symbols": [
          "FILUSDT",
          "FLUXUSDT",
          "FETUSDT",
          "ARUSDT",
          "ETCUSDT",
          "DOTUSDT",
          "APTUSDT",
          "ASTERUSDT",
          "ARBUSDT",
          "DOGEUSDT",
          "DUSKUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BCHUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "DASHUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 119,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-09",
        "decision_time_utc": "2025-11-09T00:00:00+00:00",
        "selected_symbols": [
          "0GUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "FILUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "DASHUSDT",
          "FETUSDT",
          "AAVEUSDT",
          "DOTUSDT",
          "ARUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "ETCUSDT",
          "FLUXUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 123,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-10",
        "decision_time_utc": "2025-11-10T00:00:00+00:00",
        "selected_symbols": [
          "0GUSDT",
          "ETHUSDT",
          "ASTERUSDT",
          "BTCUSDT",
          "FUSDT",
          "DOGEUSDT",
          "FETUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "FILUSDT",
          "AVAXUSDT",
          "DASHUSDT",
          "ARUSDT",
          "DOTUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 125,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-11",
        "decision_time_utc": "2025-11-11T00:00:00+00:00",
        "selected_symbols": [
          "FUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "DOTUSDT",
          "FILUSDT",
          "FETUSDT",
          "DASHUSDT",
          "COTIUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 125,
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
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "FILUSDT",
          "ADAUSDT",
          "FETUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "DASHUSDT",
          "CAKEUSDT",
          "BCHUSDT",
          "DOTUSDT",
          "AAVEUSDT",
          "CFXUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 9,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 124,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-13",
        "decision_time_utc": "2025-11-13T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "FILUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "DASHUSDT",
          "AVAXUSDT",
          "FETUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "ALLOUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 9,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 127,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-14",
        "decision_time_utc": "2025-11-14T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "ALCXUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "ENAUSDT",
          "FILUSDT",
          "DASHUSDT",
          "FETUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "ALLOUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 125,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-15",
        "decision_time_utc": "2025-11-15T00:00:00+00:00",
        "selected_symbols": [
          "DASHUSDT",
          "BTCUSDT",
          "ASTERUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "ALLOUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "FILUSDT",
          "ARBUSDT",
          "APTUSDT",
          "DOTUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 126,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-16",
        "decision_time_utc": "2025-11-16T00:00:00+00:00",
        "selected_symbols": [
          "DASHUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "FILUSDT",
          "ADAUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 133,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-17",
        "decision_time_utc": "2025-11-17T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DASHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "FILUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 132,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-18",
        "decision_time_utc": "2025-11-18T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "FILUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "DASHUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "BANANAS31USDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 129,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-19",
        "decision_time_utc": "2025-11-19T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "FETUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "BCHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "FILUSDT",
          "AVAXUSDT",
          "DASHUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 130,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-20",
        "decision_time_utc": "2025-11-20T00:00:00+00:00",
        "selected_symbols": [
          "FETUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DASHUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "FILUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 131,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-21",
        "decision_time_utc": "2025-11-21T00:00:00+00:00",
        "selected_symbols": [
          "DYMUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "FETUSDT",
          "ALLOUSDT",
          "DASHUSDT",
          "ENAUSDT",
          "BCHUSDT",
          "AAVEUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 127,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-22",
        "decision_time_utc": "2025-11-22T00:00:00+00:00",
        "selected_symbols": [
          "BCHUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "DASHUSDT",
          "FETUSDT",
          "FILUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "DOTUSDT",
          "ALLOUSDT",
          "DYMUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 124,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-23",
        "decision_time_utc": "2025-11-23T00:00:00+00:00",
        "selected_symbols": [
          "BCHUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "DASHUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 132,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-24",
        "decision_time_utc": "2025-11-24T00:00:00+00:00",
        "selected_symbols": [
          "DYMUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "DASHUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 132,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-25",
        "decision_time_utc": "2025-11-25T00:00:00+00:00",
        "selected_symbols": [
          "BANANAS31USDT",
          "ALLOUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 131,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-26",
        "decision_time_utc": "2025-11-26T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "ALLOUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 133,
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
          "AVAXUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "ALLOUSDT",
          "ASTERUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 129,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2025-11-28",
        "decision_time_utc": "2025-11-28T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "ASTERUSDT",
          "BANANAS31USDT",
          "ADAUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 132,
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
          "BNBUSDT",
          "DOGEUSDT",
          "ATUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 132,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-30",
        "decision_time_utc": "2025-11-30T00:00:00+00:00",
        "selected_symbols": [
          "ATUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "BCHUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 136,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-01",
        "decision_time_utc": "2025-12-01T00:00:00+00:00",
        "selected_symbols": [
          "BCHUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ATUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 134,
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
          "BNBUSDT",
          "ASTERUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BCHUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "ATUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 132,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-03",
        "decision_time_utc": "2025-12-03T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ASTERUSDT",
          "BCHUSDT",
          "ATUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 132,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-04",
        "decision_time_utc": "2025-12-04T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "ASTERUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "ATUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 132,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-05",
        "decision_time_utc": "2025-12-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "BCHUSDT",
          "ATUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 132,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-06",
        "decision_time_utc": "2025-12-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "ATUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 134,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-07",
        "decision_time_utc": "2025-12-07T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 138,
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
          "ENAUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "AVAXUSDT",
          "ATUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 134,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-09",
        "decision_time_utc": "2025-12-09T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "ATUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 135,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-10",
        "decision_time_utc": "2025-12-10T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "ATUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 133,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-11",
        "decision_time_utc": "2025-12-11T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "ASTERUSDT",
          "ATUSDT",
          "ENAUSDT",
          "BCHUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 133,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-12",
        "decision_time_utc": "2025-12-12T00:00:00+00:00",
        "selected_symbols": [
          "BARDUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "ATUSDT",
          "AVAXUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 133,
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
          "BCHUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 133,
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
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 140,
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
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 137,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-16",
        "decision_time_utc": "2025-12-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 135,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-17",
        "decision_time_utc": "2025-12-17T00:00:00+00:00",
        "selected_symbols": [
          "FORMUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "AVAXUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 135,
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
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "FORMUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 134,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-19",
        "decision_time_utc": "2025-12-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 134,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-20",
        "decision_time_utc": "2025-12-20T00:00:00+00:00",
        "selected_symbols": [
          "BCHUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "ASTERUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 133,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-21",
        "decision_time_utc": "2025-12-21T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 138,
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
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 138,
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
          "AVAXUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "ASTERUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 134,
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
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "AVAXUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 136,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-25",
        "decision_time_utc": "2025-12-25T00:00:00+00:00",
        "selected_symbols": [
          "AVNTUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 138,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-26",
        "decision_time_utc": "2025-12-26T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 138,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-27",
        "decision_time_utc": "2025-12-27T00:00:00+00:00",
        "selected_symbols": [
          "ATUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 136,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-28",
        "decision_time_utc": "2025-12-28T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "FLOWUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 139,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-29",
        "decision_time_utc": "2025-12-29T00:00:00+00:00",
        "selected_symbols": [
          "ATUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 137,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-30",
        "decision_time_utc": "2025-12-30T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ATUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 135,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-31",
        "decision_time_utc": "2025-12-31T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "BCHUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 137,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-01",
        "decision_time_utc": "2026-01-01T00:00:00+00:00",
        "selected_symbols": [
          "CHZUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ATUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BROCCOLI714USDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 135,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-02",
        "decision_time_utc": "2026-01-02T00:00:00+00:00",
        "selected_symbols": [
          "FILUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BROCCOLI714USDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 135,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-03",
        "decision_time_utc": "2026-01-03T00:00:00+00:00",
        "selected_symbols": [
          "DOGEUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "ASTERUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 133,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-04",
        "decision_time_utc": "2026-01-04T00:00:00+00:00",
        "selected_symbols": [
          "BCHUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 135,
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
          "FLOKIUSDT",
          "FETUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 131,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-06",
        "decision_time_utc": "2026-01-06T00:00:00+00:00",
        "selected_symbols": [
          "FETUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "FILUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "ENAUSDT",
          "ASTERUSDT",
          "BROCCOLI714USDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 130,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-07",
        "decision_time_utc": "2026-01-07T00:00:00+00:00",
        "selected_symbols": [
          "BROCCOLI714USDT",
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "ASTERUSDT",
          "FETUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 131,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-08",
        "decision_time_utc": "2026-01-08T00:00:00+00:00",
        "selected_symbols": [
          "BREVUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "BROCCOLI714USDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 134,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-09",
        "decision_time_utc": "2026-01-09T00:00:00+00:00",
        "selected_symbols": [
          "BROCCOLI714USDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "BREVUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 135,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-10",
        "decision_time_utc": "2026-01-10T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 139,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-11",
        "decision_time_utc": "2026-01-11T00:00:00+00:00",
        "selected_symbols": [
          "BNBUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 140,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-12",
        "decision_time_utc": "2026-01-12T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 139,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-13",
        "decision_time_utc": "2026-01-13T00:00:00+00:00",
        "selected_symbols": [
          "DOLOUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 135,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-14",
        "decision_time_utc": "2026-01-14T00:00:00+00:00",
        "selected_symbols": [
          "DASHUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "BREVUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 133,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-15",
        "decision_time_utc": "2026-01-15T00:00:00+00:00",
        "selected_symbols": [
          "BERAUSDT",
          "DASHUSDT",
          "AXSUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "FILUSDT",
          "BCHUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "BREVUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 129,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-16",
        "decision_time_utc": "2026-01-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DASHUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BREVUSDT",
          "ASTERUSDT",
          "AVAXUSDT",
          "FILUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 2,
          "reconstruct_error": 0,
          "low_quote_volume": 133,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-17",
        "decision_time_utc": "2026-01-17T00:00:00+00:00",
        "selected_symbols": [
          "DASHUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "FOGOUSDT",
          "ADAUSDT",
          "BREVUSDT",
          "AUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 135,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-18",
        "decision_time_utc": "2026-01-18T00:00:00+00:00",
        "selected_symbols": [
          "AXSUSDT",
          "BERAUSDT",
          "DUSKUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BREVUSDT",
          "BNBUSDT",
          "DASHUSDT",
          "DOGEUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 136,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-19",
        "decision_time_utc": "2026-01-19T00:00:00+00:00",
        "selected_symbols": [
          "FRAXUSDT",
          "DASHUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "AXSUSDT",
          "BREVUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 137,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-20",
        "decision_time_utc": "2026-01-20T00:00:00+00:00",
        "selected_symbols": [
          "ARPAUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "BREVUSDT",
          "ADAUSDT",
          "DASHUSDT",
          "ASTERUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "FOGOUSDT",
          "FRAXUSDT",
          "FILUSDT",
          "BCHUSDT",
          "DUSKUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 130,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-21",
        "decision_time_utc": "2026-01-21T00:00:00+00:00",
        "selected_symbols": [
          "AXSUSDT",
          "DUSKUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BREVUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "DASHUSDT",
          "ADAUSDT",
          "ASTERUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 133,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-22",
        "decision_time_utc": "2026-01-22T00:00:00+00:00",
        "selected_symbols": [
          "AXSUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "DASHUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 136,
          "low_trades": 0,
          "stable_like": 0
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
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 140,
          "low_trades": 0,
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
          "BNBUSDT",
          "DOGEUSDT",
          "FOGOUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 138,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-25",
        "decision_time_utc": "2026-01-25T00:00:00+00:00",
        "selected_symbols": [
          "ENSOUSDT",
          "FOGOUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "AXSUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 140,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-26",
        "decision_time_utc": "2026-01-26T00:00:00+00:00",
        "selected_symbols": [
          "AUCTIONUSDT",
          "DUSKUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "FOGOUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AXSUSDT",
          "ENSOUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 136,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-27",
        "decision_time_utc": "2026-01-27T00:00:00+00:00",
        "selected_symbols": [
          "AXSUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "FOGOUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 139,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-28",
        "decision_time_utc": "2026-01-28T00:00:00+00:00",
        "selected_symbols": [
          "FOGOUSDT",
          "ETHUSDT",
          "AXSUSDT",
          "BTCUSDT",
          "DASHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 138,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-29",
        "decision_time_utc": "2026-01-29T00:00:00+00:00",
        "selected_symbols": [
          "FOGOUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 139,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-30",
        "decision_time_utc": "2026-01-30T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "FOGOUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 138,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-31",
        "decision_time_utc": "2026-01-31T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ASTERUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 138,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-01",
        "decision_time_utc": "2026-02-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ASTERUSDT",
          "ENAUSDT",
          "AAVEUSDT",
          "BCHUSDT",
          "FILUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 135,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-02",
        "decision_time_utc": "2026-02-02T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 139,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-03",
        "decision_time_utc": "2026-02-03T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 139,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-04",
        "decision_time_utc": "2026-02-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "ASTERUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 139,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-05",
        "decision_time_utc": "2026-02-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 140,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-06",
        "decision_time_utc": "2026-02-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ASTERUSDT",
          "AAVEUSDT",
          "BCHUSDT",
          "ENAUSDT",
          "FILUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 134,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-07",
        "decision_time_utc": "2026-02-07T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "FILUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 135,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-08",
        "decision_time_utc": "2026-02-08T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ASTERUSDT",
          "BCHUSDT",
          "AVAXUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 137,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-09",
        "decision_time_utc": "2026-02-09T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 140,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-10",
        "decision_time_utc": "2026-02-10T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "BERAUSDT",
          "ADAUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 139,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-11",
        "decision_time_utc": "2026-02-11T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 141,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-12",
        "decision_time_utc": "2026-02-12T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "BERAUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 140,
          "low_trades": 0,
          "stable_like": 0
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
          "BNBUSDT",
          "BERAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 140,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-14",
        "decision_time_utc": "2026-02-14T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-15",
        "decision_time_utc": "2026-02-15T00:00:00+00:00",
        "selected_symbols": [
          "DOGEUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-16",
        "decision_time_utc": "2026-02-16T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-17",
        "decision_time_utc": "2026-02-17T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-18",
        "decision_time_utc": "2026-02-18T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-19",
        "decision_time_utc": "2026-02-19T00:00:00+00:00",
        "selected_symbols": [
          "ESPUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-20",
        "decision_time_utc": "2026-02-20T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-21",
        "decision_time_utc": "2026-02-21T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "ENSOUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 139,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-22",
        "decision_time_utc": "2026-02-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-23",
        "decision_time_utc": "2026-02-23T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-24",
        "decision_time_utc": "2026-02-24T00:00:00+00:00",
        "selected_symbols": [
          "ESPUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "BCHUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 140,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-25",
        "decision_time_utc": "2026-02-25T00:00:00+00:00",
        "selected_symbols": [
          "ENSOUSDT",
          "ESPUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 140,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-26",
        "decision_time_utc": "2026-02-26T00:00:00+00:00",
        "selected_symbols": [
          "DOTUSDT",
          "APTUSDT",
          "FILUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ENSOUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 137,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-27",
        "decision_time_utc": "2026-02-27T00:00:00+00:00",
        "selected_symbols": [
          "BARDUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "DOTUSDT",
          "AVAXUSDT",
          "ENSOUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 138,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-28",
        "decision_time_utc": "2026-02-28T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-01",
        "decision_time_utc": "2026-03-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOTUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 140,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-02",
        "decision_time_utc": "2026-03-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 141,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-03",
        "decision_time_utc": "2026-03-03T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 140,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-04",
        "decision_time_utc": "2026-03-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-05",
        "decision_time_utc": "2026-03-05T00:00:00+00:00",
        "selected_symbols": [
          "DOGEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ENSOUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 140,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-06",
        "decision_time_utc": "2026-03-06T00:00:00+00:00",
        "selected_symbols": [
          "BARDUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 140,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-07",
        "decision_time_utc": "2026-03-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-08",
        "decision_time_utc": "2026-03-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-09",
        "decision_time_utc": "2026-03-09T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-10",
        "decision_time_utc": "2026-03-10T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-11",
        "decision_time_utc": "2026-03-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 141,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-12",
        "decision_time_utc": "2026-03-12T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-13",
        "decision_time_utc": "2026-03-13T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-14",
        "decision_time_utc": "2026-03-14T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 141,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-15",
        "decision_time_utc": "2026-03-15T00:00:00+00:00",
        "selected_symbols": [
          "COSUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "BANANAS31USDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 141,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-16",
        "decision_time_utc": "2026-03-16T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-17",
        "decision_time_utc": "2026-03-17T00:00:00+00:00",
        "selected_symbols": [
          "FETUSDT",
          "DOTUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 139,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-18",
        "decision_time_utc": "2026-03-18T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "ASTERUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 141,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-19",
        "decision_time_utc": "2026-03-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ASTERUSDT",
          "AVAXUSDT",
          "BARDUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 140,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-20",
        "decision_time_utc": "2026-03-20T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 144,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-21",
        "decision_time_utc": "2026-03-21T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 144,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-22",
        "decision_time_utc": "2026-03-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 144,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-23",
        "decision_time_utc": "2026-03-23T00:00:00+00:00",
        "selected_symbols": [
          "BANANAS31USDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-24",
        "decision_time_utc": "2026-03-24T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-25",
        "decision_time_utc": "2026-03-25T00:00:00+00:00",
        "selected_symbols": [
          "FETUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-26",
        "decision_time_utc": "2026-03-26T00:00:00+00:00",
        "selected_symbols": [
          "FETUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-27",
        "decision_time_utc": "2026-03-27T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-28",
        "decision_time_utc": "2026-03-28T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "CFGUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-29",
        "decision_time_utc": "2026-03-29T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 144,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-30",
        "decision_time_utc": "2026-03-30T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "DOGEUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-31",
        "decision_time_utc": "2026-03-31T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 144,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-01",
        "decision_time_utc": "2026-04-01T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-02",
        "decision_time_utc": "2026-04-02T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-03",
        "decision_time_utc": "2026-04-03T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-04",
        "decision_time_utc": "2026-04-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 144,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-05",
        "decision_time_utc": "2026-04-05T00:00:00+00:00",
        "selected_symbols": [
          "DUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 144,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-06",
        "decision_time_utc": "2026-04-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "DUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-07",
        "decision_time_utc": "2026-04-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-08",
        "decision_time_utc": "2026-04-08T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-09",
        "decision_time_utc": "2026-04-09T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-10",
        "decision_time_utc": "2026-04-10T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ENJUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-11",
        "decision_time_utc": "2026-04-11T00:00:00+00:00",
        "selected_symbols": [
          "DASHUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "FFUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-12",
        "decision_time_utc": "2026-04-12T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DASHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "FFUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 141,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-13",
        "decision_time_utc": "2026-04-13T00:00:00+00:00",
        "selected_symbols": [
          "ENJUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "DASHUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 141,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-14",
        "decision_time_utc": "2026-04-14T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "ENJUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 141,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-15",
        "decision_time_utc": "2026-04-15T00:00:00+00:00",
        "selected_symbols": [
          "ENJUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "BARDUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 140,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-16",
        "decision_time_utc": "2026-04-16T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "ENJUSDT",
          "BARDUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 140,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-17",
        "decision_time_utc": "2026-04-17T00:00:00+00:00",
        "selected_symbols": [
          "1000SATSUSDT",
          "AAVEUSDT",
          "BIOUSDT",
          "BARDUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ENJUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 137,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-18",
        "decision_time_utc": "2026-04-18T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "AVNTUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 140,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-19",
        "decision_time_utc": "2026-04-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "AVNTUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "ALICEUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 141,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-20",
        "decision_time_utc": "2026-04-20T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "ENJUSDT",
          "DOGEUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BOMEUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 140,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-21",
        "decision_time_utc": "2026-04-21T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-22",
        "decision_time_utc": "2026-04-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-23",
        "decision_time_utc": "2026-04-23T00:00:00+00:00",
        "selected_symbols": [
          "CHIPUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-24",
        "decision_time_utc": "2026-04-24T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "CHIPUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-25",
        "decision_time_utc": "2026-04-25T00:00:00+00:00",
        "selected_symbols": [
          "APEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "CHIPUSDT",
          "BNBUSDT",
          "ENJUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-26",
        "decision_time_utc": "2026-04-26T00:00:00+00:00",
        "selected_symbols": [
          "AXSUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "CHIPUSDT",
          "DOGEUSDT",
          "API3USDT",
          "BNBUSDT",
          "APEUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 141,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-27",
        "decision_time_utc": "2026-04-27T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "CHIPUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 144,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-28",
        "decision_time_utc": "2026-04-28T00:00:00+00:00",
        "selected_symbols": [
          "CHIPUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 144,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-29",
        "decision_time_utc": "2026-04-29T00:00:00+00:00",
        "selected_symbols": [
          "APEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "CHIPUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-30",
        "decision_time_utc": "2026-04-30T00:00:00+00:00",
        "selected_symbols": [
          "DOGEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "CHIPUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
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
          "BNBUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-02",
        "decision_time_utc": "2026-05-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "CHIPUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 144,
          "low_trades": 0,
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
          "DOGEUSDT",
          "CHIPUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-04",
        "decision_time_utc": "2026-05-04T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "CHIPUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "BABYUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-05",
        "decision_time_utc": "2026-05-05T00:00:00+00:00",
        "selected_symbols": [
          "DASHUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "CHIPUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-06",
        "decision_time_utc": "2026-05-06T00:00:00+00:00",
        "selected_symbols": [
          "DOGSUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "ETHUSDT",
          "DASHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-07",
        "decision_time_utc": "2026-05-07T00:00:00+00:00",
        "selected_symbols": [
          "FILUSDT",
          "ENAUSDT",
          "DASHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "BCHUSDT",
          "CHIPUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 138,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-08",
        "decision_time_utc": "2026-05-08T00:00:00+00:00",
        "selected_symbols": [
          "DOGSUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "CHIPUSDT",
          "DOGEUSDT",
          "DASHUSDT",
          "BNBUSDT",
          "FILUSDT",
          "DUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 140,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-09",
        "decision_time_utc": "2026-05-09T00:00:00+00:00",
        "selected_symbols": [
          "CHIPUSDT",
          "FILUSDT",
          "GALAUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 141,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-10",
        "decision_time_utc": "2026-05-10T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "CHIPUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "GALAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-11",
        "decision_time_utc": "2026-05-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "APTUSDT",
          "BNBUSDT",
          "CHIPUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-12",
        "decision_time_utc": "2026-05-12T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "CHIPUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 144,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-13",
        "decision_time_utc": "2026-05-13T00:00:00+00:00",
        "selected_symbols": [
          "CHIPUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 144,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-14",
        "decision_time_utc": "2026-05-14T00:00:00+00:00",
        "selected_symbols": [
          "DOGEUSDT",
          "BTCUSDT",
          "CHIPUSDT",
          "COSUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-15",
        "decision_time_utc": "2026-05-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 144,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-16",
        "decision_time_utc": "2026-05-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "AIGENSYNUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 145,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-17",
        "decision_time_utc": "2026-05-17T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 146,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-18",
        "decision_time_utc": "2026-05-18T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 146,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-19",
        "decision_time_utc": "2026-05-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 145,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-20",
        "decision_time_utc": "2026-05-20T00:00:00+00:00",
        "selected_symbols": [
          "EDENUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 145,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-21",
        "decision_time_utc": "2026-05-21T00:00:00+00:00",
        "selected_symbols": [
          "FIDAUSDT",
          "EDENUSDT",
          "DASHUSDT",
          "ALTUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-22",
        "decision_time_utc": "2026-05-22T00:00:00+00:00",
        "selected_symbols": [
          "FIDAUSDT",
          "ALLOUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "EDENUSDT",
          "ASTERUSDT",
          "ALTUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 141,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-23",
        "decision_time_utc": "2026-05-23T00:00:00+00:00",
        "selected_symbols": [
          "ALTUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ALLOUSDT",
          "ADAUSDT",
          "EDENUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-24",
        "decision_time_utc": "2026-05-24T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "EDENUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 144,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-25",
        "decision_time_utc": "2026-05-25T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 146,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-26",
        "decision_time_utc": "2026-05-26T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 146,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-27",
        "decision_time_utc": "2026-05-27T00:00:00+00:00",
        "selected_symbols": [
          "FETUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 145,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-28",
        "decision_time_utc": "2026-05-28T00:00:00+00:00",
        "selected_symbols": [
          "ALTUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "FILUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 144,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-29",
        "decision_time_utc": "2026-05-29T00:00:00+00:00",
        "selected_symbols": [
          "ALLOUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "BCHUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-30",
        "decision_time_utc": "2026-05-30T00:00:00+00:00",
        "selected_symbols": [
          "ALLOUSDT",
          "FETUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 144,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-31",
        "decision_time_utc": "2026-05-31T00:00:00+00:00",
        "selected_symbols": [
          "FETUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ALLOUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-06-01",
        "decision_time_utc": "2026-06-01T00:00:00+00:00",
        "selected_symbols": [
          "ALLOUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "DOGEUSDT",
          "FETUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 143,
          "low_trades": 0,
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
