# 执行契约 v1（2026-10-09）

## 目标

让回测、模拟盘和 independent shadow 的信号、成交、止损和缺口口径可解释、可审计；本文件只固化研究与 paper 语义，不授权修改生产参数或实盘下单。

## 已落地的契约

- **单一信号时点**：一次 scan 使用一个 `signal_as_of_ms`。指标 K 线只接受 `close_time <= signal_as_of_ms - 60s` 的已闭合数据；ticker 是扫描时点的报价观测，不与指标时间混写。
- **市场状态**：BTC/ETH regime 使用同一个信号时点的已闭合日线。`UNKNOWN` 是数据门禁失败，禁止新的 `BUY_CANDIDATE`，即使 symbol 属于 core/large-cap；`RISK_OFF` 的现有例外开关保持原语义，`NEUTRAL` 与关闭过滤器的行为不变。
- **回放成交**：历史 replay 明确区分本根已生效 stop 与下一根才生效的收盘 EMA；先检查已有 barrier，再按已声明的 intrabar `stop_first` 规则结算，费用和现金同步记录。
- **Paper update**：4h 评价使用已收 4h K 线；ticker 只用于当前报价快照。该流程不是交易所常驻保护单的等价模拟，停机或接口错误必须记录为 skip/gap，而不是伪造连续保护。
- **Independent shadow**：每个 4h 档一次 ticker 采样；`GAP_AFFECTED`/`CONFIG_CHANGED` 的金额只用于诊断，不进入可信配对成绩。policy fingerprint 包含 scanner/regime 代码和信号配置，语义变化会开启新 epoch。

## 验收标准

1. 指标不读取未闭合或未来 K 线；
2. stop、EMA、TP 和费用的生效顺序在 replay/paper/shadow 中有文字说明；
3. 停机、接口 skip、跨边界读取不会被当成连续样本；
4. 重复运行不重复创建同一事件或计划；
5. 证据不足时保持 `insufficient_*`，不因候选数或单次收益改变生产配置。

## 当前限制

执行语义已明确并有针对性测试，但自然运行连续性和配对终态样本仍不足；本契约因此支持“可审计”，还不支持“策略有效性已证明”。
