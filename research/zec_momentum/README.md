# ZEC 短线顺势研究

本目录为 CryptoTrading 的独立研究入口。复用系统指标，不调用现货回测默认 runner，不读取生产 SQLite、现有 reports、模拟盘或 Obsidian 状态。

先读 [PROTOCOL.md](PROTOCOL.md)。封存起点固定为北京时间 2026-06-23 00:00，本次额外保留全部 2026 年数据，只处理 2023-12 预热和 2024–2025 评估数据。

从项目根目录运行（Python 3.12+）：

```powershell
python -m pytest tests/test_zec_momentum_data.py tests/test_zec_momentum_engine.py tests/test_zec_momentum_report.py
python -m research.zec_momentum.run --cache-dir C:/isolated/zec-cache --output-dir C:/isolated/zec-results --download
```

缓存和输出路径必须显式给出；不使用默认线上目录。原始 ZIP、SHA256、每个来源 URL、实际时间边界和代码哈希会随运行记录保存。下载仅使用 Binance 官方已冻结月份归档。

评估是连续数量、固定费用/滑点情景下的永续方向研究，未重建历史下单最小量、tick size、盘口、部分成交和完整强平制度；不能当作已经验收的实盘策略。2025 年验证结果不能用于本轮再次选参。

输出：`report.md`、`summary.json`、`trades.csv`、`monthly.csv`、`equity.csv`、`data_manifest.json`、`run_manifest.json`。所有候选和成本情景均保留；不自动推荐最高收益组。
