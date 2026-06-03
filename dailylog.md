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

## 2026-06-03

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
