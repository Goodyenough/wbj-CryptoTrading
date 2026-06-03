---
created: 2026-05-19 23:37:17 CST
tags:
  - crypto
  - trading-system
  - paper-trading
account: demo
---

# 模拟盘报告 demo

- 报告时间：2026-05-19 23:37:17 CST
- 模拟账户权益基准：10,000.00 USDT
- 单笔计划风险：1.00%
- 开放交易/观察：10
- 已结束交易：10
- 已实现 PnL：0.00 USDT
- 未实现 PnL：39.60 USDT
- 已入场交易数：6
- 胜率：0.00%
- TP1 命中率：0.00%

## 复盘统计

| Metric | Value |
|---|---:|
| Total plans | 20 |
| Open watching/positions | 10 |
| Entered trades | 6 |
| Closed trades | 10 |
| Winning closed trades | 0 |
| Losing closed trades | 0 |
| Win rate | 0.00% |
| TP1 hit rate | 0.00% |
| Realized PnL | 0.00 USDT |
| Unrealized PnL | 39.60 USDT |

## 当前观察与持仓

| Status | Symbol | Last | Entry Zone | Entry | Stop | TP1 | TP2 | Qty | Unrealized | Notes |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| WATCHING | `NEARUSDT` | 1.6230 | 1.5680 - 1.5999 | n/a | 1.4470 | 1.8580 | 1.9949 | n/a | 0.00 | Watching: price is above entry zone; waiting for pullback. |
| WATCHING | `ZECUSDT` | 564.64 | 543.64 - 559.54 | n/a | 489.02 | 676.72 | 739.29 | n/a | 0.00 | Watching: price is above entry zone; waiting for pullback. |
| WATCHING | `ONDOUSDT` | 0.36390 | 0.36411 - 0.36489 | n/a | 0.32820 | 0.43709 | 0.47339 | n/a | 0.00 | Watching: price is below entry zone but above stop; waiting for recovery. |
| WATCHING | `TRXUSDT` | 0.35440 | 0.35351 - 0.35433 | n/a | 0.34751 | 0.36673 | 0.38140 | n/a | 0.00 | Watching: price is above entry zone; waiting for pullback. |
| ENTERED | `TONUSDT` | 1.9770 | 1.9697 - 1.9829 | 1.9770 | 1.8311 | 2.2668 | 2.4120 | 685.47 | 0.00 | Paper entry triggered inside entry zone. |
| ENTERED | `ONDOUSDT` | 0.36390 | 0.35390 - 0.36268 | 0.36110 | 0.32820 | 0.41847 | 0.44856 | 3,039.70 | 8.51 | Paper entry triggered inside entry zone. |
| ENTERED | `ONDOUSDT` | 0.36390 | 0.35394 - 0.36309 | 0.36190 | 0.32820 | 0.41914 | 0.44945 | 2,967.54 | 5.94 | Paper entry triggered inside entry zone. |
| ENTERED | `TONUSDT` | 1.9770 | 1.9692 - 1.9769 | 1.9710 | 1.8311 | 2.2569 | 2.3988 | 714.87 | 4.29 | Paper entry triggered inside entry zone. |
| ENTERED | `ZECUSDT` | 564.64 | 542.46 - 555.25 | 553.89 | 489.02 | 668.52 | 728.36 | 1.54 | 16.57 | Paper entry triggered inside entry zone. |
| ENTERED | `TONUSDT` | 1.9770 | 1.9698 - 1.9829 | 1.9710 | 1.8311 | 2.2669 | 2.4122 | 714.87 | 4.29 | Paper entry triggered inside entry zone. |

## 已结束交易

| Status | Symbol | Entry | Exit | Qty | Realized PnL | Source Scan | Notes |
|---|---|---:|---:|---:|---:|---|---|
| ARCHIVED | `NEARUSDT` | n/a | n/a | n/a | 0.00 | 5e1db9afc001 | Archived because scan c2d8a8204b8a created a newer WATCHING plan for NEARUSDT. |
| ARCHIVED | `ZECUSDT` | n/a | n/a | n/a | 0.00 | 5e1db9afc001 | Archived because scan c2d8a8204b8a created a newer WATCHING plan for ZECUSDT. |
| ARCHIVED | `TRXUSDT` | n/a | n/a | n/a | 0.00 | 5e1db9afc001 | Archived because scan c2d8a8204b8a created a newer WATCHING plan for TRXUSDT. |
| ARCHIVED | `TONUSDT` | n/a | n/a | n/a | 0.00 | 5e1db9afc001 | Archived because scan c2d8a8204b8a created a newer WATCHING plan for TONUSDT. |
| ARCHIVED | `NEARUSDT` | n/a | n/a | n/a | 0.00 | a0af416b7052 | Archived because scan 5e1db9afc001 created a newer WATCHING plan for NEARUSDT. |
| ARCHIVED | `ZECUSDT` | n/a | n/a | n/a | 0.00 | a0af416b7052 | Archived because scan 5e1db9afc001 created a newer WATCHING plan for ZECUSDT. |
| ARCHIVED | `TRXUSDT` | n/a | n/a | n/a | 0.00 | a0af416b7052 | Archived because scan 5e1db9afc001 created a newer WATCHING plan for TRXUSDT. |
| ARCHIVED | `NEARUSDT` | n/a | n/a | n/a | 0.00 | 644f2c98e0a5 | Archived because scan 5e1db9afc001 created a newer WATCHING plan for NEARUSDT. |
| ARCHIVED | `ONDOUSDT` | n/a | n/a | n/a | 0.00 | 644f2c98e0a5 | Archived because scan 5e1db9afc001 created a newer WATCHING plan for ONDOUSDT. |
| ARCHIVED | `TRXUSDT` | n/a | n/a | n/a | 0.00 | 644f2c98e0a5 | Archived because scan 5e1db9afc001 created a newer WATCHING plan for TRXUSDT. |

## 交易生命周期

### NEARUSDT `fcbf85c001a3`

- 当前状态：`WATCHING`
- 来源扫描：`c2d8a8204b8a` rank 1

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 23:37:15 CST | WATCHLIST_ADDED | 1.6210 | n/a | 0.00 | 0.00 | Imported rank 1 from scan c2d8a8204b8a; entry zone 1.5680499-1.5998701. |

### ZECUSDT `bca28ae77b59`

- 当前状态：`WATCHING`
- 来源扫描：`c2d8a8204b8a` rank 2

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 23:37:15 CST | WATCHLIST_ADDED | 564.51 | n/a | 0.00 | 0.00 | Imported rank 2 from scan c2d8a8204b8a; entry zone 543.6375-559.54036. |

### ONDOUSDT `b044885db771`

- 当前状态：`WATCHING`
- 来源扫描：`c2d8a8204b8a` rank 3

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 23:37:15 CST | WATCHLIST_ADDED | 0.36380 | n/a | 0.00 | 0.00 | Imported rank 3 from scan c2d8a8204b8a; entry zone 0.36410617-0.3648914. |

### TRXUSDT `a60457e724a8`

- 当前状态：`WATCHING`
- 来源扫描：`c2d8a8204b8a` rank 4

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 23:37:15 CST | WATCHLIST_ADDED | 0.35450 | n/a | 0.00 | 0.00 | Imported rank 4 from scan c2d8a8204b8a; entry zone 0.3535056-0.354325. |

### TONUSDT `136c277b7ecb`

- 当前状态：`ENTERED`
- 来源扫描：`c2d8a8204b8a` rank 5

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 23:37:15 CST | WATCHLIST_ADDED | 1.9770 | n/a | 0.00 | 0.00 | Imported rank 5 from scan c2d8a8204b8a; entry zone 1.9697346-1.982931. |
| 2026-05-19 23:37:17 CST | ENTERED | 1.9770 | 685.47 | 0.00 | 0.00 | Paper entry triggered at 1.977; quantity 685.47143. |

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

- 当前状态：`ENTERED`
- 来源扫描：`5e1db9afc001` rank 3

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 23:25:16 CST | WATCHLIST_ADDED | 0.36160 | n/a | 0.00 | 0.00 | Imported rank 3 from scan 5e1db9afc001; entry zone 0.35389662-0.3626848. |
| 2026-05-19 23:25:22 CST | ENTERED | 0.36110 | 3,039.70 | 0.00 | 0.00 | Paper entry triggered at 0.3611; quantity 3039.6985. |

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

- 当前状态：`ENTERED`
- 来源扫描：`a0af416b7052` rank 3

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 23:14:11 CST | WATCHLIST_ADDED | 0.36200 | n/a | 0.00 | 0.00 | Imported rank 3 from scan a0af416b7052; entry zone 0.35394433-0.363086. |
| 2026-05-19 23:14:20 CST | ENTERED | 0.36190 | 2,967.54 | 0.00 | 0.00 | Paper entry triggered at 0.3619; quantity 2967.5352. |

### TRXUSDT `f9ef653b0a17`

- 当前状态：`ARCHIVED`
- 来源扫描：`a0af416b7052` rank 4

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 23:14:11 CST | WATCHLIST_ADDED | 0.35460 | n/a | 0.00 | 0.00 | Imported rank 4 from scan a0af416b7052; entry zone 0.3535056-0.354325. |
| 2026-05-19 23:25:16 CST | ARCHIVED | 0.35460 | n/a | 0.00 | 0.00 | Archived because scan 5e1db9afc001 created a newer WATCHING plan for TRXUSDT. |

### TONUSDT `195cc3f0d481`

- 当前状态：`ENTERED`
- 来源扫描：`a0af416b7052` rank 5

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 23:14:11 CST | WATCHLIST_ADDED | 1.9710 | n/a | 0.00 | 0.00 | Imported rank 5 from scan a0af416b7052; entry zone 1.969162-1.976913. |
| 2026-05-19 23:14:20 CST | ENTERED | 1.9710 | 714.87 | 0.00 | 0.00 | Paper entry triggered at 1.971; quantity 714.87293. |

### ZECUSDT `1b124f8886a4`

- 当前状态：`ENTERED`
- 来源扫描：`644f2c98e0a5` rank 1

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 22:53:38 CST | WATCHLIST_ADDED | 555.32 | 1.54 | 0.00 | 2.20 | Backfilled event: trade existed before event logging was enabled. |
| 2026-05-19 22:53:44 CST | ENTERED | 553.89 | 1.54 | 0.00 | 2.20 | Backfilled event: trade was already entered before event logging was enabled. |

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

- 当前状态：`ENTERED`
- 来源扫描：`644f2c98e0a5` rank 5

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-05-19 22:53:38 CST | WATCHLIST_ADDED | 1.9660 | n/a | 0.00 | 0.00 | Backfilled event: trade existed before event logging was enabled. |
| 2026-05-19 23:14:20 CST | ENTERED | 1.9710 | 714.87 | 0.00 | 0.00 | Paper entry triggered at 1.971; quantity 714.87293. |


## 状态说明

- `WATCHING`：计划已加入模拟盘，等待价格进入入场区间。
- `ENTERED`：价格触发入场区，已模拟买入。
- `TP1_HIT`：已触发第一止盈，继续跟踪第二止盈。
- `STOPPED`：入场后触发止损。
- `CLOSED`：触发 TP2 后模拟平仓。
- `INVALIDATED`：尚未入场就跌破止损，计划失效。
- `ARCHIVED`：尚未入场的旧计划被同币种新计划替换。
