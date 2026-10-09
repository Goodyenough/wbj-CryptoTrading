---
created: 2026-10-09 04:10:27 CST
tags:
  - crypto
  - trading-system
  - paper-trading
account: demo
report_version: v1
---

# 模拟盘报告 demo v1

- 报告时间：2026-10-09 04:10:27 CST
- Run ID：`20261008_201003_8395086a`
- Run type：`paper_4h_update`
- 数据来源：SQLite
- 报告版本：v1
- 模拟账户权益基准：10,000.00 USDT
- 单笔计划风险：1.00%
- 开放交易/观察：13
- 已结束交易：52
- 已实现 PnL：1,422.14 USDT
- 未实现 PnL：122.34 USDT
- 已入场交易数：20
- 胜率：17.31%
- TP1 命中率：40.00%

## 今日大盘环境

_大盘环境数据获取失败。_

## 复盘统计

| Metric | Value |
|---|---:|
| Total plans | 65 |
| Open watching/positions | 13 |
| Entered trades | 20 |
| Closed trades | 52 |
| Winning closed trades | 9 |
| Losing closed trades | 8 |
| Win rate | 17.31% |
| TP1 hit rate | 40.00% |
| Realized PnL | 1,422.14 USDT |
| Unrealized PnL | 122.34 USDT |
| Entry reclaim blocks | 550 |
| Avg holding time | 529.1h |
| TP1 EMA trailing activated | 8 |
| TP1 EMA trailing raises | 56 |
| TP1 EMA trailing stops | 5 |
| TP1 EMA trailing active trades | 0 |
| This run events | 13 |
| This run API delay skipped | 13 |

## Entry Reclaim 后续追踪

| Symbol | Status | Pending Events | First Pending | Last Pending | Outcome | Detail |
|---|---|---:|---|---|---|---|
| `DOGEUSDT` | WATCHING | 5 | 2026-09-24 00:10:20 CST | 2026-10-09 00:10:13 CST | still_waiting | Watching: entry zone touched, but 4h close has not reclaimed entry_high. |
| `XRPUSDT` | WATCHING | 5 | 2026-09-24 00:10:20 CST | 2026-10-09 00:10:14 CST | still_waiting | Watching: entry zone touched, but 4h close has not reclaimed entry_high. |
| `HBARUSDT` | WATCHING | 5 | 2026-09-24 00:10:21 CST | 2026-10-09 00:10:15 CST | still_waiting | Watching: entry zone touched, but 4h close has not reclaimed entry_high. |
| `LTCUSDT` | WATCHING | 2 | 2026-09-22 20:07:11 CST | 2026-09-24 00:10:19 CST | still_waiting | Watching: price is above entry zone; waiting for pullback. |
| `SUIUSDT` | WATCHING | 2 | 2026-09-10 00:10:25 CST | 2026-09-10 04:10:09 CST | still_waiting | Watching: price is above entry zone; waiting for pullback. |
| `ENAUSDT` | WATCHING | 10 | 2026-09-07 00:10:32 CST | 2026-09-10 04:10:08 CST | still_waiting | Watching: price is above entry zone; waiting for pullback. |
| `DOGEUSDT` | STOPPED | 1 | 2026-09-07 00:10:33 CST | 2026-09-07 00:10:33 CST | reclaimed_entered | Paper entry triggered at 0.08898; quantity 15487.788. |
| `SUIUSDT` | ARCHIVED | 1 | 2026-09-07 00:10:34 CST | 2026-09-07 00:10:34 CST | archived | Archived because scan 1be61ae78f1e created a newer WATCHING plan for SUIUSDT. |
| `ADAUSDT` | CLOSED | 1 | 2026-09-07 00:10:35 CST | 2026-09-07 00:10:35 CST | reclaimed_entered | Paper entry triggered at 0.219; quantity 7670.7705. |
| `BNBUSDT` | WATCHING | 11 | 2026-09-07 00:10:35 CST | 2026-10-09 00:10:11 CST | still_waiting | Watching: entry zone touched, but 4h close has not reclaimed entry_high. |
| `SOLUSDT` | ENTERED | 1 | 2026-09-03 20:17:47 CST | 2026-09-03 20:17:47 CST | reclaimed_entered | Paper entry triggered at 104.48; quantity 9.1288769. |
| `BTCUSDT` | STOPPED | 8 | 2026-08-28 20:06:29 CST | 2026-09-07 00:10:31 CST | reclaimed_entered | Paper entry triggered at 79776.6; quantity 0.030225098. |
| `LINKUSDT` | WATCHING | 9 | 2026-08-28 20:06:30 CST | 2026-09-05 20:06:10 CST | still_waiting | Watching: price is above entry zone; waiting for pullback. |
| `ETHUSDT` | STOPPED | 2 | 2026-08-28 20:06:30 CST | 2026-09-03 20:17:49 CST | reclaimed_entered | Paper entry triggered at 2500.89; quantity 0.81652916. |
| `ENAUSDT` | ARCHIVED | 1 | 2026-08-27 20:07:47 CST | 2026-08-27 20:07:47 CST | archived | Archived because scan 23537861af20 created a newer WATCHING plan for ENAUSDT. |
| `ETHUSDT` | ARCHIVED | 1 | 2026-08-28 12:10:09 CST | 2026-08-28 12:10:09 CST | archived | Archived because scan 637752924d13 created a newer WATCHING plan for ETHUSDT. |
| `PEPEUSDT` | WATCHING | 37 | 2026-08-27 20:07:49 CST | 2026-10-09 00:10:10 CST | still_waiting | Watching: entry zone touched, but 4h close has not reclaimed entry_high. |
| `ZROUSDT` | STOPPED | 36 | 2026-08-26 20:06:43 CST | 2026-09-10 04:10:07 CST | reclaimed_entered | Paper entry triggered at 1.172; quantity 696.08799. |
| `BNBUSDT` | ARCHIVED | 4 | 2026-08-26 20:06:44 CST | 2026-08-27 12:10:11 CST | archived | Archived because scan 05233b4f12a0 created a newer WATCHING plan for BNBUSDT. |
| `SOLUSDT` | ARCHIVED | 6 | 2026-08-26 08:10:08 CST | 2026-08-27 04:10:10 CST | archived | Archived because scan 637752924d13 created a newer WATCHING plan for SOLUSDT. |
| `BTCUSDT` | ARCHIVED | 4 | 2026-08-26 08:10:09 CST | 2026-08-27 04:10:10 CST | archived | Archived because scan 637752924d13 created a newer WATCHING plan for BTCUSDT. |
| `TAOUSDT` | CLOSED | 2 | 2026-08-26 04:10:07 CST | 2026-08-26 08:10:08 CST | reclaimed_entered | Paper entry triggered at 233.7; quantity 4.3649062. |
| `TRXUSDT` | ENTERED | 8 | 2026-08-26 08:10:07 CST | 2026-08-27 20:07:45 CST | reclaimed_entered | Paper entry triggered at 0.3375; quantity 9196.2479. |
| `ETHUSDT` | ARCHIVED | 1 | 2026-08-18 12:10:06 CST | 2026-08-18 12:10:06 CST | archived | Archived because scan 110604e1204a created a newer WATCHING plan for ETHUSDT. |
| `ONDOUSDT` | WATCHING | 387 | 2026-06-11 20:47:37 CST | 2026-09-10 04:10:05 CST | still_waiting | Watching: price is above entry zone; waiting for pullback. |

## TP1 EMA Trailing Stop 追踪

| Metric | Value |
|---|---:|
| Activated events | 8 |
| Stop raise events | 56 |
| Stop exits from EMA trailing | 5 |
| Currently active trades | 0 |

## 本次 Run 状态变化

| Time | Event | Symbol | Old Status | New Status | Price | Old Stop | New Stop | Kline Time | Reason |
|---|---|---|---|---|---:|---:|---:|---|---|
| 2026-10-09 04:10:03 CST | API_DELAY_SKIPPED | `PEPEUSDT` | WATCHING | WATCHING | 3.77e-06 | 3.59525e-06 | 3.59525e-06 | 2026-10-08T20:10:27Z | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-10-09 04:10:03 CST | API_DELAY_SKIPPED | `TRXUSDT` | ENTERED | ENTERED | 0.33300 | 0.32663 | 0.32663 | 2026-10-08T20:10:27Z | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-10-09 04:10:03 CST | API_DELAY_SKIPPED | `DOGEUSDT` | WATCHING | WATCHING | 0.08308 | 0.08433 | 0.08433 | 2026-10-08T20:10:27Z | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-10-09 04:10:03 CST | API_DELAY_SKIPPED | `LINKUSDT` | WATCHING | WATCHING | 12.4140 | 10.9000 | 10.9000 | 2026-10-08T20:10:27Z | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-10-09 04:10:03 CST | API_DELAY_SKIPPED | `ENAUSDT` | WATCHING | WATCHING | 0.20470 | 0.15465 | 0.15465 | 2026-10-08T20:10:27Z | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-10-09 04:10:03 CST | API_DELAY_SKIPPED | `ONDOUSDT` | WATCHING | WATCHING | 0.44750 | 0.33845 | 0.33845 | 2026-10-08T20:10:27Z | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-10-09 04:10:03 CST | API_DELAY_SKIPPED | `HBARUSDT` | WATCHING | WATCHING | 0.08980 | 0.08324 | 0.08324 | 2026-10-08T20:10:27Z | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-10-09 04:10:03 CST | API_DELAY_SKIPPED | `SOLUSDT` | ENTERED | ENTERED | 108.69 | 93.5258 | 93.5258 | 2026-10-08T20:10:27Z | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-10-09 04:10:03 CST | API_DELAY_SKIPPED | `XRPUSDT` | WATCHING | WATCHING | 1.3504 | 1.3668 | 1.3668 | 2026-10-08T20:10:27Z | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-10-09 04:10:03 CST | API_DELAY_SKIPPED | `BNBUSDT` | WATCHING | WATCHING | 730.83 | 698.25 | 698.25 | 2026-10-08T20:10:27Z | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-10-09 04:10:03 CST | API_DELAY_SKIPPED | `LTCUSDT` | WATCHING | WATCHING | 62.0800 | 55.6821 | 55.6821 | 2026-10-08T20:10:27Z | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-10-09 04:10:03 CST | API_DELAY_SKIPPED | `SUIUSDT` | WATCHING | WATCHING | 1.0308 | 0.73629 | 0.73629 | 2026-10-08T20:10:27Z | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-10-09 04:10:03 CST | API_DELAY_SKIPPED | `AAVEUSDT` | ENTERED | ENTERED | 165.58 | 132.93 | 132.93 | 2026-10-08T20:10:27Z | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |

## 当前观察与持仓

| Status | Symbol | Last | Entry Zone | Entry | Stop | TP1 | TP2 | Qty | Unrealized | Notes |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| ENTERED | `AAVEUSDT` | 165.58 | 144.30 - 147.62 | 147.42 | 132.93 | 172.02 | 185.06 | 6.90 | 125.29 | Paper entry triggered inside entry zone. |
| WATCHING | `DOGEUSDT` | 0.08308 | 0.09675 - 0.09924 | n/a | 0.08433 | 0.12533 | 0.13900 | n/a | 0.00 | Watching: entry zone touched, but 4h close has not reclaimed entry_high. |
| WATCHING | `XRPUSDT` | 1.3504 | 1.5245 - 1.5546 | n/a | 1.3668 | 1.8849 | 2.0577 | n/a | 0.00 | Watching: entry zone touched, but 4h close has not reclaimed entry_high. |
| WATCHING | `HBARUSDT` | 0.08980 | 0.09281 - 0.09509 | n/a | 0.08324 | 0.11537 | 0.12608 | n/a | 0.00 | Watching: entry zone touched, but 4h close has not reclaimed entry_high. |
| WATCHING | `LTCUSDT` | 62.0800 | 59.4888 - 60.4671 | n/a | 55.6821 | 68.5698 | 72.8657 | n/a | 0.00 | Watching: price is above entry zone; waiting for pullback. |
| WATCHING | `SUIUSDT` | 1.0308 | 0.79279 - 0.80479 | n/a | 0.73629 | 0.92379 | 0.98630 | n/a | 0.00 | Watching: price is above entry zone; waiting for pullback. |
| WATCHING | `ENAUSDT` | 0.20470 | 0.16740 - 0.17167 | n/a | 0.15465 | 0.19931 | 0.21420 | n/a | 0.00 | Watching: price is above entry zone; waiting for pullback. |
| WATCHING | `BNBUSDT` | 730.83 | 741.35 - 747.76 | n/a | 698.25 | 837.17 | 883.47 | n/a | 0.00 | Watching: entry zone touched, but 4h close has not reclaimed entry_high. |
| ENTERED | `SOLUSDT` | 108.69 | 102.90 - 104.60 | 104.48 | 93.5258 | 124.20 | 134.42 | 9.13 | 38.43 | Paper entry triggered inside entry zone. |
| WATCHING | `LINKUSDT` | 12.4140 | 11.6712 - 11.8172 | n/a | 10.9000 | 13.4326 | 14.2767 | n/a | 0.00 | Watching: price is above entry zone; waiting for pullback. |
| WATCHING | `PEPEUSDT` | 3.77e-06 | 3.8806586e-06 - 3.93176e-06 | n/a | 3.59525e-06 | 4.5372e-06 | 4.8390871e-06 | n/a | 0.00 | Watching: entry zone touched, but 4h close has not reclaimed entry_high. |
| ENTERED | `TRXUSDT` | 0.33300 | 0.33688 - 0.33763 | 0.33750 | 0.32663 | 0.35851 | 0.37285 | 9,196.25 | -41.38 | Paper entry triggered inside entry zone. |
| WATCHING | `ONDOUSDT` | 0.44750 | 0.39450 - 0.41157 | n/a | 0.33845 | 0.53222 | 0.59681 | n/a | 0.00 | Watching: price is above entry zone; waiting for pullback. |

## 已结束交易

| Status | Symbol | Entry | Exit | Qty | Realized PnL | Source Scan | Notes |
|---|---|---:|---:|---:|---:|---|---|
| STOPPED | `DOGEUSDT` | 0.08898 | 0.09527 | 15,487.79 | 97.41 | 23537861af20 | EMA20 trailing stop hit. |
| ARCHIVED | `SUIUSDT` | n/a | n/a | n/a | 0.00 | 23537861af20 | Archived because scan 1be61ae78f1e created a newer WATCHING plan for SUIUSDT. |
| CLOSED | `ADAUSDT` | 0.21900 | 0.25241 | 7,670.77 | 256.25 | 23537861af20 | TP2 hit; paper trade closed. |
| ARCHIVED | `SUIUSDT` | n/a | n/a | n/a | 0.00 | 6da7db425dbd | Archived because scan 23537861af20 created a newer WATCHING plan for SUIUSDT. |
| STOPPED | `BTCUSDT` | 79,776.60 | 84,250.98 | 0.03 | 135.24 | 637752924d13 | EMA20 trailing stop hit. |
| STOPPED | `ETHUSDT` | 2,500.89 | 2,702.34 | 0.82 | 164.49 | 637752924d13 | EMA20 trailing stop hit. |
| ARCHIVED | `ENAUSDT` | n/a | n/a | n/a | 0.00 | 05233b4f12a0 | Archived because scan 23537861af20 created a newer WATCHING plan for ENAUSDT. |
| ARCHIVED | `ETHUSDT` | n/a | n/a | n/a | 0.00 | 05233b4f12a0 | Archived because scan 637752924d13 created a newer WATCHING plan for ETHUSDT. |
| STOPPED | `BNBUSDT` | 706.50 | 741.96 | 3.47 | 123.03 | 05233b4f12a0 | EMA20 trailing stop hit. |
| STOPPED | `ZROUSDT` | 1.1720 | 2.0939 | 696.09 | 641.70 | 6d047ae7c4f5 | EMA20 trailing stop hit. |
| ARCHIVED | `BNBUSDT` | n/a | n/a | n/a | 0.00 | 6d047ae7c4f5 | Archived because scan 05233b4f12a0 created a newer WATCHING plan for BNBUSDT. |
| ARCHIVED | `SOLUSDT` | n/a | n/a | n/a | 0.00 | 1480a9add8c9 | Archived because scan 637752924d13 created a newer WATCHING plan for SOLUSDT. |
| ARCHIVED | `BTCUSDT` | n/a | n/a | n/a | 0.00 | 1480a9add8c9 | Archived because scan 637752924d13 created a newer WATCHING plan for BTCUSDT. |
| CLOSED | `UNIUSDT` | 4.3370 | 6.1301 | 153.81 | 275.80 | ed103f737b70 | TP2 hit; paper trade closed. |
| CLOSED | `ETHUSDT` | 2,436.56 | 2,748.66 | 0.86 | 268.63 | ed103f737b70 | TP2 hit; paper trade closed. |
| CLOSED | `TAOUSDT` | 233.70 | 293.17 | 4.36 | 259.59 | ed103f737b70 | TP2 hit; paper trade closed. |
| ARCHIVED | `SOLUSDT` | n/a | n/a | n/a | 0.00 | ed103f737b70 | Archived because scan 1480a9add8c9 created a newer WATCHING plan for SOLUSDT. |
| ARCHIVED | `BTCUSDT` | n/a | n/a | n/a | 0.00 | ed103f737b70 | Archived because scan 1480a9add8c9 created a newer WATCHING plan for BTCUSDT. |
| ARCHIVED | `SOLUSDT` | n/a | n/a | n/a | 0.00 | 320bc0bceb6a | Archived because scan ed103f737b70 created a newer WATCHING plan for SOLUSDT. |
| ARCHIVED | `ETHUSDT` | n/a | n/a | n/a | 0.00 | 320bc0bceb6a | Archived because scan ed103f737b70 created a newer WATCHING plan for ETHUSDT. |
| ARCHIVED | `BTCUSDT` | n/a | n/a | n/a | 0.00 | 320bc0bceb6a | Archived because scan ed103f737b70 created a newer WATCHING plan for BTCUSDT. |
| ARCHIVED | `TRXUSDT` | n/a | n/a | n/a | 0.00 | 6a84e67a5013 | Archived because scan 2ee5c0fa058f created a newer WATCHING plan for TRXUSDT. |
| ARCHIVED | `ETHUSDT` | n/a | n/a | n/a | 0.00 | 110604e1204a | Archived because scan 320bc0bceb6a created a newer WATCHING plan for ETHUSDT. |
| ARCHIVED | `BTCUSDT` | n/a | n/a | n/a | 0.00 | 110604e1204a | Archived because scan 320bc0bceb6a created a newer WATCHING plan for BTCUSDT. |
| ARCHIVED | `SOLUSDT` | n/a | n/a | n/a | 0.00 | 110604e1204a | Archived because scan 320bc0bceb6a created a newer WATCHING plan for SOLUSDT. |
| ARCHIVED | `SOLUSDT` | n/a | n/a | n/a | 0.00 | 741093cc2c86 | Archived because scan 110604e1204a created a newer WATCHING plan for SOLUSDT. |
| ARCHIVED | `BTCUSDT` | n/a | n/a | n/a | 0.00 | 741093cc2c86 | Archived because scan 110604e1204a created a newer WATCHING plan for BTCUSDT. |
| ARCHIVED | `ETHUSDT` | n/a | n/a | n/a | 0.00 | d889ad7bd72e | Archived because scan 110604e1204a created a newer WATCHING plan for ETHUSDT. |
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

### AAVEUSDT `94119a9f7aee`

- 当前状态：`ENTERED`
- 来源扫描：`75c59fd5991f` rank 1

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-09-23 20:06:31 CST | ENTERED | 147.42 | 6.90 | 0.00 | 0.00 | Paper entry triggered at 147.42; quantity 6.8992876. |
| 2026-09-23 20:06:31 CST | PLAN_CREATED | 147.28 | n/a | 0.00 | 0.00 | Imported rank 1 from scan 75c59fd5991f; entry zone 144.29942-147.6174. |
| 2026-10-09 04:10:03 CST | API_DELAY_SKIPPED | 165.58 | 6.90 | 0.00 | 125.29 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |

### DOGEUSDT `e83962372405`

- 当前状态：`WATCHING`
- 来源扫描：`75c59fd5991f` rank 2

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-09-23 20:06:31 CST | PLAN_CREATED | 0.09920 | n/a | 0.00 | 0.00 | Imported rank 2 from scan 75c59fd5991f; entry zone 0.096753091-0.099237972. |
| 2026-09-24 00:10:20 CST | RECLAIM_PENDING_SET | 0.09319 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.09319) but 4h close 0.09277 < entry_high 0.09924; waiting for reclaim. |
| 2026-09-24 04:10:10 CST | RECLAIM_PENDING_SET | 0.09230 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.09230) but 4h close 0.09235 < entry_high 0.09924; waiting for reclaim. |
| 2026-09-24 08:10:07 CST | RECLAIM_PENDING_SET | 0.09269 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.09269) but 4h close 0.09272 < entry_high 0.09924; waiting for reclaim. |
| 2026-09-24 12:10:07 CST | RECLAIM_PENDING_SET | 0.09336 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.09336) but 4h close 0.09318 < entry_high 0.09924; waiting for reclaim. |
| 2026-10-09 00:10:13 CST | RECLAIM_PENDING_SET | 0.08308 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.08308) but 4h close 0.08266 < entry_high 0.09924; waiting for reclaim. |
| 2026-10-09 04:10:03 CST | API_DELAY_SKIPPED | 0.08308 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |

### XRPUSDT `d7619461e7f7`

- 当前状态：`WATCHING`
- 来源扫描：`75c59fd5991f` rank 3

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-09-23 20:06:31 CST | PLAN_CREATED | 1.5650 | n/a | 0.00 | 0.00 | Imported rank 3 from scan 75c59fd5991f; entry zone 1.5244605-1.5545527. |
| 2026-09-24 00:10:20 CST | RECLAIM_PENDING_SET | 1.5178 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.5178) but 4h close 1.5062 < entry_high 1.5546; waiting for reclaim. |
| 2026-09-24 04:10:10 CST | RECLAIM_PENDING_SET | 1.4922 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.4922) but 4h close 1.4938 < entry_high 1.5546; waiting for reclaim. |
| 2026-09-24 08:10:07 CST | RECLAIM_PENDING_SET | 1.5007 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.5007) but 4h close 1.5010 < entry_high 1.5546; waiting for reclaim. |
| 2026-09-24 12:10:08 CST | RECLAIM_PENDING_SET | 1.4929 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.4929) but 4h close 1.4942 < entry_high 1.5546; waiting for reclaim. |
| 2026-10-09 00:10:14 CST | RECLAIM_PENDING_SET | 1.3504 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.3504) but 4h close 1.3464 < entry_high 1.5546; waiting for reclaim. |
| 2026-10-09 04:10:03 CST | API_DELAY_SKIPPED | 1.3504 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |

### HBARUSDT `ed61c745d8b8`

- 当前状态：`WATCHING`
- 来源扫描：`75c59fd5991f` rank 4

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-09-23 20:06:31 CST | PLAN_CREATED | 0.09492 | n/a | 0.00 | 0.00 | Imported rank 4 from scan 75c59fd5991f; entry zone 0.092813717-0.09508746. |
| 2026-09-24 00:10:21 CST | RECLAIM_PENDING_SET | 0.09088 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.09088) but 4h close 0.08998 < entry_high 0.09509; waiting for reclaim. |
| 2026-09-24 04:10:10 CST | RECLAIM_PENDING_SET | 0.09031 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.09031) but 4h close 0.09029 < entry_high 0.09509; waiting for reclaim. |
| 2026-09-24 08:10:08 CST | RECLAIM_PENDING_SET | 0.09026 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.09026) but 4h close 0.09050 < entry_high 0.09509; waiting for reclaim. |
| 2026-09-24 12:10:08 CST | RECLAIM_PENDING_SET | 0.09063 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.09063) but 4h close 0.09067 < entry_high 0.09509; waiting for reclaim. |
| 2026-10-09 00:10:15 CST | RECLAIM_PENDING_SET | 0.08980 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.08980) but 4h close 0.08909 < entry_high 0.09509; waiting for reclaim. |
| 2026-10-09 04:10:03 CST | API_DELAY_SKIPPED | 0.08980 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |

### LTCUSDT `8be03a0ebd7e`

- 当前状态：`WATCHING`
- 来源扫描：`1f452162056b` rank 1

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-09-22 20:07:07 CST | PLAN_CREATED | 60.3600 | n/a | 0.00 | 0.00 | Imported rank 1 from scan 1f452162056b; entry zone 59.488823-60.467083. |
| 2026-09-22 20:07:11 CST | RECLAIM_PENDING_SET | 60.4000 | n/a | 0.00 | 0.00 | Entry zone touched (price=60.4000) but 4h close 60.4000 < entry_high 60.4671; waiting for reclaim. |
| 2026-09-24 00:10:19 CST | RECLAIM_PENDING_SET | 60.1600 | n/a | 0.00 | 0.00 | Entry zone touched (price=60.1600) but 4h close 59.4800 < entry_high 60.4671; waiting for reclaim. |
| 2026-10-09 04:10:03 CST | API_DELAY_SKIPPED | 62.0800 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |

### SUIUSDT `94043786e3ef`

- 当前状态：`WATCHING`
- 来源扫描：`1be61ae78f1e` rank 1

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-09-07 20:06:52 CST | PLAN_CREATED | 0.81050 | n/a | 0.00 | 0.00 | Imported rank 1 from scan 1be61ae78f1e; entry zone 0.79279113-0.80478872. |
| 2026-09-09 00:10:03 CST | API_DELAY_SKIPPED | 0.81330 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 04:10:05 CST | API_DELAY_SKIPPED | 0.81330 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 08:10:03 CST | API_DELAY_SKIPPED | 0.81330 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 12:10:02 CST | API_DELAY_SKIPPED | 0.81330 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 16:10:03 CST | API_DELAY_SKIPPED | 0.81330 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-10 00:10:25 CST | RECLAIM_PENDING_SET | 0.79360 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.79360) but 4h close 0.79450 < entry_high 0.80479; waiting for reclaim. |
| 2026-09-10 04:10:09 CST | RECLAIM_PENDING_SET | 0.78640 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.78640) but 4h close 0.78550 < entry_high 0.80479; waiting for reclaim. |
| 2026-10-09 04:10:03 CST | API_DELAY_SKIPPED | 1.0308 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |

### ENAUSDT `307336166337`

- 当前状态：`WATCHING`
- 来源扫描：`23537861af20` rank 1

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-09-06 20:13:07 CST | PLAN_CREATED | 0.17350 | n/a | 0.00 | 0.00 | Imported rank 1 from scan 23537861af20; entry zone 0.16739584-0.17167171. |
| 2026-09-07 00:10:32 CST | RECLAIM_PENDING_SET | 0.17120 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.17120) but 4h close 0.17150 < entry_high 0.17167; waiting for reclaim. |
| 2026-09-07 16:10:34 CST | RECLAIM_PENDING_SET | 0.17130 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.17130) but 4h close 0.17000 < entry_high 0.17167; waiting for reclaim. |
| 2026-09-07 20:07:01 CST | RECLAIM_PENDING_SET | 0.17010 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.17010) but 4h close 0.16980 < entry_high 0.17167; waiting for reclaim. |
| 2026-09-08 00:13:06 CST | RECLAIM_PENDING_SET | 0.16540 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.16540) but 4h close 0.16410 < entry_high 0.17167; waiting for reclaim. |
| 2026-09-08 04:10:11 CST | RECLAIM_PENDING_SET | 0.16500 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.16500) but 4h close 0.16640 < entry_high 0.17167; waiting for reclaim. |
| 2026-09-08 08:10:07 CST | RECLAIM_PENDING_SET | 0.16410 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.16410) but 4h close 0.16420 < entry_high 0.17167; waiting for reclaim. |
| 2026-09-08 12:10:26 CST | RECLAIM_PENDING_SET | 0.16430 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.16430) but 4h close 0.16420 < entry_high 0.17167; waiting for reclaim. |
| 2026-09-08 16:10:34 CST | RECLAIM_PENDING_SET | 0.16170 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.16170) but 4h close 0.16220 < entry_high 0.17167; waiting for reclaim. |
| 2026-09-09 00:10:03 CST | API_DELAY_SKIPPED | 0.16170 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 04:10:05 CST | API_DELAY_SKIPPED | 0.16170 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 08:10:03 CST | API_DELAY_SKIPPED | 0.16170 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 12:10:02 CST | API_DELAY_SKIPPED | 0.16170 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 16:10:03 CST | API_DELAY_SKIPPED | 0.16170 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-10 00:10:22 CST | RECLAIM_PENDING_SET | 0.15580 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.15580) but 4h close 0.15640 < entry_high 0.17167; waiting for reclaim. |
| 2026-09-10 04:10:08 CST | RECLAIM_PENDING_SET | 0.15360 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.15360) but 4h close 0.15280 < entry_high 0.17167; waiting for reclaim. |
| 2026-10-09 04:10:03 CST | API_DELAY_SKIPPED | 0.20470 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |

### DOGEUSDT `549cfdd6bdc4`

- 当前状态：`STOPPED`
- 来源扫描：`23537861af20` rank 2

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-09-06 20:13:07 CST | PLAN_CREATED | 0.08991 | n/a | 0.00 | 0.00 | Imported rank 2 from scan 23537861af20; entry zone 0.087811653-0.08911488. |
| 2026-09-07 00:10:33 CST | RECLAIM_PENDING_SET | 0.08883 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.08883) but 4h close 0.08897 < entry_high 0.08911; waiting for reclaim. |
| 2026-09-08 16:10:02 CST | RECLAIM_CONFIRMED_ENTERED | 0.08898 | 15,487.79 | 0.00 | 0.00 | Paper entry triggered at 0.08898; quantity 15487.788. |
| 2026-09-09 00:10:03 CST | API_DELAY_SKIPPED | 0.08898 | 15,487.79 | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 04:10:05 CST | API_DELAY_SKIPPED | 0.08898 | 15,487.79 | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 08:10:03 CST | API_DELAY_SKIPPED | 0.08898 | 15,487.79 | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 12:10:02 CST | API_DELAY_SKIPPED | 0.08898 | 15,487.79 | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 16:10:03 CST | API_DELAY_SKIPPED | 0.08898 | 15,487.79 | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-22 12:10:06 CST | TP1_EMA_TRAILING_ACTIVATED | 0.09149 | 15,487.79 | 0.00 | 239.91 | EMA20 trailing stop activated at 0.09148501. |
| 2026-09-22 12:10:06 CST | TP1_HIT | 0.10034 | 15,487.79 | 0.00 | 239.91 | TP1 hit at 0.1003432; trade remains open. |
| 2026-09-22 16:10:03 CST | TP1_EMA_TRAILING_RAISED | 0.09199 | 15,487.79 | 0.00 | 157.51 | EMA20 trailing stop raised from 0.09148501 to 0.091988557. |
| 2026-09-22 20:07:07 CST | TP1_EMA_TRAILING_RAISED | 0.09233 | 15,487.79 | 0.00 | 141.25 | EMA20 trailing stop raised from 0.091988557 to 0.092331096. |
| 2026-09-23 00:10:03 CST | TP1_EMA_TRAILING_RAISED | 0.09277 | 15,487.79 | 0.00 | 163.86 | EMA20 trailing stop raised from 0.092331096 to 0.092770716. |
| 2026-09-23 04:10:03 CST | TP1_EMA_TRAILING_RAISED | 0.09313 | 15,487.79 | 0.00 | 167.89 | EMA20 trailing stop raised from 0.092770716 to 0.093129661. |
| 2026-09-23 08:10:03 CST | TP1_EMA_TRAILING_RAISED | 0.09365 | 15,487.79 | 0.00 | 177.49 | EMA20 trailing stop raised from 0.093129661 to 0.093649345. |
| 2026-09-23 12:10:05 CST | TP1_EMA_TRAILING_RAISED | 0.09450 | 15,487.79 | 0.00 | 229.37 | EMA20 trailing stop raised from 0.093649345 to 0.094497941. |
| 2026-09-23 16:10:03 CST | TP1_EMA_TRAILING_RAISED | 0.09499 | 15,487.79 | 0.00 | 183.99 | EMA20 trailing stop raised from 0.094497941 to 0.094987053. |
| 2026-09-23 20:06:31 CST | TP1_EMA_TRAILING_RAISED | 0.09527 | 15,487.79 | 0.00 | 159.68 | EMA20 trailing stop raised from 0.094987053 to 0.095269728. |
| 2026-09-24 00:10:05 CST | EMA_TRAILING_STOPPED | 0.09527 | 15,487.79 | 97.41 | 0.00 | EMA20 trailing stop hit at 0.095269728. |

### SUIUSDT `ae8588dfe3b4`

- 当前状态：`ARCHIVED`
- 来源扫描：`23537861af20` rank 3

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-09-06 20:13:07 CST | PLAN_CREATED | 0.80580 | n/a | 0.00 | 0.00 | Imported rank 3 from scan 23537861af20; entry zone 0.78371849-0.79525418. |
| 2026-09-07 00:10:34 CST | RECLAIM_PENDING_SET | 0.79110 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.79110) but 4h close 0.79230 < entry_high 0.79525; waiting for reclaim. |
| 2026-09-07 20:06:52 CST | ARCHIVED | 0.81050 | n/a | 0.00 | 0.00 | Archived because scan 1be61ae78f1e created a newer WATCHING plan for SUIUSDT. |

### ADAUSDT `2d74b7ff6191`

- 当前状态：`CLOSED`
- 来源扫描：`23537861af20` rank 4

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-09-06 20:13:07 CST | PLAN_CREATED | 0.22100 | n/a | 0.00 | 0.00 | Imported rank 4 from scan 23537861af20; entry zone 0.21609244-0.21905612. |
| 2026-09-07 00:10:35 CST | RECLAIM_PENDING_SET | 0.21750 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.21750) but 4h close 0.21750 < entry_high 0.21906; waiting for reclaim. |
| 2026-09-07 04:10:03 CST | RECLAIM_CONFIRMED_ENTERED | 0.21900 | 7,670.77 | 0.00 | 0.00 | Paper entry triggered at 0.219; quantity 7670.7705. |
| 2026-09-09 00:10:03 CST | API_DELAY_SKIPPED | 0.21630 | 7,670.77 | 0.00 | -20.71 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 04:10:05 CST | API_DELAY_SKIPPED | 0.21630 | 7,670.77 | 0.00 | -20.71 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 08:10:03 CST | API_DELAY_SKIPPED | 0.21630 | 7,670.77 | 0.00 | -20.71 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 12:10:02 CST | API_DELAY_SKIPPED | 0.21630 | 7,670.77 | 0.00 | -20.71 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 16:10:03 CST | API_DELAY_SKIPPED | 0.21630 | 7,670.77 | 0.00 | -20.71 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-22 00:10:04 CST | TP1_EMA_TRAILING_ACTIVATED | 0.22685 | 7,670.77 | 0.00 | 197.14 | EMA20 trailing stop activated at 0.22685284. |
| 2026-09-22 00:10:04 CST | TP1_HIT | 0.24080 | 7,670.77 | 0.00 | 197.14 | TP1 hit at 0.24079584; trade remains open. |
| 2026-09-22 04:10:03 CST | TP1_EMA_TRAILING_RAISED | 0.22889 | 7,670.77 | 0.00 | 195.60 | EMA20 trailing stop raised from 0.22685284 to 0.22888868. |
| 2026-09-22 08:10:04 CST | TP1_EMA_TRAILING_RAISED | 0.23082 | 7,670.77 | 0.00 | 196.37 | EMA20 trailing stop raised from 0.22888868 to 0.23081633. |
| 2026-09-22 12:10:06 CST | TP1_EMA_TRAILING_RAISED | 0.23219 | 7,670.77 | 0.00 | 237.03 | EMA20 trailing stop raised from 0.23081633 to 0.23219052. |
| 2026-09-22 16:10:03 CST | TP1_EMA_TRAILING_RAISED | 0.23324 | 7,670.77 | 0.00 | 207.11 | EMA20 trailing stop raised from 0.23219052 to 0.23324334. |
| 2026-09-22 20:07:07 CST | TP1_EMA_TRAILING_RAISED | 0.23436 | 7,670.77 | 0.00 | 204.81 | EMA20 trailing stop raised from 0.23324334 to 0.23435674. |
| 2026-09-23 00:10:03 CST | TP1_EMA_TRAILING_RAISED | 0.23584 | 7,670.77 | 0.00 | 234.73 | EMA20 trailing stop raised from 0.23435674 to 0.23583928. |
| 2026-09-23 04:10:03 CST | TP1_EMA_TRAILING_RAISED | 0.23714 | 7,670.77 | 0.00 | 250.07 | EMA20 trailing stop raised from 0.23583928 to 0.23713698. |
| 2026-09-23 08:10:03 CST | TP1_EMA_TRAILING_RAISED | 0.23856 | 7,670.77 | 256.25 | 0.00 | EMA20 trailing stop raised from 0.23713698 to 0.23855728. |
| 2026-09-23 08:10:03 CST | TP2_HIT | 0.25241 | 7,670.77 | 256.25 | 0.00 | TP2 hit at 0.25240662; trade closed. |

### BNBUSDT `cf227f0cc559`

- 当前状态：`WATCHING`
- 来源扫描：`23537861af20` rank 5

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-09-06 20:13:07 CST | PLAN_CREATED | 757.33 | n/a | 0.00 | 0.00 | Imported rank 5 from scan 23537861af20; entry zone 741.34995-747.75671. |
| 2026-09-07 00:10:35 CST | RECLAIM_PENDING_SET | 745.33 | n/a | 0.00 | 0.00 | Entry zone touched (price=745.33) but 4h close 745.97 < entry_high 747.76; waiting for reclaim. |
| 2026-09-07 12:10:35 CST | RECLAIM_PENDING_SET | 746.43 | n/a | 0.00 | 0.00 | Entry zone touched (price=746.43) but 4h close 746.31 < entry_high 747.76; waiting for reclaim. |
| 2026-09-07 16:10:35 CST | RECLAIM_PENDING_SET | 745.39 | n/a | 0.00 | 0.00 | Entry zone touched (price=745.39) but 4h close 743.87 < entry_high 747.76; waiting for reclaim. |
| 2026-09-07 20:07:02 CST | RECLAIM_PENDING_SET | 745.73 | n/a | 0.00 | 0.00 | Entry zone touched (price=745.73) but 4h close 744.95 < entry_high 747.76; waiting for reclaim. |
| 2026-09-08 00:13:07 CST | RECLAIM_PENDING_SET | 736.45 | n/a | 0.00 | 0.00 | Entry zone touched (price=736.45) but 4h close 734.60 < entry_high 747.76; waiting for reclaim. |
| 2026-09-08 04:10:12 CST | RECLAIM_PENDING_SET | 740.38 | n/a | 0.00 | 0.00 | Entry zone touched (price=740.38) but 4h close 741.90 < entry_high 747.76; waiting for reclaim. |
| 2026-09-08 08:10:08 CST | RECLAIM_PENDING_SET | 739.51 | n/a | 0.00 | 0.00 | Entry zone touched (price=739.51) but 4h close 739.98 < entry_high 747.76; waiting for reclaim. |
| 2026-09-08 12:10:27 CST | RECLAIM_PENDING_SET | 743.08 | n/a | 0.00 | 0.00 | Entry zone touched (price=743.08) but 4h close 742.91 < entry_high 747.76; waiting for reclaim. |
| 2026-09-09 00:10:03 CST | API_DELAY_SKIPPED | 756.52 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 04:10:05 CST | API_DELAY_SKIPPED | 756.52 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 08:10:03 CST | API_DELAY_SKIPPED | 756.52 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 12:10:02 CST | API_DELAY_SKIPPED | 756.52 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 16:10:03 CST | API_DELAY_SKIPPED | 756.52 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-10 00:10:24 CST | RECLAIM_PENDING_SET | 738.98 | n/a | 0.00 | 0.00 | Entry zone touched (price=738.98) but 4h close 739.11 < entry_high 747.76; waiting for reclaim. |
| 2026-09-10 04:10:09 CST | RECLAIM_PENDING_SET | 737.61 | n/a | 0.00 | 0.00 | Entry zone touched (price=737.61) but 4h close 737.24 < entry_high 747.76; waiting for reclaim. |
| 2026-10-09 00:10:11 CST | RECLAIM_PENDING_SET | 730.83 | n/a | 0.00 | 0.00 | Entry zone touched (price=730.83) but 4h close 731.42 < entry_high 747.76; waiting for reclaim. |
| 2026-10-09 04:10:03 CST | API_DELAY_SKIPPED | 730.83 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |

### SUIUSDT `76b257687bae`

- 当前状态：`ARCHIVED`
- 来源扫描：`6da7db425dbd` rank 1

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-09-05 20:06:06 CST | PLAN_CREATED | 0.78590 | n/a | 0.00 | 0.00 | Imported rank 1 from scan 6da7db425dbd; entry zone 0.76708616-0.77871005. |
| 2026-09-06 20:13:07 CST | ARCHIVED | 0.79490 | n/a | 0.00 | 0.00 | Archived because scan 23537861af20 created a newer WATCHING plan for SUIUSDT. |

### SOLUSDT `d058835e1b0f`

- 当前状态：`ENTERED`
- 来源扫描：`637752924d13` rank 1

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-28 20:06:24 CST | PLAN_CREATED | 105.92 | n/a | 0.00 | 0.00 | Imported rank 1 from scan 637752924d13; entry zone 102.90071-104.59832. |
| 2026-09-03 20:17:47 CST | RECLAIM_PENDING_SET | 100.95 | n/a | 0.00 | 0.00 | Entry zone touched (price=100.95) but 4h close 100.81 < entry_high 104.60; waiting for reclaim. |
| 2026-09-04 00:10:04 CST | RECLAIM_CONFIRMED_ENTERED | 104.48 | 9.13 | 0.00 | 0.00 | Paper entry triggered at 104.48; quantity 9.1288769. |
| 2026-09-09 00:10:03 CST | API_DELAY_SKIPPED | 102.62 | 9.13 | 0.00 | -16.98 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 04:10:05 CST | API_DELAY_SKIPPED | 102.62 | 9.13 | 0.00 | -16.98 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 08:10:03 CST | API_DELAY_SKIPPED | 102.62 | 9.13 | 0.00 | -16.98 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 12:10:02 CST | API_DELAY_SKIPPED | 102.62 | 9.13 | 0.00 | -16.98 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 16:10:03 CST | API_DELAY_SKIPPED | 102.62 | 9.13 | 0.00 | -16.98 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-10-09 04:10:03 CST | API_DELAY_SKIPPED | 108.69 | 9.13 | 0.00 | 38.43 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |

### BTCUSDT `5ff6dab72dfa`

- 当前状态：`STOPPED`
- 来源扫描：`637752924d13` rank 2

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-28 20:06:24 CST | PLAN_CREATED | 79,611.74 | n/a | 0.00 | 0.00 | Imported rank 2 from scan 637752924d13; entry zone 79333.435-79814.717. |
| 2026-08-28 20:06:29 CST | RECLAIM_PENDING_SET | 79,668.66 | n/a | 0.00 | 0.00 | Entry zone touched (price=79,668.66) but 4h close 79,604.13 < entry_high 79,814.72; waiting for reclaim. |
| 2026-09-03 20:17:48 CST | RECLAIM_PENDING_SET | 78,070.01 | n/a | 0.00 | 0.00 | Entry zone touched (price=78,070.01) but 4h close 77,948.39 < entry_high 79,814.72; waiting for reclaim. |
| 2026-09-05 00:12:09 CST | RECLAIM_PENDING_SET | 79,458.00 | n/a | 0.00 | 0.00 | Entry zone touched (price=79,458.00) but 4h close 79,429.33 < entry_high 79,814.72; waiting for reclaim. |
| 2026-09-05 08:10:14 CST | RECLAIM_PENDING_SET | 79,649.99 | n/a | 0.00 | 0.00 | Entry zone touched (price=79,649.99) but 4h close 79,660.77 < entry_high 79,814.72; waiting for reclaim. |
| 2026-09-05 12:10:32 CST | RECLAIM_PENDING_SET | 79,547.28 | n/a | 0.00 | 0.00 | Entry zone touched (price=79,547.28) but 4h close 79,582.00 < entry_high 79,814.72; waiting for reclaim. |
| 2026-09-05 16:10:11 CST | RECLAIM_PENDING_SET | 79,645.29 | n/a | 0.00 | 0.00 | Entry zone touched (price=79,645.29) but 4h close 79,709.96 < entry_high 79,814.72; waiting for reclaim. |
| 2026-09-05 20:06:10 CST | RECLAIM_PENDING_SET | 79,654.20 | n/a | 0.00 | 0.00 | Entry zone touched (price=79,654.20) but 4h close 79,609.28 < entry_high 79,814.72; waiting for reclaim. |
| 2026-09-07 00:10:31 CST | RECLAIM_PENDING_SET | 79,631.20 | n/a | 0.00 | 0.00 | Entry zone touched (price=79,631.20) but 4h close 79,716.50 < entry_high 79,814.72; waiting for reclaim. |
| 2026-09-07 04:10:03 CST | RECLAIM_CONFIRMED_ENTERED | 79,776.60 | 0.03 | 0.00 | 0.00 | Paper entry triggered at 79776.6; quantity 0.030225098. |
| 2026-09-09 00:10:03 CST | API_DELAY_SKIPPED | 78,347.44 | 0.03 | 0.00 | -43.20 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 04:10:05 CST | API_DELAY_SKIPPED | 78,347.44 | 0.03 | 0.00 | -43.20 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 08:10:03 CST | API_DELAY_SKIPPED | 78,347.44 | 0.03 | 0.00 | -43.20 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 12:10:02 CST | API_DELAY_SKIPPED | 78,347.44 | 0.03 | 0.00 | -43.20 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 16:10:03 CST | API_DELAY_SKIPPED | 78,347.44 | 0.03 | 0.00 | -43.20 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-22 04:10:03 CST | TP1_EMA_TRAILING_ACTIVATED | 81,840.20 | 0.03 | 0.00 | 209.35 | EMA20 trailing stop activated at 81840.197. |
| 2026-09-22 04:10:03 CST | TP1_HIT | 85,786.05 | 0.03 | 0.00 | 209.35 | TP1 hit at 85786.045; trade remains open. |
| 2026-09-22 08:10:04 CST | TP1_EMA_TRAILING_RAISED | 82,383.23 | 0.03 | 0.00 | 198.57 | EMA20 trailing stop raised from 81840.197 to 82383.227. |
| 2026-09-22 12:10:06 CST | TP1_EMA_TRAILING_RAISED | 82,674.77 | 0.03 | 0.00 | 176.50 | EMA20 trailing stop raised from 82383.227 to 82674.768. |
| 2026-09-22 16:10:03 CST | TP1_EMA_TRAILING_RAISED | 82,883.83 | 0.03 | 0.00 | 172.93 | EMA20 trailing stop raised from 82674.768 to 82883.834. |
| 2026-09-22 20:07:07 CST | TP1_EMA_TRAILING_RAISED | 83,134.24 | 0.03 | 0.00 | 187.98 | EMA20 trailing stop raised from 82883.834 to 83134.239. |
| 2026-09-23 00:10:03 CST | TP1_EMA_TRAILING_RAISED | 83,335.13 | 0.03 | 0.00 | 196.20 | EMA20 trailing stop raised from 83134.239 to 83335.127. |
| 2026-09-23 04:10:03 CST | TP1_EMA_TRAILING_RAISED | 83,526.73 | 0.03 | 0.00 | 194.94 | EMA20 trailing stop raised from 83335.127 to 83526.727. |
| 2026-09-23 08:10:03 CST | TP1_EMA_TRAILING_RAISED | 83,737.26 | 0.03 | 0.00 | 195.20 | EMA20 trailing stop raised from 83526.727 to 83737.261. |
| 2026-09-23 12:10:05 CST | TP1_EMA_TRAILING_RAISED | 83,961.26 | 0.03 | 0.00 | 213.62 | EMA20 trailing stop raised from 83737.261 to 83961.259. |
| 2026-09-23 16:10:03 CST | TP1_EMA_TRAILING_RAISED | 84,112.48 | 0.03 | 0.00 | 193.95 | EMA20 trailing stop raised from 83961.259 to 84112.483. |
| 2026-09-23 20:06:31 CST | TP1_EMA_TRAILING_RAISED | 84,220.94 | 0.03 | 0.00 | 173.32 | EMA20 trailing stop raised from 84112.483 to 84220.943. |
| 2026-09-24 12:10:03 CST | EMA_TRAILING_STOPPED | 84,250.98 | 0.03 | 135.24 | 0.00 | EMA20 trailing stop hit at 84250.979. |
| 2026-09-24 12:10:03 CST | TP1_EMA_TRAILING_RAISED | 84,250.98 | 0.03 | 135.24 | 0.00 | EMA20 trailing stop raised from 84220.943 to 84250.979. |

### LINKUSDT `fb831c92566e`

- 当前状态：`WATCHING`
- 来源扫描：`637752924d13` rank 3

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-28 20:06:24 CST | PLAN_CREATED | 11.7830 | n/a | 0.00 | 0.00 | Imported rank 3 from scan 637752924d13; entry zone 11.671214-11.817168. |
| 2026-08-28 20:06:30 CST | RECLAIM_PENDING_SET | 11.7910 | n/a | 0.00 | 0.00 | Entry zone touched (price=11.7910) but 4h close 11.7820 < entry_high 11.8172; waiting for reclaim. |
| 2026-09-03 20:17:49 CST | RECLAIM_PENDING_SET | 11.2960 | n/a | 0.00 | 0.00 | Entry zone touched (price=11.2960) but 4h close 11.2720 < entry_high 11.8172; waiting for reclaim. |
| 2026-09-04 00:10:48 CST | RECLAIM_PENDING_SET | 11.7160 | n/a | 0.00 | 0.00 | Entry zone touched (price=11.7160) but 4h close 11.7820 < entry_high 11.8172; waiting for reclaim. |
| 2026-09-05 00:12:40 CST | RECLAIM_PENDING_SET | 11.6670 | n/a | 0.00 | 0.00 | Entry zone touched (price=11.6670) but 4h close 11.6570 < entry_high 11.8172; waiting for reclaim. |
| 2026-09-05 04:10:23 CST | RECLAIM_PENDING_SET | 11.7090 | n/a | 0.00 | 0.00 | Entry zone touched (price=11.7090) but 4h close 11.7120 < entry_high 11.8172; waiting for reclaim. |
| 2026-09-05 08:10:14 CST | RECLAIM_PENDING_SET | 11.6210 | n/a | 0.00 | 0.00 | Entry zone touched (price=11.6210) but 4h close 11.6320 < entry_high 11.8172; waiting for reclaim. |
| 2026-09-05 12:10:32 CST | RECLAIM_PENDING_SET | 11.6530 | n/a | 0.00 | 0.00 | Entry zone touched (price=11.6530) but 4h close 11.6690 < entry_high 11.8172; waiting for reclaim. |
| 2026-09-05 16:10:11 CST | RECLAIM_PENDING_SET | 11.7280 | n/a | 0.00 | 0.00 | Entry zone touched (price=11.7280) but 4h close 11.7420 < entry_high 11.8172; waiting for reclaim. |
| 2026-09-05 20:06:10 CST | RECLAIM_PENDING_SET | 11.7340 | n/a | 0.00 | 0.00 | Entry zone touched (price=11.7340) but 4h close 11.7240 < entry_high 11.8172; waiting for reclaim. |
| 2026-09-09 00:10:03 CST | API_DELAY_SKIPPED | 12.6300 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 04:10:05 CST | API_DELAY_SKIPPED | 12.6300 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 08:10:03 CST | API_DELAY_SKIPPED | 12.6300 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 12:10:02 CST | API_DELAY_SKIPPED | 12.6300 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 16:10:03 CST | API_DELAY_SKIPPED | 12.6300 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-10-09 04:10:03 CST | API_DELAY_SKIPPED | 12.4140 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |

### ETHUSDT `4f2f0f1fa0e7`

- 当前状态：`STOPPED`
- 来源扫描：`637752924d13` rank 4

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-28 20:06:24 CST | PLAN_CREATED | 2,505.00 | n/a | 0.00 | 0.00 | Imported rank 4 from scan 637752924d13; entry zone 2490.3307-2511.2475. |
| 2026-08-28 20:06:30 CST | RECLAIM_PENDING_SET | 2,506.51 | n/a | 0.00 | 0.00 | Entry zone touched (price=2,506.51) but 4h close 2,505.10 < entry_high 2,511.25; waiting for reclaim. |
| 2026-09-03 20:17:49 CST | RECLAIM_PENDING_SET | 2,410.88 | n/a | 0.00 | 0.00 | Entry zone touched (price=2,410.88) but 4h close 2,407.20 < entry_high 2,511.25; waiting for reclaim. |
| 2026-09-04 00:10:04 CST | RECLAIM_CONFIRMED_ENTERED | 2,500.89 | 0.82 | 0.00 | 0.00 | Paper entry triggered at 2500.89; quantity 0.81652916. |
| 2026-09-09 00:10:03 CST | API_DELAY_SKIPPED | 2,470.77 | 0.82 | 0.00 | -24.59 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 04:10:05 CST | API_DELAY_SKIPPED | 2,470.77 | 0.82 | 0.00 | -24.59 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 08:10:03 CST | API_DELAY_SKIPPED | 2,470.77 | 0.82 | 0.00 | -24.59 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 12:10:02 CST | API_DELAY_SKIPPED | 2,470.77 | 0.82 | 0.00 | -24.59 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 16:10:03 CST | API_DELAY_SKIPPED | 2,470.77 | 0.82 | 0.00 | -24.59 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-22 00:10:04 CST | TP1_EMA_TRAILING_ACTIVATED | 2,622.91 | 0.82 | 0.00 | 201.38 | EMA20 trailing stop activated at 2622.9135. |
| 2026-09-22 00:10:04 CST | TP1_HIT | 2,745.53 | 0.82 | 0.00 | 201.38 | TP1 hit at 2745.5265; trade remains open. |
| 2026-09-22 04:10:03 CST | TP1_EMA_TRAILING_RAISED | 2,638.05 | 0.82 | 0.00 | 220.10 | EMA20 trailing stop raised from 2622.9135 to 2638.0495. |
| 2026-09-22 08:10:04 CST | TP1_EMA_TRAILING_RAISED | 2,653.99 | 0.82 | 0.00 | 220.65 | EMA20 trailing stop raised from 2638.0495 to 2653.99. |
| 2026-09-22 12:10:06 CST | TP1_EMA_TRAILING_RAISED | 2,662.61 | 0.82 | 0.00 | 193.48 | EMA20 trailing stop raised from 2653.99 to 2662.6073. |
| 2026-09-22 16:10:03 CST | TP1_EMA_TRAILING_RAISED | 2,668.66 | 0.82 | 0.00 | 189.25 | EMA20 trailing stop raised from 2662.6073 to 2668.6612. |
| 2026-09-22 20:07:07 CST | TP1_EMA_TRAILING_RAISED | 2,675.73 | 0.82 | 0.00 | 199.52 | EMA20 trailing stop raised from 2668.6612 to 2675.7275. |
| 2026-09-23 00:10:03 CST | TP1_EMA_TRAILING_RAISED | 2,680.08 | 0.82 | 0.00 | 193.44 | EMA20 trailing stop raised from 2675.7275 to 2680.0756. |
| 2026-09-23 04:10:03 CST | TP1_EMA_TRAILING_RAISED | 2,684.71 | 0.82 | 0.00 | 203.76 | EMA20 trailing stop raised from 2680.0756 to 2684.712. |
| 2026-09-23 08:10:03 CST | TP1_EMA_TRAILING_RAISED | 2,690.64 | 0.82 | 0.00 | 205.41 | EMA20 trailing stop raised from 2684.712 to 2690.642. |
| 2026-09-23 12:10:05 CST | TP1_EMA_TRAILING_RAISED | 2,697.55 | 0.82 | 0.00 | 224.77 | EMA20 trailing stop raised from 2690.642 to 2697.5503. |
| 2026-09-23 16:10:03 CST | TP1_EMA_TRAILING_RAISED | 2,700.96 | 0.82 | 0.00 | 197.79 | EMA20 trailing stop raised from 2697.5503 to 2700.9638. |
| 2026-09-23 20:06:31 CST | TP1_EMA_TRAILING_RAISED | 2,702.34 | 0.82 | 0.00 | 182.47 | EMA20 trailing stop raised from 2700.9638 to 2702.3371. |
| 2026-09-24 00:10:05 CST | EMA_TRAILING_STOPPED | 2,702.34 | 0.82 | 164.49 | 0.00 | EMA20 trailing stop hit at 2702.3371. |

### ENAUSDT `f5274549c775`

- 当前状态：`ARCHIVED`
- 来源扫描：`05233b4f12a0` rank 1

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-27 20:07:42 CST | PLAN_CREATED | 0.14730 | n/a | 0.00 | 0.00 | Imported rank 1 from scan 05233b4f12a0; entry zone 0.14727305-0.1477419. |
| 2026-08-27 20:07:47 CST | RECLAIM_PENDING_SET | 0.14710 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.14710) but 4h close 0.14770 < entry_high 0.14774; waiting for reclaim. |
| 2026-09-06 20:13:07 CST | ARCHIVED | 0.17410 | n/a | 0.00 | 0.00 | Archived because scan 23537861af20 created a newer WATCHING plan for ENAUSDT. |

### ETHUSDT `172fa3911e40`

- 当前状态：`ARCHIVED`
- 来源扫描：`05233b4f12a0` rank 2

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-27 20:07:42 CST | PLAN_CREATED | 2,502.40 | n/a | 0.00 | 0.00 | Imported rank 2 from scan 05233b4f12a0; entry zone 2475.46-2496.0359. |
| 2026-08-28 12:10:09 CST | RECLAIM_PENDING_SET | 2,481.56 | n/a | 0.00 | 0.00 | Entry zone touched (price=2,481.56) but 4h close 2,489.92 < entry_high 2,496.04; waiting for reclaim. |
| 2026-08-28 20:06:24 CST | ARCHIVED | 2,499.13 | n/a | 0.00 | 0.00 | Archived because scan 637752924d13 created a newer WATCHING plan for ETHUSDT. |

### BNBUSDT `d6075516aea8`

- 当前状态：`STOPPED`
- 来源扫描：`05233b4f12a0` rank 3

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-27 20:07:42 CST | ENTERED | 706.50 | 3.47 | 0.00 | 0.00 | Paper entry triggered at 706.5; quantity 3.4698126. |
| 2026-08-27 20:07:42 CST | PLAN_CREATED | 707.02 | n/a | 0.00 | 0.00 | Imported rank 3 from scan 05233b4f12a0; entry zone 701.97004-706.52041. |
| 2026-09-06 09:36:06 CST | TP1_EMA_TRAILING_ACTIVATED | 727.66 | 3.47 | 0.00 | 206.28 | EMA20 trailing stop activated at 727.65551. |
| 2026-09-06 09:36:06 CST | TP1_HIT | 757.38 | 3.47 | 0.00 | 206.28 | TP1 hit at 757.37568; trade remains open. |
| 2026-09-06 12:10:04 CST | TP1_EMA_TRAILING_RAISED | 730.75 | 3.47 | 0.00 | 202.15 | EMA20 trailing stop raised from 727.65551 to 730.7508. |
| 2026-09-06 16:10:02 CST | TP1_EMA_TRAILING_RAISED | 732.28 | 3.47 | 0.00 | 174.15 | EMA20 trailing stop raised from 730.7508 to 732.28361. |
| 2026-09-06 20:13:07 CST | TP1_EMA_TRAILING_RAISED | 734.11 | 3.47 | 0.00 | 178.42 | EMA20 trailing stop raised from 732.28361 to 734.11296. |
| 2026-09-07 00:10:03 CST | TP1_EMA_TRAILING_RAISED | 734.97 | 3.47 | 0.00 | 134.73 | EMA20 trailing stop raised from 734.11296 to 734.96791. |
| 2026-09-07 04:10:03 CST | TP1_EMA_TRAILING_RAISED | 736.38 | 3.47 | 0.00 | 149.41 | EMA20 trailing stop raised from 734.96791 to 736.38281. |
| 2026-09-07 08:10:03 CST | TP1_EMA_TRAILING_RAISED | 738.45 | 3.47 | 0.00 | 168.56 | EMA20 trailing stop raised from 736.38281 to 738.45185. |
| 2026-09-07 12:10:04 CST | TP1_EMA_TRAILING_RAISED | 739.73 | 3.47 | 0.00 | 138.55 | EMA20 trailing stop raised from 738.45185 to 739.7279. |
| 2026-09-07 16:10:02 CST | TP1_EMA_TRAILING_RAISED | 741.05 | 3.47 | 0.00 | 134.94 | EMA20 trailing stop raised from 739.7279 to 741.05186. |
| 2026-09-07 20:06:52 CST | TP1_EMA_TRAILING_RAISED | 741.96 | 3.47 | 0.00 | 136.12 | EMA20 trailing stop raised from 741.05186 to 741.95716. |
| 2026-09-08 00:10:03 CST | EMA_TRAILING_STOPPED | 741.96 | 3.47 | 123.03 | 0.00 | EMA20 trailing stop hit at 741.95716. |

### PEPEUSDT `6602caabf17a`

- 当前状态：`WATCHING`
- 来源扫描：`05233b4f12a0` rank 4

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-27 20:07:42 CST | PLAN_CREATED | 3.92e-06 | n/a | 0.00 | 0.00 | Imported rank 4 from scan 05233b4f12a0; entry zone 3.8806586e-06-3.93176e-06. |
| 2026-08-27 20:07:49 CST | RECLAIM_PENDING_SET | 3.93e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.93e-06) but 4h close 3.91e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-08-28 00:10:20 CST | RECLAIM_PENDING_SET | 3.92e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.92e-06) but 4h close 3.92e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-08-28 04:10:08 CST | RECLAIM_PENDING_SET | 3.91e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.91e-06) but 4h close 3.92e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-08-28 08:10:07 CST | RECLAIM_PENDING_SET | 3.86e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.86e-06) but 4h close 3.9e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-08-28 12:10:10 CST | RECLAIM_PENDING_SET | 3.8e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.8e-06) but 4h close 3.81e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-08-28 16:10:13 CST | RECLAIM_PENDING_SET | 3.8e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.8e-06) but 4h close 3.79e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-08-28 20:06:29 CST | RECLAIM_PENDING_SET | 3.8e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.8e-06) but 4h close 3.8e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-03 20:17:46 CST | RECLAIM_PENDING_SET | 3.49e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.49e-06) but 4h close 3.49e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-04 00:10:43 CST | RECLAIM_PENDING_SET | 3.83e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.83e-06) but 4h close 3.86e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-04 04:10:05 CST | RECLAIM_PENDING_SET | 3.79e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.79e-06) but 4h close 3.8e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-04 08:10:05 CST | RECLAIM_PENDING_SET | 3.71e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.71e-06) but 4h close 3.71e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-04 12:10:25 CST | RECLAIM_PENDING_SET | 3.66e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.66e-06) but 4h close 3.67e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-04 16:10:31 CST | RECLAIM_PENDING_SET | 3.63e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.63e-06) but 4h close 3.63e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-05 00:11:27 CST | RECLAIM_PENDING_SET | 3.53e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.53e-06) but 4h close 3.53e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-05 04:10:21 CST | RECLAIM_PENDING_SET | 3.58e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.58e-06) but 4h close 3.59e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-05 08:10:13 CST | RECLAIM_PENDING_SET | 3.52e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.52e-06) but 4h close 3.53e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-05 12:10:28 CST | RECLAIM_PENDING_SET | 3.46e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.46e-06) but 4h close 3.46e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-05 16:10:10 CST | RECLAIM_PENDING_SET | 3.51e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.51e-06) but 4h close 3.52e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-05 20:06:09 CST | RECLAIM_PENDING_SET | 3.52e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.52e-06) but 4h close 3.53e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-06 09:36:27 CST | RECLAIM_PENDING_SET | 3.63e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.63e-06) but 4h close 3.61e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-06 12:10:20 CST | RECLAIM_PENDING_SET | 3.64e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.64e-06) but 4h close 3.67e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-06 16:10:07 CST | RECLAIM_PENDING_SET | 3.64e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.64e-06) but 4h close 3.64e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-06 20:14:44 CST | RECLAIM_PENDING_SET | 3.64e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.64e-06) but 4h close 3.64e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-07 00:10:30 CST | RECLAIM_PENDING_SET | 3.58e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.58e-06) but 4h close 3.58e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-07 04:10:06 CST | RECLAIM_PENDING_SET | 3.59e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.59e-06) but 4h close 3.6e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-07 08:10:09 CST | RECLAIM_PENDING_SET | 3.65e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.65e-06) but 4h close 3.65e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-07 12:10:29 CST | RECLAIM_PENDING_SET | 3.58e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.58e-06) but 4h close 3.58e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-07 16:10:32 CST | RECLAIM_PENDING_SET | 3.58e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.58e-06) but 4h close 3.57e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-07 20:07:00 CST | RECLAIM_PENDING_SET | 3.62e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.62e-06) but 4h close 3.6e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-08 00:13:03 CST | RECLAIM_PENDING_SET | 3.59e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.59e-06) but 4h close 3.56e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-08 04:10:09 CST | RECLAIM_PENDING_SET | 3.62e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.62e-06) but 4h close 3.63e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-08 08:10:06 CST | RECLAIM_PENDING_SET | 3.62e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.62e-06) but 4h close 3.63e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-08 12:10:23 CST | RECLAIM_PENDING_SET | 3.6e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.6e-06) but 4h close 3.61e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-08 16:10:23 CST | RECLAIM_PENDING_SET | 3.59e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.59e-06) but 4h close 3.6e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-09 00:10:03 CST | API_DELAY_SKIPPED | 3.59e-06 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 04:10:05 CST | API_DELAY_SKIPPED | 3.59e-06 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 08:10:03 CST | API_DELAY_SKIPPED | 3.59e-06 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 12:10:02 CST | API_DELAY_SKIPPED | 3.59e-06 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 16:10:03 CST | API_DELAY_SKIPPED | 3.59e-06 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-10 00:10:19 CST | RECLAIM_PENDING_SET | 3.58e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.58e-06) but 4h close 3.6e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-09-10 04:10:07 CST | RECLAIM_PENDING_SET | 3.53e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.53e-06) but 4h close 3.53e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-10-09 00:10:10 CST | RECLAIM_PENDING_SET | 3.77e-06 | n/a | 0.00 | 0.00 | Entry zone touched (price=3.77e-06) but 4h close 3.75e-06 < entry_high 3.93176e-06; waiting for reclaim. |
| 2026-10-09 04:10:03 CST | API_DELAY_SKIPPED | 3.77e-06 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |

### ZROUSDT `67ed9d733634`

- 当前状态：`STOPPED`
- 来源扫描：`6d047ae7c4f5` rank 1

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-26 20:06:38 CST | PLAN_CREATED | 1.1690 | n/a | 0.00 | 0.00 | Imported rank 1 from scan 6d047ae7c4f5; entry zone 1.1497189-1.172507. |
| 2026-08-26 20:06:43 CST | RECLAIM_PENDING_SET | 1.1680 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.1680) but 4h close 1.1700 < entry_high 1.1725; waiting for reclaim. |
| 2026-08-27 00:10:26 CST | RECLAIM_PENDING_SET | 1.1310 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.1310) but 4h close 1.1270 < entry_high 1.1725; waiting for reclaim. |
| 2026-08-27 04:10:10 CST | RECLAIM_PENDING_SET | 1.1280 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.1280) but 4h close 1.1260 < entry_high 1.1725; waiting for reclaim. |
| 2026-08-27 08:10:08 CST | RECLAIM_PENDING_SET | 1.1660 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.1660) but 4h close 1.1710 < entry_high 1.1725; waiting for reclaim. |
| 2026-08-27 12:10:10 CST | RECLAIM_PENDING_SET | 1.1610 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.1610) but 4h close 1.1650 < entry_high 1.1725; waiting for reclaim. |
| 2026-08-27 16:10:03 CST | API_DELAY_SKIPPED | 1.1610 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-08-28 12:10:09 CST | RECLAIM_PENDING_SET | 1.1320 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.1320) but 4h close 1.1430 < entry_high 1.1725; waiting for reclaim. |
| 2026-08-28 16:10:12 CST | RECLAIM_PENDING_SET | 1.1570 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.1570) but 4h close 1.1490 < entry_high 1.1725; waiting for reclaim. |
| 2026-08-28 20:06:28 CST | RECLAIM_PENDING_SET | 1.1420 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.1420) but 4h close 1.1390 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-03 20:17:44 CST | RECLAIM_PENDING_SET | 1.0620 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.0620) but 4h close 1.0540 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-04 00:10:40 CST | RECLAIM_PENDING_SET | 1.1110 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.1110) but 4h close 1.1160 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-04 04:10:05 CST | RECLAIM_PENDING_SET | 1.1120 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.1120) but 4h close 1.1090 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-04 08:10:04 CST | RECLAIM_PENDING_SET | 1.1160 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.1160) but 4h close 1.1290 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-04 12:10:23 CST | RECLAIM_PENDING_SET | 1.1270 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.1270) but 4h close 1.1380 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-04 16:10:29 CST | RECLAIM_PENDING_SET | 1.1190 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.1190) but 4h close 1.1160 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-05 00:11:04 CST | RECLAIM_PENDING_SET | 1.0590 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.0590) but 4h close 1.0550 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-05 04:10:20 CST | RECLAIM_PENDING_SET | 1.0590 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.0590) but 4h close 1.0590 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-05 08:10:12 CST | RECLAIM_PENDING_SET | 1.0400 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.0400) but 4h close 1.0370 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-05 12:10:27 CST | RECLAIM_PENDING_SET | 1.0320 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.0320) but 4h close 1.0340 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-05 16:10:07 CST | RECLAIM_PENDING_SET | 1.0540 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.0540) but 4h close 1.0530 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-05 20:06:09 CST | RECLAIM_PENDING_SET | 1.0470 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.0470) but 4h close 1.0480 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-06 09:36:25 CST | RECLAIM_PENDING_SET | 1.0830 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.0830) but 4h close 1.0610 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-06 12:10:19 CST | RECLAIM_PENDING_SET | 1.0760 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.0760) but 4h close 1.0720 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-06 16:10:06 CST | RECLAIM_PENDING_SET | 1.0700 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.0700) but 4h close 1.0740 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-06 20:14:43 CST | RECLAIM_PENDING_SET | 1.1040 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.1040) but 4h close 1.1030 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-07 00:10:28 CST | RECLAIM_PENDING_SET | 1.0940 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.0940) but 4h close 1.1080 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-07 04:10:05 CST | RECLAIM_PENDING_SET | 1.0920 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.0920) but 4h close 1.0910 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-07 08:10:08 CST | RECLAIM_PENDING_SET | 1.1050 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.1050) but 4h close 1.1050 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-07 12:10:26 CST | RECLAIM_PENDING_SET | 1.0810 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.0810) but 4h close 1.0800 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-07 16:10:30 CST | RECLAIM_PENDING_SET | 1.1240 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.1240) but 4h close 1.1160 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-08 00:13:00 CST | RECLAIM_PENDING_SET | 1.1260 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.1260) but 4h close 1.1140 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-08 04:10:08 CST | RECLAIM_PENDING_SET | 1.1280 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.1280) but 4h close 1.1320 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-08 08:10:06 CST | RECLAIM_PENDING_SET | 1.1340 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.1340) but 4h close 1.1370 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-08 12:10:23 CST | RECLAIM_PENDING_SET | 1.1400 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.1400) but 4h close 1.1280 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-08 16:10:23 CST | RECLAIM_PENDING_SET | 1.1200 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.1200) but 4h close 1.1310 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-09 00:10:03 CST | API_DELAY_SKIPPED | 1.1200 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 04:10:05 CST | API_DELAY_SKIPPED | 1.1200 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 08:10:03 CST | API_DELAY_SKIPPED | 1.1200 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 12:10:02 CST | API_DELAY_SKIPPED | 1.1200 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 16:10:03 CST | API_DELAY_SKIPPED | 1.1200 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-10 00:10:18 CST | RECLAIM_PENDING_SET | 1.1300 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.1300) but 4h close 1.1390 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-10 04:10:07 CST | RECLAIM_PENDING_SET | 1.1200 | n/a | 0.00 | 0.00 | Entry zone touched (price=1.1200) but 4h close 1.1180 < entry_high 1.1725; waiting for reclaim. |
| 2026-09-22 04:10:03 CST | RECLAIM_CONFIRMED_ENTERED | 1.1720 | 696.09 | 0.00 | 0.00 | Paper entry triggered at 1.172; quantity 696.08799. |
| 2026-09-23 12:10:05 CST | TP1_EMA_TRAILING_ACTIVATED | 1.2187 | 696.09 | 0.00 | 178.20 | EMA20 trailing stop activated at 1.2187073. |
| 2026-09-23 12:10:05 CST | TP1_HIT | 1.4267 | 696.09 | 0.00 | 178.20 | TP1 hit at 1.4266588; trade remains open. |
| 2026-09-23 16:10:03 CST | TP1_EMA_TRAILING_RAISED | 1.2354 | 696.09 | 0.00 | 187.94 | EMA20 trailing stop raised from 1.2187073 to 1.2354414. |
| 2026-09-23 20:06:31 CST | TP1_EMA_TRAILING_RAISED | 1.2527 | 696.09 | 0.00 | 210.91 | EMA20 trailing stop raised from 1.2354414 to 1.2527068. |
| 2026-09-24 00:10:05 CST | TP1_EMA_TRAILING_RAISED | 1.2637 | 696.09 | 0.00 | 218.57 | EMA20 trailing stop raised from 1.2527068 to 1.2636897. |
| 2026-09-24 04:10:06 CST | TP1_EMA_TRAILING_RAISED | 1.2835 | 696.09 | 0.00 | 242.93 | EMA20 trailing stop raised from 1.2636897 to 1.2835048. |
| 2026-09-24 08:10:04 CST | TP1_EMA_TRAILING_RAISED | 1.2997 | 696.09 | 0.00 | 238.76 | EMA20 trailing stop raised from 1.2835048 to 1.2996656. |
| 2026-09-24 12:10:03 CST | TP1_EMA_TRAILING_RAISED | 1.3179 | 696.09 | 0.00 | 256.86 | EMA20 trailing stop raised from 1.2996656 to 1.3179285. |
| 2026-10-09 00:10:03 CST | EMA_TRAILING_STOPPED | 2.0939 | 696.09 | 641.70 | 0.00 | EMA20 trailing stop hit at 2.0938614. |
| 2026-10-09 00:10:03 CST | TP1_EMA_TRAILING_RAISED | 2.0939 | 696.09 | 641.70 | 0.00 | EMA20 trailing stop raised from 1.3179285 to 2.0938614. |

### BNBUSDT `39a6ae4b393e`

- 当前状态：`ARCHIVED`
- 来源扫描：`6d047ae7c4f5` rank 2

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-26 20:06:38 CST | PLAN_CREATED | 702.64 | n/a | 0.00 | 0.00 | Imported rank 2 from scan 6d047ae7c4f5; entry zone 698.39591-704.5854. |
| 2026-08-26 20:06:44 CST | RECLAIM_PENDING_SET | 701.91 | n/a | 0.00 | 0.00 | Entry zone touched (price=701.91) but 4h close 702.15 < entry_high 704.59; waiting for reclaim. |
| 2026-08-27 00:10:27 CST | RECLAIM_PENDING_SET | 697.66 | n/a | 0.00 | 0.00 | Entry zone touched (price=697.66) but 4h close 697.00 < entry_high 704.59; waiting for reclaim. |
| 2026-08-27 04:10:11 CST | RECLAIM_PENDING_SET | 700.10 | n/a | 0.00 | 0.00 | Entry zone touched (price=700.10) but 4h close 699.53 < entry_high 704.59; waiting for reclaim. |
| 2026-08-27 12:10:11 CST | RECLAIM_PENDING_SET | 703.16 | n/a | 0.00 | 0.00 | Entry zone touched (price=703.16) but 4h close 703.34 < entry_high 704.59; waiting for reclaim. |
| 2026-08-27 16:10:03 CST | API_DELAY_SKIPPED | 703.16 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-08-27 20:07:42 CST | ARCHIVED | 703.16 | n/a | 0.00 | 0.00 | Archived because scan 05233b4f12a0 created a newer WATCHING plan for BNBUSDT. |

### SOLUSDT `c8d6065215ab`

- 当前状态：`ARCHIVED`
- 来源扫描：`1480a9add8c9` rank 1

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-25 20:06:50 CST | PLAN_CREATED | 98.4300 | n/a | 0.00 | 0.00 | Imported rank 1 from scan 1480a9add8c9; entry zone 95.956443-97.511413. |
| 2026-08-26 08:10:08 CST | RECLAIM_PENDING_SET | 96.3900 | n/a | 0.00 | 0.00 | Entry zone touched (price=96.3900) but 4h close 96.6000 < entry_high 97.5114; waiting for reclaim. |
| 2026-08-26 12:10:14 CST | RECLAIM_PENDING_SET | 97.1700 | n/a | 0.00 | 0.00 | Entry zone touched (price=97.1700) but 4h close 97.0600 < entry_high 97.5114; waiting for reclaim. |
| 2026-08-26 16:10:11 CST | RECLAIM_PENDING_SET | 97.2400 | n/a | 0.00 | 0.00 | Entry zone touched (price=97.2400) but 4h close 96.9500 < entry_high 97.5114; waiting for reclaim. |
| 2026-08-26 20:06:43 CST | RECLAIM_PENDING_SET | 96.6800 | n/a | 0.00 | 0.00 | Entry zone touched (price=96.6800) but 4h close 97.0300 < entry_high 97.5114; waiting for reclaim. |
| 2026-08-27 00:10:24 CST | RECLAIM_PENDING_SET | 95.9900 | n/a | 0.00 | 0.00 | Entry zone touched (price=95.9900) but 4h close 95.9400 < entry_high 97.5114; waiting for reclaim. |
| 2026-08-27 04:10:10 CST | RECLAIM_PENDING_SET | 96.8700 | n/a | 0.00 | 0.00 | Entry zone touched (price=96.8700) but 4h close 96.8000 < entry_high 97.5114; waiting for reclaim. |
| 2026-08-27 16:10:03 CST | API_DELAY_SKIPPED | 101.28 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-08-28 20:06:24 CST | ARCHIVED | 106.58 | n/a | 0.00 | 0.00 | Archived because scan 637752924d13 created a newer WATCHING plan for SOLUSDT. |

### BTCUSDT `b7c8dda9f475`

- 当前状态：`ARCHIVED`
- 来源扫描：`1480a9add8c9` rank 2

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-25 20:06:50 CST | PLAN_CREATED | 78,948.47 | n/a | 0.00 | 0.00 | Imported rank 2 from scan 1480a9add8c9; entry zone 77913.357-78613.806. |
| 2026-08-26 08:10:09 CST | RECLAIM_PENDING_SET | 78,324.00 | n/a | 0.00 | 0.00 | Entry zone touched (price=78,324.00) but 4h close 78,539.14 < entry_high 78,613.81; waiting for reclaim. |
| 2026-08-26 20:06:43 CST | RECLAIM_PENDING_SET | 78,373.00 | n/a | 0.00 | 0.00 | Entry zone touched (price=78,373.00) but 4h close 78,487.26 < entry_high 78,613.81; waiting for reclaim. |
| 2026-08-27 00:10:25 CST | RECLAIM_PENDING_SET | 78,132.51 | n/a | 0.00 | 0.00 | Entry zone touched (price=78,132.51) but 4h close 78,011.65 < entry_high 78,613.81; waiting for reclaim. |
| 2026-08-27 04:10:10 CST | RECLAIM_PENDING_SET | 78,476.13 | n/a | 0.00 | 0.00 | Entry zone touched (price=78,476.13) but 4h close 78,475.49 < entry_high 78,613.81; waiting for reclaim. |
| 2026-08-27 16:10:03 CST | API_DELAY_SKIPPED | 78,874.81 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-08-28 20:06:24 CST | ARCHIVED | 79,818.65 | n/a | 0.00 | 0.00 | Archived because scan 637752924d13 created a newer WATCHING plan for BTCUSDT. |

### UNIUSDT `ecdc3e95f224`

- 当前状态：`CLOSED`
- 来源扫描：`ed103f737b70` rank 1

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-24 20:07:11 CST | ENTERED | 4.3370 | 153.81 | 0.00 | 0.00 | Paper entry triggered at 4.337; quantity 153.81184. |
| 2026-08-24 20:07:11 CST | PLAN_CREATED | 4.3500 | n/a | 0.00 | 0.00 | Imported rank 1 from scan ed103f737b70; entry zone 4.2379437-4.3573847. |
| 2026-08-25 16:10:03 CST | API_DELAY_SKIPPED | 4.3700 | 153.81 | 0.00 | 5.08 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-08-27 16:10:03 CST | API_DELAY_SKIPPED | 4.4000 | 153.81 | 0.00 | 9.69 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-03 20:17:21 CST | TP2_HIT | 6.1301 | 153.81 | 275.80 | 0.00 | TP2 hit at 6.1300919; trade closed. |

### ETHUSDT `bffd2fdd7e2b`

- 当前状态：`CLOSED`
- 来源扫描：`ed103f737b70` rank 2

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-24 20:07:11 CST | PLAN_CREATED | 2,486.44 | n/a | 0.00 | 0.00 | Imported rank 2 from scan ed103f737b70; entry zone 2413.8618-2441.0322. |
| 2026-08-25 16:10:03 CST | API_DELAY_SKIPPED | 2,498.99 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-08-26 08:10:04 CST | ENTERED | 2,436.56 | 0.86 | 0.00 | 0.00 | Paper entry triggered at 2436.56; quantity 0.86069149. |
| 2026-08-27 16:10:03 CST | API_DELAY_SKIPPED | 2,494.50 | 0.86 | 0.00 | 49.87 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 00:10:03 CST | API_DELAY_SKIPPED | 2,470.77 | 0.86 | 0.00 | 29.44 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 04:10:05 CST | API_DELAY_SKIPPED | 2,470.77 | 0.86 | 0.00 | 29.44 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 08:10:03 CST | API_DELAY_SKIPPED | 2,470.77 | 0.86 | 0.00 | 29.44 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 12:10:02 CST | API_DELAY_SKIPPED | 2,470.77 | 0.86 | 0.00 | 29.44 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 16:10:03 CST | API_DELAY_SKIPPED | 2,470.77 | 0.86 | 0.00 | 29.44 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-22 00:10:04 CST | TP1_EMA_TRAILING_ACTIVATED | 2,622.91 | 0.86 | 0.00 | 267.64 | EMA20 trailing stop activated at 2622.9135. |
| 2026-09-22 00:10:04 CST | TP1_HIT | 2,641.59 | 0.86 | 0.00 | 267.64 | TP1 hit at 2641.5922; trade remains open. |
| 2026-09-22 04:10:03 CST | TP1_EMA_TRAILING_RAISED | 2,638.05 | 0.86 | 268.63 | 0.00 | EMA20 trailing stop raised from 2622.9135 to 2638.0495. |
| 2026-09-22 04:10:03 CST | TP2_HIT | 2,748.66 | 0.86 | 268.63 | 0.00 | TP2 hit at 2748.6648; trade closed. |

### TAOUSDT `0a265e9f2163`

- 当前状态：`CLOSED`
- 来源扫描：`ed103f737b70` rank 3

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-24 20:07:11 CST | PLAN_CREATED | 237.20 | n/a | 0.00 | 0.00 | Imported rank 3 from scan ed103f737b70; entry zone 228.60382-234.16753. |
| 2026-08-25 16:10:03 CST | API_DELAY_SKIPPED | 240.70 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-08-26 04:10:07 CST | RECLAIM_PENDING_SET | 232.50 | n/a | 0.00 | 0.00 | Entry zone touched (price=232.50) but 4h close 232.70 < entry_high 234.17; waiting for reclaim. |
| 2026-08-26 08:10:08 CST | RECLAIM_PENDING_SET | 228.90 | n/a | 0.00 | 0.00 | Entry zone touched (price=228.90) but 4h close 229.40 < entry_high 234.17; waiting for reclaim. |
| 2026-08-26 20:06:38 CST | RECLAIM_CONFIRMED_ENTERED | 233.70 | 4.36 | 0.00 | 0.00 | Paper entry triggered at 233.7; quantity 4.3649062. |
| 2026-08-27 16:10:03 CST | API_DELAY_SKIPPED | 239.20 | 4.36 | 0.00 | 24.01 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 00:10:03 CST | API_DELAY_SKIPPED | 253.20 | 4.36 | 0.00 | 85.12 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 04:10:05 CST | API_DELAY_SKIPPED | 253.20 | 4.36 | 0.00 | 85.12 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 08:10:03 CST | API_DELAY_SKIPPED | 253.20 | 4.36 | 0.00 | 85.12 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 12:10:02 CST | API_DELAY_SKIPPED | 253.20 | 4.36 | 0.00 | 85.12 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 16:10:03 CST | API_DELAY_SKIPPED | 253.20 | 4.36 | 0.00 | 85.12 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-22 00:10:04 CST | TP1_EMA_TRAILING_ACTIVATED | 261.50 | 4.36 | 0.00 | 236.58 | EMA20 trailing stop activated at 261.4993. |
| 2026-09-22 00:10:04 CST | TP1_HIT | 272.58 | 4.36 | 0.00 | 236.58 | TP1 hit at 272.57703; trade remains open. |
| 2026-09-22 04:10:03 CST | TP1_EMA_TRAILING_RAISED | 266.09 | 4.36 | 259.59 | 0.00 | EMA20 trailing stop raised from 261.4993 to 266.088. |
| 2026-09-22 04:10:03 CST | TP2_HIT | 293.17 | 4.36 | 259.59 | 0.00 | TP2 hit at 293.1727; trade closed. |

### SOLUSDT `eb16fbac349f`

- 当前状态：`ARCHIVED`
- 来源扫描：`ed103f737b70` rank 4

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-24 20:07:11 CST | PLAN_CREATED | 95.4800 | n/a | 0.00 | 0.00 | Imported rank 4 from scan ed103f737b70; entry zone 93.111547-94.447696. |
| 2026-08-25 16:10:03 CST | API_DELAY_SKIPPED | 101.34 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-08-25 20:06:50 CST | ARCHIVED | 101.34 | n/a | 0.00 | 0.00 | Archived because scan 1480a9add8c9 created a newer WATCHING plan for SOLUSDT. |

### BTCUSDT `34a7cc973d13`

- 当前状态：`ARCHIVED`
- 来源扫描：`ed103f737b70` rank 5

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-24 20:07:11 CST | PLAN_CREATED | 78,202.00 | n/a | 0.00 | 0.00 | Imported rank 5 from scan ed103f737b70; entry zone 76527.522-76994.942. |
| 2026-08-25 16:10:03 CST | API_DELAY_SKIPPED | 80,446.70 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-08-25 20:06:50 CST | ARCHIVED | 80,446.70 | n/a | 0.00 | 0.00 | Archived because scan 1480a9add8c9 created a newer WATCHING plan for BTCUSDT. |

### SOLUSDT `437840b57a9c`

- 当前状态：`ARCHIVED`
- 来源扫描：`320bc0bceb6a` rank 1

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-23 20:06:31 CST | PLAN_CREATED | 94.4500 | n/a | 0.00 | 0.00 | Imported rank 1 from scan 320bc0bceb6a; entry zone 91.336765-93.629956. |
| 2026-08-24 20:07:11 CST | ARCHIVED | 94.1700 | n/a | 0.00 | 0.00 | Archived because scan ed103f737b70 created a newer WATCHING plan for SOLUSDT. |

### ETHUSDT `68c9b5939b7c`

- 当前状态：`ARCHIVED`
- 来源扫描：`320bc0bceb6a` rank 2

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-23 20:06:31 CST | PLAN_CREATED | 2,427.53 | n/a | 0.00 | 0.00 | Imported rank 2 from scan 320bc0bceb6a; entry zone 2366.6754-2402.3945. |
| 2026-08-24 20:07:11 CST | ARCHIVED | 2,454.13 | n/a | 0.00 | 0.00 | Archived because scan ed103f737b70 created a newer WATCHING plan for ETHUSDT. |

### BTCUSDT `18afb7a2eddf`

- 当前状态：`ARCHIVED`
- 来源扫描：`320bc0bceb6a` rank 3

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-23 20:06:31 CST | PLAN_CREATED | 77,195.09 | n/a | 0.00 | 0.00 | Imported rank 3 from scan 320bc0bceb6a; entry zone 75422.107-76154.559. |
| 2026-08-24 20:07:11 CST | ARCHIVED | 77,342.00 | n/a | 0.00 | 0.00 | Archived because scan ed103f737b70 created a newer WATCHING plan for BTCUSDT. |

### TRXUSDT `56474a1c8879`

- 当前状态：`ENTERED`
- 来源扫描：`2ee5c0fa058f` rank 1

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-21 20:07:17 CST | PLAN_CREATED | 0.34010 | n/a | 0.00 | 0.00 | Imported rank 1 from scan 2ee5c0fa058f; entry zone 0.33687782-0.33763041. |
| 2026-08-25 16:10:03 CST | API_DELAY_SKIPPED | 0.34450 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-08-26 08:10:07 CST | RECLAIM_PENDING_SET | 0.33560 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33560) but 4h close 0.33630 < entry_high 0.33763; waiting for reclaim. |
| 2026-08-26 16:10:10 CST | RECLAIM_PENDING_SET | 0.33740 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33740) but 4h close 0.33720 < entry_high 0.33763; waiting for reclaim. |
| 2026-08-26 20:06:41 CST | RECLAIM_PENDING_SET | 0.33570 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33570) but 4h close 0.33560 < entry_high 0.33763; waiting for reclaim. |
| 2026-08-27 00:10:18 CST | RECLAIM_PENDING_SET | 0.33470 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33470) but 4h close 0.33460 < entry_high 0.33763; waiting for reclaim. |
| 2026-08-27 04:10:08 CST | RECLAIM_PENDING_SET | 0.33580 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33580) but 4h close 0.33580 < entry_high 0.33763; waiting for reclaim. |
| 2026-08-27 08:10:06 CST | RECLAIM_PENDING_SET | 0.33590 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33590) but 4h close 0.33600 < entry_high 0.33763; waiting for reclaim. |
| 2026-08-27 12:10:07 CST | RECLAIM_PENDING_SET | 0.33430 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33430) but 4h close 0.33440 < entry_high 0.33763; waiting for reclaim. |
| 2026-08-27 16:10:03 CST | API_DELAY_SKIPPED | 0.33430 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-08-27 20:07:45 CST | RECLAIM_PENDING_SET | 0.33710 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33710) but 4h close 0.33680 < entry_high 0.33763; waiting for reclaim. |
| 2026-08-28 08:10:03 CST | RECLAIM_CONFIRMED_ENTERED | 0.33750 | 9,196.25 | 0.00 | 0.00 | Paper entry triggered at 0.3375; quantity 9196.2479. |
| 2026-09-09 00:10:03 CST | API_DELAY_SKIPPED | 0.33810 | 9,196.25 | 0.00 | 5.52 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 04:10:05 CST | API_DELAY_SKIPPED | 0.33810 | 9,196.25 | 0.00 | 5.52 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 08:10:03 CST | API_DELAY_SKIPPED | 0.33810 | 9,196.25 | 0.00 | 5.52 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 12:10:02 CST | API_DELAY_SKIPPED | 0.33810 | 9,196.25 | 0.00 | 5.52 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 16:10:03 CST | API_DELAY_SKIPPED | 0.33810 | 9,196.25 | 0.00 | 5.52 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-10-09 04:10:03 CST | API_DELAY_SKIPPED | 0.33300 | 9,196.25 | 0.00 | -41.38 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |

### TRXUSDT `0629b2ffa602`

- 当前状态：`ARCHIVED`
- 来源扫描：`6a84e67a5013` rank 1

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-20 20:07:43 CST | PLAN_CREATED | 0.33730 | n/a | 0.00 | 0.00 | Imported rank 1 from scan 6a84e67a5013; entry zone 0.33427602-0.3348138. |
| 2026-08-21 20:07:17 CST | ARCHIVED | 0.33910 | n/a | 0.00 | 0.00 | Archived because scan 2ee5c0fa058f created a newer WATCHING plan for TRXUSDT. |

### ETHUSDT `fd7033e6abc6`

- 当前状态：`ARCHIVED`
- 来源扫描：`110604e1204a` rank 1

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-19 20:06:47 CST | PLAN_CREATED | 1,922.86 | n/a | 0.00 | 0.00 | Imported rank 1 from scan 110604e1204a; entry zone 1910.6153-1917.3912. |
| 2026-08-23 20:06:31 CST | ARCHIVED | 2,411.62 | n/a | 0.00 | 0.00 | Archived because scan 320bc0bceb6a created a newer WATCHING plan for ETHUSDT. |

### BTCUSDT `7b4d014fe7e2`

- 当前状态：`ARCHIVED`
- 来源扫描：`110604e1204a` rank 2

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-19 20:06:47 CST | PLAN_CREATED | 64,481.81 | n/a | 0.00 | 0.00 | Imported rank 2 from scan 110604e1204a; entry zone 64260.667-64428.494. |
| 2026-08-23 20:06:31 CST | ARCHIVED | 76,267.73 | n/a | 0.00 | 0.00 | Archived because scan 320bc0bceb6a created a newer WATCHING plan for BTCUSDT. |

### SOLUSDT `6c424aa918fb`

- 当前状态：`ARCHIVED`
- 来源扫描：`110604e1204a` rank 3

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-19 20:06:47 CST | PLAN_CREATED | 77.4700 | n/a | 0.00 | 0.00 | Imported rank 3 from scan 110604e1204a; entry zone 76.631137-76.941181. |
| 2026-08-23 20:06:31 CST | ARCHIVED | 92.9600 | n/a | 0.00 | 0.00 | Archived because scan 320bc0bceb6a created a newer WATCHING plan for SOLUSDT. |

### SOLUSDT `4a9a6cbaad0e`

- 当前状态：`ARCHIVED`
- 来源扫描：`741093cc2c86` rank 1

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-18 20:06:23 CST | PLAN_CREATED | 76.4700 | n/a | 0.00 | 0.00 | Imported rank 1 from scan 741093cc2c86; entry zone 75.944653-76.280567. |
| 2026-08-19 20:06:47 CST | ARCHIVED | 77.0900 | n/a | 0.00 | 0.00 | Archived because scan 110604e1204a created a newer WATCHING plan for SOLUSDT. |

### BTCUSDT `6360f05a90ec`

- 当前状态：`ARCHIVED`
- 来源扫描：`741093cc2c86` rank 2

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-18 20:06:23 CST | PLAN_CREATED | 64,342.23 | n/a | 0.00 | 0.00 | Imported rank 2 from scan 741093cc2c86; entry zone 64038.622-64184.644. |
| 2026-08-19 20:06:47 CST | ARCHIVED | 64,293.10 | n/a | 0.00 | 0.00 | Archived because scan 110604e1204a created a newer WATCHING plan for BTCUSDT. |

### ETHUSDT `ac939ee74e2c`

- 当前状态：`ARCHIVED`
- 来源扫描：`d889ad7bd72e` rank 1

| Time | Event | Price | Qty | Realized | Unrealized | Message |
|---|---|---:|---:|---:|---:|---|
| 2026-08-17 20:05:55 CST | PLAN_CREATED | 1,904.37 | n/a | 0.00 | 0.00 | Imported rank 1 from scan d889ad7bd72e; entry zone 1893.4206-1896.8374. |
| 2026-08-18 12:10:06 CST | RECLAIM_PENDING_SET | 1,894.02 | n/a | 0.00 | 0.00 | Entry zone touched (price=1,894.02) but 4h close 1,894.69 < entry_high 1,896.84; waiting for reclaim. |
| 2026-08-18 16:10:05 CST | API_DELAY_SKIPPED | 1,894.02 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-08-19 20:06:47 CST | ARCHIVED | 1,916.67 | n/a | 0.00 | 0.00 | Archived because scan 110604e1204a created a newer WATCHING plan for ETHUSDT. |

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
| 2026-08-07 12:10:02 CST | API_DELAY_SKIPPED | 0.38160 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: HTTPError: HTTP Error 451:  |
| 2026-08-07 16:10:02 CST | API_DELAY_SKIPPED | 0.38160 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-08-08 00:10:03 CST | API_DELAY_SKIPPED | 0.38160 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-08-08 04:10:02 CST | API_DELAY_SKIPPED | 0.38160 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-08-08 08:10:02 CST | API_DELAY_SKIPPED | 0.38160 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-08-08 12:10:02 CST | API_DELAY_SKIPPED | 0.38160 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-08-08 16:10:03 CST | API_DELAY_SKIPPED | 0.38160 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-08-09 00:10:02 CST | API_DELAY_SKIPPED | 0.38160 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-08-09 04:10:02 CST | API_DELAY_SKIPPED | 0.38160 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-08-09 08:10:02 CST | API_DELAY_SKIPPED | 0.38160 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-08-09 12:10:02 CST | API_DELAY_SKIPPED | 0.38160 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-08-09 16:10:03 CST | API_DELAY_SKIPPED | 0.38160 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-08-09 20:06:00 CST | RECLAIM_PENDING_SET | 0.34760 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34760) but 4h close 0.34800 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-10 00:10:21 CST | RECLAIM_PENDING_SET | 0.35350 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.35350) but 4h close 0.35420 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-10 04:10:06 CST | RECLAIM_PENDING_SET | 0.35240 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.35240) but 4h close 0.35190 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-10 08:10:07 CST | RECLAIM_PENDING_SET | 0.35090 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.35090) but 4h close 0.34840 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-10 12:10:05 CST | RECLAIM_PENDING_SET | 0.34940 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34940) but 4h close 0.34850 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-10 16:10:17 CST | RECLAIM_PENDING_SET | 0.35250 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.35250) but 4h close 0.35250 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-10 20:06:48 CST | RECLAIM_PENDING_SET | 0.35300 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.35300) but 4h close 0.35400 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-11 00:10:12 CST | RECLAIM_PENDING_SET | 0.34750 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34750) but 4h close 0.34710 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-11 04:10:05 CST | RECLAIM_PENDING_SET | 0.34550 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34550) but 4h close 0.34480 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-11 08:10:05 CST | RECLAIM_PENDING_SET | 0.33730 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33730) but 4h close 0.34000 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-11 12:10:05 CST | RECLAIM_PENDING_SET | 0.33970 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33970) but 4h close 0.33990 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-11 16:10:42 CST | RECLAIM_PENDING_SET | 0.33770 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33770) but 4h close 0.33740 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-11 20:06:26 CST | RECLAIM_PENDING_SET | 0.33920 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33920) but 4h close 0.33980 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-12 00:10:10 CST | RECLAIM_PENDING_SET | 0.33360 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33360) but 4h close 0.33330 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-12 04:10:05 CST | RECLAIM_PENDING_SET | 0.33770 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33770) but 4h close 0.33610 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-12 08:10:05 CST | RECLAIM_PENDING_SET | 0.33580 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33580) but 4h close 0.33600 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-13 00:10:09 CST | RECLAIM_PENDING_SET | 0.33400 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33400) but 4h close 0.33470 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-13 04:10:04 CST | RECLAIM_PENDING_SET | 0.33130 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33130) but 4h close 0.33070 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-13 08:10:05 CST | RECLAIM_PENDING_SET | 0.33290 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33290) but 4h close 0.33050 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-13 12:10:06 CST | RECLAIM_PENDING_SET | 0.33550 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33550) but 4h close 0.33480 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-13 16:10:07 CST | RECLAIM_PENDING_SET | 0.33460 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33460) but 4h close 0.33480 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-13 20:06:26 CST | RECLAIM_PENDING_SET | 0.33260 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33260) but 4h close 0.33250 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-14 00:10:09 CST | RECLAIM_PENDING_SET | 0.33380 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33380) but 4h close 0.33480 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-14 04:10:06 CST | RECLAIM_PENDING_SET | 0.33340 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33340) but 4h close 0.33330 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-14 08:10:07 CST | RECLAIM_PENDING_SET | 0.33470 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33470) but 4h close 0.33500 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-14 12:10:09 CST | RECLAIM_PENDING_SET | 0.33210 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33210) but 4h close 0.33070 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-14 16:11:22 CST | RECLAIM_PENDING_SET | 0.33130 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33130) but 4h close 0.33120 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-14 20:06:09 CST | RECLAIM_PENDING_SET | 0.32660 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32660) but 4h close 0.32680 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-15 00:10:09 CST | RECLAIM_PENDING_SET | 0.32720 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32720) but 4h close 0.32720 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-15 04:10:11 CST | RECLAIM_PENDING_SET | 0.32460 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32460) but 4h close 0.32410 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-15 08:10:05 CST | RECLAIM_PENDING_SET | 0.32770 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32770) but 4h close 0.32730 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-15 12:10:14 CST | RECLAIM_PENDING_SET | 0.33010 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33010) but 4h close 0.33050 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-15 16:10:08 CST | RECLAIM_PENDING_SET | 0.32620 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32620) but 4h close 0.32630 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-15 20:06:01 CST | RECLAIM_PENDING_SET | 0.32570 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32570) but 4h close 0.32600 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-16 00:10:06 CST | RECLAIM_PENDING_SET | 0.32710 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32710) but 4h close 0.32710 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-16 04:10:05 CST | RECLAIM_PENDING_SET | 0.32550 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32550) but 4h close 0.32560 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-16 08:10:05 CST | RECLAIM_PENDING_SET | 0.32400 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32400) but 4h close 0.32350 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-16 12:10:06 CST | RECLAIM_PENDING_SET | 0.32500 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32500) but 4h close 0.32480 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-16 16:10:07 CST | RECLAIM_PENDING_SET | 0.32430 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32430) but 4h close 0.32430 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-16 20:05:56 CST | RECLAIM_PENDING_SET | 0.32620 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32620) but 4h close 0.32620 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-17 00:10:07 CST | RECLAIM_PENDING_SET | 0.33260 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33260) but 4h close 0.33280 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-17 04:10:09 CST | RECLAIM_PENDING_SET | 0.33190 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33190) but 4h close 0.33200 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-17 08:10:05 CST | RECLAIM_PENDING_SET | 0.33090 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33090) but 4h close 0.33050 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-17 12:10:08 CST | RECLAIM_PENDING_SET | 0.33440 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33440) but 4h close 0.33380 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-17 16:10:12 CST | RECLAIM_PENDING_SET | 0.33660 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33660) but 4h close 0.33830 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-17 20:05:57 CST | RECLAIM_PENDING_SET | 0.34060 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34060) but 4h close 0.34100 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-18 00:10:10 CST | RECLAIM_PENDING_SET | 0.33800 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33800) but 4h close 0.33870 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-18 04:10:05 CST | RECLAIM_PENDING_SET | 0.33230 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33230) but 4h close 0.33310 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-18 08:10:06 CST | RECLAIM_PENDING_SET | 0.33540 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33540) but 4h close 0.33640 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-18 12:10:05 CST | RECLAIM_PENDING_SET | 0.33060 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33060) but 4h close 0.33040 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-18 16:10:05 CST | API_DELAY_SKIPPED | 0.33060 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-08-18 20:06:24 CST | RECLAIM_PENDING_SET | 0.33170 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33170) but 4h close 0.33150 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-19 00:10:19 CST | RECLAIM_PENDING_SET | 0.33320 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33320) but 4h close 0.33390 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-19 04:10:06 CST | RECLAIM_PENDING_SET | 0.33080 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.33080) but 4h close 0.33080 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-19 08:10:06 CST | RECLAIM_PENDING_SET | 0.32520 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32520) but 4h close 0.32630 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-19 12:10:07 CST | RECLAIM_PENDING_SET | 0.32490 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32490) but 4h close 0.32570 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-19 16:10:10 CST | RECLAIM_PENDING_SET | 0.32420 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32420) but 4h close 0.32450 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-19 20:06:51 CST | RECLAIM_PENDING_SET | 0.32540 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.32540) but 4h close 0.32590 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-20 00:10:13 CST | RECLAIM_PENDING_SET | 0.34030 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34030) but 4h close 0.34030 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-20 04:10:07 CST | RECLAIM_PENDING_SET | 0.34200 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34200) but 4h close 0.34120 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-20 08:10:06 CST | RECLAIM_PENDING_SET | 0.34710 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34710) but 4h close 0.34720 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-20 12:10:12 CST | RECLAIM_PENDING_SET | 0.34320 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34320) but 4h close 0.34200 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-20 16:10:08 CST | RECLAIM_PENDING_SET | 0.34590 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34590) but 4h close 0.34360 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-20 20:07:46 CST | RECLAIM_PENDING_SET | 0.35100 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.35100) but 4h close 0.35340 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-21 00:10:11 CST | RECLAIM_PENDING_SET | 0.35720 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.35720) but 4h close 0.35700 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-21 04:10:05 CST | RECLAIM_PENDING_SET | 0.34710 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.34710) but 4h close 0.34740 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-21 08:10:05 CST | RECLAIM_PENDING_SET | 0.35620 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.35620) but 4h close 0.35560 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-21 12:10:06 CST | RECLAIM_PENDING_SET | 0.36370 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36370) but 4h close 0.36400 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-21 16:10:15 CST | RECLAIM_PENDING_SET | 0.37460 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37460) but 4h close 0.37400 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-21 20:07:19 CST | RECLAIM_PENDING_SET | 0.37440 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37440) but 4h close 0.37220 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-22 00:10:12 CST | RECLAIM_PENDING_SET | 0.40550 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.40550) but 4h close 0.39960 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-22 04:10:06 CST | RECLAIM_PENDING_SET | 0.38180 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38180) but 4h close 0.37910 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-22 08:10:06 CST | RECLAIM_PENDING_SET | 0.39580 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.39580) but 4h close 0.39680 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-22 16:10:07 CST | RECLAIM_PENDING_SET | 0.38190 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38190) but 4h close 0.38410 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-22 20:06:54 CST | RECLAIM_PENDING_SET | 0.37090 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37090) but 4h close 0.37070 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-23 00:10:15 CST | RECLAIM_PENDING_SET | 0.36760 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36760) but 4h close 0.36820 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-23 04:10:07 CST | RECLAIM_PENDING_SET | 0.37590 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37590) but 4h close 0.37380 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-23 08:10:06 CST | RECLAIM_PENDING_SET | 0.36490 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36490) but 4h close 0.36360 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-23 12:10:06 CST | RECLAIM_PENDING_SET | 0.35470 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.35470) but 4h close 0.35600 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-23 16:10:07 CST | RECLAIM_PENDING_SET | 0.36020 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36020) but 4h close 0.35730 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-23 20:06:33 CST | RECLAIM_PENDING_SET | 0.36860 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36860) but 4h close 0.37020 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-24 00:10:07 CST | RECLAIM_PENDING_SET | 0.38820 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38820) but 4h close 0.38440 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-24 04:10:07 CST | RECLAIM_PENDING_SET | 0.38100 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38100) but 4h close 0.38110 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-24 08:10:06 CST | RECLAIM_PENDING_SET | 0.38050 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38050) but 4h close 0.38270 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-24 12:10:08 CST | RECLAIM_PENDING_SET | 0.37120 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37120) but 4h close 0.36950 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-24 16:10:07 CST | RECLAIM_PENDING_SET | 0.37460 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37460) but 4h close 0.37330 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-24 20:07:13 CST | RECLAIM_PENDING_SET | 0.37940 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37940) but 4h close 0.38110 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-25 00:10:06 CST | RECLAIM_PENDING_SET | 0.37830 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37830) but 4h close 0.37680 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-25 04:10:06 CST | RECLAIM_PENDING_SET | 0.38440 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38440) but 4h close 0.38190 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-25 08:10:06 CST | RECLAIM_PENDING_SET | 0.38060 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38060) but 4h close 0.38190 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-25 12:10:09 CST | RECLAIM_PENDING_SET | 0.39190 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.39190) but 4h close 0.39170 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-25 16:10:03 CST | API_DELAY_SKIPPED | 0.39190 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-08-25 20:06:52 CST | RECLAIM_PENDING_SET | 0.37600 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37600) but 4h close 0.37780 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-26 00:10:11 CST | RECLAIM_PENDING_SET | 0.37170 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37170) but 4h close 0.37340 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-26 04:10:06 CST | RECLAIM_PENDING_SET | 0.36910 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36910) but 4h close 0.36910 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-26 08:10:06 CST | RECLAIM_PENDING_SET | 0.36290 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36290) but 4h close 0.36390 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-26 12:10:06 CST | RECLAIM_PENDING_SET | 0.36770 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36770) but 4h close 0.36700 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-26 16:10:09 CST | RECLAIM_PENDING_SET | 0.36740 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36740) but 4h close 0.36670 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-26 20:06:40 CST | RECLAIM_PENDING_SET | 0.36480 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36480) but 4h close 0.36570 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-27 00:10:17 CST | RECLAIM_PENDING_SET | 0.36000 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36000) but 4h close 0.35900 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-27 04:10:08 CST | RECLAIM_PENDING_SET | 0.36400 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36400) but 4h close 0.36450 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-27 08:10:05 CST | RECLAIM_PENDING_SET | 0.37580 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37580) but 4h close 0.37460 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-27 12:10:06 CST | RECLAIM_PENDING_SET | 0.37090 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37090) but 4h close 0.37040 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-27 16:10:03 CST | API_DELAY_SKIPPED | 0.37090 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-08-27 20:07:44 CST | RECLAIM_PENDING_SET | 0.37320 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37320) but 4h close 0.37290 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-28 00:10:14 CST | RECLAIM_PENDING_SET | 0.37940 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37940) but 4h close 0.37880 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-28 04:10:06 CST | RECLAIM_PENDING_SET | 0.37410 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37410) but 4h close 0.37510 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-28 08:10:05 CST | RECLAIM_PENDING_SET | 0.37550 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37550) but 4h close 0.37710 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-28 12:10:06 CST | RECLAIM_PENDING_SET | 0.36780 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36780) but 4h close 0.37040 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-28 16:10:07 CST | RECLAIM_PENDING_SET | 0.36900 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36900) but 4h close 0.36810 < entry_high 0.41157; waiting for reclaim. |
| 2026-08-28 20:06:26 CST | RECLAIM_PENDING_SET | 0.36850 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36850) but 4h close 0.36780 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-03 20:17:37 CST | RECLAIM_PENDING_SET | 0.35610 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.35610) but 4h close 0.35510 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-04 00:10:35 CST | RECLAIM_PENDING_SET | 0.36790 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36790) but 4h close 0.37120 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-04 04:10:03 CST | RECLAIM_PENDING_SET | 0.36750 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36750) but 4h close 0.36740 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-04 08:10:03 CST | RECLAIM_PENDING_SET | 0.36300 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36300) but 4h close 0.36300 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-04 12:10:19 CST | RECLAIM_PENDING_SET | 0.36330 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36330) but 4h close 0.36340 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-04 16:10:25 CST | RECLAIM_PENDING_SET | 0.36200 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36200) but 4h close 0.36110 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-05 00:10:57 CST | RECLAIM_PENDING_SET | 0.35420 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.35420) but 4h close 0.35380 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-05 04:10:16 CST | RECLAIM_PENDING_SET | 0.35830 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.35830) but 4h close 0.35830 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-05 08:10:10 CST | RECLAIM_PENDING_SET | 0.35830 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.35830) but 4h close 0.35760 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-05 12:10:23 CST | RECLAIM_PENDING_SET | 0.36600 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36600) but 4h close 0.36740 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-05 16:10:05 CST | RECLAIM_PENDING_SET | 0.36930 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36930) but 4h close 0.36970 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-05 20:06:07 CST | RECLAIM_PENDING_SET | 0.36990 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36990) but 4h close 0.36940 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-06 09:36:22 CST | RECLAIM_PENDING_SET | 0.37720 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37720) but 4h close 0.37010 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-06 12:10:13 CST | RECLAIM_PENDING_SET | 0.37530 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37530) but 4h close 0.37660 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-06 16:10:04 CST | RECLAIM_PENDING_SET | 0.37500 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37500) but 4h close 0.37570 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-06 20:14:37 CST | RECLAIM_PENDING_SET | 0.38020 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38020) but 4h close 0.37990 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-07 00:10:24 CST | RECLAIM_PENDING_SET | 0.37360 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37360) but 4h close 0.37430 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-07 04:10:04 CST | RECLAIM_PENDING_SET | 0.37740 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37740) but 4h close 0.37760 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-07 08:10:06 CST | RECLAIM_PENDING_SET | 0.38780 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38780) but 4h close 0.38760 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-07 12:10:21 CST | RECLAIM_PENDING_SET | 0.38320 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38320) but 4h close 0.38130 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-07 16:10:27 CST | RECLAIM_PENDING_SET | 0.38610 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38610) but 4h close 0.38200 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-07 20:06:57 CST | RECLAIM_PENDING_SET | 0.38700 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38700) but 4h close 0.38480 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-08 00:12:58 CST | RECLAIM_PENDING_SET | 0.38230 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38230) but 4h close 0.37840 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-08 04:10:07 CST | RECLAIM_PENDING_SET | 0.38500 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38500) but 4h close 0.38730 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-08 08:10:04 CST | RECLAIM_PENDING_SET | 0.38320 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.38320) but 4h close 0.38380 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-08 12:10:21 CST | RECLAIM_PENDING_SET | 0.37880 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37880) but 4h close 0.37940 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-08 16:10:20 CST | RECLAIM_PENDING_SET | 0.37480 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.37480) but 4h close 0.37610 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-09 00:10:03 CST | API_DELAY_SKIPPED | 0.37480 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 04:10:05 CST | API_DELAY_SKIPPED | 0.37480 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 08:10:03 CST | API_DELAY_SKIPPED | 0.37480 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 12:10:02 CST | API_DELAY_SKIPPED | 0.37480 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-09 16:10:03 CST | API_DELAY_SKIPPED | 0.37480 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |
| 2026-09-10 00:10:16 CST | RECLAIM_PENDING_SET | 0.36850 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36850) but 4h close 0.36910 < entry_high 0.41157; waiting for reclaim. |
| 2026-09-10 04:10:05 CST | RECLAIM_PENDING_SET | 0.36580 | n/a | 0.00 | 0.00 | Entry zone touched (price=0.36580) but 4h close 0.36500 < entry_high 0.41157; waiting for reclaim. |
| 2026-10-09 04:10:03 CST | API_DELAY_SKIPPED | 0.44750 | n/a | 0.00 | 0.00 | 24h ticker unavailable; state update skipped: URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)> |

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
