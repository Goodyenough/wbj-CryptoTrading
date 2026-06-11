# Handoff Log

---

## 2026-06-11 15:30 +08:00

### 项目目录

`D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects`

---

### 任务背景

加密货币量化交易回测系统。本次会话主要完成了：性能优化文档补全、多轮 A/B 实验、模拟盘口径对齐、定时任务配置、日线趋势过滤实验。

---

### 已完成的工作

1. **性能优化文档**：创建 `reports/2026-06-11/perf_optimization_2026-06-11.md`，记录 5 轮优化（bisect、批量 SQL、float 存储、EMA 增量、kline_fetch_ranges），commit `e4b0102`

2. **tp1_ema20_trailing_stop A/B**：
   - 单段（2025-01→2025-09）：PF 0.58→0.75，净收益 -13.17%→-10.31%，verdict=`retest`
   - walk-forward 两段（2024-07→2025-01 / 2025-01→2025-09）：方向改善但近端 MDD 上升，verdict=`retest`
   - commit `080e1ba`

3. **risk_off_no_core_entry_reclaim_ema_stop 组合实验**（三项叠加：RISK_OFF 停开核心币 + 入场收盘确认 + TP1 EMA20 跟踪止损）：
   - 早期段（2024-07→2025-06）：PF 0.91→1.53，净收益 -5.59%→+16.74%，MDD 18.72%→14.99%
   - 近端段（2025-06→2026-06）：PF 0.73→1.05，净收益 -10.62%→+1.21%，MDD 24.24%→18.68%
   - verdict=`candidate_keep_review`，commit `00f596e`

4. **paper_trader.py 口径对齐**：补全 `entry_reclaim_close` 和 `tp1_ema_trailing_stop` 逻辑，同步传入 `move_stop_to_breakeven_on_tp1`，commit `417681d`

5. **模拟盘定时任务**：创建 `scripts/daily_paper_update.bat`，通过 Windows 任务计划程序每天 20:05 自动运行 scan → add-from-scan → paper update → paper report，日志写入 `logs/daily_paper_update.log`（需用户在管理员 PowerShell 完成注册，时间已由用户改为 20:05）

6. **daily_trend_required 实验**：
   - 实现：`config.py` 新增参数、`scanner.py` + `replay.py` 接入开关、`abtest.py` 白名单新增 `daily_trend` dimension
   - 修复：replay.py 初版漏传参数（delta 全为 0），修复后 v2 重跑
   - 结果：近端段 PF 0.73→0.32，净收益 -10.62%→-22.71%，止损率 77%→89%，verdict=`reject_candidate`
   - commit `14d24d7`

7. **AGENTS.md 更新**：新增 Context Handoff 规则，commit `5ba7ace`

---

### 尚未完成的事项

1. **正式 keep `risk_off_no_core_entry_reclaim_ema_stop`**：等模拟盘跑约 3 周（至 2026-07-02）后再将三项 override 写入 `settings.toml`；已设 CronCreate 提醒（session-only，可能已失效），TODO 里有记录
2. **Windows 任务计划时间确认**：用户在管理员 PowerShell 里已将时间改为 20:05，但未在本会话里验证是否成功
3. **tp1_ema_trailing_stop corner case**：TP1 命中时 4h K 线不足 20 根，`tp1_trailing_ema_stop_active` 标志设为 True 但 EMA 为 None，后续可能突然激活；已记录在 TODO，暂不修
4. **daily_trend_required 组合方向**：单独 reject，但在 RISK_ON 环境下组合使用（弱市已由 risk_off 过滤）可能有价值，未实验
5. **幸存者偏差**：Binance 历史退市币未纳入 symbol master，所有回测结果偏乐观，未处理

---

### 下一步直接执行指令

确认定时任务时间是否已改为 20:05：
```powershell
Get-ScheduledTask -TaskName "CryptoTrading_DailyPaperUpdate" | Get-ScheduledTaskInfo | Select-Object NextRunTime
```

如需继续实验，下一个有价值的方向是 `daily_trend_required` + `risk_off_no_core_entry_reclaim_ema_stop` 组合（只在 RISK_ON 下要求日线趋势确认）：
```
python main.py abtest --experiment <新实验名> --dynamic-universe \
  --symbol-master-file reports\2026-06-09\dynamic_master_full.json \
  --start 2024-07-01 --end 2025-06-01 \
  --max-symbols 40 --allow-data-gaps --no-obsidian
```

---

### 重要声明

- **两段回测不能并行运行**：SQLite 数据库会锁，必须串行执行
- **模拟盘三项规则已在代码层生效**（`paper_trader.py`），但 `settings.toml` 默认值未改，模拟盘实际运行仍用旧逻辑；等 3 周后再写入 settings.toml
- **`daily_trend_required` 实验代码已合并主分支**，默认值为 false，不影响现有行为
- 最新 commit：`5ba7ace`，已 push 到 `origin/main`
