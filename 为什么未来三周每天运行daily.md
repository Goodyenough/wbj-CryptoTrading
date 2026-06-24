# 为什么未来三周必须每天运行 daily，而不是三周后只运行一次

## 结论先行

未来三周每天运行 daily，目的不是每天重复生成一份相似报告，而是让系统按固定时间持续完成以下工作：

1. 保存当天的市场扫描快照。
2. 把当天符合条件的新计划加入模拟盘。
3. 用当天价格和最新已收盘 4h K 线推进每笔交易的状态。
4. 记录状态变化发生的时间、价格和原因。
5. 生成当天的 paper report 和三周观察 dashboard。

三周后只运行一次，只能看到三周后的市场和持仓终点，无法可靠重建这三周内发生过的入场、拦截、止损、止盈、EMA 跟踪止损变化和市场环境切换。因此，这项三周观察本质上是一项连续的前向模拟实验，而不是三周后做一次静态查询。

## daily 实际做了什么

当前 Windows 计划任务每天北京时间 20:05 执行 `scripts/daily_paper_update.bat`。批处理实际只调用一个统一入口：

```text
python main.py daily --account demo
```

`daily` 命令会创建一个 `run_type=daily_full` 的唯一 `run_id`，然后在同一次受追踪运行中依次完成：

```text
scan
  -> paper add-from-scan
  -> paper update
  -> paper report
  -> observation dashboard
```

因此，下面仍按五个业务步骤解释，但它们现在属于同一个可审计的每日运行，不再是彼此无关的五条人工命令。如果中途失败，`runs` 表会把该次运行标记为 `failed` 并保存错误信息；成功时，扫描、计划、事件、快照和报告都可以通过同一个 `run_id` 对齐。

### 1. scan：保存当天的市场截面

市场扫描会保存当天的候选币、排名、action、市场环境、价格、成交量、技术指标、入场区间、止损和止盈计划。

这些数据具有明确的时间属性。例如同一个币今天可能是 `WATCH_ONLY`，几天后可能变成 `BUY_CANDIDATE`；市场环境也可能在 `RISK_OFF`、`NEUTRAL` 和 `RISK_ON` 之间切换。

如果三周后才扫描一次，得到的只是三周后的候选名单。系统无法知道：

- 三周内每天出现过哪些候选。
- 某个候选连续出现了多少天。
- 候选最初出现时的价格、指标和交易计划。
- `RISK_OFF` 期间系统实际过滤或降级了多少机会。
- 某个后来上涨的币，在上涨前是否曾经给出过有效信号。

不能使用三周后的数据反推三周前的扫描结果，否则容易产生事后偏差。

### 2. add-from-scan：在当时创建交易计划

这一步只会根据当日扫描结果导入当时允许进入模拟盘的计划。计划保存的是创建时的 entry、stop、TP1、TP2 和来源 scan，而不是三周后重新计算出来的水平。

如果三周后才运行，系统创建的是三周后的新计划，不是三周前本来应该创建的计划。即使事后下载历史 K 线，也不能简单恢复，因为候选排名、外部数据校验、市场环境和当时的扫描配置共同决定了计划是否会被导入。

换句话说，模拟交易必须在信号出现时建立。三周后补建，会把“当时不知道的信息”带回过去，破坏前向验证。

### 3. paper update：逐日推进交易状态机

模拟盘不是只保存一个最终盈亏数字，而是保存一条状态路径，例如：

```text
WATCHING
  -> RECLAIM_PENDING
  -> ENTERED
  -> TP1_HIT
  -> TP1_EMA_TRAILING_ACTIVATED
  -> TP1_EMA_TRAILING_RAISED
  -> STOPPED / CLOSED
```

每天运行 `paper update`，系统才有机会在接近事件发生的时间记录：

- 价格是否进入 entry zone。
- 最新已收盘 4h K 线是否重新站上 `entry_high`。
- 一次触碰是否被 `RECLAIM_PENDING` 拦截。
- 被拦截后是否重新 reclaim 并入场。
- 被拦截后是否跌破 stop 或最终失效。
- 已入场交易是否触发 TP1、TP2 或 stop。
- TP1 后 EMA trailing 是否激活。
- EMA trailing stop 是否被抬高。
- 最终是否因 EMA trailing stop 出场。

三周后只更新一次，系统通常只能比较三周后的当前价格与当前状态阈值。中间曾经发生但后来价格又返回的事件可能已经不可见。

例如，某币在第 5 天进入 entry zone，第 7 天重新 reclaim 并入场，第 12 天触发 TP1，第 15 天 EMA stop 被抬高，第 18 天跌破 EMA stop。若第 21 天才运行一次，系统看到的可能只是第 21 天的价格。它无法可靠确定上述事件的先后顺序、触发时间和触发价格。

## 数据库为什么也要求逐日写入

当前实现已经不再只依赖 Markdown 报告，而是把每次运行拆成可关联的结构化记录：

- `runs`：记录这一天的 `daily_full` 是否开始、成功或失败，以及配置哈希和错误信息。
- `market_scans` / `scan_candidates`：记录当日扫描和候选市场截面。
- `paper_plans`：记录计划的当前状态和当前 stop。
- `paper_events`：记录 `PLAN_CREATED`、`RECLAIM_PENDING_SET`、`RECLAIM_CONFIRMED_ENTERED`、EMA trailing、TP2 等状态事件。
- `paper_snapshots`：记录每次运行时开放计划的状态、价格、PnL 和 stop 快照。

这里最重要的区别是：`paper_plans` 更像“现在是什么状态”，而 `paper_events` 和 `paper_snapshots` 保存“它是怎样一步步走到这里的”。三周后只跑一次，最多补上一张终点快照；它不会自动产生此前 20 天本应存在的运行记录、扫描记录和状态快照。

连续运行后，可以用 `run_id` 回答以下审计问题：

- 某个状态变化属于哪一天、哪次任务执行。
- 当天扫描报告、paper report 和 dashboard 是否来自同一批数据。
- 某天没有事件是因为市场没有触发，还是因为任务失败。
- stop 的变化是否单调，是否存在重复计划、重复事件或数据库锁错误。
- 最终统计能否回溯到具体计划、具体 K 线时间和具体运行。

如果没有这条逐日证据链，三周后的汇总数字即使看起来合理，也很难证明其完整性。

## 为什么固定在每天 20:05 也很重要

固定时间运行的意义不只是自动化方便，还在于保持样本口径一致。每天都在相近的北京时间采集市场截面，能够减少“今天早上扫、明天半夜扫、后天因为看到行情才扫”带来的主观选择偏差。

20:05 不是神奇的交易时点，但它是当前实验预先约定的观察时点。三周内保持这个时点，意味着每日结果之间具有更好的可比性：

- 相邻样本间隔大致稳定。
- 运行行为不由当天涨跌决定。
- 持仓时长和事件间隔更容易解释。
- 漏跑和延迟更容易从日志、`runs` 表和报告时间戳中识别。

三周后临时运行一次则完全失去这种固定频率的前向采样，只剩一个由最终日期决定的截面。

## 连续 5 日稳定性门槛为什么不能靠补跑伪造

项目目前要求先通过 `python main.py db stability --days 5`，再允许安装更高频的 4h paper update 定时任务。门槛会检查最近 5 个连续自然日是否都存在合格的 `daily_full` 运行，包括：

- 运行状态为 `success`。
- 每次恰有一份关联扫描。
- 存在开放计划快照。
- 市场扫描报告、paper report 和 dashboard 都能通过 `run_id` 找到。
- 没有 `database is locked`、外键错误、重复计划组或重复事件组。

这个门槛验证的是“系统能否跨多个真实日期稳定运行”，不是“同一天能否连续成功执行五次”。在同一天补跑多次，不能替代 5 个连续自然日，因为它没有覆盖跨日持久化、任务调度、市场变化、报告目录切换和无人值守恢复等风险。

同理，三周后一次性运行也只能证明那一刻命令可执行，不能证明过去三周自动化链路可靠。

## 为什么历史 K 线不能完全补回

理论上可以在三周后下载每根历史 K 线做一次回放，但那已经不是当前 paper daily 流程，而是另写一套历史 replay。即使做 replay，也需要解决以下问题：

- 每天当时的候选 universe 和排名。
- 当时的外部数据质量结果。
- 当时的市场环境判断。
- 同一根 K 线内 entry、stop、TP1、TP2 的触发顺序。
- 使用 close、high、low 还是实时价格作为触发依据。
- 每次运行时实际加载的配置和已有持仓状态。
- API 当时返回的数据与后来修订或补齐的数据是否一致。

如果没有每天保存的扫描和事件记录，历史回放必须加入大量假设。最终得到的是一个回测结果，而不是这三周真实运行的模拟盘结果。

本次三周观察的价值，恰恰在于检验生产路径中的 scanner、paper trader、数据库状态、报告统计和定时任务能否共同稳定工作。因此不能用三周后的一次回测代替。

## 两项关键规则尤其依赖连续运行

### RECLAIM_PENDING 后续追踪

我们需要判断被 entry reclaim 规则拦截的机会后来属于哪一种情况：

1. 后来重新 reclaim 并成功入场。
2. 后来跌破 stop 或计划失效。
3. 一直没有形成有效 reclaim。

这需要先在触碰当日写入 `RECLAIM_PENDING`，再在后续日期继续观察。如果第一次运行就在三周后，系统不知道三周前是否曾经触碰 entry zone，也就没有可追踪的 pending 起点。

### TP1 EMA trailing stop

EMA trailing 是一个逐步变化的退出机制。我们需要的不只是最终有没有止损，而是：

- 激活了多少次。
- stop 被抬高了多少次。
- 抬高后的 stop 路径如何变化。
- 最终有多少交易由 EMA stop 退出。

EMA 值会随每根新 4h K 线变化。每天更新可以持续把新的有效 EMA stop 写进交易状态和事件日志。三周后只计算一次 EMA，只能得到终点 EMA，无法代表过去三周真实可执行的 trailing stop 路径。

## dashboard 为什么也要每天生成

dashboard 是每日实验快照，不只是最终汇总表。它会记录：

- `RECLAIM_PENDING` 事件数及后续分类。
- TP1 EMA 激活、抬 stop 和出场次数。
- 每笔开放持仓的持仓小时数。
- 当日扫描 action 分布。
- 当日 `RISK_OFF` 候选分布。

连续保存 dashboard 后，三周复盘时可以判断指标是在某一天突然变化，还是逐步积累。若最终数字异常，也能定位从哪一天开始出现问题。

例如三周后的 EMA 激活次数仍为 0，连续 dashboard 可以帮助区分：

- 三周内确实没有交易触发 TP1。
- 某天开始定时任务没有更新持仓。
- EMA 数据不足导致未激活。
- 报告统计出现故障。

只有一份最终报告时，这几种原因很难区分。

## 每天运行还能验证系统可靠性

这三周不仅是在观察策略，也是在观察自动化系统本身：

- Windows 计划任务是否每天按 20:05 触发。
- `LastTaskResult` 是否持续为 0。
- Binance 或外部数据源失败后是否留下明确日志。
- SQLite 状态能否跨天正确持久化。
- 报告版本是否连续生成而不覆盖历史。
- paper report 与 dashboard 的统计是否一致。
- Obsidian 和仓库报告是否都能正常写入。

三周后只运行一次，只能证明那一次成功，不能证明系统具备连续无人值守运行能力。

## 如果中间漏跑一天会怎样

漏跑一天不一定让整个实验作废，但会降低记录精度，具体影响取决于当天是否发生状态变化。

可能的影响包括：

- 缺少当天扫描候选和市场环境快照。
- 当天本应创建的计划没有被及时导入。
- entry、stop、TP1 或 reclaim 事件被推迟记录。
- 若价格触发后又返回，事件可能完全漏记。
- 持仓时长仍可根据时间戳计算，但状态变化的准确时点可能丢失。
- 当日 dashboard 出现空档，三周趋势不完整。

发现漏跑后应尽快恢复任务，并在 `dailylog.md` 记录缺失日期、原因和影响。不要静默地用第二天报告冒充前一天数据。

## 每天一次仍然不是实时交易监控

需要明确：20:05 每天运行一次，比三周后只运行一次可靠得多，但它仍不是实时行情监听器。

如果价格在两次运行之间短暂触发 stop、TP1 或 TP2，之后又返回，而当前状态判断主要依赖运行时价格，那么日内瞬时事件仍可能漏记。最新已收盘 4h K 线可以支持 reclaim 和 EMA 等判断，但不能自动等同于逐笔或分钟级成交路径。

因此三周观察的正确解释是：

- 它验证每日频率下的前向模拟表现和自动化稳定性。
- 它不声称还原所有日内价格触发细节。
- 若未来要接近实盘执行精度，应把 `paper update` 提高到每 4 小时或更高频率，并明确使用 K 线 high/low 或实时 ticker 的触发规则。

在当前阶段，固定每天 20:05 运行可以保持样本口径一致，也足以检验我们当前关心的三周观察指标。

## 三周后我们最终能回答什么

连续运行三周后，我们可以基于真实保存的每日轨迹回答：

1. entry reclaim 规则实际拦截了多少次。
2. 被拦截的计划后来重新入场、跌破失效或继续等待的比例。
3. TP1 EMA trailing 是否真实激活，是否实际提高了 stop。
4. EMA trailing 导致了多少次退出，对持仓结果有什么影响。
5. 开放持仓通常持续多久，是否存在长期不触发 TP1 的资金占用。
6. `RISK_OFF` 环境出现了多少天，期间系统产生了哪些 action。
7. 模拟盘状态、报告和 dashboard 是否跨天一致。
8. 定时任务能否稳定完成无人值守运行。

如果三周后只运行一次，上述问题大部分都只能靠猜测或重新回测，不能作为这次前向模拟实验的直接证据。

## 每日最低检查项

正常情况下不需要每天人工干预策略，只需快速确认：

```powershell
Get-ScheduledTaskInfo -TaskName CryptoTrading_DailyPaperUpdate |
    Select-Object LastRunTime, LastTaskResult, NextRunTime
```

并检查当天目录至少存在：

```text
reports/YYYY-MM-DD/market_scan_*.md
reports/YYYY-MM-DD/paper_report_*.md
reports/YYYY-MM-DD/paper_observation_dashboard_*.md
```

同时确认 `logs/daily_paper_update.log` 最后出现：

```text
observation-dashboard done
=== daily paper update complete ===
```

只要这些检查正常，三周内应尽量保持策略配置不变，让每天的数据属于同一套观察口径。研究性回测和 A/B 实验可以继续进行，但不要未经决策就修改当前模拟盘默认规则。

## 一句话总结

每天运行 daily，是为了保存市场和交易状态的时间路径；三周后只运行一次，只能看到终点。我们要验证的是这三周里规则如何工作，而不仅是三周后的价格是多少。



# 4. 三周后要干什么？

三周后不是简单看“赚了还是亏了”。

三周后要做一次正式验收，决定：

<pre class="overflow-visible! px-0!" data-start="2261" data-end="2291"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼd ͼr"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>keep</span><br/><span>retest</span><br/><span>reject</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

---

## keep：保留策略，进入下一阶段

如果三周后发现：

<pre class="overflow-visible! px-0!" data-start="2329" data-end="2410"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼd ͼr"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>系统稳定</span><br/><span>数据完整</span><br/><span>状态机没乱</span><br/><span>回测和模拟盘差异可解释</span><br/><span>风险暴露可控</span><br/><span>TP1 / EMA / reclaim 有实际价值</span><br/><span>收益和回撤能接受</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

那就可以考虑：

> 保留当前策略，进入小资金实盘或更长周期模拟盘。

---

## retest：继续测试，不急着实盘

如果发现：

<pre class="overflow-visible! px-0!" data-start="2482" data-end="2563"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼd ͼr"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>样本太少</span><br/><span>RISK_OFF 天数太多</span><br/><span>交易太少</span><br/><span>同币种重复暴露影响判断</span><br/><span>TIME_EXIT 规则还需要比较</span><br/><span>模拟盘和回测有差异但原因不明确</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

那就不要急着上实盘，而是进入下一轮 retest。

比如继续测试：

<pre class="overflow-visible! px-0!" data-start="2601" data-end="2676"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼd ͼr"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>42 根固定退出</span><br/><span>42 根 + 低于 EMA20 才退出</span><br/><span>18/30/42 持仓上限</span><br/><span>altcoin 限制</span><br/><span>同币种重复持仓限制</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

---

## reject：暂时否定策略或暂停实盘

如果三周后发现：

<pre class="overflow-visible! px-0!" data-start="2716" data-end="2790"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼd ͼr"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>状态机混乱</span><br/><span>任务经常失败</span><br/><span>重复事件严重</span><br/><span>回撤过大</span><br/><span>止损率过高</span><br/><span>TP1 长期无法触发</span><br/><span>同币种风险暴露不可控</span><br/><span>模拟盘明显差于回测</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

那就应该暂停实盘推进，先修策略或系统。

---

# 5. 三周后具体看哪些指标？

重点看这些：

<pre class="overflow-visible! px-0!" data-start="2844" data-end="3142"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼd ͼr"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>daily_full 成功天数</span><br/><span>4h update 成功次数</span><br/><span>失败 run 数量</span><br/><span>scan 总数</span><br/><span>BUY_CANDIDATE 总数</span><br/><span>paper plan 总数</span><br/><span>入场计划数</span><br/><span>RECLAIM_PENDING 次数</span><br/><span>pending 后重新入场 / 失效 / 跌破 stop 的比例</span><br/><span>TP1 命中率</span><br/><span>TP2 命中率</span><br/><span>EMA trailing 激活次数</span><br/><span>EMA stop 抬高次数</span><br/><span>EMA trailing 出场次数</span><br/><span>平均持仓时间</span><br/><span>最长持仓时间</span><br/><span>同币种最大并发计划数</span><br/><span>最大风险暴露</span><br/><span>RISK_OFF 下候选和入场数量</span><br/><span>已实现 PnL</span><br/><span>未实现 PnL</span><br/><span>最大回撤</span><br/><span>模拟盘 vs 回测偏差</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

这些指标能回答：

> 策略有没有机会？
>
> 风控有没有效果？
>
> 系统有没有稳定运行？
>
> 风险是否可控？
>
> 是否值得进入下一阶段？

---

# 6. 用一句话总结

三周模拟盘的意义是：

> **用一段连续、真实时间推进、策略配置一致的样本，验证这套自动交易系统能不能稳定运行、规则能不能正确执行、风险是否可控、回测是否可信，并在三周后决定 keep、retest 还是 reject。**

所以这三周不是在浪费时间，而是在做上线前最关键的“试运行验收”。
