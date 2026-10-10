# Taskboard 待认领任务移至待立项

2026-10-10 09:02:51 +08:00

用户要求将待认领中的所有任务移至待立项。本次 93 条 todo 已全部移至 backlog，复查 todo=0。保留原优先级、内容与其他状态任务。

| 任务 | 原状态 | 新状态 | 标题 |
|---|---|---|---|
| CRYPTOTRADIN-119 | todo | backlog | [开发计划.md:511] Walk-forward 市场环境分层分析。 |
| CRYPTOTRADIN-118 | todo | backlog | [TODO.md:145] TP1 触达后将止损移动到保本价。 |
| CRYPTOTRADIN-117 | todo | backlog | [开发计划.md:526] Telegram 或邮件提醒。 |
| CRYPTOTRADIN-116 | todo | backlog | [开发计划.md:554] Open interest。 |
| CRYPTOTRADIN-115 | todo | backlog | [开发计划.md:552] OKX / Bybit 行情对照。 |
| CRYPTOTRADIN-114 | todo | backlog | [TODO.md:41] gate 已达数量门槛（10-08 为15，10-09 12:11 为16 terminal，其中7 ARCHIVED）；按顶部 G0–G2 先验执行与证据质量，再推进收益归因。保持 ATR 冻结及 TP1 实验未批准。 |
| CRYPTOTRADIN-113 | todo | backlog | [开发计划.md:556] ETF / 宏观风险指标。 |
| CRYPTOTRADIN-112 | todo | backlog | [开发计划.md:529] API 异常或数据源异常提醒。 |
| CRYPTOTRADIN-110 | todo | backlog | [TODO.md:118] A/B 测试更严格的追高规则：对 24h 强涨后远离支撑的币进行排除或降级。 |
| CRYPTOTRADIN-109 | todo | backlog | [开发计划.md:518] A/B 报告写入 Obsidian `Reports/YYYY-MM-DD/`。 |
| CRYPTOTRADIN-108 | todo | backlog | [开发计划.md:546] 最大日亏损熔断。 |
| CRYPTOTRADIN-107 | todo | backlog | [开发计划.md:545] 最大单笔下单额限制。 |
| CRYPTOTRADIN-106 | todo | backlog | [开发计划.md:547] 自动撤单和订单重试。 |
| CRYPTOTRADIN-105 | todo | backlog | [开发计划.md:553] 资金费率。 |
| CRYPTOTRADIN-103 | todo | backlog | [开发计划.md:543] 只读 / 交易权限分离。 |
| CRYPTOTRADIN-102 | todo | backlog | [TODO.md:205] 正式 keep `risk_off_no_core_entry_reclaim_ema_stop`：将三项 override（`risk_off_core_buy_enabled=false`、`entry_reclaim_close_enabled=true`、`tp1_ema_trailing_stop_enabled=tr… |
| CRYPTOTRADIN-101 | todo | backlog | [开发计划.md:519] 增加实验结论索引页。 |
| CRYPTOTRADIN-100 | todo | backlog | [开发计划.md:521] 增加每周策略复盘笔记模板。 |
| CRYPTOTRADIN-99 | todo | backlog | [开发计划.md:520] 增加交易复盘模板。 |
| CRYPTOTRADIN-98 | todo | backlog | [开发计划.md:522] 增加策略参数变更历史表。 |
| CRYPTOTRADIN-97 | todo | backlog | [TODO.md:251] 暂不把 MACD 升级为 `macd_hist_4h > 0` 硬门槛；如研究 MACD，仅做 histogram 斜率、连续恶化、reclaim 时改善等离线变体。 |
| CRYPTOTRADIN-96 | todo | backlog | [TODO.md:71] 在连续新增至少 7 个自然日数据后复跑 funnel audit，确认 `ticker_error` / `kline_error` 是否仍为主要断点。 |
| CRYPTOTRADIN-95 | todo | backlog | [TODO.md:156] 在 K 线缓存足够热之后，不使用 `--source-limit` 跑更大的 dynamic-universe A/B 实验。 |
| CRYPTOTRADIN-94 | todo | backlog | [TODO.md:271] 优先补齐 listing-date enriched `SymbolMaster` 或历史 membership 证据，然后重跑 N0；当前 `listing_dates_present=false`，第三窗口只能作为 diagnostic，不能作为 clean confirmatory validation。 |
| CRYPTOTRADIN-93 | todo | backlog | [开发计划.md:501] 引入历史/退市币 symbol master，降低当前 `exchangeInfo` 带来的退市幸存者偏差。 |
| CRYPTOTRADIN-92 | todo | backlog | [TODO.md:58] 以新 validation policy 开启 observation epoch，连续收集至少 7 个自然日数据。 |
| CRYPTOTRADIN-91 | todo | backlog | [开发计划.md:510] 移除或继续提高 `--source-limit` 复测 `liquidity_50m`。 |
| CRYPTOTRADIN-90 | todo | backlog | [TODO.md:138] 要求 RSI 出现恢复，例如从 45-55 区间重新向上。 |
| CRYPTOTRADIN-89 | todo | backlog | [TODO.md:157] 研究 Binance 历史/退市币 symbol master list，降低 dynamic universe 回测中的退市幸存者偏差。 |
| CRYPTOTRADIN-83 | todo | backlog | [开发计划.md:555] 稳定币流动性。 |
| CRYPTOTRADIN-82 | todo | backlog | [开发计划.md:541] 手动确认后下单。 |
| CRYPTOTRADIN-81 | todo | backlog | [开发计划.md:537] 收益曲线和回撤曲线。 |
| CRYPTOTRADIN-80 | todo | backlog | [TODO.md:40] 收口原 08-16–08-22 observation epoch 验收：该周任务记录齐全，但有 2 个 API skip；核查 35 candidates / 8 plans / 12 BLOCKED 的完整证据。 |
| CRYPTOTRADIN-79 | todo | backlog | [开发计划.md:490] 实现三段式历史结构。 |
| CRYPTOTRADIN-78 | todo | backlog | [开发计划.md:491] 实现趋势相关高波动惩罚实验。 |
| CRYPTOTRADIN-77 | todo | backlog | [开发计划.md:544] 实盘开关。 |
| CRYPTOTRADIN-76 | todo | backlog | [TODO.md:38] 审计 09-24 截止时的另 4 个持仓计划（TRX/ZRO/AAVE/SOL）；10-09 00:10 ZRO 已由自动任务转为 STOPPED，仍属于待审计 cohort，其他 3 个仍 ENTERED。 |
| CRYPTOTRADIN-72 | todo | backlog | [TODO.md:36] 确认 daily 下一次自动运行正常（最近仍为 10-08 的非零返回），并继续观察 4h 的连续运行健康。 |
| CRYPTOTRADIN-71 | todo | backlog | [TODO.md:28] 配对路径与采集可信后再做净收益和容量贡献归因；当前 `retest / insufficient_paired_forward_evidence`，ATR 保持冻结。 |
| CRYPTOTRADIN-70 | todo | backlog | [开发计划.md:512] 牛市、熊市、震荡、暴跌、周末分层统计。 |
| CRYPTOTRADIN-69 | todo | backlog | [开发计划.md:528] 模拟盘入场、止损、止盈触发提醒。 |
| CRYPTOTRADIN-67 | todo | backlog | [TODO.md:47] 每日运行 `python main.py db status`、`python main.py paper db-summary --limit 20`、`python main.py paper shadow-maturity --no-obsidian` 和 `python main.py paper shadow-recon… |
| CRYPTOTRADIN-66 | todo | backlog | [TODO.md:46] 每日记录观察表：daily/4h 运行健康、`CLEAN / DEGRADED / BLOCKED`、`BUY_CANDIDATE`、`PLAN_CREATED`、`skipped_data_quality`、RISK 状态和 mature terminal。 |
| CRYPTOTRADIN-65 | todo | backlog | [TODO.md:161] 每份实验报告使用清晰的规则名和版本号保存。 |
| CRYPTOTRADIN-64 | todo | backlog | [TODO.md:158] 每次实验只改变一个策略维度。 |
| CRYPTOTRADIN-63 | todo | backlog | [TODO.md:159] 每次实验使用同一个 symbol universe 和同一个日期区间。 |
| CRYPTOTRADIN-62 | todo | backlog | [TODO.md:162] 每次实验保留简短决策说明：应该保留、回滚还是继续复测。 |
| CRYPTOTRADIN-61 | todo | backlog | [TODO.md:139] 拒绝主要由放量下跌驱动的形态。 |
| CRYPTOTRADIN-60 | todo | backlog | [开发计划.md:548] 交易所故障处理。 |
| CRYPTOTRADIN-59 | todo | backlog | [开发计划.md:542] 交易所 API Key 权限隔离。 |
| CRYPTOTRADIN-58 | todo | backlog | [TODO.md:117] 将历史长度逻辑拆成三段式：`min_indicator_history_days`、极短历史硬拒绝、短历史扣分。 |
| CRYPTOTRADIN-57 | todo | backlog | [开发计划.md:492] 将被 keep 的规则单独合并到默认配置。 |
| CRYPTOTRADIN-56 | todo | backlog | [开发计划.md:488] 将 `max_holding_42x4h_no_tp1` 与 sensitive 组合合并，验证叠加效果。 |
| CRYPTOTRADIN-55 | todo | backlog | [开发计划.md:533] 简单 Web 仪表盘。 |
| CRYPTOTRADIN-52 | todo | backlog | [开发计划.md:536] 回测和 A/B 实验结果视图。 |
| CRYPTOTRADIN-51 | todo | backlog | [TODO.md:92] 后续如继续 entry-quality 研究，只允许提出单变量 retest 卡片；不得把 `atr_reclaim_0_35` 与 replacement、relative strength 或其它过滤器叠加后直接实验。 |
| CRYPTOTRADIN-50 | todo | backlog | [TODO.md:278] 构建 listing-date enriched `SymbolMaster` 或历史 membership 证据，然后重跑 N0。 |
| CRYPTOTRADIN-49 | todo | backlog | [开发计划.md:514] 更细 intrabar 数据裁决，例如 15m 或 5m。 |
| CRYPTOTRADIN-48 | todo | backlog | [TODO.md:279] 改进 opportunity alignment：为 baseline/variant 输出 strict opportunity id、capacity state at decision 和 direct filtered/retained event export，避免把 path/capacity timing 误判为 … |
| CRYPTOTRADIN-47 | todo | backlog | [TODO.md:59] 复核 degraded 候选的身份不确定比例、plan 创建率和后续 terminal 结果；不得把 BUY 数量增加直接作为策略成功结论。 |
| CRYPTOTRADIN-46 | todo | backlog | [TODO.md:160] 对比净收益、最大回撤、胜率、Profit factor、平均 R、止损率和交易次数。 |
| CRYPTOTRADIN-45 | todo | backlog | [TODO.md:148] 对比固定 TP2 和趋势跟踪退出规则。 |
| CRYPTOTRADIN-44 | todo | backlog | [开发计划.md:500] 对 promising 的 dynamic-universe 结果做跨时段复测。 |
| CRYPTOTRADIN-43 | todo | backlog | [开发计划.md:489] 对 A/B 报告写人工结论；当前第一批均应暂记 `retest`，不能 keep。 |
| CRYPTOTRADIN-42 | todo | backlog | [TODO.md:227] 冻结当前 `settings.toml`，继续 daily + 4h 至少观察 2 周；除非出现明确红线，不修改策略参数或 paper 状态机。 |
| CRYPTOTRADIN-36 | todo | backlog | [开发计划.md:535] 当前模拟盘持仓视图。 |
| CRYPTOTRADIN-35 | todo | backlog | [开发计划.md:534] 当前候选币视图。 |
| CRYPTOTRADIN-33 | todo | backlog | [TODO.md:72] 单独审计 terminal plan 与 shadow observation 的关联缺口；不得放宽 maturity gate 或将 candidate outcome 伪装成 plan-level outcome。 |
| CRYPTOTRADIN-32 | todo | backlog | [开发计划.md:527] 大盘风险变化提醒。 |
| CRYPTOTRADIN-31 | todo | backlog | [TODO.md:137] 测试更靠近 `entry_low` 的入场方式，而不是默认按 `entry_high` 附近成交。 |
| CRYPTOTRADIN-30 | todo | backlog | [TODO.md:147] 测试 TP1 后使用 ATR 跟踪止损。 |
| CRYPTOTRADIN-29 | todo | backlog | [TODO.md:146] 测试 TP1 后使用 4h EMA20 跟踪止损。 |
| CRYPTOTRADIN-28 | todo | backlog | [TODO.md:144] 测试 TP1 部分止盈，例如 TP1 卖出 50%。 |
| CRYPTOTRADIN-27 | todo | backlog | [TODO.md:149] 测试 ATR 动态止损，替代单纯结构固定止损。 |
| CRYPTOTRADIN-26 | todo | backlog | [TODO.md:140] 避免在 4h 趋势仍明显向下时接飞刀。 |
| CRYPTOTRADIN-25 | todo | backlog | [TODO.md:216] 3 周 paper 观察期结束后，优先评估固定 `max_holding_bars_without_tp1=42` 是否写入默认 `settings.toml`；须先确认 db stability 5 天稳定窗口空闲，并结合模拟盘持仓时长与 TIME_EXIT 案例人工复盘。 |
| CRYPTOTRADIN-24 | todo | backlog | [开发计划.md:86] 2026-08-22 后才做 observation epoch 决策： |
| CRYPTOTRADIN-23 | todo | backlog | [开发计划.md:85] 2026-08-19 和 2026-08-22 执行 `python main.py paper shadow-funnel-audit --account demo --days 7 --no-obsidian`，比较新的 `ticker_error`、`kline_error`、`skipped_data_quality` 和… |
| CRYPTOTRADIN-22 | todo | backlog | [开发计划.md:80] 2026-08-16 至 2026-08-22 每个自然日记录 daily/4h 健康、`CLEAN / DEGRADED / BLOCKED`、`BUY_CANDIDATE`、`PLAN_CREATED`、`skipped_data_quality`、RISK 状态和 mature terminal。每日执行： |
| CRYPTOTRADIN-21 | todo | backlog | [TODO.md:219] 2026-07-02 模拟盘复盘决策：根据 3 周观察结果（entry_reclaim 拦截次数、RISK_OFF 频率、现有持仓 WLDUSDT/ONDOUSDT 结果）决定 sensitive 组合是 keep、调参还是继续观察。 |
| CRYPTOTRADIN-20 | todo | backlog | [TODO.md:15] **P1**：明确 paper/shadow 的账户现金、仓位和容量约束范围；完整组合账本未完成时，只认证单计划诊断，capacity contribution 保持 n/a。 |
| CRYPTOTRADIN-19 | todo | backlog | [TODO.md:18] **P1 / 10-21–10-22**：完成 G0 正确性 / G1 运行连续性 / G2 研究可回答性裁决；前向样本不足则继续观察，不放宽门槛。 |
| CRYPTOTRADIN-18 | todo | backlog | [TODO.md:16] **P1 / 10-16–10-20**：冻结修复后的执行版本，收集新 epoch；目标至少 7 个完整自然日的 7 daily + 35 scheduled 4h，以及逐计划有效评价/skip 对账；执行版本改变则重新起算。 |
| CRYPTOTRADIN-17 | todo | backlog | [TODO.md:17] **P1 / 10-16–10-20**：按预声明协议审计固定历史案例的实现修复影响；建立实验 registry，记录 hash、master、窗口、成本和试验家族，旧窗口统一标 diagnostic。 |
| CRYPTOTRADIN-11 | todo | backlog | [TODO.md:8] **P0 / 10-09–10-10**：冻结代码/配置/数据/执行语义基线，收口 08-16–08-22 旧 epoch；完成 TRX/ZRO/AAVE/SOL 四笔固定 cohort 缺口审计。 |
| CRYPTOTRADIN-9 | todo | backlog | [TODO.md:50] **2026-08-22 后完成 observation epoch 决策**：若数据健康且 mature terminal 仍为 0，再提交 TP1 实验卡片审批；若发现数据/状态机问题，先修复并重启 observation epoch；若 mature terminal 开始快速增加，优先完成 `reference_basel… |
| CRYPTOTRADIN-8 | todo | backlog | [TODO.md:60] **2026-08-22 后核查数据质量分级是否正常**：统计新 observation epoch 中 `CLEAN / DEGRADED / BLOCKED` 候选、`BUY_CANDIDATE`、`PLAN_CREATED` 和 `skipped_data_quality`；确认 CMC 多匹配、429/暂时不可用等非致命 … |
| CRYPTOTRADIN-6 | todo | backlog | [TODO.md:306] ???????????????? A/B?? prospective shadow observation ???????? |
| CRYPTOTRADIN-5 | todo | backlog | [TODO.md:296] ???? blocking review queue????? `months_in_window_count=12` ? last_kline_month ????? symbols?????????????????????? current exchangeInfo ????? |
| CRYPTOTRADIN-4 | todo | backlog | [TODO.md:297] ?? official-source mapping ???????? blocking symbol ?? `source_url / source_type / mapped_to / delisting_time / confidence / notes`? |
| CRYPTOTRADIN-3 | todo | backlog | [TODO.md:285] ?? historical symbol membership dataset??? `listing_time / delisting_time / first_kline_time / last_kline_time / tradable_from / tradable_to / source / confidence`??… |
| CRYPTOTRADIN-2 | todo | backlog | [TODO.md:291] ? historical master ??? `listing_time / delisting_time / first_kline_time / last_kline_time / tradable_from / tradable_to / source / confidence`? |
| CRYPTOTRADIN-1 | todo | backlog | [TODO.md:290] ? 127 ? standard-like missing symbols ?? source-backed mapping??? true delisted?rename/migration?base replacement?????????????????? |
