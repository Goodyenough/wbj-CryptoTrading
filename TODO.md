# CryptoTradingSystem 待办清单

## 2026-07-27 当前执行状态

- [x] 完成 `replacement_closure_audit`：复用 Stage 1 JSON 与 Stage 4 Raw Summary 做去重、stale-trade 集中度、first-event-per-stale-trade、exclude 2025-07、exclude same-bar ambiguous 与 cluster bootstrap；结论 `paused_no_stable_executable_edge`，capacity replacement 分支冻结，不进入 Stage 5 shadow replacement。
- [x] 生成 `stage_a_to_e_execution_review`：整合 Stage A-E gate，确认 Stage B/C/D 证据已由既有 `atr_reclaim_0_35` A/B、交易级归因和阈值敏感性报告覆盖；Stage E 因 gate failed 不启动，下一优先级回到 capacity-neutral entry-quality retest。
- [ ] 后续如继续 entry-quality 研究，只允许提出单变量 retest 卡片；不得把 `atr_reclaim_0_35` 与 replacement、relative strength 或其它过滤器叠加后直接实验。

## 策略优化路线图

背景：当前系统已经可以扫盘、生成交易计划、跑模拟盘和回测，但策略交易质量仍然偏弱。

当前需要重点改善的问题：
- 胜率：25.42%
- 止损率：74.58%
- Profit factor：0.85
- 最大回撤：19.64%

这些数据说明：系统仍然容易生成低质量交易计划，或者当前入场和止损规则太容易被市场噪音触发。

## Priority 1：优化选币策略

- [x] 增加数据质量过滤：优先保留 `DATA_OK`，对 `DATA_WARNING` 和 `DATA_ERROR` 的买入候选降级或拒绝。
- [x] 扩大验证池后再排序：先交叉验证 `min(top_n * 2, 10)` 个候选，再按数据质量降级后的结果补足最终 `top_n`。
- [x] 增加历史长度过滤：默认要求至少 180 根日线 K 线，才允许成为买入候选。
- [x] 修复回测 warmup：历史回放至少提前加载 `min_history_days + 60` 根日线，避免早期人为无信号盲区。
- [x] 增加 BTC/ETH 大盘环境过滤：大盘弱或不明确时，将山寨币买入候选降级为观察。
- [x] 将追高扣分和高波动扣分参数化，同时保持默认行为与旧硬编码规则等效。
- [x] 对齐模拟盘和回测口径：`paper add-from-scan` 默认只导入 `BUY_CANDIDATE`。
- [x] 回测报告增加 `sample_sufficient`：闭合交易少于 20 笔时显式标记样本不足。
- [x] A/B 测试更严格的历史长度过滤：当前 180 根日线 vs 250 根 vs 365 根；当前结论为 `history_365` 跨段不稳定，暂不 keep。
- [ ] 将历史长度逻辑拆成三段式：`min_indicator_history_days`、极短历史硬拒绝、短历史扣分。
- [ ] A/B 测试更严格的追高规则：对 24h 强涨后远离支撑的币进行排除或降级。
- [x] 提高流动性门槛，并测试对交易次数、胜率和回撤的影响；`liquidity_50m` 方向较好但样本仍需继续 retest。
- [x] A/B 测试更强的日线趋势过滤：只允许 `price > EMA20_1d >= EMA50_1d * 0.98` 的币成为买入候选；早期段（2024-07→2025-06）PF 0.91→0.97、净收益略改善，但近端段（2025-06→2026-06）止损率 77%→89%、净收益 -10.62%→-22.71%、MDD 扩大，结论 `reject_candidate`；弱市中趋势恢复后才允许入场反而导致在更高位置接入，质量更差。
- [ ] A/B 测试趋势相关高波动惩罚：只有在趋势未确认时才对高波动加重扣分。
- [x] 每次 A/B 实验后补一条简短结论：`keep`、`revert` 或 `retest`；当前 dynamic-universe A/B 均通过报告、开发计划和实验日志保留结论。

## Priority 2：优化入场规则

- [x] 不在第一次触碰入场区间时立刻入场，要求 4h 收盘重新站回支撑；当前 `entry_reclaim_close_enabled=true` 已是默认模拟盘口径。
- [x] 正式单变量 A/B 测试 `reclaim_quality_matrix / atr_reclaim_0_25`：两段净收益、PF、Sharpe、胜率均改善，但早期窗口 MDD 16.59% -> 19.21%，结论 `retest`，不部署。
- [x] 做 `atr_reclaim_0_25` 同维度阈值敏感性：`0.10`、`0.15` 近端退化，`0.35` 两段净收益/PF/MDD 均改善并进入 `candidate_keep_review`。
- [x] 复核 `atr_reclaim_0_35` 的交易级归因：改善主要来自 variant-only 新增赢家而非 common trades 普遍变好；早期窗口不算单一赢家驱动，近端窗口路径依赖较强，结论为 `candidate_keep_review_but_path_dependent`，暂不部署。
- [x] 人工复盘 `atr_reclaim_0_35` 近端关键赢家/错过赢家路径：variant-only 赢家 reclaim margin 均超过 0.35 ATR，但 baseline 错过的 TP2 赢家也质量不差，且结果强受 `max_active_positions=5` 容量路径影响；状态降为 `retest_path_dependent`。
- [x] 做 `capacity_and_opportunity_order_review` 非参数复核：容量约束真实存在，部分赢家确实被长持仓/低质量仓位占用路径影响，但证据混合，不能据此修改 `max_active_positions` 或 score 排序。
- [x] 做 `signal_fill_timing_audit`：审计 entry reclaim 的 `signal_time` / `decision_time` / `fill_time`、同根 K 线 exit/entry 顺序和 fill price 口径；结论 `timing_audit_warn_same_bar_ambiguity`，Stage 1 必须显式记录 same-bar ambiguity。
- [x] 完成 `blocked_entry_event_export`：导出唯一 blocked event、`block_reason=max_active_positions`、candidate rank、active slots snapshot、`fill_time_assumption`、`active_snapshot_after_exits`、`same_bar_entry_exit_possible` 和 `same_bar_entry_tp1_possible`；canonical run `110c51eef593` 复跑导出 512 个事件，`replay_entered_trades=58` 与 source 一致。
- [x] 做 `replay_consistency_audit`：确认 blocked event export 与 canonical baseline 的 entered trades、entry time、active count path、候选排序和 blocked event 重复运行一致；结论 `replay_consistency_pass_with_ordering_limit`，source/replay entered trades、active path、final equity、blocked event repeat mismatch 均为 0，但候选排序只通过源码 marker + 重复事件签名间接验证。
- [x] 做 `stale_slot_continuation_review`：独立评估 pre-TP1 仓位达到 42 bars 后继续持有的边际价值，统一 `42 bars = 168h` 口径；结论 `stale_slot_continuation_weak_retest`，26 个合格 stale slots，`forward_R_42_mean=-0.132`，`eventual_continuation_R_mean=-0.129`，支持继续诊断 replacement 但不部署。
- [x] 做 `blocked_candidate_vs_stale_slot_review`：只比较排序第一的 capacity-blocked candidate 与事前规则选出的 pre-TP1 stale slot，post-TP1 仅作对照，oracle 仅作上限；结论 `replacement_edge_not_supported`，42 个合格比较事件中 `net_delta_R_42_mean=0.309` 但 median `-0.223`、positive ratio `42.9%`、20% trimmed mean 约 `0.001`，不进入 shadow replacement。
- [ ] 测试更靠近 `entry_low` 的入场方式，而不是默认按 `entry_high` 附近成交。
- [ ] 要求 RSI 出现恢复，例如从 45-55 区间重新向上。
- [ ] 拒绝主要由放量下跌驱动的形态。
- [ ] 避免在 4h 趋势仍明显向下时接飞刀。

## Priority 3：优化卖出规则

- [ ] 测试 TP1 部分止盈，例如 TP1 卖出 50%。
- [ ] TP1 触达后将止损移动到保本价。
- [ ] 测试 TP1 后使用 4h EMA20 跟踪止损。
- [ ] 测试 TP1 后使用 ATR 跟踪止损。
- [ ] 对比固定 TP2 和趋势跟踪退出规则。
- [ ] 测试 ATR 动态止损，替代单纯结构固定止损。

## Priority 4：回测与 A/B 纪律

- [x] 增加 `backtest-universe` snapshot 模式：用当前 Binance 市场快照选币，再回放历史 K 线，并在报告中记录快照元数据和幸存者偏差警告。
- [x] 完成 Dynamic Universe Backtest MVP：每日用已收盘历史 K 线重建 universe，再生成候选交易计划。来源：2026-06-06 universe snapshot smoke test。
- [x] 增加 K 线无数据负缓存：新上市币在指定历史区间无数据时，不要在后续 dynamic-universe smoke 中反复请求。
- [ ] 在 K 线缓存足够热之后，不使用 `--source-limit` 跑更大的 dynamic-universe A/B 实验。
- [ ] 研究 Binance 历史/退市币 symbol master list，降低 dynamic universe 回测中的退市幸存者偏差。
- [ ] 每次实验只改变一个策略维度。
- [ ] 每次实验使用同一个 symbol universe 和同一个日期区间。
- [ ] 对比净收益、最大回撤、胜率、Profit factor、平均 R、止损率和交易次数。
- [ ] 每份实验报告使用清晰的规则名和版本号保存。
- [ ] 每次实验保留简短决策说明：应该保留、回滚还是继续复测。
- [x] 增加 A/B 多时段汇总报告：`python main.py abtest-summary --experiment ... --mode dynamic_universe --reports-date ...`。
- [x] 用更长近端窗口继续验证 `liquidity_50m`；`2025-06-01 -> 2026-06-01` 样本充足且方向继续改善。
- [x] 增加 A/B walk-forward 编排命令：`python main.py abtest-walk-forward --experiment ... --periods ...`。
- [x] A/B 汇总增加时段重叠分析：输出 `unique_coverage_days` 和 `overlap_periods`，重叠窗口保持 `retest`。
- [x] A/B 汇总增加 dynamic universe 偏差提示：输出当前 `exchangeInfo` master 依赖和 `source_limit` 截断风险。
- [x] 用非重叠 walk-forward 窗口验证 `liquidity_50m`：`2025-01-01 -> 2025-06-01` 样本不足，`2025-06-01 -> 2026-06-01` 样本充足且改善，整体仍为 `retest`。
- [x] 用更大 dynamic universe 复测 `liquidity_50m`：`source-limit 150 / max-symbols 40` 样本充足且方向继续改善，但仍为 `retest`。
- [x] 支持保存/加载 dynamic universe `SymbolMaster` JSON，让 A/B 和 walk-forward 可以复用同一份固定 master。
- [x] 增加 `dynamic-symbol-master` 导出命令，并生成 `reports/2026-06-09/dynamic_master_source150.json`。
- [x] 用固定 `SymbolMaster` 文件复跑 `liquidity_50m` 的非重叠 walk-forward；近端段样本充足且方向继续改善，整体仍为 `retest`。
- [x] 导出不截断的 full dynamic `SymbolMaster`：`reports/2026-06-09/dynamic_master_full.json`，当前 master_count=418。
- [x] 用 `dynamic_master_full.json` 复跑 `liquidity_50m` 近端窗口：样本充足且方向继续改善，但策略仍为负收益，结论 `retest`。
- [x] 用 `dynamic_master_full.json` 跑 `liquidity_50m` 非重叠 walk-forward；早期窗口仍样本不足，近端窗口样本充足且改善，整体 `retest`。
- [x] 延长 full master 早期窗口到 `2025-01-01 -> 2025-09-01`；样本充足且改善延续，但仍为负收益，结论 `retest`。
- [x] 对 full master `liquidity_50m` 结果做市场环境分层：亏损主要来自 `RISK_ON` 和 `RISK_OFF`，variant 在两者中均减亏但仍为负。
- [x] 设计 `RISK_OFF` 下一轮规则 A/B：新增 `risk_off_no_core_buy`，测试弱市是否连 BTC/ETH 也暂停新开仓。
- [x] 跑完 `risk_off_no_core_buy` full master A/B：`RISK_OFF` 闭合交易降到 0，整体减亏但 `RISK_ON` 略恶化，结论 `retest`。
- [x] 设计 `RISK_ON` 下一轮规则 A/B：新增 `top_n_3`，测试降低每次扫描候选容量是否能减少同日相关拥挤开仓。
- [x] 跑完 `top_n_3` full master A/B：`RISK_ON` 净 PnL 从 -1123.23 改善到 -212.97，但 `RISK_OFF` 不变，结论 `retest`。
- [x] 设计 `risk_off_no_core_top_n_3` 组合实验：同时关闭 RISK_OFF 核心币买入并将 `top_n` 降到 3。
- [x] 运行 `risk_off_no_core_top_n_3` full master A/B：单窗口转正，PF 约 1.00，净收益 +1.04%，但仍需非重叠 walk-forward。
- [x] 跑完 `risk_off_no_core_top_n_3` full master 非重叠 walk-forward 第一段 `2025-01-01 -> 2025-06-01`：方向改善但样本不足，结论 `retest`。
- [x] 跑完 `risk_off_no_core_top_n_3` full master 非重叠 walk-forward 第二段 `2025-06-01 -> 2026-06-01`：样本充足且继续改善，但仍为负收益，结论 `retest`。
- [x] 汇总 `risk_off_no_core_top_n_3` 两段 full master 非重叠 walk-forward：2 段无重叠、仅 1 段样本充足，结论 `retest`。
- [x] 设计下一轮 `RISK_ON` 入场 A/B：新增 `entry_reclaim_close`，要求 4h 收盘重新站上 `entry_high` 后才允许入场。
- [x] 运行 `entry_reclaim_close` full master A/B：`RISK_ON` 大幅减亏但整体仍为负收益，结论 `retest`。
- [x] 对 `entry_reclaim_close` 做 full master 非重叠 walk-forward 近端段 `2025-06-01 -> 2026-06-01`：variant 转正，`RISK_ON` 明显转正。
- [x] 对 `entry_reclaim_close` 做 full master 非重叠 walk-forward 早期段 `2025-01-01 -> 2025-06-01`：样本不足，PF 略降但净收益和回撤小幅改善，整体仍为 `retest`。
- [x] 汇总 `entry_reclaim_close` full master 非重叠 walk-forward：近端转正但早期样本不足，整体仍为 `retest`。
- [x] 设计 `entry_reclaim_close + risk_off_no_core_buy` 组合 A/B：新增 `risk_off_no_core_entry_reclaim`，验证近端 `RISK_ON` 转正能否与弱市停开核心币互补。
- [x] 运行 `risk_off_no_core_entry_reclaim` full master A/B：PF 略高于 1、净收益接近打平，`RISK_OFF` 清零但 `RISK_ON` 仍为负，结论 `retest`。
- [x] 对 `risk_off_no_core_entry_reclaim` 做 full master 非重叠 walk-forward 早期段 `2025-01-01 -> 2025-06-01`：方向减亏但样本不足，`RISK_ON` 仍全止损。
- [x] 对 `risk_off_no_core_entry_reclaim` 做 full master 非重叠 walk-forward 近端段 `2025-06-01 -> 2026-06-01`：样本充足且转正，`RISK_ON` 与 `NEUTRAL` 改善明显。
- [x] 汇总 `risk_off_no_core_entry_reclaim` full master 非重叠 walk-forward：2 段无重叠、仅近端样本充足，整体仍为 `retest`。
- [x] 为 `risk_off_no_core_entry_reclaim` 扩大早期样本：将早期段扩展到 `2024-07-01 -> 2025-06-01`，两段 full master 非重叠 walk-forward 均样本充足且转正，verdict=`candidate_keep_review`。
- [x] 设计下一轮 `RISK_ON` 退出 A/B：新增 `tp1_breakeven_stop`，测试 TP1 命中后将止损移动到入场价。
- [x] 运行 `tp1_breakeven_stop` full master A/B：PF、净收益、止损率均恶化，结论 `reject_candidate`，不进入 walk-forward。
- [x] 设计下一轮退出 A/B：新增 `tp1_ema20_trailing_stop`，测试 TP1 命中后改用 4h EMA20 跟踪止损替代立刻保本。
- [x] 运行 `tp1_ema20_trailing_stop` full master A/B：PF 0.58→0.75，avg_R -0.32→-0.14，净收益 -13.17%→-10.31%，方向改善但绝对值仍为负，结论 `retest`；需跨时段 walk-forward 或与 `risk_off_no_core_entry_reclaim` 组合验证。
- [x] 对 `tp1_ema20_trailing_stop` 做非重叠 walk-forward 两段：早期段（2024-07→2025-01）PF 1.30→1.41、净收益 +7.14%→+11.82%；近端段（2025-01→2025-09）PF 0.58→0.75、净收益 -13.17%→-10.31%；两段方向均改善但近端绝对值仍负，结论 `retest`（MDD 近端小幅上升，TP2 rate 下降为副作用）。
- [x] 运行 `risk_off_no_core_entry_reclaim + tp1_ema20_trailing_stop` 组合实验：早期段（2024-07→2025-06）PF 0.91→1.53、净收益 -5.59%→+16.74%、MDD 18.72%→14.99%；近端段（2025-06→2026-06）PF 0.73→1.05、净收益 -10.62%→+1.21%、MDD 24.24%→18.68%；两段均样本充足、净收益/PF/MDD 全面改善，verdict=`candidate_keep_review`。
- [x] 对 `risk_off_no_core_entry_reclaim_ema_stop` 做 keep review：发现模拟盘口径缺失两项——`entry_reclaim_close` 检查（WATCHING 状态下 4h 收盘未站回 entry_high 时阻止入场）和 `tp1_ema_trailing_stop`（TP1 后 EMA20 跟踪止损）；已在 `paper_trader.py` 补全并对齐，`risk_off_core_buy_enabled` 口径原本一致，三项规则现已全部在模拟盘中生效，commit `417681d`。
- [ ] 正式 keep `risk_off_no_core_entry_reclaim_ema_stop`：将三项 override（`risk_off_core_buy_enabled=false`、`entry_reclaim_close_enabled=true`、`tp1_ema_trailing_stop_enabled=true`）写入默认 `settings.toml`；当前模拟盘有存量 WATCHING 持仓，写入后会立即对其生效，决定等模拟盘跑一段时间、观察到足够真实案例后再执行。

- [x] 修复 `tp1_ema_trailing_stop` 两个技术债：EMA 不足 20 根时不激活 trailing stop；`tp1_trailing_ema_stop_active` 持久化到 `paper_trades`，避免模拟盘重启/重载后丢失 TP1 EMA trailing 状态。
- [x] 做市值分层回测：将 `dynamic_master_full.json` 拆成 large-cap（BTC/ETH/BNB/SOL）和 altcoin，两组分别跑当前 sensitive 组合；近端窗口 large-cap 净收益 +3.46%、MDD 11.36%，altcoin 净收益 -10.26%、MDD 23.44%，结论为弱市中 altcoin 风险暴露更像主要拖累，large-cap 值得单独观察。
- [x] 跨区间复测市值分层：两段非重叠 walk-forward 完成。牛市（2024-07→2025-06）large-cap +14.14%/MDD 7.77%，altcoin +11.71%/MDD 15.92%；熊市（2025-06→2026-06）large-cap +3.46%/MDD 11.36%，altcoin -10.26%/MDD 23.44%。large-cap 熊市优势显著，两段均有样本，结论 `candidate_keep_review`，可推进 `large_cap_only_risk_off` 实验。
- [x] 做持仓时间过滤实验：新增 `max_holding_30x4h_no_tp1`，入场后 30 根 4h 未触 TP1 则 `TIME_EXIT`；近端 full master A/B 显示净收益 3.32% -> 27.28%、MDD 20.85% -> 11.84%、PF 1.11 -> 1.56，结论 `retest / candidate_keep_review`。
- [x] 跨区间复测 `max_holding_30x4h_no_tp1`，并尝试 18/42 根 4h 两个相邻阈值：三阈值两段全部正向改善，方向稳健，不是过拟合。42根 MDD 最低（近端 9.27%），两段净收益分别 +31.66%/+26.93%，是最平衡候选；18根净收益最高但持仓时间过短；30根近端绝对净收益最高（+27.28%）但 MDD 略高于 42根。结论 `candidate_keep_review`，建议优先考虑 42根。
- [x] 将 `max_holding_42x4h_no_tp1` 与当前 sensitive 组合叠加并完成两段非重叠 walk-forward：两段 PF、Sharpe、净收益均改善，近端 MDD 20.74% -> 11.05%，但较早窗口 MDD 18.03% -> 20.66%，结论 `retest`；95 笔 TIME_EXIT 后续路径更偏向止血，但存在延迟启动赢家，不写入默认配置。
- [x] 完成条件式 42 根相对“无时间退出”的初筛：两段非重叠 walk-forward 均明显改善，但该实验不能回答条件式是否优于固定 42 根。
- [x] 完成固定 42 根 vs 条件式 42 根严格单变量 A/B：早期窗口条件版净收益 31.86% -> 27.57%、PF 1.48 -> 1.38、MDD 20.66% -> 21.04%；近端窗口净收益 15.95% -> 30.75%、PF 1.31 -> 1.64、MDD 11.05% -> 12.40%。结论 `retest`，条件版存在阶段依赖，暂不部署。
- [x] 用 `max_holding_42_fixed_vs_conditional_sensitive` 补更早非重叠窗口 `2023-07-01 -> 2024-07-01`：条件版 Net 38.96% -> 22.26%、PF 1.32 -> 1.20、Sharpe 1.40 -> 0.89、MDD 19.81% -> 20.69%，结论 `reject_candidate`；三窗口中条件版 2 段变差、3 段 MDD 均更高，不部署 `max_holding_bars_conditional=true`。
- [ ] 3 周 paper 观察期结束后，优先评估固定 `max_holding_bars_without_tp1=42` 是否写入默认 `settings.toml`；须先确认 db stability 5 天稳定窗口空闲，并结合模拟盘持仓时长与 TIME_EXIT 案例人工复盘。
- [ ] 如继续研究延迟赢家保留，另开单变量实验：42 根后只有在 price > entry、price > EMA20 且 EMA20 斜率为正时才允许继续持有。
- [x] 设计 large-cap 单独入场规则实验：若市值分层复测确认 large-cap 在弱市仍正收益，新增 `large_cap_only_risk_off` dimension，RISK_OFF 时只允许 BTC/ETH/BNB/SOL 入场，altcoin 全部暂停；需在 `abtest.py` 注册 dimension、`experiments.toml` 加实验定义。实验已完成两段 walk-forward：早期段（2024-07→2025-06）variant net +2.37%→+13.54%（+11.17%），近端段（2025-06→2026-06）variant net +3.12%→-3.12%（-6.24%）。两段方向相反，结论 `retest`；在已有 altcoin 组合上叠加 BNB/SOL RISK_OFF 入场反而在熊市拖累整体，与单独 large-cap 回测结论不一致，暂不 keep。
- [ ] 2026-07-02 模拟盘复盘决策：根据 3 周观察结果（entry_reclaim 拦截次数、RISK_OFF 频率、现有持仓 WLDUSDT/ONDOUSDT 结果）决定 sensitive 组合是 keep、调参还是继续观察。
- [x] 建实验结论索引页：新增 `python main.py experiment-index`，生成 `reports/2026-06-11/experiment_index_2026-06-11_v2.md`。
- [x] 增强实验结论索引页：汇总 `reports/` 中的关键实验，按 `experiment_id` 聚合，输出实验名、时间段、核心变更、结论、`keep/retest/reject`、下一步；`*_review_*.md` frontmatter 覆盖自动 summary，生成 `reports/2026-06-18/experiment_index_2026-06-18_v1.md`。
- [x] 准备 3 周观察仪表：新增 `python main.py observation-dashboard`，并接入 `python main.py daily`，每天输出 `RECLAIM_PENDING` 后续、TP1 EMA trailing、开放持仓时长和 RISK_OFF 今日候选摘要。
- [x] 增强 3 周观察仪表：daily/4h 自动汇总 `RECLAIM_PENDING` 次数与后续、TP1 EMA stop 激活/抬止损/出场统计、开放持仓时长、RISK_OFF 下是否仍产生新计划，并新增 `Run Health`、`Stale Running Run 检测`、`42-bar Holding Review`，确保 2026-07-02 复盘可直接基于证据判断。

## 2026-07-02 后两周观察路线

- [ ] 冻结当前 `settings.toml`，继续 daily + 4h 至少观察 2 周；除非出现明确红线，不修改策略参数或 paper 状态机。
- [x] 新增 opportunity audit 报告：按独立 `plan_id` / `symbol` 统计 `avoided_losers`、`missed_winners`、`false_entries`，尤其不要只按 `RECLAIM_PENDING` 事件次数判断。
- [x] 补 BTC/ETH 正式窗口基准：每个验收窗口输出 BTC/ETH 收益、最大回撤和趋势状态，用于判断策略空仓或亏损是否由市场环境解释。
- [x] 逐笔复盘 8 笔 entered trades：记录入场原因、入场时 `market_regime`、最大浮盈 R、是否接近 TP1、失败原因，并归因为选币、入场、止损、退出或市场问题。
- [x] 2026-07-16 阶段检查已于 2026-07-25 补跑完成：`paper checkpoint` 返回 `formal_audit_ready`，并生成 formal audit、`entry_reclaim_confirm_1bar` shadow replay、`relative_strength_gate` shadow replay；核心证据为 `data_link_verdict=partial_pass`、`config_hash_stable=true`、`daily_success=11/14`、`paper_4h_success=56/70`、`mature=36`、`right_censored_ratio=40.0%`。
- [x] 补强 `paper audit` 规范：已完成样本成熟规则、`right_censored/open_unknown` 标记、`RECLAIM_PENDING` reconciliation、R 倍数反事实 PnL、opportunity funnel 和数据链路一致性检查；旧窗口增强报告已生成至 `reports/2026-07-08/paper_opportunity_audit_2026-06-19_2026-07-02_demo_v5.md`。
- [x] 完成 `entry_reclaim_confirm_1bar` shadow replay MVP：新增 `python main.py paper shadow-replay --variant entry_reclaim_confirm_1bar`，旧窗口报告生成至 `reports/2026-07-08/paper_shadow_replay_entry_reclaim_confirm_1bar_2026-06-19_2026-07-02_demo_v2.md`；仅离线诊断，不修改 live paper 配置。
- [x] 完成 `relative_strength_gate` shadow replay MVP：新增 `python main.py paper shadow-replay --variant relative_strength_gate`，旧窗口报告生成至 `reports/2026-07-08/paper_shadow_replay_relative_strength_gate_2026-06-19_2026-07-02_demo_v1.md`；仅离线诊断，不修改 live paper 配置。
- [x] 准备 2026-07-16 阶段检查 runbook：新增 `2026-07-16-paper-checkpoint-runbook.md`，明确 checkpoint、formal audit、shadow replay、interim report 分流和禁止启动 A/B 的红线。
- [x] 准备 2026-07-16 一键执行脚本：新增 `scripts/run_paper_checkpoint_review.ps1`，先检查 `settings.toml` 无 diff，再运行 checkpoint 严格模式；只有 `formal_audit_ready` 才继续生成 audit 和两个 shadow replay。
- [x] 用增强版 audit 先复核 2026-06-19 -> 2026-07-02 旧窗口，确认新字段能解释旧报告中的 `avoided_loser=25`、`missed_winner=12`、`false_entry=7` 和 `neutral_or_unknown=34`；生成 `reports/2026-07-08/paper_opportunity_audit_2026-06-19_2026-07-02_demo_v2.md`。
- [x] 2026-07-16 阶段检查后决策：暂不启动 `2026-07-06-abtest-plan.md` 中的正式 A/B，也不修改 `settings.toml`；formal audit 显示 `defense_net_R=-24.35`、`missed_winner=11`、`avoided_loser=7`、`false_entry=7`，说明需要先补强离线归因和 opportunity set，而不是直接部署新过滤器。
- [x] 两周后按证据决定下一步实验方向：已补跑 `2026-07-03 -> 2026-07-25` 扩展窗口，`right_censored_ratio` 从 40.0% 降至 21.6%，formal audit 结论为 `review_entry_quality`，下一步优先研究入场/动量/相对强度，不改退出规则。
- [x] GPT 进场方案评审后补强 shadow replay 统计口径：`paper shadow-replay` 已新增 R 汇总、TP1/near-TP1 rate、stop-first rate、source 分层、baseline first-hit 分层和 decision/source 分层；扩展窗口报告已生成至 `reports/2026-07-25/`。
- [x] GPT 进场方案评审后补充 ATR 标准化字段：`OpportunityRow` 已补 `distance_to_support_atr`、`reclaim_margin_atr`、`stop_distance_atr`、`pullback_from_recent_high_atr`，先用于离线报告，不直接改 live/paper。
- [x] GPT 进场方案评审后固定 shadow experiment 的 opportunity set：新增 `paper shadow-experiment`，每次写出固定 JSON 样本和 `opportunity_set_hash`；首轮三个实验均使用 `9468fbe1bab35767`。
- [x] 设计并实现 `reclaim_quality_matrix` 离线实验：首轮扩展窗口报告 `paper_shadow_experiment_reclaim_quality_matrix_2026-07-03_2026-07-25_demo_v2.md`，结论 `retest`；`confirm_1bar` 错过 4 个 winner，`atr_reclaim_0_25` 和 `quality_close` 暂更稳但仍不能部署。
- [x] 设计并实现 `momentum_pullback_definition_ab` 离线实验：首轮扩展窗口报告 `paper_shadow_experiment_momentum_pullback_definition_ab_2026-07-03_2026-07-25_demo_v2.md`，结论 `retest`；`trend_support_atr_pullback` 的 missed winner 最少且 Total Decision R 为正，优先后续复测。
- [x] 设计并实现 `relative_strength_soft_gate` 离线实验：首轮扩展窗口报告 `paper_shadow_experiment_relative_strength_soft_gate_2026-07-03_2026-07-25_demo_v3.md`，结论 `retest`；`btc_eth_soft_minus_0_5` 错过赢家最少，`btc_eth_hard_0` 过滤亏损最多，需继续跨窗口复测。
- [x] 跨窗口复核三项 fixed opportunity shadow experiment：已补跑 `2026-06-19 -> 2026-07-02` 与 `2026-07-17 -> 2026-07-25`，并汇总到 `reports/2026-07-25/paper_shadow_experiment_cross_window_review_2026-07-25_v1.md`；结论仍为 `retest`，优先级暂定 `btc_eth_soft_minus_0_5`、`atr_reclaim_0_25`、`trend_support_atr_pullback`。
- [x] 下一轮正式 A/B 只选择一个维度先做：已注册并运行 `relative_strength_soft_gate_btc_eth_minus_0_5` dynamic-universe A/B；两段非重叠窗口净收益、PF、Sharpe 和止损率均改善，但早期窗口 MDD 16.59% -> 18.96% 恶化，结论 `retest`，不部署。
- [x] 复核 `relative_strength_soft_gate_btc_eth_minus_0_5` 的早期窗口 MDD 恶化来源：variant-only trades 净贡献 +565.32，但 11 月 winner cluster 抬高权益峰值后，12 月、1 月和 5 月新增止损簇扩大 peak-to-trough；结论仍为 `retest`。
- [x] 设计并运行 `relative_strength_soft_gate` 阈值敏感性 A/B：`-1.0` 近端窗口退化，`0.0` 近端最强但早期 MDD 最差，`-0.5` 仍最平衡但不能 keep；结论 `retest`，不部署。
- [x] 下一轮正式单变量 A/B 转向 `reclaim_quality_matrix / atr_reclaim_0_25`：已注册 dynamic-universe A/B 维度并完成两段 walk-forward；不叠加相对强度门槛，结论 `retest`。
- [ ] 暂不把 MACD 升级为 `macd_hist_4h > 0` 硬门槛；如研究 MACD，仅做 histogram 斜率、连续恶化、reclaim 时改善等离线变体。

## 运维待办

- [x] Windows 任务计划 `CryptoTrading_DailyPaperUpdate` 已固定为每天 20:05；2026-06-13 08:38 检查时任务为 `Ready`，最近一次 2026-06-12 20:05:02 成功且 `LastTaskResult=0`，下一次为 2026-06-13 20:05。
- [x] 完成 SQLite 三周观察基础设施与主数据层切换：`runs`、`market_scans`、`paper_plans`、`paper_events`、`paper_snapshots`、WAL、30 秒 timeout、UTC 时间、daily_full run_id、snapshot、db-summary/events/export；`db-summary` 已直接汇总三周核心指标与 daily/4h 北京时间覆盖日期；失败 run 会记录 `run_id`、当前 `step` 和原异常；paper update/report/dashboard 已读取结构化主表，legacy 表仅保留兼容镜像；故障注入测试证明单 plan 的状态、事件和快照原子回滚，且不阻断后续 plan。
- [ ] 从首次新版 `daily_full` 成功运行开始连续观察 5 天，并运行 `python main.py db stability --days 5`；**窗口已于 2026-06-18 重新开始**：2026-06-17 20:05 定时任务启动后未生成 scan、snapshot 或 reports，run `20260617_120503_5c574dad` 已明确标记为 `failed`/缺失样本；用户确认根因为 GPT 会员/用量到期导致的外部执行资源中断，不视为脚本或数据库稳定性缺陷。连续 daily 观察仍从 2026-06-18 起算，需继续跟踪 6/18–6/22 的 daily 样本质量，`config_hash` 应保持 `be7ec39ec21f6a83`。
- [x] 准备并验收 `scripts/paper_4h_update.bat` 与 `scripts/install_4h_paper_task.ps1`：仅运行 `paper cycle`，固定 00:10、04:10、08:10、12:10、16:10，禁止 scan/add-from-scan；设置 30 分钟上限与 `IgnoreNew` 防重入，关闭 `StartWhenAvailable` 防止错过的 4h 任务补跑到 20:05 daily 附近；安装脚本先以普通权限预检 5 天门槛，再要求管理员权限；临时库集成测试确认 cycle 不新增 scan/plan，只更新已有计划并写 run/event/snapshot/report/dashboard。
- [x] 2026-06-18 用户确认 6/17 缺失样本为已知外部用量中断后，提前以 `-RequiredStableDays 1` 在管理员 PowerShell 安装 `CryptoTrading_4H_PaperUpdate`；任务已注册 00:10、04:10、08:10、12:10、16:10 五个触发器，当前 `LastTaskResult=267011` 表示尚未首次运行，下一步观察 2026-06-19 00:10 首轮 4h run 是否成功。

## TODO 维护规则

- 默认使用中文记录 TODO。
- 保留必要英文术语、命令名、配置键和状态值，例如 `BUY_CANDIDATE`、`sample_sufficient`、`python main.py ...`。
- 每条 TODO 必须是可执行动作，不写泛泛想法。
