# CryptoTradingSystem 实验账本

## 2026-10-15 16:06 +08:00 - 实时1h动能启动候选全样本因果验证

### 背景
`CRYPTOTRADIN-129`阶段A发现4h确认经常晚1至3小时，但它先知道哪些事件最终会获得4h确认，只能给出有利上界。本轮按用户授权独立生成全部实时可见的早期reclaim候选，把未保持到4h收盘的假启动也纳入。

### 假设
如果仅凭当时已完成的1h与4h信息就能识别有延续性的启动，那么唯一冻结的RT1候选应在早窗和近窗、taker与stress成本、同币不重叠、14日区块和集中度检查下均保持正净期望。

### 实验
- 实验：`realtime_momentum_start_v1 / CRYPTOTRADIN-135`。
- 变更：无生产策略变更；复用B watch计划和最近已完成4h资格，在4h区间前3根已完成1h中，累计触区且1h收盘站上`entry_high`时，于下一根1h开盘成交；未来4h确认只作事后标签。
- 样本：Binance Spot USDT current-survivor冻结输入；早窗UTC `[2024-07-01,2025-06-01)` 1,090笔，近窗`[2025-06-01,2026-06-01)` 770笔；固定`+5%/-3%/48h`，taker/stop-first主口径，stress与target-first敏感性。

### 白话结论
答案是否定的：现在这个仅靠价格触区和1h收盘站回去的实时信号，分不清真正启动和短暂反弹。约四成候选没有保持到4h收盘，这批交易两窗平均亏约1.6%，足以把最终会确认的盈利子群全部拖成亏损。阶段A的改善主要来自事后先筛掉了这些失败启动。

### 结果
- trades / closed_trades：早窗`1090/1090`，近窗`770/770`；取消成交和退出删失均为0。
- 候选频率：早/近窗每30日`97.6/63.3`笔，覆盖`26/24`个信号周；1h/2h/3h offset为`561/311/218`与`373/225/172`。
- 保持到4h确认：早窗`657/1089=60.33%`，近窗`481/767=62.71%`；约37%–40%为未保持候选。
- 胜率：taker早/近`37.98%/37.27%`；stress`36.42%/35.32%`。
- Profit factor：taker`0.844/0.783`；stress`0.683/0.622`。
- Sharpe、最大回撤、CAGR：N/A；all-events与symbol-only不是完整跨币资金账户。
- 净收益：taker`-0.2984%/-0.3854%`；stress`-0.6704%/-0.7477%`；symbol-only`-0.3817%/-0.4760%`。
- taker mean net 14日区间：早窗`[-1.1062,+0.2469]`，近窗`[-1.1179,+0.2984]`；两窗点估计均负，区间跨零。
- 机制标签：保持确认组净收益`+0.5825%/+0.3309%`、PF`1.380/1.231`；未保持组`-1.6472%/-1.5880%`、PF`0.336/0.320`。
- 同根顺序：stop-first与target-first结果相同，无双触发翻号；leave-one-symbol/week最差均值仍为负。
- 测量：因果违规0，候选1h/4h聚合`1090/1090`与`770/770`通过，成交取消0、删失0。

### 结论
`revert / reject_current_realtime_reclaim`：当前RT1 price-only实时定义不能在纳入全部假启动后形成双窗正净期望。只否定这个具体定义，不否定所有1h动能信号，也不把事后保持组直接变成可执行过滤器。

### 下一步
停止给RT1追加阈值或参数。若继续研究，单一问题应转为：在信号当时可见的信息中，什么机制能区分“会保持到4h确认”与“不会保持”的候选；需另立预注册特征诊断，不得用本轮事后标签直接挑规则。协议：`reports/2026-10-15/realtime_momentum_start_protocol_v1.md`；报告：`reports/2026-10-15/realtime_momentum_start_v1/report.md`。

## 2026-10-15 15:41 +08:00 - 动能启动时间颗粒度阶段A

### 背景
当前研究与日常采集均以4h为锚，用户担心4h确认会错过盘中启动。`CRYPTOTRADIN-129`因此改为两阶段：先量化4h确认延迟的偏有利上界，只有严格通过后才允许另冻独立1h候选；15分钟不进入本轮。

### 假设
若4h确认是当前B入场亏损的重要且可利用原因，那么在最终会通过4h确认的事件中，按已完成1h K线提前同一price-only reclaim的oracle-confirmed上界，应在两个窗口和stress成本下均绝对为正，相对原4h的14日配对区间下界不小于0，且同根顺序不翻号。

### 实验
- 实验：`momentum_resolution_stage_a_v1 / CRYPTOTRADIN-129`。
- 变更：无可执行策略变更；条件于最终4h确认，若确认K线前3根1h中已出现冻结计划的price-only reclaim，则假设下一根1h开盘成交；其余固定`+5%/-3%/48h`。
- 样本：Binance Spot USDT current-survivor冻结B all-events；早窗858笔、近窗628笔；主口径taker/stop-first，stress与target-first敏感性。

### 白话结论
4h确认确实经常晚了约两小时，普通成本下更早价格足以把这个“知道未来会确认”的理想样本变成盈利。但这已经是对1h最有利的上界，压力成本下仍略亏，而且真实1h扫描还会多出假突破。因此不能直接进入1h策略开发；真正问题不只是时间颗粒度，还包括信号选择和成本余量。

### 结果
- trades/closed_trades：早窗858/858、近窗628/628，原4h与上界全部配对闭合；3个分支逐笔共4,458行。
- 更早reclaim：早窗`691/858=80.54%`，近窗`506/628=80.57%`；平均提前`2.20/2.17h`。
- 提前成交价优势：均值`0.7793%/0.5423%`，中位`0.3749%/0.3540%`；更早价格更低比例`71.06%/76.48%`。
- 胜率（原4h→1h上界）：早窗`38.81%→46.62%`，近窗`40.76%→46.82%`。
- Profit factor：早窗`0.898→1.252`，近窗`0.898→1.227`。
- Sharpe/CAGR/账户MDD：N/A；all-events条件上界不是可执行账户。
- 净收益：taker早窗`-0.1864%→+0.3973%`，近窗`-0.1645%→+0.3210%`。
- 14日配对Δnet%区间：早窗`[+0.3494,+0.7793]`，近窗`[+0.3418,+0.6428]`；逐symbol/逐周剔除最小差值仍为正。
- stress净收益：早窗`-0.5583%→-0.0024%`，近窗`-0.5645%→-0.0599%`，绝对正收益门槛失败。
- 同根顺序：无翻号；6个原4h分支逐笔status、exit和数值误差为0；1h/4h确认聚合1486/1486通过。
- 核验：44项相关测试通过；manifest哈希闭合。

### 结论
`retest / stop_lower_timeframe_timing_route`：4h确认延迟真实且有经济影响，但即使使用未来确认筛选后的有利上界，stress下仍未形成双窗正收益；不授权独立1h阶段B，不外推否定所有1h信号。

### 下一步
停止纯时间颗粒度提前路线，不研究15分钟、不改采集与生产。若继续，由用户在4h因果特征诊断（原129广义问题）、`CRYPTOTRADIN-127` reclaim强度或`CRYPTOTRADIN-130`毛收益/成本覆盖中另行选择。协议：`reports/2026-10-15/momentum_resolution_stage_a_protocol_v1.md`；报告：`reports/2026-10-15/momentum_resolution_stage_a_v1/report.md`。

## 2026-10-15 08:46 +08:00 - ATR出口四政策2×2失败机制归因

### 背景
`CRYPTOTRADIN-133`的full ATR出口把固定出口亏损显著拉近盈亏平衡，但同时改变TP和SL，无法知道改善来自哪一组件。系统目标仍是判断B all-events入场能否在48小时内形成覆盖实际成本的稳健正期望；本轮只做组件归因，不搜索新参数。

### 假设
若动态TP或动态SL存在独立可验证优势，至少一个单组件政策应在早/近两窗、taker/stress和两种同根顺序下全部绝对转正，相对fixed的common-R不变差，且主分支14日配对区间下界不小于0。否则否定当前组件定义；测量或顺序翻号则停止解释。

### 实验
- 实验：`atr_exit_component_attribution_v1 / CRYPTOTRADIN-134`。
- 变更：交叉组合`fixed TP / ATR20×5/3 TP`与`fixed 3% SL / ATR20×1 SL`，形成四政策；入场、48小时、事件集、成本和顺序保持不变。
- 样本：Binance Spot USDT current-survivor冻结B all-events；UTC `[2024-07-01,2025-06-01)` 858笔、`[2025-06-01,2026-06-01)` 628笔；48配置，主口径next-open、taker、stop-first。

### 白话结论
ATR止盈和ATR止损单独拿出来都能让亏损数字好看一点，但没有一个能在两个时期都真正赚到钱。早窗两者一起用有协同，近窗却主要靠ATR止盈，ATR止损帮助很小且组合交互反向；所以full ATR接近盈亏平衡不是一个稳定、可复用的单一机制。

### 结果
- trades/closed_trades：四政策早窗各858、近窗各628，全部闭合；全分支逐笔共35,664行。
- 胜率（fixed / ATR TP / ATR SL / full ATR）：早窗`38.81% / 38.34% / 40.68% / 40.21%`；近窗`40.76% / 50.32% / 33.92% / 43.15%`。
- Profit factor：早窗`0.898 / 0.908 / 0.944 / 0.993`；近窗`0.898 / 0.998 / 0.920 / 0.988`。
- Sharpe/CAGR：N/A；all-events common-R曲线不是可执行账户。
- 最大回撤（诊断common-R曲线）：早窗`61.21% / 64.89% / 65.52% / 68.77%`；近窗`59.71% / 47.32% / 55.87% / 41.23%`。
- 平均净收益：早窗`-0.1864% / -0.1718% / -0.1059% / -0.0134%`；近窗`-0.1645% / -0.0034% / -0.1170% / -0.0164%`。
- 平均common-R：早窗`-0.0567 / -0.0522 / -0.0322 / -0.0041`；近窗`-0.0500 / -0.0010 / -0.0355 / -0.0050`。
- 2×2边际（net%）：早窗TP`+0.0535`、SL`+0.1195`、交互`+0.0778`；近窗TP`+0.1308`、SL`+0.0172`、交互`-0.0606`。
- 单组件相对fixed的主分支14日common-R差值95%区间：ATR TP早/近`[-0.0691,+0.0616] / [-0.0187,+0.1243]`；ATR SL`[-0.0753,+0.0964] / [-0.0214,+0.0511]`。
- stress平均净收益：ATR TP早/近`-0.5252%/-0.3819%`；ATR SL`-0.4862%/-0.5302%`，绝对正收益闸门明确失败。
- 核验：12/12测量分支通过，fixed逐笔复现12/12，同根顺序无翻号；45项相关测试通过。

### 结论
`revert / reject_current_atr_components`：两个单组件虽相对fixed改善，但都未跨双窗及stress形成正期望，区块区间也未排除负向；早/近窗2×2机制不同。停止当前`ATR20 + 1ATR SL + 5/3ATR TP`组件路线，不外推否定所有ATR退出或B入场。

### 下一步
不扫描ATR周期、倍数、clamp、trailing或持仓时间，不修改生产。研究路线回到`CRYPTOTRADIN-129`动能延续识别与`CRYPTOTRADIN-130`入场毛收益/成本余量，是否启动由用户另行授权。协议：`reports/2026-10-15/atr_exit_component_attribution_protocol_v1.md`；报告：`reports/2026-10-15/atr_exit_component_attribution_v1/report.md`。

## 2026-10-14 23:55 +08:00 - ATR自适应5:3短周期出口验证

### 背景
用户澄清原始问题是根据币种信号时点波动动态设置止盈止损，而非用NATR过滤仍固定为5%/3%的交易。系统目标仍是判断B入场能否在短周期覆盖成本；本轮只验证出口尺度适配，不改变入场或市场过滤。

### 假设
若固定百分比出口因不同币种波动尺度而错配，则用信号时点已知ATR统一为`SL=1 ATR、TP=5/3 ATR`，应在两个窗口改善等风险净R与R-PF、使其转正，并在14日配对区块、成本、同根顺序、尾部和集中度检查下保持。

### 实验
- 实验：`atr_adaptive_short_exit_v1 / CRYPTOTRADIN-133`。
- 变更：固定`+5%/-3%/48h` → 唯一预注册`TP=5/3×ATR20 / SL=1×ATR20 / 48h`；ATR只取信号时点前20根已完成4h K线，不运行倍数网格。
- 样本：Binance Spot USDT current-survivor，冻结B all-events；UTC `[2024-07-01,2025-06-01)` 858笔、`[2025-06-01,2026-06-01)` 628笔；next-open、taker、stop-first主口径。

### 白话结论
按ATR调距离确实解决了一部分“低波动币等不到5%、高波动币3%止损太近”的问题：超时大幅减少，亏损点估计接近收支平衡。但它没有创造稳定正收益，且在部分市场状态、压力成本和早窗回撤上变差。因此思路中的尺度问题真实存在，但这条最简单的1ATR止损、5/3ATR止盈公式还不能用。

### 结果
- trades：早窗`858 -> 858`、近窗`628 -> 628`，事件完全配对；closed_trades均相同且无删失。
- 胜率：早窗`38.81% -> 40.21%`（`+1.40pp`）；近窗`40.76% -> 43.15%`（`+2.39pp`）。
- Profit factor（相同名义）：早窗`0.898 -> 0.993`；近窗`0.898 -> 0.988`。
- 等风险平均净R：早窗`-0.0567 -> -0.0317`；近窗`-0.0500 -> -0.000008`。
- 等风险R-PF：早窗`0.898 -> 0.943`；近窗`0.898 -> 0.999986`。
- Sharpe/CAGR：N/A；all-events风险曲线忽略重叠容量，不是可执行账户。
- 最大回撤（诊断等风险曲线）：早窗`61.21% -> 65.46%`，恶化`4.24pp`；近窗`59.71% -> 47.99%`，改善`11.72pp`。
- 净收益：逐笔平均净收益早窗`-0.1864% -> -0.0134%`，近窗`-0.1645% -> -0.0164%`；诊断风险曲线总收益早窗`-41.70% -> -27.98%`、近窗`-29.34% -> -4.00%`。
- TIME：早窗`15.62% -> 10.96%`；近窗`30.10% -> 3.34%`。
- 14日配对ΔR 95%区间：早窗`[-0.1077,+0.1108]`，近窗`[-0.0551,+0.1542]`，均跨零。
- stress成本ΔR：早窗`+0.0196`，近窗`-0.0115`；同根两端双触发为0，`target_first`不改变结果。
- regime：NEUTRAL ΔR早/近`-0.1315/-0.0271`，RISK_ON `+0.1148/+0.0687`；但近窗RISK_ON ATR自身仍为`-0.00485R`。
- NATR桶：早窗high改善、low恶化；近窗low改善、high恶化（high仅22笔），没有跨窗稳定普适关系。
- 核验：12个固定出口成本/顺序分支逐笔状态、退出时间和数值均与cashfix匹配；2,972行主分支CSV和输出SHA256闭合；38项相关测试通过。全套为`247 passed, 5 failed`，5项均为既有database/scheduler/audit或用户未提交脚本契约失败，本轮未触及对应实现。

### 结论
`revert / reject_preregistered_atr_exit`：唯一预注册ATR版本改善点估计和TIME，但两窗仍未形成正净R/R-PF，区块区间跨零，早窗回撤恶化且近窗压力成本翻转。否定这个具体公式，不否定所有ATR出口；波动尺度错配作为机制观察保留。

### 下一步
不搜索其它ATR倍数，不增加clamp、trailing或regime规则，不修改生产。RISK_ON/NEUTRAL交互只作为已登记`CRYPTOTRADIN-131`的背景证据；是否启动该市场状态问题由用户另行授权。协议：`reports/2026-10-14/atr_adaptive_short_exit_protocol_v1.md`；报告：`reports/2026-10-14/atr_adaptive_short_exit_v1/report.md`。

## 2026-10-14 16:52 +08:00 - 固定5%/3%短周期出口的波动适配诊断

### 背景
固定百分比止盈止损在不同波动率币种上代表不同的 ATR 距离。系统级目标是判断 B 入场本身是否存在能覆盖成本的短周期优势；本轮位于退出适配诊断层，只检验信号时点波动能否识别更适合固定 `+5%/-3%/48h` 的交易，不改出口。

### 假设
如果固定出口只在某段波动率内有效，则早窗预注册的连续 NATR20 分组应使胜率提高至少 5 个百分点，同时净期望、PF、P05不恶化；固定数值切点和选择器原样应用近窗后仍应保持这些方向。任一窗口不成立、胜率改善以期望恶化换取，或没有早窗候选过闸，均不支持加入过滤器。

### 实验
- 实验：`fixed_exit_volatility_fit_v1 / CRYPTOTRADIN-132`。
- 变更：无策略参数变更；只读计算确认K线时点 `NATR20 = ATR20 / confirmation_close`，用早窗三分位固定 `2.622% / 3.926%` 两个切点，评估 `low / mid / high / low+mid / mid+high` 五个预注册选择器。
- 样本：冻结 B all-events，Binance Spot USDT current-survivor；UTC `[2024-07-01,2025-06-01)` 858笔、`[2025-06-01,2026-06-01)` 628笔；next-open、taker、stop-first、`+5%/-3%/48h`。

### 白话结论
低波动交易在早窗口看起来更好，但好得不够，而且换到近窗口后优势消失。也就是说，固定5%止盈、3%止损确实会因币种波动不同而表现不同，但仅靠入场时的NATR高低，不能稳定挑出胜率更高且仍有净利润的交易。

### 结果
- trades：早窗 baseline `858` → 最接近候选low `286`（保留33.33%）；近窗 `628` → `460`（保留73.25%）。
- closed_trades：早窗 `858 -> 286`；近窗 `628 -> 460`，均无删失。
- 胜率：早窗 `38.81% -> 43.71%`（`+4.90pp`，未达到`+5pp`）；近窗 `40.76% -> 41.52%`（`+0.76pp`）。
- Profit factor：早窗 `0.898 -> 1.029`；近窗 `0.898 -> 0.883`。
- Sharpe：N/A；主样本为 all-events 诊断集合，不是可执行账户组合。
- 最大回撤：账户MDD N/A；诊断交易序列MDD早窗 `26.77% -> 9.78%`，近窗 `24.87% -> 18.35%`，不可解释为组合风险认证。
- 净收益：以逐笔平均净收益报告，早窗 `-0.1864% -> +0.0405%`；近窗 `-0.1645% -> -0.1745%`。
- 其余早窗候选：mid/high/low+mid/mid+high 胜率变化分别 `-3.15/-1.75/+0.87/-2.45pp`，均未过闸；同根双触发为0。
- 核验：1,486条主分支逐笔记录与858/628源样本闭合，输出SHA256全通过；32项相关测试通过。全套项目测试为`241 passed, 5 failed`，5项是既有database/scheduler/audit或用户未提交脚本契约问题，本轮文件未触及对应实现。

### 结论
`revert / reject_no_early_qualifier`：五个预注册选择器均未通过早窗资格；最接近的low组即使放宽0.105pp也无法在近窗复现，且近窗净期望、PF变差。不授予 NATR 固定过滤实验或 ATR 自适应出口实验资格。

### 下一步
保持 `+5%/-3%/48h`、生产配置、paper和shadow不变。若继续研究，应回到已登记的三个上游问题——可实时识别的动能启动、能够覆盖成本的入场毛收益、以及市场状态对延续性的影响——由用户另行选择和授权，不围绕本次切点做参数搜索。协议：`reports/2026-10-14/fixed_exit_volatility_fit_protocol_v1.md`；报告：`reports/2026-10-14/fixed_exit_volatility_fit_v1/report.md`。

## 2026-10-14 00:32 +08:00 - Baseline 退出后 1R 恢复率诊断

### 背景
Baseline MAE/MFE 二级归因无法把近窗多数亏损归为入场快速恶化或盈利后回吐；23笔非容量亏损中有17笔为`other_or_inconclusive`。系统目标是判断老 baseline 应优先研究退出匹配，还是停止在该线上继续调参。

### 假设
若止损普遍切断了仍存在的方向优势，非容量`STOPPED`交易应在两个窗口都高频于退出后40根4h K线内重新达到原入场方向`+1R`；若恢复率跨窗口稳定偏低，则更支持缺少后续动能。窗口冲突、30%–40%灰区、市场beta或集中度驱动均判证据不足。

### 实验
- 实验：`baseline_post_exit_recovery_v1 / CRYPTOTRADIN-128`。
- 变更：无策略variant；只读重建`exit_bar+1`后的K20/K40/K80路径，使用原始入场风险R，同币再次入场与窗口结束按右删失处理。
- 样本：Binance Spot USDT current-survivor；UTC `[2024-07-01,2025-06-01)` 与 `[2025-06-01,2026-06-01)`；主样本为87笔非容量`STOPPED`，近窗17笔unknown单列，23笔容量竞逐`STOPPED`单列。

### 白话结论
早窗口有一部分交易止损后会恢复，但比例落在预先规定的灰区；近窗口恢复明显较少。尤其17笔最难解释的近窗亏损，40根4h K线内一笔都没有回到`+1R`，80根内也只有一笔。因此没有证据支持把近窗亏损主要归因于止损过早，但两个窗口不一致，仍不能把老 baseline 的全部亏损统一命名为“没有后续动能”。

### 结果
- trades：87 -> 87（只读路径诊断，无入场增删）；另单列23笔容量竞逐止损。
- closed_trades：87 -> 87；K40完整观察早52/55、近29/32，删失不记作失败。
- 胜率：N/A（无策略variant）。
- Profit factor：N/A（无策略variant）。
- Sharpe：N/A（无策略variant）。
- 最大回撤：N/A（无策略variant）。
- 净收益：N/A（无策略variant，原交易P&L不变）。
- K40恢复率：早`20/52=38.46%`，Wilson 95%区间`[26.47%,52.04%]`；近`6/29=20.69%`，区间`[9.85%,38.39%]`。
- 近窗unknown：K20`0/17`、K40`0/16`、K80`1/16=6.25%`。
- 市场锚：早窗非顺风/顺风K40恢复`32.00%/44.44%`，近窗`15.00%/33.33%`，整体反弹会抬高恢复率。
- 集中度：逐symbol剔除后早窗K40为`36.00%–40.00%`、近窗`17.86%–22.22%`；逐周剔除为`31.91%–42.55%`、`8.33%–25.00%`。
- 核验：新增5项合成测试通过；全套测试`236 passed, 5 failed`，5项失败均位于既有database/scheduler/audit测试或用户未提交脚本契约，与本诊断无关；110行逐笔结果及11,991条查询K线摘要双跑哈希一致，窗口边界违规0。

### 结论
`retest / insufficient_or_window_inconsistent`：早窗K40处于灰区、近窗低恢复，无法形成跨窗口统一机制；不授予退出实验资格。近窗unknown的低恢复是条件性证据，反对“这些亏损主要因为止损过早”。

### 下一步
停止在老 baseline 上自动调退出；保持生产配置冻结。`CRYPTOTRADIN-127`继续留在todo，是否启动由用户另行决定。若要把本结论外推，必须用point-in-time历史币池或自然前向样本复核。协议：`reports/2026-10-14/baseline_post_exit_recovery_protocol_v1.md`；报告：`reports/2026-10-14/baseline_post_exit_recovery_v1/report.md`。

## 2026-10-14 00:03 +08:00 - D6 vs C20 更早局部突破诊断

### 背景
20根4h突破可能在约80小时新高才成交，存在入场偏晚的合理怀疑。系统目标仍是找到共同短出口下扣成本为正的入场；本次位于更早动能研究的最小单变量步骤，先测24小时局部新高，不直接捆绑收缩、放量或防追高。

### 假设
若“更早局部突破”能够稳定改善选交易质量，D6应在两个开发窗口都实现正净期望、PF>1且优于C20，14日区块差值下界大于0，路径质量、成本压力、同币占用和集中度均不翻转。否则按预设进入否定或证据不足。

### 实验
- 实验：`breakout_d6_v1 / CRYPTOTRADIN-126`。
- 变更：`C20`首次突破过去20根4h high → `D6`首次突破过去6根；两臂同构排重、无额外冷却。next-open、`+5%/-3%/48h`、费用、滑点、stop-first和三层回放不变。
- 样本：Binance USDT current-survivor，UTC `[2024-07-01,2025-06-01)` / `[2025-06-01,2026-06-01)`；主口径all_events分别C20 650/457笔、D6 965/671笔。两个窗口均为已烧开发样本。

### 白话结论
把门槛从约80小时新高降低到约24小时新高，确实多找出近一半信号，但没有让策略赚钱。早窗口反而更差，近窗口只是“少亏一点”，且统计区间仍允许没有改善；因此不能继续往D6上叠加收缩条件，也不能据此断言所有更早动能信号无效。

### 结果
- trades / closed_trades：早窗`650 -> 965`（+48.46%），近窗`457 -> 671`（+46.83%）；主路径全部完整覆盖。
- 胜率：早窗`37.38% -> 36.58%`（-0.80pp），近窗`34.14% -> 37.56%`（+3.42pp）。
- Profit factor：早窗`0.847 -> 0.805`，近窗`0.630 -> 0.716`。
- 平均每笔净收益：早窗`-0.2982% -> -0.3802%`，近窗`-0.6995% -> -0.5064%`；D6-C20的14日区块95%区间为`[-0.289,+0.131]`、`[-0.096,+0.436]`百分点。
- 路径质量：favorable-first早窗`32.62% -> 30.57%`、近窗`20.35% -> 21.91%`；48h MFE中位数`5.346% -> 4.550%`、`2.660% -> 2.620%`，没有双窗共同改善。
- Sharpe（账户）：早窗`-1.760 -> -3.427`，近窗`-2.391 -> -1.905`。
- 最大回撤（账户4h收盘）：早窗`35.80% -> 56.81%`，近窗`32.94% -> 33.49%`。
- 净收益（账户）：早窗`-34.18% -> -56.80%`，近窗`-32.18% -> -31.91%`。
- 核验：62项相关回归通过；C20跨全部成本/顺序/层次15,389条导出记录与既有cash-fix逐笔逐金额一致；源码和协议运行前后SHA256一致。

### 结论
`retest / insufficient`：D6自身双窗净亏，早窗恶化、近窗改善但区间跨零，路径质量也不一致；不满足开发资格，同时不满足“双窗均不优于C20”的完整否定条件。

### 下一步
`no_automatic_next_experiment`。不叠加squeeze、不改退出、不修改生产配置；等待用户验收和方向选择。若未来继续，需真正未使用数据或另立可解释的单变量问题。报告：`reports/2026-10-13/breakout_d6_v1/report.md`。

## 2026-10-13 23:15 +08:00 - 20根4h突破入场时机诊断

### 背景
用户质疑20根4h新高可能要求过高：部分行情也许在到达80小时新高前已经完成5%上涨，等突破后再买并要求第二个5%会过晚。系统目标仍是找到扣成本后正期望的短周期入场；本次位于失败候选的机制诊断层，不是参数搜索。

### 假设
若入场过晚是跨窗口主因，两个窗口多数突破都应满足“此前20根低点到突破收盘已涨至少5%，但实际下一根开盘成交后48小时最高价仍不足成交价+5%”，且14日区块95%下界和逐币剔除均高于50%。双窗不一致则证据不足。

### 实验
- 实验：`breakout_lateness_diagnostic_v1`。
- 变更：无策略variant；只读重建冻结C臂1,107个全事件的突破前12/24/48h涨幅、20根区间涨幅和成交后48h MFE。
- 样本：Binance USDT current-survivor，UTC `[2024-07-01,2025-06-01)` 650笔、`[2025-06-01,2026-06-01)` 457笔；完全复用原taker/stop-first/all_events成交事件与npz。

### 白话结论
“突破前已经涨过5%”很常见，但“买入后再无5%空间”只在近窗占多数。早窗有一半以上事件后续仍有5%空间，其中不少是先止损、后来再涨；所以不能把整体失败都解释为20根突破太晚，也不能据此直接把20改成10或5。

### 结果
- trades：原C 650/457 → 诊断覆盖650/457（0变化）；closed_trades同样全部覆盖。
- 突破前20根低点至突破收盘涨幅中位数：早18.15%，近9.94%；已达到5%的事件为96.46% / 82.06%。
- 成交后48h仍有5%空间：早51.23%，近26.48%。`late_exhausted`：早45.69%，近57.99%；14日区块95%区间分别为[37.879%,58.778%]与[49.998%,66.668%]。
- 实际SL后后来仍达目标：早18.62%，近6.13%；逐一剔除任一币后的`late_exhausted`为早44.28%–46.31%、近57.07%–61.24%。
- 胜率、Profit factor、Sharpe、最大回撤、净收益：N/A（无策略variant、未重放收益；原C绩效不变）。

### 结论
`retest / insufficient_or_window_inconsistent`：近窗符合入场偏晚的方向，早窗不符合，多数/区间门槛未双窗通过；不能把该机制升级为总解释。

### 下一步
不搜索10/5根参数，不改生产配置。若另立更早动能候选，先定义可因果执行的启动信号与未使用验证数据；不能把事后20根低点当入场点。报告：`reports/2026-10-13/breakout_lateness_diagnostic_v1/report.md`。

## 2026-10-13 00:32 +08:00 - 同一短周期退出：reference入场 vs 20根新突破

### 背景
承接10-12交接，回答用户指定的入场比较问题。目标是无杠杆现货在两天内退出且扣成本正盈利；属于公开资料筛选后的条件历史诊断，不是旧ATR优化或部署。

### 假设
统一资格、next-open、+5%/-3%、48h、成本和账户约束后，突破在两个窗口都提高净期望且自身为正；双窗95%下界、压力、同币去重、集中度与执行检查同时支持才可进入独立验证。区间跨零或窗口不稳则不足。

### 实验
- 实验：`short_horizon_entry_v1`；最终产物为`short_horizon_entry_v1_cashfix`，同协议下现金数值边界纠错，不是新参数候选。
- 变更：仅研究入场模块B→C；B复用完整评分/回踩reclaim，C为4h收盘突破此前20根high且前根未突破。实际成交价+5%/-3%，48h全平。
- 样本：Binance USDT current-survivor逐日币池，早窗285币、近窗294币；UTC `[2024-07-01,2025-06-01)` / `[2025-06-01,2026-06-01)`；240日预热、1h执行路径，两窗口已被研究。
- 分支：taker/stress/legacy_fee × stop-first/target-first；all_events/symbol_only/portfolio三层。主口径taker/stop-first。

### 白话结论
这版突破更快结束，但没有更能净赚钱。全事件层双窗都弱于原入场，近窗C自身与C−B区间均低于零。原入场在同一新出口下也亏损；早窗账户少亏不能当作突破优势。封存负结果，不升级或继续调参。

### 结果
- trades（全事件B→C）：早858→650（−24.24%）；近628→457（−27.23%）。
- closed_trades：同上；全部分支无交易期缺口/期末删失；主C早4/近2个1h双触已给两种边界。
- 胜率：早38.81%→37.38%（−1.43百分点）；近40.76%→34.14%（−6.63百分点）。
- 平均每笔净收益：早−0.1864%→−0.2982%；近−0.1645%→−0.6995%。C−B的14日区块95%区间：早[−0.6541,+0.4964]、近[−1.0068,−0.0435]百分点。
- Profit factor（等现金全事件）：早0.898→0.847；近0.898→0.630。
- Sharpe（账户）：早−1.715→−1.760；近−0.642→−2.391。
- 最大回撤（账户4h收盘）：早36.47%→35.80%；近22.55%→32.94%。
- 净收益（账户）：早−35.90%→−34.18%；近−12.35%→−32.18%。账户为近似执行诊断，主分支4笔非零<10 USDT订单尚未核验历史最小订单。
- 工程核验：51测试、100真实时点scanner一致性通过；32,713条跨分支导出记录独立对账最大误差约1e-11 USDT；现金精度修正前后24份非组合逐笔文件完全一致。

### 结论
`retest / evidence_insufficient_for_positive_edge`：C双窗观测净期望均负、近窗有反证、早窗精度不足，不满足支持标准；不升级冻结候选，不能外推为所有突破无效。

### 下一步
本次研究收口，保留负结果；不自动开启参数搜索或前向交易。新研究需另立单一问题及未使用数据，生产配置不变。详细解释、全部分支与逐笔入口：`reports/2026-10-13/short_horizon_entry_v1_cashfix/report.md`。

## 2026-10-10 22:33 +08:00 - Baseline 交易路径二级归因：MAE/MFE

### 背景
Gate 3-C 已确认排除容量竞逐后 gross edge 早窗接近零、近窗为负，但逐笔 MAE/MFE 尚未可用，无法区分入场质量和退出保护。当前只推进 current-survivor 条件诊断，不把结果推广到完整历史市场。

### 假设
如果主要是入场问题，两个窗口的非容量亏损都应表现为快速 MAE、低早期 MFE；如果主要是退出问题，两个窗口都应出现足够 MFE 后明显回吐到亏损。若窗口方向不一致、标签只占少数或容量/尾部驱动，则证据不足，不形成实验卡片。

### 实验
- 实验：`baseline_trade_path_attribution_2026_10_10`。
- 变更：无策略变更；新增只读诊断脚本 `scripts/attribute_baseline_trade_path.py`，以冻结 `confirmation_close` replay 结果和 Binance 4h `kline_cache` 重建 bar-extrema MAE/MFE。
- 样本：Binance Spot USDT、current-survivor master、2024-07-01 至 2025-06-01 与 2025-06-01 至 2026-06-01；131 笔完整闭合，非容量竞逐 101 笔，容量竞逐 30 笔单列。

### 结果
- 非容量闭合：早窗 63 笔，近窗 38 笔；容量竞逐组 17 / 13 笔。
- 入场样标签：早窗 13 笔（12 纯标签 + 1 重叠），近窗 2 笔；对应亏损比例 35.14% 与 8.70%。
- 退出样标签：早窗 6 笔（5 纯标签 + 1 重叠），近窗 4 笔；对应亏损比例 16.22% 与 17.39%。
- regime：非容量 net P&L 早窗 NEUTRAL -292.23、RISK_ON +157.60；近窗 NEUTRAL +256.72、RISK_ON -69.61、RISK_OFF -436.03（4 笔）。
- 退出类型：非容量 STOPPED 早窗 55 笔 / -2256.28 USDT、近窗 32 笔 / -1560.93 USDT；CLOSED 早窗 8 笔 / +2121.66、近窗 6 笔 / +1312.02。
- 持仓时长：`<=3d` 两窗均为负；但入场样标签从早窗 11 笔降到近窗 2 笔，退出样标签在 `>7d` 由早窗 5 笔、近窗 4 笔构成，不能把它直接解释成应放宽止损或延长持仓。

### 结论
C / `C_evidence_insufficient_no_stable_dominant_mechanism`：入场样结构早窗较强、近窗明显减弱；退出样结构两个窗口都出现但不是亏损多数，现有条件样本不能把主要亏损稳定归于入场或退出。生产配置保持不变。

### 下一步
不建立 ATR、stop、TP1 或持仓时长单变量实验卡片。保留逐笔 CSV/JSON 作为当前存续币诊断证据；若要形成机制实验，先用 point-in-time 历史币池或自然前向样本复核同一标签是否跨窗口复现。

## 2026-10-09 23:03 +08:00 - ATR 0.35 修复后固定历史复核

### 背景
用户希望加速验证；完成 replay stop/EMA 修复后，按预声明协议重算两个旧窗口，隔离入场时序。系统目标是可信的成本后优势；唯一问题是避免亏损能否抵消错失盈利，属于执行正确性修复后的固定历史诊断。

### 假设
ATR 0.35 在两窗口、两种成交口径下均改善净收益/PF且回撤不恶化，并不依赖最大三项贡献，才支持继续研究。跨口径翻转为不足；确认收盘口径两窗口收益/PF均变差，则否定本批窗口内的稳定改善假设。

### 白话结论
ATR能挡掉部分亏损，也会错过赢家；本批不能认定它减少组合整体亏损或回撤。旧成交假设下两窗口收益提高，改用理想确认收盘价后两窗口收益均下降，近窗回撤还扩大。生产配置冻结，未来优化留在 CRYPTOTRADIN-51 TODO，不立即执行。

### 实验
- 实验：atr_fixed_history_v1 / CRYPTOTRADIN-120。
- 变更：baseline reclaim vs 固定 ATR 0.35；两种时序 legacy_same_bar / confirmation_close，共8个分支。
- 样本：Binance现货旧run逐日币池（早窗285币、近窗294币，含BTC/ETH基准），2024-07-01至2025-06-01、2025-06-01至2026-06-01，UTC半开区间，4h。
- 固定：初始10000 USDT、风险1%/总5%、最多5仓、watch18根、原退出逻辑；入场/TP2费用4bps、stop10bps，滑点5/10bps。只读缓存，保留存续币偏差。
- confirmation_close 为零延迟理想收盘价+滑点，沿用maker费用仅用于隔离时序；不是实盘可成交证明。旧窗口不是新样本外。

### 结果
下表为 confirmation_close，baseline → ATR0.35；全部8分支和CAGR/Sortino/exposure/turnover/费用/尾损见报告。

| 指标 | 2024-07至2025-06 | 2025-06至2026-06 |
|---|---:|---:|
| trades（计划数） | 489 → 494（+1.02%） | 386 → 381（-1.30%） |
| closed_trades | 80 → 75（-6.25%） | 51 → 46（-9.80%） |
| 胜率 | 45.00% → 46.67%（+1.67pp） | 41.18% → 39.13%（-2.05pp） |
| Profit factor | 1.12 → 1.04 | 0.95 → 0.65 |
| Sharpe | 0.37 → 0.18 | -0.03 → -0.77 |
| 最大回撤 | 17.23% → 14.81% | 17.71% → 20.21% |
| 净收益 | 4.72% → 1.50%（-3.22pp） | -1.51% → -10.20%（-8.69pp） |

旧口径净收益分别为 -2.00%→36.65%、4.55%→9.40%。确认收盘的baseline-only配对账目中，避免亏损/错失盈利分别为2626.61/3725.63和1299.47/2034.31 USDT；组合总权益差为-321.84、-868.94 USDT。账目包含组合路径变化，capacity因果贡献仍为n/a。8分支均无已入场4h跨缺口交易；现金/费用/期末权益对账通过。已知UNKNOWN缺陷在两窗口无触发，不在本任务中修复。

### 结论
retest / reject_stable_improvement_in_frozen_windows：两窗口在确认收盘口径下收益与PF均变差，旧收益优势不具执行口径稳健性；不能外推为所有未来行情无效。候选极少bug的数据分级修复keep结论不变。

### 下一步
优先定稿可执行的信号/成交/止损时序契约，处理UNKNOWN回退并验收自然daily/4h的连续覆盖；ATR优化保留TODO，待后续安排。报告：`reports/2026-10-09/atr_fixed_history/report.md`；协议、输入hash、完整事件与validation同目录/上级目录。

更新时间：2026-10-09 +08:00

## 2026-10-09 12:37 +08:00 - 整体技术路线复盘（汇总既有证据，非新策略实验）

### 背景
对技术路线、全部主要试验家族和当前前向证据做总体复盘，重新安排两周优先级。

### 假设
reclaim和退出管理可能有价值，但既有收益改善可能受执行时序、币池选择、资金路径和采集缺口影响，尚未证明稳定成本后优势。

### 实验
- 实验：项目整体证据复盘；没有新跑回测、A/B或paper update。
- 变更：只调整研究证据等级和工程计划；纯内存复现stop抬升后旧fill计价与UNKNOWN放行，不改生产实现/配置/业务库。
- 样本：既有2023–2026历史报告及2026-06至10月paper；具体symbol/window保持各源报告定义，不混成一组样本。

### 结果
非技术解释：基础架构值得保留，但三条执行路径并不等价，部分账面赢家又受停机影响；先修正确性与对照生命周期，比继续搜索参数更有价值。
- trades / closed_trades / 胜率 / Profit factor / Sharpe / 最大回撤 / 净收益：本次baseline -> variant均n/a；未运行可合并的新策略实验。
- 既有ATR双窗净收益-2.09%→18.20%、3.11%→9.33%仍为历史记录，增加成交时序与EMA stop实现待复核限制。
- 既有8笔缺口审计条件性毛损益+1580.44→+791.53 USDT；不是完整资金路径净收益。
- 既有273配对时点、12入场差异验证完成，但这12机会中合格完整同执行口径配对终态为0。
- 最新12:11运行报告16 terminal=7 ARCHIVED+9入场后退出；4h恢复四次，daily仍未出现新成功。
- 技术复现：旧stop101、EMA112、bar low110，回测调用方式仍退出100.899；UNKNOWN/False仍能生成BUY_CANDIDATE。历史影响未量化。

### 结论
keep研究基础与数据分级修复；retest策略优势；暂停新参数与新规则。原因：执行正确性、对照可比性与连续性尚未过关，数量门槛不能替代收益证据。

### 下一步
10/09–10/22优先收口存量审计、修复stop/UNKNOWN/时序、独立shadow最小生命周期与新epoch，最后按正确性/连续性/可回答性分层裁决。完整报告：[总体复盘](reports/2026-10-09/project_retrospective_and_two_week_plan_2026-10-09_v1.md)。

## 2026-10-09 00:24 +08:00 - 原规则与 ATR 0.35 的可信证据复核

### 背景
用户要求在跨停机交易审计后用可信样本比较原规则与 ATR 0.35；不能把原有受污染盈利或候选虚拟结果混作完整策略证据。

### 假设
0.35 可能过滤较差 reclaim，也可能延迟/错过盈利入场。本次核对实际同时点差异，不运行新的近端 A/B、不调阈值。

### 实验
- 实验：`atr_0_35_trusted_evidence_review_2026_10_09`，只读归因。
- 变更：无生产变更；固定已有 shadow 时点，重算两条规则并独立验证行情。
- 样本：北京时间 2026-08-16–09-24；819 rows / 273 配对时点 / 29 plans；12 个实际入场 / 11 币，全部 DEGRADED。8 个已有缺口审计结果，其余 4 个截至窗口末未退出。

### 结果
非技术结论：0.35 确实挡住了原规则的全部 12 个当时入场，但其中既有差交易也有盈利机会，尚不能证明更精准。
- trades：n/a -> n/a（没有独立完整策略交易路径）；实际时点 accept=12 -> 0。
- closed_trades：n/a -> n/a；本批可信同执行口径配对终态数=0。
- 胜率：n/a -> n/a。
- Profit factor：n/a -> n/a。
- Sharpe：n/a -> n/a。
- 最大回撤：n/a -> n/a。
- 净收益：n/a -> n/a；不把拒绝的 3 笔按“避免损失”直接记成收益，也不把 5 笔固定入场盈利直接记成全部错过收益。
- 技术证据：273 对三线齐全、无重复、controls_paper=0；12 次 close/ATR 与独立 Binance bar 一致，margin=0.0087138–0.2778030 ATR，median=0.0449301。
- 观测边界：原规则入场后这 12 个 plan 的后续 plan-level shadow rows=0；candidate 虚拟路径虽有后续/更早入场，但 entry/EMA trailing/容量/缺口口径不同，不能替代独立 paper 对照。
- 容量：6 次 available、6 次 at_capacity；direct/path contribution 字段未填，保持 n/a。

### 结论
retest：过滤机制正确但无完整同口径可信配对收益证据，暂不能认定 0.35 优于或劣于原规则，不部署、不调参；候选分级修复仍 keep。

### 下一步
先设计独立 shadow 生命周期、统一执行口径和缺口标识的工程验收，继续原待审持仓审计。报告：`reports/2026-10-09/atr_0_35_trusted_evidence_review_2026-10-09_v1.md`。

## 2026-10-09 00:13 +08:00 - 跨停机区间 8 笔退出交易审计

### 背景
确认已记录盈利是否因停机遗漏止损/止盈而失真；不涉及重新调整候选分级或 ATR 参数。

### 假设
固定已记录入场和仓位，补入原定缺失 4h 时点可能改变终态、金额或时间。原始状态保留；不是策略 A/B。

### 实验
- 实验：`closed_trade_gap_audit_2026_10_09`。
- 变更：仅离线补缺失的 5 次/日 4h 评价时点，生产 step_trade/EMA 逻辑保持不变。
- 样本：2026-08-24–2026-09-24，UNI、ETH 两笔、TAO、BNB、ADA、BTC、DOGE 共 8 笔，固定实际 entry/quantity；Binance Spot 1h/4h 与关键 1m 行情。未重建 daily/import/容量路径。

### 结果
非技术结论：3 笔原盈利应先止损，1 笔退出延迟，停机确实影响了账面成绩；其余 4 笔金额未变不代表完整验证通过。
- trades：8 -> 8（固定 cohort，非新策略交易数）。
- closed_trades：8 -> 8。
- 胜率：n/a -> n/a（选择的是已退出样本，不能推算策略胜率）。
- Profit factor：n/a -> n/a。
- Sharpe：n/a -> n/a。
- 最大回撤：n/a -> n/a。
- 净收益：n/a -> n/a；无手续费滑点或完整资金路径。
- 条件性毛损益：+1580.44 -> +791.53 USDT；仅作为缺失时点影响量化，不能当成完整回测净收益。
- ADA：+256.25 -> -100；BTC：+135.24 -> -100；DOGE：+97.41 -> -100。按原 stop 成交是假设，实际穿越后可能更差。
- UNI：毛损益 +275.80 不变，退出从 09-03 20:17 提前至 09-02 12:10（北京时间）。
- 8/8 原始 baseline 状态/时间/PnL 重放一致；3 笔止损有目标整分钟最高价低于 stop 的直接证据。
- BNB 和第二笔 ETH 有盘中破止损，但未覆盖既定 4h 时刻；不把盘中触价误归因成定时任务漏执行。

### 结论
retest：模拟盘收益受到观察缺口污染，保留原记录并标记受影响样本，暂不用于干净前向策略验证；数据分级修复仍 keep。

### 下一步
核查 4 个未平仓计划与采集恢复，明确断档处理/采样止损语义，再推进 ATR 三线归因。报告：`reports/2026-10-09/closed_trade_gap_audit_2026-10-09_v1.md`。

## 2026-08-05 atr_reclaim prospective shadow daily progress check

- 检查名：`atr_reclaim_prospective_shadow_daily_progress_check_2026_08_05`。
- 问题：8 月 5 日 daily/import 是否按计划产生新的前向 shadow 样本，是否已经达到 pre-attribution gate。
- 当前状态：`CryptoTrading_DailyPaperUpdate` 最近运行 `2026-08-05 22:21:12 +08:00`，结果 `0`；最新数据库 run 为 `20260805_142117_1c0e47c5`，`daily_full`，状态 `success`。`CryptoTrading_4H_PaperUpdate` 最近任务返回 `2147946720`（`0x800710E0`，operator/admin refused request），需等下一次 4h 任务确认是否恢复。
- 样本：`paper_shadow_decisions=123`、`opportunities=26`、`candidate-only rows=75`、`plan-linked decision rows=48`、`mature terminal rows=0`、`right-censored open rows=48`。
- 新观察链路：`paper_shadow_candidate_observations=5`，`paper_shadow_counterfactual_outcomes=15`，`terminal counterfactual outcomes=0`。这说明 8 月 3 日新增的候选级 observation/outcome 链路已经在真实 daily/import 中开始自然写入。
- 数据洁净度：`complete opportunities=26`，`incomplete opportunities=0`，`controls_paper rows=0`，`mismatch opportunities=0`，`independent symbols=15`。
- 结论：`decision_samples_not_mature` / `reconciliation_waiting_for_terminal_outcomes`。计划有推进，但 `mature terminal opportunities=0 < 5`，仍不能开始 direct filtering 或 capacity/path attribution。
- 决策：继续等待 terminal paper statuses；不修改 `config/settings.toml`；不部署 `atr_reclaim_0_35`；不启动新 challenger；单独观察 4h 计划任务下次是否恢复。

## 2026-08-03 atr_reclaim shadow gate v6 wait check

- 检查名：`atr_reclaim_shadow_gate_v6_wait_check_2026_08_03`。
- 问题：当前是否已有新的自然 4h/daily 样本，或新增 candidate/outcome 表是否已经开始积累。
- 当前状态：本机时间 `2026-08-03 00:35:14 +08:00`，下一次 4h 自动任务为 `2026-08-03 04:10:00`，因此没有新 4h run 是预期状态。
- 结果：`decisions=105`、`opportunities=21`、`complete opportunities=21`、`controls_paper rows=0`、`incomplete opportunities=0`、`independent symbols=13`，但 `mature terminal opportunities=0`；新 `candidate observations=0`、`counterfactual outcomes=0`。
- 结论：`decision_samples_not_mature` / `reconciliation_waiting_for_terminal_outcomes`。等待状态正常，不构成策略有效性证据。
- 决策：继续等待 04:10 4h run 与 20:05 daily/import；不修改配置，不部署 `0.35`，不启动新 challenger。

## 2026-08-03 atr_reclaim shadow candidate outcome infrastructure

- 检查名：`atr_reclaim_shadow_candidate_outcome_infrastructure_2026_08_03`。
- 问题：prospective shadow observation 是否需要在 plan-linked rows 之外，额外保存候选级 observation 与不控制 paper 的 counterfactual outcomes，便于后续区分直接过滤、容量路径和候选质量。
- 变更：新增 `paper_shadow_candidate_observations` 与 `paper_shadow_counterfactual_outcomes`；daily/import 阶段为 scan candidates 记录候选级 observation，并初始化 `reference_baseline`、`atr_reclaim_0_35_shadow`、`research_incumbent` 三条 counterfactual outcome；4h update 只读推进 outcomes，不改变真实 paper plan。
- 查看入口：新增 `python main.py paper shadow-candidate-observations` 与 `python main.py paper shadow-counterfactual-outcomes`；`paper shadow-maturity` 与 `paper shadow-reconciliation` 报告新增 candidate/outcome 计数。
- 当前真实库状态：新表当前为 0 条，这是预期现象，因为该结构不会倒填旧 scan，只会从后续 daily/import 开始积累。
- 验证：`python tests\test_database.py`、`python tests\test_paper_shadow_replay.py`、`python -m compileall main.py src tests`、`python main.py db status` 均通过；新 CLI 在真实库上可运行。
- 结论：`infrastructure_ready_waiting_for_new_daily_import`。这是观察基础设施增强，不是 `0.35` 有效性证据。
- 决策：不修改 `config/settings.toml`；不授权 `0.35` 控制 paper；pre-attribution gate 仍以 mature terminal opportunities 为硬门槛。

## 2026-08-03 atr_reclaim shadow gate v3 check

- 检查名：`atr_reclaim_shadow_gate_v3_check_2026_08_03`。
- 问题：在没有新 4h/daily 自动运行的情况下，当前 shadow reconciliation/maturity 是否已经满足 pre-attribution gate。
- 样本：同 `2026-08-03 00:10 +08:00` 自动运行后的真实库状态，`decisions=105`、`opportunities=21`。
- 结果：`complete opportunities=21`、`incomplete opportunities=0`、`controls_paper rows=0`、`mismatch opportunities=0`、`independent symbols=13`；`mature terminal opportunities=0`，`right_censored_ratio=100.00%`。
- 结论：`decision_samples_not_mature` / `reconciliation_waiting_for_terminal_outcomes`。没有新增 terminal 样本，不能开始 direct filtering 或 capacity/path attribution。
- 决策：继续等待正常自动任务；不修改配置，不部署 `atr_reclaim_0_35`，不启动新 challenger。

## 2026-08-03 atr_reclaim prospective shadow 00:10 check

- 检查名：`atr_reclaim_prospective_shadow_0010_check_2026_08_03`。
- 问题：正常 4h 自动任务后，前向 shadow 样本是否已经达到 pre-attribution gate，是否可以开始解释 `atr_reclaim_0_35` 的 direct filtering 或 capacity/path 价值。
- 当前状态：`CryptoTrading_4H_PaperUpdate` 上次运行 `2026-08-03 00:10:01`，结果 `0`；`CryptoTrading_DailyPaperUpdate` 上次运行 `2026-08-02 20:05:01`，结果 `0`；最新数据库 run 为 `20260802_161002_442f70b2`，`paper_4h_update`，状态 `success`。
- 样本：最新 8/3 maturity/reconciliation 报告显示 `decisions=105`、`opportunities=21`、`candidate-only rows=60`、`plan-linked decision rows=45`、`mature terminal rows=0`、`right-censored open rows=45`、`right-censored ratio=100.00%`。
- 数据洁净度：`complete opportunities=21`，`incomplete opportunities=0`，`controls_paper rows=0`，`mismatch opportunities=0`，`independent symbols=13`。
- 运行细节：当前 open plan 为 `ONDOUSDT`，仍是 `WATCHING`；本轮报告记录 `API_DELAY_SKIPPED`，原因是 24h ticker 不可用并触发 HTTP 451，状态更新被跳过。
- 结论：`decision_samples_not_mature` / `reconciliation_waiting_for_terminal_outcomes`。除 `mature terminal opportunities=0 < 5` 外，其余 pre-attribution gate 项均已满足；当前仍不能做 direct filtering 或 capacity/path attribution。
- 决策：继续等待正常自动任务；不修改 `config/settings.toml`；不部署 `atr_reclaim_0_35`；不启动新 challenger。
- 下一步：等待 `ONDOUSDT` 或后续 plan-linked opportunities 达到 terminal paper status；只有 `mature terminal opportunities >= 5` 后才允许进入只读归因。

## 2026-08-02 atr_reclaim prospective shadow progress check

- 检查名：`atr_reclaim_prospective_shadow_progress_check_2026_08_02`。
- 问题：计划是否已经从 candidate-only 等待状态推进到 plan-linked shadow observation，以及是否可以开始归因。
- 当前状态：`CryptoTrading_DailyPaperUpdate` 上次运行 `2026-08-02 20:05:01`，结果 `0`；`CryptoTrading_4H_PaperUpdate` 上次运行 `2026-08-02 16:10:01`，结果 `0`；最新数据库 run 为 `20260802_120502_350dcb28`，状态 `success`。
- 样本：最新 maturity/reconciliation 报告显示 `decisions=105`、`opportunities=21`、`candidate-only rows=60`、`plan-linked decision rows=45`、`mature terminal rows=0`、`right-censored open rows=45`。
- 数据洁净度：三线 `reference_baseline`、`atr_reclaim_0_35_shadow`、`research_incumbent` 均存在；`complete opportunities=21`，`incomplete opportunities=0`，`controls_paper rows=0`，`mismatch opportunities=0`，`independent symbols=13`。
- 结论：`decision_samples_not_mature` / `reconciliation_waiting_for_terminal_outcomes`。计划已进入 plan-linked shadow observation，但所有 plan-linked 样本仍处于 open/right-censored，尚不能开始 direct filtering 或 capacity/path attribution。
- 决策：继续观察；不修改 `config/settings.toml`；不部署 `atr_reclaim_0_35`；不启动新 challenger。
- 下一步：等待 `paper_plan:9734a33dea2e`（`ONDOUSDT`）或后续 plan-linked opportunities 达到 terminal paper status；pre-attribution gate 需要 `mature terminal opportunities >= 5`，当前为 `0`。

## 2026-07-31 atr_reclaim execution plan update

- 检查名：`atr_reclaim_execution_plan_update_2026_07_31`。
- 问题：当前是否应继续按 `0.35` prospective shadow 计划执行，以及是否已有足够样本开始归因。
- 当前状态：`CryptoTrading_DailyPaperUpdate` 上次运行 `2026-07-30 20:05:01`，结果 `0`；`CryptoTrading_4H_PaperUpdate` 上次运行 `2026-07-31 08:10:01`，结果 `0`，下一次 `2026-07-31 12:10:00`；最新数据库 run 为 `20260731_001002_b39e3bc4`，状态 `success`。
- 样本：`paper_shadow_decisions` 当前有 15 行，来自 2026-07-30 daily/import 的 5 个 scan candidates，每个 candidate 均有 `reference_baseline`、`atr_reclaim_0_35_shadow`、`research_incumbent` 三线。
- 结论：`candidate_context_only_wait_for_plan_linked_samples`。candidate-level logging 已经正常，但仍没有 plan-linked decision rows 和 mature terminal outcomes，不能开始 direct filtering 或 capacity/path attribution。
- 决策：继续执行 prospective shadow observation；不运行新的近端历史 `atr_reclaim_0_35` A/B；不修复 2023-2024 validation branch；不修改 `config/settings.toml`；不授权 `0.35` 控制 paper。
- 计划产物：`reports/2026-07-31/atr_reclaim_execution_plan_update_2026-07-31_v1.md`。
- 下一步：等待正常 `2026-07-31 12:10 +08:00` 4h 任务后复查 `paper shadow-decisions`、`paper shadow-maturity`、`paper shadow-reconciliation` 和 `db status`；若仍只有 candidate-level rows，则继续等待正常触发。

## 2026-07-30 atr_reclaim prospective shadow logging

- 实验名：`atr_reclaim_prospective_shadow_observation_logging`
- 变更：在既有 `paper_shadow_decisions` 基础上，补充 daily/import 阶段的 candidate-level context logging；每个 scan candidate 固定写入 `reference_baseline`、`atr_reclaim_0_35_shadow`、`research_incumbent` 三条参照线。
- 样本：未来真实 daily/import 与 4h paper update 产生的 prospective 样本；当前提交只验证记录链路，不形成收益判断。
- 结论：`infrastructure_ready_waiting_for_samples`。候选登记、4h decision-state、查看命令、导出链路和 `paper shadow-maturity` 成熟度报告已经具备基础能力；`daily` 与 `paper cycle` 成功运行后会自动生成 maturity review；真实库当前报告 `no_shadow_samples_yet`，需要等待新的 daily/import 或 4h update 产生前向样本。
- 决策：`atr_reclaim_0_35` 继续作为 `provisional_research_incumbent` 与独立 `atr_reclaim_0_35_shadow` 参照线保留；不控制 paper 下单，不修改 `config/settings.toml`。
- 运维边界：`ticker_24hr` 瞬断现在会记录为 `API_DELAY_SKIPPED` 并生成 snapshot，避免一次 SSL/网络错误阻断 maturity review 链路；这不是策略有效性证据。
- 链路验证：手动运行 `python main.py paper cycle --no-obsidian` 成功，run `20260730_104051_53df384d` 生成 `paper_shadow_maturity_review_2026-07-30_demo_v7.md`；verdict 仍为 `no_shadow_samples_yet`，因为本次没有 daily/import candidate rows，也没有 entry-zone 4h decision rows。
- 等待诊断：`paper_shadow_maturity_review_2026-07-30_demo_v8.md` 已补充 open plans、latest scan、latest daily/4h run 和 next trigger；当前等待条件为正常 daily/import candidate rows，或 `ONDOUSDT` WATCHING plan 触及 entry_high 触发 4h decision rows。
- 数据链路：`python main.py db stability --days 5` 已通过，2026-07-25 -> 2026-07-29 连续 5 个 daily run 全部 `ready=true`，`ready_for_4h_task=true`，config hash 稳定为 `be7ec39ec21f6a83`；这是观察链路证据，不是策略有效性证据。
- 下一步：等待新的 daily scan/import 或 open plan 触发 entry-zone 4h decision 后检查自动生成的 `paper_shadow_maturity_review`；足够成熟前不比较 `0.35` 的有效性，也不授权 paper deployment。

## 2026-07-27 Stage A-E 执行结论

- `replacement_closure_audit`：复用 Stage 1 JSON 与 Stage 4 Raw Summary，检查 512 个 blocked events、42 个 eligible comparison events 的去重、stale trade 集中度、first-event-per-stale-trade、exclude 2025-07、exclude same-bar ambiguous 与 cluster bootstrap。核心结果为 `unique_stale_trades=3`、`stale_trade_top1_share_pct=83.333%`、`first_event_per_stale_trade_R42_median=-0.004`、`cluster_bootstrap_R42_p05=-0.565`，结论 `paused_no_stable_executable_edge`。
- `stage_a_to_e_execution_review`：确认 Stage B/C/D 已由既有 `atr_reclaim_0_35` 正式 A/B、交易级归因、路径复盘和阈值敏感性报告覆盖。`atr_reclaim_0_35` 报告级指标改善，但收益来源仍主要是 variant-only 新增赢家与容量路径变化，不是 common trades 广泛改善，因此维持 `retest_path_dependent`。
- 决策：不进入 Stage 5 / Stage E shadow replacement，不部署 `atr_reclaim_0_35`，不提高 `max_active_positions`，不修改 `config/settings.toml`。后续若继续研究，必须回到 capacity-neutral 的单变量 entry-quality retest，且先写实验卡片。

## 1. 账本规则

本账本只记录实验回答了什么问题，以及结论处于什么证据等级。以后新增实验前必须先写实验卡片；实验结束后再更新本账本。

证据等级定义：

| 等级 | 含义 |
|---|---|
| 事实 | 报告或代码中直接可见的结果、配置、样本数量、指标 |
| 观察 | 某个参数在当前窗口中表现更好或更差 |
| 假设 | 对观察的解释，尚未被独立证明 |
| 决策 | 是否部署、保留为候选、否定或继续复测 |

默认纪律：

- `retest` 不是 keep。
- `candidate_keep_review` 不是自动部署。
- 只因为净收益提高，不允许修改 `config/settings.toml`。
- 未经用户明确批准，实验完成后不修改生产配置。

## 2. 当前默认生产策略变更记录

| 规则 | 当前状态 | 依据 | 证据等级 |
|---|---|---|---|
| 数据质量过滤，非 `DATA_OK` 买入候选降级 | 已部署 | scan、paper、backtest 路径均接入 | 决策 |
| `min_history_days=180` | 已部署 | 历史长度过滤已写入默认配置 | 决策 |
| `risk_off_core_buy_enabled=false` | 已部署 | 弱市核心币也暂停新开仓 | 决策 |
| `entry_reclaim_close_enabled=true` | 已部署 | 入场确认已成为默认模拟盘路径 | 决策 |
| `tp1_ema_trailing_stop_enabled=true` | 已部署 | TP1 后 EMA20 trailing 已补齐到 paper 和 backtest | 决策 |
| Regime 阈值 BTC -3%、ETH -5%、要求两者趋势 | 已部署 | 当前 `settings.toml` 已采用 sensitive 阈值 | 决策 |
| `max_holding_bars_without_tp1=42` | 未部署 | 回测候选，但需 paper 观察后 keep review | 决策：暂不部署 |
| `relative_strength_soft_gate_enabled=true` | 未部署 | 7 月 26 日阈值敏感性仍为 `retest` | 决策：暂不部署 |
| `entry_reclaim_min_atr_enabled=true` | 未部署 | `atr_reclaim_0_35` 人工路径复盘后降为 `retest_path_dependent`：新增赢家与错过赢家都存在高质量样本，且结果强受仓位容量路径影响 | 决策：暂不部署 |

## 3. 实验汇总表

| 实验 | 要回答的问题 | 唯一变量 | 样本范围 | 核心结果 | 当前结论 | 局限 |
|---|---|---|---|---|---|---|
| `history_250` / `history_365` | 更长历史长度是否提高选币质量 | `analysis.min_history_days` | 2025-01-01 起多个 dynamic universe 窗口 | `history_365` 部分窗口改善，但跨段不稳定 | `retest`，不 keep | 早期样本不足，历史长度与新币机会存在冲突 |
| `pump_chase_strict` | 更严格追高惩罚是否减少高位接盘 | 追高阈值和惩罚 | 2025-01-01 -> 2025-09-01 等 | 未形成稳定优势 | `retest` | 单窗口证据不足 |
| `liquidity_50m` | 更高流动性门槛是否减少噪音交易 | 成交额 30m -> 50m，交易数 30k -> 50k | 多个 dynamic universe / fixed master 窗口 | 多次方向改善，但早期/部分窗口样本不足或仍为负收益 | `retest` | 不能证明流动性阈值是独立优势来源 |
| `risk_off_no_core_buy` | RISK_OFF 下是否连 BTC/ETH 也应暂停新开仓 | `risk_off_core_buy_enabled` | 2025-01-01 -> 2025-09-01 | RISK_OFF 亏损减少，但 RISK_ON 仍弱 | `retest` | 需要与入场质量规则组合 |
| `top_n_3` | 降低每次候选容量是否减少拥挤开仓 | `market.top_n=3` | 2025-01-01 -> 2025-09-01 | RISK_ON 亏损减少，但不能独立转正 | `retest` | 可能只是降低暴露，不是提高胜率 |
| `risk_off_no_core_top_n_3` | 弱市暂停核心币 + 降低容量是否互补 | regime + capacity 组合 | 2025-01-01 -> 2026-06-01 两段 | 亏损减少，近端仍为负收益 | `retest` | 组合实验，归因不如单变量清晰 |
| `entry_reclaim_close` | 入场前等待 4h 收盘站回 `entry_high` 是否减少接飞刀 | `entry_reclaim_close_enabled` | 2025-01-01 -> 2026-06-01 | 近端窗口转正，早期样本不足 | `retest`，后续已进入组合策略 | 早期 RISK_ON 仍弱 |
| `risk_off_no_core_entry_reclaim` | 弱市暂停开仓与入场确认能否互补 | regime + entry 组合 | 2024-07-01 -> 2026-06-01 | 两个充分窗口净收益、PF、MDD 均改善 | `candidate_keep_review` | 组合规则，需要人工确认机制合理性 |
| `tp1_breakeven_stop` | TP1 后立即保本是否保护利润 | `tp1_move_stop_to_breakeven_enabled` | 2025-01-01 -> 2025-09-01 | PF、净收益、止损率恶化 | `reject_candidate` | 噪音止损增加 |
| `tp1_ema20_trailing_stop` | TP1 后 EMA20 trailing 是否优于立即保本 | `tp1_ema_trailing_stop_enabled` | 2024-07-01 -> 2025-09-01 | 两段方向改善，但近端绝对值仍弱 | `retest`，后续进入组合策略 | TP2 rate 下降、副作用需复核 |
| `risk_off_no_core_entry_reclaim_ema_stop` | regime + reclaim + EMA trailing 是否形成稳定组合 | 三项组合 | 2024-07-01 -> 2026-06-01 | 两段净收益、PF、MDD 全面改善 | `candidate_keep_review`，后续成为 sensitive 默认主线 | 组合策略仍需 paper 验证 |
| `daily_trend_required` | 日线趋势硬门槛是否提高质量 | `daily_trend_required=true` | 2024-07-01 -> 2026-06-01 等 | 近端止损率和净收益恶化 | `reject_candidate` | 可能导致更高位置追入 |
| `regime_sensitive` | 更严格 BTC/ETH regime 阈值是否更好 | BTC/ETH 跌幅阈值和趋势要求 | 2024-07-01 -> 2026-06-01 | 作为组合的一部分有效，单独仍需 retest | `retest` / 已进入默认组合 | 单独贡献未完全隔离 |
| 市值分层 large-cap vs altcoin | 收益/风险是否由 altcoin 拖累 | SymbolMaster 分层 | 2024-07-01 -> 2026-06-01 | large-cap 两段为正；altcoin 熊市拖累明显 | `candidate_keep_review` | 分层发现不等于组合规则可部署 |
| `large_cap_only_risk_off` | RISK_OFF 只允许 BTC/ETH/BNB/SOL 是否更好 | `risk_off_large_cap_buy_enabled=true` | 2024-07-01 -> 2026-06-01 | 两段方向相反，近端拖累 | `retest` / 不 keep | 与单独 large-cap 回测结论不一致 |
| `max_holding_18/30/42x4h_no_tp1` | 未触发 TP1 的持仓等待多久仍值得 | `max_holding_bars_without_tp1` | 2024-07-01 -> 2026-06-01 | 三阈值均改善，42 根最平衡 | `candidate_keep_review` | 可能牺牲少数延迟启动赢家 |
| `risk_off_no_core_entry_reclaim_ema_stop_sensitive_max_holding_42` | 在当前 sensitive 组合上叠加固定 42 根退出是否继续改善 | `max_holding_bars_without_tp1=42` | 2024-07-01 -> 2026-06-01 | PF、Sharpe、净收益改善；早期 MDD 恶化 | `retest` | 不能直接部署，需 paper 后复核 |
| `max_holding_42x4h_conditional` | 42 根后按 EMA/entry 条件退出是否优于无时间退出 | 42 根 + conditional | 2024-07-01 -> 2026-06-01 | 两段改善但不能回答是否优于固定 42 | `retest` | 比较对象不够严格 |
| `max_holding_42_fixed_vs_conditional_sensitive` | 条件式 42 是否优于固定 42 | `max_holding_bars_conditional` | 2023-07-01 -> 2026-06-01 三窗口 | 条件版 2/3 窗口变差，3/3 MDD 更高 | `reject_candidate` | 固定 42 仍可作为候选 |
| Paper checkpoint / formal audit | 三周模拟盘是否足以支持改 live/paper 规则 | 只审计，不改配置 | 2026-06-19 -> 2026-07-25 | 7 月 25 日 extended window `formal_audit_ready`，但结论是先研究 entry 质量 | 不改配置 | right-censored 和机会成本仍明显 |
| `reclaim_quality_matrix` shadow | RECLAIM_PENDING 后是否需要更强确认 | 离线 reclaim 变体 | 2026-06-19 -> 2026-07-25 | `atr_reclaim_0_25` 是最佳候选之一 | `retest` | shadow 不是正式 dynamic A/B |
| `momentum_pullback_definition_ab` shadow | 当前动量/回调定义是否过松 | 离线动量/回调定义 | 2026-06-19 -> 2026-07-25 | `trend_support_atr_pullback` 表现最好但仍不可部署 | `retest` | 短窗口重叠、右截尾 |
| `relative_strength_soft_gate` shadow | 相对 BTC/ETH 弱势是否应过滤或降级 | 相对强度门槛 | 2026-06-19 -> 2026-07-25 | `btc_eth_soft_minus_0_5` 最佳候选 | `retest` | 需要正式 A/B |
| `relative_strength_soft_gate_btc_eth_minus_0_5` | 正式 A/B 验证相对强度 soft gate | `relative_strength_min_pct=-0.5` | 2024-07-01 -> 2026-06-01 | 两段 PF/净收益/Sharpe 改善，但早期 MDD 16.59% -> 18.96% | `retest` | MDD 恶化来源未完全消除 |
| `relative_strength` 阈值敏感性 | -1.0、-0.5、0.0 哪个更稳 | 阈值 | 2024-07-01 -> 2026-06-01 | -0.5 最平衡；-1.0 近端退化；0.0 早期 MDD 最差 | `retest` | 该家族暂不部署 |
| `atr_reclaim_0_25` | reclaim 超过 `entry_high + 0.25 ATR` 是否提高入场质量 | `entry_reclaim_min_atr` | 2024-07-01 -> 2026-06-01 | 两段净收益、PF、Sharpe、胜率改善；早期 MDD 16.59% -> 19.21% | `retest` | 需做 0.10/0.15/0.35 同维度敏感性 |
| `atr_reclaim` 阈值敏感性 | 0.10、0.15、0.25、0.35 哪个 reclaim margin 更稳 | `entry_reclaim_min_atr` | 2024-07-01 -> 2026-06-01 | 0.10/0.15 近端净收益和 PF 退化；0.35 两段净收益、PF、MDD 均改善；交易级归因和人工路径复盘显示改善主要来自 variant-only 新增赢家与容量路径 | `retest_path_dependent` for `atr_reclaim_0_35` | 不能证明 0.35 ATR 是稳定入场质量优势 |

## 4. 事实 / 观察 / 假设 / 决策拆分

### 事实

- 当前默认配置已启用 `entry_reclaim_close_enabled=true`、`tp1_ema_trailing_stop_enabled=true`、`risk_off_core_buy_enabled=false`。
- 当前默认配置未启用 `relative_strength_soft_gate_enabled`、`entry_reclaim_min_atr_enabled`、`max_holding_bars_without_tp1`。
- A/B runner 会对实验 override 路径做白名单限制。
- A/B 自动结论不会直接给 `keep`，样本不足时保持 `retest`。
- `reports/2026-07-26/atr_reclaim_0_25_formal_ab_review_2026-07-26_v1.md` 记录 `atr_reclaim_0_25` 两段 PF/净收益改善，但早期 MDD 恶化。
- `reports/2026-07-26/atr_reclaim_threshold_sensitivity_2026-07-26_v1.md` 记录 `atr_reclaim_0_35` 两段净收益、PF、MDD 均改善，并进入 `candidate_keep_review`。
- `reports/2026-07-26/atr_reclaim_0_35_trade_attribution_review_2026-07-26_v1.md` 记录交易级归因：合并后 common trade delta 为 `-43.72 USDT`，removed baseline-only 贡献 `+594.76 USDT`，added variant-only 贡献 `+3184.11 USDT`；近端窗口 top3 正贡献占该窗口净改善 `167.7%`，说明存在路径依赖。
- `reports/2026-07-26/atr_reclaim_0_35_path_replay_review_2026-07-26_v1.md` 记录 10 笔关键路径复盘：5 笔 variant-only 赢家 reclaim margin 均超过 `0.35 ATR`，但 5 笔 missed baseline winners 同样全是 TP2 赢家；CFX/ENA/ADA 等机会出现时 baseline 多数已达到 `max_active_positions=5`，说明收益强受容量路径影响。
- `reports/2026-07-26/capacity_and_opportunity_order_review_2026-07-26_v1.md` 记录容量与机会排序复核：baseline 满仓 28.0% 的 4h bars，variant 满仓 30.3%；两组都有长期负 R 占槽问题，但关键 missed winners 的 blocker 质量混合，结论为 `retest_capacity_real_but_not_actionable`。
- `reports/2026-07-27/signal_fill_timing_audit_2026-07-27_v1.md` 记录 replay 时点审计：active exits 先于 WATCHING entries，WATCHING 按 `(-score, created_index, symbol)` 排序，reclaim 用当前 4h close 判断，entry raw price 为 `entry_high`；结论 `timing_audit_warn_same_bar_ambiguity`，后续 blocked event export 必须显式记录 same-bar ambiguity。
- `reports/2026-07-27/blocked_entry_event_export_2026-07-27_v1.md` 与 `reports/2026-07-27/blocked_entry_event_export_2026-07-27_v1.json` 记录 Stage 1 blocked event export：source run `110c51eef593` 复跑为 `ed682b4a5531`，source/replay entered trades 均为 58，导出 `blocked_entry_events=512`；`same_bar_entry_exit_possible_events=0`、`same_bar_entry_tp1_possible_events=2`。该结果只是事件样本导出完成，不构成 replacement edge 证据。
- `reports/2026-07-27/replay_consistency_audit_2026-07-27_v1.md` 记录 Stage 2 replay consistency audit：source run `110c51eef593` 复跑为 `1e3cbb13c14a`，trades `389 -> 389`，entered trades `58 -> 58`，active/open-plan path 2190 点 mismatch 均为 0，final equity delta 为 0，blocked event repeat `512 -> 512` 且 signature mismatch 为 0；结论 `replay_consistency_pass_with_ordering_limit`，候选排序因 source 未直接持久化，只能通过源码 marker 与重复事件签名间接验证。
- `reports/2026-07-27/stale_slot_continuation_review_2026-07-27_v1.md` 记录 Stage 3 stale slot continuation review：source run `110c51eef593` 复跑为 `8e24e6bda89b`，总 entered trades 58，pre-TP1 且达到 `42 bars = 168h` 的合格 stale slots 为 26，`right_censored_count=1`。继续持有增量 R：`forward_R_24_mean=-0.282`、`forward_R_42_mean=-0.132`、`forward_R_60_mean=-0.191`、`eventual_continuation_R_mean=-0.129`；first-hit outcome 为 stop 15、tp1 10、not_hit_by_end 1。结论 `stale_slot_continuation_weak_retest`，支持继续做 replacement 诊断，但不部署、不修改仓位上限。
- `reports/2026-07-27/blocked_candidate_vs_stale_slot_review_2026-07-27_v1.md` 记录 Stage 4 blocked candidate vs stale slot review：source run `110c51eef593` 复跑为 `e40da6f04438`，512 个 blocked events 中 rank1 events 为 46，合格比较事件为 42，右截尾 0，同根 TP1 ambiguity 1。主规则比较排序第一 blocked candidate 与最老 pre-TP1 stale slot：`net_delta_R_24_mean=0.436`、`net_delta_R_42_mean=0.309`、`net_delta_R_60_mean=0.176`，但 R42 median 为 `-0.223`、positive ratio 为 `42.9%`、20% trimmed mean 约 `0.001`；lowest-unrealized sensitivity 的 R42 median 仍为 `-0.276`，oracle upper bound 才明显为正。结论 `replacement_edge_not_supported`，不进入 shadow replacement。
- `reports/2026-07-26/relative_strength_soft_gate_threshold_sensitivity_2026-07-26_v1.md` 记录相对强度阈值家族全部仍为 `retest`。

### 观察

- 弱市开仓限制、4h reclaim 入场确认、TP1 后 EMA trailing 的组合比早期 baseline 更稳。
- `max_holding=42` 对未触发 TP1 的停滞交易有清理价值，但固定版与条件版的比较显示条件版不稳。
- 相对强度 soft gate 能改善 PF/净收益，但没有解决早期 MDD 问题。
- ATR reclaim 门槛能改变成交集合；`0.35` 当前最强，但人工路径复盘显示优势强受组合容量和机会排序影响，不能证明是稳定的单变量入场质量优势。

### 假设

- 长时间未触发 TP1 的交易，大概率已经失去趋势延续优势。
- 弱市中即便 BTC/ETH 也可能不适合作为新开仓对象。
- 4h 收盘重新站回入场区间可以过滤一部分接飞刀交易。
- TP1 后立即保本过于僵硬，EMA20 trailing 更能适应趋势波动。
- 相对 BTC/ETH 明显弱的币，即使绝对涨幅为正，也可能不是优先买入对象。
- ATR reclaim 的最佳阈值可能高于 0.25，但当前证据更像“路径换仓 + 容量释放”而不是纯粹质量提升；容量与机会排序复核确认约束真实存在，但尚不足以直接改仓位上限或排序。
- 满仓时真正需要验证的是换仓质量：新机会是否稳定优于当前占槽仓位，而不是简单提高 `max_active_positions`。

### 决策

- 继续暂停新增复杂度，先完成系统理解和实验账本。
- 不部署 `relative_strength_soft_gate`。
- 不部署 `atr_reclaim_0_25`。
- 不部署 `atr_reclaim_0_35`；人工路径复盘后降级为 `retest_path_dependent`，容量复核后仍不修改 `max_active_positions` 或 score 排序。
- 容量 replacement 分支当前收束：`signal_fill_timing_audit`、`blocked_entry_event_export`、`replay_consistency_audit`、`stale_slot_continuation_review` 与 `blocked_candidate_vs_stale_slot_review` 已完成。Stage 4 未证明稳定 replacement edge，因此不进入 Stage 5 shadow replacement，不新增生产过滤器；后续若重启容量研究，必须先提出更强且事前声明的 slot selection 规则或更广 walk-forward 证据。
- 不部署 `max_holding_bars_conditional=true`。
- `max_holding_bars_without_tp1=42` 仅保留为候选，等待模拟盘/人工复核。
- 后续任何实验必须先提交实验卡片并获得用户批准。

## 5. 实验卡片模板

```markdown
# 实验卡片

## 1. 本实验要回答的问题
用一句话说明。

## 2. 为什么现在需要做
它与当前系统的哪个问题有关。

## 3. 核心假设
如果假设成立，预计会看到什么结果。

## 4. 实验变量
本次只改变什么参数。

## 5. 固定条件
哪些内容必须保持不变。

## 6. 评价指标
主要指标：
次要指标：
风险指标：

## 7. 判定标准
什么结果支持假设；
什么结果否定假设；
什么结果属于证据不足。

## 8. 可能风险
样本不足、过拟合、数据泄漏、少数极端交易驱动等。

## 9. 实验完成后是否允许修改生产配置
默认：不允许。
```

## 2026-07-29 Stage N0 readiness audit - atr_reclaim_0_35 third-window gate

- `atr_reclaim_n0_readiness_audit`：固定 `atr_reclaim_0_35`、窗口 `2023-07-01 -> 2024-07-01`、master `reports/2026-06-09/dynamic_master_full.json`，生成 `reports/2026-07-29/atr_reclaim_n0_readiness_audit_2026-07-29_v1.md`。
- 核心事实：`git_dirty=false`，commit `4910a67f103d2c6d116f585e04bf66eaad7e2915`；`settings_hash=be7ec39ec21f6a838571511cb2cd0e290263031b521a9a07a6fb70164b8ef4bf`；`experiments_hash=7e6eca2609546d94293162870df6cc6ab8795666845b58facd979b698917dbe1`。
- Universe 审计：固定 master 有 418 个 symbols，但 `listing_dates_present=false`；第三窗口 1h/4h/1d 完整覆盖均为 207 个 symbols，部分覆盖 59 个，完全无历史 K 线 152 个，覆盖率约 56.1%。
- 结论：`n0_conditional_pass_with_universe_bias_warning`。`atr_reclaim_0_35` 第三窗口可以准备 diagnostic retest，但不能称为 clean confirmatory validation，不能用于 keep 或部署。
- 下一步：优先补 listing-date enriched `SymbolMaster` 或历史 membership 证据后重跑 N0；若用户明确批准，也可在 caveat 下运行 N1 diagnostic，但必须同时报告组合层、direct filtered/retained 机制层和 symbol/month/symbol-month cluster concentration。

## 2026-07-30 Stage N1 diagnostic retest - atr_reclaim_0_35

- `atr_reclaim_0_35` 第三窗口 diagnostic A/B 已完成：baseline run `86861b2dd032`，variant run `0d78a8dc60e3`，报告 `reports/2026-07-30/abtest_dynamic_universe_atr_reclaim_0_35_2023-07-01_2024-07-01_v1.md`。
- 组合层事实：closed_trades 122 -> 116，win_rate 47.54% -> 50.00%，PF 1.264 -> 1.376，net_return 22.10% -> 31.55%，MDD 21.85% -> 21.08%，Sharpe 0.932 -> 1.238，`sample_sufficient=true`。
- 机制层事实：same-key baseline entered / variant did not enter 的 50 笔直接过滤样本原本净贡献 +1335.62 USDT；避免亏损 +3141.55，但错过赢家 -4477.17，direct-filter effect 为负。
- 路径贡献：same-key variant entered / baseline not entered +1609.43，variant-only entered +2726.00，baseline-only removed -2149.62，both-entered delta +95.43；整体改善主要来自 path/capacity-timing added trades，而不是直接过滤质量。
- cluster：2023-12 +936.23、2023-11 +742.67，但 2024-02 -830.94、2024-03 -355.19；top symbol-month 贡献集中在 FET 2024-03、ETC 2024-03、NEAR 2023-11、BTC 2023-12、DOT 2023-12。
- 结论：`retest_path_dependent`。不得 keep、不得部署、不得修改 `settings.toml`；下一步优先补 listing-date enriched master / historical membership，并改进 strict opportunity id 后再重跑 N0/N1。

## 2026-07-30 Stage N2 universe gate - atr_reclaim_0_35 third-window qualification

- `atr_reclaim_stage_n2_universe_audit`?????? `2023-07-01 -> 2024-07-01` ???????????????????? `atr_reclaim_0_35` ?????
- N2-A ???418 ? current master symbols ???? listing date?`listed_after_window=152`?`listed_inside_window=49`?`full_window_coverage=208`?`partial_window_coverage=9`?
- N2-B ???Binance public-data ????? 1d monthly files ? historical USDT symbols ? `413`??? `147` ??? current master?????? `35.6%`?
- N0 rerun??? `reports/2026-07-30/dynamic_master_full_listing_enriched_2026-07-30_v2.json` ??? verdict ? `n0_conditional_pass_with_alignment_warning`?? N0 ???? historical membership ????????? N2-B gate?
- ???`third_window_diagnostic_only_do_not_rerun_n1`???????????? clean confirmatory validation??????? N1??????????
- ?????? historical symbol membership dataset????? `listing_time / delisting_time / first_kline_time / last_kline_time / tradable_from / tradable_to / source / confidence`?

## 2026-07-30 Stage N3 historical membership dataset - third-window recovery gate

- `atr_reclaim_stage_n3_historical_membership_dataset`??? N2 ? `147` ? missing historical symbols ????????????????
- ?????leveraged token `9`?stable/fiat/excluded base `10`?nonstandard wrapped/staked asset `1`?standard spot missing `120`?rename/migration candidate `7`?
- ????????????? `20` ??standard-like historical gap ?? `127` ????? universe `32.32%`?
- ???`third_window_not_recoverable_without_historical_master`??????????????????????? corrected N1??????????
- ?????? source-backed historical master?? 127 ? standard-like gaps ? delisting / migration / replacement / confidence?

## 2026-07-30 Stage N4 historical master MVP - validation blocking queue

- `atr_reclaim_stage_n4_historical_master_mvp`?? N3 dataset ?????? historical master MVP?????? blocking review queue?
- ???total rows `413`?`active_current_master=266`?`excluded_by_strategy_universe_rule=20`?`historical_standard_gap_requires_mapping=127`?
- operational actions?`eligible_for_dynamic_universe_if_data_and_liquidity_pass=266`?`exclude_from_historical_master=20`?`manual_review_delisting_or_exclusion_before_validation=120`?`manual_review_rename_or_migration_before_validation=7`?
- ???`historical_master_mvp_built_validation_blocked`?historical master MVP ??????? validation-ready????? A/B???????????
- ????? 127 ? blocking symbols ?? official/source-backed mapping???????????? universe ????

## 2026-07-30 atr_reclaim 2023-2024 window abandonment decision

- ???`abandon_2023_2024_window_for_atr_reclaim_validation`?
- ???`atr_reclaim_0_35_status=experimental_candidate_unvalidated`??? keep??? rejected?????
- ???N2 ?? 147 ? missing historical symbols?N3 ?????????? 127 ? standard-like gap?gap ratio `32.32%`?N4 verdict ? `historical_master_mvp_built_validation_blocked`?
- ???N0-N4 ????? diagnostic evidence?????? 2023-2024 historical universe???? corrected N1??? path fork audit????????? `atr_reclaim_0_35` ??????
- ????`freeze diagnostic artifacts -> candidate recent-window eligibility audit -> prospective shadow observation schema -> ?????? one-time auxiliary A/B`?

## 2026-07-30 atr_reclaim recent-window eligibility audit

- 审计目标：判断是否存在一个近端历史窗口，可以作为 `atr_reclaim_0_35` 的事前锁定 one-time A/B 验证窗口。
- 执行边界：没有运行新的 A/B，也没有查看新的 `atr_reclaim_0_35` 收益结果；只复核既有报告、账本和窗口使用记录。
- 关键事实：`2024-07-01 -> 2025-06-01` 与 `2025-06-01 -> 2026-06-01` 已被 ATR reclaim 阈值敏感性、正式 A/B、交易级归因、路径复盘和 capacity review 反复观察；`2026-06-19 -> 2026-07-02`、`2026-07-03 -> 2026-07-25`、`2026-07-17 -> 2026-07-25` 已被 paper/shadow 复盘使用。
- 结论：`no_clean_recent_window_available_for_strong_historical_validation`。现有近端历史窗口只能作为 auxiliary/context 或 diagnostic evidence，不能承担强验证。
- 决策：不运行新的近端历史 `atr_reclaim_0_35` A/B，不部署，不修改 `config/settings.toml`。
- 下一步：转向 prospective shadow observation schema/MVP，记录 baseline 与 `atr_reclaim_0_35` variant 的同一时点决策、capacity state、direct filtering 与 path contribution。

## 2026-07-30 atr_reclaim provisional research incumbent decision

- 决策：`accept_atr_reclaim_0_35_as_provisional_research_incumbent`。
- 定义：`reference_baseline=original_strategy_without_atr_reclaim_0_35`；`atr_reclaim_0_35_shadow=original_strategy_plus_atr_reclaim_0_35`；`research_incumbent=reference_baseline_plus_atr_reclaim_0_35`。
- 边界：`paper_deployment=pending_shadow_or_explicit_user_approval`；`real_money_deployment=not_authorized`；`parameter_tuning=frozen`。
- 证据状态：`historical_validation_status=promising_but_not_independently_validated`；`mechanism_status=direct_filter_advantage_unconfirmed / capacity_path_advantage_plausible_but_unconfirmed`。
- 比较框架：日常研发用 `new challenger vs research_incumbent`；长期校准保留 `atr_reclaim_0_35_shadow vs reference_baseline`；完整系统检查看 `new challenger vs reference_baseline`。
- 后续优先级：满仓候选排序与机会成本、容量利用、`TIME_EXIT` 与退出规则、执行质量/滑点/状态一致性、市场状态适应性、新入场过滤因素。

## 2026-07-30 atr_reclaim incumbent shadow MVP

- 实现：新增只读 shadow experiment `atr_reclaim_incumbent_shadow`，通过 `python main.py paper shadow-experiment --experiment atr_reclaim_incumbent_shadow` 生成固定 opportunity set 上的三线对照。
- 三线：`reference_baseline`、`atr_reclaim_0_35_shadow`、`research_incumbent`；其中 `research_incumbent` 在当前 MVP 中等同 `atr_reclaim_0_35_shadow`，但仍独立输出，便于后续 challenger 对照。
- 输出字段：decision timestamp、symbol、variant decision、reclaim margin ATR、mature outcome、direct filter R；capacity/path 字段暂标记为 `not_available_in_offline_opportunity_set`。
- 验证运行：`2026-07-03 -> 2026-07-25` demo opportunity set `9468fbe1bab35767`；报告 `reports/2026-07-30/paper_shadow_experiment_atr_reclaim_incumbent_shadow_2026-07-03_2026-07-25_demo_v1.md`。
- 诊断结果：`atr_reclaim_0_35_shadow` opportunities `95`、accepted `75`、filtered `20`、total_decision_R `50.14`、direct_filter_R `10.00`；`reference_baseline` total_decision_R `44.14`。这是 MVP smoke/diagnostic，不是强验证或部署依据。
- 下一步：在 live paper 4h/daily 决策点补 `active_positions`、capacity state、strict opportunity id 与 reference/0.35 shadow decisions，才能做完整 path/capacity attribution。

## 2026-07-30 atr_reclaim live decision-state logging

- 实现：新增 SQLite 表 `paper_shadow_decisions`，只追加记录 shadow decision，不改变 `paper_plans` / `paper_events` 的交易状态语义。
- 接入点：`paper update` 中 WATCHING 计划触及 entry zone 且存在已收 4h K 线时，写入 `reference_baseline`、`atr_reclaim_0_35_shadow`、`research_incumbent` 三条同一时点决策。
- 记录字段：`opportunity_id=paper_plan:{plan_id}`、plan_id、symbol、decision_time、kline_time、line_name、decision、accepted、current_price、last_4h_close、entry_high、atr_4h、reclaim_margin_atr、active_positions、max_active_positions、capacity_state。
- 可见性：新增 `python main.py paper shadow-decisions --limit N`；`db-export` 新增 `paper_shadow_decisions_YYYY-MM-DD.csv`。
- 验证：`python main.py db status` 真实库 schema/tables/indexes OK；`python main.py paper shadow-decisions --limit 5` 当前返回空列表，说明新表已可读，但新 logging 尚需下一次符合条件的 paper update 触发。
- 边界：仍不修改 `config/settings.toml`，不启用 `0.35` 控制 paper 下单，不授权实盘。


## 2026-07-30 paper max_holding_42 forward review

- Experiment: `paper_max_holding_42_forward_review`.
- Question: does current paper evidence support writing fixed `max_holding_bars_without_tp1=42` into default `config/settings.toml`?
- Evidence: `db stability --days 5` passed; `paper_4h_dashboard_1840_demo_v1.md` found 3 positions over `42 x 4h / 168h`; event review checked plans `2ed171ff8ada`, `5d1c3b7ddf56`, and `616e1bbfd4c6`.
- Result: all 3 over-threshold paper cases ultimately ended as `STOPPED`, with no `TP1_HIT` event found before the terminal stop; however, 2/3 cases are `ONDOUSDT` and the sample covers only 2 independent symbols.
- Conclusion: `defer_keep_review_insufficient_forward_evidence`. Fixed 42-bar exit remains directionally supported, but current forward evidence is too small and concentrated to justify default deployment.
- Decision: do not modify `config/settings.toml`; keep observing daily + 4h paper samples and reopen keep review after at least 5 independent symbols or 8-10 terminal over-42h cases.

## 2026-07-30 paper execution state consistency precheck

- Experiment: `paper_execution_state_consistency_precheck`.
- Question: is the current paper database and shadow logging chain clean enough to continue prospective observation?
- Evidence: `db status` OK; `db stability --days 5` passed; paper DB contains 25 plans, 534 snapshots, 0 duplicate event groups, 0 events without plan, and 0 snapshots without plan.
- Result: paper event/state linkage is clean; the only current open plan is `ONDOUSDT` `9734a33dea2e` in `WATCHING`; one transient market-data issue was recorded as `API_DELAY_SKIPPED` without changing paper state.
- Limitation: `paper_shadow_decisions` remains empty, so reference baseline vs `atr_reclaim_0_35_shadow` vs research incumbent cannot yet be reconciled.
- Conclusion: `execution_precheck_pass_shadow_reconciliation_waiting_for_samples`; continue observation, but do not validate or deploy `0.35` or any new challenger yet.

## 2026-07-30 paper shadow reconciliation MVP

- Experiment/tooling: `paper_shadow_reconciliation_mvp`.
- Purpose: create the read-only report that will be used once prospective shadow rows exist, before interpreting direct filtering or capacity/path contribution.
- Implementation: added `python main.py paper shadow-reconciliation --no-obsidian`, backed by `paper_shadow_reconciliation.py`.
- Checks: required three lines are `reference_baseline`, `atr_reclaim_0_35_shadow`, and `research_incumbent`; report flags missing lines, `controls_paper=1`, decision mismatches, terminal maturity, and right-censored opportunities.
- Verification: `python tests\test_database.py`, `python -m compileall main.py src tests`, and real-db `python main.py paper shadow-reconciliation --no-obsidian` passed.
- Current real-db result: `no_shadow_samples_yet`, `decisions=0`, `opportunities=0`; report `reports/2026-07-30/paper_shadow_reconciliation_2026-07-30_demo_v1.md`.
- Decision: tooling is ready, but no `atr_reclaim_0_35` validity conclusion is available until shadow rows and mature terminal opportunities exist.

## 2026-07-30 paper shadow reconciliation auto-report

- Tooling change: `daily` and `paper cycle` now generate `paper_shadow_reconciliation` automatically after `paper_shadow_maturity_review`.
- Report-state fix: maturity/reconciliation reports now accept the current run id and display the in-progress current run as `success` for report context, matching the final tracked-run result after report generation.
- Verification: `python tests\test_database.py`, `python tests\test_paper_shadow_replay.py`, `python -m compileall main.py src tests`, and real-db `python main.py paper cycle --no-obsidian` passed.
- Real run: `20260730_111428_76a80af1` generated `paper_shadow_maturity_review_2026-07-30_demo_v9.md` and `paper_shadow_reconciliation_2026-07-30_demo_v2.md`; both show latest 4h run status=`success`.
- Current evidence: `paper_shadow_decisions` remains empty, so the result is still `no_shadow_samples_yet`; this is an automation readiness improvement, not a strategy validity result.

## 2026-07-30 paper shadow reconciliation sample gate

- Tooling change: `paper_shadow_reconciliation` now has a pre-attribution sample gate.
- Default gate: at least 10 complete three-line opportunities, 5 mature terminal opportunities, 3 independent symbols, `controls_paper rows=0`, and `incomplete opportunities=0`.
- Purpose: prevent one or two early terminal samples from being interpreted as a stable `atr_reclaim_0_35` signal.
- Verification: `python tests\test_database.py`, `python -m compileall main.py src tests`, and real-db `python main.py paper shadow-reconciliation --no-obsidian` passed.
- Current real-db result: `paper_shadow_reconciliation_2026-07-30_demo_v3.md` still has `no_shadow_samples_yet`, `decisions=0`, and gate current values all zero.
- Boundary: passing this gate only allows direct filtering / path-capacity attribution to begin; it is not deployment approval.

## 2026-07-30 atr_reclaim 2023-2024 repair branch frozen

- Decision cleanup: historical repair tasks for the `2023-07-01 -> 2024-07-01` `atr_reclaim_0_35` validation branch are now explicitly frozen in `TODO.md`.
- Scope frozen: listing/delisting enrichment, source-backed mapping for the 127 standard-like missing symbols, corrected N0/N1, and N2/N3/N4 historical master expansion.
- Reason: the project already decided `abandon_2023_2024_window_for_atr_reclaim_validation`; continuing this repair branch would consume engineering time without producing clean validation evidence for the current main line.
- Evidence retained: N0-N4 reports, historical master MVP, blocking review queue, and diagnostic conclusions remain useful as data-quality evidence.
- Boundary: these artifacts must not be used to keep, reject, or deploy `atr_reclaim_0_35`.
- Current main line: prospective shadow observation only; wait for normal daily/import or entry-zone 4h update to create `paper_shadow_decisions`.

## 2026-07-30 atr_reclaim prospective shadow runbook

- Artifact: `2026-07-30-atr-reclaim-prospective-shadow-runbook.md`.
- Purpose: define the operational decision tree after normal daily/cycle jobs produce or fail to produce shadow rows.
- Covered cases: no shadow rows, candidate-only rows, plan-linked but immature rows, missing required lines, accidental `controls_paper=1`, sample gate not reached, and attribution-ready state.
- Gate reminder: reconciliation ready only allows read-only attribution review; it does not authorize `atr_reclaim_0_35` deployment or `settings.toml` changes.
- Current state: `paper_shadow_decisions=[]`; action remains `wait_for_normal_daily_or_entry_zone_4h_trigger`.
## 2026-07-30 19:36 +08:00 - atr_reclaim prospective shadow runbook check

- Experiment/check: `atr_reclaim_prospective_shadow_runbook_check`.
- Question: after the approved global plan, have normal paper/shadow rows appeared so attribution can begin?
- Commands: `python main.py paper shadow-decisions --limit 20`, `python main.py paper shadow-maturity --no-obsidian`, `python main.py paper shadow-reconciliation --no-obsidian`, and `python main.py db status`.
- Result: `paper_shadow_decisions=[]`; generated `paper_shadow_maturity_review_2026-07-30_demo_v10.md` and `paper_shadow_reconciliation_2026-07-30_demo_v4.md`.
- Verdict: both reports are `no_shadow_samples_yet`; pre-attribution gate remains at 0 complete opportunities, 0 mature terminal opportunities, and 0 independent symbols.
- Decision: `operations_wait`; no direct filtering attribution, no capacity/path attribution, no `atr_reclaim_0_35` deployment, and no `config/settings.toml` change.
- Next action: wait for normal daily/import or `ONDOUSDT` entry-zone 4h decision to create prospective shadow rows, then rerun maturity and reconciliation.

## 2026-07-30 19:43 +08:00 - paper 4h scheduler observability check

- Experiment/check: `paper_4h_scheduler_observability_check`.
- Question: is the automatic 4h observation chain healthy enough to support prospective shadow observation?
- Evidence: Windows task `CryptoTrading_4H_PaperUpdate` showed `LastTaskResult=1` for the 16:10 run; `paper_4h_update.log` contained only the start line and no run_id or failure detail.
- Verification: manual execution of the same `scripts/paper_4h_update.bat` succeeded, creating run `20260730_114150_57deaf93`.
- Result: generated `paper_shadow_maturity_review_2026-07-30_demo_v11.md` and `paper_shadow_reconciliation_2026-07-30_demo_v5.md`; both still have verdict `no_shadow_samples_yet`.
- Tooling change: `scripts/run_logged_paper_task.ps1` now logs PowerShell-level exceptions through `trap` and checks that the configured Python interpreter exists before invoking the task.
- Decision: `operations_wait_with_improved_logging`; continue waiting for normal daily/import or entry-zone 4h samples, and inspect the next scheduled task run if it returns nonzero again.

## 2026-07-31 11:35 +08:00 - atr_reclaim prospective shadow candidate context check

- Experiment/check: `atr_reclaim_prospective_shadow_candidate_context_check`.
- Question: did overnight normal daily/import and 4h runs start producing prospective shadow rows, and are the three required lines structurally complete?
- Evidence: `CryptoTrading_DailyPaperUpdate` last result 0 at 2026-07-30 20:05; `CryptoTrading_4H_PaperUpdate` last result 0 at 2026-07-31 08:10; latest DB run `20260731_001002_b39e3bc4` success.
- Result: `paper_shadow_decisions` contains 15 candidate-level rows from daily run `20260730_120502_4a73a4c7`, covering 5 opportunities and all three lines: `reference_baseline`, `atr_reclaim_0_35_shadow`, and `research_incumbent`.
- Maturity report: `paper_shadow_maturity_review_2026-07-31_demo_v3.md`, verdict `candidate_context_only`, with 15 candidate-only rows and 0 plan-linked rows.
- Reconciliation report: `paper_shadow_reconciliation_2026-07-31_demo_v3.md`, verdict `reconciliation_waiting_for_terminal_outcomes`, complete opportunities 5/10, mature terminal opportunities 0/5, independent symbols 5/3, controls_paper rows 0, incomplete opportunities 0.
- Decision: `operations_wait_for_plan_linked_rows`; candidate-level logging is structurally working, but attribution is still blocked until plan-linked and mature terminal samples exist.
- Next action: wait for `ONDOUSDT` or later WATCHING plans to touch entry_high during a 4h paper update; do not deploy or tune `atr_reclaim_0_35`.
