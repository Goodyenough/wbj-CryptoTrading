---
created: 2026-06-23 16:10:09 CST
tags:
  - crypto
  - trading-system
  - paper-trading
account: demo
report_version: v1
---

# 模拟盘报告 demo v1

- 报告时间：2026-06-23 16:10:09 CST
- Run ID：`20260623_081005_343b2207`
- Run type：`paper_4h_update`
- 数据来源：SQLite
- 报告版本：v1
- 模拟账户权益基准：10,000.00 USDT
- 单笔计划风险：1.00%
- 开放交易/观察：2
- 已结束交易：23
- 已实现 PnL：-700.00 USDT
- 未实现 PnL：92.49 USDT
- 已入场交易数：8
- 胜率：0.00%
- TP1 命中率：0.00%

## 今日大盘环境

- **状态：RISK_OFF** — BTC/ETH 大盘偏弱，山寨币买入候选降级为观察。
- BTC 7d 涨跌：-4.34% ⚠ 低于阈值 -3.0%（阈值 -3.0%）
- ETH 7d 涨跌：-6.24% ⚠ 低于阈值 -5.0%（阈值 -5.0%）
- BTC 日线趋势：✗ 趋势未确认
- ETH 日线趋势：✗ 趋势未确认
- require_both_trend：是

## 复盘统计

| Metric | Value |
|---|---:|
| Total plans | 25 |
| Open watching/positions | 2 |
| Entered trades | 8 |
| Closed trades | 23 |
| Winning closed trades | 0 |
| Losing closed trades | 7 |
| Win rate | 0.00% |
| TP1 hit rate | 0.00% |
| Realized PnL | -700.00 USDT |
| Unrealized PnL | 92.49 USDT |
| Entry reclaim blocks | 37 |
| Avg holding time | 571.8h |
| TP1 EMA trailing activated | 0 |
| TP1 EMA trailing raises | 0 |
| TP1 EMA trailing stops | 0 |
| TP1 EMA trailing active trades | 0 |
| This run events | 1 |
| This run API delay skipped | 0 |

## Entry Reclaim 后续追踪

| Symbol | Status | Pending Events | First Pending | Last Pending | Outcome | Detail |
|---|---|---:|---|---|---|---|
| `ONDOUSDT` | WATCHING | 37 | 2026-06-11 20:47:37 CST | 2026-06-23 16:10:09 CST | still_waiting | Watching: entry zone touched, but 4h close has not reclaimed entry_high. |

## TP1 EMA Trailing Stop 追踪

| Metric | Value |
|---|---:|
| Activated events | 0 |
| Stop raise events | 0 |
| Stop exits from EMA trailing | 0 |
| Currently active trades | 0 |

## 本次 Run 状态变化

| Time | Event | Symbol | Old Status | New Status | Price | Old Stop | New Stop | Kline Time | Reason |
|---|---|---|---|---|---:|---:|---:|---|---|
| 2026-06-23 16:10:09 CST | RECLAIM_PENDING_SET | `ONDOUSDT` | WATCHING | WATCHING | 0.31670 | 0.33845 | 0.33845 | 2026-06-23T07:59:59Z | Entry zone touched (price=0.31670) but 4h close 0.31450 < entry_high 0.41157; waiting for reclaim. |

## 当前观察与持仓

| Status | Symbol | Last | Entry Zone | Entry | Stop | TP1 | TP2 | Qty | Unrealized | Notes |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| ENTERED | `WLDUSDT` | 0.58910 | 0.43071 - 0.46770 | 0.45830 | 0.31687 | 0.71386 | 0.84619 | 707.09 | 92.49 | Paper entry triggered inside entry zone. |
| WATCHING | `ONDOUSDT` | 0.31670 | 0.39450 - 0.41157 | n/a | 0.33845 | 0.53222 | 0.59681 | n/a | 0.00 | Watching: entry zone touched, but 4h close has not reclaimed entry_high. |

## 已结束交易

| Status | Symbol | Entry | Exit | Qty | Realized PnL | Source Scan | Notes |
|---|---|---:|---:|---:|---:|---|---|
| STOPPED | `ZECUSDT` | 597.81 | 518.76 | 1.27 | -100.00 | 7a562bac13ec | Stop loss hit. |
| INVALIDATED | `NEARUSDT` | n/a | 1.9710 | n/a | 0.00 | 7a562bac13ec | Plan invalidated before entry: current price is below stop loss. |
| INVALIDATED | `PORTALUSDT` | n/a | 0.01492 | n/a | 0.00 | 7a562bac13ec | Plan invalidated before entry: current price is below stop loss. |
| ARCHIVED | `NEARUSDT` | n/a | n/a | n/a | 0.00 | c2d8a8204b8a | Archived because scan 7a562bac13ec created a newer WATCHING plan for NEARUSDT. |
| ARCHIVED | `ZECUSDT` | n/a | n/a | n/a | 0.00 | c2d8a8204b8a | Archived because scan 7a562bac13ec created a newer WATCHING plan for ZECUSDT. |
| ARCHIVED | `ONDOUSDT` | n/a | n/a | n/a | 0.00 | c2d8a8204b8a | Archived because scan 7a562bac13ec created a newer WATCHING plan for ONDOUSDT. |
| INVALIDATED | `TRXUSDT` | n/a | 0.33220 | n/a | 0.00 | c2d8a8204b8a | Plan invalidated before entry: current price is below stop loss. |
| STOPPED | `TONUSDT` | 1.9770 | 1.8311 | 685.47 | -100.00 | c2d8a8204b8a | Stop loss hit. |
| ARCHIVED | `NEARUSDT` | n/a | n/a | n/a | 0.00 | 5e1db9afc001 | Archived because scan c2d8a8204b8a created a newer WATCHING plan for NEARUSDT. |
| ARCHIVED | `ZECUSDT` | n/a | n/a | n/a | 0.00 | 5e1db9afc001 | Archived because scan c2d8a8204b8a created a newer WATCHING plan for ZECUSDT. |
| STOPPED | `ONDOUSDT` | 0.36110 | 0.32820 | 3,039.70 | -100.00 | 5e1db9afc001 | Stop loss hit. |
| ARCHIVED | `TRXUSDT` | n/a | n/a | n/a | 0.00 | 5e1db9afc001 | Archived because scan c2d8a8204b8a created a newer WATCHING plan for TRXUSDT. |
| ARCHIVED | `TONUSDT` | n/a | n/a | n/a | 0.00 | 5e1db9afc001 | Archived because scan c2d8a8204b8a created a newer WATCHING plan for TONUSDT. |
| ARCHIVED | `NEARUSDT` | n/a | n/a | n/a | 0.00 | a0af416b7052 | Archived because scan 5e1db9afc001 created a newer WATCHING plan for NEARUSDT. |
| ARCHIVED | `ZECUSDT` | n/a | n/a | n/a | 0.00 | a0af416b7052 | Archived because scan 5e1db9afc001 created a newer WATCHING plan for ZECUSDT. |
| STOPPED | `ONDOUSDT` | 0.36190 | 0.32820 | 2,967.54 | -100.00 | a0af416b7052 | Stop loss hit. |
| ARCHIVED | `TRXUSDT` | n/a | n/a | n/a | 0.00 | a0af416b7052 | Archived because scan 5e1db9afc001 created a newer WATCHING plan for TRXUSDT. |
| STOPPED | `TONUSDT` | 1.9710 | 1.8311 | 714.87 | -100.00 | a0af416b7052 | Stop loss hit. |
| STOPPED | `ZECUSDT` | 553.89 | 489.02 | 1.54 | -100.00 | 644f2c98e0a5 | Stop loss hit. |
| ARCHIVED | `NEARUSDT` | n/a | n/a | n/a | 0.00 | 644f2c98e0a5 | Archived because scan 5e1db9afc001 created a newer WATCHING plan for NEARUSDT. |
| ARCHIVED | `ONDOUSDT` | n/a | n/a | n/a | 0.00 | 644f2c98e0a5 | Archived because scan 5e1db9afc001 created a newer WATCHING plan for ONDOUSDT. |
| ARCHIVED | `TRXUSDT` | n/a | n/a | n/a | 0.00 | 644f2c98e0a5 | Archived because scan 5e1db9afc001 created a newer WATCHING plan for TRXUSDT. |
| STOPPED | `TONUSDT` | 1.9710 | 1.8311 | 714.87 | -100.00 | 644f2c98e0a5 | Stop loss hit. |

## 交易生命周期

### ZECUSDT `bf97525097f3`

- 当前状态：`STOPPED`
- 来源扫描：`7a562bac13ec` rank 1

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-06-03 20:11:39 CST | WATCHLIST_ADDED | 599.60 | n/a | 0.00 | 0.00 | Imported rank 1 from scan 7a562bac13ec; entry zone 578.56138-600.19857. |
| 2026-06-03 20:11:45 CST | ENTERED | 597.81 | 1.27 | 0.00 | 0.00 | Paper entry triggered at 597.81; quantity 1.2650237. |
| 2026-06-11 11:36:50 CST | STOPPED | 518.76 | 1.27 | -100.00 | 0.00 | Stop loss hit at 518.7601. |

### WLDUSDT `616e1bbfd4c6`

- 当前状态：`ENTERED`
- 来源扫描：`7a562bac13ec` rank 2

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-06-03 20:11:39 CST | WATCHLIST_ADDED | 0.49690 | n/a | 0.00 | 0.00 | Imported rank 2 from scan 7a562bac13ec; entry zone 0.43070929-0.46769821. |
| 2026-06-11 11:36:50 CST | ENTERED | 0.45830 | 707.09 | 0.00 | 0.00 | Paper entry triggered at 0.4583; quantity 707.08606. |

### NEARUSDT `86dd0c09db92`

- 当前状态：`INVALIDATED`
- 来源扫描：`7a562bac13ec` rank 3

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-06-03 20:11:39 CST | WATCHLIST_ADDED | 2.9580 | n/a | 0.00 | 0.00 | Imported rank 3 from scan 7a562bac13ec; entry zone 2.6609857-2.8269643. |
| 2026-06-11 11:36:50 CST | INVALIDATED | 1.9710 | n/a | 0.00 | 0.00 | Plan invalidated before entry: current price is below stop loss. |

### ONDOUSDT `9734a33dea2e`

- 当前状态：`WATCHING`
- 来源扫描：`7a562bac13ec` rank 4

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-06-03 20:11:39 CST | WATCHLIST_ADDED | 0.41690 | n/a | 0.00 | 0.00 | Imported rank 4 from scan 7a562bac13ec; entry zone 0.394505-0.41156786. |
| 2026-06-11 20:47:37 CST | RECLAIM_PENDING | 0.34570 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34570) but 4h close 0.34910 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-11 23:06:26 CST | RECLAIM_PENDING | 0.34620 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34620) but 4h close 0.34910 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-12 20:06:50 CST | RECLAIM_PENDING | 0.36700 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36700) but 4h close 0.36620 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-13 20:06:37 CST | RECLAIM_PENDING_SET | 0.36720 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36720) but 4h close 0.36720 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-14 20:06:28 CST | RECLAIM_PENDING_SET | 0.35550 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.35550) but 4h close 0.35650 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-15 20:06:35 CST | RECLAIM_PENDING_SET | 0.38070 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38070) but 4h close 0.38320 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-16 20:06:52 CST | RECLAIM_PENDING_SET | 0.38400 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38400) but 4h close 0.38470 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-18 20:07:19 CST | RECLAIM_PENDING_SET | 0.36080 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36080) but 4h close 0.36230 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-19 00:10:07 CST | RECLAIM_PENDING_SET | 0.36030 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36030) but 4h close 0.35640 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-19 04:10:05 CST | RECLAIM_PENDING_SET | 0.35920 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.35920) but 4h close 0.35710 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-19 08:10:07 CST | RECLAIM_PENDING_SET | 0.36450 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36450) but 4h close 0.36640 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-19 12:10:09 CST | RECLAIM_PENDING_SET | 0.35930 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.35930) but 4h close 0.35800 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-19 16:10:07 CST | RECLAIM_PENDING_SET | 0.35020 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.35020) but 4h close 0.34910 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-19 20:07:10 CST | RECLAIM_PENDING_SET | 0.34870 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34870) but 4h close 0.34870 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-20 00:10:12 CST | RECLAIM_PENDING_SET | 0.35390 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.35390) but 4h close 0.35490 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-20 04:10:04 CST | RECLAIM_PENDING_SET | 0.35030 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.35030) but 4h close 0.34960 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-20 08:10:05 CST | RECLAIM_PENDING_SET | 0.35420 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.35420) but 4h close 0.35570 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-20 12:10:06 CST | RECLAIM_PENDING_SET | 0.34940 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34940) but 4h close 0.35010 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-20 16:10:08 CST | RECLAIM_PENDING_SET | 0.35030 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.35030) but 4h close 0.35050 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-20 20:07:11 CST | RECLAIM_PENDING_SET | 0.34860 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34860) but 4h close 0.34790 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-21 00:10:28 CST | RECLAIM_PENDING_SET | 0.34250 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34250) but 4h close 0.34440 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-21 04:10:04 CST | RECLAIM_PENDING_SET | 0.33880 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33880) but 4h close 0.33890 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-21 08:10:04 CST | RECLAIM_PENDING_SET | 0.34220 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34220) but 4h close 0.34360 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-21 12:10:07 CST | RECLAIM_PENDING_SET | 0.34040 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34040) but 4h close 0.34030 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-21 16:10:07 CST | RECLAIM_PENDING_SET | 0.33870 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33870) but 4h close 0.33880 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-21 20:07:11 CST | RECLAIM_PENDING_SET | 0.33780 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33780) but 4h close 0.33700 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-22 00:10:11 CST | RECLAIM_PENDING_SET | 0.34150 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34150) but 4h close 0.34170 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-22 04:10:05 CST | RECLAIM_PENDING_SET | 0.34000 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34000) but 4h close 0.34050 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-22 08:10:04 CST | RECLAIM_PENDING_SET | 0.33250 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33250) but 4h close 0.32980 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-22 12:10:06 CST | RECLAIM_PENDING_SET | 0.33460 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33460) but 4h close 0.33360 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-22 16:10:07 CST | RECLAIM_PENDING_SET | 0.33750 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33750) but 4h close 0.33750 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-22 20:07:12 CST | RECLAIM_PENDING_SET | 0.34000 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34000) but 4h close 0.33940 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-23 00:10:08 CST | RECLAIM_PENDING_SET | 0.33200 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33200) but 4h close 0.33310 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-23 04:10:05 CST | RECLAIM_PENDING_SET | 0.33200 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33200) but 4h close 0.33080 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-23 08:10:05 CST | RECLAIM_PENDING_SET | 0.32830 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32830) but 4h close 0.32910 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-23 12:10:06 CST | RECLAIM_PENDING_SET | 0.32440 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32440) but 4h close 0.32480 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-23 16:10:09 CST | RECLAIM_PENDING_SET | 0.31670 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31670) but 4h close 0.31450 < entry_high 0.41157; waiting for reclaim. |

### PORTALUSDT `4a445771b4fd`

- 当前状态：`INVALIDATED`
- 来源扫描：`7a562bac13ec` rank 5

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-06-03 20:11:39 CST | WATCHLIST_ADDED | 0.02503 | n/a | 0.00 | 0.00 | Imported rank 5 from scan 7a562bac13ec; entry zone 0.021045357-0.022741223. |
| 2026-06-11 11:36:50 CST | INVALIDATED | 0.01492 | n/a | 0.00 | 0.00 | Plan invalidated before entry: current price is below stop loss. |

### NEARUSDT `fcbf85c001a3`

- 当前状态：`ARCHIVED`
- 来源扫描：`c2d8a8204b8a` rank 1

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 23:37:15 CST | WATCHLIST_ADDED | 1.6210 | n/a | 0.00 | 0.00 | Imported rank 1 from scan c2d8a8204b8a; entry zone 1.5680499-1.5998701. |
| 2026-06-03 20:11:39 CST | ARCHIVED | 2.8880 | n/a | 0.00 | 0.00 | Archived because scan 7a562bac13ec created a newer WATCHING plan for NEARUSDT. |

### ZECUSDT `bca28ae77b59`

- 当前状态：`ARCHIVED`
- 来源扫描：`c2d8a8204b8a` rank 2

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 23:37:15 CST | WATCHLIST_ADDED | 564.51 | n/a | 0.00 | 0.00 | Imported rank 2 from scan c2d8a8204b8a; entry zone 543.6375-559.54036. |
| 2026-06-03 20:11:39 CST | ARCHIVED | 593.25 | n/a | 0.00 | 0.00 | Archived because scan 7a562bac13ec created a newer WATCHING plan for ZECUSDT. |

### ONDOUSDT `b044885db771`

- 当前状态：`ARCHIVED`
- 来源扫描：`c2d8a8204b8a` rank 3

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 23:37:15 CST | WATCHLIST_ADDED | 0.36380 | n/a | 0.00 | 0.00 | Imported rank 3 from scan c2d8a8204b8a; entry zone 0.36410617-0.3648914. |
| 2026-06-03 20:11:39 CST | ARCHIVED | 0.41270 | n/a | 0.00 | 0.00 | Archived because scan 7a562bac13ec created a newer WATCHING plan for ONDOUSDT. |

### TRXUSDT `a60457e724a8`

- 当前状态：`INVALIDATED`
- 来源扫描：`c2d8a8204b8a` rank 4

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 23:37:15 CST | WATCHLIST_ADDED | 0.35450 | n/a | 0.00 | 0.00 | Imported rank 4 from scan c2d8a8204b8a; entry zone 0.3535056-0.354325. |
| 2026-06-03 19:55:38 CST | INVALIDATED | 0.33220 | n/a | 0.00 | 0.00 | Plan invalidated before entry: current price is below stop loss. |

### TONUSDT `136c277b7ecb`

- 当前状态：`STOPPED`
- 来源扫描：`c2d8a8204b8a` rank 5

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 23:37:15 CST | WATCHLIST_ADDED | 1.9770 | n/a | 0.00 | 0.00 | Imported rank 5 from scan c2d8a8204b8a; entry zone 1.9697346-1.982931. |
| 2026-05-19 23:37:17 CST | ENTERED | 1.9770 | 685.47 | 0.00 | 0.00 | Paper entry triggered at 1.977; quantity 685.47143. |
| 2026-06-11 11:36:50 CST | STOPPED | 1.8311 | 685.47 | -100.00 | 0.00 | Stop loss hit at 1.831115. |

### NEARUSDT `37c396de0f99`

- 当前状态：`ARCHIVED`
- 来源扫描：`5e1db9afc001` rank 1

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 23:25:16 CST | WATCHLIST_ADDED | 1.6110 | n/a | 0.00 | 0.00 | Imported rank 1 from scan 5e1db9afc001; entry zone 1.5670956-1.5989177. |
| 2026-05-19 23:37:15 CST | ARCHIVED | 1.6080 | n/a | 0.00 | 0.00 | Archived because scan c2d8a8204b8a created a newer WATCHING plan for NEARUSDT. |

### ZECUSDT `7492d02b3365`

- 当前状态：`ARCHIVED`
- 来源扫描：`5e1db9afc001` rank 2

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 23:25:16 CST | WATCHLIST_ADDED | 557.92 | n/a | 0.00 | 0.00 | Imported rank 2 from scan 5e1db9afc001; entry zone 542.75017-555.58184. |
| 2026-05-19 23:37:15 CST | ARCHIVED | 557.63 | n/a | 0.00 | 0.00 | Archived because scan c2d8a8204b8a created a newer WATCHING plan for ZECUSDT. |

### ONDOUSDT `5d1c3b7ddf56`

- 当前状态：`STOPPED`
- 来源扫描：`5e1db9afc001` rank 3

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 23:25:16 CST | WATCHLIST_ADDED | 0.36160 | n/a | 0.00 | 0.00 | Imported rank 3 from scan 5e1db9afc001; entry zone 0.35389662-0.3626848. |
| 2026-05-19 23:25:22 CST | ENTERED | 0.36110 | 3,039.70 | 0.00 | 0.00 | Paper entry triggered at 0.3611; quantity 3039.6985. |
| 2026-06-23 12:10:05 CST | STOPPED | 0.32820 | 3,039.70 | -100.00 | 0.00 | Stop loss hit at 0.328202. |

### TRXUSDT `d5f1ac1e39b8`

- 当前状态：`ARCHIVED`
- 来源扫描：`5e1db9afc001` rank 4

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 23:25:16 CST | WATCHLIST_ADDED | 0.35470 | n/a | 0.00 | 0.00 | Imported rank 4 from scan 5e1db9afc001; entry zone 0.3535056-0.354325. |
| 2026-05-19 23:37:15 CST | ARCHIVED | 0.35470 | n/a | 0.00 | 0.00 | Archived because scan c2d8a8204b8a created a newer WATCHING plan for TRXUSDT. |

### TONUSDT `19feb0407108`

- 当前状态：`ARCHIVED`
- 来源扫描：`5e1db9afc001` rank 5

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 23:25:16 CST | WATCHLIST_ADDED | 1.9580 | n/a | 0.00 | 0.00 | Imported rank 5 from scan 5e1db9afc001; entry zone 1.87415-1.9380357. |
| 2026-05-19 23:37:15 CST | ARCHIVED | 1.9570 | n/a | 0.00 | 0.00 | Archived because scan c2d8a8204b8a created a newer WATCHING plan for TONUSDT. |

### NEARUSDT `06b59e5772f3`

- 当前状态：`ARCHIVED`
- 来源扫描：`a0af416b7052` rank 1

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 23:14:11 CST | WATCHLIST_ADDED | 1.6190 | n/a | 0.00 | 0.00 | Imported rank 1 from scan a0af416b7052; entry zone 1.5678591-1.5996796. |
| 2026-05-19 23:25:16 CST | ARCHIVED | 1.6200 | n/a | 0.00 | 0.00 | Archived because scan 5e1db9afc001 created a newer WATCHING plan for NEARUSDT. |

### ZECUSDT `3b1d9db16481`

- 当前状态：`ARCHIVED`
- 来源扫描：`a0af416b7052` rank 2

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 23:14:11 CST | WATCHLIST_ADDED | 557.63 | n/a | 0.00 | 0.00 | Imported rank 2 from scan a0af416b7052; entry zone 542.72823-555.55994. |
| 2026-05-19 23:25:16 CST | ARCHIVED | 558.04 | n/a | 0.00 | 0.00 | Archived because scan 5e1db9afc001 created a newer WATCHING plan for ZECUSDT. |

### ONDOUSDT `2ed171ff8ada`

- 当前状态：`STOPPED`
- 来源扫描：`a0af416b7052` rank 3

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 23:14:11 CST | WATCHLIST_ADDED | 0.36200 | n/a | 0.00 | 0.00 | Imported rank 3 from scan a0af416b7052; entry zone 0.35394433-0.363086. |
| 2026-05-19 23:14:20 CST | ENTERED | 0.36190 | 2,967.54 | 0.00 | 0.00 | Paper entry triggered at 0.3619; quantity 2967.5352. |
| 2026-06-23 12:10:05 CST | STOPPED | 0.32820 | 2,967.54 | -100.00 | 0.00 | Stop loss hit at 0.328202. |

### TRXUSDT `f9ef653b0a17`

- 当前状态：`ARCHIVED`
- 来源扫描：`a0af416b7052` rank 4

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 23:14:11 CST | WATCHLIST_ADDED | 0.35460 | n/a | 0.00 | 0.00 | Imported rank 4 from scan a0af416b7052; entry zone 0.3535056-0.354325. |
| 2026-05-19 23:25:16 CST | ARCHIVED | 0.35460 | n/a | 0.00 | 0.00 | Archived because scan 5e1db9afc001 created a newer WATCHING plan for TRXUSDT. |

### TONUSDT `195cc3f0d481`

- 当前状态：`STOPPED`
- 来源扫描：`a0af416b7052` rank 5

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 23:14:11 CST | WATCHLIST_ADDED | 1.9710 | n/a | 0.00 | 0.00 | Imported rank 5 from scan a0af416b7052; entry zone 1.969162-1.976913. |
| 2026-05-19 23:14:20 CST | ENTERED | 1.9710 | 714.87 | 0.00 | 0.00 | Paper entry triggered at 1.971; quantity 714.87293. |
| 2026-06-11 11:36:50 CST | STOPPED | 1.8311 | 714.87 | -100.00 | 0.00 | Stop loss hit at 1.831115. |

### ZECUSDT `1b124f8886a4`

- 当前状态：`STOPPED`
- 来源扫描：`644f2c98e0a5` rank 1

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 22:53:38 CST | WATCHLIST_ADDED | 555.32 | 1.54 | 0.00 | 2.20 | Backfilled event: trade existed before event logging was enabled. |
| 2026-05-19 22:53:44 CST | ENTERED | 553.89 | 1.54 | 0.00 | 2.20 | Backfilled event: trade was already entered before event logging was enabled. |
| 2026-06-11 11:36:50 CST | STOPPED | 489.02 | 1.54 | -100.00 | 0.00 | Stop loss hit at 489.02295. |

### NEARUSDT `65381ba94662`

- 当前状态：`ARCHIVED`
- 来源扫描：`644f2c98e0a5` rank 2

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 22:53:38 CST | WATCHLIST_ADDED | 1.6160 | n/a | 0.00 | 0.00 | Backfilled event: trade existed before event logging was enabled. |
| 2026-05-19 23:25:16 CST | ARCHIVED | 1.6200 | n/a | 0.00 | 0.00 | Archived because scan 5e1db9afc001 created a newer WATCHING plan for NEARUSDT. |

### ONDOUSDT `e6573e503a1b`

- 当前状态：`ARCHIVED`
- 来源扫描：`644f2c98e0a5` rank 3

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 22:53:38 CST | WATCHLIST_ADDED | 0.36070 | n/a | 0.00 | 0.00 | Backfilled event: trade existed before event logging was enabled. |
| 2026-05-19 23:25:16 CST | ARCHIVED | 0.36190 | n/a | 0.00 | 0.00 | Archived because scan 5e1db9afc001 created a newer WATCHING plan for ONDOUSDT. |

### TRXUSDT `482fc18a8c7a`

- 当前状态：`ARCHIVED`
- 来源扫描：`644f2c98e0a5` rank 4

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 22:53:38 CST | WATCHLIST_ADDED | 0.35430 | n/a | 0.00 | 0.00 | Backfilled event: trade existed before event logging was enabled. |
| 2026-05-19 23:25:16 CST | ARCHIVED | 0.35460 | n/a | 0.00 | 0.00 | Archived because scan 5e1db9afc001 created a newer WATCHING plan for TRXUSDT. |

### TONUSDT `da78b42d2554`

- 当前状态：`STOPPED`
- 来源扫描：`644f2c98e0a5` rank 5

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 22:53:38 CST | WATCHLIST_ADDED | 1.9660 | n/a | 0.00 | 0.00 | Backfilled event: trade existed before event logging was enabled. |
| 2026-05-19 23:14:20 CST | ENTERED | 1.9710 | 714.87 | 0.00 | 0.00 | Paper entry triggered at 1.971; quantity 714.87293. |
| 2026-06-11 11:36:50 CST | STOPPED | 1.8311 | 714.87 | -100.00 | 0.00 | Stop loss hit at 1.831115. |


## 状态说明

- `WATCHING`：计划已加入模拟盘，等待价格进入入场区间。
- `ENTERED`：价格触发入场区，已模拟买入。
- `TP1_HIT`：已触发第一止盈，继续跟踪第二止盈。
- `STOPPED`：入场后触发止损。
- `CLOSED`：触发 TP2 后模拟平仓。
- `INVALIDATED`：尚未入场就跌破止损，计划失效。
- `ARCHIVED`：尚未入场的旧计划被同币种新计划替换。
