---
created: 2026-06-18
tags:
  - crypto
  - trading-system
  - plan
period: 2026-06-13 -> 2026-07-03
---

# 三周开发与实验计划 2026-06-13 → 2026-07-03

三周观察窗口：`2026-06-13` 起，`2026-07-02` 完成复盘决策。
计划分三条主线并行推进：**运维稳定性**、**策略实验**、**工程基础设施**。

---

## 一、运维稳定性（4h 任务 + 每日 daily）

### 目标
在不破坏 `config_hash` 连续性的前提下，完成 daily 观察样本积累，确保 4h 任务稳定运行到 7/2 复盘。

### 任务清单

- [x] 完成 SQLite 观察 DB 全套基础设施（6 张表、WAL、UTC、foreign keys、30s timeout）
- [x] 实现 `db stability --days 5` 五维门槛（config_hash、重复 run、生命周期元数据、scan 完整性、snapshot 覆盖、数据库健康）
- [x] 实现 `db mark-run-failed` 命令（2026-06-17 stale run 已标记）
- [x] 添加 `.gitattributes` 固定 `settings.toml` 换行为 LF，防止 hash drift
- [x] 添加 pre-commit hook，冻结 `settings.toml` 到 2026-06-20（hook 到期后自动解冻）
- [x] 完成 `scripts/paper_4h_update.bat` 与 `scripts/install_4h_paper_task.ps1` 验收
- [x] 提前安装 `CryptoTrading_4H_PaperUpdate`（2026-06-18，`-RequiredStableDays 1`）
- [x] 添加企业微信任务完成通知（daily + 4h 两种模式）
- [ ] **验证 4h 任务首轮运行**（2026-06-19 00:10，检查 run_id、snapshot、report 是否生成）
- [ ] **完成 daily 5 天稳定窗口**（6/18–6/22，全部 success + 同一 config_hash `be7ec39ec21f6a83`）
- [ ] **7/2 每日观察**：每天确认 daily 20:05 和 4h 五轮均无异常，记录 dailylog

### 关键约束
- `settings.toml` 在 **2026-06-20 前禁止提交**（pre-commit hook 保护）
- 任何修改 `settings.toml` 的操作将重置稳定性窗口，需同步更新 TODO 预计安装日期
- 6/17 daily run 已标记 failed，新窗口从 **6/18 重新起算**，满 5 天需到 **6/22**

---

## 二、策略实验

### 已完成实验

#### 退出规则
- [x] **`max_holding_30x4h_no_tp1`**：30 根 4h 无 TP1 强退；近端 Net +27.28%、MDD 11.84%，结论 `candidate_keep_review`
- [x] **`max_holding_18x4h_no_tp1`**：18 根阈值；净收益最高但持仓太短，MDD 更差
- [x] **`max_holding_42x4h_no_tp1`**：42 根阈值；三窗口均改善、MDD 最低（近端 9.27%），结论 `candidate_keep_review`
- [x] **`risk_off_no_core_entry_reclaim_ema_stop_sensitive_max_holding_42`**（sensitive + 固定 42 根）：两段改善，近端 MDD 11.05%，结论 `retest`；95 笔 TIME_EXIT 复盘发现延迟赢家，触发条件退出研究
- [x] **`max_holding_42x4h_conditional`**（vs 无退出 baseline）：两段 Net +25–28pp，PF +0.3–0.5，但 baseline 太弱，结论 `retest`
- [x] **`max_holding_42_fixed_vs_conditional_sensitive`**（固定 vs 条件，3 窗口）：条件版 2/3 段变差，MDD 三段均更高，结论 **`reject_candidate`**；不部署 `max_holding_bars_conditional=true`
- [x] **`tp1_breakeven_stop`**：TP1 后保本止损；PF/净收益/止损率全面恶化，结论 `reject_candidate`
- [x] **`tp1_ema20_trailing_stop`**：TP1 后 EMA20 跟踪止损；方向改善但绝对值仍负，结论 `retest`

#### 入场规则
- [x] **`entry_reclaim_close`**：近端转正，两段 `candidate_keep_review`
- [x] **`risk_off_no_core_entry_reclaim`**：两段均正，`candidate_keep_review`
- [x] **`risk_off_no_core_entry_reclaim_ema_stop`**：两段净收益/PF/MDD 全面改善，`candidate_keep_review`；paper_trader.py 口径已对齐，生效于生产模拟盘
- [x] **`risk_off_no_core_entry_reclaim_ema_stop_sensitive`**：当前 production 配置（已写入 settings.toml）
- [x] **RECLAIM_PENDING 机会成本复盘**（2026-06-18）：8 次事件价格均低于 `entry_low`，无证据显示 `entry_reclaim_close` 导致明显机会成本

#### 选币/大盘过滤
- [x] **`daily_trend_required`**：近端熊市弱化效果，结论 `reject_candidate`
- [x] **`regime_sensitive`**（BTC -3%/ETH -5% 阈值）：已纳入 production sensitive combo
- [x] **`liquidity_50m`**：多段 walk-forward 方向改善但绝对值仍负，结论 `retest`
- [x] **`risk_off_no_core_buy`**、**`top_n_3`**、**`risk_off_no_core_top_n_3`**：结论均 `retest`
- [x] **`large_cap_only_risk_off`**（RISK_OFF 时只允许 BTC/ETH/BNB/SOL）：两段方向相反（牛市 +11pp，熊市 -6pp），结论 `retest`；在已有 altcoin 组合上叠加 large-cap RISK_OFF 入场反而拖累熊市，暂不 keep

### 计划中的实验（6/19–7/2）

#### 高优先级（直接支撑 7/2 复盘决策）

- [ ] **固定 42 根 keep review 决策**（2026-06-20 后）
  - 三个窗口均正向改善，是最平衡的时间退出候选
  - 决策前需看：是否与当前 production sensitive 组合叠加后 7/2 前仍 `candidate_keep_review`
  - 部署路径：修改 `settings.toml` → 重置稳定窗口 → 重新等 5 天

- [ ] **max_holding_42 + sensitive 第三时段补测**（`2023-07-01:2024-07-01`）
  - 现有两段均改善；第三段能确认结论独立于牛熊环境
  - 纯回测命令，无需改代码

#### 中优先级（为下一阶段准备）

- [ ] **EMA20 斜率过滤实验**（仅在固定 42 根 keep 后有意义）
  - 条件：42 根后且 `close > entry` 且 `close > EMA20` 且 `slope(EMA20, k) > 0`
  - 预期：过滤牛市漂移仓位，但需测试是否引入新的过拟合
  - 先做设计文档，确认思路后再实现

- [ ] **退市币幸存者偏差量化**
  - 目标：估算 dynamic universe 回测中因 current exchangeInfo 缺少历史退市币导致的偏差方向和幅度
  - 方法：比对 Binance 历史 `GET /api/v3/exchangeInfo` 快照（如有存档）或第三方退市记录
  - 输出：偏差程度报告，决定是否需要构建历史 symbol master

#### 低优先级（有空再做）

- [ ] **`top_n_3` 与 `entry_reclaim` 组合**：两者均单独 retest，组合可能互补
- [ ] **ATR 动态止损实验**：替代结构固定止损，减少噪音触发止损

---

## 三、工程基础设施

### 已完成

- [x] Dynamic Universe Backtest MVP（每日重建 universe，回放历史 K 线）
- [x] K 线无数据负缓存（避免新上市币反复请求）
- [x] A/B walk-forward 编排命令 `abtest-walk-forward`
- [x] A/B 多时段汇总报告 `abtest-summary`（含时段重叠分析、dynamic universe 偏差提示）
- [x] `SymbolMaster` JSON 保存/加载，支持固定 master 复用
- [x] `dynamic-symbol-master` 导出命令，已生成 `dynamic_master_full.json`（418 symbols）
- [x] Fixed baseline A/B override 支持（`baseline_overrides` 字段）
- [x] 实验结论索引升级（按 `experiment_id` 聚合，`review` 结论优先覆盖 `summary`）
- [x] 三周观察仪表 `observation-dashboard`（RECLAIM_PENDING、TP1 EMA trailing、持仓时长、RISK_OFF 摘要）

### 计划中

- [ ] **observation-dashboard 增强**（week 2）
  - 增加：`entry_reclaim` 拦截次数与后续价格追踪
  - 增加：TIME_EXIT 统计（已有多少单触发固定 42 根退出）
  - 增加：4h task run 健康摘要（每日几轮成功/失败）

- [ ] **experiment-index 进一步完善**（按需，week 2-3）
  - 目前已聚合；考虑增加"当前 production 设置使用了哪些实验的结论"高亮

---

## 四、关键时间节点

| 日期 | 事件 |
|---|---|
| **2026-06-19** | 4h 任务首轮运行（00:10），验证 snapshot/report 生成 |
| **2026-06-20** | pre-commit hook 解冻，settings.toml 可修改 |
| **2026-06-22** | daily 稳定窗口满 5 天（6/18–6/22，若全部 success） |
| **2026-06-23** | `ready_for_4h_task=true`（预计），正式确认 4h 任务运行正常 |
| **2026-07-02** | **三周 paper 复盘**：sensitive combo keep/调参/继续观察；fixed 42 根部署评估 |

---

## 五、7/2 复盘决策框架

复盘需回答的核心问题：

1. **entry_reclaim_close 效果**：RECLAIM_PENDING 后续有多少进入 entry zone？hit rate 如何？当前样本（仅 ONDOUSDT 8 次，全低于 entry_low）不够，需继续观察
2. **RISK_OFF 频率**：三周内触发几天？每次暂停了多少候选？这些候选后来表现如何？
3. **TP1 EMA trailing stop**：触发次数？平均比固定止损多拿了多少涨幅？
4. **持仓时长分布**：有多少仓位会超过 42 根 4h（168 小时）？这些仓位的后续走势？
5. **现有持仓结果**：WLDUSDT、ONDOUSDT 等当前持仓最终结果

**决策路径**：

```
sensitive combo 效果符合预期？
  ├─ 是 → keep：写入 settings.toml（已写入，确认即可）
  └─ 否 → 调参（放宽阈值？去掉某一项？）或继续观察

fixed 42 根要部署？
  ├─ 三段均改善，7/2 前无反例 → keep：写入 max_holding_bars_without_tp1=42
  └─ 有反例或新证据 → 继续 retest
  
注意：修改 settings.toml 会重置 db stability 窗口，
      需在 4h 任务确认稳定后再改，并接受约 5 天的新窗口积累期
```

---

*本计划基于 dailylog.md 和 git log 截至 2026-06-18 的状态自动整理。*
*每次实验完成后更新 TODO.md；重大决策节点更新本文件。*
