# Baseline 盈亏归因闸门 2：clean 样本 census

Taskboard：`CRYPTOTRADIN-123`
状态：`done`
裁决：`C_insufficient_clean_evidence`

## 白话结论

闸门 2 已经数清楚样本，但不能放行闸门 3。

两个窗口共有 134 笔已入场 baseline 交易，其中 131 笔完整平仓，交易期内 4h 缺口为 0。单看闭合度，数据看起来足够；但冻结协议使用“当前仍在 Binance 上市的币”构成历史 symbol master，历史已退市币从候选池中消失，因此 134/134 都带 cohort 级 `survivorship_suspect`。这不是某几笔可以单独摘掉的瑕疵：被遗漏的历史候选可能改变每日排名、入场集合和 5 仓容量路径。

容量污染也不是小项。31 笔入场发生在同一决策时点还有候选因 `max_active_positions=5` 被拒的情况下。早窗中，排除这些容量竞逐交易后剩余 63 笔净亏 134.63 USDT；17 笔容量竞逐交易却净赚 702.63 USDT，把全体 80 笔平仓结果翻成净赚 568.00 USDT。污染组直接改变了方向，触发预声明的 C 类停止条件。

因此，本批可以说明“在当前存续币样本和既有容量路径里发生了什么”，但不能作为 clean baseline 样本回答普遍盈利/亏损机制。闸门 3 不启动，生产配置不变。

## 系统目标、唯一问题与判定标准

- 系统目标：判断修复后的 reference baseline 是否有足够 clean、闭合、无缺口样本，支持成本栈与亏损机制归因。
- 唯一问题：严格 clean 的真实 N 是否能在两个窗口形成方向判断，且污染不主导结论。
- 路线图位置：闸门 1 已通过；本报告是闸门 2 的唯一 census；只有通过才允许进入闸门 3。
- 支持：两个窗口都有可分层的 strict-clean 交易，且污染组不会改变 clean 方向。
- 拒绝/停止：strict-clean 样本不足，或污染组与 clean/条件清洁组方向冲突并主导组合结果。
- 证据不足：无法把执行/数据伪影与策略结果分开；结论落 C，不硬做机制归因。

## 冻结输入与执行口径

- 场所与标的：Binance Spot USDT，冻结旧 run 的逐日 selected symbols。
- 周期与窗口：4h；`[2024-07-01, 2025-06-01)`、`[2025-06-01, 2026-06-01)`，UTC。
- 入场：`confirmation_close`，确认收盘价加配置滑点，入场 bar 不再用于退出。
- 退出：已生效 stop 先检查；本根收盘 EMA 从下一根生效；stop gap 按 `min(open, stop)` 后计滑点。
- 资金：初始 10,000 USDT，单笔风险 1%，总活跃风险 5%，最多 5 仓、10 个计划，无杠杆，无强制期末平仓。
- 成本：入场/TP2 maker 4 bps，stop taker 10 bps，入场滑点 5 bps、stop 滑点 10 bps。
- 早窗结果 SHA256：`e589f10536cf1771523199116d1dfd36b64abf46091333604cd91e1f41000025`。
- 近窗结果 SHA256：`cab46e67662a791ddd5e7581a30651021925011af0079b7de48f07302e9df435`。

## clean 与 reason code 定义

一笔 strict-clean 交易必须同时满足：已入场且完整闭合、入场到退出无缺失 4h bar、入场决策没有容量竞逐、没有存续币偏差、没有其他状态或字段异常。

| reason code | 机械判定 |
|---|---|
| `gap_filled` | 交易从确认 bar 到退出期间缺少预期 4h bar。 |
| `capacity_distorted` | 该交易入场的同一 `decision_time_utc`，至少有一个合格候选因 `max_active_positions` 被拒；表示样本归属受容量排序影响，不表示容量规则本身是 bug。 |
| `survivorship_suspect` | 冻结 dynamic master 来自 current `exchangeInfo`，历史已退市币不在 master；该限制会通过候选排序和容量路径影响整个 cohort，因此逐笔继承。 |
| `other` | 已入场但期末未平仓，或缺少闭合所需字段。本批仅为 3 笔期末右删失。 |

reason code 允许一笔交易多选；`clean` 只在 reason code 为空时成立。逐笔记录见 `baseline_gate_2_trade_census_2026-10-10_v1.csv`，聚合原始值见 `baseline_gate_2_census_summary_2026-10-10_v1.json`。

## Strict census

| 窗口 | 计划 | 已入场 | 完整闭合 | 右删失 | strict clean | contaminated | `gap_filled` | `capacity_distorted` | `survivorship_suspect` | `other` |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2024-07-01 至 2025-06-01 | 489 | 83 | 80 | 3 | 0 | 83 | 0 | 18 | 83 | 3 |
| 2025-06-01 至 2026-06-01 | 386 | 51 | 51 | 0 | 0 | 51 | 0 | 13 | 51 | 0 |
| 合计 | 875 | 134 | 131 | 3 | 0 | 134 | 0 | 31 | 134 | 3 |

完整闭合率为 `131 / 134 = 97.76%`。但 strict-clean 闭合率无法计算，因为 strict-clean 分母为 0。strict clean 按 regime、symbol、月份的分层表均为空；这不是缺少聚合能力，而是没有任何交易通过全部清洁条件。

## 条件诊断：只忽略全局幸存者偏差

下表不是 clean 结论，只用于判断其他污染是否会主导方向。`execution-clean conditional` 表示完整闭合、无缺口、无同决策时点容量竞逐，但仍带 `survivorship_suspect`。

| 窗口 | 分组 | N | 胜/负 | 净 P&L | PF |
|---|---|---:|---:|---:|---:|
| 早窗 | execution-clean conditional | 63 | 26 / 37 | -134.63 | 0.9661 |
| 早窗 | capacity-contested | 17 | 10 / 7 | +702.63 | 1.9103 |
| 早窗 | 全部闭合 | 80 | 36 / 44 | +568.00 | 1.1198 |
| 近窗 | execution-clean conditional | 38 | 15 / 23 | -248.92 | 0.8942 |
| 近窗 | capacity-contested | 13 | 6 / 7 | +98.18 | 1.1298 |
| 近窗 | 全部闭合 | 51 | 21 / 30 | -150.74 | 0.9515 |

早窗的容量竞逐组不只是影响幅度，而是把净收益从负翻成正，因此“污染不主导结论”不成立。近窗方向没有翻转，但容量竞逐组仍抵消了 98.18 USDT 的亏损。

## 条件分层覆盖

由于 strict clean 为 0，以下仍是带幸存者偏差的 conditional 诊断，不用于放行闸门 3。

| 窗口 | conditional N | RISK_ON | NEUTRAL | RISK_OFF | UNKNOWN | 覆盖月份 | distinct symbols |
|---|---:|---:|---:|---:|---:|---:|---:|
| 早窗 | 63 | 22 | 41 | 0 | 0 | 9 | 40 |
| 近窗 | 38 | 17 | 17 | 4 | 0 | 8 | 29 |

月份分布：

- 早窗：2024-07 `5`、08 `1`、09 `9`、10 `9`、11 `14`、12 `9`、2025-01 `7`、04 `5`、05 `4`。
- 近窗：2025-06 `9`、07 `6`、08 `5`、09 `2`、10 `3`、2026-01 `6`、04 `4`、05 `3`。

逐 symbol 计数保存在 summary JSON；早窗单 symbol 最多 4 笔，近窗最多 4 笔，不能靠少数 symbol 构成严格 clean 分层，因为 strict clean 本身为 0。

## 闸门 3 数据可用性

- 每笔 entry/exit fee、slippage、gross/net P&L：有。
- 同决策时点 `max_active_positions` blocked events：有。
- MAE/MFE：交易记录中没有，若未来进入机制分层需要另行计算。
- 交易期内 4h gap 审计：有，本批为 0。

这些字段足以做条件成本栈，但不足以推翻本闸门的 clean 结论；不能因为技术上“算得出来”就跳过污染门槛。

## 事实、观察、假设与决定

- 事实：134 笔入场、131 笔完整闭合、3 笔期末右删失；交易期缺口为 0。
- 事实：134/134 继承冻结协议明确声明的 current-master 幸存者偏差；31/134 还有同决策时点容量竞逐。
- 观察：忽略幸存者偏差后，两个窗口的 conditional execution-clean 都为净亏；容量竞逐组两个窗口都为净赚，并在早窗翻转组合收益方向。
- 假设：如果污染不主导，则排除容量竞逐不应改变窗口方向；早窗结果否定该假设。
- 决定：落 C（证据不足），不是 A（找到可实验机制）也不是 B（证明无优势）。闸门 3 不启动。

## 闸门裁决

- 样本数量已查明：PASS。
- 闭合与缺口：PASS，131 笔闭合且 0 笔 gap affected。
- strict clean 跨窗口样本：FAIL，两个窗口均为 0。
- 污染不主导：FAIL，容量竞逐组翻转早窗收益方向。
- 总裁决：`C_insufficient_clean_evidence`。

下一步需要项目所有者在两条路中选择：补 point-in-time 历史 symbol master（包含历史已退市币）后重跑闸门 1/2，或暂停历史 baseline 机制归因、等待冻结版本的自然前向 clean 样本。除非明确批准重新定义为“仅研究当前存续币的条件结果”，否则不得降低 clean 标准，也不得启动闸门 3。
