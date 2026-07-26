---
created: 2026-07-26 23:16:56 CST
tags:
  - crypto
  - trading-system
  - abtest
  - path-replay
experiment: atr_reclaim_0_35
verdict: retest_path_dependent
---

# atr_reclaim_0_35 关键交易路径复盘

## 研究框架

- 系统级目标：确认策略优势是否可解释、可复核，而不是继续叠加过滤器。
- 单一问题：`atr_reclaim_0_35` 的 variant-only 赢家是否来自真实的入场质量提升？
- 路线图位置：交易级归因之后、是否允许 keep 之前的人工路径复盘。
- 固定条件：不新增参数实验，不修改 `config/settings.toml`，只复盘既有 `110c51eef593` baseline 与 `54da79435459` variant。

## 白话结论

`atr_reclaim_0_35` 暂时应从 `candidate_keep_review_but_path_dependent` 降级为 `retest_path_dependent`。

原因不是它没价值，而是这 10 笔关键交易说明：改善并不只是“0.35 ATR reclaim 过滤掉弱入场”。更准确地说，它改变了组合路径，释放了部分仓位容量，让 variant 在 2025-07 到 2025-08 接入了一批强趋势赢家；同时它也错过了若干 baseline 里的高质量赢家。

特别关键的一点：5 笔 variant-only 赢家中，4 笔在 baseline 里同一计划是 `EXPIRED`，但 baseline 理论上更宽松。复盘发现，当 CFX、ENA、ADA 等机会出现时，baseline 多数时候已经有 5 个活跃仓位，容量满了；variant 因前面少进或晚进一些交易，组合路径不同，反而有空间接入这些赢家。

所以，当前不能说 `0.35 ATR` 本身已经被证明为稳定入场质量优势。它仍是候选线索，但下一步要研究的是“组合容量与机会排序”，而不是直接部署该阈值。

## 复盘对象

### Variant-only 新增赢家

| Symbol | Created | Entered | Net PnL | Net R | Opposite status |
|---|---|---|---:|---:|---|
| CFXUSDT | 2025-07-27T12:00 | 2025-07-27T20:00 | +390.71 | +3.34 | baseline EXPIRED |
| ALPINEUSDT | 2025-08-14T04:00 | 2025-08-15T08:00 | +336.86 | +2.85 | baseline EXPIRED |
| ENAUSDT | 2025-07-24T12:00 | 2025-07-24T16:00 | +325.06 | +2.90 | baseline EXPIRED |
| LINKUSDT | 2025-06-26T16:00 | 2025-06-28T16:00 | +288.84 | +2.87 | baseline EXPIRED |
| ADAUSDT | 2025-07-17T00:00 | 2025-07-17T08:00 | +270.86 | +2.44 | baseline NO_PLAN |

### Baseline 被错过赢家

| Symbol | Created | Entered | Net PnL | Net R | Opposite status |
|---|---|---|---:|---:|---|
| BTCUSDT | 2025-06-28T00:00 | 2025-06-28T04:00 | +323.68 | +3.16 | variant EXPIRED |
| UNIUSDT | 2025-07-16T04:00 | 2025-07-18T04:00 | +290.47 | +2.47 | variant NO_PLAN |
| LINKUSDT | 2025-07-13T08:00 | 2025-07-15T04:00 | +282.23 | +2.57 | variant NO_PLAN |
| UNIUSDT | 2025-06-08T00:00 | 2025-06-08T20:00 | +279.07 | +2.77 | variant EXPIRED |
| BONKUSDT | 2025-07-10T08:00 | 2025-07-12T00:00 | +262.57 | +2.44 | variant NO_PLAN |

## Reclaim 强度与后续路径

| 类型 | Symbol | Entry margin ATR | MFE R | MAE R | Bars to TP1 | Bars to TP2 |
|---|---|---:|---:|---:|---:|---:|
| variant-only winner | CFXUSDT | 0.73 | 4.65 | -0.28 | 9 | 9 |
| variant-only winner | ALPINEUSDT | 0.68 | 3.20 | -0.24 | 3 | 11 |
| variant-only winner | ENAUSDT | 0.47 | 3.41 | -0.23 | 8 | 19 |
| variant-only winner | LINKUSDT | 0.44 | 3.08 | -0.22 | 109 | 118 |
| variant-only winner | ADAUSDT | 0.82 | 2.63 | -0.22 | 5 | 6 |
| missed baseline winner | BTCUSDT | 0.03 | 3.56 | -0.72 | 76 | 79 |
| missed baseline winner | UNIUSDT 2025-07 | 1.95 | 2.65 | -0.37 | 1 | 21 |
| missed baseline winner | LINKUSDT 2025-07 | 0.07 | 2.80 | -0.09 | 17 | 18 |
| missed baseline winner | UNIUSDT 2025-06 | 0.10 | 2.93 | -0.25 | 10 | 11 |
| missed baseline winner | BONKUSDT | 0.34 | 3.31 | -0.19 | 5 | 20 |

解读：

- 支持点：5 笔 variant-only 赢家的入场 reclaim margin 都高于 `0.35 ATR`，且 MAE 均不深，后续路径整体顺畅。
- 反证点：missed baseline winners 里也有质量很好的交易，尤其 2025-07 的 UNIUSDT entry margin 达 `1.95 ATR`，但 variant 没有该计划。
- 混合点：BTCUSDT、LINKUSDT、2025-06 UNIUSDT、BONKUSDT 的 entry margin 低于或接近 0.35，却后续仍成为 TP2 赢家，说明 “低 reclaim margin = 低质量” 并不总成立。

## 容量与路径依赖

| 机会 | Baseline active positions | Variant active positions | 解释 |
|---|---:|---:|---|
| CFXUSDT variant entry | 5 | 4 | baseline 已满仓，variant 有容量 |
| ALPINEUSDT variant entry | 5 | 5 | 两边均满，但 variant 已包含 ALPINE，路径不同 |
| ENAUSDT variant entry | 5 | 4 | baseline 已满仓，variant 有容量 |
| LINKUSDT variant entry | 4 | 4 | 不完全由容量解释 |
| ADAUSDT variant entry | 5 | 5 | baseline 无同一计划，路径/排序差异 |
| BTCUSDT baseline entry | 4 | 1 | variant 有容量但未入场，说明 ATR 门槛或计划路径错过 |
| UNIUSDT 2025-07 baseline entry | 5 | 5 | 两边均满，路径/排序差异 |
| LINKUSDT 2025-07 baseline entry | 5 | 5 | 两边均满，路径/排序差异 |
| UNIUSDT 2025-06 baseline entry | 4 | 2 | variant 有容量但未入场，说明 ATR 门槛错过 |
| BONKUSDT baseline entry | 4 | 4 | 不完全由容量解释 |

这张表是复盘的核心：`atr_reclaim_0_35` 的结果不是一个纯 entry gate 的单点效果，而是一个组合路径效果。它改变早期入场集合，进而改变之后哪些机会能排进仓位容量。

## 事实、观察、假设、决策

事实：

- 5 笔 variant-only 赢家全部达到或超过 `0.35 ATR` reclaim margin。
- 5 笔 missed baseline winners 也全部是 TP2 赢家，合计净 PnL `+1438.01 USDT`。
- CFX、ENA 等 variant-only 机会出现时，baseline 已达到 `max_active_positions=5`。
- BTCUSDT 与 2025-06 UNIUSDT 在 variant 中有容量但仍过期，说明 stricter reclaim 本身也会错过赢家。

观察：

- `0.35 ATR` 对 variant-only 赢家有解释力，但解释不完整。
- 近端窗口收益改善更像“路径换仓”而不是“同一批机会质量普遍提升”。
- 被错过的 baseline 赢家质量并不差，不能简单归类为应该过滤掉的弱机会。

假设：

- `0.35 ATR` reclaim margin 可能有助于等待更强确认，但它与组合容量、机会排序、已有持仓占用强耦合。
- 近端窗口的改善可能主要来自 2025-07 到 2025-08 的趋势簇和容量释放，而不是稳定跨阶段的单变量优势。

决策：

- `atr_reclaim_0_35` 当前降级为 `retest_path_dependent`。
- 不部署，不修改 `settings.toml`。
- 不继续叠加过滤器。
- 下一步研究方向不应是调更高/更低 ATR reclaim，而应先复盘组合容量和机会排序：当多个机会同时出现时，系统为什么选择 A 而错过 B。

## 下一步

优先做一个非参数复核报告：`capacity_and_opportunity_order_review`。

目标不是改规则，而是回答：

1. `max_active_positions=5` 是否导致高质量机会被低质量长持仓占住？
2. variant 的赢家是否只是因为前面少进了一些仓位，从而偶然腾出容量？
3. 如果只看“同一时点候选机会池”，系统的排序是否能把 CFX/ENA/ADA 这类赢家排在 BTC/UNI/LINK/BONK 之前？

通过标准：

- 如果 winner replacement 有清晰质量差异，才允许继续研究容量/排序规则。
- 如果赢家只是行情簇偶然，`atr_reclaim_0_35` 保持 `retest`。
- 如果证据混合，继续冻结配置，等更多独立窗口或 paper 机会验证。
