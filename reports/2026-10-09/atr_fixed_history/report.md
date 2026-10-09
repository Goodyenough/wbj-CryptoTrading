# 原规则 vs ATR 0.35：修复后固定历史诊断

裁决：`retest_reject_stable_improvement_in_frozen_windows`。旧窗口 diagnostic，不作为新的样本外证据。

## 白话结论

ATR 0.35 暂时不能认定为稳定有效的收益改进。较早窗口里，旧成交假设显示它大幅领先；按确认收盘价成交后，它反而比原规则少赚约3.22个百分点，虽然回撤更低。等待更强确认有代价，旧回测按更早的价格回填成交会掩盖这一点。组合路径也会随之改变，所以差值不能全部归因于单笔入场溢价。
较近窗口同样反转：确认收盘价成交时，净收益从原规则的-1.51%变为ATR线的-10.20%，最大回撤从17.71%扩大到20.21%。因此更准确的说法是：ATR能挡掉部分亏损机会，也会漏掉赢家，但未必减少组合整体亏损或回撤。两个固定窗口均未支持稳定收益改善；这不是对所有未来行情的证明。
保留 ATR 0.35 作为研究对照，维持 retest，生产配置冻结。此前候选极少 bug 的数据分级修复属于另一项工程验收，本次收益裁决不推翻它。

## 技术证据

较早窗口 legacy_same_bar 的净收益差为 +38.64pp，confirmation_close 变为 -3.22pp；后者 PF 1.12→1.04、MDD 17.23%→14.81%。至少一个预声明窗口已经发生方向反转，稳定改善的支持门槛未通过。其收盘模式 baseline-only 账目中，避免亏损2626.61 USDT、错失盈利3725.63 USDT；结合共同交易、新增交易与未平仓残差，最终少321.84 USDT。以下完整保留第二窗口及全部口径。

## 所有预声明分支

表中均为 baseline → ATR0.35；百分比变化用百分点理解。

| 窗口 | 成交口径 | 平仓数 | 净收益% | PF | 最大回撤% |
|---|---|---:|---:|---:|---:|
| 2024-07-01 至 2025-06-01 | legacy_same_bar | 76.00 → 77.00 | -2.00 → 36.65 | 0.95 → 1.78 | 16.59 → 14.30 |
| 2024-07-01 至 2025-06-01 | confirmation_close | 80.00 → 75.00 | 4.72 → 1.50 | 1.12 → 1.04 | 17.23 → 14.81 |
| 2025-06-01 至 2026-06-01 | legacy_same_bar | 58.00 → 53.00 | 4.55 → 9.40 | 1.14 → 1.31 | 19.17 → 15.27 |
| 2025-06-01 至 2026-06-01 | confirmation_close | 51.00 → 46.00 | -1.51 → -10.20 | 0.95 → 0.65 | 17.71 → 20.21 |

## 机会配对账目

金额为USDT；按 symbol + plan_created_at 配对。这里的避免亏损/错失盈利包含组合路径变化，不能解释为ATR过滤的纯因果效应。capacity causal contribution = n/a。

| 窗口/口径 | 避免亏损 | 错失盈利 | 共同平仓差值 | variant-only净额 | 未平仓/混合状态残差 | 总权益差 | 去最大3贡献后 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2024-07-01 / legacy_same_bar | 3031.80 | 2100.38 | 44.76 | 2925.41 | -37.17 | 3864.42 | 2880.97 |
| 2024-07-01 / confirmation_close | 2626.61 | 3725.63 | -232.95 | 936.58 | 73.54 | -321.84 | -984.33 |
| 2025-06-01 / legacy_same_bar | 2385.44 | 2803.00 | -83.00 | 990.09 | -4.71 | 484.82 | -568.51 |
| 2025-06-01 / confirmation_close | 1299.47 | 2034.31 | -73.05 | -61.06 | 0.00 | -868.94 | -1472.49 |

## 完整指标

历史字段 `trades` 统计全部计划；实际入场数为 closed_trades + open_trades。

### 2024-07-01 — 2025-06-01 / legacy_same_bar

| 指标 | baseline | ATR0.35 |
|---|---:|---:|
| avg_r | -0.01 | 0.44 |
| cagr | -2.17 | 40.52 |
| closed_trades | 76.00 | 77.00 |
| exposure_pct | 58.06 | 58.11 |
| fee_drag | 101.30 | 112.42 |
| intrabar_max_drawdown | 1900.62 | 2106.01 |
| intrabar_max_drawdown_pct | 16.55 | 14.18 |
| max_drawdown | 1915.33 | 2134.39 |
| max_drawdown_pct | 16.59 | 14.30 |
| net_return_pct | -2.00 | 36.65 |
| open_trades | 2.00 | 3.00 |
| profit_factor | 0.95 | 1.78 |
| sharpe | -0.01 | 1.65 |
| sortino | -0.01 | 1.74 |
| stop_rate | 89.47 | 75.32 |
| tail_max_loss | -115.40 | -151.72 |
| tp1_rate | 38.16 | 49.35 |
| tp2_rate | 10.53 | 24.68 |
| trades | 491.00 | 493.00 |
| turnover | 7.73 | 9.27 |
| win_rate | 38.16 | 49.35 |

成交后4h缺口影响：baseline 0 / ATR 0 笔。

最大三项正向配对贡献：TAOUSDT 2025-05-07T04:00:00+00:00: 338.61; BCHUSDT 2025-04-25T08:00:00+00:00: 324.57; AVAXUSDT 2024-12-02T12:00:00+00:00: 320.27

### 2024-07-01 — 2025-06-01 / confirmation_close

| 指标 | baseline | ATR0.35 |
|---|---:|---:|
| avg_r | 0.09 | 0.05 |
| cagr | 5.15 | 1.64 |
| closed_trades | 80.00 | 75.00 |
| exposure_pct | 60.35 | 58.11 |
| fee_drag | 103.45 | 74.64 |
| intrabar_max_drawdown | 2093.87 | 1716.82 |
| intrabar_max_drawdown_pct | 16.92 | 14.81 |
| max_drawdown | 2146.23 | 1720.18 |
| max_drawdown_pct | 17.23 | 14.81 |
| net_return_pct | 4.72 | 1.50 |
| open_trades | 3.00 | 2.00 |
| profit_factor | 1.12 | 1.04 |
| sharpe | 0.37 | 0.18 |
| sortino | 0.39 | 0.18 |
| stop_rate | 83.75 | 80.00 |
| tail_max_loss | -126.61 | -118.26 |
| tp1_rate | 43.75 | 46.67 |
| tp2_rate | 16.25 | 20.00 |
| trades | 489.00 | 494.00 |
| turnover | 8.38 | 6.06 |
| win_rate | 45.00 | 46.67 |

成交后4h缺口影响：baseline 0 / ATR 0 笔。

最大三项正向配对贡献：TIAUSDT 2024-11-07T20:00:00+00:00: 235.34; DOGEUSDT 2024-10-12T04:00:00+00:00: 226.43; ONEUSDT 2024-12-05T16:00:00+00:00: 200.72

### 2025-06-01 — 2026-06-01 / legacy_same_bar

| 指标 | baseline | ATR0.35 |
|---|---:|---:|
| avg_r | 0.10 | 0.21 |
| cagr | 4.55 | 9.40 |
| closed_trades | 58.00 | 53.00 |
| exposure_pct | 52.10 | 52.05 |
| fee_drag | 109.71 | 97.15 |
| intrabar_max_drawdown | 2277.85 | 1808.14 |
| intrabar_max_drawdown_pct | 18.86 | 14.88 |
| max_drawdown | 2332.75 | 1869.22 |
| max_drawdown_pct | 19.17 | 15.27 |
| net_return_pct | 4.55 | 9.40 |
| open_trades | 1.00 | 1.00 |
| profit_factor | 1.14 | 1.31 |
| sharpe | 0.34 | 0.61 |
| sortino | 0.35 | 0.61 |
| stop_rate | 84.48 | 84.91 |
| tail_max_loss | -123.91 | -125.61 |
| tp1_rate | 39.66 | 43.40 |
| tp2_rate | 15.52 | 15.09 |
| trades | 390.00 | 391.00 |
| turnover | 8.59 | 7.48 |
| win_rate | 39.66 | 45.28 |

成交后4h缺口影响：baseline 0 / ATR 0 笔。

最大三项正向配对贡献：CFXUSDT 2025-07-27T12:00:00+00:00: 390.97; ALPINEUSDT 2025-08-14T04:00:00+00:00: 337.09; ENAUSDT 2025-07-24T12:00:00+00:00: 325.28

### 2025-06-01 — 2026-06-01 / confirmation_close

| 指标 | baseline | ATR0.35 |
|---|---:|---:|
| avg_r | -0.02 | -0.21 |
| cagr | -1.51 | -10.20 |
| closed_trades | 51.00 | 46.00 |
| exposure_pct | 51.05 | 49.63 |
| fee_drag | 79.02 | 61.43 |
| intrabar_max_drawdown | 1995.94 | 2207.25 |
| intrabar_max_drawdown_pct | 17.56 | 20.03 |
| max_drawdown | 2026.79 | 2241.23 |
| max_drawdown_pct | 17.71 | 20.21 |
| net_return_pct | -1.51 | -10.20 |
| open_trades | 0.00 | 0.00 |
| profit_factor | 0.95 | 0.65 |
| sharpe | -0.03 | -0.77 |
| sortino | -0.03 | -0.71 |
| stop_rate | 84.31 | 86.96 |
| tail_max_loss | -116.31 | -112.03 |
| tp1_rate | 43.14 | 36.96 |
| tp2_rate | 15.69 | 13.04 |
| trades | 386.00 | 381.00 |
| turnover | 6.21 | 4.75 |
| win_rate | 41.18 | 39.13 |

成交后4h缺口影响：baseline 0 / ATR 0 笔。

最大三项正向配对贡献：LINKUSDT 2025-06-26T16:00:00+00:00: 260.61; ETHUSDT 2025-07-13T16:00:00+00:00: 229.33; ADAUSDT 2025-07-18T16:00:00+00:00: 113.60

## 口径与复现

- 预声明协议：`../atr_fixed_history_protocol_v1.md`。所有8个分支的完整交易/事件/权益和指标均在本目录JSON中；inputs含逐日币池、配置和各币各周期数据SHA256；manifest含代码/协议SHA256。
- 使用旧run逐日币池，保留2026-07-26存续币选择偏差；没有新建历史master。数据来自只读本地缓存，禁止网络补数；基于closed bars，warmup至少240天。
- legacy_same_bar仍有收盘确认后回填entry_high的前视成交假设，只作为诊断对照。confirmation_close按确认收盘价+滑点理想成交，从下一根检查退出；零延迟且沿用maker入场费用，不能视为实盘可成交或真实市价成本。
- 所有分支保留仓位容量、排序和资金限制；期末持仓按市值计算，不强平。因此平仓收益归因与总权益存在明确残差。
- 当前scanner与旧研究版本不同，不能把新旧报告差值全部归因于stop修复。UNKNOWN回退缺陷另行处理；本次不改生产配置。
- 独立按同一缓存、240天warmup与旧regime参数逐4h重算：早窗 RISK_OFF/NEUTRAL/RISK_ON = 1217/397/396；近窗 = 1471/221/498；两窗口 UNKNOWN 均为0。
- intrabar_max_drawdown是既有快照近似，收盘入场已排除入场前low；主裁决使用close-to-close max_drawdown_pct。
- 核验：8个分支逐笔费用、现金、末期权益一致；收盘模式无入场当根止盈止损。详见validation.json。
- 执行期间为兼容旧源码审计，最终源码将等价raw_entry条件表达式展开，并恢复legacy blocked-event标签。运行时实际replay源码已保存executed_replay.py.txt，hash对应manifest；变动不改变成交、筛选或收益。
- 重算前先保留现有产物；脚本发现summary.json会拒绝覆盖。原始缓存未提交，复现需匹配inputs中的每组数据hash。
