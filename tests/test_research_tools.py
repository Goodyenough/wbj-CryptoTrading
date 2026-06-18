from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from crypto_trading_system.research_tools import build_experiment_index


def _settings(tmp_path: Path):
    reports_dir = tmp_path / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    return SimpleNamespace(output=SimpleNamespace(reports_dir=reports_dir, obsidian_dir=None))


def _write_abtest(path: Path, *, experiment_id: str = "single_exp", verdict: str = "retest") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join(
            [
                "---",
                "created: 2026-06-10 01:00:00 CST",
                "tags:",
                "  - crypto",
                "  - trading-system",
                "  - abtest",
                f"experiment_id: {experiment_id}",
                "changed_param: analysis.foo",
                "old_value: 1",
                "new_value: 2",
                "sample_sufficient: true",
                f"verdict: {verdict}",
                "report_version: v1",
                "---",
                "",
                f"# A/B 实验报告 {experiment_id}",
                "",
                "- reason: single period reason",
            ]
        ),
        encoding="utf-8",
    )


def _write_summary(
    path: Path,
    *,
    experiment_id: str = "summary_exp",
    version: int = 1,
    verdict: str = "candidate_keep_review",
    reason: str = "summary raw reason",
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    source = path.parent / f"abtest_dynamic_universe_{experiment_id}_2025-01-01_2025-06-01_v1.md"
    source_value = source.as_posix()
    _write_abtest(source, experiment_id=experiment_id)
    path.write_text(
        "\n".join(
            [
                "---",
                f"created: 2026-06-1{version} 01:00:00 CST",
                "tags:",
                "  - crypto",
                "  - trading-system",
                "  - abtest-summary",
                f"experiment_id: {experiment_id}",
                "mode: dynamic_universe",
                "periods: 2",
                "sufficient_periods: 2",
                f"verdict: {verdict}",
                f"report_version: v{version}",
                "---",
                "",
                f"# A/B 多时段汇总 {experiment_id}",
                "",
                "## Raw Summary",
                "",
                "```json",
                "{",
                f'  "experiment_id": "{experiment_id}",',
                '  "periods": 2,',
                '  "sufficient_periods": 2,',
                '  "variant_under_sample_periods": 0,',
                f'  "verdict": "{verdict}",',
                f'  "reason": "{reason}",',
                '  "records": [',
                "    {",
                f'      "path": "{source_value}",',
                '      "start": "2025-01-01",',
                '      "end": "2025-06-01",',
                '      "sample_sufficient": true',
                "    },",
                "    {",
                f'      "path": "{source_value}",',
                '      "start": "2025-06-01",',
                '      "end": "2026-06-01",',
                '      "sample_sufficient": true',
                "    }",
                "  ]",
                "}",
                "```",
            ]
        ),
        encoding="utf-8",
    )


def _write_review(path: Path, *, experiment_id: str = "summary_exp") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join(
            [
                "---",
                "created: 2026-06-16T00:10:00+08:00",
                "tags:",
                "  - crypto",
                "  - trading-system",
                "  - exit-review",
                f"experiment_id: {experiment_id}",
                "verdict: reject_candidate",
                "reason: review overrides summary",
                "next_action: do not deploy",
                "changed_param: analysis.foo",
                "old_value: 1",
                "new_value: 2",
                "start: 2025-01-01",
                "end: 2026-06-01",
                "periods: 2",
                "sufficient_periods: 2",
                "report_version: v1",
                "---",
                "",
                "# Review",
            ]
        ),
        encoding="utf-8",
    )


def test_single_abtest_generates_index_entry(tmp_path: Path) -> None:
    settings = _settings(tmp_path)
    _write_abtest(settings.output.reports_dir / "2026-06-10" / "abtest_dynamic_universe_single_exp_2025-01-01_2025-06-01_v1.md")

    text, _ = build_experiment_index(settings)

    assert "`single_exp`" in text
    assert "2025-01-01 -> 2025-06-01" in text
    assert "`analysis.foo`: `1` -> `2`" in text


def test_summary_aggregates_periods_and_raw_reason(tmp_path: Path) -> None:
    settings = _settings(tmp_path)
    _write_summary(settings.output.reports_dir / "2026-06-11" / "abtest_summary_dynamic_universe_summary_exp_2026-06-11_v1.md")

    text, _ = build_experiment_index(settings)

    assert "`summary_exp`" in text
    assert "2025-01-01 -> 2026-06-01" in text
    assert "summary raw reason" in text
    assert "| `summary_exp` | candidate_keep_review |" in text


def test_latest_summary_version_wins(tmp_path: Path) -> None:
    settings = _settings(tmp_path)
    _write_summary(
        settings.output.reports_dir / "2026-06-11" / "abtest_summary_dynamic_universe_summary_exp_2026-06-11_v1.md",
        version=1,
        reason="old reason",
    )
    _write_summary(
        settings.output.reports_dir / "2026-06-11" / "abtest_summary_dynamic_universe_summary_exp_2026-06-11_v2.md",
        version=2,
        reason="new reason",
    )

    text, _ = build_experiment_index(settings)

    assert "new reason" in text
    assert "old reason" not in text


def test_review_frontmatter_overrides_summary_verdict(tmp_path: Path) -> None:
    settings = _settings(tmp_path)
    _write_summary(settings.output.reports_dir / "2026-06-11" / "abtest_summary_dynamic_universe_summary_exp_2026-06-11_v1.md")
    _write_review(settings.output.reports_dir / "2026-06-16" / "summary_exp_review_2026-06-16_v1.md")

    text, _ = build_experiment_index(settings)

    assert "| `summary_exp` | reject_candidate | review overrides summary | do not deploy |" in text
    assert "| `summary_exp` | review | 2025-01-01 -> 2026-06-01 |" in text


def test_attention_excludes_retest(tmp_path: Path) -> None:
    settings = _settings(tmp_path)
    _write_abtest(
        settings.output.reports_dir / "2026-06-10" / "abtest_dynamic_universe_retest_exp_2025-01-01_2025-06-01_v1.md",
        experiment_id="retest_exp",
        verdict="retest",
    )
    _write_summary(
        settings.output.reports_dir / "2026-06-11" / "abtest_summary_dynamic_universe_keep_exp_2026-06-11_v1.md",
        experiment_id="keep_exp",
    )

    text, _ = build_experiment_index(settings)
    attention = text.split("## 完整索引", 1)[0]

    assert "`keep_exp`" in attention
    assert "`retest_exp`" not in attention
    assert "`retest_exp`" in text


if __name__ == "__main__":
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        test_single_abtest_generates_index_entry(root / "single")
        test_summary_aggregates_periods_and_raw_reason(root / "summary")
        test_latest_summary_version_wins(root / "version")
        test_review_frontmatter_overrides_summary_verdict(root / "review")
        test_attention_excludes_retest(root / "attention")
