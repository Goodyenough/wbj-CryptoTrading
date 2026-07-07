# 2026-07-06 A/B 实验计划：选币强度与入场确认

## 1. 当前背景

本计划用于记录 2026-07-02 阶段性验收之后，下一轮可能要做的 A/B 实验方向，避免后续忘记当时为什么要设计这些实验。

当前项目状态：

- 7 月 2 日 paper 阶段性验收结论是 `keep_observing`，不是 `keep`。
- 当前不证明策略已经具备长期盈利能力。
- 当前默认动作仍然是：冻结 `settings.toml`，继续 daily + 4h 观察。
- 7 月 2 日之后新增了 `paper audit`，用于解释“没赚钱的原因是什么”，而不是直接改策略。

最近一次 audit 报告：

```text
reports/2026-07-07/paper_opportunity_audit_2026-06-19_2026-07-02_demo_v1.md
```

审查窗口：

```text
2026-06-19 -> 2026-07-02
```

关键结论：

- BTCUSDT：-2.13%，最大回撤 -9.96%，trend=`sideways`
- ETHUSDT：-0.49%，最大回撤 -12.59%，trend=`sideways`
- opportunity audit：
  - `avoided_loser=25`
  - `missed_winner=12`
  - `false_entry=7`
  - `neutral_or_unknown=34`
- entered trades：
  - `entry_issue=5`
  - `selection_issue=2`
  - `exit_issue=0`
  - `open_unknown=1`

当前解释：

```text
亏损更像来自选币质量和入场确认不足，而不是退出规则明显失败。
```

## 2. 当前不应立刻改默认策略

现在不建议直接修改 `settings.toml` 或默认策略参数。

原因：

1. entered trades 只有 8 笔，足够提示方向，不足以证明新规则应该进入默认配置。
2. 多数 entered trades 来自旧 paper 逻辑阶段，不能完全代表当前补齐后的 `entry_reclaim_close` / TP1 EMA trailing 逻辑。
3. 7 月 2 日后计划是继续观察 2 周，当前改配置会破坏 7 月 3 日之后观察窗口的可比性。
4. audit 指向的是下一轮实验方向，不是部署结论。

当前默认动作：

```text
不改 settings.toml
继续 daily + 4h
等 2026-07-16 左右再跑一次 paper audit
若新窗口仍显示 entry_issue / selection_issue 为主，再启动 A/B
```

## 3. A/B 实验触发条件

只有满足以下条件之一，才启动本计划中的 A/B：

### 条件 A：入场问题继续主导

下一次 audit 中：

```text
entry_issue + selection_issue >= entered trades 的 50%
```

并且：

```text
exit_issue 仍然不是主要问题
```

解释：说明问题仍然发生在入场前后，而不是利润保护。

### 条件 B：false entries 继续偏高

下一次 audit 中：

```text
false_entry 明显存在
```

尤其是实际入场后：

```text
MFE_R < 0.5
MAE_R 接近 -1R
```

解释：说明系统放进去的交易没有足够正向推进，入场确认需要更严格。

### 条件 C：missed winners 明显增加

如果下一次 audit 中：

```text
missed_winner > avoided_loser
```

则不要优先做更严格入场实验，而要转向复查 `RECLAIM_PENDING` / `RISK_OFF` 是否过度保守。

## 4. 推荐实验优先级

### Priority 1：入场确认增强 A/B

实验目标：

验证“入场太早”是否是主要亏损来源。

当前证据：

- 8 笔 entered trades 中 `entry_issue=5`
- ZEC、TON 多笔 `MFE_R=0.00`
- 多数交易没有接近 TP1 就止损

实验假设：

```text
如果要求 reclaim 后再多等一根 4h 确认，或要求价格不立刻跌回 entry zone，
则会减少 false entries 和快速止损。
```

建议实验名：

```text
entry_reclaim_confirm_1bar
```

建议 variant 规则：

```text
baseline:
  当前默认配置

variant:
  在 entry_reclaim_close 基础上，要求：
  1. 4h close 重新站上 entry_high
  2. 下一根 4h close 仍然 >= entry_high
  3. 下一根 4h low 不跌破 entry_low
```

核心观察指标：

- closed_trades
- stop_rate
- false_entry_count
- average MFE_R before stop
- win_rate
- profit_factor
- net_return_pct
- max_drawdown_pct
- missed_winner_count

成功条件：

```text
stop_rate 下降
profit_factor 改善
max_drawdown 不扩大
missed_winner 不明显增加
closed_trades 不被压到样本不足
```

失败条件：

```text
交易数量大幅下降，但净收益/PF/MDD 没有改善；
或 missed winners 明显增加，说明确认条件太慢。
```

### Priority 2：选币相对强度 A/B

实验目标：

验证“候选币质量不足”是否是主要亏损来源。

当前证据：

- `selection_issue=2`
- ONDO 有一定 MFE，但没有接近 TP1，最后完整止损
- BTC/ETH 正式窗口偏横盘，山寨币若不能明显跑赢大盘，入场价值有限

实验假设：

```text
横盘偏弱环境下，只允许相对 BTC/ETH 明显更强的币进入 BUY_CANDIDATE，
可以减少弱反弹和低质量突破。
```

建议实验名：

```text
relative_strength_gate
```

建议 variant 规则：

```text
baseline:
  当前默认配置

variant:
  对非 BTC/ETH/BNB/SOL 的币，要求至少满足一个相对强度条件：
  1. symbol 7d return >= max(BTC 7d return, ETH 7d return) + 3 percentage points
  2. 或 symbol 14d return >= max(BTC 14d return, ETH 14d return) + 5 percentage points
```

注意：

- 先作为硬过滤还是扣分，需要实现时再看现有 scanner 结构。
- 如果用硬过滤，必须重点检查是否造成 `possible_over_filtering=true`。
- 如果用扣分，应输出分数变化，避免无法解释。

核心观察指标：

- BUY_CANDIDATE 数量
- closed_trades
- stop_rate
- average R
- profit_factor
- net_return_pct
- max_drawdown_pct
- RISK_ON / RISK_OFF 分层表现
- altcoin vs large-cap 分层表现

成功条件：

```text
交易质量改善，stop_rate 下降，PF/MDD 改善；
且 closed_trades 仍保持 sample_sufficient。
```

失败条件：

```text
过滤后交易数量过少，或错过明显 winner；
或只是在样本内减少交易，未改善风险收益。
```

### Priority 3：组合实验

只有在 Priority 1 和 Priority 2 至少有一个单变量实验明确改善后，才考虑组合实验。

建议实验名：

```text
relative_strength_entry_confirm
```

组合内容：

```text
relative_strength_gate
+
entry_reclaim_confirm_1bar
```

不建议直接先跑组合实验。

原因：

```text
组合实验难以归因。若结果改善，不知道是选币强度生效、入场确认生效，还是两者交互。
```

## 5. 回测窗口设计

默认使用固定 full dynamic master：

```text
reports/2026-06-09/dynamic_master_full.json
```

默认 universe：

```text
dynamic universe
max-symbols=40
allow-data-gaps=true
```

建议窗口：

```text
2024-07-01 -> 2025-06-01
2025-06-01 -> 2026-06-01
```

如前两段结果方向一致，再补第三段：

```text
2023-07-01 -> 2024-07-01
```

判定要求：

- 至少两个非重叠窗口。
- 每个窗口检查 `sample_sufficient`。
- 如果只有一个窗口改善，结论最多为 `retest`。
- 如果改善来自交易数量大幅下降，必须检查 `possible_over_filtering`。

## 6. 推荐执行顺序

### Step 1：先等新 paper audit

执行时间建议：

```text
2026-07-16 左右
```

先运行：

```powershell
python main.py paper audit --account demo --start-date 2026-07-03 --end-date 2026-07-16 --no-obsidian
```

如果新窗口仍然显示：

```text
entry_issue / selection_issue 主导
```

再进入 Step 2。

### Step 2：实现并跑 `entry_reclaim_confirm_1bar`

原因：

当前 entered trades 里 `entry_issue=5`，入场确认是证据最直接的方向。

执行要求：

- 新增实验参数时，不修改默认 `settings.toml`。
- 只通过 `config/experiments.toml` 和 A/B override 控制。
- baseline 必须保持当前默认配置。
- variant 只改入场确认一个变量。

### Step 3：如果入场实验不够，再跑 `relative_strength_gate`

原因：

如果入场确认改善有限，说明问题可能更靠前，应该检查候选币质量。

执行要求：

- 单变量。
- 不与入场确认同时叠加。
- 必须输出 BUY_CANDIDATE 数量变化，避免误把“少交易”当成“质量改善”。

### Step 4：只有单变量成立后再做组合

组合实验只用于验证最终候选配置，不用于发现问题。

## 7. 不要做的事

当前不要做：

- 不要直接修改 `settings.toml`。
- 不要因为 8 笔 entered trades 就部署新规则。
- 不要同时改选币和入场。
- 不要只看净收益，忽略 closed_trades 和 sample_sufficient。
- 不要把 `missed_winner` 直接理解为防守规则错误，需要先看是否先 hit stop。
- 不要把 `keep_observing` 解读为策略已经有效。

## 8. 最终决策口径

如果后续 A/B 显示：

```text
entry_reclaim_confirm_1bar 改善 PF / MDD / stop_rate，
且 missed_winner 没有明显增加
```

则结论：

```text
candidate_keep_review
```

如果显示：

```text
relative_strength_gate 改善质量，但交易数量明显不足
```

则结论：

```text
retest
```

如果两个方向都没有改善：

```text
不继续围绕选币/入场微调；
回到 paper audit，检查是否其实是市场环境或样本不足。
```

当前最重要的原则：

```text
先解释亏损来源，再设计单变量实验；先 A/B 验证，再考虑写入默认配置。
```
