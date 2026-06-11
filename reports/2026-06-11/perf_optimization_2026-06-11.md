# 性能优化记录：Dynamic Universe 回测加速（2026-06-11）

## 背景与问题

Dynamic universe 回测（~418 symbols × 3 intervals）原始运行时间约 644 秒/次，严重影响迭代效率。
通过 5 轮 profiling 驱动的优化，将第二次及后续运行时间压缩到约 114 秒（约 3.5x 提速）。

基准测试窗口：2024-07-01 → 2025-01-01（约 540 bars，历史稳定期）

---

## Profiling 方法与工具

- Python 内置 `cProfile` + `pstats` 输出 cumtime 排序
- 针对热点函数逐一分析调用链
- 每轮优化后重跑基准测试验证实际收益

---

## 五轮优化详情

### Round 1 — `_closed_slice` 二分查找

**Commit:** `477c2ab`

**根因：** `_closed_slice` 在每个 bar 遍历已收盘列表时使用 O(n) 线性扫描。
在 418 symbols × 540 bars 的规模下，调用次数极高，累计开销显著。

**改动：** 将线性扫描替换为 `bisect.bisect_right` 二分查找，复杂度降至 O(log n)。

**实测：** benchmark 显示单次调用约 96x 加速。

---

### Round 2 — `batch_load_klines_cached` 单次 SQL IN 查询

**Commit:** `81965db`

**根因：** 原逻辑对 418 symbols × 3 intervals 逐一查询数据库，产生大量小型 SQL 请求，
I/O 往返次数高。

**改动：** 合并为单次 `SELECT ... WHERE symbol IN (...)` 批量查询，一次性加载全部 kline 数据。

**实测：** 加载阶段结构性改善，减少数据库往返开销。

---

### Round 3 — kline 字段类型优化（str → float/int）

**Commit:** `2a0be7d`

**根因：** `_normalise_kline` / `_normalise_kline_row` 将所有字段存储为字符串，
每次访问时在运算层做隐式转换，累计约 44 秒无效开销。

**改动：** 在 normalise 阶段直接将数值字段转换为 `float`/`int` 存储。

**实测：** 消除约 44 秒转换开销。

---

### Round 4 — per-symbol EMA 增量缓存

**Commit:** `c0b1f60`

**根因：** 每个 bar 计算 EMA 时从头重算整个序列（`ema_series`），
对 418 symbols 每 bar 均触发全量重算，理论开销约 26 秒。

**改动：** 引入 `ema_step` 增量更新，per-symbol 缓存最新 EMA 值，
每 bar 仅做一步增量计算，跳过全序列重算。

**实测：** 理论节省约 26 秒。

---

### Round 5 — `kline_fetch_ranges` 跳过冗余 API 请求（最大收益）

**Commit:** `84b8c55`

**根因（核心问题）：**
`fetch_klines_cached` 的缓存命中逻辑：比较"理论 bar 数（expected）"与"实际缓存数"，
因为 symbol 存在数据空洞，实际缓存数永远 < expected，
导致每次运行都触发 API 请求，即使数据已抓取过。
原始约有 200+ 次重复 Binance API 请求，累计约 327 秒。

**改动：** 新增 `kline_fetch_ranges` 数据库表，记录"已成功抓取过的 (symbol, interval, start, end) 范围"。
每次运行前查表，命中则直接跳过 API 请求，不再依赖 expected vs actual 的数量比较。

**实测：** 第一次运行 327s → 第二次及后续 114s，约 2.9x 单项提速。

---

## 基准测试结果汇总

| 阶段 | 运行时间 | 说明 |
|------|---------|------|
| 优化前（原始） | ~644s | 含 200+ 次重复 API 请求 |
| 优化前（基准窗口） | ~400s | 2024-07→2025-01，~540 bars |
| 优化后（首次运行） | ~327s | Round 5 前，仍触发 API |
| 优化后（第二次起） | ~114s | Round 5 后，命中 fetch_ranges 缓存 |
| **总提速** | **约 3.5x** | 相对基准窗口 400s |

---

## 剩余瓶颈与未完成工作

按 profiling 估算的剩余开销（第二次运行后）：

| 瓶颈 | 估算开销 | 状态 |
|------|---------|------|
| ATR 增量缓存 | ~15–20s | 未优化，逻辑与 EMA 类似 |
| `_quote_closes` / `_quote_volumes` | ~8s | float 优化后残余 |

**未运行的实验：**
- `tp1_ema20_trailing_stop` A/B 实验（代码已在 commit `2de9c5f`，待执行）

**待手动验证：**
- `risk_off_no_core_entry_reclaim` keep review：需确认 `_entry_reclaim_close_satisfied` 逻辑与模拟盘口径一致

---

## 测试验证

每轮优化后执行：
```
python main.py backtest --dynamic-universe \
  --symbol-master-file reports/2026-06-09/dynamic_master_full.json \
  --start 2024-07-01 --end 2025-01-01 \
  --max-symbols 40 --allow-data-gaps --no-obsidian
```

验证指标：运行时间、交易数、PF、Sharpe 与优化前一致（功能无回归）。
