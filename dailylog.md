# Daily Log

用途：记录 CryptoTradingSystem 每天每次代码或工程文件改动，使用北京时间时间戳。

记录格式：

```text
### HH:mm:ss +08:00 - 改动标题
- 类型：代码 / 报告 / 文档 / 配置 / Git
- 改动：
- 影响：
- 验证：
- Git：
```

## 2026-06-24

### 23:03:50 +08:00 - 补充 7 月 2 日 paper 观察验收标准
- 类型：文档 / 报告 / Git
- 改动：新增 `2026-07-02-paper-acceptance-criteria.md`，将 7 月 2 日前 paper 观察的验收标准整理为数据链路、`RISK_OFF`、`RECLAIM_PENDING`、42 根 4h 持仓、TP1 EMA trailing stop 与总体策略六个决策问题。
- 影响：仅新增复盘文档，不修改 `settings.toml`、交易策略、定时任务或数据库；为 2026-07-02 验收提供统一判定口径。
- 验证：检查文档已生成；提交时按项目规则纳入当前未跟踪的 `reports/` 自动报告；不纳入用户已有未提交修改 `为什么未来三周每天运行daily.md`。
- Git：计划提交 `Add July 2 paper acceptance criteria`。

## 2026-06-21

### 16:39:26 +08:00 - 修复企业微信数据库状态检查
- 类型：脚本 / 运维 / 测试 / Git
- 改动：修复 `scripts/run_logged_paper_task.ps1` 中企业微信通知的数据库确认逻辑，将 inline Python 从 `python -c` 多行参数调用改为 `python -` stdin 调用，避免计划任务/PowerShell 环境下多行脚本被截断导致 `SyntaxError`。
- 影响：4h 与 daily 完成通知仍会附带 `database: run_id=... run_type=... status=... snapshots=... events=...`；本次修复不修改 `settings.toml`、交易策略或 paper plan。
- 验证：用 2026-06-21 16:10 真实 4h run `20260621_081003_20ee7d9a` 验证数据库确认行返回 `status=success snapshots=4 events=1`；PowerShell `[scriptblock]::Create(...)` 解析通过；`python tests\test_database.py` 通过；`python -m compileall main.py src tests` 通过；`settings.toml` SHA256 保持 `be7ec39ec21f6a83...`。
- Git：计划提交 `Fix database status notification check`。

### 12:55:43 +08:00 - 企业微信通知增加数据库确认
- 类型：脚本 / 运维 / 测试 / Git
- 改动：增强 `scripts/run_logged_paper_task.ps1` 的企业微信通知内容，任务结束后从输出中提取 `run_id`，再查询 SQLite `runs`、`paper_snapshots`、`paper_events`，在通知中追加 `database: run_id=... run_type=... status=... snapshots=... events=...`。
- 影响：daily 与 4h 通知会同时显示脚本完成状态和数据库落库状态；不修改 `settings.toml`、交易策略或 paper plan。
- 验证：PowerShell `[scriptblock]::Create(...)` 语法解析通过；`python tests\test_database.py` 通过；`python -m compileall main.py src tests` 通过；未手动触发真实 daily/4h 任务，避免污染运行样本。
- Git：计划提交 `Include database status in task notifications`。

## 2026-06-18

### 23:25:15 +08:00 - 增强三周观察仪表
- 类型：代码 / 报告 / 测试 / 文档 / Git
- 改动：在 `python main.py observation-dashboard` 中新增三块观察口径：`Run Health / 自动任务健康`、`Stale Running Run 检测`、`42-bar Holding Review`。
- 改动：`Run Health` 汇总最近 24h 的 `daily_full` / `paper_4h_update` 成功、失败、running 数，并列出最新 daily 与 4h run；`Stale Running Run 检测` 列出超过 2h 仍为 `running` 的 run，并给出 `mark-run-failed` 建议命令；`42-bar Holding Review` 汇总超过 42 根 4h（168h）的持仓、首次观测超过阈值时的价格/PnL、最新价格/PnL、阈值后最高/最低价格与浮盈亏、后续 outcome。
- 改动：新增测试 `test_observation_dashboard_includes_run_health_stale_and_42_bar_review`，并生成 `reports/2026-06-18/paper_observation_dashboard_2026-06-18_demo_v3.md` 作为当前证据报告；更新 `TODO.md` 将三周观察仪表增强项标记完成。
- 影响：不修改 `settings.toml`，不修改交易策略，不新增或修改 paper plan；daily 与 4h 后续运行会自动带出新增观察小节。
- 验证：`python tests\test_database.py` 通过；`python tests\test_research_tools.py` 通过；`python -m compileall main.py src tests` 通过；`python main.py observation-dashboard --account demo --no-obsidian` 成功生成 v3；`config_hash` 保持 `be7ec39ec21f6a83`。
- Git：计划提交 `Enhance observation dashboard monitoring`。

### 22:48:25 +08:00 - RECLAIM_PENDING 机会成本复盘
- 类型：实验 / 报告 / 文档 / Git
- 改动：生成 `reports/2026-06-18/reclaim_pending_opportunity_cost_review_2026-06-18_v1.md`，并同步到 Obsidian Reports；更新 Obsidian `CryptoTrading 实验日志.md` 记录实验背景、样本、结论和下一步。
- 结果：现有 `RECLAIM_PENDING` 样本全部来自 ONDOUSDT plan `9734a33dea2e`，8 次事件价格均低于 `entry_low=0.394505`，没有一次进入计划入场区间或 4h close reclaim `entry_high=0.411568`；当前不能证明 `entry_reclaim_close` 造成明显机会成本。
- 影响：不修改 `settings.toml`，不新增/修改 paper plan，不运行 backtest 或 daily/4h 任务；仅基于 SQLite paper events/snapshots 和既有报告做离线复盘。
- 验证：确认报告文件生成；`python main.py db status` 显示数据库健康；`_config_hash(Path("config/settings.toml"))` 保持 `be7ec39ec21f6a83`。
- Git：计划提交 `Review reclaim pending opportunity cost`。

### 22:14:16 +08:00 - daily 与 4h 任务完成后发送企业微信通知
- 类型：脚本 / 运维 / 文档 / Git
- 改动：在 `scripts/run_logged_paper_task.ps1` 增加企业微信机器人通知逻辑；`daily` 与 `paper_4h` 两种模式成功完成时发送 `completed` 通知，失败时发送 `failed` 通知。
- 改动：通知 webhook 从环境变量读取，依次支持 `CRYPTO_TRADING_WECOM_WEBHOOK_URL`、`WECHAT_WORK_WEBHOOK_URL`、`WECOM_WEBHOOK_URL`、`QYWX_WEBHOOK_URL`，避免把密钥写入仓库；未配置 webhook 时仅写日志 `notification skipped`，不影响任务成功/失败状态。
- 影响：无需重新注册 Windows 任务；`CryptoTrading_DailyPaperUpdate` 与 `CryptoTrading_4H_PaperUpdate` 均通过同一封装器执行，下一次运行会自动使用新通知逻辑。
- 验证：使用 `[scriptblock]::Create((Get-Content -Raw scripts\run_logged_paper_task.ps1))` 完成 PowerShell 语法解析检查；未手动触发真实 daily/4h 任务，避免污染 paper 观察样本。
- Git：计划提交 `Notify on scheduled task completion`。

### 21:48:50 +08:00 - 提前安装 4h paper 定时任务
- 类型：运维 / 文档 / Git
- 改动：用户确认 2026-06-17 daily 缺失样本的根因为 GPT 会员/用量到期导致的外部执行资源中断，而非脚本、SQLite、定时任务或交易逻辑缺陷；据此提前以 `-RequiredStableDays 1` 安装 `CryptoTrading_4H_PaperUpdate`。
- 改动：更新 `TODO.md`，将 4h 任务安装项标记完成，并保留 daily 连续观察窗口仍从 2026-06-18 起算的说明。
- 影响：4h 任务已注册 00:10、04:10、08:10、12:10、16:10 五个触发器，仅运行 `paper cycle`，不执行 scan 或 add-from-scan；仍需观察 2026-06-19 00:10 首轮 4h run 是否成功。
- 验证：`Get-ScheduledTask -TaskName CryptoTrading_4H_PaperUpdate` 显示任务存在且触发器启用；`Get-ScheduledTaskInfo` 显示 `NextRunTime=2026-06-19 00:10:00`、`LastTaskResult=267011`（尚未首次运行）、`NumberOfMissedRuns=0`。
- Git：计划提交 `Record early 4h task install`。

### 21:42:30 +08:00 - 标记 2026-06-17 daily 缺失样本
- 类型：代码 / 数据库 / 运维 / 测试 / 文档 / Git
- 改动：新增 `python main.py db mark-run-failed --run-id ... --reason ...`，只允许把仍处于 `running` 的 observation run 显式标记为 `failed`，并要求写入失败原因。
- 改动：将 stale run `20260617_120503_5c574dad` 标记为 `failed`；该 run 于 2026-06-17 20:05 +08:00 启动，但未生成 scan、paper snapshots 或 reports，按缺失样本处理，不补跑。
- 改动：更新 `TODO.md`，将 5 天连续观察窗口从 2026-06-18 重新起算；若 2026-06-18 至 2026-06-22 全部成功且 `config_hash` 保持 `be7ec39ec21f6a83`，最早 2026-06-23 再安装 4h 任务。
- 影响：不修改 `settings.toml`，不改变交易策略；本地 SQLite 中 2026-06-17 run 的 `finished_at/status/error_message` 已更新，数据库文件仍不纳入 Git。
- 验证：`python tests\test_database.py` 通过；`python -m compileall main.py src tests` 通过；`python main.py db status` 显示 latest run `20260618_120504_52821c3b` 为 `success`、latest failed run 为 `20260617_120503_5c574dad`；`python main.py db stability --days 5` 预期返回非 0，显示 2026-06-17 `ready=false`、2026-06-18 `ready=true`、`ready_for_4h_task=false`。
- Git：计划提交 `Mark stale daily run failed`。

### 21:33:29 +08:00 - 增强实验结论索引页
- 类型：代码 / 报告 / 测试 / 文档 / Git
- 改动：升级 `python main.py experiment-index`，从“每份报告一行”改为按 `experiment_id` 聚合；仅扫描项目 `reports/`，不读取 Obsidian 作为输入；`*_review_*.md` frontmatter 优先覆盖 `abtest_summary_*.md`，单段 `abtest_*.md` 作为兜底。
- 改动：为 `max_holding_42_exit_review_2026-06-13_v1.md` 与 `max_holding_42_fixed_vs_conditional_review_2026-06-16_v1.md` 补充 `experiment_id`、`verdict`、`reason`、`next_action` 等结构化 frontmatter，并生成 `reports/2026-06-18/experiment_index_2026-06-18_v1.md`。
- 改动：按项目规则同步纳入 2026-06-18 20:05 daily 自动生成的 market scan、paper report、observation dashboard 与候选图表。
- 原因：A/B、summary 和 review 报告数量增加后，原索引需要人工扫描大量重复行；按实验聚合后可直接查看综合结论、核心变更、下一步和证据报告。
- 影响：不修改 `settings.toml` 或交易策略配置；Obsidian 仍作为索引输出目标，不作为数据输入源。
- 验证：`python tests\test_research_tools.py` 通过；`python -m compileall main.py src tests` 通过；`python main.py experiment-index` 成功输出项目与 Obsidian 索引；`python main.py db status` 显示 2026-06-18 daily run `20260618_120504_52821c3b` 成功；`config_hash` 保持 `be7ec39ec21f6a83`。
- Git：计划提交 `Aggregate experiment conclusion index`。

## 2026-06-16

### 23:02:12 +08:00 - 补充实验索引与三周观察仪表待办
- 类型：文档 / Git
- 改动：在 `TODO.md` 新增两项待办：增强实验结论索引页，以及增强 3 周观察仪表的 daily 汇总指标。
- 原因：报告数量增加后，实验结论和 paper 观察证据开始分散，需要把实验名、时间段、结论、`keep/retest/reject`、下一步，以及 `RECLAIM_PENDING`、TP1 EMA stop、开放持仓时长、RISK_OFF 新计划等三周复盘证据集中管理。
- 影响：仅更新任务清单，不修改策略代码、`settings.toml`、定时任务或数据库。
- 验证：检查 `TODO.md` 已在实验索引和观察仪表既有完成项旁新增两条未完成增强任务；`git status` 仅包含文档变更。
- Git：计划提交 `Add experiment index and observation dashboard todos`。

### 20:19:51 +08:00 - 跟踪 2026-06-16 daily 自动报告
- 类型：报告 / 文档 / Git
- 改动：将 2026-06-16 20:05 daily 自动生成的 market scan、paper report、three-week observation dashboard 和对应 5 张候选 SVG 图表纳入版本控制。
- 原因：项目规则要求提交生成的 `reports/`，便于三周 paper 观察期回溯每日样本和报告证据。
- 影响：不修改策略代码、`settings.toml` 或本地 SQLite 数据库；仅跟踪已生成的 Markdown/SVG 报告产物。
- 验证：定时任务返回码为 0；数据库 latest run 为 `20260616_120503_7c6775dd` 且 `status=success`；`config_hash` 保持 `be7ec39ec21f6a83`；报告文件与图表文件均存在。
- Git：计划提交 `Track 2026-06-16 daily reports`。

### 14:32:05 +08:00 - 固定 settings.toml 的 Git 换行规则
- 类型：配置 / 文档 / Git
- 改动：新增 `.gitattributes`，将 `config/settings.toml` 显式设置为 `text eol=lf`，并将 `.gitattributes` 自身固定为 LF。
- 原因：本机全局 `core.autocrlf=true` 会在 Git 触碰文件时提示或尝试把 LF 转为 CRLF；`settings.toml` 的 `config_hash` 依赖原始字节，换行变化会导致 paper 观察窗口出现不必要的 hash drift。
- 影响：不修改 `settings.toml` 内容，不改变策略参数；以后 `git restore`、checkout、merge 等操作应保持该文件 LF，降低误操作导致 `config_hash` 变化的风险。
- 验证：`git ls-files --eol -- config/settings.toml .gitattributes` 显示 `config/settings.toml` 命中 `attr/text eol=lf`；`_config_hash(Path("config/settings.toml"))` 仍为 `be7ec39ec21f6a83`；`settings.toml` 未出现在待提交变更中。
- Git：计划提交 `Pin settings line endings for stable config hash`。

### 10:05:00 +08:00 - 补跑固定 vs 条件式 42 根第三窗口
- 类型：实验 / 报告 / 文档 / Git
- 实验：继续 `max_holding_42_fixed_vs_conditional_sensitive`，补跑 `2023-07-01 -> 2024-07-01`，仍使用固定 `dynamic_master_full.json`、`max-symbols=40`、sensitive 策略与 42 根阈值，唯一变量为 `max_holding_bars_conditional=false -> true`。
- 结果：条件版 trades 769 -> 758、closed_trades 207 -> 197、胜率 49.76% -> 45.69%、PF 1.32 -> 1.20、Sharpe 1.40 -> 0.89、MDD 19.81% -> 20.69%、Net 38.96% -> 22.26%、stop rate 47.34% -> 48.22%。
- 分层：第三窗口全部闭合交易均为 `RISK_ON`，净 PnL 3896.37 -> 2225.91；证明条件式延迟持有在更早强趋势窗口反而保留了更多回吐仓位。
- 结论：`reject_candidate`。三窗口中条件版 2 段变差、3 段 MDD 均更高；不部署 `max_holding_bars_conditional=true`，下一步回到固定 42 根的 keep review，或另开 EMA20 斜率确认实验。
- 约束：未修改 `settings.toml`；保留用户已有暂存 `# test` 原样，不纳入本次提交。
- Git：计划提交 `Record third fixed versus conditional 42-bar window`。

### 00:10:00 +08:00 - 实验：固定 42 根退出 vs 条件式 42 根退出
- 类型：实验 / 报告 / 文档 / Git
- 实验：`max_holding_42_fixed_vs_conditional_sensitive`，固定 sensitive 策略、418-symbol master、`max-symbols=40` 与 42 根阈值，唯一变量为 `max_holding_bars_conditional=false -> true`。
- 结果：早期窗口条件版 Net 31.86% -> 27.57%、PF 1.48 -> 1.38、Sharpe 1.31 -> 1.21、MDD 20.66% -> 21.04%；近端窗口 Net 15.95% -> 30.75%、PF 1.31 -> 1.64、Sharpe 0.86 -> 1.42、MDD 11.05% -> 12.40%。两段 closed_trades 分别保持 134 与 110。
- 分层：差异主要来自 `RISK_ON`；早期净 PnL 3226.48 -> 2911.83，近端 1996.22 -> 3480.82；近端 `RISK_OFF` 基本不变。
- 结论：`retest`。条件版在近端捕捉延迟趋势赢家，但早期全面弱于固定退出，且两个窗口 MDD 均上升；暂不修改默认配置，下一步补 `2023-07-01 -> 2024-07-01` 第三非重叠窗口。
- 验证：四份 raw backtest 配置确认 baseline/variant 都为 42 根且 sensitive 参数一致；A/B 报告只列出 conditional bool 一个变化；两段样本均充足、覆盖 700 天、无重叠；生成两份 regime breakdown 与人工复盘报告。
- Git：计划提交 `Record fixed versus conditional 42-bar experiment`。

## 2026-06-15

### 20:15:00 +08:00 - 发现 config_hash 漂移，5 天稳定窗口重置
- 类型：运维 / 文档
- 改动：无代码变更；记录原因与新窗口起点。
- 原因：`b665076`（2026-06-14 晚条件退出实验）向 `settings.toml` 新增了 `max_holding_bars_conditional = false` 一行。该字段值未变，但 `_config_hash` 使用 `read_bytes()` 计算原始字节 hash，文件字节发生变化，导致 hash 从 `311322be2029f063` 变为 `be7ec39ec21f6a83`。今日 20:05 daily run 使用了新 hash，db stability 报告 `config_hash_drift`，6/13–6/14 两天样本作废。
- 影响：5 天稳定窗口重置为 2026-06-15（1/5）；4h 任务安装最早推迟至 **2026-06-20**（需 6/15–6/19 连续 5 天同 hash 且全部 ready）。当前 settings.toml 状态正确，无需任何修改。
- 教训：今后凡修改 `settings.toml`（即使只加注释或默认值行），须在 5 天窗口完成后再操作，或接受重置并更新 TODO 中的预计安装日期。
- 验证：`python main.py db stability --days 5` 显示 3/5、config_hash `be7ec39ec21f6a83`、今日 run ready；6/14 run 仍 ready 但 hash 不一致，稳定性整体仍为 `ready_for_4h_task=false`。


- 类型：代码 / 配置 / 测试 / 文档 / Git
- 改动：A/B 实验定义新增可选 `baseline_overrides`，runner 先构造固定 baseline，再从该 baseline 应用 variant override；新增 `max_holding_42_fixed_vs_conditional_sensitive`，两组均固定 sensitive 组合与 42 根阈值，唯一变量为 `max_holding_bars_conditional=false -> true`。
- 原因：原 `max_holding_42x4h_conditional` 实验以无时间退出为 baseline，无法直接回答条件式 42 根是否优于固定 42 根。
- 影响：不修改默认 `settings.toml`，不影响生产 paper 策略或 daily 的 `config_hash`；仅增强研究 A/B 编排能力。
- 验证：新增测试确认源 settings 不变、两组阈值均为 42、sensitive 参数一致且变更列表只有 conditional bool；`python tests\\test_abtest.py`、`python tests\\test_replay.py`、compileall 和 `git diff --check` 通过。
- Git：计划提交 `Support fixed baseline A/B overrides`。

### 23:43:00 +08:00 - 补交上一轮回测与当日 daily 报告
- 类型：报告 / Git
- 改动：将 2026-06-14 条件式 42-bar A/B 已生成的 8 份原始 dynamic-universe backtest 报告，以及 2026-06-15 20:05 daily 自动生成的 market scan、paper report、observation dashboard 和图表纳入版本控制。
- 原因：上一轮实验提交已包含 A/B 汇总与结论，但原始 baseline/variant backtest 报告仍未跟踪；新实验开始前先清理并固定既有证据边界。
- 影响：仅补交既有生成报告，不运行回测、不修改策略配置或生产数据库。
- 验证：确认 Git 变更仅为 `reports/` 与本条 `dailylog.md`；提交后推送并重新检查工作区。
- Git：计划提交 `Track generated experiment and daily reports`。

## 2026-06-14

### 22:45:00 +08:00 - 实验：条件 42-bar 时间退出（max_holding_42x4h_conditional）
- 类型：代码 / 实验 / 报告 / 测试 / Git
- 改动：新增 `max_holding_bars_conditional` bool 字段（`config.py`、`settings.toml`）；在 `replay.py` 将 42-bar TIME_EXIT 改为条件触发：仅当 `close < EMA20` 或 `close < entry_price` 时才强制退出，否则继续持仓。EMA20 计算复用 `tp1_ema_trailing_stop` 已有路径，零额外开销。`abtest.py` 新增 `holding_time_conditional` 和 `combined_regime_entry_exit_sensitivity_holding_conditional` 两个维度；`experiments.toml` 新增两个实验。测试：新增 `test_conditional_holding_time_override_sets_both_fields`（abtest）、`test_conditional_time_exit_does_not_fire_when_above_entry_and_ema`、`test_conditional_time_exit_fires_when_below_entry`（replay）；全套 10 个测试脚本通过。
- 动机：TIME_EXIT 复盘发现 95 单中 47 单两者均未触及，60/95 在 42-bar 强退后 7 日继续上涨（ORDIUSDT +52.9%、PEPEUSDT +40.6%）；固定退出切掉了延迟启动的赢家，条件退出保留真正停滞/反转的单子。
- walk-forward 结果（两时段均充足样本，418 个 symbol 动态 universe）：
  - 2024-07-01→2025-06-01：Net 2.4%→**27.6%**，PF 1.04→**1.38**，Sharpe 0.23→**1.21**，MDD 18.0%→21.0%（微升），Stop rate 84%→54%
  - 2025-06-01→2026-06-01：Net 3.1%→**30.8%**，PF 1.11→**1.64**，Sharpe 0.26→**1.42**，MDD 20.7%→**12.4%**（改善），Stop rate 86%→47%
  - Sensitive combo 叠加版结果完全相同（settings.toml 默认值已是 production sensitive combo，两个实验的 baseline 一致）。
- 结论：两时段净收益均改善 +25~28pp，PF 和 Sharpe 双升，最近时段 MDD 也改善；自动 verdict=retest（系统规则，不自动写 keep）。下一步需增加第三时段或更早时间段复测，并在通过 3 周 paper 观察后评估是否部署。
- 验证：5 个源文件 + 2 个测试文件，全套测试退出码 0；`git diff --check` 通过；settings.toml 改动仅为默认值 false，不影响生产 config_hash。
- Git：提交 `Add conditional 42-bar time exit experiment`（b665076）。

### 22:50:00 +08:00 - 验证快速连续 4h cycle 的幂等性与无锁运行
- 类型：测试 / 文档 / Git
- 改动：将 4h cycle 集成测试扩展为快速连续执行两轮，校验两个独立 `paper_4h_update` run 均成功、每轮各有 snapshot，且 scan/plan 数量不增加、`ENTERED` 事件不重复。
- 原因：开发计划第 14.3 和 14.6 要求重复 update 不重复写关键事件，快速连续执行两个 paper update 不产生 `database locked`；原测试只覆盖单轮 cycle。
- 影响：不修改生产策略、配置、数据库或定时任务，仅增强 4h 启用前的可执行验收证据。
- 验证：仓库 10 个带 `__main__` 的测试脚本全部退出码 0（含 database、trade_state、scanner_regime、replay、history、universe、abtest、summary、walk-forward、regime analysis）；`python -m compileall -q src main.py tests` 与 `git diff --check` 通过；生产稳定性审计仍为健康的 2/5，自然日门槛未被测试运行污染。
- Git：计划提交 `Verify consecutive 4h paper cycles`。

### 22:36:00 +08:00 - 将数据库底层健康接入 4h 安装门槛
- 类型：代码 / 数据库 / 测试 / 文档 / Git
- 改动：稳定性审计新增 `database_health/database_health_errors`，非修复式检查 schema v2、WAL、`synchronous=NORMAL`、foreign keys、busy timeout=30000、6 张观察表和 11 个必需索引。
- 原因：原先这些指标只由 `db status` 展示，5 天审计没有把它们纳入放行条件；底层配置退化时仍可能错误安装 4h 任务。
- 测试：新增 journal mode 退回 DELETE、删除必需索引、schema version 错配三个拒绝案例。
- 验证：`python tests\\test_database.py` 通过；`python -m compileall -q src main.py` 与 `git diff --check` 通过；生产 `python main.py db stability --days 5` 显示 schema v2、WAL、`synchronous=1`、`foreign_keys=1`、`busy_timeout_ms=30000`、无缺表/缺索引及健康错误，当前自然日样本 2/5，故仍为 `ready_for_4h_task=false`；安装拒绝探针退出码 1、包含稳定性门槛提示且未创建 `CryptoTrading_4H_PaperUpdate`。
- Git：计划提交 `Gate 4h task on database health`。

### 22:21:00 +08:00 - 将同日重复 daily_full 接入稳定性门槛
- 类型：代码 / 数据库 / 运维 / 测试 / 文档 / Git
- 改动：新增 `duplicate_daily_run_dates`，按北京时间自然日列出全部 daily_full run ID/status；同日超过一条即拒绝 4h 安装，不再静默只取最新 run。
- 原因：同日双 success 或失败后补跑会污染“一日一次”的前向观察样本，不能因最后一次成功而被遮蔽。
- 测试：新增同日双 success、同日 failed 后 success 两个拒绝案例；生产库当前 2026-06-13、14 均恰好一条 success。
- 验证：`tests/test_database.py`、`compileall` 与 `git diff --check` 通过；生产输出 `duplicate_daily_run_dates=[]`，两天逐 run 及全局审计继续通过；安装拒绝探针仍为非零且 4h 任务不存在。
- Git：计划提交 `Reject duplicate daily observation runs`。

### 22:08:00 +08:00 - 将 run 生命周期与日志元数据接入稳定性门槛
- 类型：代码 / 数据库 / 日志 / 测试 / 文档 / Git
- 改动：每个 success daily run 新增 `run_metadata_errors` 审计，要求 `finished_at` 存在且不早于 started_at、Git commit 为 40 位十六进制、log_path 非空且文件存在、success 不携带 error_message。
- 原因：避免残缺或手工误标为 success 的 run 只凭 status 通过 5 天门槛，确保运行审计链真实可追溯。
- 测试：稳定性种子补齐 commit 和真实日志；新增缺完成时间、完成时间倒序、日志文件不存在三个拒绝案例。
- 验证：`tests/test_database.py`、`compileall` 与 `git diff --check` 通过；生产两个 run 均为 `run_metadata_errors=[]`，配置、scan、snapshot、报告和 UTC 审计继续通过；安装拒绝探针保持非零且 4h 任务未注册。
- Git：计划提交 `Validate daily run lifecycle`。

### 21:55:00 +08:00 - 将配置口径一致性接入 5 天稳定性门槛
- 类型：代码 / 配置 / 数据库 / 测试 / 文档 / Git
- 改动：稳定窗口内 daily run 必须具有同一个非空 `config_hash`；新增 `observed_config_hashes/config_hash_errors`，并要求 `market_scans.config_hash` 与所属 run 一致。
- 口径：git commit 允许因工程修复跨日变化，不作为失败；策略配置 hash 变化则表示观察条件发生改变，不能拼成同一个 5 天样本。
- 测试：稳定性种子补齐 run/scan config hash；新增跨日配置漂移和 scan 未继承 run hash 两个拒绝案例。
- 验证：`tests/test_database.py`、`compileall` 与 `git diff --check` 通过；生产稳定性输出唯一 `observed_config_hashes=[311322be2029f063]`、`config_hash_errors=[]`，其余 scan/snapshot/report/UTC 审计继续通过；安装拒绝探针仍未注册 4h 任务。
- Git：计划提交 `Require stable observation config`。

### 21:43:00 +08:00 - 将报告 run 元数据完整性接入稳定性门槛
- 类型：代码 / 报告 / 数据库 / 测试 / 文档 / Git
- 改动：三类 daily Markdown 报告必须精确包含对应 `Run ID`、`Run type=daily_full` 与 `数据来源：SQLite`；新增 `report_metadata_errors` 定位具体报告和字段。
- 原因：原门槛只搜索 run_id 任意子串，无法识别报告误标 run type 或漏写 SQLite 来源，展示层可能与结构化主数据错配。
- 测试：稳定性报告种子改为真实元数据格式；新增错误 run type 和缺少 SQLite 来源两个拒绝案例。
- 验证：`tests/test_database.py`、`compileall` 与 `git diff --check` 通过；生产两个 run 的三类报告均为 `report_metadata_errors=[]`，scan 和 snapshot 审计继续通过；安装拒绝探针返回非零码且未注册 4h 任务。
- Git：计划提交 `Validate report run metadata`。

### 21:31:00 +08:00 - 将 scan 汇总与候选明细一致性接入稳定性门槛
- 类型：代码 / 数据库 / 测试 / 文档 / Git
- 改动：每个 daily run 新增 `scan_integrity_errors`，核对 `candidate_count`、`buy_candidate_count`、`watch_only_count` 与 `scan_candidates` 实际行数/action 分组是否一致。
- 门槛：即使存在一条 market scan，只要候选明细缺失或 action 汇总漂移，该 run 也不能 ready，防止三周复盘使用不完整选币样本。
- 测试：稳定性种子现在写入真实 candidate 明细；新增候选总数不一致和 BUY_CANDIDATE 计数不一致两个拒绝案例。
- 验证：`tests/test_database.py`、`compileall` 与 `git diff --check` 通过；生产两个 run 均为 `scan_integrity_errors=[]`、5 行候选明细与汇总一致，snapshot 仍为 4/4；安装拒绝探针继续通过且 4h 任务不存在。
- Git：计划提交 `Validate scan candidate integrity`。

### 21:18:00 +08:00 - 将 snapshot 完整覆盖接入 5 天稳定性门槛
- 类型：代码 / 数据库 / 测试 / 文档 / Git
- 改动：稳定性审计不再只检查 `snapshot_count > 0`，而是按 run 时间范围计算所有应由 paper update 处理的活动计划，输出 `expected_snapshot_count` 与 `missing_snapshot_plan_ids`。
- 口径：同一 daily run 在 add-from-scan 阶段已经归档的旧 WATCHING 计划不要求 snapshot；其余当时活动的计划必须逐一存在。
- 测试：新增两个活动计划只写一个 snapshot 的部分覆盖案例，要求即使 `snapshot_count > 0` 也必须拒绝安装；强化原缺失 snapshot 测试的具体 plan 断言。
- 验证：`tests/test_database.py`、`compileall` 与 `git diff --check` 通过；生产 2026-06-13、14 两个 run 均为 `snapshot_count=4`、`expected_snapshot_count=4`、缺失列表为空；安装拒绝探针继续通过，4h 任务未注册。
- Git：计划提交 `Require complete paper snapshots`。

### 21:04:00 +08:00 - 将 UTC 时间字段审计接入数据库状态与安装门槛
- 类型：代码 / 数据库 / 测试 / 文档 / Git
- 改动：新增 17 个观察时间字段的严格 UTC 审计，要求值可解析且明确以 `Z` 或 `+00:00` 表示零时区；`db status` 输出 `utc_timestamps_ok/utc_timestamp_errors`，5 天稳定性门槛在存在异常时拒绝 4h 安装。
- 诊断：错误条目包含 table、column、rowid 和 value，可直接定位无时区、本地时区或损坏时间戳。
- 测试：新增 `db status` 识别 `+08:00` 时间，以及完整 5 天审计因无时区 snapshot 时间而拒绝安装的测试。
- 验证：`tests/test_database.py`、`compileall` 和 `git diff --check` 通过；生产 `db status` 返回 `utc_timestamps_ok=true`、错误为空，稳定性输出同样无 UTC 错误且保持 `ready_for_4h_task=false`；安装拒绝探针返回非零码，执行前后 4h 任务均不存在。
- Git：计划提交 `Enforce UTC observation timestamps`。

### 20:52:00 +08:00 - 拆分稳定性日期连续性与窗口完整性
- 类型：代码 / 数据库 / 测试 / 文档 / Git
- 改动：`db stability` 的 `consecutive_days` 现在真实反映当前已观察日期是否连续；新增 `required_window_complete` 表示是否已收满要求天数，避免 `2/5` 连续日期被显示为不连续。
- 门槛：`ready_for_4h_task` 仍要求窗口完整、日期连续、每个 run ready、无重复 plan/event 且无外键错误，不降低安装标准。
- 测试：新增 2 天连续进度和 2 天日期断档测试，并补充完整 5 天字段断言。
- 验证：`tests/test_database.py`、`compileall` 与 `git diff --check` 通过；生产审计输出 `observed_day_count=2`、`consecutive_days=true`、`required_window_complete=false`、`ready_for_4h_task=false`；安装拒绝探针继续通过且未注册 4h 任务。
- Git：计划提交 `Clarify database stability progress`。

### 20:43:00 +08:00 - 禁止 4h 任务错过触发后延迟补跑
- 类型：代码 / 运维 / 测试 / 文档 / Git
- 改动：从 `CryptoTrading_4H_PaperUpdate` 设置中移除 `StartWhenAvailable`；电脑休眠或关机期间错过的 4h 时点不再于恢复后补跑，而是等待下一个固定时点。
- 原因：若错过 16:10 后在 20:05 左右恢复，补跑可能与 `CryptoTrading_DailyPaperUpdate` 并发；这与开发计划“不设置 20:10，避免重复和锁冲突”的约束相悖。
- 保留：daily 任务继续允许错过后补跑；4h 任务仍保留 5 个固定触发器、30 分钟执行上限和 `IgnoreNew` 防重入。
- 验证：`tests/test_database.py` 与 PowerShell parser 通过；任务对象探针确认 `StartWhenAvailable=False`、`ExecutionTimeLimit=PT30M`、`MultipleInstances=IgnoreNew`，5 个触发器为 00:10/04:10/08:10/12:10/16:10；现有 daily 仍为 `StartWhenAvailable=True/Ready`，4h 任务仍未注册；`git diff --check` 通过。
- Git：计划提交 `Prevent delayed 4h task conflicts`。

### 20:32:00 +08:00 - 将 4h 安装稳定性门槛前移到提权检查之前
- 类型：代码 / 运维 / 测试 / 文档 / Git
- 改动：`install_4h_paper_task.ps1` 现在先运行只读的 `db stability --days 5`，门槛通过后才检查管理员权限；普通 PowerShell 可直接预检稳定性，`2/5` 时不会触及任务注册。
- 安全约束：任务仍固定 00:10、04:10、08:10、12:10、16:10，不含 20:10；仍使用 30 分钟上限与 `IgnoreNew`，4h runner 仍只执行 `paper cycle`。
- 验证：`tests/test_database.py` 与 PowerShell parser 通过；生产库 `2/5` 非管理员拒绝探针返回 exit code 1 和稳定性门槛消息，未提前进入管理员检查；执行前后 `CryptoTrading_4H_PaperUpdate` 均未注册；`git diff --check` 通过。
- Git：计划提交 `Validate 4h task installation gate`。

### 20:19:34 +08:00 - 验收第二个新版 daily_full 真实样本
- 类型：运行验收 / 数据库 / 报告 / 文档 / Git
- 运行结果：Windows 任务于 20:05:01 自动触发，`LastTaskResult=0`；run `20260614_120504_da0fe713` 为 `daily_full/success`，20:06:30 完成，稳定性进度从 `1/5` 变为 `2/5`。
- 数据证据：本次恰有 1 个 scan、5 个候选、0 个 BUY_CANDIDATE、4 个开放计划 snapshot；market scan、paper report、observation dashboard 均包含同一 run_id、`daily_full` 与 SQLite 来源。
- 状态证据：ONDOUSDT 再次写入 `RECLAIM_PENDING_SET`，目标 4h kline_time=`2026-06-14T11:59:59Z`，继续保持 WATCHING；另外 3 个 ENTERED 计划正常写入 snapshot，证明 pending 与持仓状态可跨日持续推进。
- 验证：`db status` 显示 schema v2、WAL、30 秒 timeout、外键与 11 个索引正常；`db stability --days 5` 的两个 run check 均 `ready=true`，无重复 plan/event；生产库 `quick_check=ok`、外键错误为 0；`tests/test_database.py` 通过。
- 影响：只更新稳定性审计记录并纳入当天自动生成的 reports；未手工运行 daily，未安装 4h 任务，未修改策略配置或生产数据库内容。
- Git：计划提交 `Validate second daily database sample`。

## 2026-06-13

### 23:45:00 +08:00 - 完成 sensitive 与 42 根持仓过滤组合实验
- 类型：配置 / 回测 / 报告 / 文档 / Git
- 改动：在 `config/experiments.toml` 新增 `risk_off_no_core_entry_reclaim_ema_stop_sensitive_max_holding_42`，使用固定 full master 完成两个非重叠窗口 A/B、regime breakdown 和 95 笔 `TIME_EXIT` 后续 42 根 4h K 路径审查。
- 结果：两段 PF、Sharpe、净收益均改善；近端 MDD 20.74% -> 11.05%，较早窗口 MDD 18.03% -> 20.66%，总体 `retest`。路径审查显示 33/95 先触原 stop、15/95 先触原 TP1、60/95 一周后低于退出价。
- 影响：新增实验定义和研究报告，未修改 `settings.toml`，未运行 daily，未改变 20:05 连续观察样本。
- 验证：两段 `abtest-walk-forward` 成功；两份 `backtest-regime-breakdown` 成功；后续路径 95/95 均有完整 42 根 4h K；`compileall`、`tests/test_abtest.py`、实验定义加载和 `git diff --check` 均通过。
- Git：计划提交 `Evaluate sensitive 42-bar time exit`。

### 22:05:37 +08:00 - 验收首个新版 daily_full 真实样本
- 类型：运行验收 / 数据库 / 报告 / 日志 / 配置 / Git
- 运行结果：Windows 任务于 20:05:02 自动触发，`LastTaskResult=0`；run `20260613_120503_7a5f6892` 为 `daily_full/success`，20:06:39 完成，稳定性进度从 `0/5` 变为 `1/5`。
- 数据证据：本次恰有 1 个 scan、5 个候选、0 个 BUY_CANDIDATE、4 个开放计划 snapshot；无 `database is locked`、重复 plan/event 或外键错误，market scan、paper report、observation dashboard 均存在并包含同一 run_id、`daily_full` 与 SQLite 来源。
- 事件证据：ONDOUSDT 写入 1 条 `RECLAIM_PENDING_SET`，目标 4h kline_time=`2026-06-13T11:59:59Z`，状态保持 WATCHING；其余 3 个 ENTERED 计划也写入 snapshot。
- 日志修复：首样本日志文件已统一为 UTF-8，但 Python 中文经过 Windows PowerShell 5.1 native pipeline 时仍出现误解码；runner 增加 Console Input/OutputEncoding、`$OutputEncoding` 与 `PYTHONIOENCODING=utf-8`，独立中文路径/候选探针通过。未重跑 daily，不改变第 1 天样本。
- 验证：生产 `db stability --days 5` 返回 date=2026-06-13、run ready=true、总体 `ready_for_4h_task=false`；Python UTF-8 读取确认三份报告中文内容完整，数据库路径字段字节为正确 UTF-8。
- Git：本次提交 `Validate first daily database sample`。

### 16:22:36 +08:00 - 为受跟踪运行补充失败步骤上下文
- 类型：代码 / 数据库 / 日志 / 测试 / 文档 / Git
- 改动：新增 `_run_step` 上下文，将 `run_id`、步骤名、原异常类型和原因包装进异常；接入 daily 的 scan/add_from_scan/paper_update/paper_report/observation_dashboard、4h cycle 三步及手工 paper update。
- 改动：daily dashboard 的临时 Obsidian 路径恢复改用 `finally`，即使 dashboard 失败也不会污染同进程配置状态。
- 原因：满足 `数据库开发计划.md` 对 `database is locked` 日志必须明确记录 run_id 和当前步骤的要求，同时让所有失败 run 都具备一致诊断口径。
- 验证：故障注入 `sqlite3.OperationalError("database is locked")` 后，异常与 `runs.error_message` 均包含真实 run_id、`step=paper_update` 和锁错误，run status 为 failed；`test_database.py`、`test_trade_state.py`、`test_replay.py` 全部通过。
- Git：本次提交 `Add tracked run step context`。

### 16:18:00 +08:00 - 将外键与索引验收接入快速 db status
- 类型：代码 / 数据库 / 测试 / 文档 / Git
- 改动：为 `python main.py db status` 增加 `foreign_key_errors`、`indexes_ok` 和 `missing_indexes`，直接检查开发计划要求的 11 个观察索引，不再依赖临时 SQL 人工核对。
- 验证：生产库 `PRAGMA integrity_check=ok`、`foreign_key_check=[]`，11 个必需索引全部存在；所有 runs、scan、plan、event、snapshot 时间字段均为 `Z` 或 `+00:00` UTC 表达。
- 性能决策：完整 `integrity_check` 约需数十秒，`quick_check` 也约 11.5 秒，因此不纳入高频 `db status`；保留低成本外键与索引检查后命令耗时约 0.40 秒。
- 验证：`python tests\test_database.py` 通过，新增状态字段断言覆盖无外键错误、索引完整和空缺失列表。
- Git：本次提交 `Expose database index and foreign key health`。

### 16:14:31 +08:00 - 补齐三周数据库复盘汇总指标
- 类型：代码 / 数据库 / 测试 / 文档 / Git
- 改动：扩展 `python main.py paper db-summary`，新增 `observation_totals`，直接汇总 scan、候选、`BUY_CANDIDATE`、paper plan、reclaim pending plan、TP1、EMA trailing 激活/抬 stop/出场、`API_DELAY_SKIPPED` 和各终态数量。
- 改动：新增 `run_type_summary`，分别统计 `daily_full` 与 `paper_4h_update` 的 total/success/failed/running，并把 UTC started_at 转换为北京时间日期列表，便于审计两类运行是否连续覆盖。
- 原因：补齐 `数据库开发计划.md` 第十二节与三周后 15 个复盘问题的直接查询能力，避免用户从通用 `event_counts` 或 Markdown 手工拼接核心指标。
- 验证：`python tests\test_database.py` 通过，新增有数据断言覆盖 scan、candidate、BUY_CANDIDATE、plan、TP1、EMA 和北京时间日期；生产 `db-summary` 当前显示历史 scan=17、candidate=66、BUY_CANDIDATE=1、plan=25，且新版 `daily_full=0`，未把 backfill 误计为自动运行。
- Git：本次提交 `Expand database observation summary`。

### 16:10:00 +08:00 - 修复定时任务日志混合编码
- 类型：代码 / 运维 / 测试 / 文档 / Git
- 改动：新增 `scripts/run_logged_paper_task.ps1`，统一执行 daily 与 4h paper 命令，以 UTF-8 逐行写日志、设置 `PYTHONUTF8=1`、记录成功步骤和失败退出码，并向任务计划原样返回 Python exit code。
- 改动：`daily_paper_update.bat` 与 `paper_4h_update.bat` 保留为稳定计划任务入口，改为委托 PowerShell 日志执行器；检测到 UTF-16 BOM 的历史日志时自动带时间戳归档，杜绝 UTF-16、OEM 和 UTF-8 内容继续混写。
- 本地状态：原 `logs/daily_paper_update.log` 已原样移动为 `daily_paper_update.legacy_utf16_20260613_1610.log`；任务计划仍指向原 daily `.bat`，无需管理员重装，今晚 20:05 将创建全新 UTF-8 日志。
- 原因：旧日志起始为 UTF-16LE BOM，后续由 cmd/Python 追加单字节内容，导致人工读取和错误审计出现乱码；SQLite 数据不受影响，但不满足清晰运维日志要求。
- 验证：`python tests\test_database.py` 通过；三个 PowerShell 脚本 parser 均通过；测试验证 4h runner 命令不包含 scan/add-from-scan、使用 UTF-8 追加并传递非零退出码；任务 Action 路径和 WorkingDirectory 保持不变。
- Git：本次提交 `Normalize scheduled task logs to UTF-8`。

### 16:08:11 +08:00 - 验证 per-plan 事务原子回滚与故障隔离
- 类型：测试 / 数据库 / 文档 / Git
- 改动：新增双 plan 故障注入测试，强制第一笔在 `paper_plans` UPDATE 后、`paper_events` INSERT 前抛错，验证同一事务中的 plan/event/snapshot 全部回滚。
- 改动：验证第一笔失败后循环仍继续处理第二笔，第二笔正常推进为 `ENTERED` 并写入 event 与 snapshot；处理结束后整轮抛出汇总错误，供 `tracked_run` 标记 failed。
- 原因：为 `数据库开发计划.md` 第 7.4 节“单 plan 失败回滚、继续下一 plan、三类写入原子化”提供直接故障注入证据，而不是仅用成功路径推断原子性。
- 验证：`python tests\test_database.py` 通过；失败 plan 保持 `WATCHING` 且 event/snapshot 均为 0，后续 plan 为 `ENTERED` 且 event/snapshot 均为 1。
- 运行态：北京时间 16:08，尚未到 2026-06-13 20:05 的首个新版 daily_full 固定采样点，未手工运行 daily。
- Git：本次提交 `Verify per-plan transaction isolation`。

### 08:43:00 +08:00 - 补齐 4h cycle 与数据库锁竞争验收
- 类型：代码 / 数据库 / 测试 / 文档 / Git
- 改动：将 `paper cycle` 提取为可直接验收的 `_run_paper_cycle` 应用流程，并用 `finally` 恢复临时修改的 Obsidian 输出目录，避免 dashboard 异常污染同进程后续状态。
- 改动：新增临时 SQLite 集成测试，真实执行 `paper_4h_update` cycle，验证只推进已有计划，写入 success run、结构化 event、snapshot、独立 4h report/dashboard，且 scan 与 plan 数量不增加。
- 改动：新增写锁竞争测试，以缩短的测试 timeout 模拟生产 30 秒 busy timeout，验证业务 SQL 会等待、超时抛出 `database is locked`，并由 `tracked_run` 将该次 run 标记为 `failed`、保存错误原因。
- 改动：修正 `TODO.md` 中已过期的 09:00 定时任务描述；当前 daily 任务已是每天 20:05，并在 2026-06-12 20:05 成功执行。
- 原因：补齐 `数据库开发计划.md` 第 14.6、14.7 节对锁超时失败审计和 4h update 运行级行为的直接证据，避免只依赖静态脚本文本或局部单元测试验收。
- 验证：`python tests\test_database.py` 及完整 compile、状态机、回放、历史、scanner regime、universe、regime analysis、A/B 测试全部通过；生产定时任务为 `Ready`，`LastTaskResult=0`，下一次为 2026-06-13 20:05。
- 运行态：稳定性门槛仍为 `0/5`，因为 2026-06-13 20:05 的首个新版 `daily_full` 自然日样本尚未产生；未手工补跑。
- Git：本次提交 `Strengthen database cycle acceptance tests`。

### 08:33:47 +08:00 - 将结构化 paper 表切换为模拟盘主数据层
- 类型：代码 / 数据库 / 报告 / 测试 / 文档 / Git
- 改动：数据库 schema 升级到 v2，为 `paper_plans` 增加 source rank、仓位、入场、TP1、退出、PnL、last price、EMA trailing 等完整运行态字段，并从 legacy `paper_trades` 幂等迁移已有状态。
- 改动：`paper update` 的开放计划读取、状态前置检查和单向更新改为以 `paper_plans` 为准；`paper report` 与 observation dashboard 改为读取 `paper_plans/paper_events`。旧 `paper_trades/paper_trade_events` 继续在同一事务中兼容镜像，但不再是报告和状态推进的必需依赖。
- 改动：结构化事件优先写入 `paper_events`，legacy plan 存在时再镜像；报告和 dashboard 同时兼容旧 `RECLAIM_PENDING/ENTERED/STOPPED` 与新 `RECLAIM_PENDING_SET/RECLAIM_CONFIRMED_ENTERED/EMA_TRAILING_STOPPED` 事件语义。
- 改动：删除不再被调用的 legacy row 转换函数，消除 `paper update`、paper report 和 observation dashboard 误回退读取旧表的代码入口。
- 原因：补齐 `数据库开发计划.md` 的核心验收项“SQLite 成为 paper trading 主数据源”以及 report/dashboard 从结构化表读取，避免仅建立观察副本却继续依赖 legacy 表。
- 验证：新增 schema v2 状态迁移测试，以及删除 legacy plan/event 行后仍能推进状态、写结构化事件并生成 4h paper report/dashboard 的独立性测试；完整数据库、状态机、回放、历史、scanner regime、universe、regime analysis 和 A/B 测试全部通过。
- 验证：生产库执行幂等迁移后为 schema version 2、WAL、foreign_keys=1、busy_timeout=30000；成功从结构化表加载 25 个计划和 25 条 plan 事件路径，新旧层均为 25 个计划、57 个事件，`missing_operational_fields=0`，当前开放计划 4 个。
- 运行态：2026-06-13 08:26 检查时 daily 任务最近一次仍为 2026-06-12 20:05 成功，下一次为 2026-06-13 20:05；稳定性门槛仍为 `0/5`，未提前手工运行，避免破坏固定采样口径。
- Git：本次提交 `Make structured paper tables canonical`。

## 2026-06-12

### 23:04:25 +08:00 - 完成结构化 paper 事件与 4h 报告审计
- 类型：代码 / 数据库 / 报告 / 测试 / 文档 / Git
- 改动：统一新写入 `paper_events` 的事件语义，新计划写 `PLAN_CREATED`，reclaim 后入场写 `RECLAIM_CONFIRMED_ENTERED`，TP2 和 EMA trailing stop 出场分别写 `TP2_HIT`、`EMA_TRAILING_STOPPED`；保留 legacy `paper_trade_events` 兼容口径。
- 改动：4h paper report 增加本次 `run_id` 的结构化状态变化表、事件总数和 `API_DELAY_SKIPPED` 数量；K 线未收盘或 K 线 API 延迟时按 plan 跳过，不再改写 `paper_plans`，并按 plan + kline_time 防重复写入跳过事件。
- 改动：`market_scans` 自动保存 run 的 `config_hash` 和扫描 `market_regime`，候选与 `paper_plans` 继承同一市场环境；补充 `EXPIRED` 终态与单向流转保护。
- 原因：完成 `数据库开发计划.md` 对事件可复盘性、4h 报告、API 延迟安全、元数据关联和幂等性的逐项收尾，确保三周后可直接按结构化表归因。
- 验证：`python -m compileall main.py src tests -q`、`test_database.py`、`test_trade_state.py`、`test_replay.py`、`test_history.py`、`test_scanner_regime.py`、`test_universe.py`、`test_regime_analysis.py`、`test_abtest.py`、`test_abtest_summary.py`、`test_abtest_walk_forward.py` 全部通过；两个 PowerShell 安装脚本 parser 检查及 4h batch 禁止 scan/add-from-scan 检查通过。
- 验证：生产库 `db status` 为 schema version 1、WAL、foreign_keys=1、busy_timeout=30000、无缺表；`db stability --days 5` 当前按预期返回 exit 2、`observed_day_count=0`、`ready_for_4h_task=false`；每日任务最近一次 2026-06-12 20:05 成功，下一次为 2026-06-13 20:05。
- Git：本次提交 `Complete structured paper event audit`。

### 22:57:48 +08:00 - 更新三周每日运行 daily 的必要性说明
- 类型：文档 / Git
- 改动：更新 `为什么未来三周每天运行daily.md`，将旧的五条独立命令说明修正为当前统一的 `python main.py daily --account demo` 和 `daily_full` run_id 执行链。
- 改动：补充 SQLite 逐日证据链、固定 20:05 采样口径，以及 `python main.py db stability --days 5` 连续自然日门槛为何不能由同日补跑或三周后单次运行替代。
- 原因：数据库化和统一 daily 入口已经落地，原说明需要与当前实现一致，并进一步解释连续前向采样对状态事件、快照、报告关联和无人值守稳定性验证的意义。
- 验证：对照 `scripts/daily_paper_update.bat`、`main.py` 的 `daily` 路径和 `src/crypto_trading_system/paper_db.py` 的稳定性审计规则人工核对；仅文档变更，未运行代码测试。
- Git：本次提交 `Update daily observation rationale`。

### 22:48:56 +08:00 - 准备 4h 更新任务并增加五天稳定性硬门槛
- 类型：代码 / 脚本 / 测试 / 运维 / 文档 / Git
- 改动：新增 `python main.py db stability --days 5`，自动审计连续 daily_full 日期、run success、market scan、snapshot、三类带 run_id 报告、重复 plan/event、外键错误及 `database is locked`；未满足时退出码为 2。
- 改动：新增 `scripts/paper_4h_update.bat`，只运行 `python main.py paper cycle --run-type paper_4h_update --account demo`，不执行 scan 或 add-from-scan，并记录独立 `logs/paper_4h_update.log`。
- 改动：新增 `scripts/install_4h_paper_task.ps1`，注册 00:10、04:10、08:10、12:10、16:10 五个触发器；安装前强制通过 5 天数据库审计，设置 30 分钟执行上限和 `IgnoreNew` 防止任务重叠。当前未实际安装任务。
- 改动：同步更新 `README.md`、`TODO.md`、`开发计划.md` 和 `数据库开发计划.md`，明确管理员最后执行步骤。
- 验证：`test_database.py` 增加完整 5 天通过、缺 snapshot 拒绝和 4h batch 禁止 scan/add-from-scan 测试并通过；PowerShell parser 检查安装脚本通过；当前生产库审计正确返回 `observed_day_count=0`、`ready_for_4h_task=false`。
- Git：本次提交 `Prepare gated 4h paper task`。

### 22:40:52 +08:00 - 实现三周模拟盘 SQLite 结构化观察基础设施
- 类型：代码 / 数据库 / 脚本 / 测试 / 文档 / Git
- 改动：在现有 `data/crypto_trading.db` 上新增兼容 schema migration，创建 `schema_metadata`、`runs`、`market_scans`、`paper_plans`、`paper_events`、`paper_snapshots`，并为旧 scan、paper trade 和 event 幂等回填观察数据。
- 改动：统一 SQLite 连接为 WAL、`synchronous=NORMAL`、`foreign_keys=ON`、`busy_timeout=30000`、30 秒 connect timeout；新增 `python main.py db init/status`。
- 改动：将 daily 定时脚本改为调用单一 `python main.py daily --account demo`；daily 五个步骤共享 `daily_full` run_id，失败时 runs 写入 error_message，成功后标记 success。
- 改动：paper update 将 API 请求移出写事务，每个 plan 使用独立短事务；增加前置状态条件、非法状态回滚拒绝、stop 不降低校验、严格 4h close_time 校验、`API_DELAY_SKIPPED`、结构化 event 和每 run/plan snapshot。
- 改动：新增 `paper db-summary`、`paper db-events`、`paper db-export` 与 `paper cycle --run-type paper_4h_update`；4h cycle 不执行 scan/add-from-scan，并使用独立报告文件名前缀。暂不安装 4h Windows 任务，需先通过 5 天稳定观察门槛。
- 改动：market scan、paper report、observation dashboard 增加 `run_id`、`run_type` 和 SQLite 数据来源说明；同步更新 `README.md`、`TODO.md`、`开发计划.md` 与 `数据库开发计划.md`。
- 验证：`python -m compileall main.py src tests -q` 通过；`test_database.py`、`test_trade_state.py`、`test_replay.py`、`test_abtest.py`、`test_history.py`、`test_scanner_regime.py`、`test_universe.py`、`test_abtest_summary.py`、`test_abtest_walk_forward.py`、`test_regime_analysis.py` 全部通过。
- 验证：生产库执行 `python main.py db init/status` 成功，确认 schema version=1、journal_mode=wal、synchronous=1、foreign_keys=1、busy_timeout=30000、open_plan_count=4；`paper db-events` 和三份 CSV 导出成功。
- Git：本次提交 `Add structured paper observation database`。

### 22:24:29 +08:00 - 保存数据库开发前基线
- 类型：脚本 / 文档 / Git
- 改动：提交用户新增的 `数据库开发计划.md`，作为三周模拟盘 SQLite 主数据源、状态事件、快照、复盘查询和后续 4h update 的开发依据。
- 改动：一并保存当前 `scripts/install_daily_task.ps1` 调整，包括 `RunLevel Limited`、允许电池供电运行及 `StartWhenAvailable` 设置。
- 影响：建立数据库开发开始前的可追溯 Git 基线；本提交不包含数据库功能实现。
- 验证：使用 PowerShell parser 检查 `scripts/install_daily_task.ps1`，语法通过；人工读取并确认数据库开发计划文件可正常按 UTF-8 加载。
- Git：本次提交 `Save database development baseline`。

### 21:25:26 +08:00 - 补充三周内每日运行 daily 的必要性说明
- 类型：文档 / Git
- 改动：新增 `为什么未来三周每天运行daily.md`，详细说明 daily 的扫描快照、计划导入、模拟盘状态推进、事件记录和 dashboard 沉淀职责，并解释为何三周后单次运行或事后历史回放不能替代连续前向观察。
- 影响：明确三周观察的数据口径、漏跑风险、每日最低检查项及“每日运行不等于实时监控”的能力边界，便于后续统一执行和解释实验结果。
- 验证：人工检查文档覆盖 `RECLAIM_PENDING`、TP1 EMA trailing、持仓时长、市场环境、定时任务可靠性和漏跑影响；仅文档变更，未运行代码测试。
- Git：本次提交 `Document daily observation rationale`。

### 21:09:43 +08:00 - 将三周观察仪表接入 daily 定时脚本
- 类型：代码 / 脚本 / 报告 / 运维 / Git
- 改动：在 `scripts/daily_paper_update.bat` 的 `paper report` 之后新增 `python main.py observation-dashboard --account demo`，并向 `logs/daily_paper_update.log` 写入独立的 `observation-dashboard done` 完成标记。
- 改动：修复 observation dashboard 的 `RISK_OFF-tagged` 统计口径；除英文 `RISK_OFF` 外，同时识别扫描候选实际保存的中文风险标记“BTC/ETH 大盘环境未确认强势”。
- 影响：从下一次每天 20:05 定时运行开始，将自动生成三周观察仪表，持续记录 reclaim 后续、TP1 EMA trailing、逐仓持仓时长及每日 action/RISK_OFF 摘要。
- 验证：运行 `python -m compileall main.py src -q` 通过；两次手动运行 `python main.py observation-dashboard --account demo` 成功生成 v1/v2，v2 确认今日 `All candidates` 与 `RISK_OFF-tagged` 均为 5 个 `WATCH_ONLY`。
- Git：本次提交 `Add observation dashboard to daily task`。

## 2026-06-11

### 23:15:00 +08:00 - 实现并运行 large_cap_only_risk_off 实验
- 类型：代码 / 配置 / 回测 / 文档
- 改动：`config.py` 新增 `risk_off_large_cap_buy_enabled` 字段（默认 `False`，不改现有行为）。
- 改动：`scanner.py` 扩展豁免逻辑，新参数 `risk_off_large_cap_buy_enabled`；RISK_OFF 下 `{"BTCUSDT","ETHUSDT","BNBUSDT","SOLUSDT"}` 可独立豁免，与旧的 `risk_off_core_buy_enabled` 互不干扰。
- 改动：`backtest/replay.py` 同步透传新参数。
- 改动：`abtest.py` 新增 `large_cap_regime` dimension，`experiments.toml` 新增 `large_cap_only_risk_off` 实验定义（`risk_off_core_buy_enabled=false` + `risk_off_large_cap_buy_enabled=true`）。
- 改动：`tests/test_abtest.py` 新增两个测试：实验加载覆盖验证、`_analyze_ticker` 豁免行为验证（BNBUSDT 不被 regime 阻断，ADAUSDT 仍被阻断）。
- 结果（两段 walk-forward）：
  - 早期段（2024-07→2025-06）baseline net +2.37% → variant +13.54%（+11.17%），PF 1.04→1.22，MDD 18.03%→17.01%，方向改善
  - 近端段（2025-06→2026-06）baseline net +3.12% → variant -3.12%（-6.24%），PF 1.11→0.95，MDD 20.74%→22.19%，方向恶化
  - 结论：`retest`，两段方向不一致；在已有 altcoin 组合上叠加 BNB/SOL RISK_OFF 入场，熊市反而拖累整体，与单独 large-cap 回测结论不一致，暂不 keep。
- 验证：`python -m compileall main.py src tests -q` 无错；`test_abtest.py` 和 `test_replay.py` 全通过；两段 A/B 回测 exit code 0。

### 22:50:00 +08:00 - 市值分层跨区间复测 + max_holding 三阈值两段 walk-forward
- 类型：回测 / 配置 / 文档
- 改动：在 `config/experiments.toml` 新增 `max_holding_18x4h_no_tp1` 和 `max_holding_42x4h_no_tp1` 两个实验定义，分别对应 18 根和 42 根 4h 持仓上限。
- 改动：串行跑 7 段回测：large-cap（BTC/ETH/BNB/SOL）早期段、altcoin 早期段、max_holding 三阈值各两段；生成对应报告。
- 结果（市值分层两段非重叠 walk-forward）：
  - 牛市（2024-07→2025-06）large-cap closed=25、PF 2.02、净收益 +14.14%、MDD 7.77%；altcoin closed=54、PF 1.35、净收益 +11.71%、MDD 15.92%
  - 熊市（2025-06→2026-06）large-cap closed=30、PF 1.19、净收益 +3.46%、MDD 11.36%；altcoin closed=57、PF 0.76、净收益 -10.26%、MDD 23.44%
  - 结论：large-cap 两段均正收益，熊市优势显著；altcoin 熊市严重拖累，结论 `candidate_keep_review`，可推进 `large_cap_only_risk_off` 实验设计。
- 结果（max_holding 三阈值两段 walk-forward）：
  - 18根：早期段 +17.98%→+34.25%（Δ+16.3%）MDD 12.09%，近端段 +5.46%→+21.06%（Δ+15.6%）MDD 11.50%
  - 30根：早期段 +17.98%→+25.03%（Δ+7.1%）MDD 12.84%，近端段 +3.32%→+27.28%（Δ+24.0%）MDD 11.84%
  - 42根：早期段 +17.98%→+31.66%（Δ+13.7%）MDD 13.08%，近端段 +5.46%→+26.93%（Δ+21.5%）MDD 9.27%
  - 结论：三阈值两段全部正向改善，方向稳健，不是过拟合 30 根。42根 MDD 最低（近端 9.27%），是最平衡候选；30根近端绝对净收益最高；18根净收益最高但持仓时间过短。整体结论 `candidate_keep_review`，建议优先考虑 42根。
- 影响：TODO.md 两项跨区间复测任务标为完成，新增 `large_cap_only_risk_off` 实验设计和 2026-07-02 复盘决策两项待办。
- 验证：所有回测命令正常退出（exit code 0），报告文件确认生成。

### 21:37:08 +08:00 - 补齐 daily 定时任务安装脚本
- 类型：脚本 / 运维 / 文档 / Git
- 改动：新增 `scripts/install_daily_task.ps1`，用于以管理员 PowerShell 覆盖注册 Windows 任务计划 `CryptoTrading_DailyPaperUpdate`，触发时间固定为每天 `20:05`，执行 `scripts\daily_paper_update.bat`，并输出 trigger 与 `Get-ScheduledTaskInfo` 便于验证。
- 改动：更新 `TODO.md` 运维待办，将修正计划任务的下一步明确为运行 `powershell -ExecutionPolicy Bypass -File scripts\install_daily_task.ps1` 后检查 `LastRunTime`、`LastTaskResult` 和 `logs/daily_paper_update.log`。
- 影响：当前非管理员会话仍无法直接修改系统计划任务；后续只需在管理员 PowerShell 中运行脚本即可避免手工配置遗漏，并把任务从 09:00 调整到 20:05。
- 验证：本会话中 `Set-ScheduledTask`、`schtasks /Change /ST 20:05`、`schtasks /Create /F /IT` 均因 `Access is denied` 被系统拒绝；计划任务当前仍显示 `Next Run Time=2026-06-12 9:00:00`，需要提升权限执行安装脚本完成最终修改。
- Git：本次提交 `79c14b4 Add daily task installer`。

### 21:30:39 +08:00 - 完成三周等待期五项补强
- 类型：代码 / 配置 / 回测 / A/B / 报告 / 测试 / 文档 / Git
- 改动：修复 `tp1_ema_trailing_stop` 两个一致性问题：`step_trade` 只有在调用方明确传入 `tp1_trailing_ema_stop_ready=true` 时才允许 TP1 EMA trailing 激活；`paper_trades` 新增 `tp1_trailing_ema_stop_active` 持久化列，并在旧库上自动 `ALTER TABLE` 补列。
- 改动：新增 `backtest.max_holding_bars_without_tp1` 与实验 `max_holding_30x4h_no_tp1`；回测中持仓进入 `ENTERED` 后若 30 根 4h 未触 TP1，则按 `TIME_EXIT` 防守性退出，并纳入 closed trade 指标。
- 改动：新增 `research_tools.py` 和 CLI：`split-symbol-master` 拆分 large-cap/altcoin master，`experiment-index` 生成实验结论索引，`observation-dashboard` 生成三周观察仪表；`daily` 流程在 paper report 后自动输出观察仪表。
- 改动：将 `dynamic_master_full.json` 拆成 `dynamic_master_full_large_cap.json` 与 `dynamic_master_full_altcoin.json`；分别运行当前 sensitive 组合回测，并生成 `market_cap_split_sensitive_2026-06-11_v1.md`。
- 影响：三周观察期每天会额外沉淀 `RECLAIM_PENDING` 后续、TP1 EMA trailing 激活/抬止损/出场、开放持仓时长、今日扫描 action 与 RISK_OFF 摘要；后续实验可以从 `experiment_index_2026-06-11_v2.md` 快速检索结论。
- 结果：市值分层近端窗口 `2025-06-01 -> 2026-06-01` 显示 large-cap（BTC/ETH/BNB/SOL）closed_trades=30、PF=1.19、净收益 +3.46%、MDD 11.36%；altcoin closed_trades=57、PF=0.76、净收益 -10.26%、MDD 23.44%，结论为 `retest / candidate_keep_review`。
- 结果：`max_holding_30x4h_no_tp1` full master A/B 显示 closed_trades 63 -> 111、stop_rate 84.13% -> 31.53%、PF 1.11 -> 1.56、净收益 3.32% -> 27.28%、MDD 20.85% -> 11.84%，结论为 `retest / candidate_keep_review`，需跨区间复测。
- 验证：运行 `python -m compileall main.py src tests`、`python tests\test_trade_state.py`、`python tests\test_replay.py`、`python tests\test_abtest.py` 均通过；运行 `python main.py paper report --account demo` 成功生成 `paper_report_2026-06-11_demo_v5.md`，验证 SQLite 新列迁移和读取正常。
- Git：本次提交 `Add three-week validation workflows`。

### 21:01:16 +08:00 - 增强 paper report 三周验证追踪字段
- 类型：代码 / 报告 / 测试 / Git
- 改动：在 `trade_state.step_trade` 中新增 `TP1_EMA_TRAILING_ACTIVATED` 与 `TP1_EMA_TRAILING_RAISED` 事件，并在 EMA20 trailing stop 触发止损时写入明确事件说明；在 `paper_trader.generate_paper_report` 中新增 TP1 EMA trailing stop 激活次数、抬止损次数、EMA stop 出场次数、当前激活持仓统计，以及 `RECLAIM_PENDING` 后续追踪表。
- 改动：更新 `tests/test_trade_state.py` 覆盖 TP1 EMA trailing 激活、抬止损和 EMA stop 出场事件；更新 `tests/test_abtest.py`，让相关 A/B 单测显式设置 baseline 默认值，避免被当前生产配置默认开关影响。
- 影响：三周后复盘模拟盘时，可以直接从 paper report 判断 TP1 EMA trailing 是否真正介入、是否抬过止损、是否导致出场，也可以看到 `RECLAIM_PENDING` 后续是重新入场、跌破/失效还是仍在等待。新报告 `reports/2026-06-11/paper_report_2026-06-11_demo_v4.md` 当前显示 ONDOUSDT 的 reclaim outcome 为 `still_waiting`，TP1 EMA trailing 统计均为 0。
- 验证：运行 `python -m compileall main.py src tests`、`python tests\test_trade_state.py`、`python tests\test_replay.py`、`python tests\test_abtest.py` 均通过；运行 `python main.py paper report` 成功生成 v4 paper report。
- Git：本次提交 `Add paper report validation tracking`。

### 20:49:20 +08:00 - 手动运行 daily 扫盘并发现定时任务配置问题
- 类型：扫描 / 模拟盘 / 报告 / 脚本 / 运维 / Git
- 改动：手动运行 `python main.py daily` 完成日常流程，生成 `reports/2026-06-11/market_scan_2026-06-11_v2.md`、`paper_report_2026-06-11_demo_v3.md` 和对应图表；修正 `scripts/daily_paper_update.bat`，将硬编码中文项目路径改为 `%~dp0..` 自动定位项目根目录，降低 `cmd.exe` 编码解析风险。
- 影响：本次 scan_id=`d81f9cdeba05`，候选 5 个；`paper_added=0`、`paper_skipped_action=5`，未新增模拟盘计划；模拟盘更新 4 笔开放观察/持仓，未实现 PnL 从 -128.53 USDT 改为 -61.72 USDT；新增 1 次 `RECLAIM_PENDING`，ONDOUSDT 触碰 entry zone 但 4h 收盘未重新站上 `entry_high`，继续等待。
- 验证：`python main.py daily` 成功输出 `daily=completed`；检查 Windows 任务计划发现 `CryptoTrading_DailyPaperUpdate` 当前触发时间为每天 09:00，非预期 20:05，且 `LastRunTime=1999-11-30` 表示尚未成功自动运行。尝试 `Set-ScheduledTask` 与 `schtasks /Change /ST 20:05` 均因 `Access is denied` 失败，需要管理员权限或任务计划程序中输入当前用户任务密码后调整。
- Git：本次提交 `Run daily scan and fix daily batch path`。

### 20:39:46 +08:00 - 调整 handoff.md 更新规则为顶部插入
- 类型：文档 / 规则 / Git
- 改动：更新 `AGENTS.md` 的 `Context Handoff` 规则，明确新增 handoff 条目不得覆盖、删除或重写历史内容；最新条目应插入到 `handoff.md` 顶部、位于文件级标题或说明之后，旧条目作为历史记录完整保留并下移。
- 影响：后续上下文交接会按时间倒序保留，最近交接信息更容易读取，同时避免此前更新 handoff 时覆盖旧内容。
- 验证：已检查 `AGENTS.md` 目标段落内容；未运行代码测试（仅文档规则变更）。
- Git：本次提交 `Update handoff insertion rule in AGENTS`。

### 14:55:00 +08:00 - daily_trend_required A/B 实验：reject_candidate
- 类型：代码 / 回测 / A/B / 报告 / Git
- 改动：新增 `analysis.daily_trend_required` 参数（默认 false）；scanner `_analyze_ticker` 和 replay `_analyze_ticker` 调用均传入此参数；`trend_ok` 逻辑改为：启用时必须同时满足 `trend_1d`（`price > EMA20_1d >= EMA50_1d * 0.98`），否则仅需 `trend_4h OR trend_1d`。修复：replay.py 初版漏传参数导致 baseline=variant，修复后 v2 重跑。
- 影响：早期段（2024-07→2025-06）：PF 0.91→0.97，净收益 -5.59%→-3.54%，MDD 小幅上升（18.72%→19.52%）。近端段（2025-06→2026-06）：PF 0.73→0.32，净收益 -10.62%→-22.71%，MDD 24.24%→28.30%，止损率 77%→89%，大幅恶化。
- 验证：近端段 verdict=`reject_candidate`；根因：弱市中日线趋势恢复滞后，过滤后实际在更高位置入场，质量反而更差；不适合作为单独规则使用。
- Git：commit `18663db`（实验代码）、`1642731`（修复 replay 漏传参数），已 push。


- 类型：代码 / 测试 / Git
- 改动：`paper_trader.py` `update_paper_trades` 补全两项与回测不一致的逻辑：
  1. `entry_reclaim_close_enabled`：WATCHING 状态下，当前价格已触碰 entry zone 但最新已收盘 4h K线收盘价低于 `entry_high` 时，跳过本次入场判断，写入 notes 并继续等待；
  2. `tp1_ema_trailing_stop_enabled`：ENTERED/TP1_HIT 状态下，从 Binance 拉取最近 25 根 4h K线（去掉未收盘的最后一根），计算 EMA20 后传入 `step_trade`；两者共用同一次 API 请求（`klines_4h_cache`）。
  3. 同步传入 `move_stop_to_breakeven_on_tp1`（此前也未传，现在一并对齐）。
- 影响：`risk_off_core_buy_enabled` 原本口径一致；修复后三项规则在模拟盘中全部生效，回测与模拟盘行为对齐。
- 验证：`test_trade_state`、`test_abtest`、`test_replay` 全部通过。
- Git：commit `417681d`，已 push。


- 类型：代码 / 回测 / A/B / 报告 / Git
- 改动：新增 `combined_regime_entry_exit` dimension 至 `abtest.py` ALLOWED_OVERRIDE_PATHS；新增 `risk_off_no_core_entry_reclaim_ema_stop` 实验至 `config/experiments.toml`（三项叠加：RISK_OFF 停开核心币 + 入场收盘确认 + TP1 EMA20 跟踪止损）。
- 改动：串行运行早期段（`2024-07-01 -> 2025-06-01`，baseline `de633d08ae00`，variant `1159c2ab9b5e`）和近端段（`2025-06-01 -> 2026-06-01`，baseline `9d9664bd1085`，variant `4eb256b0c879`）。
- 影响：早期段：closed_trades 52→50，PF 0.91→1.53，avg_R -0.03→+0.37，净收益 -5.59%→+16.74%，MDD 18.72%→14.99%，Sharpe -0.25→1.07。近端段：closed_trades 49→64，PF 0.73→1.05，avg_R -0.20→+0.03，净收益 -10.62%→+1.21%，MDD 24.24%→18.68%，Sharpe -0.54→0.16。两段 net/PF/MDD 全面改善，stop_rate 小幅上升（副作用）。
- 验证：汇总 `unique_coverage_days=700`，`overlap_periods=0`，`sufficient_periods=2`，verdict=**`candidate_keep_review`**；为继 `risk_off_no_core_entry_reclaim` 后第二个达到此门槛的实验，且近端 MDD 改善更显著（-5.56pp vs 组合基线的 -9.76pp）。
- 注意：两段不能并行运行（SQLite 数据库锁），需串行执行。


- 类型：回测 / A/B / 报告
- 改动：运行早期段（`2024-07-01 -> 2025-01-01`，baseline `ec6edacdae47`，variant `7b1855f719a3`），与已有近端段汇总为两段非重叠 walk-forward。
- 影响：早期段：closed_trades 35→49，PF 1.30→1.41，净收益 +7.14%→+11.82%，Sharpe 0.78→1.20，MDD 10.67%→10.54%，方向全面改善。近端段：PF 0.58→0.75，净收益 -13.17%→-10.31%，MDD 小幅上升（19.43%→19.78%），两段均样本充足且净收益/PF 改善，但近端绝对值仍负；TP2 rate 在两段均下降（副作用：EMA 跟踪止损提前锁定部分本可到 TP2 的仓位）。
- 验证：汇总 `unique_coverage_days=427`，`overlap_periods=0`，`sufficient_periods=2`，`net_improved_periods=2`，`drawdown_improved_periods=1`，verdict=**`retest`**；近端 MDD 未改善是无法升级到 `candidate_keep_review` 的主因。
- 结论：`tp1_ema20_trailing_stop` 在牛市段（早期）效果显著，在震荡/弱市段（近端）方向正确但不足以扭转负收益；下一步设计与 `risk_off_no_core_entry_reclaim` 的组合实验。


- 类型：回测 / A/B / 报告
- 改动：运行 `tp1_ema20_trailing_stop` A/B，baseline `8a881bbd789e`，variant `c5afb1a8dbdc`，区间 `2025-01-01 -> 2025-09-01`，使用 `dynamic_master_full.json`，`--max-symbols 40 --allow-data-gaps`。
- 影响：variant closed_trades=53（baseline=42），样本充足；PF 0.58→0.75，avg_R -0.32→-0.14，净收益 -13.17%→-10.31%，MDD 19.43%→19.78%（小幅上升），stop_rate 80.95%→86.79%（略上升），Sharpe -1.03→-0.77。fee_drag 51→72（换手率上升带来更多手续费）。TP2 rate 下降（19.05%→13.21%），说明跟踪止损提前锁定了一些本可到 TP2 的仓位。
- 验证：verdict=`retest`；绝对值仍为负收益，需跨时段 walk-forward 或与 `risk_off_no_core_entry_reclaim` 组合后验证。
- Git：（报告自动生成，无代码改动）

### 10:05:00 +08:00 - 创建性能优化文档并提交
- 类型：文档 / Git
- 改动：创建 `reports/2026-06-11/perf_optimization_2026-06-11.md`，记录 5 轮 profiling 驱动优化全貌（`_closed_slice` bisect、批量 SQL、kline float 存储、EMA 增量缓存、kline_fetch_ranges）。
- 影响：优化前 ~400s/540bar → 优化后（第二次起）~114s，约 3.5x 提速；文档覆盖根因、commit、实测数据和剩余瓶颈。
- Git：commit `e4b0102`，已 push。

### 02:00:00 +08:00 - 性能优化系列：profiling 驱动的三轮优化
- 类型：代码 / 性能 / 测试 / Git

#### 背景
dynamic universe 回测（1 年窗口，418 symbols，全缓存）约 644 秒。profiling 发现真正的瓶颈分布：
- 网络 I/O（SSL read + TLS + sleep）：~261s（数据未完全缓存时）
- `_closed_slice` 线性扫描：每根 4h bar ~150 次调用 × O(n) 全量扫描
- `_normalise_kline/row`：str→float 逐字段转换，每次 4506k 次调用
- `ema_series`/`atr`：110k 次调用，每次从头算 ~2290 点历史
- `_quote_closes`/`_quote_volumes`：每次 `float()` 转换全量 closes 列表

#### 优化 1：`_closed_slice` bisect（commit `477c2ab`）
- `replay.py` 和 `universe.py` 的 `_closed_slice` 从 O(n) 线性扫描改为 `bisect.bisect_right` 二分查找
- benchmark：10000 次调用 1.38ms/call → 0.014ms/call，加速 **96x**，结果完全一致

#### 优化 2：批量 klines 加载（commit `81965db`）
- 新增 `batch_load_klines_cached`，418 symbols × 3 intervals 用单次 SQL IN 查询而非 1254 次独立连接
- 实测：全缓存时加载阶段节省有限（SQLite IN 查询本身仍需时间）

#### 优化 3：kline 字段存 float/int（commit `2a0be7d`）
- `_normalise_kline` 和 `_normalise_kline_row` 直接存 float/int 而非 str
- 消除 `_quote_closes`、`_quote_volumes`、replay 热路径中的无效 str→float 转换
- 实测节省：~44s（profiling 前后对比：_normalise -14s，_normalise_row -11s，_quote_closes -10s，_quote_volumes -9s）
- 端到端：644s → 543s（混合有网络下载的窗口）

#### 优化 5：kline_fetch_ranges——消除重复 API 请求（commit `84b8c55`）
- 根因：`fetch_klines_cached` 用 `len(cached) < expected` 判断缓存完整性，但 expected 是时间跨度理论值，实际上许多 symbol 有数据空洞（暂停交易等），导致每次跑都触发 200-400 次 Binance API 请求来"补充"数据——即使数据已经抓过了。
- 修复：新增 `kline_fetch_ranges` 表，成功 fetch 后写入 `(symbol, interval, start, end)` 记录；下次检查时如果范围已覆盖，直接跳过 API 调用。
- 实测：同一 6 个月历史窗口（2024-07→2025-01，~540 bars）：Run 1=327s（210 次 fetching） → Run 2=116s（0 次 fetching） → Run 3=114s，加速 **2.9x**，结果完全一致（closed_trades=35，net_return=7.14%）。
- 影响：首次运行仍需下载数据（不变）；重复运行同一时间段大幅加速，walk-forward 多轮重复段直接受益。

#### 全量优化效果总结（纯 CPU 基准，历史稳定窗口）
| 阶段 | 说明 | 时间 |
|---|---|---|
| 优化前（估计） | 含重复 API + 线性扫描 + str→float | ~400s/540bar |
| 优化后（Run 2+） | bisect + float klines + EMA 增量 + fetch_ranges | **114s/540bar** |
| 加速比 | | **~3.5x** |

剩余 114 秒的主要开销（profiling 估算）：
- batch SQL 查询 + fetchall：~30s（SQLite 读 960 万行表）
- ATR 每 bar 从头算：~15s（未优化）
- `list.append`（ema_series 内部）：~12s（部分由 EMA 增量减少）
- `_quote_closes`/`_quote_volumes`：~8s（float 优化后剩余）


- `indicators.py` 新增 `ema_step(prev, value, period)` 单步递推函数
- `_analyze_ticker` 增加 `precomputed_indicators` 可选参数，传入时跳过 `ema_series` 全量计算
- `replay.py` 主循环维护 `_ema_cache[symbol]`，每根 bar 只用 `ema_step` 做增量更新
- 理论节省：~26s（ema_series 110k 次调用 × 2290 点）；实测被网络时间掩盖，需纯缓存窗口验证

#### 验证
- 所有优化：`test_replay`、`test_universe`、`test_trade_state`、`test_abtest` 全部通过
- 数值一致性：net_return_pct=-10.78，max_drawdown_pct=20.70，closed_trades=35 在各轮均相同


- 类型：代码 / 性能 / 测试 / Git
- 改动：`replay.py` 和 `universe.py` 中的 `_closed_slice` 函数从全量线性扫描改为 `bisect.bisect_right` 二分查找。klines 列表按 open_time 升序排列，用 `bisect` 直接定位截止下标，取前缀切片，无需逐元素过滤。
- 原因：性能分析发现 `_closed_slice` 是回测最大瓶颈——每根 4h bar 被调用约 150 次，每次对最多 9000 条 1h klines 做 O(n) 线性扫描并分配新 list。1 年回测约 33 万次调用，累积约 30 亿次元素比较。bisect 将单次调用从 O(n) 降到 O(log n)，benchmark 测得加速比约 96x，行为完全一致。
- 影响：不改变任何策略逻辑和输出结果；所有现有测试通过；实际回测端到端时间预期大幅缩短。
- 验证：`python -m compileall`、`test_replay`、`test_universe`、`test_trade_state` 均通过；benchmark 10000 次调用：旧实现 1.38ms/call → 新实现 0.014ms/call，加速 96x，结果一致。
- Git：`Optimize _closed_slice with bisect binary search`（本条随该提交一起提交并 push）。


- 类型：回测 / A/B / 报告 / 文档 / Git
- 改动：将早期段从 `2025-01-01 -> 2025-06-01` 扩展到 `2024-07-01 -> 2025-06-01`，复用近端 baseline `93b978d7a8c5` 及新生成的近端 variant `d32443a95501`，与 `2026-06-10` 早期段报告一起汇总。
- 改动：生成 `reports/2026-06-11/abtest_dynamic_universe_risk_off_no_core_entry_reclaim_2025-06-01_2026-06-01_v1.md`（近端段复跑）和 `abtest_summary_dynamic_universe_risk_off_no_core_entry_reclaim_2026-06-11_v1.md`。
- 影响：早期段（2024-07-01 → 2025-06-01）：baseline/variant closed_trades=52/41，PF=0.91→1.40，净收益=-5.59%→+11.74%，MDD=18.72%→14.31%，样本充足。近端段（2025-06-01 → 2026-06-01）：baseline/variant closed_trades=49/46，PF=0.73→1.20，净收益=-10.62%→+5.96%，MDD=24.24%→14.46%，样本充足。
- 验证：汇总 `unique_coverage_days=700`，`overlap_periods=0`，`sufficient_periods=2`，verdict=**`candidate_keep_review`**；两段均转正且 PF>1，为首次达到 keep review 门槛。
- Git：`Run entry reclaim combo extended walk-forward`（本条随该提交一起提交并 push）。

### 21:00:00 +08:00 - 增加 TP1 后 EMA20 跟踪止损实验
- 类型：代码 / 配置 / 测试 / 文档 / Git
- 改动：新增 `analysis.tp1_ema_trailing_stop_enabled`，默认 `false`；新增 `tp1_trailing_ema_stop_active` 字段于 `PaperTrade`；`step_trade` 增加 `tp1_trailing_ema_stop: float | None` 参数，TP1 命中后每根 bar 用 4h EMA20 跟踪抬止损（只升不降，不低于入场价）。
- 改动：`replay.py` 两处 `step_trade` 调用处均计算当前 bar 4h EMA20 并传入；`abtest.py` exit_timing 维度扩展；`experiments.toml` 新增 `tp1_ema20_trailing_stop` 实验。
- 改动：新增 4 个 `test_trade_state.py` 测试，1 个 `test_abtest.py` 测试。
- 影响：默认行为不变；后续可运行 `python main.py abtest --experiment tp1_ema20_trailing_stop ...` 做退出质量 A/B。
- 验证：`python -m compileall main.py src tests`、`test_trade_state`、`test_abtest`、`test_replay` 均通过。
- Git：`Add TP1 EMA20 trailing stop experiment`（commit hash `2de9c5f`，已 push）。

### 21:30:00 +08:00 - 增加 SymbolMaster 上市日期过滤
- 类型：代码 / 测试 / 文档 / Git
- 改动：`SymbolMaster` 新增可选字段 `listing_dates: dict[str, str] | None`；`load_symbol_master` 向后兼容旧文件（无 `listing_dates` 字段时为 None）。
- 改动：新增 `fetch_symbol_listing_dates` 函数，批量查询 Binance 各 symbol 最早 1d K 线日期；新增 `listing_date_allows_analysis` 函数，在 dynamic universe 每日过滤中排除历史数据不足的近期上市 symbol。
- 改动：`build_current_symbol_master` 增加 `fetch_listing_dates: bool = False` 开关；`dynamic-symbol-master` CLI 增加 `--fetch-listing-dates` 标志；`replay.py` 在 `for symbol in analysis_symbols:` 循环中增加上市日期过滤层。
- 改动：`test_universe.py` 新增 7 个测试覆盖 round-trip、向后兼容和 `listing_date_allows_analysis` 逻辑。
- 影响：现有 `dynamic_master_full.json`（无 `listing_dates`）加载后过滤层不生效，行为不变；使用 `--fetch-listing-dates` 导出新 master 后可精确排除在早期回测窗口没有足够历史的近期上市 symbol。
- 验证：`python -m compileall main.py src tests`、`test_universe`、`test_replay` 均通过。
- Git：`Add listing_dates to SymbolMaster for early-sample filtering`（commit hash `03700df`，已 push）。

## 2026-06-10

### 04:06:00 +08:00 - tp1_breakeven_stop full master A/B
- 类型：回测 / A/B / 报告 / 文档 / Git
- 改动：复用 baseline run `73cadcfc0a45`，运行 `tp1_breakeven_stop` variant `1d313ac1b8eb`，区间 `2025-01-01 -> 2025-09-01`，使用 `dynamic_master_full.json` 与 `--max-symbols 40 --allow-data-gaps`。
- 改动：生成 TP1 保本止损 A/B 报告、variant dynamic-universe backtest 报告和 regime breakdown；同步更新 `TODO.md`、`开发计划.md` 和 Obsidian 实验日志。
- 原因：验证 TP1 后将止损移动到入场价，是否能减少盈利后回吐并改善退出质量。
- 影响：variant closed_trades=48，样本充足；PF 0.579 -> 0.546，净收益 -13.17% -> -14.90%，最大回撤 19.43% -> 19.43%，stop_rate 80.95% -> 83.33%。分层显示 `RISK_ON` 净 PnL -1123.23 -> -1318.06。
- 验证：A/B 报告给出 `verdict=reject_candidate`，原因是收益更差且最大回撤没有改善；regime breakdown 显示恶化主要来自 `RISK_ON`。
- Git：`Reject TP1 breakeven stop retest`（本条随该提交一起提交并 push）。

### 04:02:00 +08:00 - 增加 TP1 后保本止损实验
- 类型：代码 / 配置 / 测试 / 文档 / Git
- 改动：新增 `analysis.tp1_move_stop_to_breakeven_enabled`，默认 `false` 保持现有行为；新增 `tp1_breakeven_stop` A/B 实验，variant 在 TP1 命中后将止损抬到入场价。
- 改动：扩展 `step_trade` 与回测 replay，把 TP1 后保本止损作为显式开关传入；新增状态机和 A/B override 测试。
- 原因：组合实验显示近端可转正，但早期 `RISK_ON` 仍全止损；下一步需要测试 TP1 后保护性退出，减少盈利后回吐到原始结构止损。
- 影响：默认扫描、模拟盘和回测行为不变；后续可运行 `python main.py abtest --experiment tp1_breakeven_stop ...` 做退出质量 A/B。
- 验证：运行 `python tests\test_trade_state.py`、`python tests\test_abtest.py`、`python tests\test_replay.py` 和 `python -m compileall main.py src tests`，均通过。
- Git：`Add TP1 breakeven stop experiment`（本条随该提交一起提交并 push）。

### 03:45:00 +08:00 - risk_off_no_core_entry_reclaim 近端 walk-forward 与汇总
- 类型：回测 / A/B / 报告 / 文档 / Git
- 改动：复用近端 baseline run `93b978d7a8c5`，运行 `risk_off_no_core_entry_reclaim` variant `d32443a95501`，区间 `2025-06-01 -> 2026-06-01`。
- 改动：生成近端段 A/B 报告、variant dynamic-universe backtest 报告、regime breakdown、含重叠窗口汇总和非重叠 walk-forward 汇总；同步更新项目记忆和 Obsidian 实验日志。
- 原因：组合 full master 与早期段均显示减亏，需要近端段与非重叠汇总判断是否具备 keep 候选资格。
- 影响：近端 variant closed_trades=46，样本充足；PF 0.734 -> 1.204，净收益 -10.62% -> +5.96%，最大回撤 24.24% -> 14.46%。分层显示 `RISK_ON` 净 PnL -458.33 -> +289.35，`RISK_OFF` closed_trades 9 -> 1。
- 验证：非重叠汇总保留 2 段、`overlap_periods=0`、`sufficient_periods=1`，因早期段样本不足仍为 `retest`；不能 keep。
- Git：`Summarize combo entry reclaim walk-forward`（本条随该提交一起提交并 push）。

### 03:13:00 +08:00 - risk_off_no_core_entry_reclaim 早期 walk-forward
- 类型：回测 / A/B / 报告 / 文档 / Git
- 改动：复用早期 baseline run `e6133152fb7e`，运行 `risk_off_no_core_entry_reclaim` variant `c7be05461e78`，区间 `2025-01-01 -> 2025-06-01`。
- 改动：生成早期段 A/B 报告、variant dynamic-universe backtest 报告和 regime breakdown；同步更新 `TODO.md`、`开发计划.md` 和 Obsidian 实验日志。
- 原因：组合 full master 接近打平，但需要非重叠 walk-forward 验证，先补早期段。
- 影响：variant closed_trades=15，仍低于样本线；PF 0.327 -> 0.413，净收益 -11.80% -> -8.17%，最大回撤 14.49% -> 10.85%。分层显示 `RISK_OFF` closed_trades 8 -> 0，但 `RISK_ON` closed_trades 7 -> 9 且仍全部止损。
- 验证：A/B 报告显示 `sample_sufficient=false`、`verdict=retest`；regime breakdown 证实早期改善主要来自去掉 `RISK_OFF` 交易，而不是 `RISK_ON` 转强。
- Git：`Run combo entry reclaim early walk-forward`（本条随该提交一起提交并 push）。

### 03:01:00 +08:00 - risk_off_no_core_entry_reclaim full master A/B
- 类型：回测 / A/B / 报告 / 文档 / Git
- 改动：复用 baseline run `73cadcfc0a45`，运行 `risk_off_no_core_entry_reclaim` variant `400001fc7ad6`，区间 `2025-01-01 -> 2025-09-01`，使用 `dynamic_master_full.json` 与 `--max-symbols 40 --allow-data-gaps`。
- 改动：生成组合实验 A/B 报告、variant dynamic-universe backtest 报告和 regime breakdown；同步更新 `TODO.md`、`开发计划.md` 和 Obsidian 实验日志。
- 原因：`entry_reclaim_close` 近端能改善 `RISK_ON`，但 `RISK_OFF` 仍为负；需要验证弱市停开核心币与入场确认是否互补。
- 影响：variant closed_trades=38，样本充足；PF 0.579 -> 1.025，净收益 -13.17% -> -0.03%，最大回撤 19.43% -> 15.11%。分层显示 `RISK_OFF` closed_trades 10 -> 0，`RISK_ON` 净 PnL -1123.23 -> -320.18。
- 验证：A/B 报告显示 `sample_sufficient=true`、`possible_over_filtering=false`、`verdict=retest`；regime breakdown 显示 `RISK_OFF` 亏损清零，但 `RISK_ON` 仍未转正。
- Git：`Run regime entry reclaim combo retest`（本条随该提交一起提交并 push）。

### 02:42:00 +08:00 - 增加 risk_off_no_core_entry_reclaim 组合实验
- 类型：代码 / 配置 / 测试 / 文档 / Git
- 改动：新增 `risk_off_no_core_entry_reclaim` A/B 实验，同时覆盖 `analysis.risk_off_core_buy_enabled=false` 与 `analysis.entry_reclaim_close_enabled=true`。
- 改动：为 A/B override 白名单增加 `combined_regime_entry` dimension，并补充测试验证组合 override 不会污染 baseline。
- 原因：`entry_reclaim_close` 近端能让 `RISK_ON` 转正，但早期样本不足且 `RISK_OFF` 仍有亏损；需要验证它和弱市停开核心币是否互补。
- 影响：默认配置不变；后续可运行 `python main.py abtest --experiment risk_off_no_core_entry_reclaim --dynamic-universe ...` 做 full master A/B。
- 验证：运行 `python tests\test_abtest.py` 和 `python -m compileall main.py src tests`，均通过。
- Git：`Add regime entry reclaim combo experiment`（本条随该提交一起提交并 push）。

### 02:38:00 +08:00 - entry_reclaim_close 早期段与 walk-forward 汇总
- 类型：回测 / A/B / 报告 / 文档 / Git
- 改动：补齐 `entry_reclaim_close` full master 非重叠 walk-forward 早期段，复用 baseline run `e6133152fb7e` 并对比 variant run `a049fb3cf4d3`，区间 `2025-01-01 -> 2025-06-01`。
- 改动：生成早期段 A/B 报告、regime breakdown、含重叠窗口汇总和非重叠 walk-forward 汇总；同步更新 `TODO.md`、`开发计划.md` 和 Obsidian 实验日志。
- 原因：近端段已经转正，但要判断 `entry_reclaim_close` 是否能进入组合验证，必须补齐早期非重叠段并做汇总。
- 影响：早期 variant closed_trades=18，仍低于样本线；PF 0.327 -> 0.305，净收益 -11.80% -> -11.36%，最大回撤 14.49% -> 13.50%。非重叠汇总保留 2 段、`overlap_periods=0`、`sufficient_periods=1`，结论仍为 `retest`。
- 验证：`abtest_dynamic_universe_entry_reclaim_close_2025-01-01_2025-06-01_v1.md`、`backtest_regime_breakdown_e6133152fb7e_a049fb3cf4d3_v1.md`、`abtest_summary_dynamic_universe_entry_reclaim_close_2026-06-10_v2.md` 和 `abtest_summary_dynamic_universe_entry_reclaim_close_2026-06-10_v3.md` 均已生成；非重叠汇总原因是 variant 有一个时段低于闭合交易样本线。
- Git：`Summarize entry reclaim walk-forward`（本条随该提交一起提交并 push）。

### 02:23:23 +08:00 - entry_reclaim_close 近端非重叠段复测
- 类型：回测 / A/B / 报告 / 文档 / Git
- 改动：复用近端 baseline run `93b978d7a8c5`，单独运行 `entry_reclaim_close` variant `9770a33e7f77`，区间 `2025-06-01 -> 2026-06-01`，并生成标准 A/B 报告与 regime breakdown。
- 改动：生成 `abtest_dynamic_universe_entry_reclaim_close_2025-06-01_2026-06-01_v1.md`、`backtest_dynamic_universe_2025-06-01_2026-06-01_v1.md`、`backtest_dynamic_universe_2025-06-01_2026-06-01_v2.md` 和 `backtest_regime_breakdown_93b978d7a8c5_9770a33e7f77_v1.md`。
- 原因：full master extended 窗口显示 `entry_reclaim_close` 对 `RISK_ON` 有明显改善，需要用近端非重叠窗口确认效果是否延续。
- 影响：近端 variant 样本充足且转正，PF 0.734 -> 1.142，净收益 -10.62% -> +5.34%，最大回撤 24.24% -> 15.90%；分层显示 `RISK_ON` 净 PnL -458.33 -> +627.20，`RISK_OFF` 仍为负且略恶化。
- 验证：A/B 报告显示 `sample_sufficient=true`、`possible_over_filtering=false`、`verdict=retest`；regime breakdown 显示 `RISK_ON` PF 0.84 -> 1.23、stop_rate 75.00% -> 66.67%。
- Git：`Run entry reclaim close near walk-forward`（本条随该提交一起提交并 push）。

### 00:49:00 +08:00 - entry_reclaim_close full master A/B
- 类型：回测 / A/B / 报告 / 文档 / Git
- 改动：运行 `entry_reclaim_close` full master dynamic-universe A/B，区间 `2025-01-01 -> 2025-09-01`，使用 `reports/2026-06-09/dynamic_master_full.json` 与 `--max-symbols 40 --allow-data-gaps --no-obsidian`。
- 改动：生成 `reports/2026-06-10/abtest_dynamic_universe_entry_reclaim_close_2025-01-01_2025-09-01_v1.md`、`backtest_dynamic_universe_2025-01-01_2025-09-01_v1.md`、`backtest_dynamic_universe_2025-01-01_2025-09-01_v2.md` 和 `backtest_regime_breakdown_73cadcfc0a45_d088ff687ea1_v1.md`。
- 原因：`risk_off_no_core_top_n_3` 汇总显示下一步应优先优化 `RISK_ON` 入场/退出质量；本轮先测试 4h 收盘重新站上 `entry_high` 的入场确认。
- 影响：variant 样本充足，PF 0.579 -> 0.905，净收益 -13.17% -> -3.50%，最大回撤 19.43% -> 17.63%；`RISK_ON` 净 PnL 从 -1123.23 改善到 -121.79，但整体仍为负收益，结论 `retest`。
- 验证：A/B 报告显示 `sample_sufficient=true`、`possible_over_filtering=false`、`verdict=retest`；regime breakdown 显示 `RISK_ON` PF 0.51 -> 0.94、stop_rate 82.76% -> 72.41%。
- Git：`Run entry reclaim close full-master retest`（本条随该提交一起提交并 push）。

## 2026-06-09

### 23:59:08 +08:00 - 增加 entry_reclaim_close 入场确认实验
- 类型：代码 / 配置 / 测试 / 计划 / Git
- 改动：新增 `analysis.entry_reclaim_close_enabled`，默认 `false` 保持现有行为；当开启时，回测中的 WATCHING 计划只有在入场区触碰后 4h 收盘重新站上 `entry_high` 才允许入场。
- 改动：新增 `entry_reclaim_close` A/B 实验，dimension 为 `entry_timing`，variant 将 `analysis.entry_reclaim_close_enabled` 设为 `true`；扩展 A/B override 白名单。
- 原因：`risk_off_no_core_top_n_3` 已能减少 `RISK_OFF` 亏损，但近端和早期 `RISK_ON` 仍容易止损；下一步需要验证延迟入场/重新确认是否能减少接飞刀。
- 影响：默认扫描、模拟盘和回测行为不变；后续可运行 `python main.py abtest --experiment entry_reclaim_close --dynamic-universe ...` 做 full master A/B。
- 验证：运行 `python tests\test_abtest.py`、`python tests\test_replay.py` 和 `python -m compileall main.py src tests`，均通过。
- Git：`Add entry reclaim close experiment`（本条随该提交一起提交并 push）。

### 23:54:45 +08:00 - 增加非重叠 A/B 汇总过滤
- 类型：代码 / 测试 / 报告 / 文档 / Git
- 改动：为 `abtest-summary` 增加 `--drop-overlap-periods`，汇总前按结束日期优先保留最大数量的非重叠 A/B 窗口，避免 extended 诊断窗口和 walk-forward 子窗口混在一起。
- 改动：新增 `select_non_overlapping_records` 并补充单元测试，验证 `2025-01-01 -> 2025-09-01` 这类重叠 extended 窗口会被排除，保留 `2025-01-01 -> 2025-06-01` 与 `2025-06-01 -> 2026-06-01`。
- 改动：生成 `abtest_summary_dynamic_universe_risk_off_no_core_top_n_3_2026-06-09_v1.md` 全证据汇总和 `v2.md` 非重叠 walk-forward 汇总。
- 原因：组合实验已有 extended 窗口和两个非重叠子窗口；若直接汇总全部报告，结论会被重叠窗口原因主导，不利于区分诊断证据和 walk-forward 证据。
- 影响：`v2` 汇总显示 periods=2、unique_coverage_days=516、overlap_periods=0、sufficient_periods=1，结论仍为 `retest`，原因变为早期 variant 样本不足。
- 验证：运行 `python tests\test_abtest_summary.py` 和 `python -m compileall main.py src tests`，均通过；运行 `python main.py abtest-summary --experiment risk_off_no_core_top_n_3 --mode dynamic_universe --reports-date 2026-06-09 --drop-overlap-periods --no-obsidian` 成功生成 v2 汇总。
- Git：`Add non-overlap abtest summary filter`（本条随该提交一起提交并 push）。

### 23:48:55 +08:00 - risk_off_no_core_top_n_3 近端非重叠段复测
- 类型：回测 / A/B / 报告 / 文档 / Git
- 改动：使用 `reports/2026-06-09/dynamic_master_full.json` 单独运行 `risk_off_no_core_top_n_3` 近端窗口 variant，区间 `2025-06-01 -> 2026-06-01`，并复用 baseline run `359a6c461f6c` 生成 A/B 报告。
- 改动：生成 `backtest_dynamic_universe_2025-06-01_2026-06-01_v12.md`、`abtest_dynamic_universe_risk_off_no_core_top_n_3_2025-06-01_2026-06-01_v1.md` 和 `backtest_regime_breakdown_359a6c461f6c_1f9a0a132e6f_v1.md`。
- 原因：组合实验在 full master extended 窗口转正，早期非重叠段方向改善但样本不足；需要补完近端非重叠段，判断改善是否跨窗口延续。
- 影响：近端段 variant 样本充足，PF 0.734 -> 0.876，净收益 -10.62% -> -5.36%，最大回撤 24.24% -> 21.38%，暴露 88.45% -> 63.01%；但策略仍为负收益，结论继续 `retest`，不能 keep。
- 验证：A/B 报告显示 `sample_sufficient=true`、`possible_over_filtering=false`、`verdict=retest`；regime breakdown 显示 `RISK_OFF` closed_trades 9 -> 1、净 PnL -541.46 -> -106.97，`RISK_ON` PF 0.84 -> 0.86。
- Git：`Run combined regime capacity near walk-forward`（本条随该提交一起提交并 push）。

### 21:26:58 +08:00 - risk_off_no_core_top_n_3 早期非重叠段复测
- 类型：回测 / A/B / 报告 / 文档 / Git
- 改动：使用 `reports/2026-06-09/dynamic_master_full.json` 单独运行 `risk_off_no_core_top_n_3` 早期窗口 variant，区间 `2025-01-01 -> 2025-06-01`，并复用 baseline run `e6133152fb7e` 生成 A/B 报告。
- 改动：生成 `backtest_dynamic_universe_2025-01-01_2025-06-01_v9.md`、`abtest_dynamic_universe_risk_off_no_core_top_n_3_2025-01-01_2025-06-01_v1.md` 和 `backtest_regime_breakdown_e6133152fb7e_2ec5278f62cb_v1.md`。
- 原因：组合实验在 extended 窗口首度转正后，需要用非重叠 walk-forward 检查是否稳定。
- 影响：variant closed_trades=13，低于样本线；PF 0.327 -> 0.488，净收益 -11.80% -> -8.03%，最大回撤 14.49% -> 11.46%。`RISK_OFF` 闭合交易从 8 降到 0，但 `RISK_ON` 仍 7/7 全部止损。结论仍为 `retest`。
- 验证：A/B 报告显示 `sample_sufficient=false`、`possible_over_filtering=false`、`verdict=retest`；regime breakdown 显示 `RISK_OFF baseline_closed=8 variant_closed=0`。
- Git：`Run combined regime capacity early walk-forward`（本条随该提交一起提交并 push）。

### 21:06:32 +08:00 - risk_off_no_core_top_n_3 full master A/B
- 类型：回测 / A/B / 报告 / 文档 / Git
- 改动：使用 `reports/2026-06-09/dynamic_master_full.json` 单独运行 `risk_off_no_core_top_n_3` variant，并复用 baseline run `1d0037a773ff` 生成标准 A/B 报告。
- 改动：生成 `backtest_dynamic_universe_2025-01-01_2025-09-01_v12.md`、`abtest_dynamic_universe_risk_off_no_core_top_n_3_2025-01-01_2025-09-01_v1.md` 和 `backtest_regime_breakdown_1d0037a773ff_8068142bf3c8_v1.md`。
- 原因：`risk_off_no_core_buy` 主要改善 `RISK_OFF`，`top_n_3` 主要改善 `RISK_ON`，需要验证两条互补规则叠加后能否接近转正。
- 影响：variant 将 PF 从 0.579 提升到 1.0005，净收益从 -13.17% 改善到 +1.04%，最大回撤从 19.43% 降到 15.96%；分层显示 `RISK_OFF` 亏损归零，`RISK_ON` 净 PnL 从 -1123.23 改善到 -387.41。结论为 promising `retest`，不能 keep，下一步必须做非重叠 walk-forward。
- 验证：A/B 报告显示 `sample_sufficient=true`、`possible_over_filtering=false`、`verdict=retest`；regime breakdown 显示 `RISK_OFF baseline_closed=10 variant_closed=0`、`RISK_ON baseline_closed=29 variant_closed=28`。
- Git：`Run combined regime capacity full-master retest`（本条随该提交一起提交并 push）。

### 20:39:11 +08:00 - 增加 risk_off_no_core_top_n_3 组合实验
- 类型：代码 / 配置 / 测试 / 计划 / Git
- 改动：新增 `risk_off_no_core_top_n_3` A/B 实验，同时设置 `analysis.risk_off_core_buy_enabled=false` 与 `market.top_n=3`；扩展 `combined_regime_capacity` 覆盖白名单。
- 原因：`risk_off_no_core_buy` 主要改善 `RISK_OFF`，`top_n_3` 主要改善 `RISK_ON`，两者在分层结果中互补，需要验证组合后是否能接近转正。
- 影响：下一步可复用 full master baseline `1d0037a773ff` 单独运行组合 variant，并生成 A/B 与 regime breakdown 报告；默认配置不改变。
- 验证：运行 `python tests\test_abtest.py`、`python -m compileall main.py src tests`，均通过。
- Git：`Add combined regime capacity experiment`（本条随该提交一起提交并 push）。

### 20:36:39 +08:00 - top_n_3 full master A/B
- 类型：回测 / A/B / 报告 / 文档 / Git
- 改动：使用 `reports/2026-06-09/dynamic_master_full.json` 单独运行 `top_n_3` variant，并复用 baseline run `1d0037a773ff` 生成标准 A/B 报告。
- 改动：生成 `backtest_dynamic_universe_2025-01-01_2025-09-01_v11.md`、`abtest_dynamic_universe_top_n_3_2025-01-01_2025-09-01_v1.md` 和 `backtest_regime_breakdown_1d0037a773ff_c9f68192026d_v1.md`。
- 原因：`RISK_ON` 亏损按日期聚集，怀疑每次扫描候选容量过高导致同日相关拥挤开仓。
- 影响：variant 将 PF 从 0.579 提升到 0.837，净收益从 -13.17% 改善到 -3.63%；分层显示 `RISK_ON` 净 PnL 从 -1123.23 改善到 -212.97，但 `RISK_OFF` 完全不变，最大回撤也未改善。因此结论仍为 `retest`，下一步应测试 `risk_off_no_core_buy + top_n_3` 组合。
- 验证：A/B 报告显示 `sample_sufficient=true`、`possible_over_filtering=false`、`verdict=retest`；regime breakdown 显示 `RISK_ON baseline_closed=29 variant_closed=26`。
- Git：`Run top-n capacity full-master retest`（本条随该提交一起提交并 push）。

### 20:09:21 +08:00 - 增加 top_n_3 容量实验
- 类型：代码 / 配置 / 测试 / 计划 / Git
- 改动：新增 `top_n_3` A/B 实验，variant 将 `market.top_n` 从 5 降到 3；扩展 `capacity` 维度的配置覆盖白名单。
- 原因：`RISK_ON` 亏损按日期聚集明显，例如 2025-05-11、2025-01-04、2025-07-22 等同日多笔相关交易同时止损，score 阈值本身无法区分赢家和输家。
- 影响：下一步可以单独验证降低每次扫描候选容量是否能减少拥挤开仓和 `RISK_ON` 止损簇；默认配置不改变。
- 验证：运行 `python tests\test_abtest.py`、`python -m compileall main.py src tests`，均通过。
- Git：`Add top-n capacity experiment`（本条随该提交一起提交并 push）。

### 20:05:30 +08:00 - risk_off_no_core_buy full master A/B
- 类型：回测 / A/B / 报告 / 文档 / Git
- 改动：使用 `reports/2026-06-09/dynamic_master_full.json` 跑 `risk_off_no_core_buy` full master A/B，区间为 `2025-01-01 -> 2025-09-01`，参数为 `--max-symbols 40 --allow-data-gaps --no-obsidian`。
- 改动：完整 A/B 命令首次在 30 分钟超时前写出 baseline 报告 `backtest_dynamic_universe_2025-01-01_2025-09-01_v9.md`；随后复用 SQLite 中的 baseline run `1d0037a773ff`，单独运行 variant `b4ef9a870efb` 并生成 `abtest_dynamic_universe_risk_off_no_core_buy_2025-01-01_2025-09-01_v1.md`。
- 改动：生成 `backtest_regime_breakdown_1d0037a773ff_b4ef9a870efb_v1.md`，确认 variant 的 `RISK_OFF` 闭合交易从 10 降到 0。
- 原因：上一轮分层显示 `RISK_OFF` 亏损几乎全部来自 BTC/ETH 核心币豁免，需要验证弱市是否应完全暂停新开仓。
- 影响：variant 将 PF 从 0.579 提升到 0.707，净收益从 -13.17% 改善到 -7.96%，最大回撤从 19.43% 降到 15.03%；但 `RISK_ON` 净 PnL 从 -1123.23 恶化到 -1243.74，因此结论仍为 `retest`，不能 keep。
- 验证：A/B 报告显示 `sample_sufficient=true`、`possible_over_filtering=false`、`verdict=retest`；regime breakdown 显示 `RISK_OFF baseline_closed=10 variant_closed=0`。
- Git：`Run risk-off core buy full-master retest`（本条随该提交一起提交并 push）。

### 19:07:43 +08:00 - 增加 RISK_OFF 核心币暂停买入实验
- 类型：代码 / 配置 / 测试 / 计划 / Git
- 改动：新增 `[analysis].risk_off_core_buy_enabled` 配置，默认 `true` 保持旧行为；新增 `risk_off_no_core_buy` A/B 实验，variant 将该开关设为 `false`。
- 改动：扫描器和回测重放在传入 `market_regime_status="RISK_OFF"` 时，可按该开关取消 BTC/ETH 核心币买入豁免，将候选降级为 `WATCH_ONLY`。
- 原因：regime breakdown 显示 `RISK_OFF` 亏损几乎全部来自 BTC/ETH，当前只降级山寨币不足以防守弱市。
- 影响：下一步可以用 full master A/B 单独验证“弱市完全暂停新开仓”是否减少亏损；默认配置不改变现有行为。
- 验证：运行 `python tests\test_scanner_regime.py`、`python tests\test_abtest.py`、`python tests\test_replay.py`、`python -m compileall main.py src tests`，均通过。
- Git：`Add risk-off core buy experiment`（本条随该提交一起提交并 push）。

### 19:00:38 +08:00 - 增加回测市场环境分层报告
- 类型：代码 / 报告 / 测试 / 文档 / Git
- 改动：新增 `src/crypto_trading_system/backtest/regime_analysis.py` 和 `python main.py backtest-regime-breakdown --baseline-run-id ... --variant-run-id ...`，按交易创建日的 BTC/ETH 日线 regime 对真实入场且已闭合的回测交易分组。
- 改动：生成 `reports/2026-06-09/backtest_regime_breakdown_1c1bd1b7b9ad_4dae110c062c_v1.md`，对 full master extended 的 baseline/variant 做 `RISK_ON`、`RISK_OFF`、`NEUTRAL` 分层。
- 原因：`liquidity_50m` 在 full master 下持续减亏但不能转正，需要定位亏损主要来自哪类市场环境，避免继续盲目提高流动性门槛。
- 影响：`RISK_ON` 与 `RISK_OFF` 是主要亏损来源；variant 在两者中均减亏，但仍为负，说明下一步应做 regime-aware 入场/退出规则，而不是直接 keep `liquidity_50m`。
- 验证：运行 `python tests\test_regime_analysis.py`、`python tests\test_abtest_summary.py`、`python -m compileall main.py src tests`，并用 `backtest-regime-breakdown` 生成报告；修正过一次口径，确保只统计 `entered_at_utc IS NOT NULL` 且 `closed_at_utc IS NOT NULL` 的真实闭合交易。
- Git：`Add backtest regime breakdown report`（本条随该提交一起提交并 push）。

### 18:52:14 +08:00 - Full master liquidity_50m 延长早期窗口 A/B
- 类型：回测 / A/B / 报告 / 文档 / Git
- 改动：使用 `reports/2026-06-09/dynamic_master_full.json` 运行 `liquidity_50m` 延长早期窗口 dynamic-universe A/B，区间为 `2025-01-01 -> 2025-09-01`，参数为 `--max-symbols 40 --allow-data-gaps --no-obsidian`。
- 改动：生成 `reports/2026-06-09/abtest_dynamic_universe_liquidity_50m_2025-01-01_2025-09-01_v2.md` 及底层 `backtest_dynamic_universe_2025-01-01_2025-09-01_v7.md`、`v8.md`。
- 原因：早期短窗口 `2025-01-01 -> 2025-06-01` 在 full master 下仍只有 17/17 笔闭合交易，需要延长窗口确认样本不足是否只是时间长度问题。
- 影响：baseline/variant trades=271/242，closed_trades=42/41，PF=0.579/0.693，净收益=-13.17%/-9.60%，最大回撤=19.43%/18.81%，样本充足且改善延续，但策略仍为负收益，结论继续 `retest`。
- 验证：A/B 命令完成并输出 `sample_sufficient=true`、`possible_over_filtering=false`、`verdict=retest`；抽取报告 Raw Metrics 确认指标。
- Git：`Run full-master extended liquidity retest`（本条随该提交一起提交并 push）。

### 18:10:11 +08:00 - Full master liquidity_50m 早期窗口 A/B
- 类型：回测 / A/B / 报告 / 文档 / Git
- 改动：使用 `reports/2026-06-09/dynamic_master_full.json` 运行 `liquidity_50m` 早期窗口 dynamic-universe A/B，区间为 `2025-01-01 -> 2025-06-01`，参数为 `--max-symbols 40 --allow-data-gaps --no-obsidian`。
- 改动：生成 `reports/2026-06-09/abtest_dynamic_universe_liquidity_50m_2025-01-01_2025-06-01_v3.md` 及底层 `backtest_dynamic_universe_2025-01-01_2025-06-01_v7.md`、`v8.md`。
- 原因：补齐 full master 非重叠验证的早期窗口，确认 `liquidity_50m` 在 `source_limit=None` 时早期样本是否过线。
- 影响：baseline/variant trades=91/88，closed_trades=17/17，PF=0.327/0.327，净收益=-11.80%/-10.31%，最大回撤=14.49%/13.47%；variant 仍低于 20 笔闭合交易，full master 非重叠整体继续 `retest`。
- 验证：A/B 命令完成并输出 `sample_sufficient=false`、`verdict=retest`；抽取报告 Raw Metrics 确认早期窗口指标。
- Git：`Run full-master early liquidity retest`（本条随该提交一起提交并 push）。

### 17:12:29 +08:00 - Full master liquidity_50m 近端 A/B
- 类型：回测 / A/B / 报告 / 文档 / Git
- 改动：使用不截断的 `reports/2026-06-09/dynamic_master_full.json` 运行 `liquidity_50m` dynamic-universe A/B，窗口为 `2025-06-01 -> 2026-06-01`，参数为 `--max-symbols 40 --allow-data-gaps --no-obsidian`。
- 改动：生成 `reports/2026-06-09/abtest_dynamic_universe_liquidity_50m_2025-06-01_2026-06-01_v5.md` 及底层 `backtest_dynamic_universe_2025-06-01_2026-06-01_v10.md`、`v11.md`。
- 原因：验证 `liquidity_50m` 的近端改善是否仍能在无 `source_limit` 截断、418 个 symbol 的 full master 下延续。
- 影响：baseline/variant trades=302/240，closed_trades=49/51，PF=0.734/0.852，净收益=-10.62%/-6.11%，最大回撤=24.24%/21.32%，样本充足但整体仍为负收益，结论继续 `retest`，不能 keep。
- 验证：A/B 命令完成并输出 `sample_sufficient=true`、`possible_over_filtering=false`、`verdict=retest`；抽取报告 Raw Metrics 确认指标。
- Git：`Run full-master liquidity retest`（本条随该提交一起提交并 push）。

### 15:09:31 +08:00 - 导出 full dynamic symbol master
- 类型：报告 / 文档 / Git
- 改动：运行 `python main.py dynamic-symbol-master --output reports\2026-06-09\dynamic_master_full.json`，导出不使用 `--source-limit` 的 full dynamic `SymbolMaster`。
- 原因：为下一轮 `liquidity_50m` full master A/B 准备固定 universe，降低 source-limit 截断样本对实验判断的干扰。
- 影响：生成 `reports/2026-06-09/dynamic_master_full.json`，当前包含 418 个 Binance 现货 USDT symbols；本节点只固化 universe，不产生 A/B keep/retest 结论。
- 验证：命令成功输出 `symbols=418`、`source_limit=None`、`source_limit_applied=false`；抽查 JSON 文件头部确认 `created_at_utc=2026-06-09T07:07:56+00:00` 且 symbols 已写入。
- Git：`Export full dynamic universe symbol master`（本条随该提交一起提交并 push）。

### 15:03:41 +08:00 - 固定 master 的 liquidity_50m 非重叠 walk-forward
- 类型：回测 / A/B / 报告 / 文档 / Git
- 改动：使用 `reports/2026-06-09/dynamic_master_source150.json` 作为固定 `SymbolMaster`，运行 `liquidity_50m` 非重叠 walk-forward：`2025-01-01 -> 2025-06-01` 与 `2025-06-01 -> 2026-06-01`，参数为 `--max-symbols 40 --allow-data-gaps --no-obsidian`。
- 改动：生成 `abtest_dynamic_universe_liquidity_50m_2025-01-01_2025-06-01_v2.md`、`abtest_dynamic_universe_liquidity_50m_2025-06-01_2026-06-01_v4.md`、`abtest_summary_dynamic_universe_liquidity_50m_2026-06-09_v7.md` 及对应底层 backtest 报告。
- 原因：验证 `liquidity_50m` 在固定 master 文件下是否仍延续改善，降低当前 `exchangeInfo` 快照漂移对实验结论的影响。
- 影响：早期段 baseline/variant closed_trades=19/16，样本仍不足但 variant 改善 PF、净收益和回撤；近端段 baseline/variant closed_trades=55/56，样本充足且 PF 0.697 -> 0.753、净收益 -13.04% -> -10.31%、最大回撤 26.71% -> 24.92%。汇总 v7 显示 `unique_coverage_days=516`、`overlap_periods=0`，但因一个 variant period 样本不足和 `source_limit` 风险继续 `retest`。
- 验证：`abtest-walk-forward` 命令成功完成；抽取 Raw Metrics 确认两段指标和 v7 汇总结论。
- Git：`Run fixed-master liquidity walk-forward retest`（本条随该提交一起提交并 push）。

### 14:20:26 +08:00 - 增加 dynamic symbol master 导出命令
- 类型：代码 / 报告 / 测试 / 文档 / Git
- 改动：新增 `python main.py dynamic-symbol-master --output ... [--source-limit N]`，可只导出 dynamic universe `SymbolMaster` JSON，不触发长回测或 A/B。
- 改动：用新命令导出 `reports/2026-06-09/dynamic_master_source150.json`，固定当前 `source-limit=150` 的 150 个 symbols，供后续 `--symbol-master-file` 复跑使用。
- 原因：上一节点已支持保存/加载 master，但只能绑在长回测/A/B 命令上；单独导出命令更符合固定数据集后再实验的回测纪律，也方便后续复现实验 universe。
- 影响：后续可以先导出 master，再对 `liquidity_50m` 做非重叠 walk-forward 或更大 universe 复测，避免每次都重新依赖当前 `exchangeInfo`。
- 验证：运行 `python main.py dynamic-symbol-master --help`、`python -m compileall main.py src tests`、`python tests\test_universe.py` 均通过；实际运行 `python main.py dynamic-symbol-master --source-limit 150 --output reports\2026-06-09\dynamic_master_source150.json` 成功输出 150 个 symbols。
- Git：`Add dynamic symbol master export command`（本条随该提交一起提交并 push）。

### 14:16:17 +08:00 - Dynamic universe 支持固定 symbol master
- 类型：代码 / 测试 / 文档 / Git
- 改动：新增 `save_symbol_master` 和 `load_symbol_master`，支持把 dynamic universe 的 `SymbolMaster` 保存为 JSON，并在后续回测中复用。
- 改动：`backtest-dynamic-universe`、`abtest` 和 `abtest-walk-forward` 新增 `--symbol-master-file` 与 `--write-symbol-master`；`--symbol-master-file` 与 `--source-limit` 互斥，避免同时声明两套 master 来源。
- 改动：`run_abtest` 支持传入预构建 `dynamic_symbol_master`，A/B baseline 和 variant 继续共享同一份 master；walk-forward 也可在多个 period 间复用同一份 master。
- 原因：参考开源量化回测项目的固定数据集/固定 pair universe 纪律，减少每次运行依赖当前 Binance `exchangeInfo` 快照带来的漂移，让后续 `liquidity_50m` 扩大 universe 复测更可复现。
- 影响：后续可以先用 `--write-symbol-master reports/.../dynamic_master.json` 固化 master，再用 `--symbol-master-file` 对不同实验或不同时间段复跑，确保只改变实验参数或日期窗口。
- 验证：运行 `python tests\test_universe.py`、`python tests\test_abtest.py`、`python -m compileall main.py src tests` 均通过；`python main.py abtest --help` 与 `python main.py backtest-dynamic-universe --help` 均显示新参数；非 dynamic A/B 误传 `--symbol-master-file` 会报错。
- Git：`Add reusable dynamic universe symbol masters`（本条随该提交一起提交并 push）。

### 14:07:33 +08:00 - Dynamic Universe liquidity_50m 扩大 universe 复测
- 类型：回测 / A/B / 报告 / 文档 / Git
- 改动：运行 `liquidity_50m` dynamic universe A/B，区间为 `2025-06-01 -> 2026-06-01`，参数扩大到 `--source-limit 150 --max-symbols 40 --allow-data-gaps --no-obsidian`。
- 改动：第一次运行在 30 分钟超时前生成 baseline 报告 `reports/2026-06-09/backtest_dynamic_universe_2025-06-01_2026-06-01_v5.md`；缓存变热后第二次完整生成 `backtest_dynamic_universe_2025-06-01_2026-06-01_v6.md`、`backtest_dynamic_universe_2025-06-01_2026-06-01_v7.md`、`abtest_dynamic_universe_liquidity_50m_2025-06-01_2026-06-01_v3.md` 和 `abtest_summary_dynamic_universe_liquidity_50m_2026-06-09_v6.md`。
- 原因：上一轮 `source-limit 100 / max-symbols 30` 的 `liquidity_50m` 改善仍可能依赖当前快照 master 的前 100 个 symbols；需要用更大的 dynamic universe 检查方向是否延续。
- 影响：扩大到 150/40 后，baseline closed_trades=55、variant closed_trades=56，样本充足；variant 将 PF 从 0.697 提升到 0.753，净收益从 -13.04% 改善到 -10.31%，最大回撤从 26.71% 降到 24.92%。方向仍改善，但总汇总 v6 因 period 重叠和 `source_limit` 风险继续保持 `retest`。
- 验证：A/B 命令第二次成功完成；`abtest-summary` v6 成功生成，显示 periods=6、sufficient_periods=4、unique_coverage_days=516、overlap_periods=5、verdict=`retest`。
- Git：`Run larger liquidity universe retest`（本条随该提交一起提交并 push）。

### 13:07:37 +08:00 - A/B 汇总增加 dynamic universe 偏差提示
- 类型：代码 / 报告 / 测试 / 文档 / Git
- 改动：扩展 `src/crypto_trading_system/abtest_summary.py`，从单段 A/B 报告的 Dynamic Universe Metadata 中提取 master count、`source_limit` 和 universe refreshes，并在汇总报告中输出 `Universe Bias Checks`。
- 改动：更新 `tests/test_abtest_summary.py`，覆盖 dynamic metadata 解析、`universe_warnings` 汇总和 Markdown / Raw Summary 输出。
- 改动：重新生成 `reports/2026-06-09/abtest_summary_dynamic_universe_liquidity_50m_2026-06-09_v5.md`，报告显示 `universe_warnings=2`，包括当前 Binance `exchangeInfo` master 依赖和 5/5 periods 使用 `source_limit`。
- 原因：参考 Freqtrade、VectorBT、Backtrader 等开源项目的回测纪律后，当前最需要补强的是让 dynamic universe 回测报告显式暴露幸存者偏差、当前快照 master 和调试截断风险，而不是只看 PF/净收益。
- 影响：以后 A/B 汇总不会只给指标结论，还会提醒在进入 keep review 前先扩大或取消 `source_limit`，并研究历史/退市 symbol master。
- 验证：运行 `python tests\test_abtest_summary.py`、`python tests\test_abtest_walk_forward.py`、`python -m compileall main.py src tests` 均通过；运行 `python main.py abtest-summary --experiment liquidity_50m --mode dynamic_universe --reports-date 2026-06-09 --no-obsidian` 成功生成 v5。
- Git：`Add dynamic universe bias warnings to abtest summary`（本条随该提交一起提交并 push）。

### 13:00:10 +08:00 - Dynamic Universe liquidity_50m 非重叠 walk-forward 验证
- 类型：回测 / A/B / 报告 / 文档 / Git
- 改动：运行 `liquidity_50m` dynamic universe 非重叠 walk-forward A/B，区间为 `2025-01-01 -> 2025-06-01` 与 `2025-06-01 -> 2026-06-01`，参数为 `--source-limit 100 --max-symbols 30 --allow-data-gaps --no-obsidian`。
- 改动：生成 `reports/2026-06-09/abtest_dynamic_universe_liquidity_50m_2025-01-01_2025-06-01_v1.md`、`reports/2026-06-09/abtest_dynamic_universe_liquidity_50m_2025-06-01_2026-06-01_v2.md` 和 `reports/2026-06-09/abtest_summary_dynamic_universe_liquidity_50m_2026-06-09_v4.md`，并同步更新 TODO、开发计划和 Obsidian 实验日志。
- 原因：上一轮 `liquidity_50m` 的多窗口证据存在重叠，不能当作独立 walk-forward 证据；需要用非重叠窗口确认改善是否稳定。
- 影响：非重叠覆盖为 `unique_coverage_days=516`、`overlap_periods=0`，但只有 1 个 period 样本充足；早期窗口 variant closed_trades=12，低于 `closed_trades >= 20` 样本线，因此自动结论仍为 `retest`。
- 验证：A/B walk-forward 命令成功完成；抽取 Raw Metrics 确认 `2025-01-01 -> 2025-06-01` 为 baseline PF=0.198 / net=-10.37% / MDD=12.67%，variant PF=0.232 / net=-8.51% / MDD=10.33%，但样本不足；`2025-06-01 -> 2026-06-01` 为 baseline PF=0.718 / net=-8.77% / MDD=19.70%，variant PF=0.810 / net=-5.53% / MDD=18.76%，样本充足且方向改善。
- Git：`Run non-overlap liquidity walk-forward retest`（本条随该提交一起提交并 push）。

### 12:31:40 +08:00 - A/B 汇总增加时段重叠分析
- 类型：代码 / 报告 / 测试 / 文档 / Git
- 改动：扩展 `src/crypto_trading_system/abtest_summary.py`，在多时段汇总中计算 `total_period_days`、`unique_coverage_days` 和 `overlap_periods`。
- 改动：当 A/B 汇总时段存在重叠时，自动结论保持 `retest`，避免把重叠窗口误判为完全独立证据。
- 改动：更新 `tests/test_abtest_summary.py`，覆盖非重叠窗口的候选 keep 逻辑和重叠窗口保持 `retest` 的规则。
- 改动：重新生成 `reports/2026-06-09/abtest_summary_dynamic_universe_liquidity_50m_2026-06-09_v3.md`，显示 `total_period_days=881`、`unique_coverage_days=516`、`overlap_periods=2`。
- 原因：`liquidity_50m` 当前多个验证窗口存在明显重叠，直接按 periods 数量计数会高估证据独立性。
- 影响：多时段汇总更接近专业 walk-forward 纪律；`liquidity_50m` 仍是优先验证对象，但在存在重叠窗口时不会被自动提升为 keep 候选。
- 验证：运行 `python tests\test_abtest_summary.py`、`python tests\test_abtest_walk_forward.py`、`python -m compileall main.py src tests` 均通过；真实运行 `python main.py abtest-summary --experiment liquidity_50m --mode dynamic_universe --reports-date 2026-06-09 --no-obsidian` 成功生成 v3 汇总。
- Git：`Add abtest overlap coverage summary`（本条随该提交一起提交并 push）。

### 02:47:41 +08:00 - 增加 A/B walk-forward 编排命令
- 类型：代码 / 测试 / 文档 / Git
- 改动：新增 `src/crypto_trading_system/abtest_walk_forward.py`，支持解析 `START:END` 或 `START -> END` 多时段参数，并校验日期顺序。
- 改动：新增 CLI 命令 `python main.py abtest-walk-forward --experiment ... --periods ...`，可按多个时段顺序运行同一 A/B 实验，并在本次运行结束后生成只包含本次 period reports 的多时段汇总报告。
- 改动：新增 `tests/test_abtest_walk_forward.py`，覆盖 period 解析、空输入和非递增日期校验。
- 原因：`liquidity_50m` 已进入跨时段验证阶段，手工逐段运行再单独汇总容易漏步骤；需要一个可复现的 walk-forward 编排入口。
- 影响：后续可以用单条命令运行多个 dynamic universe A/B 时段，例如 `python main.py abtest-walk-forward --experiment liquidity_50m --dynamic-universe --periods 2025-01-01:2025-09-01,2025-06-01:2026-06-01 --source-limit 100 --max-symbols 30 --allow-data-gaps --no-obsidian`。
- 验证：运行 `python tests\test_abtest_walk_forward.py`、`python tests\test_abtest_summary.py`、`python tests\test_abtest.py`、`python -m compileall main.py src tests`，均通过；运行 `python main.py abtest-walk-forward --help` 成功显示 CLI 帮助。
- Git：`Add abtest walk-forward command`（本条随该提交一起提交并 push）。

### 02:43:31 +08:00 - Dynamic Universe liquidity_50m 更长近端窗口复测
- 类型：回测 / A/B / 报告 / 文档 / Git
- 改动：运行 `liquidity_50m` dynamic universe A/B，区间为 `2025-06-01 -> 2026-06-01`，参数为 `--source-limit 100 --max-symbols 30 --allow-data-gaps --no-obsidian`。
- 改动：生成 `reports/2026-06-09/abtest_dynamic_universe_liquidity_50m_2025-06-01_2026-06-01_v1.md` 及底层 dynamic universe backtest 报告。
- 改动：重新运行 `abtest-summary`，生成 `reports/2026-06-09/abtest_summary_dynamic_universe_liquidity_50m_2026-06-09_v2.md`，纳入 3 个 `liquidity_50m` dynamic universe 时段。
- 原因：上一段 `2025-09-01 -> 2026-06-01` 的 variant closed_trades=19，刚好低于样本线；需要用更长近端窗口确认方向改善是否能在充足样本下成立。
- 影响：本轮 baseline closed_trades=36、variant closed_trades=38，样本充足；variant 将 PF 从 0.718 提升到 0.810，净收益从 -8.77% 改善到 -5.53%，最大回撤从 19.70% 降到 18.76%。多时段汇总显示 3 个时段中 2 个充足样本时段均改善，但仍因一个短切片 variant 样本不足保持 `retest`。
- 验证：A/B 命令和 `abtest-summary` 命令均成功完成；自动结论为 `sample_sufficient=true`、`verdict=retest`。
- Git：`Run longer liquidity dynamic universe retest`（本条随该提交一起提交并 push）。

### 02:27:20 +08:00 - 增加 A/B 多时段汇总报告
- 类型：代码 / 报告 / 测试 / 文档 / Git
- 改动：新增 `src/crypto_trading_system/abtest_summary.py`，支持从已生成的 A/B Markdown 报告中解析 Raw Metrics JSON，并按 experiment、mode、日期目录聚合多时段结果。
- 改动：新增 CLI 命令 `python main.py abtest-summary --experiment ... --mode dynamic_universe --reports-date ...`，输出 `abtest_summary_*` Markdown 汇总报告。
- 改动：新增 `tests/test_abtest_summary.py`，覆盖报告解析、跨时段汇总、variant 样本不足时保持 `retest` 的规则。
- 改动：生成 `reports/2026-06-09/abtest_summary_dynamic_universe_liquidity_50m_2026-06-09_v1.md` 和 `reports/2026-06-09/abtest_summary_dynamic_universe_history_365_2026-06-09_v1.md`。
- 原因：dynamic universe A/B 已经进入多时段验证阶段，继续手工翻单份报告容易遗漏样本不足、浮点微差和跨段不稳定问题；需要一个轻量汇总入口辅助 keep/retest/reject 判断。
- 影响：`liquidity_50m` 汇总为 2 个时段、1 个充足样本时段，结论 `retest`；`history_365` 汇总为 3 个时段、2 个充足样本时段，因仍包含样本不足时段且近端段无实质改善，结论 `retest`。
- 验证：运行 `python tests\test_abtest_summary.py`、`python tests\test_abtest.py`、`python tests\test_history.py`、`python tests\test_trade_state.py`、`python tests\test_replay.py`、`python tests\test_universe.py`、`python -m compileall main.py src tests`，均通过；真实运行两次 `abtest-summary` 成功生成汇总报告。
- Git：`Add abtest multi-period summary`（本条随该提交一起提交并 push）。

### 02:19:05 +08:00 - Dynamic Universe liquidity_50m 近端跨段复测
- 类型：回测 / A/B / 报告 / 文档 / Git
- 改动：运行 `liquidity_50m` dynamic universe A/B，区间为 `2025-09-01 -> 2026-06-01`，参数为 `--source-limit 100 --max-symbols 30 --allow-data-gaps --no-obsidian`。
- 改动：生成 `reports/2026-06-09/abtest_dynamic_universe_liquidity_50m_2025-09-01_2026-06-01_v1.md` 及底层 dynamic universe backtest 报告，并更新仓库开发计划与 Obsidian 实验日志。
- 原因：`liquidity_50m` 在 `2025-01-01 -> 2025-09-01` 显示 promising retest，需要验证近端市场中方向是否延续。
- 影响：variant 将 trades 从 37 降到 24、closed_trades 从 20 降到 19；PF 从 0.451 提升到 0.479，最大回撤从 18.06% 降到 15.99%，净收益从 -10.09% 改善到 -8.23%。方向延续但 variant 样本未达到 `closed_trades >= 20`，仍不能 keep。
- 验证：A/B 命令成功完成；自动结论为 `sample_sufficient=false`、`verdict=retest`。
- Git：`Run dynamic universe liquidity cross-period retest`（本条随该提交一起提交并 push）。

### 02:07:15 +08:00 - Dynamic Universe history_365 近端跨段复测
- 类型：回测 / A/B / 报告 / 文档 / Git
- 改动：运行 `history_365` dynamic universe A/B，区间为 `2025-09-01 -> 2026-06-01`，参数为 `--source-limit 100 --max-symbols 30 --allow-data-gaps --no-obsidian`。
- 改动：生成 `reports/2026-06-09/abtest_dynamic_universe_history_365_2025-09-01_2026-06-01_v1.md` 及底层 dynamic universe backtest 报告，并更新仓库开发计划与 Obsidian 实验日志。
- 原因：前一段 `2025-01-01 -> 2025-09-01` 中 `history_365` 显示 promising retest，需要用另一段市场验证改善是否稳定。
- 影响：本轮 baseline closed_trades=20、variant closed_trades=20，样本充足；但胜率、Profit factor、Sharpe、最大回撤、净收益、止损率和 avg_r 完全一致，说明 `history_365` 的改善不具备跨段稳定性，不能 keep。
- 验证：A/B 命令成功完成；baseline trades=37、closed_trades=20、PF=0.451、净收益=-10.09%、最大回撤=18.06%；variant trades=35、closed_trades=20、PF=0.451、净收益=-10.09%、最大回撤=18.06%。
- 备注：曾尝试运行 `2024-06-01 -> 2024-12-31` 同参数长窗口，20 分钟超时且只留下 baseline 半成品报告，已删除该未完成报告，未作为实验结论。
- Git：`Run dynamic universe history cross-period retest`（本条随该提交一起提交并 push）。

### 01:22:00 +08:00 - Dynamic Universe liquidity_50m 充足样本复测
- 类型：回测 / A/B / 报告 / 文档 / Git
- 改动：运行 `liquidity_50m` dynamic universe A/B，区间为 `2025-01-01 -> 2025-09-01`，参数为 `--source-limit 100 --max-symbols 30 --allow-data-gaps --no-obsidian`。
- 改动：生成 `reports/2026-06-09/abtest_dynamic_universe_liquidity_50m_2025-01-01_2025-09-01_v1.md` 及底层 dynamic universe backtest 报告，并更新仓库开发计划与 Obsidian 实验日志。
- 原因：`history_365` 已在同一窗口显示 promising retest，`pump_chase_strict` 无差异；需要验证提高最小成交额门槛是否也能在充足样本下改善风险收益。
- 影响：variant 将 trades 从 108 降到 60、closed_trades 从 33 降到 30，同时将 Profit factor 从 0.431 提升到 0.648，最大回撤从 19.84% 降到 14.69%，净收益从 -15.27% 改善到 -8.13%；结论为 promising `retest`，仍不能直接 keep。
- 验证：A/B 命令成功完成；baseline closed_trades=33、PF=0.431、Sharpe=-1.345、净收益=-15.27%；variant closed_trades=30、PF=0.648、Sharpe=-0.630、净收益=-8.13%。
- Git：`Run sufficient dynamic universe liquidity retest`（本条随该提交一起提交并 push）。

### 01:10:49 +08:00 - Dynamic Universe pump_chase_strict 充足样本复测
- 类型：回测 / A/B / 报告 / 文档 / Git
- 改动：运行 `pump_chase_strict` dynamic universe A/B，区间为 `2025-01-01 -> 2025-09-01`，参数为 `--source-limit 100 --max-symbols 30 --allow-data-gaps --no-obsidian`。
- 改动：生成 `reports/2026-06-09/abtest_dynamic_universe_pump_chase_strict_2025-01-01_2025-09-01_v1.md` 及底层 dynamic universe backtest 报告，并更新仓库开发计划与 Obsidian 实验日志。
- 原因：在 `history_365` 样本过线后，用同一 dynamic universe 和日期窗口检验收紧追高扣分是否能改变交易集。
- 影响：baseline 与 variant 完全一致，closed_trades 均为 33，PF 均为 0.431，净收益均为 -15.27%；说明当前 `pump_chase_strict` 参数在该 dynamic universe 样本中没有实际筛选效果。
- 验证：A/B 命令成功完成；`sample_sufficient=true`，但所有核心指标无差异。
- Git：`Run sufficient dynamic universe pump retest`（本条随该提交一起提交并 push）。

### 00:58:53 +08:00 - Dynamic Universe history_365 样本过线复测
- 类型：回测 / A/B / 报告 / 文档 / Git
- 改动：运行 `history_365` dynamic universe A/B，区间拉长到 `2025-01-01 -> 2025-09-01`，参数保持 `--source-limit 100 --max-symbols 30 --allow-data-gaps --no-obsidian`。
- 改动：生成 `reports/2026-06-09/abtest_dynamic_universe_history_365_2025-01-01_2025-09-01_v1.md` 及底层 dynamic universe backtest 报告，并更新仓库开发计划与 Obsidian 实验日志。
- 原因：上一轮 `2025-01-01 -> 2025-06-01` 只有 14/13 笔闭合交易，仍未达到 `closed_trades >= 20`；需要拉长时间段验证 `history_365` 是否在充足样本下改善策略质量。
- 影响：本轮 baseline closed_trades=33、variant closed_trades=29，样本首次充足；variant 胜率、Profit factor、净收益和最大回撤均改善，但策略整体仍为负收益，因此结论为 promising `retest`，不能直接 keep。
- 验证：A/B 命令成功完成；baseline PF=0.431、净收益=-15.27%、最大回撤=19.84%；variant PF=0.654、净收益=-7.84%、最大回撤=15.99%；`sample_sufficient=true`。
- Git：`Run sufficient dynamic universe history retest`（本条随该提交一起提交并 push）。

### 00:30:11 +08:00 - 负缓存后扩大 Dynamic Universe A/B
- 类型：回测 / A/B / 报告 / 文档 / Git
- 改动：运行 `history_365` dynamic universe A/B，区间为 `2025-01-01 -> 2025-06-01`，参数为 `--source-limit 100 --max-symbols 30 --allow-data-gaps --no-obsidian`。
- 改动：生成 `reports/2026-06-09/abtest_dynamic_universe_history_365_2025-01-01_2025-06-01_v1.md` 及底层 dynamic universe backtest 报告，并更新仓库开发计划与 Obsidian 实验日志。
- 原因：验证 K 线无数据负缓存后，扩大 dynamic universe 是否能让 A/B 样本达到 `closed_trades >= 20`。
- 影响：样本从上一轮扩大版的 baseline 17 trades / 11 closed_trades 提升到 36 trades / 14 closed_trades，但仍未达到样本充足门槛；`history_365` 继续保留为 `retest`，不能 keep。
- 验证：A/B 命令成功完成；baseline closed_trades=14、PF=0.198、净收益=-10.37%、最大回撤=12.67%；variant closed_trades=13、PF=0.214、净收益=-9.44%、最大回撤=11.66%；`sample_sufficient=false`。
- Git：`Run larger dynamic universe history retest`（本条随该提交一起提交并 push）。

### 00:03:57 +08:00 - 增加 K 线无数据负缓存
- 类型：代码 / 数据库 / 测试 / 文档 / Git
- 改动：新增 `kline_unavailable_ranges` SQLite 表，用于记录 Binance 对指定 `symbol`、`interval`、时间区间返回空 K 线批次的情况。
- 改动：`fetch_klines_cached` 在命中无数据区间时直接使用 no-data marker，不再重复请求 Binance；同时保留 `allow_data_gaps=false` 时抛出数据质量错误的原有行为。
- 改动：新增 `tests/test_history.py`，覆盖空批次写入负缓存、二次请求不再访问 API、严格数据缺口模式仍然报错。
- 改动：更新 `TODO.md`、仓库开发计划和 Obsidian 开发计划，将 K 线无数据负缓存标记为已完成。
- 原因：dynamic universe A/B 扩大时，新上市或历史区间无数据的 symbol 会反复触发 Binance 请求，拖慢实验迭代。
- 影响：后续同区间 dynamic universe smoke / A/B 对无历史 symbol 的重复请求会减少；已有正向 K 线缓存和正常有数据路径不变。
- 验证：运行 `python tests\test_history.py`、`python tests\test_replay.py`、`python tests\test_universe.py`、`python tests\test_abtest.py`，均通过。
- Git：`Add kline no-data negative cache`（本条随该提交一起提交并 push）。

## 2026-06-08

### 23:53:36 +08:00 - 跑 Dynamic Universe A/B 扩大复测
- 类型：回测 / A/B / 报告 / 文档 / Git
- 改动：运行 `history_365`、`pump_chase_strict`、`liquidity_50m` 三组 dynamic universe A/B，区间为 `2025-01-01 -> 2025-04-01`，参数为 `--source-limit 60 --max-symbols 10 --allow-data-gaps --no-obsidian`。
- 改动：追加运行扩大版 `history_365` dynamic universe A/B，区间为 `2025-01-01 -> 2025-06-01`，参数为 `--source-limit 60 --max-symbols 20 --allow-data-gaps --no-obsidian`。
- 改动：生成 `reports/2026-06-08/` 下的 dynamic universe A/B 报告，并更新仓库开发计划、Obsidian 开发计划和 Obsidian 实验日志。
- 原因：固定 symbols A/B 对选币过滤参数没有区分度；需要用历史动态 universe 验证参数类实验是否真正改变交易集和风险收益。
- 影响：确认 dynamic universe A/B 链路可运行；但当前 `source-limit` 和当前 `exchangeInfo` master 下的闭合交易仍不足 20，所有自动结论均为 `retest`，不能 keep 默认策略。
- 验证：四份 A/B 报告均生成成功；`history_365` 扩大版 closed_trades 为 11，`sample_sufficient=false`；`liquidity_50m` 能减少交易数和回撤但样本仅 3 笔闭合交易。
- Git：`Run dynamic universe A/B retests`（本条随该提交一起提交并 push）。

## 2026-06-07

### 00:16:58 +08:00 - 增加 commit 后自动 push 规则
- 类型：文档 / 规则 / Git
- 改动：在 `AGENTS.md` 中增加规则，要求每次创建 Git commit 后继续 push 当前分支到 `origin`，除非用户明确要求不 push，或遇到网络、权限、远端冲突等失败。
- 改动：同步调整失败处理规则，若无法 commit 或 push，都需要写入 `dailylog.md` 并明确告知用户。
- 原因：用户希望工程文件夹中的代码、说明文件和报告能及时同步到 GitHub，方便另一台电脑继续工作。
- 影响：后续改动完成后会默认进入“记录 dailylog -> commit -> push”的闭环；重要信息更不容易只留在本机。
- 验证：检查 `AGENTS.md` 已包含 commit 后 push 的规则；文档变更，未运行代码测试。
- Git：`Push after each commit by default`（本条随该提交一起提交并 push）。

### 00:13:28 +08:00 - 将近期 dailylog 改为中文
- 类型：文档 / 规则 / Git
- 改动：将 `dailylog.md` 近期英文记录改为中文表达，并保留必要的命令名、配置键、状态值和 Git commit message。
- 改动：在 `AGENTS.md` 中增加规则，要求以后 `dailylog.md` 默认尽量使用中文记录。
- 原因：dailylog 是恢复项目上下文的重要入口，中文记录更方便快速回顾当天做了什么。
- 影响：后续工程审计日志会优先使用中文；技术标识如 `BUY_CANDIDATE`、`sample_sufficient`、`python main.py ...` 仍保持原样。
- 验证：检查 `dailylog.md` 近期记录已改为中文，确认 `AGENTS.md` 包含 dailylog 中文记录规则；文档变更，未运行代码测试。
- Git：`Localize dailylog entries`（本条随该提交一起提交）。

### 00:06:21 +08:00 - 将 TODO 改为中文
- 类型：文档 / 规则 / Git
- 改动：将 `TODO.md` 重写为中文，同时保留准确的命令名、配置键、状态值和代码标识。
- 改动：在 `AGENTS.md` 中增加 `TODO.md` 维护规则，要求后续 TODO 主要使用中文记录。
- 原因：TODO 是日常规划入口，纯英文任务会让恢复项目上下文变慢。
- 影响：后续任务清单更容易阅读；`BUY_CANDIDATE`、`sample_sufficient`、`python main.py ...` 等技术标识保持不变。
- 验证：检查 `TODO.md` 已改为中文，并确认 `AGENTS.md` 包含 TODO 中文记录规则；文档变更，未运行代码测试。
- Git：`Convert TODO to Chinese`（本条随该提交一起提交）。

## 2026-06-06

### 23:49:57 +08:00 - 增加 Dynamic Universe Backtest MVP
- 类型：代码 / 回测 / 报告 / 测试 / 文档 / Git
- 改动：新增 Dynamic Universe Backtest MVP，`backtest-dynamic-universe` 会基于已收盘 1h K 线每日重建历史 universe，使用 BTCUSDT 4h 作为全局时间轴，并把动态 universe 元数据写入报告。
- 改动：新增动态 universe helper，支持当前 `exchangeInfo` symbol master、`--source-limit`、预筛分数、每日刷新 key、过滤统计和 summary 生成。
- 改动：扩展 A/B 测试，支持 `--dynamic-universe`、`--max-symbols` 和 `--source-limit`；baseline 和 variant 共享同一份内存中的动态 symbol master。
- 改动：新增测试，覆盖未来数据排除、24h universe 过滤、source-limit 排序、BTC 时间轴失败、每日刷新 key 行为和动态 A/B 共享 master。
- 改动：更新 `TODO.md`、开发计划、Obsidian 实验日志，并生成 `reports/2026-06-06/` 下的最终 smoke 报告。
- 原因：固定 symbols 回测和当前快照回测不足以验证选币过滤参数；要做有意义的选币规则 A/B，必须先有动态 universe 历史回放。
- 影响：可以运行 `python main.py backtest-dynamic-universe --start 2025-01-01 --end 2025-02-01 --source-limit 20 --max-symbols 5 --no-obsidian --allow-data-gaps`，也可以用 `python main.py abtest --experiment history_250 --dynamic-universe ...` 做动态 A/B。
- 验证：运行 `python -m compileall main.py src tests`、`python tests\test_trade_state.py`、`python tests\test_replay.py`、`python tests\test_universe.py`、`python tests\test_abtest.py`；smoke 生成 `backtest_dynamic_universe_2025-01-01_2025-02-01_v4.md`，trades=3、closed_trades=3、sample_sufficient=false；动态 A/B 生成 `abtest_dynamic_universe_history_250_2025-01-01_2025-02-01_v2.md`，verdict=retest。
- Git：`Add dynamic universe backtest MVP`（本条随该提交一起提交）。

### 23:02:52 +08:00 - 增加 Universe Snapshot 回测
- 类型：代码 / 报告 / 测试 / 文档 / Git
- 改动：新增 `src/crypto_trading_system/backtest/universe.py` 和 `backtest-universe` CLI 命令，用当前 Binance 市场快照构建 symbol 池，筛选交易对并回放历史 K 线。
- 改动：扩展回测 replay 和报告，加入 `universe_mode`、快照元数据、replay/skipped symbol 数量、当前快照警告和 `backtest_universe_*` 报告文件名。
- 改动：当快照 symbol 在指定回测区间没有主周期历史数据时跳过，而不是让回测崩溃；被跳过的 symbol 会记录到报告里。
- 改动：新增 `tests/test_universe.py`，更新 `TODO.md`，同步开发计划，并将 universe snapshot smoke-test 摘要写入 Obsidian 实验日志。
- 原因：固定 symbols 回测不适合评估选币过滤参数；snapshot MVP 提供一个更广、更可复现的第一步，同时明确记录幸存者偏差限制。
- 影响：可以运行 `python main.py backtest-universe --start 2025-01-01 --end 2025-02-01 --max-symbols 3 --no-obsidian --allow-data-gaps` 生成 universe snapshot 回测报告。
- 验证：运行 `python -m compileall main.py src tests`、`python tests\test_trade_state.py`、`python tests\test_replay.py`、`python tests\test_abtest.py`、`python tests\test_universe.py`；smoke 生成 `reports/2026-06-06/backtest_universe_2025-01-01_2025-02-01_v1.md`，trades=1、closed_trades=1、sample_sufficient=false。
- Git：`Add universe snapshot backtest`（本条随该提交一起提交）。

### 21:46:06 +08:00 - 增加项目记忆规则
- 类型：文档 / 规则 / Git
- 改动：更新 `AGENTS.md`，增加 Project Memory Rules，将 `dailylog.md`、`TODO.md`、Obsidian 开发计划和 Obsidian 实验日志的职责拆开。
- 改动：创建 Obsidian 笔记 `D:\MyNotebook-Obsidian\CryptoTradingSystem\CryptoTrading Experiment Log.md`，使用预期的中文文件名；加入使用说明、固定实验模板和 2026-06-06 A/B 选币参数复盘。
- 原因：`dailylog.md` 只适合审计工程改动，实验结果和研究结论容易在几天后丢失上下文。
- 影响：以后每次任务结束前都要判断该更新哪些记忆文件；跑回测、A/B、模拟盘评估或扫盘对比并形成结论时，必须更新 Obsidian 实验日志。
- 验证：确认 `AGENTS.md` 包含 Project Memory Rules；确认 Obsidian 实验日志存在，且包含预期文件名、标题、模板和 A/B 复盘章节。
- Git：`Update project memory rules`（本条随该提交一起提交）。

### 19:51:07 +08:00 - 增加 A/B 实验框架
- 类型：代码 / 配置 / 回测 / 报告 / 测试
- 改动：新增 `config/experiments.toml`，定义 `history_250`、`history_365`、`pump_chase_strict`、`liquidity_50m` 等配置覆盖类实验，并将需要结构性逻辑支持的实验标记为 disabled。
- 改动：新增 `abtest` runner 和 CLI，支持自动运行 baseline 与 variant 两次回测、受控应用实验 override、生成统一 A/B Markdown 报告。
- 改动：A/B 报告固定输出 changed_param、old_value、new_value、closed_trades、stop_rate、profit_factor、avg_r、max_drawdown_pct、net_return_pct、sharpe、sample_sufficient、possible_over_filtering、verdict 和 reason。
- 改动：新增 A/B 单元测试，覆盖未知实验、disabled 实验、baseline 不被 variant 污染、override 路径白名单。
- 影响：参数类选币实验可以通过 `python main.py abtest --experiment ...` 复现和对比，不修改默认 `settings.toml`；结构性逻辑实验仍需单独分支实现。
- 验证：运行 `python -m compileall main.py src tests`、`python tests\test_trade_state.py`、`python tests\test_replay.py`、`python tests\test_abtest.py`，均通过；烟测 `python main.py abtest --experiment history_250 --symbols BTCUSDT,ETHUSDT,SOLUSDT --start 2025-01-01 --end 2025-06-01 --no-obsidian` 生成 A/B 报告，因 closed_trades=12 自动标记 `sample_sufficient=false`、`verdict=retest`。
- Git：`Add abtest experiment runner`（本条随该提交一并提交）。

### 18:42:44 +08:00 - 更新选币优化 TODO
- 类型：文档 / 计划
- 改动：更新 `TODO.md` 的 Priority 1 清单，将验证池补位、动态 warmup、扣分参数化、模拟盘只导入 `BUY_CANDIDATE`、`sample_sufficient` 标记列为已完成。
- 改动：新增后续待实施的单独 A/B 项，包括 180/250/365 历史长度对比、三段式历史结构、追高过滤收紧、流动性门槛、日线强趋势硬门槛和趋势相关高波动惩罚。
- 影响：后续选币策略优化会按单一变量逐项验证，避免一次性叠加多个硬过滤导致结果无法归因。
- 验证：文档变更，未运行代码测试；已确认 `TODO.md` 写入成功。
- Git：`Update selection optimization todo`（本条随该提交一并提交）。

### 18:40:43 +08:00 - 收紧选币流程并修复回测预热
- 类型：代码 / 配置 / 回测 / 扫描 / 模拟盘
- 改动：回测预热改为动态覆盖 `min_history_days + 60` 根日线，避免回测早期因历史长度不足产生人为无信号盲区，并同步覆盖 BTC/ETH 大盘环境历史。
- 改动：市场扫描先验证 `min(top_n * 2, 10)` 个候选，数据质量降级后再按 `BUY_CANDIDATE`、`WAIT_PULLBACK`、`WATCH_ONLY`、`REJECT` 优先级和 score 补足最终名单；扫描报告主表新增 `Action` 列。
- 改动：模拟盘导入默认只接受 `[paper].import_actions = ["BUY_CANDIDATE"]`，非允许 action 会计入 `skipped_action`，且不会触发旧 WATCHING 计划归档。
- 影响：回测、扫描和模拟盘的可交易信号口径更一致；该提交属于行为修复，回测结果允许变化。
- 验证：运行 `python -m compileall main.py src tests`、`python tests\test_trade_state.py`、`python tests\test_replay.py`，均通过；`python main.py scan --top 5 --no-obsidian` 生成 scan_id=502521f405e0，验证池为 10 个候选，报告含 Action 列；`python main.py paper add-from-scan --scan-id 502521f405e0` 输出 added=0、skipped=5、skipped_action=5、archived=0；BTCUSDT/ETHUSDT/SOLUSDT 2025-01-01 至 2025-06-01 回测从 baseline trades=6、closed_trades=3、first_trade=2025-04-12 变为 trades=15、closed_trades=12、first_trade=2025-01-02，确认旧 warmup 早期盲区被修复，且报告标记 sample_sufficient=false。
- Git：`Tighten selection workflow`（本条随该提交一并提交）。

### 18:33:47 +08:00 - 参数化选币扣分并增加回测样本字段
- 类型：代码 / 配置 / 回测 / 报告
- 改动：将追高扣分和 24h 高波动扣分从扫描器硬编码提取为 `[analysis]` 配置项，默认值保持旧逻辑等效。
- 改动：扫描、回测和单币复核共用新的扣分配置；回测报告新增 `sample_sufficient` 字段，闭合交易少于 20 笔时显式标记样本不足。
- 影响：默认参数下交易判定不应改变；新增字段用于防止把小样本回测指标误读为策略改善。
- 验证：运行 `python -m compileall main.py src tests`、`python tests\test_trade_state.py`、`python tests\test_replay.py`，均通过；BTCUSDT/ETHUSDT/SOLUSDT 2025-01-01 至 2025-06-01 阶段 A before/after 回测均为 trades=6、closed_trades=3、net_return=3.77%、max_drawdown=3.34%、win_rate=66.67%、profit_factor=4.80、stop_rate=33.33%。
- Git：`Parameterize selection penalties`（本条随该提交一并提交）。

### 17:44:49 +08:00 - 新增策略优化 TODO 清单
- 类型：文档 / 计划
- 改动：新增根目录 `TODO.md`，记录选币策略、买入规则、卖出规则和回测 A/B 测试的后续优化路线。
- 改动：将已完成的“数据质量 + 历史长度 + 大盘环境”过滤标记为完成，并把 365 天历史过滤、远离支撑过滤、流动性门槛、趋势强度、TP1 减仓和移动止损等规则列为待办。
- 影响：后续策略优化有了统一的待办入口，可以按单一变量逐项回测验证，避免一次改太多导致无法归因。
- 验证：文档变更，未运行代码测试；已检查 `TODO.md` 写入成功。
- Git：`Add strategy optimization todo`（本条随该提交一并提交）。

### 17:35:59 +08:00 - 增加数据质量、历史长度和大盘环境过滤
- 类型：代码 / 配置 / 回测 / 扫描
- 改动：新增 `market_regime.py`，用 BTC/ETH 日线 EMA20、EMA50 和 7 日涨跌判断 `RISK_ON`、`NEUTRAL`、`RISK_OFF`，弱市时将山寨币买入候选降级为观察。
- 改动：在 `[analysis]` 增加 `min_history_days`、`market_regime_filter_enabled`、`data_quality_filter_enabled`、`strict_data_quality_for_buy`，默认要求 180 根 1d K 线并启用严格数据质量过滤。
- 改动：扫描器在生成候选前应用历史长度和大盘环境过滤，在 CoinGecko/CoinMarketCap 交叉验证后将非 `DATA_OK` 的买入候选降级为观察。
- 改动：回测重放也接入同一套历史长度和 BTC/ETH 大盘环境过滤，避免回测与实时扫描使用不同买入门槛。
- 影响：当前策略会更保守；弱市或数据交叉验证异常时不会直接给出买入候选，而是保留为关注对象。
- 验证：运行 `python -m compileall main.py src tests`、`python tests\test_trade_state.py`、`python tests\test_replay.py`、`python main.py scan --top 3 --no-obsidian`，均通过；扫描结果显示 `RISK_OFF` 时候选被降级为 `WATCH_ONLY`。
- Git：`Add strategy quality filters`（本条随该提交一并提交）。

### 11:39:08 +08:00 - 增加回测模块基础设施和共享状态机
- 类型：代码 / 配置 / 数据库
- 改动：新增 `[backtest]` 配置和 `BacktestSettings`，扩展 Binance K 线接口支持 `startTime/endTime` 分页参数。
- 改动：新增 `ticker_utils.reconstruct_ticker`、`trade_state.step_trade`、`backtest/history.py`，支持历史 1h ticker 重建、共享交易状态机、K 线缓存和数据质量检查。
- 改动：扩展 SQLite 初始化，加入 `kline_cache`、`backtest_runs`、`backtest_trades`、`backtest_metrics` 表；`TradeCandidate` 增加结构化 `action` 字段。
- 改动：`paper_trader.update_paper_trades` 改为调用共享 `step_trade`；修正扫描器 7 日涨幅为固定 168 根 1h K 线口径。
- 影响：为回测引擎提供无前视 ticker 重建、历史数据缓存和可复用状态机，同时保持现有模拟盘更新路径行为一致。
- 验证：运行 `python -m compileall main.py src tests`、`python tests/test_trade_state.py`，均通过。
- Git：`e383554` - `Add backtest foundations`。

### 11:47:56 +08:00 - 增加回测引擎、指标、报告和 CLI
- 类型：代码 / 报告 / 数据库
- 改动：新增 `backtest/costs.py`、`backtest/replay.py`、`backtest/metrics.py`、`backtest/runner.py`，实现 4h 全局时间轴历史回放、手续费/滑点、组合权益曲线、绩效指标和 Markdown 报告。
- 改动：`main.py` 新增 `backtest` 子命令，支持 `--symbols`、`--start`、`--end`、`--interval`、`--intrabar`、`--allow-data-gaps`、`--no-obsidian`。
- 改动：新增 `tests/test_replay.py`，验证历史 ticker 重建不读取未来数据、未收盘 K 线不会进入决策切片。
- 影响：可以运行 `python main.py backtest --symbols BTCUSDT --start 2024-06-01 --end 2024-09-01 --interval 4h` 生成回测报告并写入 SQLite。
- 验证：运行 `python -m compileall main.py src tests`、`python tests/test_trade_state.py`、`python tests/test_replay.py`，并完成 BTCUSDT 2024-06-01 至 2024-09-01 回测烟测。
- Git：`b05a89d` - `Add backtest engine`。

### 11:48:50 +08:00 - 生成回测模块验收报告
- 类型：报告 / Git
- 改动：运行 BTCUSDT 2024-06-01 至 2024-09-01 的 4h 回测，生成 `reports/2026-06-06/backtest_2024-06-01_2024-09-01_v1.md`。
- 影响：仓库内保留一份可人工复核的回测验收样例，报告包含回测假设、核心指标、benchmark、交易明细和代码 commit hash。
- 验证：运行 `python -m compileall main.py src tests`、`python tests/test_trade_state.py`、`python tests/test_replay.py`、`python main.py backtest --symbols BTCUSDT --start 2024-06-01 --end 2024-09-01 --interval 4h --no-obsidian`，全部通过。
- Git：待本次验收报告提交后回填。

### 12:09:21 +08:00 - 回测报告增加中英文术语对照
- 类型：代码 / 报告
- 改动：在回测报告核心指标、benchmark、交易明细、开放持仓、过期计划和数据质量表中，将英文表头、指标名、状态名改为英文 + 中文对照。
- 改动：新增“术语速查”段，解释 PnL、Gross PnL、Net PnL、R、Drawdown、Profit factor、Sharpe、Sortino、Exposure、Turnover 等术语。
- 影响：阅读回测报告时可以直接理解英文指标含义，降低复盘门槛；不改变回测计算逻辑。
- 验证：运行 `python -m compileall main.py src tests`、`python tests/test_trade_state.py`、`python tests/test_replay.py`、短区间 `python main.py backtest --symbols BTCUSDT --start 2024-06-01 --end 2024-06-15 --interval 4h --no-obsidian`，确认报告显示中英文对照；临时短报告未纳入提交。
- Git：待本次术语对照提交后回填。

## 2026-06-03

### 22:20:37 +08:00 - 增加 doctor 命令和扫描进度输出
- 类型：代码 / 报告 / 文档
- 改动：新增 `src/crypto_trading_system/doctor.py`，支持 `python main.py doctor` 检查 Binance、CoinGecko、CoinMarketCap API Key、SQLite、项目报告目录和 Obsidian 目录。
- 改动：`scan`、`daily`、`verify` 增加实时进度输出，显示加载 Binance 行情、逐个交易对分析、外部数据交叉验证、保存数据库和写报告等步骤。
- 改动：更新 `README.md`，补充 `doctor` 命令和扫描进度说明。
- 影响：运行耗时命令时不再长时间空白，API 或目录问题也可以用 `doctor` 快速定位。
- 验证：运行 `python -m compileall main.py src`、`python main.py doctor`、`python main.py scan --top 1`；验证生成 `market_scan_2026-06-03_v5.md`，进度输出正常。
- Git：随本次 doctor 和进度输出提交一起记录。

### 21:50:22 +08:00 - 增加数据交叉验证模块
- 类型：代码 / 报告 / 数据库 / 文档
- 改动：新增 `src/crypto_trading_system/data_validation.py`，支持 Binance 主源、CoinGecko 自动对照、CoinMarketCap API Key 可选对照。
- 改动：扩展配置、模型、扫描器、单币复核、报告渲染和 SQLite 存储，新增 `DATA_OK`、`DATA_WARNING`、`DATA_ERROR`、`DATA_SKIPPED` 状态。
- 改动：新增 `data_cross_checks` SQLite 表，保存每个 scan_id、symbol、provider 的价格差异、24h 涨跌差异、状态和说明。
- 改动：报告增加“数据交叉验证摘要”和每个候选币的“多数据源对照”表；重大数据错误会把候选降级为“只观察”。
- 改动：修正 `PORTAL` 的 CoinGecko 映射覆盖为 `portal-2`。
- 影响：候选币报告不再只依赖 Binance 单源数据，可以人工复核 CoinGecko / CoinMarketCap 对照状态。
- 验证：运行 `python -m compileall main.py src`、`python main.py scan --top 2` 两次，生成 `market_scan_2026-06-03_v2.md` 和修正映射后的 `market_scan_2026-06-03_v3.md`；运行轻量单币复核脚本确认 ZECUSDT 有 3 条数据检查记录。
- Git：随本次数据交叉验证提交一起记录。

### 21:27:09 +08:00 - 增加工作空间级提交与日志规则
- 类型：文档 / Git
- 改动：新增 `AGENTS.md`，声明本工作空间每次代码改动后都要更新 `dailylog.md` 并创建 Git commit。
- 影响：后续开发任务会固定留下时间戳日志和对应提交，便于回溯每次改动。
- 验证：确认规则文件位于仓库根目录，适用于整个 CryptoTradingSystem 工作空间。
- Git：随本次规则变更提交一起记录。

### 21:23:37 +08:00 - 新建 dailylog 文件
- 类型：文档
- 改动：新增 `dailylog.md`，用于记录每天每次代码或工程文件改动。
- 影响：后续可以从一个固定文件回看每天做了哪些开发动作。
- 验证：确认当前 Git 工作区在创建前为 `main...origin/main` 干净状态。
- Git：本条为日志文件新增记录，不自引用 commit hash。

### 21:22:20 +08:00 - 报告文件名改为每日版本号
- 类型：代码 / 报告 / 文档
- 改动：新增 `src/crypto_trading_system/report_versions.py`，让市场扫描、单币复核、模拟盘报告按 `v1`、`v2`、`v3` 自动递增命名。
- 改动：更新 `src/crypto_trading_system/reports.py` 和 `src/crypto_trading_system/paper_trader.py`，在报告 frontmatter 和正文中写入 `report_version`，同时保留 `scan_id`。
- 改动：将已有报告重命名为可读版本号格式，例如 `market_scan_2026-06-03_v1.md`、`paper_report_2026-06-03_demo_v1.md`。
- 影响：同一天多次运行脚本时，报告文件名更容易人工识别；原始 `scan_id` 仍可用于追溯数据库记录。
- 验证：运行 `python -m compileall main.py src` 和 `python main.py paper report`，确认生成 `paper_report_2026-06-03_demo_v2.md`。
- Git：`dd11fc9` - `Use daily report version filenames`。

### 21:06:18 +08:00 - 上传生成报告到 GitHub
- 类型：报告 / Git
- 改动：取消 `.gitignore` 对 `reports/` 的忽略，将历史 Markdown 报告和 SVG 图表纳入 Git。
- 影响：GitHub 仓库可以查看已生成的市场扫描报告、单币复核报告和模拟盘报告。
- 验证：确认 `data/crypto_trading.db` 仍被 `.gitignore` 忽略，没有上传本地数据库。
- Git：`390e3c3` - `Add generated trading reports`。

### 21:03:08 +08:00 - 初始化 GitHub 工程
- 类型：代码 / 配置 / Git
- 改动：初始化 Git 仓库，提交 CryptoTradingSystem MVP 代码、配置、README 和 `.codex/skills`。
- 改动：配置 `.gitignore`，忽略 Python 缓存、本地数据库、虚拟环境和日志文件。
- 影响：工程代码首次同步到 GitHub 仓库 `Goodyenough/wbj-CryptoTrading`。
- 验证：确认远程 `origin/main` 指向提交 `45b6ed9`。
- Git：`45b6ed9` - `Initial crypto trading system MVP`。
