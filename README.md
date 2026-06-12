# CryptoTradingSystem MVP

本项目是一个本地加密货币交易研究系统。第一版只使用公开行情，不需要 API Key，不会自动实盘下单。

## 当前已实现

- Binance USDT 现货市场扫描
- 稳定币、杠杆币、低流动性币过滤
- 1h / 4h / 1d K 线获取
- EMA、RSI、MACD、ATR、成交量变化计算
- 5 个候选币交易计划生成
- 入场区间、止损、止盈、风险收益比、风险提示
- 人工可验证证据：Binance/TradingView 链接、指标表、推导公式、最近 4h K线表
- 数据交叉验证：Binance + CoinGecko 自动对照，CoinMarketCap API Key 可选对照
- DATA_OK / DATA_WARNING / DATA_ERROR 标记和多数据源对照表
- 本地 SVG 证据图：K线 + 入场区 + 止损 + TP1 + TP2
- 单币复核命令
- 模拟盘观察列表和虚拟持仓
- 模拟盘状态更新：WATCHING、ENTERED、TP1_HIT、STOPPED、CLOSED、INVALIDATED
- 模拟盘旧计划归档：新计划会替换同币种未入场旧计划
- 模拟盘事件日志：WATCHLIST_ADDED、ENTERED、TP1_HIT、STOPPED、CLOSED、INVALIDATED、ARCHIVED
- 模拟盘复盘统计：入场数、已结束数、胜率、TP1 命中率、已实现/未实现 PnL
- 模拟盘报告输出到项目和 Obsidian
- SQLite 扫描记录
- Markdown 报告按日期输出到项目 `reports/YYYY-MM-DD/` 和 Obsidian `Reports/YYYY-MM-DD/`

## 运行

日常完整流程：

```powershell
python main.py daily
```

`daily` 会自动执行：

1. 重新扫描大盘；
2. 生成市场扫描报告；
3. 把最新候选加入模拟盘；
4. 更新所有模拟盘状态；
5. 生成模拟盘报告。

以上步骤共享一个 SQLite `run_id`，运行状态记录在 `runs` 表；daily 还会生成三周观察 dashboard。

初始化或检查数据库：

```powershell
python main.py db init
python main.py db status
```

结构化复盘和导出：

```powershell
python main.py paper db-summary
python main.py paper db-events --limit 100
python main.py paper db-export --output-dir exports
```

为后续 4h 更新准备的单次循环命令：

```powershell
python main.py paper cycle --run-type paper_4h_update --account demo
```

该命令只更新已有 paper plans 并生成报告/dashboard，不运行 scan，也不从 scan 创建新计划。Windows 4h 计划任务必须等 SQLite daily_full 连续稳定运行 5 天后再启用。

检查 5 天门槛：

```powershell
python main.py db stability --days 5
```

只有输出 `ready_for_4h_task: true` 后，才在管理员 PowerShell 中安装任务：

```powershell
powershell -ExecutionPolicy Bypass -File scripts\install_4h_paper_task.ps1
```

导入最新候选时，系统会自动归档同币种的旧 `WATCHING` 计划。已经入场的 `ENTERED` / `TP1_HIT` 持仓不会被替换。

只想盘中更新已有模拟仓位：

```powershell
python main.py paper update
python main.py paper report
```

检查 API、数据库和输出目录：

```powershell
python main.py doctor
```

`doctor` 会检查 Binance、CoinGecko、CoinMarketCap API Key、SQLite 数据库、项目报告目录和 Obsidian 目录。CoinMarketCap 未配置 API Key 时会显示 `SKIP`，不是错误。

单独扫描大盘：

```powershell
python main.py scan
```

`scan` 和 `daily` 会在运行中输出进度，例如正在加载 Binance 行情、分析第几个交易对、检查 CoinGecko/CoinMarketCap、写入报告。

只写项目报告，不写 Obsidian：

```powershell
python main.py scan --no-obsidian
```

指定候选数量：

```powershell
python main.py scan --top 10
```

单独复核某个币：

```powershell
python main.py verify --symbol ZECUSDT
```

`verify` 报告会包含两部分：

- 被复核币种的详细证据：图表、指标、推导、最近 4h K线。
- 同步跑出的当前大盘 5 个候选币对照表。

把某次扫描结果加入模拟盘：

```powershell
python main.py paper add-from-scan --scan-id 644f2c98e0a5
```

如果不指定 `--scan-id`，默认使用最新的大盘扫描：

```powershell
python main.py paper add-from-scan
```

用当前价格更新模拟盘状态：

```powershell
python main.py paper update
```

生成模拟盘报告：

```powershell
python main.py paper report
```

模拟盘报告会包含：

- 当前观察与持仓
- 已结束交易
- 复盘统计
- 每笔交易生命周期时间线

## 输出

- 本地数据库：`data/crypto_trading.db`
- 项目报告：`reports/YYYY-MM-DD/market_scan_YYYY-MM-DD_vN.md`
- 单币复核报告：`reports/YYYY-MM-DD/verify_<symbol>_YYYY-MM-DD_vN.md`
- 模拟盘报告：`reports/YYYY-MM-DD/paper_report_YYYY-MM-DD_<account>_vN.md`
- 项目图表：`reports/YYYY-MM-DD/charts/<scan_id>_<symbol>.svg`
- Obsidian 报告：`D:/MyNotebook-Obsidian/CryptoTradingSystem/Reports/YYYY-MM-DD/market_scan_YYYY-MM-DD_vN.md`
- Obsidian 单币复核报告：`D:/MyNotebook-Obsidian/CryptoTradingSystem/Reports/YYYY-MM-DD/verify_<symbol>_YYYY-MM-DD_vN.md`
- Obsidian 模拟盘报告：`D:/MyNotebook-Obsidian/CryptoTradingSystem/Reports/YYYY-MM-DD/paper_report_YYYY-MM-DD_<account>_vN.md`
- Obsidian 图表：`D:/MyNotebook-Obsidian/CryptoTradingSystem/Reports/YYYY-MM-DD/charts/<scan_id>_<symbol>.svg`

Obsidian `CryptoTradingSystem` 根目录用于保留开发计划、实现日志和后续手写交易笔记；脚本自动生成的报告统一进入 `Reports/YYYY-MM-DD/`。
同一天多次运行会自动生成 `v1`、`v2`、`v3` 等版本号；原始 `scan_id` 会保留在报告正文和图表文件名中，便于回溯数据库记录。

## 人工验证方式

每个候选币报告会包含：

- Binance 交易页链接
- TradingView 图表链接
- CoinGecko / CoinMarketCap 搜索链接
- Binance / CoinGecko / CoinMarketCap 多数据源对照表
- 数据状态：
  - `DATA_OK`：外部来源与 Binance 在阈值内一致
  - `DATA_WARNING`：价格、24h 涨跌或映射需要人工复核
  - `DATA_ERROR`：出现重大差异或映射失败，候选会降级为只观察
- 当前价、24h/7d 涨跌、EMA、RSI、ATR、支撑位等指标证据表
- 入场区间、止损、TP1、TP2 的推导公式
- 最近 10 根 4h K线明细
- 本地 SVG 图表，画出入场区、止损和止盈线

## 风险声明

报告用于研究和模拟盘，不是确定收益或自动实盘下单指令。所有交易计划都必须人工复核，并控制单笔风险。
