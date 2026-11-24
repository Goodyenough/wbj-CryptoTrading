import copy
import unittest

from research.short_trend.run import (canonical_digest, EXPECTED_PROTOCOL_SHA256,
                                     locked_protocol, validate_event_bounds)


class FrozenRunnerTests(unittest.TestCase):
    def test_frozen_semantic_protocol_hash_is_exact(self):
        config = locked_protocol()
        self.assertEqual(canonical_digest(config), EXPECTED_PROTOCOL_SHA256)
        config["risk"]["target_fraction"] = 0.02
        self.assertNotEqual(canonical_digest(config), EXPECTED_PROTOCOL_SHA256)

    def test_complete_horizon_cannot_cross_segment(self):
        event = {"decision_ms": 10, "entry_ms": 20, "deadline_ms": 100,
                 "signal": {"exit_ms": 90}, "mirror": {"exit_ms": 100}}
        validate_event_bounds(event, 0, 110)
        with self.assertRaises(AssertionError):
            validate_event_bounds(event, 0, 100)

    def test_funding_cannot_be_attributed_before_entry_or_after_exit(self):
        event = {"decision_ms": 10, "entry_ms": 20, "deadline_ms": 100,
                 "signal": {"exit_ms": 90, "funding_events": [{"time_ms": 20}]},
                 "mirror": {"exit_ms": 100}}
        with self.assertRaises(AssertionError):
            validate_event_bounds(event, 0, 110)
        event["signal"]["funding_events"][0]["time_ms"] = 91
        with self.assertRaises(AssertionError):
            validate_event_bounds(event, 0, 110)


if __name__ == "__main__":
    unittest.main()
