---
created: 2026-06-12 21:09:32 CST
tags:
  - crypto
  - trading-system
  - paper-observation
account: demo
report_version: v1
---

# 三周观察仪表 2026-06-12 demo v1

## 核心指标

| Metric | Value |
|---|---:|
| RECLAIM_PENDING events | 3 |
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
| `ONDOUSDT` | ENTERED | 573.9 |
| `ONDOUSDT` | ENTERED | 573.7 |
| `WLDUSDT` | ENTERED | 33.5 |

## 今日扫描 Action 与 RISK_OFF

| Scope | BUY_CANDIDATE | WAIT_PULLBACK | WATCH_ONLY | REJECT | Other |
|---|---:|---:|---:|---:|---:|
| All candidates | 0 | 0 | 5 | 0 | 0 |
| RISK_OFF-tagged | 0 | 0 | 0 | 0 | 0 |

## RECLAIM_PENDING 明细

| Symbol | Status | Stop | Last Price | Outcome | Last Pending |
|---|---|---:|---:|---|---|
| `ONDOUSDT` | WATCHING | 0.338446 | 0.367 | still_waiting | 2026-06-12 20:06:50 CST |
