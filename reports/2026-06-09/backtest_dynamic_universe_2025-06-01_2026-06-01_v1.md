---
created: 2026-06-09 02:36:48 CST
tags:
  - crypto
  - trading-system
  - backtest
backtest_run_id: 7c5b1099c837
report_version: v1
sample_sufficient: true
universe_mode: true
universe_type: dynamic
---

# 回测报告 2025-06-01 至 2026-06-01 v1

- 回测 ID：`7c5b1099c837`
- 交易对：`0GUSDT`, `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1INCHUSDT`, `2ZUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACHUSDT`, `ADAUSDT`, `AEVOUSDT`, `AIGENSYNUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALCXUSDT`, `ALGOUSDT`, `ALICEUSDT`, `ALLOUSDT`, `ALPINEUSDT`, `ALTUSDT`, `ANIMEUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ASRUSDT`, `ASTERUSDT`, `ATMUSDT`, `ATOMUSDT`, `ATUSDT`, `AUCTIONUSDT`, `AUSDT`, `AVAXUSDT`, `AVNTUSDT`, `AWEUSDT`, `AXLUSDT`, `AXSUSDT`, `BABYUSDT`, `BANANAS31USDT`, `BARDUSDT`, `BATUSDT`, `BBUSDT`, `BCHUSDT`, `BELUSDT`, `BERAUSDT`, `BIOUSDT`, `BMTUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BREVUSDT`, `BROCCOLI714USDT`, `BTCUSDT`, `C98USDT`, `CAKEUSDT`, `CELOUSDT`, `CFGUSDT`, `CFXUSDT`, `CHIPUSDT`, `CHZUSDT`, `CKBUSDT`, `COMPUSDT`, `COSUSDT`, `COTIUSDT`, `COWUSDT`
- UTC 区间：2025-06-01T00:00:00+00:00 -> 2026-06-01T00:00:00+00:00
- 初始权益：10,000.00 USDT
- 最终权益：9,123.21 USDT
- 净收益：-8.77%
- 代码 commit：`04b5bba7fbfa17b6d3ff44c764c1b9f5a4e5b40b`
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
- Master symbols / Master 币种数：100
- Source limit / 调试截断：100
- Source limit applied / 是否截断：true
- Refresh frequency / 刷新频率：daily
- Universe refreshes / Universe 刷新次数：366
- Selected symbols per refresh / 每次入选数量：min=2, avg=6.25, max=18
- Top selected symbols / 最常入选：`BNBUSDT`(366), `BTCUSDT`(366), `ADAUSDT`(288), `AVAXUSDT`(226), `AAVEUSDT`(132), `BCHUSDT`(122), `ASTERUSDT`(111), `ARBUSDT`(103), `BONKUSDT`(97), `APTUSDT`(61)
- Filter counts / 过滤统计：
```json
{
  "missing_1h": 2349,
  "insufficient_24h": 13,
  "reconstruct_error": 0,
  "low_quote_volume": 31934,
  "low_trades": 16,
  "stable_like": 2
}
```
> Warning / 警告：dynamic universe 的 symbol master 来自当前 Binance exchangeInfo；历史上曾交易但今天已退市的币不会进入 master list，因此仍有退市幸存者偏差。
> Runtime / 耗时提示：第一次完整运行需要缓存大量 1h/4h/1d K 线，可能很慢；缓存命中后后续回测会明显加快。

## 核心指标

| Metric（指标） | Value（数值） |
|---|---:|
| Trades（计划总数） | 108 |
| Closed trades（已结束交易） | 36 |
| Open trades（仍开放持仓） | 3 |
| Win rate（胜率） | 22.22% |
| Profit factor（盈利因子） | 0.72 |
| Avg R（平均R倍数） | -0.21 |
| Net return（净收益率） | -8.77% |
| Max drawdown（最大回撤） | 2,171.68 / 19.70% |
| Intrabar max drawdown（K线内最大回撤） | 2,110.81 / 19.31% |
| TP1 touched rate（第一止盈触达率） | 30.56% |
| TP2 close rate（第二止盈平仓率） | 22.22% |
| Stop rate（止损率） | 77.78% |
| Fee drag（手续费拖累） | 64.39 USDT |
| Tail max single loss（最大单笔亏损） | -112.00 USDT |
| CAGR（年化复合收益率） | -8.77% |
| Sharpe（夏普比率） | -0.53 |
| Sortino（索提诺比率） | -0.58 |
| Exposure（持仓暴露时间） | 84.16% |
| Turnover（换手率） | 5.33 |
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
| Equal-weight symbols（等权持有本次币种） | -56.46% |

## 已结束交易

| Symbol（交易对） | Status（状态） | Created（创建时间） | Entry（入场价） | Exit（出场价） | Qty（数量） | Gross PnL（毛盈亏） | Net PnL（净盈亏） | Net R（净R倍数） | Fees（手续费） | Notes（备注） |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| `BTCUSDT` | STOPPED（已止损） | 2025-06-06T16:00:00+00:00 | 105,460.26 | 98,767.81 | 0.02 | -102.32 | -104.47 | -1.04 | 2.15 | Stop loss hit. |
| `AVAXUSDT` | STOPPED（已止损） | 2025-06-10T00:00:00+00:00 | 21.79 | 19.25 | 40.13 | -101.83 | -102.95 | -1.02 | 1.12 | Stop loss hit. |
| `ADAUSDT` | STOPPED（已止损） | 2025-06-10T00:00:00+00:00 | 0.71 | 0.64 | 1,494.04 | -102.12 | -103.49 | -1.02 | 1.38 | Stop loss hit. |
| `BNBUSDT` | STOPPED（已止损） | 2025-06-10T12:00:00+00:00 | 660.52 | 636.16 | 4.29 | -104.57 | -108.43 | -1.06 | 3.86 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-06-24T16:00:00+00:00 | 105,613.24 | 96,630.27 | 0.01 | -97.43 | -98.93 | -1.03 | 1.51 | Stop loss hit. |
| `AAVEUSDT` | CLOSED（已按TP2平仓） | 2025-06-30T08:00:00+00:00 | 269.57 | 322.83 | 4.77 | 254.31 | 253.18 | 2.62 | 1.13 | TP2 hit; paper trade closed. |
| `ARBUSDT` | CLOSED（已按TP2平仓） | 2025-06-30T16:00:00+00:00 | 0.34 | 0.45 | 2,170.72 | 246.58 | 245.89 | 2.53 | 0.69 | TP2 hit; paper trade closed. |
| `BCHUSDT` | STOPPED（已止损） | 2025-07-01T00:00:00+00:00 | 505.13 | 479.22 | 3.81 | -98.82 | -101.42 | -1.05 | 2.60 | Stop loss hit. |
| `AVAXUSDT` | CLOSED（已按TP2平仓） | 2025-07-03T00:00:00+00:00 | 18.57 | 23.93 | 51.73 | 277.07 | 276.19 | 2.83 | 0.88 | TP2 hit; paper trade closed. |
| `BONKUSDT` | CLOSED（已按TP2平仓） | 2025-07-08T20:00:00+00:00 | 0.00 | 0.00 | 21,773,576.00 | 262.21 | 261.72 | 2.67 | 0.49 | TP2 hit; paper trade closed. |
| `ARKUSDT` | STOPPED（已止损） | 2025-07-13T04:00:00+00:00 | 0.46 | 0.37 | 1,201.02 | -104.36 | -105.03 | -1.01 | 0.67 | Stop loss hit. |
| `COMPUSDT` | STOPPED（已止损） | 2025-07-15T00:00:00+00:00 | 48.95 | 44.40 | 23.51 | -107.02 | -108.53 | -1.02 | 1.50 | Stop loss hit. |
| `ARBUSDT` | STOPPED（已止损） | 2025-07-17T04:00:00+00:00 | 0.43 | 0.38 | 2,252.46 | -107.32 | -108.57 | -1.02 | 1.25 | Stop loss hit. |
| `AAVEUSDT` | STOPPED（已止损） | 2025-07-18T04:00:00+00:00 | 329.07 | 301.27 | 3.97 | -110.28 | -112.00 | -1.03 | 1.72 | Stop loss hit. |
| `ADAUSDT` | STOPPED（已止损） | 2025-07-21T20:00:00+00:00 | 0.87 | 0.78 | 1,189.98 | -108.52 | -109.87 | -1.02 | 1.35 | Stop loss hit. |
| `BNBUSDT` | STOPPED（已止损） | 2025-07-23T08:00:00+00:00 | 776.34 | 731.66 | 2.39 | -106.62 | -109.11 | -1.04 | 2.49 | Stop loss hit. |
| `CFXUSDT` | STOPPED（已止损） | 2025-07-31T08:00:00+00:00 | 0.21 | 0.18 | 3,296.25 | -102.62 | -103.49 | -1.01 | 0.87 | Stop loss hit. |
| `BCHUSDT` | STOPPED（已止损） | 2025-08-08T00:00:00+00:00 | 576.71 | 532.94 | 2.36 | -103.11 | -104.91 | -1.03 | 1.80 | Stop loss hit. |
| `AVAXUSDT` | CLOSED（已按TP2平仓） | 2025-08-08T00:00:00+00:00 | 23.09 | 28.40 | 51.66 | 274.22 | 273.15 | 2.68 | 1.06 | TP2 hit; paper trade closed. |
| `APTUSDT` | STOPPED（已止损） | 2025-08-12T16:00:00+00:00 | 4.73 | 4.41 | 321.15 | -103.41 | -105.44 | -1.03 | 2.03 | Stop loss hit. |
| `AVAXUSDT` | CLOSED（已按TP2平仓） | 2025-09-16T00:00:00+00:00 | 29.85 | 34.86 | 49.15 | 246.40 | 245.13 | 2.43 | 1.27 | TP2 hit; paper trade closed. |
| `BNBUSDT` | CLOSED（已按TP2平仓） | 2025-09-16T08:00:00+00:00 | 930.05 | 1,025.84 | 3.08 | 295.12 | 292.71 | 2.87 | 2.41 | TP2 hit; paper trade closed. |
| `BONKUSDT` | STOPPED（已止损） | 2025-09-16T20:00:00+00:00 | 0.00 | 0.00 | 45,847,437.66 | -102.90 | -104.36 | -1.02 | 1.46 | Stop loss hit. |
| `BCHUSDT` | STOPPED（已止损） | 2025-09-18T00:00:00+00:00 | 604.38 | 578.40 | 4.18 | -108.57 | -111.99 | -1.06 | 3.43 | Stop loss hit. |
| `AAVEUSDT` | STOPPED（已止损） | 2025-09-18T04:00:00+00:00 | 309.62 | 284.85 | 4.33 | -107.31 | -109.08 | -1.03 | 1.77 | Stop loss hit. |
| `BNBUSDT` | STOPPED（已止损） | 2025-09-21T12:00:00+00:00 | 1,025.08 | 958.33 | 1.55 | -103.39 | -105.50 | -1.04 | 2.12 | Stop loss hit. |
| `CAKEUSDT` | STOPPED（已止损） | 2025-09-21T12:00:00+00:00 | 2.89 | 2.59 | 349.55 | -103.88 | -105.19 | -1.02 | 1.31 | Stop loss hit. |
| `ADAUSDT` | STOPPED（已止损） | 2025-10-02T00:00:00+00:00 | 0.85 | 0.77 | 1,282.99 | -102.02 | -103.44 | -1.02 | 1.42 | Stop loss hit. |
| `AAVEUSDT` | STOPPED（已止损） | 2025-10-02T00:00:00+00:00 | 287.76 | 261.85 | 3.94 | -102.04 | -103.53 | -1.02 | 1.48 | Stop loss hit. |
| `AVAXUSDT` | STOPPED（已止损） | 2025-10-02T20:00:00+00:00 | 30.78 | 28.35 | 42.26 | -102.83 | -104.55 | -1.03 | 1.72 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-11-30T04:00:00+00:00 | 91,152.21 | 88,714.33 | 0.04 | -99.63 | -104.74 | -1.09 | 5.12 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-12-03T08:00:00+00:00 | 93,325.63 | 82,482.85 | 0.01 | -94.21 | -95.25 | -1.02 | 1.04 | Stop loss hit. |
| `BNBUSDT` | STOPPED（已止损） | 2026-01-18T00:00:00+00:00 | 944.78 | 908.92 | 2.71 | -96.99 | -100.47 | -1.06 | 3.48 | Stop loss hit. |
| `BNBUSDT` | CLOSED（已按TP2平仓） | 2026-04-16T00:00:00+00:00 | 618.86 | 718.19 | 2.56 | 254.67 | 253.30 | 2.73 | 1.37 | TP2 hit; paper trade closed. |
| `AVAXUSDT` | STOPPED（已止损） | 2026-04-17T00:00:00+00:00 | 9.63 | 9.06 | 167.71 | -94.41 | -96.58 | -1.04 | 2.17 | Stop loss hit. |
| `ADAUSDT` | STOPPED（已止损） | 2026-04-17T00:00:00+00:00 | 0.25 | 0.23 | 4,645.45 | -93.63 | -95.19 | -1.03 | 1.56 | Stop loss hit. |

## 回测结束仍开放

| Symbol（交易对） | Status（状态） | Entry（入场价） | Qty（数量） | Unrealized Handling（未实现盈亏处理） | Notes（备注） |
|---|---|---:|---:|---|---|
| `BTCUSDT` | TP1_HIT（第一止盈已触达） | 69,208.02 | 0.01 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |
| `ALICEUSDT` | ENTERED（已入场） | 0.15 | 2,423.13 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |
| `BOMEUSDT` | ENTERED（已入场） | 0.00 | 938,947.62 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |

## 未入场/过期计划

| Symbol（交易对） | Status（状态） | Created（创建时间） | Entry Zone（入场区间） | Score（评分） | Notes（备注） |
|---|---|---|---:|---:|---|
| `BCHUSDT` | INVALIDATED（未入场前失效） | 2025-06-12T20:00:00+00:00 | 429.90 - 433.00 | 60.69 | Plan invalidated before entry: current price is below stop loss. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-06-30T00:00:00+00:00 | 648.87 - 649.59 | 56.89 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-03T04:00:00+00:00 | 656.07 - 657.93 | 62.47 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-07-03T08:00:00+00:00 | 0.59 - 0.60 | 66.10 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-07-04T16:00:00+00:00 | 0.00 - 0.00 | 71.04 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-06T12:00:00+00:00 | 657.05 - 658.15 | 45.07 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-07-07T00:00:00+00:00 | 0.58 - 0.58 | 49.98 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-09T20:00:00+00:00 | 662.59 - 663.99 | 61.84 | Backtest WATCHING plan expired before entry. |
| `BCHUSDT` | EXPIRED（观察计划过期） | 2025-07-11T00:00:00+00:00 | 508.00 - 512.65 | 65.30 | Backtest WATCHING plan expired before entry. |
| `APTUSDT` | EXPIRED（观察计划过期） | 2025-07-12T00:00:00+00:00 | 4.76 - 4.84 | 57.90 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-13T16:00:00+00:00 | 686.16 - 689.46 | 57.50 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-07-14T12:00:00+00:00 | 0.72 - 0.74 | 74.57 | Backtest WATCHING plan expired before entry. |
| `AAVEUSDT` | EXPIRED（观察计划过期） | 2025-07-14T16:00:00+00:00 | 310.43 - 316.01 | 71.35 | Backtest WATCHING plan expired before entry. |
| `APTUSDT` | EXPIRED（观察计划过期） | 2025-07-16T00:00:00+00:00 | 4.95 - 5.04 | 66.51 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-16T20:00:00+00:00 | 692.57 - 697.70 | 66.79 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-07-18T16:00:00+00:00 | 0.79 - 0.82 | 76.32 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-07-18T20:00:00+00:00 | 22.96 - 23.49 | 75.25 | Backtest WATCHING plan expired before entry. |
| `CAKEUSDT` | EXPIRED（观察计划过期） | 2025-07-19T00:00:00+00:00 | 2.58 - 2.64 | 68.50 | Backtest WATCHING plan expired before entry. |
| `BCHUSDT` | EXPIRED（观察计划过期） | 2025-07-19T20:00:00+00:00 | 509.15 - 516.54 | 60.29 | Backtest WATCHING plan expired before entry. |
| `APTUSDT` | EXPIRED（观察计划过期） | 2025-07-20T00:00:00+00:00 | 5.27 - 5.34 | 59.34 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-20T00:00:00+00:00 | 726.59 - 735.19 | 59.00 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-07-20T04:00:00+00:00 | 0.00 - 0.00 | 71.27 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | INVALIDATED（未入场前失效） | 2025-07-22T00:00:00+00:00 | 24.88 - 25.36 | 71.69 | Plan invalidated before entry: current price is below stop loss. |
| `ANIMEUSDT` | INVALIDATED（未入场前失效） | 2025-07-22T04:00:00+00:00 | 0.02 - 0.02 | 57.18 | Plan invalidated before entry: current price is below stop loss. |
| `BCHUSDT` | INVALIDATED（未入场前失效） | 2025-07-23T00:00:00+00:00 | 523.61 - 527.68 | 44.30 | Plan invalidated before entry: current price is below stop loss. |
| `APTUSDT` | INVALIDATED（未入场前失效） | 2025-07-23T04:00:00+00:00 | 5.37 - 5.42 | 59.38 | Plan invalidated before entry: current price is below stop loss. |
| `BONKUSDT` | INVALIDATED（未入场前失效） | 2025-07-23T08:00:00+00:00 | 0.00 - 0.00 | 67.92 | Plan invalidated before entry: current price is below stop loss. |
| `CFXUSDT` | EXPIRED（观察计划过期） | 2025-07-24T08:00:00+00:00 | 0.18 - 0.18 | 57.69 | Backtest WATCHING plan expired before entry. |
| `BCHUSDT` | EXPIRED（观察计划过期） | 2025-07-24T16:00:00+00:00 | 520.12 - 523.27 | 60.23 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-07-26T00:00:00+00:00 | 0.00 - 0.00 | 66.50 | Backtest WATCHING plan expired before entry. |
| `CAKEUSDT` | EXPIRED（观察计划过期） | 2025-07-26T00:00:00+00:00 | 2.69 - 2.75 | 64.55 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-07-26T00:00:00+00:00 | 24.02 - 24.08 | 46.51 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-07-26T16:00:00+00:00 | 0.82 - 0.84 | 63.08 | Backtest WATCHING plan expired before entry. |
| `CFXUSDT` | EXPIRED（观察计划过期） | 2025-07-27T12:00:00+00:00 | 0.18 - 0.19 | 68.36 | Backtest WATCHING plan expired before entry. |
| `CKBUSDT` | INVALIDATED（未入场前失效） | 2025-07-30T00:00:00+00:00 | 0.01 - 0.01 | 57.54 | Plan invalidated before entry: current price is below stop loss. |
| `BIOUSDT` | INVALIDATED（未入场前失效） | 2025-07-30T08:00:00+00:00 | 0.07 - 0.07 | 60.16 | Plan invalidated before entry: current price is below stop loss. |
| `BCHUSDT` | INVALIDATED（未入场前失效） | 2025-07-30T16:00:00+00:00 | 570.12 - 571.01 | 50.29 | Plan invalidated before entry: current price is below stop loss. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-08-08T08:00:00+00:00 | 773.64 - 778.88 | 60.60 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-08-08T16:00:00+00:00 | 0.76 - 0.77 | 65.29 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-08-10T04:00:00+00:00 | 0.00 - 0.00 | 63.87 | Backtest WATCHING plan expired before entry. |
| `AAVEUSDT` | EXPIRED（观察计划过期） | 2025-08-10T08:00:00+00:00 | 291.23 - 295.48 | 73.60 | Backtest WATCHING plan expired before entry. |
| `ARBUSDT` | EXPIRED（观察计划过期） | 2025-08-11T08:00:00+00:00 | 0.45 - 0.46 | 68.68 | Backtest WATCHING plan expired before entry. |
| `APTUSDT` | INVALIDATED（未入场前失效） | 2025-08-11T08:00:00+00:00 | 4.68 - 4.74 | 53.67 | Plan invalidated before entry: current price is below stop loss. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-08-11T16:00:00+00:00 | 801.89 - 809.22 | 62.06 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-08-12T16:00:00+00:00 | 0.79 - 0.81 | 65.38 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | INVALIDATED（未入场前失效） | 2025-08-13T20:00:00+00:00 | 0.00 - 0.00 | 62.03 | Plan invalidated before entry: current price is below stop loss. |
| `ALPINEUSDT` | EXPIRED（观察计划过期） | 2025-08-14T04:00:00+00:00 | 1.34 - 1.36 | 73.39 | Backtest WATCHING plan expired before entry. |
| `BERAUSDT` | EXPIRED（观察计划过期） | 2025-08-15T08:00:00+00:00 | 2.12 - 2.15 | 56.07 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-08-15T20:00:00+00:00 | 0.91 - 0.93 | 73.08 | Backtest WATCHING plan expired before entry. |
| `APTUSDT` | INVALIDATED（未入场前失效） | 2025-08-23T00:00:00+00:00 | 4.63 - 4.69 | 53.21 | Plan invalidated before entry: current price is below stop loss. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-08-23T04:00:00+00:00 | 861.81 - 871.06 | 71.00 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-08-23T12:00:00+00:00 | 0.89 - 0.91 | 71.43 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-09-17T08:00:00+00:00 | 0.88 - 0.88 | 50.38 | Backtest WATCHING plan expired before entry. |
| `ARBUSDT` | EXPIRED（观察计划过期） | 2025-09-18T00:00:00+00:00 | 0.51 - 0.52 | 46.78 | Backtest WATCHING plan expired before entry. |
| `BIOUSDT` | INVALIDATED（未入场前失效） | 2025-09-21T00:00:00+00:00 | 0.18 - 0.18 | 73.51 | Plan invalidated before entry: current price is below stop loss. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-10-02T00:00:00+00:00 | 1,011.09 - 1,019.11 | 63.44 | Backtest WATCHING plan expired before entry. |
| `ARBUSDT` | EXPIRED（观察计划过期） | 2025-10-03T04:00:00+00:00 | 0.44 - 0.44 | 55.25 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-10-03T16:00:00+00:00 | 0.00 - 0.00 | 54.75 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-10-05T12:00:00+00:00 | 1,131.18 - 1,149.27 | 72.89 | Backtest WATCHING plan expired before entry. |
| `APTUSDT` | EXPIRED（观察计划过期） | 2025-10-05T20:00:00+00:00 | 5.26 - 5.38 | 76.12 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | INVALIDATED（未入场前失效） | 2025-10-07T00:00:00+00:00 | 0.00 - 0.00 | 62.93 | Plan invalidated before entry: current price is below stop loss. |
| `ARBUSDT` | INVALIDATED（未入场前失效） | 2025-10-07T00:00:00+00:00 | 0.45 - 0.46 | 61.41 | Plan invalidated before entry: current price is below stop loss. |
| `API3USDT` | INVALIDATED（未入场前失效） | 2025-10-08T00:00:00+00:00 | 0.85 - 0.88 | 64.48 | Plan invalidated before entry: current price is below stop loss. |
| `BNBUSDT` | INVALIDATED（未入场前失效） | 2025-10-08T16:00:00+00:00 | 1,249.87 - 1,275.74 | 83.10 | Plan invalidated before entry: current price is below stop loss. |
| `AVNTUSDT` | EXPIRED（观察计划过期） | 2026-04-18T12:00:00+00:00 | 0.14 - 0.14 | 53.00 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2026-04-21T12:00:00+00:00 | 9.37 - 9.47 | 48.53 | Backtest WATCHING plan expired before entry. |
| `BCHUSDT` | EXPIRED（观察计划过期） | 2026-05-07T00:00:00+00:00 | 458.71 - 463.32 | 56.00 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2026-05-07T08:00:00+00:00 | 9.47 - 9.56 | 61.12 | Backtest WATCHING plan expired before entry. |
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
| INFO | n/a | n/a | Additional issues omitted: 1100. |

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
    "created_at_utc": "2026-06-08T18:36:48+00:00",
    "refresh_frequency": "daily",
    "max_symbols": 30,
    "master_count": 100,
    "source_limit": 100,
    "source_limit_applied": true,
    "universe_refresh_count": 366,
    "selected_count_min": 2,
    "selected_count_avg": 6.245901639344262,
    "selected_count_max": 18,
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
        "symbol": "ADAUSDT",
        "days_selected": 288
      },
      {
        "symbol": "AVAXUSDT",
        "days_selected": 226
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
        "symbol": "APTUSDT",
        "days_selected": 61
      },
      {
        "symbol": "AVNTUSDT",
        "days_selected": 36
      },
      {
        "symbol": "CAKEUSDT",
        "days_selected": 36
      },
      {
        "symbol": "BIOUSDT",
        "days_selected": 34
      },
      {
        "symbol": "BANANAS31USDT",
        "days_selected": 23
      },
      {
        "symbol": "CFXUSDT",
        "days_selected": 23
      },
      {
        "symbol": "CHIPUSDT",
        "days_selected": 21
      },
      {
        "symbol": "ATUSDT",
        "days_selected": 18
      },
      {
        "symbol": "BARDUSDT",
        "days_selected": 18
      },
      {
        "symbol": "ALLOUSDT",
        "days_selected": 14
      },
      {
        "symbol": "AXSUSDT",
        "days_selected": 13
      }
    ],
    "filter_counts": {
      "missing_1h": 2349,
      "insufficient_24h": 13,
      "reconstruct_error": 0,
      "low_quote_volume": 31934,
      "low_trades": 16,
      "stable_like": 2
    },
    "selection_by_day": [
      {
        "date_utc": "2025-06-01",
        "decision_time_utc": "2025-06-01T04:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 82,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-02",
        "decision_time_utc": "2025-06-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 83,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-03",
        "decision_time_utc": "2025-06-03T00:00:00+00:00",
        "selected_symbols": [
          "AAVEUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "AUSDT",
          "AVAXUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-04",
        "decision_time_utc": "2025-06-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-05",
        "decision_time_utc": "2025-06-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "COMPUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-06",
        "decision_time_utc": "2025-06-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "CAKEUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-07",
        "decision_time_utc": "2025-06-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "COMPUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "ANIMEUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-08",
        "decision_time_utc": "2025-06-08T00:00:00+00:00",
        "selected_symbols": [
          "ANIMEUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 82,
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
          "AVAXUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 82,
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
          "BTCUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
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
          "BTCUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ANIMEUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 77,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-12",
        "decision_time_utc": "2025-06-12T00:00:00+00:00",
        "selected_symbols": [
          "AUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ANIMEUSDT",
          "BCHUSDT",
          "ARBUSDT",
          "CAKEUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 77,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-13",
        "decision_time_utc": "2025-06-13T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 82,
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
          "BNBUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "APTUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 78,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-15",
        "decision_time_utc": "2025-06-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 83,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-16",
        "decision_time_utc": "2025-06-16T00:00:00+00:00",
        "selected_symbols": [
          "BCHUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 84,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-17",
        "decision_time_utc": "2025-06-17T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ALTUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-18",
        "decision_time_utc": "2025-06-18T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ALTUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-19",
        "decision_time_utc": "2025-06-19T00:00:00+00:00",
        "selected_symbols": [
          "ALTUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
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
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-21",
        "decision_time_utc": "2025-06-21T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "BCHUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-22",
        "decision_time_utc": "2025-06-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-23",
        "decision_time_utc": "2025-06-23T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BCHUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-24",
        "decision_time_utc": "2025-06-24T00:00:00+00:00",
        "selected_symbols": [
          "BANANAS31USDT",
          "AAVEUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
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
          "BTCUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
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
          "BNBUSDT",
          "APTUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-27",
        "decision_time_utc": "2025-06-27T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "BANANAS31USDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
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
          "AAVEUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "APTUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-29",
        "decision_time_utc": "2025-06-29T00:00:00+00:00",
        "selected_symbols": [
          "BANANAS31USDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 83,
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
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 82,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-01",
        "decision_time_utc": "2025-07-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ARBUSDT",
          "ADAUSDT",
          "BANANAS31USDT",
          "BCHUSDT",
          "AAVEUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-02",
        "decision_time_utc": "2025-07-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 82,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-03",
        "decision_time_utc": "2025-07-03T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-04",
        "decision_time_utc": "2025-07-04T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
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
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-06",
        "decision_time_utc": "2025-07-06T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "BMTUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 83,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-07",
        "decision_time_utc": "2025-07-07T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 82,
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
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 82,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-09",
        "decision_time_utc": "2025-07-09T00:00:00+00:00",
        "selected_symbols": [
          "BANANAS31USDT",
          "BTCUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-10",
        "decision_time_utc": "2025-07-10T00:00:00+00:00",
        "selected_symbols": [
          "BANANAS31USDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
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
          "ADAUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 77,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-12",
        "decision_time_utc": "2025-07-12T00:00:00+00:00",
        "selected_symbols": [
          "1INCHUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "ALTUSDT",
          "BANANAS31USDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 75,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-13",
        "decision_time_utc": "2025-07-13T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ARKUSDT",
          "BANANAS31USDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
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
          "BONKUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "1INCHUSDT",
          "BANANAS31USDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 77,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-15",
        "decision_time_utc": "2025-07-15T00:00:00+00:00",
        "selected_symbols": [
          "ALGOUSDT",
          "BTCUSDT",
          "COMPUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "BANANAS31USDT",
          "ADAUSDT",
          "BNBUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 76,
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
          "AVAXUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "APTUSDT",
          "BNBUSDT",
          "ALGOUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 78,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-17",
        "decision_time_utc": "2025-07-17T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "BOMEUSDT",
          "COWUSDT",
          "BERAUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "APTUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 76,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-18",
        "decision_time_utc": "2025-07-18T00:00:00+00:00",
        "selected_symbols": [
          "ALGOUSDT",
          "ADAUSDT",
          "BOMEUSDT",
          "AVAXUSDT",
          "AIXBTUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "APTUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 76,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-19",
        "decision_time_utc": "2025-07-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "CAKEUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "ALGOUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 76,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-20",
        "decision_time_utc": "2025-07-20T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "BTCUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "BNBUSDT",
          "APTUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
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
          "ACHUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ARBUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "APTUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 75,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-22",
        "decision_time_utc": "2025-07-22T00:00:00+00:00",
        "selected_symbols": [
          "ANIMEUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "CAKEUSDT",
          "CFXUSDT",
          "ARBUSDT",
          "BCHUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 75,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-23",
        "decision_time_utc": "2025-07-23T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "BCHUSDT",
          "CFXUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 77,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-24",
        "decision_time_utc": "2025-07-24T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "CAKEUSDT",
          "CFXUSDT",
          "BCHUSDT",
          "BERAUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 75,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-25",
        "decision_time_utc": "2025-07-25T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "CFXUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "BCHUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "CAKEUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 76,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-26",
        "decision_time_utc": "2025-07-26T00:00:00+00:00",
        "selected_symbols": [
          "BCHUSDT",
          "BONKUSDT",
          "CFXUSDT",
          "BTCUSDT",
          "CAKEUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "APTUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 76,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-27",
        "decision_time_utc": "2025-07-27T00:00:00+00:00",
        "selected_symbols": [
          "CKBUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "CFXUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
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
          "BNBUSDT",
          "BCHUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 76,
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
          "1000CATUSDT",
          "BTCUSDT",
          "CFXUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "CAKEUSDT",
          "BCHUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "APTUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 72,
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
          "CFXUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "CAKEUSDT",
          "APTUSDT",
          "BCHUSDT",
          "AAVEUSDT",
          "BANANAS31USDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 73,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-31",
        "decision_time_utc": "2025-07-31T00:00:00+00:00",
        "selected_symbols": [
          "CFXUSDT",
          "BCHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "APTUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 77,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-01",
        "decision_time_utc": "2025-08-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "CFXUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BCHUSDT",
          "APTUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 77,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-02",
        "decision_time_utc": "2025-08-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "CFXUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 77,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-03",
        "decision_time_utc": "2025-08-03T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "APTUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-04",
        "decision_time_utc": "2025-08-04T00:00:00+00:00",
        "selected_symbols": [
          "CFXUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 82,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-05",
        "decision_time_utc": "2025-08-05T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "CFXUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-06",
        "decision_time_utc": "2025-08-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "APTUSDT",
          "CFXUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-07",
        "decision_time_utc": "2025-08-07T00:00:00+00:00",
        "selected_symbols": [
          "CFXUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
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
          "AAVEUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "CFXUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 77,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-09",
        "decision_time_utc": "2025-08-09T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "APTUSDT",
          "ASRUSDT",
          "ARBUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "CFXUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 76,
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
          "ARBUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "BIOUSDT",
          "CFXUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 76,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-11",
        "decision_time_utc": "2025-08-11T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "BTCUSDT",
          "BONKUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "APTUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 78,
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
          "BNBUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "APTUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 76,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-13",
        "decision_time_utc": "2025-08-13T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "APTUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "BIOUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 77,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-14",
        "decision_time_utc": "2025-08-14T00:00:00+00:00",
        "selected_symbols": [
          "ARBUSDT",
          "ALPINEUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "APTUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 77,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-15",
        "decision_time_utc": "2025-08-15T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "BTCUSDT",
          "BERAUSDT",
          "BNBUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "BCHUSDT",
          "CFXUSDT",
          "ALGOUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 75,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-16",
        "decision_time_utc": "2025-08-16T00:00:00+00:00",
        "selected_symbols": [
          "ALPINEUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "AAVEUSDT",
          "APTUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-17",
        "decision_time_utc": "2025-08-17T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "ALPINEUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 82,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-18",
        "decision_time_utc": "2025-08-18T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "ARBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "ASRUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-19",
        "decision_time_utc": "2025-08-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "BIOUSDT",
          "AAVEUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-20",
        "decision_time_utc": "2025-08-20T00:00:00+00:00",
        "selected_symbols": [
          "API3USDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "BIOUSDT",
          "BONKUSDT",
          "AAVEUSDT",
          "APTUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 78,
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
          "ARBUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "API3USDT",
          "AVAXUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 78,
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
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
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
          "ARBUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "APTUSDT",
          "BTCUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 77,
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
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BIOUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-25",
        "decision_time_utc": "2025-08-25T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "BOMEUSDT",
          "BIOUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-26",
        "decision_time_utc": "2025-08-26T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BIOUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "APTUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-27",
        "decision_time_utc": "2025-08-27T00:00:00+00:00",
        "selected_symbols": [
          "BERAUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "BCHUSDT",
          "BIOUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-28",
        "decision_time_utc": "2025-08-28T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "CKBUSDT",
          "AVAXUSDT",
          "BERAUSDT",
          "BIOUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 78,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-29",
        "decision_time_utc": "2025-08-29T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ARBUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BIOUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-30",
        "decision_time_utc": "2025-08-30T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "BCHUSDT",
          "BIOUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-08-31",
        "decision_time_utc": "2025-08-31T00:00:00+00:00",
        "selected_symbols": [
          "CFXUSDT",
          "BTCUSDT",
          "BONKUSDT",
          "ARBUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-01",
        "decision_time_utc": "2025-09-01T00:00:00+00:00",
        "selected_symbols": [
          "AXSUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 82,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-02",
        "decision_time_utc": "2025-09-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "AAVEUSDT",
          "BIOUSDT",
          "APTUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-03",
        "decision_time_utc": "2025-09-03T00:00:00+00:00",
        "selected_symbols": [
          "BCHUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-04",
        "decision_time_utc": "2025-09-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BCHUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-05",
        "decision_time_utc": "2025-09-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-06",
        "decision_time_utc": "2025-09-06T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "BTCUSDT",
          "BCHUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-07",
        "decision_time_utc": "2025-09-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "BIOUSDT",
          "BCHUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 83,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-08",
        "decision_time_utc": "2025-09-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 84,
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
          "ADAUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
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
          "BTCUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "AAVEUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 78,
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
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "ARBUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-12",
        "decision_time_utc": "2025-09-12T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "BTCUSDT",
          "BIOUSDT",
          "ARKMUSDT",
          "ARBUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ACEUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 78,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-13",
        "decision_time_utc": "2025-09-13T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-14",
        "decision_time_utc": "2025-09-14T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-15",
        "decision_time_utc": "2025-09-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BIOUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-16",
        "decision_time_utc": "2025-09-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 11,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 82,
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
          "ADAUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "AVNTUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 11,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-18",
        "decision_time_utc": "2025-09-18T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "BNBUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "AVNTUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "BCHUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 11,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
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
          "AVNTUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "ARBUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-20",
        "decision_time_utc": "2025-09-20T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "AVNTUSDT",
          "ARBUSDT",
          "BARDUSDT",
          "BONKUSDT",
          "APTUSDT",
          "BCHUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
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
          "BTCUSDT",
          "AVAXUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
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
          "BARDUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "CAKEUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 82,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-23",
        "decision_time_utc": "2025-09-23T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "APTUSDT",
          "BBUSDT",
          "CAKEUSDT",
          "AVNTUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 9,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
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
          "AVAXUSDT",
          "AVNTUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 9,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-25",
        "decision_time_utc": "2025-09-25T00:00:00+00:00",
        "selected_symbols": [
          "BBUSDT",
          "AVNTUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "0GUSDT",
          "BARDUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 9,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 82,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-26",
        "decision_time_utc": "2025-09-26T00:00:00+00:00",
        "selected_symbols": [
          "1000SATSUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "BARDUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "0GUSDT",
          "BONKUSDT",
          "APTUSDT",
          "AWEUSDT",
          "AVNTUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 9,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 78,
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
          "AVNTUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "0GUSDT",
          "BARDUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 9,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
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
          "BTCUSDT",
          "BNBUSDT",
          "AVNTUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "1000SATSUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 9,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 83,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-29",
        "decision_time_utc": "2025-09-29T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVNTUSDT",
          "BARDUSDT",
          "ALPINEUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 9,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 84,
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
          "AVAXUSDT",
          "AVNTUSDT",
          "ADAUSDT",
          "0GUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 9,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 83,
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
          "APTUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "ALPINEUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 9,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 83,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-02",
        "decision_time_utc": "2025-10-02T00:00:00+00:00",
        "selected_symbols": [
          "APTUSDT",
          "0GUSDT",
          "BTCUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "BARDUSDT",
          "AVNTUSDT",
          "ALPINEUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 9,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-03",
        "decision_time_utc": "2025-10-03T00:00:00+00:00",
        "selected_symbols": [
          "C98USDT",
          "CAKEUSDT",
          "BNBUSDT",
          "APTUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "ADAUSDT",
          "BARDUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "AVNTUSDT",
          "AAVEUSDT",
          "ALPINEUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 78,
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
          "APTUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "2ZUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-05",
        "decision_time_utc": "2025-10-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "CAKEUSDT",
          "AVNTUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 84,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-06",
        "decision_time_utc": "2025-10-06T00:00:00+00:00",
        "selected_symbols": [
          "CELOUSDT",
          "APTUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AVNTUSDT",
          "CAKEUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 83,
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
          "BNBUSDT",
          "ARBUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "CELOUSDT",
          "AVAXUSDT",
          "AVNTUSDT",
          "APTUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-08",
        "decision_time_utc": "2025-10-08T00:00:00+00:00",
        "selected_symbols": [
          "CAKEUSDT",
          "BNBUSDT",
          "API3USDT",
          "BROCCOLI714USDT",
          "BTCUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "BONKUSDT",
          "ARBUSDT",
          "AVNTUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-09",
        "decision_time_utc": "2025-10-09T00:00:00+00:00",
        "selected_symbols": [
          "1000CHEEMSUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ASTERUSDT",
          "CAKEUSDT",
          "APTUSDT",
          "AVNTUSDT",
          "BROCCOLI714USDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 83,
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
          "BNBUSDT",
          "ASTERUSDT",
          "CAKEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "APTUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 84,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-11",
        "decision_time_utc": "2025-10-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "1000CHEEMSUSDT",
          "ASTERUSDT",
          "ALGOUSDT",
          "CAKEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "AVNTUSDT",
          "ARKMUSDT",
          "BONKUSDT",
          "APTUSDT",
          "BNSOLUSDT",
          "ALICEUSDT",
          "ATOMUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 75,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-12",
        "decision_time_utc": "2025-10-12T00:00:00+00:00",
        "selected_symbols": [
          "AVNTUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "BONKUSDT",
          "ARBUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "BNSOLUSDT",
          "APTUSDT",
          "CAKEUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-13",
        "decision_time_utc": "2025-10-13T00:00:00+00:00",
        "selected_symbols": [
          "CAKEUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "AVNTUSDT",
          "BTCUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 82,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-14",
        "decision_time_utc": "2025-10-14T00:00:00+00:00",
        "selected_symbols": [
          "ALICEUSDT",
          "BATUSDT",
          "BONKUSDT",
          "CAKEUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "2ZUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "ASTERUSDT",
          "APTUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
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
          "BTCUSDT",
          "BNBUSDT",
          "2ZUSDT",
          "ADAUSDT",
          "CAKEUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-16",
        "decision_time_utc": "2025-10-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "2ZUSDT",
          "ASTERUSDT",
          "CAKEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 84,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-17",
        "decision_time_utc": "2025-10-17T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "2ZUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "CAKEUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "BELUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 82,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-18",
        "decision_time_utc": "2025-10-18T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BCHUSDT",
          "CAKEUSDT",
          "ARBUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 83,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-19",
        "decision_time_utc": "2025-10-19T00:00:00+00:00",
        "selected_symbols": [
          "BNBUSDT",
          "BTCUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 88,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-20",
        "decision_time_utc": "2025-10-20T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ASTERUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 88,
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
          "BIOUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ASTERUSDT",
          "AVAXUSDT",
          "CAKEUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 84,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-22",
        "decision_time_utc": "2025-10-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "AVNTUSDT",
          "ADAUSDT",
          "BCHUSDT",
          "AVAXUSDT",
          "CAKEUSDT",
          "AAVEUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 83,
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
          "BNBUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "CAKEUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 85,
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
          "ADAUSDT",
          "AVNTUSDT",
          "BCHUSDT",
          "CAKEUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 85,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-25",
        "decision_time_utc": "2025-10-25T00:00:00+00:00",
        "selected_symbols": [
          "AVNTUSDT",
          "BTCUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "CAKEUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 86,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-26",
        "decision_time_utc": "2025-10-26T00:00:00+00:00",
        "selected_symbols": [
          "AIXBTUSDT",
          "BTCUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "AVNTUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 88,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-27",
        "decision_time_utc": "2025-10-27T00:00:00+00:00",
        "selected_symbols": [
          "AIXBTUSDT",
          "BCHUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "AVNTUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 85,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-28",
        "decision_time_utc": "2025-10-28T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "1000CHEEMSUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 86,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-29",
        "decision_time_utc": "2025-10-29T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 87,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-30",
        "decision_time_utc": "2025-10-30T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 86,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-31",
        "decision_time_utc": "2025-10-31T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "ARBUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 85,
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
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 86,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-02",
        "decision_time_utc": "2025-11-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 89,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-03",
        "decision_time_utc": "2025-11-03T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 89,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-04",
        "decision_time_utc": "2025-11-04T00:00:00+00:00",
        "selected_symbols": [
          "0GUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "BCHUSDT",
          "BONKUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 82,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-05",
        "decision_time_utc": "2025-11-05T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "BCHUSDT",
          "CAKEUSDT",
          "APTUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-06",
        "decision_time_utc": "2025-11-06T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 86,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-07",
        "decision_time_utc": "2025-11-07T00:00:00+00:00",
        "selected_symbols": [
          "ARUSDT",
          "BTCUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ALCXUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 85,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-08",
        "decision_time_utc": "2025-11-08T00:00:00+00:00",
        "selected_symbols": [
          "ARUSDT",
          "APTUSDT",
          "ASTERUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 82,
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
          "BNBUSDT",
          "ASTERUSDT",
          "AAVEUSDT",
          "ARUSDT",
          "AVAXUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 85,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-10",
        "decision_time_utc": "2025-11-10T00:00:00+00:00",
        "selected_symbols": [
          "0GUSDT",
          "ASTERUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ARUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 86,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-11",
        "decision_time_utc": "2025-11-11T00:00:00+00:00",
        "selected_symbols": [
          "AAVEUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "COTIUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 86,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-12",
        "decision_time_utc": "2025-11-12T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "CAKEUSDT",
          "BCHUSDT",
          "AAVEUSDT",
          "CFXUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 84,
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
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "ALLOUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 86,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-14",
        "decision_time_utc": "2025-11-14T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ALCXUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "ALLOUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 84,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-15",
        "decision_time_utc": "2025-11-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "ALLOUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "APTUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 85,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-16",
        "decision_time_utc": "2025-11-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 91,
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
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-18",
        "decision_time_utc": "2025-11-18T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "BANANAS31USDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 87,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-19",
        "decision_time_utc": "2025-11-19T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "BCHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 89,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-20",
        "decision_time_utc": "2025-11-20T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-21",
        "decision_time_utc": "2025-11-21T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ALLOUSDT",
          "BCHUSDT",
          "AAVEUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 86,
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
          "ASTERUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "ALLOUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 85,
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
          "BNBUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 88,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-24",
        "decision_time_utc": "2025-11-24T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 89,
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
          "BTCUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 87,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-26",
        "decision_time_utc": "2025-11-26T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "ALLOUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 89,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-27",
        "decision_time_utc": "2025-11-27T00:00:00+00:00",
        "selected_symbols": [
          "BANANAS31USDT",
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "ALLOUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 86,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2025-11-28",
        "decision_time_utc": "2025-11-28T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ASTERUSDT",
          "BANANAS31USDT",
          "ADAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 88,
          "low_trades": 0,
          "stable_like": 1
        }
      },
      {
        "date_utc": "2025-11-29",
        "decision_time_utc": "2025-11-29T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "ATUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 88,
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
          "BNBUSDT",
          "ASTERUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 91,
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
          "ATUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-02",
        "decision_time_utc": "2025-12-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "BCHUSDT",
          "AVAXUSDT",
          "ATUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 88,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-03",
        "decision_time_utc": "2025-12-03T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ASTERUSDT",
          "BCHUSDT",
          "ATUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 88,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-04",
        "decision_time_utc": "2025-12-04T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "ATUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 88,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-05",
        "decision_time_utc": "2025-12-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "ATUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 88,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-06",
        "decision_time_utc": "2025-12-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "ATUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-07",
        "decision_time_utc": "2025-12-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-08",
        "decision_time_utc": "2025-12-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ASTERUSDT",
          "AVAXUSDT",
          "ATUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-09",
        "decision_time_utc": "2025-12-09T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ATUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 91,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-10",
        "decision_time_utc": "2025-12-10T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "ATUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 89,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-11",
        "decision_time_utc": "2025-12-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ASTERUSDT",
          "ATUSDT",
          "BCHUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 89,
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
          "BNBUSDT",
          "ADAUSDT",
          "ATUSDT",
          "AVAXUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 89,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-13",
        "decision_time_utc": "2025-12-13T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ATUSDT",
          "BCHUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 89,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-14",
        "decision_time_utc": "2025-12-14T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-15",
        "decision_time_utc": "2025-12-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 92,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-16",
        "decision_time_utc": "2025-12-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 91,
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
          "ASTERUSDT",
          "AVAXUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 91,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-18",
        "decision_time_utc": "2025-12-18T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 91,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-19",
        "decision_time_utc": "2025-12-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-20",
        "decision_time_utc": "2025-12-20T00:00:00+00:00",
        "selected_symbols": [
          "BCHUSDT",
          "ASTERUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 89,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-21",
        "decision_time_utc": "2025-12-21T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-22",
        "decision_time_utc": "2025-12-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-23",
        "decision_time_utc": "2025-12-23T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "ASTERUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 89,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-24",
        "decision_time_utc": "2025-12-24T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "AVAXUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 91,
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
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-26",
        "decision_time_utc": "2025-12-26T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-27",
        "decision_time_utc": "2025-12-27T00:00:00+00:00",
        "selected_symbols": [
          "ATUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 91,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-28",
        "decision_time_utc": "2025-12-28T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
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
          "BNBUSDT",
          "ADAUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 91,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-30",
        "decision_time_utc": "2025-12-30T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ATUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-31",
        "decision_time_utc": "2025-12-31T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 92,
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
          "ATUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BROCCOLI714USDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-02",
        "decision_time_utc": "2026-01-02T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "ADAUSDT",
          "BROCCOLI714USDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 91,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-03",
        "decision_time_utc": "2026-01-03T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "ADAUSDT",
          "ASTERUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 89,
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
          "AVAXUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
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
          "ASTERUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 88,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-06",
        "decision_time_utc": "2026-01-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "ASTERUSDT",
          "BROCCOLI714USDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 88,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-07",
        "decision_time_utc": "2026-01-07T00:00:00+00:00",
        "selected_symbols": [
          "BROCCOLI714USDT",
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 88,
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
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "BROCCOLI714USDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
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
          "BNBUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "BREVUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-10",
        "decision_time_utc": "2026-01-10T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-11",
        "decision_time_utc": "2026-01-11T00:00:00+00:00",
        "selected_symbols": [
          "BNBUSDT",
          "BTCUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-12",
        "decision_time_utc": "2026-01-12T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BCHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-13",
        "decision_time_utc": "2026-01-13T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 91,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-14",
        "decision_time_utc": "2026-01-14T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "BREVUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-15",
        "decision_time_utc": "2026-01-15T00:00:00+00:00",
        "selected_symbols": [
          "BERAUSDT",
          "AXSUSDT",
          "BTCUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "BREVUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 87,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-16",
        "decision_time_utc": "2026-01-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BREVUSDT",
          "ASTERUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-17",
        "decision_time_utc": "2026-01-17T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BREVUSDT",
          "AUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
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
          "BTCUSDT",
          "BREVUSDT",
          "BNBUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 91,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-19",
        "decision_time_utc": "2026-01-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "AXSUSDT",
          "BREVUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 92,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-20",
        "decision_time_utc": "2026-01-20T00:00:00+00:00",
        "selected_symbols": [
          "ARPAUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "BREVUSDT",
          "ADAUSDT",
          "ASTERUSDT",
          "AVAXUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 89,
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
          "BREVUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ASTERUSDT",
          "AVAXUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 89,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-22",
        "decision_time_utc": "2026-01-22T00:00:00+00:00",
        "selected_symbols": [
          "AXSUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 91,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-23",
        "decision_time_utc": "2026-01-23T00:00:00+00:00",
        "selected_symbols": [
          "AXSUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-24",
        "decision_time_utc": "2026-01-24T00:00:00+00:00",
        "selected_symbols": [
          "AXSUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-25",
        "decision_time_utc": "2026-01-25T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "AXSUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-26",
        "decision_time_utc": "2026-01-26T00:00:00+00:00",
        "selected_symbols": [
          "AUCTIONUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AXSUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 92,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-27",
        "decision_time_utc": "2026-01-27T00:00:00+00:00",
        "selected_symbols": [
          "AXSUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-28",
        "decision_time_utc": "2026-01-28T00:00:00+00:00",
        "selected_symbols": [
          "AXSUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-29",
        "decision_time_utc": "2026-01-29T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-30",
        "decision_time_utc": "2026-01-30T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 92,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-31",
        "decision_time_utc": "2026-01-31T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 92,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-01",
        "decision_time_utc": "2026-02-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ASTERUSDT",
          "AAVEUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-02",
        "decision_time_utc": "2026-02-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 92,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-03",
        "decision_time_utc": "2026-02-03T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 92,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-04",
        "decision_time_utc": "2026-02-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ASTERUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 92,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-05",
        "decision_time_utc": "2026-02-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-06",
        "decision_time_utc": "2026-02-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ASTERUSDT",
          "AAVEUSDT",
          "BCHUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 89,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-07",
        "decision_time_utc": "2026-02-07T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "BTCUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-08",
        "decision_time_utc": "2026-02-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ASTERUSDT",
          "BCHUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 91,
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
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-10",
        "decision_time_utc": "2026-02-10T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "BERAUSDT",
          "ADAUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 92,
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
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
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
          "BNBUSDT",
          "BERAUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
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
          "BNBUSDT",
          "BERAUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-14",
        "decision_time_utc": "2026-02-14T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-15",
        "decision_time_utc": "2026-02-15T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-16",
        "decision_time_utc": "2026-02-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-17",
        "decision_time_utc": "2026-02-17T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-18",
        "decision_time_utc": "2026-02-18T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-19",
        "decision_time_utc": "2026-02-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-20",
        "decision_time_utc": "2026-02-20T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-21",
        "decision_time_utc": "2026-02-21T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 92,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-22",
        "decision_time_utc": "2026-02-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-23",
        "decision_time_utc": "2026-02-23T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-24",
        "decision_time_utc": "2026-02-24T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-25",
        "decision_time_utc": "2026-02-25T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-26",
        "decision_time_utc": "2026-02-26T00:00:00+00:00",
        "selected_symbols": [
          "APTUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 92,
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
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 92,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-28",
        "decision_time_utc": "2026-02-28T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-01",
        "decision_time_utc": "2026-03-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-02",
        "decision_time_utc": "2026-03-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-03",
        "decision_time_utc": "2026-03-03T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 92,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-04",
        "decision_time_utc": "2026-03-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-05",
        "decision_time_utc": "2026-03-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
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
          "BNBUSDT",
          "ADAUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 92,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-07",
        "decision_time_utc": "2026-03-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-08",
        "decision_time_utc": "2026-03-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-09",
        "decision_time_utc": "2026-03-09T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-10",
        "decision_time_utc": "2026-03-10T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-11",
        "decision_time_utc": "2026-03-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-12",
        "decision_time_utc": "2026-03-12T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-13",
        "decision_time_utc": "2026-03-13T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-14",
        "decision_time_utc": "2026-03-14T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
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
          "BNBUSDT",
          "BANANAS31USDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-16",
        "decision_time_utc": "2026-03-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-17",
        "decision_time_utc": "2026-03-17T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-18",
        "decision_time_utc": "2026-03-18T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-19",
        "decision_time_utc": "2026-03-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ASTERUSDT",
          "AVAXUSDT",
          "BARDUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 92,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-20",
        "decision_time_utc": "2026-03-20T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-21",
        "decision_time_utc": "2026-03-21T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-22",
        "decision_time_utc": "2026-03-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
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
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-24",
        "decision_time_utc": "2026-03-24T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-25",
        "decision_time_utc": "2026-03-25T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-26",
        "decision_time_utc": "2026-03-26T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-27",
        "decision_time_utc": "2026-03-27T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-28",
        "decision_time_utc": "2026-03-28T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "CFGUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-29",
        "decision_time_utc": "2026-03-29T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-30",
        "decision_time_utc": "2026-03-30T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-31",
        "decision_time_utc": "2026-03-31T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-01",
        "decision_time_utc": "2026-04-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-02",
        "decision_time_utc": "2026-04-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-03",
        "decision_time_utc": "2026-04-03T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-04",
        "decision_time_utc": "2026-04-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-05",
        "decision_time_utc": "2026-04-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-06",
        "decision_time_utc": "2026-04-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-07",
        "decision_time_utc": "2026-04-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-08",
        "decision_time_utc": "2026-04-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-09",
        "decision_time_utc": "2026-04-09T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-10",
        "decision_time_utc": "2026-04-10T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-11",
        "decision_time_utc": "2026-04-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-12",
        "decision_time_utc": "2026-04-12T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-13",
        "decision_time_utc": "2026-04-13T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-14",
        "decision_time_utc": "2026-04-14T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-15",
        "decision_time_utc": "2026-04-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "BARDUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-16",
        "decision_time_utc": "2026-04-16T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "BARDUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
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
          "ADAUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-18",
        "decision_time_utc": "2026-04-18T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AVNTUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-19",
        "decision_time_utc": "2026-04-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AVNTUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "ALICEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-20",
        "decision_time_utc": "2026-04-20T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BOMEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-21",
        "decision_time_utc": "2026-04-21T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-22",
        "decision_time_utc": "2026-04-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AAVEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
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
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-24",
        "decision_time_utc": "2026-04-24T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "CHIPUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
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
          "CHIPUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
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
          "CHIPUSDT",
          "API3USDT",
          "BNBUSDT",
          "APEUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-27",
        "decision_time_utc": "2026-04-27T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "CHIPUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
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
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
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
          "CHIPUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-30",
        "decision_time_utc": "2026-04-30T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "CHIPUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
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
          "CHIPUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-02",
        "decision_time_utc": "2026-05-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "CHIPUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
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
          "CHIPUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
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
          "CHIPUSDT",
          "BNBUSDT",
          "BABYUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-05",
        "decision_time_utc": "2026-05-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "CHIPUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-06",
        "decision_time_utc": "2026-05-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-07",
        "decision_time_utc": "2026-05-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "CHIPUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-08",
        "decision_time_utc": "2026-05-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "CHIPUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-09",
        "decision_time_utc": "2026-05-09T00:00:00+00:00",
        "selected_symbols": [
          "CHIPUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-10",
        "decision_time_utc": "2026-05-10T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "CHIPUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-11",
        "decision_time_utc": "2026-05-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "APTUSDT",
          "BNBUSDT",
          "CHIPUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-12",
        "decision_time_utc": "2026-05-12T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "CHIPUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
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
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-14",
        "decision_time_utc": "2026-05-14T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "CHIPUSDT",
          "COSUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-15",
        "decision_time_utc": "2026-05-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-16",
        "decision_time_utc": "2026-05-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "AIGENSYNUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 97,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-17",
        "decision_time_utc": "2026-05-17T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 98,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-18",
        "decision_time_utc": "2026-05-18T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 98,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-19",
        "decision_time_utc": "2026-05-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 97,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-20",
        "decision_time_utc": "2026-05-20T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 98,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-21",
        "decision_time_utc": "2026-05-21T00:00:00+00:00",
        "selected_symbols": [
          "ALTUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 97,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-22",
        "decision_time_utc": "2026-05-22T00:00:00+00:00",
        "selected_symbols": [
          "ALLOUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "ALTUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
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
          "BNBUSDT",
          "ALLOUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-24",
        "decision_time_utc": "2026-05-24T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 97,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-25",
        "decision_time_utc": "2026-05-25T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 98,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-26",
        "decision_time_utc": "2026-05-26T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 98,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-27",
        "decision_time_utc": "2026-05-27T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 98,
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
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 97,
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
          "BNBUSDT",
          "BCHUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
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
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 97,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-31",
        "decision_time_utc": "2026-05-31T00:00:00+00:00",
        "selected_symbols": [
          "BNBUSDT",
          "ASTERUSDT",
          "BTCUSDT",
          "ALLOUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
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
          "BNBUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
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
