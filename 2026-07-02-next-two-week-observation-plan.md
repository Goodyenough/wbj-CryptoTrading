# 2026-07-02 后两周观察计划

## 核心判断

7 月 2 日阶段性验收后的下一步，不是马上优化策略，而是继续解释：

> 没赚钱的原因是什么？

当前最合理路线：

```text
保持配置不变
继续 daily + 4h 观察 2 周
补 BTC/ETH 正式窗口基准
新增 opportunity audit
逐笔复盘 entered trades
等 entered / TP1 / RECLAIM 样本够了再决定是否改策略
```

核心判断标准从“有没有赚钱”升级为：

```text
没赚钱的原因是什么？
```

只有把亏损和空仓解释清楚，后面才知道到底该改选币、改入场、改退出，还是继续空仓等待。

## Step 1: 冻结配置，继续 daily + 4h

保持当前 `settings.toml` 不变，至少再运行 2 周。

执行原则：

- 不修改 `settings.toml`。
- 不新增策略参数。
- 不改 paper 状态机。
- 不补跑污染样本。
- daily 继续作为主观察链路。
- 4h update 继续作为关键状态补充。

原因：

- 7/2 verdict 是 `keep_observing`，不是 `keep`。
- 当前样本不足以证明策略有效，也不足以定位唯一问题。
- 现在改配置会让后续样本失去可比性。

## Step 2: 新增 opportunity audit 报告

目标：判断系统是在正确空仓，还是错过行情。

报告重点统计：

```text
avoided losers
missed winners
false entries
```

### RECLAIM_PENDING

不要只看 `RECLAIM_PENDING` 事件次数，例如 91 次事件本身意义有限。

必须按独立 `plan_id` / `symbol` 判断：

- avoided losers：被拦截后继续下跌、跌破 stop、长期不能 reclaim。
- missed winners：被拦截后重新 reclaim，并达到 TP1 或产生明显正收益。
- false entries：如果没有 reclaim 过滤，本来会入场，但随后快速止损或明显走弱。

建议输出字段：

```text
symbol
plan_id
first_pending_time
last_pending_time
entry_low
entry_high
stop
max_price_after_pending
min_price_after_pending
reclaimed_entry_high
hit_tp1_after_pending
fell_below_stop
outcome
classification
```

### WATCH_ONLY / REJECT

opportunity audit 不应只看 `RECLAIM_PENDING`。

还要看：

- `RISK_OFF` 下被降级的 `WATCH_ONLY` 后面有没有大涨。
- `REJECT` 的币后面有没有明显跑赢。
- `BUY_CANDIDATE=0` 的日子，BTC/ETH 或山寨是否其实在启动。

这能判断整体防守模式是否过度保守。

## Step 3: 补 BTC/ETH 正式窗口基准

每个验收窗口都要知道大盘到底是涨、跌、横盘。

至少补充：

```text
BTC return over window
ETH return over window
BTC max drawdown over window
ETH max drawdown over window
BTC trend state
ETH trend state
alt market proxy if available
```

用途：

- 如果 BTC/ETH 也弱，策略空仓或亏损更容易解释为市场环境。
- 如果 BTC/ETH 大涨，而策略没动或持续亏损，就要怀疑选币、入场或进攻模式。
- 如果 BTC/ETH 横盘但山寨普跌，RISK_OFF 防守可能是合理的。

注意：

- 7/2 验收报告中只能使用已有 7d BTC/ETH 数据，不能伪造正式窗口基准。
- 后续应把正式稳定窗口 BTC/ETH 基准变成自动报告字段。

## Step 4: 复盘 8 笔 entered trades

逐笔回答：

```text
为什么入场？
入场时 market regime 是什么？
入场后最大浮盈是多少？
是否曾达到 0.5R / 1R 浮盈？
有没有接近 TP1？
最后为什么失败？
是选币问题、入场问题、止损问题，还是市场问题？
```

建议分类：

- selection_issue：选币本身质量差，入场后几乎没有顺势空间。
- entry_issue：方向可能没错，但入场太早或追高。
- stop_issue：方向可接受，但 stop 太紧或结构止损位置不好。
- exit_issue：曾有明显浮盈但没有保护，最后回吐。
- market_issue：大盘或山寨环境持续恶化，个体 setup 难以发挥。
- sample_noise：样本不足或事件路径不完整，暂不归因。

尤其要记录：

```text
max_favorable_excursion_R
max_adverse_excursion_R
time_to_max_favorable
time_to_stop_or_latest
```

如果很多单子曾经有 `0.5R` 到 `1R` 浮盈但最后止损，问题可能在退出或保护利润。

如果多数单子几乎没有浮盈就止损，问题更可能在选币或入场。

## Step 5: 等样本够了再决定改哪里

两周后根据证据判断：

| Evidence | Interpretation | Next Focus |
|---|---|---|
| avoided losers 很多，missed winners 很少 | 防守规则有效 | 继续保留 `RECLAIM_PENDING` / `RISK_OFF` |
| missed winners 很多 | 防守过度保守 | 复测 `RECLAIM_PENDING` 或 `RISK_OFF` |
| entered trades 继续多数止损 | 入场质量不足 | 优先改入场规则 |
| 经常大浮盈回落 | 利润保护不足 | 优先改退出规则 |
| BTC/ETH 大涨而策略没动 | 进攻模式不足 | 检查选币、RISK_OFF、BUY_CANDIDATE |
| BTC/ETH 弱且策略少动 | 防守可能合理 | 继续观察 |

## 两周后的决策口径

不要直接问：

```text
策略有没有赚钱？
```

要问：

```text
亏损来自哪里？
空仓是否正确？
被拦截的机会后来怎样？
入场后的路径是否支持当前止损和退出？
大盘环境是否允许策略发挥？
```

两周后可能的结论：

- `continue_observing`：样本仍不足，但系统行为合理。
- `retest_reclaim`：missed winners 明显增多。
- `retest_entry`：entered trades 多数几乎无浮盈后止损。
- `retest_exit`：多笔交易大浮盈后回吐。
- `retest_risk_off`：BTC/ETH 或强币上涨时系统长期不参与。
- `fix_reporting`：报告口径或数据链路影响判断。

## 当前默认行动

当前默认行动不是“优化策略”，而是：

> 继续按当前配置观察，同时新增机会漏检分析，判断系统到底是在正确空仓，还是错过行情。

除非出现明确红线，否则 7/2 后两周内不修改 `settings.toml`。
