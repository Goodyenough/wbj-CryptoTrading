---
created: 2026-06-06 23:43:36 CST
tags:
  - crypto
  - trading-system
  - backtest
backtest_run_id: aef9051097a3
report_version: v4
sample_sufficient: false
universe_mode: true
universe_type: dynamic
---

# 回测报告 2025-01-01 至 2025-02-01 v4

- 回测 ID：`aef9051097a3`
- 交易对：`1000SATSUSDT`, `1MBABYDOGEUSDT`, `AAVEUSDT`, `ACHUSDT`, `ACTUSDT`, `ADAUSDT`, `AGLDUSDT`, `AIUSDT`, `AIXBTUSDT`
- UTC 区间：2025-01-01T00:00:00+00:00 -> 2025-02-01T00:00:00+00:00
- 初始权益：10,000.00 USDT
- 最终权益：9,692.27 USDT
- 净收益：-3.08%
- 代码 commit：`085feff13ca20eb79ee2d6872ca49901aae814e1`
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
- Master symbols / Master 币种数：20
- Source limit / 调试截断：20
- Source limit applied / 是否截断：true
- Refresh frequency / 刷新频率：daily
- Universe refreshes / Universe 刷新次数：32
- Selected symbols per refresh / 每次入选数量：min=1, avg=4.19, max=5
- Top selected symbols / 最常入选：`ADAUSDT`(32), `AAVEUSDT`(29), `ACTUSDT`(26), `AIXBTUSDT`(20), `1000SATSUSDT`(11), `AGLDUSDT`(6), `ACHUSDT`(5), `AIUSDT`(4), `1MBABYDOGEUSDT`(1)
- Filter counts / 过滤统计：
```json
{
  "missing_1h": 138,
  "insufficient_24h": 1,
  "reconstruct_error": 0,
  "low_quote_volume": 362,
  "low_trades": 0,
  "stable_like": 0
}
```
> Warning / 警告：dynamic universe 的 symbol master 来自当前 Binance exchangeInfo；历史上曾交易但今天已退市的币不会进入 master list，因此仍有退市幸存者偏差。
> Runtime / 耗时提示：第一次完整运行需要缓存大量 1h/4h/1d K 线，可能很慢；缓存命中后后续回测会明显加快。

## 核心指标

| Metric（指标） | Value（数值） |
|---|---:|
| Trades（计划总数） | 3 |
| Closed trades（已结束交易） | 3 |
| Open trades（仍开放持仓） | 0 |
| Win rate（胜率） | 0.00% |
| Profit factor（盈利因子） | 0.00 |
| Avg R（平均R倍数） | -1.02 |
| Net return（净收益率） | -3.08% |
| Max drawdown（最大回撤） | 347.12 / 3.46% |
| Intrabar max drawdown（K线内最大回撤） | 334.89 / 3.34% |
| TP1 touched rate（第一止盈触达率） | 0.00% |
| TP2 close rate（第二止盈平仓率） | 0.00% |
| Stop rate（止损率） | 100.00% |
| Fee drag（手续费拖累） | 3.74 USDT |
| Tail max single loss（最大单笔亏损） | -103.38 USDT |
| CAGR（年化复合收益率） | -30.79% |
| Sharpe（夏普比率） | -6.10 |
| Sortino（索提诺比率） | -2.66 |
| Exposure（持仓暴露时间） | 14.52% |
| Turnover（换手率） | 0.29 |
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
| BTC buy-hold（买入并持有BTC） | 9.05% |
| ETH buy-hold（买入并持有ETH） | -1.71% |
| Cash（现金不交易） | 0.00% |
| Equal-weight symbols（等权持有本次币种） | -6.47% |

## 已结束交易

| Symbol（交易对） | Status（状态） | Created（创建时间） | Entry（入场价） | Exit（出场价） | Qty（数量） | Gross PnL（毛盈亏） | Net PnL（净盈亏） | Net R（净R倍数） | Fees（手续费） | Notes（备注） |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| `AAVEUSDT` | STOPPED（已止损） | 2025-01-04T04:00:00+00:00 | 340.44 | 301.35 | 2.59 | -101.22 | -102.35 | -1.02 | 1.13 | Stop loss hit. |
| `ADAUSDT` | STOPPED（已止损） | 2025-01-05T12:00:00+00:00 | 1.06 | 0.93 | 772.92 | -100.95 | -102.00 | -1.02 | 1.05 | Stop loss hit. |
| `AGLDUSDT` | STOPPED（已止损） | 2025-01-06T00:00:00+00:00 | 2.77 | 2.53 | 428.28 | -101.82 | -103.38 | -1.03 | 1.56 | Stop loss hit. |

## 回测结束仍开放

| Symbol（交易对） | Status（状态） | Entry（入场价） | Qty（数量） | Unrealized Handling（未实现盈亏处理） | Notes（备注） |
|---|---|---:|---:|---|---|

## 未入场/过期计划

| Symbol（交易对） | Status（状态） | Created（创建时间） | Entry Zone（入场区间） | Score（评分） | Notes（备注） |
|---|---|---|---:|---:|---|
| n/a | n/a | n/a | n/a | n/a | No inactive plans. |

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
| ERROR | `1000CHEEMSUSDT` | 1h | No klines available for requested range. |
| ERROR | `1000CHEEMSUSDT` | 4h | No klines available for requested range. |
| ERROR | `1000CHEEMSUSDT` | 1d | No klines available for requested range. |
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
| ERROR | `2ZUSDT` | 1h | No klines available for requested range. |
| ERROR | `2ZUSDT` | 4h | No klines available for requested range. |
| ERROR | `2ZUSDT` | 1d | No klines available for requested range. |
| WARNING | `ACEUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACHUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACHUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACHUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACHUSDT` | 1d | Large wick/range candle. |
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
| WARNING | `ACXUSDT` | 1h | Large wick/range candle. |
| WARNING | `ACXUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACXUSDT` | 4h | Large wick/range candle. |
| WARNING | `ACXUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACXUSDT` | 1d | Large wick/range candle. |
| WARNING | `ACXUSDT` | 1d | Large wick/range candle. |
| WARNING | `ADXUSDT` | 1h | Large wick/range candle. |
| WARNING | `ADXUSDT` | 4h | Large wick/range candle. |
| WARNING | `ADXUSDT` | 1d | Large wick/range candle. |
| WARNING | `ADXUSDT` | 1d | Large wick/range candle. |
| WARNING | `AEVOUSDT` | 1d | Large wick/range candle. |
| WARNING | `AEVOUSDT` | 1d | Large wick/range candle. |
| WARNING | `AGLDUSDT` | 1h | Large wick/range candle. |
| WARNING | `AGLDUSDT` | 4h | Large wick/range candle. |
| WARNING | `AGLDUSDT` | 4h | Large wick/range candle. |
| WARNING | `AGLDUSDT` | 1d | Large wick/range candle. |
| WARNING | `AGLDUSDT` | 1d | Large wick/range candle. |
| WARNING | `AGLDUSDT` | 1d | Large wick/range candle. |
| WARNING | `AGLDUSDT` | 1d | Large wick/range candle. |
| WARNING | `AGLDUSDT` | 1d | Large wick/range candle. |
| WARNING | `AGLDUSDT` | 1d | Large wick/range candle. |
| ERROR | `AIGENSYNUSDT` | 1h | No klines available for requested range. |
| ERROR | `AIGENSYNUSDT` | 4h | No klines available for requested range. |
| ERROR | `AIGENSYNUSDT` | 1d | No klines available for requested range. |
| WARNING | `AIUSDT` | 1d | Large wick/range candle. |
| WARNING | `AIUSDT` | 1d | Large wick/range candle. |
| WARNING | `AIXBTUSDT` | 1h | Large wick/range candle. |
| WARNING | `AIXBTUSDT` | 4h | Large wick/range candle. |
| WARNING | `AIXBTUSDT` | 1d | Large wick/range candle. |
| WARNING | `AIXBTUSDT` | 1d | Large wick/range candle. |
| WARNING | `AIXBTUSDT` | 1d | Large wick/range candle. |
| ERROR | `0GUSDT` | 4h | No primary interval klines inside requested backtest period. |
| ERROR | `1000CHEEMSUSDT` | 4h | No primary interval klines inside requested backtest period. |
| ERROR | `2ZUSDT` | 4h | No primary interval klines inside requested backtest period. |
| ERROR | `AIGENSYNUSDT` | 4h | No primary interval klines inside requested backtest period. |

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
    "created_at_utc": "2026-06-06T15:43:36+00:00",
    "refresh_frequency": "daily",
    "max_symbols": 5,
    "master_count": 20,
    "source_limit": 20,
    "source_limit_applied": true,
    "universe_refresh_count": 32,
    "selected_count_min": 1,
    "selected_count_avg": 4.1875,
    "selected_count_max": 5,
    "top_selected_symbols": [
      {
        "symbol": "ADAUSDT",
        "days_selected": 32
      },
      {
        "symbol": "AAVEUSDT",
        "days_selected": 29
      },
      {
        "symbol": "ACTUSDT",
        "days_selected": 26
      },
      {
        "symbol": "AIXBTUSDT",
        "days_selected": 20
      },
      {
        "symbol": "1000SATSUSDT",
        "days_selected": 11
      },
      {
        "symbol": "AGLDUSDT",
        "days_selected": 6
      },
      {
        "symbol": "ACHUSDT",
        "days_selected": 5
      },
      {
        "symbol": "AIUSDT",
        "days_selected": 4
      },
      {
        "symbol": "1MBABYDOGEUSDT",
        "days_selected": 1
      }
    ],
    "filter_counts": {
      "missing_1h": 138,
      "insufficient_24h": 1,
      "reconstruct_error": 0,
      "low_quote_volume": 362,
      "low_trades": 0,
      "stable_like": 0
    },
    "selection_by_day": [
      {
        "date_utc": "2025-01-01",
        "decision_time_utc": "2025-01-01T04:00:00+00:00",
        "selected_symbols": [
          "ACTUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "AGLDUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 11,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-02",
        "decision_time_utc": "2025-01-02T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "AGLDUSDT",
          "ACTUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 11,
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
          "AGLDUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 10,
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
          "AAVEUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 11,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-05",
        "decision_time_utc": "2025-01-05T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "AAVEUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 12,
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
          "AGLDUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 11,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-07",
        "decision_time_utc": "2025-01-07T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "ACTUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 12,
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
          "AAVEUSDT",
          "1000SATSUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 9,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-09",
        "decision_time_utc": "2025-01-09T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "ACTUSDT",
          "AAVEUSDT",
          "1000SATSUSDT",
          "AIUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 10,
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
          "AAVEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 5,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 11,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-11",
        "decision_time_utc": "2025-01-11T00:00:00+00:00",
        "selected_symbols": [
          "AIUSDT",
          "1000SATSUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 1,
          "reconstruct_error": 0,
          "low_quote_volume": 10,
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
          "AIXBTUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 13,
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
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 15,
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
          "ACTUSDT",
          "AIXBTUSDT",
          "1000SATSUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 11,
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
          "ACTUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 12,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-16",
        "decision_time_utc": "2025-01-16T00:00:00+00:00",
        "selected_symbols": [
          "AIXBTUSDT",
          "ADAUSDT",
          "AAVEUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 12,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-17",
        "decision_time_utc": "2025-01-17T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "AIXBTUSDT",
          "AAVEUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 12,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-18",
        "decision_time_utc": "2025-01-18T00:00:00+00:00",
        "selected_symbols": [
          "AAVEUSDT",
          "ADAUSDT",
          "ACTUSDT",
          "AIXBTUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 12,
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
          "AAVEUSDT",
          "ACTUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 12,
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
          "AAVEUSDT",
          "ACTUSDT",
          "1000SATSUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 10,
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
          "ADAUSDT",
          "ACTUSDT",
          "1000SATSUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 10,
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
          "1MBABYDOGEUSDT",
          "ADAUSDT",
          "AIXBTUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 10,
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
          "AAVEUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 12,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-24",
        "decision_time_utc": "2025-01-24T00:00:00+00:00",
        "selected_symbols": [
          "1000SATSUSDT",
          "ADAUSDT",
          "ACTUSDT",
          "AIXBTUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 11,
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
          "AIXBTUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 12,
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
          "ADAUSDT",
          "AIXBTUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 11,
          "low_trades": 0,
          "stable_like": 0
        }
      },
      {
        "date_utc": "2025-01-27",
        "decision_time_utc": "2025-01-27T00:00:00+00:00",
        "selected_symbols": [
          "ADAUSDT",
          "AIXBTUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 3,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 13,
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
          "AIXBTUSDT",
          "AAVEUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 11,
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
          "AAVEUSDT",
          "AIXBTUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 12,
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
          "ADAUSDT"
        ],
        "candidate_count": 6,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 10,
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
          "AIXBTUSDT",
          "ADAUSDT"
        ],
        "candidate_count": 4,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 12,
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
          "ADAUSDT",
          "AIXBTUSDT"
        ],
        "candidate_count": 5,
        "filter_counts": {
          "missing_1h": 4,
          "insufficient_24h": 0,
          "reconstruct_error": 0,
          "low_quote_volume": 11,
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
