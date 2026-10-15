import numpy as np

from scripts.research_realtime_momentum_start import (
    H4,
    HOUR,
    Market,
    generate_rt1_candidates,
    reclaim_after_hour,
    symbol_only,
)


def bar(opened, opening, high, low, close):
    return np.asarray([opened, opening, high, low, close, 1.0, opened + 3_599_999, 1.0, 1.0])


def test_reclaim_uses_only_completed_hour_and_cumulative_touch():
    plan = {"entry_low": 99.0, "entry_high": 101.0}
    first = bar(0, 98.0, 100.0, 97.0, 98.5)
    triggered, high, low = reclaim_after_hour(plan, first, -np.inf, np.inf)
    assert not triggered
    second = bar(3_600_000, 98.5, 102.0, 98.0, 101.5)
    triggered, high, low = reclaim_after_hour(plan, second, high, low)
    assert triggered
    assert high == 102.0
    assert low == 97.0


def test_reclaim_requires_close_above_entry_high():
    plan = {"entry_low": 99.0, "entry_high": 101.0}
    row = bar(0, 100.0, 103.0, 98.0, 100.5)
    triggered, _high, _low = reclaim_after_hour(plan, row, -np.inf, np.inf)
    assert not triggered


def test_symbol_only_blocks_overlapping_same_symbol_but_not_other_symbol():
    rows = [
        {"symbol": "AAA", "entry_ms": 10, "exit_ms": 30, "closed": True, "plan_created_ms": 0},
        {"symbol": "AAA", "entry_ms": 20, "exit_ms": 40, "closed": True, "plan_created_ms": 1},
        {"symbol": "BBB", "entry_ms": 20, "exit_ms": 25, "closed": True, "plan_created_ms": 1},
        {"symbol": "AAA", "entry_ms": 30, "exit_ms": 50, "closed": True, "plan_created_ms": 2},
    ]
    accepted, blocked = symbol_only(rows)
    assert blocked == 1
    assert [(row["symbol"], row["entry_ms"]) for row in accepted] == [
        ("AAA", 10),
        ("BBB", 20),
        ("AAA", 30),
    ]


def feature():
    return {
        "candidate": {"entry_low": 99.0, "entry_high": 101.0, "original_stop": 95.0},
        "qv": 10.0,
        "regime": "NEUTRAL",
        "crash": False,
    }


def market_with_interval(hour_closes):
    hours = []
    for index, close in enumerate(hour_closes):
        opened = H4 + index * HOUR
        hours.append(bar(opened, 100.0, max(102.0, close), 98.0, close))
    # Include the next-hour open when an offset-3 signal enters.
    hours.append(bar(H4 + 4 * HOUR, 100.0, 102.0, 98.0, 100.0))
    four_hours = np.asarray([
        bar(0, 100.0, 100.0, 99.0, 100.0),
        bar(H4, 100.0, max(row[2] for row in hours[:4]), min(row[3] for row in hours[:4]), hour_closes[-1]),
    ])
    return Market({"AAA": {"1h": np.asarray(hours), "4h": four_hours}})


def test_generator_emits_first_three_hour_signal_without_future_eligibility():
    market = market_with_interval([101.5, 100.0, 100.0, 100.0])
    frames = {H4: {"AAA": feature()}, 2 * H4: {}}
    events, counts = generate_rt1_candidates(frames, market, 0, 3 * H4)
    assert len(events) == 1
    assert events[0]["signal_ms"] == H4 + HOUR
    assert events[0]["knowledge_cutoff_ms"] == events[0]["signal_ms"]
    assert counts["causal_violations"] == 0


def test_generator_excludes_fourth_hour_reclaim():
    market = market_with_interval([100.0, 100.0, 100.0, 101.5])
    frames = {H4: {"AAA": feature()}, 2 * H4: {"AAA": feature()}}
    events, _counts = generate_rt1_candidates(frames, market, 0, 2 * H4)
    assert events == []
