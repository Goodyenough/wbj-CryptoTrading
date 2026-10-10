# Baseline 盈亏归因闸门 1：可复现性与口径冻结

Taskboard：`CRYPTOTRADIN-122`  
状态：`in_progress`  
裁决：`determinism_pass_scope_diff_partial`

## 白话结论

修复后固定历史 replay 可以稳定复现。完全相同的代码、配置、历史币池和本地 K 线缓存连续运行 A/B 两次，8 个预声明分支剥离随机生成的 `run_id / trade_id / event_id` 和运行时间戳后，业务内容 checksum 全部一致；两个窗口的输入 hash 也完全一致。

但闸门 1 尚未全部通过。现有 runner 能比较旧存档、`legacy_same_bar` 和 `confirmation_close` 的交易及 P&L 变化，却不能把近窗全部差异严格拆成 stop 计价、EMA 时序、scanner 演化等单一根因。近窗旧存档到当前 legacy baseline 出现 3 笔 old-only 和 4 笔 new-only 平仓，现有报告也已声明当前 scanner 与旧研究版本不同。因此现在只能确认“结果可复现”和“变化幅度已量出”，还不能声称“所有变化均已逐项归因”。闸门 2 暂不启动。

## 系统目标、问题与路线图位置

- 系统目标：判断修复后的 reference baseline 在费用、滑点、容量和执行约束下是否存在可信优势。
- 本闸门唯一问题：相同输入能否得到相同交易与逐笔 P&L，并且旧新口径差异是否足够清楚，能安全进入样本清点。
- 路线图位置：闸门 1（可复现性与口径冻结）→ 闸门 2（clean 样本 census）→ 闸门 3（成本栈与亏损机制）。
- 当前决定：确定性检查通过；根因拆解部分通过，`CRYPTOTRADIN-122` 保持 `in_progress`，不放行 `CRYPTOTRADIN-123`。

## 事实、观察、假设、决定

- 事实：A/B 两次运行使用同一 commit、settings、experiments、runner、协议和数据输入；全部 canonical checksum 一致。
- 事实：运行只读 SQLite 与本地缓存，禁止网络补数；没有修改生产配置。
- 事实：旧存档到当前 legacy baseline 的早窗交易集合相同；近窗交易集合发生变化。
- 观察：原始 JSON SHA256 不同，差异来自每次运行随机生成的身份字段和运行时间戳，不是交易路径或 P&L 漂移。
- 假设：剥离运行身份字段后，业务字段应逐位一致；本次得到支持。
- 决定：接受可复现性；不接受“旧新差异已完全归因”，闸门 1 继续停留在根因 diff 收口。

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

根因状态：

- stop 计价 / EMA 时序：修复已由测试和工程报告证明，但当前 A/B runner 的两个 timing 分支都使用修复后引擎，没有同输入的单修复 counterfactual，不能把上述全部 P&L 差异拆给二者。
- entry timing：`legacy_same_bar` 与 `confirmation_close` 直接比较，结果高度路径敏感。
- `UNKNOWN`：固定窗口重算的 market-regime 时间轴中 `UNKNOWN=0`，本批没有可归因影响。
- 断档：8 个分支的 `gap_affected_trades` 均为 0。
- scanner 演化：近窗出现交易集合变化，且既有报告明确声明当前 scanner 与旧研究版本不同，因此保留为未拆分混合项。

## `paired_closed_trades=0` 并行初查

最新 independent shadow 报告中，旧 `CONFIG_CHANGED` epoch 与当前 `ACTIVE` epoch 的 baseline/ATR 两条线均为 `opportunities=0 / entered=0 / closed_trades=0`。因此当前独立账本的零配对首先是上游机会真空，不是“已有双方平仓但配对键匹配失败”。reconciliation/maturity 报告中的旧 plan-linked rows 属于另一条历史 shadow 证据路径，不能补记为 independent paired closed trades。

该结论只解决当前 independent epoch 的三分诊断；旧 cohort 的逐行配对键审计仍属于后续收口项，不改变闸门 1 当前状态。

## 闸门判定

- 确定性：PASS。
- 冻结输入：PASS。
- 当前执行语义记录：PASS，沿用 `confirmation_close`、已生效 stop 检查、本根收盘 EMA 下一根生效、断档不伪装真实前向表现。
- 新旧变化幅度：PASS，已量出。
- 新旧变化逐项根因归属：PARTIAL；近窗仍有 scanner / 路径混合项。
- 总裁决：`determinism_pass_scope_diff_partial`，闸门 1 保持进行中，闸门 2 不启动。

## 下一步

只补闸门 1 的最小缺口：把旧存档与当前 repaired baseline 的增删改交易清单按 `stop_or_ema_accounting / scanner_or_signal_set / unresolved` 分类；如果无法在不新增策略逻辑的情况下完成，就将闸门 1 正式判为“基础设施阻塞”，再决定是否补最小诊断能力。不得提前进入样本归因或参数实验。
