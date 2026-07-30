# CryptoTradingSystem 实验账本

更新时间：2026-07-27 23:57 +08:00

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

