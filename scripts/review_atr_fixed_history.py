"""Frozen historical ATR diagnostic. Read-only SQLite; no API or production writes.

Run: python scripts/review_atr_fixed_history.py
Protocol: reports/2026-10-09/atr_fixed_history_protocol_v1.md
"""
from __future__ import annotations

from copy import deepcopy
from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sqlite3
import subprocess
import sys
import time
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from crypto_trading_system.config import load_settings
from crypto_trading_system.backtest import replay
from crypto_trading_system.backtest.history import _load_cached_klines, _quality_issues, KlineFetchResult, interval_ms
from crypto_trading_system.backtest.metrics import calculate_metrics
from crypto_trading_system.backtest.universe import DynamicUniverseSelection, SymbolMaster

OUT = ROOT / "reports/2026-10-09/atr_fixed_history"
WINDOWS = [("2024-07-01", "2025-06-01", "e1231e5ad711"),
           ("2025-06-01", "2026-06-01", "110c51eef593")]
TERMINAL = {"CLOSED", "STOPPED", "TIME_EXIT"}


def encode(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, default=str, allow_nan=False)


def digest(value):
    return hashlib.sha256(encode(value).encode()).hexdigest()


def save(name, value):
    (OUT / name).write_text(encode(value) + "\n", encoding="utf-8")


def attribution(baseline, variant):
    """Descriptive paired portfolio accounting, not a capacity counterfactual."""
    def keyed(result):
        values = {(t.symbol, t.created_at_utc): t for t in result.trades if t.entered_at_utc}
        assert len(values) == sum(bool(t.entered_at_utc) for t in result.trades)
        return values
    b, v = keyed(baseline), keyed(variant)
    both = b.keys() & v.keys()
    closed_both = [k for k in both if b[k].status in TERMINAL and v[k].status in TERMINAL]
    only_b = [b[k] for k in b.keys() - v.keys() if b[k].status in TERMINAL]
    only_v = [v[k] for k in v.keys() - b.keys() if v[k].status in TERMINAL]
    contributions = [(k, v[k].net_pnl - b[k].net_pnl) for k in closed_both]
    contributions += [((t.symbol, t.created_at_utc), -t.net_pnl) for t in only_b]
    contributions += [((t.symbol, t.created_at_utc), t.net_pnl) for t in only_v]
    contributions.sort(key=lambda pair: pair[1], reverse=True)
    accounted = sum(x[1] for x in contributions)
    delta = variant.final_equity - baseline.final_equity
    top3 = sum(max(0, x[1]) for x in contributions[:3])
    return dict(common_closed=len(closed_both), baseline_only_closed=len(only_b), variant_only_closed=len(only_v),
                common_closed_delta=sum(v[k].net_pnl - b[k].net_pnl for k in closed_both),
                avoided_losses=-sum(min(0, t.net_pnl) for t in only_b),
                missed_profits=sum(max(0, t.net_pnl) for t in only_b),
                variant_only_pnl=sum(t.net_pnl for t in only_v),
                accounted_closed_delta=accounted, final_equity_delta=delta,
                open_or_mixed_status_residual=delta-accounted,
                largest_3_positive_contributions=contributions[:3],
                delta_less_top3=delta-top3, contributions=contributions,
                capacity_causal_contribution=None)


def audit_trades(result, cache):
    affected = []
    for trade in result.trades:
        if not trade.entered_at_utc:
            continue
        start = replay._date_to_ms(trade.entered_at_utc)
        end = replay._date_to_ms(trade.closed_at_utc or result.end_utc)
        # Include confirming bar and every bar through exit/end.
        times = {int(k[0]) for k in cache[trade.symbol]["4h"]}
        missing = [t for t in range(start-interval_ms("4h"), end, interval_ms("4h")) if t not in times]
        if missing:
            affected.append(dict(symbol=trade.symbol, created_at=trade.created_at_utc, missing_count=len(missing)))
    return affected


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    # Prevent accidental overwrite of a completed experiment.
    if (OUT / "summary.json").exists():
        raise SystemExit("Existing summary.json: preserve completed experiment; inspect it instead.")
    settings = load_settings(ROOT / "config/settings.toml")
    connection = sqlite3.connect(settings.output.database_path.resolve().as_uri() + "?mode=ro", uri=True)
    manifest = {"created_utc": datetime.now(timezone.utc).isoformat(),
                "head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
                "source_sha256": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                                  for p in sorted((ROOT / "src").rglob("*.py"))},
                "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                "protocol_sha256": hashlib.sha256((OUT.parent / "atr_fixed_history_protocol_v1.md").read_bytes()).hexdigest(),
                "windows": []}
    summaries = []
    for start, end, old_id in WINDOWS:
        print(f"LOAD {start} {end}", flush=True)
        old = json.loads(connection.execute("SELECT payload_json FROM backtest_runs WHERE run_id=?", (old_id,)).fetchone()[0])
        frozen = deepcopy(settings)
        for section in ("analysis", "backtest"):
            for key, value in old["config_snapshot"][section].items():
                setattr(getattr(frozen, section), key, value)
        frozen.market.top_n = old["config_snapshot"]["market_top_n"]
        selections = old["dynamic_universe_summary"]["selection_by_day"]
        by_day = {x["date_utc"]: x for x in selections}
        symbols = sorted({s for x in selections for s in x["selected_symbols"]} | {"BTCUSDT", "ETHUSDT"})
        master = SymbolMaster("Frozen 2026-07-26 daily membership (survivorship biased)",
                              old["created_at_utc"], symbols, None, False, "frozen_daily_selection")
        begin = replay._date_to_ms(start) - replay._effective_warmup_ms(frozen)
        finish = replay._date_to_ms(end) + interval_ms("4h")
        cache, issues, coverage = {}, {}, []
        # One SQLite read snapshot per window, released before lengthy computation.
        connection.execute("BEGIN")
        for index, symbol in enumerate(symbols):
            cache[symbol] = {}
            for interval in ("1h", "4h", "1d"):
                rows = _load_cached_klines(connection, symbol, interval, begin, finish)
                cache[symbol][interval] = rows
                issues[symbol, interval] = _quality_issues(symbol, interval, rows)
                malformed = sum(not (float(k[3]) <= min(float(k[1]), float(k[4])) <= max(float(k[1]), float(k[4])) <= float(k[2])) for k in rows)
                if malformed:
                    raise ValueError(f"Malformed OHLC {symbol} {interval}: {malformed}")
                coverage.append(dict(symbol=symbol, interval=interval, bars=len(rows),
                                     first=rows[0][0] if rows else None, last=rows[-1][0] if rows else None,
                                     sha256=digest(rows), errors=sum(x.severity == "ERROR" for x in issues[symbol, interval])))
            if index % 25 == 0:
                print(f"loaded {index+1}/{len(symbols)}", flush=True)
        connection.rollback()
        btc_times = {int(k[0]) for k in cache["BTCUSDT"]["4h"]}
        assert all(t in btc_times for t in range(replay._date_to_ms(start), replay._date_to_ms(end), interval_ms("4h")))
        inputs = dict(start=start, end=end, old_run_id=old_id, frozen_analysis=asdict(frozen.analysis),
                      frozen_backtest=asdict(frozen.backtest), frozen_market=asdict(frozen.market),
                      selections=selections, symbols=symbols, coverage=coverage)
        save(f"{start}_inputs.json", inputs)
        manifest["windows"].append(dict(start=start, end=end, input_sha256=digest(inputs)))
        save("manifest.json", manifest)

        def fetch(_settings, symbol, interval, a, b, **kwargs):
            assert a == begin and b == finish
            return KlineFetchResult(symbol, interval, cache[symbol][interval], issues[symbol, interval], 0)

        def bulk(_settings, requested, intervals, a, b):
            assert a == begin and b == finish and set(requested) == set(symbols)
            return cache

        def select(_settings, _symbols, _cache, ms, **kwargs):
            key = replay.dynamic_universe_refresh_key(ms)
            return DynamicUniverseSelection(**deepcopy(by_day[key]))

        last_progress = [0.0]
        def progress(message):
            if "backtest replay" in message and time.monotonic() - last_progress[0] > 15:
                print(message, flush=True)
                last_progress[0] = time.monotonic()

        with patch.object(replay, "fetch_klines_cached", fetch), patch.object(replay, "batch_load_klines_cached", bulk), patch.object(replay, "select_dynamic_universe_for_day", select):
            for timing in ("legacy_same_bar", "confirmation_close"):
                results, metrics, gaps = {}, {}, {}
                for arm in ("baseline", "atr035"):
                    branch = deepcopy(frozen)
                    branch.analysis.entry_reclaim_min_atr_enabled = arm == "atr035"
                    branch.analysis.entry_reclaim_min_atr = 0.35 if arm == "atr035" else 0.0
                    print(f"RUN {start} {timing} {arm}", flush=True)
                    result = replay.run_backtest_replay(branch, symbols, start, end, dynamic_universe_mode=True,
                                                        dynamic_symbol_master=master, entry_timing=timing, progress=progress)
                    result.limitations.append("Daily universe selection is frozen from old run; no current exchangeInfo request. Current scanner implementation; not a stop-fix-only attribution.")
                    metric = calculate_metrics(result)
                    results[arm], metrics[arm] = result, asdict(metric) if hasattr(metric, "__dataclass_fields__") else metric
                    gaps[arm] = audit_trades(result, cache)
                    save(f"{start}_{timing}_{arm}.json", dict(result=asdict(result), metrics=metrics[arm], gap_affected_trades=gaps[arm]))
                    print(f"DONE {start} {timing} {arm}: {encode(metrics[arm])}", flush=True)
                summary = dict(start=start, end=end, timing=timing, metrics=metrics, gap_affected=gaps,
                               attribution=attribution(results["baseline"], results["atr035"]))
                summaries.append(summary)
                save("progress_summary.json", summaries)
        del cache
    connection.close()
    save("summary.json", summaries)
    print("COMPLETE", flush=True)


if __name__ == "__main__":
    main()
