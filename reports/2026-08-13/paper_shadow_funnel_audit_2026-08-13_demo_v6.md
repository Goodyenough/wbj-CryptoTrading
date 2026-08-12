# Paper Shadow Funnel Audit

## 目标

- 本报告只诊断 `candidate -> plan -> terminal` 漏斗，不改变策略、paper 状态或 maturity 定义。
- account: `demo`
- window: `2026-07-13T17:37:49.138671Z` -> `2026-08-12T17:37:49.138671Z`
- verdict: `mixed_causes`
- reason: Pipeline, lifecycle, and/or execution signals coexist; isolate them before strategy conclusions.

## 运行覆盖

| 指标 | 当前 | 最低要求 |
|---|---:|---:|
| daily success runs | 24 | 5 |
| daily success dates | 24 | 5 |
| paper 4h success runs | 146 | 20 |
| failed runs | 7 | 0（诊断信号） |
| coverage_ok | `True` | `true` |

## 漏斗摘要

| 阶段 | 数量 |
|---|---:|
| candidate observations | 20 |
| plan-level plans created in window | 0 |
| plan-level plans touched in window | 2 |
| existing plans at window start | 25 |
| plan-linked decisions | 1 |
| mature terminal plans | 1 |
| current open plans | 1 |
| candidate terminal counterfactual outcomes | 0 |
| plans without plan-linked decision | 0 |
| archived without entry evaluation | 0 |
| terminal plans without terminal shadow outcome | 1 |
| candidate terminal without plan terminal | 0 |
| orphan plan-linked decisions | 0 |

## 主要断点

| 诊断信号 | 是否存在 |
|---|---|
| pipeline_loss | `True` |
| lifecycle_blocked | `False` |
| execution_observability_gap | `True` |

## 更新跳过原因

| reason_code | Count |
|---|---:|
| `kline_error` | 1 |
| `ticker_error` | 33 |

## 按日阶段计数

| 日期 | 阶段计数 |
|---|---|
| `2026-07-29` | plan_update_skipped=1, terminal_reached=1 |
| `2026-07-31` | plan_update_skipped=3 |
| `2026-08-03` | plan_update_skipped=5 |
| `2026-08-04` | plan_update_skipped=5 |
| `2026-08-05` | candidate_observed=5 |
| `2026-08-06` | plan_update_skipped=5 |
| `2026-08-07` | plan_update_skipped=5 |
| `2026-08-08` | plan_update_skipped=5 |
| `2026-08-09` | candidate_observed=5, plan_update_skipped=5 |
| `2026-08-10` | candidate_observed=5 |
| `2026-08-11` | candidate_observed=5 |

## 当前开放计划生命周期

| Plan | Symbol | Status | Source scan | Rank | Events |
|---|---|---|---|---:|---|
| `9734a33dea2e` | `ONDOUSDT` | `WATCHING` | `7a562bac13ec` | 4 | `API_DELAY_SKIPPED` |

## 限制

- Historical reconstructed events are diagnostic evidence only and do not alter maturity or reconciliation gates.
- Candidate rows are correlated observations, not independent trades.
- No strategy configuration or paper state was changed by this audit.

- JSON sidecar: `paper_shadow_funnel_audit_2026-08-13_demo_v6.json`