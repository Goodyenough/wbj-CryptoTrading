"""Synthetic measurement and verdict checks for CRYPTOTRADIN-134."""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from research_atr_exit_component_attribution import (  # noqa: E402
    POLICIES,
    attach_common_r,
    decide,
    factorial_effects,
    measurement_checks,
    transition_summary,
)


def row(policy: str, *, net: float, gross: float, cost: float, risk: float, status: str = "TP") -> dict:
    return {
        "symbol": "XUSDT",
        "signal_ms": 1,
        "entry_ms": 2,
        "exit_ms": 3,
        "closed": True,
        "status": status,
        "raw_return_pct": gross,
        "net_return_pct": net,
        "fee_pct": cost,
        "slippage_pct": 0.0,
        "planned_risk_pct": risk,
        "net_r": net / risk,
        "cost_r": cost / risk,
        "model": policy,
    }


def four_rows() -> dict[str, list[dict]]:
    return {
        "fixed_fixed": [row("fixed_fixed", net=4.8, gross=5.0, cost=0.2, risk=3.2)],
        "atr_tp_fixed_sl": [row("atr_tp_fixed_sl", net=5.8, gross=6.0, cost=0.2, risk=3.2)],
        "fixed_tp_atr_sl": [row("fixed_tp_atr_sl", net=4.8, gross=5.0, cost=0.2, risk=2.2)],
        "atr_atr": [row("atr_atr", net=6.8, gross=7.0, cost=0.2, risk=2.2)],
    }


def test_common_r_uses_actual_fixed_risk_and_identities_close() -> None:
    rows = four_rows()
    attach_common_r(rows)
    assert rows["atr_atr"][0]["common_planned_risk_pct"] == 3.2
    assert np.isclose(rows["atr_atr"][0]["net_common_r"], 6.8 / 3.2)
    assert measurement_checks(rows)["passed"]


def test_factorial_effects_and_transition_contributions_close() -> None:
    rows = four_rows()
    attach_common_r(rows)
    effects = factorial_effects(rows)
    assert np.isclose(effects["net_pct"]["tp_marginal"], 1.5)
    assert np.isclose(effects["net_pct"]["sl_marginal"], 0.5)
    assert np.isclose(effects["net_pct"]["interaction"], 1.0)
    transitions = transition_summary(rows["fixed_fixed"], rows["atr_atr"])
    assert abs(transitions["closure_error_common_r"]) < 1e-12
    assert abs(transitions["closure_error_net_pct"]) < 1e-12


def test_measurement_gate_rejects_policy_dependent_censoring() -> None:
    rows = four_rows()
    rows["atr_atr"][0]["closed"] = False
    attach_common_r(rows)
    result = measurement_checks(rows)
    assert not result["passed"]
    assert any("policy_dependent_censoring" in error for error in result["errors"])


def synthetic_summary(*, qualified: bool, measurement: bool = True, order: bool = True) -> dict:
    qualification = {
        "atr_tp_fixed_sl": {"qualified": qualified},
        "fixed_tp_atr_sl": {"qualified": False},
    }
    branch = {"measurement": {"passed": measurement}}
    return {
        "windows": {
            "early": {"branches": {"x": branch}},
            "near": {"branches": {"x": branch}},
        },
        "order_flip_check": {"passed": order},
        "qualification": qualification,
    }


def test_verdicts_follow_preregistered_measurement_first_order() -> None:
    assert decide(synthetic_summary(qualified=True))[0] == "component_validation_eligible"
    assert decide(synthetic_summary(qualified=False))[0] == "reject_current_atr_components"
    assert decide(synthetic_summary(qualified=True, measurement=False))[0] == "measurement_insufficient"
    assert decide(synthetic_summary(qualified=True, order=False))[0] == "measurement_insufficient"
