# Handoff — 2026-06-12 00:00 +08:00


## 2026-08-13 00:21 +08:00

### 项目目录

工作目录：`D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects`

这是一个本地 Python 加密货币交易研究系统，当前 Git 分支为 `main`，远程为 `origin/main`。数据库位于 `data/crypto_trading.db`，自动任务日志位于 `logs/`，自动生成的 Markdown/JSON/图表报告位于 `reports/YYYY-MM-DD/`。项目根目录中的主要记忆文件分别承担不同职责：

- `dailylog.md`：工程、配置、项目文档和运行维护的审计日志。
- `TODO.md`：可执行待办，不承担大段研究叙事。
- `开发计划.md`：项目阶段、研究路线和模块状态。
- `EXPERIMENT_LEDGER.md`：仓库内的实验索引和结论。
- Obsidian 文件 `D:\MyNotebook-Obsidian\CryptoTradingSystem\CryptoTrading 实验日志.md`：回测、A/B、paper 和前向研究的详细实验叙事。
- `handoff.md`：跨会话交接记录；本章节是截至本次交接的最新总览，旧章节必须保留为历史记录。

本项目没有得到实盘下单授权。任何 `live` 交易、真实资金部署、自动下单权限配置，都必须另行获得明确批准；当前所有工作属于 research、backtest、paper 或 read-only diagnostics。

### 任务背景

#### 1. 项目总目标

系统的长期目标是建立一个可复核的研究闭环：

`daily 扫盘 -> 生成候选和交易计划 -> 数据质量/市场环境检查 -> paper 跟踪 -> 4h 状态推进 -> 回测/A-B -> 归因复盘 -> 再决定是否研究下一条规则`

项目当前并不是“尽快让某个参数上线”，而是先把策略行为、容量约束、执行时点、退出路径和数据链路记录完整。项目规则要求：每次实验只回答一个主要问题；`retest` 不等于 keep；回测收益改善不自动授权修改 `config/settings.toml`；paper 证据不自动等于实盘授权。

#### 2. 当前研究主线：`atr_reclaim_0_35`

前期 A/B 和离线归因发现，要求 4h 收盘超过 `entry_high + 0.35 * ATR` 的 `atr_reclaim_0_35` 在若干历史窗口中表现较好，但改善来源并不简单：

- common trades 并没有普遍变好；
- 改善的一部分来自 variant-only 新增赢家；
- baseline 错过的部分赢家本身质量并不差；
- `max_active_positions=5`、候选排序、满仓阻挡、旧仓长期占槽等容量路径可能改变最终交易组合；
- 早期/近端窗口表现存在路径依赖，不能仅凭净收益或 PF 判断规则机制已经被证明；
- 旧的 `2023-07-01 -> 2024-07-01` 历史窗口存在 historical universe membership 缺口，N0-N4 产物只保留为 diagnostic evidence，不能作为新的 keep、reject 或 deploy 依据。

因此在 2026-07-30 正式把该规则定位为：

- `provisional_research_incumbent`：当前研究阶段默认的 incumbent，供后续新 challenger 比较；
- 不是 paper deployment；
- 不是 live deployment；
- 不代表 `0.35` 已经得到严格前向验证。

当前必须长期保留三条线：

| 线名 | 含义 | 作用 |
|---|---|---|
| `reference_baseline` | 原策略，不含 `atr_reclaim_0_35` | 判断 `0.35` 相对原策略的直接前向贡献 |
| `atr_reclaim_0_35_shadow` | 原策略加 `0.35`，独立记录，不控制 paper | 长期保留的 `0.35` challenger-like 参照线 |
| `research_incumbent` | 当前研究 incumbent，现阶段等同采用 `0.35` 的研究参照版本 | 后续新 challenger 的默认比较基准 |

如果未来研究新因素，原则上采用：

`new_challenger = research_incumbent + one_new_factor`

每轮只改变一个主要研究维度。新 challenger 研究在当前 shadow gate 未成熟前暂不启动。

#### 3. 六个研究优先级

前向研究不是只为了回答“0.35 是否有效”，还要利用每次 4h 扫描和状态更新产生的全部信息，逐项回答以下六类问题：

1. **候选排序和满仓机会成本**：同一轮有多个合格候选时，为什么进入某个候选而没有进入另一个？被 `max_active_positions` 阻挡的高排名候选，事后是赢家还是亏损？
2. **容量利用和旧仓占槽**：满仓是否经常被长期、低质量、尚未 TP1 的仓位占用？替换一个 stale slot 是否有稳定、可执行的边际收益？此前容量 replacement 分支已因证据集中且不稳定而冻结。
3. **持仓时间和退出路径**：`TIME_EXIT`、TP1、止损、TP2、EMA/ATR trailing 的不同路径怎样影响 slot 释放、延迟赢家和组合结果？固定 `42` 根 4h 的方向曾显示价值，但 paper 前向独立 symbol 样本不足，不能部署。
4. **执行质量和状态一致性**：scanner、entry trigger、4h close reclaim、fill time、同根 K 线 stop/TP、API 延迟、paper state 和 shadow state 是否按同一时点、同一口径记录？
5. **市场状态适应性**：`RISK_ON`、`RISK_OFF`、趋势、波动率、market breadth、signal density 等状态是否改变 `0.35` 的直接过滤贡献、容量路径贡献或退出结果？
6. **后续单变量入场因素**：在现有 incumbent 已有足够证据之后，才研究 entry_low 附近成交、RSI recovery、放量下跌拒绝、4h 下行趋势接飞刀等因素；这些不能在当前未成熟 shadow 阶段随意叠加。

### 已完成的工作

#### A. 研究纪律和历史分支处理

- 已完成 `atr_reclaim_0_35` 的历史回测、阈值敏感性、交易级归因和关键路径复盘。
- `0.10`、`0.15`、`0.25`、`0.35` 的阈值敏感性已经做过；`0.35` 是当前最强候选，但结论保留为 `candidate_keep_review` / `retest_path_dependent`，不是部署批准。
- 已确认不能继续围绕 `0.30 / 0.35 / 0.40` 进行无止境阈值搜索。
- 已完成 `signal_fill_timing_audit` Stage 0，结论为 `timing_audit_warn_same_bar_ambiguity`：当前 replay 在同一次调用里可能让 WATCHING 计划入场后继续评估同根 stop/TP，因此研究报告必须保留 `fill_time_assumption`、same-bar ambiguity 等字段。
- 已完成 `blocked_entry_event_export` Stage 1：canonical run `110c51eef593` 复跑导出 `512` 个 `block_reason=max_active_positions` 事件，`replay_entered_trades=58` 与 source 一致。
- 已完成 `replay_consistency_audit` Stage 2：source/replay entered trades、active path、final equity、blocked event repeat mismatch 均通过；但候选排序不是 source 原生持久化字段，只能通过源码 marker 和重复事件签名间接验证。
- 已完成 `stale_slot_continuation_review` Stage 3：统一 `42 bars = 168h`；26 个合格 stale slots，`forward_R_42_mean=-0.132`，`eventual_continuation_R_mean=-0.129`，说明旧仓继续占槽有弱点，但不等于替换一定有收益。
- 已完成 `blocked_candidate_vs_stale_slot_review` Stage 4：42 个合格比较事件，`net_delta_R_42_mean=0.309` 但 median `-0.223`、positive ratio `42.9%`、20% trimmed mean 约 `0.001`；结果为 `replacement_edge_not_supported`。
- 已完成 `replacement_closure_audit`：Stage 4 样本高度集中于 3 个 stale trades，top1 占 `83.333%`，cluster bootstrap 不能支持稳定 edge；capacity replacement 分支正式冻结为 `paused_no_stable_executable_edge`。
- 已明确不提高 `max_active_positions`，不启动 Stage 5 / Stage E shadow replacement，不修改 `config/settings.toml`。
- 2023-2024 historical universe 修复分支已经停止作为 `0.35` 的强验证路线；不重新打开该窗口，也不以当前 master list 伪装成无幸存者偏差的历史 universe。

#### B. prospective shadow 数据链路

已把研究从“事后只看实际 paper 交易”扩展为“记录每次扫描的候选上下文、每个计划的三线决策，以及被过滤候选的反事实路径”。这正是本项目此前讨论的“充分利用每次 4h 扫描全部信息”的落地版本。

已存在或已增强的核心表/记录：

- `paper_shadow_decisions`：4h plan-linked decision-state 和 daily candidate-level context 的统一研究记录。
- `paper_shadow_candidate_observations`：每个 scan candidate 的候选级观察，包含 rank、score、scanner action、entry/stop/TP、容量和市场状态等上下文。
- `paper_shadow_counterfactual_outcomes`：对候选或计划按 `reference_baseline`、`atr_reclaim_0_35_shadow`、`research_incumbent` 三条线初始化并持续推进的反事实结果。
- `paper_plans`、`paper_events`、`paper_snapshots`：paper 状态机的结构化主表。
- `runs`、`market_scans`：运行链路和 scan 证据。

记录口径已经明确区分：

1. **候选级诊断样本**：同一轮可能有 10 个候选，能够同时研究 rank、score、reclaim margin、market regime、capacity state 等，但候选之间相关，不能把 10 个候选简单当成 10 笔独立交易。
2. **plan-linked decision 样本**：实际进入 paper plan 状态机的机会，在 4h 更新中会记录三条线在同一时点的决策、容量状态、reclaim margin 等；这些才是严格前向三线比较的主要入口。
3. **mature terminal opportunity**：plan-linked opportunity 对应的 paper plan 已到达终端状态，并且满足成熟度定义；这是当前 pre-attribution gate 的关键指标。只有它达到门槛，才开始 direct filtering / capacity/path attribution。
4. **candidate counterfactual terminal outcome**：候选级反事实可能已经达到 stop/TP/TIME_EXIT 等终点，但它仍然可能没有对应真实 `paper_plan`。它适合诊断和扩大标签覆盖，不能直接替换 plan-level mature terminal opportunity。

已实现的行为：

- daily/import 为每个 scan candidate 写三条参照线，而不是只写最终导入 paper 的那一笔。
- 4h update 只读推进候选/计划反事实 outcome，不控制 paper 下单，不改变 `settings.toml`。
- `paper_shadow_0_35` 相关记录不会改变当前 paper plan 的实际入场逻辑。
- 4h 的 `ticker_24hr` 瞬断现在通过 `API_DELAY_SKIPPED` 事件和 snapshot 记录，不再因为单次 SSL/网络失败直接丢掉后续报告链路；这改善可观测性，不是策略变更。
- maturity 和 reconciliation 报告会同时显示 candidate observations、counterfactual outcomes、terminal counterfactual outcomes，避免把不同样本层级混在一起。

相关入口命令：

```powershell
python main.py paper shadow-decisions --limit 100
python main.py paper shadow-candidate-observations --limit 100
python main.py paper shadow-counterfactual-outcomes --limit 100
python main.py paper shadow-maturity --no-obsidian
python main.py paper shadow-reconciliation --no-obsidian
```

#### C. 严格 pre-attribution gate

`paper shadow-reconciliation` 已经把最小归因门槛代码化：

| 要求 | 最低值 | 当前值（2026-08-13） | 状态 |
|---|---:|---:|---|
| complete opportunities | 10 | 41 | 通过 |
| mature terminal opportunities | 5 | 0 | 未通过 |
| independent symbols | 3 | 19 | 通过 |
| `controls_paper` rows | 0 | 0 | 通过 |
| incomplete opportunities | 0 | 0 | 通过 |

因此当前 verdict 仍是：

- maturity：`decision_samples_not_mature`
- reconciliation：`reconciliation_waiting_for_terminal_outcomes`
- 不能开始 `0.35` direct filtering contribution 解释。
- 不能开始 capacity/path contribution 的正式归因。
- 不能把 `0.35` 升级为 paper deployment。

#### D. 当前真实前向样本状态

截至 2026-08-13 00:15 左右最新报告 `reports/2026-08-13/paper_shadow_maturity_review_2026-08-13_demo_v2.md` 和 `reports/2026-08-13/paper_shadow_reconciliation_2026-08-13_demo_v1.md`：

- `decisions=219`
- `opportunities=41`
- `candidate-only rows=120`
- `plan-linked decision rows=99`
- `complete opportunities=41`
- `incomplete opportunities=0`
- `controls_paper rows=0`
- `mismatch opportunities=0`
- `independent symbols=19`
- `candidate observations=20`
- `counterfactual outcomes=60`
- `terminal counterfactual outcomes=6`
- `mature terminal opportunities=0`
- `right-censored open rows=99`
- `right-censored ratio=100.00%`（对当前 plan-linked rows 而言）

当前只有一个 plan-linked open opportunity：

- plan id：`9734a33dea2e`
- symbol：`ONDOUSDT`
- status：`WATCHING`
- entry_low：`0.394505`
- entry_high：`0.41156785714285715`
- 最新 shadow decision 覆盖三条线，三线都没有 accepted entry；这是同一观察机会的三线同步记录，不是 99 个独立交易机会。

为什么 `mature terminal opportunities` 仍是 0：

- 目前所有 `paper_shadow_decisions` 的 plan-linked rows 都挂在 ONDOUSDT 这个仍为 `WATCHING` 的计划上。
- ONDOUSDT 多次产生的是 `RECLAIM_PENDING_SET` 或等待状态，4h close 没有站回 `entry_high`，因此没有进入 `ENTERED`，也没有 `STOPPED`、`TP1_HIT`、`CLOSED`、`INVALIDATED` 等终端状态。
- 计划一直未终结，所以严格 maturity 逻辑只能把这些 rows 标成 `right_censored_open`。
- 候选级反事实已经有 6 条终端结果，但候选没有形成对应的 plan-level terminal opportunity，不能直接满足 gate。
- 这不是“数据库没有记录”或“4h 没有运行”，而是严格样本定义要求观察对象完成，而唯一 plan-linked 对象还没有完成。

#### E. 4h 和 daily 自动化

当前 Windows 任务通过统一入口 `scripts/run_logged_paper_task.ps1` 运行：

- daily 任务：`CryptoTrading_DailyPaperUpdate`
- daily 时间：每天北京时间 `20:05`
- daily 内容：扫描、导入候选、更新 paper、生成报告/dashboard、写入候选级 shadow context、推进可推进的反事实并生成 maturity/reconciliation 报告。
- 4h 任务：`CryptoTrading_4H_PaperUpdate`
- 4h 时间：北京时间 `00:10`、`04:10`、`08:10`、`12:10`、`16:10`
- 4h 内容：只推进已有 paper plan 和 shadow state，不执行新的 scan，不执行 `add-from-scan`。
- daily `20:05` 负责覆盖 20:00 收盘后的日常处理；下一次 4h 是 `00:10`。

任务安装和运维特征：

- `WakeToRun=True`
- `StartWhenAvailable=True`
- 错过触发时间后尽快运行
- 失败后每 5 分钟重试，最多 3 次
- `MultipleInstances=IgnoreNew`
- 4h 单次上限约 30 分钟
- daily 单次上限约 2 小时
- 4h 不扫描、不增加 plan，避免和 daily 产生职责重叠。

截至本次检查：

- `CryptoTrading_4H_PaperUpdate`：2026-08-13 00:10 最近运行成功，`LastTaskResult=0`，下一次 `04:10`。
- `CryptoTrading_DailyPaperUpdate`：最近一次显示为 2026-08-11 20:05，`LastTaskResult=0`，`NumberOfMissedRuns=1`；这需要新会话继续核对 8/12、8/13 daily 是否有数据库 run 或日志证据，但不应凭任务元数据直接判定样本丢失。
- 数据库最新成功 run：`20260812_161003_81857d77`，类型 `paper_4h_update`，配置 hash `be7ec39ec21f6a83`，Git commit `761114a2198878e4376a08c6c91f3c0c24bbcb1b`。
- 数据库最新失败 run：`20260808_120503_c29c4076`，类型 `daily_full`，失败阶段为 scan，原因是 Binance SSL EOF；这属于网络失败，不是策略失败。
- 当前 `open_plan_count=1`。

#### F. 最近关键提交和文件状态

最近相关提交：

- `6c720df Add paper shadow candidate outcomes`：新增候选观察和反事实 outcome 数据链路。
- `4374851 Record atr reclaim Aug 5 shadow progress`：记录真实 daily/import 的候选级样本增长。
- `4edb503 Unify scheduled paper task entrypoint`：统一 daily/4h 计划任务入口。
- `e991858 Record scheduled task entrypoint commit hash`：记录统一入口提交关系。
- `80e0cbd Record Aug 6 automatic 4h reports`：纳入自动 4h 报告。
- `6cc77a2 Document sleep wake task operations`：记录唤醒运行和计划任务操作。
- `6a2bfc5 Record sleep wake operations commit hash`：记录相关操作提交。
- `761114a Record Aug 12 project status review`：截至 8/12 的状态审查、报告归档和 TODO 更新。

本次交接开始时工作区唯一未跟踪内容是 `reports/2026-08-13/`，里面包含 00:10 自动 4h 报告，以及本次只读 maturity/reconciliation 报告。它们应和本次文档/日志提交一起纳入 Git；`data/crypto_trading.db` 不应提交。

### 尚未完成的事项

#### P0：前向 shadow gate 尚未通过

- [ ] 等待 `paper_plan:9734a33dea2e` 或后续新的 plan-linked opportunities 进入终端 paper 状态。
- [ ] 使严格的 `mature terminal opportunities` 从 `0` 达到至少 `5`。
- [ ] 保持至少 `3` 个独立 symbol；当前已有 19，不是当前瓶颈。
- [ ] 保持 complete opportunities、三线齐全、`controls_paper=0`、incomplete=0；当前均正常。
- [ ] 成熟度达到后重新运行 `paper shadow-reconciliation`，确认 verdict 变为 `reconciliation_ready_for_attribution`。
- [ ] 在 gate 未通过前，不解释 `0.35` 的直接过滤收益，不下结论说它优于 baseline，也不把它升级为 paper deployment。

#### P1：gate 通过后的第一轮只读归因

达到 gate 后，只允许先做归因，不允许立即改配置。顺序建议如下：

1. 对 `reference_baseline` vs `atr_reclaim_0_35_shadow` 做 direct filtering attribution：统计 `filtered_loser`、`missed_winner`、同一 opportunity 的 first-hit/terminal outcome、实现 R、MFE、MAE。
2. 单独拆 direct filter contribution 与 capacity/path contribution：不能把因容量导致的不同入场顺序算成 `0.35` 过滤本身的收益。
3. 按 `candidate_rank`、`reclaim_margin_atr`、`capacity_state`、`scanner_action`、`market_regime`、`signal_density`、`active_positions`、`time_in_position` 分层。
4. 检查 symbol、月份、市场状态集中度，避免 5 个 terminal opportunity 全部来自一个币或一个行情阶段。
5. 检查 right-censoring、API delay、same-bar ambiguity、数据缺失和状态不一致；任何异常都先标记为数据问题，不直接归因于策略规则。
6. 形成“非技术结论 + 技术证据 + keep/retest/reject/insufficient evidence”三层报告。

#### P1：候选级数据如何使用

- [ ] 继续让 daily 保存每个候选的 rank、score、scanner action、entry/stop/TP、ATR、市场状态、capacity state 等字段。
- [ ] 继续让 4h 只读推进被过滤候选的 counterfactual path。
- [ ] 核对 candidate-level terminal outcomes 是否能形成足够广泛的诊断证据，尤其是 `0.35` 拒绝但 baseline 可能入场的候选。
- [ ] 候选级结果只能作为诊断和标签扩展，最终统计要标注候选相关性，不能和独立组合级交易样本混合计算置信度。
- [ ] 如发现候选已终结而 plan 没有 plan-linked outcome，先审计数据关联和样本定义，再决定是否需要代码修复；不能为了让 gate 通过而放宽定义。

#### P2：容量/排序研究仍未完成

- [ ] 等严格 shadow gate 通过后，研究满仓阻挡的机会成本：每次记录 rank、阻挡原因、active slots、被阻挡候选后续 R、替代旧仓后续 R。
- [ ] 先使用已有 `blocked_entry_event_export`、`replay_consistency_audit` 和 `stale_slot_continuation_review` 的口径，不直接修改 `max_active_positions`。
- [ ] capacity replacement 分支当前是 `paused_no_stable_executable_edge`，不能未经新计划重新开启。
- [ ] 如果未来重启，必须先提出事前确定的 slot selection 规则，并用更广泛、去聚类的 walk-forward 样本验证；不能使用 oracle 规则或事后挑选最差旧仓。
- [ ] 新 challenger 方向暂定为 candidate ranking / full-capacity opportunity cost，但应等 shadow logging/reconciliation 稳定后再正式开始。

#### P2：退出和持仓时间研究仍未完成

- [ ] `max_holding_bars_without_tp1=42` 的历史和组合回测方向较好，但 paper 前向只出现过 3 个超过 42 根 4h 的 terminal cases，且仅 2 个独立 symbol，结论是 `defer_keep_review_insufficient_forward_evidence`。
- [ ] 继续 daily + 4h 观察，目标至少 5 个独立 symbol 或 8-10 个 over-42h terminal cases 后，再重开 42-bar keep review。
- [ ] 尚未完成 TP1 部分止盈、TP1 后保本、EMA20 trailing、ATR trailing、固定 TP2 vs 趋势退出、ATR 动态止损等正式单变量实验的最终 keep/revert 决策。
- [ ] 任何退出实验都要注意它同时改变持仓时长、容量释放和后续候选机会，必须单独拆解退出收益和容量路径收益。

#### P2：后续入场因素仍未完成

以下属于未来单变量研究，不是当前立即改配置的 TODO：

- [ ] 测试更靠近 `entry_low` 的入场方式，而不是默认按 `entry_high` 附近成交。
- [ ] 测试 RSI 从 45-55 区间恢复向上的条件。
- [ ] 拒绝主要由放量下跌驱动的形态。
- [ ] 避免 4h 趋势仍明显向下时接飞刀。
- [ ] 更严格追高排除/降级。
- [ ] 只有在 incumbent 前向证据稳定后，才选择其中一个方向做新的 `new_challenger`。
- [ ] MACD 暂不升级为 `macd_hist_4h > 0` 硬门槛；若研究 MACD，只做 histogram 斜率、连续恶化、reclaim 时改善等离线变体。

#### P3：回测基础设施待办

- [ ] K 线缓存足够热后，不使用 `--source-limit` 跑更大 dynamic-universe A/B。
- [ ] 继续研究 Binance 历史/退市币 symbol master，降低当前 `exchangeInfo` master 带来的 survivorship bias。
- [ ] 保持固定 symbol universe、日期区间、配置 hash 和单变量变更纪律。
- [ ] 所有实验报告保留 trades、closed_trades、胜率、PF、平均 R、止损率、Sharpe、MDD、净收益和 `sample_sufficient`。
- [ ] `closed_trades < 20` 的结果只能标为样本不足，不能作为 keep 依据。

#### P4：运维和数据链路待办

- [ ] 新会话首先核对 `CryptoTrading_DailyPaperUpdate` 的 8/12、8/13 实际 DB run、日志和报告，解释 `NumberOfMissedRuns=1` 是否是真缺失、任务元数据滞后，还是正常错过后补跑。
- [ ] 持续观察 4h/daily 是否维持 `LastTaskResult=0`，以及是否产生新的 `API_DELAY_SKIPPED`、SSL 或超时错误。
- [ ] 如果网络错误再次出现，先保留失败 run 和错误阶段，不手动补造研究样本；按运行日志决定是否需要运维修复。
- [ ] 任何脚本/代码/配置/项目文档改变后，必须更新 `dailylog.md`；如果 TODO 或 roadmap 改变，同步更新 `TODO.md` / `开发计划.md`；如果产生实验判断，更新 Obsidian 实验日志。
- [ ] 任何项目文件变更后创建 Git commit 并 push 到 `origin`；staging 时必须包含 `reports/`，但不要提交 `data/crypto_trading.db`。

### 下一步直接执行指令

新会话打开后，先在项目目录执行以下命令。它们都是只读检查，不会制造 paper 样本，也不会改变策略配置：

```powershell
Set-Location 'D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects'
git status --short --branch
python main.py db status
python main.py paper shadow-maturity --no-obsidian
python main.py paper shadow-reconciliation --no-obsidian
python main.py paper shadow-decisions --limit 30
python main.py paper shadow-candidate-observations --limit 30
python main.py paper shadow-counterfactual-outcomes --limit 30
Get-ScheduledTaskInfo -TaskName 'CryptoTrading_4H_PaperUpdate' | Select-Object TaskName,LastRunTime,LastTaskResult,NextRunTime,NumberOfMissedRuns
Get-ScheduledTaskInfo -TaskName 'CryptoTrading_DailyPaperUpdate' | Select-Object TaskName,LastRunTime,LastTaskResult,NextRunTime,NumberOfMissedRuns
```

然后做以下顺序核对：

1. 以最新 `paper_shadow_reconciliation` 的 Summary 和 Pre-Attribution Gate 为准，不以旧报告或 `TODO.md` 中早期数字为准。
2. 确认当前是否仍只有 `paper_plan:9734a33dea2e / ONDOUSDT` 一个 plan-linked opportunity。
3. 查看最新 daily/4h run 的 `status`、`step`、`error_message`、`config_hash` 和 `git_commit`。
4. 如果发现新 terminal plan，重新检查三线是否齐全、是否 `controls_paper=0`、是否存在 incomplete/mismatch。
5. 若 gate 仍未通过，继续等待正常任务，不手动运行 daily/cycle 来“制造”机会，不运行新的近端 `0.35` A/B。
6. 若 gate 已通过，只生成只读 attribution 报告，先不要修改 `config/settings.toml`、`max_active_positions` 或 paper 状态机。

如需进一步核对 ONDOUSDT 的具体状态，可以使用下面的只读 SQL 检查；不要通过 SQL 修改数据库：

```powershell
@'
import sqlite3
from pathlib import Path

db = Path("data/crypto_trading.db")
con = sqlite3.connect(db)
con.row_factory = sqlite3.Row
for row in con.execute("""
    SELECT plan_id, symbol, status, created_at, updated_at,
           entry_low, entry_high, source_scan_id, source_rank
    FROM paper_plans
    WHERE plan_id = '9734a33dea2e'
"""):
    print(dict(row))
con.close()
'@ | python -
```

如果需要检查最近运行是否有真正缺失，优先查看：

```powershell
Get-Content -LiteralPath 'logs\daily_paper_update.log' -Tail 160
Get-Content -LiteralPath 'logs\paper_4h_update.log' -Tail 160
Get-ChildItem -LiteralPath 'reports\2026-08-13' -Force | Sort-Object LastWriteTime
```

### 重要声明

- 当前研究阶段是“等待 terminal outcomes”，不是“已经证明 `0.35` 优于其他因子”。
- `mature terminal opportunities=0` 的含义是严格的 plan-level 观察对象尚未终结，不是说系统完全没有数据，也不是说 candidate-level 反事实没有任何终端结果。
- 当前 `terminal counterfactual outcomes=6` 与 `mature terminal opportunities=0` 可以同时成立；前者是候选/反事实层，后者是严格 plan-linked gate 层。
- `decisions=219` 也不等于 219 笔独立交易；其中 120 条是候选级记录，99 条是同一个 ONDOUSDT plan-linked opportunity 在多个 4h 时点的重复决策观察。
- 当前 4h/daily 脚本的主要任务是保证数据自然积累和状态可审计，不是主动提高交易频率。把 4h 改成 2h 不是当前优先级。
- 不要为了让成熟度门槛通过而放宽 terminal 定义、把候选样本伪装成 plan 样本、删除 right-censored rows、手动制造 plan 或补造交易。
- 不要修改 `config/settings.toml`，不要把 `atr_reclaim_0_35` 直接接管 paper，下单或实盘都不在授权范围内。
- 不要重新开启 `2023-2024` historical repair branch，不要开始新的近端历史 `0.35` A/B，不要继续做无目标的 ATR 阈值搜索。
- 不要修改 `max_active_positions=5`。capacity replacement 已明确为 `paused_no_stable_executable_edge`，若要重启必须先提出新的单独研究计划和批准标准。
- 如果新会话要提出实验，必须先说明：系统级目标、唯一问题、所属研究优先级、事实/观察/假设/决策的区分、支持/拒绝/证据不足的判定标准，以及是否允许修改配置。
- 所有真实资金风险保持关闭。`paper` 也只是研究观察，不应被描述成实际交易表现。





## 2026-07-30 12:26 +08:00

### ????
`D:\OneDrive - whut.edu.cn\??\CryptoTradingPorjects`

### ????
???????? `2023-07-01 -> 2024-07-01` ??????? N2-N4 ??? historical universe ?????????????????????

### ??????
- ?? `reports/2026-07-30/atr_reclaim_2023_2024_window_abandonment_decision_2026-07-30_v1.md`????? `abandon_2023_2024_window_for_atr_reclaim_validation`?
- ?? `reports/2026-07-30/atr_reclaim_next_action_plan_2026-07-30_v1.md`??? Stage A-E ?????
- ?? `reports/2026-07-30/atr_reclaim_recent_window_eligibility_audit_plan_2026-07-30_v1.md`????????????????? A/B ???
- ?? `reports/2026-07-30/atr_reclaim_prospective_shadow_observation_plan_2026-07-30_v1.md`??? prospective shadow observation schema?
- ??? `dailylog.md`?`TODO.md`?`EXPERIMENT_LEDGER.md`?`????.md` ? Obsidian ?????

### ???????
- ????/?????????
- ?????? recent-window eligibility audit?
- ???? prospective shadow logger?

### ?????????
```powershell
git status --short
git add dailylog.md TODO.md EXPERIMENT_LEDGER.md ????.md handoff.md reports/
git commit -m "Record atr reclaim validation reset plan"
git push origin main
```

### ????
- `atr_reclaim_0_35_status=experimental_candidate_unvalidated`?
- ??? 2023-2024 historical universe???? corrected N1??? path fork audit?
- ??? `config/settings.toml`???? `atr_reclaim_0_35`???? `max_active_positions`?
- ???????????? recent-window eligibility audit ? prospective shadow logger ??????? A/B?

## 2026-07-30 11:44 +08:00

### ????
`D:\OneDrive - whut.edu.cn\??\CryptoTradingPorjects`

### ????
???????? N3 ???????????????? historical membership ????? source-backed historical master ?????????? `atr_reclaim_0_35` ????????

### ??????
- ?? `scripts/n4_historical_master_mvp.py`?
- ?? N4??? `reports/2026-07-30/atr_reclaim_stage_n4_historical_master_mvp_2026-07-30_v1.md`?`*_master_v1.json`?`*_review_queue_v1.json`?`*_raw_v1.json`?
- ?????total rows `413`?`active_current_master=266`?`excluded_by_strategy_universe_rule=20`?`historical_standard_gap_requires_mapping=127`?
- verdict=`historical_master_mvp_built_validation_blocked`?
- ??? `dailylog.md`?`TODO.md`?`EXPERIMENT_LEDGER.md`?`????.md` ? Obsidian ?????
- ??????`python -m compileall scripts\n4_historical_master_mvp.py`?`python tests\test_universe.py`?

### ???????
- ?? commit/push?
- 127 ? blocking review queue ??? official/source-backed mapping?
- N4 MVP ??????? A/B?

### ?????????
```powershell
git status --short
git add scripts/n4_historical_master_mvp.py dailylog.md TODO.md EXPERIMENT_LEDGER.md ????.md handoff.md reports/
git commit -m "Add atr reclaim N4 historical master MVP"
git push origin main
```

### ????
- ???? third-window corrected N1???????????
- ???? `atr_reclaim_0_35`????? `config/settings.toml`????? `max_active_positions`?
- ???? official-source mapping pipeline?

## 2026-07-30 11:36 +08:00

### ????
`D:\OneDrive - whut.edu.cn\??\CryptoTradingPorjects`

### ????
????? N2 ????????????????? `atr_reclaim_0_35` ???? `2023-07-01 -> 2024-07-01` ??????????????????????????????? historical membership ?????????

### ??????
- ?? `scripts/n3_historical_membership_dataset.py`??? N2 ? historical/current JSON??? historical membership dataset MVP?
- ?? N3??? `reports/2026-07-30/atr_reclaim_stage_n3_historical_membership_dataset_2026-07-30_v1.md`?
- ?????`missing_from_current_master=147`??? `excludable_missing_count=20`?`standard_gap_count=127`?`standard_gap_ratio_pct=32.32%`?
- ?? gate decision `reports/2026-07-30/atr_reclaim_stage_n3_gate_decision_2026-07-30_v1.md`??? `third_window_not_recoverable_without_historical_master`?
- ??? `dailylog.md`?`TODO.md`?`EXPERIMENT_LEDGER.md`?`????.md` ? Obsidian `CryptoTrading ????.md`?
- ??????`python -m compileall scripts\n3_historical_membership_dataset.py`?`python tests\test_universe.py`?

### ???????
- ???? commit/push?????????
- ???? source-backed historical master?N3 ?? MVP ???
- 127 ? standard-like missing symbols ????????? `delisting / rename / migration / tradable_to / source / confidence`?

### ?????????
```powershell
git status --short
git add scripts/n3_historical_membership_dataset.py dailylog.md TODO.md EXPERIMENT_LEDGER.md ????.md handoff.md reports/
git commit -m "Add atr reclaim N3 historical membership gate"
git push origin main
```

### ????
- ???????? corrected N1???????????N3 ?????????????????
- ???? `atr_reclaim_0_35`????? `config/settings.toml`????? `max_active_positions`?
- ????? source-backed historical master???????????

## 2026-07-30 00:57 +08:00

### ????
`D:\OneDrive - whut.edu.cn\??\CryptoTradingPorjects`

### ????
?????? N2-A / N2-B / ?? N0 / ???????? / ? gate ?????? N1 ????????????? `atr_reclaim_0_35` ????? `2023-07-01 -> 2024-07-01` ??????

### ??????
- ?? `scripts/n2_universe_audit.py`??? current master listing date?local kline coverage?Binance public-data historical membership ???
- ?? N2????? `reports/2026-07-30/atr_reclaim_stage_n2_universe_audit_2026-07-30_v2.md`?verdict=`diagnostic_only_historical_membership_gap`?
- ?????418 ? current master symbols ???? listing date?`listed_after_window=152`?`listed_inside_window=49`?`full_window_coverage=208`?`partial_window_coverage=9`???? historical USDT symbols `413`??? `147` ??? current master?
- ?? `reports/2026-07-30/dynamic_master_full_listing_enriched_2026-07-30_v2.json` ?? N0??? `reports/2026-07-30/atr_reclaim_n0_readiness_audit_2026-07-30_v1.md`?verdict=`n0_conditional_pass_with_alignment_warning`?
- ?? gate decision ?? `reports/2026-07-30/atr_reclaim_stage_n2_gate_decision_2026-07-30_v1.md`??? `third_window_diagnostic_only_do_not_rerun_n1`?
- ??? `dailylog.md`?`TODO.md`?`EXPERIMENT_LEDGER.md`?`????.md` ? Obsidian `CryptoTrading ????.md`?
- ??????`python -m compileall scripts\n2_universe_audit.py`?`python tests\test_universe.py`?

### ???????
- ???? commit/push??????????
- ?????? N1???? N2 gate failed????? historical membership ?????
- ??????????????
- ????????? historical symbol membership dataset?

### ?????????
```powershell
git status --short
git add .gitignore scripts/n2_universe_audit.py dailylog.md TODO.md EXPERIMENT_LEDGER.md ????.md reports/
git commit -m "Add atr reclaim N2 universe gate audit"
git push origin main
```

### ????
- ???? `atr_reclaim_0_35`????? `config/settings.toml`????? `max_active_positions`?
- N0 ? conditional pass ????? master + local kline readiness ?????????? historical membership ???????? N2-B gate ???
- `reports/2026-07-30/.n2_cache/` ??? `.gitignore`???????????
- 2026-07-30 00:10 ????? paper ???? `reports/2026-07-30/`??????? reports ?????

## 项目目录

`D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects`

- **Git 远端**：`https://github.com/Goodyenough/wbj-CryptoTrading.git`
- **当前分支**：`main`
- **最新已 push commit**：`d45b609`
- **运行环境**：Windows 11 Pro，PowerShell，Python，SQLite
- **数据库**：`data/crypto_trading.db`（SQLite，**两段回测必须串行**）

---

## 任务背景

当前处于"策略质量优化"阶段。sensitive 组合（`risk_off_core_buy=false` + `entry_reclaim_close=true` + `tp1_ema_trailing_stop=true` + BTC -3% / ETH -5% / `require_both_trend=true`）已于 2026-06-11 写入 `settings.toml` 并在模拟盘生效，观察期至 **2026-07-02**。

本次 session 的主要工作：市值分层两段 walk-forward、max_holding 三阈值两段 walk-forward、实现并运行 `large_cap_only_risk_off` 实验。

---

## 已完成的工作

| 内容 | commit / 状态 |
|---|---|
| 市值分层 2024-07→2025-06 早期段：large-cap +14.14%/MDD 7.77%，altcoin +11.71%/MDD 15.92% | `d45b609` |
| max_holding 三阈值（18/30/42根）两段全部改善，42根最平衡（近端 MDD 9.27%，net +26.93%） | `d45b609` |
| 实现 `risk_off_large_cap_buy_enabled` 字段（`config.py`、`scanner.py`、`replay.py`）| `d45b609` |
| 注册 `large_cap_regime` dimension，新增 `large_cap_only_risk_off` 实验 | `d45b609` |
| `large_cap_only_risk_off` 两段 walk-forward：早期 +11.17%，近端 -6.24%，结论 `retest` | `d45b609` |
| dailylog、TODO、开发计划、实验日志全部更新 | `d45b609` |
| experiments.toml 新增 `max_holding_18x4h_no_tp1` 和 `max_holding_42x4h_no_tp1` 定义 | `d45b609` |

---

## 尚未完成的事项

### 1. 2026-07-02 模拟盘复盘决策（主线，等待观察期结束）

届时检查：entry_reclaim 拦截次数、RISK_OFF 频率、WLDUSDT/ONDOUSDT 持仓结果，决定 sensitive 组合是否 keep。观察期结束后再一起决定下一步实验方向。

### 2. `sensitive + max_holding_42x4h` 组合实验（等观察期结束后再做）

**不着急，等 2026-07-02 复盘后再推进。**

当前准备工作已完成：
- `abtest.py` 已注册 `combined_regime_entry_exit_sensitivity_holding` dimension（commit `6cab41d`）
- `experiments.toml` 尚未添加实验定义（留待观察期结束后补）

届时在 `experiments.toml` 末尾添加：

```toml
[sensitive_max_holding_42x4h]
enabled = true
description = "Sensitive combo (6 params) + max_holding_42x4h: validate that time-based exit still improves on top of sensitive defaults."
dimension = "combined_regime_entry_exit_sensitivity_holding"

[sensitive_max_holding_42x4h.overrides.analysis]
risk_off_core_buy_enabled = false
entry_reclaim_close_enabled = true
tp1_ema_trailing_stop_enabled = true
regime_btc_7d_drop_pct = -3.0
regime_eth_7d_drop_pct = -5.0
regime_require_both_trend = true

[sensitive_max_holding_42x4h.overrides.backtest]
max_holding_bars_without_tp1 = 42
```

然后串行跑两段 A/B（`2024-07-01 -> 2025-06-01` 和 `2025-06-01 -> 2026-06-01`），使用 `reports/2026-06-09/dynamic_master_full.json`，`--max-symbols 40`。

---

## 重要声明

1. **SQLite 单写**：两段 A/B 必须串行，不能并行跑。
2. **symbol master**：所有回测使用 `reports/2026-06-09/dynamic_master_full.json`（418 个币）。
3. **实验新增 dimension 必须先在 `abtest.py` 的 `ALLOWED_OVERRIDE_PATHS` 里注册**，否则运行时报错。`combined_regime_entry_exit_sensitivity_holding` 已注册（未 commit）。
4. **`daily_trend_required` 已 reject**，不要在新实验里复用。
5. **`large_cap_only_risk_off` 已 retest**：近端熊市反而变差，不要 keep，不要继续推进参数叠加方向。
6. **当前未 commit 的文件**：`src/crypto_trading_system/abtest.py`（已加新 dimension）、`TODO.md`、`scripts/install_daily_task.ps1`——下次 session 完成 experiments.toml 添加后一起 commit。
7. **定时任务**：`CryptoTrading_DailyPaperUpdate` 每天 20:05 自动执行，但当前触发时间仍是 09:00，需要管理员权限运行 `powershell -ExecutionPolicy Bypass -File scripts\install_daily_task.ps1` 修正。

---

# Handoff — 2026-06-11 18:00 +08:00


## 项目基本信息

- **项目目录**：`D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects`
- **Git 远端**：`https://github.com/Goodyenough/wbj-CryptoTrading.git`
- **当前分支**：`main`
- **最新 commit**：`0ac8f74` (已 push 到 origin/main)
- **运行环境**：Windows 11 Pro，PowerShell，Python，SQLite
- **数据库**：`data/crypto_trading.db`（SQLite，单文件，**不支持并发写入，两段回测必须串行**）

---

## 系统架构概览

```
main.py                          # 入口，子命令：scan / daily / backtest / abtest / paper 等
config/
  settings.toml                  # 生产配置（当前已激活 sensitive 组合）
  experiments.toml               # A/B 实验定义，所有 variant 参数在此声明
src/crypto_trading_system/
  config.py                      # Settings dataclass，load_settings()
  scanner.py                     # 市场扫描，输出 BUY_CANDIDATE
  market_regime.py               # classify_market_regime()，判断 RISK_ON/NEUTRAL/RISK_OFF
  paper_trader.py                # 模拟盘：add_from_scan / update_paper_trades / generate_paper_report
  trade_state.py                 # 单笔交易状态机：step_trade()
  abtest.py                      # A/B 实验框架，ALLOWED_OVERRIDE_PATHS 白名单
  backtest/replay.py             # 回测主循环
  backtest/runner.py             # 回测入口
  indicators.py                  # ema(), percent_change() 等
  models.py                      # PaperTrade, PaperTradeEvent dataclass
  storage.py                     # DB schema，建表语句
reports/                         # 每日报告输出目录（按日期子目录）
scripts/
  daily_paper_update.bat         # 每天 20:05 定时执行：scan→add-from-scan→update→report
logs/
  daily_paper_update.log         # 定时任务日志
```

---

## 当前生产配置（settings.toml [analysis] 关键字段）

```toml
risk_off_core_buy_enabled = false       # RISK_OFF 时不开新 BTC/ETH 多单
entry_reclaim_close_enabled = true      # 进入 entry zone 后须 4h 收盘确认才入场
tp1_ema_trailing_stop_enabled = true    # TP1 命中后用 4h EMA20 跟踪止损
regime_btc_7d_drop_pct = -3.0          # BTC 7日跌幅阈值（旧值 -5.0）
regime_eth_7d_drop_pct = -5.0          # ETH 7日跌幅阈值（旧值 -8.0）
regime_require_both_trend = true        # BTC+ETH 必须同时 price>EMA20>EMA50 才算趋势确认
```

这六个参数合称 **sensitive 组合**（`risk_off_no_core_entry_reclaim_ema_stop_sensitive`），于 2026-06-11 写入 settings.toml，模拟盘当日起生效。

---

## 实验历史与结论（按时间顺序）

### 1. tp1_ema20_trailing_stop（单项）
- 结论：retest，单独使用效果有限，近端 MDD 上升

### 2. risk_off_no_core_entry_reclaim_ema_stop（三项组合）
- 三项：`risk_off_core_buy=false` + `entry_reclaim_close=true` + `tp1_ema_trailing_stop=true`
- 早期段 2024-07→2025-06：PF 0.91→1.53，净收益 -5.6%→+16.7%，MDD 18.7%→15.0%
- 近端段 2025-06→2026-06：PF 0.73→1.05，净收益 -10.6%→+1.2%，MDD 24.2%→18.7%
- **verdict：candidate_keep_review**

### 3. daily_trend_required（单项 + 四项组合）
- 单项 reject：近端段止损率 77%→89%，净收益 -10%→-23%
- 四项组合 reject：近端段止损率 77%→92%，净收益 -14%→-7.8%（不如三项组合）

### 4. regime_sensitive（仅收紧阈值）
- BTC -5%→-3%，ETH -8%→-5%，require_both_trend=true
- 单独使用方向改善但仍亏损，需配合出入场规则

### 5. risk_off_no_core_entry_reclaim_ema_stop_sensitive（三项 + 收紧阈值，当前主候选）

四段 walk-forward 完整结果：

| 段 | 市场环境 | baseline 净收益 | variant 净收益 | PF | MDD |
|---|---|---:|---:|---:|---:|
| 2024-07→2025-01 | 牛市 | +2.4% | **+25.4%** | 2.52 | 9.0% |
| 2024-07→2025-06 | 牛+震荡 | -14.3% | **+18.0%** | 1.58 | 15.0% |
| 2025-01→2025-06 | 震荡转熊⚠ | -19.7% | **-6.5%** | 0.53 | 10.0% |
| 2025-06→2026-06 | 熊市 | -14.2% | **+5.5%** | 1.17 | 17.8% |

⚠ 2025-01→2025-06 段：sample_insufficient（15笔）+ possible_over_filtering，数据供参考。四段均优于或持平三项组合。

---

## 模拟盘状态

- **账户**：demo，初始权益 10,000 USDT，单笔风险 1%
- **定时任务**：Windows 任务计划 `CryptoTrading_DailyPaperUpdate`，每天 20:05 自动执行
- **执行脚本**：`scripts/daily_paper_update.bat`，依次跑 scan → add-from-scan → paper update → paper report
- **日志**：`logs/daily_paper_update.log`
- **sensitive 组合生效日期**：2026-06-11
- **建议观察截止**：2026-07-02（约 3 周），届时根据模拟盘结果决定是否继续保留

### paper report 现包含的信息（2026-06-11 新增）

每日报告新增三项，专门用于 3 周后的判断：

1. **今日大盘环境节**：regime 状态（RISK_ON/NEUTRAL/RISK_OFF）、BTC/ETH 7d 涨跌与阈值对比、趋势确认情况
2. **RECLAIM_PENDING 事件**：每次价格进入 entry zone 但 4h 收盘未确认时记录事件，可追溯 entry_reclaim 拦截了哪些单
3. **统计补充**：Entry reclaim blocks 累计次数、平均持仓时长

---

## 关键代码位置

### market_regime.py — RISK_OFF 判断逻辑

```python
def classify_market_regime(
    btc_1d, eth_1d,
    btc_7d_drop_pct=-5.0,    # settings.analysis.regime_btc_7d_drop_pct
    eth_7d_drop_pct=-8.0,    # settings.analysis.regime_eth_7d_drop_pct
    require_both_trend=False  # settings.analysis.regime_require_both_trend
) -> MarketRegime
# RISK_ON 条件：trend_ok AND btc_not_breaking AND eth_not_breaking
# require_both_trend=True 时，BTC+ETH 必须同时满足 price>EMA20>EMA50
# 调用方：replay.py:622, scanner.py:356（均透传 settings 参数）
# regime_analysis.py:148 用默认值（仅用于事后分析，不影响回测/扫盘）
```

### paper_trader.py — entry_reclaim 逻辑

```python
# update_paper_trades() 约 437 行
# 条件：entry_reclaim_enabled AND status==WATCHING AND price<=entry_high
# 若 4h 最新已收盘 close < entry_high → 记录 RECLAIM_PENDING 事件，跳过入场
# 每天定时任务运行一次，不会重复记录
```

### abtest.py — dimension 白名单

新增的两个 dimension（可直接在 experiments.toml 引用）：

```python
"regime_sensitivity": {
    "analysis.regime_btc_7d_drop_pct",
    "analysis.regime_eth_7d_drop_pct",
    "analysis.regime_require_both_trend",
},
"combined_regime_entry_exit_sensitivity": {
    "analysis.risk_off_core_buy_enabled",
    "analysis.entry_reclaim_close_enabled",
    "analysis.tp1_ema_trailing_stop_enabled",
    "analysis.regime_btc_7d_drop_pct",
    "analysis.regime_eth_7d_drop_pct",
    "analysis.regime_require_both_trend",
},
```

---

## 已知问题 / 技术债

### 1. tp1_ema_trailing_stop corner case（未修，低风险）
- **现象**：TP1 命中时若 4h K 线不足 20 根，`tp1_trailing_ema_stop_active` 在内存中被置为 True，但 EMA 计算返回 None；下次 update 时可能突然激活跟踪止损
- **位置**：`trade_state.py`（step_trade 内部），`paper_trader.py:454-457`
- **影响**：模拟盘偶发，不影响回测（回测有足够历史 K 线）
- **修法**：仅当 EMA 有效时才设 active=True

### 2. tp1_trailing_ema_stop_active 不持久化（未修）
- **现象**：`PaperTrade.tp1_trailing_ema_stop_active` 是 dataclass 字段，DB 里没有对应列；每次 update 重新加载 trade 时该字段重置为 False
- **影响**：TP1_HIT 状态的跟踪止损每次 update 都重新从零判断，行为与回测不完全一致
- **修法**：在 paper_trades 表加列 `tp1_trailing_ema_stop_active INTEGER NOT NULL DEFAULT 0`，或改为从事件日志推断

### 3. 幸存者偏差（未修，结构性问题）
- Binance 历史退市币未纳入 symbol master（`reports/2026-06-09/dynamic_master_full.json`）
- 所有回测结果偏乐观，无法量化偏差幅度

---

## 接下来可以做的实验（按优先级）

### A. 持仓时间过滤（需改代码）
- **假设**：部分止损单是入场后长期横盘最终慢慢跌破止损，而非快速止损
- **实验**：入场后 N 根 4h K 线内未触 TP1 则强制平仓（N 约 18～36）
- **需改**：`trade_state.py`（step_trade 加 bar_count 计数）+ `config.py` 加参数 + `abtest.py` 白名单 + `experiments.toml` 加实验定义

### B. 市值分层分析（无需改代码，直接跑）
- **目标**：确认亏损主要来自 altcoin 还是 large-cap，熊市是否应只做 large-cap
- **做法**：用 `--symbol-master-file` 分别传只含 large-cap 和只含 altcoin 的 master JSON，跑两段对比回测
- **large-cap 参考**：BTC/ETH/BNB/SOL/XRP/DOGE/ADA/AVAX/TRX/TON 等前 20

### C. 修 tp1_trailing_ema_stop_active 持久化（改代码）
- 加 DB 迁移，在 paper_trades 表加列，保证模拟盘行为与回测一致

---

## 常用命令

```bash
# A/B 实验（两段必须串行，不能同时跑）
python main.py abtest --experiment <实验名> \
  --dynamic-universe \
  --symbol-master-file reports/2026-06-09/dynamic_master_full.json \
  --start 2024-07-01 --end 2025-06-01 \
  --max-symbols 40 --allow-data-gaps --no-obsidian

# 回测
python main.py backtest-dynamic-universe \
  --symbol-master-file reports/2026-06-09/dynamic_master_full.json \
  --start 2024-07-01 --end 2025-06-01 \
  --max-symbols 40 --allow-data-gaps --no-obsidian

# 模拟盘手动触发（定时任务每天 20:05 自动跑）
python main.py daily --no-obsidian

# 只生成模拟盘报告（不跑扫盘）
python main.py paper report

# 确认定时任务是否正常
Get-ScheduledTask -TaskName "CryptoTrading_DailyPaperUpdate" | Get-ScheduledTaskInfo | Select-Object NextRunTime
```

---

## 重要约束

1. **SQLite 单写**：两段回测/实验不能并行，必须串行
2. **symbol master**：所有回测使用 `reports/2026-06-09/dynamic_master_full.json`（418 个币），不要用其他文件
3. **实验新增 dimension**：必须先在 `abtest.py` 的 `ALLOWED_OVERRIDE_PATHS` 里注册，否则运行时报错
4. **不要直接改 settings.toml 的 analysis 参数来做实验**：应通过 experiments.toml + abtest 命令，保持生产配置稳定
5. **daily_trend_required 已 reject**：不要在新实验里复用，浪费算力
