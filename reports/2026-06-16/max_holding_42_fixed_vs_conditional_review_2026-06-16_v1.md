---
created: 2026-06-16T00:10:00+08:00
tags:
  - crypto
  - trading-system
  - abtest
  - exit-review
experiment: max_holding_42_fixed_vs_conditional_sensitive
---

# 固定 42 根退出 vs 条件式 42 根退出复盘

## 背景

上一轮条件式 42 根实验以“无持仓时间退出”为 baseline，不能直接证明条件式退出优于固定 42 根退出。本轮在相同 sensitive 策略、symbol master、窗口和 42 根阈值下，仅切换 `max_holding_bars_conditional`。

## 假设

条件式版本只在 42 根后收盘低于 EMA20 或入场价时退出，可能保留延迟启动赢家，同时维持固定 42 根规则的止血能力。

## 实验

- 实验：`max_holding_42_fixed_vs_conditional_sensitive`
- baseline：`max_holding_bars_without_tp1=42`，`max_holding_bars_conditional=false`
- variant：`max_holding_bars_without_tp1=42`，`max_holding_bars_conditional=true`
- 唯一变化：`backtest.max_holding_bars_conditional: false -> true`
- 策略：`risk_off_core_buy_enabled=false`、`entry_reclaim_close_enabled=true`、`tp1_ema_trailing_stop_enabled=true`、sensitive regime 阈值
- 样本：固定 `reports/2026-06-09/dynamic_master_full.json`（418 symbols），`max-symbols=40`
- 窗口：`2024-07-01 -> 2025-06-01`、`2025-06-01 -> 2026-06-01`，无重叠，共 700 天

## 结果

### 2024-07-01 -> 2025-06-01

- trades：517 -> 509，变化 -1.55%
- closed_trades：134 -> 134，变化 0%
- 胜率：50.00% -> 44.78%，变化 -5.22 个百分点
- Profit factor：1.48 -> 1.38
- Sharpe：1.31 -> 1.21
- 最大回撤：20.66% -> 21.04%
- 净收益：31.86% -> 27.57%，变化 -4.30 个百分点
- avg R：0.235 -> 0.219
- stop rate：50.00% -> 54.48%
- RISK_ON 净 PnL：3226.48 -> 2911.83

### 2025-06-01 -> 2026-06-01

- trades：420 -> 412，变化 -1.90%
- closed_trades：110 -> 110，变化 0%
- 胜率：47.27% -> 49.09%，变化 +1.82 个百分点
- Profit factor：1.31 -> 1.64
- Sharpe：0.86 -> 1.42
- 最大回撤：11.05% -> 12.40%
- 净收益：15.95% -> 30.75%，变化 +14.80 个百分点
- avg R：0.140 -> 0.249
- stop rate：45.45% -> 47.27%
- RISK_ON 净 PnL：1996.22 -> 3480.82
- RISK_OFF 净 PnL：-401.00 -> -405.70，基本不变

## 结论

`retest`：条件式版本存在明显的时间阶段依赖。它在近端窗口显著提高收益、PF、Sharpe 与 avg R，但在较早窗口降低胜率、PF、Sharpe 和净收益；两个窗口的最大回撤都略高于固定 42 根版本。因此不能证明条件式版本稳定优于固定退出，也不应写入默认配置。

直接对照还修正了上一轮判断：条件式版本相对“无时间退出”表现优秀，不等于它优于固定 42 根。当前证据下，固定 42 根更稳健，条件式 42 根更偏向捕捉近期延迟趋势赢家。

## 下一步

1. 用同一 fixed-vs-conditional 定义补一个更早、非重叠且样本充足的窗口，优先 `2023-07-01 -> 2024-07-01`。
2. 若第三窗口仍显示阶段分化，再测试“42 根后必须同时位于 entry 与 EMA20 上方，且 EMA20 斜率为正才继续持有”，只新增 EMA 斜率确认一个变量。
3. 在额外证据完成前，不修改默认 `settings.toml`，也不影响当前 5 天数据库稳定性窗口。

## 第三窗口补测（2026-06-16）

按上述下一步补跑 `2023-07-01 -> 2024-07-01`，仍使用固定 `dynamic_master_full.json`、`max-symbols=40`、同一 sensitive 组合，唯一变量仍为 `max_holding_bars_conditional=false -> true`。

- trades：baseline 769 -> variant 758，变化 -1.43%
- closed_trades：207 -> 197，变化 -4.83%
- 胜率：49.76% -> 45.69%，变化 -4.07 个百分点
- Profit factor：1.32 -> 1.20
- Sharpe：1.40 -> 0.89
- 最大回撤：19.81% -> 20.69%
- 净收益：38.96% -> 22.26%，变化 -16.70 个百分点
- avg R：0.173 -> 0.117
- stop rate：47.34% -> 48.22%
- regime：全部闭合交易均为 `RISK_ON`，净 PnL 3896.37 -> 2225.91

### 三窗口综合判断

`reject_candidate`：第三窗口样本充足，并且与较早的 `2024-07-01 -> 2025-06-01` 一样，条件式 42 根弱于固定 42 根；只有近端 `2025-06-01 -> 2026-06-01` 明显改善。三段中条件版有 2 段净收益/PF/Sharpe 变差，3 段 MDD 全部更高，因此不应部署 `max_holding_bars_conditional=true`。

更稳健的结论是：固定 42 根退出仍是当前较优候选；条件式退出更像近端行情特化，对早期强 RISK_ON 趋势阶段反而保留了更多最终回吐的仓位。

### 更新后的下一步

1. 不把 `max_holding_bars_conditional=true` 写入默认 `settings.toml`。
2. 若继续研究“延迟赢家保留”，应另开单变量实验：42 根后只有在 price > entry、price > EMA20 且 EMA20 斜率为正时才允许继续持有。
3. 固定 42 根退出可进入 3 周 paper 观察后的 keep review，但必须等待当前数据库稳定窗口完成，避免再次改动 `settings.toml` 重置 config hash。

## 证据

- `abtest_summary_dynamic_universe_max_holding_42_fixed_vs_conditional_sensitive_2026-06-15_v1.md`
- `backtest_regime_breakdown_5c8c378c16fd_e562c08d5fca_v1.md`
- `backtest_regime_breakdown_31f5e44d3d40_eb11621e6738_v1.md`
- `abtest_dynamic_universe_max_holding_42_fixed_vs_conditional_sensitive_2023-07-01_2024-07-01_v1.md`
- `backtest_regime_breakdown_6228ab0da9d5_769b52c120b5_v1.md`
