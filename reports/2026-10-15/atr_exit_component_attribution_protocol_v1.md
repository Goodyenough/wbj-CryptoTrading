# ATR 出口四政策 2×2 失败机制归因协议 v1

冻结时间：2026-10-15 00:45 +08:00

Taskboard：`CRYPTOTRADIN-134`（`in_progress`）

前置任务：`CRYPTOTRADIN-133`（`reject_preregistered_atr_exit`）

讨论记录：`claude-discussions/2026-10-15-0003-atr-exit-failure-attribution.md`

## 系统级目标

判断 B all-events 入场在 48 小时内是否能通过当前固定或 ATR 出口组件形成覆盖手续费、滑点和执行歧义的稳健正期望；在机制未解释前，不增加 ATR 参数、条件规则或生产复杂度。

## 单一问题与路线位置

保持入场、事件集、最长持仓、成本和同根顺序不变，交叉组合固定/ATR止盈与固定/ATR止损，判断：

1. 动态 TP 是否产生稳定改善；
2. 动态 SL 是否产生稳定改善或抵消；
3. TP/SL 是否存在不可忽略的路径交互；
4. 点估计改善是否主要被实际成本侵蚀；
5. 当前 `ATR20 + 1ATR SL + 5/3ATR TP` 组件定义是否值得进入独立验证。

本任务是 `CRYPTOTRADIN-133` 的失败机制归因，不是新的参数优化。若当前组件被否定，默认回到 `CRYPTOTRADIN-129/130` 的入场延续性与成本覆盖研究；不自动扫描 ATR 周期、倍数、收益风险比或持仓时间。

## 事实、观察、假设与决定

### 已确认事实

- `CRYPTOTRADIN-133` 中 full ATR 使早/近窗平均净收益从 `-0.1864%/-0.1645%` 改善到 `-0.0134%/-0.0164%`，胜率提高且 TIME 下降。
- 两窗 own-risk 净 R 仍未稳定为正，14日配对区块差值区间跨零；早窗风险曲线 MDD 恶化，近窗 stress 成本下相对改善转负。
- full ATR 同时改变 TP 和 SL，现有结果不能识别是哪一组件产生改善或抵消。
- 两个历史窗口已烧，币池为 current-survivor；通过也只能授予新窗口与 point-in-time 币池验证资格。

### 观察

- 低波动组出现更多 ATR 止损，但在早窗与近窗的净效果翻转。
- RISK_ON 相对改善、NEUTRAL 相对恶化跨窗同向，但近窗 RISK_ON 自身仍略亏，不能形成状态规则。
- ATR 止损缩短时，费用和滑点占 own-risk R 的比例会上升；只看 R 可能掩盖现金期望仍为负。

### 待检验假设

- H1：ATR TP 捕获原 TIME 的收益，但 ATR SL 过早止损并抵消改善。
- H2：ATR SL 改善风险控制，但 ATR TP 破坏盈利尾部。
- H3：TP/SL 存在显著交互，单一主效应不足以解释 full ATR。
- H4a：四个冻结出口均不能把 B all-events 转成稳健正期望。
- H4b：B all-events 入场本身缺乏可执行毛优势；本任务不能直接判定，只能为独立入场研究提供线索。
- H5：4h 同根 TP/SL 顺序足以改变资格结论，当前粒度可能不足。

### 当前决定

- 一次性完成四政策回放，不设置 MFE/MAE 前置闸门。
- MFE/MAE 只用于解释路径，不触发参数实验或持仓时间调整。
- 状态转移只解释 full fixed 到 full ATR 的差值构成，不赋予组件因果含义。
- 不修改生产、paper、shadow 或 `config/settings.toml`。

## 冻结样本与执行语义

- 交易所/币种：Binance Spot USDT，既有 current-survivor 冻结输入。
- 周期：4h；优先复用现有 1h 子K线分段，缺失时沿用既有 4h fallback 语义。
- 入场：B all-events，signal 后 next-open；四政策使用完全相同的事件集。
- 窗口：early `[2024-07-01, 2025-06-01)`；near `[2025-06-01, 2026-06-01)`。
- 最长持仓：48小时。
- ATR：信号时点因果 `ATR20`，定义与 `CRYPTOTRADIN-133` 完全一致。
- 成本：`taker / stress / legacy_fee`。
- 同根顺序：`stop_first / target_first`。

## 四个冻结出口政策

| 政策 | TP | SL |
|---|---|---|
| `fixed+fixed` | `+5%` | `-3%` |
| `ATR_TP+fixed_SL` | `+5/3 × ATR20` | `-3%` |
| `fixed_TP+ATR_SL` | `+5%` | `-1 × ATR20` |
| `ATR+ATR` | `+5/3 × ATR20` | `-1 × ATR20` |

总配置数：`4 policies × 2 windows × 3 costs × 2 tie-breaks = 48`。

禁止添加 clamp、trailing、保本、分批止盈、NATR过滤或其他参数。

## 三套收益单位

### 原始百分比

- `gross_return_pct`
- `fee_pct`
- `slippage_pct`
- `total_cost_pct = fee_pct + slippage_pct`
- `net_return_pct = gross_return_pct - total_cost_pct`

用于判断实际绝对期望是否转正。

### Own-risk R

- `own_planned_risk_pct`：该政策按既有成本引擎计算的计划止损完整损失。
- `own_net_R = net_return_pct / own_planned_risk_pct`
- `own_cost_R = total_cost_pct / own_planned_risk_pct`

用于比较各政策按自身计划风险等风险配置后的表现。

### Common-risk R

- 对同一笔交易、同一成本口径，使用 `fixed+fixed` 的实际 `planned_risk_pct` 作为四政策共同分母。
- `net_common_R = net_return_pct / fixed_planned_risk_pct`
- `cost_common_R = total_cost_pct / fixed_planned_risk_pct`

用于逐笔配对差值、状态贡献和 2×2 主效应/交互。不得硬编码名义 `3%`。

## 必须输出

### 逐笔输出

- 标识：window、symbol、signal/entry/exit 时间、policy、cost、tie-break。
- 水平：entry、ATR20、NATR20、target、stop、own/common planned risk。
- 结果：TP/SL/TIME/GAP、duration、gross/fee/slippage/net 百分比、own-R、common-R。
- 路径：48h MFE/MAE 百分比、首次触及、可达集合、同根双触发、uncaptured 百分比。

### 汇总输出

1. 四政策绝对表现：mean/median net%、胜率、PF、TIME/TP/SL、own-R、common-R、成本拖累、尾部和诊断性回撤。
2. 2×2：TP 边际平均差异、SL 边际平均差异、交互；均以 common-R 和 net% 报告。
3. 状态转移：`fixed+fixed → ATR+ATR` 九格转移的数量、平均/总 common-R 贡献；只作描述。
4. 成本/顺序：taker、stress、legacy_fee 与 stop-first、target-first 全分支。
5. 14日配对区块：四政策差值使用同一事件成块重采样，固定种子并报告95%区间。
6. MFE/MAE：仅作描述性路径上界，不进入资格判定。
7. manifest：输入、协议、源码和关键输出 SHA256；固定回放必须复现既有结果。

## 测量闸门

- 每笔必须满足 `gross - fee - slippage = net`、own-R、common-R 恒等式；任一失败即停止对应分支裁决并修复。
- 四政策必须在完全相同的配对事件集上计算；若缺口或删失随政策变化且无法统一，裁决 `measurement_insufficient`。
- 若 stop-first 与 target-first 使候选政策的绝对收益或资格结论翻号，当前 4h 粒度不足以授予资格。
- 不使用任意缺口比例、MFE比例或顺序差异容忍阈值。

## 预注册裁决

### `component_validation_eligible`

至少一个单组件政策 `ATR_TP+fixed_SL` 或 `fixed_TP+ATR_SL` 同时满足：

- early/near 的 `taker_stop_first`、`taker_target_first`、`stress_stop_first`、`stress_target_first` 八个绝对 `mean net_return_pct` 均大于 0；
- 主分支 `taker_stop_first` 相对 `fixed+fixed` 的14日配对区块 common-R 差值95%区间，early/near 下界均不小于0；
- 其余三个资格分支相对 baseline 的 common-R 点估计不为负；
- 所有测量闸门通过。

只生成新窗口与 point-in-time 币池独立验证卡片，不直接 keep 或改生产。

### `reject_current_atr_components`

测量闭合且配对样本一致，但两个单组件政策均未满足全部资格。只否定当前 `ATR20 + 1ATR SL + 5/3ATR TP` 组件定义，不外推所有 ATR 退出，也不证明 H4b。

### `measurement_insufficient`

恒等式、配对事件集、政策相关删失或同根顺序翻号使当前 4h 回放无法可信裁决。先修复测量，不作策略结论。

## 停止条件与下一步

- 获得 `component_validation_eligible`：停止当前开发窗口分析，另立独立验证卡片。
- 获得 `reject_current_atr_components`：停止当前 ATR 组件研究，回到 `CRYPTOTRADIN-129/130`；不扫描新 ATR 参数。
- 获得 `measurement_insufficient`：停止策略解释，先修数据或回放语义。

## 实施顺序

1. 泛化 `research_atr_adaptive_short_exit.py`，保留既有 fixed/full-ATR 逐笔复现。
2. 增加两个单组件政策和三套收益单位。
3. 补充合成测试：四出口水平、跳空、同根双触发、TIME、成本恒等、common-R 分母、同一事件集。
4. 运行48配置并生成逐笔与汇总产物。
5. 先过测量闸门，再按三类裁决收口；更新 Taskboard、项目记忆和实验日志，移至 `in_review` 等待用户验收。
