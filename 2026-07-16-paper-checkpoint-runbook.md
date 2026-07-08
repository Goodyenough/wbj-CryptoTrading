# 2026-07-16 Paper 阶段检查 Runbook

## 目的

2026-07-16 不是最终策略结论日，而是阶段检查点。

当天先判断新观察窗口是否具备 formal audit 条件，再决定输出正式 audit、interim report，或继续等待样本成熟。

本 runbook 只用于复盘和诊断：

- 不修改 `settings.toml`。
- 不修改 live paper 状态机。
- 不补跑或重算历史 paper 状态。
- 不根据单次 checkpoint 直接启动正式 A/B。

## 观察窗口

主窗口：

```text
2026-07-03 -> 2026-07-16
```

原因：

- 2026-07-02 已完成阶段性验收；
- 2026-07-03 起进入下一段冻结配置观察；
- 2026-07-16 作为两周后的阶段检查点。

## Step 1: 检查工作区和配置

```powershell
git status --short
git diff -- config/settings.toml
```

通过条件：

- `config/settings.toml` 没有 diff；
- 若工作区有自动报告文件，可以继续，但不要混入无关代码改动；
- 若 `settings.toml` 有变化，停止 formal audit，先解释配置变化来源。

## Step 2: 运行 checkpoint

```powershell
python main.py paper checkpoint --account demo --start-date 2026-07-03 --end-date 2026-07-16
```

先读 checkpoint 报告中的：

- `verdict`
- `data_link_verdict`
- `config_hash_stable`
- `daily_success`
- `paper_4h_success`
- `mature`
- `right_censored_ratio`
- `entered_trades`

命令也会在终端直接输出上述关键字段；若终端摘要与报告不一致，以报告正文和 `Raw Summary` 为准，并停止 formal audit 先排查。

## Step 3: 根据 checkpoint verdict 分流

### A. `formal_audit_ready`

可以继续生成正式审查证据：

```powershell
python main.py paper audit --account demo --start-date 2026-07-03 --end-date 2026-07-16
python main.py paper shadow-replay --account demo --start-date 2026-07-03 --end-date 2026-07-16 --variant entry_reclaim_confirm_1bar
python main.py paper shadow-replay --account demo --start-date 2026-07-03 --end-date 2026-07-16 --variant relative_strength_gate
```

正式审查仍然只回答：

```text
没赚钱或少赚钱的原因是什么
```

不能直接写：

```text
策略已证明有效
```

### B. `wait_for_more_data`

不做策略结论，只输出 interim report。

记录重点：

- 样本为什么不成熟；
- `right_censored` 比例是多少；
- 需要等到哪一天再复查；
- daily + 4h 是否继续正常。

不启动 A/B，不修改配置。

### C. `interim_report_required`

说明数据链路或配置存在影响解释的问题。

优先排查：

- `config_hash` 是否漂移；
- daily 是否漏跑；
- 4h 是否连续失败；
- stale running 是否不为 0；
- 数据库、report、dashboard 是否不一致。

问题未解释前，不做策略优化结论。

## Step 4: formal audit 后的判断口径

如果已进入 formal audit，最终仍按以下问题归因：

| 证据 | 优先解释 |
|---|---|
| `avoided_loser` 多，`missed_winner` 少 | 防守规则阶段性有效，继续观察 |
| `missed_winner` 多，且 R 倍数损失大 | `RECLAIM_PENDING` / `RISK_OFF` 可能过保守 |
| entered trades 多数无明显 MFE | 选币或入场质量问题 |
| entered trades 有明显 MFE 后回吐 | 退出规则问题 |
| BTC/ETH 明显上涨但策略参与少 | 进攻模式或候选生成问题 |
| 数据链路异常 | 先修数据链路，不解释策略 |

## Step 5: 提交记录

若当天生成了报告，按项目规则提交：

```powershell
git add reports TODO.md dailylog.md
git commit -m "Add July 16 paper checkpoint review"
git push origin main
```

如果当天也新增了代码或修复脚本，commit message 应对应实际改动，不要混用验收报告提交名。

## 红线

出现以下任一情况，不得启动正式 A/B：

- `settings.toml` 发生未解释变化；
- checkpoint verdict 不是 `formal_audit_ready`；
- daily 或 4h 缺失影响关键状态判断；
- 数据库存在 stale running、重复事件或明显状态机异常；
- 报告试图用未成熟样本证明长期盈利能力；
- 只因为短期亏损就直接改参数。

## 当天推荐结论模板

如果 checkpoint 通过但交易样本仍有限：

```text
数据链路和配置冻结状态满足阶段性审查条件；当前证据可用于分析策略行为与机会成本，但仍不足以证明长期盈利能力。下一步根据 formal audit、shadow replay 和 entered trades 归因，决定是否继续观察或设计单变量 A/B。
```

如果 checkpoint 不通过：

```text
本窗口暂不具备 formal audit 条件；当前结果只作为 interim observation，优先解释数据链路、配置稳定性或样本成熟度问题，不启动策略参数调整。
```
