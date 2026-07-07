# Codex 对 GPT 评审的处理

## 总体判断

采纳 GPT 的核心修正。原路线“不改配置、继续观察、后续做 audit 和 A/B”仍成立，但需要把 2026-07-16 从“完整决策日”改成“阶段检查点”，并提前补齐 audit 口径、样本成熟规则、右截尾标记、反事实 R 倍数计量和 A/B 验收标准。

## 接受的意见

- 继续冻结当前 paper 配置，不修改 `settings.toml`。
- `keep_observing` 仍是当前合理状态，不能写成策略有效。
- 7 月 16 日改为阶段检查点，不保证当天能形成完整策略结论。
- audit 必须区分成熟样本和未成熟样本，未成熟样本标记为 `right_censored` 或 `open_unknown`。
- `avoided_loser` 与 `missed_winner` 不能只比次数，必须增加 R 倍数或反事实 PnL。
- 需要解释 `RECLAIM_PENDING_SET=104` 与 audit 分类样本 78 的映射关系。
- 入场/选币是下一步优先调查方向，但不是已完成因果确认。
- `exit_issue=0` 只表示暂未发现明确退出问题，不表示退出机制通过。
- 7 月 16 日前可以做 shadow replay 和 audit/A/B 规范补强。
- A/B 必须使用 matched opportunities 做 paired comparison，并设置交易数、样本保留率、missed winner 增量等 guardrails。

## 部分接受的意见

- GPT 建议新增的市场环境指标很完整，但实现上应分阶段做。第一阶段先补候选池上涨比例、候选池相对 BTC 为正比例、RISK_OFF 覆盖时长和不同 regime 下的关键分类；更复杂的波动率/宽度指标可后续扩展。
- GPT 给出的 fix/retest 阈值可作为预注册草案，但具体数值如漏跑率 5%、missed-winner 损失 1.5 倍，需要结合项目数据可得性和样本量再落地。
- 两个 A/B 候选变量需要补定义，但暂不应立即变成正式实验。先做 shadow replay，确认哪个变量更接近真实问题来源。

## 拒绝的意见及原因

暂无明确拒绝项。GPT 的意见基本都与当前项目约束一致。

## 暂缓的意见及验证条件

- 完整的反事实资金容量和并发仓位模拟暂缓。先以 plan/opportunity 级 R 倍数计量为主，若结果显示 missed winner 经济影响较大，再加入资金占用和并发限制。
- 全量跨 regime A/B 暂缓。当前先保证 2026-06-19 以来 paper 链路和 audit 口径正确，再用历史回测窗口补跨 regime 验证。

## 已对方案作出的修正

修正后的后续路线：

1. 继续冻结 `settings.toml`，daily + 4h 正常运行。
2. 立即补强 `paper audit` 规范：
   - 样本成熟规则；
   - `right_censored/open_unknown` 标记；
   - 104 pending events 到 78 audit samples 的映射说明；
   - R 倍数反事实 PnL；
   - opportunity funnel；
   - 数据链路一致性；
   - A/B primary metric 和 guardrails。
3. 7 月 16 日前做两个 shadow replay：
   - `entry_reclaim_confirm_1bar`；
   - `relative_strength_gate`。
4. 2026-07-16 只作为阶段检查点：
   - 若成熟样本足够，生成正式 audit；
   - 若成熟样本不足，只生成 interim report；
   - 若需要 42 根 4h 后验观察，则约 2026-07-23 后再完整评估截至 2026-07-16 的机会。
5. 根据 shadow replay 和下一轮 audit 决定正式 A/B 顺序：
   - 假 reclaim 主导：先测 `entry_reclaim_confirm_1bar`；
   - 弱币选择主导：先测 `relative_strength_gate`；
   - 市场缺乏机会：继续观察，不急于改策略；
   - 防守规则净机会成本明显为负：单独设计 `RECLAIM_PENDING` 分层或阈值实验；
   - 数据链路异常：先 fix，策略结论作废。

## 仍未解决的分歧

没有实质分歧。剩余问题是执行顺序和实现成本控制：

- audit 补强要先做最关键字段，不一次性过度工程化。
- shadow replay 要与 live paper 隔离，不能影响当前配置和 paper 状态。

## 是否建议再进行一轮 GPT 复审

暂不需要。下一步应先把修正后的路线写入项目计划或 TODO，并实现 audit 规范补强与 shadow replay 设计。

