---
created: 2026-06-09 14:06:30 CST
tags:
  - crypto
  - trading-system
  - backtest
backtest_run_id: 838e78b04c3a
report_version: v7
sample_sufficient: true
universe_mode: true
universe_type: dynamic
---

# 回测报告 2025-06-01 至 2026-06-01 v7

- 回测 ID：`838e78b04c3a`
- 交易对：`0GUSDT`, `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1INCHUSDT`, `2ZUSDT`, `AAVEUSDT`, `ACEUSDT`, `ADAUSDT`, `AEVOUSDT`, `AIUSDT`, `ALCXUSDT`, `ALGOUSDT`, `ALICEUSDT`, `ALLOUSDT`, `ALPINEUSDT`, `ALTUSDT`, `ANIMEUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARKMUSDT`, `ARUSDT`, `ASRUSDT`, `ASTERUSDT`, `ATUSDT`, `AUCTIONUSDT`, `AUSDT`, `AVAXUSDT`, `AVNTUSDT`, `AXLUSDT`, `AXSUSDT`, `BANANAS31USDT`, `BARDUSDT`, `BCHUSDT`, `BELUSDT`, `BERAUSDT`, `BIOUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BREVUSDT`, `BROCCOLI714USDT`, `BTCUSDT`, `CAKEUSDT`, `CFGUSDT`, `CFXUSDT`, `CHIPUSDT`, `CKBUSDT`, `COMPUSDT`, `COWUSDT`, `CRVUSDT`, `CTSIUSDT`, `CUSDT`, `CYBERUSDT`, `DASHUSDT`, `DCRUSDT`, `DIAUSDT`, `DOGEUSDT`, `DOGSUSDT`, `DOLOUSDT`, `DOTUSDT`, `DUSKUSDT`, `DYMUSDT`, `EDENUSDT`, `EIGENUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSOUSDT`, `EPICUSDT`, `ERAUSDT`, `ESPUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `EULUSDT`, `FETUSDT`, `FFUSDT`, `FILUSDT`, `FLOKIUSDT`, `FLOWUSDT`, `FLUXUSDT`, `FOGOUSDT`, `FORMUSDT`, `FUSDT`
- UTC 区间：2025-06-01T00:00:00+00:00 -> 2026-06-01T00:00:00+00:00
- 初始权益：10,000.00 USDT
- 最终权益：8,969.39 USDT
- 净收益：-10.31%
- 代码 commit：`6422fbd58a463293fcce66b875526ef203f4fba6`
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
- Selected symbols per refresh / 每次入选数量：min=2, avg=7.15, max=24
- Top selected symbols / 最常入选：`BTCUSDT`(366), `ETHUSDT`(366), `BNBUSDT`(344), `DOGEUSDT`(331), `ADAUSDT`(193), `ENAUSDT`(142), `AVAXUSDT`(130), `ASTERUSDT`(80), `BONKUSDT`(57), `AAVEUSDT`(51)
- Filter counts / 过滤统计：
```json
{
  "missing_1h": 3908,
  "insufficient_24h": 24,
  "reconstruct_error": 0,
  "low_quote_volume": 48346,
  "low_trades": 4,
  "stable_like": 1
}
```
> Warning / 警告：dynamic universe 的 symbol master 来自当前 Binance exchangeInfo；历史上曾交易但今天已退市的币不会进入 master list，因此仍有退市幸存者偏差。
> Runtime / 耗时提示：第一次完整运行需要缓存大量 1h/4h/1d K 线，可能很慢；缓存命中后后续回测会明显加快。

## 核心指标

| Metric（指标） | Value（数值） |
|---|---:|
| Trades（计划总数） | 120 |
| Closed trades（已结束交易） | 56 |
| Open trades（仍开放持仓） | 2 |
| Win rate（胜率） | 23.21% |
| Profit factor（盈利因子） | 0.75 |
| Avg R（平均R倍数） | -0.18 |
| Net return（净收益率） | -10.31% |
| Max drawdown（最大回撤） | 2,839.95 / 24.92% |
| Intrabar max drawdown（K线内最大回撤） | 2,780.03 / 24.55% |
| TP1 touched rate（第一止盈触达率） | 33.93% |
| TP2 close rate（第二止盈平仓率） | 23.21% |
| Stop rate（止损率） | 76.79% |
| Fee drag（手续费拖累） | 91.82 USDT |
| Tail max single loss（最大单笔亏损） | -116.67 USDT |
| CAGR（年化复合收益率） | -10.31% |
| Sharpe（夏普比率） | -0.48 |
| Sortino（索提诺比率） | -0.55 |
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
| Equal-weight symbols（等权持有本次币种） | -57.77% |

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
| `ARBUSDT` | CLOSED（已按TP2平仓） | 2025-06-30T16:00:00+00:00 | 0.34 | 0.45 | 2,104.91 | 239.11 | 238.44 | 2.53 | 0.67 | TP2 hit; paper trade closed. |
| `ADAUSDT` | CLOSED（已按TP2平仓） | 2025-07-03T08:00:00+00:00 | 0.60 | 0.80 | 1,315.43 | 263.65 | 262.91 | 2.74 | 0.74 | TP2 hit; paper trade closed. |
| `BONKUSDT` | CLOSED（已按TP2平仓） | 2025-07-08T20:00:00+00:00 | 0.00 | 0.00 | 21,820,182.61 | 262.77 | 262.28 | 2.67 | 0.49 | TP2 hit; paper trade closed. |
| `AAVEUSDT` | STOPPED（已止损） | 2025-07-10T04:00:00+00:00 | 296.13 | 273.05 | 4.50 | -103.91 | -105.68 | -1.03 | 1.76 | Stop loss hit. |
| `DOGEUSDT` | CLOSED（已按TP2平仓） | 2025-07-13T16:00:00+00:00 | 0.20 | 0.26 | 4,808.61 | 280.39 | 279.51 | 2.58 | 0.88 | TP2 hit; paper trade closed. |
| `APTUSDT` | STOPPED（已止损） | 2025-07-17T00:00:00+00:00 | 5.16 | 4.71 | 242.13 | -109.23 | -110.87 | -1.03 | 1.64 | Stop loss hit. |
| `ARBUSDT` | STOPPED（已止损） | 2025-07-17T04:00:00+00:00 | 0.43 | 0.38 | 2,323.41 | -110.70 | -111.99 | -1.02 | 1.29 | Stop loss hit. |
| `BONKUSDT` | STOPPED（已止损） | 2025-07-20T12:00:00+00:00 | 0.00 | 0.00 | 39,746,347.79 | -114.90 | -116.67 | -1.03 | 1.77 | Stop loss hit. |
| `BNBUSDT` | STOPPED（已止损） | 2025-07-23T08:00:00+00:00 | 776.34 | 731.66 | 2.50 | -111.50 | -114.11 | -1.04 | 2.60 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-07-27T20:00:00+00:00 | 3,787.59 | 3,516.63 | 0.40 | -107.89 | -109.89 | -1.03 | 2.00 | Stop loss hit. |
| `CAKEUSDT` | STOPPED（已止损） | 2025-07-28T16:00:00+00:00 | 3.00 | 2.57 | 254.06 | -109.50 | -110.46 | -1.01 | 0.96 | Stop loss hit. |
| `CFXUSDT` | STOPPED（已止损） | 2025-07-30T00:00:00+00:00 | 0.21 | 0.18 | 3,534.37 | -103.23 | -104.15 | -1.02 | 0.92 | Stop loss hit. |
| `ENAUSDT` | STOPPED（已止损） | 2025-07-31T00:00:00+00:00 | 0.61 | 0.52 | 1,194.01 | -102.51 | -103.42 | -1.02 | 0.92 | Stop loss hit. |
| `BCHUSDT` | STOPPED（已止损） | 2025-08-08T00:00:00+00:00 | 576.71 | 532.94 | 2.36 | -103.08 | -104.88 | -1.03 | 1.80 | Stop loss hit. |
| `AVAXUSDT` | CLOSED（已按TP2平仓） | 2025-08-08T00:00:00+00:00 | 23.09 | 28.40 | 51.60 | 273.90 | 272.83 | 2.68 | 1.06 | TP2 hit; paper trade closed. |
| `ENAUSDT` | CLOSED（已按TP2平仓） | 2025-08-08T08:00:00+00:00 | 0.63 | 0.83 | 1,305.83 | 260.04 | 259.28 | 2.55 | 0.76 | TP2 hit; paper trade closed. |
| `BONKUSDT` | STOPPED（已止损） | 2025-08-10T04:00:00+00:00 | 0.00 | 0.00 | 24,341,169.93 | -105.52 | -106.38 | -1.01 | 0.85 | Stop loss hit. |
| `ETHFIUSDT` | STOPPED（已止损） | 2025-08-12T20:00:00+00:00 | 1.24 | 1.13 | 897.31 | -103.76 | -105.22 | -1.02 | 1.46 | Stop loss hit. |
| `ENAUSDT` | STOPPED（已止损） | 2025-08-15T08:00:00+00:00 | 0.74 | 0.67 | 1,405.75 | -103.62 | -104.98 | -1.02 | 1.35 | Stop loss hit. |
| `ADAUSDT` | STOPPED（已止损） | 2025-08-15T20:00:00+00:00 | 0.93 | 0.82 | 901.40 | -101.75 | -102.82 | -1.02 | 1.08 | Stop loss hit. |
| `BNBUSDT` | CLOSED（已按TP2平仓） | 2025-08-23T04:00:00+00:00 | 871.49 | 1,045.94 | 1.55 | 271.07 | 269.87 | 2.68 | 1.19 | TP2 hit; paper trade closed. |
| `ETHUSDT` | STOPPED（已止损） | 2025-09-05T08:00:00+00:00 | 4,432.76 | 4,189.79 | 0.41 | -99.69 | -102.13 | -1.04 | 2.45 | Stop loss hit. |
| `AVAXUSDT` | CLOSED（已按TP2平仓） | 2025-09-16T00:00:00+00:00 | 29.85 | 34.86 | 49.41 | 247.74 | 246.46 | 2.43 | 1.28 | TP2 hit; paper trade closed. |
| `DOGEUSDT` | STOPPED（已止损） | 2025-09-16T16:00:00+00:00 | 0.27 | 0.25 | 7,592.06 | -104.23 | -106.96 | -1.05 | 2.73 | Stop loss hit. |
| `BONKUSDT` | STOPPED（已止损） | 2025-09-18T08:00:00+00:00 | 0.00 | 0.00 | 39,593,489.27 | -106.57 | -107.84 | -1.02 | 1.27 | Stop loss hit. |
| `BIOUSDT` | STOPPED（已止损） | 2025-09-21T00:00:00+00:00 | 0.18 | 0.16 | 4,637.06 | -105.68 | -106.76 | -1.02 | 1.08 | Stop loss hit. |
| `BNBUSDT` | STOPPED（已止损） | 2025-09-21T12:00:00+00:00 | 1,025.08 | 958.33 | 1.53 | -101.85 | -103.94 | -1.04 | 2.09 | Stop loss hit. |
| `CAKEUSDT` | STOPPED（已止损） | 2025-09-21T12:00:00+00:00 | 2.89 | 2.59 | 344.83 | -102.48 | -103.77 | -1.02 | 1.29 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-10-01T12:00:00+00:00 | 4,306.31 | 3,902.60 | 0.25 | -100.14 | -101.53 | -1.02 | 1.40 | Stop loss hit. |
| `ADAUSDT` | STOPPED（已止损） | 2025-10-02T00:00:00+00:00 | 0.85 | 0.77 | 1,270.76 | -101.05 | -102.45 | -1.02 | 1.40 | Stop loss hit. |
| `DOGEUSDT` | STOPPED（已止损） | 2025-10-02T00:00:00+00:00 | 0.25 | 0.22 | 4,131.58 | -100.37 | -101.70 | -1.02 | 1.33 | Stop loss hit. |
| `AVAXUSDT` | STOPPED（已止损） | 2025-10-02T20:00:00+00:00 | 30.78 | 28.35 | 41.90 | -101.95 | -103.65 | -1.03 | 1.70 | Stop loss hit. |
| `APTUSDT` | STOPPED（已止损） | 2025-10-05T20:00:00+00:00 | 5.38 | 4.99 | 256.81 | -100.27 | -102.11 | -1.03 | 1.83 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-10-26T16:00:00+00:00 | 4,060.46 | 3,757.68 | 0.31 | -94.93 | -96.62 | -1.03 | 1.69 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-11-27T16:00:00+00:00 | 2,996.52 | 2,797.38 | 0.46 | -92.35 | -94.21 | -1.03 | 1.85 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-11-30T04:00:00+00:00 | 91,152.21 | 88,714.33 | 0.04 | -95.67 | -100.58 | -1.09 | 4.91 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-12-03T08:00:00+00:00 | 93,325.63 | 82,482.85 | 0.01 | -89.48 | -90.47 | -1.02 | 0.99 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-12-07T20:00:00+00:00 | 3,107.08 | 2,861.04 | 0.36 | -89.78 | -91.28 | -1.03 | 1.50 | Stop loss hit. |
| `ETHUSDT` | CLOSED（已按TP2平仓） | 2025-12-31T00:00:00+00:00 | 2,984.10 | 3,318.38 | 0.75 | 250.95 | 249.06 | 2.82 | 1.89 | TP2 hit; paper trade closed. |
| `ETHUSDT` | STOPPED（已止损） | 2026-01-17T16:00:00+00:00 | 3,319.13 | 3,201.01 | 0.80 | -94.02 | -97.63 | -1.07 | 3.60 | Stop loss hit. |
| `BNBUSDT` | STOPPED（已止损） | 2026-01-18T00:00:00+00:00 | 944.78 | 908.92 | 2.61 | -93.72 | -97.08 | -1.06 | 3.36 | Stop loss hit. |
| `DASHUSDT` | STOPPED（已止损） | 2026-01-18T12:00:00+00:00 | 80.43 | 70.28 | 9.00 | -91.37 | -92.29 | -1.02 | 0.92 | Stop loss hit. |
| `BNBUSDT` | CLOSED（已按TP2平仓） | 2026-04-16T00:00:00+00:00 | 618.86 | 718.19 | 2.48 | 246.61 | 245.29 | 2.73 | 1.33 | TP2 hit; paper trade closed. |
| `DOGEUSDT` | CLOSED（已按TP2平仓） | 2026-04-16T00:00:00+00:00 | 0.09 | 0.11 | 16,219.08 | 227.82 | 226.50 | 2.53 | 1.32 | TP2 hit; paper trade closed. |
| `ADAUSDT` | STOPPED（已止损） | 2026-04-17T00:00:00+00:00 | 0.25 | 0.23 | 4,505.48 | -90.81 | -92.32 | -1.03 | 1.51 | Stop loss hit. |
| `DOGEUSDT` | STOPPED（已止损） | 2026-05-02T00:00:00+00:00 | 0.11 | 0.10 | 9,109.48 | -92.04 | -93.32 | -1.02 | 1.28 | Stop loss hit. |

## 回测结束仍开放

| Symbol（交易对） | Status（状态） | Entry（入场价） | Qty（数量） | Unrealized Handling（未实现盈亏处理） | Notes（备注） |
|---|---|---:|---:|---|---|
| `ETHUSDT` | TP1_HIT（第一止盈已触达） | 1,990.26 | 0.48 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |
| `BTCUSDT` | TP1_HIT（第一止盈已触达） | 69,208.02 | 0.01 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |

## 未入场/过期计划

| Symbol（交易对） | Status（状态） | Created（创建时间） | Entry Zone（入场区间） | Score（评分） | Notes（备注） |
|---|---|---|---:|---:|---|
| `DOGEUSDT` | INVALIDATED（未入场前失效） | 2025-06-11T00:00:00+00:00 | 0.20 - 0.20 | 54.27 | Plan invalidated before entry: current price is below stop loss. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-01T00:00:00+00:00 | 652.84 - 653.99 | 57.15 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-04T04:00:00+00:00 | 659.14 - 661.18 | 57.11 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-07-04T16:00:00+00:00 | 0.00 - 0.00 | 71.04 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-07T08:00:00+00:00 | 659.71 - 660.49 | 56.33 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-10T12:00:00+00:00 | 665.56 - 666.92 | 59.24 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-07-13T08:00:00+00:00 | 2,901.59 - 2,932.21 | 68.11 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-13T16:00:00+00:00 | 686.16 - 689.46 | 57.50 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-07-14T00:00:00+00:00 | 20.77 - 21.13 | 66.99 | Backtest WATCHING plan expired before entry. |
| `ENAUSDT` | EXPIRED（观察计划过期） | 2025-07-15T16:00:00+00:00 | 0.34 - 0.35 | 70.16 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-07-16T12:00:00+00:00 | 3,041.39 - 3,079.50 | 79.73 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-16T20:00:00+00:00 | 692.57 - 697.70 | 66.79 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-07-17T04:00:00+00:00 | 21.75 - 22.21 | 68.54 | Backtest WATCHING plan expired before entry. |
| `ETHFIUSDT` | EXPIRED（观察计划过期） | 2025-07-18T12:00:00+00:00 | 1.28 - 1.32 | 71.95 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-07-18T16:00:00+00:00 | 0.79 - 0.82 | 76.32 | Backtest WATCHING plan expired before entry. |
| `ENAUSDT` | EXPIRED（观察计划过期） | 2025-07-19T00:00:00+00:00 | 0.38 - 0.39 | 74.86 | Backtest WATCHING plan expired before entry. |
| `CRVUSDT` | EXPIRED（观察计划过期） | 2025-07-19T16:00:00+00:00 | 0.93 - 0.96 | 71.91 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-07-19T20:00:00+00:00 | 3,472.71 - 3,527.19 | 71.70 | Backtest WATCHING plan expired before entry. |
| `FETUSDT` | EXPIRED（观察计划过期） | 2025-07-19T20:00:00+00:00 | 0.77 - 0.79 | 65.49 | Backtest WATCHING plan expired before entry. |
| `DOTUSDT` | EXPIRED（观察计划过期） | 2025-07-19T20:00:00+00:00 | 4.25 - 4.35 | 63.66 | Backtest WATCHING plan expired before entry. |
| `BCHUSDT` | EXPIRED（观察计划过期） | 2025-07-19T20:00:00+00:00 | 509.15 - 516.54 | 60.29 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-20T00:00:00+00:00 | 726.59 - 735.19 | 59.00 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-07-21T00:00:00+00:00 | 24.24 - 24.66 | 71.70 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | INVALIDATED（未入场前失效） | 2025-07-21T20:00:00+00:00 | 0.86 - 0.87 | 76.27 | Plan invalidated before entry: current price is below stop loss. |
| `FLOKIUSDT` | INVALIDATED（未入场前失效） | 2025-07-22T04:00:00+00:00 | 0.00 - 0.00 | 76.73 | Plan invalidated before entry: current price is below stop loss. |
| `CRVUSDT` | EXPIRED（观察计划过期） | 2025-07-23T00:00:00+00:00 | 0.96 - 0.99 | 63.77 | Backtest WATCHING plan expired before entry. |
| `DOTUSDT` | INVALIDATED（未入场前失效） | 2025-07-23T00:00:00+00:00 | 4.44 - 4.53 | 63.59 | Plan invalidated before entry: current price is below stop loss. |
| `CFXUSDT` | EXPIRED（观察计划过期） | 2025-07-24T08:00:00+00:00 | 0.18 - 0.18 | 57.69 | Backtest WATCHING plan expired before entry. |
| `ENAUSDT` | EXPIRED（观察计划过期） | 2025-07-24T12:00:00+00:00 | 0.48 - 0.48 | 62.68 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-07-24T16:00:00+00:00 | 3,675.13 - 3,734.05 | 66.35 | Backtest WATCHING plan expired before entry. |
| `BCHUSDT` | EXPIRED（观察计划过期） | 2025-07-25T00:00:00+00:00 | 510.37 - 514.54 | 36.35 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-07-26T00:00:00+00:00 | 24.02 - 24.08 | 46.51 | Backtest WATCHING plan expired before entry. |
| `CRVUSDT` | EXPIRED（观察计划过期） | 2025-07-26T04:00:00+00:00 | 1.00 - 1.03 | 68.04 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-07-26T16:00:00+00:00 | 0.82 - 0.84 | 63.08 | Backtest WATCHING plan expired before entry. |
| `CRVUSDT` | INVALIDATED（未入场前失效） | 2025-07-29T08:00:00+00:00 | 1.02 - 1.03 | 50.75 | Plan invalidated before entry: current price is below stop loss. |
| `CRVUSDT` | INVALIDATED（未入场前失效） | 2025-07-30T16:00:00+00:00 | 1.01 - 1.02 | 60.26 | Plan invalidated before entry: current price is below stop loss. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-08-08T08:00:00+00:00 | 773.64 - 778.88 | 60.60 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-08-08T16:00:00+00:00 | 0.76 - 0.77 | 65.29 | Backtest WATCHING plan expired before entry. |
| `CRVUSDT` | EXPIRED（观察计划过期） | 2025-08-09T00:00:00+00:00 | 0.93 - 0.95 | 54.65 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-08-10T08:00:00+00:00 | 4,043.50 - 4,095.99 | 74.86 | Backtest WATCHING plan expired before entry. |
| `DOGEUSDT` | EXPIRED（观察计划过期） | 2025-08-11T08:00:00+00:00 | 0.23 - 0.23 | 67.47 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-08-11T16:00:00+00:00 | 801.89 - 809.22 | 62.06 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-08-12T16:00:00+00:00 | 0.79 - 0.81 | 65.38 | Backtest WATCHING plan expired before entry. |
| `CRVUSDT` | INVALIDATED（未入场前失效） | 2025-08-12T16:00:00+00:00 | 0.96 - 0.98 | 61.02 | Plan invalidated before entry: current price is below stop loss. |
| `ENAUSDT` | INVALIDATED（未入场前失效） | 2025-08-13T12:00:00+00:00 | 0.78 - 0.80 | 72.65 | Plan invalidated before entry: current price is below stop loss. |
| `APTUSDT` | EXPIRED（观察计划过期） | 2025-08-14T08:00:00+00:00 | 4.85 - 4.94 | 69.05 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | INVALIDATED（未入场前失效） | 2025-08-17T04:00:00+00:00 | 4,376.86 - 4,430.92 | 37.85 | Plan invalidated before entry: current price is below stop loss. |
| `DOTUSDT` | EXPIRED（观察计划过期） | 2025-08-23T04:00:00+00:00 | 3.95 - 4.01 | 58.40 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-08-24T12:00:00+00:00 | 4,618.70 - 4,688.98 | 62.65 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-08-27T16:00:00+00:00 | 4,587.70 - 4,652.44 | 68.89 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-09-17T08:00:00+00:00 | 0.88 - 0.88 | 50.38 | Backtest WATCHING plan expired before entry. |
| `ARBUSDT` | EXPIRED（观察计划过期） | 2025-09-18T00:00:00+00:00 | 0.51 - 0.52 | 46.78 | Backtest WATCHING plan expired before entry. |
| `BCHUSDT` | EXPIRED（观察计划过期） | 2025-09-19T00:00:00+00:00 | 616.88 - 624.29 | 67.37 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-10-02T00:00:00+00:00 | 1,011.09 - 1,019.11 | 63.44 | Backtest WATCHING plan expired before entry. |
| `ENAUSDT` | EXPIRED（观察计划过期） | 2025-10-03T04:00:00+00:00 | 0.60 - 0.61 | 55.01 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-10-05T12:00:00+00:00 | 1,131.18 - 1,149.27 | 72.89 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | INVALIDATED（未入场前失效） | 2025-10-07T00:00:00+00:00 | 0.00 - 0.00 | 62.93 | Plan invalidated before entry: current price is below stop loss. |
| `FORMUSDT` | INVALIDATED（未入场前失效） | 2025-10-08T08:00:00+00:00 | 1.41 - 1.46 | 75.54 | Plan invalidated before entry: current price is below stop loss. |
| `BNBUSDT` | INVALIDATED（未入场前失效） | 2025-10-08T16:00:00+00:00 | 1,249.87 - 1,275.74 | 83.10 | Plan invalidated before entry: current price is below stop loss. |
| `FLOKIUSDT` | INVALIDATED（未入场前失效） | 2025-10-08T20:00:00+00:00 | 0.00 - 0.00 | 54.13 | Plan invalidated before entry: current price is below stop loss. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2026-01-14T12:00:00+00:00 | 3,202.86 - 3,234.96 | 72.24 | Backtest WATCHING plan expired before entry. |
| `AVNTUSDT` | EXPIRED（观察计划过期） | 2026-04-18T12:00:00+00:00 | 0.14 - 0.14 | 53.00 | Backtest WATCHING plan expired before entry. |

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
    "created_at_utc": "2026-06-09T06:06:30+00:00",
    "refresh_frequency": "daily",
    "max_symbols": 40,
    "master_count": 150,
    "source_limit": 150,
    "source_limit_applied": true,
    "universe_refresh_count": 366,
    "selected_count_min": 2,
    "selected_count_avg": 7.1502732240437155,
    "selected_count_max": 24,
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
        "symbol": "BNBUSDT",
        "days_selected": 344
      },
      {
        "symbol": "DOGEUSDT",
        "days_selected": 331
      },
      {
        "symbol": "ADAUSDT",
        "days_selected": 193
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
        "symbol": "ASTERUSDT",
        "days_selected": 80
      },
      {
        "symbol": "BONKUSDT",
        "days_selected": 57
      },
      {
        "symbol": "AAVEUSDT",
        "days_selected": 51
      },
      {
        "symbol": "BCHUSDT",
        "days_selected": 49
      },
      {
        "symbol": "ARBUSDT",
        "days_selected": 46
      },
      {
        "symbol": "DASHUSDT",
        "days_selected": 35
      },
      {
        "symbol": "APTUSDT",
        "days_selected": 25
      },
      {
        "symbol": "AVNTUSDT",
        "days_selected": 24
      },
      {
        "symbol": "CRVUSDT",
        "days_selected": 22
      },
      {
        "symbol": "BIOUSDT",
        "days_selected": 21
      },
      {
        "symbol": "CAKEUSDT",
        "days_selected": 18
      },
      {
        "symbol": "CHIPUSDT",
        "days_selected": 18
      },
      {
        "symbol": "FILUSDT",
        "days_selected": 16
      }
    ],
    "filter_counts": {
      "missing_1h": 3908,
      "insufficient_24h": 24,
      "reconstruct_error": 0,
      "low_quote_volume": 48346,
      "low_trades": 4,
      "stable_like": 1
    },
    "selection_by_day": [
      {
        "date_utc": "2025-06-01",
        "decision_time_utc": "2025-06-01T04:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "ADAUSDT",
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
        "date_utc": "2025-06-02",
        "decision_time_utc": "2025-06-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT"
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
        "date_utc": "2025-06-03",
        "decision_time_utc": "2025-06-03T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "AUSDT"
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
        "date_utc": "2025-06-04",
        "decision_time_utc": "2025-06-04T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
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
        "date_utc": "2025-06-05",
        "decision_time_utc": "2025-06-05T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ENAUSDT",
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
          "AAVEUSDT"
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
        "date_utc": "2025-06-07",
        "decision_time_utc": "2025-06-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "ENAUSDT",
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
        "date_utc": "2025-06-08",
        "decision_time_utc": "2025-06-08T00:00:00+00:00",
        "selected_symbols": [
          "ANIMEUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BTCUSDT",
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
        "date_utc": "2025-06-09",
        "decision_time_utc": "2025-06-09T00:00:00+00:00",
        "selected_symbols": [
          "ANIMEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 122,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-10",
        "decision_time_utc": "2025-06-10T00:00:00+00:00",
        "selected_symbols": [
          "ANIMEUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
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
        "date_utc": "2025-06-11",
        "decision_time_utc": "2025-06-11T00:00:00+00:00",
        "selected_symbols": [
          "AXLUSDT",
          "COMPUSDT",
          "AAVEUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "ADAUSDT",
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
        "date_utc": "2025-06-12",
        "decision_time_utc": "2025-06-12T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ANIMEUSDT"
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
          "AVAXUSDT"
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
        "date_utc": "2025-06-14",
        "decision_time_utc": "2025-06-14T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AVAXUSDT"
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
        "date_utc": "2025-06-15",
        "decision_time_utc": "2025-06-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 122,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-16",
        "decision_time_utc": "2025-06-16T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 122,
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
          "AAVEUSDT",
          "ADAUSDT",
          "ALTUSDT"
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
        "date_utc": "2025-06-18",
        "decision_time_utc": "2025-06-18T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "ENAUSDT"
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
        "date_utc": "2025-06-19",
        "decision_time_utc": "2025-06-19T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT"
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
        "date_utc": "2025-06-20",
        "decision_time_utc": "2025-06-20T00:00:00+00:00",
        "selected_symbols": [
          "BCHUSDT",
          "BTCUSDT",
          "ETHUSDT",
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
        "date_utc": "2025-06-21",
        "decision_time_utc": "2025-06-21T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT"
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
        "date_utc": "2025-06-22",
        "decision_time_utc": "2025-06-22T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT"
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
        "date_utc": "2025-06-24",
        "decision_time_utc": "2025-06-24T00:00:00+00:00",
        "selected_symbols": [
          "AAVEUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
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
        "date_utc": "2025-06-25",
        "decision_time_utc": "2025-06-25T00:00:00+00:00",
        "selected_symbols": [
          "APTUSDT",
          "BANANAS31USDT",
          "ETHUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "DOGEUSDT",
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
        "date_utc": "2025-06-27",
        "decision_time_utc": "2025-06-27T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BANANAS31USDT"
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
        "date_utc": "2025-06-28",
        "decision_time_utc": "2025-06-28T00:00:00+00:00",
        "selected_symbols": [
          "BANANAS31USDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "APTUSDT"
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
        "date_utc": "2025-06-29",
        "decision_time_utc": "2025-06-29T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 124,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-30",
        "decision_time_utc": "2025-06-30T00:00:00+00:00",
        "selected_symbols": [
          "ARBUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ADAUSDT"
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
        "date_utc": "2025-07-01",
        "decision_time_utc": "2025-07-01T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ARBUSDT",
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
        "date_utc": "2025-07-02",
        "decision_time_utc": "2025-07-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
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
        "date_utc": "2025-07-03",
        "decision_time_utc": "2025-07-03T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "ARBUSDT",
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
        "date_utc": "2025-07-04",
        "decision_time_utc": "2025-07-04T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
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
        "date_utc": "2025-07-05",
        "decision_time_utc": "2025-07-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 122,
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
          "BTCUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 123,
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
          "ETHUSDT",
          "BTCUSDT",
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
        "date_utc": "2025-07-08",
        "decision_time_utc": "2025-07-08T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "BTCUSDT",
          "ETHUSDT",
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
        "date_utc": "2025-07-09",
        "decision_time_utc": "2025-07-09T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BONKUSDT",
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
        "date_utc": "2025-07-10",
        "decision_time_utc": "2025-07-10T00:00:00+00:00",
        "selected_symbols": [
          "BANANAS31USDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "BONKUSDT"
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
        "date_utc": "2025-07-11",
        "decision_time_utc": "2025-07-11T00:00:00+00:00",
        "selected_symbols": [
          "BANANAS31USDT",
          "BONKUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "AAVEUSDT"
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
        "date_utc": "2025-07-12",
        "decision_time_utc": "2025-07-12T00:00:00+00:00",
        "selected_symbols": [
          "1INCHUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "ARBUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ALTUSDT",
          "BANANAS31USDT"
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
        "date_utc": "2025-07-13",
        "decision_time_utc": "2025-07-13T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "BANANAS31USDT"
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
        "date_utc": "2025-07-14",
        "decision_time_utc": "2025-07-14T00:00:00+00:00",
        "selected_symbols": [
          "ALGOUSDT",
          "AUCTIONUSDT",
          "ENAUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "1INCHUSDT",
          "BANANAS31USDT"
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
        "date_utc": "2025-07-15",
        "decision_time_utc": "2025-07-15T00:00:00+00:00",
        "selected_symbols": [
          "ALGOUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "AVAXUSDT"
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
        "date_utc": "2025-07-16",
        "decision_time_utc": "2025-07-16T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "ARBUSDT",
          "ETHUSDT",
          "CRVUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "BNBUSDT"
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
        "date_utc": "2025-07-17",
        "decision_time_utc": "2025-07-17T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "FLOKIUSDT",
          "CRVUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ETHFIUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "APTUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
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
        "date_utc": "2025-07-18",
        "decision_time_utc": "2025-07-18T00:00:00+00:00",
        "selected_symbols": [
          "ALGOUSDT",
          "CRVUSDT",
          "ADAUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "FLOKIUSDT",
          "ETHFIUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 112,
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
          "ARBUSDT",
          "BONKUSDT",
          "ERAUSDT",
          "APTUSDT",
          "CRVUSDT",
          "AVAXUSDT",
          "DOTUSDT",
          "ETHFIUSDT",
          "FETUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 107,
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
          "BNBUSDT",
          "ERAUSDT",
          "CRVUSDT",
          "EPICUSDT"
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
        "date_utc": "2025-07-21",
        "decision_time_utc": "2025-07-21T00:00:00+00:00",
        "selected_symbols": [
          "CFXUSDT",
          "CKBUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ARBUSDT",
          "BTCUSDT",
          "ETHFIUSDT",
          "ERAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ETCUSDT",
          "BONKUSDT",
          "FLOKIUSDT",
          "CRVUSDT",
          "APTUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 109,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-22",
        "decision_time_utc": "2025-07-22T00:00:00+00:00",
        "selected_symbols": [
          "DIAUSDT",
          "FLOKIUSDT",
          "ENAUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "CFXUSDT",
          "ERAUSDT",
          "ARBUSDT",
          "BCHUSDT",
          "AAVEUSDT"
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
        "date_utc": "2025-07-23",
        "decision_time_utc": "2025-07-23T00:00:00+00:00",
        "selected_symbols": [
          "CUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "CRVUSDT",
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
          "DOTUSDT"
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
          "BCHUSDT",
          "FLOKIUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "DOTUSDT"
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
        "date_utc": "2025-07-26",
        "decision_time_utc": "2025-07-26T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "CRVUSDT",
          "BCHUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "ERAUSDT",
          "AVAXUSDT"
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
        "date_utc": "2025-07-27",
        "decision_time_utc": "2025-07-27T00:00:00+00:00",
        "selected_symbols": [
          "CKBUSDT",
          "CRVUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "ERAUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BONKUSDT"
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
        "date_utc": "2025-07-28",
        "decision_time_utc": "2025-07-28T00:00:00+00:00",
        "selected_symbols": [
          "ASRUSDT",
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
          "BONKUSDT",
          "CRVUSDT"
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
        "date_utc": "2025-07-29",
        "decision_time_utc": "2025-07-29T00:00:00+00:00",
        "selected_symbols": [
          "ASRUSDT",
          "BANANAS31USDT",
          "1000CATUSDT",
          "ETHUSDT",
          "BTCUSDT",
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
        "date_utc": "2025-07-30",
        "decision_time_utc": "2025-07-30T00:00:00+00:00",
        "selected_symbols": [
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
          "BANANAS31USDT",
          "CUSDT"
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
        "date_utc": "2025-07-31",
        "decision_time_utc": "2025-07-31T00:00:00+00:00",
        "selected_symbols": [
          "CFXUSDT",
          "ENAUSDT",
          "CRVUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ERAUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "AVAXUSDT"
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
          "AVAXUSDT"
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
          "APTUSDT"
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
        "date_utc": "2025-08-03",
        "decision_time_utc": "2025-08-03T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 121,
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
          "ADAUSDT",
          "BTCUSDT",
          "ETCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 120,
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
          "ADAUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "CRVUSDT",
          "BONKUSDT"
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
          "CRVUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 120,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-07",
        "decision_time_utc": "2025-08-07T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "ENAUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 122,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-08",
        "decision_time_utc": "2025-08-08T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "BCHUSDT",
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
        "date_utc": "2025-08-09",
        "decision_time_utc": "2025-08-09T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "DOGEUSDT",
          "APTUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "CRVUSDT"
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
        "date_utc": "2025-08-10",
        "decision_time_utc": "2025-08-10T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 120,
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
          "ADAUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 120,
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
          "ADAUSDT",
          "BONKUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "CRVUSDT",
          "ETHFIUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 114,
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
          "BCHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "BONKUSDT",
          "CYBERUSDT"
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
        "date_utc": "2025-08-14",
        "decision_time_utc": "2025-08-14T00:00:00+00:00",
        "selected_symbols": [
          "ARBUSDT",
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
          "ENAUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 21,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 114,
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
          "CFXUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 21,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 113,
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
          "ENAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "BONKUSDT"
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
        "date_utc": "2025-08-17",
        "decision_time_utc": "2025-08-17T00:00:00+00:00",
        "selected_symbols": [
          "CTSIUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 21,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 122,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-18",
        "decision_time_utc": "2025-08-18T00:00:00+00:00",
        "selected_symbols": [
          "ARBUSDT",
          "ADAUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 21,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 121,
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
          "BIOUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 21,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 120,
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
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "BIOUSDT"
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
        "date_utc": "2025-08-21",
        "decision_time_utc": "2025-08-21T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "CFXUSDT",
          "ETHUSDT",
          "ARBUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "ENAUSDT"
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
        "date_utc": "2025-08-22",
        "decision_time_utc": "2025-08-22T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "API3USDT",
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 21,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 120,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-23",
        "decision_time_utc": "2025-08-23T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
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
          "DOTUSDT",
          "BNBUSDT",
          "BTCUSDT"
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
          "BIOUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 21,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 118,
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
          "AAVEUSDT",
          "BIOUSDT"
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
          "AAVEUSDT"
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
        "date_utc": "2025-08-27",
        "decision_time_utc": "2025-08-27T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "DOGEUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "ENAUSDT",
          "BIOUSDT"
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
        "date_utc": "2025-08-28",
        "decision_time_utc": "2025-08-28T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "BIOUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "ARBUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 119,
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
          "AVAXUSDT",
          "ADAUSDT",
          "BIOUSDT",
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
          "ARBUSDT"
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
        "date_utc": "2025-08-31",
        "decision_time_utc": "2025-08-31T00:00:00+00:00",
        "selected_symbols": [
          "DOLOUSDT",
          "CFXUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 122,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-01",
        "decision_time_utc": "2025-09-01T00:00:00+00:00",
        "selected_symbols": [
          "DOLOUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "FORMUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 122,
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
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "FILUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "ARBUSDT",
          "BONKUSDT"
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
        "date_utc": "2025-09-03",
        "decision_time_utc": "2025-09-03T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "ADAUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 122,
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
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 122,
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
          "AVAXUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 123,
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
          "ADAUSDT",
          "ARBUSDT",
          "BNBUSDT",
          "AVAXUSDT"
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
        "date_utc": "2025-09-07",
        "decision_time_utc": "2025-09-07T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "BIOUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 123,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-08",
        "decision_time_utc": "2025-09-08T00:00:00+00:00",
        "selected_symbols": [
          "DOGEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 124,
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
          "AVAXUSDT",
          "BNBUSDT",
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
          "ADAUSDT",
          "BNBUSDT",
          "ARBUSDT",
          "BONKUSDT"
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
          "ENAUSDT",
          "ARBUSDT"
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
        "date_utc": "2025-09-12",
        "decision_time_utc": "2025-09-12T00:00:00+00:00",
        "selected_symbols": [
          "ETHFIUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOLOUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "FORMUSDT",
          "ACEUSDT"
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
        "date_utc": "2025-09-13",
        "decision_time_utc": "2025-09-13T00:00:00+00:00",
        "selected_symbols": [
          "DOGEUSDT",
          "ETHUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 122,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-14",
        "decision_time_utc": "2025-09-14T00:00:00+00:00",
        "selected_symbols": [
          "DOGEUSDT",
          "AVAXUSDT",
          "DOTUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "ENAUSDT"
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
        "date_utc": "2025-09-15",
        "decision_time_utc": "2025-09-15T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 123,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-16",
        "decision_time_utc": "2025-09-16T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 19,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 122,
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
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "FORMUSDT",
          "AVNTUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 19,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 122,
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
          "ETHUSDT",
          "BNBUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "AVNTUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 19,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 121,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-19",
        "decision_time_utc": "2025-09-19T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "EIGENUSDT",
          "AVNTUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 18,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 121,
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
          "ARBUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 18,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 122,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-21",
        "decision_time_utc": "2025-09-21T00:00:00+00:00",
        "selected_symbols": [
          "AVNTUSDT",
          "CAKEUSDT",
          "BNBUSDT",
          "BIOUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 18,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 124,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-22",
        "decision_time_utc": "2025-09-22T00:00:00+00:00",
        "selected_symbols": [
          "AVNTUSDT",
          "BARDUSDT",
          "BNBUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 18,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 123,
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
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "DOTUSDT",
          "BONKUSDT",
          "AVNTUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 120,
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
          "ADAUSDT"
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
        "date_utc": "2025-09-25",
        "decision_time_utc": "2025-09-25T00:00:00+00:00",
        "selected_symbols": [
          "AVNTUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "0GUSDT",
          "ENAUSDT",
          "BARDUSDT"
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
        "date_utc": "2025-09-26",
        "decision_time_utc": "2025-09-26T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "ARBUSDT",
          "ETHFIUSDT",
          "AAVEUSDT",
          "0GUSDT",
          "AVNTUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 121,
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
          "ENAUSDT",
          "AVNTUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "0GUSDT"
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
          "1000SATSUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 124,
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
          "AVNTUSDT",
          "BARDUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 125,
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
          "ENAUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 16,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 123,
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
          "BNBUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "FFUSDT",
          "ALPINEUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 123,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-02",
        "decision_time_utc": "2025-10-02T00:00:00+00:00",
        "selected_symbols": [
          "APTUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "FFUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "BARDUSDT",
          "AVNTUSDT",
          "EDENUSDT",
          "ALPINEUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 122,
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
          "ENAUSDT",
          "BNBUSDT",
          "APTUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DASHUSDT",
          "ADAUSDT",
          "BARDUSDT",
          "AVAXUSDT",
          "AVNTUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 122,
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
          "BTCUSDT",
          "ETHUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "2ZUSDT",
          "ENAUSDT",
          "FORMUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 123,
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
          "BNBUSDT",
          "DOGEUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "CAKEUSDT",
          "AVNTUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 126,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-06",
        "decision_time_utc": "2025-10-06T00:00:00+00:00",
        "selected_symbols": [
          "APTUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 128,
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
          "ADAUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "FORMUSDT",
          "APTUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 124,
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
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "ENAUSDT",
          "FLOKIUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 124,
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
          "CAKEUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 126,
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
          "FORMUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 125,
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
          "DASHUSDT",
          "ASTERUSDT",
          "CAKEUSDT",
          "DOGEUSDT",
          "ETCUSDT",
          "ADAUSDT",
          "FFUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "CRVUSDT",
          "ENAUSDT",
          "FETUSDT",
          "BONKUSDT",
          "DOTUSDT",
          "APTUSDT",
          "BNSOLUSDT",
          "FILUSDT",
          "FORMUSDT",
          "ETHFIUSDT"
        ],
        "candidate_count": 24,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 113,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-12",
        "decision_time_utc": "2025-10-12T00:00:00+00:00",
        "selected_symbols": [
          "FFUSDT",
          "BNBUSDT",
          "FETUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ETCUSDT",
          "BTCUSDT",
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
          "FORMUSDT"
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
        "date_utc": "2025-10-13",
        "decision_time_utc": "2025-10-13T00:00:00+00:00",
        "selected_symbols": [
          "FORMUSDT",
          "CAKEUSDT",
          "ASTERUSDT",
          "DASHUSDT",
          "FFUSDT",
          "BNBUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 124,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-14",
        "decision_time_utc": "2025-10-14T00:00:00+00:00",
        "selected_symbols": [
          "FFUSDT",
          "ENAUSDT",
          "FORMUSDT",
          "BONKUSDT",
          "CAKEUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "APTUSDT",
          "FETUSDT",
          "DASHUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 121,
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
          "FFUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 11,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 122,
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
          "ENSOUSDT"
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
          "BELUSDT"
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
          "BCHUSDT"
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
        "date_utc": "2025-10-19",
        "decision_time_utc": "2025-10-19T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 11,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 133,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-20",
        "decision_time_utc": "2025-10-20T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 11,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 132,
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
          "BIOUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ASTERUSDT",
          "ENAUSDT",
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
        "date_utc": "2025-10-22",
        "decision_time_utc": "2025-10-22T00:00:00+00:00",
        "selected_symbols": [
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
          "CAKEUSDT"
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
          "BCHUSDT",
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
          "BNBUSDT"
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
        "date_utc": "2025-10-26",
        "decision_time_utc": "2025-10-26T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 134,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-27",
        "decision_time_utc": "2025-10-27T00:00:00+00:00",
        "selected_symbols": [
          "BCHUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ASTERUSDT"
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
        "date_utc": "2025-10-28",
        "decision_time_utc": "2025-10-28T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "ENSOUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "ENAUSDT",
          "ADAUSDT"
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
          "ADAUSDT",
          "ENAUSDT",
          "ENSOUSDT"
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
          "ENAUSDT"
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
        "date_utc": "2025-11-01",
        "decision_time_utc": "2025-11-01T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 134,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-02",
        "decision_time_utc": "2025-11-02T00:00:00+00:00",
        "selected_symbols": [
          "DASHUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 134,
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
          "DOGEUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 134,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-04",
        "decision_time_utc": "2025-11-04T00:00:00+00:00",
        "selected_symbols": [
          "DASHUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 130,
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
          "DCRUSDT"
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
        "date_utc": "2025-11-06",
        "decision_time_utc": "2025-11-06T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "DASHUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 131,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-07",
        "decision_time_utc": "2025-11-07T00:00:00+00:00",
        "selected_symbols": [
          "FILUSDT",
          "DASHUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "ALCXUSDT"
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
        "date_utc": "2025-11-08",
        "decision_time_utc": "2025-11-08T00:00:00+00:00",
        "selected_symbols": [
          "FILUSDT",
          "FETUSDT",
          "ARUSDT",
          "ETCUSDT",
          "DOTUSDT",
          "APTUSDT",
          "ASTERUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BCHUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "DASHUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 124,
          "low_trades": 0,
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
          "FLUXUSDT"
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
        "date_utc": "2025-11-10",
        "decision_time_utc": "2025-11-10T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "ASTERUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "FETUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "FILUSDT",
          "DASHUSDT"
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
        "date_utc": "2025-11-11",
        "decision_time_utc": "2025-11-11T00:00:00+00:00",
        "selected_symbols": [
          "FUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "FILUSDT",
          "FETUSDT",
          "DASHUSDT"
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
          "CFXUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 9,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 128,
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
          "ALLOUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 9,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 132,
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
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ALLOUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 133,
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
          "DOGEUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "FILUSDT"
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
          "ADAUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 134,
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
          "ENAUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 134,
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
          "BANANAS31USDT"
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
        "date_utc": "2025-11-19",
        "decision_time_utc": "2025-11-19T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
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
        "date_utc": "2025-11-20",
        "decision_time_utc": "2025-11-20T00:00:00+00:00",
        "selected_symbols": [
          "FETUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "DOGEUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 135,
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
          "DASHUSDT"
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
          "ALLOUSDT",
          "DYMUSDT"
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
        "date_utc": "2025-11-23",
        "decision_time_utc": "2025-11-23T00:00:00+00:00",
        "selected_symbols": [
          "BCHUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 136,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-24",
        "decision_time_utc": "2025-11-24T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 137,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-25",
        "decision_time_utc": "2025-11-25T00:00:00+00:00",
        "selected_symbols": [
          "ALLOUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 134,
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
          "BNBUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 136,
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
          "BNBUSDT",
          "BCHUSDT",
          "DOGEUSDT",
          "ALLOUSDT",
          "ASTERUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 131,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-28",
        "decision_time_utc": "2025-11-28T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 137,
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
          "ASTERUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 135,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-30",
        "decision_time_utc": "2025-11-30T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "ASTERUSDT"
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
        "date_utc": "2025-12-01",
        "decision_time_utc": "2025-12-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT"
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
        "date_utc": "2025-12-02",
        "decision_time_utc": "2025-12-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "DOGEUSDT",
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
          "ADAUSDT"
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
        "date_utc": "2025-12-05",
        "decision_time_utc": "2025-12-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
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
        "date_utc": "2025-12-06",
        "decision_time_utc": "2025-12-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
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
        "date_utc": "2025-12-07",
        "decision_time_utc": "2025-12-07T00:00:00+00:00",
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
        "date_utc": "2025-12-08",
        "decision_time_utc": "2025-12-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "ATUSDT"
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
        "date_utc": "2025-12-09",
        "decision_time_utc": "2025-12-09T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "ASTERUSDT",
          "DOGEUSDT",
          "BNBUSDT"
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
        "date_utc": "2025-12-10",
        "decision_time_utc": "2025-12-10T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "BCHUSDT"
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
        "date_utc": "2025-12-12",
        "decision_time_utc": "2025-12-12T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "ATUSDT",
          "AVAXUSDT"
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
        "date_utc": "2025-12-13",
        "decision_time_utc": "2025-12-13T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "ATUSDT",
          "BNBUSDT",
          "DOGEUSDT",
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
          "DOGEUSDT"
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
        "date_utc": "2025-12-16",
        "decision_time_utc": "2025-12-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "ASTERUSDT",
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
        "date_utc": "2025-12-17",
        "decision_time_utc": "2025-12-17T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ETHUSDT",
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
        "date_utc": "2025-12-18",
        "decision_time_utc": "2025-12-18T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
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
          "AVAXUSDT"
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
        "date_utc": "2025-12-20",
        "decision_time_utc": "2025-12-20T00:00:00+00:00",
        "selected_symbols": [
          "BCHUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "ASTERUSDT",
          "BTCUSDT",
          "BNBUSDT"
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
        "date_utc": "2025-12-21",
        "decision_time_utc": "2025-12-21T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 141,
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
        "date_utc": "2025-12-23",
        "decision_time_utc": "2025-12-23T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "AAVEUSDT"
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
        "date_utc": "2025-12-24",
        "decision_time_utc": "2025-12-24T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT"
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
        "date_utc": "2025-12-25",
        "decision_time_utc": "2025-12-25T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
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
        "date_utc": "2025-12-26",
        "decision_time_utc": "2025-12-26T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT"
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
        "date_utc": "2025-12-27",
        "decision_time_utc": "2025-12-27T00:00:00+00:00",
        "selected_symbols": [
          "ATUSDT",
          "ETHUSDT",
          "BTCUSDT",
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
          "BTCUSDT",
          "ETHUSDT",
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
        "date_utc": "2025-12-30",
        "decision_time_utc": "2025-12-30T00:00:00+00:00",
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
        "date_utc": "2025-12-31",
        "decision_time_utc": "2025-12-31T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT"
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
        "date_utc": "2026-01-01",
        "decision_time_utc": "2026-01-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "BROCCOLI714USDT"
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
        "date_utc": "2026-01-02",
        "decision_time_utc": "2026-01-02T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "DOGEUSDT",
          "BROCCOLI714USDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
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
        "date_utc": "2026-01-03",
        "decision_time_utc": "2026-01-03T00:00:00+00:00",
        "selected_symbols": [
          "DOGEUSDT",
          "ADAUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT"
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
        "date_utc": "2026-01-04",
        "decision_time_utc": "2026-01-04T00:00:00+00:00",
        "selected_symbols": [
          "BCHUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT"
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
        "date_utc": "2026-01-05",
        "decision_time_utc": "2026-01-05T00:00:00+00:00",
        "selected_symbols": [
          "BROCCOLI714USDT",
          "BONKUSDT",
          "DOGEUSDT",
          "ASTERUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "BCHUSDT"
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
        "date_utc": "2026-01-06",
        "decision_time_utc": "2026-01-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "BCHUSDT",
          "ASTERUSDT",
          "BROCCOLI714USDT"
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
        "date_utc": "2026-01-07",
        "decision_time_utc": "2026-01-07T00:00:00+00:00",
        "selected_symbols": [
          "BROCCOLI714USDT",
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "ASTERUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 134,
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
        "date_utc": "2026-01-09",
        "decision_time_utc": "2026-01-09T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT"
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
        "date_utc": "2026-01-10",
        "decision_time_utc": "2026-01-10T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
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
        "date_utc": "2026-01-11",
        "decision_time_utc": "2026-01-11T00:00:00+00:00",
        "selected_symbols": [
          "BNBUSDT",
          "BTCUSDT",
          "ETHUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 141,
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
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "BCHUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 138,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-14",
        "decision_time_utc": "2026-01-14T00:00:00+00:00",
        "selected_symbols": [
          "DASHUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "BREVUSDT",
          "BCHUSDT"
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
        "date_utc": "2026-01-15",
        "decision_time_utc": "2026-01-15T00:00:00+00:00",
        "selected_symbols": [
          "DASHUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "BCHUSDT",
          "ENAUSDT",
          "ADAUSDT"
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
        "date_utc": "2026-01-16",
        "decision_time_utc": "2026-01-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DASHUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 2,
          "reconstruct_error": 0,
          "low_quote_volume": 137,
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
          "FOGOUSDT"
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
        "date_utc": "2026-01-18",
        "decision_time_utc": "2026-01-18T00:00:00+00:00",
        "selected_symbols": [
          "AXSUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BREVUSDT",
          "BNBUSDT",
          "DASHUSDT"
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
        "date_utc": "2026-01-19",
        "decision_time_utc": "2026-01-19T00:00:00+00:00",
        "selected_symbols": [
          "DASHUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
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
        "date_utc": "2026-01-20",
        "decision_time_utc": "2026-01-20T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "BREVUSDT",
          "ADAUSDT",
          "DASHUSDT",
          "ASTERUSDT",
          "DUSKUSDT"
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
        "date_utc": "2026-01-21",
        "decision_time_utc": "2026-01-21T00:00:00+00:00",
        "selected_symbols": [
          "AXSUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BREVUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "DASHUSDT",
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
        "date_utc": "2026-01-22",
        "decision_time_utc": "2026-01-22T00:00:00+00:00",
        "selected_symbols": [
          "AXSUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "BNBUSDT"
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
        "date_utc": "2026-01-25",
        "decision_time_utc": "2026-01-25T00:00:00+00:00",
        "selected_symbols": [
          "ENSOUSDT",
          "FOGOUSDT",
          "BTCUSDT",
          "ETHUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-26",
        "decision_time_utc": "2026-01-26T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "FOGOUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ENSOUSDT"
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
        "date_utc": "2026-01-27",
        "decision_time_utc": "2026-01-27T00:00:00+00:00",
        "selected_symbols": [
          "AXSUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "FOGOUSDT",
          "DOGEUSDT",
          "BNBUSDT"
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
        "date_utc": "2026-01-28",
        "decision_time_utc": "2026-01-28T00:00:00+00:00",
        "selected_symbols": [
          "FOGOUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT"
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
        "date_utc": "2026-01-29",
        "decision_time_utc": "2026-01-29T00:00:00+00:00",
        "selected_symbols": [
          "FOGOUSDT",
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
        "date_utc": "2026-01-30",
        "decision_time_utc": "2026-01-30T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "FOGOUSDT",
          "BNBUSDT",
          "DOGEUSDT",
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
        "date_utc": "2026-01-31",
        "decision_time_utc": "2026-01-31T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT"
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
        "date_utc": "2026-02-02",
        "decision_time_utc": "2026-02-02T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT"
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
        "date_utc": "2026-02-03",
        "decision_time_utc": "2026-02-03T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "BNBUSDT"
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
        "date_utc": "2026-02-04",
        "decision_time_utc": "2026-02-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT"
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
        "date_utc": "2026-02-05",
        "decision_time_utc": "2026-02-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
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
          "AAVEUSDT"
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
        "date_utc": "2026-02-07",
        "decision_time_utc": "2026-02-07T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "BNBUSDT"
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
        "date_utc": "2026-02-08",
        "decision_time_utc": "2026-02-08T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT"
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
          "DOGEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
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
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 142,
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
        "date_utc": "2026-02-15",
        "decision_time_utc": "2026-02-15T00:00:00+00:00",
        "selected_symbols": [
          "DOGEUSDT",
          "BTCUSDT",
          "ETHUSDT",
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
        "date_utc": "2026-02-16",
        "decision_time_utc": "2026-02-16T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
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
        "date_utc": "2026-02-17",
        "decision_time_utc": "2026-02-17T00:00:00+00:00",
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
        "date_utc": "2026-02-22",
        "decision_time_utc": "2026-02-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 144,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-23",
        "decision_time_utc": "2026-02-23T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 145,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-24",
        "decision_time_utc": "2026-02-24T00:00:00+00:00",
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
        "date_utc": "2026-02-25",
        "decision_time_utc": "2026-02-25T00:00:00+00:00",
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
        "date_utc": "2026-02-26",
        "decision_time_utc": "2026-02-26T00:00:00+00:00",
        "selected_symbols": [
          "DOTUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ENSOUSDT"
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
        "date_utc": "2026-02-27",
        "decision_time_utc": "2026-02-27T00:00:00+00:00",
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
        "date_utc": "2026-02-28",
        "decision_time_utc": "2026-02-28T00:00:00+00:00",
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
        "date_utc": "2026-03-01",
        "decision_time_utc": "2026-03-01T00:00:00+00:00",
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
        "date_utc": "2026-03-02",
        "decision_time_utc": "2026-03-02T00:00:00+00:00",
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
        "date_utc": "2026-03-03",
        "decision_time_utc": "2026-03-03T00:00:00+00:00",
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
          "ENSOUSDT"
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
        "date_utc": "2026-03-06",
        "decision_time_utc": "2026-03-06T00:00:00+00:00",
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
        "date_utc": "2026-03-07",
        "decision_time_utc": "2026-03-07T00:00:00+00:00",
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
        "date_utc": "2026-03-08",
        "decision_time_utc": "2026-03-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 145,
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
        "date_utc": "2026-03-11",
        "decision_time_utc": "2026-03-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "ADAUSDT",
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
        "date_utc": "2026-03-12",
        "decision_time_utc": "2026-03-12T00:00:00+00:00",
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
        "date_utc": "2026-03-15",
        "decision_time_utc": "2026-03-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 144,
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
          "ETHUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 141,
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
        "date_utc": "2026-03-19",
        "decision_time_utc": "2026-03-19T00:00:00+00:00",
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
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 145,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-22",
        "decision_time_utc": "2026-03-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 146,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-23",
        "decision_time_utc": "2026-03-23T00:00:00+00:00",
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
        "date_utc": "2026-03-26",
        "decision_time_utc": "2026-03-26T00:00:00+00:00",
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
        "date_utc": "2026-03-27",
        "decision_time_utc": "2026-03-27T00:00:00+00:00",
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
        "date_utc": "2026-03-28",
        "decision_time_utc": "2026-03-28T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "CFGUSDT",
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
        "date_utc": "2026-03-29",
        "decision_time_utc": "2026-03-29T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 145,
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
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 145,
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
        "date_utc": "2026-04-02",
        "decision_time_utc": "2026-04-02T00:00:00+00:00",
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
        "date_utc": "2026-04-03",
        "decision_time_utc": "2026-04-03T00:00:00+00:00",
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
        "date_utc": "2026-04-04",
        "decision_time_utc": "2026-04-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 146,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-05",
        "decision_time_utc": "2026-04-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 146,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-06",
        "decision_time_utc": "2026-04-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 146,
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
        "date_utc": "2026-04-08",
        "decision_time_utc": "2026-04-08T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "AVAXUSDT",
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
        "date_utc": "2026-04-09",
        "decision_time_utc": "2026-04-09T00:00:00+00:00",
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
        "date_utc": "2026-04-10",
        "decision_time_utc": "2026-04-10T00:00:00+00:00",
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
        "date_utc": "2026-04-11",
        "decision_time_utc": "2026-04-11T00:00:00+00:00",
        "selected_symbols": [
          "DASHUSDT",
          "ETHUSDT",
          "BTCUSDT",
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
        "date_utc": "2026-04-12",
        "decision_time_utc": "2026-04-12T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 145,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-13",
        "decision_time_utc": "2026-04-13T00:00:00+00:00",
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
        "date_utc": "2026-04-14",
        "decision_time_utc": "2026-04-14T00:00:00+00:00",
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
        "date_utc": "2026-04-15",
        "decision_time_utc": "2026-04-15T00:00:00+00:00",
        "selected_symbols": [
          "ENJUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "BARDUSDT"
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
        "date_utc": "2026-04-16",
        "decision_time_utc": "2026-04-16T00:00:00+00:00",
        "selected_symbols": [
          "ENJUSDT",
          "BARDUSDT",
          "ETHUSDT",
          "BTCUSDT",
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
        "date_utc": "2026-04-17",
        "decision_time_utc": "2026-04-17T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "BARDUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "ENJUSDT"
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
        "date_utc": "2026-04-18",
        "decision_time_utc": "2026-04-18T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "AVNTUSDT",
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
        "date_utc": "2026-04-19",
        "decision_time_utc": "2026-04-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "AVNTUSDT",
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
        "date_utc": "2026-04-20",
        "decision_time_utc": "2026-04-20T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "AAVEUSDT",
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
        "date_utc": "2026-04-21",
        "decision_time_utc": "2026-04-21T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "AAVEUSDT"
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
        "date_utc": "2026-04-22",
        "decision_time_utc": "2026-04-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 145,
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
        "date_utc": "2026-04-24",
        "decision_time_utc": "2026-04-24T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "CHIPUSDT"
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
        "date_utc": "2026-04-25",
        "decision_time_utc": "2026-04-25T00:00:00+00:00",
        "selected_symbols": [
          "APEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "CHIPUSDT"
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
        "date_utc": "2026-04-26",
        "decision_time_utc": "2026-04-26T00:00:00+00:00",
        "selected_symbols": [
          "AXSUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "CHIPUSDT",
          "APEUSDT"
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
        "date_utc": "2026-04-27",
        "decision_time_utc": "2026-04-27T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "CHIPUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 145,
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
          "BTCUSDT",
          "ETHUSDT",
          "CHIPUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 145,
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
        "date_utc": "2026-05-01",
        "decision_time_utc": "2026-05-01T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "CHIPUSDT"
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
          "DOGEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 145,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-04",
        "decision_time_utc": "2026-05-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "CHIPUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 146,
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
        "date_utc": "2026-05-06",
        "decision_time_utc": "2026-05-06T00:00:00+00:00",
        "selected_symbols": [
          "DOGSUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "ETHUSDT",
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
        "date_utc": "2026-05-07",
        "decision_time_utc": "2026-05-07T00:00:00+00:00",
        "selected_symbols": [
          "FILUSDT",
          "DASHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ETHUSDT",
          "DOGEUSDT"
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
        "date_utc": "2026-05-08",
        "decision_time_utc": "2026-05-08T00:00:00+00:00",
        "selected_symbols": [
          "DOGSUSDT",
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
        "date_utc": "2026-05-09",
        "decision_time_utc": "2026-05-09T00:00:00+00:00",
        "selected_symbols": [
          "CHIPUSDT",
          "FILUSDT",
          "ETHUSDT",
          "BTCUSDT",
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
        "date_utc": "2026-05-10",
        "decision_time_utc": "2026-05-10T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "CHIPUSDT",
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
        "date_utc": "2026-05-11",
        "decision_time_utc": "2026-05-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "CHIPUSDT"
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
          "ETHUSDT",
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
        "date_utc": "2026-05-15",
        "decision_time_utc": "2026-05-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 145,
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
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 147,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-21",
        "decision_time_utc": "2026-05-21T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 147,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-22",
        "decision_time_utc": "2026-05-22T00:00:00+00:00",
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
        "date_utc": "2026-05-23",
        "decision_time_utc": "2026-05-23T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "EDENUSDT"
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
        "date_utc": "2026-05-24",
        "decision_time_utc": "2026-05-24T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
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
        "date_utc": "2026-05-25",
        "decision_time_utc": "2026-05-25T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 148,
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
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 147,
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
        "date_utc": "2026-05-29",
        "decision_time_utc": "2026-05-29T00:00:00+00:00",
        "selected_symbols": [
          "ALLOUSDT",
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
        "date_utc": "2026-05-30",
        "decision_time_utc": "2026-05-30T00:00:00+00:00",
        "selected_symbols": [
          "ALLOUSDT",
          "BTCUSDT",
          "ETHUSDT",
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
        "date_utc": "2026-05-31",
        "decision_time_utc": "2026-05-31T00:00:00+00:00",
        "selected_symbols": [
          "FETUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "ETHUSDT"
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
        "date_utc": "2026-06-01",
        "decision_time_utc": "2026-06-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 147,
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
