# Handoff — 2026-06-12 00:00 +08:00




## 2026-07-30 11:44 +08:00

### ????
`D:\OneDrive - whut.edu.cn\??\CryptoTradingPorjects`

### ????
???????? N3 ???????????????? historical membership ????? source-backed historical master ?????????? `atr_reclaim_0_35` ????????

### ??????
- ?? `scripts/n4_historical_master_mvp.py`?
- ?? N4??? `reports/2026-07-30/atr_reclaim_stage_n4_historical_master_mvp_2026-07-30_v1.md`?`*_master_v1.json`?`*_review_queue_v1.json`?`*_raw_v1.json`?
- ?????total rows `413`?`active_current_master=266`?`excluded_by_strategy_universe_rule=20`?`historical_standard_gap_requires_mapping=127`?
- verdict=`historical_master_mvp_built_validation_blocked`?
- ??? `dailylog.md`?`TODO.md`?`EXPERIMENT_LEDGER.md`?`????.md` ? Obsidian ?????
- ??????`python -m compileall scripts\n4_historical_master_mvp.py`?`python tests\test_universe.py`?

### ???????
- ?? commit/push?
- 127 ? blocking review queue ??? official/source-backed mapping?
- N4 MVP ??????? A/B?

### ?????????
```powershell
git status --short
git add scripts/n4_historical_master_mvp.py dailylog.md TODO.md EXPERIMENT_LEDGER.md ????.md handoff.md reports/
git commit -m "Add atr reclaim N4 historical master MVP"
git push origin main
```

### ????
- ???? third-window corrected N1???????????
- ???? `atr_reclaim_0_35`????? `config/settings.toml`????? `max_active_positions`?
- ???? official-source mapping pipeline?

## 2026-07-30 11:36 +08:00

### ????
`D:\OneDrive - whut.edu.cn\??\CryptoTradingPorjects`

### ????
????? N2 ????????????????? `atr_reclaim_0_35` ???? `2023-07-01 -> 2024-07-01` ??????????????????????????????? historical membership ?????????

### ??????
- ?? `scripts/n3_historical_membership_dataset.py`??? N2 ? historical/current JSON??? historical membership dataset MVP?
- ?? N3??? `reports/2026-07-30/atr_reclaim_stage_n3_historical_membership_dataset_2026-07-30_v1.md`?
- ?????`missing_from_current_master=147`??? `excludable_missing_count=20`?`standard_gap_count=127`?`standard_gap_ratio_pct=32.32%`?
- ?? gate decision `reports/2026-07-30/atr_reclaim_stage_n3_gate_decision_2026-07-30_v1.md`??? `third_window_not_recoverable_without_historical_master`?
- ??? `dailylog.md`?`TODO.md`?`EXPERIMENT_LEDGER.md`?`????.md` ? Obsidian `CryptoTrading ????.md`?
- ??????`python -m compileall scripts\n3_historical_membership_dataset.py`?`python tests\test_universe.py`?

### ???????
- ???? commit/push?????????
- ???? source-backed historical master?N3 ?? MVP ???
- 127 ? standard-like missing symbols ????????? `delisting / rename / migration / tradable_to / source / confidence`?

### ?????????
```powershell
git status --short
git add scripts/n3_historical_membership_dataset.py dailylog.md TODO.md EXPERIMENT_LEDGER.md ????.md handoff.md reports/
git commit -m "Add atr reclaim N3 historical membership gate"
git push origin main
```

### ????
- ???????? corrected N1???????????N3 ?????????????????
- ???? `atr_reclaim_0_35`????? `config/settings.toml`????? `max_active_positions`?
- ????? source-backed historical master???????????

## 2026-07-30 00:57 +08:00

### ????
`D:\OneDrive - whut.edu.cn\??\CryptoTradingPorjects`

### ????
?????? N2-A / N2-B / ?? N0 / ???????? / ? gate ?????? N1 ????????????? `atr_reclaim_0_35` ????? `2023-07-01 -> 2024-07-01` ??????

### ??????
- ?? `scripts/n2_universe_audit.py`??? current master listing date?local kline coverage?Binance public-data historical membership ???
- ?? N2????? `reports/2026-07-30/atr_reclaim_stage_n2_universe_audit_2026-07-30_v2.md`?verdict=`diagnostic_only_historical_membership_gap`?
- ?????418 ? current master symbols ???? listing date?`listed_after_window=152`?`listed_inside_window=49`?`full_window_coverage=208`?`partial_window_coverage=9`???? historical USDT symbols `413`??? `147` ??? current master?
- ?? `reports/2026-07-30/dynamic_master_full_listing_enriched_2026-07-30_v2.json` ?? N0??? `reports/2026-07-30/atr_reclaim_n0_readiness_audit_2026-07-30_v1.md`?verdict=`n0_conditional_pass_with_alignment_warning`?
- ?? gate decision ?? `reports/2026-07-30/atr_reclaim_stage_n2_gate_decision_2026-07-30_v1.md`??? `third_window_diagnostic_only_do_not_rerun_n1`?
- ??? `dailylog.md`?`TODO.md`?`EXPERIMENT_LEDGER.md`?`????.md` ? Obsidian `CryptoTrading ????.md`?
- ??????`python -m compileall scripts\n2_universe_audit.py`?`python tests\test_universe.py`?

### ???????
- ???? commit/push??????????
- ?????? N1???? N2 gate failed????? historical membership ?????
- ??????????????
- ????????? historical symbol membership dataset?

### ?????????
```powershell
git status --short
git add .gitignore scripts/n2_universe_audit.py dailylog.md TODO.md EXPERIMENT_LEDGER.md ????.md reports/
git commit -m "Add atr reclaim N2 universe gate audit"
git push origin main
```

### ????
- ???? `atr_reclaim_0_35`????? `config/settings.toml`????? `max_active_positions`?
- N0 ? conditional pass ????? master + local kline readiness ?????????? historical membership ???????? N2-B gate ???
- `reports/2026-07-30/.n2_cache/` ??? `.gitignore`???????????
- 2026-07-30 00:10 ????? paper ???? `reports/2026-07-30/`??????? reports ?????

## 项目目录

`D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects`

- **Git 远端**：`https://github.com/Goodyenough/wbj-CryptoTrading.git`
- **当前分支**：`main`
- **最新已 push commit**：`d45b609`
- **运行环境**：Windows 11 Pro，PowerShell，Python，SQLite
- **数据库**：`data/crypto_trading.db`（SQLite，**两段回测必须串行**）

---

## 任务背景

当前处于"策略质量优化"阶段。sensitive 组合（`risk_off_core_buy=false` + `entry_reclaim_close=true` + `tp1_ema_trailing_stop=true` + BTC -3% / ETH -5% / `require_both_trend=true`）已于 2026-06-11 写入 `settings.toml` 并在模拟盘生效，观察期至 **2026-07-02**。

本次 session 的主要工作：市值分层两段 walk-forward、max_holding 三阈值两段 walk-forward、实现并运行 `large_cap_only_risk_off` 实验。

---

## 已完成的工作

| 内容 | commit / 状态 |
|---|---|
| 市值分层 2024-07→2025-06 早期段：large-cap +14.14%/MDD 7.77%，altcoin +11.71%/MDD 15.92% | `d45b609` |
| max_holding 三阈值（18/30/42根）两段全部改善，42根最平衡（近端 MDD 9.27%，net +26.93%） | `d45b609` |
| 实现 `risk_off_large_cap_buy_enabled` 字段（`config.py`、`scanner.py`、`replay.py`）| `d45b609` |
| 注册 `large_cap_regime` dimension，新增 `large_cap_only_risk_off` 实验 | `d45b609` |
| `large_cap_only_risk_off` 两段 walk-forward：早期 +11.17%，近端 -6.24%，结论 `retest` | `d45b609` |
| dailylog、TODO、开发计划、实验日志全部更新 | `d45b609` |
| experiments.toml 新增 `max_holding_18x4h_no_tp1` 和 `max_holding_42x4h_no_tp1` 定义 | `d45b609` |

---

## 尚未完成的事项

### 1. 2026-07-02 模拟盘复盘决策（主线，等待观察期结束）

届时检查：entry_reclaim 拦截次数、RISK_OFF 频率、WLDUSDT/ONDOUSDT 持仓结果，决定 sensitive 组合是否 keep。观察期结束后再一起决定下一步实验方向。

### 2. `sensitive + max_holding_42x4h` 组合实验（等观察期结束后再做）

**不着急，等 2026-07-02 复盘后再推进。**

当前准备工作已完成：
- `abtest.py` 已注册 `combined_regime_entry_exit_sensitivity_holding` dimension（commit `6cab41d`）
- `experiments.toml` 尚未添加实验定义（留待观察期结束后补）

届时在 `experiments.toml` 末尾添加：

```toml
[sensitive_max_holding_42x4h]
enabled = true
description = "Sensitive combo (6 params) + max_holding_42x4h: validate that time-based exit still improves on top of sensitive defaults."
dimension = "combined_regime_entry_exit_sensitivity_holding"

[sensitive_max_holding_42x4h.overrides.analysis]
risk_off_core_buy_enabled = false
entry_reclaim_close_enabled = true
tp1_ema_trailing_stop_enabled = true
regime_btc_7d_drop_pct = -3.0
regime_eth_7d_drop_pct = -5.0
regime_require_both_trend = true

[sensitive_max_holding_42x4h.overrides.backtest]
max_holding_bars_without_tp1 = 42
```

然后串行跑两段 A/B（`2024-07-01 -> 2025-06-01` 和 `2025-06-01 -> 2026-06-01`），使用 `reports/2026-06-09/dynamic_master_full.json`，`--max-symbols 40`。

---

## 重要声明

1. **SQLite 单写**：两段 A/B 必须串行，不能并行跑。
2. **symbol master**：所有回测使用 `reports/2026-06-09/dynamic_master_full.json`（418 个币）。
3. **实验新增 dimension 必须先在 `abtest.py` 的 `ALLOWED_OVERRIDE_PATHS` 里注册**，否则运行时报错。`combined_regime_entry_exit_sensitivity_holding` 已注册（未 commit）。
4. **`daily_trend_required` 已 reject**，不要在新实验里复用。
5. **`large_cap_only_risk_off` 已 retest**：近端熊市反而变差，不要 keep，不要继续推进参数叠加方向。
6. **当前未 commit 的文件**：`src/crypto_trading_system/abtest.py`（已加新 dimension）、`TODO.md`、`scripts/install_daily_task.ps1`——下次 session 完成 experiments.toml 添加后一起 commit。
7. **定时任务**：`CryptoTrading_DailyPaperUpdate` 每天 20:05 自动执行，但当前触发时间仍是 09:00，需要管理员权限运行 `powershell -ExecutionPolicy Bypass -File scripts\install_daily_task.ps1` 修正。

---

# Handoff — 2026-06-11 18:00 +08:00


## 项目基本信息

- **项目目录**：`D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects`
- **Git 远端**：`https://github.com/Goodyenough/wbj-CryptoTrading.git`
- **当前分支**：`main`
- **最新 commit**：`0ac8f74` (已 push 到 origin/main)
- **运行环境**：Windows 11 Pro，PowerShell，Python，SQLite
- **数据库**：`data/crypto_trading.db`（SQLite，单文件，**不支持并发写入，两段回测必须串行**）

---

## 系统架构概览

```
main.py                          # 入口，子命令：scan / daily / backtest / abtest / paper 等
config/
  settings.toml                  # 生产配置（当前已激活 sensitive 组合）
  experiments.toml               # A/B 实验定义，所有 variant 参数在此声明
src/crypto_trading_system/
  config.py                      # Settings dataclass，load_settings()
  scanner.py                     # 市场扫描，输出 BUY_CANDIDATE
  market_regime.py               # classify_market_regime()，判断 RISK_ON/NEUTRAL/RISK_OFF
  paper_trader.py                # 模拟盘：add_from_scan / update_paper_trades / generate_paper_report
  trade_state.py                 # 单笔交易状态机：step_trade()
  abtest.py                      # A/B 实验框架，ALLOWED_OVERRIDE_PATHS 白名单
  backtest/replay.py             # 回测主循环
  backtest/runner.py             # 回测入口
  indicators.py                  # ema(), percent_change() 等
  models.py                      # PaperTrade, PaperTradeEvent dataclass
  storage.py                     # DB schema，建表语句
reports/                         # 每日报告输出目录（按日期子目录）
scripts/
  daily_paper_update.bat         # 每天 20:05 定时执行：scan→add-from-scan→update→report
logs/
  daily_paper_update.log         # 定时任务日志
```

---

## 当前生产配置（settings.toml [analysis] 关键字段）

```toml
risk_off_core_buy_enabled = false       # RISK_OFF 时不开新 BTC/ETH 多单
entry_reclaim_close_enabled = true      # 进入 entry zone 后须 4h 收盘确认才入场
tp1_ema_trailing_stop_enabled = true    # TP1 命中后用 4h EMA20 跟踪止损
regime_btc_7d_drop_pct = -3.0          # BTC 7日跌幅阈值（旧值 -5.0）
regime_eth_7d_drop_pct = -5.0          # ETH 7日跌幅阈值（旧值 -8.0）
regime_require_both_trend = true        # BTC+ETH 必须同时 price>EMA20>EMA50 才算趋势确认
```

这六个参数合称 **sensitive 组合**（`risk_off_no_core_entry_reclaim_ema_stop_sensitive`），于 2026-06-11 写入 settings.toml，模拟盘当日起生效。

---

## 实验历史与结论（按时间顺序）

### 1. tp1_ema20_trailing_stop（单项）
- 结论：retest，单独使用效果有限，近端 MDD 上升

### 2. risk_off_no_core_entry_reclaim_ema_stop（三项组合）
- 三项：`risk_off_core_buy=false` + `entry_reclaim_close=true` + `tp1_ema_trailing_stop=true`
- 早期段 2024-07→2025-06：PF 0.91→1.53，净收益 -5.6%→+16.7%，MDD 18.7%→15.0%
- 近端段 2025-06→2026-06：PF 0.73→1.05，净收益 -10.6%→+1.2%，MDD 24.2%→18.7%
- **verdict：candidate_keep_review**

### 3. daily_trend_required（单项 + 四项组合）
- 单项 reject：近端段止损率 77%→89%，净收益 -10%→-23%
- 四项组合 reject：近端段止损率 77%→92%，净收益 -14%→-7.8%（不如三项组合）

### 4. regime_sensitive（仅收紧阈值）
- BTC -5%→-3%，ETH -8%→-5%，require_both_trend=true
- 单独使用方向改善但仍亏损，需配合出入场规则

### 5. risk_off_no_core_entry_reclaim_ema_stop_sensitive（三项 + 收紧阈值，当前主候选）

四段 walk-forward 完整结果：

| 段 | 市场环境 | baseline 净收益 | variant 净收益 | PF | MDD |
|---|---|---:|---:|---:|---:|
| 2024-07→2025-01 | 牛市 | +2.4% | **+25.4%** | 2.52 | 9.0% |
| 2024-07→2025-06 | 牛+震荡 | -14.3% | **+18.0%** | 1.58 | 15.0% |
| 2025-01→2025-06 | 震荡转熊⚠ | -19.7% | **-6.5%** | 0.53 | 10.0% |
| 2025-06→2026-06 | 熊市 | -14.2% | **+5.5%** | 1.17 | 17.8% |

⚠ 2025-01→2025-06 段：sample_insufficient（15笔）+ possible_over_filtering，数据供参考。四段均优于或持平三项组合。

---

## 模拟盘状态

- **账户**：demo，初始权益 10,000 USDT，单笔风险 1%
- **定时任务**：Windows 任务计划 `CryptoTrading_DailyPaperUpdate`，每天 20:05 自动执行
- **执行脚本**：`scripts/daily_paper_update.bat`，依次跑 scan → add-from-scan → paper update → paper report
- **日志**：`logs/daily_paper_update.log`
- **sensitive 组合生效日期**：2026-06-11
- **建议观察截止**：2026-07-02（约 3 周），届时根据模拟盘结果决定是否继续保留

### paper report 现包含的信息（2026-06-11 新增）

每日报告新增三项，专门用于 3 周后的判断：

1. **今日大盘环境节**：regime 状态（RISK_ON/NEUTRAL/RISK_OFF）、BTC/ETH 7d 涨跌与阈值对比、趋势确认情况
2. **RECLAIM_PENDING 事件**：每次价格进入 entry zone 但 4h 收盘未确认时记录事件，可追溯 entry_reclaim 拦截了哪些单
3. **统计补充**：Entry reclaim blocks 累计次数、平均持仓时长

---

## 关键代码位置

### market_regime.py — RISK_OFF 判断逻辑

```python
def classify_market_regime(
    btc_1d, eth_1d,
    btc_7d_drop_pct=-5.0,    # settings.analysis.regime_btc_7d_drop_pct
    eth_7d_drop_pct=-8.0,    # settings.analysis.regime_eth_7d_drop_pct
    require_both_trend=False  # settings.analysis.regime_require_both_trend
) -> MarketRegime
# RISK_ON 条件：trend_ok AND btc_not_breaking AND eth_not_breaking
# require_both_trend=True 时，BTC+ETH 必须同时满足 price>EMA20>EMA50
# 调用方：replay.py:622, scanner.py:356（均透传 settings 参数）
# regime_analysis.py:148 用默认值（仅用于事后分析，不影响回测/扫盘）
```

### paper_trader.py — entry_reclaim 逻辑

```python
# update_paper_trades() 约 437 行
# 条件：entry_reclaim_enabled AND status==WATCHING AND price<=entry_high
# 若 4h 最新已收盘 close < entry_high → 记录 RECLAIM_PENDING 事件，跳过入场
# 每天定时任务运行一次，不会重复记录
```

### abtest.py — dimension 白名单

新增的两个 dimension（可直接在 experiments.toml 引用）：

```python
"regime_sensitivity": {
    "analysis.regime_btc_7d_drop_pct",
    "analysis.regime_eth_7d_drop_pct",
    "analysis.regime_require_both_trend",
},
"combined_regime_entry_exit_sensitivity": {
    "analysis.risk_off_core_buy_enabled",
    "analysis.entry_reclaim_close_enabled",
    "analysis.tp1_ema_trailing_stop_enabled",
    "analysis.regime_btc_7d_drop_pct",
    "analysis.regime_eth_7d_drop_pct",
    "analysis.regime_require_both_trend",
},
```

---

## 已知问题 / 技术债

### 1. tp1_ema_trailing_stop corner case（未修，低风险）
- **现象**：TP1 命中时若 4h K 线不足 20 根，`tp1_trailing_ema_stop_active` 在内存中被置为 True，但 EMA 计算返回 None；下次 update 时可能突然激活跟踪止损
- **位置**：`trade_state.py`（step_trade 内部），`paper_trader.py:454-457`
- **影响**：模拟盘偶发，不影响回测（回测有足够历史 K 线）
- **修法**：仅当 EMA 有效时才设 active=True

### 2. tp1_trailing_ema_stop_active 不持久化（未修）
- **现象**：`PaperTrade.tp1_trailing_ema_stop_active` 是 dataclass 字段，DB 里没有对应列；每次 update 重新加载 trade 时该字段重置为 False
- **影响**：TP1_HIT 状态的跟踪止损每次 update 都重新从零判断，行为与回测不完全一致
- **修法**：在 paper_trades 表加列 `tp1_trailing_ema_stop_active INTEGER NOT NULL DEFAULT 0`，或改为从事件日志推断

### 3. 幸存者偏差（未修，结构性问题）
- Binance 历史退市币未纳入 symbol master（`reports/2026-06-09/dynamic_master_full.json`）
- 所有回测结果偏乐观，无法量化偏差幅度

---

## 接下来可以做的实验（按优先级）

### A. 持仓时间过滤（需改代码）
- **假设**：部分止损单是入场后长期横盘最终慢慢跌破止损，而非快速止损
- **实验**：入场后 N 根 4h K 线内未触 TP1 则强制平仓（N 约 18～36）
- **需改**：`trade_state.py`（step_trade 加 bar_count 计数）+ `config.py` 加参数 + `abtest.py` 白名单 + `experiments.toml` 加实验定义

### B. 市值分层分析（无需改代码，直接跑）
- **目标**：确认亏损主要来自 altcoin 还是 large-cap，熊市是否应只做 large-cap
- **做法**：用 `--symbol-master-file` 分别传只含 large-cap 和只含 altcoin 的 master JSON，跑两段对比回测
- **large-cap 参考**：BTC/ETH/BNB/SOL/XRP/DOGE/ADA/AVAX/TRX/TON 等前 20

### C. 修 tp1_trailing_ema_stop_active 持久化（改代码）
- 加 DB 迁移，在 paper_trades 表加列，保证模拟盘行为与回测一致

---

## 常用命令

```bash
# A/B 实验（两段必须串行，不能同时跑）
python main.py abtest --experiment <实验名> \
  --dynamic-universe \
  --symbol-master-file reports/2026-06-09/dynamic_master_full.json \
  --start 2024-07-01 --end 2025-06-01 \
  --max-symbols 40 --allow-data-gaps --no-obsidian

# 回测
python main.py backtest-dynamic-universe \
  --symbol-master-file reports/2026-06-09/dynamic_master_full.json \
  --start 2024-07-01 --end 2025-06-01 \
  --max-symbols 40 --allow-data-gaps --no-obsidian

# 模拟盘手动触发（定时任务每天 20:05 自动跑）
python main.py daily --no-obsidian

# 只生成模拟盘报告（不跑扫盘）
python main.py paper report

# 确认定时任务是否正常
Get-ScheduledTask -TaskName "CryptoTrading_DailyPaperUpdate" | Get-ScheduledTaskInfo | Select-Object NextRunTime
```

---

## 重要约束

1. **SQLite 单写**：两段回测/实验不能并行，必须串行
2. **symbol master**：所有回测使用 `reports/2026-06-09/dynamic_master_full.json`（418 个币），不要用其他文件
3. **实验新增 dimension**：必须先在 `abtest.py` 的 `ALLOWED_OVERRIDE_PATHS` 里注册，否则运行时报错
4. **不要直接改 settings.toml 的 analysis 参数来做实验**：应通过 experiments.toml + abtest 命令，保持生产配置稳定
5. **daily_trend_required 已 reject**：不要在新实验里复用，浪费算力
