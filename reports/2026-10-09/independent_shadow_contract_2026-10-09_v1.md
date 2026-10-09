# 独立 ATR shadow 执行契约 v1

## 目标与研究边界

系统目标：获得可追溯、连续、可比的策略证据。唯一问题：原规则入场后，ATR 0.35 若独立继续等待、入场和退出，会产生怎样的完整路径？本次是可信前向比较的工程前置，不是新参数实验或收益裁决。

- 事实：旧 plan-level shadow 随实际 paper 入场停止该类观察；旧 candidate outcome 的成交、EMA、费用和容量口径不同。
- 观察：可信同时点比较中 baseline 放行 12 次、0.35 放行 0 次；尚无同执行口径的完整配对终态。
- 假设：独立状态及统一执行契约能补足上述证据缺口；不预设 ATR 会改善收益。
- 决定：新增隔离的前向 epoch 和快照；旧记录保留。冻结 0 / 0.35 两个门槛，incumbent 为 0.35 的同义线，不重复计为第三份证据。生产配置不变。

## 固定执行语义

1. 仅导入 epoch 启动后自然 daily 生成的 BUY_CANDIDATE，数据分级限 CLEAN/DEGRADED。共同机会来自 candidate observation，不依赖实际 paper 是否成功建仓。保留质量分层。
2. 每根已闭合 4h bar 最多推进一次；daily 与 4h cycle 均调用。确认价和 ATR/EMA 只取当时已闭合的连续 4h K 线，之后用实际获取的当前 ticker 决策。保留行情原文、观测时间、版本和状态。
3. 明确采用“定时 ticker 采样执行”，不模拟交易所常驻保护单、不用本根历史高低点回填触发。其收益不能代表连续止损交易。两线共用完全相同的输入；同 run 或同 bar 重跑不得重复扣费/成交。
4. 区间内 ticker + 已闭合 close >= entry_high + 阈值×ATR 才入场。baseline 阈值 0，variant 0.35。独立 WATCHING/ENTERED/TP1_HIT/终态；一线进入后不停止另一线。低于初始 stop 的未入场计划失效；新同币机会替换旧 WATCHING，持仓不替换。无新增持仓时限或 watch 过期规则。
5. 复用 step_trade 的 TP1/TP2/EMA 规则。EMA 在当前观测前已知，针对当前 ticker 评估，不回看更早 low。止损成交为当前 ticker 扣既有 stop slippage，不使用旧 stop override；TP2 保守按目标价。TP1 仅标记并管理 stop，不部分兑现。
6. 两线各自从 paper.account_equity 开始；复用 backtest 的 maker/taker fee 和滑点函数（entry/TP2 maker、stop taker 是模型假设，不是实际成交保证）。按 paper.risk_per_trade_pct 计算风险，使用 backtest 中既有持仓数/总风险/单仓名义价值/不加杠杆限制；先退出后按候选时间、rank、ID 入场。持仓风险保守占用初始 cash_risk，释放本金、扣费和净值独立记账。max_open_plans 限制各线未结束计划。所有限制两线相同。
7. 新 baseline 是统一成本/容量下的对照线，不声称精确复刻旧 paper 的毛 PnL；旧 paper 没有同等组合成本约束。每次保存 policy 和实现文件摘要，变化则隔离新 epoch。

## 断档与样本

- 每个 4h 档必须在收盘后 30 分钟内采样；相邻档位跳过、超过容许延迟、缺 ticker、K 线过期/缺口/非法值、程序异常均停止该 epoch，记为 GAP_AFFECTED。未结束交易右删失，不伪造成退出交易。
- 为避免资金和容量路径污染，整个受影响 epoch 不进入可信组合成绩；已闭合交易可保留原始诊断，但不得自动放入干净汇总。
- 下一次健康调用以新的开始时间、空组合重新开始，只接受新机会；不重导停机前/恢复前候选，不补造前向历史。
- 未闭合机会、无入场机会、入场后真实退出分别计数。收益有效性仍为 insufficient_paired_forward_evidence，工程通过不等于 ATR 有效。

## 验收与判定

支持工程假设：合成时间序列证明 baseline 先入场、ATR 后入场并各自退出；成本/现金守恒、独立容量、EMA、重复调用、重启续跑和断档隔离测试通过；现有 paper 表零副作用；自然 daily/4h 后出现新 tick 和新机会。

否定工程假设：baseline 状态导致 variant 停止、重复成交扣费、未来信息或旧候选进入新 epoch、跨断档样本仍标可信、旧 paper 被改写；任何一项均需修复后重新验收。

证据不足：只有合成测试、尚无自然运行/候选/完整配对终态。不能用此判定 ATR 收益，更不能修改生产默认参数。下一次研究裁决须另行预声明样本窗口和主要指标；本次不添加新阈值扫描。
