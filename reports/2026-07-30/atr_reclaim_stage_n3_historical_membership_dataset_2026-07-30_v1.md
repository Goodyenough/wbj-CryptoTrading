---
created: 2026-07-30T11:34:41+08:00
tags:
  - crypto
  - trading-system
  - historical-membership
experiment: atr_reclaim_stage_n3_historical_membership_dataset
verdict: third_window_not_recoverable_without_historical_master
---

# Stage N3 Historical Membership Dataset MVP

## Plain-language conclusion

The third window still should not be rescued for validation. After excluding obvious leveraged tokens, stable/fiat pairs, and known nonstandard assets, the missing historical standard-like spot gap remains material.

## Artifacts

| Artifact | Path |
|---|---|
| dataset_json | `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-07-30\atr_reclaim_stage_n3_historical_membership_dataset_2026-07-30_dataset_v1.json` |
| raw_summary_json | `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-07-30\atr_reclaim_stage_n3_historical_membership_dataset_2026-07-30_raw_v1.json` |

## Scope

- Window: `2023-07-01 -> 2024-07-01`
- Historical symbols: `413`
- Present in current master: `266`
- Missing from current master: `147`

## Missing Symbol Classification

| Metric | Value |
|---|---:|
| excludable_missing_count | 20 |
| standard_gap_count | 127 |
| standard_universe_count | 393 |
| standard_gap_ratio_pct | 32.32 |

### Missing Type Counts

| Type | Count |
|---|---:|
| `leveraged_token` | 9 |
| `nonstandard_wrapped_or_staked_asset` | 1 |
| `stable_or_fiat_or_excluded_base` | 10 |
| `standard_spot_missing_from_current_master` | 120 |
| `standard_spot_rename_or_migration_candidate` | 7 |

### Standard-like missing examples

`ACAUSDT`, `AERGOUSDT`, `AGIXUSDT`, `AKROUSDT`, `ALPACAUSDT`, `ALPHAUSDT`, `AMBUSDT`, `ANTUSDT`, `ASTUSDT`, `ATAUSDT`, `BADGERUSDT`, `BAKEUSDT`, `BALUSDT`, `BETAUSDT`, `BIFIUSDT`, `BLZUSDT`, `BNXUSDT`, `BONDUSDT`, `BSWUSDT`, `BTSUSDT`, `BURGERUSDT`, `CHESSUSDT`, `CLVUSDT`, `COMBOUSDT`, `CREAMUSDT`, `CTXCUSDT`, `CVPUSDT`, `DARUSDT`, `DATAUSDT`, `DEGOUSDT`, `DENTUSDT`, `DFUSDT`, `DOCKUSDT`, `DREPUSDT`, `ELFUSDT`, `EOSUSDT`, `EPXUSDT`, `ERNUSDT`, `FARMUSDT`, `FIOUSDT`, `FIROUSDT`, `FISUSDT`, `FLMUSDT`, `FORTHUSDT`, `FORUSDT`, `FRONTUSDT`, `FTMUSDT`, `FUNUSDT`, `FXSUSDT`, `GALUSDT`, `GFTUSDT`, `GHSTUSDT`, `HARDUSDT`, `HIFIUSDT`, `HOOKUSDT`, `IDEXUSDT`, `IRISUSDT`, `KDAUSDT`, `KEYUSDT`, `KLAYUSDT`, `KMDUSDT`, `KP3RUSDT`, `LEVERUSDT`, `LINAUSDT`, `LITUSDT`, `LOKAUSDT`, `LOOMUSDT`, `LRCUSDT`, `LTOUSDT`, `MATICUSDT`, `MCUSDT`, `MDTUSDT`, `MDXUSDT`, `MKRUSDT`, `MLNUSDT`, `MOBUSDT`, `MULTIUSDT`, `NKNUSDT`, `NTRNUSDT`, `NULSUSDT`

### Excludable missing examples

`ADADOWNUSDT`, `ADAUPUSDT`, `AEURUSDT`, `BETHUSDT`, `BNBDOWNUSDT`, `BNBUPUSDT`, `BTCDOWNUSDT`, `BTCUPUSDT`, `BUSDUSDT`, `ETHDOWNUSDT`, `ETHUPUSDT`, `EURUSDT`, `FDUSDUSDT`, `GBPUSDT`, `JUPUSDT`, `PAXGUSDT`, `TUSDUSDT`, `USDCUSDT`, `USDPUSDT`, `USTCUSDT`

## Verdict

`third_window_not_recoverable_without_historical_master`

Standard-like historical symbol gap remains material after excluding leveraged, stable/fiat, and nonstandard assets.

## Decision

Do not rerun corrected N1 on the third window until a historical master can add or explicitly exclude the standard-like missing symbols with source-backed rules.

## Raw Summary

```json
{
  "total_historical_symbols": 413,
  "present_in_current_master": 266,
  "missing_from_current_master": 147,
  "excludable_missing_count": 20,
  "standard_gap_count": 127,
  "standard_universe_count": 393,
  "standard_gap_ratio_pct": 32.31552162849873,
  "missing_symbol_type_counts": {
    "leveraged_token": 9,
    "nonstandard_wrapped_or_staked_asset": 1,
    "stable_or_fiat_or_excluded_base": 10,
    "standard_spot_missing_from_current_master": 120,
    "standard_spot_rename_or_migration_candidate": 7
  },
  "standard_gap_examples": [
    "ACAUSDT",
    "AERGOUSDT",
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
    "BIFIUSDT",
    "BLZUSDT",
    "BNXUSDT",
    "BONDUSDT",
    "BSWUSDT",
    "BTSUSDT",
    "BURGERUSDT",
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
    "FARMUSDT",
    "FIOUSDT",
    "FIROUSDT",
    "FISUSDT",
    "FLMUSDT",
    "FORTHUSDT",
    "FORUSDT",
    "FRONTUSDT",
    "FTMUSDT",
    "FUNUSDT",
    "FXSUSDT",
    "GALUSDT",
    "GFTUSDT",
    "GHSTUSDT",
    "HARDUSDT",
    "HIFIUSDT",
    "HOOKUSDT",
    "IDEXUSDT",
    "IRISUSDT",
    "KDAUSDT",
    "KEYUSDT",
    "KLAYUSDT",
    "KMDUSDT",
    "KP3RUSDT",
    "LEVERUSDT",
    "LINAUSDT",
    "LITUSDT",
    "LOKAUSDT",
    "LOOMUSDT",
    "LRCUSDT",
    "LTOUSDT",
    "MATICUSDT",
    "MCUSDT",
    "MDTUSDT",
    "MDXUSDT",
    "MKRUSDT",
    "MLNUSDT",
    "MOBUSDT",
    "MULTIUSDT",
    "NKNUSDT",
    "NTRNUSDT",
    "NULSUSDT"
  ],
  "verdict": "third_window_not_recoverable_without_historical_master"
}
```
