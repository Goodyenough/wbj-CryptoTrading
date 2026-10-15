# 实时动能启动识别：冻结协议 v1

冻结日期：2026-10-15 +08:00；在本轮收益结果产生前写入。用户已授权启动。仅研究，不修改生产、paper、shadow、采集或默认配置。

## 系统目标、单一问题与路线图位置

- 系统目标：在 Binance USDT 现货、只做多、无杠杆、最长持仓48小时的框架中，寻找仅凭当时可见信息仍能覆盖交易摩擦的简单入场优势。
- 单一问题：不使用未来4h确认结果，仅使用已完成的1h K线、最近已完成的4h特征和此前已经创建的 B watch 计划，实时产生全部早期 reclaim 候选；在纳入未保持到4h收盘的候选、固定 `+5%/-3%/48h` 与成本后，这些候选是否仍能预测后续上涨并形成正净期望？
- 路线图：承接 `CRYPTOTRADIN-129` 阶段A。阶段A只证明4h确认存在延迟并给出有未来筛选的上界；本研究第一次测量同一机制的完整实时候选集及假突破代价。

## 事实、观察、假设与当前决策

- 事实：阶段A约80.5%的最终4h确认事件可提前1至3小时；但该样本先知道未来会确认，不能执行。
- 事实：两个固定窗口已经被多轮研究使用，币池为 current-survivor；本轮只能作为开发诊断，不能成为生产上线证据。
- 观察：阶段A普通 taker 成本下提前上界转正，stress 下仍略负，说明延迟有价值但成本余量薄。
- 假设 H1：完整实时候选虽然会引入假突破，但仍在早窗和近窗形成成本后正期望。
- 假设 H0：加入未保持到4h收盘的候选后，优势消失；阶段A改善主要来自未来确认筛选。
- 决策：只检验下述唯一候选定义，不扫描1h窗口、阈值、ATR、成交量、regime或退出参数。

## 固定输入

1. 交易场所与方向：Binance Spot USDT，只做多，无杠杆。
2. 时间窗口：UTC `[2024-07-01, 2025-06-01)`（早窗）与 `[2025-06-01, 2026-06-01)`（近窗）。
3. 数据：复用 `short_horizon_entry_v1` 已冻结的逐日币池、4h eligibility frames 与本地 `1h/4h/1d` NPZ；不联网补数、不写数据库。
4. B watch 创建、失效、18根4h过期、`entry_low/entry_high/original_stop` 均沿用冻结实现；计划只在4h收盘创建。
5. 4h边界上的 eligibility 仅来自当时已经完成的4h计算；区间内前3个1h收盘沿用区间开始时最后已知的 eligibility。不得读取区间结束时才知道的 eligibility。

## 唯一实时候选 RT1

对每个已激活的 B watch，在每个4h区间的前3根已完成1h K线后进行检查：

1. 截至该小时收盘，当前4h区间内累计 high/low 已触及冻结 `[entry_low, entry_high]`；
2. 该1h close `>= entry_high`；
3. 该币在区间开始时最近已完成的4h eligibility frame 中仍合格；
4. 满足后在下一根1h open 成交，并立即消费该 watch；同一计划只产生一次候选。

第4根1h收盘等于4h确认时点，不属于 RT1 早期候选。未提前触发的 watch 在4h边界继续按原 B 顺序执行过期、失效、4h确认消费与新计划创建。未来是否在该4h边界满足 B 确认，仅作为事后 `retained_4h_confirmation` 标签，不参与信号生成、成交或主结果筛选。

## 成交、退出与成本

- 信号在1h收盘形成，下一根1h open 成交；入场 bar 的高低可触发退出，信号 bar 高低不可用于退出。
- 成交后固定实际成交价上方5%止盈、下方3%止损，48小时到期按开盘退出；gap、窗口尾部删失、同根双触发处理沿用阶段A小时级实现。
- 主结果：`taker + stop_first`；压力：`stress + stop_first`；顺序敏感性：`taker + target_first`。费率与滑点完全沿用冻结 `COSTS`。
- 主层 `all_events`：每个 RT1 候选等现金，允许假想持仓重叠，只回答信号质量。
- 辅助层 `symbol_only`：同币前一笔尚未退出时，后续候选记录为容量阻挡而不成交；检验简单可执行约束是否改变方向。无跨币组合资金竞争，本研究不声称账户级 CAGR。

## 输出与机制诊断

1. 每窗候选数、闭合/删失、信号周、币数、每30日频率、1h offset 分布。
2. `retained_4h_confirmation` 比例及 retained / not-retained 的 TP、SL、TIME、净收益；该标签只解释假突破代价。
3. mean raw/net、胜率、PF、费用、滑点、尾部、持仓期、同根歧义；按 regime、周末、月份、symbol 描述集中度。
4. 14日时间区块 bootstrap（2,000次，seed `20261015`）给出 RT1 mean net 95% 区间；leave-one-symbol 与 leave-one-week 稳健性。
5. 与冻结4h B all-events只作参照，不用其未来确认事件筛选 RT1。

## 通过、否定与证据不足标准

### `realtime_signal_supported_for_new_validation`

仅当以下全部成立：

- 两窗主层闭合交易均不少于30、信号周不少于20，成交取消与退出删失比例分别不高于1%；
- 两窗 `taker/stop_first` mean net 均大于0、PF均大于1，14日区块95%区间下界均不小于0；
- 两窗 `stress/stop_first` mean net 均大于0；
- `symbol_only` 两窗 mean net 均大于0；
- `target_first` 不改变正负结论，leave-one-symbol 与 leave-one-week 最差值仍大于0。

通过只允许创建独立未使用数据/前向 shadow 验证，不允许修改生产配置。

### `reject_current_realtime_reclaim`

测量闭合，且两窗主口径 mean net 均不大于0，或任一窗口区块区间上界不大于0；否定这个 RT1 定义，不外推否定所有1h动能信号。

### `retest_or_insufficient`

其余情况：窗口冲突、区间跨零、只在乐观成本为正、集中度/顺序翻号、样本或覆盖不足。不得据此增加筛选条件；若要研究新特征必须另立单一机制问题。

## 防泄漏与研究边界

- 信号生成断言只能访问 `signal_ms` 之前已完成的数据；保存每笔 `knowledge_cutoff_ms` 并要求 `knowledge_cutoff_ms == signal_ms`。
- `retained_4h_confirmation`、退出路径和收益均在信号形成后计算，只能用于标签与评价。
- 不运行15分钟、不扫描参数、不修改生产/配置/数据库，不把烧过的窗口称为样本外。
- 当前币池缺少完整 point-in-time 退市历史，任何支持性结果仍带 current-survivor 偏差。
