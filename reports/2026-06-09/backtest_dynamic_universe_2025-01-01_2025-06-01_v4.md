---
created: 2026-06-09 12:41:43 CST
tags:
  - crypto
  - trading-system
  - backtest
backtest_run_id: 7b80538b60e9
report_version: v4
sample_sufficient: false
universe_mode: true
universe_type: dynamic
---

# 回测报告 2025-01-01 至 2025-06-01 v4

- 回测 ID：`7b80538b60e9`
- 交易对：`1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `AAVEUSDT`, `ACHUSDT`, `ACTUSDT`, `ACXUSDT`, `ADAUSDT`, `AGLDUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALGOUSDT`, `AMPUSDT`, `ANIMEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ARUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AVAXUSDT`, `BABYUSDT`, `BCHUSDT`, `BERAUSDT`, `BIOUSDT`, `BMTUSDT`, `BNBUSDT`, `BNSOLUSDT`, `BOMEUSDT`, `BONKUSDT`, `BTCUSDT`, `CAKEUSDT`, `CETUSUSDT`, `CFXUSDT`, `CGPTUSDT`, `CKBUSDT`, `COMPUSDT`, `COOKIEUSDT`, `COWUSDT`
- UTC 区间：2025-01-01T00:00:00+00:00 -> 2025-06-01T00:00:00+00:00
- 初始权益：10,000.00 USDT
- 最终权益：9,149.05 USDT
- 净收益：-8.51%
- 代码 commit：`cf624ae3ed8e743e425db9cef65f99ab8b77b134`
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
- Master symbols / Master 币种数：100
- Source limit / 调试截断：100
- Source limit applied / 是否截断：true
- Refresh frequency / 刷新频率：daily
- Universe refreshes / Universe 刷新次数：152
- Selected symbols per refresh / 每次入选数量：min=2, avg=6.12, max=18
- Top selected symbols / 最常入选：`BNBUSDT`(152), `BTCUSDT`(152), `ADAUSDT`(144), `AVAXUSDT`(89), `AAVEUSDT`(66), `APTUSDT`(39), `BONKUSDT`(37), `ACTUSDT`(32), `ARBUSDT`(30), `BERAUSDT`(27)
- Filter counts / 过滤统计：
```json
{
  "missing_1h": 2848,
  "insufficient_24h": 14,
  "reconstruct_error": 0,
  "low_quote_volume": 11408,
  "low_trades": 0,
  "stable_like": 0
}
```
> Warning / 警告：dynamic universe 的 symbol master 来自当前 Binance exchangeInfo；历史上曾交易但今天已退市的币不会进入 master list，因此仍有退市幸存者偏差。
> Runtime / 耗时提示：第一次完整运行需要缓存大量 1h/4h/1d K 线，可能很慢；缓存命中后后续回测会明显加快。

## 核心指标

| Metric（指标） | Value（数值） |
|---|---:|
| Trades（计划总数） | 22 |
| Closed trades（已结束交易） | 12 |
| Open trades（仍开放持仓） | 2 |
| Win rate（胜率） | 8.33% |
| Profit factor（盈利因子） | 0.23 |
| Avg R（平均R倍数） | -0.71 |
| Net return（净收益率） | -8.51% |
| Max drawdown（最大回撤） | 1,053.00 / 10.33% |
| Intrabar max drawdown（K线内最大回撤） | 1,028.27 / 10.14% |
| TP1 touched rate（第一止盈触达率） | 16.67% |
| TP2 close rate（第二止盈平仓率） | 8.33% |
| Stop rate（止损率） | 91.67% |
| Fee drag（手续费拖累） | 17.85 USDT |
| Tail max single loss（最大单笔亏损） | -108.15 USDT |
| CAGR（年化复合收益率） | -19.34% |
| Sharpe（夏普比率） | -1.74 |
| Sortino（索提诺比率） | -1.54 |
| Exposure（持仓暴露时间） | 81.57% |
| Turnover（换手率） | 1.51 |
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
| Equal-weight symbols（等权持有本次币种） | -46.82% |

## 已结束交易

| Symbol（交易对） | Status（状态） | Created（创建时间） | Entry（入场价） | Exit（出场价） | Qty（数量） | Gross PnL（毛盈亏） | Net PnL（净盈亏） | Net R（净R倍数） | Fees（手续费） | Notes（备注） |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| `BTCUSDT` | STOPPED（已止损） | 2025-01-02T12:00:00+00:00 | 97,071.70 | 90,067.34 | 0.01 | -102.02 | -103.90 | -1.03 | 1.88 | Stop loss hit. |
| `BNBUSDT` | STOPPED（已止损） | 2025-01-04T00:00:00+00:00 | 712.59 | 685.89 | 3.91 | -104.35 | -108.15 | -1.06 | 3.79 | Stop loss hit. |
| `AAVEUSDT` | STOPPED（已止损） | 2025-01-04T04:00:00+00:00 | 340.44 | 301.35 | 2.59 | -101.39 | -102.53 | -1.02 | 1.13 | Stop loss hit. |
| `ADAUSDT` | STOPPED（已止损） | 2025-01-05T12:00:00+00:00 | 1.06 | 0.93 | 785.55 | -102.60 | -103.67 | -1.02 | 1.06 | Stop loss hit. |
| `ARBUSDT` | STOPPED（已止损） | 2025-01-07T00:00:00+00:00 | 0.91 | 0.81 | 1,057.40 | -102.81 | -104.05 | -1.02 | 1.24 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-01-14T20:00:00+00:00 | 96,875.83 | 87,829.92 | 0.01 | -96.23 | -97.57 | -1.02 | 1.35 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-03-06T08:00:00+00:00 | 90,332.96 | 80,197.22 | 0.01 | -94.98 | -96.07 | -1.02 | 1.09 | Stop loss hit. |
| `BTCUSDT` | STOPPED（已止损） | 2025-03-20T00:00:00+00:00 | 86,570.94 | 79,837.72 | 0.01 | -94.57 | -96.18 | -1.03 | 1.61 | Stop loss hit. |
| `BTCUSDT` | CLOSED（已按TP2平仓） | 2025-04-12T08:00:00+00:00 | 83,637.41 | 108,712.75 | 0.01 | 256.70 | 255.91 | 2.77 | 0.79 | TP2 hit; paper trade closed. |
| `ACTUSDT` | STOPPED（已止损） | 2025-05-11T04:00:00+00:00 | 0.06 | 0.05 | 8,720.66 | -94.62 | -95.28 | -1.01 | 0.66 | Stop loss hit. |
| `ADAUSDT` | STOPPED（已止损） | 2025-05-11T12:00:00+00:00 | 0.80 | 0.70 | 1,003.66 | -95.18 | -96.21 | -1.02 | 1.03 | Stop loss hit. |
| `BONKUSDT` | STOPPED（已止损） | 2025-05-12T16:00:00+00:00 | 0.00 | 0.00 | 50,949,536.08 | -96.70 | -98.20 | -1.03 | 1.50 | Stop loss hit. |

## 回测结束仍开放

| Symbol（交易对） | Status（状态） | Entry（入场价） | Qty（数量） | Unrealized Handling（未实现盈亏处理） | Notes（备注） |
|---|---|---:|---:|---|---|
| `BNBUSDT` | ENTERED（已入场） | 649.68 | 1.87 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |
| `AAVEUSDT` | ENTERED（已入场） | 255.84 | 2.28 | 按最后 close 计入净值，不计入胜率/profit_factor/avg_R | Open at backtest end; mark-to-market only. |

## 未入场/过期计划

| Symbol（交易对） | Status（状态） | Created（创建时间） | Entry Zone（入场区间） | Score（评分） | Notes（备注） |
|---|---|---|---:|---:|---|
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-01-04T12:00:00+00:00 | 40.15 - 40.76 | 72.48 | Backtest WATCHING plan expired before entry. |
| `BONKUSDT` | INVALIDATED（未入场前失效） | 2025-01-07T00:00:00+00:00 | 0.00 - 0.00 | 56.33 | Plan invalidated before entry: current price is below stop loss. |
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-05-11T16:00:00+00:00 | 23.58 - 24.13 | 77.80 | Backtest WATCHING plan expired before entry. |
| `AAVEUSDT` | EXPIRED（观察计划过期） | 2025-05-13T00:00:00+00:00 | 216.64 - 221.74 | 72.23 | Backtest WATCHING plan expired before entry. |
| `ARBUSDT` | INVALIDATED（未入场前失效） | 2025-05-14T04:00:00+00:00 | 0.43 - 0.45 | 79.05 | Plan invalidated before entry: current price is below stop loss. |
| `BTCUSDT` | EXPIRED（观察计划过期） | 2025-05-24T12:00:00+00:00 | 108,941.18 - 109,536.19 | 56.27 | Backtest WATCHING plan expired before entry. |
| `BTCUSDT` | INVALIDATED（未入场前失效） | 2025-05-27T16:00:00+00:00 | 109,347.06 - 109,999.08 | 64.37 | Plan invalidated before entry: current price is below stop loss. |
| `AVAXUSDT` | INVALIDATED（未入场前失效） | 2025-05-28T00:00:00+00:00 | 23.38 - 23.45 | 49.29 | Plan invalidated before entry: current price is below stop loss. |

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
| INFO | n/a | n/a | Additional issues omitted: 401. |

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
    "created_at_utc": "2026-06-09T04:41:43+00:00",
    "refresh_frequency": "daily",
    "max_symbols": 30,
    "master_count": 100,
    "source_limit": 100,
    "source_limit_applied": true,
    "universe_refresh_count": 152,
    "selected_count_min": 2,
    "selected_count_avg": 6.118421052631579,
    "selected_count_max": 18,
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
        "symbol": "ADAUSDT",
        "days_selected": 144
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
        "symbol": "ARBUSDT",
        "days_selected": 30
      },
      {
        "symbol": "BERAUSDT",
        "days_selected": 27
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
        "symbol": "ALGOUSDT",
        "days_selected": 14
      },
      {
        "symbol": "BIOUSDT",
        "days_selected": 12
      },
      {
        "symbol": "ACHUSDT",
        "days_selected": 10
      },
      {
        "symbol": "AUCTIONUSDT",
        "days_selected": 10
      },
      {
        "symbol": "1000SATSUSDT",
        "days_selected": 9
      },
      {
        "symbol": "BCHUSDT",
        "days_selected": 8
      },
      {
        "symbol": "COOKIEUSDT",
        "days_selected": 6
      },
      {
        "symbol": "BOMEUSDT",
        "days_selected": 5
      }
    ],
    "filter_counts": {
      "missing_1h": 2848,
      "insufficient_24h": 14,
      "reconstruct_error": 0,
      "low_quote_volume": 11408,
      "low_trades": 0,
      "stable_like": 0
    },
    "selection_by_day": [
      {
        "date_utc": "2025-01-01",
        "decision_time_utc": "2025-01-01T04:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "BONKUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 27,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 68,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-02",
        "decision_time_utc": "2025-01-02T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "ACTUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 27,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 68,
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
          "BNBUSDT",
          "AGLDUSDT"
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
        "date_utc": "2025-01-04",
        "decision_time_utc": "2025-01-04T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "BONKUSDT",
          "AGLDUSDT",
          "AVAXUSDT",
          "ALGOUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 64,
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
          "ADAUSDT",
          "BNBUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 67,
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
          "BNBUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 67,
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
          "ADAUSDT",
          "BIOUSDT",
          "ARBUSDT",
          "ACTUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 65,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-08",
        "decision_time_utc": "2025-01-08T00:00:00+00:00",
        "selected_symbols": [
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
          "ALGOUSDT"
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
        "date_utc": "2025-01-09",
        "decision_time_utc": "2025-01-09T00:00:00+00:00",
        "selected_symbols": [
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
          "BONKUSDT"
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
        "date_utc": "2025-01-10",
        "decision_time_utc": "2025-01-10T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ACTUSDT",
          "BIOUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "APTUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 26,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 66,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-11",
        "decision_time_utc": "2025-01-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "APTUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "BIOUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 3,
          "reconstruct_error": 0,
          "low_quote_volume": 65,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-12",
        "decision_time_utc": "2025-01-12T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "CGPTUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 73,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-13",
        "decision_time_utc": "2025-01-13T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 74,
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
          "AIXBTUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 66,
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
          "ADAUSDT",
          "BTCUSDT",
          "BIOUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 70,
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
          "BIOUSDT",
          "APTUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 12,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 65,
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
          "ADAUSDT",
          "AIXBTUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "CGPTUSDT",
          "ARBUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 67,
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
          "APTUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ALGOUSDT",
          "AIXBTUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 66,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-19",
        "decision_time_utc": "2025-01-19T00:00:00+00:00",
        "selected_symbols": [
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
          "APTUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 66,
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
          "BIOUSDT"
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
        "date_utc": "2025-01-21",
        "decision_time_utc": "2025-01-21T00:00:00+00:00",
        "selected_symbols": [
          "AAVEUSDT",
          "AIXBTUSDT",
          "ALGOUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "ACTUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "BONKUSDT",
          "APTUSDT",
          "1000SATSUSDT",
          "ARBUSDT",
          "BOMEUSDT",
          "BCHUSDT",
          "COWUSDT",
          "ARKMUSDT"
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
        "date_utc": "2025-01-22",
        "decision_time_utc": "2025-01-22T00:00:00+00:00",
        "selected_symbols": [
          "AAVEUSDT",
          "BONKUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "APTUSDT",
          "ADAUSDT",
          "AIXBTUSDT",
          "ALGOUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 23,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 66,
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
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT",
          "AAVEUSDT",
          "AVAXUSDT"
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
        "date_utc": "2025-01-24",
        "decision_time_utc": "2025-01-24T00:00:00+00:00",
        "selected_symbols": [
          "BIOUSDT",
          "BTCUSDT",
          "ARBUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ACTUSDT",
          "AIXBTUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BONKUSDT",
          "APTUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 66,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-25",
        "decision_time_utc": "2025-01-25T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "AIXBTUSDT",
          "BONKUSDT",
          "ANIMEUSDT"
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
        "date_utc": "2025-01-26",
        "decision_time_utc": "2025-01-26T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ANIMEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 73,
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
          "AIXBTUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 73,
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
        "date_utc": "2025-01-29",
        "decision_time_utc": "2025-01-29T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ACHUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 72,
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
          "BONKUSDT",
          "BTCUSDT",
          "AIXBTUSDT",
          "ADAUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "BNBUSDT"
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
        "date_utc": "2025-01-31",
        "decision_time_utc": "2025-01-31T00:00:00+00:00",
        "selected_symbols": [
          "ACHUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "AIXBTUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 72,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-01",
        "decision_time_utc": "2025-02-01T00:00:00+00:00",
        "selected_symbols": [
          "AAVEUSDT",
          "BTCUSDT",
          "ACHUSDT",
          "ARBUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "APTUSDT"
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
          "AAVEUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 69,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-03",
        "decision_time_utc": "2025-02-03T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "BONKUSDT",
          "AIXBTUSDT",
          "ALGOUSDT",
          "ARPAUSDT",
          "ACHUSDT"
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
          "ACHUSDT",
          "BOMEUSDT",
          "ARUSDT",
          "ARKMUSDT",
          "ADAUSDT"
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
        "date_utc": "2025-02-06",
        "decision_time_utc": "2025-02-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "ACTUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "APTUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 22,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 71,
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
          "AVAXUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 21,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 72,
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
          "APTUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 21,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 72,
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
          "BTCUSDT",
          "BERAUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 21,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 74,
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
          "ADAUSDT",
          "BERAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 74,
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
          "AVAXUSDT",
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
        "date_utc": "2025-02-12",
        "decision_time_utc": "2025-02-12T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "BERAUSDT",
          "CAKEUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "1000CHEEMSUSDT",
          "AIXBTUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
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
        "date_utc": "2025-02-13",
        "decision_time_utc": "2025-02-13T00:00:00+00:00",
        "selected_symbols": [
          "CAKEUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "BERAUSDT",
          "AIXBTUSDT"
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
        "date_utc": "2025-02-14",
        "decision_time_utc": "2025-02-14T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "CAKEUSDT",
          "APTUSDT"
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
        "date_utc": "2025-02-15",
        "decision_time_utc": "2025-02-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "CAKEUSDT",
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
          "BNBUSDT",
          "BTCUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 77,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-18",
        "decision_time_utc": "2025-02-18T00:00:00+00:00",
        "selected_symbols": [
          "BERAUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "CAKEUSDT",
          "ARKUSDT"
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
        "date_utc": "2025-02-19",
        "decision_time_utc": "2025-02-19T00:00:00+00:00",
        "selected_symbols": [
          "ACHUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "CAKEUSDT",
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
        "date_utc": "2025-02-20",
        "decision_time_utc": "2025-02-20T00:00:00+00:00",
        "selected_symbols": [
          "APTUSDT",
          "CAKEUSDT",
          "BERAUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT"
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
        "date_utc": "2025-02-21",
        "decision_time_utc": "2025-02-21T00:00:00+00:00",
        "selected_symbols": [
          "BERAUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "CAKEUSDT",
          "APTUSDT"
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
        "date_utc": "2025-02-22",
        "decision_time_utc": "2025-02-22T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AIXBTUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BERAUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "CAKEUSDT",
          "AAVEUSDT",
          "ARKMUSDT"
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
        "date_utc": "2025-02-23",
        "decision_time_utc": "2025-02-23T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "BNBUSDT",
          "CAKEUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BERAUSDT"
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
        "date_utc": "2025-02-24",
        "decision_time_utc": "2025-02-24T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 77,
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
          "AAVEUSDT"
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
        "date_utc": "2025-02-26",
        "decision_time_utc": "2025-02-26T00:00:00+00:00",
        "selected_symbols": [
          "ACTUSDT",
          "COWUSDT",
          "BTCUSDT",
          "APTUSDT",
          "BNBUSDT",
          "ARBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BERAUSDT"
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
        "date_utc": "2025-02-27",
        "decision_time_utc": "2025-02-27T00:00:00+00:00",
        "selected_symbols": [
          "BERAUSDT",
          "ACTUSDT",
          "APTUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
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
        "date_utc": "2025-02-28",
        "decision_time_utc": "2025-02-28T00:00:00+00:00",
        "selected_symbols": [
          "BERAUSDT",
          "BTCUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "BNBUSDT",
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
        "date_utc": "2025-03-01",
        "decision_time_utc": "2025-03-01T00:00:00+00:00",
        "selected_symbols": [
          "CKBUSDT",
          "ACTUSDT",
          "BERAUSDT",
          "APTUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
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
        "date_utc": "2025-03-02",
        "decision_time_utc": "2025-03-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 77,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-03",
        "decision_time_utc": "2025-03-03T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "ALGOUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BTCUSDT",
          "APTUSDT",
          "BNBUSDT",
          "BERAUSDT",
          "ACTUSDT"
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
        "date_utc": "2025-03-05",
        "decision_time_utc": "2025-03-05T00:00:00+00:00",
        "selected_symbols": [
          "AAVEUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "BERAUSDT",
          "ARBUSDT"
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
        "date_utc": "2025-03-08",
        "decision_time_utc": "2025-03-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "BCHUSDT"
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
        "date_utc": "2025-03-09",
        "decision_time_utc": "2025-03-09T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 77,
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
          "AVAXUSDT"
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
        "date_utc": "2025-03-11",
        "decision_time_utc": "2025-03-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "AVAXUSDT"
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
        "date_utc": "2025-03-12",
        "decision_time_utc": "2025-03-12T00:00:00+00:00",
        "selected_symbols": [
          "AUCTIONUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "AAVEUSDT",
          "ARKMUSDT"
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
        "date_utc": "2025-03-13",
        "decision_time_utc": "2025-03-13T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
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
        "date_utc": "2025-03-14",
        "decision_time_utc": "2025-03-14T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
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
        "date_utc": "2025-03-15",
        "decision_time_utc": "2025-03-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 20,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 77,
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
        "date_utc": "2025-03-17",
        "decision_time_utc": "2025-03-17T00:00:00+00:00",
        "selected_symbols": [
          "AUCTIONUSDT",
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
        "date_utc": "2025-03-18",
        "decision_time_utc": "2025-03-18T00:00:00+00:00",
        "selected_symbols": [
          "CAKEUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "AUCTIONUSDT"
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
        "date_utc": "2025-03-19",
        "decision_time_utc": "2025-03-19T00:00:00+00:00",
        "selected_symbols": [
          "AUCTIONUSDT",
          "CAKEUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "API3USDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 19,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 74,
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
          "AUCTIONUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "CAKEUSDT",
          "BMTUSDT"
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
        "date_utc": "2025-03-21",
        "decision_time_utc": "2025-03-21T00:00:00+00:00",
        "selected_symbols": [
          "AUCTIONUSDT",
          "BNBUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "CAKEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 19,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 76,
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
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 19,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 76,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-23",
        "decision_time_utc": "2025-03-23T00:00:00+00:00",
        "selected_symbols": [
          "API3USDT",
          "BTCUSDT",
          "CAKEUSDT",
          "BNBUSDT",
          "ACXUSDT",
          "AUCTIONUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 19,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 75,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-24",
        "decision_time_utc": "2025-03-24T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AUCTIONUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 19,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 77,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-25",
        "decision_time_utc": "2025-03-25T00:00:00+00:00",
        "selected_symbols": [
          "BERAUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "AUCTIONUSDT",
          "BNBUSDT",
          "CAKEUSDT"
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
        "date_utc": "2025-03-26",
        "decision_time_utc": "2025-03-26T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "1000SATSUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 19,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 76,
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
          "CAKEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 19,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 76,
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
          "1000SATSUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 2,
          "reconstruct_error": 0,
          "low_quote_volume": 75,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-29",
        "decision_time_utc": "2025-03-29T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BERAUSDT"
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
        "date_utc": "2025-03-30",
        "decision_time_utc": "2025-03-30T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BERAUSDT"
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
        "date_utc": "2025-03-31",
        "decision_time_utc": "2025-03-31T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
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
          "ADAUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-02",
        "decision_time_utc": "2025-04-02T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "COMPUSDT",
          "ACTUSDT"
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
        "date_utc": "2025-04-03",
        "decision_time_utc": "2025-04-03T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ACTUSDT"
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
        "date_utc": "2025-04-04",
        "decision_time_utc": "2025-04-04T00:00:00+00:00",
        "selected_symbols": [
          "ACTUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
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
        "date_utc": "2025-04-05",
        "decision_time_utc": "2025-04-05T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-06",
        "decision_time_utc": "2025-04-06T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 17,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
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
        "date_utc": "2025-04-08",
        "decision_time_utc": "2025-04-08T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "BNBUSDT",
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
        "date_utc": "2025-04-09",
        "decision_time_utc": "2025-04-09T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
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
        "date_utc": "2025-04-10",
        "decision_time_utc": "2025-04-10T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "BNBUSDT",
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
        "date_utc": "2025-04-11",
        "decision_time_utc": "2025-04-11T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 16,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 80,
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
          "AVAXUSDT",
          "ADAUSDT",
          "BNBUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-13",
        "decision_time_utc": "2025-04-13T00:00:00+00:00",
        "selected_symbols": [
          "BABYUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "BNBUSDT"
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
        "date_utc": "2025-04-14",
        "decision_time_utc": "2025-04-14T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BABYUSDT",
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
        "date_utc": "2025-04-15",
        "decision_time_utc": "2025-04-15T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AVAXUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BABYUSDT",
          "ACTUSDT"
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
        "date_utc": "2025-04-16",
        "decision_time_utc": "2025-04-16T00:00:00+00:00",
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
        "date_utc": "2025-04-17",
        "decision_time_utc": "2025-04-17T00:00:00+00:00",
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
        "date_utc": "2025-04-18",
        "decision_time_utc": "2025-04-18T00:00:00+00:00",
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
        "date_utc": "2025-04-19",
        "decision_time_utc": "2025-04-19T00:00:00+00:00",
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
        "date_utc": "2025-04-22",
        "decision_time_utc": "2025-04-22T00:00:00+00:00",
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
        "date_utc": "2025-04-23",
        "decision_time_utc": "2025-04-23T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BNBUSDT"
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
        "date_utc": "2025-04-24",
        "decision_time_utc": "2025-04-24T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "ACTUSDT"
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
        "date_utc": "2025-04-25",
        "decision_time_utc": "2025-04-25T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "BTCUSDT",
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
        "date_utc": "2025-04-26",
        "decision_time_utc": "2025-04-26T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "BTCUSDT",
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
        "date_utc": "2025-04-27",
        "decision_time_utc": "2025-04-27T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "BONKUSDT",
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
        "date_utc": "2025-04-28",
        "decision_time_utc": "2025-04-28T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BONKUSDT",
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
        "date_utc": "2025-04-29",
        "decision_time_utc": "2025-04-29T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT",
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
        "date_utc": "2025-04-30",
        "decision_time_utc": "2025-04-30T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT"
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
        "date_utc": "2025-05-01",
        "decision_time_utc": "2025-05-01T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "BONKUSDT"
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
        "date_utc": "2025-05-02",
        "decision_time_utc": "2025-05-02T00:00:00+00:00",
        "selected_symbols": [
          "AIXBTUSDT",
          "BTCUSDT",
          "ADAUSDT",
          "BNBUSDT"
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
        "date_utc": "2025-05-03",
        "decision_time_utc": "2025-05-03T00:00:00+00:00",
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
        "date_utc": "2025-05-06",
        "decision_time_utc": "2025-05-06T00:00:00+00:00",
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
        "date_utc": "2025-05-07",
        "decision_time_utc": "2025-05-07T00:00:00+00:00",
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
        "date_utc": "2025-05-08",
        "decision_time_utc": "2025-05-08T00:00:00+00:00",
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
        "date_utc": "2025-05-09",
        "decision_time_utc": "2025-05-09T00:00:00+00:00",
        "selected_symbols": [
          "AAVEUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "BCHUSDT",
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
        "date_utc": "2025-05-10",
        "decision_time_utc": "2025-05-10T00:00:00+00:00",
        "selected_symbols": [
          "BONKUSDT",
          "BERAUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "BTCUSDT",
          "AAVEUSDT",
          "ADAUSDT"
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
        "date_utc": "2025-05-11",
        "decision_time_utc": "2025-05-11T00:00:00+00:00",
        "selected_symbols": [
          "ARBUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "ADAUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "1000CATUSDT",
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
        "date_utc": "2025-05-12",
        "decision_time_utc": "2025-05-12T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "ARBUSDT",
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
        "date_utc": "2025-05-13",
        "decision_time_utc": "2025-05-13T00:00:00+00:00",
        "selected_symbols": [
          "ACTUSDT",
          "BOMEUSDT",
          "BTCUSDT",
          "BONKUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ARBUSDT",
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
        "date_utc": "2025-05-14",
        "decision_time_utc": "2025-05-14T00:00:00+00:00",
        "selected_symbols": [
          "BOMEUSDT",
          "ARBUSDT",
          "BTCUSDT",
          "AVAXUSDT",
          "BONKUSDT",
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
        "date_utc": "2025-05-15",
        "decision_time_utc": "2025-05-15T00:00:00+00:00",
        "selected_symbols": [
          "1000SATSUSDT",
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
        "date_utc": "2025-05-16",
        "decision_time_utc": "2025-05-16T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "1000SATSUSDT"
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
        "date_utc": "2025-05-17",
        "decision_time_utc": "2025-05-17T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT"
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
        "date_utc": "2025-05-18",
        "decision_time_utc": "2025-05-18T00:00:00+00:00",
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
        "date_utc": "2025-05-19",
        "decision_time_utc": "2025-05-19T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "BNBUSDT"
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
        "date_utc": "2025-05-20",
        "decision_time_utc": "2025-05-20T00:00:00+00:00",
        "selected_symbols": [
          "AAVEUSDT",
          "BTCUSDT",
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
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
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
          "BTCUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "BNBUSDT",
          "CETUSUSDT"
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
        "date_utc": "2025-05-24",
        "decision_time_utc": "2025-05-24T00:00:00+00:00",
        "selected_symbols": [
          "COOKIEUSDT",
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BONKUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 79,
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
          "ADAUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 82,
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
          "BNBUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 82,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-05-27",
        "decision_time_utc": "2025-05-27T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "COOKIEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 81,
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
          "BTCUSDT",
          "BNBUSDT",
          "AVAXUSDT",
          "ADAUSDT"
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
        "date_utc": "2025-05-29",
        "decision_time_utc": "2025-05-29T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 83,
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
        "date_utc": "2025-05-31",
        "decision_time_utc": "2025-05-31T00:00:00+00:00",
        "selected_symbols": [
          "BTCUSDT",
          "BNBUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ARBUSDT"
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
        "date_utc": "2025-06-01",
        "decision_time_utc": "2025-06-01T00:00:00+00:00",
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
