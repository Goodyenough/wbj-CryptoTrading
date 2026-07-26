# 容量与换仓研究新版计划

更新时间：2026-07-26 23:59 +08:00

## 结论

下一步研究方向仍然成立，但不再直接执行 `slot_replacement_quality_review`。

新版路线改为：

```text
signal_fill_timing_audit
-> blocked_entry_event_export
-> replay_consistency_audit
-> stale_slot_continuation_review
-> blocked_candidate_vs_stale_slot_review
-> shadow replacement experiment
```

前五步都是诊断，不是策略部署依据。只有诊断证据通过后，才允许设计完整 shadow replacement experiment。当前继续冻结 `config/settings.toml`，不部署 `atr_reclaim_0_35`，不提高 `max_active_positions`，不修改 score 排序，也不把 replacement 写入 paper/live 状态机。

## 背景

`atr_reclaim_0_35` 在两段 dynamic-universe A/B 中表面指标改善，但交易级归因和关键路径复盘显示：

- 改善主要来自 variant-only 新增赢家，而不是 common trades 普遍变好。
- 近端窗口少数赢家对净改善贡献很高，路径依赖明显。
- 部分赢家出现时 opposite run 已达到 `max_active_positions=5`。
- missed baseline winners 也包含高质量 TP2 交易。

随后 `capacity_and_opportunity_order_review` 进一步确认：

- baseline 满仓占 28.0% 的 4h bars，variant 满仓占 30.3%。
- 两组都有长期负 R 占槽问题。
- blocker 质量混合，不能直接推出提高仓位数或改变排序会改善。

因此，研究问题从“继续调入场阈值”转为“满仓时旧仓是否值得继续占槽，新机会是否有可执行的替换价值”。

## 已采纳 GPT 评审意见

### 1. 增加第 0 步：`signal_fill_timing_audit`

在导出 blocked event 前，必须先审计回放时间轴：

- reclaim 信号在哪根 4h K 线完成确认。
- 容量判断发生在信号确认前还是确认后。
- 成交使用本根 close、下一根 open，还是其他价格。
- 同一根 K 线上 exit 与 entry 的处理顺序。
- replay 与原 backtest 是否使用完全相同的顺序。

原因：如果 signal / decision / fill 的时间顺序不可靠，后续 blocked event、active slot snapshot 和 replacement 标签都会建立在错误时点上。

### 2. 先导出可审计的 blocked event

`blocked_entry_event_export` 的目标不是得出策略结论，而是生成可重复、可审计的事件表。

每个事件至少记录：

- unique event id
- run id / commit / config hash / universe id
- `signal_time`
- `decision_time`
- `fill_time`
- `block_reason`
- candidate rank
- active count before decision
- candidate snapshot
- all active slots snapshot

模糊表述“可合理视为 entry-ready”删除。事件必须来自确定的状态机条件。

### 3. 增加 replay 一致性审计

在计算 future outcome 前，必须先证明导出器与原 run 一致：

- 实际进入交易集合一致。
- 入场时间一致。
- 排序一致。
- 每根 K 线 active position 数量一致。
- block reason 可重复。

如果不能通过一致性审计，历史 blocked event 分析只能作为案例复盘，不能作为 replacement 诊断证据。

### 4. `stale_slot_continuation_review` 独立于 blocked event

`stale_slot_continuation_review` 先回答旧仓自身问题：

> 所有 pre-TP1 仓位达到 42 根 4h K 线后，继续持有的边际价值如何？

它不应只限于发生 blocked candidate 的时点。这样可以区分：

- 旧仓是否已经失去价值。
- 新机会是否确实更好。

可能出现“旧仓很差，但新机会也很差”的情况。此时可能支持 time exit 继续研究，但不支持 replacement。

### 5. 统一 42 bars 与 240h 口径

- `42 bars = 168h`：候选 time-exit 或 stale 判定口径。
- `240h+ = 60 bars`：长期占槽观察口径。

后续报告不得混写 `42 bars / 240h`。

如果使用 42 bars 作为主期限，必须说明它来自既有候选假设，而不是在当前窗口中重新挑选出的最优期限。由于 `2025-06-01 -> 2026-06-01` 已被多轮研究查看，也不能把该窗口称为完全独立 confirmatory holdout。

### 6. V1 replacement eligibility 只允许 pre-TP1 stale slots

V1 中：

- pre-TP1 stale slots 可以成为 replacement 对象。
- post-TP1 slots 只作为描述和对照。
- post-TP1 slots 暂不进入主要替换规则。

原因：TP1 后仓位可能已经有 realized R、剩余风险下降、EMA trailing 激活或剩余数量变化，和完整未减仓仓位不可直接公平比较。

### 7. 预先定义替换哪个旧仓

禁止使用“新机会优于至少一个 active slot”作为主证据。该表述存在 oracle 风险。

主规则候选：

- 替换最老的、未触发 TP1、age >= 42 bars 的仓位。

敏感性规则：

- 在符合 age >= 42 bars 且 pre-TP1 的仓位中，替换 event-time unrealized R 最低者。

事后最差 slot 只能作为 `oracle_upper_bound`，不得作为策略证据。

### 8. 同一时点多个候选归一

如果同一决策时点有多个 entry-ready candidates：

- 主样本只采用现有排序 `(-score, created_index, symbol)` 下第一个真正因 `max_active_positions` 被拒绝的候选。
- 其他候选记录在附属表。
- 不把同一时点多个候选全部计为独立主样本。

统计单位是 unique blocked-candidate event，不是 candidate-slot pair。

### 9. baseline 证据层级

baseline 是主证据，但必须先确认它是 canonical baseline：

- commit 是否匹配当前研究口径。
- config hash 是否匹配当前默认配置。
- universe 构造是否固定。
- 数据范围是否完整。
- 当前默认规则是否一致。

如果不一致，应重跑冻结后的 canonical baseline。`atr_reclaim_0_35` variant 只能作为机制敏感性样本，不能与 baseline 合并提高样本量。

### 10. 成本模型采用轻量但明确的 V1

V1 不建立复杂撮合模型，但必须报告：

- gross replacement delta
- 当前 backtest 手续费口径下的 net delta
- 卖出旧仓 + 买入新仓的额外成本
- 低/中/高滑点敏感性
- replacement 次数/月
- top1/top3 事件贡献
- 去掉 top1/top3 后结果

## 阶段计划

### Stage 0：`signal_fill_timing_audit`

目标：确认当前 replay 的信号、决策和成交时间轴没有前视或不一致。

状态：已完成。报告 `reports/2026-07-27/signal_fill_timing_audit_2026-07-27_v1.md` 给出 `timing_audit_warn_same_bar_ambiguity`。

输出：

- 当前 entry reclaim 的 `signal_time` / `decision_time` / `fill_time` 说明。
- 同根 K 线 exit / entry 顺序说明。
- 是否需要改写或补充 replay 事件记录。

通过标准：

- 能清楚说明每个价格和状态判断来自哪个时间点。
- 若发现本根 close 确认与本根 close 成交存在不可接受前视，则先修正回测口径，再继续后续阶段。

### Stage 1：`blocked_entry_event_export`

目标：导出完整、可重复的 capacity-blocked event 表。

通过标准：

- 每个 blocked event 有唯一 ID。
- `block_reason=max_active_positions` 与其他阻塞原因分离。
- candidate 和 active slots 快照完整。
- 必须记录 `fill_time_assumption`、`active_snapshot_after_exits`、`same_bar_entry_exit_possible` 和 `same_bar_entry_tp1_possible`。
- 重复运行结果一致。

### Stage 2：`replay_consistency_audit`

目标：确认 blocked event export 与原 backtest run 行为一致。

通过标准：

- entered trades、entry time、active count path 与原 run 对齐。
- 候选排序与 replay 源码一致。
- 若不一致，先修导出器，不进入 outcome 分析。

### Stage 3：`stale_slot_continuation_review`

目标：独立评估 pre-TP1 仓位达到 42 bars 后继续持有的边际价值。

主样本：

- canonical baseline 中所有 pre-TP1 且 age 达到 42 bars 的仓位。

主标签：

- `forward_R_42_from_stale_time`
- `first_hit_outcome_after_stale_time`
- MFE / MAE after stale time

辅助标签：

- `forward_R_24`
- `forward_R_60`
- eventual R
- censored 标记

判定：

- 如果 stale continuation 明显为负，支持继续研究 time exit 或 replacement。
- 如果 stale continuation 不差，则 replacement 研究优先级下降。

### Stage 4：`blocked_candidate_vs_stale_slot_review`

目标：在真实 capacity-blocked event 中，比较 entry-ready candidate 与按事前规则选出的 stale slot。

主规则：

- candidate：排序第一且确认为 `block_reason=max_active_positions` 的 entry-ready candidate。
- slot：最老的 pre-TP1 且 age >= 42 bars 的 active slot。

主标签：

- `net_replacement_delta_R_42`

敏感性：

- `net_replacement_delta_R_24`
- `net_replacement_delta_R_60`
- lowest-unrealized-R eligible slot
- `oracle_upper_bound`

稳健性输出：

- median
- 20% trimmed mean
- positive-event ratio
- top1/top3 contribution
- top1/top3 removal
- month leave-one-out
- symbol / regime / large-cap vs altcoin 分层
- gross vs net-of-cost
- censored ratio

判定：

- 只能输出诊断 verdict。
- 最多进入 `retest_replacement_candidate`。
- 不允许直接 keep 或部署。

### Stage 5：shadow replacement experiment

只有 Stage 3 和 Stage 4 都显示稳定、成本后仍存在的 replacement edge，才允许设计完整状态机 shadow experiment。

shadow experiment 需要回答：

- replacement 是否改善完整组合收益。
- 是否降低或扩大 MDD。
- 是否增加止损率。
- 是否提高换手、手续费和滑点暴露。
- 是否改变后续机会链。

## 暂不做的事

- 不部署 `atr_reclaim_0_35`。
- 不提高 `max_active_positions`。
- 不修改 scanner score。
- 不把 replacement 写入 paper/live 状态机。
- 不把 post-TP1 slots 放入 V1 replacement eligibility。
- 不把 oracle upper bound 当作策略证据。
- 不把 baseline 和 variant 合并成一个统计总体。
- 不继续调 ATR reclaim、RSI、MACD 或 relative strength 过滤器，直到容量/时点问题厘清。

## 下一步直接执行

1. 设计 `blocked_entry_event_export` 的事件 schema 和导出入口。
2. 事件必须只记录确定状态机条件下的 `block_reason=max_active_positions`。
3. 事件快照必须在同根 active exits/time exits 处理之后生成。
4. 导出器实现后先跑 `replay_consistency_audit`，再计算任何 future outcome。

## 当前决策

`修改后可以执行`。

执行前仍需保持配置冻结。任何诊断完成后，都必须先更新实验日志和项目文档，再决定是否进入下一阶段。

## 2026-07-27 执行进展

### Stage 1：`blocked_entry_event_export`

状态：已完成。

输出：
- 报告：`reports/2026-07-27/blocked_entry_event_export_2026-07-27_v1.md`
- JSON sidecar：`reports/2026-07-27/blocked_entry_event_export_2026-07-27_v1.json`

核心事实：
- source run：`110c51eef593`
- replay run：`ed682b4a5531`
- source/replay entered trades：`58 -> 58`
- `blocked_entry_events=512`
- `same_bar_entry_exit_possible_events=0`
- `same_bar_entry_tp1_possible_events=2`

解释：Stage 1 只证明 `max_active_positions` blocked events 可以被可审计地导出，不证明 replacement 有价值。

下一步直接执行：
1. 设计并实现 `replay_consistency_audit`。
2. 对比 source run `110c51eef593` 与 exported replay `ed682b4a5531` 的 entered trades、entry time、active count path、candidate ordering 和 blocked event 重复运行一致性。
3. 若一致性审计未通过，先修正导出器或 source-run 复现口径，不进入 outcome 分析。
4. 一致性审计通过后，才进入 `stale_slot_continuation_review`。
