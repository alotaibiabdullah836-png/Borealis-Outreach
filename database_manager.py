"""Transactional CRM state management for Borealis outreach."""

from __future__ import annotations

from datetime import datetime, timezone
import json
import logging
from pathlib import Path
import sqlite3
from typing import Dict, List

import pandas as pd

from lead_discovery import normalize_email

log = logging.getLogger(__name__)

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS leads (
    email TEXT PRIMARY KEY,
    name TEXT DEFAULT '',
    title TEXT DEFAULT '',
    company TEXT DEFAULT '',
    country TEXT DEFAULT '',
    source TEXT DEFAULT '',
    lawful_basis TEXT DEFAULT '',
    status TEXT NOT NULL DEFAULT 'new',
    send_attempts INTEGER NOT NULL DEFAULT 0,
    message_id TEXT DEFAULT '',
    last_error TEXT DEFAULT '',
    date_added TEXT NOT NULL,
    date_contacted TEXT DEFAULT '',
    metadata_json TEXT DEFAULT '{}'
);
CREATE INDEX IF NOT EXISTS idx_leads_status ON leads(status);
"""

BLOCKING_STATUSES = {"sending", "sent", "dry_run"}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


class DatabaseManager:
    """SQLite-backed CRM with unique email constraints and Excel reporting export."""

    def __init__(self, db_path: str | Path = "data/outreach.sqlite3", excel_path: str | Path = "data/crm_database.xlsx"):
        self.db_path = Path(db_path)
        self.excel_path = Path(excel_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.excel_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path, timeout=30)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA busy_timeout=30000")
        return conn

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.executescript(SCHEMA_SQL)
            conn.commit()

    def claim_for_sending(self, prospect: Dict[str, str]) -> bool:
        """Atomically claim a prospect before delivery.

        Returns False if the email already exists in a blocking state, preventing duplicate
        sends after reruns or partially completed runs.
        """

        email = normalize_email(prospect.get("email"))
        if not email:
            return False
        now = utc_now()
        metadata = {k: v for k, v in prospect.items() if k not in {"email", "name", "title", "company", "country", "source", "lawful_basis"}}

        with self._connect() as conn:
            existing = conn.execute("SELECT status FROM leads WHERE email = ?", (email,)).fetchone()
            if existing and existing["status"] in BLOCKING_STATUSES:
                return False
            if existing and existing["status"] == "failed":
                # Failed records are left for manual review rather than retried automatically.
                return False
            conn.execute(
                """
                INSERT INTO leads(email, name, title, company, country, source, lawful_basis, status, send_attempts, date_added, metadata_json)
                VALUES (?, ?, ?, ?, ?, ?, ?, 'sending', 1, ?, ?)
                ON CONFLICT(email) DO UPDATE SET
                    name=excluded.name,
                    title=excluded.title,
                    company=excluded.company,
                    country=excluded.country,
                    source=excluded.source,
                    lawful_basis=excluded.lawful_basis,
                    status='sending',
                    send_attempts=leads.send_attempts + 1,
                    metadata_json=excluded.metadata_json
                """,
                (
                    email,
                    prospect.get("name", ""),
                    prospect.get("title", ""),
                    prospect.get("company", ""),
                    prospect.get("country", ""),
                    prospect.get("source", ""),
                    prospect.get("lawful_basis", ""),
                    now,
                    json.dumps(metadata, sort_keys=True),
                ),
            )
            conn.commit()
            return True

    def mark_result(self, email: str, *, success: bool, status: str, message_id: str = "", error: str = "") -> None:
        normalized = normalize_email(email)
        if not normalized:
            return
        date_contacted = utc_now() if success else ""
        with self._connect() as conn:
            conn.execute(
                """
                UPDATE leads
                SET status = ?, message_id = ?, last_error = ?, date_contacted = ?
                WHERE email = ?
                """,
                (status, message_id, error[:1000], date_contacted, normalized),
            )
            conn.commit()

    def list_rows(self) -> List[Dict[str, str]]:
        with self._connect() as conn:
            rows = conn.execute("SELECT * FROM leads ORDER BY date_added ASC, email ASC").fetchall()
        return [dict(row) for row in rows]

    def export_excel(self) -> Path:
        rows = self.list_rows()
        columns = [
            "email",
            "name",
            "title",
            "company",
            "country",
            "source",
            "lawful_basis",
            "status",
            "send_attempts",
            "message_id",
            "last_error",
            "date_added",
            "date_contacted",
        ]
        df = pd.DataFrame(rows, columns=columns)
        self.excel_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_excel(self.excel_path, index=False)
        log.info("Exported CRM report to %s", self.excel_path)
        return self.excel_path


# Backward-compatible helper.
def add_lead(prospect: Dict[str, str]) -> None:
    db = DatabaseManager()
    if db.claim_for_sending(prospect):
        db.mark_result(prospect.get("email", ""), success=False, status="manual_review", error="legacy add_lead call")
        db.export_excel()
