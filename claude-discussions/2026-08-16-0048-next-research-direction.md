---
status: WAITING_CLAUDE
round: 1
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

<!-- 由 Claude Code 追加；Codex 不代写。 -->

## Round 1：GPT 归纳与追问

<!-- 由 Codex 追加。 -->
