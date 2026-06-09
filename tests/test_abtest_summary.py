from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from crypto_trading_system.abtest_summary import build_abtest_summary, load_abtest_records


def _write_report(
    directory: Path,
    name: str,
    *,
    experiment_id: str = "liquidity_50m",
    sample_sufficient: bool = True,
    baseline_closed: int = 20,
    variant_closed: int = 20,
    baseline_pf: float = 0.4,
    variant_pf: float = 0.6,
    baseline_net: float = -10.0,
    variant_net: float = -5.0,
    baseline_mdd: float = 20.0,
    variant_mdd: float = 15.0,
) -> None:
    variant_sample = "true" if variant_closed >= 20 else "false"
    directory.mkdir(parents=True, exist_ok=True)
    (directory / name).write_text(
        "\n".join(
            [
                "---",
                f"experiment_id: {experiment_id}",
                "universe_mode: dynamic",
                f"sample_sufficient: {str(sample_sufficient).lower()}",
                "verdict: retest",
                "---",
                "",
                "## Raw Metrics",
                "",
                "```json",
                "{",
                '  "baseline": {',
                f'    "trades": {baseline_closed + 5},',
                f'    "closed_trades": {baseline_closed},',
                '    "win_rate": 15.0,',
                f'    "profit_factor": {baseline_pf},',
                '    "sharpe": -1.0,',
                f'    "max_drawdown_pct": {baseline_mdd},',
                f'    "net_return_pct": {baseline_net},',
                '    "stop_rate": 85.0,',
                '    "avg_r": -0.4,',
                '    "sample_sufficient": true',
                "  },",
                '  "variant": {',
                f'    "trades": {variant_closed + 3},',
                f'    "closed_trades": {variant_closed},',
                '    "win_rate": 20.0,',
                f'    "profit_factor": {variant_pf},',
                '    "sharpe": -0.5,',
                f'    "max_drawdown_pct": {variant_mdd},',
                f'    "net_return_pct": {variant_net},',
                '    "stop_rate": 80.0,',
                '    "avg_r": -0.2,',
                f'    "sample_sufficient": {variant_sample}',
                "  }",
                "}",
                "```",
                "",
            ]
        ),
        encoding="utf-8",
    )


def test_load_abtest_records_parses_matching_reports(tmp_path: Path) -> None:
    _write_report(
        tmp_path,
        "abtest_dynamic_universe_liquidity_50m_2025-01-01_2025-09-01_v1.md",
    )
    _write_report(
        tmp_path,
        "abtest_dynamic_universe_history_365_2025-01-01_2025-09-01_v1.md",
        experiment_id="history_365",
    )

    records = load_abtest_records(tmp_path, "liquidity_50m", "dynamic_universe")

    assert len(records) == 1
    assert records[0].start == "2025-01-01"
    assert records[0].end == "2025-09-01"
    assert records[0].baseline["closed_trades"] == 20
    assert records[0].variant["profit_factor"] == 0.6


def test_build_abtest_summary_marks_candidate_keep_review_for_consistent_improvement(tmp_path: Path) -> None:
    _write_report(tmp_path, "abtest_dynamic_universe_liquidity_50m_2025-01-01_2025-09-01_v1.md")
    _write_report(tmp_path, "abtest_dynamic_universe_liquidity_50m_2025-09-01_2026-01-01_v1.md")
    records = load_abtest_records(tmp_path, "liquidity_50m", "dynamic_universe")

    summary = build_abtest_summary(records, "liquidity_50m", "dynamic_universe")

    assert summary.sufficient_periods == 2
    assert summary.total_period_days == 365
    assert summary.unique_coverage_days == 365
    assert summary.overlap_periods == 0
    assert summary.net_improved_periods == 2
    assert summary.profit_factor_improved_periods == 2
    assert summary.drawdown_improved_periods == 2
    assert summary.verdict == "candidate_keep_review"


def test_build_abtest_summary_keeps_retest_when_variant_sample_is_short(tmp_path: Path) -> None:
    _write_report(tmp_path, "abtest_dynamic_universe_liquidity_50m_2025-01-01_2025-09-01_v1.md")
    _write_report(
        tmp_path,
        "abtest_dynamic_universe_liquidity_50m_2025-09-01_2026-06-01_v1.md",
        sample_sufficient=False,
        variant_closed=19,
    )
    records = load_abtest_records(tmp_path, "liquidity_50m", "dynamic_universe")

    summary = build_abtest_summary(records, "liquidity_50m", "dynamic_universe")

    assert summary.sufficient_periods == 1
    assert summary.variant_under_sample_periods == 1
    assert summary.verdict == "retest"


def test_build_abtest_summary_keeps_retest_when_periods_overlap(tmp_path: Path) -> None:
    _write_report(tmp_path, "abtest_dynamic_universe_liquidity_50m_2025-01-01_2025-09-01_v1.md")
    _write_report(tmp_path, "abtest_dynamic_universe_liquidity_50m_2025-06-01_2026-06-01_v1.md")
    records = load_abtest_records(tmp_path, "liquidity_50m", "dynamic_universe")

    summary = build_abtest_summary(records, "liquidity_50m", "dynamic_universe")

    assert summary.sufficient_periods == 2
    assert summary.total_period_days == 608
    assert summary.unique_coverage_days == 516
    assert summary.overlap_periods == 1
    assert summary.verdict == "retest"
    assert "overlap" in summary.reason


if __name__ == "__main__":
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        test_load_abtest_records_parses_matching_reports(Path(tmp) / "parse")
        test_build_abtest_summary_marks_candidate_keep_review_for_consistent_improvement(Path(tmp) / "keep")
        test_build_abtest_summary_keeps_retest_when_variant_sample_is_short(Path(tmp) / "retest")
        test_build_abtest_summary_keeps_retest_when_periods_overlap(Path(tmp) / "overlap")
    print("test_abtest_summary=passed")
