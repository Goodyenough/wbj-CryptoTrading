# Baseline 盈亏归因闸门 1：可复现性与口径冻结

Taskboard：`CRYPTOTRADIN-122`
状态：`done`
裁决：`pass_no_unresolved_trade_diff`

## 白话结论

修复后固定历史 replay 可以稳定复现。完全相同的代码、配置、历史币池和本地 K 线缓存连续运行 A/B 两次，8 个预声明分支剥离随机生成的 `run_id / trade_id / event_id` 和运行时间戳后，业务内容 checksum 全部一致；两个窗口的输入 hash 也完全一致。

逐笔收口现已完成。两个窗口 130 笔同键平仓的信号、计划和入场字段全部一致；3 笔平仓时点变化由 EMA 收盘更新下一根生效的事件链直接解释，其余共同交易变化仅为浮点尾差或前序权益变化后的仓位/费用/P&L 连锁。近窗 7 条 old/new-only 平仓中，6 条有 `max_active_positions=5` 或同币计划接续证据，1 条 SOL 明确属于 scanner 将计划提前一根 4h bar 后改变 entry/score 的信号集合变化。期末权益差由共同平仓、only 交易和同键未平仓盯市完全闭合，`unresolved=0`。闸门 1 通过；闸门 2 可以按原依赖进入，但本报告不自动启动它。

## 系统目标、问题与路线图位置

- 系统目标：判断修复后的 reference baseline 在费用、滑点、容量和执行约束下是否存在可信优势。
- 本闸门唯一问题：相同输入能否得到相同交易与逐笔 P&L，并且旧新口径差异是否足够清楚，能安全进入样本清点。
- 路线图位置：闸门 1（可复现性与口径冻结）→ 闸门 2（clean 样本 census）→ 闸门 3（成本栈与亏损机制）。
- 当前决定：确定性和根因拆解均通过，`CRYPTOTRADIN-122` 完成；`CRYPTOTRADIN-123` 解除前置阻塞，仍保持 `todo`，等待单独启动。

## 事实、观察、假设、决定

- 事实：A/B 两次运行使用同一 commit、settings、experiments、runner、协议和数据输入；全部 canonical checksum 一致。
- 事实：运行只读 SQLite 与本地缓存，禁止网络补数；没有修改生产配置。
- 事实：旧存档到当前 legacy baseline 的早窗交易集合相同；近窗交易集合发生变化。
- 观察：原始 JSON SHA256 不同，差异来自每次运行随机生成的身份字段和运行时间戳，不是交易路径或 P&L 漂移。
- 假设：剥离运行身份字段后，业务字段应逐位一致；本次得到支持。
- 决定：接受可复现性与逐笔差异收口；冻结 repaired `confirmation_close` baseline 进入下一道样本 census，不改变生产配置。

## 冻结戳

| 项目 | SHA256 / 值 |
|---|---|
| Git commit | `21564d296b53309ecc4e640964b3ffafce3585b7` |
| `config/settings.toml` | `be7ec39ec21f6a838571511cb2cd0e290263031b521a9a07a6fb70164b8ef4bf` |
| `config/experiments.toml` | `7e6eca2609546d94293162870df6cc6ab8795666845b58facd979b698917dbe1` |
| runner | `f6e34570b6f7a97ffb448cf30049501ae57242a54f90579ebacaf905f6eaa0b7` |
| protocol | `2408baa4f3d85ce27036812cd71dbf1061a07e767b693fb418a339ab2e611553` |
| 2024-07-01 输入 digest | `224a6132dc45125c90fc29e11134f19e9334ab2899875052b4329b67686ccbdb` |
| 2025-06-01 输入 digest | `0c00940908744e2ccaf35e20a309a3d56e90ed7e161a7bf7713a9a713733159a` |

A 运行创建于 `2026-10-10T02:37:51Z`，B 运行创建于 `2026-10-10T03:03:57Z`。两次都由 `scripts/review_atr_fixed_history.py` 在独立输出目录运行。

## 确定性双跑

Canonical 规则：递归剥离 `run_id`、`trade_id`、`event_id`；只剥离 result 级和 dynamic-universe summary 级运行创建时间，保留每笔交易自身的 `created_at_utc`、入场、出场、事件、费用、滑点和 P&L。

| 分支 | A/B canonical SHA256 | 结果 |
|---|---|---|
| 2024-07-01 / legacy / baseline | `ca51f2148f56ed7e65bce54d24feef35dbe788cdfc018c99df0f9191ce570c43` | PASS |
| 2024-07-01 / legacy / ATR0.35 | `7e8e1d5952f084ae1be000c7f906a36f83db6e206192b7be59b9286eb9785046` | PASS |
| 2024-07-01 / confirmation / baseline | `5017a347b447ea42ceeccb179da665fa43fa031768942659f24894b69be0fddf` | PASS |
| 2024-07-01 / confirmation / ATR0.35 | `2893a85fe11855bfbcf9f6f1cf706163dd3918aa4d43f974a579f445bf4bed7b` | PASS |
| 2025-06-01 / legacy / baseline | `c99336cd2c5c67a90bef93f97d9c40a12e2fd9706e9231589ad1352bdb4635b6` | PASS |
| 2025-06-01 / legacy / ATR0.35 | `d7be97db7b79de1625a998cb30e30a4e5112cac05df61219599bc36ceede7114` | PASS |
| 2025-06-01 / confirmation / baseline | `e5e548233e894f5a997a68fc404515c9be0cfb831ee4cbcc97a565598df27b5d` | PASS |
| 2025-06-01 / confirmation / ATR0.35 | `5e43b19e41eb727a60ac8e4c6c0e77f2e350018f55e4b121dae9815d33745f0a` | PASS |

输入 JSON 的原始文件 SHA256 也分别一致：早窗 `4f1b3edd06176d11284d2b70e043ef30a1cab20d0131860bfe37e1511d548d2f`，近窗 `4bf8f8f0690b82f07988fff9bf194ec4e2e62eb730331abb20a633cfca51d0df`。

## 修复后 baseline 复现值

| 窗口 | 计划数 | 入场数 | 平仓数 | 净收益 | PF | 最终权益 |
|---|---:|---:|---:|---:|---:|---:|
| 2024-07-01 至 2025-06-01 | 489 | 83 | 80 | 4.7199% | 1.1198 | 10471.99 |
| 2025-06-01 至 2026-06-01 | 386 | 51 | 51 | -1.5074% | 0.9515 | 9849.26 |

## 口径差异

### 当前 legacy baseline → confirmation-close baseline

该比较直接隔离成交确认时序，但组合路径会随之改变，不能把权益差全部理解为单笔成交价影响。

| 窗口 | 平仓数 | 净收益 | PF | 最终权益变化 | 共同平仓 P&L 变化 | legacy-only 平仓 | confirmation-only 平仓 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2024-07-01 | 76 → 80 | -1.9952% → 4.7199% | 0.9516 → 1.1198 | +671.52 | -741.70 | 23 / -722.64 | 27 / +818.84 |
| 2025-06-01 | 58 → 51 | 4.5509% → -1.5074% | 1.1423 → 0.9515 | -605.83 | -1028.57 | 20 / -418.62 | 13 / -87.91 |

### 旧存档 baseline → 当前 repaired legacy baseline

| 窗口 | 平仓数 | 净收益 | PF | 最终权益变化 | 交易集合变化 |
|---|---:|---:|---:|---:|---|
| 2024-07-01 | 76 → 76 | -2.0854% → -1.9952% | 0.9497 → 0.9516 | +9.01 | 76 个共同平仓；无 old/new-only |
| 2025-06-01 | 57 → 58 | 3.1141% → 4.5509% | 1.1084 → 1.1423 | +143.68 | 54 个共同平仓；3 old-only、4 new-only |

根因收口：

- 130 笔共同平仓的信号与入场字段全部一致；早窗为 15 笔完全不变、60 笔记账/资金路径变化、1 笔 EMA 时序变化，近窗为 35 / 17 / 2 笔。
- 3 笔 EMA 时序变化为 SUI、BNB、PEPE；事件记录均显示旧路径在本根抬升 EMA 后立即触发，新路径从下一根使用新 stop。
- 近窗 7 条 old/new-only 中，6 条是满 5 仓导致同计划入场换位或后续计划接续；1 条 SOL 是 scanner/signal-set 演化，当前计划比旧计划提前 4 小时且 entry/TP/score 不同。
- `UNKNOWN`：固定窗口重算的 market-regime 时间轴中 `UNKNOWN=0`，本批没有可归因影响。
- 断档：8 个分支的 `gap_affected_trades` 均为 0。
- 权益对账：早窗 +9.0137、近窗 +143.6756 的最终权益变化均由共同平仓、old/new-only 和同键未平仓盯市闭合。
- 完整逐笔证据：`reports/2026-10-10/baseline_gate_1_trade_diff_2026-10-10_v1.md`。

## `paired_closed_trades=0` 并行初查

最新 independent shadow 报告中，旧 `CONFIG_CHANGED` epoch 与当前 `ACTIVE` epoch 的 baseline/ATR 两条线均为 `opportunities=0 / entered=0 / closed_trades=0`。因此当前独立账本的零配对首先是上游机会真空，不是“已有双方平仓但配对键匹配失败”。reconciliation/maturity 报告中的旧 plan-linked rows 属于另一条历史 shadow 证据路径，不能补记为 independent paired closed trades。

该结论解决当前 independent epoch 的三分诊断：零配对是当前 epoch 上游机会真空，而不是已有双方平仓的配对键 bug。旧 plan-linked cohort 属于另一条历史证据路径，应在闸门 2 按 clean/contaminated 口径处理，不能补记为 independent paired closed trades。

## 闸门判定

- 确定性：PASS。
- 冻结输入：PASS。
- 当前执行语义记录：PASS，沿用 `confirmation_close`、已生效 stop 检查、本根收盘 EMA 下一根生效、断档不伪装真实前向表现。
- 新旧变化幅度：PASS，已量出。
- 新旧变化逐项根因归属：PASS；`stop_or_ema_accounting`、`scanner_or_signal_set` 均有证据，`unresolved=0`。
- 总裁决：`pass_no_unresolved_trade_diff`，闸门 1 完成。

## 下一步

按依赖进入闸门 2：以 repaired `confirmation_close` baseline 为唯一输入，清点 clean/contaminated、缺口、容量与存续币偏差，先取得真实 N，再判断是否足以进入闸门 3。闸门 1 未修改生产配置，也没有启动新参数实验。
