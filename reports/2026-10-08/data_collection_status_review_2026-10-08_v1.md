# 数据收集与项目状态复核

检查时间：2026-10-08 23:45 +08:00。业务数据截止：2026-09-24 12:10:17 +08:00。

## 负责人结论

项目已经从“等待第一批成熟样本”推进到“数量达到初步归因门槛，但先核查采集缺口对样本的影响”。数据质量分级已恢复候选到计划的流转，已有数据有诊断价值；当前尚不能据此验证盈利能力或部署 ATR 0.35。没有运行新回测、A/B、实时扫描或 paper update，没有修改业务数据库或策略配置。

## 研究口径

- 系统目标：验证可解释、可复核的研究与模拟盘链路，最终判断是否存在稳定交易优势。
- 本次唯一问题：8 月 16 日后的非连续采集是否推进了上次 observation epoch，现有样本能支持什么判断？
- 路线位置：既有七天 observation epoch 的状态复核；不是新的参数实验。
- 事实：以下数据库计数、历史报告和源码行为。
- 观察：降级候选可进入 plan，终态数已超过最低门槛；采集中断与请求跳过仍存在。
- 待验证假设：停机期间可能遗漏止损、止盈或入场事件，改变现有 terminal/PnL；尚未重建历史路径，不能断言每笔结果都错误。
- 决定：retest；保留原始记录，继续冻结策略变更，先审计缺口，再解释 0.35 的过滤贡献。没有批准或启动新实验。

## 新增数据：2026-08-16 至业务数据截止

| 项目 | 数量 |
|---|---:|
| successful daily / scans | 18 |
| daily failed / stale running | 3 / 1 |
| successful 4h runs / stale running | 109 / 1 |
| scan candidates | 90 |
| CLEAN / DEGRADED / BLOCKED candidates | 6 / 67 / 17 |
| BUY_CANDIDATE | 40 |
| CLEAN BUY / DEGRADED BUY | 1 / 39 |
| PLAN_CREATED | 40 |
| data_quality_blocked import decisions | 17 |
| API_DELAY_SKIPPED plan events | 93 |

40 个允许导入的候选全部产生新计划；17 个 BLOCKED 候选全部被 import 阻断。该窗口没有“有 BUY 却漏建计划”的证据。BLOCKED 不等于 17 个原本都符合买入条件。质量 issue 表包含更广验证池与多条 issue，不能将 issue 条数当作最终候选数量。

非阻断 issue 包括 CMC/CG identity ambiguous 和 CG rate limited；阻断 issue 包括 Binance extreme range 与 external 24h difference。说明分级路径有真实执行证据，尚未逐个证明 provider 身份或阈值准确性；同期市场也从 RISK_OFF/NEUTRAL 转向 RISK_ON，不能将 BUY 增加全部归因于数据修复。

## 连续性

- 2026-08-16–08-28：13 天每天 1 次 daily、5 次 4h 均记录 success；原定 08-16–08-22 七日窗口已采到 35 个候选、8 个 BUY/新计划（CLEAN BUY=1、DEGRADED BUY=7；BLOCKED=12）。但 08-18 有 2 次 plan-level API skip，不能直接称为零缺失的清洁窗口。
- API skip 分布：08-18=2，08-25=7，08-27=9，09-09=75。93 是逐计划事件数，不是 93 次任务失败。
- 完全没有 run 记录的整日区间：08-29–09-02、09-11–09-21、09-25–10-07。09-03 有两条至今为 running 的未收尾任务，也产生过部分业务事件，不能把该日全部当作无数据。
- 相邻成功 4h 的大空档：08-28 16:10 → 09-04 00:10，约 152 小时；09-10 04:10 → 09-22 00:10，约 284 小时。该口径是成功任务间隔，不代表期间绝无业务写入。
- 成功 daily 空档：08-28 → 09-05（约 8 天）；09-07 → 09-22（约 15 天）。09-04/08/09 的 daily 分别因 timeout/SSL 请求错误失败。
- 最新 daily：09-23 20:05；最新 4h：09-24 12:10（北京时间）。10-08 22:55 两项调度任务均返回 3221225786（0xC000013A），daily 日志仅见 start；当前未证明已恢复。未诊断是手动终止、关机或其他原因。

## 样本成熟度：比较上次与最新报告

| 指标 | 08-16 v1 | 09-24 v4 |
|---|---:|---:|
| decisions（重复观察行，非交易数） | 318 | 1404 |
| complete opportunities | 56 | 174 |
| independent symbols | 25 | 45 |
| mature terminal opportunities | 0 | 15 |
| incomplete opportunities | 0 | 0 |
| controls_paper rows | 0 | 0 |

最新 reconciliation verdict=`reconciliation_ready_for_attribution`，数量门槛确实已满足（10 opportunities / 5 terminal / 3 symbols）。但 15 个 terminal 由 7 ARCHIVED、4 CLOSED、4 STOPPED 组成；只有 8 个已入场后退出的计划。4 STOPPED 均为 EMA_TRAILING_STOPPED，账面 realized_pnl 为正，不能将 STOPPED 一概算亏损。

全体新增计划状态：ARCHIVED=19、CLOSED=4、STOPPED=4、ENTERED=3、TP1_HIT=1、WATCHING=9。新增计划与 shadow plan-linked 子集不同；有些计划在首次 4h 决策前已被替换。包括旧 ONDO 在内，当前 shadow linked open plans=14，实际持仓 4 个、WATCHING 10 个。

8 个已退出计划为 UNI、ETH（两笔）、TAO、ADA、BNB、DOGE、BTC，均跨越上述至少一段采集中断。paper_trader.py 以当前 ticker 价格传入 step_trade 的 high/low/close；counterfactual 每次使用最新闭合 4h bar，不逐根补走遗漏区间。因此终态和账面 PnL 只能视作间断观察结果，不能计算可信的完整前向胜率、PF、Sharpe、最大回撤或净收益。

另有值得后续核查的机制事实：plan-level baseline accept=12，而 atr_reclaim_0_35_shadow 和 research_incumbent accept=0；12 次分歧的 0.35 reject 原因均为 close below entry_high + 0.35 ATR。报告 mismatch=12 指三线决策差异，不是 12 处数据库损坏。它不代表独立 0.35 组合必然没有任何交易；后续时点、入场路径和容量仍需独立归因。

## 验证与下一步

SQLite 通过 mode=ro 连接；PRAGMA quick_check=ok，foreign_key_check 无行。交叉核对 market_scans、runs、paper_plans、paper_events、candidate observations、funnel events、shadow decisions，及最新成熟度/对账报告。未下载行情、未修改历史状态、未启动新的实验。

1. 先检查 10-08 调度中断，恢复既有 daily/4h 采集并验证后续业务写入；不要仅看 scheduler Ready。
2. 对 8 个跨空档已退出计划与 4 个未平仓计划做独立缺口审计；不能自动覆盖原始 paper 结果或补造前向样本。
3. 完成已有 observation epoch 的正式质量/漏斗验收，再对有效样本解释三线 direct filtering 与 capacity/path；保留 0.35 冻结、TP1 卡片 gated_not_approved。

证据：reports/2026-08-16/paper_shadow_reconciliation_2026-08-16_demo_v1.md；reports/2026-09-24/paper_shadow_reconciliation_2026-09-24_demo_v4.md；reports/2026-09-24/paper_shadow_maturity_review_2026-09-24_demo_v4.md；data/crypto_trading.db（本地只读，不提交）。
