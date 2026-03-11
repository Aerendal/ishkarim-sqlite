#!/usr/bin/env python3
"""
demo.py — demo ishkarim-sqlite

SQLite jako baza agentów AI — WAL, checkpointing, FTS5, event-sourcing w jednym pliku

Uruchomienie:
    python projects/ishkarim-sqlite/demo.py
"""
import sqlite3, pathlib, json

DB = pathlib.Path(__file__).parents[2] / "tools" / "search.db"
if not DB.exists():
    print("Zbuduj najpierw: python3 scripts/build_index.py"); exit(1)

with sqlite3.connect(DB) as con:
    # Statystyki bazy
    count = con.execute("SELECT count(*) FROM docs").fetchone()[0]
    tables = [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table'")]
    ok = con.execute("PRAGMA integrity_check").fetchone()[0]
    page_size = con.execute("PRAGMA page_size").fetchone()[0]
    page_count = con.execute("PRAGMA page_count").fetchone()[0]

stats = {
    "dokumenty": count, "tabele": tables,
    "integralność": ok,
    "rozmiar_MB": round(page_size * page_count / 1024 / 1024, 2)
}
print(json.dumps(stats, ensure_ascii=False, indent=2))

