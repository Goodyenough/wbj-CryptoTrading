from __future__ import annotations

from dataclasses import asdict
import json
from pathlib import Path
import sqlite3

from .models import ScanResult


def init_db(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(path) as connection:
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
                payload_json TEXT NOT NULL,
                UNIQUE (account_name, source_scan_id, source_rank)
            )
            """
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


def save_scan_result(path: Path, result: ScanResult) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(path) as connection:
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
