# Baseline 闸门 1：旧存档到 repaired legacy 的逐笔差异收口

Taskboard：`CRYPTOTRADIN-122`
结论：`pass_no_unresolved_trade_diff`

## 白话结论

旧存档和当前修复版之间的差异已经能解释完，不再有“看见结果变了，但不知道为什么”的交易。

- 两个窗口共有 130 笔同键平仓；其信号、计划价格、初始止损、止盈、入场时点和入场价格全部一致。
- 3 笔交易的平仓时点变化，事件链直接对应 EMA 收盘更新改为下一根生效。
- 其余共同交易的差异只落在浮点尾差，或前序盈亏改变后产生的仓位、费用、滑点和 P&L 连锁。
- 近窗 7 条 old/new-only 平仓记录中，6 条来自相同计划在 `max_active_positions=5` 下的容量换位或同币后续计划接续；1 条 SOL 来自当前 scanner 将计划提前一根 4h bar、同时改变 entry/score，随后又被容量拦截。
- 两个窗口的期末权益残差都能由同键未平仓头寸的数量和期末盯市差异解释。
- `unresolved=0`。这只证明口径变化可审计，不证明旧口径或当前 baseline 有盈利优势。

## 系统目标、唯一问题与判定标准

- 系统目标：确认修复后的 reference baseline 在冻结执行语义下能产生可复现、可审计的交易与 P&L，为后续盈亏归因建立可信输入。
- 唯一问题：旧存档到当前 repaired baseline 的增删改和权益变化，是否都能落到已知执行、记账、容量或 scanner 差异，而不是未解释漂移。
- 路线图位置：闸门 1 的最后一个缺口；通过后才允许进入闸门 2 的 clean 样本 census。
- 支持：同键交易的信号/入场保持一致；变化有事件或容量证据；权益可对账；`unresolved=0`。
- 拒绝：出现同输入随机漂移、无法解释的交易增删或无法闭合的权益差。
- 证据不足：原始运行没有所需字段，且没有一致性复跑或旁证可以恢复原因。

## 证据与方法

- 旧存档：SQLite `backtest_runs` 中 `e1231e5ad711`、`110c51eef593`。
- 当前结果：`reports/2026-10-09/atr_fixed_history_gate1_run_a/*_legacy_same_bar_baseline.json`。
- 配对键：`symbol + created_at_utc`；终态为 `CLOSED / STOPPED / TIME_EXIT`。
- 当前容量旁证：当前结果内的 `blocked_entry_events`。
- 旧容量旁证：`reports/2026-07-27/blocked_entry_event_export_2026-07-27_v1.json`；该导出已由 `replay_consistency_audit_2026-07-27_v1.md` 验证，旧 source 与 replay 的 389 个计划、58 个入场、active/open-plan 路径和 512 个 blocked-event 签名一致。
- 分类是描述性归因，不把组合路径变化冒充单笔因果贡献。

## 共同平仓差异

| 窗口 | 共同平仓 | 完全不变 | `stop_or_ema_accounting`：记账/资金路径 | `stop_or_ema_accounting`：EMA 时序 | 信号/入场字段不一致 |
|---|---:|---:|---:|---:|---:|
| 2024-07-01 至 2025-06-01 | 76 | 15 | 60 | 1 | 0 |
| 2025-06-01 至 2026-06-01 | 54 | 35 | 17 | 2 | 0 |

130 笔共同平仓的 `entry_low / entry_high / stop_loss / take_profit_1 / take_profit_2 / score / setup / action / verdict / entered_at_utc / entry_price_raw / entry_price_filled` 全部一致。

记账/资金路径组中，早窗 60 笔有 57 笔出现实质净 P&L 变化、3 笔只有约 `1e-16` 的浮点尾差；近窗 17 笔有 16 笔出现实质净 P&L 变化、1 笔只有浮点尾差。变化字段局限于 `quantity / entry_fee / exit_fee / slippage_cost / gross_pnl / net_pnl / r_multiple_net`，符合前序权益变化后的 sizing 与成本连锁。

### 3 笔 EMA 时序交易

| 窗口 | 交易键 | 旧平仓 | 新平仓 | 净 P&L 变化 | 证据 |
|---|---|---|---|---:|---|
| 早窗 | `SUIUSDT / 2024-09-29T12:00Z` | 2024-10-02 16:00 | 2024-10-02 20:00 | +8.3215 | 旧路径在 16:00 同根抬高 EMA stop 后立即用本根 low 触发；新路径标记 `effective from next bar`，到 20:00 才按已生效 stop 退出。 |
| 近窗 | `BNBUSDT / 2025-09-04T00:00Z` | 2025-09-15 04:00 | 2025-09-15 12:00 | +4.2262 | 旧路径 04:00 同根抬升后退出；新路径 04:00 的 EMA 只供下一根使用，08:00 再抬升，12:00 退出。 |
| 近窗 | `PEPEUSDT / 2026-05-08T04:00Z` | 2026-05-11 00:00 | 2026-05-11 04:00 | +9.3648 | 旧路径 00:00 同根抬升后退出；新路径 04:00 才触发。数量还承接了此前资金路径差异。 |

## 近窗 7 条 old/new-only 平仓

| 方向 | 交易键 | 净 P&L | 主分类 | 对账证据 |
|---|---|---:|---|---|
| old-only | `ETHFIUSDT / 2025-09-14T12:00Z` | +63.3224 | `stop_or_ema_accounting`：容量路径 | 当前存在完全相同计划，但在满 5 仓时反复记录 `max_active_positions`，最终未入场并过期。 |
| old-only | `SOLUSDT / 2025-09-18T00:00Z` | -117.0091 | `scanner_or_signal_set` | 当前没有同键计划；最近计划提前到 2025-09-17 20:00，entry、TP、score 均不同，并在 2025-09-18 00:00 满 5 仓时被拦截。 |
| old-only | `TRXUSDT / 2026-05-10T04:00Z` | +173.2964 | `stop_or_ema_accounting`：容量路径 | 当前存在完全相同计划，但在 2026-05-12 00:00 满 5 仓被拦截并过期。 |
| new-only | `AVAXUSDT / 2025-09-16T00:00Z` | +271.3248 | `stop_or_ema_accounting`：容量路径 | 旧一致性 replay 中同计划多次因满 5 仓被拦截；当前路径获得仓位并入场。 |
| new-only | `DOGEUSDT / 2025-09-17T20:00Z` | -118.3870 | `stop_or_ema_accounting`：容量路径 | 旧一致性 replay 中同计划因满 5 仓被拦截；当前路径获得仓位并入场。 |
| new-only | `ETHUSDT / 2026-05-08T20:00Z` | -115.6450 | `stop_or_ema_accounting`：容量路径 | 旧一致性 replay 中同计划多次因满 5 仓被拦截；当前路径获得仓位并入场。 |
| new-only | `TRXUSDT / 2026-05-13T08:00Z` | +220.9714 | `stop_or_ema_accounting`：计划接续 | 当前旧键 TRX 计划因容量过期后生成后续计划并入场；旧路径中旧键 TRX 已占用该 symbol，未生成这条接续路径。 |

这里的 6 条容量/接续记录是组合路径结果，不应分别宣称为 stop 修复的纯因果收益。SOL 的分类也只定位到 scanner/signal-set 演化，不主张已经找到具体源码提交。

## 权益闭合

| 窗口 | 共同平仓 ΔP&L | 减 old-only P&L | 加 new-only P&L | 未平仓/盯市残差 | 最终权益变化 |
|---|---:|---:|---:|---:|---:|
| 早窗 | +8.9840 | 0.0000 | 0.0000 | +0.0297 | +9.0137 |
| 近窗 | +6.8226 | -119.6098 | +258.2642 | -1.8015 | +143.6756 |

共同平仓 ΔP&L 进一步拆分：早窗 EMA 时序 +8.3215、记账/资金路径 +0.6625；近窗 EMA 时序 +13.5910、记账/资金路径 -6.7684。

期末残差不是未知损益：早窗未平仓仍为同键 `ASRUSDT`、`AAVEUSDT`，近窗仍为同键 `ZBTUSDT`；三者的入场信号和价格相同，仅数量承接前序权益变化，因此期末盯市与入场费用不同。

## 事实、观察、假设与决定

- 事实：当前 Gate 1 A/B 双跑 8/8 canonical checksum 一致。
- 事实：130/130 共同平仓的信号与入场字段一致；3 笔退出事件链直接命中已知 EMA 因果修复。
- 事实：近窗 6 条容量/接续差异有 `max_active_positions=5` 或同币计划生命周期证据；1 条 SOL 的计划键和几何发生 scanner 变化。
- 观察：执行/记账差异会先改变权益和空闲仓位，再改变后续 sizing 与候选能否入场，因此组合权益变化不能全归给那 3 笔 EMA 交易。
- 假设：若剩余差异都是上述连锁，则权益应由共同平仓、only 交易和未平仓盯市闭合；结果支持该假设。
- 决定：`unresolved=0`，闸门 1 通过；冻结当前 `confirmation_close` baseline 作为闸门 2 的输入，不修改生产配置，不启动参数实验。

## 闸门裁决

- 确定性：PASS。
- 输入与执行语义冻结：PASS。
- 新旧交易增删改归因：PASS。
- 权益闭合：PASS。
- `unresolved`：0。
- 总裁决：`pass_no_unresolved_trade_diff`。

下一步仅进入闸门 2：逐笔清点 repaired `confirmation_close` baseline 的 clean/contaminated、缺口、容量和存续币偏差；在真实 N 明确前不预设新参数或生产变更。
