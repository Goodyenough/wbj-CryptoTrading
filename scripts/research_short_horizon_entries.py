"""Freeze local inputs, then compare entry modules under one short-horizon exit.

python scripts/research_short_horizon_entries.py prepare
python scripts/research_short_horizon_entries.py run

Uses NumPy only in the isolated research harness, not the production package.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import asdict
from datetime import datetime, timezone
import gzip
import hashlib
import json
from pathlib import Path
import sqlite3
import subprocess
import sys
import time
from unittest.mock import patch

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from crypto_trading_system import scanner
from crypto_trading_system.backtest.history import _load_cached_klines
from crypto_trading_system.config import load_settings
from crypto_trading_system.indicators import ema_series
from crypto_trading_system.market_regime import classify_market_regime
from crypto_trading_system.ticker_utils import reconstruct_ticker
from short_horizon_core import (COSTS, DAY, H4, HOUR, Market, account_metrics,
                                bootstrap, new_breakout, replay, trade_metrics, utc)

OUT = ROOT / "reports/2026-10-13/short_horizon_entry_v1"
FROZEN_OUT = OUT
SNAP = ROOT / "data/research_snapshots/short_horizon_entry_v1"
PROTOCOL = OUT.parent / "short_horizon_entry_protocol_v1.md"
WINDOWS = (("2024-07-01", "2025-06-01"), ("2025-06-01", "2026-06-01"))


def ms(value):
    dt = datetime.fromisoformat(value)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return int(dt.timestamp() * 1000)


def digest_bytes(value):
    return hashlib.sha256(value).hexdigest()


def file_hash(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False,
                      default=lambda x: x.item() if isinstance(x, np.generic) else str(x)) + "\n"
    if path.suffix == ".gz":
        with gzip.open(path, "wt", encoding="utf-8") as stream:
            stream.write(text)
    else:
        path.write_text(text, encoding="utf-8")


def source_hashes():
    names = ["scripts/research_short_horizon_entries.py", "scripts/short_horizon_core.py",
             "src/crypto_trading_system/scanner.py", "src/crypto_trading_system/indicators.py",
             "src/crypto_trading_system/market_regime.py", "src/crypto_trading_system/ticker_utils.py",
             "src/crypto_trading_system/config.py", "src/crypto_trading_system/backtest/history.py",
             "config/settings.toml"]
    return {name: file_hash(ROOT / name) for name in names}


def prepare():
    if (OUT / "inputs_manifest.json").exists():
        raise SystemExit("Frozen inputs already exist; preserve them.")
    OUT.mkdir(parents=True, exist_ok=True)
    SNAP.mkdir(parents=True, exist_ok=True)
    settings = load_settings(ROOT / "config/settings.toml")
    manifest = dict(created_utc=datetime.now(timezone.utc).isoformat(),
                    head=subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
                    protocol_sha256=file_hash(PROTOCOL), source_sha256=source_hashes(),
                    numpy_version=np.__version__, database=str(settings.output.database_path), windows=[])
    connection = sqlite3.connect(settings.output.database_path.resolve().as_uri() + "?mode=ro", uri=True)
    connection.execute("BEGIN")
    try:
        for start, end in WINDOWS:
            source = ROOT / f"reports/2026-10-09/atr_fixed_history/{start}_inputs.json"
            frozen = json.loads(source.read_text(encoding="utf-8"))
            symbols = sorted(set(frozen["symbols"]) | {"BTCUSDT", "ETHUSDT"})
            arrays, coverage = {}, []
            for i, symbol in enumerate(symbols):
                for interval, step in (("1h", HOUR), ("4h", H4), ("1d", DAY)):
                    rows = _load_cached_klines(connection, symbol, interval, ms(start) - 240 * DAY, ms(end) + H4)
                    arr = np.asarray(rows, dtype=np.float64).reshape(-1, 12)
                    key = f"{symbol}__{interval}"
                    arrays[key] = arr
                    coverage.append(dict(symbol=symbol, interval=interval, bars=len(arr),
                                         first_open=int(arr[0, 0]) if len(arr) else None,
                                         last_open=int(arr[-1, 0]) if len(arr) else None,
                                         gaps=int(np.sum(np.diff(arr[:, 0]) != step)),
                                         sha256=digest_bytes(arr.tobytes())))
                if i % 40 == 0:
                    print(f"FREEZE {start} {i + 1}/{len(symbols)}", flush=True)
            archive = SNAP / f"{start}.npz"
            if archive.exists():
                raise SystemExit(f"Preserve existing partial archive: {archive}")
            np.savez_compressed(archive, **arrays)
            item = dict(start=start, end=end, old_inputs_file=str(source.relative_to(ROOT)),
                        old_inputs_sha256=file_hash(source), archive=str(archive.relative_to(ROOT)),
                        archive_sha256=file_hash(archive), archive_bytes=archive.stat().st_size,
                        symbols=symbols, frozen_analysis=frozen["frozen_analysis"],
                        selections=frozen["selections"], coverage=coverage)
            save(OUT / f"{start}_inputs.json", item)
            manifest["windows"].append(dict(start=start, end=end, input_sha256=file_hash(OUT / f"{start}_inputs.json")))
            del arrays
        connection.rollback()
    finally:
        connection.close()
    save(OUT / "inputs_manifest.json", manifest)
    print("FROZEN", flush=True)


class Series:
    def __init__(self, rows, step):
        self.rows, self.step = rows, step
        if len(rows):
            bad = (~np.isfinite(rows).all(axis=1) | (rows[:, 3] <= 0) | (rows[:, 5] <= 0)
                   | (rows[:, 7] < 0) | (rows[:, 8] < 0)
                   | (rows[:, 2] < np.maximum(rows[:, 1], rows[:, 4]))
                   | (rows[:, 3] > np.minimum(rows[:, 1], rows[:, 4]))
                   | (rows[:, 2] / np.maximum(rows[:, 3], 1e-300) > 1.4)
                   | (rows[:, 6] != rows[:, 0] + step - 1))
            gaps = np.r_[False, np.diff(rows[:, 0]) != step]
        else:
            bad, gaps = np.zeros(0, dtype=bool), np.zeros(0, dtype=bool)
        self.bad = np.r_[0, np.cumsum(bad)]
        self.gaps = np.r_[0, np.cumsum(gaps)]
        self.ema = {}
        if step in (H4, DAY):
            closes = rows[:, 4].tolist()
            for period in (12, 20, 26, 50):
                self.ema[period] = aligned_ema(closes, period)
            if len(rows) >= 26:
                line = (self.ema[12] - self.ema[26])[25:]
                signal = aligned_ema(line.tolist(), 9)
                self.hist = np.r_[np.full(25, np.nan), line - signal]
            else:
                self.hist = np.full(len(rows), np.nan)

    def index(self, now):
        return int(np.searchsorted(self.rows[:, 0], now - self.step, side="right"))

    def quality(self, n, count, now, *, range_filter=True):
        if n < count:
            return "insufficient_history"
        first = n - count
        if self.rows[n - 1, 0] != (now // self.step) * self.step - self.step:
            return "stale"
        if self.gaps[n] != self.gaps[first + 1]:
            return "history_gap"
        if range_filter and self.bad[n] != self.bad[first]:
            return "invalid_zero_or_extreme"
        return None


def aligned_ema(values, period):
    if len(values) < period:
        return np.full(len(values), np.nan)
    return np.r_[np.full(period - 1, np.nan), ema_series(values, period)]


def analyze_fast(symbol, series, indices, ticker, analysis, regime, *, verify=False):
    s1, s4, sd = (series[k] for k in ("1h", "4h", "1d"))
    n1, n4, nd = (indices[k] for k in ("1h", "4h", "1d"))
    cached = {"ema20_4h": s4.ema[20][n4 - 1], "ema50_4h": s4.ema[50][n4 - 1],
              "ema20_1d": sd.ema[20][nd - 1], "ema50_1d": sd.ema[50][nd - 1]}
    kwargs = {k: analysis[k] for k in (
        "min_history_days", "risk_off_core_buy_enabled", "risk_off_large_cap_buy_enabled",
        "pump_chase_24h_pct", "pump_chase_distance_pct", "pump_chase_penalty",
        "high_volatility_range_pct", "high_volatility_penalty", "daily_trend_required",
        "relative_strength_soft_gate_enabled", "relative_strength_min_pct")}
    kwargs.update(market_regime_allows_buy=regime.allows_alt_buy, market_regime_status=regime.status)
    # Only MACD needs the full recursive past beyond these tails. Pass its exact precomputed
    # value temporarily to the original scanner; all other calculations use exact finite windows.
    with patch.object(scanner, "macd", return_value=(None, None, float(s4.hist[n4 - 1]))):
        candidate = scanner._analyze_ticker(ticker, s1.rows[n1-168:n1].tolist(),
                    s4.rows[n4-120:n4].tolist(), sd.rows[nd-180:nd].tolist(),
                    analysis["risk_reward_min"], precomputed_indicators=cached, **kwargs)
    if verify:
        original = scanner._analyze_ticker(ticker, s1.rows[:n1].tolist(), s4.rows[:n4].tolist(),
                                           sd.rows[:nd].tolist(), analysis["risk_reward_min"], **kwargs)
        assert (candidate is None) == (original is None)
        if candidate is not None:
            for key in ("score", "entry_low", "entry_high", "stop_loss", "take_profit_1", "take_profit_2", "rsi_4h", "atr_4h", "macd_hist_4h"):
                assert np.isclose(getattr(candidate, key), getattr(original, key), rtol=1e-10, atol=1e-10), (symbol, key)
            assert candidate.action == original.action
    return candidate


def features(market, item):
    start, end = ms(item["start"]), ms(item["end"])
    series = {s: {i: Series(arr, {"1h": HOUR, "4h": H4, "1d": DAY}[i])
                  for i, arr in intervals.items()} for s, intervals in market.arrays.items()}
    selections = sorted(item["selections"], key=lambda r: ms(r["decision_time_utc"]))
    selection_index = -1
    counts, frames, regimes = Counter(), {}, {}
    checks = 0
    analysis = item["frozen_analysis"]
    assert not analysis["relative_strength_soft_gate_enabled"]
    assert not analysis["entry_reclaim_min_atr_enabled"]
    for now in range(start + H4, end, H4):
        while selection_index + 1 < len(selections) and ms(selections[selection_index + 1]["decision_time_utc"]) <= now:
            selection_index += 1
        if selection_index < 0:
            counts["no_effective_membership"] += 1
            continue
        day = now // DAY
        if day not in regimes:
            ds = [series[s]["1d"] for s in ("BTCUSDT", "ETHUSDT")]
            ns = [s.index(now) for s in ds]
            if any(s.quality(n, 60, now) for s, n in zip(ds, ns)):
                regimes[day] = None
            else:
                regimes[day] = classify_market_regime(
                    ds[0].rows[:ns[0]].tolist(), ds[1].rows[:ns[1]].tolist(),
                    btc_7d_drop_pct=analysis["regime_btc_7d_drop_pct"],
                    eth_7d_drop_pct=analysis["regime_eth_7d_drop_pct"],
                    require_both_trend=analysis["regime_require_both_trend"])
        regime = regimes[day]
        if regime is None or regime.status in {"RISK_OFF", "UNKNOWN"}:
            counts["regime_block_bars"] += 1
            continue
        frame = {}
        for symbol in selections[selection_index]["selected_symbols"]:
            ss = series[symbol]
            indices = {i: s.index(now) for i, s in ss.items()}
            reason = next((reason for i, count in (("1h", 168), ("4h", 120), ("1d", 180))
                           if (reason := ss[i].quality(indices[i], count, now))), None)
            if reason:
                counts[reason] += 1
                continue
            k1 = ss["1h"].rows[indices["1h"] - 168:indices["1h"]].tolist()
            ticker = reconstruct_ticker(symbol, symbol.removesuffix("USDT"), k1)
            if ticker.quote_volume_24h < 30_000_000 or ticker.trades_24h < 30_000:
                counts["liquidity"] += 1
                continue
            if .97 < ticker.price < 1.03 and ticker.high_low_range_24h < 1:
                counts["stable_like"] += 1
                continue
            candidate = analyze_fast(symbol, ss, indices, ticker, analysis, regime, verify=checks < 50)
            checks += 1
            entry = None
            if candidate is not None and candidate.action == "BUY_CANDIDATE":
                entry = dict(score=float(candidate.score), entry_low=float(candidate.entry_low),
                             entry_high=float(candidate.entry_high), original_stop=float(candidate.stop_loss))
                counts["B_buy_candidate_bars"] += 1
            n4 = indices["4h"]
            breakout = new_breakout(ss["4h"].rows[n4 - 22:n4])
            counts["C_breakout_events"] += int(breakout)
            frame[symbol] = dict(qv=ticker.quote_volume_24h, regime=regime.status,
                                 crash=regime.btc_pct_7d is not None and regime.btc_pct_7d <= -10,
                                 candidate=entry, breakout=breakout)
        frames[now] = frame
        if (now - start) % (30 * DAY) == 0:
            print(f"FEATURES {utc(now)} eligible={sum(len(v) for v in frames.values())}", flush=True)
    counts["fast_scanner_parity_checks"] = min(checks, 50)
    return frames, dict(counts)


def grouped(rows):
    groups = defaultdict(list)
    for r in rows:
        dt = datetime.fromtimestamp(r["entry_ms"] / 1000, timezone.utc)
        duration = r["duration_hours"]
        fields = dict(symbol=r["symbol"], month=dt.strftime("%Y-%m"), week=dt.strftime("%G-W%V"),
                      regime=r["regime"], exit=r["status"], weekend=str(dt.weekday() >= 5),
                      crash=str(r["crash"]), duration="<=8h" if duration <= 8 else "<=24h" if duration <= 24 else "<=48h")
        for kind, label in fields.items():
            groups[kind, label].append(r)
    return [dict(dimension=k, label=v, **trade_metrics(rs), equal_cash_net_usdt=sum(r["net_pnl"] for r in rs if r["closed"]))
            for (k, v), rs in sorted(groups.items())]


def concentration(rows):
    closed = [r for r in rows if r["closed"]]
    result = {}
    for kind in ("symbol", "month"):
        sums = Counter()
        for r in closed:
            key = r["symbol"] if kind == "symbol" else utc(r["entry_ms"])[:7]
            sums[key] += r["net_return_pct"]
        best = [k for k, value in sums.most_common(3) if value > 0]
        kept = [r for r in closed if (r["symbol"] if kind == "symbol" else utc(r["entry_ms"])[:7]) not in best]
        result[kind] = dict(removed=best, remaining=trade_metrics(kept))
    return result


def run():
    if (OUT / "summary.json").exists():
        raise SystemExit("Completed results exist; do not overwrite or select new parameters.")
    manifest = json.loads((FROZEN_OUT / "inputs_manifest.json").read_text(encoding="utf-8"))
    assert manifest["protocol_sha256"] == file_hash(PROTOCOL), "Protocol changed after freeze"
    run_manifest = dict(started_utc=datetime.now(timezone.utc).isoformat(), source_sha256=source_hashes(),
                        protocol_sha256=file_hash(PROTOCOL), input_manifest_sha256=file_hash(FROZEN_OUT / "inputs_manifest.json"),
                        frozen_input_directory=str(FROZEN_OUT.relative_to(ROOT)))
    save(OUT / "run_manifest.json", run_manifest)
    summaries = []
    for wm in manifest["windows"]:
        item_path = FROZEN_OUT / f"{wm['start']}_inputs.json"
        assert file_hash(item_path) == wm["input_sha256"]
        item = json.loads(item_path.read_text(encoding="utf-8"))
        archive = ROOT / item["archive"]
        assert file_hash(archive) == item["archive_sha256"]
        print(f"LOAD {item['start']}", flush=True)
        arrays = defaultdict(dict)
        with np.load(archive, allow_pickle=False) as saved:
            for key in saved.files:
                s, i = key.split("__")
                arrays[s][i] = saved[key]
        market = Market(dict(arrays))
        start, end = ms(item["start"]), ms(item["end"])
        for s in ("BTCUSDT", "ETHUSDT"):
            assert all(market.row(s, "4h", t) is not None for t in range(start, end, H4))
        frames, quality = features(market, item)
        save(OUT / f"{item['start']}_features.json.gz", frames)
        summary = dict(start=item["start"], end=item["end"], quality=quality, branches=[])
        for costs in COSTS:
            for policy in ("stop_first", "target_first"):
                print(f"REPLAY {item['start']} {costs.name} {policy}", flush=True)
                branch = dict(cost=costs.name, policy=policy, layers={})
                for layer in ("all_events", "symbol_only", "portfolio"):
                    results = {arm: replay(market, frames, start, end, arm, layer, costs, policy) for arm in ("B", "C")}
                    details = {arm: dict(metrics=trade_metrics(r["trades"]), counts=r["counts"],
                                        account=account_metrics(r, start, end) if layer == "portfolio" else None)
                               for arm, r in results.items()}
                    details["bootstrap"] = bootstrap(results["B"]["trades"], results["C"]["trades"], start, end)
                    details["c_concentration"] = concentration(results["C"]["trades"])
                    branch["layers"][layer] = details
                    prefix = f"{item['start']}_{costs.name}_{policy}_{layer}"
                    save(OUT / f"{prefix}_trades.json.gz", {a: r["trades"] for a, r in results.items()})
                    if costs.name == "taker" and policy == "stop_first":
                        save(OUT / f"{prefix}_diagnostics.json.gz", {
                            a: dict(groups=grouped(r["trades"]), blocks=r["blocks"], curve=r["curve"])
                            for a, r in results.items()})
                summary["branches"].append(branch)
                save(OUT / f"{item['start']}_summary.json", summary)
        summaries.append(summary)
        print(f"WINDOW COMPLETE {item['start']}", flush=True)
        del market, arrays, frames
    run_manifest["completed_utc"] = datetime.now(timezone.utc).isoformat()
    assert run_manifest["source_sha256"] == source_hashes(), "Source changed during run"
    save(OUT / "run_manifest.json", run_manifest)
    save(OUT / "summary.json", summaries)
    print("COMPLETE", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=("prepare", "run"))
    parser.add_argument("--cash-fix", action="store_true", help="Preserve first run and write audited cash-precision revision")
    args = parser.parse_args()
    if args.cash_fix:
        if args.stage != "run":
            parser.error("--cash-fix reuses existing frozen inputs; use with run")
        OUT = OUT.parent / "short_horizon_entry_v1_cashfix"
    (prepare if args.stage == "prepare" else run)()
