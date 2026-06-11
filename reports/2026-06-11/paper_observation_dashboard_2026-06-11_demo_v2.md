---
created: 2026-06-11 21:31:14 CST
tags:
  - crypto
  - trading-system
  - paper-observation
account: demo
report_version: v2
---

# 三周观察仪表 2026-06-11 demo v2

## 核心指标

| Metric | Value |
|---|---:|
| RECLAIM_PENDING events | 1 |
| Reclaim trades | 1 |
| Reclaim fell below stop / invalidated | 0 |
| Reclaim later entered | 0 |
| Reclaim still waiting | 1 |
| TP1 EMA activations | 0 |
| TP1 EMA stop raises | 0 |
| TP1 EMA stop exits | 0 |
| Open entered/TP1 positions | 3 |

## 开放持仓时长

| Symbol | Status | Holding Hours |
|---|---|---:|
| `ONDOUSDT` | ENTERED | 550.3 |
| `ONDOUSDT` | ENTERED | 550.1 |
| `WLDUSDT` | ENTERED | 9.9 |

## 今日扫描 Action 与 RISK_OFF

| Scope | BUY_CANDIDATE | WAIT_PULLBACK | WATCH_ONLY | REJECT | Other |
|---|---:|---:|---:|---:|---:|
| All candidates | 0 | 0 | 6 | 4 | 0 |
| RISK_OFF-tagged | 0 | 0 | 0 | 0 | 0 |

## RECLAIM_PENDING 明细

| Symbol | Status | Stop | Last Price | Outcome | Last Pending |
|---|---|---:|---:|---|---|
| `ONDOUSDT` | WATCHING | 0.338446 | 0.3457 | still_waiting | 2026-06-11 20:47:37 CST |
