---
created: 2026-06-09 14:33:24 CST
tags:
  - crypto
  - trading-system
  - backtest
backtest_run_id: c431a48d0643
report_version: v5
sample_sufficient: false
universe_mode: true
universe_type: dynamic
---

# 回测报告 2025-01-01 至 2025-06-01 v5

- 回测 ID：`c431a48d0643`
- 交易对：`1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1MBABYDOGEUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACHUSDT`, `ACTUSDT`, `ACXUSDT`, `ADAUSDT`, `AEVOUSDT`, `AGLDUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALGOUSDT`, `ALPINEUSDT`, `AMPUSDT`, `ANIMEUSDT`, `ANKRUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARDRUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ASRUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AUDIOUSDT`, `AVAXUSDT`, `BABYUSDT`, `BANANAUSDT`, `BCHUSDT`, `BEAMXUSDT`, `BERAUSDT`, `BIOUSDT`, `BMTUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BTCUSDT`, `C98USDT`, `CAKEUSDT`, `CATIUSDT`, `CETUSUSDT`, `CFXUSDT`, `CGPTUSDT`, `CKBUSDT`, `COMPUSDT`, `COOKIEUSDT`, `COWUSDT`, `CRVUSDT`, `CVCUSDT`, `DEXEUSDT`, `DOGEUSDT`, `DOGSUSDT`, `DOTUSDT`, `DUSDT`, `DYDXUSDT`, `DYMUSDT`, `EGLDUSDT`, `EIGENUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `FETUSDT`, `FIDAUSDT`, `FILUSDT`, `FLOKIUSDT`, `FORMUSDT`, `FTTUSDT`, `GALAUSDT`, `GASUSDT`
- UTC 区间：2025-01-01T00:00:00+00:00 -> 2025-06-01T00:00:00+00:00
- 初始权益：10,000.00 USDT
- 最终权益：8,877.42 USDT
- 净收益：-11.23%
- 代码 commit：`c330af5b5b1c8691611578c246f5405ead0ece2d`
- 样本是否充分：false
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
- Master symbols / Master 币种数：150
- Source limit / 调试截断：150
- Source limit applied / 是否截断：true
- Refresh frequency / 刷新频率：daily
- Universe refreshes / Universe 刷新次数：152
- Selected symbols per refresh / 每次入选数量：min=4, avg=15.37, max=40
- Top selected symbols / 最常入选：`BNBUSDT`(152), `BTCUSDT`(152), `DOGEUSDT`(152), `ETHUSDT`(152), `ADAUSDT`(150), `ENAUSDT`(141), `AVAXUSDT`(137), `AAVEUSDT`(105), `CRVUSDT`(79), `BONKUSDT`(77)
- Filter counts / 过滤统计：
```json
{
  "missing_1h": 4679,
  "insufficient_24h": 17,
  "reconstruct_error": 0,
  "low_quote_volume": 15768,
  "low_trades": 0,
  "stable_like": 0
}
```
> Warning / 警告：dynamic universe 的 symbol master 来自当前 Binance exchangeInfo；历史上曾交易但今天已退市的币不会进入 master list，因此仍有退市幸存者偏差。
> Runtime / 耗时提示：第一次完整运行需要缓存大量 1h/4h/1d K 线，可能很慢；缓存命中后后续回测会明显加快。

## 核心指标

| Metric（指标） | Value（数值） |
|---|---:|
| Trades（计划总数） | 71 |
| Closed trades（已结束交易） | 19 |
| Open trades（仍开放持仓） | 2 |
| Win rate（胜率） | 10.53% |
| Profit factor（盈利因子） | 0.29 |
| Avg R（平均R倍数） | -0.64 |
| Net return（净收益率） | -11.23% |
| Max drawdown（最大回撤） | 1,490.08 / 14.48% |
| Intrabar max drawdown（K线内最大回撤） | 1,398.46 / 13.71% |
| TP1 touched rate（第一止盈触达率） | 21.05% |
| TP2 close rate（第二止盈平仓率） | 10.53% |
| Stop rate（止损率） | 89.47% |
| Fee drag（手续费拖累） | 27.01 USDT |
| Tail max single loss（最大单笔亏损） | -108.74 USDT |
| CAGR（年化复合收益率） | -25.01% |
| Sharpe（夏普比率） | -1.90 |
| Sortino（索提诺比率） | -1.84 |
| Exposure（持仓暴露时间） | 81.57% |
| Turnover（换手率） | 2.26 |
| Sample sufficient（样本是否充分） | false |

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
| BTC buy-hold（买入并持有BTC） | 11.35% |
| ETH buy-hold（买入并持有ETH） | -24.73% |
| Cash（现金不交易） | 0.00% |
| Equal-weight symbols（等权持有本次币种） | -47.06% |

## 已结束交易

| Symbol（交易对） | Status（状态） | Created（创建时间） | Entry（入场价） | Exit（出场价） | Qty（数量） | Gross PnL（毛盈亏） | Net PnL（净盈亏） | Net R（净R倍数） | Fees（手续费） | Notes（备注） |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| `ETHUSDT` | STOPPED（已止损） | 2025-01-02T12:00:00+00:00 | 3,483.33 | 3,252.17 | 0.44 | -102.21 | -104.26 | -1.03 | 2.05 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-01-02T12:00:00+00:00 | 97,071.70 | 90,067.34 | 0.01 | -101.92 | -103.80 | -1.03 | 1.88 | Stop loss hit. |
| `BNBUSDT` | STOPPED（已止损） | 2025-01-04T00:00:00+00:00 | 712.59 | 685.89 | 3.93 | -104.92 | -108.74 | -1.06 | 3.82 | Stop loss hit. |
| `AAVEUSDT` | STOPPED（已止损） | 2025-01-04T04:00:00+00:00 | 340.44 | 301.35 | 2.61 | -101.88 | -103.02 | -1.02 | 1.14 | Stop loss hit. |
| `APTUSDT` | STOPPED（已止损） | 2025-01-05T04:00:00+00:00 | 9.75 | 8.97 | 127.41 | -98.44 | -100.08 | -1.03 | 1.64 | Stop loss hit. |
| `GALAUSDT` | STOPPED（已止损） | 2025-01-06T04:00:00+00:00 | 0.04 | 0.04 | 26,929.25 | -102.96 | -104.45 | -1.02 | 1.49 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-01-14T20:00:00+00:00 | 96,875.83 | 87,829.92 | 0.01 | -95.19 | -96.52 | -1.02 | 1.33 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-01-16T08:00:00+00:00 | 3,396.15 | 2,873.32 | 0.18 | -95.02 | -95.79 | -1.01 | 0.77 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-02-20T08:00:00+00:00 | 2,739.78 | 2,563.79 | 0.54 | -94.95 | -96.93 | -1.04 | 1.97 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-03-06T08:00:00+00:00 | 90,332.96 | 80,197.22 | 0.01 | -92.00 | -93.06 | -1.02 | 1.06 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-03-20T00:00:00+00:00 | 86,570.94 | 79,837.72 | 0.01 | -91.61 | -93.17 | -1.03 | 1.56 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-03-20T04:00:00+00:00 | 1,991.87 | 1,842.38 | 0.61 | -91.52 | -93.14 | -1.03 | 1.62 | Stop loss hit. |
| `BTCUSDT` | CLOSED（已按TP2平仓） | 2025-04-12T08:00:00+00:00 | 83,637.41 | 108,712.75 | 0.01 | 246.06 | 245.30 | 2.77 | 0.75 | TP2 hit; paper trade closed. |
| `ETHUSDT` | CLOSED（已按TP2平仓） | 2025-04-25T20:00:00+00:00 | 1,781.57 | 2,078.51 | 0.78 | 231.33 | 230.13 | 2.56 | 1.20 | TP2 hit; paper trade closed. |
| `ACTUSDT` | STOPPED（已止损） | 2025-05-11T04:00:00+00:00 | 0.06 | 0.05 | 8,572.91 | -93.01 | -93.66 | -1.01 | 0.65 | Stop loss hit. |
| `ADAUSDT` | STOPPED（已止损） | 2025-05-11T12:00:00+00:00 | 0.80 | 0.70 | 986.64 | -93.57 | -94.58 | -1.02 | 1.01 | Stop loss hit. |
| `FETUSDT` | STOPPED（已止损） | 2025-05-11T16:00:00+00:00 | 0.85 | 0.73 | 779.58 | -93.41 | -94.25 | -1.02 | 0.83 | Stop loss hit. |
| `APTUSDT` | STOPPED（已止损） | 2025-05-11T16:00:00+00:00 | 5.83 | 5.08 | 125.99 | -93.59 | -94.52 | -1.02 | 0.93 | Stop loss hit. |
| `1000SATSUSDT` | STOPPED（已止损） | 2025-05-23T12:00:00+00:00 | 0.00 | 0.00 | 7,848,041.98 | -92.90 | -93.45 | -1.01 | 0.55 | Stop loss hit. |

## 回测结束仍开放

| Symbol（交易对） | Status（状态） | Entry（入场价） | Qty（数量） | Unrealized Handling（未实现盈亏处理） | Notes（备注） |
|---|---|---:|---:|---|---|
| `AAVEUSDT` | TP1_HIT（第一止盈已触达） | 230.27 | 3.92 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |
| `ETHUSDT` | ENTERED（已入场） | 2,527.64 | 0.38 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |

## 未入场/过期计划

| Symbol（交易对） | Status（状态） | Created（创建时间） | Entry Zone（入场区间） | Score（评分） | Notes（备注） |
|---|---|---|---:|---:|---|
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-01-04T12:00:00+00:00 | 40.15 - 40.76 | 72.48 | Backtest WATCHING plan expired before entry. |
| `DOTUSDT` | EXPIRED（观察计划过期） | 2025-01-04T12:00:00+00:00 | 7.45 - 7.57 | 72.30 | Backtest WATCHING plan expired before entry. |
| `FILUSDT` | EXPIRED（观察计划过期） | 2025-01-04T12:00:00+00:00 | 5.43 - 5.51 | 68.25 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-01-05T12:00:00+00:00 | 1.04 - 1.06 | 70.76 | Backtest WATCHING plan expired before entry. |
| `DOGEUSDT` | EXPIRED（观察计划过期） | 2025-01-05T16:00:00+00:00 | 0.37 - 0.38 | 69.12 | Backtest WATCHING plan expired before entry. |
| `FLOKIUSDT` | INVALIDATED（未入场前失效） | 2025-01-05T16:00:00+00:00 | 0.00 - 0.00 | 54.99 | Plan invalidated before entry: current price is below stop loss. |
| `FETUSDT` | INVALIDATED（未入场前失效） | 2025-01-05T16:00:00+00:00 | 1.46 - 1.48 | 51.03 | Plan invalidated before entry: current price is below stop loss. |
| `AGLDUSDT` | INVALIDATED（未入场前失效） | 2025-01-06T00:00:00+00:00 | 2.74 - 2.77 | 54.01 | Plan invalidated before entry: current price is below stop loss. |
| `BONKUSDT` | INVALIDATED（未入场前失效） | 2025-01-06T16:00:00+00:00 | 0.00 - 0.00 | 56.17 | Plan invalidated before entry: current price is below stop loss. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-04-22T16:00:00+00:00 | 1,657.99 - 1,682.01 | 65.88 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-05-11T04:00:00+00:00 | 641.66 - 649.35 | 65.46 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-05-11T16:00:00+00:00 | 23.58 - 24.13 | 77.80 | Backtest WATCHING plan expired before entry. |
| `CAKEUSDT` | EXPIRED（观察计划过期） | 2025-05-11T16:00:00+00:00 | 2.35 - 2.41 | 72.71 | Backtest WATCHING plan expired before entry. |
| `DOGEUSDT` | EXPIRED（观察计划过期） | 2025-05-12T16:00:00+00:00 | 0.23 - 0.23 | 86.14 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-05-12T16:00:00+00:00 | 2,424.67 - 2,480.54 | 82.20 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-05-12T16:00:00+00:00 | 0.00 - 0.00 | 80.84 | Backtest WATCHING plan expired before entry. |
| `DOTUSDT` | EXPIRED（观察计划过期） | 2025-05-12T16:00:00+00:00 | 4.98 - 5.11 | 75.70 | Backtest WATCHING plan expired before entry. |
| `AAVEUSDT` | EXPIRED（观察计划过期） | 2025-05-12T16:00:00+00:00 | 215.77 - 219.22 | 70.15 | Backtest WATCHING plan expired before entry. |
| `FLOKIUSDT` | EXPIRED（观察计划过期） | 2025-05-12T20:00:00+00:00 | 0.00 - 0.00 | 88.10 | Backtest WATCHING plan expired before entry. |
| `GALAUSDT` | EXPIRED（观察计划过期） | 2025-05-13T00:00:00+00:00 | 0.02 - 0.02 | 79.62 | Backtest WATCHING plan expired before entry. |
| `ARBUSDT` | INVALIDATED（未入场前失效） | 2025-05-14T08:00:00+00:00 | 0.44 - 0.44 | 69.34 | Plan invalidated before entry: current price is below stop loss. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-05-15T16:00:00+00:00 | 655.00 - 657.37 | 57.38 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | INVALIDATED（未入场前失效） | 2025-05-16T04:00:00+00:00 | 2,558.21 - 2,589.09 | 56.00 | Plan invalidated before entry: current price is below stop loss. |
| `DOGEUSDT` | EXPIRED（观察计划过期） | 2025-05-16T08:00:00+00:00 | 0.22 - 0.23 | 37.66 | Backtest WATCHING plan expired before entry. |
| `ENAUSDT` | INVALIDATED（未入场前失效） | 2025-05-16T08:00:00+00:00 | 0.38 - 0.38 | 35.35 | Plan invalidated before entry: current price is below stop loss. |
| `DOTUSDT` | INVALIDATED（未入场前失效） | 2025-05-16T12:00:00+00:00 | 4.94 - 4.95 | 45.15 | Plan invalidated before entry: current price is below stop loss. |
| `ETHFIUSDT` | EXPIRED（观察计划过期） | 2025-05-18T08:00:00+00:00 | 1.32 - 1.33 | 56.51 | Backtest WATCHING plan expired before entry. |
| `DOGEUSDT` | EXPIRED（观察计划过期） | 2025-05-20T04:00:00+00:00 | 0.22 - 0.23 | 64.45 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-05-20T04:00:00+00:00 | 647.50 - 652.06 | 59.89 | Backtest WATCHING plan expired before entry. |
| `ENAUSDT` | EXPIRED（观察计划过期） | 2025-05-20T04:00:00+00:00 | 0.37 - 0.39 | 54.07 | Backtest WATCHING plan expired before entry. |
| `ETHFIUSDT` | EXPIRED（观察计划过期） | 2025-05-21T16:00:00+00:00 | 1.30 - 1.32 | 58.56 | Backtest WATCHING plan expired before entry. |
| `CRVUSDT` | EXPIRED（观察计划过期） | 2025-05-22T00:00:00+00:00 | 0.72 - 0.74 | 60.92 | Backtest WATCHING plan expired before entry. |
| `DOTUSDT` | EXPIRED（观察计划过期） | 2025-05-22T08:00:00+00:00 | 4.73 - 4.81 | 47.13 | Backtest WATCHING plan expired before entry. |
| `DOGEUSDT` | EXPIRED（观察计划过期） | 2025-05-23T08:00:00+00:00 | 0.24 - 0.24 | 70.51 | Backtest WATCHING plan expired before entry. |
| `ARBUSDT` | EXPIRED（观察计划过期） | 2025-05-23T08:00:00+00:00 | 0.42 - 0.42 | 65.40 | Backtest WATCHING plan expired before entry. |
| `APTUSDT` | EXPIRED（观察计划过期） | 2025-05-23T12:00:00+00:00 | 5.48 - 5.60 | 69.06 | Backtest WATCHING plan expired before entry. |
| `BCHUSDT` | EXPIRED（观察计划过期） | 2025-05-23T20:00:00+00:00 | 424.58 - 433.82 | 66.84 | Backtest WATCHING plan expired before entry. |
| `BTCUSDT` | EXPIRED（观察计划过期） | 2025-05-24T12:00:00+00:00 | 108,941.18 - 109,536.19 | 56.27 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-05-24T12:00:00+00:00 | 670.52 - 676.06 | 53.11 | Backtest WATCHING plan expired before entry. |
| `FETUSDT` | EXPIRED（观察计划过期） | 2025-05-25T00:00:00+00:00 | 0.82 - 0.86 | 42.21 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | INVALIDATED（未入场前失效） | 2025-05-25T00:00:00+00:00 | 0.00 - 0.00 | 41.54 | Plan invalidated before entry: current price is below stop loss. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-05-26T04:00:00+00:00 | 0.00 - 0.00 | 49.18 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-05-26T04:00:00+00:00 | 23.34 - 23.44 | 36.07 | Backtest WATCHING plan expired before entry. |
| `ENAUSDT` | EXPIRED（观察计划过期） | 2025-05-26T04:00:00+00:00 | 0.38 - 0.38 | 35.35 | Backtest WATCHING plan expired before entry. |
| `DOGEUSDT` | EXPIRED（观察计划过期） | 2025-05-26T12:00:00+00:00 | 0.22 - 0.22 | 42.54 | Backtest WATCHING plan expired before entry. |
| `BTCUSDT` | INVALIDATED（未入场前失效） | 2025-05-27T16:00:00+00:00 | 109,347.06 - 109,999.08 | 64.37 | Plan invalidated before entry: current price is below stop loss. |
| `CRVUSDT` | INVALIDATED（未入场前失效） | 2025-05-28T00:00:00+00:00 | 0.74 - 0.75 | 46.32 | Plan invalidated before entry: current price is below stop loss. |
| `BNBUSDT` | INVALIDATED（未入场前失效） | 2025-05-28T04:00:00+00:00 | 679.18 - 682.44 | 59.85 | Plan invalidated before entry: current price is below stop loss. |
| `FETUSDT` | INVALIDATED（未入场前失效） | 2025-05-29T00:00:00+00:00 | 0.88 - 0.91 | 62.42 | Plan invalidated before entry: current price is below stop loss. |
| `ETHFIUSDT` | INVALIDATED（未入场前失效） | 2025-05-29T16:00:00+00:00 | 1.37 - 1.37 | 67.40 | Plan invalidated before entry: current price is below stop loss. |

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
| WARNING | `1000CHEEMSUSDT` | 1h | Large wick/range candle. |
| WARNING | `1000CHEEMSUSDT` | 4h | Large wick/range candle. |
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
| WARNING | `ACHUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACHUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACHUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACHUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACHUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACHUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACMUSDT` | 1h | Large wick/range candle. |
| WARNING | `ACMUSDT` | 1h | Large wick/range candle. |
| WARNING | `ACMUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACMUSDT` | 4h | Large wick/range candle. |
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
| WARNING | `ACTUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACTUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACTUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACTUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACTUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACXUSDT` | 1h | Large wick/range candle. |
| WARNING | `ACXUSDT` | 1h | Large wick/range candle. |
| WARNING | `ACXUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACXUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACXUSDT` | 4h | Large wick/range candle. |
| INFO | n/a | n/a | Additional issues omitted: 627. |

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
    "created_at_utc": "2026-06-09T06:33:24+00:00",
    "refresh_frequency": "daily",
    "max_symbols": 40,
    "master_count": 150,
    "source_limit": 150,
    "source_limit_applied": true,
    "universe_refresh_count": 152,
    "selected_count_min": 4,
    "selected_count_avg": 15.368421052631579,
    "selected_count_max": 40,
    "top_selected_symbols": [
      {
        "symbol": "BNBUSDT",
        "days_selected": 152
      },
      {
        "symbol": "BTCUSDT",
        "days_selected": 152
      },
      {
        "symbol": "DOGEUSDT",
        "days_selected": 152
      },
      {
        "symbol": "ETHUSDT",
        "days_selected": 152
      },
      {
        "symbol": "ADAUSDT",
        "days_selected": 150
      },
      {
        "symbol": "ENAUSDT",
        "days_selected": 141
      },
      {
        "symbol": "AVAXUSDT",
        "days_selected": 137
      },
      {
        "symbol": "AAVEUSDT",
        "days_selected": 105
      },
      {
        "symbol": "CRVUSDT",
        "days_selected": 79
      },
      {
        "symbol": "BONKUSDT",
        "days_selected": 77
      },
      {
        "symbol": "APTUSDT",
        "days_selected": 76
      },
      {
        "symbol": "DOTUSDT",
        "days_selected": 70
      },
      {
        "symbol": "FETUSDT",
        "days_selected": 70
      },
      {
        "symbol": "FLOKIUSDT",
        "days_selected": 67
      },
      {
        "symbol": "ARBUSDT",
        "days_selected": 64
      },
      {
        "symbol": "ACTUSDT",
        "days_selected": 56
      },
      {
        "symbol": "AIXBTUSDT",
        "days_selected": 56
      },
      {
        "symbol": "BERAUSDT",
        "days_selected": 49
      },
      {
        "symbol": "ETHFIUSDT",
        "days_selected": 44
      },
      {
        "symbol": "CAKEUSDT",
        "days_selected": 42
      }
    ],
    "filter_counts": {
      "missing_1h": 4679,
      "insufficient_24h": 17,
      "reconstruct_error": 0,
      "low_quote_volume": 15768,
      "low_trades": 0,
      "stable_like": 0
    },
    "selection_by_day": [
      {
        "date_utc": "2025-01-01",
        "decision_time_utc": "2025-01-01T04:00:00+00:00",
        "selected_symbols": [
          "ACTUSDT",
          "FLOKIUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ALGOUSDT",
          "ETHUSDT",
          "ETHFIUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "FETUSDT",
          "CRVUSDT",
          "AAVEUSDT",
          "ENAUSDT",
          "BONKUSDT",
          "AGLDUSDT",
          "EIGENUSDT",
          "APTUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 41,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 91,
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
          "GALAUSDT",
          "CRVUSDT",
          "AGLDUSDT",
          "DOTUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "ACTUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "ETHUSDT",
          "APTUSDT",
          "FILUSDT",
          "BNBUSDT",
          "FLOKIUSDT",
          "BONKUSDT",
          "CVCUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 41,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-03",
        "decision_time_utc": "2025-01-03T00:00:00+00:00",
        "selected_symbols": [
          "AIUSDT",
          "DEXEUSDT",
          "ACTUSDT",
          "ENAUSDT",
          "BONKUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "GALAUSDT",
          "ADAUSDT",
          "CRVUSDT",
          "FETUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ALGOUSDT",
          "ARBUSDT",
          "FLOKIUSDT",
          "FILUSDT",
          "APTUSDT",
          "DOTUSDT",
          "BNBUSDT",
          "AGLDUSDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 41,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 87,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-04",
        "decision_time_utc": "2025-01-04T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "BONKUSDT",
          "GALAUSDT",
          "AGLDUSDT",
          "FLOKIUSDT",
          "DOTUSDT",
          "FETUSDT",
          "ETHUSDT",
          "CRVUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "EIGENUSDT",
          "ALGOUSDT",
          "FILUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 21,
        "filter_counts": {
          "missing_1h": 40,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 88,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-05",
        "decision_time_utc": "2025-01-05T00:00:00+00:00",
        "selected_symbols": [
          "ARBUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "BIOUSDT",
          "APTUSDT",
          "ADAUSDT",
          "COWUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "GALAUSDT",
          "FLOKIUSDT",
          "BONKUSDT",
          "ACTUSDT",
          "DOTUSDT",
          "CRVUSDT",
          "FETUSDT",
          "ALGOUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 40,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-06",
        "decision_time_utc": "2025-01-06T00:00:00+00:00",
        "selected_symbols": [
          "ACTUSDT",
          "FETUSDT",
          "BIOUSDT",
          "FILUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "APTUSDT",
          "AGLDUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "FLOKIUSDT",
          "GALAUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 40,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 92,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-07",
        "decision_time_utc": "2025-01-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "GALAUSDT",
          "BONKUSDT",
          "ALGOUSDT",
          "FILUSDT",
          "ADAUSDT",
          "DOTUSDT",
          "BIOUSDT",
          "FLOKIUSDT",
          "ENAUSDT",
          "ARBUSDT",
          "APTUSDT",
          "ACTUSDT",
          "FETUSDT",
          "CRVUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 40,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
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
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ACTUSDT",
          "ENAUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "BIOUSDT",
          "FETUSDT",
          "DOTUSDT",
          "GALAUSDT",
          "FILUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "AAVEUSDT",
          "ALGOUSDT",
          "FLOKIUSDT",
          "CRVUSDT",
          "ATOMUSDT",
          "EIGENUSDT",
          "ETHFIUSDT",
          "ETCUSDT",
          "1000SATSUSDT",
          "1MBABYDOGEUSDT",
          "BCHUSDT",
          "BOMEUSDT"
        ],
        "candidate_count": 29,
        "filter_counts": {
          "missing_1h": 40,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-09",
        "decision_time_utc": "2025-01-09T00:00:00+00:00",
        "selected_symbols": [
          "GASUSDT",
          "ARKUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "ACTUSDT",
          "AVAXUSDT",
          "BIOUSDT",
          "FETUSDT",
          "APTUSDT",
          "DOTUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "GALAUSDT",
          "FILUSDT",
          "FLOKIUSDT",
          "1000SATSUSDT",
          "AIUSDT",
          "BONKUSDT",
          "CRVUSDT",
          "EIGENUSDT",
          "ALGOUSDT",
          "ETHFIUSDT",
          "BOMEUSDT",
          "ARKMUSDT",
          "CAKEUSDT"
        ],
        "candidate_count": 29,
        "filter_counts": {
          "missing_1h": 40,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
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
          "1000SATSUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "FETUSDT",
          "ACTUSDT",
          "BIOUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "GALAUSDT",
          "APTUSDT",
          "FILUSDT",
          "ARBUSDT",
          "FLOKIUSDT",
          "DOTUSDT",
          "CRVUSDT",
          "BONKUSDT",
          "ALGOUSDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 39,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 88,
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
          "DOGEUSDT",
          "1000SATSUSDT",
          "APTUSDT",
          "ETHUSDT",
          "GALAUSDT",
          "ADAUSDT",
          "FILUSDT",
          "FETUSDT",
          "DOTUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "AAVEUSDT",
          "CRVUSDT",
          "FLOKIUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "ARBUSDT",
          "BIOUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 36,
          "insufficient_24h": 3,
          "reconstruct_error": 0,
          "low_quote_volume": 89,
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
          "DOGEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "GALAUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "CGPTUSDT",
          "BIOUSDT",
          "AIXBTUSDT",
          "FETUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 36,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 101,
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
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "BIOUSDT",
          "FETUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 36,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 105,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-14",
        "decision_time_utc": "2025-01-14T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "AAVEUSDT",
          "FETUSDT",
          "AVAXUSDT",
          "GALAUSDT",
          "APTUSDT",
          "CGPTUSDT",
          "ACTUSDT",
          "ARBUSDT",
          "FILUSDT",
          "DOTUSDT",
          "CRVUSDT",
          "BIOUSDT",
          "FLOKIUSDT",
          "AIXBTUSDT",
          "EIGENUSDT",
          "BONKUSDT",
          "BOMEUSDT",
          "ALGOUSDT",
          "ETHFIUSDT",
          "1000SATSUSDT",
          "ATOMUSDT"
        ],
        "candidate_count": 27,
        "filter_counts": {
          "missing_1h": 36,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 87,
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
          "GALAUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "CRVUSDT",
          "ETHUSDT",
          "APTUSDT",
          "BIOUSDT",
          "ENAUSDT",
          "ARBUSDT",
          "FETUSDT",
          "ACTUSDT",
          "DOTUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 36,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
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
          "ENAUSDT",
          "CRVUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "CGPTUSDT",
          "COOKIEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "FILUSDT",
          "BTCUSDT",
          "GALAUSDT",
          "DOTUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "FLOKIUSDT",
          "ACTUSDT",
          "BIOUSDT",
          "FETUSDT",
          "APTUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 23,
        "filter_counts": {
          "missing_1h": 36,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 91,
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
          "ETHUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "AIXBTUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "DOTUSDT",
          "APTUSDT",
          "FILUSDT",
          "FETUSDT",
          "CRVUSDT",
          "GALAUSDT",
          "CGPTUSDT",
          "ARBUSDT",
          "BCHUSDT",
          "AAVEUSDT",
          "FLOKIUSDT",
          "BONKUSDT",
          "BIOUSDT",
          "ACTUSDT",
          "COOKIEUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 36,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 89,
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
          "DOGEUSDT",
          "CRVUSDT",
          "FLOKIUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "GALAUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "BCHUSDT",
          "APTUSDT",
          "FETUSDT",
          "ACTUSDT",
          "DOTUSDT",
          "FILUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ALGOUSDT",
          "AIXBTUSDT",
          "CGPTUSDT",
          "BIOUSDT"
        ],
        "candidate_count": 24,
        "filter_counts": {
          "missing_1h": 36,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-19",
        "decision_time_utc": "2025-01-19T00:00:00+00:00",
        "selected_symbols": [
          "BNSOLUSDT",
          "FIDAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "AIXBTUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "FILUSDT",
          "CRVUSDT",
          "ARBUSDT",
          "ACTUSDT",
          "FLOKIUSDT",
          "GALAUSDT",
          "FETUSDT",
          "DOTUSDT",
          "ALGOUSDT",
          "APTUSDT",
          "BIOUSDT",
          "BOMEUSDT",
          "BCHUSDT",
          "EIGENUSDT",
          "ETHFIUSDT"
        ],
        "candidate_count": 27,
        "filter_counts": {
          "missing_1h": 36,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 87,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-20",
        "decision_time_utc": "2025-01-20T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "COWUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "BONKUSDT",
          "AIXBTUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "FETUSDT",
          "DOTUSDT",
          "FLOKIUSDT",
          "FIDAUSDT",
          "CRVUSDT",
          "FILUSDT",
          "GALAUSDT",
          "ACTUSDT",
          "ENSUSDT",
          "ALGOUSDT",
          "BOMEUSDT",
          "EIGENUSDT",
          "ETHFIUSDT",
          "ETCUSDT",
          "BNSOLUSDT",
          "1000SATSUSDT",
          "BIOUSDT",
          "BCHUSDT",
          "APEUSDT",
          "ARKMUSDT",
          "DYDXUSDT",
          "CGPTUSDT",
          "1MBABYDOGEUSDT",
          "ATOMUSDT",
          "CAKEUSDT",
          "COOKIEUSDT"
        ],
        "candidate_count": 39,
        "filter_counts": {
          "missing_1h": 36,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 75,
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
          "ETHUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "CRVUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "FILUSDT",
          "ACTUSDT",
          "DOTUSDT",
          "ATOMUSDT",
          "ENSUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "FETUSDT",
          "BONKUSDT",
          "APTUSDT",
          "1000SATSUSDT",
          "EIGENUSDT",
          "ETCUSDT",
          "APEUSDT",
          "ARBUSDT",
          "BOMEUSDT",
          "BCHUSDT",
          "FLOKIUSDT",
          "GALAUSDT",
          "COWUSDT",
          "ETHFIUSDT",
          "ARKMUSDT",
          "BIOUSDT",
          "FIDAUSDT",
          "DYDXUSDT",
          "1MBABYDOGEUSDT",
          "DOGSUSDT"
        ],
        "candidate_count": 36,
        "filter_counts": {
          "missing_1h": 36,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 78,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-22",
        "decision_time_utc": "2025-01-22T00:00:00+00:00",
        "selected_symbols": [
          "AAVEUSDT",
          "FETUSDT",
          "BONKUSDT",
          "1000SATSUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "ETCUSDT",
          "GALAUSDT",
          "DOTUSDT",
          "FLOKIUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "1MBABYDOGEUSDT",
          "BNBUSDT",
          "FILUSDT",
          "ARKMUSDT",
          "BOMEUSDT",
          "APTUSDT",
          "ETHFIUSDT",
          "ADAUSDT",
          "AIXBTUSDT",
          "CRVUSDT",
          "ALGOUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 26,
        "filter_counts": {
          "missing_1h": 36,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 88,
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
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "BONKUSDT",
          "AAVEUSDT",
          "BIOUSDT",
          "AVAXUSDT",
          "FETUSDT",
          "APTUSDT",
          "CGPTUSDT",
          "ARBUSDT",
          "ALGOUSDT",
          "FLOKIUSDT",
          "GALAUSDT",
          "FILUSDT",
          "CRVUSDT",
          "DOTUSDT"
        ],
        "candidate_count": 23,
        "filter_counts": {
          "missing_1h": 36,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 91,
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
          "ARBUSDT",
          "1000SATSUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ACTUSDT",
          "ENAUSDT",
          "AIXBTUSDT",
          "FILUSDT",
          "ALGOUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "CRVUSDT",
          "BONKUSDT",
          "FETUSDT",
          "APTUSDT",
          "FLOKIUSDT",
          "GALAUSDT",
          "DOTUSDT"
        ],
        "candidate_count": 23,
        "filter_counts": {
          "missing_1h": 35,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 91,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-25",
        "decision_time_utc": "2025-01-25T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "ACTUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "EIGENUSDT",
          "AVAXUSDT",
          "AIXBTUSDT",
          "BONKUSDT",
          "CRVUSDT",
          "APTUSDT",
          "ARBUSDT",
          "FETUSDT",
          "ETCUSDT",
          "ETHFIUSDT",
          "ALGOUSDT",
          "FLOKIUSDT",
          "ANIMEUSDT"
        ],
        "candidate_count": 21,
        "filter_counts": {
          "missing_1h": 35,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
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
          "ETHUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ANIMEUSDT",
          "AIXBTUSDT",
          "CRVUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 35,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 100,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-27",
        "decision_time_utc": "2025-01-27T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AIXBTUSDT",
          "AAVEUSDT",
          "ANIMEUSDT",
          "BONKUSDT",
          "FETUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 35,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 103,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-28",
        "decision_time_utc": "2025-01-28T00:00:00+00:00",
        "selected_symbols": [
          "ACHUSDT",
          "DUSDT",
          "CFXUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ACTUSDT",
          "ADAUSDT",
          "ALGOUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "AIXBTUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "BONKUSDT",
          "ARBUSDT",
          "DOTUSDT",
          "FLOKIUSDT",
          "FETUSDT",
          "FILUSDT",
          "GALAUSDT",
          "CRVUSDT",
          "EIGENUSDT",
          "ETCUSDT",
          "BOMEUSDT",
          "ARKMUSDT",
          "ANIMEUSDT"
        ],
        "candidate_count": 28,
        "filter_counts": {
          "missing_1h": 35,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 87,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-29",
        "decision_time_utc": "2025-01-29T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "FLOKIUSDT",
          "ACHUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "FETUSDT",
          "AIXBTUSDT",
          "GALAUSDT",
          "BONKUSDT",
          "ARBUSDT",
          "APTUSDT",
          "CRVUSDT",
          "DUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 35,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 97,
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
          "FLOKIUSDT",
          "EIGENUSDT",
          "BOMEUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "AIXBTUSDT",
          "GALAUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "CRVUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ARBUSDT",
          "FETUSDT",
          "DOTUSDT",
          "DEXEUSDT"
        ],
        "candidate_count": 23,
        "filter_counts": {
          "missing_1h": 35,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 92,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-31",
        "decision_time_utc": "2025-01-31T00:00:00+00:00",
        "selected_symbols": [
          "ACHUSDT",
          "ENAUSDT",
          "CRVUSDT",
          "AAVEUSDT",
          "ETHUSDT",
          "EIGENUSDT",
          "DOTUSDT",
          "APTUSDT",
          "FETUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "ARBUSDT",
          "AIXBTUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "FLOKIUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 35,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 97,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-01",
        "decision_time_utc": "2025-02-01T00:00:00+00:00",
        "selected_symbols": [
          "FLOKIUSDT",
          "ACTUSDT",
          "EIGENUSDT",
          "AAVEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ACHUSDT",
          "DOTUSDT",
          "GALAUSDT",
          "ARBUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "ETCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "AIXBTUSDT",
          "BONKUSDT",
          "ANIMEUSDT",
          "CRVUSDT",
          "FETUSDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 35,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
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
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "DOTUSDT",
          "AIXBTUSDT",
          "CRVUSDT",
          "FLOKIUSDT",
          "BONKUSDT",
          "EIGENUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 35,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 97,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-03",
        "decision_time_utc": "2025-02-03T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "1000SATSUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "ACTUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "FETUSDT",
          "DOTUSDT",
          "CRVUSDT",
          "ARBUSDT",
          "FILUSDT",
          "FLOKIUSDT",
          "BONKUSDT",
          "EIGENUSDT",
          "AIXBTUSDT",
          "ALGOUSDT",
          "GALAUSDT",
          "ETHFIUSDT",
          "ETCUSDT",
          "BCHUSDT",
          "BOMEUSDT",
          "ARKMUSDT",
          "ATOMUSDT",
          "DYDXUSDT",
          "ARPAUSDT",
          "ACHUSDT"
        ],
        "candidate_count": 31,
        "filter_counts": {
          "missing_1h": 35,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 84,
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
          "BTCUSDT",
          "DOGEUSDT",
          "APTUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "ALGOUSDT",
          "FETUSDT",
          "DOTUSDT",
          "BONKUSDT",
          "1000SATSUSDT",
          "AIXBTUSDT",
          "ATOMUSDT",
          "FILUSDT",
          "EGLDUSDT",
          "ETCUSDT",
          "BCHUSDT",
          "ARBUSDT",
          "BIOUSDT",
          "CRVUSDT",
          "ACEUSDT",
          "GALAUSDT",
          "FLOKIUSDT",
          "CFXUSDT",
          "ENSUSDT",
          "ACHUSDT",
          "BOMEUSDT",
          "ANIMEUSDT",
          "APEUSDT",
          "ARUSDT",
          "ARKMUSDT",
          "CAKEUSDT",
          "DYDXUSDT",
          "AEVOUSDT",
          "ADAUSDT",
          "EIGENUSDT",
          "ETHFIUSDT"
        ],
        "candidate_count": 40,
        "filter_counts": {
          "missing_1h": 35,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 75,
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
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "ARBUSDT",
          "DOTUSDT",
          "ACTUSDT",
          "ACHUSDT",
          "FLOKIUSDT",
          "AIXBTUSDT",
          "FETUSDT",
          "ETHFIUSDT",
          "FILUSDT",
          "CRVUSDT",
          "BONKUSDT",
          "GALAUSDT",
          "EIGENUSDT",
          "ALGOUSDT",
          "ARKMUSDT",
          "ETCUSDT",
          "1000SATSUSDT"
        ],
        "candidate_count": 26,
        "filter_counts": {
          "missing_1h": 35,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 89,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-06",
        "decision_time_utc": "2025-02-06T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "ACTUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "ARBUSDT",
          "ETHFIUSDT",
          "ACHUSDT",
          "FLOKIUSDT",
          "CRVUSDT",
          "DOTUSDT",
          "FETUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 35,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 97,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-07",
        "decision_time_utc": "2025-02-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "FLOKIUSDT",
          "ACTUSDT",
          "AIXBTUSDT",
          "ARBUSDT",
          "ETHFIUSDT",
          "FETUSDT",
          "DOTUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 34,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 99,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-08",
        "decision_time_utc": "2025-02-08T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOTUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "FETUSDT",
          "BERAUSDT",
          "ADAUSDT",
          "CRVUSDT",
          "ACTUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ETHFIUSDT",
          "ARBUSDT",
          "AIXBTUSDT",
          "FLOKIUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 34,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 98,
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
          "ENAUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "APTUSDT",
          "BERAUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ARKMUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 34,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 104,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-10",
        "decision_time_utc": "2025-02-10T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "CAKEUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "FLOKIUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "BERAUSDT",
          "ENAUSDT",
          "DOTUSDT",
          "EIGENUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 102,
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
          "ETHUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "BERAUSDT",
          "BNBUSDT",
          "ARKMUSDT",
          "DOTUSDT",
          "ENAUSDT",
          "CRVUSDT",
          "FLOKIUSDT",
          "FETUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 98,
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
          "ETHUSDT",
          "1000CHEEMSUSDT",
          "AIXBTUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "BONKUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "DOTUSDT",
          "CRVUSDT",
          "FLOKIUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 99,
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
          "DOTUSDT",
          "ETHUSDT",
          "FLOKIUSDT",
          "ETHFIUSDT",
          "FETUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "DOGEUSDT",
          "GALAUSDT",
          "ALGOUSDT",
          "EIGENUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "CRVUSDT",
          "FILUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "ENAUSDT",
          "ARKMUSDT",
          "BERAUSDT",
          "AIXBTUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 92,
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
          "ETHUSDT",
          "ADAUSDT",
          "CAKEUSDT",
          "DOGEUSDT",
          "AAVEUSDT",
          "ENAUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "BERAUSDT",
          "AIXBTUSDT",
          "1000CATUSDT",
          "FLOKIUSDT",
          "DOTUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 101,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-15",
        "decision_time_utc": "2025-02-15T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "BONKUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "FLOKIUSDT",
          "AIXBTUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "CAKEUSDT",
          "ADAUSDT",
          "DOTUSDT",
          "ETHFIUSDT",
          "APTUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 102,
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
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 110,
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
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 109,
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
          "ETHUSDT",
          "EIGENUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "ETHFIUSDT",
          "BTCUSDT",
          "APTUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "CAKEUSDT",
          "ARKUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 102,
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
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "BERAUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "CAKEUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "EIGENUSDT",
          "DOTUSDT",
          "FLOKIUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 101,
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
          "ETHUSDT",
          "ADAUSDT",
          "FLOKIUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "ACHUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 103,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-21",
        "decision_time_utc": "2025-02-21T00:00:00+00:00",
        "selected_symbols": [
          "BERAUSDT",
          "EIGENUSDT",
          "ACHUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "ETHUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "DOTUSDT",
          "FLOKIUSDT",
          "BNBUSDT",
          "CAKEUSDT",
          "DOGEUSDT",
          "APTUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 101,
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
          "ACTUSDT",
          "AIXBTUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BERAUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "EIGENUSDT",
          "DOTUSDT",
          "CAKEUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "FLOKIUSDT",
          "FETUSDT",
          "ETHFIUSDT",
          "ARKMUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 97,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-23",
        "decision_time_utc": "2025-02-23T00:00:00+00:00",
        "selected_symbols": [
          "AIXBTUSDT",
          "ETHUSDT",
          "ACTUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "CAKEUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "BERAUSDT",
          "ENAUSDT",
          "APTUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 104,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-24",
        "decision_time_utc": "2025-02-24T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "ANIMEUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "BERAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 108,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-25",
        "decision_time_utc": "2025-02-25T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "BERAUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "EIGENUSDT",
          "DOTUSDT",
          "ARBUSDT",
          "AIXBTUSDT",
          "ARKMUSDT",
          "FILUSDT",
          "FETUSDT",
          "CAKEUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 99,
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
          "ENAUSDT",
          "COWUSDT",
          "EIGENUSDT",
          "DOTUSDT",
          "BTCUSDT",
          "GALAUSDT",
          "APTUSDT",
          "ETHUSDT",
          "CRVUSDT",
          "FILUSDT",
          "FTTUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ARBUSDT",
          "ARKMUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "AVAXUSDT",
          "ETHFIUSDT",
          "ETCUSDT",
          "FLOKIUSDT",
          "AAVEUSDT",
          "BERAUSDT",
          "FETUSDT",
          "CAKEUSDT"
        ],
        "candidate_count": 27,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
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
          "ENAUSDT",
          "APTUSDT",
          "BTCUSDT",
          "EIGENUSDT",
          "ETHUSDT",
          "DOTUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "COWUSDT",
          "FETUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 100,
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
          "DOTUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 106,
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
          "ETCUSDT",
          "ETHUSDT",
          "AIXBTUSDT",
          "BONKUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "DOTUSDT",
          "AAVEUSDT",
          "1000SATSUSDT",
          "ARBUSDT",
          "EIGENUSDT",
          "FILUSDT",
          "FLOKIUSDT",
          "ETHFIUSDT",
          "FETUSDT"
        ],
        "candidate_count": 24,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
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
          "DOGEUSDT",
          "ETHUSDT",
          "BERAUSDT",
          "APTUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 107,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-03",
        "decision_time_utc": "2025-03-03T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "ENAUSDT",
          "AIXBTUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "FETUSDT",
          "ALGOUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "CRVUSDT",
          "ETHFIUSDT",
          "DOTUSDT",
          "ARBUSDT",
          "FILUSDT",
          "ETCUSDT",
          "FLOKIUSDT",
          "APTUSDT",
          "BCHUSDT",
          "CAKEUSDT",
          "BNBUSDT",
          "BERAUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 24,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-04",
        "decision_time_utc": "2025-03-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "BCHUSDT",
          "DOTUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "BERAUSDT",
          "ARBUSDT",
          "CRVUSDT",
          "CAKEUSDT",
          "FILUSDT",
          "ALGOUSDT",
          "AIXBTUSDT",
          "FLOKIUSDT",
          "FETUSDT",
          "ACTUSDT",
          "ETHFIUSDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
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
          "ENAUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "ACTUSDT",
          "CRVUSDT",
          "APTUSDT",
          "DOTUSDT",
          "BERAUSDT",
          "ARBUSDT",
          "FILUSDT",
          "ALGOUSDT",
          "FETUSDT",
          "FLOKIUSDT",
          "BONKUSDT",
          "BCHUSDT",
          "ETHFIUSDT"
        ],
        "candidate_count": 21,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
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
          "ETHUSDT",
          "ADAUSDT",
          "BERAUSDT",
          "DOGEUSDT",
          "DOTUSDT",
          "BNBUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 104,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-07",
        "decision_time_utc": "2025-03-07T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "BERAUSDT",
          "DOTUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 106,
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
          "ADAUSDT",
          "APTUSDT",
          "ETCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "FILUSDT",
          "AAVEUSDT",
          "BCHUSDT",
          "DOTUSDT",
          "BERAUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 102,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-09",
        "decision_time_utc": "2025-03-09T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "ENAUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 109,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-10",
        "decision_time_utc": "2025-03-10T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "DOTUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 108,
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
          "ETHUSDT",
          "AUDIOUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "DOTUSDT",
          "APTUSDT",
          "BERAUSDT",
          "FETUSDT",
          "ARBUSDT",
          "BCHUSDT",
          "C98USDT",
          "FLOKIUSDT",
          "FILUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 98,
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
          "DOGEUSDT",
          "AVAXUSDT",
          "BANANAUSDT",
          "ETHUSDT",
          "C98USDT",
          "BNBUSDT",
          "ARBUSDT",
          "ETCUSDT",
          "DOTUSDT",
          "FETUSDT",
          "FILUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "ENAUSDT",
          "ARKMUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 99,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-13",
        "decision_time_utc": "2025-03-13T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ETHUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "ENAUSDT",
          "AUCTIONUSDT",
          "BANANAUSDT",
          "DOTUSDT",
          "APTUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 104,
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
          "ETHUSDT",
          "DOGEUSDT",
          "AUCTIONUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 32,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 108,
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
          "ETHUSDT",
          "DOGEUSDT",
          "DOTUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 32,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 108,
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
          "ENAUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 32,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 109,
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
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "CAKEUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 32,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 109,
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
          "ENAUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "AUCTIONUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 32,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 107,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-19",
        "decision_time_utc": "2025-03-19T00:00:00+00:00",
        "selected_symbols": [
          "AUCTIONUSDT",
          "DYMUSDT",
          "CAKEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "API3USDT",
          "ENAUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 31,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 107,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-20",
        "decision_time_utc": "2025-03-20T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AAVEUSDT",
          "AUCTIONUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "DOTUSDT",
          "CAKEUSDT",
          "BMTUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 30,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 107,
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
          "ETHUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "CAKEUSDT",
          "BMTUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 30,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 108,
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
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 30,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 110,
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
          "ETHUSDT",
          "BTCUSDT",
          "CAKEUSDT",
          "DOGSUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "ACXUSDT",
          "AUCTIONUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 30,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 107,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-24",
        "decision_time_utc": "2025-03-24T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "FORMUSDT",
          "BTCUSDT",
          "API3USDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "CAKEUSDT",
          "AUCTIONUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 30,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 110,
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
          "ANKRUSDT",
          "AIXBTUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BOMEUSDT",
          "ADAUSDT",
          "AUCTIONUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "CAKEUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 30,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 105,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-26",
        "decision_time_utc": "2025-03-26T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "BERAUSDT",
          "CAKEUSDT",
          "FORMUSDT",
          "AUCTIONUSDT",
          "1000SATSUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 30,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 108,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-27",
        "decision_time_utc": "2025-03-27T00:00:00+00:00",
        "selected_symbols": [
          "CRVUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "FLOKIUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "1000SATSUSDT",
          "CAKEUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BERAUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 30,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 106,
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
          "CRVUSDT",
          "ENAUSDT",
          "CAKEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "1000SATSUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 28,
          "insufficient_24h": 2,
          "reconstruct_error": 0,
          "low_quote_volume": 109,
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
          "AUCTIONUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BERAUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "CRVUSDT",
          "CAKEUSDT",
          "API3USDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 28,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 110,
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
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BERAUSDT",
          "AVAXUSDT",
          "AUCTIONUSDT",
          "ENAUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 28,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 112,
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
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 28,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 116,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-01",
        "decision_time_utc": "2025-04-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "BERAUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 28,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 114,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-02",
        "decision_time_utc": "2025-04-02T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "ENAUSDT",
          "CRVUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "BERAUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "COMPUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 28,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 111,
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
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "CRVUSDT",
          "BERAUSDT",
          "1000SATSUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 28,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 109,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-04",
        "decision_time_utc": "2025-04-04T00:00:00+00:00",
        "selected_symbols": [
          "ACTUSDT",
          "CRVUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "BERAUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 28,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 112,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-05",
        "decision_time_utc": "2025-04-05T00:00:00+00:00",
        "selected_symbols": [
          "DOGEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "FILUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "BERAUSDT",
          "CRVUSDT",
          "APTUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 28,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 111,
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
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 28,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 115,
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
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "AUCTIONUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 28,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 114,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-08",
        "decision_time_utc": "2025-04-08T00:00:00+00:00",
        "selected_symbols": [
          "CRVUSDT",
          "ENAUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "ETHUSDT",
          "ACTUSDT",
          "ADAUSDT",
          "FLOKIUSDT",
          "AAVEUSDT",
          "DOGEUSDT",
          "ARBUSDT",
          "BNBUSDT",
          "ETCUSDT",
          "APTUSDT",
          "BERAUSDT",
          "DOTUSDT",
          "FILUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 28,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 105,
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
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BERAUSDT",
          "ENAUSDT",
          "CRVUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 28,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 112,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-10",
        "decision_time_utc": "2025-04-10T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "ENAUSDT",
          "CRVUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "APTUSDT",
          "DOTUSDT",
          "BNBUSDT",
          "BERAUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 28,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 109,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-11",
        "decision_time_utc": "2025-04-11T00:00:00+00:00",
        "selected_symbols": [
          "GASUSDT",
          "CRVUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BERAUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 27,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 111,
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
          "CRVUSDT",
          "BERAUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 112,
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
          "ENAUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "CRVUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 114,
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
          "ETHUSDT",
          "FETUSDT",
          "DOGEUSDT",
          "BABYUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "CRVUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 113,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-15",
        "decision_time_utc": "2025-04-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BABYUSDT",
          "ENAUSDT",
          "BCHUSDT",
          "CRVUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 113,
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
          "ACHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "BABYUSDT",
          "CRVUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 114,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-17",
        "decision_time_utc": "2025-04-17T00:00:00+00:00",
        "selected_symbols": [
          "CRVUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ARDRUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "BABYUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 114,
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
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "CRVUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 117,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-19",
        "decision_time_utc": "2025-04-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 119,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-20",
        "decision_time_utc": "2025-04-20T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 120,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-21",
        "decision_time_utc": "2025-04-21T00:00:00+00:00",
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
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 118,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-22",
        "decision_time_utc": "2025-04-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ENJUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "FETUSDT",
          "ENAUSDT",
          "CRVUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 114,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-23",
        "decision_time_utc": "2025-04-23T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "CRVUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "APTUSDT",
          "FETUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 112,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-24",
        "decision_time_utc": "2025-04-24T00:00:00+00:00",
        "selected_symbols": [
          "AIXBTUSDT",
          "FLOKIUSDT",
          "ENAUSDT",
          "AAVEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "DOTUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "CRVUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 110,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-25",
        "decision_time_utc": "2025-04-25T00:00:00+00:00",
        "selected_symbols": [
          "ARDRUSDT",
          "FETUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "BONKUSDT",
          "CRVUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 111,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-26",
        "decision_time_utc": "2025-04-26T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "FLOKIUSDT",
          "AIXBTUSDT",
          "BTCUSDT",
          "FETUSDT",
          "BCHUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "CETUSUSDT",
          "CRVUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 109,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-27",
        "decision_time_utc": "2025-04-27T00:00:00+00:00",
        "selected_symbols": [
          "AIXBTUSDT",
          "ETHUSDT",
          "FETUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "CRVUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 113,
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
          "ETHUSDT",
          "DOGEUSDT",
          "BONKUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "FETUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 115,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-29",
        "decision_time_utc": "2025-04-29T00:00:00+00:00",
        "selected_symbols": [
          "AIXBTUSDT",
          "FLOKIUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "FETUSDT",
          "ENAUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 112,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-30",
        "decision_time_utc": "2025-04-30T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "ENAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 116,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-01",
        "decision_time_utc": "2025-05-01T00:00:00+00:00",
        "selected_symbols": [
          "BABYUSDT",
          "CRVUSDT",
          "FLOKIUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 113,
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
          "DOGEUSDT",
          "ETHUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "CRVUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 112,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-03",
        "decision_time_utc": "2025-05-03T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AIXBTUSDT",
          "ENAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 116,
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
          "ADAUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 119,
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
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 118,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-06",
        "decision_time_utc": "2025-05-06T00:00:00+00:00",
        "selected_symbols": [
          "FORMUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BONKUSDT",
          "BNBUSDT",
          "AIXBTUSDT",
          "DOGEUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 116,
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
          "ETHUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 115,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-08",
        "decision_time_utc": "2025-05-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 117,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-09",
        "decision_time_utc": "2025-05-09T00:00:00+00:00",
        "selected_symbols": [
          "EIGENUSDT",
          "ETHFIUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "AAVEUSDT",
          "FLOKIUSDT",
          "BERAUSDT",
          "BONKUSDT",
          "DOGEUSDT",
          "AIXBTUSDT",
          "ARBUSDT",
          "ADAUSDT",
          "CRVUSDT",
          "AVAXUSDT",
          "DOTUSDT",
          "BTCUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "FORMUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 105,
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
          "ETHUSDT",
          "BONKUSDT",
          "EIGENUSDT",
          "AIXBTUSDT",
          "ENAUSDT",
          "FLOKIUSDT",
          "BERAUSDT",
          "BNBUSDT",
          "DOTUSDT",
          "FETUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "APTUSDT",
          "CRVUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 21,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 103,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-11",
        "decision_time_utc": "2025-05-11T00:00:00+00:00",
        "selected_symbols": [
          "ETHFIUSDT",
          "ARBUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "BERAUSDT",
          "AVAXUSDT",
          "DOTUSDT",
          "DOGSUSDT",
          "FLOKIUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "FETUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "CAKEUSDT",
          "1000CATUSDT",
          "AIXBTUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 21,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 103,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-12",
        "decision_time_utc": "2025-05-12T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ACTUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "ETHFIUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "DOTUSDT",
          "APTUSDT",
          "BERAUSDT",
          "GALAUSDT",
          "AAVEUSDT",
          "FLOKIUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 107,
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
          "FORMUSDT",
          "FIDAUSDT",
          "FLOKIUSDT",
          "BOMEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "AIXBTUSDT",
          "BONKUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "DOTUSDT",
          "ETHFIUSDT",
          "GALAUSDT",
          "FETUSDT",
          "APTUSDT",
          "CRVUSDT",
          "CAKEUSDT",
          "BERAUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 99,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-14",
        "decision_time_utc": "2025-05-14T00:00:00+00:00",
        "selected_symbols": [
          "ETHFIUSDT",
          "BOMEUSDT",
          "ENAUSDT",
          "1MBABYDOGEUSDT",
          "ETHUSDT",
          "FETUSDT",
          "DOGEUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "FLOKIUSDT",
          "DOTUSDT",
          "CRVUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 105,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-15",
        "decision_time_utc": "2025-05-15T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "1000SATSUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "BONKUSDT",
          "ETHFIUSDT",
          "AVAXUSDT",
          "BOMEUSDT",
          "ARBUSDT",
          "ACTUSDT",
          "FLOKIUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 109,
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
          "DOGEUSDT",
          "CVCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "EIGENUSDT",
          "DOTUSDT",
          "APTUSDT",
          "FLOKIUSDT",
          "FETUSDT",
          "CRVUSDT",
          "BOMEUSDT",
          "1000SATSUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 104,
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
          "AAVEUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ETHFIUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 113,
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
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "ETHFIUSDT",
          "AVAXUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 115,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-19",
        "decision_time_utc": "2025-05-19T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "BONKUSDT",
          "DOGEUSDT",
          "FLOKIUSDT",
          "ETHFIUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 112,
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
          "DOGEUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "ETHFIUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 114,
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
          "CRVUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ETHFIUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 114,
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
          "EIGENUSDT",
          "BTCUSDT",
          "FETUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "ETHUSDT",
          "CRVUSDT",
          "ETHFIUSDT",
          "ARBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "DOTUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 25,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 107,
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
          "CRVUSDT",
          "AVAXUSDT",
          "FLOKIUSDT",
          "FETUSDT",
          "BCHUSDT",
          "ETHUSDT",
          "APTUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "1000SATSUSDT",
          "ETHFIUSDT",
          "CETUSUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 25,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 106,
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
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "FETUSDT",
          "BONKUSDT",
          "AAVEUSDT",
          "ETHFIUSDT",
          "CRVUSDT",
          "DOTUSDT",
          "ARBUSDT",
          "BCHUSDT",
          "FLOKIUSDT",
          "APTUSDT",
          "CETUSUSDT",
          "BOMEUSDT",
          "ARKMUSDT",
          "EIGENUSDT",
          "1000SATSUSDT",
          "AIXBTUSDT",
          "GALAUSDT"
        ],
        "candidate_count": 25,
        "filter_counts": {
          "missing_1h": 25,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 100,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-25",
        "decision_time_utc": "2025-05-25T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "BONKUSDT",
          "FETUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 25,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 115,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-26",
        "decision_time_utc": "2025-05-26T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "AAVEUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 25,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 116,
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
          "ETHUSDT",
          "FETUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "COOKIEUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 25,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 113,
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
          "ETHFIUSDT",
          "ETHUSDT",
          "COOKIEUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "FETUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "CRVUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 25,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 110,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-29",
        "decision_time_utc": "2025-05-29T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "FETUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "ETHFIUSDT",
          "ADAUSDT",
          "CAKEUSDT",
          "CETUSUSDT",
          "AIXBTUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 112,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-30",
        "decision_time_utc": "2025-05-30T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ETHFIUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "EIGENUSDT",
          "BONKUSDT",
          "CAKEUSDT",
          "CRVUSDT"
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
        "date_utc": "2025-05-31",
        "decision_time_utc": "2025-05-31T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "ETHFIUSDT",
          "APTUSDT",
          "CAKEUSDT",
          "BONKUSDT",
          "DOTUSDT",
          "FILUSDT",
          "FETUSDT",
          "CRVUSDT",
          "AIXBTUSDT"
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
        "date_utc": "2025-06-01",
        "decision_time_utc": "2025-06-01T00:00:00+00:00",
        "selected_symbols": [
          "ETHFIUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ADAUSDT",
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
