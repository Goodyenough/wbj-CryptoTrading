---
created: 2026-07-30T11:44:20+08:00
tags:
  - crypto
  - trading-system
  - historical-master
experiment: atr_reclaim_stage_n4_historical_master_mvp
verdict: historical_master_mvp_built_validation_blocked
---

# Stage N4 Historical Master MVP

## Plain-language conclusion

A first historical master dataset now exists, but it is not validation-ready because standard-like missing symbols still need source-backed mapping.

## Artifacts

| Artifact | Path |
|---|---|
| historical_master_mvp_json | `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-07-30\atr_reclaim_stage_n4_historical_master_mvp_2026-07-30_master_v1.json` |
| blocking_review_queue_json | `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-07-30\atr_reclaim_stage_n4_historical_master_mvp_2026-07-30_review_queue_v1.json` |
| raw_summary_json | `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-07-30\atr_reclaim_stage_n4_historical_master_mvp_2026-07-30_raw_v1.json` |

## Scope

- Window: `2023-07-01 -> 2024-07-01`
- Historical master rows: `413`
- Blocking review queue: `127`

## Membership Status Counts

| Status | Count |
|---|---:|
| `active_current_master` | 266 |
| `excluded_by_strategy_universe_rule` | 20 |
| `historical_standard_gap_requires_mapping` | 127 |

## Operational Action Counts

| Action | Count |
|---|---:|
| `eligible_for_dynamic_universe_if_data_and_liquidity_pass` | 266 |
| `exclude_from_historical_master` | 20 |
| `manual_review_delisting_or_exclusion_before_validation` | 120 |
| `manual_review_rename_or_migration_before_validation` | 7 |

## Review Queue Examples

| Symbol | Type | First Month | Last Month | Window Months |
|---|---|---:|---:|---:|
| `ACAUSDT` | `standard_spot_missing_from_current_master` | `2022-01` | `2026-02` | 12 |
| `AERGOUSDT` | `standard_spot_missing_from_current_master` | `2023-05` | `2025-03` | 12 |
| `AGIXUSDT` | `standard_spot_rename_or_migration_candidate` | `2023-02` | `2024-07` | 12 |
| `AKROUSDT` | `standard_spot_missing_from_current_master` | `2020-11` | `2024-12` | 12 |
| `ALPACAUSDT` | `standard_spot_missing_from_current_master` | `2021-08` | `2025-05` | 12 |
| `ALPHAUSDT` | `standard_spot_missing_from_current_master` | `2020-10` | `2025-07` | 12 |
| `AMBUSDT` | `standard_spot_missing_from_current_master` | `2023-03` | `2025-02` | 12 |
| `ANTUSDT` | `standard_spot_missing_from_current_master` | `2020-08` | `2024-02` | 8 |
| `ASTUSDT` | `standard_spot_missing_from_current_master` | `2023-05` | `2025-03` | 12 |
| `ATAUSDT` | `standard_spot_missing_from_current_master` | `2021-06` | `2026-05` | 12 |
| `BADGERUSDT` | `standard_spot_missing_from_current_master` | `2021-03` | `2025-04` | 12 |
| `BAKEUSDT` | `standard_spot_missing_from_current_master` | `2021-04` | `2025-09` | 12 |
| `BALUSDT` | `standard_spot_missing_from_current_master` | `2020-08` | `2025-04` | 12 |
| `BETAUSDT` | `standard_spot_missing_from_current_master` | `2021-10` | `2025-04` | 12 |
| `BIFIUSDT` | `standard_spot_missing_from_current_master` | `2022-04` | `2026-04` | 12 |
| `BLZUSDT` | `standard_spot_missing_from_current_master` | `2020-08` | `2024-12` | 12 |
| `BNXUSDT` | `standard_spot_missing_from_current_master` | `2021-11` | `2025-03` | 12 |
| `BONDUSDT` | `standard_spot_missing_from_current_master` | `2021-07` | `2024-07` | 12 |
| `BSWUSDT` | `standard_spot_missing_from_current_master` | `2022-03` | `2025-07` | 12 |
| `BTSUSDT` | `standard_spot_missing_from_current_master` | `2020-02` | `2023-12` | 6 |
| `BURGERUSDT` | `standard_spot_missing_from_current_master` | `2021-04` | `2025-03` | 12 |
| `CHESSUSDT` | `standard_spot_missing_from_current_master` | `2021-10` | `2026-02` | 12 |
| `CLVUSDT` | `standard_spot_missing_from_current_master` | `2021-07` | `2025-02` | 12 |
| `COMBOUSDT` | `standard_spot_missing_from_current_master` | `2023-06` | `2025-03` | 12 |
| `CREAMUSDT` | `standard_spot_missing_from_current_master` | `2023-09` | `2025-04` | 10 |
| `CTXCUSDT` | `standard_spot_missing_from_current_master` | `2019-11` | `2025-04` | 12 |
| `CVPUSDT` | `standard_spot_missing_from_current_master` | `2021-10` | `2024-08` | 12 |
| `DARUSDT` | `standard_spot_missing_from_current_master` | `2021-11` | `2025-01` | 12 |
| `DATAUSDT` | `standard_spot_missing_from_current_master` | `2020-04` | `2026-02` | 12 |
| `DEGOUSDT` | `standard_spot_missing_from_current_master` | `2021-03` | `2026-04` | 12 |
| `DENTUSDT` | `standard_spot_missing_from_current_master` | `2019-08` | `2026-04` | 12 |
| `DFUSDT` | `standard_spot_missing_from_current_master` | `2021-09` | `2026-02` | 12 |
| `DOCKUSDT` | `standard_spot_missing_from_current_master` | `2019-08` | `2024-07` | 12 |
| `DREPUSDT` | `standard_spot_missing_from_current_master` | `2020-01` | `2024-04` | 10 |
| `ELFUSDT` | `standard_spot_missing_from_current_master` | `2021-09` | `2025-04` | 12 |
| `EOSUSDT` | `standard_spot_missing_from_current_master` | `2018-05` | `2025-05` | 12 |
| `EPXUSDT` | `standard_spot_missing_from_current_master` | `2022-05` | `2024-08` | 12 |
| `ERNUSDT` | `standard_spot_missing_from_current_master` | `2021-06` | `2025-03` | 12 |
| `FARMUSDT` | `standard_spot_missing_from_current_master` | `2021-08` | `2026-05` | 12 |
| `FIOUSDT` | `standard_spot_missing_from_current_master` | `2020-09` | `2026-04` | 12 |
| `FIROUSDT` | `standard_spot_missing_from_current_master` | `2021-01` | `2025-04` | 12 |
| `FISUSDT` | `standard_spot_missing_from_current_master` | `2021-03` | `2025-12` | 12 |
| `FLMUSDT` | `standard_spot_missing_from_current_master` | `2020-09` | `2025-11` | 12 |
| `FORTHUSDT` | `standard_spot_missing_from_current_master` | `2021-04` | `2026-04` | 12 |
| `FORUSDT` | `standard_spot_missing_from_current_master` | `2021-08` | `2024-08` | 12 |
| `FRONTUSDT` | `standard_spot_missing_from_current_master` | `2021-10` | `2024-08` | 12 |
| `FTMUSDT` | `standard_spot_rename_or_migration_candidate` | `2019-06` | `2025-01` | 12 |
| `FUNUSDT` | `standard_spot_missing_from_current_master` | `2019-08` | `2026-04` | 12 |
| `FXSUSDT` | `standard_spot_missing_from_current_master` | `2021-12` | `2026-01` | 12 |
| `GALUSDT` | `standard_spot_rename_or_migration_candidate` | `2022-05` | `2024-07` | 12 |

## Verdict

`historical_master_mvp_built_validation_blocked`

127 standard-like historical symbols still require source-backed mapping before validation.

## Decision

Do not connect this MVP historical master to A/B execution yet. It is a data-engineering artifact until the blocking review queue is resolved or quantified as immaterial.

## Raw Summary

```json
{
  "total_rows": 413,
  "membership_status_counts": {
    "active_current_master": 266,
    "excluded_by_strategy_universe_rule": 20,
    "historical_standard_gap_requires_mapping": 127
  },
  "operational_action_counts": {
    "eligible_for_dynamic_universe_if_data_and_liquidity_pass": 266,
    "exclude_from_historical_master": 20,
    "manual_review_delisting_or_exclusion_before_validation": 120,
    "manual_review_rename_or_migration_before_validation": 7
  },
  "blocking_review_count": 127,
  "verdict": "historical_master_mvp_built_validation_blocked",
  "reason": "127 standard-like historical symbols still require source-backed mapping before validation."
}
```
