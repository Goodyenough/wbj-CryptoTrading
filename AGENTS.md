# Workspace Rules

These rules apply to the entire CryptoTradingSystem workspace.

## Change Logging And Commits

- After every code change, update `dailylog.md` with a Beijing time timestamp and a concise record of what changed, why it changed, how it was verified, and the related Git commit.
- After every code change, create a Git commit for the completed change before considering the task finished.
- Keep generated local state such as `data/crypto_trading.db` out of commits unless the user explicitly requests otherwise.
- If a change cannot be committed, record the reason in `dailylog.md` and tell the user clearly.

## Project Memory Rules

Use these files as separate memory layers:

- `dailylog.md`: engineering audit log for code/config/project-file changes.
- `TODO.md`: actionable engineering tasks.
- `D:\MyNotebook-Obsidian\CryptoTradingSystem\CryptoTradingSystem 开发计划.md`: roadmap, module status, and next priority.
- `D:\MyNotebook-Obsidian\CryptoTradingSystem\CryptoTrading 实验日志.md`: backtest, A/B, paper-trading experiments, results, and conclusions.

Before finishing any task, decide which files must be updated:

- If code/config/tests/docs inside the repo changed, update `dailylog.md` and create a Git commit.
- If an actionable task is created, completed, cancelled, or reprioritized, update `TODO.md`.
- If module status, project phase, or next priority changes, update the Obsidian development plan.
- If a backtest, A/B experiment, scan comparison, or paper-trading evaluation was run and produced a judgment, update the Obsidian experiment log.

Do not overload files:

- `dailylog.md` should not contain long experiment analysis.
- `TODO.md` should not contain narrative reasoning.
- The development plan should not contain raw metric dumps.
- The experiment log should contain the research narrative and the keep/revert/retest conclusion.

Experiment log entries must include:

- Experiment name.
- Change tested.
- Symbols and date range.
- Baseline vs variant metrics.
- `keep / revert / retest` conclusion.
- One-sentence reason.
- Next action.

Use this event-to-file decision table:

| Event | dailylog.md | TODO.md | Development plan | Experiment log |
|---|---|---|---|---|
| Code/config/project-file changed | Required | If tasks changed | If phase changed | No |
| Backtest or A/B experiment run | No | If new tasks arise | If roadmap changes | Required |
| New actionable task found | No | Required | If priority changes | Optional |
| Module completed | Required | Required | Required | Optional |
| Concept learned | No | No | No | Learning note, not these four files |
| Project direction changed | Optional | Required | Required | Required if experiment-driven |

Use this template for experiment-log entries:

```markdown
## YYYY-MM-DD HH:mm +08:00 - Experiment title

### Background
Why this experiment was run.

### Hypothesis
What the experiment is testing.

### Experiment
- Experiment: [name]
- Change: [specific change]
- Sample: [symbols / date range / parameters]

### Results
- trades: baseline -> variant, delta X%
- closed_trades: baseline -> variant, delta X%
- win_rate: baseline -> variant, delta X%
- Profit factor: baseline -> variant
- Sharpe: baseline -> variant
- Max drawdown: baseline -> variant
- Net return: baseline -> variant

### Conclusion
keep / revert / retest: one-sentence reason.

### Next Action
What should happen next.
```
