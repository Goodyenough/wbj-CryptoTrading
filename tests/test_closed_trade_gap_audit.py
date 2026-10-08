"""Guard against inventing missing slots or using final stops at entry."""
import importlib.util
from pathlib import Path
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/audit_closed_trade_gaps.py"
spec = importlib.util.spec_from_file_location("gap_audit", SCRIPT)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class GapAuditTests(unittest.TestCase):
    def test_resumption_minute_is_not_a_missing_update(self):
        slots = list(audit.missed_slots("2026-09-10T04:10:03Z", "2026-09-10T16:10:04Z"))
        self.assertEqual([t.isoformat() for t in slots], ["2026-09-10T08:10:00+00:00"])

    def test_daily_time_is_not_treated_as_four_hour_trigger(self):
        slots = list(audit.missed_slots("2026-09-10T08:10:03Z", "2026-09-10T20:10:04Z"))
        self.assertEqual([t.hour for t in slots], [16])

    def test_timezone_and_midnight(self):
        slots = list(audit.missed_slots("2026-09-10T20:10:03Z", "2026-09-11T04:10:04Z"))
        self.assertEqual([t.isoformat() for t in slots], ["2026-09-11T00:10:00+00:00"])


if __name__ == "__main__":
    unittest.main()
