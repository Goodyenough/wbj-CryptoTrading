# 固定 BTC / ETH / SOL 研究池：2024–2025 历史交易条件证据审计

审计日期：2026-11-24 23:37（北京时间）。仅审计元数据和公开规则，不运行信号、参数实验或回测，不修改仓库。

## 结论

**目前不足以把下一次回放称为“完整复原历史真实可下单条件”。** 找到了两项明确的历史规则变更，但没有找到覆盖 2024–2025 每个有效区间的 `exchangeInfo` / filters 快照，尤其缺 `LOT_SIZE`、`MARKET_LOT_SIZE`、`minQty` 和 BTC / ETH 的历史 tick。不能用当前接口结果替代。

固定对象是 Binance USD-M 的 BTCUSDT、ETHUSDT、SOLUSDT 永续；110 USDT 初始权益，名义仓位上限 220 USDT，计划风险上限 1.65 USDT。这个对象及参数由父任务预先固定，本审计不提出替代币种或信号参数。

## 证据分级与来源

| ID | 已证实事项 | 证据与边界 |
|---|---|---|
| E1 | BTCUSDT、ETHUSDT 永续在 2019 年已存在 | [Binance 2020-01-16 官方回顾](https://www.binance.com/en/blog/all/421499824684900356)说明 2019 年产品及 USDT 结算方式。这只能证明早于研究期上市，不是逐时连续可交易证明。 |
| E2 | 公告要求截至 2023-11-02 10:00 UTC 完成调整：BTCUSDT 最小开单名义值由 5 调为 100 USDT，ETHUSDT 由 5 调为 20 USDT | [2023-10-27 官方公告](https://www.binance.com/en/support/announcement/detail/e4384cba297a4bd2a154be644d5d76f9)，正文 13–18 行。公告是确切历史锚点；本审计未证明随后整个 2024–2025 从未再次改变。 |
| E3 | SOLUSDT tick 在 2024-10-14 06:30 UTC 从 0.001 调为 0.01 | [2024-10-01 官方公告](https://www.binance.com/en/support/announcement/detail/8bfe2e9b86734cd08f3cbcdb82b79f51)，正文 15、23–24 行。旧订单保持原 tick，新增订单才用新 tick。这也证明该时点存在该永续产品；不能单凭本公告证明 2024-01-01 时点全部交易条件。 |
| E4 | 2025-05-02 08:00 UTC 起可由 8 / 4 小时资金费周期转为 1 小时 | [2025-04-25 Binance 官方公告账户转载](https://www.binance.com/en/square/post/23394853587906)，正文 19、44、48–51 行。触发条件是上一结算费率达到上限或下限；不是说三个币实际都发生过切换。 |
| E5 | 2025-09-01 有 1 小时恢复为 4 小时的规则变更公告 | [官方公告索引命中](https://www.binance.com/en/support/announcement/detail/6d707b1f7ae34f419621b4c807464ab1)：绝对费率连续 36 次不超过 0.002% 时，第 37 次恢复。直接打开本次跳转至公告首页，只有官方搜索索引保留正文，故标记 `PARTIAL_ACCESS`，不当成已归档原件。 |
| E6 | precision 字段不能代替 tick / step；需要实际 filters | [Binance API 官方文档](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Exchange-Information)明确警告 `pricePrecision` 不能当 tick，`quantityPrecision` 不能当 step。现行文档只用于说明字段语义，文档样例不作为任何币的历史参数。 |
| E7 | 历史资金费接口提供实际结算时间；不传起止时间会返回近期记录 | [Binance API 官方文档](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History)有 `startTime`、`endTime`、`fundingTime` 及对应结算 markPrice。本审计只读文档，没有调用此接口。 |

所有来源均为 Binance 自己发布的材料；没有使用第三方给出的合约参数。旧公告现在的页面可能含动态导航 / 行情挂件，只有历史正文的规则信息进入本报告。

## 本地证据检查

- 原仓库 `src/`、`config/` 和研究 worktree `research/` 按 `exchangeInfo`、`filters`、`MIN_NOTIONAL`、`LOT_SIZE`、`MARKET_LOT_SIZE`、`tickSize`、`stepSize` 搜索；未找到 BTC / ETH / SOL 的 2024–2025 filters 快照。
- 原仓库 `data/` 仅列文件名和目录，发现 SQLite 与旧研究 `.npz` 快照；没有打开价格数组或交易结果。
- SQLite 以 `mode=ro` 只读取 `sqlite_master` 表名与匹配元数据表的 schema。只有数据库自身的 `schema_metadata(key,value,updated_at)`，未发现独立交易所过滤器或合约主表；没有查询市场行或扫描结果行。
- 原系统 source 明确写有动态币池来自“当前 Binance exchangeInfo”的局限；这是现货系统资料，不足以证明 USD-M 永续历史规则。
- 未调用当前 `exchangeInfo`、ticker、mark-price、funding-rate、kline 等实时接口；未下载任何 2026 原始行情 / 资金费。

## 2024–2025 状态表

| 字段 | BTCUSDT | ETHUSDT | SOLUSDT |
|---|---|---|---|
| 早于研究期已上市 | 已有 2019 官方证据 | 已有 2019 官方证据 | 本次未补足上市日原始公告；2024-10-14 规则公告证明该时点存在 |
| 2024–2025 全期连续 `TRADING` | UNKNOWN，上市不等于无维护 / 暂停 | UNKNOWN | UNKNOWN |
| 最小开仓名义值 | 2023-11 锚点 100；全期连续性 UNKNOWN | 2023-11 锚点 20；全期连续性 UNKNOWN | UNKNOWN |
| `LOT_SIZE.stepSize/minQty/maxQty` | UNKNOWN | UNKNOWN | UNKNOWN |
| `MARKET_LOT_SIZE` | UNKNOWN | UNKNOWN | UNKNOWN |
| `PRICE_FILTER.tickSize` | UNKNOWN | UNKNOWN | 已证实 2024-10-14 的 0.001 → 0.01；其他变化与全期覆盖 UNKNOWN |
| 价格限制 / stop-trigger / margin tiers | UNKNOWN | UNKNOWN | UNKNOWN |
| 实际资金费结算时间与费率 | 待明确限定 2024–2025 的官方历史记录 | 同左 | 同左 |

UNKNOWN 的含义是本次证据不足，不是认定不能交易。没有用 BTC 的常见 `0.001` 步长或 SOL 常见 `0.1` 步长填空。

## 小账户的条件化可执行性边界

以下只推导下单约束，没有用任何价格路径。令当时价格为 P、止损价为 S，数量步长为 h，最小数量为 q_min，最小开单名义值为 M，账户权益为 E；费用、滑点和预留资金费占名义值的合计比例为 c。

候选数量上界：

`q_cap = min(2E/P, 0.015E / (abs(P-S) + P*c))`

按历史步长向下取整后：

`q = floor(q_cap/h)*h`

至少需要：

`q >= q_min`，`q*P >= M`，市场单 / 委托单的全部其他历史 filters 通过，保证金及费用足够。

等价的最小可下数量是 `h*ceil(max(q_min,M/P)/h)`；如果其名义值超过 220 USDT，或其止损加预算成本超过 1.65 USDT，则该事件必须跳过，不能向上加仓追求最小订单。

为便于检查旧协议成本假设，若仅采用原先**假设**的双边费与滑点合计 0.16%，再加 0.05% 资金费预留，即 c=0.21%（不是已核实真实费率 / 资金费上限）：

- 任何按满 220 USDT 名义值计算的仓位，止损价差最多 0.54% 才能满足 1.65 USDT 计划预算。
- 若以 BTC 历史公告锚点 M=100 条件化计算，忽略步长向上取整的额外最小仓位，结构止损价差必须不超过 1.44%。这只是必要条件，步长会使它更严格。
- 若以 ETH 锚点 M=20 条件化计算，同样必要条件是止损价差不超过 8.04%。这不说明 ETH 任何事件实际可成交。
- SOL 的 M、h 没有历史证据，不能给数字化小账户可执行率。
- 预留费用不是实际损失上限；跳空、滑点超假设、资金费变化可使实际损失超过计划风险。

这些是规则约束推导，不能拿它们选择标的或优化止损。

## 资金费回放要求

不能为 2024–2025 全程硬编码“每天三次”。官方 2025 公告已经说明资金费周期可变化；旧公告和现行 FAQ 也存在按年份改变的政策。实际结算应按严格限定到 2025-12-31 的官方历史事件时间入账，保留毫秒时间戳，而不是四舍五入到整点；缺失记录应标记，不能自动视为 0。

当前 `fundingInfo` 不是历史区间查询，不应用它倒填 2024–2025。旧 FAQ 的假设例子不是实际资金费观测。没有逐笔结算 mark 时，任何 mark 代理与时间同桶冲突都应作为回放假设显式披露。

## 最小后续方案（只处理证据缺口）

1. 给三个固定合约补历史 filters 的区间表：`symbol / valid_from_utc / valid_to_utc / order_type / filter_type / exact_decimal_value / source / confidence`，来源优先官方历史快照、官方变更公告与可固定 commit 的 Binance 历史文档。
2. 无证据的区间保留 UNKNOWN。协议不得把假设过滤器标记为真实历史；连续数量的信号层研究和“假设参数条件化”的执行敏感性可另命名，但不可宣称真实可执行回放。
3. 只有历史 filters 足够，才对每个事件按当时规则进行 quantity / trigger / notional 检验；对无法确认的订单独立输出 `UNKNOWN_EXECUTION_METADATA`。
4. 资金费数据后续若下载，必须 URL / 请求范围双重限制在 2024–2025，响应再次硬断言时间上界，不能使用接口默认近期返回。此审计没有下载。

本次对“足以宣称真实可执行回放”的判定为 **NO / INSUFFICIENT_METADATA**；没有对策略有效性作新结论。

## 检索过程边界事件

一次历史上市搜索没有在工具层设置官方 domains，只在搜索串写 site 限制，意外返回第三方近期行情摘要。该摘要未打开，没有把其中行情值复制到本报告、结构化证据、父任务消息或任何文件，没有据此提出信号、参数或币种选择。已立即告知父任务并改用官方 domains / 已知历史公告 URL；之后只完成固定标的规则元数据核对。

历史官方页面自身也可能带当前行情挂件；挂件信息不进入审计证据。不能表述为“从未接触任何近期信息”，可以表述为“没有下载或用于研究近期原始行情；发生过已隔离的检索摘要意外暴露”。
