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

## 2026-06-06

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
