# Workspace Rules

These rules apply to the entire CryptoTradingSystem workspace.

## Change Logging And Commits

- After every code change, update `dailylog.md` with a Beijing time timestamp and a concise record of what changed, why it changed, how it was verified, and the related Git commit.
- After every code change, create a Git commit for the completed change before considering the task finished.
- Keep generated local state such as `data/crypto_trading.db` out of commits unless the user explicitly requests otherwise.
- If a change cannot be committed, record the reason in `dailylog.md` and tell the user clearly.
