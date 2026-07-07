# 2026-07-08 Audit 规范补强与 Shadow Replay 计划

## 背景

本计划用于承接 2026-07-07 `paper audit` 和 GPT 复核后的修正意见。

当前项目状态仍是：

```text
keep_observing
```

含义：

- paper 链路基本可用；
- 当前配置继续冻结；
- 不证明策略已经长期有效；
- 不修改 `settings.toml`；
- 后续重点从“有没有赚钱”转为“没赚钱的原因是什么”。

最近一次 audit：

```text
reports/2026-07-07/paper_opportunity_audit_2026-06-19_2026-07-02_demo_v1.md
```

关键结果：

- BTCUSDT: -2.13%，趋势偏横盘；
- ETHUSDT: -0.49%，趋势偏横盘；
- `avoided_loser=25`;
- `missed_winner=12`;
- `false_entry=7`;
- `neutral_or_unknown=34`;
- entered trade 归因：`entry_issue=5`，`selection_issue=2`，`exit_issue=0`，`open_unknown=1`。

GPT 复核后的核心修正：

- 2026-07-16 只能作为阶段检查点，不应自动视为完整结论日；
- audit 需要区分成熟样本与右截尾样本；
- `avoided_loser` 与 `missed_winner` 不能只比次数，必须补 R 倍数或反事实 PnL；
- 必须解释 `RECLAIM_PENDING_SET=104` 与 audit 分类样本 78 的映射关系；
- A/B 之前先做不改变 paper 配置的 shadow replay。

## 总原则

### 不变事项

- 不修改 `settings.toml`。
- 不修改当前 live paper 状态机。
- 不补跑或重算已有 paper 状态。
- daily + 4h 继续按现有任务运行。
- 任何 A/B 或 shadow replay 都必须与 live paper 隔离。

### 7 月 16 日定位

2026-07-16 不再定义为“最终审判日”，而是定义为：

```text
阶段检查点
```

当天应先判断：

- 数据链路是否完整；
- daily / 4h 运行是否连续；
- config hash 是否稳定；
- 成熟 entered trades 是否足够；
- 成熟 opportunity 样本是否足够；
- 未成熟 / 右截尾样本比例是否过高。

如果样本不足，只输出 interim report，不强行得出策略结论。

## Audit 补强要求

### 1. 样本成熟规则

每个 opportunity / entered trade 必须标记成熟状态：

| 字段 | 含义 |
|---|---|
| `maturity_status` | `mature` / `right_censored` / `open_unknown` / `data_gap` |
| `observation_bars` | 信号后可观察的 4h K 数量 |
| `required_bars` | 判定所需的最小 4h K 数量 |
| `observation_end` | 实际观察截止时间 |
| `classification_final` | 当前分类是否可作为最终分类 |

建议默认：

```text
required_bars = 42
```

理由：当前策略已有 42 根 4h 的 max holding 观察口径，机会后验也应避免过短窗口误判。

若在 2026-07-16 执行 audit：

- 只对约 2026-07-09 及以前产生的 opportunity 做完整成熟分类；
- 2026-07-10 至 2026-07-16 的新 opportunity 应标记为 `right_censored` 或 `open_unknown`；
- 若要完整评估截至 2026-07-16 的机会，应等到约 2026-07-23 之后。

### 2. 104 pending events 到 78 audit samples 的映射

必须在 audit 中新增一段 reconciliation：

```text
raw_RECLAIM_PENDING_SET_events
deduped_reclaim_plans
scan_candidate_opportunities
entered_false_entries
excluded_events
final_classified_opportunities
```

每个数字必须说明：

- 来源表；
- 过滤条件；
- 去重键；
- 排除原因；
- 是否只统计正式窗口；
- 是否包含 WATCH_ONLY / REJECT / ENTERED_TRADE false entry。

当前必须优先解释：

```text
RECLAIM_PENDING_SET=104
audit opportunity rows=78
```

否则不能用 `avoided_loser` 与 `missed_winner` 的数量差做强结论。

### 3. R 倍数反事实计量

每个 opportunity 应补充：

| 字段 | 含义 |
|---|---|
| `risk_R` | `entry - stop` |
| `mfe_R` | 后续最大有利波动，按 R 计 |
| `mae_R` | 后续最大不利波动，按 R 计 |
| `counterfactual_pnl_R` | 若按原 entry/stop/TP1 执行的估计 R 结果 |
| `first_hit` | `stop_first` / `near_tp1_first` / `tp1_first` / `none` |
| `time_to_first_hit_bars` | 首次触达关键路径的 4h K 数 |

阶段性判断必须从：

```text
avoided_loser count vs missed_winner count
```

升级为：

```text
avoided_loss_R vs missed_profit_R
```

建议新增净防守价值：

```text
defense_net_R = avoided_loss_R - missed_profit_R
```

只有当 `defense_net_R` 明显为正，且成熟样本足够，才可以说 `RECLAIM_PENDING` 的阶段性净价值偏正。

### 4. Opportunity funnel

新增 funnel：

```text
scanned
-> eligible
-> BUY_CANDIDATE / WATCH_ONLY / REJECT
-> blocked_by_RISK_OFF
-> RECLAIM_PENDING
-> reclaim_confirmed
-> entered
-> STOP / TP1 / TIME_EXIT / still_open
```

每一层输出：

- count；
- conversion rate；
- dedupe key；
- excluded count；
- mature count；
- right-censored count。

用途：

- 区分“市场没有机会”和“系统错过机会”；
- 区分“防守有效”和“防守过度保守”；
- 区分“选币问题”和“入场确认问题”。

### 5. 数据链路一致性

audit 报告必须包含：

- daily 预期次数 / 实际成功次数 / 失败次数；
- 4h 预期次数 / 实际成功次数 / 失败次数；
- scheduled run success rate；
- timeout / failed run 是否影响关键状态；
- config hash 是否稳定；
- database / report / dashboard / WeCom notification 是否一致；
- stale running 是否为 0；
- plan/event 是否存在越序、重复、丢失或不可能状态。

若出现以下任一项，策略结论必须降级：

- config hash 非预期变化；
- 连续两次 scheduled run 失败；
- 任务漏跑影响关键 4h 状态；
- STOP / TP1 / ENTRY 无法用 OHLC 复核；
- 数据库与 dashboard / report 结果不一致；
- plan/event 状态异常。

## Shadow Replay 计划

Shadow replay 的目标是：

```text
在不改变 live paper 配置的前提下，评估候选规则如果当时启用，会怎样影响 false entries、missed winners 和期望 R。
```

### Replay A: entry_reclaim_confirm_1bar

待定义清楚的规则：

```text
baseline:
  当前 live paper 逻辑

variant:
  在 entry_reclaim_close 基础上，再要求下一根已收盘 4h K 继续确认。
```

建议具体定义：

- 第一次 reclaim close 必须 `close >= entry_high`；
- 下一根 4h close 仍需 `close >= entry_high`；
- 下一根 4h low 不得跌破 `entry_low`；
- 确认期间若先跌破 stop 或 invalidation level，则该机会失效；
- 入场价使用确认 K 收盘价或下一根开盘价，必须固定一种，不得使用未收盘 K 线；
- 延迟入场后是否重算 stop / TP1 必须明确，默认先不重算，避免混入第二个变量。

输出指标：

- 原本会入场但 1-bar 后不会入场的数量；
- 被过滤的 false entries；
- 新增 missed winners；
- 延迟入场后的 entry price 差异；
- `mfe_R` / `mae_R` 差异；
- `counterfactual_pnl_R` 差异；
- trade retention rate；
- sample sufficient。

优先触发条件：

- false entries 主要来自 reclaim 后立即失败；
- 1-bar replay 能过滤多数 false entries；
- 对原 winners / missed winners 的损害可接受；
- 交易数没有被压到样本不足。

### Replay B: relative_strength_gate

待定义清楚的规则：

```text
baseline:
  当前 live paper 逻辑

variant:
  非核心币必须相对 BTC/ETH 或候选池中位数显示更强。
```

候选定义：

- `rs_7d = symbol_7d_return - max(BTC_7d_return, ETH_7d_return)`；
- `rs_14d = symbol_14d_return - max(BTC_14d_return, ETH_14d_return)`；
- 初始阈值仅作为 shadow replay 诊断，不直接写入配置：

```text
rs_7d >= 3 percentage points
or
rs_14d >= 5 percentage points
```

输出指标：

- winners vs losers 的 RS 分布；
- 被过滤的 false entries；
- 被误杀的 missed winners；
- BUY_CANDIDATE 保留率；
- `counterfactual_pnl_R` 差异；
- RISK_ON / RISK_OFF 分层；
- core / altcoin 分层。

优先触发条件：

- false entries 主要来自入场前已经弱于 BTC/ETH 的币；
- 1-bar replay 改善有限；
- winners 与 losers 在入场前 RS 上有明显分离；
- 过滤后仍有足够交易数量。

## 2026-07-16 阶段检查流程

先运行链路检查：

```powershell
python main.py db status
python main.py db stability --days 14
```

再运行 audit：

```powershell
python main.py paper audit --account demo --start-date 2026-07-03 --end-date 2026-07-16 --no-obsidian
```

检查结果分三种：

### 1. 可形成正式 audit

条件：

- 数据链路完整；
- config hash 稳定；
- 成熟 entered trades / opportunity 样本足够；
- `right_censored` 比例可接受；
- 关键分类有 R 倍数支持。

输出：

```text
formal audit
```

### 2. 只能形成 interim report

条件：

- 数据链路完整；
- 但多数新 opportunity 尚未成熟；
- entered / TP1 样本仍不足。

输出：

```text
interim report
```

不做策略参数结论。

### 3. 进入 fix / retest

条件：

- 数据链路异常；
- 任务漏跑影响关键状态；
- plan/event 状态异常；
- missed-winner R 损失明显高于 avoided-loser R 收益；
- 新增连续 4 笔成熟入场均止损且没有 meaningful MFE。

输出：

```text
fix 或 retest
```

先处理工程或口径问题，再谈策略优化。

## A/B 优先级决策

正式 A/B 之前先看 shadow replay 和下一轮 audit。

| 证据结构 | 下一步 |
|---|---|
| 假 reclaim 主导，1-bar replay 明显过滤 false entries | 先测 `entry_reclaim_confirm_1bar` |
| 弱币选择主导，RS 能区分 winners / losers | 先测 `relative_strength_gate` |
| 市场整体缺机会，候选池也弱 | 继续观察，不急于改策略 |
| `missed_profit_R > avoided_loss_R` 且成熟样本足够 | 单独复查 `RECLAIM_PENDING` / `RISK_OFF` |
| 数据链路异常 | 先 fix，策略结论作废 |

组合实验只在至少一个单变量通过后进行。

## 下一步执行顺序

1. 将本计划加入项目 TODO。
2. 补强 `python main.py paper audit`：
   - 样本成熟；
   - 右截尾；
   - R 倍数；
   - 104 -> 78 reconciliation；
   - opportunity funnel；
   - 数据链路一致性。
3. 新增 shadow replay 设计或命令入口。
4. 先对 2026-06-19 -> 2026-07-02 旧窗口重跑增强版 audit，确认新字段可解释旧报告。
5. 2026-07-16 执行阶段检查。

