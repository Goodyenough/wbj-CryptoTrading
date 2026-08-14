from __future__ import annotations

from dataclasses import asdict
import json
from pathlib import Path
import sqlite3

from .database import connect_db, init_observation_db, utc_now
from .models import ScanResult


def _market_regime_from_limitations(limitations: list[str]) -> str | None:
    text = " ".join(str(item) for item in limitations).upper()
    for status in ("RISK_OFF", "RISK_ON", "NEUTRAL", "UNKNOWN"):
        if status in text:
            return status
    return None


def init_db(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with connect_db(path) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS scan_runs (
                scan_id TEXT PRIMARY KEY,
                timestamp_utc TEXT NOT NULL,
                source TEXT NOT NULL,
                filters TEXT NOT NULL,
                limitations_json TEXT NOT NULL
            )
            """
        )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS scan_candidates (
                scan_id TEXT NOT NULL,
                rank INTEGER NOT NULL,
                symbol TEXT NOT NULL,
                base_asset TEXT NOT NULL,
                verdict TEXT NOT NULL,
                score REAL NOT NULL,
                payload_json TEXT NOT NULL,
                PRIMARY KEY (scan_id, rank),
                FOREIGN KEY (scan_id) REFERENCES scan_runs(scan_id)
            )
            """
        )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS paper_trades (
                paper_trade_id TEXT PRIMARY KEY,
                account_name TEXT NOT NULL,
                source_scan_id TEXT NOT NULL,
                source_rank INTEGER NOT NULL,
                symbol TEXT NOT NULL,
                base_asset TEXT NOT NULL,
                status TEXT NOT NULL,
                created_at_utc TEXT NOT NULL,
                updated_at_utc TEXT NOT NULL,
                setup TEXT NOT NULL,
                verdict TEXT NOT NULL,
                entry_low REAL NOT NULL,
                entry_high REAL NOT NULL,
                planned_entry_mid REAL NOT NULL,
                stop_loss REAL NOT NULL,
                take_profit_1 REAL NOT NULL,
                take_profit_2 REAL NOT NULL,
                risk_reward_1 REAL NOT NULL,
                risk_reward_2 REAL NOT NULL,
                account_equity REAL NOT NULL,
                risk_per_trade_pct REAL NOT NULL,
                cash_risk REAL NOT NULL,
                quantity REAL,
                entry_price REAL,
                entered_at_utc TEXT,
                tp1_hit_at_utc TEXT,
                closed_at_utc TEXT,
                exit_price REAL,
                realized_pnl REAL NOT NULL DEFAULT 0,
                unrealized_pnl REAL NOT NULL DEFAULT 0,
                last_price REAL,
                notes TEXT NOT NULL DEFAULT '',
                tp1_trailing_ema_stop_active INTEGER NOT NULL DEFAULT 0,
                payload_json TEXT NOT NULL,
                UNIQUE (account_name, source_scan_id, source_rank)
            )
            """
        )
        columns = {
            str(row[1])
            for row in connection.execute("PRAGMA table_info(paper_trades)").fetchall()
        }
        if "tp1_trailing_ema_stop_active" not in columns:
            connection.execute(
                "ALTER TABLE paper_trades "
                "ADD COLUMN tp1_trailing_ema_stop_active INTEGER NOT NULL DEFAULT 0"
            )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS paper_trade_events (
                event_id TEXT PRIMARY KEY,
                paper_trade_id TEXT NOT NULL,
                account_name TEXT NOT NULL,
                symbol TEXT NOT NULL,
                event_type TEXT NOT NULL,
                event_time_utc TEXT NOT NULL,
                price REAL,
                quantity REAL,
                realized_pnl REAL NOT NULL DEFAULT 0,
                unrealized_pnl REAL NOT NULL DEFAULT 0,
                message TEXT NOT NULL,
                FOREIGN KEY (paper_trade_id) REFERENCES paper_trades(paper_trade_id)
            )
            """
        )
        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_paper_trade_events_trade_time "
            "ON paper_trade_events (paper_trade_id, event_time_utc)"
        )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS data_cross_checks (
                scan_id TEXT NOT NULL,
                symbol TEXT NOT NULL,
                provider TEXT NOT NULL,
                status TEXT NOT NULL,
                provider_asset_id TEXT,
                provider_symbol TEXT,
                price_usd REAL,
                pct_24h REAL,
                volume_24h REAL,
                last_updated TEXT,
                fetched_at_utc TEXT NOT NULL,
                price_diff_pct REAL,
                pct_24h_diff REAL,
                volume_note TEXT NOT NULL,
                message TEXT NOT NULL,
                PRIMARY KEY (scan_id, symbol, provider),
                FOREIGN KEY (scan_id) REFERENCES scan_runs(scan_id)
            )
            """
        )
        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_data_cross_checks_scan_symbol "
            "ON data_cross_checks (scan_id, symbol)"
        )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS data_quality_issues (
                issue_id INTEGER PRIMARY KEY AUTOINCREMENT,
                scan_id TEXT NOT NULL,
                symbol TEXT NOT NULL,
                provider TEXT NOT NULL,
                issue_code TEXT NOT NULL,
                severity TEXT NOT NULL,
                blocking INTEGER NOT NULL,
                message TEXT NOT NULL,
                context_json TEXT NOT NULL,
                FOREIGN KEY (scan_id) REFERENCES scan_runs(scan_id)
            )
            """
        )
        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_data_quality_issues_scan_symbol "
            "ON data_quality_issues (scan_id, symbol)"
        )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS kline_cache (
                source TEXT NOT NULL,
                symbol TEXT NOT NULL,
                interval TEXT NOT NULL,
                open_time INTEGER NOT NULL,
                open REAL NOT NULL,
                high REAL NOT NULL,
                low REAL NOT NULL,
                close REAL NOT NULL,
                volume REAL NOT NULL,
                close_time INTEGER NOT NULL,
                quote_volume REAL NOT NULL,
                trades INTEGER NOT NULL,
                taker_buy_base_volume REAL NOT NULL,
                taker_buy_quote_volume REAL NOT NULL,
                is_closed INTEGER NOT NULL,
                fetched_at_utc TEXT NOT NULL,
                PRIMARY KEY (source, symbol, interval, open_time)
            )
            """
        )
        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_kline_cache_symbol_interval_time "
            "ON kline_cache (symbol, interval, open_time)"
        )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS kline_unavailable_ranges (
                source TEXT NOT NULL,
                symbol TEXT NOT NULL,
                interval TEXT NOT NULL,
                start_time INTEGER NOT NULL,
                end_time INTEGER NOT NULL,
                reason TEXT NOT NULL,
                fetched_at_utc TEXT NOT NULL,
                PRIMARY KEY (source, symbol, interval, start_time, end_time)
            )
            """
        )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS kline_fetch_ranges (
                source TEXT NOT NULL,
                symbol TEXT NOT NULL,
                interval TEXT NOT NULL,
                start_time INTEGER NOT NULL,
                end_time INTEGER NOT NULL,
                fetched_at_utc TEXT NOT NULL,
                PRIMARY KEY (source, symbol, interval, start_time, end_time)
            )
            """
        )
        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_kline_fetch_ranges_lookup "
            "ON kline_fetch_ranges (source, symbol, interval, start_time, end_time)"
        )
        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_kline_unavailable_lookup "
            "ON kline_unavailable_ranges (source, symbol, interval, start_time, end_time)"
        )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS backtest_runs (
                run_id TEXT PRIMARY KEY,
                created_at_utc TEXT NOT NULL,
                symbols_json TEXT NOT NULL,
                start_utc TEXT NOT NULL,
                end_utc TEXT NOT NULL,
                config_json TEXT NOT NULL,
                commit_hash TEXT NOT NULL,
                metrics_json TEXT NOT NULL,
                report_path TEXT,
                payload_json TEXT NOT NULL
            )
            """
        )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS backtest_trades (
                run_id TEXT NOT NULL,
                trade_id TEXT NOT NULL,
                symbol TEXT NOT NULL,
                status TEXT NOT NULL,
                created_at_utc TEXT NOT NULL,
                entered_at_utc TEXT,
                closed_at_utc TEXT,
                entry_price_raw REAL,
                entry_price_filled REAL,
                exit_price_raw REAL,
                exit_price_filled REAL,
                entry_fee REAL NOT NULL DEFAULT 0,
                exit_fee REAL NOT NULL DEFAULT 0,
                slippage_cost REAL NOT NULL DEFAULT 0,
                gross_pnl REAL NOT NULL DEFAULT 0,
                net_pnl REAL NOT NULL DEFAULT 0,
                r_multiple_net REAL,
                payload_json TEXT NOT NULL,
                PRIMARY KEY (run_id, trade_id),
                FOREIGN KEY (run_id) REFERENCES backtest_runs(run_id)
            )
            """
        )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS backtest_metrics (
                run_id TEXT NOT NULL,
                metric_name TEXT NOT NULL,
                metric_value REAL,
                metric_text TEXT,
                PRIMARY KEY (run_id, metric_name),
                FOREIGN KEY (run_id) REFERENCES backtest_runs(run_id)
            )
            """
        )
    init_observation_db(path)


def save_scan_result(path: Path, result: ScanResult, run_id: str | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with connect_db(path) as connection:
        connection.execute(
            """
            INSERT OR REPLACE INTO scan_runs
            (scan_id, timestamp_utc, source, filters, limitations_json)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                result.scan_id,
                result.timestamp_utc,
                result.source,
                result.filters,
                json.dumps(result.limitations, ensure_ascii=False),
            ),
        )
        connection.execute("DELETE FROM scan_candidates WHERE scan_id = ?", (result.scan_id,))
        connection.execute("DELETE FROM data_cross_checks WHERE scan_id = ?", (result.scan_id,))
        connection.execute("DELETE FROM data_quality_issues WHERE scan_id = ?", (result.scan_id,))
        for candidate in result.candidates:
            connection.execute(
                """
                INSERT INTO scan_candidates
                (scan_id, rank, symbol, base_asset, verdict, score, payload_json)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    result.scan_id,
                    candidate.rank,
                    candidate.symbol,
                    candidate.base_asset,
                    candidate.verdict,
                    candidate.score,
                    json.dumps(asdict(candidate), ensure_ascii=False),
                ),
            )
            for check in candidate.data_checks:
                connection.execute(
                    """
                    INSERT INTO data_cross_checks (
                        scan_id, symbol, provider, status, provider_asset_id, provider_symbol,
                        price_usd, pct_24h, volume_24h, last_updated, fetched_at_utc,
                        price_diff_pct, pct_24h_diff, volume_note, message
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        result.scan_id,
                        candidate.symbol,
                        check.provider,
                        check.status,
                        check.provider_asset_id,
                        check.provider_symbol,
                        check.price_usd,
                        check.pct_24h,
                        check.volume_24h,
                        check.last_updated,
                        check.fetched_at_utc,
                        check.price_diff_pct,
                        check.pct_24h_diff,
                        check.volume_note,
                        check.message,
                    ),
                )
                for issue in check.issues:
                    connection.execute(
                        """
                        INSERT INTO data_quality_issues (
                            scan_id, symbol, provider, issue_code, severity,
                            blocking, message, context_json
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            result.scan_id,
                            candidate.symbol,
                            issue.provider,
                            issue.code,
                            issue.severity,
                            1 if issue.blocking else 0,
                            issue.message,
                            json.dumps(issue.context, ensure_ascii=False, sort_keys=True),
                        ),
                    )
        if run_id is not None:
            actions = [str(candidate.action) for candidate in result.candidates]
            market_regime = _market_regime_from_limitations(result.limitations)
            run_row = connection.execute(
                "SELECT config_hash FROM runs WHERE run_id = ?",
                (run_id,),
            ).fetchone()
            config_hash = None if run_row is None else run_row["config_hash"]
            risk_off_count = sum(
                1
                for candidate in result.candidates
                if "大盘环境未确认强势" in " ".join(candidate.risks)
            )
            connection.execute(
                """
                INSERT INTO market_scans(
                    scan_id, run_id, scan_time, market_regime, candidate_count, buy_candidate_count,
                    watch_only_count, risk_off_count, config_hash, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(scan_id) DO UPDATE SET
                    run_id=excluded.run_id,
                    scan_time=excluded.scan_time,
                    market_regime=excluded.market_regime,
                    candidate_count=excluded.candidate_count,
                    buy_candidate_count=excluded.buy_candidate_count,
                    watch_only_count=excluded.watch_only_count,
                    risk_off_count=excluded.risk_off_count,
                    config_hash=excluded.config_hash
                """,
                (
                    result.scan_id,
                    run_id,
                    result.timestamp_utc,
                    market_regime,
                    len(result.candidates),
                    actions.count("BUY_CANDIDATE"),
                    actions.count("WATCH_ONLY"),
                    risk_off_count,
                    config_hash,
                    utc_now(),
                ),
            )
            for candidate in result.candidates:
                payload = asdict(candidate)
                connection.execute(
                    """
                    UPDATE scan_candidates SET
                        action=?, price=?, volume=?, entry_low=?, entry_high=?, stop=?,
                        tp1=?, tp2=?, market_regime=?, reason=?, raw_json=?, created_at=?
                    WHERE scan_id=? AND symbol=?
                    """,
                    (
                        candidate.action,
                        candidate.price,
                        candidate.quote_volume_24h,
                        candidate.entry_low,
                        candidate.entry_high,
                        candidate.stop_loss,
                        candidate.take_profit_1,
                        candidate.take_profit_2,
                        market_regime,
                        candidate.setup,
                        json.dumps(payload, ensure_ascii=False),
                        result.timestamp_utc,
                        result.scan_id,
                        candidate.symbol,
                    ),
                )


def update_market_scan_report_path(path: Path, scan_id: str, report_path: Path) -> None:
    with connect_db(path) as connection:
        connection.execute(
            "UPDATE market_scans SET report_path = ? WHERE scan_id = ?",
            (str(report_path), scan_id),
        )
