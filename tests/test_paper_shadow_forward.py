from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from crypto_trading_system.database import connect_db
from crypto_trading_system.paper_shadow_forward import ensure_epoch, forward_summary, run_forward_shadow
from crypto_trading_system.storage import init_db
from crypto_trading_system.config import load_settings


ROOT = Path(__file__).resolve().parents[1]


def _settings(tmp_path: Path):
    settings = load_settings(ROOT / "config" / "settings.toml")
    settings.output.database_path = tmp_path / "forward.db"
    settings.output.reports_dir = tmp_path / "reports"
    settings.output.obsidian_dir = None
    return settings


def _iso(hour: int, minute: int = 10) -> str:
    return f"2026-01-01T{hour:02d}:{minute:02d}:00Z"


def _market(now: str, close: float, quote: float):
    dt = datetime.fromisoformat(now.replace("Z", "+00:00"))
    close_ms = int(dt.timestamp() * 1000) // (4 * 60 * 60 * 1000) * (4 * 60 * 60 * 1000) - 1
    bars = []
    for index in range(20):
        end = close_ms - (19 - index) * 4 * 60 * 60 * 1000
        bars.append([end - 4 * 60 * 60 * 1000 + 1, "100", "130", "90", str(close), "10", end])
    return {"TESTUSDT": {"price": quote, "quote_time_ms": int(dt.timestamp() * 1000), "bars": bars}}


def _candidate(path: Path, scan_time: str):
    with connect_db(path) as connection:
        connection.execute(
            """
            INSERT INTO paper_shadow_candidate_observations(
                observation_id, account_name, scan_id, scan_time, symbol, source_rank,
                scanner_action, data_quality_state, entry_low, entry_high, stop_loss,
                tp1, tp2, sample_level, created_at, updated_at
            ) VALUES ('obs1','demo','scan1',?,'TESTUSDT',1,'BUY_CANDIDATE','CLEAN',100,110,90,120,140,'candidate_level',?,?)
            """,
            (scan_time, scan_time, scan_time),
        )


def test_baseline_and_atr_have_independent_lifecycles(tmp_path: Path) -> None:
    settings = _settings(tmp_path)
    init_db(settings.output.database_path)
    first = _iso(4)
    ensure_epoch(settings, now=first)
    _candidate(settings.output.database_path, first)

    # The baseline close reclaim is true; 0.35 ATR is still pending.
    result = run_forward_shadow(settings, run_id="run1", now=first,
                                market=_market(first, close=110, quote=106))
    assert result["status"] == "OK"
    result = run_forward_shadow(settings, run_id="run2", now=_iso(8),
                                market=_market(_iso(8), close=100, quote=140))
    assert result["status"] == "OK"
    # The baseline has stopped; the ATR line is still watching and may enter.
    result = run_forward_shadow(settings, run_id="run3", now=_iso(12),
                                market=_market(_iso(12), close=130, quote=106))
    assert result["status"] == "OK"
    result = run_forward_shadow(settings, run_id="run4", now=_iso(16),
                                market=_market(_iso(16), close=130, quote=140))
    assert result["status"] == "OK"

    summary = forward_summary(settings)
    lines = summary["epochs"][0]["lines"]
    assert lines["reference_baseline"]["closed_trades"] == 1
    assert lines["atr_reclaim_0_35_shadow"]["entered"] == 1
    assert lines["atr_reclaim_0_35_shadow"]["closed_trades"] == 1
    # Both paths reach terminal state, but only after the ATR line enters later;
    # this is precisely the paired lifecycle the old plan-level logger omitted.
    assert summary["epochs"][0]["paired_closed_trades"] == 1


def test_duplicate_run_is_idempotent_and_gap_censors_epoch(tmp_path: Path) -> None:
    settings = _settings(tmp_path)
    init_db(settings.output.database_path)
    first = _iso(4)
    ensure_epoch(settings, now=first)
    _candidate(settings.output.database_path, first)
    market = _market(first, close=110, quote=106)
    first_result = run_forward_shadow(settings, run_id="same", now=first, market=market)
    duplicate = run_forward_shadow(settings, run_id="same", now=first, market=market)
    assert duplicate["status"] == first_result["status"]
    with connect_db(settings.output.database_path) as connection:
        assert connection.execute("SELECT count(*) FROM paper_forward_ticks").fetchone()[0] == 1

    gap = run_forward_shadow(settings, run_id="missed", now=_iso(16), market=market)
    assert gap["status"] == "GAP_AFFECTED"
    summary = forward_summary(settings)
    assert summary["epochs"][0]["status"] == "GAP_AFFECTED"
    assert summary["epochs"][0]["lines"]["reference_baseline"]["censored"] >= 0
