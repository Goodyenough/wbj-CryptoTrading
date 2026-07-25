from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from crypto_trading_system.paper_audit import DataLinkHealth, OpportunityRow, RunTypeHealth
from crypto_trading_system.paper_checkpoint import (
    PaperCheckpoint,
    checkpoint_summary_lines,
    decide_checkpoint,
    render_paper_checkpoint_report,
)


def _run_type(run_type: str) -> RunTypeHealth:
    return RunTypeHealth(
        run_type=run_type,
        expected_runs=1,
        observed_runs=1,
        success_runs=1,
        failed_runs=0,
        running_runs=0,
        success_rate_pct=100.0,
        latest_started_at="2026-07-16T12:00:00Z",
    )


def _data_link(*, verdict: str = "pass", config_hash_stable: bool = True) -> DataLinkHealth:
    return DataLinkHealth(
        daily=_run_type("daily_full"),
        paper_4h=_run_type("paper_4h_update"),
        config_hashes=["be7ec39ec21f6a83"],
        config_hash_stable=config_hash_stable,
        stale_running_runs=0,
        duplicate_events=0,
        impossible_event_order=0,
        verdict=verdict,
        note="ok",
    )


def _opportunity(status: str = "mature") -> OpportunityRow:
    return OpportunityRow(
        source="WATCH_ONLY",
        symbol="TESTUSDT",
        plan_id="plan1",
        first_time="2026-07-03T12:00:00Z",
        reason="test",
        entry=100.0,
        entry_low=98.0,
        stop=90.0,
        tp1=120.0,
        max_price_after=110.0,
        min_price_after=95.0,
        reclaimed=True,
        hit_tp1=False,
        hit_stop=False,
        classification="neutral_or_unknown",
        explanation="test",
        observation_bars=42 if status == "mature" else 5,
        required_bars=42,
        maturity_status=status,
        classification_final=status == "mature",
    )


def test_checkpoint_decision_ready_when_data_and_samples_are_mature() -> None:
    decision = decide_checkpoint(_data_link(), [_opportunity() for _ in range(20)])
    assert decision.verdict == "formal_audit_ready"


def test_checkpoint_decision_interim_on_config_hash_drift() -> None:
    decision = decide_checkpoint(_data_link(config_hash_stable=False), [_opportunity() for _ in range(20)])
    assert decision.verdict == "interim_report_required"
    assert "config_hash" in decision.reason


def test_checkpoint_decision_waits_when_right_censored_ratio_is_high() -> None:
    opportunities = [_opportunity() for _ in range(20)] + [_opportunity("right_censored") for _ in range(20)]
    decision = decide_checkpoint(_data_link(), opportunities)
    assert decision.verdict == "wait_for_more_data"
    assert "right-censored" in decision.reason


def test_checkpoint_report_contains_gates_and_next_commands() -> None:
    opportunities = [_opportunity() for _ in range(20)]
    checkpoint = PaperCheckpoint(
        account="demo",
        start_date="2026-07-03",
        end_date="2026-07-16",
        data_link=_data_link(),
        opportunities=opportunities,
        entered_trades=[],
        entry_reclaim_shadow=[],
        relative_strength_shadow=[],
        decision=decide_checkpoint(_data_link(), opportunities),
    )
    text = render_paper_checkpoint_report(checkpoint, 1)
    assert "## Data Link Gate" in text
    assert "## Sample Maturity Gate" in text
    assert "python main.py paper audit" in text
    assert "relative_strength_gate" in text


def test_checkpoint_summary_lines_expose_cli_gate_values() -> None:
    opportunities = [_opportunity() for _ in range(20)]
    checkpoint = PaperCheckpoint(
        account="demo",
        start_date="2026-07-03",
        end_date="2026-07-16",
        data_link=_data_link(),
        opportunities=opportunities,
        entered_trades=[],
        entry_reclaim_shadow=[],
        relative_strength_shadow=[],
        decision=decide_checkpoint(_data_link(), opportunities),
    )
    lines = checkpoint_summary_lines(checkpoint)
    assert "verdict=formal_audit_ready" in lines
    assert "mature=20" in lines
    assert "right_censored_ratio=0.0%" in lines
    assert any(line.startswith("next_action=") for line in lines)


if __name__ == "__main__":
    test_checkpoint_decision_ready_when_data_and_samples_are_mature()
    test_checkpoint_decision_interim_on_config_hash_drift()
    test_checkpoint_decision_waits_when_right_censored_ratio_is_high()
    test_checkpoint_report_contains_gates_and_next_commands()
    test_checkpoint_summary_lines_expose_cli_gate_values()
