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

## 2026-06-11

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
