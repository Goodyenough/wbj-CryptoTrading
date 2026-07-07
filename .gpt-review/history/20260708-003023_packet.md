# GPT 评审包：CryptoTrading 项目阶段简报与后续计划复核

## 你需要完成的任务

请作为独立评审者，复核下面这份 Codex 对 CryptoTrading 项目的阶段简报和后续计划。重点判断：

1. 当前“不修改 `settings.toml`，继续 daily + 4h 观察到 2026-07-16 左右再 audit”的决策是否理性。
2. 目前把问题重点放在“选币/入场质量”而不是立即改退出或防守规则，是否有足够证据支持。
3. 7 月 16 日前后要做的下一轮 audit 和 A/B 实验计划是否完整、可执行、风险可控。
4. 是否存在被低估的风险、遗漏的验证项、或应该提前触发 `retest/fix` 的条件。

请不要泛泛鼓励。请指出不严谨、不足、或可能误判的地方，并给出具体修正建议。

## 项目背景

项目目录：

```text
D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects
```

这是一个加密货币策略工程，包含：

- 市场扫描；
- paper trading；
- SQLite 数据库记录；
- daily 定时任务；
- 4h paper update 定时任务；
- paper report / dashboard；
- A/B 回测与实验报告；
- 企业微信通知；
- Obsidian / reports 归档。

当前重点不是上线真实交易，而是验证 paper 观察链路、关键防守机制，以及找出策略没有赚钱的主要原因。

## 当前事实

### 1. 自动任务与数据库链路

已确认：

- daily 和 4h 定时任务近期可运行。
- SQLite 数据库 schema version 为 2。
- WAL、FK、UTC、index/table 健康检查通过。
- `stale running = 0`。
- 企业微信通知已接入。
- `settings.toml` 配置 hash 稳定为：

```text
be7ec39ec21f6a83
```

最近一次数据库状态检查：

- latest run: `20260707_161003_d8630195`
- mode: `paper_4h_update`
- status: success
- UTC time: `2026-07-07T16:10:03Z`
- Beijing time: `2026-07-08 00:10`
- config hash: `be7ec39ec21f6a83`

最近一次失败 run：

- `20260704_161005_4e047f61`
- failure reason: timeout

当前计划统计：

- open plans: 2
  - WLDUSDT `616e1bbfd4c6`, status `ENTERED`
  - ONDOUSDT `9734a33dea2e`, status `WATCHING`
- plan counts:
  - ARCHIVED: 13
  - ENTERED: 1
  - INVALIDATED: 3
  - STOPPED: 7
  - WATCHING: 1
- event counts:
  - ENTERED: 8
  - STOPPED: 7
  - RECLAIM_PENDING_SET: 104
  - TP1: 0

### 2. 2026-07-02 阶段验收结论

7 月 2 日验收口径为：

- 总体 verdict: `keep_observing`
- 不是 `keep`
- 不证明策略长期盈利能力。

模块结论：

- 数据链路：基本通过。
- RISK_OFF：行为初步符合防守设计。
- RECLAIM_PENDING：当时没有观察到明显 material missed winner。
- 42-bar holding：维持当前默认。
- TP1 EMA trailing：样本不足，不评价好坏。
- 策略盈利能力：尚未证明。

验收强调：

- `keep_observing` 仅表示系统链路和关键防守机制没有发现重大问题。
- 不等于策略已经有效。
- 不应据此上线真实交易或扩大风险。

### 3. 最新 opportunity audit

最新审查报告：

```text
reports/2026-07-07/paper_opportunity_audit_2026-06-19_2026-07-02_demo_v1.md
```

窗口：

```text
2026-06-19 至 2026-07-02
```

BTC/ETH 基准：

- BTC: -2.13%
- ETH: -0.49%
- 解释：偏横盘或轻微下跌，不是强趋势上涨窗口。

Opportunity audit 汇总：

- `avoided_loser = 25`
- `missed_winner = 12`
- `false_entry = 7`
- `neutral_or_unknown = 34`

Entered trades 复盘归因：

- `entry_issue = 5`
- `selection_issue = 2`
- `exit_issue = 0`
- `open_unknown = 1`

初步解释：

- 当前亏损更像是选币/入场质量不足，而不是退出机制明显太差。
- 目前没有 TP1 样本，无法评价 TP1 EMA trailing。
- `missed_winner = 12` 说明 RECLAIM_PENDING 有机会成本，但还不足以直接证明防守规则过保守。
- `avoided_loser = 25` 高于 `missed_winner = 12`，防守规则仍可能有价值。

## Codex 当前建议

Codex 给出的阶段简报核心判断如下：

### 当前项目状态

项目现在处于：

```text
paper 观察期后半段 / 策略尚未证明盈利 / 系统链路基本可用 / 暂不改配置
```

可以确定的事情：

1. 工程链路基本跑通。
   - daily / 4h 定时任务可运行。
   - 数据库能记录 run、plan、event。
   - 报告、dashboard、企业微信通知能输出。
   - `settings.toml` hash 稳定。

2. 7 月 2 日验收不等于策略通过。
   - 验收结论是 `keep_observing`。
   - 主要通过的是数据链路和防守机制观察。
   - 没有证明策略长期盈利。

3. 当前策略样本暴露的问题主要是入场/选币。
   - 8 笔 entered trades 中，多数没有足够 MFE。
   - `TP1 = 0`，说明没有足够成功推进样本。
   - `exit_issue = 0`，暂时不能优先怪退出。
   - `entry_issue + selection_issue` 占主要比例。

4. RECLAIM_PENDING 不能简单取消。
   - 它确实可能错过机会。
   - 但 avoided losers 也不少。
   - 当前更合理的做法是继续观察机会成本，而不是立即放宽。

### 后面应该做什么

Codex 建议按以下顺序：

1. 继续冻结配置。
   - 不改 `settings.toml`。
   - 继续 daily + 4h。
   - 至少观察到 2026-07-16 左右。

2. 到 2026-07-16 左右跑下一次 audit。

命令：

```powershell
python main.py paper audit --account demo --start-date 2026-07-03 --end-date 2026-07-16 --no-obsidian
```

3. 用下一轮 audit 判断是否进入 A/B。

如果仍然出现：

- entered trades 多数无 MFE；
- `TP1` 仍然很少或为 0；
- `entry_issue / selection_issue` 继续主导；

才开始做 A/B。

4. A/B 优先级：

第一优先级：

```text
entry_reclaim_confirm_1bar
```

目的：

- 不再在刚 reclaim 时立即入场；
- 要求 reclaim 后至少 1 根 4h 继续站稳；
- 目标是过滤假 reclaim。

第二优先级：

```text
relative_strength_gate
```

目的：

- 要求候选币相对 BTC/ETH 有更强表现；
- 目标是提升选币质量。

第三步：

```text
entry_reclaim_confirm_1bar + relative_strength_gate
```

只有在前两个单变量 A/B 至少一个有正向证据后再组合。

### 不建议现在做的事情

Codex 不建议现在：

- 修改 `settings.toml`；
- 上线真实交易；
- 放宽 RECLAIM_PENDING；
- 因为 7 月 2 日亏损就立刻重写策略；
- 大量测试 50/60 根 holding bars；
- 在 TP1 样本为 0 时优化 TP1 EMA trailing。

理由：

- 当前样本不足。
- 过早改参数会破坏正在形成的 paper 可比性。
- 目前最需要回答的问题是“没赚钱的原因是什么”，不是直接追求参数优化。

## 已形成的 7 月 6 日 A/B 实验计划

已写入：

```text
2026-07-06-abtest-plan.md
```

核心内容：

- 现在不立即做 A/B。
- 等 2026-07-16 左右再跑 audit。
- 如果新 audit 仍支持“入场/选币问题主导”，再进行 A/B。
- A/B 必须单变量、可复核、不修改当前 paper 配置。

候选实验：

1. `entry_reclaim_confirm_1bar`
2. `relative_strength_gate`
3. 组合实验仅在单变量有效后执行。

## 需要 GPT 重点评审的问题

请逐条回答：

1. 在当前证据下，“继续冻结配置到 2026-07-16 再 audit”是否是合理选择？有没有应该提前修改策略的理由？
2. `avoided_loser=25`、`missed_winner=12`、`false_entry=7` 这个结构，是否支持“RECLAIM_PENDING 暂不放宽”的结论？
3. 8 笔 entered trades 中 `entry_issue=5`、`selection_issue=2`、`exit_issue=0`，是否足以把下一步重点放在选币/入场，而不是退出？
4. `missed_winner=12` 是否被低估？它应该触发什么额外检查？
5. 7 月 16 日下一轮 audit 需要新增哪些指标，才能更可靠地区分：
   - 选币问题；
   - 入场问题；
   - 防守规则过保守；
   - 市场环境不支持？
6. `entry_reclaim_confirm_1bar` 和 `relative_strength_gate` 哪个更适合作为第一个 A/B？为什么？
7. 在 2026-07-16 前，哪些异常情况应该提前触发 `retest` 或 `fix`，而不是继续等待？

## 期望输出格式

请按下面格式输出：

```markdown
## 总体判断

## 同意 Codex 的部分

## 不同意或需要修正的部分

## 被低估的风险

## 建议新增的验证指标

## 7 月 16 日前的触发条件

## A/B 优先级建议

## 最终建议路线
```

请明确区分：

- 已有事实；
- 从事实推出的判断；
- 仍然只是猜测的假设。

