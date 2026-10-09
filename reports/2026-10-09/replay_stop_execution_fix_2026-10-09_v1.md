# Replay 止损计价与 EMA 生效时序修复验收

时间：2026-10-09 17:35 +08:00。Taskboard：CRYPTOTRADIN-15；后续固定历史复核：CRYPTOTRADIN-120。

## 负责人结论

第 1 项工程修复完成：历史回放先检查当时已生效的止损，收盘才能算出的 EMA 不再回头触发本根更早的最低价。新止损用于下一根；成交、手续费和现金流共用同一个成交结果。工程通过不说明 ATR 0.35 已有效，也不能给旧收益简单加一个修正值。

## 变更及证据

- `backtest/replay.py` 新增 `_step_replay_bar`，已持仓与新入场两个路径统一退出结算。在本根区间检查完成后，仍存续的 TP1 持仓才记录 EMA activation/raise，事件说明 next bar 生效。止损只升不降；不开启 EMA、缺少 EMA、TP1 保本设置保持原有选择逻辑。
- 原复现：entry=100、旧 stop=101、收盘 EMA=112，bar O/H/L/C=114/115/110/114。旧实现先抬触发位至112，却按101扣10bps成交100.899。新实现本根不退出，收盘将止损设为112；下一根实际触及时按112扣滑点成交111.888，费用、现金与净损益对账一致。
- 已持仓跳空：若下一根 open=108 低于已生效 stop=112，原始成交价取108，再扣止损滑点；不会按不可获得的112记账。仅 entry bar 保留已有 intrabar 假设。
- 同一结算重构发现入场当根 TP2 的旧分支只处理 STOPPED，遗漏 CLOSED 的退出费用和现金回收。新路径统一处理两类退出；合成调用层用例核对 final cash = initial equity + net PnL。
- 修改仅在历史 replay 内完成。`trade_state.py`、`paper_trader.py`、独立前向 shadow、生产配置未修改，不改变已存 paper 记录或重启其 epoch。

## 验证

1. 修改前基线：`tests/test_replay.py tests/test_trade_state.py` 为19通过、2失败；两项失败来自旧 fixture 的 `plan_id`/缺失 account 以及不存在的 `paper.events` 字段。本次修正 fixture 后恢复检验。
2. `python -m pytest tests/test_replay_ema_execution.py tests/test_replay.py tests/test_trade_state.py -q`：37通过。新增16个用例覆盖新/旧止损边界、下一根生效、跳空、TP1激活、保本/关闭/未就绪、终态重复调用、入场当根stop/TP2费用和真实 replay 调用。
3. 用 `git show 691964f:src/crypto_trading_system/backtest/replay.py` 捕获本次修改前已提交源码（执行时 HEAD=691964f），内存加载后运行同一组 replay 集成断言；EMA路径与当根TP2路径均复现失败。修复后同组断言通过。无网络、无历史业务库写入。
4. 全量 `python -m pytest -q`：186通过、5失败。剩余失败是已有的导出文件数、funnel 重复事件期望、未定义 outcomes、安装器 StartWhenAvailable 期望和 N0 报告 fixture 缺 min_bars；本次无新增失败。

## 未解决范围和下一项约束

- 旧历史 A/B 结果标为“执行版本待复核”。需在任务2重算完整路径、资金和容量，不能只替换受影响交易金额。
- reclaim 入场仍沿用“本根 close 确认后按同根 entry_high 成交”的旧假设；本次未改变入场策略。已在 replay limitations 显式标注。任务2开始前必须解决或隔离这一入场时序限制，不能声称本次已完成所有执行正确性工作。
- scanner 的 UNKNOWN 回退、历史退市币池、采集断档是另外的既有任务；此次不扩展。
- 任务2仅登记：唯一问题为减少的损失能否抵消错过机会损失；固定窗口/币池/版本/时序/成本/容量后才能运行。支持为跨窗方向一致且非少数赢家驱动；持续恶化则否定；口径、样本或敏感性不满足则证据不足。已研究窗口仍属 diagnostic。

本次是合成工程回归验收，不是新历史 A/B 或策略收益实验。
