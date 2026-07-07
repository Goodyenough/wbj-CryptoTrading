# GPT Review Summary

## 总体判断

GPT 的结论是：Codex 的总体方向基本正确，但应评为“有条件通过”，不能简单按原计划原样执行。

核心判断：

- 继续冻结当前 paper 配置是合理的。
- 现在不应修改 `settings.toml`。
- 7 月 16 日不应被视为唯一决策条件，应改成“日期检查点 + 有效成熟样本量 + 数据完整性”的三重条件。
- 当前证据支持优先调查入场和选币，但不能证明退出机制没有问题。
- `RECLAIM_PENDING` 暂不放宽是合理的，但不能仅凭 `avoided_loser=25 > missed_winner=12` 证明防守规则净收益为正。
- 7 月 16 日更适合作为阶段检查点；如果机会样本需要 42 根 4h K 线后验观察，则 7 月 16 日附近产生的样本尚未成熟。

## GPT 同意的部分

- 继续冻结当前 paper 配置。
- 不立即取消或放宽 `RECLAIM_PENDING`。
- 不在 `TP1=0` 的情况下优化 TP1 EMA trailing。
- A/B 应单变量进行，单变量有效后再测试组合。
- 不因短期亏损从零重写策略。

## GPT 要求修正的部分

- 将“观察到 2026-07-16”改为阶段检查点，而不是完整 audit 的固定最终截点。
- audit 应加入样本成熟规则，对右截尾样本标记 `right_censored` 或 `open_unknown`。
- `avoided_loser` 与 `missed_winner` 需要按 R 倍数和反事实 PnL 比较，不能只比次数。
- 需要解释数据库中 104 次 `RECLAIM_PENDING_SET` 与 audit 中 78 个分类样本之间的映射关系。
- 8 笔 entered trades 的归因只能说明下一步优先调查入场/选币，不能形成因果确认。
- `exit_issue=0` 只能写“暂未发现明确退出问题”，不能写“退出机制通过”。
- 7 月 16 日前可以做 shadow replay、指标定义、报告模板和 A/B 验收标准准备，不必等到 7 月 16 日才开始。
- 两个候选 A/B 变量目前还需要更精确定义。

## GPT 建议新增的验证项

- daily/4h 预期运行次数、实际运行次数、成功率、漏跑率、延迟和数据新鲜度。
- timeout 后是否补跑、是否影响关键 4h 状态。
- database/report/dashboard/notification 的一致性。
- plan/event 是否存在重复、越序、丢失或不可能状态。
- opportunity funnel：scan -> eligible -> RISK_OFF blocked -> RECLAIM_PENDING -> reclaim -> entered -> STOP/TP1/TIME_EXIT。
- 每层 funnel 的数量、转化率、去重规则、排除原因、成熟样本和未成熟样本。
- 入场后 1/2/4/12/42 根 4h K 的 MFE/MAE、MFE/MAE 顺序、0.5R/1R/TP1 触达比例。
- 选币时相对 BTC/ETH 和候选池中位数的强弱、winners/losers 的 RS 分布。
- `RECLAIM_PENDING` 的 avoided loser 与 missed winner 均按 R 计量，并计算净防守价值。
- 市场环境增加候选池上涨比例、相对 BTC 为正比例、RISK_OFF 覆盖时长、不同 regime 下的 entered/false entry/missed winner/avoided loser。
- A/B 使用 matched opportunities 做 paired comparison，避免因交易数量减少造成虚假改善。

## GPT 建议的触发条件

立即 `fix`：

- config hash 非预期变化。
- 时间戳、时区、K 线闭合逻辑错误。
- 使用未来数据或未收盘 K 线。
- STOP/TP1/ENTRY 无法用原始 OHLC 复核。
- plan/event 状态越序、重复或丢失。
- 数据库与 dashboard/report 结果不一致。
- 漏跑后未补算且影响关键 4h 状态。
- 连续两次 scheduled run 失败。
- 窗口内任务漏跑率超过预设阈值，例如 5%。
- 同一输入和配置无法复现结果。

提前 `retest`：

- 新增连续 4 笔成熟入场均止损，且均未达到 meaningful MFE。
- 多笔交易重复出现相同假 reclaim 路径。
- 至少 3 个去重 missed winner 被同一条件拦截，且原 stop/TP1 回放均先到 TP1。
- 按 R 计量的 missed-winner 损失明显超过 avoided-loser 收益，例如超过 1.5 倍。
- `neutral_or_unknown` 持续过高，使 audit 无法给出明确结论。
- timeout 或数据延迟与异常入场、漏入场存在时间关联。
- 1-bar shadow replay 稳定过滤多数 false entry，且未显著增加 missed winner。

## GPT 对 A/B 优先级的建议

- 不能仅凭 `entry_issue=5` 直接确认 `entry_reclaim_confirm_1bar` 一定第一。
- 应先做不改变 paper 配置的诊断性 shadow replay。
- 如果 false entries 主要来自 reclaim 后立即失败，并且 1-bar replay 能过滤大部分，同时不过度损害 winners，则优先 `entry_reclaim_confirm_1bar`。
- 如果 false entries 主要来自币种本身持续弱于市场，且 winners/losers 在入场前 RS 已有明显分离，则优先 `relative_strength_gate`。
- 组合实验只能在至少一个单变量改善 primary metric 且未突破 guardrail 后执行。

## GPT 最终建议路线

- 现在至 2026-07-16 继续冻结 live paper 配置。
- 立即补强 audit 规范，而不是等待。
- 立即解释 104 次 pending event 与 78 个 audit 分类样本的差异。
- 7 月 16 日前完成两个候选变量的 shadow replay。
- 将 2026-07-16 定义为阶段检查点。
- 完整 audit 必须避免右截尾；若需要 42 根 4h K 后验观察，则 7 月 16 日只对约 7 月 9 日及以前机会做完整归类，或在约 7 月 23 日后完整评估截至 7 月 16 日的机会。
- audit 后先确认问题类型，再确定正式 A/B 顺序。
- 当前总体状态仍为 `keep_observing`。

