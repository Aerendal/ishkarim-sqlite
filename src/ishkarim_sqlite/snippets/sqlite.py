"""
sqlite.py — fragmenty kodu z WORK.md dla obszaru sqlite.

UWAGA: To są fragmenty referencyjne wyekstrahowane z notatek badawczych.
Mogą wymagać dostosowania przed użyciem w produkcji.

Zawiera 5 fragmentów. Każdy poprzedzony komentarzem ze źródłem.
"""
# ruff: noqa
# type: ignore
from __future__ import annotations

# Source: Atestacja zakresów LTX-WAL w Litestream
schema_text = sqlite3.connect(db).execute(
    "SELECT COALESCE(group_concat(sql,'\n'),'') "
    "FROM (SELECT sql FROM sqlite_schema WHERE sql IS NOT NULL ORDER BY type, name);"
).fetchone()[0]
schema_sha256 = hashlib.sha256(schema_text.encode()).hexdigest()

# ────────────────────────────────────────────────────────────

# Source: Budżet wykonania dla każdego cyklu agenta
from runtime.ResourceGovernor.Policies import get_policy_limits
limits = get_policy_limits(source="sqlite", policy_name="default", sqlite_path="var/db/core.sqlite3")
guard = BudgetGuard(limits, mode="hard")

# ────────────────────────────────────────────────────────────

# Source: Kopia WAL i snapshoty dla odtwarzania offline_04
# Snapshot przez Backup API
src = sqlite3.connect('live.db', isolation_level=None)
dst = sqlite3.connect(dst_path)
dst.backup(src)
h = hashlib.sha256(open(dst_path,'rb').read()).hexdigest()
meta = {"snapshot_path": dst_path, "sha256": h}

# ────────────────────────────────────────────────────────────

# Source: LangGraph Checkpointing i trwałość stanu agenta
from langgraph.checkpoint.sqlite import SqliteSaver
with SqliteSaver.from_conn_string("./checkpoints.db") as saver:
    graph = builder.compile(checkpointer=saver)
    result = graph.invoke(input, config={"configurable": {"thread_id": "session-1"}})

# ────────────────────────────────────────────────────────────

# Source: SQLite checkpointing i snapshoty dla replay_04
def backup_db(src_path, dst_path):
    src = sqlite3.connect(src_path)
    dst = sqlite3.connect(dst_path + ".tmp")
    src.backup(dst)           # sqlite3_backup API — spójny snapshot
    dst.close(); src.close()
    os.rename(dst_path + ".tmp", dst_path)  # atomowe publish
