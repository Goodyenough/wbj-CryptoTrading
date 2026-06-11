---
created: 2026-06-11 21:56:22 CST
tags:
  - crypto
  - trading-system
  - backtest
backtest_run_id: 263dff513b17
report_version: v14
sample_sufficient: true
universe_mode: true
universe_type: dynamic
---

# 回测报告 2024-07-01 至 2025-06-01 v14

- 回测 ID：`263dff513b17`
- 交易对：`BNBUSDT`, `BTCUSDT`, `ETHUSDT`, `SOLUSDT`
- UTC 区间：2024-07-01T00:00:00+00:00 -> 2025-06-01T00:00:00+00:00
- 初始权益：10,000.00 USDT
- 最终权益：11,413.70 USDT
- 净收益：14.14%
- 代码 commit：`d8a90ede399147dfdaf855d4f188ce45ddf2f9e2`
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

- Source / 来源：Binance current exchangeInfo tradable USDT spot symbols; cap_split=large_cap
- Master symbols / Master 币种数：4
- Source limit / 调试截断：None
- Source limit applied / 是否截断：false
- Refresh frequency / 刷新频率：daily
- Universe refreshes / Universe 刷新次数：336
- Selected symbols per refresh / 每次入选数量：min=4, avg=4.00, max=4
- Top selected symbols / 最常入选：`BNBUSDT`(336), `BTCUSDT`(336), `ETHUSDT`(336), `SOLUSDT`(336)
- Filter counts / 过滤统计：
```json
{
  "missing_1h": 0,
  "insufficient_24h": 0,
  "reconstruct_error": 0,
  "low_quote_volume": 0,
  "low_trades": 0,
  "stable_like": 0
}
```
> Warning / 警告：dynamic universe 的 symbol master 来自当前 Binance exchangeInfo；历史上曾交易但今天已退市的币不会进入 master list，因此仍有退市幸存者偏差。
> Runtime / 耗时提示：第一次完整运行需要缓存大量 1h/4h/1d K 线，可能很慢；缓存命中后后续回测会明显加快。

## 核心指标

| Metric（指标） | Value（数值） |
|---|---:|
| Trades（计划总数） | 40 |
| Closed trades（已结束交易） | 25 |
| Open trades（仍开放持仓） | 4 |
| Win rate（胜率） | 52.00% |
| Profit factor（盈利因子） | 2.02 |
| Avg R（平均R倍数） | 0.56 |
| Net return（净收益率） | 14.14% |
| Max drawdown（最大回撤） | 906.15 / 7.77% |
| Intrabar max drawdown（K线内最大回撤） | 883.06 / 7.62% |
| TP1 touched rate（第一止盈触达率） | 52.00% |
| TP2 close rate（第二止盈平仓率） | 24.00% |
| Stop rate（止损率） | 76.00% |
| Fee drag（手续费拖累） | 57.71 USDT |
| Tail max single loss（最大单笔亏损） | -122.31 USDT |
| CAGR（年化复合收益率） | 15.50% |
| Sharpe（夏普比率） | 1.25 |
| Sortino（索提诺比率） | 1.30 |
| Exposure（持仓暴露时间） | 53.33% |
| Turnover（换手率） | 4.96 |
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
| BTC buy-hold（买入并持有BTC） | 64.71% |
| ETH buy-hold（买入并持有ETH） | -27.81% |
| Cash（现金不交易） | 0.00% |
| Equal-weight symbols（等权持有本次币种） | 13.77% |

## 已结束交易

| Symbol（交易对） | Status（状态） | Created（创建时间） | Entry（入场价） | Exit（出场价） | Qty（数量） | Gross PnL（毛盈亏） | Net PnL（净盈亏） | Net R（净R倍数） | Fees（手续费） | Notes（备注） |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| `BTCUSDT` | STOPPED（已止损） | 2024-09-23T00:00:00+00:00 | 63,225.93 | 65,376.51 | 0.06 | 120.85 | 115.75 | 1.14 | 5.09 | EMA20 trailing stop hit. |
| `ETHUSDT` | STOPPED（已止损） | 2024-09-23T08:00:00+00:00 | 2,596.55 | 2,475.98 | 0.86 | -103.18 | -106.19 | -1.05 | 3.01 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2024-10-12T00:00:00+00:00 | 62,635.36 | 71,176.52 | 0.02 | 188.22 | 186.10 | 1.85 | 2.12 | EMA20 trailing stop hit. |
| `ETHUSDT` | CLOSED（已按TP2平仓） | 2024-10-13T12:00:00+00:00 | 2,463.60 | 2,938.69 | 0.60 | 285.46 | 284.16 | 2.82 | 1.30 | TP2 hit; paper trade closed. |
| `SOLUSDT` | CLOSED（已按TP2平仓） | 2024-10-22T12:00:00+00:00 | 166.01 | 204.56 | 7.07 | 272.52 | 271.47 | 2.64 | 1.05 | TP2 hit; paper trade closed. |
| `BTCUSDT` | STOPPED（已止损） | 2024-11-02T04:00:00+00:00 | 69,616.55 | 67,720.05 | 0.06 | -108.17 | -113.63 | -1.09 | 5.45 | Stop loss hit. |
| `BTCUSDT` | CLOSED（已按TP2平仓） | 2024-11-04T04:00:00+00:00 | 68,783.56 | 76,182.10 | 0.04 | 326.43 | 323.88 | 3.17 | 2.56 | TP2 hit; paper trade closed. |
| `BNBUSDT` | STOPPED（已止损） | 2024-11-08T00:00:00+00:00 | 592.36 | 642.92 | 2.23 | 112.84 | 110.87 | 1.01 | 1.96 | EMA20 trailing stop hit. |
| `ETHUSDT` | STOPPED（已止损） | 2024-11-12T12:00:00+00:00 | 3,258.73 | 3,759.44 | 0.35 | 177.44 | 175.65 | 1.58 | 1.79 | EMA20 trailing stop hit. |
| `SOLUSDT` | STOPPED（已止损） | 2024-11-13T16:00:00+00:00 | 216.03 | 235.64 | 5.75 | 112.68 | 110.83 | 1.00 | 1.85 | EMA20 trailing stop hit. |
| `BTCUSDT` | STOPPED（已止损） | 2024-11-16T16:00:00+00:00 | 90,631.09 | 97,125.60 | 0.02 | 137.08 | 134.27 | 1.21 | 2.82 | EMA20 trailing stop hit. |
| `BNBUSDT` | STOPPED（已止损） | 2024-11-25T00:00:00+00:00 | 659.05 | 605.22 | 2.15 | -115.55 | -117.41 | -1.03 | 1.87 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2024-11-25T00:00:00+00:00 | 98,007.08 | 94,204.45 | 0.03 | -118.16 | -122.31 | -1.06 | 4.15 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2024-11-27T16:00:00+00:00 | 95,890.60 | 104,729.58 | 0.02 | 154.28 | 151.79 | 1.35 | 2.50 | EMA20 trailing stop hit. |
| `SOLUSDT` | STOPPED（已止损） | 2024-11-27T16:00:00+00:00 | 241.43 | 218.25 | 4.92 | -113.95 | -115.50 | -1.02 | 1.55 | Stop loss hit. |
| `BNBUSDT` | CLOSED（已按TP2平仓） | 2024-11-27T16:00:00+00:00 | 638.73 | 772.23 | 2.36 | 315.70 | 314.37 | 2.79 | 1.33 | TP2 hit; paper trade closed. |
| `SOLUSDT` | STOPPED（已止损） | 2024-12-04T00:00:00+00:00 | 234.74 | 211.56 | 5.00 | -115.81 | -117.33 | -1.02 | 1.53 | Stop loss hit. |
| `BNBUSDT` | STOPPED（已止损） | 2024-12-06T04:00:00+00:00 | 731.90 | 612.89 | 0.98 | -116.59 | -117.48 | -1.01 | 0.89 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2024-12-06T08:00:00+00:00 | 3,862.73 | 3,444.05 | 0.28 | -116.36 | -117.74 | -1.02 | 1.39 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-01-03T00:00:00+00:00 | 97,239.11 | 90,562.57 | 0.02 | -116.69 | -118.95 | -1.03 | 2.26 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-01-03T08:00:00+00:00 | 3,442.32 | 3,260.91 | 0.64 | -116.63 | -119.61 | -1.04 | 2.98 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-01-15T04:00:00+00:00 | 97,333.55 | 87,829.92 | 0.01 | -112.60 | -114.11 | -1.02 | 1.50 | Stop loss hit. |
| `ETHUSDT` | STOPPED（已止损） | 2025-01-16T08:00:00+00:00 | 3,396.15 | 2,873.32 | 0.22 | -112.80 | -113.71 | -1.01 | 0.91 | Stop loss hit. |
| `ETHUSDT` | CLOSED（已按TP2平仓） | 2025-04-25T08:00:00+00:00 | 1,766.22 | 2,248.32 | 0.61 | 294.56 | 293.58 | 2.71 | 0.98 | TP2 hit; paper trade closed. |
| `BTCUSDT` | CLOSED（已按TP2平仓） | 2025-04-28T08:00:00+00:00 | 94,464.15 | 103,945.22 | 0.04 | 340.79 | 337.93 | 3.08 | 2.85 | TP2 hit; paper trade closed. |

## 回测结束仍开放

| Symbol（交易对） | Status（状态） | Entry（入场价） | Qty（数量） | Unrealized Handling（未实现盈亏处理） | Notes（备注） |
|---|---|---:|---:|---|---|
| `BTCUSDT` | ENTERED（已入场） | 102,242.99 | 0.01 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |
| `BNBUSDT` | ENTERED（已入场） | 649.68 | 2.27 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |
| `SOLUSDT` | ENTERED（已入场） | 170.76 | 5.33 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |
| `ETHUSDT` | ENTERED（已入场） | 2,481.78 | 0.48 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |

## 未入场/过期计划

| Symbol（交易对） | Status（状态） | Created（创建时间） | Entry Zone（入场区间） | Score（评分） | Notes（备注） |
|---|---|---|---:|---:|---|
| `ETHUSDT` | INVALIDATED（未入场前失效） | 2024-07-24T00:00:00+00:00 | 3,483.94 - 3,492.96 | 62.23 | Plan invalidated before entry: current price is below stop loss. |
| `BTCUSDT` | INVALIDATED（未入场前失效） | 2024-07-24T20:00:00+00:00 | 65,626.04 - 65,848.96 | 35.03 | Plan invalidated before entry: current price is below stop loss. |
| `BNBUSDT` | INVALIDATED（未入场前失效） | 2024-10-22T16:00:00+00:00 | 595.37 - 598.59 | 45.18 | Plan invalidated before entry: current price is below stop loss. |
| `BTCUSDT` | EXPIRED（观察计划过期） | 2024-11-08T00:00:00+00:00 | 73,527.37 - 74,542.55 | 67.35 | Backtest WATCHING plan expired before entry. |
| `SOLUSDT` | EXPIRED（观察计划过期） | 2024-11-10T00:00:00+00:00 | 194.87 - 197.80 | 69.47 | Backtest WATCHING plan expired before entry. |
| `BTCUSDT` | EXPIRED（观察计划过期） | 2024-11-13T12:00:00+00:00 | 84,928.45 - 86,483.36 | 74.54 | Backtest WATCHING plan expired before entry. |
| `SOLUSDT` | EXPIRED（观察计划过期） | 2024-11-21T04:00:00+00:00 | 230.06 - 234.28 | 50.22 | Backtest WATCHING plan expired before entry. |
| `SOLUSDT` | INVALIDATED（未入场前失效） | 2024-11-25T12:00:00+00:00 | 252.43 - 252.93 | 50.50 | Plan invalidated before entry: current price is below stop loss. |
| `SOLUSDT` | INVALIDATED（未入场前失效） | 2024-12-17T20:00:00+00:00 | 226.91 - 228.13 | 59.54 | Plan invalidated before entry: current price is below stop loss. |
| `SOLUSDT` | INVALIDATED（未入场前失效） | 2025-01-06T12:00:00+00:00 | 213.54 - 215.25 | 56.96 | Plan invalidated before entry: current price is below stop loss. |
| `BTCUSDT` | EXPIRED（观察计划过期） | 2025-04-25T00:00:00+00:00 | 91,873.03 - 92,606.43 | 67.35 | Backtest WATCHING plan expired before entry. |

## 数据质量摘要

| Severity（严重程度） | Symbol（交易对） | Interval（周期） | Message（说明） |
|---|---|---|---|
| OK | n/a | n/a | No issues recorded. |

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
    "max_holding_bars_without_tp1": 0,
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
    "risk_off_core_buy_enabled": false,
    "regime_btc_7d_drop_pct": -3.0,
    "regime_eth_7d_drop_pct": -5.0,
    "regime_require_both_trend": true,
    "entry_reclaim_close_enabled": true,
    "tp1_move_stop_to_breakeven_enabled": false,
    "tp1_ema_trailing_stop_enabled": true,
    "daily_trend_required": false,
    "validation_pool_multiplier": 2,
    "validation_pool_max": 10
  },
  "market_top_n": 5,
  "universe_mode": false,
  "universe_snapshot": null,
  "dynamic_universe_mode": true,
  "dynamic_universe_summary": {
    "mode": "dynamic_universe",
    "source": "Binance current exchangeInfo tradable USDT spot symbols; cap_split=large_cap",
    "created_at_utc": "2026-06-11T13:56:22+00:00",
    "refresh_frequency": "daily",
    "max_symbols": 4,
    "master_count": 4,
    "source_limit": null,
    "source_limit_applied": false,
    "universe_refresh_count": 336,
    "selected_count_min": 4,
    "selected_count_avg": 4.0,
    "selected_count_max": 4,
    "top_selected_symbols": [
      {
        "symbol": "BNBUSDT",
        "days_selected": 336
      },
      {
        "symbol": "BTCUSDT",
        "days_selected": 336
      },
      {
        "symbol": "ETHUSDT",
        "days_selected": 336
      },
      {
        "symbol": "SOLUSDT",
        "days_selected": 336
      }
    ],
    "filter_counts": {
      "missing_1h": 0,
      "insufficient_24h": 0,
      "reconstruct_error": 0,
      "low_quote_volume": 0,
      "low_trades": 0,
      "stable_like": 0
    },
    "selection_by_day": [
      {
        "date_utc": "2024-07-01",
        "decision_time_utc": "2024-07-01T04:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-02",
        "decision_time_utc": "2024-07-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-03",
        "decision_time_utc": "2024-07-03T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-04",
        "decision_time_utc": "2024-07-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-05",
        "decision_time_utc": "2024-07-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-06",
        "decision_time_utc": "2024-07-06T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-07",
        "decision_time_utc": "2024-07-07T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "ETHUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-08",
        "decision_time_utc": "2024-07-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-09",
        "decision_time_utc": "2024-07-09T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "BTCUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-10",
        "decision_time_utc": "2024-07-10T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-11",
        "decision_time_utc": "2024-07-11T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-12",
        "decision_time_utc": "2024-07-12T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-13",
        "decision_time_utc": "2024-07-13T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-14",
        "decision_time_utc": "2024-07-14T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-15",
        "decision_time_utc": "2024-07-15T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-16",
        "decision_time_utc": "2024-07-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-17",
        "decision_time_utc": "2024-07-17T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-18",
        "decision_time_utc": "2024-07-18T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-19",
        "decision_time_utc": "2024-07-19T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-20",
        "decision_time_utc": "2024-07-20T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-21",
        "decision_time_utc": "2024-07-21T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-22",
        "decision_time_utc": "2024-07-22T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-23",
        "decision_time_utc": "2024-07-23T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-24",
        "decision_time_utc": "2024-07-24T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-25",
        "decision_time_utc": "2024-07-25T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-26",
        "decision_time_utc": "2024-07-26T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-27",
        "decision_time_utc": "2024-07-27T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-28",
        "decision_time_utc": "2024-07-28T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-29",
        "decision_time_utc": "2024-07-29T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-30",
        "decision_time_utc": "2024-07-30T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-07-31",
        "decision_time_utc": "2024-07-31T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ETHUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-01",
        "decision_time_utc": "2024-08-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-02",
        "decision_time_utc": "2024-08-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-03",
        "decision_time_utc": "2024-08-03T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-04",
        "decision_time_utc": "2024-08-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-05",
        "decision_time_utc": "2024-08-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-06",
        "decision_time_utc": "2024-08-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-07",
        "decision_time_utc": "2024-08-07T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ETHUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-08",
        "decision_time_utc": "2024-08-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-09",
        "decision_time_utc": "2024-08-09T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-10",
        "decision_time_utc": "2024-08-10T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-11",
        "decision_time_utc": "2024-08-11T00:00:00+00:00",
        "selected_symbols": [
          "BNBUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-12",
        "decision_time_utc": "2024-08-12T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-13",
        "decision_time_utc": "2024-08-13T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-14",
        "decision_time_utc": "2024-08-14T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-15",
        "decision_time_utc": "2024-08-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-16",
        "decision_time_utc": "2024-08-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-17",
        "decision_time_utc": "2024-08-17T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-18",
        "decision_time_utc": "2024-08-18T00:00:00+00:00",
        "selected_symbols": [
          "BNBUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-19",
        "decision_time_utc": "2024-08-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-20",
        "decision_time_utc": "2024-08-20T00:00:00+00:00",
        "selected_symbols": [
          "BNBUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-21",
        "decision_time_utc": "2024-08-21T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ETHUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-22",
        "decision_time_utc": "2024-08-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-23",
        "decision_time_utc": "2024-08-23T00:00:00+00:00",
        "selected_symbols": [
          "BNBUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-24",
        "decision_time_utc": "2024-08-24T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-25",
        "decision_time_utc": "2024-08-25T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-26",
        "decision_time_utc": "2024-08-26T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-27",
        "decision_time_utc": "2024-08-27T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-28",
        "decision_time_utc": "2024-08-28T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-29",
        "decision_time_utc": "2024-08-29T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-30",
        "decision_time_utc": "2024-08-30T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-08-31",
        "decision_time_utc": "2024-08-31T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-01",
        "decision_time_utc": "2024-09-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-02",
        "decision_time_utc": "2024-09-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-03",
        "decision_time_utc": "2024-09-03T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-04",
        "decision_time_utc": "2024-09-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-05",
        "decision_time_utc": "2024-09-05T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-06",
        "decision_time_utc": "2024-09-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-07",
        "decision_time_utc": "2024-09-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-08",
        "decision_time_utc": "2024-09-08T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-09",
        "decision_time_utc": "2024-09-09T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-10",
        "decision_time_utc": "2024-09-10T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-11",
        "decision_time_utc": "2024-09-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-12",
        "decision_time_utc": "2024-09-12T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ETHUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-13",
        "decision_time_utc": "2024-09-13T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "ETHUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-14",
        "decision_time_utc": "2024-09-14T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-15",
        "decision_time_utc": "2024-09-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-16",
        "decision_time_utc": "2024-09-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-17",
        "decision_time_utc": "2024-09-17T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-18",
        "decision_time_utc": "2024-09-18T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-19",
        "decision_time_utc": "2024-09-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-20",
        "decision_time_utc": "2024-09-20T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-21",
        "decision_time_utc": "2024-09-21T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-22",
        "decision_time_utc": "2024-09-22T00:00:00+00:00",
        "selected_symbols": [
          "BNBUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BTCUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-23",
        "decision_time_utc": "2024-09-23T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-24",
        "decision_time_utc": "2024-09-24T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-25",
        "decision_time_utc": "2024-09-25T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-26",
        "decision_time_utc": "2024-09-26T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-27",
        "decision_time_utc": "2024-09-27T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-28",
        "decision_time_utc": "2024-09-28T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-29",
        "decision_time_utc": "2024-09-29T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-09-30",
        "decision_time_utc": "2024-09-30T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-01",
        "decision_time_utc": "2024-10-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-02",
        "decision_time_utc": "2024-10-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-03",
        "decision_time_utc": "2024-10-03T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-04",
        "decision_time_utc": "2024-10-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-05",
        "decision_time_utc": "2024-10-05T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-06",
        "decision_time_utc": "2024-10-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-07",
        "decision_time_utc": "2024-10-07T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-08",
        "decision_time_utc": "2024-10-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-09",
        "decision_time_utc": "2024-10-09T00:00:00+00:00",
        "selected_symbols": [
          "BNBUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-10",
        "decision_time_utc": "2024-10-10T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-11",
        "decision_time_utc": "2024-10-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-12",
        "decision_time_utc": "2024-10-12T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-13",
        "decision_time_utc": "2024-10-13T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-14",
        "decision_time_utc": "2024-10-14T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-15",
        "decision_time_utc": "2024-10-15T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-16",
        "decision_time_utc": "2024-10-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-17",
        "decision_time_utc": "2024-10-17T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-18",
        "decision_time_utc": "2024-10-18T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-19",
        "decision_time_utc": "2024-10-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-20",
        "decision_time_utc": "2024-10-20T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-21",
        "decision_time_utc": "2024-10-21T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-22",
        "decision_time_utc": "2024-10-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-23",
        "decision_time_utc": "2024-10-23T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-24",
        "decision_time_utc": "2024-10-24T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-25",
        "decision_time_utc": "2024-10-25T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-26",
        "decision_time_utc": "2024-10-26T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-27",
        "decision_time_utc": "2024-10-27T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-28",
        "decision_time_utc": "2024-10-28T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-29",
        "decision_time_utc": "2024-10-29T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-30",
        "decision_time_utc": "2024-10-30T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-10-31",
        "decision_time_utc": "2024-10-31T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-01",
        "decision_time_utc": "2024-11-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-02",
        "decision_time_utc": "2024-11-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-03",
        "decision_time_utc": "2024-11-03T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-04",
        "decision_time_utc": "2024-11-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-05",
        "decision_time_utc": "2024-11-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-06",
        "decision_time_utc": "2024-11-06T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-07",
        "decision_time_utc": "2024-11-07T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-08",
        "decision_time_utc": "2024-11-08T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-09",
        "decision_time_utc": "2024-11-09T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-10",
        "decision_time_utc": "2024-11-10T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-11",
        "decision_time_utc": "2024-11-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-12",
        "decision_time_utc": "2024-11-12T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-13",
        "decision_time_utc": "2024-11-13T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-14",
        "decision_time_utc": "2024-11-14T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-15",
        "decision_time_utc": "2024-11-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-16",
        "decision_time_utc": "2024-11-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-17",
        "decision_time_utc": "2024-11-17T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-18",
        "decision_time_utc": "2024-11-18T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-19",
        "decision_time_utc": "2024-11-19T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-20",
        "decision_time_utc": "2024-11-20T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-21",
        "decision_time_utc": "2024-11-21T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-22",
        "decision_time_utc": "2024-11-22T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-23",
        "decision_time_utc": "2024-11-23T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-24",
        "decision_time_utc": "2024-11-24T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-25",
        "decision_time_utc": "2024-11-25T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ETHUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-26",
        "decision_time_utc": "2024-11-26T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-27",
        "decision_time_utc": "2024-11-27T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-28",
        "decision_time_utc": "2024-11-28T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-29",
        "decision_time_utc": "2024-11-29T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-11-30",
        "decision_time_utc": "2024-11-30T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-01",
        "decision_time_utc": "2024-12-01T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-02",
        "decision_time_utc": "2024-12-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-03",
        "decision_time_utc": "2024-12-03T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-04",
        "decision_time_utc": "2024-12-04T00:00:00+00:00",
        "selected_symbols": [
          "BNBUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-05",
        "decision_time_utc": "2024-12-05T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-06",
        "decision_time_utc": "2024-12-06T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-07",
        "decision_time_utc": "2024-12-07T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-08",
        "decision_time_utc": "2024-12-08T00:00:00+00:00",
        "selected_symbols": [
          "BNBUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-09",
        "decision_time_utc": "2024-12-09T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-10",
        "decision_time_utc": "2024-12-10T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-11",
        "decision_time_utc": "2024-12-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-12",
        "decision_time_utc": "2024-12-12T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-13",
        "decision_time_utc": "2024-12-13T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-14",
        "decision_time_utc": "2024-12-14T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ETHUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-15",
        "decision_time_utc": "2024-12-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-16",
        "decision_time_utc": "2024-12-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-17",
        "decision_time_utc": "2024-12-17T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-18",
        "decision_time_utc": "2024-12-18T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-19",
        "decision_time_utc": "2024-12-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-20",
        "decision_time_utc": "2024-12-20T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-21",
        "decision_time_utc": "2024-12-21T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-22",
        "decision_time_utc": "2024-12-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-23",
        "decision_time_utc": "2024-12-23T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-24",
        "decision_time_utc": "2024-12-24T00:00:00+00:00",
        "selected_symbols": [
          "BNBUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BTCUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-25",
        "decision_time_utc": "2024-12-25T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-26",
        "decision_time_utc": "2024-12-26T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-27",
        "decision_time_utc": "2024-12-27T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-28",
        "decision_time_utc": "2024-12-28T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-29",
        "decision_time_utc": "2024-12-29T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BNBUSDT",
          "ETHUSDT",
          "BTCUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-30",
        "decision_time_utc": "2024-12-30T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2024-12-31",
        "decision_time_utc": "2024-12-31T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-01",
        "decision_time_utc": "2025-01-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-02",
        "decision_time_utc": "2025-01-02T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-03",
        "decision_time_utc": "2025-01-03T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-04",
        "decision_time_utc": "2025-01-04T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-05",
        "decision_time_utc": "2025-01-05T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-06",
        "decision_time_utc": "2025-01-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-07",
        "decision_time_utc": "2025-01-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-09",
        "decision_time_utc": "2025-01-09T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-10",
        "decision_time_utc": "2025-01-10T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-11",
        "decision_time_utc": "2025-01-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-12",
        "decision_time_utc": "2025-01-12T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-15",
        "decision_time_utc": "2025-01-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-16",
        "decision_time_utc": "2025-01-16T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-17",
        "decision_time_utc": "2025-01-17T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-18",
        "decision_time_utc": "2025-01-18T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-19",
        "decision_time_utc": "2025-01-19T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-21",
        "decision_time_utc": "2025-01-21T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-22",
        "decision_time_utc": "2025-01-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-23",
        "decision_time_utc": "2025-01-23T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-24",
        "decision_time_utc": "2025-01-24T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-26",
        "decision_time_utc": "2025-01-26T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-28",
        "decision_time_utc": "2025-01-28T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-30",
        "decision_time_utc": "2025-01-30T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-31",
        "decision_time_utc": "2025-01-31T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-01",
        "decision_time_utc": "2025-02-01T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-02",
        "decision_time_utc": "2025-02-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-04",
        "decision_time_utc": "2025-02-04T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-08",
        "decision_time_utc": "2025-02-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-09",
        "decision_time_utc": "2025-02-09T00:00:00+00:00",
        "selected_symbols": [
          "BNBUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BTCUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-11",
        "decision_time_utc": "2025-02-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-12",
        "decision_time_utc": "2025-02-12T00:00:00+00:00",
        "selected_symbols": [
          "BNBUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-13",
        "decision_time_utc": "2025-02-13T00:00:00+00:00",
        "selected_symbols": [
          "BNBUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-15",
        "decision_time_utc": "2025-02-15T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-16",
        "decision_time_utc": "2025-02-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-17",
        "decision_time_utc": "2025-02-17T00:00:00+00:00",
        "selected_symbols": [
          "BNBUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-18",
        "decision_time_utc": "2025-02-18T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-19",
        "decision_time_utc": "2025-02-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-20",
        "decision_time_utc": "2025-02-20T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-21",
        "decision_time_utc": "2025-02-21T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-22",
        "decision_time_utc": "2025-02-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-23",
        "decision_time_utc": "2025-02-23T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BNBUSDT",
          "SOLUSDT",
          "BTCUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-26",
        "decision_time_utc": "2025-02-26T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-27",
        "decision_time_utc": "2025-02-27T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-28",
        "decision_time_utc": "2025-02-28T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-01",
        "decision_time_utc": "2025-03-01T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "ETHUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-03",
        "decision_time_utc": "2025-03-03T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-05",
        "decision_time_utc": "2025-03-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-06",
        "decision_time_utc": "2025-03-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-07",
        "decision_time_utc": "2025-03-07T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-08",
        "decision_time_utc": "2025-03-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-09",
        "decision_time_utc": "2025-03-09T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-12",
        "decision_time_utc": "2025-03-12T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-13",
        "decision_time_utc": "2025-03-13T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ETHUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-15",
        "decision_time_utc": "2025-03-15T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-16",
        "decision_time_utc": "2025-03-16T00:00:00+00:00",
        "selected_symbols": [
          "BNBUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-17",
        "decision_time_utc": "2025-03-17T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-18",
        "decision_time_utc": "2025-03-18T00:00:00+00:00",
        "selected_symbols": [
          "BNBUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-19",
        "decision_time_utc": "2025-03-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-20",
        "decision_time_utc": "2025-03-20T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-21",
        "decision_time_utc": "2025-03-21T00:00:00+00:00",
        "selected_symbols": [
          "BNBUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-22",
        "decision_time_utc": "2025-03-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-23",
        "decision_time_utc": "2025-03-23T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-24",
        "decision_time_utc": "2025-03-24T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-25",
        "decision_time_utc": "2025-03-25T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-26",
        "decision_time_utc": "2025-03-26T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-27",
        "decision_time_utc": "2025-03-27T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-28",
        "decision_time_utc": "2025-03-28T00:00:00+00:00",
        "selected_symbols": [
          "BNBUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-02",
        "decision_time_utc": "2025-04-02T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-04",
        "decision_time_utc": "2025-04-04T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-05",
        "decision_time_utc": "2025-04-05T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-08",
        "decision_time_utc": "2025-04-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-10",
        "decision_time_utc": "2025-04-10T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-12",
        "decision_time_utc": "2025-04-12T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-13",
        "decision_time_utc": "2025-04-13T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-17",
        "decision_time_utc": "2025-04-17T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-20",
        "decision_time_utc": "2025-04-20T00:00:00+00:00",
        "selected_symbols": [
          "SOLUSDT",
          "BTCUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-21",
        "decision_time_utc": "2025-04-21T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-22",
        "decision_time_utc": "2025-04-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-23",
        "decision_time_utc": "2025-04-23T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-24",
        "decision_time_utc": "2025-04-24T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-25",
        "decision_time_utc": "2025-04-25T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-26",
        "decision_time_utc": "2025-04-26T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-29",
        "decision_time_utc": "2025-04-29T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-01",
        "decision_time_utc": "2025-05-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-02",
        "decision_time_utc": "2025-05-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-06",
        "decision_time_utc": "2025-05-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-09",
        "decision_time_utc": "2025-05-09T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-10",
        "decision_time_utc": "2025-05-10T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "BTCUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-11",
        "decision_time_utc": "2025-05-11T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-13",
        "decision_time_utc": "2025-05-13T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-14",
        "decision_time_utc": "2025-05-14T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "SOLUSDT",
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-15",
        "decision_time_utc": "2025-05-15T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-16",
        "decision_time_utc": "2025-05-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-17",
        "decision_time_utc": "2025-05-17T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-19",
        "decision_time_utc": "2025-05-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-20",
        "decision_time_utc": "2025-05-20T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-21",
        "decision_time_utc": "2025-05-21T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-22",
        "decision_time_utc": "2025-05-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT",
          "ETHUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-23",
        "decision_time_utc": "2025-05-23T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-24",
        "decision_time_utc": "2025-05-24T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ETHUSDT",
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-25",
        "decision_time_utc": "2025-05-25T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "SOLUSDT",
          "ETHUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-28",
        "decision_time_utc": "2025-05-28T00:00:00+00:00",
        "selected_symbols": [
          "ETHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "SOLUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
          "SOLUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 0,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 0,
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
