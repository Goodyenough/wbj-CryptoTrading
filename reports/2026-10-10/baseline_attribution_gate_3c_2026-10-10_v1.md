# Baseline 归因闸门 3-C：当前存续币条件成本栈与亏损机制诊断

> **CONDITIONAL / NON-GENERALIZABLE**：本报告只回答冻结 current-survivor symbol master 内发生了什么。它不代表完整历史市场，不替代 point-in-time 正式闸门 3，也不能证明未来 expectancy。

## 白话结论

在排除入场时点存在容量竞逐的交易后，baseline 在两个窗口都没有显示出稳健的成本前优势：早窗 63 笔交易按原始价格计算只赚 33.42 USDT，平均每笔 0.53 USDT，滑点和手续费合计 168.05 USDT 后变成亏损 134.63 USDT；近窗 38 笔交易在计算费用前已经亏损 125.90 USDT，成本再把亏损扩大到 248.92 USDT。

所以，“成本太高”只能解释早窗为什么从接近打平变成亏损，不能解释近窗的全部亏损。更根本的问题是：非容量竞逐组的毛优势本来就接近零或为负，且没有找到跨窗口稳定的 regime、持仓时长或退出机制结构。

全体 131 笔闭合交易合计仍净赚 417.27 USDT，是因为 30 笔容量竞逐组贡献了 800.81 USDT，抵消了非容量组的 383.54 USDT 亏损。这个容量组是既有排名和五仓路径选出来的结果，不是可验证反事实，不能把它解释成“容量规则创造了 800.81 USDT”。

本闸门裁决为 **`B_conditional_no_robust_gross_edge`**：在当前存续币条件样本内，没有证据支持 baseline 存在稳健、可单变量映射的毛优势；不形成参数实验卡片，不修改生产配置。这里的 B 是“没有得到可靠优势证据”，不是统计证明真实 expectancy 必然小于零。

## 研究问题与预声明出口

- 系统目标：解释当前存续 Binance Spot USDT 币条件下，baseline 净收益由 gross edge、fee、slippage、capacity path 或可复现执行机制中的哪一层主导。
- 单一问题：冻结币池、窗口、执行语义和成本后，是否存在跨窗口、非容量路径驱动、可映射单变量的稳定亏损机制。
- 路线图位置：正式闸门 2 因幸存者偏差裁决 C；用户明确批准缩窄问题后，另开 `CRYPTOTRADIN-125`。正式 `CRYPTOTRADIN-124` 继续由 `CRYPTOTRADIN-89` 阻塞。
- 支持 A：同一机制在两个窗口方向一致，且不只由容量竞逐组驱动。
- 拒绝 B：gross edge 接近零或为负，且没有稳定可复现结构。
- 证据不足 C：结果随窗口/容量组翻转，或关键字段无法可靠重建。

## 冻结口径

- Venue：Binance Spot USDT。
- Symbol universe：冻结 current-master，source=`Frozen 2026-07-26 daily membership (survivorship biased)`，master count=285；历史已退市币缺失。
- 窗口：`[2024-07-01, 2025-06-01)` 与 `[2025-06-01, 2026-06-01)`。
- Timeframe / entry：4h，`confirmation_close`，退出从下一根 bar 开始生效。
- 风险与容量：单笔风险 1%，总活跃风险 5%，最多 5 个持仓，无杠杆。
- 费用与滑点：maker 4 bps、taker 10 bps、entry slippage 5 bps、stop slippage 10 bps；沿用 Gate 1 冻结实现。
- 样本：134 笔入场，131 笔完整闭合，3 笔右删失；交易期 4h gap=0。全部交易仍带 `survivorship_suspect`。

## 成本栈定义

逐笔字段关系已经核对：

```text
raw_price_pnl = gross_pnl + slippage_cost
after_slippage_gross = gross_pnl
fees = entry_fee + exit_fee
net_pnl = gross_pnl - fees
```

`gross_pnl` 已经使用 filled entry/exit，因此滑点已经包含在 gross 与 raw price P&L 的差中，不能再次从 net 重复扣除。

## 成本栈结果

| 窗口 | 分组 | N | 胜率 | raw price P&L | slippage | after-slippage gross | fees | net P&L | PF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 早窗 | all closed | 80 | 45.00% | +772.43 | 102.99 | +669.44 | 101.44 | +568.00 | 1.1198 |
| 早窗 | execution-clean conditional | 63 | 41.27% | +33.42 | 84.91 | -51.49 | 83.14 | -134.63 | 0.9661 |
| 早窗 | capacity-contested | 17 | 58.82% | +739.01 | 18.07 | +720.93 | 18.30 | +702.63 | 1.9103 |
| 近窗 | all closed | 51 | 41.18% | +8.29 | 80.01 | -71.72 | 79.02 | -150.74 | 0.9515 |
| 近窗 | execution-clean conditional | 38 | 39.47% | -125.90 | 61.82 | -187.72 | 61.20 | -248.92 | 0.8942 |
| 近窗 | capacity-contested | 13 | 46.15% | +134.19 | 18.19 | +116.00 | 17.82 | +98.18 | 1.1298 |

两窗合并后，execution-clean conditional 的 raw price P&L 为 -92.48 USDT，滑点与费用合计 291.06 USDT，net 为 -383.54 USDT。容量竞逐组 net 为 +800.81 USDT，因此全体闭合样本 net 为 +417.27 USDT。容量分组只能说明路径敏感性，不能当作因果容量收益。

## 不确定性

固定随机种子、20,000 次 trade-level bootstrap 的均值 95% 区间如下。区间没有处理同日/同币相关性，因此仍偏乐观，只用于显示估计不稳定：

| 窗口 | 分组 | raw mean / trade (95% CI) | net mean / trade (95% CI) | mean net R (95% CI) |
|---|---|---:|---:|---:|
| 早窗 | execution-clean conditional | +0.53 [-32.27, 36.16] | -2.14 [-35.43, 32.61] | +0.005 [-0.313, 0.337] |
| 近窗 | execution-clean conditional | -3.31 [-43.83, 39.85] | -6.55 [-46.33, 36.68] | -0.048 [-0.437, 0.375] |
| 早窗 | capacity-contested | +43.47 [-18.79, 103.58] | +41.33 [-21.36, 101.55] | +0.406 [-0.200, 0.991] |
| 近窗 | capacity-contested | +10.32 [-59.08, 86.92] | +7.55 [-63.34, 82.35] | +0.068 [-0.601, 0.793] |

四组区间均跨零。结论不是“精确证明无优势”，而是现有条件样本不足以支持稳健优势声明。

## 全体组合指标（仍混有容量路径）

| 窗口 | closed | CAGR | Sharpe | Sortino | max DD | exposure | turnover | stop rate | tail max loss |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 早窗 | 80 | 5.1533% | 0.3705 | 0.3861 | 17.2261% | 60.35% | 8.3834 | 83.75% | -126.61 |
| 近窗 | 51 | -1.5074% | -0.0280 | -0.0277 | 17.7107% | 51.05% | 6.2133 | 84.31% | -116.31 |

不能从 all-closed 权益曲线推导 execution-clean conditional 的 CAGR、Sharpe 或 drawdown；子集交易存在重叠和资金/容量反馈，必须专门重放才能得到组合级指标。本报告不伪造这些指标。

## 机制分层

### 退出结构

非容量竞逐组中，structural stop 在早窗为 36/63（57.14%），净亏 3,966.67 USDT；近窗为 22/38（57.89%），净亏 2,351.24 USDT。TP2 与 EMA20 trail 的赢家抵消大部分亏损，但最终未形成稳定正 expectancy。

“止损交易亏损”本身是退出定义，不是可行动因果解释。由于逐笔 `mae_available=false`、`mfe_available=false`，无法区分入场质量差、止损距离错误、正常噪声或盈利回吐，不据此提出调 stop 参数。

### Regime

- 早窗 execution-clean conditional：NEUTRAL -292.23，RISK_ON +157.60。
- 近窗 execution-clean conditional：NEUTRAL +256.72，RISK_ON -69.61，RISK_OFF -436.03（仅 4 笔）。

NEUTRAL 与 RISK_ON 均跨窗口翻转；RISK_OFF 样本过少。没有达到 A 的跨窗口复现标准。

### 持仓时长

- `<=3d`：早窗 -480.72，近窗 -258.65。
- `3-7d`：早窗 +633.52，近窗 +26.36。
- `>7d`：早窗 -287.42，近窗 -16.62。

短持仓亏损在两窗重复，但它主要由快速触发 structural stop 的结果定义，属于事后 outcome bucket；缺少 MAE/MFE 与可验证入场反事实，不能直接映射为“延长持仓”或“放宽止损”。

### 时间与尾部集中

- 早窗 execution-clean conditional 9 个有平仓月份中 4 正 5 负，净收益高度依赖 2024-11 的 +1,579.81 USDT。
- 近窗 8 个月中 5 正 3 负，但 2026-01 单月 -636.85 USDT 足以压低全年结果。
- 近窗前三大赢家占全部赢家收益 39.92%；尾部与时间集中进一步削弱稳定性解释。

## 裁决

- 事实：非容量组 net 两窗均为负；raw edge 早窗接近零、近窗为负；成本只在早窗翻转方向。
- 观察：容量竞逐组两窗均为正，但样本小、bootstrap 区间跨零，且属于路径选择结果。
- 假设：baseline 的主要问题不是某一项费用异常，而是非容量组缺乏足以覆盖正常交易成本的稳定 gross edge。
- 决定：`B_conditional_no_robust_gross_edge`，`retest`。不形成新参数实验，不修改生产配置。

正式历史判断仍需 `CRYPTOTRADIN-89` 的 point-in-time 历史币池，并重新执行正式闸门 1、2、3。

## 输入与可复现性

- Gate 2 census CSV SHA256：`a277a3195ee447c32129cfbca850cd0de5b7c8d1a5c4ba46413567fde20c84cc`
- 早窗 JSON SHA256：`e589f10536cf1771523199116d1dfd36b64abf46091333604cd91e1f41000025`
- 近窗 JSON SHA256：`cab46e67662a791ddd5e7581a30651021925011af0079b7de48f07302e9df435`
- 机器可读汇总：`baseline_gate_3c_summary_2026-10-10_v1.json`
- 成本栈 CSV：`baseline_gate_3c_cost_stack_2026-10-10_v1.csv`
