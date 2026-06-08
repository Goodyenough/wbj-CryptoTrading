---
created: 2026-06-09 02:42:40 CST
tags:
  - crypto
  - trading-system
  - backtest
backtest_run_id: 4051ae365f6b
report_version: v2
sample_sufficient: true
universe_mode: true
universe_type: dynamic
---

# 回测报告 2025-06-01 至 2026-06-01 v2

- 回测 ID：`4051ae365f6b`
- 交易对：`0GUSDT`, `1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1INCHUSDT`, `2ZUSDT`, `AAVEUSDT`, `ACEUSDT`, `ADAUSDT`, `AEVOUSDT`, `AIUSDT`, `ALCXUSDT`, `ALGOUSDT`, `ALICEUSDT`, `ALLOUSDT`, `ALPINEUSDT`, `ALTUSDT`, `ANIMEUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARKMUSDT`, `ARUSDT`, `ASRUSDT`, `ASTERUSDT`, `ATUSDT`, `AUCTIONUSDT`, `AUSDT`, `AVAXUSDT`, `AVNTUSDT`, `AXLUSDT`, `AXSUSDT`, `BANANAS31USDT`, `BARDUSDT`, `BCHUSDT`, `BELUSDT`, `BERAUSDT`, `BIOUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BREVUSDT`, `BROCCOLI714USDT`, `BTCUSDT`, `CAKEUSDT`, `CFGUSDT`, `CFXUSDT`, `CHIPUSDT`, `CKBUSDT`, `COMPUSDT`, `COWUSDT`
- UTC 区间：2025-06-01T00:00:00+00:00 -> 2026-06-01T00:00:00+00:00
- 初始权益：10,000.00 USDT
- 最终权益：9,446.79 USDT
- 净收益：-5.53%
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
- Selected symbols per refresh / 每次入选数量：min=1, avg=4.26, max=12
- Top selected symbols / 最常入选：`BTCUSDT`(366), `BNBUSDT`(344), `ADAUSDT`(193), `AVAXUSDT`(130), `ASTERUSDT`(80), `BONKUSDT`(57), `AAVEUSDT`(51), `BCHUSDT`(49), `ARBUSDT`(46), `APTUSDT`(25)
- Filter counts / 过滤统计：
```json
{
  "missing_1h": 2349,
  "insufficient_24h": 13,
  "reconstruct_error": 0,
  "low_quote_volume": 32674,
  "low_trades": 4,
  "stable_like": 1
}
```
> Warning / 警告：dynamic universe 的 symbol master 来自当前 Binance exchangeInfo；历史上曾交易但今天已退市的币不会进入 master list，因此仍有退市幸存者偏差。
> Runtime / 耗时提示：第一次完整运行需要缓存大量 1h/4h/1d K 线，可能很慢；缓存命中后后续回测会明显加快。

## 核心指标

| Metric（指标） | Value（数值） |
|---|---:|
| Trades（计划总数） | 60 |
| Closed trades（已结束交易） | 38 |
| Open trades（仍开放持仓） | 2 |
| Win rate（胜率） | 23.68% |
| Profit factor（盈利因子） | 0.81 |
| Avg R（平均R倍数） | -0.13 |
| Net return（净收益率） | -5.53% |
| Max drawdown（最大回撤） | 2,117.66 / 18.76% |
| Intrabar max drawdown（K线内最大回撤） | 2,071.58 / 18.48% |
| TP1 touched rate（第一止盈触达率） | 28.95% |
| TP2 close rate（第二止盈平仓率） | 23.68% |
| Stop rate（止损率） | 76.32% |
| Fee drag（手续费拖累） | 63.15 USDT |
| Tail max single loss（最大单笔亏损） | -113.30 USDT |
| CAGR（年化复合收益率） | -5.53% |
| Sharpe（夏普比率） | -0.29 |
| Sortino（索提诺比率） | -0.31 |
| Exposure（持仓暴露时间） | 84.16% |
| Turnover（换手率） | 5.28 |
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
| Equal-weight symbols（等权持有本次币种） | -57.54% |

## 已结束交易

| Symbol（交易对） | Status（状态） | Created（创建时间） | Entry（入场价） | Exit（出场价） | Qty（数量） | Gross PnL（毛盈亏） | Net PnL（净盈亏） | Net R（净R倍数） | Fees（手续费） | Notes（备注） |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| `BTCUSDT` | STOPPED（已止损） | 2025-06-06T16:00:00+00:00 | 105,460.26 | 98,767.81 | 0.02 | -102.32 | -104.47 | -1.04 | 2.15 | Stop loss hit. |
| `AVAXUSDT` | STOPPED（已止损） | 2025-06-10T00:00:00+00:00 | 21.79 | 19.25 | 40.13 | -101.83 | -102.95 | -1.02 | 1.12 | Stop loss hit. |
| `ADAUSDT` | STOPPED（已止损） | 2025-06-10T00:00:00+00:00 | 0.71 | 0.64 | 1,494.04 | -102.12 | -103.49 | -1.02 | 1.38 | Stop loss hit. |
| `BNBUSDT` | STOPPED（已止损） | 2025-06-10T12:00:00+00:00 | 660.52 | 636.16 | 4.29 | -104.57 | -108.43 | -1.06 | 3.86 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-06-24T16:00:00+00:00 | 105,613.24 | 96,630.27 | 0.01 | -97.43 | -98.93 | -1.03 | 1.51 | Stop loss hit. |
| `ARBUSDT` | CLOSED（已按TP2平仓） | 2025-06-30T16:00:00+00:00 | 0.34 | 0.45 | 2,156.44 | 244.96 | 244.27 | 2.53 | 0.69 | TP2 hit; paper trade closed. |
| `BNBUSDT` | CLOSED（已按TP2平仓） | 2025-07-01T00:00:00+00:00 | 654.32 | 718.72 | 4.93 | 317.50 | 314.79 | 3.24 | 2.71 | TP2 hit; paper trade closed. |
| `ADAUSDT` | CLOSED（已按TP2平仓） | 2025-07-03T08:00:00+00:00 | 0.60 | 0.80 | 1,334.51 | 267.47 | 266.72 | 2.74 | 0.75 | TP2 hit; paper trade closed. |
| `BONKUSDT` | CLOSED（已按TP2平仓） | 2025-07-08T20:00:00+00:00 | 0.00 | 0.00 | 21,819,066.30 | 262.75 | 262.26 | 2.67 | 0.49 | TP2 hit; paper trade closed. |
| `AAVEUSDT` | STOPPED（已止损） | 2025-07-15T00:00:00+00:00 | 316.24 | 288.18 | 3.92 | -110.06 | -111.69 | -1.03 | 1.63 | Stop loss hit. |
| `APTUSDT` | STOPPED（已止损） | 2025-07-17T00:00:00+00:00 | 5.16 | 4.71 | 241.73 | -109.05 | -110.68 | -1.03 | 1.64 | Stop loss hit. |
| `ARBUSDT` | STOPPED（已止损） | 2025-07-17T04:00:00+00:00 | 0.43 | 0.38 | 2,290.76 | -109.14 | -110.42 | -1.02 | 1.28 | Stop loss hit. |
| `AVAXUSDT` | CLOSED（已按TP2平仓） | 2025-07-17T04:00:00+00:00 | 22.22 | 27.66 | 50.98 | 277.71 | 276.69 | 2.55 | 1.02 | TP2 hit; paper trade closed. |
| `ADAUSDT` | STOPPED（已止损） | 2025-07-21T20:00:00+00:00 | 0.87 | 0.78 | 1,202.64 | -109.68 | -111.04 | -1.02 | 1.36 | Stop loss hit. |
| `BNBUSDT` | STOPPED（已止损） | 2025-07-23T16:00:00+00:00 | 783.39 | 732.83 | 2.15 | -108.51 | -110.76 | -1.04 | 2.25 | Stop loss hit. |
| `CFXUSDT` | CLOSED（已按TP2平仓） | 2025-07-24T08:00:00+00:00 | 0.18 | 0.26 | 4,410.97 | 353.66 | 352.89 | 3.34 | 0.77 | TP2 hit; paper trade closed. |
| `CAKEUSDT` | STOPPED（已止损） | 2025-07-28T16:00:00+00:00 | 3.00 | 2.57 | 260.60 | -112.32 | -113.30 | -1.01 | 0.98 | Stop loss hit. |
| `CFXUSDT` | STOPPED（已止损） | 2025-07-30T00:00:00+00:00 | 0.21 | 0.18 | 3,673.72 | -107.30 | -108.25 | -1.02 | 0.96 | Stop loss hit. |
| `BCHUSDT` | STOPPED（已止损） | 2025-08-08T00:00:00+00:00 | 576.71 | 532.94 | 2.46 | -107.79 | -109.67 | -1.03 | 1.88 | Stop loss hit. |
| `BONKUSDT` | STOPPED（已止损） | 2025-08-10T04:00:00+00:00 | 0.00 | 0.00 | 24,483,081.70 | -106.14 | -107.00 | -1.01 | 0.86 | Stop loss hit. |
| `ADAUSDT` | STOPPED（已止损） | 2025-08-15T20:00:00+00:00 | 0.93 | 0.82 | 930.40 | -105.02 | -106.13 | -1.02 | 1.11 | Stop loss hit. |
| `BNBUSDT` | CLOSED（已按TP2平仓） | 2025-08-23T04:00:00+00:00 | 871.49 | 1,045.94 | 1.62 | 281.96 | 280.72 | 2.68 | 1.24 | TP2 hit; paper trade closed. |
| `AVAXUSDT` | CLOSED（已按TP2平仓） | 2025-09-16T00:00:00+00:00 | 29.85 | 34.86 | 50.96 | 255.51 | 254.19 | 2.43 | 1.32 | TP2 hit; paper trade closed. |
| `ADAUSDT` | STOPPED（已止损） | 2025-09-17T08:00:00+00:00 | 0.89 | 0.84 | 2,304.82 | -107.44 | -110.19 | -1.04 | 2.75 | Stop loss hit. |
| `ARBUSDT` | STOPPED（已止损） | 2025-09-18T00:00:00+00:00 | 0.52 | 0.48 | 2,582.77 | -109.48 | -111.24 | -1.03 | 1.76 | Stop loss hit. |
| `BONKUSDT` | STOPPED（已止损） | 2025-09-18T08:00:00+00:00 | 0.00 | 0.00 | 40,791,151.16 | -109.80 | -111.11 | -1.02 | 1.31 | Stop loss hit. |
| `BIOUSDT` | STOPPED（已止损） | 2025-09-21T00:00:00+00:00 | 0.18 | 0.16 | 4,766.50 | -108.63 | -109.74 | -1.02 | 1.11 | Stop loss hit. |
| `BNBUSDT` | STOPPED（已止损） | 2025-09-21T12:00:00+00:00 | 1,025.08 | 958.33 | 1.58 | -105.37 | -107.53 | -1.04 | 2.16 | Stop loss hit. |
| `CAKEUSDT` | STOPPED（已止损） | 2025-09-21T12:00:00+00:00 | 2.89 | 2.59 | 356.44 | -105.93 | -107.27 | -1.02 | 1.34 | Stop loss hit. |
| `ADAUSDT` | STOPPED（已止损） | 2025-10-02T00:00:00+00:00 | 0.85 | 0.77 | 1,306.21 | -103.87 | -105.31 | -1.02 | 1.44 | Stop loss hit. |
| `AVAXUSDT` | STOPPED（已止损） | 2025-10-02T20:00:00+00:00 | 30.78 | 28.35 | 42.92 | -104.44 | -106.19 | -1.03 | 1.75 | Stop loss hit. |
| `BNBUSDT` | STOPPED（已止损） | 2025-10-05T12:00:00+00:00 | 1,149.84 | 1,024.45 | 0.82 | -103.26 | -104.48 | -1.02 | 1.22 | Stop loss hit. |
| `APTUSDT` | STOPPED（已止损） | 2025-10-05T20:00:00+00:00 | 5.38 | 4.99 | 268.30 | -104.76 | -106.68 | -1.03 | 1.92 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-11-30T04:00:00+00:00 | 91,152.21 | 88,714.33 | 0.04 | -101.13 | -106.32 | -1.09 | 5.19 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-12-03T08:00:00+00:00 | 93,325.63 | 82,482.85 | 0.01 | -95.63 | -96.69 | -1.02 | 1.06 | Stop loss hit. |
| `BNBUSDT` | STOPPED（已止损） | 2026-01-18T00:00:00+00:00 | 944.78 | 908.92 | 2.75 | -98.45 | -101.98 | -1.06 | 3.53 | Stop loss hit. |
| `BNBUSDT` | CLOSED（已按TP2平仓） | 2026-04-16T00:00:00+00:00 | 618.86 | 718.19 | 2.60 | 258.51 | 257.12 | 2.73 | 1.39 | TP2 hit; paper trade closed. |
| `ADAUSDT` | STOPPED（已止损） | 2026-04-17T00:00:00+00:00 | 0.25 | 0.23 | 4,722.33 | -95.18 | -96.77 | -1.03 | 1.59 | Stop loss hit. |

## 回测结束仍开放

| Symbol（交易对） | Status（状态） | Entry（入场价） | Qty（数量） | Unrealized Handling（未实现盈亏处理） | Notes（备注） |
|---|---|---:|---:|---|---|
| `BTCUSDT` | TP1_HIT（第一止盈已触达） | 69,208.02 | 0.01 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |
| `AVNTUSDT` | TP1_HIT（第一止盈已触达） | 0.14 | 5,713.47 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |

## 未入场/过期计划

| Symbol（交易对） | Status（状态） | Created（创建时间） | Entry Zone（入场区间） | Score（评分） | Notes（备注） |
|---|---|---|---:|---:|---|
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-07-04T16:00:00+00:00 | 0.00 - 0.00 | 71.04 | Backtest WATCHING plan expired before entry. |
| `AAVEUSDT` | EXPIRED（观察计划过期） | 2025-07-10T04:00:00+00:00 | 291.48 - 295.98 | 68.64 | Backtest WATCHING plan expired before entry. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-07-14T00:00:00+00:00 | 20.77 - 21.13 | 66.99 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-17T04:00:00+00:00 | 695.83 - 701.13 | 62.82 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-07-18T16:00:00+00:00 | 0.79 - 0.82 | 76.32 | Backtest WATCHING plan expired before entry. |
| `BCHUSDT` | EXPIRED（观察计划过期） | 2025-07-19T20:00:00+00:00 | 509.15 - 516.54 | 60.29 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-07-20T04:00:00+00:00 | 0.00 - 0.00 | 71.27 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-07-20T08:00:00+00:00 | 729.99 - 738.45 | 60.86 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | INVALIDATED（未入场前失效） | 2025-07-23T08:00:00+00:00 | 0.00 - 0.00 | 67.92 | Plan invalidated before entry: current price is below stop loss. |
| `BCHUSDT` | EXPIRED（观察计划过期） | 2025-07-25T00:00:00+00:00 | 510.37 - 514.54 | 36.35 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-07-26T00:00:00+00:00 | 0.00 - 0.00 | 66.50 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-07-26T16:00:00+00:00 | 0.82 - 0.84 | 63.08 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-08-08T08:00:00+00:00 | 773.64 - 778.88 | 60.60 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-08-08T16:00:00+00:00 | 0.76 - 0.77 | 65.29 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-08-11T16:00:00+00:00 | 801.89 - 809.22 | 62.06 | Backtest WATCHING plan expired before entry. |
| `ADAUSDT` | EXPIRED（观察计划过期） | 2025-08-12T16:00:00+00:00 | 0.79 - 0.81 | 65.38 | Backtest WATCHING plan expired before entry. |
| `APTUSDT` | EXPIRED（观察计划过期） | 2025-08-14T08:00:00+00:00 | 4.85 - 4.94 | 69.05 | Backtest WATCHING plan expired before entry. |
| `BCHUSDT` | EXPIRED（观察计划过期） | 2025-09-19T00:00:00+00:00 | 616.88 - 624.29 | 67.37 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-10-02T00:00:00+00:00 | 1,011.09 - 1,019.11 | 63.44 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | INVALIDATED（未入场前失效） | 2025-10-07T00:00:00+00:00 | 0.00 - 0.00 | 62.93 | Plan invalidated before entry: current price is below stop loss. |

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
    "created_at_utc": "2026-06-08T18:42:40+00:00",
    "refresh_frequency": "daily",
    "max_symbols": 30,
    "master_count": 100,
    "source_limit": 100,
    "source_limit_applied": true,
    "universe_refresh_count": 366,
    "selected_count_min": 1,
    "selected_count_avg": 4.259562841530054,
    "selected_count_max": 12,
    "top_selected_symbols": [
      {
        "symbol": "BTCUSDT",
        "days_selected": 366
      },
      {
        "symbol": "BNBUSDT",
        "days_selected": 344
      },
      {
        "symbol": "ADAUSDT",
        "days_selected": 193
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
        "symbol": "APTUSDT",
        "days_selected": 25
      },
      {
        "symbol": "AVNTUSDT",
        "days_selected": 24
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
        "symbol": "BANANAS31USDT",
        "days_selected": 14
      },
      {
        "symbol": "CFXUSDT",
        "days_selected": 14
      },
      {
        "symbol": "BARDUSDT",
        "days_selected": 10
      },
      {
        "symbol": "ALLOUSDT",
        "days_selected": 8
      },
      {
        "symbol": "AXSUSDT",
        "days_selected": 8
      },
      {
        "symbol": "ALPINEUSDT",
        "days_selected": 7
      }
    ],
    "filter_counts": {
      "missing_1h": 2349,
      "insufficient_24h": 13,
      "reconstruct_error": 0,
      "low_quote_volume": 32674,
      "low_trades": 4,
      "stable_like": 1
    },
    "selection_by_day": [
      {
        "date_utc": "2025-06-01",
        "decision_time_utc": "2025-06-01T04:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
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
        "date_utc": "2025-06-02",
        "decision_time_utc": "2025-06-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
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
        "date_utc": "2025-06-03",
        "decision_time_utc": "2025-06-03T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "AUSDT"
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
        "date_utc": "2025-06-04",
        "decision_time_utc": "2025-06-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
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
        "date_utc": "2025-06-05",
        "decision_time_utc": "2025-06-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "AAVEUSDT"
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
        "date_utc": "2025-06-06",
        "decision_time_utc": "2025-06-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
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
        "date_utc": "2025-06-07",
        "decision_time_utc": "2025-06-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
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
        "date_utc": "2025-06-08",
        "decision_time_utc": "2025-06-08T00:00:00+00:00",
        "selected_symbols": [
          "ANIMEUSDT",
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
        "date_utc": "2025-06-09",
        "decision_time_utc": "2025-06-09T00:00:00+00:00",
        "selected_symbols": [
          "ANIMEUSDT",
          "BTCUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 85,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-10",
        "decision_time_utc": "2025-06-10T00:00:00+00:00",
        "selected_symbols": [
          "ANIMEUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "AVAXUSDT",
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
        "date_utc": "2025-06-11",
        "decision_time_utc": "2025-06-11T00:00:00+00:00",
        "selected_symbols": [
          "AXLUSDT",
          "COMPUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BNBUSDT"
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
        "date_utc": "2025-06-12",
        "decision_time_utc": "2025-06-12T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ANIMEUSDT"
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
          "BTCUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "ADAUSDT",
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
        "date_utc": "2025-06-15",
        "decision_time_utc": "2025-06-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 85,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-16",
        "decision_time_utc": "2025-06-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 85,
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
          "AAVEUSDT",
          "ADAUSDT",
          "ALTUSDT"
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
        "date_utc": "2025-06-18",
        "decision_time_utc": "2025-06-18T00:00:00+00:00",
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
        "date_utc": "2025-06-19",
        "decision_time_utc": "2025-06-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
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
        "date_utc": "2025-06-20",
        "decision_time_utc": "2025-06-20T00:00:00+00:00",
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
        "date_utc": "2025-06-21",
        "decision_time_utc": "2025-06-21T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
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
        "date_utc": "2025-06-22",
        "decision_time_utc": "2025-06-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
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
        "date_utc": "2025-06-23",
        "decision_time_utc": "2025-06-23T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BCHUSDT",
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
        "date_utc": "2025-06-24",
        "decision_time_utc": "2025-06-24T00:00:00+00:00",
        "selected_symbols": [
          "AAVEUSDT",
          "AVAXUSDT",
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
        "date_utc": "2025-06-25",
        "decision_time_utc": "2025-06-25T00:00:00+00:00",
        "selected_symbols": [
          "APTUSDT",
          "BANANAS31USDT",
          "BTCUSDT",
          "AAVEUSDT",
          "ADAUSDT",
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
        "date_utc": "2025-06-26",
        "decision_time_utc": "2025-06-26T00:00:00+00:00",
        "selected_symbols": [
          "BANANAS31USDT",
          "BCHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "APTUSDT",
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
        "date_utc": "2025-06-27",
        "decision_time_utc": "2025-06-27T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BANANAS31USDT"
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
        "date_utc": "2025-06-28",
        "decision_time_utc": "2025-06-28T00:00:00+00:00",
        "selected_symbols": [
          "BANANAS31USDT",
          "BTCUSDT",
          "BNBUSDT",
          "APTUSDT"
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
        "date_utc": "2025-06-29",
        "decision_time_utc": "2025-06-29T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT"
        ],
        "candidate_count": 1,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 86,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-06-30",
        "decision_time_utc": "2025-06-30T00:00:00+00:00",
        "selected_symbols": [
          "ARBUSDT",
          "BTCUSDT",
          "ADAUSDT"
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
        "date_utc": "2025-07-01",
        "decision_time_utc": "2025-07-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ARBUSDT",
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
        "date_utc": "2025-07-02",
        "decision_time_utc": "2025-07-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
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
        "date_utc": "2025-07-03",
        "decision_time_utc": "2025-07-03T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "BTCUSDT",
          "ARBUSDT",
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
        "date_utc": "2025-07-04",
        "decision_time_utc": "2025-07-04T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
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
        "date_utc": "2025-07-05",
        "decision_time_utc": "2025-07-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 85,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-06",
        "decision_time_utc": "2025-07-06T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "BTCUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 85,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-07-07",
        "decision_time_utc": "2025-07-07T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
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
        "date_utc": "2025-07-08",
        "decision_time_utc": "2025-07-08T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
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
        "date_utc": "2025-07-09",
        "decision_time_utc": "2025-07-09T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BONKUSDT",
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
        "date_utc": "2025-07-10",
        "decision_time_utc": "2025-07-10T00:00:00+00:00",
        "selected_symbols": [
          "BANANAS31USDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "BONKUSDT"
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
        "date_utc": "2025-07-11",
        "decision_time_utc": "2025-07-11T00:00:00+00:00",
        "selected_symbols": [
          "BANANAS31USDT",
          "BONKUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "AAVEUSDT"
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
        "date_utc": "2025-07-12",
        "decision_time_utc": "2025-07-12T00:00:00+00:00",
        "selected_symbols": [
          "1INCHUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ALTUSDT",
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
        "date_utc": "2025-07-13",
        "decision_time_utc": "2025-07-13T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "BANANAS31USDT"
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
          "1INCHUSDT",
          "BANANAS31USDT"
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
        "date_utc": "2025-07-15",
        "decision_time_utc": "2025-07-15T00:00:00+00:00",
        "selected_symbols": [
          "ALGOUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT"
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
        "date_utc": "2025-07-16",
        "decision_time_utc": "2025-07-16T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "BNBUSDT"
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
        "date_utc": "2025-07-17",
        "decision_time_utc": "2025-07-17T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "APTUSDT",
          "ARBUSDT",
          "AVAXUSDT",
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
        "date_utc": "2025-07-18",
        "decision_time_utc": "2025-07-18T00:00:00+00:00",
        "selected_symbols": [
          "ALGOUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ARBUSDT",
          "BONKUSDT",
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
          "APTUSDT",
          "AVAXUSDT"
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
        "date_utc": "2025-07-20",
        "decision_time_utc": "2025-07-20T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "BTCUSDT",
          "BONKUSDT",
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
        "date_utc": "2025-07-21",
        "decision_time_utc": "2025-07-21T00:00:00+00:00",
        "selected_symbols": [
          "CFXUSDT",
          "CKBUSDT",
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
        "date_utc": "2025-07-22",
        "decision_time_utc": "2025-07-22T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "CFXUSDT",
          "ARBUSDT",
          "BCHUSDT",
          "AAVEUSDT"
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
          "CFXUSDT"
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
          "AAVEUSDT"
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
        "date_utc": "2025-07-26",
        "decision_time_utc": "2025-07-26T00:00:00+00:00",
        "selected_symbols": [
          "BCHUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "AVAXUSDT"
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
        "date_utc": "2025-07-27",
        "decision_time_utc": "2025-07-27T00:00:00+00:00",
        "selected_symbols": [
          "CKBUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
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
        "date_utc": "2025-07-28",
        "decision_time_utc": "2025-07-28T00:00:00+00:00",
        "selected_symbols": [
          "ASRUSDT",
          "CAKEUSDT",
          "BNBUSDT",
          "BCHUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "ADAUSDT",
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
        "date_utc": "2025-07-29",
        "decision_time_utc": "2025-07-29T00:00:00+00:00",
        "selected_symbols": [
          "ASRUSDT",
          "BANANAS31USDT",
          "1000CATUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "CAKEUSDT",
          "BCHUSDT",
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
        "date_utc": "2025-07-30",
        "decision_time_utc": "2025-07-30T00:00:00+00:00",
        "selected_symbols": [
          "CFXUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "AVAXUSDT",
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
        "date_utc": "2025-07-31",
        "decision_time_utc": "2025-07-31T00:00:00+00:00",
        "selected_symbols": [
          "CFXUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "BONKUSDT",
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
        "date_utc": "2025-08-01",
        "decision_time_utc": "2025-08-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "CFXUSDT",
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
          "APTUSDT"
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
        "date_utc": "2025-08-03",
        "decision_time_utc": "2025-08-03T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT"
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
        "date_utc": "2025-08-04",
        "decision_time_utc": "2025-08-04T00:00:00+00:00",
        "selected_symbols": [
          "CFXUSDT",
          "ADAUSDT",
          "BTCUSDT",
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
        "date_utc": "2025-08-05",
        "decision_time_utc": "2025-08-05T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "BONKUSDT"
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
        "date_utc": "2025-08-06",
        "decision_time_utc": "2025-08-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT"
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
        "date_utc": "2025-08-07",
        "decision_time_utc": "2025-08-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
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
        "date_utc": "2025-08-08",
        "decision_time_utc": "2025-08-08T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "BCHUSDT",
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
        "date_utc": "2025-08-09",
        "decision_time_utc": "2025-08-09T00:00:00+00:00",
        "selected_symbols": [
          "APTUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ADAUSDT",
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
        "date_utc": "2025-08-10",
        "decision_time_utc": "2025-08-10T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
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
        "date_utc": "2025-08-11",
        "decision_time_utc": "2025-08-11T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "BTCUSDT",
          "BONKUSDT",
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
        "date_utc": "2025-08-12",
        "decision_time_utc": "2025-08-12T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "BANANAS31USDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "AAVEUSDT"
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
        "date_utc": "2025-08-13",
        "decision_time_utc": "2025-08-13T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "BCHUSDT",
          "BTCUSDT",
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
        "date_utc": "2025-08-14",
        "decision_time_utc": "2025-08-14T00:00:00+00:00",
        "selected_symbols": [
          "ARBUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "APTUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 78,
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
          "BNBUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "BCHUSDT",
          "CFXUSDT"
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
        "date_utc": "2025-08-16",
        "decision_time_utc": "2025-08-16T00:00:00+00:00",
        "selected_symbols": [
          "ALPINEUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "AVAXUSDT",
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
        "date_utc": "2025-08-17",
        "decision_time_utc": "2025-08-17T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 85,
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
          "AVAXUSDT",
          "BNBUSDT",
          "BTCUSDT"
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
        "date_utc": "2025-08-19",
        "decision_time_utc": "2025-08-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "BIOUSDT"
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
        "date_utc": "2025-08-20",
        "decision_time_utc": "2025-08-20T00:00:00+00:00",
        "selected_symbols": [
          "API3USDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "BIOUSDT"
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
        "date_utc": "2025-08-21",
        "decision_time_utc": "2025-08-21T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "CFXUSDT",
          "ARBUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BTCUSDT",
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
        "date_utc": "2025-08-22",
        "decision_time_utc": "2025-08-22T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "API3USDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ARBUSDT"
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
        "date_utc": "2025-08-23",
        "decision_time_utc": "2025-08-23T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "BTCUSDT"
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
          "BIOUSDT"
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
        "date_utc": "2025-08-26",
        "decision_time_utc": "2025-08-26T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BIOUSDT",
          "ARBUSDT",
          "AVAXUSDT",
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
        "date_utc": "2025-08-27",
        "decision_time_utc": "2025-08-27T00:00:00+00:00",
        "selected_symbols": [
          "AAVEUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "BIOUSDT"
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
        "date_utc": "2025-08-28",
        "decision_time_utc": "2025-08-28T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AVAXUSDT",
          "BIOUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ARBUSDT",
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
        "date_utc": "2025-08-31",
        "decision_time_utc": "2025-08-31T00:00:00+00:00",
        "selected_symbols": [
          "CFXUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
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
        "date_utc": "2025-09-01",
        "decision_time_utc": "2025-09-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 85,
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
        "date_utc": "2025-09-03",
        "decision_time_utc": "2025-09-03T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "ADAUSDT",
          "BNBUSDT"
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
        "date_utc": "2025-09-04",
        "decision_time_utc": "2025-09-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BCHUSDT",
          "AVAXUSDT",
          "BNBUSDT",
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
        "date_utc": "2025-09-05",
        "decision_time_utc": "2025-09-05T00:00:00+00:00",
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
        "date_utc": "2025-09-06",
        "decision_time_utc": "2025-09-06T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "BTCUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "BNBUSDT",
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
        "date_utc": "2025-09-07",
        "decision_time_utc": "2025-09-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "BIOUSDT",
          "BCHUSDT"
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
        "date_utc": "2025-09-08",
        "decision_time_utc": "2025-09-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 85,
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
          "AVAXUSDT",
          "BNBUSDT",
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
        "date_utc": "2025-09-11",
        "decision_time_utc": "2025-09-11T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "1000SATSUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ARBUSDT"
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
        "date_utc": "2025-09-12",
        "decision_time_utc": "2025-09-12T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ACEUSDT"
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
        "date_utc": "2025-09-13",
        "decision_time_utc": "2025-09-13T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT"
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
        "date_utc": "2025-09-14",
        "decision_time_utc": "2025-09-14T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "BONKUSDT"
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
        "date_utc": "2025-09-15",
        "decision_time_utc": "2025-09-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ADAUSDT"
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
        "date_utc": "2025-09-16",
        "decision_time_utc": "2025-09-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 11,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 83,
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
          "ADAUSDT",
          "AVAXUSDT",
          "AVNTUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 11,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 84,
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
          "BTCUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 11,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 82,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-09-19",
        "decision_time_utc": "2025-09-19T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "AVNTUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "BCHUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 83,
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
          "ARBUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 84,
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
          "BTCUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 84,
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
          "BTCUSDT",
          "AVAXUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 10,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 84,
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
          "AVNTUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 9,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 82,
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
          "ADAUSDT"
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
        "date_utc": "2025-09-25",
        "decision_time_utc": "2025-09-25T00:00:00+00:00",
        "selected_symbols": [
          "AVNTUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "0GUSDT",
          "BARDUSDT"
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
        "date_utc": "2025-09-26",
        "decision_time_utc": "2025-09-26T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "0GUSDT",
          "AVNTUSDT"
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
        "date_utc": "2025-09-27",
        "decision_time_utc": "2025-09-27T00:00:00+00:00",
        "selected_symbols": [
          "ALPINEUSDT",
          "1000SATSUSDT",
          "AVNTUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
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
        "date_utc": "2025-09-28",
        "decision_time_utc": "2025-09-28T00:00:00+00:00",
        "selected_symbols": [
          "ALPINEUSDT",
          "AEVOUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "AVNTUSDT",
          "AVAXUSDT",
          "1000SATSUSDT"
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
        "date_utc": "2025-09-29",
        "decision_time_utc": "2025-09-29T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "AVNTUSDT",
          "BARDUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 9,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 86,
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
          "ADAUSDT"
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
        "date_utc": "2025-10-01",
        "decision_time_utc": "2025-10-01T00:00:00+00:00",
        "selected_symbols": [
          "AVNTUSDT",
          "BARDUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ADAUSDT",
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
        "date_utc": "2025-10-02",
        "decision_time_utc": "2025-10-02T00:00:00+00:00",
        "selected_symbols": [
          "APTUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "BARDUSDT",
          "AVNTUSDT",
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
        "date_utc": "2025-10-03",
        "decision_time_utc": "2025-10-03T00:00:00+00:00",
        "selected_symbols": [
          "BNBUSDT",
          "APTUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BARDUSDT",
          "AVAXUSDT",
          "AVNTUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 84,
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
          "2ZUSDT"
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
        "date_utc": "2025-10-05",
        "decision_time_utc": "2025-10-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "CAKEUSDT",
          "AVNTUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 85,
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
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 8,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 87,
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
          "ADAUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "APTUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 84,
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
          "BROCCOLI714USDT",
          "BTCUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "APTUSDT"
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
        "date_utc": "2025-10-09",
        "decision_time_utc": "2025-10-09T00:00:00+00:00",
        "selected_symbols": [
          "1000CHEEMSUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ASTERUSDT",
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
        "date_utc": "2025-10-11",
        "decision_time_utc": "2025-10-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "CAKEUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "APTUSDT",
          "BNSOLUSDT"
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
        "date_utc": "2025-10-12",
        "decision_time_utc": "2025-10-12T00:00:00+00:00",
        "selected_symbols": [
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
          "CAKEUSDT"
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
        "date_utc": "2025-10-13",
        "decision_time_utc": "2025-10-13T00:00:00+00:00",
        "selected_symbols": [
          "CAKEUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "AVAXUSDT"
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
        "date_utc": "2025-10-14",
        "decision_time_utc": "2025-10-14T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "CAKEUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
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
          "BCHUSDT"
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
        "date_utc": "2025-10-16",
        "decision_time_utc": "2025-10-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "2ZUSDT",
          "ASTERUSDT",
          "CAKEUSDT",
          "ADAUSDT",
          "AVAXUSDT"
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
          "BELUSDT"
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
        "date_utc": "2025-10-18",
        "decision_time_utc": "2025-10-18T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
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
        "date_utc": "2025-10-19",
        "decision_time_utc": "2025-10-19T00:00:00+00:00",
        "selected_symbols": [
          "BNBUSDT",
          "BTCUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
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
        "date_utc": "2025-10-21",
        "decision_time_utc": "2025-10-21T00:00:00+00:00",
        "selected_symbols": [
          "AUCTIONUSDT",
          "BIOUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ASTERUSDT",
          "AVAXUSDT"
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
          "CAKEUSDT"
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
        "date_utc": "2025-10-23",
        "decision_time_utc": "2025-10-23T00:00:00+00:00",
        "selected_symbols": [
          "AVNTUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
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
        "date_utc": "2025-10-24",
        "decision_time_utc": "2025-10-24T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BCHUSDT",
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
        "date_utc": "2025-10-25",
        "decision_time_utc": "2025-10-25T00:00:00+00:00",
        "selected_symbols": [
          "AVNTUSDT",
          "BTCUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "BNBUSDT"
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
        "date_utc": "2025-10-26",
        "decision_time_utc": "2025-10-26T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ASTERUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-10-27",
        "decision_time_utc": "2025-10-27T00:00:00+00:00",
        "selected_symbols": [
          "BCHUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ASTERUSDT"
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
        "date_utc": "2025-10-28",
        "decision_time_utc": "2025-10-28T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
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
        "date_utc": "2025-10-31",
        "decision_time_utc": "2025-10-31T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
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
        "date_utc": "2025-11-01",
        "decision_time_utc": "2025-11-01T00:00:00+00:00",
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
        "date_utc": "2025-11-02",
        "decision_time_utc": "2025-11-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
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
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-04",
        "decision_time_utc": "2025-11-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 87,
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
          "ARBUSDT"
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
        "date_utc": "2025-11-06",
        "decision_time_utc": "2025-11-06T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 7,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 87,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-07",
        "decision_time_utc": "2025-11-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ALCXUSDT"
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
        "date_utc": "2025-11-08",
        "decision_time_utc": "2025-11-08T00:00:00+00:00",
        "selected_symbols": [
          "ARUSDT",
          "APTUSDT",
          "ASTERUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "BTCUSDT"
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
        "date_utc": "2025-11-11",
        "decision_time_utc": "2025-11-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ASTERUSDT"
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
        "date_utc": "2025-11-12",
        "decision_time_utc": "2025-11-12T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "CFXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 87,
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
          "ALLOUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 6,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 89,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-14",
        "decision_time_utc": "2025-11-14T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ALLOUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 88,
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
          "ADAUSDT",
          "AAVEUSDT",
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
        "date_utc": "2025-11-18",
        "decision_time_utc": "2025-11-18T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BANANAS31USDT"
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
        "date_utc": "2025-11-21",
        "decision_time_utc": "2025-11-21T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
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
        "date_utc": "2025-11-22",
        "decision_time_utc": "2025-11-22T00:00:00+00:00",
        "selected_symbols": [
          "BCHUSDT",
          "BTCUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ALLOUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 88,
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
          "BNBUSDT",
          "ASTERUSDT"
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
        "date_utc": "2025-11-24",
        "decision_time_utc": "2025-11-24T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 92,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-25",
        "decision_time_utc": "2025-11-25T00:00:00+00:00",
        "selected_symbols": [
          "ALLOUSDT",
          "BTCUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BNBUSDT"
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
        "date_utc": "2025-11-26",
        "decision_time_utc": "2025-11-26T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 92,
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
          "BNBUSDT",
          "BCHUSDT",
          "ALLOUSDT",
          "ASTERUSDT"
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
        "date_utc": "2025-11-28",
        "decision_time_utc": "2025-11-28T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 92,
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
          "ASTERUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
          "low_trades": 1,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-11-30",
        "decision_time_utc": "2025-11-30T00:00:00+00:00",
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
        "date_utc": "2025-12-01",
        "decision_time_utc": "2025-12-01T00:00:00+00:00",
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
        "date_utc": "2025-12-02",
        "decision_time_utc": "2025-12-02T00:00:00+00:00",
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
        "date_utc": "2025-12-03",
        "decision_time_utc": "2025-12-03T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ASTERUSDT"
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
        "date_utc": "2025-12-04",
        "decision_time_utc": "2025-12-04T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "BCHUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "ASTERUSDT",
          "ADAUSDT"
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
        "date_utc": "2025-12-05",
        "decision_time_utc": "2025-12-05T00:00:00+00:00",
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
        "date_utc": "2025-12-06",
        "decision_time_utc": "2025-12-06T00:00:00+00:00",
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
        "date_utc": "2025-12-07",
        "decision_time_utc": "2025-12-07T00:00:00+00:00",
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
        "date_utc": "2025-12-08",
        "decision_time_utc": "2025-12-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "ATUSDT"
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
        "date_utc": "2025-12-09",
        "decision_time_utc": "2025-12-09T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ASTERUSDT",
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
        "date_utc": "2025-12-10",
        "decision_time_utc": "2025-12-10T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "BTCUSDT",
          "ASTERUSDT",
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
        "date_utc": "2025-12-11",
        "decision_time_utc": "2025-12-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ASTERUSDT",
          "ATUSDT",
          "BCHUSDT"
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
        "date_utc": "2025-12-12",
        "decision_time_utc": "2025-12-12T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ATUSDT",
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
        "date_utc": "2025-12-13",
        "decision_time_utc": "2025-12-13T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ATUSDT",
          "BNBUSDT",
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
        "date_utc": "2025-12-16",
        "decision_time_utc": "2025-12-16T00:00:00+00:00",
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
        "date_utc": "2025-12-17",
        "decision_time_utc": "2025-12-17T00:00:00+00:00",
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
        "date_utc": "2025-12-18",
        "decision_time_utc": "2025-12-18T00:00:00+00:00",
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
          "BTCUSDT",
          "BNBUSDT"
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
        "date_utc": "2025-12-21",
        "decision_time_utc": "2025-12-21T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT"
        ],
        "candidate_count": 1,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 95,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-12-22",
        "decision_time_utc": "2025-12-22T00:00:00+00:00",
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
        "date_utc": "2025-12-23",
        "decision_time_utc": "2025-12-23T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "AAVEUSDT"
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
        "date_utc": "2025-12-24",
        "decision_time_utc": "2025-12-24T00:00:00+00:00",
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
        "date_utc": "2025-12-25",
        "decision_time_utc": "2025-12-25T00:00:00+00:00",
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
        "date_utc": "2025-12-26",
        "decision_time_utc": "2025-12-26T00:00:00+00:00",
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
        "date_utc": "2025-12-27",
        "decision_time_utc": "2025-12-27T00:00:00+00:00",
        "selected_symbols": [
          "ATUSDT",
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
        "date_utc": "2025-12-30",
        "decision_time_utc": "2025-12-30T00:00:00+00:00",
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
        "date_utc": "2025-12-31",
        "decision_time_utc": "2025-12-31T00:00:00+00:00",
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
        "date_utc": "2026-01-01",
        "decision_time_utc": "2026-01-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "BROCCOLI714USDT"
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
        "date_utc": "2026-01-02",
        "decision_time_utc": "2026-01-02T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "BROCCOLI714USDT",
          "BTCUSDT",
          "BNBUSDT"
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
        "date_utc": "2026-01-03",
        "decision_time_utc": "2026-01-03T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
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
        "date_utc": "2026-01-04",
        "decision_time_utc": "2026-01-04T00:00:00+00:00",
        "selected_symbols": [
          "BCHUSDT",
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
        "date_utc": "2026-01-05",
        "decision_time_utc": "2026-01-05T00:00:00+00:00",
        "selected_symbols": [
          "BROCCOLI714USDT",
          "BONKUSDT",
          "ASTERUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "BCHUSDT"
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
        "date_utc": "2026-01-06",
        "decision_time_utc": "2026-01-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "BCHUSDT",
          "ASTERUSDT",
          "BROCCOLI714USDT"
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
        "date_utc": "2026-01-07",
        "decision_time_utc": "2026-01-07T00:00:00+00:00",
        "selected_symbols": [
          "BROCCOLI714USDT",
          "BTCUSDT",
          "BNBUSDT",
          "ASTERUSDT",
          "ADAUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 90,
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
        "date_utc": "2026-01-09",
        "decision_time_utc": "2026-01-09T00:00:00+00:00",
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
        "date_utc": "2026-01-10",
        "decision_time_utc": "2026-01-10T00:00:00+00:00",
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
        "date_utc": "2026-01-14",
        "decision_time_utc": "2026-01-14T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "BREVUSDT",
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
        "date_utc": "2026-01-15",
        "decision_time_utc": "2026-01-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ASTERUSDT",
          "BNBUSDT",
          "BCHUSDT",
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
        "date_utc": "2026-01-16",
        "decision_time_utc": "2026-01-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BCHUSDT",
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
        "date_utc": "2026-01-17",
        "decision_time_utc": "2026-01-17T00:00:00+00:00",
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
        "date_utc": "2026-01-18",
        "decision_time_utc": "2026-01-18T00:00:00+00:00",
        "selected_symbols": [
          "AXSUSDT",
          "BTCUSDT",
          "BREVUSDT",
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
        "date_utc": "2026-01-19",
        "decision_time_utc": "2026-01-19T00:00:00+00:00",
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
        "date_utc": "2026-01-20",
        "decision_time_utc": "2026-01-20T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "BREVUSDT",
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
        "date_utc": "2026-01-21",
        "decision_time_utc": "2026-01-21T00:00:00+00:00",
        "selected_symbols": [
          "AXSUSDT",
          "BTCUSDT",
          "BREVUSDT",
          "BNBUSDT",
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
        "date_utc": "2026-01-22",
        "decision_time_utc": "2026-01-22T00:00:00+00:00",
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
          "low_quote_volume": 94,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-25",
        "decision_time_utc": "2026-01-25T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT"
        ],
        "candidate_count": 1,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-01-26",
        "decision_time_utc": "2026-01-26T00:00:00+00:00",
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
        "date_utc": "2026-01-27",
        "decision_time_utc": "2026-01-27T00:00:00+00:00",
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
        "date_utc": "2026-01-28",
        "decision_time_utc": "2026-01-28T00:00:00+00:00",
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
        "date_utc": "2026-01-29",
        "decision_time_utc": "2026-01-29T00:00:00+00:00",
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
        "date_utc": "2026-01-30",
        "decision_time_utc": "2026-01-30T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "AVAXUSDT"
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
        "date_utc": "2026-01-31",
        "decision_time_utc": "2026-01-31T00:00:00+00:00",
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
        "date_utc": "2026-02-01",
        "decision_time_utc": "2026-02-01T00:00:00+00:00",
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
        "date_utc": "2026-02-02",
        "decision_time_utc": "2026-02-02T00:00:00+00:00",
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
        "date_utc": "2026-02-03",
        "decision_time_utc": "2026-02-03T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
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
        "date_utc": "2026-02-04",
        "decision_time_utc": "2026-02-04T00:00:00+00:00",
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
        "date_utc": "2026-02-05",
        "decision_time_utc": "2026-02-05T00:00:00+00:00",
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
        "date_utc": "2026-02-06",
        "decision_time_utc": "2026-02-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ASTERUSDT",
          "AAVEUSDT"
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
        "date_utc": "2026-02-07",
        "decision_time_utc": "2026-02-07T00:00:00+00:00",
        "selected_symbols": [
          "ASTERUSDT",
          "BTCUSDT",
          "BCHUSDT",
          "ADAUSDT",
          "AVAXUSDT",
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
        "date_utc": "2026-02-08",
        "decision_time_utc": "2026-02-08T00:00:00+00:00",
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
        "date_utc": "2026-02-15",
        "decision_time_utc": "2026-02-15T00:00:00+00:00",
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
        "date_utc": "2026-02-16",
        "decision_time_utc": "2026-02-16T00:00:00+00:00",
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
        "date_utc": "2026-02-17",
        "decision_time_utc": "2026-02-17T00:00:00+00:00",
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
          "BTCUSDT"
        ],
        "candidate_count": 1,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-02-24",
        "decision_time_utc": "2026-02-24T00:00:00+00:00",
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
        "date_utc": "2026-02-25",
        "decision_time_utc": "2026-02-25T00:00:00+00:00",
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
        "date_utc": "2026-02-26",
        "decision_time_utc": "2026-02-26T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "AVAXUSDT",
          "BTCUSDT",
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
        "date_utc": "2026-02-27",
        "decision_time_utc": "2026-02-27T00:00:00+00:00",
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
        "date_utc": "2026-02-28",
        "decision_time_utc": "2026-02-28T00:00:00+00:00",
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
        "date_utc": "2026-03-01",
        "decision_time_utc": "2026-03-01T00:00:00+00:00",
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
        "date_utc": "2026-03-02",
        "decision_time_utc": "2026-03-02T00:00:00+00:00",
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
        "date_utc": "2026-03-03",
        "decision_time_utc": "2026-03-03T00:00:00+00:00",
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
        "date_utc": "2026-03-06",
        "decision_time_utc": "2026-03-06T00:00:00+00:00",
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
        "date_utc": "2026-03-07",
        "decision_time_utc": "2026-03-07T00:00:00+00:00",
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
        "date_utc": "2026-03-08",
        "decision_time_utc": "2026-03-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT"
        ],
        "candidate_count": 1,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
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
        "date_utc": "2026-03-11",
        "decision_time_utc": "2026-03-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
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
        "date_utc": "2026-03-12",
        "decision_time_utc": "2026-03-12T00:00:00+00:00",
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
        "date_utc": "2026-03-15",
        "decision_time_utc": "2026-03-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT"
        ],
        "candidate_count": 1,
        "filter_counts": {
          "missing_1h": 3,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
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
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 94,
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
        "date_utc": "2026-03-19",
        "decision_time_utc": "2026-03-19T00:00:00+00:00",
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
          "BTCUSDT"
        ],
        "candidate_count": 1,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 97,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-23",
        "decision_time_utc": "2026-03-23T00:00:00+00:00",
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
        "date_utc": "2026-03-27",
        "decision_time_utc": "2026-03-27T00:00:00+00:00",
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
        "date_utc": "2026-03-28",
        "decision_time_utc": "2026-03-28T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "CFGUSDT",
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
        "date_utc": "2026-03-29",
        "decision_time_utc": "2026-03-29T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT"
        ],
        "candidate_count": 1,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 97,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-03-30",
        "decision_time_utc": "2026-03-30T00:00:00+00:00",
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
        "date_utc": "2026-04-02",
        "decision_time_utc": "2026-04-02T00:00:00+00:00",
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
        "date_utc": "2026-04-03",
        "decision_time_utc": "2026-04-03T00:00:00+00:00",
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
        "date_utc": "2026-04-04",
        "decision_time_utc": "2026-04-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT"
        ],
        "candidate_count": 1,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 97,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-05",
        "decision_time_utc": "2026-04-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT"
        ],
        "candidate_count": 1,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 97,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-06",
        "decision_time_utc": "2026-04-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT"
        ],
        "candidate_count": 1,
        "filter_counts": {
          "missing_1h": 2,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 97,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-04-07",
        "decision_time_utc": "2026-04-07T00:00:00+00:00",
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
        "date_utc": "2026-04-08",
        "decision_time_utc": "2026-04-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AVAXUSDT",
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
        "date_utc": "2026-04-09",
        "decision_time_utc": "2026-04-09T00:00:00+00:00",
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
        "date_utc": "2026-04-13",
        "decision_time_utc": "2026-04-13T00:00:00+00:00",
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
        "date_utc": "2026-04-14",
        "decision_time_utc": "2026-04-14T00:00:00+00:00",
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
        "date_utc": "2026-04-15",
        "decision_time_utc": "2026-04-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "BARDUSDT"
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
        "date_utc": "2026-04-16",
        "decision_time_utc": "2026-04-16T00:00:00+00:00",
        "selected_symbols": [
          "BARDUSDT",
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
        "date_utc": "2026-04-17",
        "decision_time_utc": "2026-04-17T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "BARDUSDT",
          "ADAUSDT",
          "BTCUSDT",
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
        "date_utc": "2026-04-18",
        "decision_time_utc": "2026-04-18T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AVNTUSDT",
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
        "date_utc": "2026-04-19",
        "decision_time_utc": "2026-04-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AVNTUSDT",
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
        "date_utc": "2026-04-20",
        "decision_time_utc": "2026-04-20T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AAVEUSDT",
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
        "date_utc": "2026-04-21",
        "decision_time_utc": "2026-04-21T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "AAVEUSDT"
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
        "date_utc": "2026-04-22",
        "decision_time_utc": "2026-04-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 96,
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
        "date_utc": "2026-04-24",
        "decision_time_utc": "2026-04-24T00:00:00+00:00",
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
        "date_utc": "2026-04-25",
        "decision_time_utc": "2026-04-25T00:00:00+00:00",
        "selected_symbols": [
          "APEUSDT",
          "BTCUSDT",
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
        "date_utc": "2026-04-26",
        "decision_time_utc": "2026-04-26T00:00:00+00:00",
        "selected_symbols": [
          "AXSUSDT",
          "BTCUSDT",
          "CHIPUSDT",
          "APEUSDT"
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
        "date_utc": "2026-04-27",
        "decision_time_utc": "2026-04-27T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "CHIPUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 97,
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
          "BTCUSDT",
          "CHIPUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 97,
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
        "date_utc": "2026-05-01",
        "decision_time_utc": "2026-05-01T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "BTCUSDT",
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
          "BTCUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 97,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-04",
        "decision_time_utc": "2026-05-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "CHIPUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 97,
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
        "date_utc": "2026-05-06",
        "decision_time_utc": "2026-05-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 97,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-07",
        "decision_time_utc": "2026-05-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 97,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-08",
        "decision_time_utc": "2026-05-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 1,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 97,
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
        "date_utc": "2026-05-15",
        "decision_time_utc": "2026-05-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 97,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2026-05-16",
        "decision_time_utc": "2026-05-16T00:00:00+00:00",
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
        "date_utc": "2026-05-22",
        "decision_time_utc": "2026-05-22T00:00:00+00:00",
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
        "date_utc": "2026-05-23",
        "decision_time_utc": "2026-05-23T00:00:00+00:00",
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
        "date_utc": "2026-05-24",
        "decision_time_utc": "2026-05-24T00:00:00+00:00",
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
        "date_utc": "2026-05-25",
        "decision_time_utc": "2026-05-25T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT"
        ],
        "candidate_count": 1,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 99,
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
          "BTCUSDT"
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
        "date_utc": "2026-06-01",
        "decision_time_utc": "2026-06-01T00:00:00+00:00",
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
