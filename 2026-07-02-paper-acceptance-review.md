# 2026-07-02 Paper 阶段性验收

## Executive Summary

本次验收定位为“近三周背景观察、两周连续稳定样本”的阶段性验收，不把结果解读为策略长期盈利能力已被证明。

核心结论：

> 数据链路基本通过，策略防守机制初步符合预期，但 paper 有效成交样本不足，暂不能证明策略盈利能力；建议保持当前配置继续观察，并将 `RISK_OFF`、`RECLAIM_PENDING`、`42-bar` 作为重点跟踪项。

最终 verdict：`keep_observing`

含义：

- `keep_observing` 不等于策略已证明有效。
- `keep_observing` 仅表示系统链路与关键防守机制未发现重大问题，建议继续观察。
- 本次不修改 `settings.toml`、不改策略参数、不补跑、不重算 paper 状态。

## Acceptance Scope

本次验收分为三层：

1. 数据链路验收：判断 paper 观察数据是否可追溯、可复核、可用于分析。
2. 策略行为验收：判断 `RISK_OFF`、`RECLAIM_PENDING`、`42-bar`、TP1 EMA trailing 等规则是否按设计运行。
3. 策略有效性评估：仅做阶段性观察，不作为长期盈利能力确认依据。

本报告主要回答“当前系统是否值得继续按同一配置观察”，不回答“策略长期是否能稳定盈利”。

## Observation Window

| Window | Dates | Role | Notes |
|---|---|---|---|
| 三周背景窗口 | 2026-06-12 -> 2026-07-02 | 补充观察 | 用于理解近三周项目背景、报告积累和 paper 状态变化。 |
| 正式稳定窗口 | 2026-06-19 -> 2026-07-02 | 主证据 | 14 天 daily 样本连续完整，且 `config_hash=be7ec39ec21f6a83` 保持一致。 |
| 4h 高频观察窗口 | 2026-06-19 -> 2026-07-02 | 增强证据 | 预期 70 次，成功 69 次，2026-06-25 16:10 +08:00 有 1 次 SSL 网络失败。 |

三周背景窗口仅作为补充观察证据。若前一周存在配置变化、数据缺口或记录不完整，不纳入主验收结论。

## Evidence Sources

- `reports/2026-07-02/paper_report_2026-07-02_demo_v1.md`
- `reports/2026-07-02/paper_observation_dashboard_2026-07-02_demo_v1.md`
- `python main.py db status`
- `python main.py db stability --days 14`
- `2026-07-02-paper-acceptance-criteria.md`

## 1. 数据链路验收

Verdict：`pass`

关键证据：

| Item | Result |
|---|---:|
| 正式稳定窗口 daily 天数 | 14 |
| daily success | 14 |
| daily failed | 0 |
| observed config hashes | `be7ec39ec21f6a83` |
| duplicate plan groups | 0 |
| duplicate event groups | 0 |
| foreign key errors | 0 |
| UTC timestamp errors | 0 |
| database stale running | 0 |
| schema version | 2 |
| journal mode | WAL |

`python main.py db stability --days 14` 显示 2026-06-19 至 2026-07-02 连续 14 天 daily run 全部 `ready=true`，且 `config_hash` 未漂移。

`python main.py db status` 显示最新 daily run：

```text
run_id=20260702_120504_e19c34c5
run_type=daily_full
status=success
config_hash=be7ec39ec21f6a83
```

4h 高频任务：

| Item | Result |
|---|---:|
| Expected 4h runs | 70 |
| Success | 69 |
| Failed | 1 |
| Success rate | 98.57% |
| Failed run | `20260625_081003_6ddd41f5` |
| Failure reason | SSL `UNEXPECTED_EOF_WHILE_READING` |

4h 失败影响判断：

- 失败发生在 2026-06-25 16:10 +08:00。
- 当前证据未显示该失败改变了关键入场、止损、TP1 或 `RECLAIM_PENDING` 判断。
- 该失败应披露为 4h 增强证据的局部瑕疵，但不足以否定正式稳定窗口的 daily 主证据。

注意：7/2 observation dashboard 生成时曾显示 latest daily 为 `running`，但之后 `db status` 已确认同一 run 最终为 `success`。因此以 SQLite 最新状态为准。

## 2. RISK_OFF 防守机制

Verdict：`keep_observing`

正式稳定窗口内 scan 行为：

| Market Regime | Action | Count |
|---|---|---:|
| `RISK_OFF` | `WATCH_ONLY` | 47 |
| `RISK_OFF` | `REJECT` | 23 |
| `RISK_OFF` | `BUY_CANDIDATE` | 0 |

正式稳定窗口内没有新增 paper plan。

判断：

- `RISK_OFF` 下未产生新的 `BUY_CANDIDATE`。
- `RISK_OFF` 下没有由当日新增计划触发的新开仓。
- 候选被降级为 `WATCH_ONLY` / `REJECT`，符合防守设计。

结论：`RISK_OFF` 防守机制初步符合预期，但仍属于阶段性观察，不等于策略长期有效。

## 3. RECLAIM_PENDING 机会成本

Verdict：`keep_observing / no material missed winner observed`

7/2 报告核心数据：

| Metric | Value |
|---|---:|
| Entry reclaim blocks | 91 |
| Reclaim trades | 1 |
| Reclaim later entered | 0 |
| Reclaim still waiting | 0 |
| Formal-window `RECLAIM_PENDING_SET` events | 83 |

去重口径：

- 不能按 91 次事件机械判断。
- 这些事件主要集中在 ONDOUSDT 同一类机会反复触发。
- 判断重点应是 plan/symbol 级别的 avoided losers 与 missed winners。

Avoided losers：

- ONDOUSDT 多次触碰 entry zone，但 4h close 未 reclaim 到 `entry_high=0.41157` 上方。
- 7/2 最新价格约 `0.33470`，低于 stop `0.33845`。
- dashboard 对该机会给出 `fell_below_stop_or_invalidated`，支持“避免弱反弹误入场”的解释。

Missed winners：

- 当前没有观察到明确的 missed winner。
- 没有出现“被 `RECLAIM_PENDING` 拦截后重新 reclaim，并走到 TP1 或明显正收益”的证据。

口径差异：

- 7/2 paper report 的 Entry Reclaim 追踪行仍写 `still_waiting`。
- 7/2 observation dashboard 明细写 `fell_below_stop_or_invalidated`。
- 这反映报告口径存在细微不一致：plan 状态仍是 `WATCHING`，但价格层面已经低于 stop。

结论：当前没有证据证明 `RECLAIM_PENDING` 造成重大机会成本；相反，ONDOUSDT 更像 avoided loser。后续应继续追踪 missed winners，并修正 report/dashboard 的 outcome 口径一致性。

## 4. 42-bar Holding Review

Verdict：`maintain_default`

本次只判断是否维持当前默认，不写“42-bar 已证明有效”。

超过 42 根 4h 的仓位：

| Symbol | Plan | Status | PnL@first >=168h | Latest PnL | Max/Min PnL After | Outcome |
|---|---|---|---:|---:|---:|---|
| `ONDOUSDT` | `2ed171ff8ada` | STOPPED | 15.73 | 0.00 | 65.58 / -99.71 | stopped |
| `ONDOUSDT` | `5d1c3b7ddf56` | STOPPED | 18.54 | 0.00 | 69.61 / -99.70 | stopped |
| `WLDUSDT` | `616e1bbfd4c6` | ENTERED | 120.13 | -54.80 | 132.65 / -69.79 | still_open |

判断：

- 两个 ONDOUSDT 样本最终 stopped。
- WLDUSDT 在超过 42 根后曾有较高浮盈，但到 7/2 已回落为负浮盈。
- 当前 paper 证据不支持立即放宽持仓上限。
- 但样本数仍少，不能写成“42-bar 已证明有效”。

结论：维持当前 42-bar 默认规则，继续观察超过 42 根后的边际收益与回撤。

## 5. TP1 EMA Trailing Stop

Verdict：`sample_insufficient`

7/2 报告数据：

| Metric | Value |
|---|---:|
| TP1 hit rate | 0.00% |
| TP1 EMA trailing activated | 0 |
| TP1 EMA trailing raises | 0 |
| TP1 EMA trailing stops | 0 |
| TP1 EMA trailing active trades | 0 |

判断：

- 当前没有 TP1 样本。
- 没有 EMA trailing activation、raise 或 stop exit。
- 不能评价 TP1 EMA trailing stop 好坏。

结论：样本不足，不做参数调整，继续观察。

## 6. 收益与风险表现

Verdict：`not_sufficient_for_profitability_claim`

7/2 paper report：

| Metric | Value |
|---|---:|
| Total plans | 25 |
| Open watching/positions | 2 |
| Entered trades | 8 |
| Closed trades | 23 |
| Winning closed trades | 0 |
| Losing closed trades | 7 |
| Win rate | 0.00% |
| TP1 hit rate | 0.00% |
| Realized PnL | -700.00 USDT |
| Unrealized PnL | -54.80 USDT |
| Realized + Unrealized PnL | -754.80 USDT |

R 倍数口径：

- 每笔入场计划 `cash_risk=100 USDT`。
- 入场计划数为 8，合计初始风险约 800 USDT。
- Realized + unrealized PnL 为 -754.80 USDT。
- 当前总 R 约为 `-0.94R`，按 8 笔入场平均约 `-0.12R/trade`。

同期 BTC/ETH 基准：

- 当前本地 `kline_cache` 无法直接覆盖 2026-06-19 至 2026-07-02 的 BTC/ETH 全窗口价格。
- 7/2 paper report 可得近 7 日基准：BTC 7d `+2.61%`，ETH 7d `+5.30%`。
- 本次不伪造全窗口 BTC/ETH 表现；后续建议在 daily report 或 acceptance report 中加入正式稳定窗口基准计算。

判断：

- 当前收益表现偏弱，且 TP1 样本为 0。
- 但本次验收不以短期收益单独判定策略失败。
- closed winners 为 0，说明不能宣称策略已具备盈利能力。

结论：收益与成交样本不足以证明长期盈利能力；继续观察，不上调为 `keep`。

## Downgrade Rules Check

| Rule | Result | Impact |
|---|---|---|
| 正式稳定窗口内 daily 数据不连续 | 未触发 | 14 天 daily 连续成功。 |
| `config_hash` 在正式稳定窗口内变化 | 未触发 | 始终为 `be7ec39ec21f6a83`。 |
| `RISK_OFF` 下仍产生新 `BUY_CANDIDATE` | 未触发 | RISK_OFF / BUY_CANDIDATE 为 0。 |
| `RISK_OFF` 当日新增计划触发新开仓 | 未触发 | 稳定窗口内无新增 paper plan。 |
| 4h 缺失影响关键状态判断 | 未触发 | 1 次 SSL 失败已披露，未见关键状态受影响。 |
| 数据库 stale running、状态机异常或重复导入 | 未触发 | stale running 为 0，duplicate groups 为 0。 |
| 样本不足却判断长期盈利能力 | 未触发 | 本报告明确不做长期盈利能力确认。 |
| PnL 出现无法解释的风控异常 | 未触发 | 亏损主要来自止损与未实现回撤，未见单笔超风险异常。 |

总体结论无需降级到 `retest`，但也不能上调为 `keep`。

## Final Verdict

| Module | Verdict |
|---|---|
| 数据链路 | `pass` |
| RISK_OFF | `keep_observing` |
| RECLAIM_PENDING | `keep_observing / no material missed winner observed` |
| 42-bar | `maintain_default` |
| TP1 EMA trailing | `sample_insufficient` |
| 收益与风险 | `not_sufficient_for_profitability_claim` |
| 总体 | `keep_observing` |

最终判断：

> 数据链路基本通过，策略防守机制初步符合预期，但 paper 有效成交样本不足，暂不能证明策略盈利能力；建议保持当前配置继续观察，并将 `RISK_OFF`、`RECLAIM_PENDING`、`42-bar` 作为重点跟踪项。

## Next Actions

1. 保持当前 `settings.toml` 不变，继续运行 daily 与 4h 观察。
2. 后续重点跟踪 `RECLAIM_PENDING` 的 missed winners / avoided losers，不只看事件次数。
3. 继续跟踪超过 42 根 4h 的仓位，记录 42 根后的边际收益与回撤。
4. 等出现 TP1 样本后再评价 TP1 EMA trailing stop。
5. 给后续报告增加正式稳定窗口 BTC/ETH 基准表现，避免只引用 7d 短窗口。
6. 修正或复核 `RECLAIM_PENDING` 在 paper report 与 observation dashboard 中的 outcome 口径一致性。
