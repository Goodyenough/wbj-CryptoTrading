# Baseline 退出后 1R 恢复率诊断协议 v1

冻结时间：2026-10-14 00:27 +08:00
Taskboard：`CRYPTOTRADIN-128`

## 系统级目标

判断老 baseline 在正常成本后盈利能力不足时，下一步应优先研究退出匹配，还是停止优化该 baseline 并转向新的入场机制；避免把“最终止损”直接解释成“止损参数有问题”。

## 单一问题

冻结的 repaired `confirmation_close` baseline 非容量 `STOPPED` 交易，从 `exit_bar + 1` 开始，是否在两个已烧窗口内经常于 20、40、80 根 4h K 线内重新达到原入场方向 `+1R`，足以把“退出可能过早”保留为可复核机制？

## 路线位置

本诊断位于 baseline 三道归因闸门与 MAE/MFE 二级路径归因之后，是老 baseline 的最后一个分流诊断。它不是止损参数实验，也不属于 `CRYPTOTRADIN-127` 的 B 入场 `reclaim_strength` 研究。

## 事实、观察、假设与决定

### 事实

- 早窗非容量组 raw/net 为 `+33.42 / -134.63 USDT`；近窗为 `-125.90 / -248.92 USDT`。
- 近窗 23 笔非容量亏损中，2 笔带入场样标签、4 笔带退出样标签，其余 17 笔为 `other_or_inconclusive`。
- 现有 MAE/MFE 包含退出 bar，4h OHLC 无法判定退出 bar 内 high/low 的先后。
- Claude 文件化讨论已经定义退出后恢复率，但此前没有执行脚本、报告或 Taskboard 任务。

### 观察

多数近窗 `unknown` 没有形成足够正向延伸，也不是入场后立即单边恶化；“慢性无跟随”是候选解释，但缺少退出后的路径证据。

### 假设

- 若两个窗口的恢复率稳定偏高，退出可能过早的必要条件成立。
- 若两个窗口的恢复率稳定偏低，更支持缺少后续动能或毛优势不足。

### 决定

只做退出后路径诊断，不修改 stop、TP、持仓时长、入场规则或生产配置；结果只负责分流，不直接生成生产候选。

## 冻结输入与边界

- 交易输入：`reports/2026-10-10/baseline_trade_path_attribution_2026-10-10_v1.csv`。
- replay 输入：
  - `reports/2026-10-09/atr_fixed_history/2024-07-01_confirmation_close_baseline.json`
  - `reports/2026-10-09/atr_fixed_history/2025-06-01_confirmation_close_baseline.json`
- K 线输入：本地只读 `data/crypto_trading.db` 的 Binance `4h` `kline_cache`。
- 样本窗口：`[2024-07-01, 2025-06-01)` 与 `[2025-06-01, 2026-06-01)`。
- 数据预算：早窗禁止读取 `2025-06-01T00:00:00Z` 及以后；近窗禁止读取 `2026-06-01T00:00:00Z` 及以后，不消耗 2026-06 之后数据。
- 主样本：`capacity_group=non_capacity AND status=STOPPED`；近窗 17 笔 `other_or_inconclusive` 亏损单列。
- 容量竞逐 `STOPPED` 单列；非容量 `CLOSED` 仅保留为描述性锚，不作为恢复率主分母。

## 指标定义

- `R = abs(entry_price_filled - stop_loss)`；当前样本均为多头。
- 恢复目标：`entry_price_filled + 1R`；辅助目标为 `entry_price_filled + 2R`。
- 起点：严格从 `exit_bar + 1` 开始，退出 bar 永不进入恢复路径。
- horizon：`K={20,40,80}` 根 4h bar；主口径 `K=40`，三者全部报告。
- 同币再次入场：恢复窗口截断到下一次入场 bar 之前。
- 窗口结束、同币再次入场或 K 线缺口导致不足 K 根时，该交易在对应 K 标记为右删失，不记作“未恢复”。
- 主恢复率：仅在具有完整 K 根、连续 K 线的交易中，`high >= entry + 1R` 的比例；同时报告删失数量和删失前已观察到的恢复事件。
- 区间：Wilson 95% 比例区间；因交易存在时间聚类，区间只作不确定性诊断，不当作独立同分布证明。
- 集中度：报告移除单一 symbol 和单一退出 ISO week 后的 K40 恢复率范围。
- 市场锚：报告同一 post-exit horizon 的 BTC/ETH 中位累计收益，并比较市场顺风与非顺风子组；不能把整体反弹误当原信号仍有效。

## 预声明裁决

### 支持“退出可能过早”的必要条件

- 两个窗口主口径 `recover_1R_40 >= 40%`；
- 不是只在 K80 才成立；
- Wilson 区间、移除头部 symbol/week 和市场顺风分层不显示结论由少数样本或整体反弹独占驱动。

该结果只允许形成一张退出匹配单变量实验卡片并申请批准，不允许直接修改退出规则。

### 支持“缺少后续动能 / 毛优势不足”

- 两个窗口主口径 `recover_1R_40 <= 30%`；
- K20/40/80 给出一致的低恢复解释；
- 集中度检查不把任一窗口推过 40%。

### 证据不足

任一条件成立即判证据不足：

- 任一窗口 K40 落在 `(30%, 40%)`；
- 两窗口落入不同决策区；
- 结果只在 K80 出现；
- 完整 K40 样本或 `unknown` 子集不足以判断；
- 结论依赖单一 symbol/week、市场整体反弹或高删失；
- current-survivor 幸存者偏差使结果不能外推。

## 输出与停止条件

- `reports/2026-10-14/baseline_post_exit_recovery_v1/trades.csv`
- `reports/2026-10-14/baseline_post_exit_recovery_v1/summary.json`
- `reports/2026-10-14/baseline_post_exit_recovery_v1/report.md`

完成后更新实验账本、当前策略文档、Obsidian 实验日志、Taskboard 和工程审计日志；停下等待用户裁决，不自动启动退出实验或 `CRYPTOTRADIN-127`。
