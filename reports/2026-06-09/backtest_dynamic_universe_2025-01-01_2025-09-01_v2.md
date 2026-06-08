---
created: 2026-06-09 00:58:18 CST
tags:
  - crypto
  - trading-system
  - backtest
backtest_run_id: e92bd90fdc7d
report_version: v2
sample_sufficient: true
universe_mode: true
universe_type: dynamic
---

# 回测报告 2025-01-01 至 2025-09-01 v2

- 回测 ID：`e92bd90fdc7d`
- 交易对：`1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1INCHUSDT`, `1MBABYDOGEUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACHUSDT`, `ACTUSDT`, `ACXUSDT`, `ADAUSDT`, `AEVOUSDT`, `AGLDUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALGOUSDT`, `ALPINEUSDT`, `ALTUSDT`, `AMPUSDT`, `ANIMEUSDT`, `ANKRUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARDRUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ASRUSDT`, `ATMUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AUDIOUSDT`, `AUSDT`, `AVAXUSDT`, `AXLUSDT`, `AXSUSDT`, `BABYUSDT`, `BANANAS31USDT`, `BANANAUSDT`, `BBUSDT`, `BCHUSDT`, `BEAMXUSDT`, `BERAUSDT`, `BIOUSDT`, `BMTUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BTCUSDT`, `C98USDT`, `CAKEUSDT`, `CATIUSDT`, `CETUSUSDT`, `CFXUSDT`, `CGPTUSDT`, `CKBUSDT`, `COMPUSDT`, `COOKIEUSDT`, `COWUSDT`
- UTC 区间：2025-01-01T00:00:00+00:00 -> 2025-09-01T00:00:00+00:00
- 初始权益：10,000.00 USDT
- 最终权益：9,216.01 USDT
- 净收益：-7.84%
- 代码 commit：`98bc2f824a4f5ffc71421db3446ea34dcb6973b5`
- 样本是否充分：true
- 样本提示：样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。
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
- Universe refreshes / Universe 刷新次数：244
- Selected symbols per refresh / 每次入选数量：min=2, avg=8.86, max=25
- Top selected symbols / 最常入选：`BNBUSDT`(244), `BTCUSDT`(244), `ADAUSDT`(240), `AVAXUSDT`(214), `AAVEUSDT`(182), `BONKUSDT`(132), `ARBUSDT`(122), `APTUSDT`(113), `BCHUSDT`(66), `AIXBTUSDT`(57)
- Filter counts / 过滤统计：
```json
{
  "missing_1h": 4025,
  "insufficient_24h": 15,
  "reconstruct_error": 0,
  "low_quote_volume": 18197,
  "low_trades": 2,
  "stable_like": 0
}
```
> Warning / 警告：dynamic universe 的 symbol master 来自当前 Binance exchangeInfo；历史上曾交易但今天已退市的币不会进入 master list，因此仍有退市幸存者偏差。
> Runtime / 耗时提示：第一次完整运行需要缓存大量 1h/4h/1d K 线，可能很慢；缓存命中后后续回测会明显加快。

## 核心指标

| Metric（指标） | Value（数值） |
|---|---:|
| Trades（计划总数） | 95 |
| Closed trades（已结束交易） | 29 |
| Open trades（仍开放持仓） | 2 |
| Win rate（胜率） | 20.69% |
| Profit factor（盈利因子） | 0.65 |
| Avg R（平均R倍数） | -0.26 |
| Net return（净收益率） | -7.84% |
| Max drawdown（最大回撤） | 1,637.62 / 15.99% |
| Intrabar max drawdown（K线内最大回撤） | 1,605.39 / 15.77% |
| TP1 touched rate（第一止盈触达率） | 24.14% |
| TP2 close rate（第二止盈平仓率） | 20.69% |
| Stop rate（止损率） | 79.31% |
| Fee drag（手续费拖累） | 36.96 USDT |
| Tail max single loss（最大单笔亏损） | -108.15 USDT |
| CAGR（年化复合收益率） | -11.54% |
| Sharpe（夏普比率） | -0.69 |
| Sortino（索提诺比率） | -0.77 |
| Exposure（持仓暴露时间） | 88.55% |
| Turnover（换手率） | 3.11 |
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
| Equal-weight symbols（等权持有本次币种） | -44.03% |

## 已结束交易

| Symbol（交易对） | Status（状态） | Created（创建时间） | Entry（入场价） | Exit（出场价） | Qty（数量） | Gross PnL（毛盈亏） | Net PnL（净盈亏） | Net R（净R倍数） | Fees（手续费） | Notes（备注） |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| `BTCUSDT` | STOPPED（已止损） | 2025-01-02T12:00:00+00:00 | 97,071.70 | 90,067.34 | 0.01 | -102.02 | -103.90 | -1.03 | 1.88 | Stop loss hit. |
| `BNBUSDT` | STOPPED（已止损） | 2025-01-04T00:00:00+00:00 | 712.59 | 685.89 | 3.91 | -104.35 | -108.15 | -1.06 | 3.79 | Stop loss hit. |
| `AAVEUSDT` | STOPPED（已止损） | 2025-01-04T04:00:00+00:00 | 340.44 | 301.35 | 2.59 | -101.39 | -102.53 | -1.02 | 1.13 | Stop loss hit. |
| `APTUSDT` | STOPPED（已止损） | 2025-01-05T04:00:00+00:00 | 9.75 | 8.97 | 131.80 | -101.83 | -103.52 | -1.03 | 1.70 | Stop loss hit. |
| `ADAUSDT` | STOPPED（已止损） | 2025-01-05T12:00:00+00:00 | 1.06 | 0.93 | 789.83 | -103.16 | -104.23 | -1.02 | 1.07 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-01-14T20:00:00+00:00 | 96,875.83 | 87,829.92 | 0.01 | -96.23 | -97.57 | -1.02 | 1.35 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-03-06T08:00:00+00:00 | 90,332.96 | 80,197.22 | 0.01 | -94.98 | -96.07 | -1.02 | 1.09 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-03-20T00:00:00+00:00 | 86,570.94 | 79,837.72 | 0.01 | -94.57 | -96.18 | -1.03 | 1.61 | Stop loss hit. |
| `BTCUSDT` | CLOSED（已按TP2平仓） | 2025-04-12T08:00:00+00:00 | 83,637.41 | 108,712.75 | 0.01 | 256.70 | 255.91 | 2.77 | 0.79 | TP2 hit; paper trade closed. |
| `BNBUSDT` | CLOSED（已按TP2平仓） | 2025-05-11T04:00:00+00:00 | 649.68 | 784.82 | 1.87 | 253.26 | 252.18 | 2.66 | 1.08 | TP2 hit; paper trade closed. |
| `ADAUSDT` | STOPPED（已止损） | 2025-05-11T12:00:00+00:00 | 0.80 | 0.70 | 1,002.58 | -95.08 | -96.11 | -1.02 | 1.03 | Stop loss hit. |
| `APTUSDT` | STOPPED（已止损） | 2025-05-11T16:00:00+00:00 | 5.83 | 5.08 | 128.07 | -95.13 | -96.08 | -1.02 | 0.95 | Stop loss hit. |
| `CAKEUSDT` | STOPPED（已止损） | 2025-05-11T16:00:00+00:00 | 2.41 | 2.14 | 353.28 | -95.34 | -96.44 | -1.02 | 1.10 | Stop loss hit. |
| `AAVEUSDT` | STOPPED（已止损） | 2025-05-22T12:00:00+00:00 | 255.84 | 214.03 | 2.25 | -93.92 | -94.63 | -1.01 | 0.71 | Stop loss hit. |
| `ARBUSDT` | STOPPED（已止损） | 2025-05-23T08:00:00+00:00 | 0.42 | 0.37 | 1,826.66 | -93.63 | -94.62 | -1.02 | 0.99 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-06-06T16:00:00+00:00 | 105,460.26 | 98,767.81 | 0.01 | -92.49 | -94.43 | -1.04 | 1.95 | Stop loss hit. |
| `AVAXUSDT` | STOPPED（已止损） | 2025-06-10T00:00:00+00:00 | 21.79 | 19.25 | 36.77 | -93.31 | -94.33 | -1.02 | 1.03 | Stop loss hit. |
| `ADAUSDT` | STOPPED（已止损） | 2025-06-10T00:00:00+00:00 | 0.71 | 0.64 | 1,383.24 | -94.54 | -95.82 | -1.02 | 1.28 | Stop loss hit. |
| `AAVEUSDT` | CLOSED（已按TP2平仓） | 2025-06-30T08:00:00+00:00 | 269.57 | 322.83 | 4.33 | 230.65 | 229.62 | 2.62 | 1.03 | TP2 hit; paper trade closed. |
| `ARBUSDT` | CLOSED（已按TP2平仓） | 2025-06-30T16:00:00+00:00 | 0.34 | 0.45 | 1,970.92 | 223.89 | 223.26 | 2.53 | 0.63 | TP2 hit; paper trade closed. |
| `APTUSDT` | STOPPED（已止损） | 2025-07-12T00:00:00+00:00 | 4.84 | 4.33 | 181.80 | -92.75 | -93.89 | -1.02 | 1.14 | Stop loss hit. |
| `COMPUSDT` | STOPPED（已止损） | 2025-07-15T00:00:00+00:00 | 48.95 | 44.40 | 20.96 | -95.40 | -96.74 | -1.02 | 1.34 | Stop loss hit. |
| `ARBUSDT` | STOPPED（已止损） | 2025-07-20T08:00:00+00:00 | 0.47 | 0.42 | 2,123.27 | -98.98 | -100.28 | -1.02 | 1.30 | Stop loss hit. |
| `BNBUSDT` | CLOSED（已按TP2平仓） | 2025-07-23T00:00:00+00:00 | 769.46 | 896.33 | 1.95 | 247.99 | 246.69 | 2.58 | 1.30 | TP2 hit; paper trade closed. |
| `CFXUSDT` | STOPPED（已止损） | 2025-07-31T08:00:00+00:00 | 0.21 | 0.18 | 3,027.88 | -94.27 | -95.06 | -1.01 | 0.79 | Stop loss hit. |
| `BCHUSDT` | STOPPED（已止损） | 2025-08-08T00:00:00+00:00 | 576.71 | 532.94 | 2.17 | -94.79 | -96.44 | -1.03 | 1.65 | Stop loss hit. |
| `ALPINEUSDT` | CLOSED（已按TP2平仓） | 2025-08-14T04:00:00+00:00 | 1.36 | 2.30 | 284.11 | 265.79 | 265.37 | 2.85 | 0.42 | TP2 hit; paper trade closed. |
| `ADAUSDT` | STOPPED（已止损） | 2025-08-15T20:00:00+00:00 | 0.93 | 0.82 | 854.66 | -96.47 | -97.49 | -1.02 | 1.02 | Stop loss hit. |
| `APTUSDT` | STOPPED（已止损） | 2025-08-23T00:00:00+00:00 | 4.69 | 4.20 | 200.16 | -97.39 | -98.61 | -1.02 | 1.22 | Stop loss hit. |

## 回测结束仍开放

| Symbol（交易对） | Status（状态） | Entry（入场价） | Qty（数量） | Unrealized Handling（未实现盈亏处理） | Notes（备注） |
|---|---|---:|---:|---|---|
| `BTCUSDT` | TP1_HIT（第一止盈已触达） | 105,613.24 | 0.01 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |
| `ARKUSDT` | ENTERED（已入场） | 0.46 | 1,086.04 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |

## 未入场/过期计划

| Symbol（交易对） | Status（状态） | Created（创建时间） | Entry Zone（入场区间） | Score（评分） | Notes（备注） |
|---|---|---|---:|---:|---|
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-01-04T12:00:00+00:00 | 40.15 - 40.76 | 72.48 | Backtest WATCHING plan expired before entry. |
| `AGLDUSDT` | INVALIDATED（未入场前失效） | 2025-01-06T00:00:00+00:00 | 2.74 - 2.77 | 54.01 | Plan invalidated before entry: current price is below stop loss. |
| `BONKUSDT` | INVALIDATED（未入场前失效） | 2025-01-06T16:00:00+00:00 | 0.00 - 0.00 | 56.17 | Plan invalidated before entry: current price is below stop loss. |
| `ARBUSDT` | INVALIDATED（未入场前失效） | 2025-01-07T00:00:00+00:00 | 0.89 - 0.91 | 76.00 | Plan invalidated before entry: current price is below stop loss. |
| `ALGOUSDT` | INVALIDATED（未入场前失效） | 2025-01-07T00:00:00+00:00 | 0.41 - 0.42 | 72.57 | Plan invalidated before entry: current price is below stop loss. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-05-11T16:00:00+00:00 | 23.58 - 24.13 | 77.80 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-05-12T16:00:00+00:00 | 0.00 - 0.00 | 80.84 | Backtest WATCHING plan expired before entry. |
| `AAVEUSDT` | EXPIRED（观察计划过期） | 2025-05-12T16:00:00+00:00 | 215.77 - 219.22 | 70.15 | Backtest WATCHING plan expired before entry. |
| `ARBUSDT` | INVALIDATED（未入场前失效） | 2025-05-14T04:00:00+00:00 | 0.43 - 0.45 | 79.05 | Plan invalidated before entry: current price is below stop loss. |
| `AAVEUSDT` | EXPIRED（观察计划过期） | 2025-05-16T04:00:00+00:00 | 225.63 - 230.16 | 56.79 | Backtest WATCHING plan expired before entry. |
| `APTUSDT` | EXPIRED（观察计划过期） | 2025-05-23T12:00:00+00:00 | 5.48 - 5.60 | 69.06 | Backtest WATCHING plan expired before entry. |
| `1000SATSUSDT` | EXPIRED（观察计划过期） | 2025-05-23T12:00:00+00:00 | 0.00 - 0.00 | 67.15 | Backtest WATCHING plan expired before entry. |
| `BCHUSDT` | EXPIRED（观察计划过期） | 2025-05-23T20:00:00+00:00 | 424.58 - 433.82 | 66.84 | Backtest WATCHING plan expired before entry. |
| `BTCUSDT` | EXPIRED（观察计划过期） | 2025-05-24T12:00:00+00:00 | 108,941.18 - 109,536.19 | 56.27 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | INVALIDATED（未入场前失效） | 2025-05-25T00:00:00+00:00 | 0.00 - 0.00 | 41.54 | Plan invalidated before entry: current price is below stop loss. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-05-26T04:00:00+00:00 | 0.00 - 0.00 | 49.18 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-05-26T04:00:00+00:00 | 23.34 - 23.44 | 36.07 | Backtest WATCHING plan expired before entry. |
| `BTCUSDT` | INVALIDATED（未入场前失效） | 2025-05-27T16:00:00+00:00 | 109,347.06 - 109,999.08 | 64.37 | Plan invalidated before entry: current price is below stop loss. |
| `BCHUSDT` | INVALIDATED（未入场前失效） | 2025-06-12T20:00:00+00:00 | 429.90 - 433.00 | 60.69 | Plan invalidated before entry: current price is below stop loss. |
| `BCHUSDT` | EXPIRED（观察计划过期） | 2025-07-01T00:00:00+00:00 | 499.10 - 504.88 | 64.61 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-07-03T00:00:00+00:00 | 18.43 - 18.57 | 61.42 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-07-03T08:00:00+00:00 | 0.59 - 0.60 | 66.10 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-07-04T16:00:00+00:00 | 0.00 - 0.00 | 71.04 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-07-07T00:00:00+00:00 | 0.58 - 0.58 | 49.98 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-07-08T20:00:00+00:00 | 0.00 - 0.00 | 84.85 | Backtest WATCHING plan expired before entry. |
| `BCHUSDT` | EXPIRED（观察计划过期） | 2025-07-11T00:00:00+00:00 | 508.00 - 512.65 | 65.30 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-07-12T16:00:00+00:00 | 0.00 - 0.00 | 75.65 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-07-13T00:00:00+00:00 | 20.31 - 20.70 | 57.91 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-07-14T12:00:00+00:00 | 0.72 - 0.74 | 74.57 | Backtest WATCHING plan expired before entry. |
| `AAVEUSDT` | EXPIRED（观察计划过期） | 2025-07-14T16:00:00+00:00 | 310.43 - 316.01 | 71.35 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-07-16T04:00:00+00:00 | 21.28 - 21.74 | 71.69 | Backtest WATCHING plan expired before entry. |
| `ARBUSDT` | EXPIRED（观察计划过期） | 2025-07-17T04:00:00+00:00 | 0.42 - 0.43 | 71.97 | Backtest WATCHING plan expired before entry. |
| `AAVEUSDT` | EXPIRED（观察计划过期） | 2025-07-18T04:00:00+00:00 | 321.92 - 328.91 | 64.28 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-07-18T16:00:00+00:00 | 0.79 - 0.82 | 76.32 | Backtest WATCHING plan expired before entry. |
| `CAKEUSDT` | EXPIRED（观察计划过期） | 2025-07-19T00:00:00+00:00 | 2.58 - 2.64 | 68.50 | Backtest WATCHING plan expired before entry. |
| `BCHUSDT` | EXPIRED（观察计划过期） | 2025-07-19T20:00:00+00:00 | 509.15 - 516.54 | 60.29 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-07-20T04:00:00+00:00 | 0.00 - 0.00 | 71.27 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-07-21T00:00:00+00:00 | 24.24 - 24.66 | 71.70 | Backtest WATCHING plan expired before entry. |
| `AAVEUSDT` | INVALIDATED（未入场前失效） | 2025-07-21T08:00:00+00:00 | 324.98 - 329.68 | 61.71 | Plan invalidated before entry: current price is below stop loss. |
| `ADAUSDT` | INVALIDATED（未入场前失效） | 2025-07-21T20:00:00+00:00 | 0.86 - 0.87 | 76.27 | Plan invalidated before entry: current price is below stop loss. |
| `BCHUSDT` | INVALIDATED（未入场前失效） | 2025-07-23T00:00:00+00:00 | 523.61 - 527.68 | 44.30 | Plan invalidated before entry: current price is below stop loss. |
| `BONKUSDT` | INVALIDATED（未入场前失效） | 2025-07-23T08:00:00+00:00 | 0.00 - 0.00 | 67.92 | Plan invalidated before entry: current price is below stop loss. |
| `CFXUSDT` | EXPIRED（观察计划过期） | 2025-07-24T08:00:00+00:00 | 0.18 - 0.18 | 57.69 | Backtest WATCHING plan expired before entry. |
| `BCHUSDT` | EXPIRED（观察计划过期） | 2025-07-24T16:00:00+00:00 | 520.12 - 523.27 | 60.23 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-07-26T00:00:00+00:00 | 0.00 - 0.00 | 66.50 | Backtest WATCHING plan expired before entry. |
| `CAKEUSDT` | EXPIRED（观察计划过期） | 2025-07-26T00:00:00+00:00 | 2.69 - 2.75 | 64.55 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-07-26T00:00:00+00:00 | 24.02 - 24.08 | 46.51 | Backtest WATCHING plan expired before entry. |
| `ARBUSDT` | EXPIRED（观察计划过期） | 2025-07-26T00:00:00+00:00 | 0.44 - 0.44 | 45.35 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-07-26T16:00:00+00:00 | 0.82 - 0.84 | 63.08 | Backtest WATCHING plan expired before entry. |
| `CFXUSDT` | EXPIRED（观察计划过期） | 2025-07-27T12:00:00+00:00 | 0.18 - 0.19 | 68.36 | Backtest WATCHING plan expired before entry. |
| `CKBUSDT` | INVALIDATED（未入场前失效） | 2025-07-30T00:00:00+00:00 | 0.01 - 0.01 | 57.54 | Plan invalidated before entry: current price is below stop loss. |
| `BCHUSDT` | INVALIDATED（未入场前失效） | 2025-07-30T16:00:00+00:00 | 570.12 - 571.01 | 50.29 | Plan invalidated before entry: current price is below stop loss. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-08-08T00:00:00+00:00 | 22.80 - 23.08 | 49.26 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-08-08T16:00:00+00:00 | 0.76 - 0.77 | 65.29 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-08-10T04:00:00+00:00 | 0.00 - 0.00 | 63.87 | Backtest WATCHING plan expired before entry. |
| `AAVEUSDT` | EXPIRED（观察计划过期） | 2025-08-10T08:00:00+00:00 | 291.23 - 295.48 | 73.60 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | INVALIDATED（未入场前失效） | 2025-08-11T04:00:00+00:00 | 23.79 - 24.13 | 62.86 | Plan invalidated before entry: current price is below stop loss. |
| `ARBUSDT` | EXPIRED（观察计划过期） | 2025-08-11T08:00:00+00:00 | 0.45 - 0.46 | 68.68 | Backtest WATCHING plan expired before entry. |
| `APTUSDT` | INVALIDATED（未入场前失效） | 2025-08-11T08:00:00+00:00 | 4.68 - 4.74 | 53.67 | Plan invalidated before entry: current price is below stop loss. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-08-12T16:00:00+00:00 | 0.79 - 0.81 | 65.38 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-08-12T16:00:00+00:00 | 23.58 - 23.99 | 62.85 | Backtest WATCHING plan expired before entry. |
| `APTUSDT` | EXPIRED（观察计划过期） | 2025-08-12T16:00:00+00:00 | 4.65 - 4.73 | 54.04 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | INVALIDATED（未入场前失效） | 2025-08-13T20:00:00+00:00 | 0.00 - 0.00 | 62.03 | Plan invalidated before entry: current price is below stop loss. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-08-23T04:00:00+00:00 | 861.81 - 871.06 | 71.00 | Backtest WATCHING plan expired before entry. |

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
| WARNING | `1000SATSUSDT` | 1h | Large wick/range candle. |
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
| WARNING | `1000SATSUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000SATSUSDT` | 1d | Large wick/range candle. |
| WARNING | `1000SATSUSDT` | 1d | Large wick/range candle. |
| WARNING | `1INCHUSDT` | 1d | Large wick/range candle. |
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
| WARNING | `AAVEUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACEUSDT` | 1h | Large wick/range candle. |
| WARNING | `ACEUSDT` | 1h | Large wick/range candle. |
| WARNING | `ACEUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACEUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACEUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACEUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACEUSDT` | 1d | Large wick/range candle. |
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
| INFO | n/a | n/a | Additional issues omitted: 724. |

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
    "min_history_days": 365,
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
    "created_at_utc": "2026-06-08T16:58:18+00:00",
    "refresh_frequency": "daily",
    "max_symbols": 30,
    "master_count": 100,
    "source_limit": 100,
    "source_limit_applied": true,
    "universe_refresh_count": 244,
    "selected_count_min": 2,
    "selected_count_avg": 8.85655737704918,
    "selected_count_max": 25,
    "top_selected_symbols": [
      {
        "symbol": "BNBUSDT",
        "days_selected": 244
      },
      {
        "symbol": "BTCUSDT",
        "days_selected": 244
      },
      {
        "symbol": "ADAUSDT",
        "days_selected": 240
      },
      {
        "symbol": "AVAXUSDT",
        "days_selected": 214
      },
      {
        "symbol": "AAVEUSDT",
        "days_selected": 182
      },
      {
        "symbol": "BONKUSDT",
        "days_selected": 132
      },
      {
        "symbol": "ARBUSDT",
        "days_selected": 122
      },
      {
        "symbol": "APTUSDT",
        "days_selected": 113
      },
      {
        "symbol": "BCHUSDT",
        "days_selected": 66
      },
      {
        "symbol": "AIXBTUSDT",
        "days_selected": 57
      },
      {
        "symbol": "ACTUSDT",
        "days_selected": 56
      },
      {
        "symbol": "BERAUSDT",
        "days_selected": 54
      },
      {
        "symbol": "CAKEUSDT",
        "days_selected": 52
      },
      {
        "symbol": "BIOUSDT",
        "days_selected": 41
      },
      {
        "symbol": "ALGOUSDT",
        "days_selected": 35
      },
      {
        "symbol": "1000SATSUSDT",
        "days_selected": 25
      },
      {
        "symbol": "CFXUSDT",
        "days_selected": 24
      },
      {
        "symbol": "BOMEUSDT",
        "days_selected": 22
      },
      {
        "symbol": "AUCTIONUSDT",
        "days_selected": 21
      },
      {
        "symbol": "ACHUSDT",
        "days_selected": 18
      }
    ],
    "filter_counts": {
      "missing_1h": 4025,
      "insufficient_24h": 15,
      "reconstruct_error": 0,
      "low_quote_volume": 18197,
      "low_trades": 2,
      "stable_like": 0
    },
    "selection_by_day": [
      {
        "date_utc": "2025-01-01",
        "decision_time_utc": "2025-01-01T04:00:00+00:00",
        "selected_symbols": [
          "ACTUSDT",
          "BTCUSDT",
          "ALGOUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "AGLDUSDT",
          "APTUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 27,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 63,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-02",
        "decision_time_utc": "2025-01-02T00:00:00+00:00",
        "selected_symbols": [
          "ALGOUSDT",
          "ADAUSDT",
          "AGLDUSDT",
          "AVAXUSDT",
          "ACTUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "BNBUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 27,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 63,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-03",
        "decision_time_utc": "2025-01-03T00:00:00+00:00",
        "selected_symbols": [
          "AIUSDT",
          "ACTUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ALGOUSDT",
          "ARBUSDT",
          "APTUSDT",
          "BNBUSDT",
          "AGLDUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 27,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 61,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-04",
        "decision_time_utc": "2025-01-04T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "BONKUSDT",
          "AGLDUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "ALGOUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 62,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-05",
        "decision_time_utc": "2025-01-05T00:00:00+00:00",
        "selected_symbols": [
          "ARBUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "BIOUSDT",
          "APTUSDT",
          "ADAUSDT",
          "COWUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "ACTUSDT",
          "ALGOUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 62,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-06",
        "decision_time_utc": "2025-01-06T00:00:00+00:00",
        "selected_symbols": [
          "ACTUSDT",
          "BIOUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "APTUSDT",
          "AGLDUSDT",
          "AAVEUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 63,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-07",
        "decision_time_utc": "2025-01-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "ALGOUSDT",
          "ADAUSDT",
          "BIOUSDT",
          "ARBUSDT",
          "APTUSDT",
          "ACTUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 63,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-08",
        "decision_time_utc": "2025-01-08T00:00:00+00:00",
        "selected_symbols": [
          "AIUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ACTUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "BIOUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "AAVEUSDT",
          "ALGOUSDT",
          "ATOMUSDT",
          "1000SATSUSDT",
          "1MBABYDOGEUSDT",
          "BCHUSDT",
          "BOMEUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 57,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-09",
        "decision_time_utc": "2025-01-09T00:00:00+00:00",
        "selected_symbols": [
          "ARKUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ACTUSDT",
          "AVAXUSDT",
          "BIOUSDT",
          "APTUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "1000SATSUSDT",
          "AIUSDT",
          "BONKUSDT",
          "ALGOUSDT",
          "BOMEUSDT",
          "ARKMUSDT",
          "CAKEUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 57,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-10",
        "decision_time_utc": "2025-01-10T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "1000SATSUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ACTUSDT",
          "BIOUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "ALGOUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 62,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-11",
        "decision_time_utc": "2025-01-11T00:00:00+00:00",
        "selected_symbols": [
          "AIUSDT",
          "ALGOUSDT",
          "BTCUSDT",
          "1000SATSUSDT",
          "APTUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "ARBUSDT",
          "BIOUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 3,
          "reconstruct_error": 0,
          "low_quote_volume": 61,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-12",
        "decision_time_utc": "2025-01-12T00:00:00+00:00",
        "selected_symbols": [
          "AGLDUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "CGPTUSDT",
          "BIOUSDT",
          "AIXBTUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 69,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-13",
        "decision_time_utc": "2025-01-13T00:00:00+00:00",
        "selected_symbols": [
          "CGPTUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "BIOUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 72,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-14",
        "decision_time_utc": "2025-01-14T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "CGPTUSDT",
          "ACTUSDT",
          "ARBUSDT",
          "BIOUSDT",
          "AIXBTUSDT",
          "BONKUSDT",
          "BOMEUSDT",
          "ALGOUSDT",
          "1000SATSUSDT",
          "ATOMUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 61,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-15",
        "decision_time_utc": "2025-01-15T00:00:00+00:00",
        "selected_symbols": [
          "AIXBTUSDT",
          "COWUSDT",
          "CGPTUSDT",
          "COOKIEUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "APTUSDT",
          "BIOUSDT",
          "ARBUSDT",
          "ACTUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 64,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-16",
        "decision_time_utc": "2025-01-16T00:00:00+00:00",
        "selected_symbols": [
          "AIXBTUSDT",
          "ALGOUSDT",
          "CGPTUSDT",
          "COOKIEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "ACTUSDT",
          "BIOUSDT",
          "APTUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 63,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-17",
        "decision_time_utc": "2025-01-17T00:00:00+00:00",
        "selected_symbols": [
          "AMPUSDT",
          "ALGOUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "AIXBTUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "CGPTUSDT",
          "ARBUSDT",
          "BCHUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "BIOUSDT",
          "ACTUSDT",
          "COOKIEUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 61,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-18",
        "decision_time_utc": "2025-01-18T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "AMPUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "ADAUSDT",
          "BCHUSDT",
          "APTUSDT",
          "ACTUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ALGOUSDT",
          "AIXBTUSDT",
          "CGPTUSDT",
          "BIOUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 62,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-19",
        "decision_time_utc": "2025-01-19T00:00:00+00:00",
        "selected_symbols": [
          "BNSOLUSDT",
          "BTCUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AIXBTUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "ACTUSDT",
          "ALGOUSDT",
          "APTUSDT",
          "BIOUSDT",
          "BOMEUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 62,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-20",
        "decision_time_utc": "2025-01-20T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "COWUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "AIXBTUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "ACTUSDT",
          "ALGOUSDT",
          "BOMEUSDT",
          "BNSOLUSDT",
          "1000SATSUSDT",
          "BIOUSDT",
          "BCHUSDT",
          "APEUSDT",
          "ARKMUSDT",
          "CGPTUSDT",
          "1MBABYDOGEUSDT",
          "ATOMUSDT",
          "CAKEUSDT",
          "COOKIEUSDT"
        ],
        "candidate_count": 24,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 53,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-21",
        "decision_time_utc": "2025-01-21T00:00:00+00:00",
        "selected_symbols": [
          "AAVEUSDT",
          "AIXBTUSDT",
          "ALGOUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "ACTUSDT",
          "ATOMUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "APTUSDT",
          "1000SATSUSDT",
          "APEUSDT",
          "ARBUSDT",
          "BOMEUSDT",
          "BCHUSDT",
          "COWUSDT",
          "ARKMUSDT",
          "BIOUSDT",
          "1MBABYDOGEUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 57,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-22",
        "decision_time_utc": "2025-01-22T00:00:00+00:00",
        "selected_symbols": [
          "AAVEUSDT",
          "BONKUSDT",
          "1000SATSUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "1MBABYDOGEUSDT",
          "BNBUSDT",
          "ARKMUSDT",
          "BOMEUSDT",
          "APTUSDT",
          "ADAUSDT",
          "AIXBTUSDT",
          "ALGOUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 62,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-23",
        "decision_time_utc": "2025-01-23T00:00:00+00:00",
        "selected_symbols": [
          "AIXBTUSDT",
          "COOKIEUSDT",
          "ACTUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "AAVEUSDT",
          "BIOUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "CGPTUSDT",
          "ARBUSDT",
          "ALGOUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 63,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-24",
        "decision_time_utc": "2025-01-24T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "1000SATSUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ACTUSDT",
          "AIXBTUSDT",
          "ALGOUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "APTUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 64,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-25",
        "decision_time_utc": "2025-01-25T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ACTUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "AIXBTUSDT",
          "BONKUSDT",
          "APTUSDT",
          "ARBUSDT",
          "ALGOUSDT",
          "ANIMEUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 66,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-26",
        "decision_time_utc": "2025-01-26T00:00:00+00:00",
        "selected_symbols": [
          "1000SATSUSDT",
          "ACTUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ANIMEUSDT",
          "AIXBTUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 67,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-27",
        "decision_time_utc": "2025-01-27T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AIXBTUSDT",
          "AAVEUSDT",
          "ANIMEUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 70,
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
          "BTCUSDT",
          "BNBUSDT",
          "ACTUSDT",
          "ADAUSDT",
          "ALGOUSDT",
          "AVAXUSDT",
          "AIXBTUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "BONKUSDT",
          "ARBUSDT",
          "BOMEUSDT",
          "ARKMUSDT",
          "ANIMEUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 62,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-29",
        "decision_time_utc": "2025-01-29T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ACHUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "AIXBTUSDT",
          "BONKUSDT",
          "ARBUSDT",
          "APTUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 68,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-30",
        "decision_time_utc": "2025-01-30T00:00:00+00:00",
        "selected_symbols": [
          "ACTUSDT",
          "ACHUSDT",
          "1000SATSUSDT",
          "BOMEUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "AIXBTUSDT",
          "ADAUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 65,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-31",
        "decision_time_utc": "2025-01-31T00:00:00+00:00",
        "selected_symbols": [
          "ACHUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "AIXBTUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 68,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-01",
        "decision_time_utc": "2025-02-01T00:00:00+00:00",
        "selected_symbols": [
          "ACTUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "ACHUSDT",
          "ARBUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "AIXBTUSDT",
          "BONKUSDT",
          "ANIMEUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 66,
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
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "AIXBTUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 67,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-03",
        "decision_time_utc": "2025-02-03T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "1000SATSUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ACTUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "AIXBTUSDT",
          "ALGOUSDT",
          "BCHUSDT",
          "BOMEUSDT",
          "ARKMUSDT",
          "ATOMUSDT",
          "ARPAUSDT",
          "ACHUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 60,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-04",
        "decision_time_utc": "2025-02-04T00:00:00+00:00",
        "selected_symbols": [
          "ACTUSDT",
          "BTCUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "ALGOUSDT",
          "BONKUSDT",
          "1000SATSUSDT",
          "AIXBTUSDT",
          "ATOMUSDT",
          "BCHUSDT",
          "ARBUSDT",
          "BIOUSDT",
          "ACEUSDT",
          "CFXUSDT",
          "ACHUSDT",
          "BOMEUSDT",
          "ANIMEUSDT",
          "APEUSDT",
          "ARUSDT",
          "ARKMUSDT",
          "CAKEUSDT",
          "AEVOUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 53,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-05",
        "decision_time_utc": "2025-02-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "ARBUSDT",
          "ACTUSDT",
          "ACHUSDT",
          "AIXBTUSDT",
          "BONKUSDT",
          "ALGOUSDT",
          "ARKMUSDT",
          "1000SATSUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 64,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-06",
        "decision_time_utc": "2025-02-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ACTUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "ARBUSDT",
          "ACHUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 68,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-07",
        "decision_time_utc": "2025-02-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ACTUSDT",
          "AIXBTUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 21,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 69,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-08",
        "decision_time_utc": "2025-02-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "BERAUSDT",
          "ADAUSDT",
          "ACTUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "AIXBTUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 21,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 69,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-09",
        "decision_time_utc": "2025-02-09T00:00:00+00:00",
        "selected_symbols": [
          "CAKEUSDT",
          "1000CATUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "APTUSDT",
          "BERAUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ARKMUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 21,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 70,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-10",
        "decision_time_utc": "2025-02-10T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "CAKEUSDT",
          "BNBUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "BERAUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 71,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-11",
        "decision_time_utc": "2025-02-11T00:00:00+00:00",
        "selected_symbols": [
          "1000CHEEMSUSDT",
          "COOKIEUSDT",
          "AIXBTUSDT",
          "CAKEUSDT",
          "APTUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "BERAUSDT",
          "BNBUSDT",
          "ARKMUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 68,
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
          "CAKEUSDT",
          "BNBUSDT",
          "ARKMUSDT",
          "BTCUSDT",
          "1000CHEEMSUSDT",
          "AIXBTUSDT",
          "BONKUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 68,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-13",
        "decision_time_utc": "2025-02-13T00:00:00+00:00",
        "selected_symbols": [
          "CAKEUSDT",
          "1000CHEEMSUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "ALGOUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "ARKMUSDT",
          "BERAUSDT",
          "AIXBTUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 66,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-14",
        "decision_time_utc": "2025-02-14T00:00:00+00:00",
        "selected_symbols": [
          "AUCTIONUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "CAKEUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "BERAUSDT",
          "AIXBTUSDT",
          "1000CATUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 69,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-15",
        "decision_time_utc": "2025-02-15T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "AIXBTUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "CAKEUSDT",
          "ADAUSDT",
          "APTUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 71,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-16",
        "decision_time_utc": "2025-02-16T00:00:00+00:00",
        "selected_symbols": [
          "CAKEUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 76,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-17",
        "decision_time_utc": "2025-02-17T00:00:00+00:00",
        "selected_symbols": [
          "CAKEUSDT",
          "ACHUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 75,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-18",
        "decision_time_utc": "2025-02-18T00:00:00+00:00",
        "selected_symbols": [
          "ACHUSDT",
          "BERAUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "APTUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "CAKEUSDT",
          "ARKUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 70,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-19",
        "decision_time_utc": "2025-02-19T00:00:00+00:00",
        "selected_symbols": [
          "ACHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "BERAUSDT",
          "ADAUSDT",
          "CAKEUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 70,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-20",
        "decision_time_utc": "2025-02-20T00:00:00+00:00",
        "selected_symbols": [
          "ARKUSDT",
          "APTUSDT",
          "CAKEUSDT",
          "BERAUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ACHUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 70,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-21",
        "decision_time_utc": "2025-02-21T00:00:00+00:00",
        "selected_symbols": [
          "BERAUSDT",
          "ACHUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "CAKEUSDT",
          "APTUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 70,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-22",
        "decision_time_utc": "2025-02-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ACTUSDT",
          "AIXBTUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BERAUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "CAKEUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "ARKMUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 68,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-23",
        "decision_time_utc": "2025-02-23T00:00:00+00:00",
        "selected_symbols": [
          "AIXBTUSDT",
          "ACTUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "CAKEUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "BERAUSDT",
          "APTUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 70,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-24",
        "decision_time_utc": "2025-02-24T00:00:00+00:00",
        "selected_symbols": [
          "ANIMEUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BERAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 74,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-25",
        "decision_time_utc": "2025-02-25T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BERAUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "AIXBTUSDT",
          "ARKMUSDT",
          "CAKEUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 69,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-26",
        "decision_time_utc": "2025-02-26T00:00:00+00:00",
        "selected_symbols": [
          "ACTUSDT",
          "AIXBTUSDT",
          "COWUSDT",
          "BTCUSDT",
          "APTUSDT",
          "BNBUSDT",
          "ARBUSDT",
          "ARKMUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BERAUSDT",
          "CAKEUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 66,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-27",
        "decision_time_utc": "2025-02-27T00:00:00+00:00",
        "selected_symbols": [
          "BERAUSDT",
          "ACTUSDT",
          "1000SATSUSDT",
          "AIXBTUSDT",
          "APTUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "COWUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 69,
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
          "AVAXUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 73,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-01",
        "decision_time_utc": "2025-03-01T00:00:00+00:00",
        "selected_symbols": [
          "CKBUSDT",
          "ACTUSDT",
          "BERAUSDT",
          "BCHUSDT",
          "APTUSDT",
          "BTCUSDT",
          "AIXBTUSDT",
          "BONKUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "1000SATSUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 66,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-02",
        "decision_time_utc": "2025-03-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BERAUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 73,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-03",
        "decision_time_utc": "2025-03-03T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "AIXBTUSDT",
          "ALGOUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "APTUSDT",
          "BCHUSDT",
          "CAKEUSDT",
          "BNBUSDT",
          "BERAUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 66,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-04",
        "decision_time_utc": "2025-03-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "BERAUSDT",
          "ARBUSDT",
          "CAKEUSDT",
          "ALGOUSDT",
          "AIXBTUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 67,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-05",
        "decision_time_utc": "2025-03-05T00:00:00+00:00",
        "selected_symbols": [
          "AAVEUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ACTUSDT",
          "APTUSDT",
          "BERAUSDT",
          "ARBUSDT",
          "ALGOUSDT",
          "BONKUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 68,
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
          "AVAXUSDT",
          "ARBUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "BERAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 71,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-07",
        "decision_time_utc": "2025-03-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "BERAUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 73,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-08",
        "decision_time_utc": "2025-03-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "APTUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BCHUSDT",
          "BERAUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 71,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-09",
        "decision_time_utc": "2025-03-09T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 75,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-10",
        "decision_time_utc": "2025-03-10T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 75,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-11",
        "decision_time_utc": "2025-03-11T00:00:00+00:00",
        "selected_symbols": [
          "AUCTIONUSDT",
          "BTCUSDT",
          "AUDIOUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "BERAUSDT",
          "ARBUSDT",
          "BCHUSDT",
          "C98USDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 68,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-12",
        "decision_time_utc": "2025-03-12T00:00:00+00:00",
        "selected_symbols": [
          "AUCTIONUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BANANAUSDT",
          "C98USDT",
          "BNBUSDT",
          "ARBUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "ARKMUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 69,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-13",
        "decision_time_utc": "2025-03-13T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AUCTIONUSDT",
          "BANANAUSDT",
          "APTUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 71,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-14",
        "decision_time_utc": "2025-03-14T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "AUCTIONUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 74,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-15",
        "decision_time_utc": "2025-03-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AUCTIONUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 74,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-16",
        "decision_time_utc": "2025-03-16T00:00:00+00:00",
        "selected_symbols": [
          "CAKEUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "BTCUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 74,
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
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "CAKEUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 74,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-18",
        "decision_time_utc": "2025-03-18T00:00:00+00:00",
        "selected_symbols": [
          "CAKEUSDT",
          "API3USDT",
          "1000CHEEMSUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "AUCTIONUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 72,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-19",
        "decision_time_utc": "2025-03-19T00:00:00+00:00",
        "selected_symbols": [
          "AUCTIONUSDT",
          "CAKEUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "API3USDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 19,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 73,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-20",
        "decision_time_utc": "2025-03-20T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AUCTIONUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "CAKEUSDT",
          "BMTUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 19,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 73,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-21",
        "decision_time_utc": "2025-03-21T00:00:00+00:00",
        "selected_symbols": [
          "BANANAUSDT",
          "AUCTIONUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "CAKEUSDT",
          "BMTUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 19,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 72,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-22",
        "decision_time_utc": "2025-03-22T00:00:00+00:00",
        "selected_symbols": [
          "CAKEUSDT",
          "ACHUSDT",
          "BERAUSDT",
          "AUCTIONUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 19,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 74,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-23",
        "decision_time_utc": "2025-03-23T00:00:00+00:00",
        "selected_symbols": [
          "API3USDT",
          "BEAMXUSDT",
          "BANANAUSDT",
          "BTCUSDT",
          "CAKEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ACXUSDT",
          "AUCTIONUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 19,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 72,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-24",
        "decision_time_utc": "2025-03-24T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "BTCUSDT",
          "API3USDT",
          "ADAUSDT",
          "BNBUSDT",
          "CAKEUSDT",
          "AUCTIONUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 19,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 74,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-25",
        "decision_time_utc": "2025-03-25T00:00:00+00:00",
        "selected_symbols": [
          "BERAUSDT",
          "ANKRUSDT",
          "AIXBTUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "BOMEUSDT",
          "ADAUSDT",
          "AUCTIONUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "CAKEUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 19,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 70,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-26",
        "decision_time_utc": "2025-03-26T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "BERAUSDT",
          "CAKEUSDT",
          "AUCTIONUSDT",
          "1000SATSUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 19,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 73,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-27",
        "decision_time_utc": "2025-03-27T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "1000SATSUSDT",
          "CAKEUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BERAUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 19,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 72,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-28",
        "decision_time_utc": "2025-03-28T00:00:00+00:00",
        "selected_symbols": [
          "BERAUSDT",
          "BNBUSDT",
          "CAKEUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "1000SATSUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 2,
          "reconstruct_error": 0,
          "low_quote_volume": 74,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-29",
        "decision_time_utc": "2025-03-29T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AUCTIONUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BERAUSDT",
          "AVAXUSDT",
          "CAKEUSDT",
          "API3USDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 75,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-30",
        "decision_time_utc": "2025-03-30T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BERAUSDT",
          "AVAXUSDT",
          "AUCTIONUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 76,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-31",
        "decision_time_utc": "2025-03-31T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-01",
        "decision_time_utc": "2025-04-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BERAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 78,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-02",
        "decision_time_utc": "2025-04-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AVAXUSDT",
          "BERAUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "COMPUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 76,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-03",
        "decision_time_utc": "2025-04-03T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "BERAUSDT",
          "1000SATSUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 74,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-04",
        "decision_time_utc": "2025-04-04T00:00:00+00:00",
        "selected_symbols": [
          "ACTUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BERAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 77,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-05",
        "decision_time_utc": "2025-04-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "BERAUSDT",
          "APTUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 77,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-06",
        "decision_time_utc": "2025-04-06T00:00:00+00:00",
        "selected_symbols": [
          "AUCTIONUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-07",
        "decision_time_utc": "2025-04-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AUCTIONUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 78,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-08",
        "decision_time_utc": "2025-04-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AVAXUSDT",
          "ACTUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "BNBUSDT",
          "APTUSDT",
          "BERAUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 74,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-09",
        "decision_time_utc": "2025-04-09T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BERAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 77,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-10",
        "decision_time_utc": "2025-04-10T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "APTUSDT",
          "BNBUSDT",
          "BERAUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 75,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-11",
        "decision_time_utc": "2025-04-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BERAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 16,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 77,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-12",
        "decision_time_utc": "2025-04-12T00:00:00+00:00",
        "selected_symbols": [
          "BABYUSDT",
          "BTCUSDT",
          "BERAUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 77,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-13",
        "decision_time_utc": "2025-04-13T00:00:00+00:00",
        "selected_symbols": [
          "ARKUSDT",
          "BABYUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-14",
        "decision_time_utc": "2025-04-14T00:00:00+00:00",
        "selected_symbols": [
          "COWUSDT",
          "BTCUSDT",
          "BABYUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-15",
        "decision_time_utc": "2025-04-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BABYUSDT",
          "BCHUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 78,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-16",
        "decision_time_utc": "2025-04-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ACHUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "BABYUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-17",
        "decision_time_utc": "2025-04-17T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ARDRUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BABYUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-18",
        "decision_time_utc": "2025-04-18T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-19",
        "decision_time_utc": "2025-04-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 82,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-20",
        "decision_time_utc": "2025-04-20T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 83,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-21",
        "decision_time_utc": "2025-04-21T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 82,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-22",
        "decision_time_utc": "2025-04-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-23",
        "decision_time_utc": "2025-04-23T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "APTUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 78,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-24",
        "decision_time_utc": "2025-04-24T00:00:00+00:00",
        "selected_symbols": [
          "AIXBTUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 77,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-25",
        "decision_time_utc": "2025-04-25T00:00:00+00:00",
        "selected_symbols": [
          "ARDRUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "BONKUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 77,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-26",
        "decision_time_utc": "2025-04-26T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "AIXBTUSDT",
          "BTCUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "CETUSUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 76,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-27",
        "decision_time_utc": "2025-04-27T00:00:00+00:00",
        "selected_symbols": [
          "AIXBTUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-28",
        "decision_time_utc": "2025-04-28T00:00:00+00:00",
        "selected_symbols": [
          "BMTUSDT",
          "BTCUSDT",
          "BONKUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-29",
        "decision_time_utc": "2025-04-29T00:00:00+00:00",
        "selected_symbols": [
          "AIXBTUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 78,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-30",
        "decision_time_utc": "2025-04-30T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-01",
        "decision_time_utc": "2025-05-01T00:00:00+00:00",
        "selected_symbols": [
          "BABYUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-02",
        "decision_time_utc": "2025-05-02T00:00:00+00:00",
        "selected_symbols": [
          "AIXBTUSDT",
          "BEAMXUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 77,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-03",
        "decision_time_utc": "2025-05-03T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AIXBTUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-04",
        "decision_time_utc": "2025-05-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 82,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-05",
        "decision_time_utc": "2025-05-05T00:00:00+00:00",
        "selected_symbols": [
          "ASRUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-06",
        "decision_time_utc": "2025-05-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BONKUSDT",
          "BNBUSDT",
          "AIXBTUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-07",
        "decision_time_utc": "2025-05-07T00:00:00+00:00",
        "selected_symbols": [
          "ALPINEUSDT",
          "ASRUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-08",
        "decision_time_utc": "2025-05-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-09",
        "decision_time_utc": "2025-05-09T00:00:00+00:00",
        "selected_symbols": [
          "AAVEUSDT",
          "BERAUSDT",
          "BONKUSDT",
          "AIXBTUSDT",
          "ARBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "BCHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 75,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-10",
        "decision_time_utc": "2025-05-10T00:00:00+00:00",
        "selected_symbols": [
          "BOMEUSDT",
          "ACTUSDT",
          "BONKUSDT",
          "AIXBTUSDT",
          "BERAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "APTUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 72,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-11",
        "decision_time_utc": "2025-05-11T00:00:00+00:00",
        "selected_symbols": [
          "ARBUSDT",
          "BERAUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "CAKEUSDT",
          "1000CATUSDT",
          "AIXBTUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 72,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-12",
        "decision_time_utc": "2025-05-12T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ACTUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "APTUSDT",
          "BERAUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 75,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-13",
        "decision_time_utc": "2025-05-13T00:00:00+00:00",
        "selected_symbols": [
          "ACTUSDT",
          "CATIUSDT",
          "BOMEUSDT",
          "BTCUSDT",
          "AIXBTUSDT",
          "BONKUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "CAKEUSDT",
          "BERAUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 71,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-14",
        "decision_time_utc": "2025-05-14T00:00:00+00:00",
        "selected_symbols": [
          "BOMEUSDT",
          "1MBABYDOGEUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 74,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-15",
        "decision_time_utc": "2025-05-15T00:00:00+00:00",
        "selected_symbols": [
          "1000SATSUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "AVAXUSDT",
          "BOMEUSDT",
          "ARBUSDT",
          "ACTUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 75,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-16",
        "decision_time_utc": "2025-05-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "BOMEUSDT",
          "1000SATSUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 75,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-17",
        "decision_time_utc": "2025-05-17T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 78,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-18",
        "decision_time_utc": "2025-05-18T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-19",
        "decision_time_utc": "2025-05-19T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 78,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-20",
        "decision_time_utc": "2025-05-20T00:00:00+00:00",
        "selected_symbols": [
          "AAVEUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-21",
        "decision_time_utc": "2025-05-21T00:00:00+00:00",
        "selected_symbols": [
          "AAVEUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-22",
        "decision_time_utc": "2025-05-22T00:00:00+00:00",
        "selected_symbols": [
          "COOKIEUSDT",
          "1000SATSUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ARBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 76,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-23",
        "decision_time_utc": "2025-05-23T00:00:00+00:00",
        "selected_symbols": [
          "COOKIEUSDT",
          "BONKUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "APTUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "1000SATSUSDT",
          "CETUSUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 74,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-24",
        "decision_time_utc": "2025-05-24T00:00:00+00:00",
        "selected_symbols": [
          "COOKIEUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "BCHUSDT",
          "APTUSDT",
          "CETUSUSDT",
          "BOMEUSDT",
          "ARKMUSDT",
          "1000SATSUSDT",
          "AIXBTUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 71,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-25",
        "decision_time_utc": "2025-05-25T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-26",
        "decision_time_utc": "2025-05-26T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-27",
        "decision_time_utc": "2025-05-27T00:00:00+00:00",
        "selected_symbols": [
          "AIXBTUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "COOKIEUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 78,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-28",
        "decision_time_utc": "2025-05-28T00:00:00+00:00",
        "selected_symbols": [
          "CETUSUSDT",
          "AIXBTUSDT",
          "CAKEUSDT",
          "COOKIEUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 77,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-29",
        "decision_time_utc": "2025-05-29T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "CAKEUSDT",
          "CETUSUSDT",
          "AIXBTUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 78,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-30",
        "decision_time_utc": "2025-05-30T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "CAKEUSDT"
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
        "date_utc": "2025-05-31",
        "decision_time_utc": "2025-05-31T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "APTUSDT",
          "CAKEUSDT",
          "BONKUSDT",
          "AIXBTUSDT"
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
        "date_utc": "2025-06-01",
        "decision_time_utc": "2025-06-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "AVAXUSDT",
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
