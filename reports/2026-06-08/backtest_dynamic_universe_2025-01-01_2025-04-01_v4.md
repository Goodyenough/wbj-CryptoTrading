---
created: 2026-06-08 23:24:00 CST
tags:
  - crypto
  - trading-system
  - backtest
backtest_run_id: 0e45b2c869c6
report_version: v4
sample_sufficient: false
universe_mode: true
universe_type: dynamic
---

# 回测报告 2025-01-01 至 2025-04-01 v4

- 回测 ID：`0e45b2c869c6`
- 交易对：`1000CATUSDT`, `1000CHEEMSUSDT`, `1000SATSUSDT`, `1MBABYDOGEUSDT`, `AAVEUSDT`, `ACEUSDT`, `ACHUSDT`, `ACTUSDT`, `ACXUSDT`, `ADAUSDT`, `AGLDUSDT`, `AIUSDT`, `AIXBTUSDT`, `ALGOUSDT`, `AMPUSDT`, `ANIMEUSDT`, `ANKRUSDT`, `APEUSDT`, `API3USDT`, `APTUSDT`, `ARBUSDT`, `ARKMUSDT`, `ARKUSDT`, `ARPAUSDT`, `ATOMUSDT`, `AUCTIONUSDT`, `AUDIOUSDT`, `AVAXUSDT`, `BANANAUSDT`
- UTC 区间：2025-01-01T00:00:00+00:00 -> 2025-04-01T00:00:00+00:00
- 初始权益：10,000.00 USDT
- 最终权益：9,486.54 USDT
- 净收益：-5.13%
- 代码 commit：`47eb40372651e9f7763faf9cf147d0ab45352d11`
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
- Master symbols / Master 币种数：60
- Source limit / 调试截断：60
- Source limit applied / 是否截断：true
- Refresh frequency / 刷新频率：daily
- Universe refreshes / Universe 刷新次数：91
- Selected symbols per refresh / 每次入选数量：min=1, avg=6.31, max=10
- Top selected symbols / 最常入选：`ADAUSDT`(90), `AVAXUSDT`(85), `AAVEUSDT`(70), `APTUSDT`(63), `ARBUSDT`(46), `ACTUSDT`(42), `AIXBTUSDT`(40), `ALGOUSDT`(29), `1000SATSUSDT`(18), `AUCTIONUSDT`(18)
- Filter counts / 过滤统计：
```json
{
  "missing_1h": 1251,
  "insufficient_24h": 4,
  "reconstruct_error": 0,
  "low_quote_volume": 3610,
  "low_trades": 0,
  "stable_like": 0
}
```
> Warning / 警告：dynamic universe 的 symbol master 来自当前 Binance exchangeInfo；历史上曾交易但今天已退市的币不会进入 master list，因此仍有退市幸存者偏差。
> Runtime / 耗时提示：第一次完整运行需要缓存大量 1h/4h/1d K 线，可能很慢；缓存命中后后续回测会明显加快。

## 核心指标

| Metric（指标） | Value（数值） |
|---|---:|
| Trades（计划总数） | 7 |
| Closed trades（已结束交易） | 5 |
| Open trades（仍开放持仓） | 0 |
| Win rate（胜率） | 0.00% |
| Profit factor（盈利因子） | 0.00 |
| Avg R（平均R倍数） | -1.02 |
| Net return（净收益率） | -5.13% |
| Max drawdown（最大回撤） | 577.78 / 5.74% |
| Intrabar max drawdown（K线内最大回撤） | 540.62 / 5.39% |
| TP1 touched rate（第一止盈触达率） | 0.00% |
| TP2 close rate（第二止盈平仓率） | 0.00% |
| Stop rate（止损率） | 100.00% |
| Fee drag（手续费拖累） | 6.65 USDT |
| Tail max single loss（最大单笔亏损） | -103.88 USDT |
| CAGR（年化复合收益率） | -19.25% |
| Sharpe（夏普比率） | -3.34 |
| Sortino（索提诺比率） | -0.76 |
| Exposure（持仓暴露时间） | 5.00% |
| Turnover（换手率） | 0.51 |
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
| BTC buy-hold（买入并持有BTC） | -12.12% |
| ETH buy-hold（买入并持有ETH） | -45.74% |
| Cash（现金不交易） | 0.00% |
| Equal-weight symbols（等权持有本次币种） | -47.02% |

## 已结束交易

| Symbol（交易对） | Status（状态） | Created（创建时间） | Entry（入场价） | Exit（出场价） | Qty（数量） | Gross PnL（毛盈亏） | Net PnL（净盈亏） | Net R（净R倍数） | Fees（手续费） | Notes（备注） |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| `AAVEUSDT` | STOPPED（已止损） | 2025-01-04T04:00:00+00:00 | 340.44 | 301.35 | 2.59 | -101.22 | -102.35 | -1.02 | 1.13 | Stop loss hit. |
| `APTUSDT` | STOPPED（已止损） | 2025-01-05T04:00:00+00:00 | 9.75 | 8.97 | 131.94 | -101.94 | -103.64 | -1.03 | 1.70 | Stop loss hit. |
| `ADAUSDT` | STOPPED（已止损） | 2025-01-05T12:00:00+00:00 | 1.06 | 0.93 | 777.19 | -101.51 | -102.56 | -1.02 | 1.05 | Stop loss hit. |
| `AGLDUSDT` | STOPPED（已止损） | 2025-01-06T00:00:00+00:00 | 2.77 | 2.53 | 430.37 | -102.31 | -103.88 | -1.03 | 1.56 | Stop loss hit. |
| `ARBUSDT` | STOPPED（已止损） | 2025-01-07T00:00:00+00:00 | 0.91 | 0.81 | 1,026.60 | -99.82 | -101.02 | -1.02 | 1.21 | Stop loss hit. |

## 回测结束仍开放

| Symbol（交易对） | Status（状态） | Entry（入场价） | Qty（数量） | Unrealized Handling（未实现盈亏处理） | Notes（备注） |
|---|---|---:|---:|---|---|

## 未入场/过期计划

| Symbol（交易对） | Status（状态） | Created（创建时间） | Entry Zone（入场区间） | Score（评分） | Notes（备注） |
|---|---|---|---:|---:|---|
| `AVAXUSDT` | EXPIRED（观察计划过期） | 2025-01-04T12:00:00+00:00 | 40.15 - 40.76 | 72.48 | Backtest WATCHING plan expired before entry. |
| `ALGOUSDT` | INVALIDATED（未入场前失效） | 2025-01-07T00:00:00+00:00 | 0.41 - 0.42 | 72.57 | Plan invalidated before entry: current price is below stop loss. |

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
| WARNING | `ACHUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACHUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACHUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACHUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACHUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACHUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACMUSDT` | 1h | Large wick/range candle. |
| WARNING | `ACMUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACMUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACTUSDT` | 1h | Large wick/range candle. |
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
| WARNING | `ACXUSDT` | 1h | Large wick/range candle. |
| WARNING | `ACXUSDT` | 1h | Large wick/range candle. |
| WARNING | `ACXUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACXUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACXUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACXUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACXUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACXUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACXUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACXUSDT` | 1d | Large wick/range candle. |
| WARNING | `ADAUSDT` | 4h | Large wick/range candle. |
| WARNING | `ADAUSDT` | 1d | Large wick/range candle. |
| WARNING | `ADAUSDT` | 1d | Large wick/range candle. |
| WARNING | `ADAUSDT` | 1d | Large wick/range candle. |
| WARNING | `ADXUSDT` | 1h | Large wick/range candle. |
| WARNING | `ADXUSDT` | 4h | Large wick/range candle. |
| WARNING | `ADXUSDT` | 1d | Large wick/range candle. |
| WARNING | `ADXUSDT` | 1d | Large wick/range candle. |
| WARNING | `AEVOUSDT` | 4h | Large wick/range candle. |
| WARNING | `AEVOUSDT` | 1d | Large wick/range candle. |
| WARNING | `AEVOUSDT` | 1d | Large wick/range candle. |
| WARNING | `AEVOUSDT` | 1d | Large wick/range candle. |
| WARNING | `AGLDUSDT` | 1h | Large wick/range candle. |
| INFO | n/a | n/a | Additional issues omitted: 193. |

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
    "created_at_utc": "2026-06-08T15:24:00+00:00",
    "refresh_frequency": "daily",
    "max_symbols": 10,
    "master_count": 60,
    "source_limit": 60,
    "source_limit_applied": true,
    "universe_refresh_count": 91,
    "selected_count_min": 1,
    "selected_count_avg": 6.3076923076923075,
    "selected_count_max": 10,
    "top_selected_symbols": [
      {
        "symbol": "ADAUSDT",
        "days_selected": 90
      },
      {
        "symbol": "AVAXUSDT",
        "days_selected": 85
      },
      {
        "symbol": "AAVEUSDT",
        "days_selected": 70
      },
      {
        "symbol": "APTUSDT",
        "days_selected": 63
      },
      {
        "symbol": "ARBUSDT",
        "days_selected": 46
      },
      {
        "symbol": "ACTUSDT",
        "days_selected": 42
      },
      {
        "symbol": "AIXBTUSDT",
        "days_selected": 40
      },
      {
        "symbol": "ALGOUSDT",
        "days_selected": 29
      },
      {
        "symbol": "1000SATSUSDT",
        "days_selected": 18
      },
      {
        "symbol": "AUCTIONUSDT",
        "days_selected": 18
      },
      {
        "symbol": "ACHUSDT",
        "days_selected": 14
      },
      {
        "symbol": "ARKMUSDT",
        "days_selected": 12
      },
      {
        "symbol": "AGLDUSDT",
        "days_selected": 6
      },
      {
        "symbol": "ANIMEUSDT",
        "days_selected": 5
      },
      {
        "symbol": "API3USDT",
        "days_selected": 5
      },
      {
        "symbol": "1000CHEEMSUSDT",
        "days_selected": 4
      },
      {
        "symbol": "AIUSDT",
        "days_selected": 4
      },
      {
        "symbol": "ATOMUSDT",
        "days_selected": 4
      },
      {
        "symbol": "BANANAUSDT",
        "days_selected": 4
      },
      {
        "symbol": "ARKUSDT",
        "days_selected": 3
      }
    ],
    "filter_counts": {
      "missing_1h": 1251,
      "insufficient_24h": 4,
      "reconstruct_error": 0,
      "low_quote_volume": 3610,
      "low_trades": 0,
      "stable_like": 0
    },
    "selection_by_day": [
      {
        "date_utc": "2025-01-01",
        "decision_time_utc": "2025-01-01T04:00:00+00:00",
        "selected_symbols": [
          "ACTUSDT",
          "ALGOUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AGLDUSDT",
          "APTUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 16,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 37,
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
          "AAVEUSDT",
          "APTUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 16,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 37,
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
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ALGOUSDT",
          "ARBUSDT",
          "APTUSDT",
          "AGLDUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 16,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 35,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-04",
        "decision_time_utc": "2025-01-04T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "AGLDUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "ALGOUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 16,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 36,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-05",
        "decision_time_utc": "2025-01-05T00:00:00+00:00",
        "selected_symbols": [
          "ARBUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "ACTUSDT",
          "ALGOUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 16,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 37,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-06",
        "decision_time_utc": "2025-01-06T00:00:00+00:00",
        "selected_symbols": [
          "ACTUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "AGLDUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 16,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 37,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-07",
        "decision_time_utc": "2025-01-07T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "ALGOUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "APTUSDT",
          "ACTUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 16,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 37,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-08",
        "decision_time_utc": "2025-01-08T00:00:00+00:00",
        "selected_symbols": [
          "AIUSDT",
          "ADAUSDT",
          "ACTUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "ALGOUSDT",
          "ATOMUSDT",
          "1000SATSUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 16,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 33,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-09",
        "decision_time_utc": "2025-01-09T00:00:00+00:00",
        "selected_symbols": [
          "ARKUSDT",
          "ADAUSDT",
          "ACTUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "1000SATSUSDT",
          "AIUSDT",
          "ALGOUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 16,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 33,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-10",
        "decision_time_utc": "2025-01-10T00:00:00+00:00",
        "selected_symbols": [
          "1000SATSUSDT",
          "ADAUSDT",
          "ACTUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "ARBUSDT",
          "ALGOUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 16,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 36,
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
          "1000SATSUSDT",
          "APTUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 35,
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
          "AVAXUSDT",
          "AIXBTUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 41,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-13",
        "decision_time_utc": "2025-01-13T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT"
        ],
        "candidate_count": 1,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 44,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-14",
        "decision_time_utc": "2025-01-14T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "ACTUSDT",
          "ARBUSDT",
          "AIXBTUSDT",
          "ALGOUSDT",
          "1000SATSUSDT",
          "ATOMUSDT"
        ],
        "candidate_count": 10,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 35,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-15",
        "decision_time_utc": "2025-01-15T00:00:00+00:00",
        "selected_symbols": [
          "AIXBTUSDT",
          "ADAUSDT",
          "APTUSDT",
          "ARBUSDT",
          "ACTUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 38,
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
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "ACTUSDT",
          "APTUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 37,
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
          "ADAUSDT",
          "AIXBTUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 36,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-18",
        "decision_time_utc": "2025-01-18T00:00:00+00:00",
        "selected_symbols": [
          "AMPUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "ADAUSDT",
          "APTUSDT",
          "ACTUSDT",
          "AVAXUSDT",
          "ALGOUSDT",
          "AIXBTUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 36,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-19",
        "decision_time_utc": "2025-01-19T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "AIXBTUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "ACTUSDT",
          "ALGOUSDT",
          "APTUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 37,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-20",
        "decision_time_utc": "2025-01-20T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "AIXBTUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "ACTUSDT",
          "ALGOUSDT",
          "1000SATSUSDT",
          "APEUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 32,
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
          "ADAUSDT",
          "ACTUSDT",
          "ATOMUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "1000SATSUSDT",
          "APEUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 32,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-22",
        "decision_time_utc": "2025-01-22T00:00:00+00:00",
        "selected_symbols": [
          "AAVEUSDT",
          "1000SATSUSDT",
          "ARBUSDT",
          "AVAXUSDT",
          "1MBABYDOGEUSDT",
          "ARKMUSDT",
          "APTUSDT",
          "ADAUSDT",
          "AIXBTUSDT",
          "ALGOUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 34,
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
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "ARBUSDT",
          "ALGOUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 15,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 37,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-24",
        "decision_time_utc": "2025-01-24T00:00:00+00:00",
        "selected_symbols": [
          "ARBUSDT",
          "1000SATSUSDT",
          "ADAUSDT",
          "ACTUSDT",
          "AIXBTUSDT",
          "ALGOUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "APTUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 36,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-25",
        "decision_time_utc": "2025-01-25T00:00:00+00:00",
        "selected_symbols": [
          "ACTUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "AIXBTUSDT",
          "APTUSDT",
          "ARBUSDT",
          "ALGOUSDT",
          "ANIMEUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 37,
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
          "ADAUSDT",
          "ANIMEUSDT",
          "AIXBTUSDT",
          "AAVEUSDT",
          "APTUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 38,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-27",
        "decision_time_utc": "2025-01-27T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "AVAXUSDT",
          "AIXBTUSDT",
          "AAVEUSDT",
          "ANIMEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 41,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-28",
        "decision_time_utc": "2025-01-28T00:00:00+00:00",
        "selected_symbols": [
          "ACHUSDT",
          "ACTUSDT",
          "ADAUSDT",
          "ALGOUSDT",
          "AVAXUSDT",
          "AIXBTUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "ARBUSDT",
          "ARKMUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 35,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-29",
        "decision_time_utc": "2025-01-29T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "ACHUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "AIXBTUSDT",
          "ARBUSDT",
          "APTUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 39,
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
          "AIXBTUSDT",
          "ADAUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 37,
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
          "AVAXUSDT",
          "ARBUSDT",
          "AIXBTUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 39,
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
          "ACHUSDT",
          "ARBUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "AIXBTUSDT",
          "ANIMEUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 37,
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
          "ADAUSDT",
          "ARBUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "AIXBTUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 38,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-03",
        "decision_time_utc": "2025-02-03T00:00:00+00:00",
        "selected_symbols": [
          "1000SATSUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ACTUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "AIXBTUSDT",
          "ALGOUSDT",
          "ARKMUSDT"
        ],
        "candidate_count": 13,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 33,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-04",
        "decision_time_utc": "2025-02-04T00:00:00+00:00",
        "selected_symbols": [
          "ACTUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ALGOUSDT",
          "1000SATSUSDT",
          "AIXBTUSDT",
          "ATOMUSDT",
          "ARBUSDT",
          "ACEUSDT"
        ],
        "candidate_count": 17,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 29,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-05",
        "decision_time_utc": "2025-02-05T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "ARBUSDT",
          "ACTUSDT",
          "ACHUSDT",
          "AIXBTUSDT",
          "ALGOUSDT",
          "ARKMUSDT"
        ],
        "candidate_count": 11,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 35,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-06",
        "decision_time_utc": "2025-02-06T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "ACTUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "ARBUSDT",
          "ACHUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 39,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-07",
        "decision_time_utc": "2025-02-07T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ACTUSDT",
          "AIXBTUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 39,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-08",
        "decision_time_utc": "2025-02-08T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "ACTUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "AIXBTUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 39,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-09",
        "decision_time_utc": "2025-02-09T00:00:00+00:00",
        "selected_symbols": [
          "1000CATUSDT",
          "APTUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "ARKMUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 14,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 41,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-10",
        "decision_time_utc": "2025-02-10T00:00:00+00:00",
        "selected_symbols": [
          "APTUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 42,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-11",
        "decision_time_utc": "2025-02-11T00:00:00+00:00",
        "selected_symbols": [
          "1000CHEEMSUSDT",
          "AIXBTUSDT",
          "APTUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ARKMUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 40,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-12",
        "decision_time_utc": "2025-02-12T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "ARKMUSDT",
          "1000CHEEMSUSDT",
          "AIXBTUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 40,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-13",
        "decision_time_utc": "2025-02-13T00:00:00+00:00",
        "selected_symbols": [
          "1000CHEEMSUSDT",
          "ARBUSDT",
          "ALGOUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "ARKMUSDT",
          "AIXBTUSDT"
        ],
        "candidate_count": 9,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 38,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-14",
        "decision_time_utc": "2025-02-14T00:00:00+00:00",
        "selected_symbols": [
          "AUCTIONUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "AIXBTUSDT",
          "1000CATUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 40,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-15",
        "decision_time_utc": "2025-02-15T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "AIXBTUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "APTUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 42,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-16",
        "decision_time_utc": "2025-02-16T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT"
        ],
        "candidate_count": 1,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 46,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-17",
        "decision_time_utc": "2025-02-17T00:00:00+00:00",
        "selected_symbols": [
          "ACHUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 45,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-18",
        "decision_time_utc": "2025-02-18T00:00:00+00:00",
        "selected_symbols": [
          "ACHUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "ARKUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 41,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-19",
        "decision_time_utc": "2025-02-19T00:00:00+00:00",
        "selected_symbols": [
          "ACHUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 41,
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
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "ACHUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 41,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-21",
        "decision_time_utc": "2025-02-21T00:00:00+00:00",
        "selected_symbols": [
          "ACHUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "APTUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 41,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-22",
        "decision_time_utc": "2025-02-22T00:00:00+00:00",
        "selected_symbols": [
          "ACTUSDT",
          "AIXBTUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "ARKMUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 39,
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
          "ADAUSDT",
          "AAVEUSDT",
          "APTUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 41,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-24",
        "decision_time_utc": "2025-02-24T00:00:00+00:00",
        "selected_symbols": [
          "ANIMEUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 44,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-25",
        "decision_time_utc": "2025-02-25T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "AIXBTUSDT",
          "ARKMUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 40,
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
          "APTUSDT",
          "ARBUSDT",
          "ARKMUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 39,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-27",
        "decision_time_utc": "2025-02-27T00:00:00+00:00",
        "selected_symbols": [
          "ACTUSDT",
          "1000SATSUSDT",
          "AIXBTUSDT",
          "APTUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 40,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-02-28",
        "decision_time_utc": "2025-02-28T00:00:00+00:00",
        "selected_symbols": [
          "APTUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 43,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-01",
        "decision_time_utc": "2025-03-01T00:00:00+00:00",
        "selected_symbols": [
          "ACTUSDT",
          "APTUSDT",
          "AIXBTUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "1000SATSUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 39,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-02",
        "decision_time_utc": "2025-03-02T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 43,
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
          "ARBUSDT",
          "APTUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 39,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-04",
        "decision_time_utc": "2025-03-04T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "ARBUSDT",
          "ALGOUSDT",
          "AIXBTUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 39,
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
          "AVAXUSDT",
          "ACTUSDT",
          "APTUSDT",
          "ARBUSDT",
          "ALGOUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 40,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-06",
        "decision_time_utc": "2025-03-06T00:00:00+00:00",
        "selected_symbols": [
          "APTUSDT",
          "AVAXUSDT",
          "ARBUSDT",
          "AAVEUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 42,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-07",
        "decision_time_utc": "2025-03-07T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 44,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-08",
        "decision_time_utc": "2025-03-08T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "APTUSDT",
          "AVAXUSDT",
          "AAVEUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 42,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-09",
        "decision_time_utc": "2025-03-09T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "ADAUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 44,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-10",
        "decision_time_utc": "2025-03-10T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 44,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-11",
        "decision_time_utc": "2025-03-11T00:00:00+00:00",
        "selected_symbols": [
          "AUCTIONUSDT",
          "AUDIOUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AVAXUSDT",
          "APTUSDT",
          "ARBUSDT"
        ],
        "candidate_count": 7,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 40,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-12",
        "decision_time_utc": "2025-03-12T00:00:00+00:00",
        "selected_symbols": [
          "AUCTIONUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "BANANAUSDT",
          "ARBUSDT",
          "APTUSDT",
          "AAVEUSDT",
          "ARKMUSDT"
        ],
        "candidate_count": 8,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 39,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-13",
        "decision_time_utc": "2025-03-13T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AUCTIONUSDT",
          "BANANAUSDT",
          "APTUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 41,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-14",
        "decision_time_utc": "2025-03-14T00:00:00+00:00",
        "selected_symbols": [
          "AUCTIONUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 43,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-15",
        "decision_time_utc": "2025-03-15T00:00:00+00:00",
        "selected_symbols": [
          "AUCTIONUSDT",
          "AAVEUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 43,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-16",
        "decision_time_utc": "2025-03-16T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 45,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-17",
        "decision_time_utc": "2025-03-17T00:00:00+00:00",
        "selected_symbols": [
          "AUCTIONUSDT",
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 44,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-18",
        "decision_time_utc": "2025-03-18T00:00:00+00:00",
        "selected_symbols": [
          "API3USDT",
          "1000CHEEMSUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "AUCTIONUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 42,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-19",
        "decision_time_utc": "2025-03-19T00:00:00+00:00",
        "selected_symbols": [
          "AUCTIONUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "API3USDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 43,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-20",
        "decision_time_utc": "2025-03-20T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "AAVEUSDT",
          "AUCTIONUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 43,
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
          "ADAUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 42,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-22",
        "decision_time_utc": "2025-03-22T00:00:00+00:00",
        "selected_symbols": [
          "ACHUSDT",
          "AUCTIONUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 44,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-23",
        "decision_time_utc": "2025-03-23T00:00:00+00:00",
        "selected_symbols": [
          "API3USDT",
          "BANANAUSDT",
          "ADAUSDT",
          "ACXUSDT",
          "AUCTIONUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 42,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-24",
        "decision_time_utc": "2025-03-24T00:00:00+00:00",
        "selected_symbols": [
          "API3USDT",
          "ADAUSDT",
          "AUCTIONUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 44,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-25",
        "decision_time_utc": "2025-03-25T00:00:00+00:00",
        "selected_symbols": [
          "ANKRUSDT",
          "AIXBTUSDT",
          "AVAXUSDT",
          "ADAUSDT",
          "AUCTIONUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 42,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-26",
        "decision_time_utc": "2025-03-26T00:00:00+00:00",
        "selected_symbols": [
          "AVAXUSDT",
          "ADAUSDT",
          "AUCTIONUSDT",
          "1000SATSUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 43,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-27",
        "decision_time_utc": "2025-03-27T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "1000SATSUSDT",
          "AVAXUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 13,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 43,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-28",
        "decision_time_utc": "2025-03-28T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "1000SATSUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 44,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-29",
        "decision_time_utc": "2025-03-29T00:00:00+00:00",
        "selected_symbols": [
          "AUCTIONUSDT",
          "ADAUSDT",
          "AVAXUSDT",
          "API3USDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 44,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-30",
        "decision_time_utc": "2025-03-30T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "AVAXUSDT",
          "AUCTIONUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 44,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-03-31",
        "decision_time_utc": "2025-03-31T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 46,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-04-01",
        "decision_time_utc": "2025-04-01T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "AVAXUSDT"
        ],
        "candidate_count": 2,
        "filter_counts": {
          "missing_1h": 12,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 46,
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
