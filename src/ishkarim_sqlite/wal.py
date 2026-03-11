"""
wal.py — kod wyekstrahowany z WORK.md dla obszaru sqlite.

Zawiera 4 fragmentów kodu. Każdy fragment poprzedzony komentarzem
z nazwą katalogu-źródła.
"""
from __future__ import annotations



# ────────────────────────────────────────────────────────────# Source: Agent „TODO z dokumentów”: testy i metryki
conn.execute("PRAGMA journal_mode=WAL;")
conn.execute("PRAGMA synchronous=NORMAL;")
conn.execute("PRAGMA busy_timeout=5000;")
conn.execute("PRAGMA foreign_keys=ON;")

# Source: Cosign + DSSE - podpisy i atestacje SQLite
WAL_HDR_MAGIC_BE = 0x377f0682  # big endian
WAL_HDR_MAGIC_LE = 0x377f0683  # little endian
WAL_HDR_BYTES = 32
FRAME_HDR_BYTES = 24

def checksum_words(data: bytes, s0: int, s1: int, big_endian: bool):
    fmt = '>I' if big_endian else '<I'
    words = struct.unpack_from(fmt * (len(data)//4), data)
    for i in range(0, len(words), 2):
        s0 = (s0 + words[i] + s1) & 0xFFFFFFFF
        s1 = (s1 + words[i+1] + s0) & 0xFFFFFFFF
    return s0, s1

# Wynik: last_valid_frame, last_commit_frame
# Opcja trim: truncate(wal_path, last_commit_frame * frame_size + HDR)

# Source: SQLite checkpointing i snapshoty dla replay_04
def wal_checkpoint(conn, mode, attempts=10, backoff_ms=200, deadline_ms=60000):
    t0 = time.perf_counter()
    for attempt in range(1, attempts+1):
        row = conn.execute(f"PRAGMA wal_checkpoint({mode})").fetchone()
        busy_flag, log_pages, ckpt_pages = int(row[0]), int(row[1]), int(row[2])
        if busy_flag == 0: break
        if (time.perf_counter() - t0)*1000 >= deadline_ms: break
        time.sleep(backoff_ms * attempt / 1000)
    return {"busy_flag": busy_flag, "log_pages": log_pages, "ckpt_pages": ckpt_pages}

# Source: Ćwiczenia odtwarzania bazy: WAL, VACUUM, backupy
# Baseline snapshot + walidacja
conn.execute("PRAGMA wal_autocheckpoint=0")
conn.execute("PRAGMA wal_checkpoint(RESTART)")
content_sha = sha256_table(conn, 'items')
conn.execute("VACUUM INTO 'baseline.db'")

# Bariera przed snapshot
conn.execute("BEGIN IMMEDIATE"); conn.execute("COMMIT")  # flush
checkpoint(conn, mode="RESTART")
commit_seq = get_commit_seq(conn)
# Teraz kopiowanie bezpieczne

# Hash-chain manifestu
manifest = {"run_id": rid, "prev_hash": read_head(index_dir), ...}
manifest["sha256"] = sha256(json.dumps(manifest, sort_keys=True))
write_head(index_dir, manifest["sha256"])
