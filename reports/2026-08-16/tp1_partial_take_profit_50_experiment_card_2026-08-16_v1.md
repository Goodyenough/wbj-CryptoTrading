---
created: 2026-08-16 01:32:42 CST
tags:
  - crypto
  - trading-system
  - experiment-card
  - tp1
experiment_id: tp1_partial_take_profit_50
dimension: exit_timing
status: gated_not_approved
execution_status: not_run
production_change: false
config_change: false
---

# TP1 部分止盈 50% 实验卡片 v1

## 1. 系统级目标

在保持入场质量、风险预算、持仓容量和 `atr_reclaim_0_35` 研究基准不变的前提下，判断退出路径是否能在 TP1 到达后兑现一部分利润、降低后续回撤，同时不过度牺牲趋势延续收益。当前目标是形成可复现的研究证据，不是增加交易数量，也不是授权 Paper 或实盘部署。

本卡片只允许作为审批材料和实现规格。当前 observation epoch 未结束前，不实现代码、不修改 `config/settings.toml`、不写入 Paper 生产状态机。

## 2. 唯一研究问题

在完全相同的入场、初始止损、TP1、TP2、仓位风险和容量约束下，TP1 触达时卖出 50% 仓位，剩余 50% 继续执行现有 TP1 后 `EMA20` trailing 与 TP2 退出，是否比当前“TP1 只改变状态、仓位仍保持 100%”的路径带来更好的成本后风险收益？

不回答以下问题：

- 不重新选择 TP1/TP2 价格或风险收益比。
- 不比较 `0.30 / 0.35 / 0.40`，不改变 `entry_reclaim_min_atr`。
- 不同时加入保本止损、新的 EMA、ATR trailing、max holding、ranking 或 capacity replacement。
- 不把 partial exit 释放的资金带来的新交易收益直接当作退出规则本身的收益。

## 3. 研究路线位置

这是阶段 2/3 的单变量 `exit_timing` 研究，基准为当前 `research_incumbent`（研究口径上的 `atr_reclaim_0_35`），不是新的 ATR 参数实验。它必须排在 2026-08-16 至 2026-08-22 observation epoch 之后；即使历史回测支持，也只能进入 `keep_for_research_review`，不能自动改变 Paper 或生产配置。

## 4. 事实、观察、假设与当前决定

### 事实

- 当前 `src/crypto_trading_system/trade_state.py` 在 TP1 触达时将状态改为 `TP1_HIT`，但不减少 `quantity`；TP2 或止损仍按完整数量计算。
- 当前默认退出路径为 `tp1_move_stop_to_breakeven_enabled=false`、`tp1_ema_trailing_stop_enabled=true`。
- 当前回测使用 `4h` 主周期和执行周期，`intrabar_policy="stop_first"`；没有 5m/15m 路径重建。
- 当前成本口径为：入场 maker 4 bps、入场滑点 5 bps、止损 taker 10 bps、止损滑点 10 bps、目标价退出 maker 4 bps。
- 当前回测默认初始资金为 10,000 USDT，单笔风险 1%，总活动风险 5%，最多 5 个 active positions，不使用杠杆。
- 当前前向 shadow 尚无足够 mature terminal outcome，不能用 Paper 结果评价这张卡片。

### 观察

- 既有 TP1 保本止损实验回答的是 TP1 后移动止损，不回答“TP1 是否应该先卖出一半”；两者不能互相替代。
- 部分止盈会增加一次目标价成交和手续费，同时可能降低 TP1 后剩余仓位的尾部风险；它也可能减少趋势单到达 TP2 时的收益。
- 部分成交会释放现金，但不会自动释放 active-position slot；若因此允许新的候选入场，收益中会混入 capacity-path 效应。

### 假设

H1：在相同入场与风险约束下，TP1 卖出 50% 能降低 TP1 后的回撤和极端亏损；扣除新增手续费后，组合风险调整收益不劣于当前完整仓位退出路径。

H0：50% partial exit 的风险降低不足以抵消手续费和趋势收益损失，或所谓改善主要来自释放现金后的新入场，而不是原交易退出路径。

### 当前决定

`status=gated_not_approved`、`execution_status=not_run`。先保存卡片，等待 observation epoch 决策和用户明确批准；不新增 `config/experiments.toml` 定义，不执行回测，不修改生产配置。

## 5. 固定实验口径

### 5.1 交易场所与数据

- Venue：Binance Spot，USDT 交易对；不使用合约 funding、借贷利息或杠杆。
- 主周期：`4h`；每根已收盘 4h K 线完成后作决定。
- K 线路径：使用现有回放的 OHLC 规则，不伪造 5m/15m 价格路径；`stop_first` 保持不变。
- Universe：使用同一份固定 symbol master `reports/2026-06-09/dynamic_master_full.json`（基准记录为 418 个 symbols），baseline 与 variant 使用相同的 dynamic-universe 生成口径和同一份 master，不为某一 arm 单独刷新 universe。
- 日期窗口：两个非重叠窗口，均为 UTC 左闭右开：
  - `2024-07-01 -> 2025-06-01`
  - `2025-06-01 -> 2026-06-01`
- 这两个窗口已经被其他研究使用过，因此本实验结果只能标记为 `diagnostic/retest`，不能被称为 clean independent confirmation；不得使用存在明显历史 universe 缺口的 `2023-07-01 -> 2024-07-01` 窗口作为主要结论依据。
- 缺失 K 线不得填充为合成数据；若执行器需要 `--allow-data-gaps` 才能运行，报告必须列出缺口并把受影响窗口标为 diagnostic，不能隐藏数据质量问题。

### 5.2 Baseline 与 variant

| 项目 | Baseline：`research_incumbent` | Variant：`tp1_partial_take_profit_50` |
|---|---|---|
| 入场 | 现有研究基准，包含 `entry_reclaim_min_atr=0.35` 的研究口径 | 完全相同 |
| 初始仓位 | 按账户权益 × 1% 风险、entry 与初始 stop 计算 | 完全相同 |
| 初始止损 | 现有 stop | 完全相同 |
| TP1/TP2 | 候选原始 TP1/TP2 | 完全相同 |
| TP1 触达 | 状态改为 `TP1_HIT`，保留 100% 数量 | 第一次 TP1 触达时成交 50%，剩余 50% 保留 |
| TP1 后 stop | 现有 `EMA20` trailing 逻辑 | 完全相同，但只作用于剩余 50% |
| TP2 | 100% 数量按 TP2 退出 | 剩余 50% 按 TP2 退出 |
| 其他变量 | 不变 | 唯一变化是 TP1 partial exit ratio=`0.50` |

### 5.3 账户、容量与成本

- `initial_equity=10,000 USDT`。
- `risk_per_trade_pct=1%`，`total_active_risk_pct=5%`。
- `max_active_positions=5`、`max_open_plans=10`、`max_position_notional_pct=100%`。
- `allow_leverage=false`，不加仓、不补仓、不再平衡。
- `watch_expiry_bars=18`，`max_holding_bars_without_tp1=0`；不把 max holding 混入本实验。
- 入场：maker fee `4 bps`，向不利方向滑点 `5 bps`。
- TP1 partial、TP2：沿用现有目标价成交口径，maker fee `4 bps`，无额外目标价滑点；variant 必须单独记录新增 TP1 成交费。
- 止损/EMA trailing/time exit（若未来单独启用）：taker fee `10 bps`，向不利方向滑点 `10 bps`。
- 资金、手续费、滑点和剩余仓位的市值都必须进入 equity curve；不能只在最终交易表里扣一次费用。

## 6. 事件与状态机语义

这是实现前必须冻结的语义，未经重新审批不得在编码时临时改变：

1. TP1 partial 只能发生一次；重复的 4h update、重复导入或重放不能再次卖出 50%。
2. 在 `ENTERED` 状态下保留现有 `stop_first` 优先级。若同一根 K 线同时触及 stop 和 TP1，stop 优先，不产生 partial exit。
3. 若同一根 K 线同时触及 TP1 和 TP2，沿用现有引擎的 same-bar precedence，不新增“先 TP1 再 TP2”的事后推断；必须在报告中明确该根 K 线的处理结果。
4. TP1 成交后，状态进入 `TP1_HIT`，剩余数量为初始数量的 50%；同一根 K 线不得再次触发 TP2 或 trailing stop，下一根已收盘 4h K 线才继续推进，保持当前 `step_trade` 的单次事件推进语义。
5. 后续 stop、EMA trailing 和 TP2 只对剩余数量成交；最终交易的总 realized PnL 等于 TP1 partial realized PnL 加剩余数量的最终 realized PnL，扣除各自费用。
6. `r_multiple_net` 的分母仍使用原始入场风险 `cash_risk`，不能因为卖出一半而重置风险分母。
7. partial exit 不释放 active-position slot；variant 因 partial 成交而产生的新入场必须单独标记为 capacity-path trade，并与原有同机会退出收益分开归因。
8. 若新实现无法在交易、事件、现金、费用和数据库快照中完整重建上述路径，结果只能判为 `insufficient_evidence`。

## 7. 必须输出的证据

### 7.1 组合层

每个窗口、每个 arm 以及两窗口合计都要报告：

- `trades`、`closed_trades`、open trades、sample sufficiency。
- CAGR、净收益、Sharpe、Sortino、最大回撤、胜率、Profit factor。
- exposure、turnover、fee drag、最大单笔亏损、尾部亏损分位数。
- TP1 hit rate、TP2 close rate、stop rate、平均持仓 bars、部分止盈金额和新增成交次数。
- `RISK_ON`、`RISK_OFF`、震荡/趋势标签，以及 weekday/weekend 分层；某 regime 没有样本时写 `N/A`，不得补造样本。

### 7.2 交易机制层

- 同一 entry opportunity 的 baseline/variant 配对结果。
- TP1 触达后到最终退出的 MFE、MAE、最大回吐、最终 R。
- TP1 partial 产生的 realized PnL、费用、剩余仓位的 TP2/stop/trailing 结果。
- `TP1_HIT`、`TP1_PARTIAL_EXIT`、`TP2`、`STOPPED` 事件顺序和幂等性。
- 同一机会是否出现 variant-only 新入场；这部分单独列为 capacity-path，不得归入直接退出改善。
- 按 symbol、month、symbol-month 聚合，检查收益是否集中在少数样本。

### 7.3 可复现性与数据质量

- baseline/variant 使用的 Git commit、settings/config hash、symbol master 文件、窗口、intrabar policy 和成本参数。
- 每个窗口的 K 线缺口、跳过 symbol、same-bar ambiguity 和右截尾交易。
- 报告不能把未闭合交易当作 closed outcome，也不能把 variant 的新增入场当作 baseline 的同机会配对。

## 8. 审批标准

### 支持 H1 的条件

必须同时满足：

- 每个窗口 baseline 与 variant 的 `closed_trades >= 30`；两窗口合计至少 `30` 个可配对的 TP1-hit entries，覆盖至少 `5` 个独立 symbols；否则直接是证据不足。
- variant 在两个窗口中净收益均不低于 baseline 超过 `1.0` 个百分点的反向差距；Profit factor 不下降超过 `0.05`，Sharpe 不下降超过 `0.10`。
- 至少一个窗口的最大回撤相对改善 `>=10%`，另一个窗口最大回撤不得恶化超过 `5%`；同时 TP1 后最大回吐或尾部亏损有方向一致的改善。
- 配对的同一入场退出路径在扣除新增费用后不恶化；若组合改善完全来自 partial 释放现金后的 variant-only 新入场，则不能支持 H1。
- 改善不能由单个 symbol-month 贡献超过 50%，不能由单个极端赢家决定；same-bar、缺口、lookahead 和状态迁移审计通过。

### 否定 H1 的条件

满足任一项即可判定 `reject_candidate`：

- 两个窗口净收益都比 baseline 低超过 `1.0` 个百分点，或 Profit factor 都低超过 `0.10`。
- 最大回撤在两个窗口都恶化超过 `10%`，且没有相称的 TP1 后尾部风险改善。
- TP1 后趋势延续损失明显，主要赢家的收益被 50% partial 系统性截断，且费用无法解释为可接受成本。
- 组合改善主要来自 variant-only 新入场，配对的原交易退出路径没有改善。
- 发现 partial 重复成交、数量不守恒、费用重复扣除、PnL 分母变化、same-bar 前视或 Paper/回放状态语义不一致。

### 证据不足的条件

判定 `sample_insufficient` / `retest`，不写 `keep`：

- 任一窗口闭合交易或 TP1-hit 样本未达到门槛。
- 两窗口方向相反且没有足够 regime 样本解释差异。
- 结果依赖明显数据缺口、current-master survivor bias、右截尾或单个 symbol-month。
- 无法把直接退出效果与 capacity-path 新入场效果分开。
- 回测指标改善，但事件、现金、手续费或状态快照无法完整重建。

## 9. 实现前置清单

只有用户批准后才允许进入编码；至少需要：

- 明确保存初始数量、剩余数量、TP1 已成交数量、TP1 partial 成交价/时间/费用/realized PnL，并保证旧数据兼容。
- 在 `trade_state` 中实现一次性、幂等的 `TP1_PARTIAL_EXIT` 事件；保留现有 `TP1_HIT` 兼容语义。
- 在 backtest replay 中正确更新 cash、equity curve、active risk、剩余仓位和最终 `r_multiple_net`。
- 在 Paper 状态机、SQLite、snapshot、报告和 shadow 日志之间统一数量与 PnL 语义；在 backtest-only 验证通过前不接入 Paper。
- 测试：TP1 恰好卖出 50%、重复 update 不重复卖出、stop-first 同 bar、TP2 只卖剩余仓位、TP1 后 stop/EMA trailing 只作用剩余仓位、手续费只扣一次、数量守恒、capacity-path 单独标记、旧数据读取兼容。
- 实现后先跑临时 fixture 和 backtest-only replay，再决定是否允许正式 A/B；不得直接修改 `config/settings.toml`。

## 10. 执行与结论规则

审批后，先在固定两个窗口运行 backtest-only A/B，先检查状态与成本账，再看收益指标。实验完成后必须用“非技术结论 + 技术证据”两层写入实验日志，并给出 `keep / revert / retest`；任何结果都不自动授权修改默认配置、Paper 行为或实盘路径。

当前结论：`gated_not_approved`。这是一张完整的研究设计卡片，不是实验结果报告。
