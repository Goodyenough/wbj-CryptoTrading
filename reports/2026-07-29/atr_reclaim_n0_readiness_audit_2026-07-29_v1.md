---
created: 2026-07-29 23:42:18 CST
tags:
  - crypto
  - trading-system
  - atr-reclaim-n0-readiness
experiment: atr_reclaim_n0_readiness_audit
experiment_id: atr_reclaim_0_35
verdict: n0_conditional_pass_with_universe_bias_warning
---

# atr_reclaim_n0_readiness_audit

## Plain-language conclusion

Third-window retest can be run as a diagnostic, but the fixed symbol master lacks listing_dates, so the result cannot be treated as a clean confirmatory validation without survivor-bias caveat.

This is Stage N0 only. It freezes and audits prerequisites for the next retest; it does not run the `atr_reclaim_0_35` A/B, does not deploy, does not change `settings.toml`, does not restart replacement, and does not change `max_active_positions`.

## Scope

| Field | Value |
|---|---:|
| experiment_id | `atr_reclaim_0_35` |
| window | `2023-07-01T00:00:00+00:00` -> `2024-07-01T00:00:00+00:00` |
| git_commit | `4910a67f103d2c6d116f585e04bf66eaad7e2915` |
| git_dirty | False |
| settings_hash | `be7ec39ec21f6a838571511cb2cd0e290263031b521a9a07a6fb70164b8ef4bf` |
| experiments_hash | `7e6eca2609546d94293162870df6cc6ab8795666845b58facd979b698917dbe1` |
| symbol_master | `reports\2026-06-09\dynamic_master_full.json` |
| symbol_master_hash | `7e44a3b15294389e949e8c667e50592b5eed2d0ce8667d38da02a10847fbebdd` |
| symbol_master_count | 418 |
| symbol_master_created_at_utc | `2026-06-09T07:07:56+00:00` |

## Frozen Test Definition

| Field | Value |
|---|---|
| baseline.entry_reclaim_close_enabled | `True` |
| baseline.entry_reclaim_min_atr_enabled | `False` |
| baseline.entry_reclaim_min_atr | `0.0` |
| baseline.relative_strength_soft_gate_enabled | `False` |
| baseline.max_active_positions | `5` |
| baseline.intrabar_policy | `stop_first` |
| baseline.primary_interval | `4h` |
| baseline.maker_fee_bps | `4.0` |
| baseline.taker_fee_bps | `10.0` |
| baseline.entry_slippage_bps | `5.0` |
| baseline.stop_slippage_bps | `10.0` |
| variant.analysis.entry_reclaim_min_atr_enabled | `True` |
| variant.analysis.entry_reclaim_min_atr | `0.35` |
| fixed.production_settings_toml_unchanged | `True` |
| fixed.replacement_enabled | `False` |
| fixed.max_active_positions_changed | `False` |
| fixed.score_sorting_changed | `False` |
| fixed.additional_filters_stacked | `False` |
| fixed.main_test | `baseline_vs_fixed_atr_reclaim_0_35_only` |
| fixed.nearby_thresholds | `exploratory_only_if_run` |

## Symbol Master Audit

| Metric | Value |
|---|---:|
| source | `Binance current exchangeInfo tradable USDT spot symbols` |
| listing_dates_present | False |
| listed_after_start_count | n/a |
| missing_listing_dates_count | n/a |
| listed_after_start_examples | `n/a` |

## Local Kline Cache Coverage

| Interval | Symbols | Expected Bars/Symbol | Complete | Partial | Empty | Min Bars | Avg Bars | Coverage % | Examples |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `1h` | 418 | 10704 | 207 | 59 | 152 | 0 | 6007.565 | 56.124 | `0GUSDT, 1000CATUSDT, 1000CHEEMSUSDT, 1MBABYDOGEUSDT, 2ZUSDT, ACTUSDT, ACXUSDT, AIGENSYNUSDT` |
| `4h` | 418 | 2676 | 207 | 59 | 152 | 0 | 1501.921 | 56.126 | `0GUSDT, 1000CATUSDT, 1000CHEEMSUSDT, 1MBABYDOGEUSDT, 2ZUSDT, ACTUSDT, ACXUSDT, AIGENSYNUSDT` |
| `1d` | 418 | 446 | 207 | 59 | 152 | 0 | 250.383 | 56.140 | `0GUSDT, 1000CATUSDT, 1000CHEEMSUSDT, 1MBABYDOGEUSDT, 2ZUSDT, ACTUSDT, ACXUSDT, AIGENSYNUSDT` |

## Opportunity Alignment Capability

| Field | Available |
|---|---:|
| `symbol` | True |
| `decision_time_utc` | True |
| `status` | True |
| `baseline_first_hit` | True |
| `baseline_r` | True |
| `mfe_r` | True |
| `mae_r` | True |
| `reclaim_margin_atr` | True |
| `distance_to_support_atr` | True |
| `stop_distance_atr` | True |
| `capacity_state_at_decision` | False |
| `stable_opportunity_id_shared_by_baseline_variant` | False |

## Readiness Checks

| Check | Status |
|---|---|
| `git_clean` | `pass` |
| `listing_dates` | `warn_missing_listing_dates` |
| `listed_after_start` | `pass` |
| `kline_cache_coverage` | `warn_or_fail_incomplete_local_cache` |
| `opportunity_alignment` | `warn_not_strictly_capacity_path_neutral` |
| `prior_window_exists` | `pass` |

## Prior Third-window A/B References

| Path |
|---|
| `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\reports\2026-06-16\abtest_dynamic_universe_max_holding_42_fixed_vs_conditional_sensitive_2023-07-01_2024-07-01_v1.md` |

## N1 Gate

`n0_conditional_pass_with_universe_bias_warning`

## Recommended Next Action

N1 may run only as a clearly caveated third-window diagnostic. Do not call it clean confirmatory validation unless listing-date or historical membership evidence is added.

## Raw Summary

```json
{
  "experiment_id": "atr_reclaim_0_35",
  "report_date": "2026-07-29",
  "start_utc": "2023-07-01T00:00:00+00:00",
  "end_utc": "2024-07-01T00:00:00+00:00",
  "symbol_master_path": "reports\\2026-06-09\\dynamic_master_full.json",
  "symbol_master_source": "Binance current exchangeInfo tradable USDT spot symbols",
  "symbol_master_created_at_utc": "2026-06-09T07:07:56+00:00",
  "symbol_master_hash": "7e44a3b15294389e949e8c667e50592b5eed2d0ce8667d38da02a10847fbebdd",
  "settings_hash": "be7ec39ec21f6a838571511cb2cd0e290263031b521a9a07a6fb70164b8ef4bf",
  "experiments_hash": "7e6eca2609546d94293162870df6cc6ab8795666845b58facd979b698917dbe1",
  "git_commit": "4910a67f103d2c6d116f585e04bf66eaad7e2915",
  "git_dirty": false,
  "baseline_config_snapshot": {
    "entry_reclaim_close_enabled": true,
    "entry_reclaim_min_atr_enabled": false,
    "entry_reclaim_min_atr": 0.0,
    "relative_strength_soft_gate_enabled": false,
    "max_active_positions": 5,
    "intrabar_policy": "stop_first",
    "primary_interval": "4h",
    "maker_fee_bps": 4.0,
    "taker_fee_bps": 10.0,
    "entry_slippage_bps": 5.0,
    "stop_slippage_bps": 10.0
  },
  "variant_overrides": {
    "analysis.entry_reclaim_min_atr_enabled": true,
    "analysis.entry_reclaim_min_atr": 0.35
  },
  "fixed_conditions": {
    "production_settings_toml_unchanged": true,
    "replacement_enabled": false,
    "max_active_positions_changed": false,
    "score_sorting_changed": false,
    "additional_filters_stacked": false,
    "main_test": "baseline_vs_fixed_atr_reclaim_0_35_only",
    "nearby_thresholds": "exploratory_only_if_run"
  },
  "symbol_master_count": 418,
  "listing_dates_present": false,
  "listed_after_start_count": null,
  "listed_after_start_examples": [],
  "missing_listing_dates_count": null,
  "kline_coverage": {
    "1h": {
      "symbols": 418,
      "expected_bars_per_symbol": 10704,
      "complete_symbols": 207,
      "partial_symbols": 59,
      "empty_symbols": 152,
      "min_bars": 0,
      "avg_bars": 6007.564593301436,
      "coverage_pct": 56.124482373892334,
      "partial_examples": [
        "1000SATSUSDT",
        "ACEUSDT",
        "AEVOUSDT",
        "AIUSDT",
        "ALTUSDT",
        "ARKMUSDT",
        "ARKUSDT",
        "AXLUSDT",
        "BBUSDT",
        "BEAMXUSDT"
      ],
      "empty_examples": [
        "0GUSDT",
        "1000CATUSDT",
        "1000CHEEMSUSDT",
        "1MBABYDOGEUSDT",
        "2ZUSDT",
        "ACTUSDT",
        "ACXUSDT",
        "AIGENSYNUSDT",
        "AIXBTUSDT",
        "ALLOUSDT"
      ]
    },
    "4h": {
      "symbols": 418,
      "expected_bars_per_symbol": 2676,
      "complete_symbols": 207,
      "partial_symbols": 59,
      "empty_symbols": 152,
      "min_bars": 0,
      "avg_bars": 1501.921052631579,
      "coverage_pct": 56.125599874124774,
      "partial_examples": [
        "1000SATSUSDT",
        "ACEUSDT",
        "AEVOUSDT",
        "AIUSDT",
        "ALTUSDT",
        "ARKMUSDT",
        "ARKUSDT",
        "AXLUSDT",
        "BBUSDT",
        "BEAMXUSDT"
      ],
      "empty_examples": [
        "0GUSDT",
        "1000CATUSDT",
        "1000CHEEMSUSDT",
        "1MBABYDOGEUSDT",
        "2ZUSDT",
        "ACTUSDT",
        "ACXUSDT",
        "AIGENSYNUSDT",
        "AIXBTUSDT",
        "ALLOUSDT"
      ]
    },
    "1d": {
      "symbols": 418,
      "expected_bars_per_symbol": 446,
      "complete_symbols": 207,
      "partial_symbols": 59,
      "empty_symbols": 152,
      "min_bars": 0,
      "avg_bars": 250.38277511961724,
      "coverage_pct": 56.13963567704422,
      "partial_examples": [
        "1000SATSUSDT",
        "ACEUSDT",
        "AEVOUSDT",
        "AIUSDT",
        "ALTUSDT",
        "ARKMUSDT",
        "ARKUSDT",
        "AXLUSDT",
        "BBUSDT",
        "BEAMXUSDT"
      ],
      "empty_examples": [
        "0GUSDT",
        "1000CATUSDT",
        "1000CHEEMSUSDT",
        "1MBABYDOGEUSDT",
        "2ZUSDT",
        "ACTUSDT",
        "ACXUSDT",
        "AIGENSYNUSDT",
        "AIXBTUSDT",
        "ALLOUSDT"
      ]
    }
  },
  "prior_third_window_abtests": [
    "D:\\OneDrive - whut.edu.cn\\文档\\CryptoTradingPorjects\\reports\\2026-06-16\\abtest_dynamic_universe_max_holding_42_fixed_vs_conditional_sensitive_2023-07-01_2024-07-01_v1.md"
  ],
  "opportunity_alignment_fields": {
    "symbol": true,
    "decision_time_utc": true,
    "status": true,
    "baseline_first_hit": true,
    "baseline_r": true,
    "mfe_r": true,
    "mae_r": true,
    "reclaim_margin_atr": true,
    "distance_to_support_atr": true,
    "stop_distance_atr": true,
    "capacity_state_at_decision": false,
    "stable_opportunity_id_shared_by_baseline_variant": false
  },
  "readiness_checks": {
    "git_clean": "pass",
    "listing_dates": "warn_missing_listing_dates",
    "listed_after_start": "pass",
    "kline_cache_coverage": "warn_or_fail_incomplete_local_cache",
    "opportunity_alignment": "warn_not_strictly_capacity_path_neutral",
    "prior_window_exists": "pass"
  },
  "verdict": "n0_conditional_pass_with_universe_bias_warning",
  "reason": "Third-window retest can be run as a diagnostic, but the fixed symbol master lacks listing_dates, so the result cannot be treated as a clean confirmatory validation without survivor-bias caveat."
}
```
