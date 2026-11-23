# Independent result QA

Status: **PASS**. Reviewed only the six named result files in this directory plus the five code files explicitly listed in run_manifest.json. No raw market caches, production data/database, other report directories, or sealed-period market data were opened. No strategy was rerun; no code or parameters were changed.

- Run commit: `b1b7d780e5639221811a393cf04c2c6b19f47d99`.
- Checked 16 unique branches, 36,392 trade rows, 192 monthly rows, and 175,095 exported equity rows; 775,812 arithmetic/boundary assertions.
- Failure counts: `{}`.
- Per-trade gross PnL, entry/exit slippage, both fees, signed funding charges/receipts, net PnL, and account balance chains reconcile. Branch PnL equals final equity minus the separate 110 USDT starting equity; monthly and direction aggregates reconcile.
- Maximum planned stop risk: 5.000000000000 USDT (cap 5); maximum entry-notional / entry-equity: 1.000000000000 (cap 1). Reference margin equals half the entry notional. These are planned model quantities, not a validated liquidation model.
- Entry is decision + 5 minutes; positions do not overlap or cross yearly evaluation boundaries. All entries, exits, funding events and exported equity timestamps are strictly before cutoff `1782144000000`. Checked 7,197 per-trade funding applications including repeated scenarios.
- Declared source data cover only December 2023 through December 2025: 219,456 trade 5M bars and 75 explicitly named trade/mark/funding archives. Source manifest maxima are before 2026. Archive payload hashes were not independently recomputed because raw caches were deliberately not read.
- All five current code/protocol SHA256 hashes match the frozen run manifest. This verifies artifact/code consistency, not that the data manifests alone independently prove raw download completeness.
- All hourly close points and every exact/assumed exit equity point are present in equity.csv. Full 5M maximum drawdown is not independently reconstructed from the hourly export; exported drawdown does not exceed the reported full-5M measure.
- Target-clamp cases: 0; therefore the clamp correction did not affect any recorded trade in this run.

## Interpretation

The rejection of the four preregistered candidates is well supported within this historical mathematical model: every 2025 normal-cost branch has negative mean net R, Profit Factor below 1, negative long-side and short-side mean net R, and an entirely negative month-cluster 95% interval. The pressure-cost branches also lose. This is not a calibrated future price probability, a proof against all momentum strategies, or an executable-account forecast.

The very large full-year percentage losses are model-path figures. Quantity remains continuous and the simulator keeps trading as capital shrinks, including orders too small to treat as proven executable. Historical lot/tick sizes, minimum order notional, historical maintenance margin/liquidation, order-book depth and partial fills are not reconstructed. No exact historical minimum-order threshold has been applied in this QA.

Funding uses official historical rates with an earlier/same-bucket mark-open proxy rather than the exact settlement bill; declared maximum proxy age is 16 ms. Intrabar funding and price-touch ordering remains an explicit assumption. Fixed fees/slippage and 12 monthly uncertainty blocks also limit precision. These limits constrain numerical loss-path interpretation; the study gives no positive evidence for deploying this fixed candidate.

## Reconciled branches

| Window | Net target | Hold | Cost | Trades | Final equity USDT | Mean net R | Minimum entry notional USDT | Entries with equity < 1 USDT |
|---|---:|---:|---|---:|---:|---:|---:|---:|
| development_2024 | 1% | 2h | normal | 2575 | 2.97897415 | -0.092980 | 2.78672440 | 0 |
| development_2024 | 1% | 2h | stress | 2412 | 0.00950976 | -0.210364 | 0.00938835 | 1316 |
| development_2024 | 1% | 4h | normal | 2343 | 2.81467359 | -0.098015 | 2.48653171 | 0 |
| development_2024 | 1% | 4h | stress | 2153 | 0.02346671 | -0.205463 | 0.02331947 | 1028 |
| development_2024 | 2% | 2h | normal | 2167 | 3.94691853 | -0.108865 | 3.65013033 | 0 |
| development_2024 | 2% | 2h | stress | 2121 | 0.02446613 | -0.228152 | 0.02443556 | 1095 |
| development_2024 | 2% | 4h | normal | 1839 | 5.46686958 | -0.107176 | 4.95856164 | 0 |
| development_2024 | 2% | 4h | stress | 1779 | 0.09419454 | -0.224703 | 0.09310512 | 639 |
| validation_2025 | 1% | 2h | normal | 2794 | 2.70940264 | -0.076041 | 2.71380983 | 0 |
| validation_2025 | 1% | 2h | stress | 2628 | 0.00801015 | -0.176465 | 0.00806259 | 1472 |
| validation_2025 | 1% | 4h | normal | 2564 | 4.20941192 | -0.072207 | 4.24576157 | 0 |
| validation_2025 | 1% | 4h | stress | 2373 | 0.02198823 | -0.169811 | 0.02228771 | 1227 |
| validation_2025 | 2% | 2h | normal | 2362 | 4.23021371 | -0.090211 | 4.23751010 | 0 |
| validation_2025 | 2% | 2h | stress | 2300 | 0.01857346 | -0.192094 | 0.01869689 | 1206 |
| validation_2025 | 2% | 4h | normal | 2023 | 10.02973993 | -0.074104 | 8.15680742 | 0 |
| validation_2025 | 2% | 4h | stress | 1959 | 0.09287558 | -0.175841 | 0.09414978 | 853 |
