from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from crypto_trading_system.abtest import apply_experiment_overrides, load_experiment
from crypto_trading_system.config import load_settings


def test_load_unknown_experiment_reports_available_names() -> None:
    try:
        load_experiment("does_not_exist", ROOT / "config" / "experiments.toml")
    except ValueError as exc:
        message = str(exc)
        assert "Unknown experiment" in message
        assert "history_250" in message
    else:
        raise AssertionError("Expected unknown experiment to raise ValueError")


def test_disabled_logic_experiment_is_not_runnable() -> None:
    try:
        load_experiment("daily_trend_required", ROOT / "config" / "experiments.toml")
    except ValueError as exc:
        assert "disabled" in str(exc)
        assert "requires logic support" in str(exc)
    else:
        raise AssertionError("Expected disabled experiment to raise ValueError")


def test_apply_overrides_does_not_mutate_baseline() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    definition = load_experiment("history_250", ROOT / "config" / "experiments.toml")
    variant, changes = apply_experiment_overrides(settings, definition)
    assert settings.analysis.min_history_days == 180
    assert variant.analysis.min_history_days == 250
    assert [(change.path, change.old_value, change.new_value) for change in changes] == [
        ("analysis.min_history_days", 180, 250)
    ]


def test_override_paths_are_dimension_scoped() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    definition = load_experiment("history_250", ROOT / "config" / "experiments.toml")
    bad_definition = type(definition)(
        experiment_id="bad",
        description="bad",
        dimension="history",
        enabled=True,
        requires_logic=False,
        overrides={"market": {"min_quote_volume": 1}},
    )
    try:
        apply_experiment_overrides(settings, bad_definition)
    except ValueError as exc:
        assert "not allowed" in str(exc)
    else:
        raise AssertionError("Expected disallowed override path to raise ValueError")


if __name__ == "__main__":
    test_load_unknown_experiment_reports_available_names()
    test_disabled_logic_experiment_is_not_runnable()
    test_apply_overrides_does_not_mutate_baseline()
    test_override_paths_are_dimension_scoped()
    print("test_abtest=passed")
