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
- [x] A/B 测试更强的日线趋势过滤：只允许 `price > EMA20_1d >= EMA50_1d * 0.98` 的币成为买入候选；早期段（2024-07→2025-06）PF 0.91→0.97、净收益略改善，但近端段（2025-06→2026-06）止损率 77%→89%、净收益 -10.62%→-22.71%、MDD 扩大，结论 `reject_candidate`；弱市中趋势恢复后才允许入场反而导致在更高位置接入，质量更差。
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
- [ ] 增强 3 周观察仪表：daily 自动汇总 `RECLAIM_PENDING` 次数、被拦截后是否继续下跌、TP1 EMA stop 激活/抬止损/出场统计、开放持仓时长分布、RISK_OFF 下是否仍产生新计划，确保 2026-07-02 复盘可直接基于证据判断。

## 运维待办

- [x] Windows 任务计划 `CryptoTrading_DailyPaperUpdate` 已固定为每天 20:05；2026-06-13 08:38 检查时任务为 `Ready`，最近一次 2026-06-12 20:05:02 成功且 `LastTaskResult=0`，下一次为 2026-06-13 20:05。
- [x] 完成 SQLite 三周观察基础设施与主数据层切换：`runs`、`market_scans`、`paper_plans`、`paper_events`、`paper_snapshots`、WAL、30 秒 timeout、UTC 时间、daily_full run_id、snapshot、db-summary/events/export；`db-summary` 已直接汇总三周核心指标与 daily/4h 北京时间覆盖日期；失败 run 会记录 `run_id`、当前 `step` 和原异常；paper update/report/dashboard 已读取结构化主表，legacy 表仅保留兼容镜像；故障注入测试证明单 plan 的状态、事件和快照原子回滚，且不阻断后续 plan。
- [ ] 从首次新版 `daily_full` 成功运行开始连续观察 5 天，并运行 `python main.py db stability --days 5`；**窗口已于 2026-06-15 重置**：`b665076` 向 `settings.toml` 加入 `max_holding_bars_conditional = false` 一行，文件字节变化导致 `config_hash` 从 `311322be2029f063` 变为 `be7ec39ec21f6a83`，6/13–14 两天样本作废。新窗口起点为 2026-06-15（1/5），需连续到 2026-06-19 满 5 天，最早安装日期推迟至 **2026-06-20**。下次实验若需改 `settings.toml`，须先等安装完成再改，否则再次重置。
- [x] 准备并验收 `scripts/paper_4h_update.bat` 与 `scripts/install_4h_paper_task.ps1`：仅运行 `paper cycle`，固定 00:10、04:10、08:10、12:10、16:10，禁止 scan/add-from-scan；设置 30 分钟上限与 `IgnoreNew` 防重入，关闭 `StartWhenAvailable` 防止错过的 4h 任务补跑到 20:05 daily 附近；安装脚本先以普通权限预检 5 天门槛，再要求管理员权限；临时库集成测试确认 cycle 不新增 scan/plan，只更新已有计划并写 run/event/snapshot/report/dashboard。
- [ ] 5 天审计返回 `ready_for_4h_task=true` 后，在管理员 PowerShell 运行 `powershell -ExecutionPolicy Bypass -File scripts\install_4h_paper_task.ps1` 安装 `CryptoTrading_4H_PaperUpdate`。

## TODO 维护规则

- 默认使用中文记录 TODO。
- 保留必要英文术语、命令名、配置键和状态值，例如 `BUY_CANDIDATE`、`sample_sufficient`、`python main.py ...`。
- 每条 TODO 必须是可执行动作，不写泛泛想法。
