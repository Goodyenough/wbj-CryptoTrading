# Handoff — 2026-06-12 00:00 +08:00

## 2026-10-15 18:47 +08:00

### 项目目录

`D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects`，当前分支 `main`；本次交接编辑前 HEAD 为 `8c2c46f`。本节为最新研究语境，下方历史交接原文保留；旧章节中的“下一步”不能覆盖本节。以下报告和源码路径均相对项目根目录。

### 任务背景

用户原始目标是研究一个可解释的短周期交易方法：Binance USDT 现货、只做多、无杠杆，希望抓住买入后的上涨，讨论起点是固定 `+5%` 止盈、`-3%` 止损。研究平台随后冻结最长48小时；48小时是本轮实验口径，不能当成已证实的最优持有期。

经过突破、ATR出口、确认延迟和1h候选等研究，用户现在提出两项本质疑问：

1. “启动”若由后续上涨来定义，再研究“已启动的币能否继续上涨”，是否形成循环定义？
2. 如果原系统选币和候选生成本身没有优势，继续在它选出的机会里调整确认、止盈止损，是否一直在支线上打转？

用户本次要求写交接，梳理过程、进展、难点并提出本质问题。当前授权是整理研究，而不是继续运行某个实验。下一轮首先要恢复系统层面的解释，不能看到上一篇Claude记录的Phase 0建议便直接启动。

**当前状态的诚实表述：** 已经积累了执行/记账校验、多个具体方案的负结果，以及延迟和波动尺度的局部线索；尚未找到一个经新数据验证、扣足成本后稳定盈利的简单规则，也没有完成“系统到底靠哪一层产生优势”的证明。排除了几个方案是进展，但不能把报告数量、测试数量或局部少亏当成盈利研究取得突破。

| 证据层次 | 当前应如何表述 |
|---|---|
| 事实 | B、C20、D6、RT1以及已测ATR出口都未在既定双窗/成本标准下建立稳健正净期望；样本和规则彼此不同，不能混为一组 |
| 观察 | 4h确认会付出价格延迟；事后保持到4h确认的RT1子群表现较好；部分ATR出口减少TIME、改善点估计 |
| 假设 | 上游候选太晚/选币范围不佳、触发时机不佳、出口尺度错配、市场状态或成本不足均可能解释部分失败；尚未单独归因 |
| 决定 | 先完成此次交接与概念澄清；已有生产配置不因这些结果改变。后续研究方向尚未由用户重新确定 |

### 已完成的工作

#### 1. 研究路线与各阶段真正回答的问题

下表按研究推进关系整理；原始指标以各报告为准。除旧系统美元P&L外，表内百分比主要是事件层平均每笔净收益，不能读成账户收益率。

| 阶段 | 问题与结果 | 证据入口 |
|---|---|---|
| 旧系统基线的三道归因闸门，10-10 | 闸门1证明修复后执行/记账可复现；闸门2因全部样本继承current-survivor偏差而未放行；用户批准后另做3-C条件诊断。非容量组早/近raw为`+33.42/-125.90` USDT，net为`-134.63/-248.92` USDT，未显示稳定、足以覆盖成本的毛优势。不能记成“三个闸门都通过、已证明全市场无效” | [三道闸门综述](reports/2026-10-10/baseline_attribution_gates_1_2_3c_synthesis_2026-10-10_v1.md) |
| 同一短出口下B对C20，10-13 | 共同资格、next-open、`+5%/-3%/48h`下，B净收益早/近`-0.1864%/-0.1645%`，C20为`-0.2982%/-0.6995%`。20根突破没有获得替代B的资格，两者都未建立正优势 | [最终cashfix报告](reports/2026-10-13/short_horizon_entry_v1_cashfix/report.md)，`7ff9229` |
| C20是否太晚，10-13 | 突破前已有5%涨幅很普遍，但“之前已涨且入场后没有再涨空间”双窗不一致。近窗有偏晚迹象，早窗混有先止损后上涨，不能统一归为突破太晚 | [时机诊断](reports/2026-10-13/breakout_lateness_diagnostic_v1/report.md)，`06d9655` |
| D6对C20，10-13晚至10-14 | 将新高回看从20根改成6根；D6早/近净收益`-0.3802%/-0.5064%`，一窗恶化、一窗改善，相对差异区间均跨零。裁决`insufficient`，没有自动加收缩/放量条件 | [D6报告](reports/2026-10-13/breakout_d6_v1/report.md)，`ae4d44a` |
| 旧系统退出后恢复，10-14，CRYPTOTRADIN-128 | 从`exit_bar+1`按原始R看20/40/80根4h。K40恢复率早/近`38.46%/20.69%`；近窗17笔unknown的K40完整样本`0/16`，K80`1/16`。不支持把近窗这组亏损主要解释为止损过早，也不代表所有亏损同因 | [恢复率报告](reports/2026-10-14/baseline_post_exit_recovery_v1/report.md)，`d970814` |
| 固定出口加NATR过滤，10-14，CRYPTOTRADIN-132 | 固定5%/3%不变，测试波动率分组；早窗低波动组略好，近窗不延续。需要承认这是一次问题理解偏差：用户原意是按币种波动改变止盈止损距离，此任务只研究了过滤哪些币 | [固定出口波动适配](reports/2026-10-14/fixed_exit_volatility_fit_v1/report.md)，`bdeb878` |
| ATR自适应出口，10-14，CRYPTOTRADIN-133 | 按用户澄清比较固定出口与`TP=5/3×ATR20、SL=1×ATR20`；净收益改善到`-0.0134%/-0.0164%`、TIME减少，但等风险及压力成本证据不足，未获得采用资格 | [ATR出口报告](reports/2026-10-14/atr_adaptive_short_exit_v1/report.md)，`3b168c2` |
| ATR出口组件拆分，10-15，CRYPTOTRADIN-134 | 分别改TP、改SL及两者同时改；单组件仍无双窗正收益，组件贡献和交互不稳定。否定当前具体组合，不外推否定所有ATR出口或证明入场必然无效 | [2×2归因报告](reports/2026-10-15/atr_exit_component_attribution_v1/report.md)，`9ea8746` |
| 4h确认延迟阶段A，10-15，CRYPTOTRADIN-129 | 只看后来确定形成B确认的事件，约80.5%可提前1–3小时；taker净收益`+0.3973%/+0.3210%`，stress仍`-0.0024%/-0.0599%`。这是利用未来确认选择事件的偏有利诊断，不能当成可执行策略 | [阶段A报告](reports/2026-10-15/momentum_resolution_stage_a_v1/report.md)，`1f01457` |
| 独立生成RT1实时全候选，10-15，CRYPTOTRADIN-135 | 纳入未来未确认的早期候选后，早/近`1090/770`笔，taker净收益`-0.2984%/-0.3854%`，stress`-0.6704%/-0.7477%`，同币不重叠后仍负。否定当前price-only定义，不能概括为所有1h信号无效 | [RT1报告](reports/2026-10-15/realtime_momentum_start_v1/report.md)，`7a8d314` |
| Claude三轮讨论，10-15 | 建议先审计RT1的价格保持/资格保持/后续路径，再考虑单一收盘接受度特征。只形成研究建议，标签审计和特征诊断均未执行。讨论与日志提交`feeba4b`、`8c2c46f`已推送 | [完整讨论及最终修订](claude-discussions/2026-10-15-1642-realtime-momentum-continuation.md) |

#### 2. 必须分清的研究对象与继承关系

```text
冻结历史每日币池 + 数据/流动性/市场状态资格
  ├─ 原评分、趋势、动量、支撑、RSI、计划及RR筛选 → BUY_CANDIDATE → B watch
  │    ├─ 后续4h触区且收盘收回entry_high → B事件 → 固定短出口/ATR出口研究
  │    └─ 当前4h内前3根已完成1h触发reclaim → RT1事件 → 固定短出口
  └─ 无须B评分/BUY_CANDIDATE/watch → C20或D6新高突破事件 → 固定短出口
```

- **旧完整系统基线**：动态币池、扫描评分和计划、排序、最多5仓、现金与风险限制、结构止损/TP1/EMA trailing等生命周期。旧归因采用修复后的`confirmation_close`研究成交口径；它也不等同于实际盘口成交或当前paper账户。
- **B all-events短出口基线**：复用原评分/计划体系，但在共同研究平台中生成事件、next-open成交、固定`+5%/-3%/48h`。早/近858/628笔；含入场费每笔假设投入1,000 USDT，允许假想持仓重叠；去掉跨币top5/计划预算/仓位竞争，仍保留逐币watch去重与生命周期。其净收益反映“该候选与触发配上这组出口”的效果，并非脱离出口的纯入场真值。
- **RT1**：继承B watch及区间开始时最近已完成4h资格，只在当前4h区间前3个已完成1h收盘检查累计触区和收盘`>=entry_high`，下一小时开盘进入；一个计划只消费一次。并非全市场独立动能扫描，也不是“B最终成交事件的简单超集”，提前消费计划会改变后续事件路径。
- **C20/D6**：共享冻结每日币池与共同资格，但替换B评分/watch入场逻辑。因此不能说“所有尝试都只在B选中的币/计划里调整”；上游仍需拆成“每日币池/共同资格”和“B独有评分/计划”，不能笼统归罪于同一个选币模块。

依据：[入场研究冻结协议](reports/2026-10-13/short_horizon_entry_protocol_v1.md)、`scripts/research_short_horizon_entries.py::features`、`scripts/short_horizon_core.py::plan_decision/replay`及[RT1协议](reports/2026-10-15/realtime_momentum_start_protocol_v1.md)。

#### 3. 对前面聊天的精度校正，下一会话必须继承

1. **B不是旧系统“只换出口”的严格复现。** 共同研究平台在计划创建与最终信号时复查资格，旧WATCHING并非同样复查；成交也统一为next-open，不能说与旧`confirmation_close`或`legacy_same_bar`完全一样。因此两种基线的差不能直接归因给一个因素。
2. **WATCHING从计划创建就开始。** 前面“先触区，才进入WATCHING”的解释不准确。研究代码在创建后激活watch；后续同一根4h的区间触及与收盘`>=entry_high`即可触发，不要求先在一根K线回踩、再在另一根K线收回，也未证明tick级真实先后。创建后第19根4h过期，原stop仍用于入场前失效，原TP/RR仍参与计划资格；它们只是成交后不再控制短出口。
3. **all-events去掉交易竞争，不会清除全部选样依赖。** 上游每日选择、流动性、regime、B评分及计划构造仍可能决定哪些事件根本进不了样本。
4. **“启动”只能先叫候选信号。** 可见事件、未来延续、固定出口交易成功必须分开。`TP_first`不等同于长期趋势成立，TIME可能有净盈利，持有期未触碰任何一边也不证明没有动能。
5. **主结果`taker`不是所有腿都用taker费率。** 冻结入场fee/slip为10/5 bps，TP为4/0，SL和TIME为10/10；stress入场20/10、TP20/10、SL和TIME20/20。它们是研究成本假设，不能讲成已核实的用户账户真实费率。
6. **已形成的是预测/路径描述，未做充分的因果归因。** “入场只读当时信息”证明时间可执行性；按未来保持状态分组后收益不同，不证明这个标签导致盈利，更不证明它当时能预测。

#### 4. Claude讨论的具体结论和仍未解决的方法问题

- 已确认的RT1事后分组：早/近4h保持率`657/1089=60.33%`、`481/767=62.71%`；保持组taker平均净收益`+0.5825%/+0.3309%`，未保持组`-1.6472%/-1.5880%`。另有1/3笔标签unknown；标签有效分母不能写成1090/770全部样本。
- 原建议Phase 0：固定候选集上补`price_retained`、`eligibility_retained`及其交叉组合，与`TP_first/SL_first/neither`、MFE/MAE、raw/net交叉报告。它能检查标签混合与损失分布，但不能检查上游筛掉了哪些机会，也不能单凭占比认定亏损因果。
- 原建议Phase 1唯一特征：`(close_1h-entry_high)/(high_1h-low_1h)`，即突破上沿距离相对本根振幅。它并非通常的`(close-low)/(high-low)`收盘位置，也未验证有预测力。
- 第三轮Claude虽然同意删除任意门槛，后文仍出现没有依据的硬阈值；Codex收口没有采纳。讨论不等于完整可直接运行的预注册协议。
- **仍须明确**：置信区间跨零一般表示证据不足，不能据此证明无效；月度区块并不自动独立，早/近窗口约11/12个月，也不是“1,860笔全在12个月”。正式统计区块与精度需结合数据依赖预先定义。
- **neither不能被悄悄排除出经济评价。** 可单独研究已决TP/SL的条件差异，但只在TP/SL子集中报告净收益会改变目标总体；全候选（含TIME/neither）成本后期望及覆盖率必须保留。
- 讨论状态为`DONE / retest`，指建议有条件再研究；不是实验已完成、特征已有效或任务已开工。用户随后提出了更上游的疑问，Phase 0不再应被下一会话机械当作默认第一优先级。

### 尚未完成的事项

#### 1. 为什么用户感觉一直在支线上打转

- 每轮失败后，下一问题通常围绕上一轮局部结果展开：突破太晚→缩短突破窗口，出口不适配→ATR，ATR效果弱→拆组件，4h确认慢→1h，再到1h真假区分。各题有局部合理性，但尚缺少一张“哪些上游前提已被验证”的总图。
- 多次把“修正某种缺点”隐含等同于“可能得到正期望”。提前买、少TIME、少止损或胜率更高都可能成立，仍不保证保留的毛收益覆盖成本与尾部损失。
- B与RT1一直依赖原评分/计划体系，但我们没有在当前短周期目标下，完成该体系相对可比未入选机会的独立增益判断。历史上做过流动性、趋势、regime等A/B，所以不能说上游从未研究；缺的是层次清楚、口径一致且能外推的整体证据。
- `CRYPTOTRADIN-132`曾把用户“按波动调整出口”的问题理解成“固定出口按波动过滤”，让路线多走了一个分支。此处要承认理解偏差，不能把它包装成原问题已经被回答。
- 多个baseline、all-events与账户收益、历史开发与前向验证在解释中混用，使用户难以判断每轮研究究竟消除了哪个不确定性。
- 讨论轮数和审计细节增加，但“完成这个诊断会改变哪个系统级决定”没有始终明确。下一步如果只解释另一小桶亏损而不改变决策，应评估是否值得做。

#### 2. 必须提出的本质问题

1. **优势来源到底是什么？** 是市场整体顺风、每日选币、B评分、回踩收回、突破、特定状态，还是容量路径？要能用一句可证伪的话说明为什么这些机会应该优于可比机会。
2. **我们到底选择了哪些币、哪些时点，又漏掉了什么？** 必须区分原始可交易市场、每日币池、共同资格、B评分计划、实际信号、组合成交。只看最终成交，无法回答前面几层是否保留赢家或误删赢家。
3. **上游是否真的提供增量？** “B自身亏损”不等于“B筛选无效”，因为可比总体可能亏得更多；“B相对改善”也不等于“可以交易”，因为改善后仍可能为负。需要同时问相对增益与绝对成本后可行性。
4. **目标到底是持续趋势，还是48小时内的可交易净收益？** 二者不完全相同。固定5%/3%能统一衡量，但不天然等于所有币的延续；要明确哪个是主目标、哪个仅是解释标签。
5. **延续是否在当时可预测，且这种可预测性足够支付成本？** 事后组差异再大，也不构成入场边界；弱预测力也可能没有经济价值。
6. **上游质量、入场时机、出口不匹配如何区分？** 不能拿同一批最终成交反复换出口来回答选币好坏，也不能用未来MFE高直接宣称早知道可以买到。
7. **我们还有什么可用的独立证据？** 两个旧窗口都已反复使用，缺退市币历史；改变特征或统计方法不能恢复它们的样本外资格。新的验证区间是否看过、自然前向是否足够成熟，必须查使用记录，不能仅凭日期新就称未用。
8. **何时停止一条路线？** 一个特征或具体规则失败，只能否定相应定义；但也不能无限换特征、换标签、换分组延续路线。继续之前应说明下一结果会支持哪个决定，以及多大不确定性只能停留在“未知”。

上述问题是下一轮主线选择的讨论输入，尚未组成新实验授权。用户关于“上游候选不好会限制后续表现”的逻辑合理；“上游是当前亏损根因”仍是待证假设。

#### 3. 当前待办与阻塞

- `CRYPTOTRADIN-135`、`129`阶段A、`132/133/134`：依据本地最新TODO为`in_review`，实验已完成待用户验收；本次没有实时查询或修改Taskboard。
- `CRYPTOTRADIN-127`（B确认强度）、`130`（毛优势与成本覆盖）、`131`（市场状态）：依据本地TODO保持todo，未启动。不能因用户要求交接就把它们全部开起来。
- RT1标签审计Phase 0及单特征Phase 1：仅有Claude讨论建议，没有任务、协议、实现或结果。
- 正式历史总体推断仍受point-in-time历史币池限制；`CRYPTOTRADIN-89`为相关基础设施待办，正式闸门3不是已完成。
- 当前没有“已验证可采用”的新短周期策略；本次交接没有新增回测结论。

### 下一步直接执行指令

先做只读恢复，准确理解候选流转，避免自动重跑已结束支线：

```powershell
Set-Location -LiteralPath 'D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects'
git status --short
git log -8 --oneline
Get-Content -LiteralPath 'AGENTS.md' -Encoding UTF8
Get-Content -LiteralPath 'handoff.md' -Encoding UTF8 -TotalCount 260
Get-Content -LiteralPath 'reports/2026-10-13/short_horizon_entry_protocol_v1.md' -Encoding UTF8
Get-Content -LiteralPath 'reports/2026-10-15/realtime_momentum_start_protocol_v1.md' -Encoding UTF8
Get-Content -LiteralPath 'reports/2026-10-15/realtime_momentum_start_v1/report.md' -Encoding UTF8
Get-Content -LiteralPath 'TODO.md' -Encoding UTF8 -TotalCount 100
rg -n 'def features|selected_symbols|BUY_CANDIDATE|candidate=entry|breakout=breakout' scripts/research_short_horizon_entries.py
rg -n 'def plan_decision|def replay|touches|watches|layer ==|candidates =' scripts/short_horizon_core.py
rg -n 'generate_rt1_candidates|reclaim_after_hour|retained_4h_confirmation' scripts/research_realtime_momentum_start.py
```

接着向用户解释一张“市场→每日币池→共同资格→B评分计划或C20/D6→触发→退出成本→账户”的图，标注每层已经回答和仍未回答的问题。用户当前的困惑需要先被消除，再确定下一项研究是上游增益、RT1内部区分，还是其它层次；不要以“接着做Phase 0吧”代替选择依据。

**若后续决定研究上游候选增益，正式方案仍须单独冻结：**

- 系统目标：寻找可执行、短持仓且覆盖成本的优势；单一问题：在相同时间、基本可交易资格及测量规则下，被某一明确选择层保留的机会，是否比可比总体/未保留机会提供稳定增量？路线位置为下游特征/退出优化之前的上游前提检验。
- 先定义比较单位和分母、当时可用的选择记录、共同入场时点与出口、持仓重叠及币种/时间相关性；被排除者没有B计划时不能随意拼出一个不公平入场再作比较。不能直接拿“全部币的任意时点”对比“B择时信号”并把所有差异归为选币。
- 支持：双窗及预声明稳健性下有一致、经济上有意义的相对增益；只有绝对成本后也可行才值得进入策略新样本验证。否定：在精度足够时显示该层没有预声明的实用增益或稳定有害。证据不足：比较单位不匹配、缺未选中记录、区间太宽/跨零、窗口冲突、集中度或幸存者限制使结论站不住。先声明最小有用差异及其依据，不事后发明门槛。
- 这是后续协议要满足的条件，不是本交接发起实验；本次不读取新的收益窗口、不运行新的筛选器或参数组合。

### 重要声明

- 现有历史窗口统一为UTC `[2024-07-01,2025-06-01)`及`[2025-06-01,2026-06-01)`；主数据为4h，已有1h路径供短出口与RT1研究。未开展15分钟研究，日常采集/生产频率没有因此改为1h。
- 不用“后来上涨”定义当时已知的启动；不把`retained=true`事后组直接变成可执行过滤器，不把两窗点估计负说成数学证明所有机会均无效。
- 原始冻结NPZ约419MB位于忽略目录`data/research_snapshots/short_horizon_entry_v1/`，Git保存报告和指纹而非完整行情。换机复现需这些归档；勿覆盖冻结输出。账户研究尚有历史最小订单/数量步长近似问题，事件层收益不是实盘收益。
- 既有用户改动`scripts/run_logged_paper_task.ps1`必须保留且不纳入本次提交；`data/crypto_trading.db`不入Git。自然采集可能继续产生reports，按仓库规则归档时说明其并非新研究结果。
- 本次仅更新`handoff.md`和`dailylog.md`：未新建/完成/改排Taskboard任务，未正式更改开发路线或运行实验，因此不新增实验账本判断，不改TODO或开发计划。这里记录的是需要重新评估的研究主线，不是假装已有一个新的已批准方案。
- 前述Claude建议的“1–2天、3–6个月”等只是讨论估计，不是运行实测或当前承诺。不要用日历等待来替代研究问题澄清和样本成熟度检查。
- 本节以`docs: hand off research trajectory and unresolved premises`提交，并按AGENTS要求推送；实际提交号及推送结果以`dailylog.md`和Git为准。历史交接内容全部保留。

## 2026-10-13 07:17 +08:00

### 项目目录

`D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects`，分支 `main`。本节覆盖下方尚未执行研究的旧状态，不覆盖历史记录。

### 任务背景

用户要求读取交接并研究：在完全相同的短周期退出下，突破入场是否比现有入场更能选出净盈利交易。本轮已执行、审计并完成研究，不需要重新跑参数。

### 已完成的工作

- 研究提交 `7ff9229`：隔离研究脚本、冻结协议、双窗口数据指纹、三层对照与完整压力分支；统一下一根开盘、+5%/-3%、48h、费用和滑点，无生产变更。
- 主答案：不支持升级这版20根4h新突破。早窗B/C平均每笔净收益为-0.1864%/-0.2982%，近窗-0.1645%/-0.6995%；近窗C-B的95%区间全负，早窗跨零。两臂均未建立正优势；登记 `retest / evidence_insufficient_for_positive_edge`，不是自动调参指令。
- 首次账户审计发现极小浮点余款产生虚小仓位，修正为USDT维度1e-8数值容差。首次代码与结果保留，最终目录为 `reports/2026-10-13/short_horizon_entry_v1_cashfix/`；24份非账户结果不变、主账户收益不变。
- 51项针对性测试、100个真实时点scanner对照、32,713条跨分支记录审计通过；不是全套测试或32,713个独立样本。
- 已同步TODO、EXPERIMENT_LEDGER、SYSTEM_OVERVIEW、仓库开发计划、Obsidian实验日志与开发计划。
- 归档收尾：已修复Git自动换行导致的已暂存报告指纹差异；113份报告原字节、协议/输入manifest/最终9份执行源码指纹核对通过。本节随 `docs: preserve frozen research bytes and record verification` 提交，随后推送origin/main；以Git远程状态核验最终推送是否成功。

### 尚未完成的事项

- 本轮没有待执行的策略实验；禁止从早窗账户少亏推导替换默认策略。
- 历史LOT_SIZE/MIN_NOTIONAL重建是TODO待立项项，本轮未获准开展。主账户4笔非零小额订单低于10 USDT，故账户层仅为执行近似；10 USDT不是新增交易门槛。
- 两个开发窗口已重复使用，且币池存在幸存者偏差；本轮结果不能代替未使用样本外，也不能代表所有突破策略。

### 下一步直接执行指令

```powershell
Set-Location -LiteralPath 'D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects'
git status --short
git log -3 --oneline
git ls-remote origin refs/heads/main
Get-Content -LiteralPath 'reports/2026-10-13/short_horizon_entry_v1_cashfix/report.md' -Encoding utf8
```

如仅需复验代码：`python -m pytest tests/test_short_horizon_entry_study.py tests/test_replay_ema_execution.py tests/test_scanner_regime.py -q`。不要再次执行 `prepare/run` 覆盖已冻结结果；程序本身有目录防覆盖保护。若远程尚未含本轮提交，先检查是否推送失败，不要force push。

### 重要声明

- 用户原有 `scripts/run_logged_paper_task.ps1` 的两处 `--no-obsidian` 改动保留且不纳入研究提交。数据库不入Git，生产配置SHA256仍为 `be7ec39ec21f6a838571511cb2cd0e290263031b521a9a07a6fb70164b8ef4bf`。
- 约419MB原始数组只在忽略目录 `data/research_snapshots/short_horizon_entry_v1/`；换机完整重放需两份npz归档及manifest校验，Git仅含报告/指纹。
- 00:10/04:10自然调度reports依仓库规则一并提交，不是本轮实验结果；Obsidian笔记已文本核对，未声称GUI渲染验收。
- 最新可读报告用cashfix目录，不以首次目录计数作为最终结果；研究记录必须区分事实、观察、假设与决策。

## 2026-10-12 23:59 +08:00

### 项目目录

`D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects`。交接前分支 `main`，HEAD `cc78011`，远程 `origin` 为 `https://github.com/Goodyenough/wbj-CryptoTrading.git`。

本节是最新交接；下方 2026-10-09 及更早章节只作历史记录，其中 ATR 主线、旧任务状态不覆盖本节的用户意图。首先读取根目录 `AGENTS.md`。

### 任务背景

用户已完成基线归因讨论和短周期策略公开资料调研，明确提出下一项研究：

> 在完全相同的短周期退出规则下，突破入场是否比现有入场更能选出有净盈利的交易？研究这个问题。

随后用户中断准备工作，并要求“写一个 handoff，我要在新对话中开启这个研究问题”。本轮仅交接，不继续执行实验。新对话可承接该研究授权，不必重新询问是否有必要查 GitHub/YouTube；授权不包含修改生产配置、实盘交易或恢复 ATR 参数搜索。

- **系统目标**：Binance USDT 现货、只做多、无杠杆，在可执行且计入费用/滑点的条件下寻找正净期望，并满足短持仓、愿意放弃后续大涨的收益偏好。
- **单一问题**：统一短周期退出、币池、过滤、成本、成交和资金约束后，仅替换入场模块，突破是否比现有入场更好，且突破自身是否净盈利？“比原策略少亏”不等于满足目标。
- **路线图位置**：公开资料筛选之后、新方向首轮条件性实验之前。不是继续证明 ATR 0.35，也不要求先把旧策略所有亏损解释完才允许探索；同时不能声称新方向已解释或治愈旧亏损。
- **事实**：旧非容量竞逐 baseline 共 101 笔完整闭合交易；早窗 63 笔 raw/net 为 `+33.42/-134.63` USDT，近窗 38 笔为 `-125.90/-248.92` USDT。现有执行/记账修复和旧交易 4h 缺口检查已收口，但不能据此免除新实验的执行/数据检查。
- **观察**：近窗 23 笔亏损中 17 笔没有被现有入场样/退出样标签解释。用户称之为“unknown 慢性失败组”，这不是已经证实的同一种机制；不能因其事后没涨，就当作入场时可识别的排除条件。
- **假设**：新突破事件可能更直接选中短期延续机会；固定时间出口符合资金周转偏好，但不自动提高盈利。
- **决策**：研究比较问题已由用户提出；还没有最终实验协议、实现、结果或部署批准。+5%/-3% 是用户讨论的目标；20 根通道、48 小时是资料报告建议的工作值，须在看结果前一次性冻结，不能称为已选优参数。

### 已完成的工作

1. 公开资料调研已完成并提交：`8d00345 research: review short-horizon crypto strategy sources`；验证/日志回填为 `cc78011 docs: record strategy source review verification`，此前均已推送。完整报告：`reports/2026-10-11/short_horizon_strategy_sources_2026-10-11_v1.md`。下一轮优先完整读取，重点第 7 节候选卡片、第 8 节成本口径；核心论文、固定 commit 的 GitHub、YouTube 说明链接都在报告内，不需从头重查。
2. 资料结论：简单通道突破优先级来自易解释、易验证和与现有入场区别清楚，不是已证明最赚钱。均值回归是另一候选，暂不混入本轮；补仓/DCA/grinding 的高平仓胜率不能替代总投入、浮亏、成本和持仓风险审计。没有运行外部公开代码；视频只核验可获得说明，未完整观看。
3. 旧基线证据入口：`reports/2026-10-10/baseline_attribution_gates_1_2_3c_synthesis_2026-10-10_v1.md`、`baseline_attribution_gate_3c_2026-10-10_v1.md`、`baseline_trade_path_attribution_2026-10-10_v1.md`（后二者同目录）。旧路径结论为 `C_evidence_insufficient_no_stable_dominant_mechanism`；101 笔非容量与 30 笔容量竞逐必须分开理解。
4. 新实验准备仅做了只读检查：读取工作区规则、候选报告和 `crypto-backtest-expert` 技能；查看 Git 状态并定位实现/测试文件。尚未深入审查新实验所需的 replay/scanner 调用链、数据库覆盖和信号提取接口。
5. **没有为本次问题修改策略代码、配置、数据库，没有运行新回测、A/B、参数搜索或前向实验，也没有产生收益结论。** 本轮新增的是本交接、审计日志及 TODO 状态说明；自然调度生成的 reports 不属于此实验结果。

### 尚未完成的事项

#### 一、在结果出现前冻结完整协议

以资料报告第 7 节为起点，不另开参数网格：

| 项目 | 下一轮应落实的共同口径或差异 |
|---|---|
| B 对照 | 原 reference baseline 入场模块，不是默认加上 ATR 0.35 的 incumbent；出口换成共同短周期出口。需核对评分、计划 WATCHING/reclaim 生命周期及扫描节奏，不能只用一个 EMA 条件冒充原入场。 |
| C 候选 | 4h 收盘 `close[t] > max(high[t-20:t])`，通道不含当前 bar；且前一根没有满足其自己的前 20 根突破条件，形成新事件。它替换原综合评分/reclaim 模块，不再叠加新 RSI/ADX/量能阈值。 |
| 共同过滤 | 同一冻结币池、流动性、数据质量和 regime 限制。需分清两臂共享的可交易资格与 B 独有的入场评分，不能把 B 的全部入场门槛偷偷保留给 C。 |
| 成交 | 只读已收盘信息，两臂均在信号后下一根可执行 bar 开盘成交并计滑点。旧 `confirmation_close` 结果不能直接当 B 对照。明确开盘跳空、缺口、首根价格事件和时间出口的先后顺序。 |
| 共同退出 | 按实际入场成交价 +5% 止盈/-3% 止损，全平；满 48 小时后首个可执行时点全平。无补仓、分批止盈、EMA trailing 或 ATR 动态退出。 |
| 重复/再入场 | 同币持仓时不加仓；C 退出后必须等待新的突破事件，不重复买持续突破状态。B 的计划去重/再武装规则需忠实提取并写明；信号层与组合层的事件排除分别记账。 |
| 信号层 | 全量 eligible 事件按等名义本金度量净期望，不先筛选旧 17 个亏损或旧 101 笔交易。不受组合满仓选择影响的机会诊断不得称为可交易净值。 |
| 组合层 | 两臂分别重放现金与仓位路径，初始 10,000 USDT，单笔风险上限 1%、总风险上限 5%、最多 5 仓、无杠杆且受现金限制。预先冻结同刻信号流动性排序及并列规则，记录容量阻挡。 |
| 成本 | 报告核对的本地配置为 maker 4 bps、taker 10 bps、入场滑点 5 bps、止损滑点 10 bps；下一轮复核实际源码，明确 TP/SL/时间出口及 entry 的费率。next-open 主动成交沿用 maker entry 偏乐观，必须预先规定共同主动/taker 压力口径。 |

仍需解决：基线入场计划里原 stop/target/RR 是否影响资格与仓位，统一退出后如何保留“原入场”而不引入隐藏变化；历史流动性排序用什么时点可得字段；48h 出口与触价同刻时的执行顺序；缺口、退市、期末删失、同 bar 双触的具体处理；统计区块长度/置信区间及集中度检查的预声明方式。这些是尚未检查的实现问题，不是已经发现的代码缺陷。

#### 二、核实可用数据，再选择最小实现

- 开发诊断窗口：UTC `[2024-07-01, 2025-06-01)` 和 `[2025-06-01, 2026-06-01)`。这些窗口反复使用过，不是未接触样本外；独立确认需另行封存未用样本或自然前向。
- 旧协议入口：`reports/2026-10-09/atr_fixed_history_protocol_v1.md`。旧 master 为 285 个当时存续币，来源和 hash 必须从协议/实际产物复核，不能声称具有完整 point-in-time 上市退市历史。
- 新策略会产生新信号和不同的退出时间，必须覆盖全部新路径及预热期，不能沿用“旧 131 笔没有 4h 缺口”证明新样本完整。数据缺口不得默默前填后当真成交。
- MAE/MFE 不能证明先到哪条线；同 4h bar 双触优先用已可得更细 K 线缩小歧义，否则报告保守/乐观边界，若翻转结论则证据不足。
- 容量标签按每臂的新组合路径重算；分别报告信号质量与可交易账户表现，不能沿用旧容量标签，也不能假定释放资金后必有更好币。
- 现有 `kline_cache`/run 产物可望复用，但本轮没有检查 schema、覆盖、快照一致性或完整运行耗时。优先只读访问本地 DB，冻结来源及 hash；不要让自然采集变化悄悄改变同轮比较。

#### 三、验收标准必须先写，再运行

- **支持进入独立验证**：两个窗口均有 C-B 净期望改善，且 C 自身扣成本为正；成本压力、容量隔离、币种/时段集中度检查后仍站得住。收益只在一个窗口好，不算通过；即便通过也不等于部署。
- **否定冻结候选**：精度足够的结果显示 C 净期望非正，或 B 不劣于 C，或只有违反既定风险/期限才改善。否定本卡片，不外推为所有突破策略都无效。
- **证据不足**：窗口相反、区间跨零、样本太少或高度相关、少数币/尾部/容量主导、同 bar 顺序或数据问题决定方向；current-survivor 限制必须保留。
- 同时报告交易数、净期望及不确定性、胜率/平均盈亏/PF、费用拖累、时间退出比例及持仓分布；组合层补充净收益、Sharpe/Sortino、CAGR、最大回撤、暴露/换手及尾部。按币种、regime、周/月、退出类型、时长检查集中度，不能把相关信号当独立抛硬币。
- 含入场费现金、按实际成交价设置两端且沿用报告成本时，二元算术打平胜率约 39.6705%；**加入时间出口后不再是二元结果，不能拿约 40% 胜率保证不亏。** 手续费配置不是已核验的用户实际账户费率。

### 下一步直接执行指令

新对话先执行以下只读检查，随后给出简短协议/实现边界说明并推进已授权研究，不在本交接轮启动：

```powershell
Set-Location -LiteralPath 'D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects'
git status --short
git log -5 --oneline
Get-Content -LiteralPath AGENTS.md -Raw
Get-Content -LiteralPath reports/2026-10-11/short_horizon_strategy_sources_2026-10-11_v1.md -Raw
Get-Content -LiteralPath .codex/skills/crypto-backtest-expert/SKILL.md -Raw
Get-Content -LiteralPath .codex/skills/crypto-algo-trading/SKILL.md -Raw
Get-Content -LiteralPath reports/2026-10-09/atr_fixed_history_protocol_v1.md -Raw
Get-Content -LiteralPath pyproject.toml -Raw
rg -n 'def |confirmation_close|entry_reclaim|max_holding|watch_expiry|blocked_entry|kline_cache' src/crypto_trading_system/backtest/replay.py src/crypto_trading_system/scanner.py src/crypto_trading_system/trade_state.py scripts/attribute_baseline_trade_path.py
Get-Content -LiteralPath src/crypto_trading_system/backtest/costs.py -Raw
```

接着按依赖顺序做：

1. 核对 `backtest/replay.py`、`backtest/runner.py`、`scanner.py`、`trade_state.py`、`config/settings.toml` 及归因脚本的输入输出；确认原入场抽取接口、历史数据可用性和运行环境。按需读取完整函数，不能凭上述搜索片段实现。
2. 在 `reports/<执行日>/` 写正式实验协议，标识固定版本、数据/窗口/费用/事件时序及预先验收标准。没有现成的新实验命令；不要虚构已存在的 CLI 或运行产物。
3. 优先隔离研究实现，不改生产默认；复用经检查的模块。测试覆盖无未来信息、前 20 根不含本根、新事件去重、next-open、实际成交价目标、跳空/双触/时间截止、费用与现金对账、容量拒绝、删失/缺口；先小样本验证，再跑两个冻结开发窗口。
4. 报告先用非技术语言回答“哪种入场更能净赚钱/证据不足”，再给技术指标；区分信号层、组合层、旧基线背景。不得只用胜率或总收益排名给结论。
5. 真正运行且产生判断后，更新 `EXPERIMENT_LEDGER.md`、当前策略说明、TODO、dailylog 及 Obsidian 实验日志；如阶段/优先级变化，同步仓库和 Obsidian 开发计划。遵循提交及 push 规则。

### 重要声明

- 本轮遵从用户“在新对话开启”的要求，只保存交接。没有后台实验或新研究进程需要继续轮询。
- 保留用户未提交的 `scripts/run_logged_paper_task.ps1` 修改，不纳入本次交接提交。数据 DB 及 `-shm/-wal` 不提交，不覆盖、不重置工作区。
- 交接前 `reports/2026-10-11/` 与 `reports/2026-10-12/` 有自然调度新增报告/图表。依 AGENTS 要求随提交纳入 `reports/`；它们不是本轮新策略的回测结果，未做本轮收益验收。
- 资料报告第 7/9 节和旧 TODO 的“未批准启动”描述对应 10-11 当时状态；用户后续已经提出本研究，当前只因迁移新对话而尚未执行。不要误把旧文案视为必须重新申请相同问题的授权；遇到实质扩大范围再询问。
- 正式历史归因仍受 point-in-time 币池任务 `CRYPTOTRADIN-89` 阻塞，`CRYPTOTRADIN-124` 的 hold 不被本条件性新策略研究解除。不批量重开工程 backlog，不研究止损后路径来替代本问题。
- 真实 Obsidian 路径：`D:\MyNotebook-Obsidian\CryptoTradingSystem\CryptoTrading 实验日志.md`、`D:\MyNotebook-Obsidian\CryptoTradingSystem\CryptoTradingSystem 开发计划.md`。本轮没有实际实验或新阶段验收，不写虚构实验日志，不修改生产设置。
- 若未来需要 Claude 评审，须依据新用户要求及 `claude-discussion` 技能执行；旧讨论授权不意味着本轮应自动联系 Claude。

## 2026-10-09 23:03 +08:00

### 项目目录
`D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects`，main。

### 任务背景
用户要求加速ATR研究：Taskboard任务15修复历史执行错误，任务120固定历史重算；用户最新要求ATR优化留到以后并询问下一步。

### 已完成的工作
- 任务15已验收done，修复commit `207cac4`；验收文档commit `5d78633`已推送。
- 任务120已完成8分支历史诊断及现金/费用对账，报告`reports/2026-10-09/atr_fixed_history/report.md`。新增可选confirmation_close诊断，默认legacy不变；最终188测试通过/5项既有失败。
- 确认收盘净收益：早窗4.72%→1.50%，近窗-1.51%→-10.20%；近窗MDD17.71%→20.21%。结论retest，不宣称ATR一定降低整体风险。
- 用户的后续优化要求已复用CRYPTOTRADIN-51 todo，本次不执行。任务120收口送审；具体本轮提交hash见dailylog和git log。
- 仓库及Obsidian实验日志/计划、TODO、策略文档已同步；20:05 daily报告success，20:09独立shadow ACTIVE、0机会，尚无完整前向收益对照。

### 尚未完成的事项
成交执行契约、UNKNOWN放行修复、逐计划/多日自然daily/4h覆盖验收、存量TRX/ZRO/AAVE/SOL缺口审计、paper完整组合约束。ATR优化留到以后，未授权生产调参；不要重新跑固定8分支。

### 下一步直接执行指令
先`git status --short`、`git log -3 --oneline`，读`reports/2026-10-09/atr_fixed_history/report.md`与TODO顶部。用户确认继续时优先明确signal/decision/fill/stop可执行时序和UNKNOWN修复范围；不要把理想收盘模式当实盘契约。
Taskboard CLI：`node 'C:/Users/10537/Documents/Codex/2026-08-13/https-github-com-chuspeeism-dashi-taskboard/work/dashi-taskboard/cli/taskctl.mjs' issue get CRYPTOTRADIN-120 --json`。所有看板操作用taskctl，先get/comments，版本并发保护，用户验收后才能done。

### 重要声明
保留既有`scripts/run_logged_paper_task.ps1`修改，不纳入本轮提交。数据DB不提交。executed_replay.py.txt对应实际执行源码hash；最终源码仅展开等价条件并恢复legacy审计标签。两个窗口已反复研究，只是diagnostic；存续币偏差、maker费用及零延迟理想收盘假设限制外推。Obsidian真实路径`D:\MyNotebook-Obsidian\CryptoTradingSystem`。


## 2026-08-13 00:21 +08:00

### 项目目录

工作目录：`D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects`

这是一个本地 Python 加密货币交易研究系统，当前 Git 分支为 `main`，远程为 `origin/main`。数据库位于 `data/crypto_trading.db`，自动任务日志位于 `logs/`，自动生成的 Markdown/JSON/图表报告位于 `reports/YYYY-MM-DD/`。项目根目录中的主要记忆文件分别承担不同职责：

- `dailylog.md`：工程、配置、项目文档和运行维护的审计日志。
- `TODO.md`：可执行待办，不承担大段研究叙事。
- `开发计划.md`：项目阶段、研究路线和模块状态。
- `EXPERIMENT_LEDGER.md`：仓库内的实验索引和结论。
- Obsidian 文件 `D:\MyNotebook-Obsidian\CryptoTradingSystem\CryptoTrading 实验日志.md`：回测、A/B、paper 和前向研究的详细实验叙事。
- `handoff.md`：跨会话交接记录；本章节是截至本次交接的最新总览，旧章节必须保留为历史记录。

本项目没有得到实盘下单授权。任何 `live` 交易、真实资金部署、自动下单权限配置，都必须另行获得明确批准；当前所有工作属于 research、backtest、paper 或 read-only diagnostics。

### 任务背景

#### 1. 项目总目标

系统的长期目标是建立一个可复核的研究闭环：

`daily 扫盘 -> 生成候选和交易计划 -> 数据质量/市场环境检查 -> paper 跟踪 -> 4h 状态推进 -> 回测/A-B -> 归因复盘 -> 再决定是否研究下一条规则`

项目当前并不是“尽快让某个参数上线”，而是先把策略行为、容量约束、执行时点、退出路径和数据链路记录完整。项目规则要求：每次实验只回答一个主要问题；`retest` 不等于 keep；回测收益改善不自动授权修改 `config/settings.toml`；paper 证据不自动等于实盘授权。

#### 2. 当前研究主线：`atr_reclaim_0_35`

前期 A/B 和离线归因发现，要求 4h 收盘超过 `entry_high + 0.35 * ATR` 的 `atr_reclaim_0_35` 在若干历史窗口中表现较好，但改善来源并不简单：

- common trades 并没有普遍变好；
- 改善的一部分来自 variant-only 新增赢家；
- baseline 错过的部分赢家本身质量并不差；
- `max_active_positions=5`、候选排序、满仓阻挡、旧仓长期占槽等容量路径可能改变最终交易组合；
- 早期/近端窗口表现存在路径依赖，不能仅凭净收益或 PF 判断规则机制已经被证明；
- 旧的 `2023-07-01 -> 2024-07-01` 历史窗口存在 historical universe membership 缺口，N0-N4 产物只保留为 diagnostic evidence，不能作为新的 keep、reject 或 deploy 依据。

因此在 2026-07-30 正式把该规则定位为：

- `provisional_research_incumbent`：当前研究阶段默认的 incumbent，供后续新 challenger 比较；
- 不是 paper deployment；
- 不是 live deployment；
- 不代表 `0.35` 已经得到严格前向验证。

当前必须长期保留三条线：

| 线名 | 含义 | 作用 |
|---|---|---|
| `reference_baseline` | 原策略，不含 `atr_reclaim_0_35` | 判断 `0.35` 相对原策略的直接前向贡献 |
| `atr_reclaim_0_35_shadow` | 原策略加 `0.35`，独立记录，不控制 paper | 长期保留的 `0.35` challenger-like 参照线 |
| `research_incumbent` | 当前研究 incumbent，现阶段等同采用 `0.35` 的研究参照版本 | 后续新 challenger 的默认比较基准 |

如果未来研究新因素，原则上采用：

`new_challenger = research_incumbent + one_new_factor`

每轮只改变一个主要研究维度。新 challenger 研究在当前 shadow gate 未成熟前暂不启动。

#### 3. 六个研究优先级

前向研究不是只为了回答“0.35 是否有效”，还要利用每次 4h 扫描和状态更新产生的全部信息，逐项回答以下六类问题：

1. **候选排序和满仓机会成本**：同一轮有多个合格候选时，为什么进入某个候选而没有进入另一个？被 `max_active_positions` 阻挡的高排名候选，事后是赢家还是亏损？
2. **容量利用和旧仓占槽**：满仓是否经常被长期、低质量、尚未 TP1 的仓位占用？替换一个 stale slot 是否有稳定、可执行的边际收益？此前容量 replacement 分支已因证据集中且不稳定而冻结。
3. **持仓时间和退出路径**：`TIME_EXIT`、TP1、止损、TP2、EMA/ATR trailing 的不同路径怎样影响 slot 释放、延迟赢家和组合结果？固定 `42` 根 4h 的方向曾显示价值，但 paper 前向独立 symbol 样本不足，不能部署。
4. **执行质量和状态一致性**：scanner、entry trigger、4h close reclaim、fill time、同根 K 线 stop/TP、API 延迟、paper state 和 shadow state 是否按同一时点、同一口径记录？
5. **市场状态适应性**：`RISK_ON`、`RISK_OFF`、趋势、波动率、market breadth、signal density 等状态是否改变 `0.35` 的直接过滤贡献、容量路径贡献或退出结果？
6. **后续单变量入场因素**：在现有 incumbent 已有足够证据之后，才研究 entry_low 附近成交、RSI recovery、放量下跌拒绝、4h 下行趋势接飞刀等因素；这些不能在当前未成熟 shadow 阶段随意叠加。

### 已完成的工作

#### A. 研究纪律和历史分支处理

- 已完成 `atr_reclaim_0_35` 的历史回测、阈值敏感性、交易级归因和关键路径复盘。
- `0.10`、`0.15`、`0.25`、`0.35` 的阈值敏感性已经做过；`0.35` 是当前最强候选，但结论保留为 `candidate_keep_review` / `retest_path_dependent`，不是部署批准。
- 已确认不能继续围绕 `0.30 / 0.35 / 0.40` 进行无止境阈值搜索。
- 已完成 `signal_fill_timing_audit` Stage 0，结论为 `timing_audit_warn_same_bar_ambiguity`：当前 replay 在同一次调用里可能让 WATCHING 计划入场后继续评估同根 stop/TP，因此研究报告必须保留 `fill_time_assumption`、same-bar ambiguity 等字段。
- 已完成 `blocked_entry_event_export` Stage 1：canonical run `110c51eef593` 复跑导出 `512` 个 `block_reason=max_active_positions` 事件，`replay_entered_trades=58` 与 source 一致。
- 已完成 `replay_consistency_audit` Stage 2：source/replay entered trades、active path、final equity、blocked event repeat mismatch 均通过；但候选排序不是 source 原生持久化字段，只能通过源码 marker 和重复事件签名间接验证。
- 已完成 `stale_slot_continuation_review` Stage 3：统一 `42 bars = 168h`；26 个合格 stale slots，`forward_R_42_mean=-0.132`，`eventual_continuation_R_mean=-0.129`，说明旧仓继续占槽有弱点，但不等于替换一定有收益。
- 已完成 `blocked_candidate_vs_stale_slot_review` Stage 4：42 个合格比较事件，`net_delta_R_42_mean=0.309` 但 median `-0.223`、positive ratio `42.9%`、20% trimmed mean 约 `0.001`；结果为 `replacement_edge_not_supported`。
- 已完成 `replacement_closure_audit`：Stage 4 样本高度集中于 3 个 stale trades，top1 占 `83.333%`，cluster bootstrap 不能支持稳定 edge；capacity replacement 分支正式冻结为 `paused_no_stable_executable_edge`。
- 已明确不提高 `max_active_positions`，不启动 Stage 5 / Stage E shadow replacement，不修改 `config/settings.toml`。
- 2023-2024 historical universe 修复分支已经停止作为 `0.35` 的强验证路线；不重新打开该窗口，也不以当前 master list 伪装成无幸存者偏差的历史 universe。

#### B. prospective shadow 数据链路

已把研究从“事后只看实际 paper 交易”扩展为“记录每次扫描的候选上下文、每个计划的三线决策，以及被过滤候选的反事实路径”。这正是本项目此前讨论的“充分利用每次 4h 扫描全部信息”的落地版本。

已存在或已增强的核心表/记录：

- `paper_shadow_decisions`：4h plan-linked decision-state 和 daily candidate-level context 的统一研究记录。
- `paper_shadow_candidate_observations`：每个 scan candidate 的候选级观察，包含 rank、score、scanner action、entry/stop/TP、容量和市场状态等上下文。
- `paper_shadow_counterfactual_outcomes`：对候选或计划按 `reference_baseline`、`atr_reclaim_0_35_shadow`、`research_incumbent` 三条线初始化并持续推进的反事实结果。
- `paper_plans`、`paper_events`、`paper_snapshots`：paper 状态机的结构化主表。
- `runs`、`market_scans`：运行链路和 scan 证据。

记录口径已经明确区分：

1. **候选级诊断样本**：同一轮可能有 10 个候选，能够同时研究 rank、score、reclaim margin、market regime、capacity state 等，但候选之间相关，不能把 10 个候选简单当成 10 笔独立交易。
2. **plan-linked decision 样本**：实际进入 paper plan 状态机的机会，在 4h 更新中会记录三条线在同一时点的决策、容量状态、reclaim margin 等；这些才是严格前向三线比较的主要入口。
3. **mature terminal opportunity**：plan-linked opportunity 对应的 paper plan 已到达终端状态，并且满足成熟度定义；这是当前 pre-attribution gate 的关键指标。只有它达到门槛，才开始 direct filtering / capacity/path attribution。
4. **candidate counterfactual terminal outcome**：候选级反事实可能已经达到 stop/TP/TIME_EXIT 等终点，但它仍然可能没有对应真实 `paper_plan`。它适合诊断和扩大标签覆盖，不能直接替换 plan-level mature terminal opportunity。

已实现的行为：

- daily/import 为每个 scan candidate 写三条参照线，而不是只写最终导入 paper 的那一笔。
- 4h update 只读推进候选/计划反事实 outcome，不控制 paper 下单，不改变 `settings.toml`。
- `paper_shadow_0_35` 相关记录不会改变当前 paper plan 的实际入场逻辑。
- 4h 的 `ticker_24hr` 瞬断现在通过 `API_DELAY_SKIPPED` 事件和 snapshot 记录，不再因为单次 SSL/网络失败直接丢掉后续报告链路；这改善可观测性，不是策略变更。
- maturity 和 reconciliation 报告会同时显示 candidate observations、counterfactual outcomes、terminal counterfactual outcomes，避免把不同样本层级混在一起。

相关入口命令：

```powershell
python main.py paper shadow-decisions --limit 100
python main.py paper shadow-candidate-observations --limit 100
python main.py paper shadow-counterfactual-outcomes --limit 100
python main.py paper shadow-maturity --no-obsidian
python main.py paper shadow-reconciliation --no-obsidian
```

#### C. 严格 pre-attribution gate

`paper shadow-reconciliation` 已经把最小归因门槛代码化：

| 要求 | 最低值 | 当前值（2026-08-13） | 状态 |
|---|---:|---:|---|
| complete opportunities | 10 | 41 | 通过 |
| mature terminal opportunities | 5 | 0 | 未通过 |
| independent symbols | 3 | 19 | 通过 |
| `controls_paper` rows | 0 | 0 | 通过 |
| incomplete opportunities | 0 | 0 | 通过 |

因此当前 verdict 仍是：

- maturity：`decision_samples_not_mature`
- reconciliation：`reconciliation_waiting_for_terminal_outcomes`
- 不能开始 `0.35` direct filtering contribution 解释。
- 不能开始 capacity/path contribution 的正式归因。
- 不能把 `0.35` 升级为 paper deployment。

#### D. 当前真实前向样本状态

截至 2026-08-13 00:15 左右最新报告 `reports/2026-08-13/paper_shadow_maturity_review_2026-08-13_demo_v2.md` 和 `reports/2026-08-13/paper_shadow_reconciliation_2026-08-13_demo_v1.md`：

- `decisions=219`
- `opportunities=41`
- `candidate-only rows=120`
- `plan-linked decision rows=99`
- `complete opportunities=41`
- `incomplete opportunities=0`
- `controls_paper rows=0`
- `mismatch opportunities=0`
- `independent symbols=19`
- `candidate observations=20`
- `counterfactual outcomes=60`
- `terminal counterfactual outcomes=6`
- `mature terminal opportunities=0`
- `right-censored open rows=99`
- `right-censored ratio=100.00%`（对当前 plan-linked rows 而言）

当前只有一个 plan-linked open opportunity：

- plan id：`9734a33dea2e`
- symbol：`ONDOUSDT`
- status：`WATCHING`
- entry_low：`0.394505`
- entry_high：`0.41156785714285715`
- 最新 shadow decision 覆盖三条线，三线都没有 accepted entry；这是同一观察机会的三线同步记录，不是 99 个独立交易机会。

为什么 `mature terminal opportunities` 仍是 0：

- 目前所有 `paper_shadow_decisions` 的 plan-linked rows 都挂在 ONDOUSDT 这个仍为 `WATCHING` 的计划上。
- ONDOUSDT 多次产生的是 `RECLAIM_PENDING_SET` 或等待状态，4h close 没有站回 `entry_high`，因此没有进入 `ENTERED`，也没有 `STOPPED`、`TP1_HIT`、`CLOSED`、`INVALIDATED` 等终端状态。
- 计划一直未终结，所以严格 maturity 逻辑只能把这些 rows 标成 `right_censored_open`。
- 候选级反事实已经有 6 条终端结果，但候选没有形成对应的 plan-level terminal opportunity，不能直接满足 gate。
- 这不是“数据库没有记录”或“4h 没有运行”，而是严格样本定义要求观察对象完成，而唯一 plan-linked 对象还没有完成。

#### E. 4h 和 daily 自动化

当前 Windows 任务通过统一入口 `scripts/run_logged_paper_task.ps1` 运行：

- daily 任务：`CryptoTrading_DailyPaperUpdate`
- daily 时间：每天北京时间 `20:05`
- daily 内容：扫描、导入候选、更新 paper、生成报告/dashboard、写入候选级 shadow context、推进可推进的反事实并生成 maturity/reconciliation 报告。
- 4h 任务：`CryptoTrading_4H_PaperUpdate`
- 4h 时间：北京时间 `00:10`、`04:10`、`08:10`、`12:10`、`16:10`
- 4h 内容：只推进已有 paper plan 和 shadow state，不执行新的 scan，不执行 `add-from-scan`。
- daily `20:05` 负责覆盖 20:00 收盘后的日常处理；下一次 4h 是 `00:10`。

任务安装和运维特征：

- `WakeToRun=True`
- `StartWhenAvailable=True`
- 错过触发时间后尽快运行
- 失败后每 5 分钟重试，最多 3 次
- `MultipleInstances=IgnoreNew`
- 4h 单次上限约 30 分钟
- daily 单次上限约 2 小时
- 4h 不扫描、不增加 plan，避免和 daily 产生职责重叠。

截至本次检查：

- `CryptoTrading_4H_PaperUpdate`：2026-08-13 00:10 最近运行成功，`LastTaskResult=0`，下一次 `04:10`。
- `CryptoTrading_DailyPaperUpdate`：最近一次显示为 2026-08-11 20:05，`LastTaskResult=0`，`NumberOfMissedRuns=1`；这需要新会话继续核对 8/12、8/13 daily 是否有数据库 run 或日志证据，但不应凭任务元数据直接判定样本丢失。
- 数据库最新成功 run：`20260812_161003_81857d77`，类型 `paper_4h_update`，配置 hash `be7ec39ec21f6a83`，Git commit `761114a2198878e4376a08c6c91f3c0c24bbcb1b`。
- 数据库最新失败 run：`20260808_120503_c29c4076`，类型 `daily_full`，失败阶段为 scan，原因是 Binance SSL EOF；这属于网络失败，不是策略失败。
- 当前 `open_plan_count=1`。

#### F. 最近关键提交和文件状态

最近相关提交：

- `6c720df Add paper shadow candidate outcomes`：新增候选观察和反事实 outcome 数据链路。
- `4374851 Record atr reclaim Aug 5 shadow progress`：记录真实 daily/import 的候选级样本增长。
- `4edb503 Unify scheduled paper task entrypoint`：统一 daily/4h 计划任务入口。
- `e991858 Record scheduled task entrypoint commit hash`：记录统一入口提交关系。
- `80e0cbd Record Aug 6 automatic 4h reports`：纳入自动 4h 报告。
- `6cc77a2 Document sleep wake task operations`：记录唤醒运行和计划任务操作。
- `6a2bfc5 Record sleep wake operations commit hash`：记录相关操作提交。
- `761114a Record Aug 12 project status review`：截至 8/12 的状态审查、报告归档和 TODO 更新。

本次交接开始时工作区唯一未跟踪内容是 `reports/2026-08-13/`，里面包含 00:10 自动 4h 报告，以及本次只读 maturity/reconciliation 报告。它们应和本次文档/日志提交一起纳入 Git；`data/crypto_trading.db` 不应提交。

### 尚未完成的事项

#### P0：前向 shadow gate 尚未通过

- [ ] 等待 `paper_plan:9734a33dea2e` 或后续新的 plan-linked opportunities 进入终端 paper 状态。
- [ ] 使严格的 `mature terminal opportunities` 从 `0` 达到至少 `5`。
- [ ] 保持至少 `3` 个独立 symbol；当前已有 19，不是当前瓶颈。
- [ ] 保持 complete opportunities、三线齐全、`controls_paper=0`、incomplete=0；当前均正常。
- [ ] 成熟度达到后重新运行 `paper shadow-reconciliation`，确认 verdict 变为 `reconciliation_ready_for_attribution`。
- [ ] 在 gate 未通过前，不解释 `0.35` 的直接过滤收益，不下结论说它优于 baseline，也不把它升级为 paper deployment。

#### P1：gate 通过后的第一轮只读归因

达到 gate 后，只允许先做归因，不允许立即改配置。顺序建议如下：

1. 对 `reference_baseline` vs `atr_reclaim_0_35_shadow` 做 direct filtering attribution：统计 `filtered_loser`、`missed_winner`、同一 opportunity 的 first-hit/terminal outcome、实现 R、MFE、MAE。
2. 单独拆 direct filter contribution 与 capacity/path contribution：不能把因容量导致的不同入场顺序算成 `0.35` 过滤本身的收益。
3. 按 `candidate_rank`、`reclaim_margin_atr`、`capacity_state`、`scanner_action`、`market_regime`、`signal_density`、`active_positions`、`time_in_position` 分层。
4. 检查 symbol、月份、市场状态集中度，避免 5 个 terminal opportunity 全部来自一个币或一个行情阶段。
5. 检查 right-censoring、API delay、same-bar ambiguity、数据缺失和状态不一致；任何异常都先标记为数据问题，不直接归因于策略规则。
6. 形成“非技术结论 + 技术证据 + keep/retest/reject/insufficient evidence”三层报告。

#### P1：候选级数据如何使用

- [ ] 继续让 daily 保存每个候选的 rank、score、scanner action、entry/stop/TP、ATR、市场状态、capacity state 等字段。
- [ ] 继续让 4h 只读推进被过滤候选的 counterfactual path。
- [ ] 核对 candidate-level terminal outcomes 是否能形成足够广泛的诊断证据，尤其是 `0.35` 拒绝但 baseline 可能入场的候选。
- [ ] 候选级结果只能作为诊断和标签扩展，最终统计要标注候选相关性，不能和独立组合级交易样本混合计算置信度。
- [ ] 如发现候选已终结而 plan 没有 plan-linked outcome，先审计数据关联和样本定义，再决定是否需要代码修复；不能为了让 gate 通过而放宽定义。

#### P2：容量/排序研究仍未完成

- [ ] 等严格 shadow gate 通过后，研究满仓阻挡的机会成本：每次记录 rank、阻挡原因、active slots、被阻挡候选后续 R、替代旧仓后续 R。
- [ ] 先使用已有 `blocked_entry_event_export`、`replay_consistency_audit` 和 `stale_slot_continuation_review` 的口径，不直接修改 `max_active_positions`。
- [ ] capacity replacement 分支当前是 `paused_no_stable_executable_edge`，不能未经新计划重新开启。
- [ ] 如果未来重启，必须先提出事前确定的 slot selection 规则，并用更广泛、去聚类的 walk-forward 样本验证；不能使用 oracle 规则或事后挑选最差旧仓。
- [ ] 新 challenger 方向暂定为 candidate ranking / full-capacity opportunity cost，但应等 shadow logging/reconciliation 稳定后再正式开始。

#### P2：退出和持仓时间研究仍未完成

- [ ] `max_holding_bars_without_tp1=42` 的历史和组合回测方向较好，但 paper 前向只出现过 3 个超过 42 根 4h 的 terminal cases，且仅 2 个独立 symbol，结论是 `defer_keep_review_insufficient_forward_evidence`。
- [ ] 继续 daily + 4h 观察，目标至少 5 个独立 symbol 或 8-10 个 over-42h terminal cases 后，再重开 42-bar keep review。
- [ ] 尚未完成 TP1 部分止盈、TP1 后保本、EMA20 trailing、ATR trailing、固定 TP2 vs 趋势退出、ATR 动态止损等正式单变量实验的最终 keep/revert 决策。
- [ ] 任何退出实验都要注意它同时改变持仓时长、容量释放和后续候选机会，必须单独拆解退出收益和容量路径收益。

#### P2：后续入场因素仍未完成

以下属于未来单变量研究，不是当前立即改配置的 TODO：

- [ ] 测试更靠近 `entry_low` 的入场方式，而不是默认按 `entry_high` 附近成交。
- [ ] 测试 RSI 从 45-55 区间恢复向上的条件。
- [ ] 拒绝主要由放量下跌驱动的形态。
- [ ] 避免 4h 趋势仍明显向下时接飞刀。
- [ ] 更严格追高排除/降级。
- [ ] 只有在 incumbent 前向证据稳定后，才选择其中一个方向做新的 `new_challenger`。
- [ ] MACD 暂不升级为 `macd_hist_4h > 0` 硬门槛；若研究 MACD，只做 histogram 斜率、连续恶化、reclaim 时改善等离线变体。

#### P3：回测基础设施待办

- [ ] K 线缓存足够热后，不使用 `--source-limit` 跑更大 dynamic-universe A/B。
- [ ] 继续研究 Binance 历史/退市币 symbol master，降低当前 `exchangeInfo` master 带来的 survivorship bias。
- [ ] 保持固定 symbol universe、日期区间、配置 hash 和单变量变更纪律。
- [ ] 所有实验报告保留 trades、closed_trades、胜率、PF、平均 R、止损率、Sharpe、MDD、净收益和 `sample_sufficient`。
- [ ] `closed_trades < 20` 的结果只能标为样本不足，不能作为 keep 依据。

#### P4：运维和数据链路待办

- [ ] 新会话首先核对 `CryptoTrading_DailyPaperUpdate` 的 8/12、8/13 实际 DB run、日志和报告，解释 `NumberOfMissedRuns=1` 是否是真缺失、任务元数据滞后，还是正常错过后补跑。
- [ ] 持续观察 4h/daily 是否维持 `LastTaskResult=0`，以及是否产生新的 `API_DELAY_SKIPPED`、SSL 或超时错误。
- [ ] 如果网络错误再次出现，先保留失败 run 和错误阶段，不手动补造研究样本；按运行日志决定是否需要运维修复。
- [ ] 任何脚本/代码/配置/项目文档改变后，必须更新 `dailylog.md`；如果 TODO 或 roadmap 改变，同步更新 `TODO.md` / `开发计划.md`；如果产生实验判断，更新 Obsidian 实验日志。
- [ ] 任何项目文件变更后创建 Git commit 并 push 到 `origin`；staging 时必须包含 `reports/`，但不要提交 `data/crypto_trading.db`。

### 下一步直接执行指令

新会话打开后，先在项目目录执行以下命令。它们都是只读检查，不会制造 paper 样本，也不会改变策略配置：

```powershell
Set-Location 'D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects'
git status --short --branch
python main.py db status
python main.py paper shadow-maturity --no-obsidian
python main.py paper shadow-reconciliation --no-obsidian
python main.py paper shadow-decisions --limit 30
python main.py paper shadow-candidate-observations --limit 30
python main.py paper shadow-counterfactual-outcomes --limit 30
Get-ScheduledTaskInfo -TaskName 'CryptoTrading_4H_PaperUpdate' | Select-Object TaskName,LastRunTime,LastTaskResult,NextRunTime,NumberOfMissedRuns
Get-ScheduledTaskInfo -TaskName 'CryptoTrading_DailyPaperUpdate' | Select-Object TaskName,LastRunTime,LastTaskResult,NextRunTime,NumberOfMissedRuns
```

然后做以下顺序核对：

1. 以最新 `paper_shadow_reconciliation` 的 Summary 和 Pre-Attribution Gate 为准，不以旧报告或 `TODO.md` 中早期数字为准。
2. 确认当前是否仍只有 `paper_plan:9734a33dea2e / ONDOUSDT` 一个 plan-linked opportunity。
3. 查看最新 daily/4h run 的 `status`、`step`、`error_message`、`config_hash` 和 `git_commit`。
4. 如果发现新 terminal plan，重新检查三线是否齐全、是否 `controls_paper=0`、是否存在 incomplete/mismatch。
5. 若 gate 仍未通过，继续等待正常任务，不手动运行 daily/cycle 来“制造”机会，不运行新的近端 `0.35` A/B。
6. 若 gate 已通过，只生成只读 attribution 报告，先不要修改 `config/settings.toml`、`max_active_positions` 或 paper 状态机。

如需进一步核对 ONDOUSDT 的具体状态，可以使用下面的只读 SQL 检查；不要通过 SQL 修改数据库：

```powershell
@'
import sqlite3
from pathlib import Path

db = Path("data/crypto_trading.db")
con = sqlite3.connect(db)
con.row_factory = sqlite3.Row
for row in con.execute("""
    SELECT plan_id, symbol, status, created_at, updated_at,
           entry_low, entry_high, source_scan_id, source_rank
    FROM paper_plans
    WHERE plan_id = '9734a33dea2e'
"""):
    print(dict(row))
con.close()
'@ | python -
```

如果需要检查最近运行是否有真正缺失，优先查看：

```powershell
Get-Content -LiteralPath 'logs\daily_paper_update.log' -Tail 160
Get-Content -LiteralPath 'logs\paper_4h_update.log' -Tail 160
Get-ChildItem -LiteralPath 'reports\2026-08-13' -Force | Sort-Object LastWriteTime
```

### 重要声明

- 当前研究阶段是“等待 terminal outcomes”，不是“已经证明 `0.35` 优于其他因子”。
- `mature terminal opportunities=0` 的含义是严格的 plan-level 观察对象尚未终结，不是说系统完全没有数据，也不是说 candidate-level 反事实没有任何终端结果。
- 当前 `terminal counterfactual outcomes=6` 与 `mature terminal opportunities=0` 可以同时成立；前者是候选/反事实层，后者是严格 plan-linked gate 层。
- `decisions=219` 也不等于 219 笔独立交易；其中 120 条是候选级记录，99 条是同一个 ONDOUSDT plan-linked opportunity 在多个 4h 时点的重复决策观察。
- 当前 4h/daily 脚本的主要任务是保证数据自然积累和状态可审计，不是主动提高交易频率。把 4h 改成 2h 不是当前优先级。
- 不要为了让成熟度门槛通过而放宽 terminal 定义、把候选样本伪装成 plan 样本、删除 right-censored rows、手动制造 plan 或补造交易。
- 不要修改 `config/settings.toml`，不要把 `atr_reclaim_0_35` 直接接管 paper，下单或实盘都不在授权范围内。
- 不要重新开启 `2023-2024` historical repair branch，不要开始新的近端历史 `0.35` A/B，不要继续做无目标的 ATR 阈值搜索。
- 不要修改 `max_active_positions=5`。capacity replacement 已明确为 `paused_no_stable_executable_edge`，若要重启必须先提出新的单独研究计划和批准标准。
- 如果新会话要提出实验，必须先说明：系统级目标、唯一问题、所属研究优先级、事实/观察/假设/决策的区分、支持/拒绝/证据不足的判定标准，以及是否允许修改配置。
- 所有真实资金风险保持关闭。`paper` 也只是研究观察，不应被描述成实际交易表现。





## 2026-07-30 12:26 +08:00

### ????
`D:\OneDrive - whut.edu.cn\??\CryptoTradingPorjects`

### ????
???????? `2023-07-01 -> 2024-07-01` ??????? N2-N4 ??? historical universe ?????????????????????

### ??????
- ?? `reports/2026-07-30/atr_reclaim_2023_2024_window_abandonment_decision_2026-07-30_v1.md`????? `abandon_2023_2024_window_for_atr_reclaim_validation`?
- ?? `reports/2026-07-30/atr_reclaim_next_action_plan_2026-07-30_v1.md`??? Stage A-E ?????
- ?? `reports/2026-07-30/atr_reclaim_recent_window_eligibility_audit_plan_2026-07-30_v1.md`????????????????? A/B ???
- ?? `reports/2026-07-30/atr_reclaim_prospective_shadow_observation_plan_2026-07-30_v1.md`??? prospective shadow observation schema?
- ??? `dailylog.md`?`TODO.md`?`EXPERIMENT_LEDGER.md`?`????.md` ? Obsidian ?????

### ???????
- ????/?????????
- ?????? recent-window eligibility audit?
- ???? prospective shadow logger?

### ?????????
```powershell
git status --short
git add dailylog.md TODO.md EXPERIMENT_LEDGER.md ????.md handoff.md reports/
git commit -m "Record atr reclaim validation reset plan"
git push origin main
```

### ????
- `atr_reclaim_0_35_status=experimental_candidate_unvalidated`?
- ??? 2023-2024 historical universe???? corrected N1??? path fork audit?
- ??? `config/settings.toml`???? `atr_reclaim_0_35`???? `max_active_positions`?
- ???????????? recent-window eligibility audit ? prospective shadow logger ??????? A/B?

## 2026-07-30 11:44 +08:00

### ????
`D:\OneDrive - whut.edu.cn\??\CryptoTradingPorjects`

### ????
???????? N3 ???????????????? historical membership ????? source-backed historical master ?????????? `atr_reclaim_0_35` ????????

### ??????
- ?? `scripts/n4_historical_master_mvp.py`?
- ?? N4??? `reports/2026-07-30/atr_reclaim_stage_n4_historical_master_mvp_2026-07-30_v1.md`?`*_master_v1.json`?`*_review_queue_v1.json`?`*_raw_v1.json`?
- ?????total rows `413`?`active_current_master=266`?`excluded_by_strategy_universe_rule=20`?`historical_standard_gap_requires_mapping=127`?
- verdict=`historical_master_mvp_built_validation_blocked`?
- ??? `dailylog.md`?`TODO.md`?`EXPERIMENT_LEDGER.md`?`????.md` ? Obsidian ?????
- ??????`python -m compileall scripts\n4_historical_master_mvp.py`?`python tests\test_universe.py`?

### ???????
- ?? commit/push?
- 127 ? blocking review queue ??? official/source-backed mapping?
- N4 MVP ??????? A/B?

### ?????????
```powershell
git status --short
git add scripts/n4_historical_master_mvp.py dailylog.md TODO.md EXPERIMENT_LEDGER.md ????.md handoff.md reports/
git commit -m "Add atr reclaim N4 historical master MVP"
git push origin main
```

### ????
- ???? third-window corrected N1???????????
- ???? `atr_reclaim_0_35`????? `config/settings.toml`????? `max_active_positions`?
- ???? official-source mapping pipeline?

## 2026-07-30 11:36 +08:00

### ????
`D:\OneDrive - whut.edu.cn\??\CryptoTradingPorjects`

### ????
????? N2 ????????????????? `atr_reclaim_0_35` ???? `2023-07-01 -> 2024-07-01` ??????????????????????????????? historical membership ?????????

### ??????
- ?? `scripts/n3_historical_membership_dataset.py`??? N2 ? historical/current JSON??? historical membership dataset MVP?
- ?? N3??? `reports/2026-07-30/atr_reclaim_stage_n3_historical_membership_dataset_2026-07-30_v1.md`?
- ?????`missing_from_current_master=147`??? `excludable_missing_count=20`?`standard_gap_count=127`?`standard_gap_ratio_pct=32.32%`?
- ?? gate decision `reports/2026-07-30/atr_reclaim_stage_n3_gate_decision_2026-07-30_v1.md`??? `third_window_not_recoverable_without_historical_master`?
- ??? `dailylog.md`?`TODO.md`?`EXPERIMENT_LEDGER.md`?`????.md` ? Obsidian `CryptoTrading ????.md`?
- ??????`python -m compileall scripts\n3_historical_membership_dataset.py`?`python tests\test_universe.py`?

### ???????
- ???? commit/push?????????
- ???? source-backed historical master?N3 ?? MVP ???
- 127 ? standard-like missing symbols ????????? `delisting / rename / migration / tradable_to / source / confidence`?

### ?????????
```powershell
git status --short
git add scripts/n3_historical_membership_dataset.py dailylog.md TODO.md EXPERIMENT_LEDGER.md ????.md handoff.md reports/
git commit -m "Add atr reclaim N3 historical membership gate"
git push origin main
```

### ????
- ???????? corrected N1???????????N3 ?????????????????
- ???? `atr_reclaim_0_35`????? `config/settings.toml`????? `max_active_positions`?
- ????? source-backed historical master???????????

## 2026-07-30 00:57 +08:00

### ????
`D:\OneDrive - whut.edu.cn\??\CryptoTradingPorjects`

### ????
?????? N2-A / N2-B / ?? N0 / ???????? / ? gate ?????? N1 ????????????? `atr_reclaim_0_35` ????? `2023-07-01 -> 2024-07-01` ??????

### ??????
- ?? `scripts/n2_universe_audit.py`??? current master listing date?local kline coverage?Binance public-data historical membership ???
- ?? N2????? `reports/2026-07-30/atr_reclaim_stage_n2_universe_audit_2026-07-30_v2.md`?verdict=`diagnostic_only_historical_membership_gap`?
- ?????418 ? current master symbols ???? listing date?`listed_after_window=152`?`listed_inside_window=49`?`full_window_coverage=208`?`partial_window_coverage=9`???? historical USDT symbols `413`??? `147` ??? current master?
- ?? `reports/2026-07-30/dynamic_master_full_listing_enriched_2026-07-30_v2.json` ?? N0??? `reports/2026-07-30/atr_reclaim_n0_readiness_audit_2026-07-30_v1.md`?verdict=`n0_conditional_pass_with_alignment_warning`?
- ?? gate decision ?? `reports/2026-07-30/atr_reclaim_stage_n2_gate_decision_2026-07-30_v1.md`??? `third_window_diagnostic_only_do_not_rerun_n1`?
- ??? `dailylog.md`?`TODO.md`?`EXPERIMENT_LEDGER.md`?`????.md` ? Obsidian `CryptoTrading ????.md`?
- ??????`python -m compileall scripts\n2_universe_audit.py`?`python tests\test_universe.py`?

### ???????
- ???? commit/push??????????
- ?????? N1???? N2 gate failed????? historical membership ?????
- ??????????????
- ????????? historical symbol membership dataset?

### ?????????
```powershell
git status --short
git add .gitignore scripts/n2_universe_audit.py dailylog.md TODO.md EXPERIMENT_LEDGER.md ????.md reports/
git commit -m "Add atr reclaim N2 universe gate audit"
git push origin main
```

### ????
- ???? `atr_reclaim_0_35`????? `config/settings.toml`????? `max_active_positions`?
- N0 ? conditional pass ????? master + local kline readiness ?????????? historical membership ???????? N2-B gate ???
- `reports/2026-07-30/.n2_cache/` ??? `.gitignore`???????????
- 2026-07-30 00:10 ????? paper ???? `reports/2026-07-30/`??????? reports ?????

## 项目目录

`D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects`

- **Git 远端**：`https://github.com/Goodyenough/wbj-CryptoTrading.git`
- **当前分支**：`main`
- **最新已 push commit**：`d45b609`
- **运行环境**：Windows 11 Pro，PowerShell，Python，SQLite
- **数据库**：`data/crypto_trading.db`（SQLite，**两段回测必须串行**）

---

## 任务背景

当前处于"策略质量优化"阶段。sensitive 组合（`risk_off_core_buy=false` + `entry_reclaim_close=true` + `tp1_ema_trailing_stop=true` + BTC -3% / ETH -5% / `require_both_trend=true`）已于 2026-06-11 写入 `settings.toml` 并在模拟盘生效，观察期至 **2026-07-02**。

本次 session 的主要工作：市值分层两段 walk-forward、max_holding 三阈值两段 walk-forward、实现并运行 `large_cap_only_risk_off` 实验。

---

## 已完成的工作

| 内容 | commit / 状态 |
|---|---|
| 市值分层 2024-07→2025-06 早期段：large-cap +14.14%/MDD 7.77%，altcoin +11.71%/MDD 15.92% | `d45b609` |
| max_holding 三阈值（18/30/42根）两段全部改善，42根最平衡（近端 MDD 9.27%，net +26.93%） | `d45b609` |
| 实现 `risk_off_large_cap_buy_enabled` 字段（`config.py`、`scanner.py`、`replay.py`）| `d45b609` |
| 注册 `large_cap_regime` dimension，新增 `large_cap_only_risk_off` 实验 | `d45b609` |
| `large_cap_only_risk_off` 两段 walk-forward：早期 +11.17%，近端 -6.24%，结论 `retest` | `d45b609` |
| dailylog、TODO、开发计划、实验日志全部更新 | `d45b609` |
| experiments.toml 新增 `max_holding_18x4h_no_tp1` 和 `max_holding_42x4h_no_tp1` 定义 | `d45b609` |

---

## 尚未完成的事项

### 1. 2026-07-02 模拟盘复盘决策（主线，等待观察期结束）

届时检查：entry_reclaim 拦截次数、RISK_OFF 频率、WLDUSDT/ONDOUSDT 持仓结果，决定 sensitive 组合是否 keep。观察期结束后再一起决定下一步实验方向。

### 2. `sensitive + max_holding_42x4h` 组合实验（等观察期结束后再做）

**不着急，等 2026-07-02 复盘后再推进。**

当前准备工作已完成：
- `abtest.py` 已注册 `combined_regime_entry_exit_sensitivity_holding` dimension（commit `6cab41d`）
- `experiments.toml` 尚未添加实验定义（留待观察期结束后补）

届时在 `experiments.toml` 末尾添加：

```toml
[sensitive_max_holding_42x4h]
enabled = true
description = "Sensitive combo (6 params) + max_holding_42x4h: validate that time-based exit still improves on top of sensitive defaults."
dimension = "combined_regime_entry_exit_sensitivity_holding"

[sensitive_max_holding_42x4h.overrides.analysis]
risk_off_core_buy_enabled = false
entry_reclaim_close_enabled = true
tp1_ema_trailing_stop_enabled = true
regime_btc_7d_drop_pct = -3.0
regime_eth_7d_drop_pct = -5.0
regime_require_both_trend = true

[sensitive_max_holding_42x4h.overrides.backtest]
max_holding_bars_without_tp1 = 42
```

然后串行跑两段 A/B（`2024-07-01 -> 2025-06-01` 和 `2025-06-01 -> 2026-06-01`），使用 `reports/2026-06-09/dynamic_master_full.json`，`--max-symbols 40`。

---

## 重要声明

1. **SQLite 单写**：两段 A/B 必须串行，不能并行跑。
2. **symbol master**：所有回测使用 `reports/2026-06-09/dynamic_master_full.json`（418 个币）。
3. **实验新增 dimension 必须先在 `abtest.py` 的 `ALLOWED_OVERRIDE_PATHS` 里注册**，否则运行时报错。`combined_regime_entry_exit_sensitivity_holding` 已注册（未 commit）。
4. **`daily_trend_required` 已 reject**，不要在新实验里复用。
5. **`large_cap_only_risk_off` 已 retest**：近端熊市反而变差，不要 keep，不要继续推进参数叠加方向。
6. **当前未 commit 的文件**：`src/crypto_trading_system/abtest.py`（已加新 dimension）、`TODO.md`、`scripts/install_daily_task.ps1`——下次 session 完成 experiments.toml 添加后一起 commit。
7. **定时任务**：`CryptoTrading_DailyPaperUpdate` 每天 20:05 自动执行，但当前触发时间仍是 09:00，需要管理员权限运行 `powershell -ExecutionPolicy Bypass -File scripts\install_daily_task.ps1` 修正。

---

# Handoff — 2026-06-11 18:00 +08:00


## 项目基本信息

- **项目目录**：`D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects`
- **Git 远端**：`https://github.com/Goodyenough/wbj-CryptoTrading.git`
- **当前分支**：`main`
- **最新 commit**：`0ac8f74` (已 push 到 origin/main)
- **运行环境**：Windows 11 Pro，PowerShell，Python，SQLite
- **数据库**：`data/crypto_trading.db`（SQLite，单文件，**不支持并发写入，两段回测必须串行**）

---

## 系统架构概览

```
main.py                          # 入口，子命令：scan / daily / backtest / abtest / paper 等
config/
  settings.toml                  # 生产配置（当前已激活 sensitive 组合）
  experiments.toml               # A/B 实验定义，所有 variant 参数在此声明
src/crypto_trading_system/
  config.py                      # Settings dataclass，load_settings()
  scanner.py                     # 市场扫描，输出 BUY_CANDIDATE
  market_regime.py               # classify_market_regime()，判断 RISK_ON/NEUTRAL/RISK_OFF
  paper_trader.py                # 模拟盘：add_from_scan / update_paper_trades / generate_paper_report
  trade_state.py                 # 单笔交易状态机：step_trade()
  abtest.py                      # A/B 实验框架，ALLOWED_OVERRIDE_PATHS 白名单
  backtest/replay.py             # 回测主循环
  backtest/runner.py             # 回测入口
  indicators.py                  # ema(), percent_change() 等
  models.py                      # PaperTrade, PaperTradeEvent dataclass
  storage.py                     # DB schema，建表语句
reports/                         # 每日报告输出目录（按日期子目录）
scripts/
  daily_paper_update.bat         # 每天 20:05 定时执行：scan→add-from-scan→update→report
logs/
  daily_paper_update.log         # 定时任务日志
```

---

## 当前生产配置（settings.toml [analysis] 关键字段）

```toml
risk_off_core_buy_enabled = false       # RISK_OFF 时不开新 BTC/ETH 多单
entry_reclaim_close_enabled = true      # 进入 entry zone 后须 4h 收盘确认才入场
tp1_ema_trailing_stop_enabled = true    # TP1 命中后用 4h EMA20 跟踪止损
regime_btc_7d_drop_pct = -3.0          # BTC 7日跌幅阈值（旧值 -5.0）
regime_eth_7d_drop_pct = -5.0          # ETH 7日跌幅阈值（旧值 -8.0）
regime_require_both_trend = true        # BTC+ETH 必须同时 price>EMA20>EMA50 才算趋势确认
```

这六个参数合称 **sensitive 组合**（`risk_off_no_core_entry_reclaim_ema_stop_sensitive`），于 2026-06-11 写入 settings.toml，模拟盘当日起生效。

---

## 实验历史与结论（按时间顺序）

### 1. tp1_ema20_trailing_stop（单项）
- 结论：retest，单独使用效果有限，近端 MDD 上升

### 2. risk_off_no_core_entry_reclaim_ema_stop（三项组合）
- 三项：`risk_off_core_buy=false` + `entry_reclaim_close=true` + `tp1_ema_trailing_stop=true`
- 早期段 2024-07→2025-06：PF 0.91→1.53，净收益 -5.6%→+16.7%，MDD 18.7%→15.0%
- 近端段 2025-06→2026-06：PF 0.73→1.05，净收益 -10.6%→+1.2%，MDD 24.2%→18.7%
- **verdict：candidate_keep_review**

### 3. daily_trend_required（单项 + 四项组合）
- 单项 reject：近端段止损率 77%→89%，净收益 -10%→-23%
- 四项组合 reject：近端段止损率 77%→92%，净收益 -14%→-7.8%（不如三项组合）

### 4. regime_sensitive（仅收紧阈值）
- BTC -5%→-3%，ETH -8%→-5%，require_both_trend=true
- 单独使用方向改善但仍亏损，需配合出入场规则

### 5. risk_off_no_core_entry_reclaim_ema_stop_sensitive（三项 + 收紧阈值，当前主候选）

四段 walk-forward 完整结果：

| 段 | 市场环境 | baseline 净收益 | variant 净收益 | PF | MDD |
|---|---|---:|---:|---:|---:|
| 2024-07→2025-01 | 牛市 | +2.4% | **+25.4%** | 2.52 | 9.0% |
| 2024-07→2025-06 | 牛+震荡 | -14.3% | **+18.0%** | 1.58 | 15.0% |
| 2025-01→2025-06 | 震荡转熊⚠ | -19.7% | **-6.5%** | 0.53 | 10.0% |
| 2025-06→2026-06 | 熊市 | -14.2% | **+5.5%** | 1.17 | 17.8% |

⚠ 2025-01→2025-06 段：sample_insufficient（15笔）+ possible_over_filtering，数据供参考。四段均优于或持平三项组合。

---

## 模拟盘状态

- **账户**：demo，初始权益 10,000 USDT，单笔风险 1%
- **定时任务**：Windows 任务计划 `CryptoTrading_DailyPaperUpdate`，每天 20:05 自动执行
- **执行脚本**：`scripts/daily_paper_update.bat`，依次跑 scan → add-from-scan → paper update → paper report
- **日志**：`logs/daily_paper_update.log`
- **sensitive 组合生效日期**：2026-06-11
- **建议观察截止**：2026-07-02（约 3 周），届时根据模拟盘结果决定是否继续保留

### paper report 现包含的信息（2026-06-11 新增）

每日报告新增三项，专门用于 3 周后的判断：

1. **今日大盘环境节**：regime 状态（RISK_ON/NEUTRAL/RISK_OFF）、BTC/ETH 7d 涨跌与阈值对比、趋势确认情况
2. **RECLAIM_PENDING 事件**：每次价格进入 entry zone 但 4h 收盘未确认时记录事件，可追溯 entry_reclaim 拦截了哪些单
3. **统计补充**：Entry reclaim blocks 累计次数、平均持仓时长

---

## 关键代码位置

### market_regime.py — RISK_OFF 判断逻辑

```python
def classify_market_regime(
    btc_1d, eth_1d,
    btc_7d_drop_pct=-5.0,    # settings.analysis.regime_btc_7d_drop_pct
    eth_7d_drop_pct=-8.0,    # settings.analysis.regime_eth_7d_drop_pct
    require_both_trend=False  # settings.analysis.regime_require_both_trend
) -> MarketRegime
# RISK_ON 条件：trend_ok AND btc_not_breaking AND eth_not_breaking
# require_both_trend=True 时，BTC+ETH 必须同时满足 price>EMA20>EMA50
# 调用方：replay.py:622, scanner.py:356（均透传 settings 参数）
# regime_analysis.py:148 用默认值（仅用于事后分析，不影响回测/扫盘）
```

### paper_trader.py — entry_reclaim 逻辑

```python
# update_paper_trades() 约 437 行
# 条件：entry_reclaim_enabled AND status==WATCHING AND price<=entry_high
# 若 4h 最新已收盘 close < entry_high → 记录 RECLAIM_PENDING 事件，跳过入场
# 每天定时任务运行一次，不会重复记录
```

### abtest.py — dimension 白名单

新增的两个 dimension（可直接在 experiments.toml 引用）：

```python
"regime_sensitivity": {
    "analysis.regime_btc_7d_drop_pct",
    "analysis.regime_eth_7d_drop_pct",
    "analysis.regime_require_both_trend",
},
"combined_regime_entry_exit_sensitivity": {
    "analysis.risk_off_core_buy_enabled",
    "analysis.entry_reclaim_close_enabled",
    "analysis.tp1_ema_trailing_stop_enabled",
    "analysis.regime_btc_7d_drop_pct",
    "analysis.regime_eth_7d_drop_pct",
    "analysis.regime_require_both_trend",
},
```

---

## 已知问题 / 技术债

### 1. tp1_ema_trailing_stop corner case（未修，低风险）
- **现象**：TP1 命中时若 4h K 线不足 20 根，`tp1_trailing_ema_stop_active` 在内存中被置为 True，但 EMA 计算返回 None；下次 update 时可能突然激活跟踪止损
- **位置**：`trade_state.py`（step_trade 内部），`paper_trader.py:454-457`
- **影响**：模拟盘偶发，不影响回测（回测有足够历史 K 线）
- **修法**：仅当 EMA 有效时才设 active=True

### 2. tp1_trailing_ema_stop_active 不持久化（未修）
- **现象**：`PaperTrade.tp1_trailing_ema_stop_active` 是 dataclass 字段，DB 里没有对应列；每次 update 重新加载 trade 时该字段重置为 False
- **影响**：TP1_HIT 状态的跟踪止损每次 update 都重新从零判断，行为与回测不完全一致
- **修法**：在 paper_trades 表加列 `tp1_trailing_ema_stop_active INTEGER NOT NULL DEFAULT 0`，或改为从事件日志推断

### 3. 幸存者偏差（未修，结构性问题）
- Binance 历史退市币未纳入 symbol master（`reports/2026-06-09/dynamic_master_full.json`）
- 所有回测结果偏乐观，无法量化偏差幅度

---

## 接下来可以做的实验（按优先级）

### A. 持仓时间过滤（需改代码）
- **假设**：部分止损单是入场后长期横盘最终慢慢跌破止损，而非快速止损
- **实验**：入场后 N 根 4h K 线内未触 TP1 则强制平仓（N 约 18～36）
- **需改**：`trade_state.py`（step_trade 加 bar_count 计数）+ `config.py` 加参数 + `abtest.py` 白名单 + `experiments.toml` 加实验定义

### B. 市值分层分析（无需改代码，直接跑）
- **目标**：确认亏损主要来自 altcoin 还是 large-cap，熊市是否应只做 large-cap
- **做法**：用 `--symbol-master-file` 分别传只含 large-cap 和只含 altcoin 的 master JSON，跑两段对比回测
- **large-cap 参考**：BTC/ETH/BNB/SOL/XRP/DOGE/ADA/AVAX/TRX/TON 等前 20

### C. 修 tp1_trailing_ema_stop_active 持久化（改代码）
- 加 DB 迁移，在 paper_trades 表加列，保证模拟盘行为与回测一致

---

## 常用命令

```bash
# A/B 实验（两段必须串行，不能同时跑）
python main.py abtest --experiment <实验名> \
  --dynamic-universe \
  --symbol-master-file reports/2026-06-09/dynamic_master_full.json \
  --start 2024-07-01 --end 2025-06-01 \
  --max-symbols 40 --allow-data-gaps --no-obsidian

# 回测
python main.py backtest-dynamic-universe \
  --symbol-master-file reports/2026-06-09/dynamic_master_full.json \
  --start 2024-07-01 --end 2025-06-01 \
  --max-symbols 40 --allow-data-gaps --no-obsidian

# 模拟盘手动触发（定时任务每天 20:05 自动跑）
python main.py daily --no-obsidian

# 只生成模拟盘报告（不跑扫盘）
python main.py paper report

# 确认定时任务是否正常
Get-ScheduledTask -TaskName "CryptoTrading_DailyPaperUpdate" | Get-ScheduledTaskInfo | Select-Object NextRunTime
```

---

## 重要约束

1. **SQLite 单写**：两段回测/实验不能并行，必须串行
2. **symbol master**：所有回测使用 `reports/2026-06-09/dynamic_master_full.json`（418 个币），不要用其他文件
3. **实验新增 dimension**：必须先在 `abtest.py` 的 `ALLOWED_OVERRIDE_PATHS` 里注册，否则运行时报错
4. **不要直接改 settings.toml 的 analysis 参数来做实验**：应通过 experiments.toml + abtest 命令，保持生产配置稳定
5. **daily_trend_required 已 reject**：不要在新实验里复用，浪费算力
