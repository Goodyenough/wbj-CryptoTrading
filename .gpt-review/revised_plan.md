# 进场方案改进修订版

## 结论

当前进场框架保留，不在 2026-07-16 paper checkpoint 前修改 `settings.toml`、live paper 状态机或默认导入规则。

下一阶段目标不是立刻启用 `entry_reclaim_confirm_1bar`、`relative_strength_gate` 或 MACD 硬过滤，而是先把离线实验升级为可归因、可比较、可用 R 倍数判断经济价值的实验框架。

## 当前策略保留项

- 继续使用当前多因子扫描：EMA 趋势、24h/7d 动量、RSI、成交量、支撑距离、ATR、market regime、数据质量。
- MACD 继续保持辅助评分项，暂不升级为 `histogram > 0` 硬门槛。
- 模拟盘继续只导入 `BUY_CANDIDATE`。
- 保留 `entry_reclaim_close_enabled = true` 的 4h close reclaim 基础规则。
- 不正式导入 `WAIT_PULLBACK`。
- 不在 checkpoint 前直接启用任何 shadow replay 变体。

## 下一步必须补强的实验口径

所有 entry 相关 shadow replay 和 A/B 必须补充以下字段或报告维度：

- scanner action、raw score、是否被 data quality 降级；
- market regime，尤其 `RISK_OFF` / 非 `RISK_OFF` 分层；
- 是否触及入口区、是否 reclaim、是否因 variant 延迟或过滤；
- baseline 与 variant 的假设成交价、成交时间、entry zone、stop、TP1、TP2；
- R multiple、总 R、平均 R、中位数 R；
- TP1 命中率、stop-first 比例、time exit 比例；
- MFE、MAE、最大连续亏损、最大回撤；
- missed winner 的总 R 成本；
- filtered loser 避免的总 R；
- 延迟入场造成的价格滑移和 RR 变化；
- `distance_to_support / ATR`、reclaim 幅度 / ATR、stop distance / ATR；
- fixed opportunity set 标识，避免不同 variant 使用不同样本。

## 实验一：`reclaim_quality_matrix`

### 目的

判断当前单根 4h close reclaim 是否足够，以及 1bar confirm、ATR reclaim 强度、reclaim K 线质量中哪一类信息真正改善经济结果。

### 对照组

当前规则：`entry_reclaim_close_enabled = true`，即触及入口区后要求最近已收盘 4h close >= `entry_high`。

### 变体

- Variant A：`entry_reclaim_confirm_1bar`，reclaim 后再等 1 根 4h 确认。
- Variant B：不额外等待，但要求 reclaim close 超过 `entry_high` 的幅度达到最小 ATR 比例。
- Variant C：不额外等待，但要求 reclaim K 线收盘位于自身 high-low 区间上部。

初期不叠加成交量硬门槛，避免一次改变多个维度。

### 样本要求

- 先复用现有 paper opportunities。
- 后续至少扩展到 baseline entries >= 150；若短期达不到，至少覆盖 8-12 周，并明确标注样本不足。
- 必须覆盖 `RISK_OFF` 和非 `RISK_OFF` 两类环境，分层报告。

### keep 标准

- 至少两个时间分段中，期望 R 不劣于 baseline。
- 总 R、最大回撤或最大连续亏损有实质改善。
- 交易保留率不低于 baseline 的约 55%-65%。
- 改善不依赖单个极端赢家或单一 regime。

### revert 标准

- 期望 R 下降。
- missed winner 的 R 成本高于 filtered loser 的 R 改善。
- 交易数大幅下降但回撤无明显改善。
- 结果只在单一短窗口成立。

## 实验二：`momentum_pullback_definition_ab`

### 目的

验证当前 `24h > 0` 且 `7d > 0` 是否导致买在反弹末端，并寻找更贴近“优质回踩”的可回测定义。

### 对照组

当前 `BUY_CANDIDATE` 正动量硬门槛。

### 变体

- Variant A：允许 24h 小幅为负，但要求 7d 趋势仍为正。
- Variant B：取消 24h 绝对正负要求，改用从 recent high 回撤的 ATR 倍数。
- Variant C：要求中期趋势为正，同时回踩深度落在预设 ATR 区间。

所有 variant 保持 reclaim 规则不变，避免同时改变动量层和入场确认层。

### 样本要求

- 使用历史 dynamic universe replay，而不只限于当前 paper candidates。
- 覆盖上涨、震荡、下跌三个市场阶段。
- 按 large-cap、mid-cap、高波动 alt 分层报告。
- 每个 variant 至少 100-150 个可比较入场机会。

### keep 标准

- 在不明显扩大 stop-first 比例的情况下提高期望 R。
- TP1 命中率或 MFE 稳定改善。
- 没有显著增加逆势抄底样本。
- 多个市场阶段方向一致。

## 实验三：`relative_strength_soft_gate`

### 目的

验证相对强度是否提供独立于 EMA/MACD/24h 动量的信息增量，并决定它适合作为评分项、风险标签、`RISK_OFF` 专用 gate，还是暂不使用。

### 对照组

当前不使用相对强度的扫描与入场规则。

### 变体

- Variant A：相对强度只加减 score。
- Variant B：低相对强度只标记风险，不禁止入场。
- Variant C：仅在 `RISK_OFF` 下将低相对强度设为硬过滤。

### benchmark

BTC、ETH、等权 alt 市场篮子分别报告，不提前固定唯一 benchmark。

### keep 标准

- 弱相对强度组在多个时间分段内持续表现差。
- soft gate 改善期望 R 或回撤。
- 交易保留率合理。
- 结论不高度依赖单一 benchmark。

## MACD 处理

近期不做 `macd_hist_4h > 0` 硬门槛上线。

可作为低优先级离线变体测试：

- 保持正 histogram 加分；
- histogram 连续恶化时降级或风险标记；
- histogram 为负但连续两根改善时允许候选保留；
- reclaim 时 histogram 是否高于前一根。

暂不做 MACD 背离实验，避免定义自由度过高。

## `RISK_OFF` 处理

不为了收集样本而扩大 formal paper 风险暴露。

下一阶段将数据链分为：

- scanner shadow candidates：始终保存候选和指标；
- defensive shadow replay：在 `RISK_OFF` 下验证更严格规则；
- formal paper execution：继续遵守当前 regime 限制，或在 checkpoint 后按风险预算单独决定。

## 暂不做的事

- 不直接启用 `entry_reclaim_confirm_1bar`。
- 不直接启用 `relative_strength_gate` 硬门槛。
- 不把 MACD 正值设为硬门槛。
- 不正式导入 `WAIT_PULLBACK`。
- 不直接删除 24h/7d 正动量门槛。
- 不把成交量确认设为硬门槛。

## 下一步执行顺序

1. 等 2026-07-16 checkpoint review，确认窗口是否 `formal_audit_ready`。
2. 若 checkpoint ready，先生成 formal audit 和现有两个 shadow replay。
3. 在现有 shadow replay 基础上补齐 R multiple、MFE/MAE、regime 分层、ATR 标准化和 fixed opportunity set。
4. 优先实现 `reclaim_quality_matrix`。
5. 第二优先实现 `momentum_pullback_definition_ab`。
6. 第三优先实现 `relative_strength_soft_gate`。
7. 所有结果写入实验日志，并按 keep / revert / retest 输出明确结论。
