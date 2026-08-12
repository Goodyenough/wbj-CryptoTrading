---
created: 2026-08-07 08:10:04 CST
tags:
  - crypto
  - trading-system
  - paper-trading
account: demo
report_version: v1
---

# 模拟盘报告 demo v1

- 报告时间：2026-08-07 08:10:04 CST
- Run ID：`20260807_001003_6a7da75a`
- Run type：`paper_4h_update`
- 数据来源：SQLite
- 报告版本：v1
- 模拟账户权益基准：10,000.00 USDT
- 单笔计划风险：1.00%
- 开放交易/观察：1
- 已结束交易：24
- 已实现 PnL：-800.00 USDT
- 未实现 PnL：0.00 USDT
- 已入场交易数：8
- 胜率：0.00%
- TP1 命中率：0.00%

## 今日大盘环境

_大盘环境数据获取失败。_

## 复盘统计

| Metric | Value |
|---|---:|
| Total plans | 25 |
| Open watching/positions | 1 |
| Entered trades | 8 |
| Closed trades | 24 |
| Winning closed trades | 0 |
| Losing closed trades | 8 |
| Win rate | 0.00% |
| TP1 hit rate | 0.00% |
| Realized PnL | -800.00 USDT |
| Unrealized PnL | 0.00 USDT |
| Entry reclaim blocks | 250 |
| Avg holding time | 644.4h |
| TP1 EMA trailing activated | 0 |
| TP1 EMA trailing raises | 0 |
| TP1 EMA trailing stops | 0 |
| TP1 EMA trailing active trades | 0 |
| This run events | 1 |
| This run API delay skipped | 1 |

## Entry Reclaim 后续追踪

| Symbol | Status | Pending Events | First Pending | Last Pending | Outcome | Detail |
|---|---|---:|---|---|---|---|
| `ONDOUSDT` | WATCHING | 250 | 2026-06-11 20:47:37 CST | 2026-08-05 22:23:44 CST | still_waiting | Watching: entry zone touched, but 4h close has not reclaimed entry_high. |

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
| 2026-08-07 08:10:03 CST | API_DELAY_SKIPPED | `ONDOUSDT` | WATCHING | WATCHING | 0.38160 | 0.33845 | 0.33845 | 2026-08-07T00:10:04Z | 24h ticker unavailable; state update skipped: HTTPError: HTTP Error 451:  |

## 当前观察与持仓

| Status | Symbol | Last | Entry Zone | Entry | Stop | TP1 | TP2 | Qty | Unrealized | Notes |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| WATCHING | `ONDOUSDT` | 0.38160 | 0.39450 - 0.41157 | n/a | 0.33845 | 0.53222 | 0.59681 | n/a | 0.00 | Watching: entry zone touched, but 4h close has not reclaimed entry_high. |

## 已结束交易

| Status | Symbol | Entry | Exit | Qty | Realized PnL | Source Scan | Notes |
|---|---|---:|---:|---:|---:|---|---|
| STOPPED | `ZECUSDT` | 597.81 | 518.76 | 1.27 | -100.00 | 7a562bac13ec | Stop loss hit. |
| STOPPED | `WLDUSDT` | 0.45830 | 0.31687 | 707.09 | -100.00 | 7a562bac13ec | Stop loss hit. |
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

- 当前状态：`STOPPED`
- 来源扫描：`7a562bac13ec` rank 2

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-06-03 20:11:39 CST | WATCHLIST_ADDED | 0.49690 | n/a | 0.00 | 0.00 | Imported rank 2 from scan 7a562bac13ec; entry zone 0.43070929-0.46769821. |
| 2026-06-11 11:36:50 CST | ENTERED | 0.45830 | 707.09 | 0.00 | 0.00 | Paper entry triggered at 0.4583; quantity 707.08606. |
| 2026-07-29 12:10:05 CST | STOPPED | 0.31687 | 707.09 | -100.00 | 0.00 | Stop loss hit at 0.3168745. |

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
| 2026-06-23 20:07:47 CST | RECLAIM_PENDING_SET | 0.31340 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31340) but 4h close 0.31360 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-24 00:10:21 CST | RECLAIM_PENDING_SET | 0.31260 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31260) but 4h close 0.31100 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-24 04:10:05 CST | RECLAIM_PENDING_SET | 0.31440 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31440) but 4h close 0.31160 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-24 08:10:05 CST | RECLAIM_PENDING_SET | 0.31540 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31540) but 4h close 0.31480 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-24 12:10:05 CST | RECLAIM_PENDING_SET | 0.30870 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.30870) but 4h close 0.30920 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-24 16:10:08 CST | RECLAIM_PENDING_SET | 0.30820 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.30820) but 4h close 0.30730 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-24 20:06:32 CST | RECLAIM_PENDING_SET | 0.30810 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.30810) but 4h close 0.30700 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-25 00:10:10 CST | RECLAIM_PENDING_SET | 0.30040 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.30040) but 4h close 0.29840 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-25 04:10:05 CST | RECLAIM_PENDING_SET | 0.30620 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.30620) but 4h close 0.30190 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-25 08:10:05 CST | RECLAIM_PENDING_SET | 0.31700 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31700) but 4h close 0.31450 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-25 12:10:09 CST | RECLAIM_PENDING_SET | 0.31510 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31510) but 4h close 0.31510 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-25 20:08:44 CST | RECLAIM_PENDING_SET | 0.31240 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31240) but 4h close 0.31280 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-26 00:10:08 CST | RECLAIM_PENDING_SET | 0.31290 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31290) but 4h close 0.30900 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-26 04:10:05 CST | RECLAIM_PENDING_SET | 0.30760 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.30760) but 4h close 0.30680 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-26 08:10:05 CST | RECLAIM_PENDING_SET | 0.31560 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31560) but 4h close 0.31410 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-26 12:10:06 CST | RECLAIM_PENDING_SET | 0.30870 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.30870) but 4h close 0.30920 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-26 16:10:10 CST | RECLAIM_PENDING_SET | 0.31500 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31500) but 4h close 0.31730 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-26 20:06:27 CST | RECLAIM_PENDING_SET | 0.30810 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.30810) but 4h close 0.30670 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-27 00:10:09 CST | RECLAIM_PENDING_SET | 0.31540 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31540) but 4h close 0.31540 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-27 04:10:06 CST | RECLAIM_PENDING_SET | 0.31900 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31900) but 4h close 0.31740 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-27 08:10:05 CST | RECLAIM_PENDING_SET | 0.31780 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31780) but 4h close 0.31720 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-27 12:10:09 CST | RECLAIM_PENDING_SET | 0.32210 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32210) but 4h close 0.32120 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-27 16:10:08 CST | RECLAIM_PENDING_SET | 0.31850 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31850) but 4h close 0.31940 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-27 20:06:37 CST | RECLAIM_PENDING_SET | 0.31830 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31830) but 4h close 0.31820 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-28 00:10:11 CST | RECLAIM_PENDING_SET | 0.31890 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31890) but 4h close 0.31910 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-28 04:10:05 CST | RECLAIM_PENDING_SET | 0.31250 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31250) but 4h close 0.31200 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-28 08:10:05 CST | RECLAIM_PENDING_SET | 0.31220 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31220) but 4h close 0.31110 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-28 12:10:05 CST | RECLAIM_PENDING_SET | 0.30970 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.30970) but 4h close 0.31040 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-28 16:10:08 CST | RECLAIM_PENDING_SET | 0.30990 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.30990) but 4h close 0.31070 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-28 20:05:59 CST | RECLAIM_PENDING_SET | 0.31000 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31000) but 4h close 0.31000 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-29 00:10:12 CST | RECLAIM_PENDING_SET | 0.30850 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.30850) but 4h close 0.30850 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-29 04:10:05 CST | RECLAIM_PENDING_SET | 0.30710 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.30710) but 4h close 0.30750 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-29 08:10:05 CST | RECLAIM_PENDING_SET | 0.30840 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.30840) but 4h close 0.30980 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-29 12:10:08 CST | RECLAIM_PENDING_SET | 0.31150 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31150) but 4h close 0.31250 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-29 16:10:06 CST | RECLAIM_PENDING_SET | 0.31240 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31240) but 4h close 0.31160 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-29 20:06:29 CST | RECLAIM_PENDING_SET | 0.31420 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31420) but 4h close 0.31110 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-30 00:10:11 CST | RECLAIM_PENDING_SET | 0.31240 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31240) but 4h close 0.31220 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-30 04:10:06 CST | RECLAIM_PENDING_SET | 0.31980 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31980) but 4h close 0.31970 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-30 08:10:06 CST | RECLAIM_PENDING_SET | 0.31610 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31610) but 4h close 0.31740 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-30 12:10:09 CST | RECLAIM_PENDING_SET | 0.31130 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31130) but 4h close 0.31220 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-30 16:10:07 CST | RECLAIM_PENDING_SET | 0.31330 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31330) but 4h close 0.31430 < entry_high 0.41157; waiting for reclaim. |
| 2026-06-30 20:06:47 CST | RECLAIM_PENDING_SET | 0.30830 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.30830) but 4h close 0.30900 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-01 00:10:10 CST | RECLAIM_PENDING_SET | 0.30990 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.30990) but 4h close 0.30890 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-01 04:10:05 CST | RECLAIM_PENDING_SET | 0.31290 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31290) but 4h close 0.31200 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-01 08:10:05 CST | RECLAIM_PENDING_SET | 0.30880 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.30880) but 4h close 0.30840 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-01 12:10:07 CST | RECLAIM_PENDING_SET | 0.31550 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31550) but 4h close 0.31480 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-01 16:10:09 CST | RECLAIM_PENDING_SET | 0.31030 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31030) but 4h close 0.31150 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-01 20:06:39 CST | RECLAIM_PENDING_SET | 0.30980 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.30980) but 4h close 0.31060 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-02 00:10:10 CST | RECLAIM_PENDING_SET | 0.32060 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32060) but 4h close 0.32070 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-02 04:10:05 CST | RECLAIM_PENDING_SET | 0.31780 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31780) but 4h close 0.31830 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-02 08:10:05 CST | RECLAIM_PENDING_SET | 0.32450 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32450) but 4h close 0.32470 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-02 12:10:09 CST | RECLAIM_PENDING_SET | 0.33230 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33230) but 4h close 0.33370 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-02 16:10:07 CST | RECLAIM_PENDING_SET | 0.33210 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33210) but 4h close 0.33080 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-02 20:07:02 CST | RECLAIM_PENDING_SET | 0.33470 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33470) but 4h close 0.33410 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-03 00:10:08 CST | RECLAIM_PENDING_SET | 0.33380 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33380) but 4h close 0.33300 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-03 04:10:05 CST | RECLAIM_PENDING_SET | 0.33140 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33140) but 4h close 0.33130 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-03 08:10:05 CST | RECLAIM_PENDING_SET | 0.32790 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32790) but 4h close 0.32840 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-03 12:10:06 CST | RECLAIM_PENDING_SET | 0.33040 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33040) but 4h close 0.33180 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-03 16:10:06 CST | RECLAIM_PENDING_SET | 0.33030 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33030) but 4h close 0.33060 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-03 20:06:10 CST | RECLAIM_PENDING_SET | 0.33420 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33420) but 4h close 0.33390 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-04 00:10:08 CST | RECLAIM_PENDING_SET | 0.33210 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33210) but 4h close 0.33220 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-04 04:10:06 CST | RECLAIM_PENDING_SET | 0.33620 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33620) but 4h close 0.33530 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-04 08:10:05 CST | RECLAIM_PENDING_SET | 0.33500 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33500) but 4h close 0.33410 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-04 12:10:08 CST | RECLAIM_PENDING_SET | 0.33630 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33630) but 4h close 0.33600 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-04 16:10:07 CST | RECLAIM_PENDING_SET | 0.33310 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33310) but 4h close 0.33280 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-04 20:06:18 CST | RECLAIM_PENDING_SET | 0.33210 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33210) but 4h close 0.33160 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-05 04:10:08 CST | RECLAIM_PENDING_SET | 0.34000 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34000) but 4h close 0.33990 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-05 08:10:05 CST | RECLAIM_PENDING_SET | 0.33390 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33390) but 4h close 0.33580 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-05 12:10:06 CST | RECLAIM_PENDING_SET | 0.32770 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32770) but 4h close 0.32720 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-08 00:10:08 CST | RECLAIM_PENDING_SET | 0.33540 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33540) but 4h close 0.33700 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-08 04:10:06 CST | RECLAIM_PENDING_SET | 0.33100 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33100) but 4h close 0.33150 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-08 08:10:05 CST | RECLAIM_PENDING_SET | 0.32930 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32930) but 4h close 0.32780 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-08 12:10:05 CST | RECLAIM_PENDING_SET | 0.32710 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32710) but 4h close 0.32780 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-08 16:10:23 CST | RECLAIM_PENDING_SET | 0.32210 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32210) but 4h close 0.32090 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-08 20:06:22 CST | RECLAIM_PENDING_SET | 0.32020 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32020) but 4h close 0.31960 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-09 00:10:12 CST | RECLAIM_PENDING_SET | 0.31340 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31340) but 4h close 0.31160 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-09 04:10:05 CST | RECLAIM_PENDING_SET | 0.31500 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31500) but 4h close 0.31520 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-09 08:10:04 CST | RECLAIM_PENDING_SET | 0.31510 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31510) but 4h close 0.31600 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-09 12:10:05 CST | RECLAIM_PENDING_SET | 0.31400 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31400) but 4h close 0.31340 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-09 16:10:33 CST | RECLAIM_PENDING_SET | 0.31880 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31880) but 4h close 0.31910 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-09 20:06:06 CST | RECLAIM_PENDING_SET | 0.31710 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31710) but 4h close 0.31810 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-10 00:10:11 CST | RECLAIM_PENDING_SET | 0.31710 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31710) but 4h close 0.31700 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-10 04:10:05 CST | RECLAIM_PENDING_SET | 0.31810 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31810) but 4h close 0.31850 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-10 08:10:05 CST | RECLAIM_PENDING_SET | 0.31610 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31610) but 4h close 0.31670 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-10 12:10:12 CST | RECLAIM_PENDING_SET | 0.32090 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32090) but 4h close 0.32060 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-10 16:10:16 CST | RECLAIM_PENDING_SET | 0.32090 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32090) but 4h close 0.32100 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-10 20:05:56 CST | RECLAIM_PENDING_SET | 0.32670 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32670) but 4h close 0.32720 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-11 00:10:13 CST | RECLAIM_PENDING_SET | 0.32610 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32610) but 4h close 0.32640 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-11 04:10:05 CST | RECLAIM_PENDING_SET | 0.32650 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32650) but 4h close 0.32650 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-11 08:10:05 CST | RECLAIM_PENDING_SET | 0.32870 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32870) but 4h close 0.32840 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-11 22:27:23 CST | RECLAIM_PENDING_SET | 0.33610 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33610) but 4h close 0.33370 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-12 00:10:20 CST | RECLAIM_PENDING_SET | 0.33280 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33280) but 4h close 0.33440 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-12 04:10:04 CST | RECLAIM_PENDING_SET | 0.33520 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33520) but 4h close 0.33480 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-12 08:10:05 CST | RECLAIM_PENDING_SET | 0.32300 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32300) but 4h close 0.32420 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-12 12:10:07 CST | RECLAIM_PENDING_SET | 0.32670 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32670) but 4h close 0.32630 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-12 16:10:10 CST | RECLAIM_PENDING_SET | 0.32720 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32720) but 4h close 0.32570 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-12 20:05:54 CST | RECLAIM_PENDING_SET | 0.32920 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32920) but 4h close 0.32870 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-13 00:10:12 CST | RECLAIM_PENDING_SET | 0.32860 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32860) but 4h close 0.32760 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-13 04:10:04 CST | RECLAIM_PENDING_SET | 0.32560 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32560) but 4h close 0.32710 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-13 08:10:04 CST | RECLAIM_PENDING_SET | 0.32530 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32530) but 4h close 0.32290 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-13 12:10:08 CST | RECLAIM_PENDING_SET | 0.31700 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31700) but 4h close 0.31660 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-13 16:11:22 CST | RECLAIM_PENDING_SET | 0.31940 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31940) but 4h close 0.31900 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-13 20:07:34 CST | RECLAIM_PENDING_SET | 0.31800 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31800) but 4h close 0.31850 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-14 00:10:11 CST | RECLAIM_PENDING_SET | 0.31630 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31630) but 4h close 0.31590 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-14 04:10:05 CST | RECLAIM_PENDING_SET | 0.31270 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31270) but 4h close 0.31330 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-14 08:10:04 CST | RECLAIM_PENDING_SET | 0.30950 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.30950) but 4h close 0.31090 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-14 12:10:04 CST | RECLAIM_PENDING_SET | 0.30710 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.30710) but 4h close 0.30620 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-14 16:10:04 CST | RECLAIM_PENDING_SET | 0.30730 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.30730) but 4h close 0.30780 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-14 20:06:09 CST | RECLAIM_PENDING_SET | 0.30710 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.30710) but 4h close 0.30800 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-15 00:10:12 CST | RECLAIM_PENDING_SET | 0.31670 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31670) but 4h close 0.31550 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-15 04:10:05 CST | RECLAIM_PENDING_SET | 0.31490 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31490) but 4h close 0.31530 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-15 08:10:04 CST | RECLAIM_PENDING_SET | 0.31570 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31570) but 4h close 0.31490 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-15 12:10:12 CST | RECLAIM_PENDING_SET | 0.32250 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32250) but 4h close 0.32220 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-15 16:10:31 CST | RECLAIM_PENDING_SET | 0.31730 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.31730) but 4h close 0.31820 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-15 20:06:14 CST | RECLAIM_PENDING_SET | 0.32300 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32300) but 4h close 0.32310 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-16 00:10:15 CST | RECLAIM_PENDING_SET | 0.33160 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33160) but 4h close 0.33340 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-16 04:10:06 CST | RECLAIM_PENDING_SET | 0.34790 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34790) but 4h close 0.33390 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-16 08:10:05 CST | RECLAIM_PENDING_SET | 0.36700 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36700) but 4h close 0.36510 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-16 12:10:07 CST | RECLAIM_PENDING_SET | 0.36430 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36430) but 4h close 0.36820 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-16 16:10:09 CST | RECLAIM_PENDING_SET | 0.37020 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37020) but 4h close 0.37070 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-16 20:06:19 CST | RECLAIM_PENDING_SET | 0.37370 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37370) but 4h close 0.37440 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-17 00:10:11 CST | RECLAIM_PENDING_SET | 0.38290 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38290) but 4h close 0.38420 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-17 04:10:05 CST | RECLAIM_PENDING_SET | 0.37750 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37750) but 4h close 0.37590 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-17 08:10:05 CST | RECLAIM_PENDING_SET | 0.36440 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36440) but 4h close 0.36390 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-17 12:10:07 CST | RECLAIM_PENDING_SET | 0.36930 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36930) but 4h close 0.36800 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-17 16:10:09 CST | RECLAIM_PENDING_SET | 0.36480 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36480) but 4h close 0.36420 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-17 20:06:35 CST | RECLAIM_PENDING_SET | 0.38130 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38130) but 4h close 0.38040 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-18 00:10:15 CST | RECLAIM_PENDING_SET | 0.37590 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37590) but 4h close 0.37800 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-18 04:10:05 CST | RECLAIM_PENDING_SET | 0.37310 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37310) but 4h close 0.37540 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-18 08:10:04 CST | RECLAIM_PENDING_SET | 0.37180 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37180) but 4h close 0.37310 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-18 12:10:06 CST | RECLAIM_PENDING_SET | 0.37600 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37600) but 4h close 0.37810 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-18 16:10:04 CST | RECLAIM_PENDING_SET | 0.36680 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36680) but 4h close 0.36670 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-18 20:05:42 CST | RECLAIM_PENDING_SET | 0.34540 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34540) but 4h close 0.34400 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-19 00:10:08 CST | RECLAIM_PENDING_SET | 0.33900 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33900) but 4h close 0.34000 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-19 04:10:04 CST | RECLAIM_PENDING_SET | 0.34960 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34960) but 4h close 0.34840 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-19 08:10:04 CST | RECLAIM_PENDING_SET | 0.34540 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34540) but 4h close 0.34700 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-19 12:10:04 CST | RECLAIM_PENDING_SET | 0.34230 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34230) but 4h close 0.34280 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-19 16:10:05 CST | RECLAIM_PENDING_SET | 0.35030 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.35030) but 4h close 0.35100 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-19 20:05:40 CST | RECLAIM_PENDING_SET | 0.35120 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.35120) but 4h close 0.35310 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-20 00:10:05 CST | RECLAIM_PENDING_SET | 0.34680 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34680) but 4h close 0.34800 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-20 04:10:04 CST | RECLAIM_PENDING_SET | 0.34890 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34890) but 4h close 0.34750 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-20 08:10:04 CST | RECLAIM_PENDING_SET | 0.34750 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34750) but 4h close 0.34560 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-20 12:10:05 CST | RECLAIM_PENDING_SET | 0.34510 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34510) but 4h close 0.34610 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-20 16:10:11 CST | RECLAIM_PENDING_SET | 0.34250 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34250) but 4h close 0.34290 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-20 20:05:58 CST | RECLAIM_PENDING_SET | 0.35220 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.35220) but 4h close 0.35400 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-21 00:10:44 CST | RECLAIM_PENDING_SET | 0.35440 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.35440) but 4h close 0.35310 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-21 04:10:06 CST | RECLAIM_PENDING_SET | 0.35530 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.35530) but 4h close 0.35630 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-21 08:10:05 CST | RECLAIM_PENDING_SET | 0.35810 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.35810) but 4h close 0.35830 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-21 12:10:07 CST | RECLAIM_PENDING_SET | 0.36240 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36240) but 4h close 0.36360 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-21 16:10:54 CST | RECLAIM_PENDING_SET | 0.39130 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.39130) but 4h close 0.39060 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-21 20:06:17 CST | RECLAIM_PENDING_SET | 0.40260 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40260) but 4h close 0.40110 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-22 04:10:04 CST | RECLAIM_PENDING_SET | 0.40180 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40180) but 4h close 0.40130 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-22 08:10:05 CST | RECLAIM_PENDING_SET | 0.40420 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40420) but 4h close 0.40170 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-22 12:10:10 CST | RECLAIM_PENDING_SET | 0.40000 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40000) but 4h close 0.39670 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-22 16:10:16 CST | RECLAIM_PENDING_SET | 0.40230 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40230) but 4h close 0.40000 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-22 20:05:50 CST | RECLAIM_PENDING_SET | 0.40720 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40720) but 4h close 0.41040 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-23 12:10:08 CST | RECLAIM_PENDING_SET | 0.40870 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40870) but 4h close 0.40990 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-23 16:10:18 CST | RECLAIM_PENDING_SET | 0.40630 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40630) but 4h close 0.40500 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-23 20:05:53 CST | RECLAIM_PENDING_SET | 0.40190 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40190) but 4h close 0.40380 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-24 00:10:09 CST | RECLAIM_PENDING_SET | 0.40050 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40050) but 4h close 0.40080 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-24 04:10:07 CST | RECLAIM_PENDING_SET | 0.40250 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40250) but 4h close 0.40100 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-24 08:10:05 CST | RECLAIM_PENDING_SET | 0.40050 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40050) but 4h close 0.40140 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-24 12:10:07 CST | RECLAIM_PENDING_SET | 0.40500 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40500) but 4h close 0.40460 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-24 16:10:07 CST | RECLAIM_PENDING_SET | 0.39910 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.39910) but 4h close 0.40080 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-24 20:06:01 CST | RECLAIM_PENDING_SET | 0.39360 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.39360) but 4h close 0.39350 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-25 00:10:38 CST | RECLAIM_PENDING_SET | 0.39450 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.39450) but 4h close 0.39390 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-25 04:10:05 CST | RECLAIM_PENDING_SET | 0.38880 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38880) but 4h close 0.38960 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-25 08:10:05 CST | RECLAIM_PENDING_SET | 0.38120 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38120) but 4h close 0.38370 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-25 12:10:07 CST | RECLAIM_PENDING_SET | 0.37610 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37610) but 4h close 0.37520 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-25 16:10:06 CST | RECLAIM_PENDING_SET | 0.37670 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37670) but 4h close 0.37700 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-25 20:05:50 CST | RECLAIM_PENDING_SET | 0.38050 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38050) but 4h close 0.38020 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-26 00:10:06 CST | RECLAIM_PENDING_SET | 0.38100 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38100) but 4h close 0.38130 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-26 04:10:04 CST | RECLAIM_PENDING_SET | 0.38290 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38290) but 4h close 0.38300 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-26 08:10:05 CST | RECLAIM_PENDING_SET | 0.37880 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37880) but 4h close 0.37830 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-26 12:10:05 CST | RECLAIM_PENDING_SET | 0.38400 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38400) but 4h close 0.38500 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-26 16:10:06 CST | RECLAIM_PENDING_SET | 0.38660 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38660) but 4h close 0.38750 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-26 20:06:28 CST | RECLAIM_PENDING_SET | 0.38590 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38590) but 4h close 0.38450 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-27 00:10:11 CST | RECLAIM_PENDING_SET | 0.40150 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40150) but 4h close 0.39590 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-27 04:10:05 CST | RECLAIM_PENDING_SET | 0.40010 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40010) but 4h close 0.40030 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-27 08:10:05 CST | RECLAIM_PENDING_SET | 0.40360 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40360) but 4h close 0.40510 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-27 12:10:06 CST | RECLAIM_PENDING_SET | 0.40450 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40450) but 4h close 0.40570 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-27 20:05:56 CST | RECLAIM_PENDING_SET | 0.40720 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40720) but 4h close 0.40590 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-28 00:10:07 CST | RECLAIM_PENDING_SET | 0.40210 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40210) but 4h close 0.40310 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-28 04:10:05 CST | RECLAIM_PENDING_SET | 0.40280 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40280) but 4h close 0.40450 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-28 08:10:05 CST | RECLAIM_PENDING_SET | 0.39460 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.39460) but 4h close 0.39420 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-28 12:10:06 CST | RECLAIM_PENDING_SET | 0.39220 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.39220) but 4h close 0.39210 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-28 16:10:06 CST | RECLAIM_PENDING_SET | 0.38990 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38990) but 4h close 0.39020 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-28 20:06:20 CST | RECLAIM_PENDING_SET | 0.38930 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38930) but 4h close 0.38950 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-29 00:10:10 CST | RECLAIM_PENDING_SET | 0.41030 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.41030) but 4h close 0.41000 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-29 04:10:05 CST | RECLAIM_PENDING_SET | 0.40380 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40380) but 4h close 0.40610 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-29 08:10:06 CST | RECLAIM_PENDING_SET | 0.40720 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40720) but 4h close 0.40620 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-29 12:10:06 CST | RECLAIM_PENDING_SET | 0.39590 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.39590) but 4h close 0.39420 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-29 16:10:56 CST | API_DELAY_SKIPPED | 0.40420 | n/a | 0.00 | 0.00 | 4h kline unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-07-29 20:06:35 CST | RECLAIM_PENDING_SET | 0.40090 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40090) but 4h close 0.40400 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-30 00:10:09 CST | RECLAIM_PENDING_SET | 0.39180 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.39180) but 4h close 0.39360 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-30 04:10:04 CST | RECLAIM_PENDING_SET | 0.39510 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.39510) but 4h close 0.39830 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-30 08:10:04 CST | RECLAIM_PENDING_SET | 0.40450 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40450) but 4h close 0.40380 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-30 12:10:05 CST | RECLAIM_PENDING_SET | 0.40310 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40310) but 4h close 0.40270 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-31 00:10:02 CST | API_DELAY_SKIPPED | 0.42330 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-07-31 04:10:02 CST | API_DELAY_SKIPPED | 0.42330 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-07-31 08:10:02 CST | API_DELAY_SKIPPED | 0.42330 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-07-31 12:10:04 CST | RECLAIM_PENDING_SET | 0.40740 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40740) but 4h close 0.40800 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-31 16:10:04 CST | RECLAIM_PENDING_SET | 0.40490 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40490) but 4h close 0.40440 < entry_high 0.41157; waiting for reclaim. |
| 2026-07-31 20:08:33 CST | RECLAIM_PENDING_SET | 0.40160 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40160) but 4h close 0.40230 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-01 00:10:05 CST | RECLAIM_PENDING_SET | 0.39910 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.39910) but 4h close 0.39820 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-01 04:10:04 CST | RECLAIM_PENDING_SET | 0.39700 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.39700) but 4h close 0.39670 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-01 08:10:04 CST | RECLAIM_PENDING_SET | 0.39150 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.39150) but 4h close 0.39020 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-01 12:10:06 CST | RECLAIM_PENDING_SET | 0.39270 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.39270) but 4h close 0.39210 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-01 16:10:08 CST | RECLAIM_PENDING_SET | 0.38560 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38560) but 4h close 0.38640 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-01 20:05:41 CST | RECLAIM_PENDING_SET | 0.38630 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38630) but 4h close 0.38550 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-02 00:10:21 CST | RECLAIM_PENDING_SET | 0.38680 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38680) but 4h close 0.38770 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-02 04:10:04 CST | RECLAIM_PENDING_SET | 0.37800 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37800) but 4h close 0.37850 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-02 08:10:04 CST | RECLAIM_PENDING_SET | 0.38090 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38090) but 4h close 0.38000 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-02 12:10:04 CST | RECLAIM_PENDING_SET | 0.39320 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.39320) but 4h close 0.39430 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-02 16:10:04 CST | RECLAIM_PENDING_SET | 0.39090 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.39090) but 4h close 0.39200 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-02 20:05:57 CST | RECLAIM_PENDING_SET | 0.38450 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38450) but 4h close 0.38480 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-03 00:10:02 CST | API_DELAY_SKIPPED | 0.38450 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: HTTPError: HTTP Error 451:  |
| 2026-08-03 04:10:02 CST | API_DELAY_SKIPPED | 0.38450 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: HTTPError: HTTP Error 451:  |
| 2026-08-03 08:10:03 CST | API_DELAY_SKIPPED | 0.38450 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: HTTPError: HTTP Error 451:  |
| 2026-08-03 12:10:04 CST | API_DELAY_SKIPPED | 0.38450 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: HTTPError: HTTP Error 451:  |
| 2026-08-03 16:10:02 CST | API_DELAY_SKIPPED | 0.38450 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-08-04 00:10:02 CST | API_DELAY_SKIPPED | 0.38450 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: HTTPError: HTTP Error 451:  |
| 2026-08-04 04:10:02 CST | API_DELAY_SKIPPED | 0.38450 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: HTTPError: HTTP Error 451:  |
| 2026-08-04 08:10:02 CST | API_DELAY_SKIPPED | 0.38450 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: HTTPError: HTTP Error 451:  |
| 2026-08-04 12:10:04 CST | API_DELAY_SKIPPED | 0.38450 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: HTTPError: HTTP Error 451:  |
| 2026-08-04 16:10:02 CST | API_DELAY_SKIPPED | 0.38450 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: HTTPError: HTTP Error 451:  |
| 2026-08-05 22:23:44 CST | RECLAIM_PENDING_SET | 0.38160 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38160) but 4h close 0.38400 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-06 00:10:03 CST | API_DELAY_SKIPPED | 0.38160 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: HTTPError: HTTP Error 451:  |
| 2026-08-06 04:10:01 CST | API_DELAY_SKIPPED | 0.38160 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: HTTPError: HTTP Error 451:  |
| 2026-08-06 08:10:03 CST | API_DELAY_SKIPPED | 0.38160 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: HTTPError: HTTP Error 451:  |
| 2026-08-06 12:10:02 CST | API_DELAY_SKIPPED | 0.38160 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: HTTPError: HTTP Error 451:  |
| 2026-08-06 16:10:02 CST | API_DELAY_SKIPPED | 0.38160 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: HTTPError: HTTP Error 451:  |
| 2026-08-07 00:10:02 CST | API_DELAY_SKIPPED | 0.38160 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: HTTPError: HTTP Error 451:  |
| 2026-08-07 04:10:02 CST | API_DELAY_SKIPPED | 0.38160 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: HTTPError: HTTP Error 451:  |
| 2026-08-07 08:10:03 CST | API_DELAY_SKIPPED | 0.38160 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: HTTPError: HTTP Error 451:  |

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
