---
created: 2026-07-30T00:56:54+08:00
tags:
  - crypto
  - trading-system
  - universe-audit
experiment: atr_reclaim_stage_n2_universe_audit
verdict: diagnostic_only_historical_membership_gap
---

# Stage N2 Universe And Data Substrate Audit

## Plain-language conclusion

The third window should remain diagnostic only. Current-master listing dates reduce future-symbol ambiguity, but Binance public-data membership shows many USDT symbols with 1d monthly files inside the window that are missing from the current master.

## Artifacts

| Artifact | Path |
|---|---|
| raw_audit_json | `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-07-30\atr_reclaim_stage_n2_universe_audit_2026-07-30_raw_v2.json` |
| current_master_json | `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-07-30\atr_reclaim_stage_n2_universe_audit_2026-07-30_current_master_v2.json` |
| historical_membership_json | `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-07-30\atr_reclaim_stage_n2_universe_audit_2026-07-30_historical_membership_v2.json` |
| listing_enriched_master | `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-07-30\dynamic_master_full_listing_enriched_2026-07-30_v2.json` |

## N2-A Current Master Audit

| Metric | Value |
|---|---:|
| symbol_master_count | 418 |
| listing_dates_count | 418 |
| full_window_coverage | 208 |
| listed_after_window | 152 |
| listed_inside_window | 49 |
| partial_window_coverage | 9 |

## N2-B Historical Membership Audit

| Metric | Value |
|---|---:|
| historical_usdt_symbols_with_1d_monthly_data_in_window | 413 |
| present_in_current_master | 266 |
| missing_from_current_master | 147 |

### Missing-from-current examples

`ACAUSDT`, `ADADOWNUSDT`, `ADAUPUSDT`, `AERGOUSDT`, `AEURUSDT`, `AGIXUSDT`, `AKROUSDT`, `ALPACAUSDT`, `ALPHAUSDT`, `AMBUSDT`, `ANTUSDT`, `ASTUSDT`, `ATAUSDT`, `BADGERUSDT`, `BAKEUSDT`, `BALUSDT`, `BETAUSDT`, `BETHUSDT`, `BIFIUSDT`, `BLZUSDT`, `BNBDOWNUSDT`, `BNBUPUSDT`, `BNXUSDT`, `BONDUSDT`, `BSWUSDT`, `BTCDOWNUSDT`, `BTCUPUSDT`, `BTSUSDT`, `BURGERUSDT`, `BUSDUSDT`, `CHESSUSDT`, `CLVUSDT`, `COMBOUSDT`, `CREAMUSDT`, `CTXCUSDT`, `CVPUSDT`, `DARUSDT`, `DATAUSDT`, `DEGOUSDT`, `DENTUSDT`, `DFUSDT`, `DOCKUSDT`, `DREPUSDT`, `ELFUSDT`, `EOSUSDT`, `EPXUSDT`, `ERNUSDT`, `ETHDOWNUSDT`, `ETHUPUSDT`, `EURUSDT`

## Window Qualification

`diagnostic_only_historical_membership_gap`

## Decision

Do not treat the third window as a clean confirmatory validation unless historical membership is reconstructed or the missing-current-master bias is proven immaterial. If N0 is rerun with listing dates, its result must be interpreted together with this N2-B membership gap.

## Raw Summary

```json
{
  "generated_at_utc": "2026-07-29T16:56:54+00:00",
  "start": "2023-07-01",
  "end": "2024-07-01",
  "symbol_master_count": 418,
  "listing_dates_count": 418,
  "current_master_classification_counts": {
    "listed_after_window": 152,
    "listed_inside_window": 49,
    "full_window_coverage": 208,
    "partial_window_coverage": 9
  },
  "historical_membership_counts": {
    "historical_usdt_symbols_with_1d_monthly_data_in_window": 413,
    "missing_from_current_master": 147,
    "present_in_current_master": 266
  },
  "missing_from_current_master_examples": [
    "ACAUSDT",
    "ADADOWNUSDT",
    "ADAUPUSDT",
    "AERGOUSDT",
    "AEURUSDT",
    "AGIXUSDT",
    "AKROUSDT",
    "ALPACAUSDT",
    "ALPHAUSDT",
    "AMBUSDT",
    "ANTUSDT",
    "ASTUSDT",
    "ATAUSDT",
    "BADGERUSDT",
    "BAKEUSDT",
    "BALUSDT",
    "BETAUSDT",
    "BETHUSDT",
    "BIFIUSDT",
    "BLZUSDT",
    "BNBDOWNUSDT",
    "BNBUPUSDT",
    "BNXUSDT",
    "BONDUSDT",
    "BSWUSDT",
    "BTCDOWNUSDT",
    "BTCUPUSDT",
    "BTSUSDT",
    "BURGERUSDT",
    "BUSDUSDT",
    "CHESSUSDT",
    "CLVUSDT",
    "COMBOUSDT",
    "CREAMUSDT",
    "CTXCUSDT",
    "CVPUSDT",
    "DARUSDT",
    "DATAUSDT",
    "DEGOUSDT",
    "DENTUSDT",
    "DFUSDT",
    "DOCKUSDT",
    "DREPUSDT",
    "ELFUSDT",
    "EOSUSDT",
    "EPXUSDT",
    "ERNUSDT",
    "ETHDOWNUSDT",
    "ETHUPUSDT",
    "EURUSDT"
  ],
  "window_qualification": "diagnostic_only_historical_membership_gap"
}
```
