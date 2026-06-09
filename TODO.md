# CryptoTradingSystem 待办清单

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
- [ ] A/B 测试更强的日线趋势过滤：只允许 `price > EMA20 > EMA50` 的币成为买入候选。
- [ ] A/B 测试趋势相关高波动惩罚：只有在趋势未确认时才对高波动加重扣分。
- [x] 每次 A/B 实验后补一条简短结论：`keep`、`revert` 或 `retest`；当前 dynamic-universe A/B 均通过报告、开发计划和实验日志保留结论。

## Priority 2：优化入场规则

- [ ] 不在第一次触碰入场区间时立刻入场，要求 4h 收盘重新站回支撑。
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
- [ ] 为 `risk_off_no_core_entry_reclaim` 扩大早期样本：优先测试 `2025-01-01 -> 2025-09-01` 之外的更早历史或研究退市 symbol master，确认早期段不是样本不足假象。
- [ ] 设计下一轮 `RISK_ON` 退出 A/B：优先验证 TP1 后保护性退出或更快止损移动，避免继续单纯叠加防守过滤。

## TODO 维护规则

- 默认使用中文记录 TODO。
- 保留必要英文术语、命令名、配置键和状态值，例如 `BUY_CANDIDATE`、`sample_sufficient`、`python main.py ...`。
- 每条 TODO 必须是可执行动作，不写泛泛想法。
