---
created: 2026-07-30 08:10:00 +08:00
tags:
  - crypto
  - trading-system
  - historical-membership
  - atr-reclaim
experiment: atr_reclaim_stage_n3_gate_decision
verdict: third_window_not_recoverable_without_historical_master
---

# atr_reclaim Stage N3 Gate Decision

## System Goal

把 dynamic-universe 回测从“当前 exchangeInfo 回看历史”推进到“按历史时点构造 universe”，降低 survivor bias。

## Single Question

N2 发现的 `147` 个 missing historical symbols 中，有多少可以被现有或等价的排除规则解释？第三窗口是否能通过简单清洗恢复验证价值？

## Facts

- N2-B 发现第三窗口 `2023-07-01 -> 2024-07-01` 内 historical USDT symbols 为 `413`。
- 其中 `266` 个在 current master，`147` 个不在 current master。
- N3 对 147 个缺失 symbol 进行分类。
- 可解释为杠杆代币、稳定币/法币对、非标准资产的缺失 symbol：`20`。
- 剩余 standard-like historical gap：`127`。
- standard-like gap 占标准 universe 比例：`32.32%`。

## Observation

缺失不是少数非标准资产造成的。即使排除 `UP/DOWN` 杠杆代币、稳定币/法币对和已知非标准资产，仍有大量普通历史现货或迁移/退市币不在 current master。

## Decision

`third_window_not_recoverable_without_historical_master`

第三窗口不能靠 listing date、简单排除或 current master 清洗恢复为验证窗口。它仍可作为 data-quality diagnostic，但不能作为 `atr_reclaim_0_35` 的 keep/reject 证据。

## Consequence

- 不重跑第三窗口 corrected N1。
- 不做路径分叉审计。
- 不部署 `atr_reclaim_0_35`。
- 不修改 `config/settings.toml`。
- 不提高 `max_active_positions`。

## Next Action

进入 historical master 数据工程：

1. 对 standard-like missing symbols 建立 source-backed mapping。
2. 区分 true delisted、rename/migration、base-asset replacement、仍可由策略排除的低流动性资产。
3. 补齐 `listing_time / delisting_time / first_kline_time / last_kline_time / tradable_from / tradable_to / source / confidence`。
4. 只有 historical master 可构造后，才重新选择验证窗口或恢复第三窗口。

## Source Reports

- `reports/2026-07-30/atr_reclaim_stage_n2_universe_audit_2026-07-30_v2.md`
- `reports/2026-07-30/atr_reclaim_stage_n3_historical_membership_dataset_2026-07-30_v1.md`
