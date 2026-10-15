# Verification

- Decision: `reject_current_realtime_reclaim`.
- Early candidates: `1090`; near candidates: `770`.
- Causal violations: early `0`, near `0`.
- Candidate 1h/4h aggregation: early `1090/1090`, near `770/770`.
- Event generation never reads retained_4h_confirmation; future retention is added only after the event list is frozen.
- No network or database writes; no production, paper, shadow, schedule, or configuration changes.
