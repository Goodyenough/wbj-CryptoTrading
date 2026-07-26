---
created: 2026-07-26 19:08:04 CST
tags:
  - crypto
  - trading-system
  - abtest
  - attribution
experiment: atr_reclaim_0_35
verdict: candidate_keep_review_but_path_dependent
---

# atr_reclaim_0_35 交易级归因复核

## 研究框架

- 系统级目标：确认当前策略优势是否可解释、可复核，而不是继续叠加过滤器。
- 单一问题：`atr_reclaim_0_35` 的改善，来自广泛过滤亏损，还是少数赢家/路径偶然？
- 路线图位置：`atr_reclaim` 阈值敏感性之后、是否允许进入 keep review 之前的交易级归因。
- 固定条件：不修改 `config/settings.toml`；只复核已有 dynamic-universe A/B 报告。

## 白话结论

`atr_reclaim_0_35` 仍然是一个有价值的候选，但还不能部署。

它的改善不是来自共同交易普遍变好。两段合并后，共同交易反而小幅变差 `-43.72 USDT`；主要改善来自变体独有交易 `+3184.11 USDT`，也就是更严格的 reclaim 门槛改变了实际成交集合，让系统晚一点、确认更强以后才入场，捕捉到了一批新的 TP2 赢家。

早期窗口的改善比较健康：top5 正贡献只占该窗口总改善的 `49.0%`，不是单一赢家撑起来。近端窗口的改善更脆弱：top3 正贡献达到 `1052.63 USDT`，超过该窗口总改善 `627.53 USDT`，说明同时存在大量负抵消，净改善更依赖 2025-07 到 2025-08 的少数新增赢家。

因此结论是：保留 `atr_reclaim_0_35` 为 `candidate_keep_review`，但标记为 `path_dependent`。下一步不部署、不叠加新过滤器，优先做交易路径人工复盘，确认这些新增赢家是否符合可解释的入场质量提升。

## 输入报告

| 窗口 | Baseline report | Variant report | A/B report |
|---|---|---|---|
| 2024-07-01 -> 2025-06-01 | `reports/2026-07-26/backtest_dynamic_universe_2024-07-01_2025-06-01_v13.md` | `reports/2026-07-26/backtest_dynamic_universe_2024-07-01_2025-06-01_v14.md` | `reports/2026-07-26/abtest_dynamic_universe_atr_reclaim_0_35_2024-07-01_2025-06-01_v1.md` |
| 2025-06-01 -> 2026-06-01 | `reports/2026-07-26/backtest_dynamic_universe_2025-06-01_2026-06-01_v14.md` | `reports/2026-07-26/backtest_dynamic_universe_2025-06-01_2026-06-01_v15.md` | `reports/2026-07-26/abtest_dynamic_universe_atr_reclaim_0_35_2025-06-01_2026-06-01_v1.md` |

匹配口径：以 `symbol + created` 匹配共同交易；未匹配交易分为 baseline-only 和 variant-only。由于 ATR reclaim 会改变入场确认路径，未匹配并不等于同一机会完全消失，只表示最终闭合交易集合发生变化。

## 总体归因

| 口径 | 贡献 | 解释 |
|---|---:|---|
| removed baseline-only | +594.76 USDT | 移除了部分 baseline 交易，净效果小幅正向 |
| added variant-only | +3184.11 USDT | 主要改善来源，来自变体新增闭合交易 |
| common trade delta | -43.72 USDT | 两边都存在的交易没有改善，反而小幅变差 |
| 合计 | +3735.15 USDT | 约等于两段 A/B 净 PnL 改善合计 |

| 集中度 | 数值 |
|---|---:|
| 正贡献记录数 | 110 |
| 负贡献记录数 | 102 |
| Top3 正贡献 | 1052.63 USDT，占总改善 28.2% |
| Top5 正贡献 | 1688.69 USDT，占总改善 45.2% |

解读：合并口径不是一两笔交易撑起全部改善；但改善高度集中在 variant-only 新增交易，说明机制不是“广泛过滤亏损后共同交易变好”，而是“更强 reclaim 条件改变成交集合并带来新增赢家”。

## 分窗口证据

### 2024-07-01 -> 2025-06-01

| 指标 | Baseline | Variant | 变化 |
|---|---:|---:|---:|
| closed trades | 76 | 78 | +2 |
| win rate | 38.16% | 48.72% | +10.56 pp |
| Profit factor | 0.95 | 1.62 | +0.67 |
| Sharpe | -0.01 | 0.93 | +0.94 |
| Max drawdown | 16.59% | 14.95% | -1.64 pp |
| Net return | -2.09% | 18.20% | +20.29 pp |

交易级拆分：

| 分类 | 数量 | 净贡献 |
|---|---:|---:|
| common trades | 28 | +38.57 USDT |
| baseline-only removed | 48 | +867.52 USDT |
| variant-only added | 50 | +2201.53 USDT |
| 总改善 | - | +3107.62 USDT |

集中度：

| 指标 | 数值 |
|---|---:|
| Top3 正贡献 | 936.10 USDT，占改善 30.1% |
| Top5 正贡献 | 1524.19 USDT，占改善 49.0% |
| variant-only TP2 closed | 12 |
| baseline-only stop | 46 |

主要正贡献：

| 分类 | Symbol | Created | Contribution |
|---|---|---|---:|
| added_variant | ONEUSDT | 2024-12-05T16:00:00+00:00 | +324.04 |
| added_variant | BTCUSDT | 2024-11-04T04:00:00+00:00 | +312.02 |
| added_variant | WLDUSDT | 2024-11-24T20:00:00+00:00 | +300.04 |
| added_variant | PEPEUSDT | 2024-11-13T04:00:00+00:00 | +295.18 |
| added_variant | TAOUSDT | 2025-05-07T04:00:00+00:00 | +292.91 |

月度差异：

| 月份 | Delta |
|---|---:|
| 2024-07 | +307.65 |
| 2024-09 | +660.33 |
| 2024-10 | -315.87 |
| 2024-11 | +1374.01 |
| 2024-12 | +353.93 |
| 2025-04 | +409.35 |
| 2025-05 | +247.49 |

结论：早期窗口改善比较分散，既移除了一批 baseline 止损，也新增了一批 TP2 赢家。它不是单笔偶然，但 2024-11 的赢家簇贡献很大，需要承认存在行情阶段依赖。

### 2025-06-01 -> 2026-06-01

| 指标 | Baseline | Variant | 变化 |
|---|---:|---:|---:|
| closed trades | 57 | 53 | -4 |
| win rate | 40.35% | 45.28% | +4.93 pp |
| Profit factor | 1.11 | 1.31 | +0.20 |
| Sharpe | 0.26 | 0.60 | +0.34 |
| Max drawdown | 20.75% | 15.27% | -5.48 pp |
| Net return | 3.11% | 9.33% | +6.22 pp |

交易级拆分：

| 分类 | 数量 | 净贡献 |
|---|---:|---:|
| common trades | 23 | -82.29 USDT |
| baseline-only removed | 34 | -272.76 USDT |
| variant-only added | 30 | +982.58 USDT |
| 总改善 | - | +627.53 USDT |

集中度：

| 指标 | 数值 |
|---|---:|
| Top3 正贡献 | 1052.63 USDT，占改善 167.7% |
| Top5 正贡献 | 1612.33 USDT，占改善 256.9% |
| variant-only TP2 closed | 5 |
| baseline-only TP2 missed by removal | 5 |

主要正贡献：

| 分类 | Symbol | Created | Contribution |
|---|---|---|---:|
| added_variant | CFXUSDT | 2025-07-27T12:00:00+00:00 | +390.71 |
| added_variant | ALPINEUSDT | 2025-08-14T04:00:00+00:00 | +336.86 |
| added_variant | ENAUSDT | 2025-07-24T12:00:00+00:00 | +325.06 |
| added_variant | LINKUSDT | 2025-06-26T16:00:00+00:00 | +288.84 |
| added_variant | ADAUSDT | 2025-07-17T00:00:00+00:00 | +270.86 |

主要负抵消：

| 分类 | Symbol | Created | Contribution |
|---|---|---|---:|
| removed_baseline | BTCUSDT | 2025-06-28T00:00:00+00:00 | -323.68 |
| removed_baseline | UNIUSDT | 2025-07-16T04:00:00+00:00 | -290.47 |
| removed_baseline | LINKUSDT | 2025-07-13T08:00:00+00:00 | -282.23 |
| removed_baseline | UNIUSDT | 2025-06-08T00:00:00+00:00 | -279.07 |
| removed_baseline | BONKUSDT | 2025-07-10T08:00:00+00:00 | -262.57 |

月度差异：

| 月份 | Delta |
|---|---:|
| 2025-06 | -60.84 |
| 2025-07 | +470.70 |
| 2025-08 | +441.17 |
| 2025-09 | -123.65 |
| 2025-10 | -25.80 |
| 2026-01 | -18.96 |
| 2026-04 | +314.18 |
| 2026-05 | -369.27 |

结论：近端窗口改善更依赖少数新增赢家，且同时错过了一批 baseline 赢家。虽然报告级 MDD 明显改善，但交易级净收益来源的稳定性弱于早期窗口。

## MDD timing 复核

闭合交易 PnL 代理口径显示：

| 窗口 | Baseline closed-PnL MDD | Variant closed-PnL MDD | Peak -> Trough |
|---|---:|---:|---|
| 2024-07-01 -> 2025-06-01 | 1361.76 | 1523.16 | 2024-12 -> 2025-04 |
| 2025-06-01 -> 2026-06-01 | 2076.80 | 1337.68 | 2025-07 -> 2026-01 |

说明：这是按已结束交易创建时间排序的 closed-PnL 代理，不等同于回测报告里的权益曲线 MDD。报告级 MDD 使用真实权益曲线、开放持仓和 intrabar 路径；本节只用于定位交易簇和时间段。

关键观察：

- 早期窗口报告级 MDD 改善，但 closed-PnL 代理 MDD 反而略大，说明改善可能与开放持仓路径、权益峰值位置和 intrabar 处理有关，不能只看闭合交易净额。
- 近端窗口 closed-PnL 代理和报告级 MDD 都改善，主要是 2025-07 后权益峰值更高、后续回撤被压低。
- 两段 MDD timing 都提示：`atr_reclaim_0_35` 改变的是路径和成交集合，而不是单纯降低每笔亏损幅度。

## 事实、观察、假设、决策

事实：

- 两段 A/B 样本均充分，且 `atr_reclaim_0_35` 报告级净收益、PF、Sharpe、MDD、stop rate 均改善。
- 合并后共同交易贡献为 `-43.72 USDT`，不是优势来源。
- 合并后最大贡献来自 variant-only 交易 `+3184.11 USDT`。

观察：

- 早期窗口改善较分散，近端窗口更集中。
- 近端窗口 top3 正贡献超过该窗口净改善，存在明显抵消项。
- variant-only 的 TP2 赢家是改善核心，但 variant-only 同时也新增较多止损。

假设：

- `0.35 ATR` reclaim margin 可能让系统避开弱 reclaim，等待更强确认后再入场。
- 该优势可能依赖趋势启动阶段的新增赢家，而不是稳定降低所有交易亏损。

决策：

- `atr_reclaim_0_35` 保留为 `candidate_keep_review_but_path_dependent`。
- 不部署，不修改 `settings.toml`。
- 不叠加新的过滤器。
- 下一步先人工复盘 top variant-only winners 与 missed baseline winners，确认它们是否真是 reclaim 质量差异，而不是 dynamic universe 排序/行情簇偶然。

## 下一步

1. 人工复盘近端窗口 top5 variant-only winners：CFXUSDT、ALPINEUSDT、ENAUSDT、LINKUSDT、ADAUSDT。
2. 人工复盘近端窗口 top5 missed baseline winners：BTCUSDT、UNIUSDT、LINKUSDT、UNIUSDT、BONKUSDT。
3. 对比这些交易在触发时的 `reclaim_margin_atr`、entry zone、market regime、TP1/TP2 路径，判断 `0.35 ATR` 是否有稳定可解释的质量优势。
