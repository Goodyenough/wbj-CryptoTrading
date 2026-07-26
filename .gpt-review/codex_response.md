# Codex 对 GPT 评审的处理

## 总体判断

采纳 GPT 的核心评审：原方向正确，但不能原样执行。下一步不直接做 `slot_replacement_quality_review`，而是改成分阶段诊断路线：

```text
signal_fill_timing_audit
-> blocked_entry_event_export
-> replay_consistency_audit
-> stale_slot_continuation_review
-> blocked_candidate_vs_stale_slot_review
-> shadow replacement experiment
```

当前继续冻结 `config/settings.toml`，不部署 `atr_reclaim_0_35`，不提高 `max_active_positions`，不修改 score 排序。

## 接受的意见

- 增加 `signal_fill_timing_audit` 作为第 0 步，先确认 reclaim 信号、容量判断、成交价格和同根 K 线 exit/entry 顺序。
- 删除“可合理视为 entry-ready”的模糊表述，blocked event 必须来自确定状态机条件。
- 先导出 `blocked_entry_event_export`，再做 replay 一致性审计，不能用关键案例复原直接支持 replacement 结论。
- 将 `stale_slot_continuation_review` 独立出来，先回答旧仓达到 42 bars 后继续持有是否还有边际价值。
- 统一 `42 bars = 168h`，把 `240h+` 仅作为长期占槽观察口径。
- V1 replacement eligibility 仅限 pre-TP1 stale slots；post-TP1 slots 只作为描述和对照。
- 预先定义替换对象，禁止把事后最差 slot 当作策略证据；oracle 只能作为理论上限。
- 同一时点多个 entry-ready candidates 只取现有排序下第一个真正因容量被拒绝的候选作为主事件。
- baseline 必须先验证为 canonical baseline；variant 仅做机制敏感性，不能合并扩大样本量。
- V1 使用轻量但明确的成本口径，输出 gross/net、额外换仓成本、滑点敏感性和 top1/top3 concentration。

## 部分接受的意见

- 成本模型：接受必须纳入摩擦成本，但 V1 不做复杂实盘撮合模型，只使用当前 backtest 费用口径和低/中/高滑点敏感性。
- 分层变量：接受 GPT 建议进一步收敛。V1 主分层只保留 age、pre/post TP1、event-time unrealized R、regime、large-cap/altcoin；score、ATR reclaim、relative strength、momentum 暂作描述字段。
- 42 bars 主期限：接受以既有 42-bar 候选假设作为优先口径，但执行前先只看事件数量和分布，不查看 outcome，再确认最终主期限和敏感性期限。

## 拒绝的意见及原因

无明确拒绝项。GPT 的主要意见与项目当前研究纪律一致。

## 暂缓的意见及验证条件

- 是否推进完整 shadow replacement experiment：暂缓。只有 `stale_slot_continuation_review` 和 `blocked_candidate_vs_stale_slot_review` 均显示成本后、去极值后、跨月份和跨 regime 仍有稳定优势，才进入。
- 是否重跑 canonical baseline：暂缓到 `signal_fill_timing_audit` 和 baseline 一致性检查后决定。如果现有 baseline run 与当前默认配置不一致，则重跑。

## 已对方案作出的修改

- 已将 `.gpt-review/revised_plan.md` 替换为容量与换仓研究新版计划。
- 已将 TODO 下一步从单一 `slot_replacement_quality_review` 拆成 5 个诊断任务。
- 已更新 `EXPERIMENT_LEDGER.md`、`SYSTEM_OVERVIEW.md` 和 `开发计划.md`，记录新的分阶段路线。

## 仍未解决的分歧

无方向性分歧。剩余问题是执行口径必须严格化，尤其是：

- signal / decision / fill timing；
- canonical baseline 是否一致；
- blocked event 是否可重复导出；
- replacement pairing 是否完全事前可执行；
- 成本后优势是否仍存在。

## 是否建议再进行一轮 GPT 复审

暂不需要。新版计划已经吸收关键意见。建议先执行 `signal_fill_timing_audit`，若发现回放时点口径存在重大问题，再整理新的复审包。
