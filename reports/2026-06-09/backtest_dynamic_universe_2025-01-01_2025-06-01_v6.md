---
created: 2026-06-09 14:37:52 CST
tags:
  - crypto
  - trading-system
  - backtest
backtest_run_id: 41c97fd4dda5
report_version: v6
sample_sufficient: false
universe_mode: true
universe_type: dynamic
---

# 回测报告 2025-01-01 至 2025-06-01 v6

- 回测 ID：`41c97fd4dda5`
- 交易对：`1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `AAVEUSDT`, `ACHUSDT`, `ACTUSDT`, `ACXUSDT`, `ADAUSDT`, `AGLDUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALGOUSDT`, `AMPUSDT`, `ANIMEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AVAXUSDT`, `BABYUSDT`, `BCHUSDT`, `BERAUSDT`, `BIOUSDT`, `BMTUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BTCUSDT`, `CAKEUSDT`, `CETUSUSDT`, `CFXUSDT`, `CGPTUSDT`, `CKBUSDT`, `COMPUSDT`, `COOKIEUSDT`, `COWUSDT`, `CRVUSDT`, `CVCUSDT`, `DOGEUSDT`, `DOTUSDT`, `DUSDT`, `EIGENUSDT`, `ENAUSDT`, `ENJUSDT`, `ENSUSDT`, `ETCUSDT`, `ETHFIUSDT`, `ETHUSDT`, `FETUSDT`, `FIDAUSDT`, `FILUSDT`, `FLOKIUSDT`, `FORMUSDT`, `GALAUSDT`, `GASUSDT`
- UTC 区间：2025-01-01T00:00:00+00:00 -> 2025-06-01T00:00:00+00:00
- 初始权益：10,000.00 USDT
- 最终权益：9,091.44 USDT
- 净收益：-9.09%
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
- Selected symbols per refresh / 每次入选数量：min=4, avg=9.99, max=31
- Top selected symbols / 最常入选：`BNBUSDT`(152), `BTCUSDT`(152), `ETHUSDT`(152), `DOGEUSDT`(151), `ADAUSDT`(144), `ENAUSDT`(110), `AVAXUSDT`(89), `AAVEUSDT`(66), `APTUSDT`(39), `BONKUSDT`(37)
- Filter counts / 过滤统计：
```json
{
  "missing_1h": 4679,
  "insufficient_24h": 17,
  "reconstruct_error": 0,
  "low_quote_volume": 16585,
  "low_trades": 0,
  "stable_like": 0
}
```
> Warning / 警告：dynamic universe 的 symbol master 来自当前 Binance exchangeInfo；历史上曾交易但今天已退市的币不会进入 master list，因此仍有退市幸存者偏差。
> Runtime / 耗时提示：第一次完整运行需要缓存大量 1h/4h/1d K 线，可能很慢；缓存命中后后续回测会明显加快。

## 核心指标

| Metric（指标） | Value（数值） |
|---|---:|
| Trades（计划总数） | 46 |
| Closed trades（已结束交易） | 16 |
| Open trades（仍开放持仓） | 2 |
| Win rate（胜率） | 12.50% |
| Profit factor（盈利因子） | 0.35 |
| Avg R（平均R倍数） | -0.56 |
| Net return（净收益率） | -9.09% |
| Max drawdown（最大回撤） | 1,355.61 / 13.22% |
| Intrabar max drawdown（K线内最大回撤） | 1,275.99 / 12.54% |
| TP1 touched rate（第一止盈触达率） | 18.75% |
| TP2 close rate（第二止盈平仓率） | 12.50% |
| Stop rate（止损率） | 87.50% |
| Fee drag（手续费拖累） | 23.16 USDT |
| Tail max single loss（最大单笔亏损） | -108.74 USDT |
| CAGR（年化复合收益率） | -20.57% |
| Sharpe（夏普比率） | -1.64 |
| Sortino（索提诺比率） | -1.60 |
| Exposure（持仓暴露时间） | 81.57% |
| Turnover（换手率） | 1.96 |
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
| Equal-weight symbols（等权持有本次币种） | -45.26% |

## 已结束交易

| Symbol（交易对） | Status（状态） | Created（创建时间） | Entry（入场价） | Exit（出场价） | Qty（数量） | Gross PnL（毛盈亏） | Net PnL（净盈亏） | Net R（净R倍数） | Fees（手续费） | Notes（备注） |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| `ETHUSDT` | STOPPED（已止损） | 2025-01-02T12:00:00+00:00 | 3,483.33 | 3,252.17 | 0.44 | -102.21 | -104.26 | -1.03 | 2.05 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-01-02T12:00:00+00:00 | 97,071.70 | 90,067.34 | 0.01 | -101.92 | -103.80 | -1.03 | 1.88 | Stop loss hit. |
| `BNBUSDT` | STOPPED（已止损） | 2025-01-04T00:00:00+00:00 | 712.59 | 685.89 | 3.93 | -104.92 | -108.74 | -1.06 | 3.82 | Stop loss hit. |
| `AAVEUSDT` | STOPPED（已止损） | 2025-01-04T04:00:00+00:00 | 340.44 | 301.35 | 2.61 | -101.88 | -103.02 | -1.02 | 1.14 | Stop loss hit. |
| `ENAUSDT` | STOPPED（已止损） | 2025-01-06T08:00:00+00:00 | 1.22 | 1.00 | 481.65 | -102.13 | -102.85 | -1.01 | 0.72 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-01-14T20:00:00+00:00 | 96,875.83 | 87,829.92 | 0.01 | -96.22 | -97.57 | -1.02 | 1.35 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-01-16T08:00:00+00:00 | 3,396.15 | 2,873.32 | 0.18 | -96.05 | -96.83 | -1.01 | 0.78 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-02-20T08:00:00+00:00 | 2,739.78 | 2,563.79 | 0.55 | -95.98 | -97.98 | -1.04 | 2.00 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-03-06T08:00:00+00:00 | 90,332.96 | 80,197.22 | 0.01 | -93.00 | -94.07 | -1.02 | 1.07 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-03-20T00:00:00+00:00 | 86,570.94 | 79,837.72 | 0.01 | -92.60 | -94.18 | -1.03 | 1.57 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-03-20T04:00:00+00:00 | 1,991.87 | 1,842.38 | 0.62 | -92.51 | -94.15 | -1.03 | 1.63 | Stop loss hit. |
| `BTCUSDT` | CLOSED（已按TP2平仓） | 2025-04-12T08:00:00+00:00 | 83,637.41 | 108,712.75 | 0.01 | 248.73 | 247.96 | 2.77 | 0.76 | TP2 hit; paper trade closed. |
| `ETHUSDT` | CLOSED（已按TP2平仓） | 2025-04-25T20:00:00+00:00 | 1,781.57 | 2,078.51 | 0.79 | 233.84 | 232.62 | 2.56 | 1.22 | TP2 hit; paper trade closed. |
| `ACTUSDT` | STOPPED（已止损） | 2025-05-11T04:00:00+00:00 | 0.06 | 0.05 | 8,665.88 | -94.02 | -94.68 | -1.01 | 0.66 | Stop loss hit. |
| `ADAUSDT` | STOPPED（已止损） | 2025-05-11T12:00:00+00:00 | 0.80 | 0.70 | 997.33 | -94.58 | -95.60 | -1.02 | 1.02 | Stop loss hit. |
| `DOGEUSDT` | STOPPED（已止损） | 2025-05-12T16:00:00+00:00 | 0.23 | 0.20 | 2,697.38 | -95.34 | -96.13 | -1.01 | 0.79 | Stop loss hit. |

## 回测结束仍开放

| Symbol（交易对） | Status（状态） | Entry（入场价） | Qty（数量） | Unrealized Handling（未实现盈亏处理） | Notes（备注） |
|---|---|---:|---:|---|---|
| `BNBUSDT` | ENTERED（已入场） | 649.68 | 1.86 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |
| `AAVEUSDT` | ENTERED（已入场） | 255.84 | 2.29 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |

## 未入场/过期计划

| Symbol（交易对） | Status（状态） | Created（创建时间） | Entry Zone（入场区间） | Score（评分） | Notes（备注） |
|---|---|---|---:|---:|---|
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-01-04T12:00:00+00:00 | 40.15 - 40.76 | 72.48 | Backtest WATCHING plan expired before entry. |
| `DOTUSDT` | EXPIRED（观察计划过期） | 2025-01-04T12:00:00+00:00 | 7.45 - 7.57 | 72.30 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-01-05T12:00:00+00:00 | 1.04 - 1.06 | 70.76 | Backtest WATCHING plan expired before entry. |
| `DOGEUSDT` | EXPIRED（观察计划过期） | 2025-01-05T16:00:00+00:00 | 0.37 - 0.38 | 69.12 | Backtest WATCHING plan expired before entry. |
| `FILUSDT` | INVALIDATED（未入场前失效） | 2025-01-07T00:00:00+00:00 | 5.81 - 5.92 | 78.27 | Plan invalidated before entry: current price is below stop loss. |
| `ARBUSDT` | INVALIDATED（未入场前失效） | 2025-01-07T00:00:00+00:00 | 0.89 - 0.91 | 76.00 | Plan invalidated before entry: current price is below stop loss. |
| `GALAUSDT` | INVALIDATED（未入场前失效） | 2025-01-07T00:00:00+00:00 | 0.04 - 0.04 | 71.86 | Plan invalidated before entry: current price is below stop loss. |
| `FLOKIUSDT` | INVALIDATED（未入场前失效） | 2025-01-07T00:00:00+00:00 | 0.00 - 0.00 | 57.83 | Plan invalidated before entry: current price is below stop loss. |
| `BONKUSDT` | INVALIDATED（未入场前失效） | 2025-01-07T00:00:00+00:00 | 0.00 - 0.00 | 56.33 | Plan invalidated before entry: current price is below stop loss. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-04-22T16:00:00+00:00 | 1,657.99 - 1,682.01 | 65.88 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-05-11T16:00:00+00:00 | 23.58 - 24.13 | 77.80 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-05-12T16:00:00+00:00 | 2,424.67 - 2,480.54 | 82.20 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-05-12T16:00:00+00:00 | 0.00 - 0.00 | 80.84 | Backtest WATCHING plan expired before entry. |
| `AAVEUSDT` | EXPIRED（观察计划过期） | 2025-05-13T00:00:00+00:00 | 216.64 - 221.74 | 72.23 | Backtest WATCHING plan expired before entry. |
| `ARBUSDT` | INVALIDATED（未入场前失效） | 2025-05-14T04:00:00+00:00 | 0.43 - 0.45 | 79.05 | Plan invalidated before entry: current price is below stop loss. |
| `ENAUSDT` | EXPIRED（观察计划过期） | 2025-05-14T16:00:00+00:00 | 0.41 - 0.41 | 72.07 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | INVALIDATED（未入场前失效） | 2025-05-16T04:00:00+00:00 | 2,558.21 - 2,589.09 | 56.00 | Plan invalidated before entry: current price is below stop loss. |
| `ETHFIUSDT` | EXPIRED（观察计划过期） | 2025-05-19T00:00:00+00:00 | 1.32 - 1.36 | 64.63 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-05-19T20:00:00+00:00 | 2,490.90 - 2,526.38 | 63.32 | Backtest WATCHING plan expired before entry. |
| `ENAUSDT` | EXPIRED（观察计划过期） | 2025-05-20T04:00:00+00:00 | 0.37 - 0.39 | 54.07 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-05-23T00:00:00+00:00 | 2,583.29 - 2,627.72 | 66.04 | Backtest WATCHING plan expired before entry. |
| `BTCUSDT` | EXPIRED（观察计划过期） | 2025-05-24T12:00:00+00:00 | 108,941.18 - 109,536.19 | 56.27 | Backtest WATCHING plan expired before entry. |
| `ETHUSDT` | EXPIRED（观察计划过期） | 2025-05-26T04:00:00+00:00 | 2,552.13 - 2,567.98 | 60.57 | Backtest WATCHING plan expired before entry. |
| `FETUSDT` | EXPIRED（观察计划过期） | 2025-05-27T00:00:00+00:00 | 0.87 - 0.87 | 72.72 | Backtest WATCHING plan expired before entry. |
| `ENAUSDT` | EXPIRED（观察计划过期） | 2025-05-27T00:00:00+00:00 | 0.38 - 0.39 | 51.20 | Backtest WATCHING plan expired before entry. |
| `BTCUSDT` | INVALIDATED（未入场前失效） | 2025-05-27T16:00:00+00:00 | 109,347.06 - 109,999.08 | 64.37 | Plan invalidated before entry: current price is below stop loss. |
| `AVAXUSDT` | INVALIDATED（未入场前失效） | 2025-05-28T00:00:00+00:00 | 23.38 - 23.45 | 49.29 | Plan invalidated before entry: current price is below stop loss. |
| `ETHUSDT` | EXPIRED_END（回测结束仍未入场） | 2025-05-29T08:00:00+00:00 | 2,645.88 - 2,682.34 | 69.78 | Backtest ended before condition plan entered. |

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
    "created_at_utc": "2026-06-09T06:37:52+00:00",
    "refresh_frequency": "daily",
    "max_symbols": 40,
    "master_count": 150,
    "source_limit": 150,
    "source_limit_applied": true,
    "universe_refresh_count": 152,
    "selected_count_min": 4,
    "selected_count_avg": 9.993421052631579,
    "selected_count_max": 31,
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
        "symbol": "ETHUSDT",
        "days_selected": 152
      },
      {
        "symbol": "DOGEUSDT",
        "days_selected": 151
      },
      {
        "symbol": "ADAUSDT",
        "days_selected": 144
      },
      {
        "symbol": "ENAUSDT",
        "days_selected": 110
      },
      {
        "symbol": "AVAXUSDT",
        "days_selected": 89
      },
      {
        "symbol": "AAVEUSDT",
        "days_selected": 66
      },
      {
        "symbol": "APTUSDT",
        "days_selected": 39
      },
      {
        "symbol": "BONKUSDT",
        "days_selected": 37
      },
      {
        "symbol": "ACTUSDT",
        "days_selected": 32
      },
      {
        "symbol": "DOTUSDT",
        "days_selected": 31
      },
      {
        "symbol": "ARBUSDT",
        "days_selected": 30
      },
      {
        "symbol": "BERAUSDT",
        "days_selected": 27
      },
      {
        "symbol": "FETUSDT",
        "days_selected": 26
      },
      {
        "symbol": "AIXBTUSDT",
        "days_selected": 25
      },
      {
        "symbol": "CAKEUSDT",
        "days_selected": 24
      },
      {
        "symbol": "FLOKIUSDT",
        "days_selected": 23
      },
      {
        "symbol": "CRVUSDT",
        "days_selected": 22
      },
      {
        "symbol": "GALAUSDT",
        "days_selected": 20
      }
    ],
    "filter_counts": {
      "missing_1h": 4679,
      "insufficient_24h": 17,
      "reconstruct_error": 0,
      "low_quote_volume": 16585,
      "low_trades": 0,
      "stable_like": 0
    },
    "selection_by_day": [
      {
        "date_utc": "2025-01-01",
        "decision_time_utc": "2025-01-01T04:00:00+00:00",
        "selected_symbols": [
          "FLOKIUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "ENAUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 41,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 100,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-02",
        "decision_time_utc": "2025-01-02T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "CRVUSDT",
          "ENAUSDT",
          "ACTUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "CVCUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 41,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 99,
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
          "BNBUSDT",
          "AGLDUSDT"
        ],
        "candidate_count": 16,
        "filter_counts": {
          "missing_1h": 41,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
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
          "AVAXUSDT",
          "ALGOUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 40,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 92,
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
          "ADAUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "GALAUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 40,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 99,
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
          "ENAUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 40,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 99,
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
          "FILUSDT",
          "ADAUSDT",
          "DOTUSDT",
          "BIOUSDT",
          "FLOKIUSDT",
          "ENAUSDT",
          "ARBUSDT",
          "ACTUSDT",
          "FETUSDT",
          "CRVUSDT",
          "AAVEUSDT"
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
        "date_utc": "2025-01-08",
        "decision_time_utc": "2025-01-08T00:00:00+00:00",
        "selected_symbols": [
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
          "FLOKIUSDT"
        ],
        "candidate_count": 19,
        "filter_counts": {
          "missing_1h": 40,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 91,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-09",
        "decision_time_utc": "2025-01-09T00:00:00+00:00",
        "selected_symbols": [
          "GASUSDT",
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
          "CRVUSDT"
        ],
        "candidate_count": 22,
        "filter_counts": {
          "missing_1h": 40,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 88,
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
          "FILUSDT"
        ],
        "candidate_count": 15,
        "filter_counts": {
          "missing_1h": 39,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-11",
        "decision_time_utc": "2025-01-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "DOGEUSDT",
          "APTUSDT",
          "ETHUSDT",
          "GALAUSDT",
          "ADAUSDT",
          "FETUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "BIOUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 36,
          "insufficient_24h": 3,
          "reconstruct_error": 0,
          "low_quote_volume": 97,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-12",
        "decision_time_utc": "2025-01-12T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "CGPTUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 36,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 107,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-13",
        "decision_time_utc": "2025-01-13T00:00:00+00:00",
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
          "missing_1h": 36,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 108,
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
          "AIXBTUSDT"
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
        "date_utc": "2025-01-15",
        "decision_time_utc": "2025-01-15T00:00:00+00:00",
        "selected_symbols": [
          "AIXBTUSDT",
          "CGPTUSDT",
          "COOKIEUSDT",
          "GALAUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BIOUSDT",
          "ENAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 36,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 103,
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
          "BIOUSDT",
          "FETUSDT",
          "APTUSDT",
          "BNBUSDT"
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
        "date_utc": "2025-01-17",
        "decision_time_utc": "2025-01-17T00:00:00+00:00",
        "selected_symbols": [
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
          "AAVEUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 36,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
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
          "APTUSDT",
          "FETUSDT",
          "DOTUSDT",
          "FILUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ALGOUSDT",
          "AIXBTUSDT"
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
        "date_utc": "2025-01-19",
        "decision_time_utc": "2025-01-19T00:00:00+00:00",
        "selected_symbols": [
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
          "APTUSDT"
        ],
        "candidate_count": 21,
        "filter_counts": {
          "missing_1h": 36,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 93,
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
          "BIOUSDT"
        ],
        "candidate_count": 30,
        "filter_counts": {
          "missing_1h": 36,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 84,
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
          "ENSUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "FETUSDT",
          "BONKUSDT",
          "APTUSDT",
          "1000SATSUSDT",
          "EIGENUSDT",
          "ETCUSDT",
          "ARBUSDT",
          "BOMEUSDT",
          "BCHUSDT",
          "FLOKIUSDT",
          "GALAUSDT",
          "COWUSDT",
          "ETHFIUSDT",
          "ARKMUSDT"
        ],
        "candidate_count": 29,
        "filter_counts": {
          "missing_1h": 36,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 85,
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
          "BTCUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "DOTUSDT",
          "FLOKIUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "APTUSDT",
          "ADAUSDT",
          "AIXBTUSDT",
          "CRVUSDT",
          "ALGOUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 18,
        "filter_counts": {
          "missing_1h": 36,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-23",
        "decision_time_utc": "2025-01-23T00:00:00+00:00",
        "selected_symbols": [
          "AIXBTUSDT",
          "ACTUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "BONKUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "FETUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 36,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 102,
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
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ACTUSDT",
          "ENAUSDT",
          "AIXBTUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "FETUSDT",
          "APTUSDT",
          "FLOKIUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 35,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 97,
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
          "DOGEUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "AIXBTUSDT",
          "BONKUSDT",
          "ANIMEUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 35,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 104,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-26",
        "decision_time_utc": "2025-01-26T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ANIMEUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 35,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 107,
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
          "AIXBTUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 35,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 107,
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
          "CRVUSDT"
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
          "DUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 35,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 104,
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
          "FLOKIUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "AIXBTUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "FETUSDT"
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
        "date_utc": "2025-01-31",
        "decision_time_utc": "2025-01-31T00:00:00+00:00",
        "selected_symbols": [
          "ACHUSDT",
          "ENAUSDT",
          "AAVEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "AIXBTUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 35,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 106,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-01",
        "decision_time_utc": "2025-02-01T00:00:00+00:00",
        "selected_symbols": [
          "FLOKIUSDT",
          "AAVEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ACHUSDT",
          "DOTUSDT",
          "GALAUSDT",
          "ARBUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "APTUSDT"
        ],
        "candidate_count": 14,
        "filter_counts": {
          "missing_1h": 35,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 101,
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
          "AAVEUSDT"
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
        "date_utc": "2025-02-03",
        "decision_time_utc": "2025-02-03T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ENAUSDT",
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
          "ARPAUSDT",
          "ACHUSDT"
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
          "ETCUSDT",
          "BCHUSDT",
          "ARBUSDT",
          "CRVUSDT",
          "GALAUSDT",
          "FLOKIUSDT",
          "ENSUSDT",
          "ACHUSDT",
          "BOMEUSDT",
          "ARUSDT",
          "ARKMUSDT",
          "ADAUSDT",
          "EIGENUSDT",
          "ETHFIUSDT"
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
          "BONKUSDT"
        ],
        "candidate_count": 20,
        "filter_counts": {
          "missing_1h": 35,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
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
          "APTUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 35,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 105,
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
          "AVAXUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 34,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 106,
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
          "BNBUSDT",
          "DOGEUSDT",
          "BERAUSDT",
          "ADAUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 34,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 106,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-09",
        "decision_time_utc": "2025-02-09T00:00:00+00:00",
        "selected_symbols": [
          "CAKEUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BERAUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 34,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 108,
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
          "ADAUSDT",
          "BERAUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 108,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-11",
        "decision_time_utc": "2025-02-11T00:00:00+00:00",
        "selected_symbols": [
          "COOKIEUSDT",
          "AIXBTUSDT",
          "APTUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "BERAUSDT",
          "BNBUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 105,
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
          "BTCUSDT",
          "ETHUSDT",
          "1000CHEEMSUSDT",
          "AIXBTUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
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
        "date_utc": "2025-02-13",
        "decision_time_utc": "2025-02-13T00:00:00+00:00",
        "selected_symbols": [
          "CAKEUSDT",
          "BNBUSDT",
          "DOTUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "ENAUSDT",
          "BERAUSDT",
          "AIXBTUSDT"
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
        "date_utc": "2025-02-14",
        "decision_time_utc": "2025-02-14T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "CAKEUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "APTUSDT"
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
        "date_utc": "2025-02-15",
        "decision_time_utc": "2025-02-15T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "CAKEUSDT",
          "ADAUSDT"
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
        "date_utc": "2025-02-16",
        "decision_time_utc": "2025-02-16T00:00:00+00:00",
        "selected_symbols": [
          "CAKEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 111,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-17",
        "decision_time_utc": "2025-02-17T00:00:00+00:00",
        "selected_symbols": [
          "CAKEUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 112,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-18",
        "decision_time_utc": "2025-02-18T00:00:00+00:00",
        "selected_symbols": [
          "BERAUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "CAKEUSDT",
          "ARKUSDT"
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
        "date_utc": "2025-02-19",
        "decision_time_utc": "2025-02-19T00:00:00+00:00",
        "selected_symbols": [
          "ACHUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "CAKEUSDT",
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
        "date_utc": "2025-02-20",
        "decision_time_utc": "2025-02-20T00:00:00+00:00",
        "selected_symbols": [
          "APTUSDT",
          "CAKEUSDT",
          "BERAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "FLOKIUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ENAUSDT"
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
        "date_utc": "2025-02-21",
        "decision_time_utc": "2025-02-21T00:00:00+00:00",
        "selected_symbols": [
          "BERAUSDT",
          "ENAUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "ETHUSDT",
          "FLOKIUSDT",
          "BNBUSDT",
          "CAKEUSDT",
          "DOGEUSDT",
          "APTUSDT"
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
        "date_utc": "2025-02-22",
        "decision_time_utc": "2025-02-22T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "AIXBTUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BERAUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "DOTUSDT",
          "CAKEUSDT",
          "AAVEUSDT",
          "ARKMUSDT"
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
        "date_utc": "2025-02-23",
        "decision_time_utc": "2025-02-23T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "CAKEUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BERAUSDT",
          "ENAUSDT"
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
        "date_utc": "2025-02-24",
        "decision_time_utc": "2025-02-24T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 111,
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
          "AAVEUSDT"
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
        "date_utc": "2025-02-26",
        "decision_time_utc": "2025-02-26T00:00:00+00:00",
        "selected_symbols": [
          "ACTUSDT",
          "ENAUSDT",
          "COWUSDT",
          "DOTUSDT",
          "BTCUSDT",
          "APTUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ARBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BERAUSDT",
          "FETUSDT"
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
        "date_utc": "2025-02-27",
        "decision_time_utc": "2025-02-27T00:00:00+00:00",
        "selected_symbols": [
          "BERAUSDT",
          "ACTUSDT",
          "ENAUSDT",
          "APTUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOTUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 105,
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
          "ENAUSDT"
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
        "date_utc": "2025-03-01",
        "decision_time_utc": "2025-03-01T00:00:00+00:00",
        "selected_symbols": [
          "CKBUSDT",
          "ACTUSDT",
          "BERAUSDT",
          "APTUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "DOTUSDT",
          "AAVEUSDT"
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
        "date_utc": "2025-03-02",
        "decision_time_utc": "2025-03-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "ETHUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 112,
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
          "DOGEUSDT",
          "ETHUSDT",
          "ALGOUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "DOTUSDT",
          "APTUSDT",
          "BNBUSDT",
          "BERAUSDT",
          "ACTUSDT"
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
          "ARBUSDT"
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
          "APTUSDT",
          "DOTUSDT",
          "BERAUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 105,
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
          "BNBUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 105,
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
        "date_utc": "2025-03-08",
        "decision_time_utc": "2025-03-08T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BCHUSDT",
          "DOTUSDT"
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
        "date_utc": "2025-03-09",
        "decision_time_utc": "2025-03-09T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "ENAUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 33,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 111,
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
          "AVAXUSDT"
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
        "date_utc": "2025-03-11",
        "decision_time_utc": "2025-03-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "ENAUSDT",
          "AVAXUSDT"
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
        "date_utc": "2025-03-12",
        "decision_time_utc": "2025-03-12T00:00:00+00:00",
        "selected_symbols": [
          "AUCTIONUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "ENAUSDT",
          "ARKMUSDT"
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
        "date_utc": "2025-03-13",
        "decision_time_utc": "2025-03-13T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "AAVEUSDT",
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
        "date_utc": "2025-03-14",
        "decision_time_utc": "2025-03-14T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 32,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 109,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-15",
        "decision_time_utc": "2025-03-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 32,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 112,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-16",
        "decision_time_utc": "2025-03-16T00:00:00+00:00",
        "selected_symbols": [
          "BNBUSDT",
          "BCHUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 32,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 112,
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
          "ADAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 32,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 112,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-18",
        "decision_time_utc": "2025-03-18T00:00:00+00:00",
        "selected_symbols": [
          "CAKEUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AUCTIONUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 32,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 110,
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
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "API3USDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 31,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 110,
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
          "AUCTIONUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "CAKEUSDT",
          "BMTUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 30,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 109,
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
          "BTCUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "CAKEUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 30,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 113,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-22",
        "decision_time_utc": "2025-03-22T00:00:00+00:00",
        "selected_symbols": [
          "CAKEUSDT",
          "AUCTIONUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 30,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 113,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-23",
        "decision_time_utc": "2025-03-23T00:00:00+00:00",
        "selected_symbols": [
          "API3USDT",
          "ETHUSDT",
          "BTCUSDT",
          "CAKEUSDT",
          "BNBUSDT",
          "ACXUSDT",
          "AUCTIONUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 30,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 113,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-24",
        "decision_time_utc": "2025-03-24T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AUCTIONUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 30,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 114,
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
          "ENAUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "AUCTIONUSDT",
          "BNBUSDT",
          "CAKEUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 30,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 109,
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
          "1000SATSUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 30,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 112,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-27",
        "decision_time_utc": "2025-03-27T00:00:00+00:00",
        "selected_symbols": [
          "DOGEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "1000SATSUSDT",
          "CAKEUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 30,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 112,
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
          "ENAUSDT",
          "CAKEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "1000SATSUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 28,
          "insufficient_24h": 2,
          "reconstruct_error": 0,
          "low_quote_volume": 111,
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
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BERAUSDT"
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
        "date_utc": "2025-03-30",
        "decision_time_utc": "2025-03-30T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BERAUSDT"
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
        "date_utc": "2025-03-31",
        "decision_time_utc": "2025-03-31T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 28,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 118,
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
          "ADAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 28,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 117,
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
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "COMPUSDT",
          "ACTUSDT"
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
          "ACTUSDT"
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
        "date_utc": "2025-04-04",
        "decision_time_utc": "2025-04-04T00:00:00+00:00",
        "selected_symbols": [
          "ACTUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "ENAUSDT"
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
        "date_utc": "2025-04-05",
        "decision_time_utc": "2025-04-05T00:00:00+00:00",
        "selected_symbols": [
          "DOGEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "FILUSDT",
          "BNBUSDT",
          "ENAUSDT"
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
        "date_utc": "2025-04-06",
        "decision_time_utc": "2025-04-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 28,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 118,
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
        "date_utc": "2025-04-08",
        "decision_time_utc": "2025-04-08T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "BERAUSDT",
          "DOTUSDT"
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
        "date_utc": "2025-04-09",
        "decision_time_utc": "2025-04-09T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
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
        "date_utc": "2025-04-10",
        "decision_time_utc": "2025-04-10T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "ENAUSDT",
          "CRVUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "BERAUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 28,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 113,
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
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 27,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 116,
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
          "ETHUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 115,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-13",
        "decision_time_utc": "2025-04-13T00:00:00+00:00",
        "selected_symbols": [
          "BABYUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT"
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
        "date_utc": "2025-04-14",
        "decision_time_utc": "2025-04-14T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BABYUSDT",
          "BNBUSDT",
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
          "ACTUSDT"
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
        "date_utc": "2025-04-16",
        "decision_time_utc": "2025-04-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
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
        "date_utc": "2025-04-17",
        "decision_time_utc": "2025-04-17T00:00:00+00:00",
        "selected_symbols": [
          "CRVUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
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
        "date_utc": "2025-04-18",
        "decision_time_utc": "2025-04-18T00:00:00+00:00",
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
        "date_utc": "2025-04-19",
        "decision_time_utc": "2025-04-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT"
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
        "date_utc": "2025-04-22",
        "decision_time_utc": "2025-04-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ENJUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "BNBUSDT",
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
        "date_utc": "2025-04-23",
        "decision_time_utc": "2025-04-23T00:00:00+00:00",
        "selected_symbols": [
          "CRVUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BNBUSDT"
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
        "date_utc": "2025-04-24",
        "decision_time_utc": "2025-04-24T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "ACTUSDT"
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
        "date_utc": "2025-04-25",
        "decision_time_utc": "2025-04-25T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ETHUSDT",
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
        "date_utc": "2025-04-26",
        "decision_time_utc": "2025-04-26T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
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
        "date_utc": "2025-04-27",
        "decision_time_utc": "2025-04-27T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "BONKUSDT",
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
        "date_utc": "2025-04-28",
        "decision_time_utc": "2025-04-28T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BONKUSDT",
          "BNBUSDT",
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
        "date_utc": "2025-04-29",
        "decision_time_utc": "2025-04-29T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
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
        "date_utc": "2025-04-30",
        "decision_time_utc": "2025-04-30T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BONKUSDT"
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
        "date_utc": "2025-05-01",
        "decision_time_utc": "2025-05-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT"
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
        "date_utc": "2025-05-02",
        "decision_time_utc": "2025-05-02T00:00:00+00:00",
        "selected_symbols": [
          "AIXBTUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "BNBUSDT"
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
        "date_utc": "2025-05-03",
        "decision_time_utc": "2025-05-03T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT"
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
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT"
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
        "date_utc": "2025-05-06",
        "decision_time_utc": "2025-05-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT"
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
        "date_utc": "2025-05-07",
        "decision_time_utc": "2025-05-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "DOGEUSDT"
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
        "date_utc": "2025-05-08",
        "decision_time_utc": "2025-05-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT"
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
        "date_utc": "2025-05-09",
        "decision_time_utc": "2025-05-09T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "ETHUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "BCHUSDT",
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
        "date_utc": "2025-05-10",
        "decision_time_utc": "2025-05-10T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BONKUSDT",
          "EIGENUSDT",
          "ENAUSDT",
          "FLOKIUSDT",
          "BERAUSDT",
          "BNBUSDT",
          "DOTUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "ADAUSDT"
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
        "date_utc": "2025-05-11",
        "decision_time_utc": "2025-05-11T00:00:00+00:00",
        "selected_symbols": [
          "ETHFIUSDT",
          "ARBUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "DOTUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "1000CATUSDT",
          "ACTUSDT"
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
        "date_utc": "2025-05-12",
        "decision_time_utc": "2025-05-12T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "ETHFIUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "BONKUSDT"
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
        "date_utc": "2025-05-13",
        "decision_time_utc": "2025-05-13T00:00:00+00:00",
        "selected_symbols": [
          "ACTUSDT",
          "FIDAUSDT",
          "FLOKIUSDT",
          "BOMEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BONKUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ENAUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "DOTUSDT"
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
        "date_utc": "2025-05-14",
        "decision_time_utc": "2025-05-14T00:00:00+00:00",
        "selected_symbols": [
          "ETHFIUSDT",
          "BOMEUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "ARBUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "BNBUSDT"
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
          "AVAXUSDT"
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
        "date_utc": "2025-05-16",
        "decision_time_utc": "2025-05-16T00:00:00+00:00",
        "selected_symbols": [
          "ETHFIUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "1000SATSUSDT"
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
        "date_utc": "2025-05-17",
        "decision_time_utc": "2025-05-17T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ENAUSDT",
          "ETHUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ETHFIUSDT",
          "ADAUSDT",
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
        "date_utc": "2025-05-18",
        "decision_time_utc": "2025-05-18T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ENAUSDT"
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
        "date_utc": "2025-05-19",
        "decision_time_utc": "2025-05-19T00:00:00+00:00",
        "selected_symbols": [
          "ENAUSDT",
          "DOGEUSDT",
          "ETHFIUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BNBUSDT"
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
        "date_utc": "2025-05-21",
        "decision_time_utc": "2025-05-21T00:00:00+00:00",
        "selected_symbols": [
          "AAVEUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "ENAUSDT",
          "DOGEUSDT",
          "AVAXUSDT",
          "BNBUSDT",
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
        "date_utc": "2025-05-22",
        "decision_time_utc": "2025-05-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "DOGEUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "ETHUSDT",
          "ETHFIUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 25,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 114,
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
          "ETHUSDT",
          "DOGEUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "ENAUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "CETUSUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 25,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 114,
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
          "CRVUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 25,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 112,
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
          "ADAUSDT",
          "ENAUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 25,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 118,
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
          "ADAUSDT",
          "DOGEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 25,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 119,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-27",
        "decision_time_utc": "2025-05-27T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "FETUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "DOGEUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "COOKIEUSDT"
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
        "date_utc": "2025-05-28",
        "decision_time_utc": "2025-05-28T00:00:00+00:00",
        "selected_symbols": [
          "AIXBTUSDT",
          "CAKEUSDT",
          "ETHFIUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "ENAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "DOGEUSDT",
          "ADAUSDT"
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
        "date_utc": "2025-05-29",
        "decision_time_utc": "2025-05-29T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "DOGEUSDT",
          "BNBUSDT",
          "ENAUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 24,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 119,
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
        "date_utc": "2025-06-01",
        "decision_time_utc": "2025-06-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "ENAUSDT",
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
