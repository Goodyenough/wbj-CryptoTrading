---
created: 2026-06-09 02:00:04 CST
tags:
  - crypto
  - trading-system
  - backtest
backtest_run_id: 3ad4659b89d8
report_version: v1
sample_sufficient: true
universe_mode: true
universe_type: dynamic
---

# 回测报告 2025-09-01 至 2026-06-01 v1

- 回测 ID：`3ad4659b89d8`
- 交易对：`0GUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `2ZUSDT`, `AAVEUSDT`, `ACEUSDT`, `ADAUSDT`, `AEVOUSDT`, `AIGENSYNUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALCXUSDT`, `ALGOUSDT`, `ALICEUSDT`, `ALLOUSDT`, `ALPINEUSDT`, `ALTUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARKMUSDT`, `ARPAUSDT`, `ARUSDT`, `ASTERUSDT`, `ATOMUSDT`, `ATUSDT`, `AUCTIONUSDT`, `AUSDT`, `AVAXUSDT`, `AVNTUSDT`, `AWEUSDT`, `AXSUSDT`, `BABYUSDT`, `BANANAS31USDT`, `BARDUSDT`, `BATUSDT`, `BBUSDT`, `BCHUSDT`, `BELUSDT`, `BERAUSDT`, `BIOUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BREVUSDT`, `BROCCOLI714USDT`, `BTCUSDT`, `C98USDT`, `CAKEUSDT`, `CELOUSDT`, `CFGUSDT`, `CFXUSDT`, `CHIPUSDT`, `CHZUSDT`, `COSUSDT`, `COTIUSDT`, `COWUSDT`
- UTC 区间：2025-09-01T00:00:00+00:00 -> 2026-06-01T00:00:00+00:00
- 初始权益：10,000.00 USDT
- 最终权益：8,991.28 USDT
- 净收益：-10.09%
- 代码 commit：`8147332e5066dabcd8b03e6c9507cffc7ba513a8`
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
- Universe refreshes / Universe 刷新次数：274
- Selected symbols per refresh / 每次入选数量：min=2, avg=5.60, max=18
- Top selected symbols / 最常入选：`BNBUSDT`(274), `BTCUSDT`(274), `ADAUSDT`(198), `AVAXUSDT`(149), `ASTERUSDT`(111), `BCHUSDT`(82), `AAVEUSDT`(54), `ARBUSDT`(46), `BONKUSDT`(43), `AVNTUSDT`(36)
- Filter counts / 过滤统计：
```json
{
  "missing_1h": 1171,
  "insufficient_24h": 12,
  "reconstruct_error": 0,
  "low_quote_volume": 24667,
  "low_trades": 14,
  "stable_like": 2
}
```
> Warning / 警告：dynamic universe 的 symbol master 来自当前 Binance exchangeInfo；历史上曾交易但今天已退市的币不会进入 master list，因此仍有退市幸存者偏差。
> Runtime / 耗时提示：第一次完整运行需要缓存大量 1h/4h/1d K 线，可能很慢；缓存命中后后续回测会明显加快。

## 核心指标

| Metric（指标） | Value（数值） |
|---|---:|
| Trades（计划总数） | 37 |
| Closed trades（已结束交易） | 20 |
| Open trades（仍开放持仓） | 3 |
| Win rate（胜率） | 15.00% |
| Profit factor（盈利因子） | 0.45 |
| Avg R（平均R倍数） | -0.48 |
| Net return（净收益率） | -10.09% |
| Max drawdown（最大回撤） | 1,922.85 / 18.06% |
| Intrabar max drawdown（K线内最大回撤） | 1,906.38 / 17.99% |
| TP1 touched rate（第一止盈触达率） | 25.00% |
| TP2 close rate（第二止盈平仓率） | 15.00% |
| Stop rate（止损率） | 85.00% |
| Fee drag（手续费拖累） | 41.58 USDT |
| Tail max single loss（最大单笔亏损） | -112.38 USDT |
| CAGR（年化复合收益率） | -13.25% |
| Sharpe（夏普比率） | -1.09 |
| Sortino（索提诺比率） | -1.02 |
| Exposure（持仓暴露时间） | 72.41% |
| Turnover（换手率） | 3.45 |
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
| BTC buy-hold（买入并持有BTC） | -31.64% |
| ETH buy-hold（买入并持有ETH） | -54.47% |
| Cash（现金不交易） | 0.00% |
| Equal-weight symbols（等权持有本次币种） | -57.88% |

## 已结束交易

| Symbol（交易对） | Status（状态） | Created（创建时间） | Entry（入场价） | Exit（出场价） | Qty（数量） | Gross PnL（毛盈亏） | Net PnL（净盈亏） | Net R（净R倍数） | Fees（手续费） | Notes（备注） |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| `BTCUSDT` | STOPPED（已止损） | 2025-09-05T08:00:00+00:00 | 113,079.17 | 106,660.72 | 0.02 | -102.61 | -105.04 | -1.04 | 2.43 | Stop loss hit. |
| `AVAXUSDT` | CLOSED（已按TP2平仓） | 2025-09-16T00:00:00+00:00 | 29.85 | 34.86 | 49.25 | 246.92 | 245.65 | 2.43 | 1.27 | TP2 hit; paper trade closed. |
| `BNBUSDT` | CLOSED（已按TP2平仓） | 2025-09-16T08:00:00+00:00 | 930.05 | 1,025.84 | 3.09 | 295.59 | 293.18 | 2.87 | 2.41 | TP2 hit; paper trade closed. |
| `BONKUSDT` | STOPPED（已止损） | 2025-09-16T20:00:00+00:00 | 0.00 | 0.00 | 45,914,145.85 | -103.05 | -104.51 | -1.02 | 1.46 | Stop loss hit. |
| `ADAUSDT` | STOPPED（已止损） | 2025-09-17T08:00:00+00:00 | 0.89 | 0.84 | 2,289.93 | -106.75 | -109.48 | -1.04 | 2.73 | Stop loss hit. |
| `BCHUSDT` | STOPPED（已止损） | 2025-09-18T00:00:00+00:00 | 604.38 | 578.40 | 4.19 | -108.94 | -112.38 | -1.06 | 3.44 | Stop loss hit. |
| `AAVEUSDT` | STOPPED（已止损） | 2025-09-18T04:00:00+00:00 | 309.62 | 284.85 | 4.38 | -108.36 | -110.15 | -1.03 | 1.79 | Stop loss hit. |
| `BNBUSDT` | STOPPED（已止损） | 2025-09-21T12:00:00+00:00 | 1,025.08 | 958.33 | 1.54 | -102.59 | -104.69 | -1.04 | 2.10 | Stop loss hit. |
| `CAKEUSDT` | STOPPED（已止损） | 2025-09-21T12:00:00+00:00 | 2.89 | 2.59 | 348.35 | -103.53 | -104.83 | -1.02 | 1.31 | Stop loss hit. |
| `ADAUSDT` | STOPPED（已止损） | 2025-10-02T00:00:00+00:00 | 0.85 | 0.77 | 1,274.82 | -101.37 | -102.78 | -1.02 | 1.41 | Stop loss hit. |
| `AAVEUSDT` | STOPPED（已止损） | 2025-10-02T00:00:00+00:00 | 287.76 | 261.85 | 3.91 | -101.41 | -102.89 | -1.02 | 1.47 | Stop loss hit. |
| `AVAXUSDT` | STOPPED（已止损） | 2025-10-02T20:00:00+00:00 | 30.78 | 28.35 | 42.00 | -102.18 | -103.89 | -1.03 | 1.71 | Stop loss hit. |
| `ARBUSDT` | STOPPED（已止损） | 2025-10-03T04:00:00+00:00 | 0.44 | 0.40 | 2,260.74 | -102.48 | -103.78 | -1.02 | 1.30 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-10-21T16:00:00+00:00 | 113,819.76 | 104,407.30 | 0.01 | -95.38 | -96.90 | -1.03 | 1.52 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-11-30T04:00:00+00:00 | 91,152.21 | 88,714.33 | 0.04 | -98.19 | -103.23 | -1.09 | 5.04 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-12-03T08:00:00+00:00 | 93,325.63 | 82,482.85 | 0.01 | -92.85 | -93.88 | -1.02 | 1.03 | Stop loss hit. |
| `BNBUSDT` | STOPPED（已止损） | 2026-01-18T00:00:00+00:00 | 944.78 | 908.92 | 2.67 | -95.58 | -99.02 | -1.06 | 3.43 | Stop loss hit. |
| `BNBUSDT` | CLOSED（已按TP2平仓） | 2026-04-16T00:00:00+00:00 | 618.86 | 718.19 | 2.53 | 250.99 | 249.64 | 2.73 | 1.35 | TP2 hit; paper trade closed. |
| `AVAXUSDT` | STOPPED（已止损） | 2026-04-17T00:00:00+00:00 | 9.63 | 9.06 | 165.28 | -93.05 | -95.18 | -1.04 | 2.13 | Stop loss hit. |
| `ADAUSDT` | STOPPED（已止损） | 2026-04-17T00:00:00+00:00 | 0.25 | 0.23 | 4,578.27 | -92.28 | -93.82 | -1.03 | 1.54 | Stop loss hit. |

## 回测结束仍开放

| Symbol（交易对） | Status（状态） | Entry（入场价） | Qty（数量） | Unrealized Handling（未实现盈亏处理） | Notes（备注） |
|---|---|---:|---:|---|---|
| `BTCUSDT` | TP1_HIT（第一止盈已触达） | 69,208.02 | 0.01 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |
| `ALICEUSDT` | ENTERED（已入场） | 0.15 | 2,388.09 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |
| `BOMEUSDT` | ENTERED（已入场） | 0.00 | 925,369.35 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |

## 未入场/过期计划

| Symbol（交易对） | Status（状态） | Created（创建时间） | Entry Zone（入场区间） | Score（评分） | Notes（备注） |
|---|---|---|---:|---:|---|
| `ARBUSDT` | EXPIRED（观察计划过期） | 2025-09-18T00:00:00+00:00 | 0.51 - 0.52 | 46.78 | Backtest WATCHING plan expired before entry. |
| `BIOUSDT` | INVALIDATED（未入场前失效） | 2025-09-21T00:00:00+00:00 | 0.18 - 0.18 | 73.51 | Plan invalidated before entry: current price is below stop loss. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-10-02T00:00:00+00:00 | 1,011.09 - 1,019.11 | 63.44 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | EXPIRED（观察计划过期） | 2025-10-03T16:00:00+00:00 | 0.00 - 0.00 | 54.75 | Backtest WATCHING plan expired before entry. |
| `BNBUSDT` | EXPIRED（观察计划过期） | 2025-10-05T12:00:00+00:00 | 1,131.18 - 1,149.27 | 72.89 | Backtest WATCHING plan expired before entry. |
| `APTUSDT` | EXPIRED（观察计划过期） | 2025-10-05T20:00:00+00:00 | 5.26 - 5.38 | 76.12 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | INVALIDATED（未入场前失效） | 2025-10-07T00:00:00+00:00 | 0.00 - 0.00 | 62.93 | Plan invalidated before entry: current price is below stop loss. |
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
| WARNING | `1000CATUSDT` | 4h | Large wick/range candle. |
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
| WARNING | `1INCHUSDT` | 1h | Large wick/range candle. |
| WARNING | `1INCHUSDT` | 4h | Large wick/range candle. |
| WARNING | `1INCHUSDT` | 1d | Large wick/range candle. |
| WARNING | `1INCHUSDT` | 1d | Large wick/range candle. |
| WARNING | `1MBABYDOGEUSDT` | 1h | Large wick/range candle. |
| WARNING | `1MBABYDOGEUSDT` | 1h | Large wick/range candle. |
| WARNING | `1MBABYDOGEUSDT` | 4h | Large wick/range candle. |
| WARNING | `1MBABYDOGEUSDT` | 1d | Large wick/range candle. |
| WARNING | `1MBABYDOGEUSDT` | 1d | Large wick/range candle. |
| WARNING | `2ZUSDT` | 1h | Large wick/range candle. |
| WARNING | `2ZUSDT` | 1h | Large wick/range candle. |
| WARNING | `2ZUSDT` | 1h | Large wick/range candle. |
| WARNING | `2ZUSDT` | 4h | Large wick/range candle. |
| WARNING | `2ZUSDT` | 4h | Large wick/range candle. |
| WARNING | `2ZUSDT` | 4h | Large wick/range candle. |
| WARNING | `2ZUSDT` | 4h | Large wick/range candle. |
| WARNING | `2ZUSDT` | 1d | Large wick/range candle. |
| WARNING | `2ZUSDT` | 1d | Large wick/range candle. |
| INFO | n/a | n/a | Additional issues omitted: 969. |

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
    "created_at_utc": "2026-06-08T18:00:04+00:00",
    "refresh_frequency": "daily",
    "max_symbols": 30,
    "master_count": 100,
    "source_limit": 100,
    "source_limit_applied": true,
    "universe_refresh_count": 274,
    "selected_count_min": 2,
    "selected_count_avg": 5.598540145985401,
    "selected_count_max": 18,
    "top_selected_symbols": [
      {
        "symbol": "BNBUSDT",
        "days_selected": 274
      },
      {
        "symbol": "BTCUSDT",
        "days_selected": 274
      },
      {
        "symbol": "ADAUSDT",
        "days_selected": 198
      },
      {
        "symbol": "AVAXUSDT",
        "days_selected": 149
      },
      {
        "symbol": "ASTERUSDT",
        "days_selected": 111
      },
      {
        "symbol": "BCHUSDT",
        "days_selected": 82
      },
      {
        "symbol": "AAVEUSDT",
        "days_selected": 54
      },
      {
        "symbol": "ARBUSDT",
        "days_selected": 46
      },
      {
        "symbol": "BONKUSDT",
        "days_selected": 43
      },
      {
        "symbol": "AVNTUSDT",
        "days_selected": 36
      },
      {
        "symbol": "CAKEUSDT",
        "days_selected": 26
      },
      {
        "symbol": "APTUSDT",
        "days_selected": 24
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
        "symbol": "BIOUSDT",
        "days_selected": 14
      },
      {
        "symbol": "AXSUSDT",
        "days_selected": 12
      },
      {
        "symbol": "BROCCOLI714USDT",
        "days_selected": 11
      },
      {
        "symbol": "0GUSDT",
        "days_selected": 10
      }
    ],
    "filter_counts": {
      "missing_1h": 1171,
      "insufficient_24h": 12,
      "reconstruct_error": 0,
      "low_quote_volume": 24667,
      "low_trades": 14,
      "stable_like": 2
    },
    "selection_by_day": [
      {
        "date_utc": "2025-09-01",
        "decision_time_utc": "2025-09-01T04:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "AVAXUSDT"
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
