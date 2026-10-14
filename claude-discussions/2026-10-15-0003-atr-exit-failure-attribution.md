---
status: DONE
round: 3
max_rounds: 3
decision: retest
---

# Claude 讨论：如何归因 ATR 自适应短周期出口未形成正收益

## 当前状态

- 系统级目标：判断当前 B all-events 入场是否存在足够、可执行的短周期毛优势，以及怎样设计退出才能在手续费、滑点和 48 小时持仓约束后保留该优势；在机制不清楚前不增加策略复杂度。
- 当前决策问题：`TP=5/3×ATR20、SL=1×ATR20、最长48h` 相对固定 `+5%/-3%/48h` 改善了胜率和平均净收益点估计，却没有形成跨窗口、跨成本的稳健正期望。下一步应采用什么最小诊断，才能区分问题主要来自动态止盈、动态止损、交易成本、市场状态交互，还是入场本身缺少延续性？
- 已确认事实：
  - 本轮使用 Binance Spot USDT、4h、current-survivor 币池、B all-events、next-open 入场、48h 最长持仓；主口径为 taker 成本和 stop-first，同一批入场逐笔配对比较固定出口与 ATR 出口。
  - 早窗 `[2024-07-01, 2025-06-01)` 共 858 笔：平均净收益 `-0.1864% -> -0.0134%`，胜率 `38.81% -> 40.21%`，平均净 R `-0.0567 -> -0.0317`，TIME `15.62% -> 10.96%`，但等风险诊断 MDD `61.21% -> 65.46%`。
  - 近窗 `[2025-06-01, 2026-06-01)` 共 628 笔：平均净收益 `-0.1645% -> -0.0164%`，胜率 `40.76% -> 43.15%`，平均净 R `-0.0500 -> -0.000008`，TIME `30.10% -> 3.34%`，等风险诊断 MDD `59.71% -> 47.99%`。
  - 两窗 `ATR-fixed` 的 14 日配对区块 95% 区间分别为 `[-0.1077, +0.1108]R`、`[-0.0551, +0.1542]R`，都跨零；近窗 stress 成本下相对差值由 `+0.0500R` 翻为 `-0.0115R`。
  - 市场状态交互同向：早/近窗 `RISK_ON` 相对改善 `+0.1148/+0.0687R`，`NEUTRAL` 相对恶化 `-0.1315/-0.0271R`；但近窗 `RISK_ON` 的 ATR 版本自身仍约为 `-0.00485R`，尚无绝对正优势。
  - 波动分层不稳定。早窗 low-NATR 组平均 R `+0.0123 -> -0.1198`，SL 数 `104 -> 161`；近窗 low-NATR 组 `-0.0530 -> +0.0176`，SL 数 `178 -> 248`。早窗 high-NATR 改善，近窗 high-NATR（仅 22 笔）恶化。
  - 成本占 R 的比例上升，尤其近窗从固定出口约 `0.0932R` 上升至 ATR 出口约 `0.1428R`。
  - 已有退出后恢复率诊断显示：旧 baseline 非容量止损的 K40 恢复率早窗为 `38.46%`、近窗为 `20.69%`，近窗 17 笔 unknown 在 K40 为 `0/16`；结论为窗口不一致，且近窗不支持“主要因为止损过早”。这项结果不能直接归因当前 ATR 出口的新旧交易状态变化。
- 观察：
  - ATR 方案不是完全无效：它显著减少 TIME，并把两窗点估计推近盈亏平衡；真正的问题是改善不稳健、绝对期望仍未转正，而且成本与部分分层抵消了改善。
  - 当前同时改变 TP 和 SL，无法仅凭完整方案判断收益变化来自哪一侧，也无法判断 TIME 转化为 TP 的收益是否被新增或更早的 SL 抵消。
  - 按 NATR、regime 做事后切片能发现交互，但容易把样本噪声误当机制，特别是近窗 high-NATR 只有 22 笔。
- 假设：
  - H1：动态 TP 是主要改善来源；低波动币更近的目标把原 TIME 转成盈利，但动态 SL 同时制造过早止损并抵消收益。
  - H2：动态 SL 是主要改善来源；风险尺度匹配减少了异常损失，而动态 TP 扩大或缩小后破坏了收益尾部。
  - H3：TP/SL 单独都不是稳定主因，只有与 `RISK_ON/NEUTRAL` 或 NATR 水平交互时才有方向；统一 ATR 公式因此失效。
  - H4：退出调整只能重新分配 TP/SL/TIME，入场毛优势不足；手续费和滑点占 R 上升后，任何短距离自适应出口都难以转正。
  - H5：4h 同根 high/low 顺序和 stop-first 假设可能影响状态归因，若不做路径边界或敏感性检查，2×2 结果仍可能误导。
- 已有决定与约束：
  - 预注册的 `1ATR SL / 5:3ATR TP` 方案已判 `reject_preregistered_atr_exit`；这只否定该具体定义，不否定所有 ATR 出口。
  - 不修改生产、paper 或 shadow 配置；不扫描新的 ATR 倍数、NATR 阈值或持仓时间。
  - 两个窗口均已烧，且使用 current-survivor 币池；任何结果最多生成下一张单变量实验卡片，不能直接升级生产。
  - 机制诊断必须保持同一入场、窗口、成本和 48h 约束，并明确事实、观察、假设与决定，以及支持、否定、证据不足标准。
- GPT 当前判断：优先做冻结参数的 `2×2` 因子拆解：固定 TP+固定 SL、ATR TP+固定 SL、固定 TP+ATR SL、ATR TP+ATR SL；随后对同一交易做结果状态转移、毛收益/成本 R 分解和必要的路径诊断。先判断哪一侧产生改善、哪一侧抵消，再决定是否需要 regime/NATR 分层。
- GPT 最没有把握的地方：
  - 这个 `2×2` 是否足以形成可信的组件归因，还是 TP 与 SL 存在强路径交互，导致“主效应”没有可解释性。
  - 是否应该先做交易状态转移和费用侵蚀分解，再做 `2×2`；或者先检查入场后的无退出 MFE/MAE，避免在没有毛优势时继续研究出口。
  - 如何处理 4h 同根同时触及 TP/SL 的顺序不确定性，才能防止 stop-first/take-first 假设主导机制结论。
  - regime/NATR 应作为预注册分层、因果交互项，还是只作为解释性附录；什么样的跨窗一致性才足以支持继续研究。
- 希望 Claude 重点评估：
  - 挑战 GPT 的 `2×2` 方案：它能回答什么、不能回答什么，是否存在更高信息量但仍然最小的设计。
  - 给出诊断顺序和停止规则，避免开放式切片或新的参数搜索。
  - 给出逐笔必须输出的状态转移、路径、毛收益、成本和风险字段，以及窗口/分层汇总方式。
  - 为 H1–H5 分别定义支持、否定和证据不足标准；指出哪些结果只说明“值得复核”，不能证明应修改退出。
  - 明确如何区分“退出几何不合适”和“入场本身没有足够毛优势”。

## Round 1：GPT 发起

### 背景

用户最初提出：不同币种自身波动率差异很大，固定 `+5%/-3%` 对低波动币可能太远，对高波动币可能只是日常噪声，因此应根据 ATR 调整止盈和止损。现已完成一个冻结定义的验证：`SL=1×ATR20`，`TP=(5/3)×ATR20`，保持原 5:3 收益风险比和 48 小时上限。

结果不是简单的“无改善”：胜率和平均净收益在两个窗口都改善，TIME 明显下降；但绝对净期望仍未稳定转正，配对区块区间跨零，早窗回撤恶化，近窗在 stress 成本下相对改善翻负，且 NATR 分层和市场状态交互明显。因此现在需要解释“改善为什么不够”，而不是继续换 ATR 倍数。

### 相关证据与文件

- `reports/2026-10-14/atr_adaptive_short_exit_v1/report.md`
- `claude-discussions/2026-10-10-0947-baseline-loss-attribution-next-step.md`
- `claude-discussions/2026-10-10-2321-near-window-unknown-losses.md`
- `reports/2026-10-14/baseline_post_exit_recovery_v1/report.md`
- `AGENTS.md`

### 候选方向

1. **冻结定义的 2×2 组件归因**：保持现有 fixed 与 ATR 距离不变，仅交叉组合 TP 和 SL。优点是直接拆分组件；风险是 TP/SL 是路径竞争事件，简单主效应可能不具有加法解释。
2. **逐笔状态转移优先**：先统计 fixed 的 TP/SL/TIME 分别转成四种方案下什么状态，并分解每类转移的 gross R、cost R、net R；再决定是否需要 2×2。优点是贴近“改善被谁抵消”；风险是仍是描述性、可能受同根顺序影响。
3. **入场路径上限优先**：先忽略具体出口，检查同一入场在 48h 内的 MFE/MAE、先到达固定或 ATR 水平的竞争概率，以及扣费前可捕获空间；如果多数交易连足够毛空间都没有，则停止出口研究。优点是先检验 H4；风险是 4h OHLC 顺序和事后最优路径可能高估可交易优势。
4. **regime/NATR 交互优先**：把退出差值按预注册状态分层，判断统一公式失效是否主要由市场状态决定。优点是已有同向线索；风险是样本切碎、事后解释和近窗 high-NATR 小样本。

### 请求 Claude

请独立评估如何最有效地找到本轮失败的原因。先给出推荐的诊断顺序，再展开说明理由、备选方案、权衡、风险和缺失证据。请重点回答：

1. `2×2` 是否应是第一步？如果不是，哪一步的信息增益更高？
2. 如何定义不依赖参数搜索的逐笔反事实/状态转移分析，避免把 TP/SL 路径竞争错误地解释为可加的主效应？
3. 怎样处理同一根 4h K 线同时触及 TP 和 SL的顺序不确定性？哪些结论必须在 stop-first 与 take-first 下同向才成立？
4. 如何把 gross edge、cost drag、exit geometry 和 regime interaction 分层判断，并在何处停止，避免无穷切片？
5. 请为建议的最小诊断给出：必须字段、汇总表、支持/否定/证据不足标准，以及能够触发或禁止下一张单变量实验卡片的闸门。

不要提出新的 ATR 倍数、阈值优化或生产配置修改。若现有证据最合理的结论是“先验证入场毛优势，暂停出口研究”，请明确指出并说明依据。

## Round 1：Claude 回复

### 推荐诊断顺序

**Phase 1：入场路径上限检查（优先级最高）**
**Phase 2：逐笔状态转移与成本分解**
**Phase 3：条件性 2×2 组件归因**
**Phase 4：regime/NATR 交互解释（仅当前三步显示稳健改善时）**

### 核心判断

GPT 的 2×2 方案**不应是第一步**。理由：

1. **因果顺序倒置**：你已经观察到"改善不稳健、绝对期望仍未转正"，这强烈暗示 H4（入场毛优势不足）。在证实入场后确实存在足够的可捕获空间之前，研究如何分配 TP/SL/TIME 是在优化一个可能不存在的优势。

2. **路径竞争掩盖机制**：2×2 设计假设 TP 和 SL 的效应可分离，但它们在时间轴上竞争——动态 SL 更近时会更早触发，改变了 TP 的有效样本分布。如果不先做状态转移分析，你无法判断"ATR TP+fixed SL"中观察到的改善是 TP 几何本身的效果，还是因为 fixed SL 让更多交易活到了新的 TP 水平。

3. **成本侵蚀未拆分**：近窗 ATR 出口的成本占 R 从 0.0932 升至 0.1428，上升 53%。这可能来自：(a) ATR SL 更近导致更频繁止损、每笔固定费用摊到更小 R；(b) 低波动币的 ATR 距离绝对值过小、费用占比天然更高；(c) 近窗币种波动率结构变化。在分解 gross R 和 cost R 之前，2×2 的净收益对比会把几何效应与成本结构混淆。

### Phase 1：入场路径上限检查

**目标**：判断同一入场在 48h 内、扣费前，是否存在足够的可捕获毛空间支持任何短距离自适应出口。

**方法**：

对每笔交易，从 entry_time 到 exit_time（或 +48h），扫描 4h K 线序列，记录：

- **MFE_gross**（Maximum Favorable Excursion）：入场后最高点相对入场价的最大收益，未扣费
- **MAE_gross**（Maximum Adverse Excursion）：入场后最低点相对入场价的最大损失，未扣费
- **First_reach**：四种水平中最先到达的是哪个——`fixed_TP`、`ATR_TP`、`fixed_SL`、`ATR_SL`
- **Reachable_set**：在实际退出前，四种水平中哪些曾被触及（可能多个）
- **Gross_captured_if_optimal**：如果在 MFE 点平仓的理论毛收益
- **Cost_R_at_entry**：入场时的 ATR20 值，费用占 R 的比例 = `(taker_fee_bps × 2) / (ATR20 / entry_price)`

**汇总**：

分早/近窗，统计：

1. **MFE 分布**：中位数、25%/75% 分位数、大于 `1.5×cost_R` 的比例
2. **毛空间充足率**：`MFE_gross > 2×cost_R` 且 `MFE_gross > 0.5×ATR` 的交易占比——这是"理论上有利可图"的下界
3. **先达竞争**：`First_reach` 的四类频数，特别是 `ATR_SL` 先达的比例
4. **路径顺序不确定性**：同一根 K 线同时触及多个水平的笔数与占比

**停止规则**：

- 若两窗 `MFE > 2×cost_R` 的比例 < 55%，且中位 MFE < 1.0R，**结论为 H4 成立**：入场本身缺少足够延续性，暂停出口研究，转向入场改进或放弃 B all-events 短周期方向。
- 若早窗充足但近窗不充足，标记为窗口依赖，需要重新验证币池、regime 分布或市场结构变化，仍不继续出口优化。
- 仅当两窗充足率 > 60% 且中位 MFE > 1.2R 时，进入 Phase 2。

**顺序不确定性处理**：

对同一根 K 同时触及 TP 和 SL 的情况，记录为 `ambiguous_path`。在 Phase 1 只统计频数；若占比 > 15%，Phase 3 的 2×2 必须在 stop-first 和 take-first 两种假设下各跑一遍，仅当方向一致时才采纳结论。

---

### Phase 2：逐笔状态转移与成本分解

**前提**：Phase 1 显示入场存在毛优势。

**目标**：将 fixed 出口的每笔交易映射到 ATR 出口的状态，分解毛收益变化与成本变化，判断"改善被谁抵消"。

**字段**：

每笔交易输出：

| 字段 | 定义 |
|------|------|
| `trade_id` | 唯一标识 |
| `window` | early/near |
| `regime` | RISK_ON/NEUTRAL/RISK_OFF |
| `NATR_bucket` | low/mid/high（按 NATR 三等分） |
| `fixed_outcome` | TP/SL/TIME |
| `ATR_outcome` | TP/SL/TIME |
| `state_transition` | 9 种组合，如 `TP→SL`、`TIME→TP` |
| `fixed_gross_R` | 固定出口的毛收益（未扣费） |
| `ATR_gross_R` | ATR 出口的毛收益（未扣费） |
| `fixed_cost_R` | 固定出口的费用（以 R 计） |
| `ATR_cost_R` | ATR 出口的费用（以 R 计） |
| `fixed_net_R` | `gross - cost` |
| `ATR_net_R` | `gross - cost` |
| `delta_gross_R` | `ATR_gross - fixed_gross` |
| `delta_cost_R` | `ATR_cost - fixed_cost` |
| `delta_net_R` | `ATR_net - fixed_net` |
| `MFE_gross` | 来自 Phase 1 |
| `uncaptured_R` | `MFE_gross - ATR_gross_R`（离开桌面的钱） |

**状态转移汇总表**：

分早/近窗，按 9 种转移类型统计：

```
Transition    Count    Avg_delta_gross_R    Avg_delta_cost_R    Avg_delta_net_R    Median_delta_net_R
TP→TP         ...      ...                  ...                 ...                ...
TP→SL         ...      ...                  ...                 ...                ...
TP→TIME       ...      ...                  ...                 ...                ...
SL→TP         ...      ...                  ...                 ...                ...
SL→SL         ...      ...                  ...                 ...                ...
SL→TIME       ...      ...                  ...                 ...                ...
TIME→TP       ...      ...                  ...                 ...                ...
TIME→SL       ...      ...                  ...                 ...                ...
TIME→TIME     ...      ...                  ...                 ...                ...
```

**关键诊断**：

1. **TIME→TP 的净贡献**：若该转移的 `avg_delta_net_R > 0` 且样本量足够（如 >50 笔），说明动态 TP 确实捕获了原 TIME 的延续。检查 `delta_cost_R`：若接近零，说明成本未恶化；若显著为正，说明费用侵蚀了毛改善。

2. **TP→SL 的净损失**：若该转移的 `avg_delta_net_R < -0.3R` 且频数高，说明动态 SL 过早截断了原本会盈利的交易——这是 H1 的证据。检查这些交易的 `MFE_gross`：若多数 MFE 远超 fixed_TP，说明入场有延续但 ATR SL 几何不当。

3. **SL→SL 的成本差异**：若 `delta_cost_R` 显著为正，说明 ATR SL 更近、更频繁触发，固定费用占比上升——这解释了近窗成本占 R 上升 53% 的部分原因。

4. **未捕获空间**：按转移类型统计 `uncaptured_R` 中位数。若 TIME→TP 的 `uncaptured_R` 中位数 > 1.0R，说明动态 TP 虽然比 TIME 好，但仍然过早；若 TP→SL 的 `uncaptured_R` 中位数 > 2.0R，说明 ATR SL 在入场仍有大幅毛优势时就止损了。

**支持/否定标准**：

- **H1 支持**：`TP→SL` 频数 > 80 且 `avg_delta_net_R < -0.25R`，且该类交易的 `MFE_gross` 中位数 > 1.5R。
- **H1 否定**：`TP→SL` 频数 < 30 或 `avg_delta_net_R > -0.1R`。
- **H4 支持（即使 Phase 1 通过）**：所有转移类型的 `uncaptured_R` 中位数 < 0.5R，说明 MFE 本身就不高，出口几何不是瓶颈。
- **成本主导**：任一窗口中，`|avg_delta_gross_R|` 的加权和 > 0.15R，但 `avg_delta_net_R` 的加权和 < 0.05R——说明毛改善被成本抵消。

**停止规则**：

若 Phase 2 显示：

- 两窗 `TIME→TP` 和 `TIME→SL` 的净贡献之和 < 0.05R，且成本差异 > 0.05R，**结论**：ATR 出口重新分配了状态，但毛改善不足以覆盖成本上升，**停止出口研究**，不进入 Phase 3。
- 若某一转移类型显示稳健净改善（两窗同向、中位数 > 0.1R、95% CI 不跨零），但加总后仍不转正，进入 Phase 3 做组件拆分。

---

### Phase 3：条件性 2×2 组件归因

**前提**：Phase 2 显示存在部分转移的净改善，但不清楚来自 TP 还是 SL。

**设计**：

四种出口组合，保持 48h 上限和 next-open 入场不变：

1. `fixed_TP + fixed_SL`（baseline，已有）
2. `ATR_TP + fixed_SL`
3. `fixed_TP + ATR_SL`
4. `ATR_TP + ATR_SL`（已有）

每笔交易跑四次，记录净 R 和状态。

**主效应估计**（需谨慎解释）：

- **TP 效应** = `[mean(ATR_TP + fixed_SL) + mean(ATR_TP + ATR_SL)] / 2 - [mean(fixed_TP + fixed_SL) + mean(fixed_TP + ATR_SL)] / 2`
- **SL 效应** = `[mean(fixed_TP + ATR_SL) + mean(ATR_TP + ATR_SL)] / 2 - [mean(fixed_TP + fixed_SL) + mean(ATR_TP + fixed_SL)] / 2`
- **交互效应** = `mean(ATR_TP + ATR_SL) - mean(ATR_TP + fixed_SL) - mean(fixed_TP + ATR_SL) + mean(fixed_TP + fixed_SL)`

**路径竞争校正**：

对每种组合，统计"TP 先达"与"SL 先达"的频数。若 `ATR_TP + fixed_SL` 中 SL 先达的比例显著低于 `ATR_TP + ATR_SL`，说明 fixed SL 让更多交易活到了 ATR TP，此时 TP 效应被**高估**了（它不是 TP 几何本身的效果，而是 SL 宽松的副产品）。

**顺序不确定性处理**：

若 Phase 1 显示 `ambiguous_path` 占比 > 15%，对这些交易分别用 stop-first 和 take-first 重算四种组合的净 R。若两种假设下 TP/SL 效应的符号翻转，**结论**：当前 4h 粒度无法支持可信的组件归因，需要用 tick 数据或标记为"证据不足"。

**支持/否定标准**：

- **H1 支持**：两窗 TP 效应 > +0.10R，SL 效应 < -0.08R，交互效应 < -0.05R——说明动态 TP 有效，但动态 SL 抵消且存在负交互。
- **H2 支持**：两窗 SL 效应 > +0.10R，TP 效应 < 0.05R——说明风险匹配是主因。
- **H3 支持**：交互效应的绝对值 > 0.15R 且跨窗同向——说明 TP/SL 不可独立解释。
- **证据不足**：任一效应在两窗异号，或所有效应 < 0.08R 且 95% CI 跨零。

**停止规则**：

若 Phase 3 的主效应与 Phase 2 的状态转移分析矛盾（例如 Phase 2 显示 `TIME→TP` 有净贡献，但 Phase 3 显示 TP 效应为负），**优先采信 Phase 2**——因为状态转移是逐笔反事实，2×2 的主效应可能被路径竞争扭曲。

若 Phase 3 显示某一组件单独有效（如 `ATR_TP + fixed_SL` 两窗期望 > 0.15R），生成下一张**单变量实验卡片**，仅改变该组件，其余冻结，用新窗口 + out-of-sample 币池验证。

若所有组件效应 < 0.08R 或异号，**结论**：当前 ATR 定义（20 周期、5:3 比例）无稳健改善，**不生成新卡片**。

---

### Phase 4：regime/NATR 交互解释

**前提**：Phase 2 或 Phase 3 显示某一组件在汇总水平有稳健改善。

**目标**：解释为什么改善不稳健、哪些子集拖累了整体。

**方法**：

将 Phase 2 的状态转移或 Phase 3 的组件效应，按 `regime × NATR_bucket` 分层（最多 3×3=9 个子集），统计每个子集的：

- 样本量
- 平均 delta_net_R
- 中位 delta_net_R
- 95% CI

**分层可信度标准**：

- 子集样本量 < 40 笔，标记为"小样本，仅作探索性解释"
- 两窗同一子集的方向相反，标记为"窗口依赖，不支持生产化"
- 两窗同向且样本量 > 50，标记为"稳健交互"

**解释 vs 决策**：

- **仅解释**：若 Phase 3 已判定不生成新卡片，Phase 4 的分层只用于事后理解（如"近窗 NEUTRAL 下 low-NATR 组恶化解释了整体未转正"），写入报告但不触发行动。
- **前置分层**：若希望把 regime/NATR 作为**预注册的因果交互项**（即未来生产时根据实时 regime 和 NATR 选择不同 TP/SL），则需要：
  - 在 Phase 3 之前做分层，每个子集单独跑 2×2
  - 每个子集必须两窗样本量 > 60，且方向一致
  - 需要额外的 regime 转换期的表现验证（如 RISK_ON → NEUTRAL 过渡期）

  当前证据不支持前置分层——你的 `RISK_ON` 样本在近窗仍约 -0.00485R，不是"显著正且稳健"的子集。

**停止规则**：

Phase 4 是**解释性附录**，不生成新卡片，不修改生产配置。唯一例外：若某一子集（如早窗 RISK_ON + high-NATR）两窗期望 > 0.25R 且样本量 > 80，可生成一张**条件触发卡片**——但该卡片的前置条件是"实时 regime 分类器已上线并经独立验证"，否则不实施。

---

### 必须字段（Phase 2 逐笔输出）

```python
{
  "trade_id": str,
  "window": "early" | "near",
  "symbol": str,
  "entry_time": datetime,
  "entry_price": float,
  "exit_time_fixed": datetime,
  "exit_time_atr": datetime,
  "regime": "RISK_ON" | "NEUTRAL" | "RISK_OFF",
  "NATR_at_entry": float,
  "NATR_bucket": "low" | "mid" | "high",
  "ATR20_at_entry": float,
  "cost_R_at_entry": float,  # (fee_bps * 2) / (ATR20 / entry_price)

  "fixed_outcome": "TP" | "SL" | "TIME",
  "ATR_outcome": "TP" | "SL" | "TIME",
  "state_transition": str,  # e.g., "TIME→TP"

  "fixed_gross_R": float,
  "ATR_gross_R": float,
  "fixed_cost_R": float,
  "ATR_cost_R": float,
  "fixed_net_R": float,
  "ATR_net_R": float,

  "delta_gross_R": float,
  "delta_cost_R": float,
  "delta_net_R": float,

  "MFE_gross": float,  # from Phase 1
  "MAE_gross": float,
  "MFE_time": datetime,
  "first_reach": "fixed_TP" | "ATR_TP" | "fixed_SL" | "ATR_SL",
  "reachable_set": list[str],
  "ambiguous_path": bool,
  "uncaptured_R": float,  # MFE_gross - ATR_gross_R

  # Phase 3 字段（若进入）
  "net_R_atr_tp_fixed_sl": float,
  "net_R_fixed_tp_atr_sl": float,
  "outcome_atr_tp_fixed_sl": str,
  "outcome_fixed_tp_atr_sl": str
}
```

---

### 汇总表模板

**Phase 1 汇总（入场路径上限）**

```
Window    N     MFE_median    MFE_p25    MFE_p75    Pct_MFE>2cost    Pct_MFE>0.5R    First_reach_ATR_SL_pct    Ambiguous_path_pct
early     858   ...           ...        ...        ...              ...             ...                       ...
near      628   ...           ...        ...        ...              ...             ...                       ...
```

**Phase 2 汇总（状态转移）**

```
Window    Transition    Count    Avg_delta_gross    Avg_delta_cost    Avg_delta_net    Median_delta_net    CI_95_lower    CI_95_upper    Avg_uncaptured
early     TP→TP         ...      ...                ...               ...              ...                 ...            ...            ...
early     TP→SL         ...      ...                ...               ...              ...                 ...            ...            ...
...       ...           ...      ...                ...               ...              ...                 ...            ...            ...
near      TP→TP         ...      ...                ...               ...              ...                 ...            ...            ...
...       ...           ...      ...                ...               ...              ...                 ...            ...            ...
```

**Phase 3 汇总（2×2 主效应）**

```
Window    Fixed+Fixed    ATR_TP+Fixed_SL    Fixed_TP+ATR_SL    ATR+ATR    TP_effect    SL_effect    Interaction
early     -0.0567        ...                ...                -0.0317    ...          ...          ...
near      -0.0500        ...                ...                -0.000008  ...          ...          ...
```

---

### 假设检验标准总结

| 假设 | 支持标准（Phase 2） | 支持标准（Phase 3） | 否定标准 | 证据不足 |
|------|---------------------|---------------------|----------|----------|
| H1: 动态 TP 有效、动态 SL 抵消 | `TIME→TP` 净贡献 > 0.10R 且 `TP→SL` 净损失 < -0.25R，两窗同向 | TP 效应 > 0.10R，SL 效应 < -0.08R，交互 < -0.05R，两窗同向 | `TP→SL` 频数 < 30 或净损失 > -0.1R | 任一效应两窗异号或 CI 跨零 |
| H2: 动态 SL 有效、动态 TP 破坏 | `SL→SL` 和 `SL→TIME` 净贡献 > 0.10R，`TP→TIME` 净损失显著 | SL 效应 > 0.10R，TP 效应 < 0.05R，两窗同向 | `SL` 相关转移净贡献 < 0.05R | 同上 |
| H3: 强路径交互、主效应无意义 | 状态转移的净贡献高度依赖路径顺序（stop-first vs take-first 翻号） | 交互效应绝对值 > 0.15R，两窗同向，且大于任一主效应 | 交互效应 < 0.05R | 样本量不足或顺序不确定性 > 20% |
| H4: 入场毛优势不足 | Phase 1: 两窗 MFE > 2cost 比例 < 55%，中位 MFE < 1.0R | Phase 2: 所有转移的 uncaptured_R 中位数 < 0.5R | Phase 1: 两窗充足率 > 60% 且中位 MFE > 1.2R | 早窗充足、近窗不充足（窗口依赖） |
| H5: 4h 粒度顺序假设影响结论 | `ambiguous_path` > 15%，且 stop-first 与 take-first 下主效应翻号 | — | `ambiguous_path` < 10% 且两种假设下方向一致 | 需 tick 数据验证 |

---

### 闸门：何时生成/禁止下一张实验卡片

**生成新卡片的条件（必须全部满足）**：

1. Phase 1 显示两窗入场毛优势充足（MFE > 2cost 比例 > 60%）
2. Phase 2 或 Phase 3 显示某一单独组件（仅 ATR TP 或仅 ATR SL）两窗期望 > 0.12R，中位数 > 0.10R，95% CI 下界 > 0
3. 该组件的改善不依赖另一组件保持 fixed（即路径竞争校正后仍成立）
4. `ambiguous_path` < 15% 或在两种顺序假设下均成立
5. 改善不局限于单一 regime 或 NATR 子集（除非该子集样本量 > 100 且有独立触发机制）

**禁止新卡片的条件（任一成立即停止）**：

1. Phase 1: 任一窗口 MFE > 2cost 比例 < 55%
2. Phase 2: 成本上升抵消了毛改善（delta_cost > delta_gross）
3. Phase 3: 所有组件效应 < 0.08R 或两窗异号
4. Phase 2 与 Phase 3 矛盾，且无法用路径竞争解释
5. 改善仅在小样本子集（< 50 笔）中出现
6. 早窗改善但近窗恶化（窗口依赖）

**当前预判**：
基于你提供的证据（两窗净 R 接近零、近窗 stress 成本下翻负、NATR 分层不一致、成本占 R 上升 53%），我预期 Phase 1 会显示近窗 MFE 充足率边缘（55%-65%），Phase 2 会显示成本侵蚀主导，最终结论为**禁止新卡片，标记 H4 为主要原因，建议优先验证入场毛优势或放弃 B all-events 短周期方向**。

但必须先跑完诊断，用数据而非先验判断。

---

### 关键权衡与风险

**权衡 1：Phase 1 的 MFE 是否高估可交易优势？**

- **风险**：4h OHLC 的 MFE 是事后最优路径，实际交易无法在精确的高点平仓。真实可捕获空间可能只有 MFE 的 60%-80%。
- **缓解**：Phase 1 只用于判断"是否存在足够毛空间"，不用于估计精确期望。若 MFE 连 2×cost 都不到，即使打 60% 折扣也不够。

**权衡 2：Phase 2 的状态转移是否受 stop-first 假设影响？**

- **风险**：若同一根 K 同时触及 TP 和 SL，`TP→SL` 的频数会被 stop-first 夸大。
- **缓解**：Phase 2 先统计 `ambiguous_path` 占比。若 > 15%，Phase 3 必须双假设验证；若 < 10%，影响可控。

**权衡 3：2×2 是否值得做？**

- **权衡**：Phase 2 已经给出状态转移和成本分解，Phase 3 的 2×2 增加 2 倍计算量，但信息增益可能有限——它只是把转移分析重新组合成主效应形式。
- **建议**：若 Phase 2 已明确某一转移（如 `TIME→TP`）主导改善且不被成本抵消，可跳过 Phase 3，直接生成"仅改 TP"的单变量卡片。仅当 Phase 2 显示多个转移有混合效应、无法判断主因时，才需要 Phase 3 拆分。

**权衡 4：regime/NATR 分层是否过早？**

- **风险**：你已有同向线索（RISK_ON 改善、NEUTRAL 恶化），但近窗 RISK_ON 自身仍 -0.00485R，不足以支持"条件触发"策略。若现在就按分层设计出口，需要实时 regime 分类器、更多样本、转换期验证——这超出了"最小诊断"范围。
- **建议**：Phase 4 仅作事后解释，不触发行动。若未来某个子集经独立验证后稳健转正，再考虑条件策略。

---

### 缺失证据与后续需求

1. **Tick 数据或 1m K 线**：若 `ambiguous_path` > 15% 且影响结论，当前 4h 粒度不够，需要更高频数据确定 TP/SL 触发顺序。
2. **实时 regime 分类器**：若希望基于 regime 条件触发不同出口，需要先验证分类器的准确率、滞后性和转换期表现。
3. **Out-of-sample 币池**：当前使用 current-survivor，引入幸存者偏差。若某个组件在两窗表现稳健，下一张卡片应使用时点币池（如入场时市值前 50）或前向扩展的币池。
4. **滑点模型**：当前只用 taker 费用，未建模滑点。若 ATR SL 触发时市场快速下跌，实际成交价可能比 SL 水平更差。近窗 stress 成本应包含滑点估计。
5. **入场时机优化**：若 Phase 1 显示 MFE 充足但 Phase 2 显示早期 MAE 过深，问题可能不是出口几何，而是入场时机（如 4h 收盘入场 vs. 突破后回调入场）。

---

### 对 GPT 方案的挑战总结

**GPT 的 2×2 能回答什么**：

- 在路径竞争校正后,TP 和 SL 各自的平均效应方向和量级
- 是否存在负交互（即两者同时调整反而更差）

**不能回答什么**：

- 改善是否源于毛收益增加还是成本结构变化（需 Phase 2 分解）
- 入场是否有足够毛优势支持任何短距离出口（需 Phase 1 前置）
- 哪些具体交易被 ATR SL 过早截断、损失了多少 MFE（需逐笔状态转移）
- 4h 同根顺序不确定性是否影响结论（需双假设验证）

**更高信息量的设计**：

Phase 1 + Phase 2 的组合——先确认毛空间存在,再用状态转移直接定位改善与抵消的来源,比 2×2 更直接且避免了路径竞争的加法假设。2×2 只在"Phase 2 显示混合效应、无法判断主因"时才必要。

---

### 最终建议

1. **立即执行 Phase 1**：这是 20 分钟的计算,能快速判断是否值得继续。若两窗 MFE 充足率 < 60%,直接停止,转向入场改进。

2. **Phase 1 通过后执行 Phase 2**：这是核心诊断,必须做。输出完整的逐笔字段和状态转移汇总表。

3. **根据 Phase 2 结果决定是否需要 Phase 3**：
   - 若某一转移主导且方向明确 → 跳过 Phase 3,直接生成单变量卡片
   - 若多个转移混合 → 执行 Phase 3 拆分主效应
   - 若成本抵消毛改善 → 停止,不做 Phase 3

4. **Phase 4 永远是附录**,不触发行动,除非某个子集有压倒性证据且独立验证过。

5. **若 Phase 2 显示成本主导或 MFE 不足,最合理的结论就是 H4 成立**：暂停出口研究,优先验证 B all-events 入场在 48h 内是否有足够延续性,或考虑更长持仓周期、不同入场信号、或放弃该方向。

不要因为"已经做了 ATR 实验"就强行继续优化出口。机制诊断的目的是告诉你何时停止。

<!-- 由 Claude Code 追加；Codex 不代写。 -->

## Round 1：GPT 归纳与追问

### 已达成共识

- 不再扫描 ATR 倍数、NATR 阈值或持仓时间；当前任务是机制归因，不是优化。
- 不能只看 full ATR 与 fixed 的整体净收益，需要逐笔拆分毛收益变化、成本变化、状态变化和同根顺序敏感性。
- regime/NATR 当前只能作为解释性附录。近窗 `RISK_ON` 的 ATR 策略自身仍未转正，现有证据不足以支持条件化生产规则。
- 任何新实验卡片都必须要求两窗同向、成本压力和 stop-first/target-first 不翻转，并且不能由小样本切片单独触发。
- 当前证据更接近“改善不够且可能被成本抵消”，而不是“ATR 出口已经可用”。

### 关键分歧与方法修正

1. **不能把事后 MFE 当作出口研究的硬前置闸门。** MFE 是事后上界，不是可执行收益；一笔交易可以先经历不可承受 MAE、随后才形成高 MFE，也可以只有无法实时识别的瞬时高点。`MFE > 2×cost` 只能说明价格曾提供空间，不能证明存在可交易毛优势，更不能据此判定或否定 H4。Claude 提出的 `55%/60%` 和 `1.0R/1.2R` 阈值目前没有来自策略经济学、既有基线或抽样误差的依据，不应成为停止条件。
2. **状态转移是描述性配对，不是组件级因果反事实。** full fixed 与 full ATR 的 `TIME→TP`、`TP→SL` 等转移同时包含 TP 与 SL 两项变化，按转移分组还是对处理后结果的选择。它能解释“净差值由哪些交易贡献”，但不能单独证明贡献来自 TP 还是 SL。真正定义了四个出口政策的 2×2 才能回答组件政策效应与交互，尽管仍需谨慎解释路径竞争。
3. **现有 R 口径必须显式处理。** 当前实现中 `net_r = net / planned_risk`，而 `planned_risk` 由每个模型自己的止损距离决定。它适合比较“每个政策按各自初始风险等风险配置后的结果”，但 `fixed_R` 与 `ATR_R` 的分母不同。逐笔 `delta_gross_R`、`delta_cost_R` 和 2×2 主效应若不同时报告共同单位，会把收益路径变化与风险分母变化混在一起。
4. **Claude 的 Phase 1 字段存在单位歧义。** `MFE_gross` 被描述成相对价格收益，`cost_R` 则是风险单位，二者不能直接比较；`0.5×ATR` 又是第三种单位。费用也不应只用简化的 `(fee_bps×2)/NATR` 推导，现有回放已有实际 entry/exit fee 与 slippage，应直接使用相同成本引擎。
5. **2×2 不需要因计算量而延期。** baseline 与 full ATR 已有，只缺 `ATR_TP+fixed_SL`、`fixed_TP+ATR_SL` 两个政策，且现有回放已具备 stop-first/target-first 和多成本分支。它可以与路径诊断一次生成；没有必要先用任意 MFE 阈值决定是否“允许”运行两个只读政策。

### 新核对到的实现证据

- `scripts/research_atr_adaptive_short_exit.py` 在每个政策下按该政策的 planned stop 计算 `planned_risk`，再计算 `net_r` 和 `cost_r`；因此机制报告必须同时给出：
  - 不依赖止损分母的 `gross_return_pct / cost_pct / net_return_pct`；
  - 各政策自身风险单位 `own_risk_R`，用于等风险配置比较；
  - 一个预先固定的共同参考风险单位，例如 fixed 3% 风险或入场 ATR 风险，用于逐笔差值归因。
- 当前回放已经同时执行 `stop_first` 与 `target_first`，无需等 ambiguous 比例超过任意门槛才看第二种顺序；主结论从一开始就应报告两种边界。

## Round 2：Codex 追问

请基于以上修正，重新给出一个**不依赖任意 MFE 硬阈值、单位一致、能区分描述性贡献与政策效应**的最小诊断协议。重点回答以下问题：

1. 你是否同意取消“Phase 1 通过后才运行 2×2”的硬闸门，改为一次只读运行同时生成四个冻结政策、路径上界和状态转移？如果仍不同意，请说明只增加两个政策回放会带来什么具体统计或决策风险，而不是计算成本。
2. 请严格区分三类问题及相应证据：
   - **入场是否提供价格空间**：48h MFE/MAE、first-passage，仅作为描述性路径上界；
   - **某个完整出口政策是否可执行地改善结果**：四政策实际退出的 gross/cost/net；
   - **哪一组件造成改善或抵消**：2×2 的政策对比与交互，并承认 TP/SL 路径竞争是政策机制的一部分，而不是可被完全“校正”掉的偏差。
3. 为逐笔与汇总指标指定统一单位。至少说明：
   - 哪些指标用原始百分比；
   - 哪些用各政策 own-risk R；
   - 是否需要共同参考 R，若需要应选 fixed 3% 还是 entry ATR，为什么；
   - gross、fee、slippage、net 必须如何恒等回对。
4. 重新定位状态转移分析。它应如何用于解释总体差值的贡献，同时避免把 `TIME→TP` 或 `TP→SL` 直接解释成 TP/SL 的因果效应？请给出与 2×2 结果互相验证而非“冲突时永远优先状态转移”的规则。
5. 重新定义 H4“入场毛优势不足”的判定。禁止使用目前无依据的 `55%/60%`、`1.0R/1.2R` 硬阈值。请给出以下两种之一：
   - 有经济含义且可追溯的阈值来源；或
   - 不设固定阈值，改用跨窗方向、配对区块区间、可执行政策上界与成本压力的一组判据。
6. 给出最终最小输出和停止规则，要求：
   - 四政策、两窗口、三成本口径和两种同根顺序一次完成；
   - 主结果同时报告绝对净收益和 own-risk R，不因只在 R 上改善而忽略现金期望仍为负；
   - MFE/MAE 不能触发参数实验，只能解释为什么实际政策失败；
   - 只有单组件政策在两窗的**绝对扣费后期望**均转正、相对 baseline 的配对差值对不利方向有足够排除、stress 与同根顺序不翻号，才允许形成后续独立验证卡片；否则 `revert` 当前 ATR 定义或 `defer` 更广义 ATR 方向。

请在第二轮明确指出：第一轮哪些建议你保留，哪些阈值或因果表述需要撤回。目标是得到一张可以直接冻结的诊断规格，而不是继续扩展分析层次。

<!-- 由 Codex 追加。 -->

## Round 2：Claude 回复

### 对 Round 1 的撤回与保留

**撤回的内容**：

1. **Phase 1 作为硬闸门的所有阈值**：`55%/60%` MFE 充足率、`1.0R/1.2R` 中位数阈值、"Phase 1 不通过则停止"的决策逻辑——这些都是我在没有经济学依据的情况下设定的任意门槛，撤回。
2. **"Phase 2 与 Phase 3 冲突时优先 Phase 2"**：状态转移是描述性分组，不是因果识别；它不能替代 2×2 的组件拆分，也不存在"更可信"的优先级。撤回。
3. **MFE 可以判定 H4 的表述**：MFE 是事后路径上界，不能证明入场有可执行毛优势。我错误地把"价格曾提供空间"等同于"存在可交易优势"。撤回。
4. **成本公式 `(fee_bps×2)/NATR` 的简化推导**：现有回放已有实际成本引擎，不应用近似公式。撤回。
5. **Phase 1/2/3/4 的顺序结构**：这种分阶段设计隐含了"先判断是否值得研究出口、再研究出口"的逻辑，但实际上四个政策回放是一次性完成的只读分析，不存在"运行 Phase 1 后决定是否运行 Phase 2"的计算成本或风险。撤回分阶段框架。

**保留的内容**：

1. **MFE/MAE 作为描述性路径上界**：它们可以解释"为什么某个政策未能捕获更多收益"，但不用于触发或禁止实验。保留作为解释性指标。
2. **状态转移分析的描述性价值**：按 `fixed → ATR` 的 9 种转移分组，可以直观展示"哪些交易改变了状态、贡献了多少净差值"，作为对 2×2 主效应的补充说明。保留作为描述性汇总，但不赋予因果解释。
3. **路径竞争的承认**：TP 和 SL 在时间轴上竞争，这是政策机制的一部分，不是可被"校正"的偏差。2×2 的交互效应反映了这种竞争。保留。
4. **同根顺序敏感性检查**：stop-first 与 target-first 两种边界必须同时报告，主结论必须在两种假设下同向才成立。保留。
5. **单位一致性要求**：逐笔差值和主效应必须使用共同单位，避免把收益路径变化与风险分母变化混淆。保留并在下文明确定义。

---

### 重新设计的最小诊断协议

**核心原则**：一次性生成四政策、两窗口、三成本、两顺序的完整回放，不设 MFE 硬闸门；用经济学标准而非任意阈值判定是否形成后续卡片。

---

### 1. 同意取消 Phase 1 硬闸门

**回答**：同意。

**理由**：

- 四个政策（`fixed+fixed`、`ATR_TP+fixed_SL`、`fixed_TP+ATR_SL`、`ATR+ATR`）都是冻结参数的只读回放，计算成本与运行两个政策相同。
- MFE 充足率无法回答"某个政策是否可执行地改善结果"——即使 MFE 很高，如果 ATR SL 过早止损，政策仍然失败；即使 MFE 很低，如果 ATR TP 缩短了持仓时间且降低了成本，政策仍可能改善。
- 唯一有意义的停止条件是"所有政策的绝对期望都未转正、且组件政策相对 baseline 无稳健改善"——这需要先跑完四政策才能判断。

**无风险**：增加两个政策回放没有统计风险（样本不变）、没有决策风险（不触发生产配置）、没有数据窥探风险（四政策都是预注册的组件组合）。

---

### 2. 三类问题的严格区分

| 问题类型 | 用途 | 证据来源 | 不能用于 |
|---------|------|---------|---------|
| **入场是否提供价格空间** | 解释为什么实际政策未能捕获更多收益；判断"最优出口上界"与实际政策的差距 | 48h 内 MFE/MAE、first-reach 竞争、可达集合 | 不能判定 H4；不能触发或禁止政策实验；不能替代实际政策的期望估计 |
| **某个完整出口政策是否改善** | 判断该政策在两窗的绝对期望是否转正；判断相对 baseline 的配对差值是否稳健 | 四政策实际退出的 gross_pct、cost_pct、net_pct、net_R（own-risk） | 不能单独回答改善来自 TP 还是 SL |
| **哪一组件造成改善或抵消** | 识别 TP/SL 的主效应和交互；为单组件政策验证提供依据 | 2×2 政策对比、主效应/交互效应、路径竞争频数 | 不能忽略交互效应；不能假设主效应在所有子集都成立 |

**关键承认**：TP/SL 路径竞争是政策机制的一部分。`ATR_TP + fixed_SL` 中，fixed SL 更宽松会让更多交易"活到" ATR TP，这不是 ATR TP 的"纯效应"，而是该组合政策的实际表现。2×2 的主效应只是边际平均，交互效应若显著则说明 TP/SL 不可独立优化。

---

### 3. 统一单位定义

#### 3.1 逐笔字段

每笔交易在每个政策下输出：

```python
{
  # 标识
  "trade_id": str,
  "window": "early" | "near",
  "symbol": str,
  "entry_time": datetime,
  "entry_price": float,
  "regime": "RISK_ON" | "NEUTRAL" | "RISK_OFF",
  "NATR_at_entry": float,
  "ATR20_at_entry": float,

  # 政策参数（冻结）
  "policy": "fixed+fixed" | "ATR_TP+fixed_SL" | "fixed_TP+ATR_SL" | "ATR+ATR",
  "cost_regime": "taker" | "maker" | "stress",
  "tie_break": "stop_first" | "target_first",

  # 退出结果
  "exit_time": datetime,
  "exit_price": float,
  "outcome": "TP" | "SL" | "TIME",

  # 原始百分比（不依赖风险分母）
  "gross_return_pct": float,  # (exit_price - entry_price) / entry_price
  "entry_fee_pct": float,     # 实际入场费用 / entry_price
  "exit_fee_pct": float,      # 实际退出费用 / exit_price，转换为入场价基准
  "entry_slippage_pct": float,
  "exit_slippage_pct": float,
  "total_cost_pct": float,    # sum of above four
  "net_return_pct": float,    # gross_return_pct - total_cost_pct

  # 该政策自身风险单位（用于等风险配置比较）
  "own_planned_risk_pct": float,  # 该政策的止损距离 / entry_price
  "own_risk_R": float,            # net_return_pct / own_planned_risk_pct
  "own_cost_R": float,            # total_cost_pct / own_planned_risk_pct

  # 共同参考风险单位（用于逐笔差值归因，见下文）
  "common_ref_risk_pct": float,  # 固定为 baseline 的 3% 止损
  "net_return_common_R": float,  # net_return_pct / common_ref_risk_pct
  "cost_common_R": float,        # total_cost_pct / common_ref_risk_pct

  # 路径上界（仅用于解释）
  "MFE_pct": float,              # 48h 内最高点相对入场价
  "MAE_pct": float,              # 48h 内最低点相对入场价
  "MFE_time": datetime,
  "first_reach": str,            # "fixed_TP" | "ATR_TP" | "fixed_SL" | "ATR_SL" | "TIME"
  "reachable_set": list[str],    # 实际退出前曾触及的水平
  "ambiguous_bar": bool,         # 同一根 4h K 同时触及 TP 和 SL
  "uncaptured_pct": float        # MFE_pct - gross_return_pct（离开桌面的钱）
}
```

#### 3.2 共同参考风险单位的选择

**选择**：使用 **baseline fixed 3% 止损**作为共同参考 R。

**理由**：

1. **固定性**：baseline 止损在所有交易中都是 3%，不因币种、时间或波动率变化，避免了分母漂移。
2. **可比性**：所有逐笔差值（`delta_net_common_R`、`delta_cost_common_R`）使用相同分母，可以直接加总和比较。
3. **经济含义**：以 baseline 风险为基准，回答"如果按 baseline 风险配置，ATR 政策改变了多少 R"——这正是"组件归因"的目标。

**不选 entry ATR 的理由**：ATR 在不同交易、不同币种间差异巨大，用它做分母会把"ATR 政策选择了不同风险尺度"与"ATR 政策改变了收益路径"混在一起。

#### 3.3 恒等式验证

每笔交易必须满足：

```python
# 百分比恒等
assert abs(net_return_pct - (gross_return_pct - total_cost_pct)) < 1e-6

# own-risk R 恒等
assert abs(own_risk_R - (net_return_pct / own_planned_risk_pct)) < 1e-6
assert abs(own_cost_R - (total_cost_pct / own_planned_risk_pct)) < 1e-6

# common-risk R 恒等
assert abs(net_return_common_R - (net_return_pct / common_ref_risk_pct)) < 1e-6
assert abs(cost_common_R - (total_cost_pct / common_ref_risk_pct)) < 1e-6

# 成本分解恒等（若有细分）
assert abs(total_cost_pct - (entry_fee_pct + exit_fee_pct + entry_slippage_pct + exit_slippage_pct)) < 1e-6
```

---

### 4. 状态转移分析的重新定位

**用途**：描述性地展示"baseline → ATR 的净差值由哪些交易贡献"，作为 2×2 主效应的补充说明，不赋予因果解释。

**方法**：

对同一笔交易，比较 `fixed+fixed` 与 `ATR+ATR` 在相同成本、相同顺序假设下的状态，分为 9 种转移：

```
TP→TP, TP→SL, TP→TIME,
SL→TP, SL→SL, SL→TIME,
TIME→TP, TIME→SL, TIME→TIME
```

汇总表（分窗口、成本、顺序）：

```
Transition  Count  Avg_delta_net_pct  Avg_delta_net_common_R  Median_delta_net_common_R  Total_contribution_common_R
TP→TP       N1     ...                ...                     ...                        N1 × Avg
TP→SL       N2     ...                ...                     ...                        N2 × Avg
...
```

**与 2×2 的互相验证规则**：

1. **加总一致性**：所有转移的 `Total_contribution_common_R` 之和必须等于 `mean(ATR+ATR) - mean(fixed+fixed)` 的 common_R 差值（在相同成本、顺序下）。
2. **方向一致性**：若 `TIME→TP` 贡献为正且 `TP→SL` 贡献为负，2×2 应显示 TP 主效应为正、SL 主效应为负或负交互——但不能直接从转移推断主效应大小，因为转移是 full fixed vs full ATR 的对比，包含了两个组件的联合变化。
3. **冲突处理**：若状态转移显示某类转移贡献很大，但 2×2 显示对应组件主效应很小，优先检查**交互效应**——很可能该转移的贡献依赖于另一组件的配合。不存在"永远优先状态转移"或"永远优先 2×2"的规则，而是用两者的不一致来识别路径竞争。

**明确不能做的推断**：

- 不能从 `TIME→TP` 的正贡献推断"TP 组件单独有效"——因为该转移同时改变了 TP 和 SL。
- 不能从 `TP→SL` 的负贡献推断"SL 组件单独有害"——可能是 ATR TP 缩短了持仓、暴露给了 ATR SL 更多早期波动。

---

### 5. H4 判定标准的重新定义

**H4**：退出调整只能重新分配 TP/SL/TIME，入场毛优势不足；手续费和滑点压力上升后，任何短距离自适应出口都难以转正。

**判定标准（不设固定阈值，用一组判据）**：

H4 成立需要**同时满足**以下全部条件：

1. **绝对期望未转正**：
   - 两窗所有四个政策在 taker 成本下的 `mean(net_return_pct)` 均 ≤ 0
   - 两窗所有四个政策在 taker 成本下的 `mean(net_return_common_R)` 均 ≤ 0

2. **跨窗方向不一致或全部为负**：
   - 若某政策在早窗 `mean(net_return_pct) > 0` 但近窗 `mean(net_return_pct) < 0`，标记为窗口依赖，支持 H4
   - 若某政策在两窗都 `mean(net_return_pct) ≤ 0`，支持 H4

3. **配对区块区间跨零或负偏**：
   - 14 日配对区块的 95% CI 跨零，说明改善不稳健
   - 若早窗 CI 右端为正但近窗 CI 右端为负，支持 H4

4. **成本压力主导**：
   - 在 stress 成本下，所有政策相对 baseline 的 `mean(delta_net_common_R)` 翻负或恶化 > 0.05R
   - 近窗 `mean(cost_common_R)` 相对早窗上升 > 30%（当前证据显示上升 53%）

5. **路径上界与实际捕获的差距不可归因于出口几何**：
   - 若 MFE 中位数 > 2.0R（common_R），但所有政策的 `mean(gross_return_common_R)` < 0.5R，且 `first_reach` 显示 TIME 占主导（> 40%），说明问题是持仓时间不够，不是 TP/SL 几何
   - 但这只是**补充证据**，不能单独触发 H4——因为 MFE 是事后上界

6. **组件政策无单独改善**：
   - `ATR_TP+fixed_SL` 和 `fixed_TP+ATR_SL` 两个单组件政策，在两窗的 `mean(net_return_pct)` 均 ≤ 0，或虽为正但配对差值 CI 跨零

**H4 不成立**（可以继续研究出口）需要**至少一个**条件：

- 某个单组件政策在两窗的 `mean(net_return_pct)` 均 > 0，且配对差值 95% CI 下界 > 0，且 stress 成本与同根顺序不翻号

**关键**：不设任意的 55%/60% 或 1.0R/1.2R 阈值，而是用"所有政策期望都未转正 + 成本压力主导 + 跨窗不一致"的组合判定。

---

### 6. 最终最小输出和停止规则

#### 6.1 一次性完成的回放范围

- **政策**：4 个（`fixed+fixed`, `ATR_TP+fixed_SL`, `fixed_TP+ATR_SL`, `ATR+ATR`）
- **窗口**：2 个（early `[2024-07-01, 2025-06-01)`, near `[2025-06-01, 2026-06-01)`）
- **成本口径**：3 个（taker, maker, stress）
- **同根顺序**：2 个（stop_first, target_first）
- **总组合**：4 × 2 × 3 × 2 = 48 种配置，对同一批入场（early 858 笔 + near 628 笔）回放

#### 6.2 主结果报告格式

**汇总表 1：政策表现（主口径 = taker + stop_first）**

```
Policy              Window  N    Mean_net_pct  Median_net_pct  Mean_net_common_R  Median_net_common_R  Mean_own_R  WinRate  Mean_cost_pct  Paired_block_95CI_common_R
fixed+fixed         early   858  -0.186%       ...             -0.0567            ...                  -0.0567     38.81%   ...            [...]
fixed+fixed         near    628  -0.165%       ...             -0.0500            ...                  -0.0500     40.76%   ...            [...]
ATR_TP+fixed_SL     early   858  ...           ...             ...                ...                  ...         ...      ...            [...]
ATR_TP+fixed_SL     near    628  ...           ...             ...                ...                  ...         ...      ...            [...]
fixed_TP+ATR_SL     early   858  ...           ...             ...                ...                  ...         ...      ...            [...]
fixed_TP+ATR_SL     near    628  ...           ...             ...                ...                  ...         ...      ...            [...]
ATR+ATR             early   858  -0.013%       ...             -0.0317            ...                  -0.0317     40.21%   ...            [...]
ATR+ATR             near    628  -0.016%       ...             -0.000008          ...                  -0.000008   43.15%   ...            [...]
```

**汇总表 2：2×2 主效应与交互（分窗口，common_R 单位）**

```
Window  TP_effect  SL_effect  Interaction  TP_effect_stderr  SL_effect_stderr  Interaction_stderr
early   ...        ...        ...          ...               ...               ...
near    ...        ...        ...          ...               ...               ...
```

计算公式：
```python
TP_effect = (mean[ATR_TP+fixed_SL] + mean[ATR+ATR]) / 2 - (mean[fixed+fixed] + mean[fixed_TP+ATR_SL]) / 2
SL_effect = (mean[fixed_TP+ATR_SL] + mean[ATR+ATR]) / 2 - (mean[fixed+fixed] + mean[ATR_TP+fixed_SL]) / 2
Interaction = mean[ATR+ATR] - mean[ATR_TP+fixed_SL] - mean[fixed_TP+ATR_SL] + mean[fixed+fixed]
```

**汇总表 3：同根顺序敏感性（分窗口、主口径）**

```
Policy              Window  Stop_first_mean_net_pct  Target_first_mean_net_pct  Delta_pct  Direction_flips
fixed+fixed         early   ...                      ...                        ...        No
...
ATR+ATR             near    ...                      ...                        ...        No/Yes
```

**汇总表 4：成本压力测试（分窗口、政策）**

```
Policy              Window  Taker_mean_net_common_R  Stress_mean_net_common_R  Delta_R  Flips_negative
fixed+fixed         early   -0.0567                  ...                       ...      ...
...
```

**汇总表 5：状态转移贡献（baseline → full ATR，taker + stop_first）**

```
Window  Transition  Count  Avg_delta_net_pct  Avg_delta_net_common_R  Total_contribution_common_R  Median_uncaptured_pct
early   TP→TP       ...    ...                ...                     ...                          ...
early   TP→SL       ...    ...                ...                     ...                          ...
...
```

**汇总表 6：路径上界（描述性，不触发决策）**

```
Window  MFE_median_pct  MFE_p25_pct  MFE_p75_pct  MAE_median_pct  First_reach_TIME_pct  Ambiguous_bar_pct
early   ...             ...          ...          ...             ...                   ...
near    ...             ...          ...          ...             ...                   ...
```

#### 6.3 停止规则与决策树

```
IF (所有四政策在两窗的 mean(net_return_pct) 均 ≤ 0
    AND 配对区块 95% CI 均跨零或负偏
    AND stress 成本下相对差值翻负或恶化 > 0.05R
    AND 近窗成本占 R 上升 > 30%):
    结论 = "H4 成立：入场毛优势不足，revert 当前 ATR 定义"
    不生成后续卡片

ELSE IF (某个单组件政策【ATR_TP+fixed_SL 或 fixed_TP+ATR_SL】满足：
         两窗 mean(net_return_pct) 均 > 0
         AND 两窗配对差值 95% CI 下界均 > 0
         AND stress 成本下不翻负
         AND stop_first 与 target_first 方向一致):
    结论 = "该组件稳健改善，生成单组件验证卡片"
    卡片内容：仅改变该组件，用新窗口 + out-of-sample 币池验证

ELSE IF (full ATR 在两窗 mean(net_return_pct) 均 > 0
         BUT 配对差值 CI 跨零或 stress 翻负
         AND 2×2 显示显著负交互 < -0.10R):
    结论 = "TP/SL 存在负交互，当前 5:3 比例不当，defer ATR 方向"
    建议：若继续研究 ATR，需重新校准 TP/SL 比例或引入条件规则
    不生成当前定义的验证卡片

ELSE:
    结论 = "改善不稳健或方向不一致，defer 当前 ATR 定义"
    建议：优先验证入场延续性、考虑更长持仓周期、或改进入场信号
    不生成当前定义的验证卡片
```

#### 6.4 MFE/MAE 的使用约束

- **仅用于事后解释**：若某政策失败（期望为负），检查 MFE/MAE 和 `uncaptured_pct`，解释"是因为价格空间不足（MFE 低），还是出口几何未捕获（MFE 高但 uncaptured 大）"。
- **不触发实验**：无论 MFE 多高或多低，都不能触发新的 TP/SL 参数扫描或持仓时间调整。
- **不判定 H4**：MFE 低可以支持 H4，但不能单独判定 H4——必须结合实际政策的期望、成本压力和跨窗一致性。

#### 6.5 生成验证卡片的最低标准

必须**同时满足**：

1. 两窗 `mean(net_return_pct) > 0`（绝对期望转正）
2. 两窗配对差值 `mean(delta_net_common_R)` 的 95% CI 下界 > 0（相对改善稳健）
3. Stress 成本下 `mean(net_return_pct) > -0.05%`（成本压力不翻负太多）
4. Stop_first 与 target_first 的 `mean(net_return_pct)` 同号且差异 < 0.10%（顺序稳健）
5. 改善不局限于单一 regime 或 NATR 子集，或该子集样本量 > 100 且有独立触发机制（当前不满足）

若任一条件不满足，判定为 `revert`（当前定义失败）或 `defer`（方向值得研究但当前定义不够）。

---

### 最终协议摘要

1. **一次性回放**：4 政策 × 2 窗口 × 3 成本 × 2 顺序 = 48 种配置，无 MFE 硬闸门。
2. **单位一致**：主结果同时报告 `net_pct`（绝对期望）和 `net_common_R`（以 baseline 3% 风险为基准的归因单位）。
3. **三类证据分离**：MFE/MAE 仅解释、不决策；实际政策期望判定是否改善；2×2 拆分组件效应。
4. **状态转移为补充**：描述性展示贡献分布，与 2×2 互相验证，冲突时检查交互效应。
5. **H4 判定**：不设任意阈值，用"全部政策未转正 + 成本压力 + 跨窗不一致"组合判定。
6. **停止规则**：仅当单组件政策在两窗绝对期望均转正、配对差值 CI 不跨零、stress 和顺序不翻号，才生成验证卡片；否则 revert 或 defer。

这是可以直接冻结并实施的最小诊断规格。

<!-- 由 Claude Code 追加；Codex 不代写。 -->

## Round 2：GPT 归纳与最终审计追问

### 已解决的核心分歧

- Claude 明确撤回了第一轮的 MFE 充足率阈值、MFE 判定 H4、状态转移优先于 2×2、近似成本公式和分阶段硬闸门。
- 双方同意一次性完成四个冻结政策的回放；MFE/MAE 只作描述性路径上界；状态转移只解释 full-fixed 到 full-ATR 的贡献构成；2×2 用于估计四个已定义政策的边际平均差异与交互。
- 双方同意主结果必须同时报告不依赖风险分母的绝对净收益、各政策 own-risk R 和共同参考 R，并要求 gross/cost/net 逐笔恒等闭合。
- 双方同意：只有单组件政策在两个已烧窗口都绝对转正、相对 baseline 的配对区块区间排除不利方向、成本压力与同根顺序不翻号，才有资格生成后续独立验证卡片；否则不修改生产。

### 仍需修正的四个实施级问题

1. **成本分支名称与现有冻结协议不一致。** 当前回放的三种成本是 `taker / stress / legacy_fee`，不是 `taker / maker / stress`。最终协议必须复用现有 `short_horizon_core.COSTS` 和 `BRANCHES`，不能临时引入未定义的 maker 分支。
2. **共同参考 R 应复用 baseline 实际 planned risk，而不是名义 3%。** 现有实现的 baseline `planned_risk` 包含入场成本及计划止损成交的 fee/slippage，`net_r = net / planned_risk`。为使 common-R 与现有 fixed own-R 精确一致，应对每笔、每个成本口径使用同一 `fixed+fixed` baseline 产生的 `planned_risk_pct` 作为所有四政策的共同分母，而不是硬编码 `3%`。该共同分母在政策间固定，但随成本口径合理变化。
3. **稳健性闸门不能再次引入无依据的容忍阈值。** 第二轮提出 stress 下 `mean(net_return_pct) > -0.05%`、同根顺序差异 `<0.10%`、成本上升 `>30%`、恶化 `>0.05R` 等数值，这些没有预先经济依据。当前卡片资格应更简单：单组件政策在 `taker` 与 `stress` 下两窗绝对净期望都必须 `>0`，stop-first 与 target-first 下两窗也都必须 `>0`，且相对 baseline 的预注册配对区块区间下界不得小于 0。`legacy_fee` 只作历史可比敏感性，不作为主资格门。
4. **不能把“四个测试出口均失败”命名为“入场毛优势不足已成立”。** 四个冻结政策都不盈利，只能支持“当前固定/ATR 组件集合没有捕获可执行正期望”，不能排除其他实时退出，也不能单独证明 B 入场没有毛优势。H4 应拆成：
   - `H4a`：当前四个冻结出口政策均不能把 B all-events 转成稳健正期望；可由本诊断判定。
   - `H4b`：B all-events 入场本身缺乏可执行毛优势；本诊断最多提供支持性证据，必须由独立的入场延续性/可执行路径研究判定。

## Round 3：Codex 最终审计请求

这是最后一轮，不再增加分析层次。请只审计并收敛以下内容：

1. 明确接受或反对上述四项修正，并说明任何反对会怎样改变最终决策。
2. 给出最终冻结规格的简明版本，必须使用：
   - `4 policies × 2 windows × 3 costs(taker/stress/legacy_fee) × 2 tie-breaks`；
   - common-R = 同笔、同成本口径下 `fixed+fixed` 的实际 `planned_risk_pct`；
   - 原始百分比、own-risk R、common-R 三套单位并列；
   - 状态转移、2×2、MFE/MAE 的角色边界保持第二轮共识。
3. 最终只允许三类裁决：
   - `component_validation_eligible`：某个单组件政策满足两窗绝对净期望、配对差值、stress 与双同根顺序全部通过；只授予新窗口/point-in-time 币池独立验证资格，不直接 keep。
   - `reject_current_atr_components`：四政策或单组件未通过，否定当前 `ATR20 + 1ATR SL + 5/3ATR TP` 组件定义，不外推所有 ATR 退出。
   - `measurement_insufficient`：4h 同根顺序、数据缺口或成本恒等无法闭合，无法判断当前定义。
4. 对于 `H4a/H4b`，明确本诊断能判定什么、不能判定什么，并给出若 `reject_current_atr_components` 后的最小下一步：是回到入场延续性研究，还是仍有理由继续出口研究。不得建议新的 ATR 倍数或阈值扫描。
5. 给出最终支持、否定、证据不足标准，删除第二轮残留的 `-0.05%`、`0.10%`、`30%`、`0.05R` 等未经依据的容忍门槛。

如果接受上述修正，请明确写出”协议已可冻结”；如果仍有实质分歧，请只保留会改变是否实施该诊断的分歧，交由用户裁决。

<!-- 由 Codex 追加。 -->

## Round 3：Claude 最终审计回复

### 对四项修正的接受与澄清

**1. 成本分支名称：完全接受**

使用现有 `taker / stress / legacy_fee`，不引入未定义的 maker。修正所有提到 maker 的地方为 legacy_fee。

**2. 共同参考 R 使用实际 planned_risk：完全接受**

修正为：对每笔交易、每个成本口径，使用该笔、该口径下 `fixed+fixed` 政策产生的实际 `planned_risk_pct` 作为所有四政策的共同分母。这确保了 common-R 与现有 fixed own-R 在同一口径下精确一致，同时允许 planned_risk 随成本口径合理变化（因为入场成本和计划止损成交的 fee/slippage 会随口径变化）。

**3. 稳健性闸门删除无依据阈值：完全接受**

删除所有 `-0.05%`、`0.10%`、`30%`、`0.05R` 等数值。修正为：单组件政策资格要求两窗在 `taker` 和 `stress` 下绝对净期望均 `>0`、在 `stop_first` 和 `target_first` 下两窗均 `>0`、且相对 baseline 的预注册配对区块区间下界 `≥0`。不设容忍度，严格符号要求。

**4. H4 拆分为 H4a 和 H4b：完全接受**

- **H4a**（本诊断可判定）：当前四个冻结出口政策均不能把 B all-events 转成稳健正期望。
- **H4b**（本诊断不能判定）：B all-events 入场本身缺乏可执行毛优势。本诊断最多提供支持性证据（如 MFE 低、成本占比高、TIME 主导），但无法排除其他实时退出政策的可能性，也无法证明入场延续性不足。H4b 必须由独立的入场延续性/可执行路径研究判定。

---

### 最终冻结规格（简明版本）

#### 回放范围

- **政策**：4 个（`fixed+fixed`, `ATR_TP+fixed_SL`, `fixed_TP+ATR_SL`, `ATR+ATR`）
- **窗口**：2 个（early `[2024-07-01, 2025-06-01)`，near `[2025-06-01, 2026-06-01)`）
- **成本口径**：3 个（`taker`, `stress`, `legacy_fee`）
- **同根顺序**：2 个（`stop_first`, `target_first`）
- **总配置**：4 × 2 × 3 × 2 = 48 种，对同一批入场（early 858 笔 + near 628 笔）

#### 单位体系

每笔交易在每个配置下输出三套单位：

1. **原始百分比**（不依赖风险分母）：
   - `gross_return_pct`、`total_cost_pct`、`net_return_pct`
   - 用于判断绝对期望是否转正

2. **Own-risk R**（各政策自身风险单位）：
   - `own_planned_risk_pct` = 该政策的实际 planned_risk（含入场成本和计划止损成交成本）
   - `own_risk_R = net_return_pct / own_planned_risk_pct`
   - 用于等风险配置比较

3. **Common-risk R**（共同参考风险单位）：
   - `common_ref_risk_pct` = 同笔、同成本口径下 `fixed+fixed` 的实际 `planned_risk_pct`
   - `net_return_common_R = net_return_pct / common_ref_risk_pct`
   - `cost_common_R = total_cost_pct / common_ref_risk_pct`
   - 用于逐笔差值归因和 2×2 主效应计算

**恒等式**：每笔必须满足
```python
net_return_pct = gross_return_pct - total_cost_pct
own_risk_R = net_return_pct / own_planned_risk_pct
net_return_common_R = net_return_pct / common_ref_risk_pct
```

#### 分析角色边界

| 分析类型 | 用途 | 不能用于 |
|---------|------|---------|
| **MFE/MAE 路径上界** | 解释为什么某政策未能捕获更多收益；描述价格路径特征 | 不能判定 H4a/H4b；不能触发参数实验；不能单独作为停止条件 |
| **状态转移（fixed→ATR）** | 描述性展示净差值由哪些交易贡献；与 2×2 互相验证 | 不能赋予因果解释（因为同时改变 TP 和 SL）；不能单独推断组件效应 |
| **2×2 主效应与交互** | 估计 TP/SL 的边际平均效应和交互；识别路径竞争 | 不能忽略交互效应；不能假设主效应在所有子集成立 |
| **四政策实际表现** | 判断绝对期望是否转正；判断相对 baseline 是否稳健改善 | 唯一决策依据 |

#### 主结果报告（主口径 = taker + stop_first）

**表 1：政策表现汇总**

```
Policy              Window  N    Mean_net_pct  Mean_net_common_R  Mean_own_R  WinRate  Paired_block_95CI_common_R
fixed+fixed         early   858  -0.186%       -0.0567            -0.0567     38.81%   [L_early, U_early]
fixed+fixed         near    628  -0.165%       -0.0500            -0.0500     40.76%   [L_near, U_near]
ATR_TP+fixed_SL     early   858  ...           ...                ...         ...      [...]
ATR_TP+fixed_SL     near    628  ...           ...                ...         ...      [...]
fixed_TP+ATR_SL     early   858  ...           ...                ...         ...      [...]
fixed_TP+ATR_SL     near    628  ...           ...                ...         ...      [...]
ATR+ATR             early   858  -0.013%       -0.0317            -0.0317     40.21%   [...]
ATR+ATR             near    628  -0.016%       -0.000008          -0.000008   43.15%   [...]
```

**表 2：稳健性检查**

```
Policy              Taker_early  Taker_near  Stress_early  Stress_near  Stop_first_early  Target_first_early  Stop_first_near  Target_first_near
                    mean_net_%   mean_net_%  mean_net_%    mean_net_%   mean_net_%        mean_net_%          mean_net_%       mean_net_%
fixed+fixed         -0.186       -0.165      ...           ...          -0.186            ...                 -0.165           ...
ATR_TP+fixed_SL     ...          ...         ...           ...          ...               ...                 ...              ...
fixed_TP+ATR_SL     ...          ...         ...           ...          ...               ...                 ...              ...
ATR+ATR             -0.013       -0.016      ...           ...          -0.013            ...                 -0.016           ...
```

**表 3：2×2 主效应（common_R，主口径）**

```
Window  TP_effect  SL_effect  Interaction  TP_stderr  SL_stderr  Int_stderr
early   ...        ...        ...          ...        ...        ...
near    ...        ...        ...          ...        ...        ...
```

**表 4：状态转移贡献（fixed→ATR，主口径）**

```
Window  Transition  Count  Avg_delta_net_common_R  Total_contribution_common_R
early   TP→TP       ...    ...                     ...
early   TP→SL       ...    ...                     ...
...     ...         ...    ...                     ...
```

**表 5：路径上界（描述性）**

```
Window  MFE_median_%  MAE_median_%  First_reach_TIME_%  Ambiguous_bar_%
early   ...           ...           ...                 ...
near    ...           ...           ...                 ...
```

---

### 三类裁决的判定标准

#### 1. `component_validation_eligible`（授予验证资格）

**必须同时满足**：

- 某单组件政策（`ATR_TP+fixed_SL` 或 `fixed_TP+ATR_SL`）在以下所有配置下 `mean(net_return_pct) > 0`：
  - early + taker
  - near + taker
  - early + stress
  - near + stress
  - early + stop_first（跨成本汇总）
  - near + stop_first（跨成本汇总）
  - early + target_first（跨成本汇总）
  - near + target_first（跨成本汇总）

- 该政策相对 baseline 的 14 日配对区块 95% CI（common_R 单位）在 early 和 near 下界均 `≥ 0`

**授予内容**：

- 生成单组件验证卡片，用新窗口（如 `[2026-06-01, 2027-06-01)`）+ point-in-time 币池（入场时市值前 N）验证
- 卡片内容：仅改变该组件，其余参数冻结（48h 上限、next-open 入场、B all-events）
- **不直接升级生产**，必须通过独立验证

#### 2. `reject_current_atr_components`（否定当前定义）

**触发条件**（任一成立）：

- 所有四个政策在 early + taker 或 near + taker 下 `mean(net_return_pct) ≤ 0`
- 所有单组件政策未满足 `component_validation_eligible` 的任一条件
- 某政策在 early 下 `mean(net_return_pct) > 0` 但 near 下 `mean(net_return_pct) ≤ 0`（窗口依赖）

**判定内容**：

- 否定当前 `ATR20 + 1ATR SL + 5/3ATR TP` 组件定义
- **不外推至所有 ATR 退出**——其他 ATR 周期、倍数或比例仍可研究，但需新的预注册卡片

**最小下一步**：

- **若 MFE 中位数 < 1.0R（common_R）且 first_reach_TIME > 50%**：问题可能是 48h 持仓约束过紧，建议优先研究更长持仓周期（如 7 日）或不同入场时机，而非继续短周期出口优化。

- **若 MFE 中位数 > 2.0R 但所有政策 mean(gross_return_common_R) < 0.8R**：说明价格提供了空间但四个冻结政策均未捕获，建议研究其他出口几何（如追踪止损、分批平仓）或实时状态触发，但不得扫描 ATR 倍数。

- **若近窗成本占 R 上升 > 50% 且 stress 下全部翻负**：成本压力是主要瓶颈，建议验证入场延续性是否足以覆盖更高成本，或考虑降低交易频率。

- **默认建议**：若以上特征均不显著，回到入场延续性研究——在更长持仓窗口（7-14 日）下验证 B all-events 是否有足够毛优势，再决定是否继续短周期出口研究。

#### 3. `measurement_insufficient`（无法判断）

**触发条件**（任一成立）：

- `ambiguous_bar` 占比 > 20%，且 stop_first 与 target_first 下某政策的 `mean(net_return_pct)` 符号翻转
- 某政策的逐笔数据中恒等式验证失败笔数 > 5%
- 数据缺口（如部分交易缺少 4h OHLC）导致无法计算 MFE/MAE 的笔数 > 10%

**判定内容**：

- 当前 4h 粒度或成本引擎无法支持可信判断
- 需要 tick 数据、1m K 线、或修复成本引擎后重新诊断

---

### H4a 与 H4b 的边界

#### 本诊断能判定的（H4a）

- 当前四个冻结出口政策（含两个单组件）均不能把 B all-events 在 48h 约束下转成稳健正期望
- 若四政策均失败，可判定 `reject_current_atr_components`

#### 本诊断不能判定的（H4b）

- **不能判定**：B all-events 入场本身是否缺乏可执行毛优势
  - 原因 1：MFE 是事后路径上界，不是可执行收益
  - 原因 2：本诊断只测试了四个冻结出口，无法排除其他实时退出政策（如追踪止损、状态机）
  - 原因 3：48h 约束可能过紧，更长持仓周期可能有不同结果

- **不能判定**：是否应放弃 B all-events 短周期方向
  - 需要独立的入场延续性研究：在无退出约束下，检查入场后价格路径的统计特征、可执行 MFE 的分布、与成本的比值

- **可提供支持性证据**：若 MFE 低、成本占比高、TIME 主导，支持 H4b；但不能单独判定

#### 若 reject 后的路径选择

**不建议**：

- 扫描新的 ATR 周期（ATR10、ATR30）
- 扫描新的 ATR 倍数（0.5ATR、2ATR）
- 扫描新的 TP/SL 比例（3:1、7:3）

**建议优先级**：

1. **若 MFE 特征支持 H4b**：优先做入场延续性研究，暂停短周期出口优化
2. **若 MFE 充足但政策未捕获**：研究其他出口机制（追踪止损、分批、状态机），但需新的预注册卡片
3. **若成本压力主导**：验证入场在更低频率或更长周期下是否有优势

---

### 最终裁决标准总结

| 条件 | 裁决 | 后续行动 |
|------|------|---------|
| 某单组件政策在两窗 × 两成本 × 两顺序下全部 `>0` 且配对区块 CI 下界 `≥0` | `component_validation_eligible` | 生成验证卡片，新窗口 + point-in-time 币池 |
| 所有政策或单组件未满足上述条件 | `reject_current_atr_components` | 根据 MFE/成本特征选择下一步：入场研究或其他出口机制 |
| 同根顺序翻号 >20%、恒等式失败 >5%、或数据缺口 >10% | `measurement_insufficient` | 需要更高频数据或修复成本引擎 |

---

## 协议已可冻结

上述规格已删除所有无依据阈值、明确了单位体系、区分了 H4a/H4b、限定了三类裁决和后续路径。

唯一剩余的实施级细节是：若 `component_validation_eligible`，验证卡片的新窗口应选择 `[2026-06-01, 2027-06-01)` 还是其他区间、point-in-time 币池应选市值前 50 还是前 100——这些不影响当前诊断的实施，可在生成卡片时决定。

协议可直接冻结并实施。

<!-- 由 Claude Code 追加；Codex 不代写。 -->

## Round 3：GPT 最终收口

### 已达成共识

- 取消 MFE/MAE 的硬闸门；它们只解释价格路径，不证明可执行优势，也不触发新参数实验。
- 一次性回放四个冻结政策、两个窗口、`taker/stress/legacy_fee` 三种成本和 `stop_first/target_first` 两种同根顺序，共 48 个配置。
- 同时报告原始百分比、各政策 own-risk R 和以同笔同成本 `fixed+fixed planned_risk_pct` 为分母的 common-R。
- 状态转移只解释 full-fixed 到 full-ATR 的差值构成；2×2 报告四个已定义政策的边际平均差异与交互；两者都不能越过实际政策绝对净期望成为决策依据。
- 当前诊断能判定 H4a（四个冻结出口能否形成稳健正期望），不能判定 H4b（B all-events 入场本身是否缺乏可执行毛优势）。
- 只有单组件政策通过两窗、成本压力、双同根顺序和配对区块差值，才授予新窗口与 point-in-time 币池验证资格；不直接 keep 或修改生产。

### 最终实施修正

Claude 第三轮仍在 `measurement_insufficient` 和 reject 后路径建议中使用了 `20%/5%/10%`、`1R/2R/0.8R/50%` 等未经依据的门槛。它们不进入冻结协议。最终采用以下无任意比例版本：

1. **候选资格按明确分支检查，不做跨成本汇总**：对 early/near 分别检查 `taker_stop_first`、`taker_target_first`、`stress_stop_first`、`stress_target_first`；四个分支的单组件绝对 `mean(net_return_pct)` 都必须大于 0。`legacy_fee` 仅作历史可比敏感性。
2. **配对稳健性**：主分支 `taker_stop_first` 下，单组件相对 `fixed+fixed` 的 14 日配对区块 95% 区间在 early/near 的下界均不得小于 0；其余三项资格分支的相对点估计不得为负。
3. **测量不足不使用比例门槛**：
   - 任一逐笔 gross-cost-net、own-R 或 common-R 恒等式失败，先判实现/数据错误并停止该分支裁决；
   - stop-first 与 target-first 使候选政策的绝对期望或资格结论翻号，判当前 4h 粒度不足以授予资格；
   - 数据缺口使四政策不能在完全相同的配对事件集上计算，或删失机制随政策而变化且无法统一，判证据不足；否则报告准确覆盖率并在同一完整样本上裁决。
4. **reject 后不按 MFE 阈值自动分流**：MFE/MAE 只能写入解释。若当前组件被否定，默认回到已登记的入场延续性与成本覆盖研究，先判断 H4b；只有独立研究形成可证伪依据后，才讨论其他实时退出机制。

### 三类最终裁决

- `component_validation_eligible`：至少一个单组件政策满足上述所有绝对收益、配对区间、stress 和双顺序要求；只生成独立验证卡片。
- `reject_current_atr_components`：测量闭合且同一配对样本可用，但两个单组件政策均未满足全部资格；否定当前 `ATR20 + 1ATR SL + 5/3ATR TP` 组件定义，不外推其他 ATR 定义。
- `measurement_insufficient`：恒等式、配对事件集、数据缺口或同根顺序翻号使当前 4h 回放无法可信裁决。

## 最终结论

- 结论：`retest`
- 当前决定：冻结并采用“四政策 2×2 + 成本/顺序边界 + 描述性路径归因”诊断协议；讨论结束，但尚未运行诊断、创建任务或修改任何策略配置。
- 理由：该协议能在不扫描新参数的前提下，区分“动态 TP 单独有效”“动态 SL 单独有效”“二者存在交互”“当前组件均无稳健正期望”，并避免用事后 MFE 或不同 R 分母制造错误原因解释。
- 主要风险：两个窗口均已烧且币池为 current-survivor；即使获得 `component_validation_eligible`，也只能进入新窗口和 point-in-time 币池独立验证。4h 同根顺序仍可能导致 `measurement_insufficient`。
- 下一步行动：等待用户明确授权后，将协议登记为独立诊断任务并执行 48 个冻结配置；若结果为 `reject_current_atr_components`，优先回到入场延续性和成本覆盖研究，不继续扫描 ATR 参数。
- 验证标准：逐笔恒等闭合、四政策同一事件集、两个窗口完整配对；按上述三类裁决规则输出绝对净收益、common-R 配对区间、own-risk R、成本与同根顺序敏感性。
- 需要更新的项目文件：当前仅更新本讨论记录与 `dailylog.md`；若用户授权执行，再更新 Taskboard、`TODO.md`、开发计划、`EXPERIMENT_LEDGER.md`、系统文档和 Obsidian 实验日志。
