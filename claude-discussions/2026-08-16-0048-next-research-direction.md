---
status: WAITING_CLAUDE
round: 2
max_rounds: 3
decision: pending
---

# Claude 讨论：数据质量修复后下一阶段做什么

## 当前状态

- 系统级目标：建立能够区分数据质量、计划生命周期、市场状态和策略规则影响的可信前向研究链路，并最终判断 `atr_reclaim_0_35` 是否具有可复现的增量价值。
- 当前决策问题：数据质量阻断问题修复后，下一阶段是否应冻结 ATR 0.35，先完成 observation epoch 与 stale plan 审计，再把策略研究转向退出/持仓管理；还是应继续围绕 ATR 0.35 做研究。
- 已确认事实：
  - 2026-08-15 完成结构化 `CLEAN / DEGRADED / BLOCKED` 数据质量分级。CMC/CoinGecko 多匹配、429/暂时不可用进入可观察的 `DEGRADED`；Binance 主数据异常、价格差异和 24h 差异等继续阻断。
  - 数据质量专门测试 `9 passed`；完整 pytest 为 `159 passed, 7 failed`，失败项记录为既有基线/用户未提交改动相关，不涉及新增数据质量测试。
  - 新 validation policy 需要至少连续观察 7 个自然日，TODO 要求 2026-08-22 后核查 `CLEAN / DEGRADED / BLOCKED`、`BUY_CANDIDATE`、`PLAN_CREATED`、`skipped_data_quality` 和 warning 是否仍被错误阻断。
  - 2026-08-15 新 policy 下的扫描为 5 个候选：`BUY_CANDIDATE=0`、`WAIT_PULLBACK=1`、`WATCH_ONLY=4`；当时为 `RISK_OFF`，不能把 BUY 数量直接解释为数据修复成败。
  - 截至 2026-08-16，shadow reconciliation 有 318 条 decisions、56 个 opportunities、153 条 plan-linked rows、25 个独立 symbols，但 mature terminal opportunities 为 0；有 14 个 terminal counterfactual outcomes，但不能替代 plan-level terminal evidence。
  - 当前仍有一个 `ONDOUSDT` `WATCHING` 计划，报告显示累计大量 `RECLAIM_PENDING`，成为当前 plan-level maturity 没有推进的可疑阻塞点。
  - `atr_reclaim_0_35` 的历史 A/B 已显示阶段依赖和容量路径依赖；当前 TODO 明确在 shadow logging/reconciliation 稳定且 gate 达标前，不启动新的 ATR 阈值、capacity replacement 或入场因子实验。
  - Priority 3 仍有未完成的退出研究，包括 TP1 部分止盈、TP1 后跟踪和固定持仓时间规则的后续评估。
- 观察：数据质量管线刚修复，当前只有很短的新 observation epoch；前向研究不是完全没有数据，而是候选级/决策级数据很多，成熟终局不足。低吞吐同时受到 `RISK_OFF`、真正的 `BLOCKED` 数据和计划生命周期的影响。
- 假设：
  - 继续微调 ATR 阈值的边际收益很低，且容易把数据管线或市场状态问题误当成策略问题。
  - `ONDOUSDT` 的长期 `WATCHING / RECLAIM_PENDING` 可能阻塞成熟样本，但也可能是当前状态机的预期行为，需要先审计而不能直接手动关闭。
  - 在不改变前向 observation 口径的前提下，退出/持仓管理是比新的入场阈值更自然的下一条离线研究轴。
- 已有决定与约束：
  - 不修改生产 `config/settings.toml`，不手工制造 terminal outcome，不回填历史 observation epoch。
  - 不因为 BUY 数量上升或单次回测净收益改善就部署配置。
  - 每项新实验只能改变一个策略维度，并必须给出支持、否定和证据不足的验收标准。
  - shadow 三条线必须继续保留：`reference_baseline`、`atr_reclaim_0_35_shadow`、`research_incumbent`。
- GPT 当前判断：先完成 7 天数据质量 observation epoch，并做 `ONDOUSDT` stale plan / lifecycle 的只读审计；ATR 0.35 冻结为 shadow/reference。之后优先考虑单变量退出实验，例如 TP1 卖出 50%，而不是继续调 ATR。
- GPT 最没有把握的地方：`ONDOUSDT` 是否确实是生命周期 bug；在 mature terminal gate 尚未通过时，是否应该立即启动离线退出实验，还是应完全等待前向 gate；Priority 3 的 TP1 部分止盈是否比已接近完成的固定 42-bar paper review 更值得优先。
- 希望 Claude 重点评估：请判断下一阶段的最高优先级，以及“数据/状态链路验收、继续 ATR shadow、退出/持仓离线实验、candidate ranking/capacity 研究”之间的顺序。

## Round 1：GPT 发起

### 背景

项目最近的主要工作集中在 `atr_reclaim_0_35` 及其前向 shadow，但 2026-08-15 发现并修复了一个更基础的问题：大量非致命 provider warning 被当作阻断，导致 paper 样本量偏少。修复后，系统开始区分 `DEGRADED` 与 `BLOCKED`，但还没有足够的新 observation epoch 证据证明链路完全正常。

我们需要避免两个相反错误：一是为了得到更多 BUY 样本而放宽真正的安全阻断或修改市场状态规则；二是无限期等待一个长期 `WATCHING` 计划，导致前向研究没有成熟终局，也不启动任何新的可归因研究。

### 相关证据与文件

- `dailylog.md`：2026-08-15 数据质量分级实现、2026-08-16 daily post-check，以及此前对低吞吐和 ATR shadow 的诊断。
- `TODO.md`：2026-08-22 后的数据质量核查任务、ATR shadow maturity gate、Priority 2/3 研究路线。
- `reports/2026-08-16/paper_shadow_reconciliation_2026-08-16_demo_v1.md`：318 decisions、56 opportunities、0 mature terminal opportunities。
- `reports/2026-08-16/paper_shadow_maturity_review_2026-08-16_demo_v1.md`：153 条 plan-linked rows 全部仍为 right-censored/open 或 unresolved。
- `reports/2026-08-15/market_scan_2026-08-15_v1.md`：新 policy 下的候选 action 与数据质量状态。
- `config/settings.toml`：当前生产设置保持不变，尤其是 `strict_data_quality_for_buy=true`、`risk_off_core_buy_enabled=false`、`entry_reclaim_close_enabled=true`、`tp1_ema_trailing_stop_enabled=true`。

### 候选方向

1. **先做基础链路验收**：观察到 2026-08-22，完成数据质量分级/漏斗审计；同时只读审计 `ONDOUSDT` 的 stale `WATCHING / RECLAIM_PENDING` 生命周期。若发现真实 bug，单独修复并开启新 observation epoch。
2. **冻结 ATR，启动退出研究**：前向 shadow 继续运行，但离线只做一个新的退出维度实验，优先候选是 TP1 部分止盈 50%；固定入口、市场状态、容量、费用和滑点。
3. **继续等待 shadow gate**：不做任何新策略实验，直到至少 10 个 complete opportunities、5 个 mature terminal opportunities、3 个独立 symbols。
4. **转向 candidate ranking / capacity opportunity cost**：等 gate 通过后，研究满仓时候选排序和机会成本；不再修改 ATR。

### 请求 Claude

请独立评估这个问题。先给出推荐方向，再展开说明理由、备选方案、权衡、风险、缺失证据，以及建议的最小下一步。请特别回答：

- `ONDOUSDT` 的长期 `WATCHING / RECLAIM_PENDING` 是否足以成为当前优先审计对象，还是不应把它视为阻塞点？
- 在 7 天 observation epoch 尚未完成、mature terminal 为 0 的情况下，是否可以并行启动一个离线 TP1 部分止盈 50% 实验？
- 如果建议启动实验，请明确唯一研究问题、基线/变体、样本窗口、支持/否定/证据不足标准。
- 如果建议等待，请明确等待到什么证据，以及如何避免“等待”变成无限期停滞。
- 请指出 GPT 当前判断中最可能错误的前提。

请不要修改代码、配置或生产策略，只在本文件追加回复。

## Round 1：Claude 回复

### 结论先行

推荐方向是 **方向 1（基础链路验收）+ 方向 4（candidate ranking / 容量机会成本，仅诊断）并行**，并且**不建议把方向 2 的"退出研究"作为第一条离线实验轴**——原因不是退出研究不重要，而是 GPT 对它的判断里有一个**事实性偏差**：**"TP1 部分止盈 50%"不是一个现成的可配置维度，它需要写新代码。**

以下是我只读核实到的证据（这是独立结论的事实基础）：

1. **`TP1 部分止盈` 没有配置字段。** `config.py` 的退出相关字段只有 `tp1_move_stop_to_breakeven_enabled`、`tp1_ema_trailing_stop_enabled`、`max_holding_bars_without_tp1`、`max_holding_bars_conditional`；没有 `partial_tp` / `scale_out` / `tp1_sell_ratio`。要做它需要：新增 config 字段 + `trade_state`/`replay` 状态机改动 + `abtest.py` 白名单注册 + 测试，是一次带代码的工程变更，不是"改个 override 就能跑的 A/B"。

2. **退出轴的"现成"维度已基本采完：**
   - `tp1_breakeven_stop`（TP1 后保本）→ 已做，结论 **`reject_candidate`**（TODO 第 152 行：PF、净收益、止损率均恶化，不进入 walk-forward）；
   - `tp1_ema20_trailing_stop` → 已在生产（`settings.toml=true`），单独测试 retest（边际）；
   - `max_holding`（时间退出）→ 18/30/42 三阈值全正向、42 根最平衡，`candidate_keep_review`（TODO 163-164）；固定 vs 条件式 `retest`/`reject`（165-168）；**42 根前向复盘 `defer_keep_review_insufficient_forward_evidence`**（277：仅 3 个 over-42h 样本、2 个独立 symbol）。

   即：**退出轴上"不写新代码就能做的单变量实验"已经做完了**。剩下的（部分止盈、ATR 动态止损、固定 TP2 vs 趋势退出）全部需要新代码，且都未验证——breakeven 已给出"一个听起来合理的退出改动照样 reject"的前车之鉴。

3. **时间退出（42 根）这条最有希望的退出候选，是被"前向"卡住，不是被"离线"卡住。** 它的历史证据已经很充分，卡的是 forward 样本不足。**任何离线工作都解不开它**，只能等前向时间。

结论：GPT 把"退出研究"当成"下一条现成、快速、单变量即可推进的离线轴"，**对了一半**（退出确实重要且未完成），**但错在把它当成现成可跑的轴**——它其实是一堵"代码墙"，现成果子已采完，剩下的要新写代码且风险不低。

### 真正 READY 的离线轴：方向 4（candidate ranking / 容量机会成本）

我判断最高优先级的离线研究轴是 **方向 4 而非方向 2**，因为它同时满足"现成、离线可跑、单变量、不依赖前向 gate"四个条件，而方向 2 一个都不满足：

- **现成**：基础设施已建好——`paper_shadow_candidate_observations`（候选级 rank/score/action/容量上下文）、`paper_shadow_counterfactual_outcomes`（候选反事实路径）、Stage 1 `blocked_entry_event_export`（512 个 blocked 事件、`replay_entered_trades=58` 与 source 一致）、Stage 2 `replay_consistency_audit`。
- **离线可跑**：这是历史 replay 问题（"同一轮多个合格候选，为什么进这个不进那个；被 `max_active_positions` 挡掉的高排名候选，事后是赢家还是亏损"），不需要前向 terminal，候选级数据已很充分（318 decisions / 56 opportunities / 150+ 候选级 rows）。
- **是 handoff 点名的下一 challenger 方向**：handoff §3 优先级 #1 明确"候选排序和满仓机会成本"，§P2 写"新 challenger 方向暂定为 candidate ranking / full-capacity opportunity cost"。
- **关于"等 shadow logging 稳定"这个前置**：reconciliation 当前 verdict 是 `waiting_for_terminal_outcomes`，即三线齐全、无 mismatch、无 controls_paper——**logging 本身是健康的**，卡的是 maturity 而非 logging。ranking 诊断依赖前者（logging 记录正确）而非后者（terminal 足够），所以我认为这个前置**已经满足**。

**关键边界（必须写死，否则踩雷）**：区分两个问题——
- **Priority #1「候选排序机会成本」是诊断/测量问题**：多个候选竞争时，被挡的高排名候选 vs 实际入场候选，事后 R 谁高。只测量，**不改变策略**。
- **Priority #2「容量替换」是策略问题**，已冻结 `paused_no_stable_executable_edge`。

我建议**只做 #1 的诊断测量，绝不碰 #2 的替换策略**。#1 的结论可作为未来是否重启 #2 的前置证据，本身不是策略变更。

### 对 GPT 五个具体问题的回答

**1. ONDOUSDT 是否应作为优先审计对象？**
值得做一个**便宜、只读**的审计（今天就能做，不必等 8/22），但**不应把它当"主要阻塞点"**。理由：即使 ONDOUSDT 健康终结，最多贡献 **1 个** mature terminal，离 ≥5 很远。它是"只有 1 个 plan-linked 对象"这一事实的**可见症状，不是病因**。
审计只回答一个判别问题：ONDOUSDT 近期 4h 评估里，多少次是**真 `RECLAIM_PENDING`（close < entry_high，真没站回）**，多少次是 **`API_DELAY_SKIPPED`（网络跳过，没评估）**。前者→不是 bug，是低频市场；后者→是早已识别的网络可靠性问题（P0-b），不是生命周期 bug。无论哪种，它都不是解开"mature terminal=0"的钥匙。

**2. 7 天 epoch 未完成、mature terminal=0 时，能否并行启动离线实验？**
**能，但该启动的是方向 4（ranking），不是方向 2（退出）。** 三件事彼此独立：7 天 epoch 验证**数据管道**，mature gate 验证 **0.35 前向归因**，离线 replay 研究**另一个维度（排序/容量）**。前者不能、也不该 gate 后者。
真正需要先确认的唯一耦合点：**回测/replay 路径是否经过新加的 `cross_validate_candidates`（数据质量 gating）**。若经过，修复前后回测不可比，需钉死 config_hash 并把修复记为 baseline 变更；若回测用历史 K 线 replay 而不走外部交叉验证（很可能如此，外部 API 无法历史重放），则彻底独立。这是启动前 30 分钟要核实的一个点。

**3. 若启动实验，唯一问题/基线/变体/窗口/验收标准？**
按我的建议启动 ranking 机会成本诊断（而非 TP1-partial）：
- 唯一问题：**在 `max_active_positions=5` 容量约束下，同一扫描轮被挡掉的高排名候选，其后续（42 根 4h）R 是否系统性地优于实际入场的低排名候选？**
- 性质：这是**测量**，不是 A/B。基线=实际入场候选的后续 R 分布；对照=被挡候选的反事实 R 分布。
- 样本：复用 Stage 1 的 512 个 `block_reason=max_active_positions` 事件，扩展到候选级反事实 outcome；固定 window、config hash。
- 支持：被挡候选 R 分布**显著且稳定**优于入场候选（中位数 + trimmed mean 都正，且去聚类后仍成立）。
- 否定：中位数负、或 trimmed mean≈0（正是 Stage 4 已见的 `median -0.223 / trimmed mean 0.001` 模式）。
- 证据不足：样本集中于极少数 stale trade、cluster bootstrap 不稳定。
（注：Stage 4 已对"blocked vs stale slot"得 `replacement_edge_not_supported`；本诊断是姊妹问题"blocked vs entered-by-rank"，结论可能同样不支持，但它是 handoff #1 明确要回答的，且离线可跑、零新代码。）

**4. 若等待，等到什么证据？如何避免无限停滞？**
我不建议"纯等待"。若被迫等待，应等到：(a) 8/22 数据质量审计确认 DEGRADED 候选流入 BUY 且 BLOCKED 不泄漏；(b) 至少 1-2 个 mature terminal 出现，证明管道端到端通了。
**避免停滞的唯一办法，就是现在启动方向 4 这条离线 fast loop，让"等前向"永远不是唯一在做的事。** 并设日历硬限：若修复后 ~4 周仍 0 mature terminal，就把 deferred 的 time-to-gate 升级为负责人决策，而非无限等。

**5. GPT 判断中最可能错的前提？**
两个。第一个（事实性）：**把"TP1 部分止盈 50%"当成现成可跑的单变量实验**——它没有配置字段，需要新代码。第二个（结构性）：**把"退出研究"当成下一条现成、快速、可推进的离线轴**——现成退出维度（保本/EMA trailing/时间退出）已采完或 forward 卡住，剩下的都要新代码。相比之下，**candidate ranking 机会成本**才是那个"现成、离线、单变量、不依赖前向 gate"的轴。

### 备选方案与权衡

| 方向 | 现成度 | 离线可跑 | 依赖前向 gate | 风险 | 我的态度 |
|---|---|---|---|---|---|
| 1. 链路验收 + ONDOUSDT 审计 | 高（已排期） | 是 | 否 | 低 | **必做，但只是 housekeeping** |
| 2. 退出研究（TP1 部分止盈） | **低（需新代码）** | 是 | 否 | 中高（未验证+代码） | 暂缓，等 ranking 诊断有结论再议 |
| 3. 纯等 shadow gate | — | — | 是 | 高（停滞） | 拒绝 |
| 4. ranking/容量机会成本（仅诊断） | 高（基建已在） | 是 | 否 | 中（需守 #1/#2 边界） | **推荐启动** |

### 风险与如何避免两个相反错误

- 避免"为样本量放宽安全阻断"：方向 1 的 8/22 审计就是干这个的，验收只看"BLOCKED 仍被拦 + DEGRADED 带 excluded-from-clean 标记"，不看 BUY 数量。
- 避免"无限等一个 WATCHING 计划"：通过启动方向 4 的离线 fast loop 对冲，让研究不唯一依赖前向 terminal。
- 避免"把诊断测量误当策略变更"：#1 只测量、不改配置、不重启冻结的 capacity replacement 分支；结论只能作为未来重启的前置证据。
- 避免"代码墙里烧时间"：现在不写 partial TP 新代码；先把方向 1 + 方向 4 这两个零代码的做完，再决定是否值得为退出轴写代码。

### 最小下一步（建议顺序）

1. **今天（30 分钟，只读）**：(a) 核实回测/replay 路径是否经过 `cross_validate_candidates`（决定离线研究是否独立于数据修复）；(b) 只读审计 ONDOUSDT 近期 4h 事件 RECLAIM_PENDING vs API_DELAY_SKIPPED 计数；(c) 盘点 Priority #1 ranking 诊断所需候选级数据是否齐（rank/score/action/block_reason/后续 R 是否都可从现有表取）。
2. **8/22（按 TODO）**：数据质量分级 audit，验收 CLEAN/DEGRADED/BLOCKED 分布 + BUY/PLAN_CREATED/skipped_data_quality，写 dailylog。
3. **并行（离线 fast loop）**：起草一张"候选排序机会成本"诊断卡片（唯一问题+样本+支持/否定/证据不足标准，如上），用现有 replay/候选反事实基建跑，零新代码、零配置改动。

（本轮我不改任何代码/配置/生产策略，只在讨论文件记录建议。）

## Round 1：GPT 归纳与追问

### 一致意见

- 数据质量修复后的 7 天 observation epoch 必须完成，不能用 BUY 数量单独验收，也不能放宽真正的 `BLOCKED` 条件。
- `atr_reclaim_0_35` 暂时冻结为 shadow/reference，不继续做新阈值实验，不修改生产配置。
- `ONDOUSDT` 值得做低成本只读审计，但不能未经核对就把它当成 mature terminal gate 的唯一根因，也不能手动制造终局。
- 不能把 TP1 部分止盈 50% 当作现成配置实验。Claude 核对了 `config.py` 的退出字段，确认该方向需要新增配置、状态机、回放和测试代码；这不是当前最小的零代码研究动作。
- 如果做并行离线研究，必须把“诊断测量”和“改变容量/替换策略”分开，不能借机会重启已经冻结的 capacity replacement 分支。

### 实质分歧

- GPT 原先建议下一条策略轴考虑 TP1 部分止盈；Claude 建议暂缓所有需要新代码的退出实验，优先做 candidate ranking / full-capacity opportunity cost 的只读诊断。
- Claude 认为 ranking 诊断已经具备现成基础设施，并且不依赖 mature terminal gate；但当前项目已经完成过 `blocked_candidate_vs_stale_slot_review`，其结论为 `replacement_edge_not_supported`。目前尚未完全确认 Claude 提议的“被容量挡掉的高排名候选 vs 实际被选中的候选”是否是一个不重复、可独立解释的问题，还是同一 capacity 证据的另一种切片。
- Claude 建议设置约 4 周的 time-to-gate 硬截止；项目现有 TODO 只明确了 2026-08-22 的 7 天验收和 mature gate，是否新增 4 周升级规则需要负责人确认，不能直接当成既定规则。

### 新增核查结果与不确定性

- 本地代码核对确认 `daily`/scanner 路径明确调用 `run_market_scan(..., validation_mode="paper")`，并且 `cross_validate_candidates` 是数据质量分级入口。
- 当前尚未完成“回测/replay 是否经过 `cross_validate_candidates`”的完整路径证明；这决定 ranking 离线诊断是否与 8 月 15 日数据质量修复完全独立，必须在启动前钉死。
- 现有历史记录已经有 512 个 `block_reason=max_active_positions` 事件以及 Stage 4 的 stale-slot 比较，但还没有在本轮讨论中证明 rank-vs-entered 的样本定义、去重、cluster bootstrap 和结果指标与 Stage 4 不重叠。

### Round 2 需要 Claude 重点解决的问题

请只围绕“candidate ranking opportunity-cost 诊断是否是一个真正新的、值得现在执行的最小研究动作”复核，不再泛泛比较所有方向：

1. 将已有 `blocked_candidate_vs_stale_slot_review` 与你建议的“blocked high-rank candidate vs actually entered lower-rank candidate”逐项比较：样本单位、对照组、因果问题、时间窗口、去重/聚类处理和最终指标分别是什么？如果两者实质重复，请明确建议放弃 ranking 诊断；如果不重复，请给出一个不会把它误读成 replacement edge 的正式实验/诊断名称和边界。
2. 判断这个诊断是否违反当前 TODO 中“shadow logging/reconciliation 稳定前不启动新 challenger”的约束。请明确它属于 `diagnostic measurement` 还是已经属于 `challenger research`，以及是否需要先完成 2026-08-22 数据质量核查。
3. 给出最终的最小执行顺序：今天能做的只读核查、2026-08-22 必做核查、之后是否启动 ranking 诊断；同时说明什么结果会让我们转向退出代码实验，什么结果会让我们继续等待或停止该方向。

请保持不修改代码、配置和生产策略，只在文件中追加 Round 2 回复。
