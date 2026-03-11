"""
extracted.py — fragmenty kodu z WORK.md dla obszaru sqlite.

UWAGA: To są fragmenty referencyjne wyekstrahowane z notatek badawczych.
Mogą wymagać dostosowania przed użyciem w produkcji.

Zawiera 44 fragmentów. Każdy poprzedzony komentarzem ze źródłem.
"""
# ruff: noqa
# type: ignore
from __future__ import annotations

# Source: Agent TODO atomowe zadania i planista offline
# Stabilne ID atomu (deterministyczne)
import hashlib, unicodedata

def make_atom_id(source_hash: str, anchor: str, text: str) -> str:
    norm = unicodedata.normalize('NFKC', text.strip())
    raw = f"{source_hash}|{anchor}|{norm}"
    return "atom_" + hashlib.sha256(raw.encode()).hexdigest()[:12]

# ────────────────────────────────────────────────────────────

# Source: Agent TODO: dokumenty w zadania z audytem
import hashlib
def make_task_id(kind, body, context):
    normalized = f"{kind.upper()}|{body.strip().lower()}|{context.strip().lower()}"
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()

# ────────────────────────────────────────────────────────────

# Source: Agent TODO: dokumenty w zadania z audytem
TODO_PAT = r'(?im)^(?:[-*]\s*)?(?:TODO|ZADANIE|Do zrobienia)\s*[:\-]\s*(.+)$'
AC_PAT   = r'(?im)^(?:[-*]\s*)?(?:AC|Kryteria|Acceptance Criteria)\s*[:\-]\s*(.+)$'
DL_PAT   = r'(?i)\b(?:deadline|termin|due|DDL)\s*[:\-]?\s*(\d{4}[-/.]\d{2}[-/.]\d{2})\b'

# ────────────────────────────────────────────────────────────

# Source: Atestacja zakresów LTX-WAL w Litestream
chain = hashlib.sha256(
    ("v1\n" + "\n".join(f"{e['txid']}:{e['sha256']}" for e in ltx_list) + "\n").encode()
).hexdigest()

# ────────────────────────────────────────────────────────────

# Source: Budżet wykonania dla każdego cyklu agenta
from runtime.ResourceGovernor.BudgetGuard import BudgetGuard
bg = BudgetGuard({"http": 120, "fs_write": 500, "purchase": 0}, mode="hard")
def safe_http_call(*args, **kw):
    bg.check_and_decrement("http")
    return real_http_call(*args, **kw)

# ────────────────────────────────────────────────────────────

# Source: Checklist inwariantów B‑Tree przy odtwarzaniu snapshotów
# Skeleton: page-level hash dla dużych DB
import hashlib, struct
def hash_db_pages(path, page_size=4096):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while chunk := f.read(page_size):
            h.update(chunk)
    return h.hexdigest()

# ────────────────────────────────────────────────────────────

# Source: Detecting Missing Links with SHACL Shapes
# Dispatcher strategii z priorytetem ryzyka
def select_strategy(violation, strategies):
    candidates = [s for s in strategies if s.matches(violation)]
    order = {"low": 0, "medium": 1, "high": 2}
    candidates.sort(key=lambda s: order[s.risk])
    return candidates[0] if candidates else None

# ────────────────────────────────────────────────────────────

# Source: Detecting tool noise through seed tasks
# Kontrakt adaptera audytu
@dataclass
class AuditResult:
    tool: str
    project_id: str
    seed_count: int
    purge_attempted: bool
    purge_succeeded: bool
    purge_time_sec: Optional[float]
    notes: str = ""

# ────────────────────────────────────────────────────────────

# Source: Dlaczego reset prestiżu w grach daje satysfakcję
event_hash = sha256(json.dumps(event, sort_keys=True)).hexdigest()
try:
    db.execute("INSERT INTO prestige_events ... VALUES ...", event)
except UNIQUE_VIOLATION:
    return  # już wykonano, nie przyznawaj ponownie

# ────────────────────────────────────────────────────────────

# Source: Dlaczego reset prestiżu w grach daje satysfakcję
def soft_cap(M, threshold, gamma=0.5):
    if M <= threshold:
        return M
    return threshold + (M - threshold) ** gamma

# ────────────────────────────────────────────────────────────

# Source: DocSchema QA walidacja JSON Schema i linting_04
def stable_fingerprint(parts: Dict[str, Any]) -> str:
    payload = json.dumps(parts, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return "sha256:" + hashlib.sha256(payload.encode("utf-8")).hexdigest()

# ────────────────────────────────────────────────────────────

# Source: Dodaj metryki uzdrawiania do run_manifest
class ExponentialBackoff(RetryPolicy):
    def next_delay(self, attempt: int) -> float:
        raw = self.base_s * (self.factor ** (attempt - 1))
        return raw * (1 + random.uniform(-self.jitter, self.jitter))
    def should_retry(self, failure) -> bool:
        return failure.transience == "transient"

# ────────────────────────────────────────────────────────────

# Source: Dwa wskaźniki centralizacji decyzji
# DRI: CF >= 4 LUB (CB >= 3 I CF >= 2)
# TEMP_DRI: CB >= 3 I CF < 2
# FEDERATED: w pozostałych przypadkach
if conflicts >= 4 or (cb >= 3 and conflicts >= 2):
    decision = "DRI"
elif cb >= 3 and conflicts < 2:
    decision = "TEMP_DRI"
else:
    decision = "FEDERATED"

# ────────────────────────────────────────────────────────────

# Source: Inwarianty replayera i testy deterministyczne_04
import hashlib, jcs
def compute_hash_intent(policy_version, intent_version, intent):
    payload = {"schema_version":"event-v1","policy_version":policy_version,
               "intent_version":intent_version,"intent":intent}
    return hashlib.sha256(jcs.canonicalize(payload)).hexdigest()

# ────────────────────────────────────────────────────────────

# Source: Inwarianty replayera i testy deterministyczne_04
def norm_tool_run(intent):
    return {"op":"tool.run","name":intent["name"],"args":intent.get("args",[]),
            "cwd":norm_path(intent.get("cwd","sandbox:/")),"seed":intent.get("seed"),
            "caps":intent.get("caps",{}),"env":stable_env_hash(intent.get("env",{}),
            ["LANG","LC_ALL","TZ","PYTHONHASHSEED"]),"tool_version":intent.get("tool_version")}

# ────────────────────────────────────────────────────────────

# Source: Inwarianty replayera i testy deterministyczne_04
def validate_trace_lines(lines):
    expected_i = 1
    for raw in lines:
        ev = json.loads(raw)
        assert ev["i"] == expected_i  # A1: gęsty licznik
        assert {"schema_version","policy_version"} <= set(ev["meta"])  # A4
        want = compute_hash_intent(ev["meta"]["policy_version"],
                                   ev["meta"].get("intent_version","v1"), ev["input"])
        assert ev["hash_intent"] == want  # A7
        expected_i += 1

# ────────────────────────────────────────────────────────────

# Source: Inwarianty replayera i testy deterministyczne_04
import resource
def _limit_resources(caps):
    if caps.get("cpu_s"): resource.setrlimit(resource.RLIMIT_CPU, (caps["cpu_s"],)*2)
    if caps.get("as_bytes"): resource.setrlimit(resource.RLIMIT_AS, (caps["as_bytes"],)*2)
subprocess.run(argv, preexec_fn=lambda: _limit_resources(caps),
               env={"TZ":"UTC","LC_ALL":"C","PYTHONHASHSEED":"0",...},
               stdin=subprocess.DEVNULL, timeout=timeout_s, ...)

# ────────────────────────────────────────────────────────────

# Source: Kopia WAL i snapshoty dla odtwarzania offline_04
# Merkle root
acc = hashlib.sha256(open(snap,'rb').read()).hexdigest().encode()
for p in patch_hashes:
    acc = hashlib.sha256(acc + p.encode()).digest()
merkle_root = acc.hex()

# ────────────────────────────────────────────────────────────

# Source: Kryptograficzne znaczniki dla uruchomień AI
def make_run_id(inputs: dict) -> str:
      canonical = json.dumps(inputs, sort_keys=True, ensure_ascii=False, separators=(",",":"))
      return "sha256:" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()

# ────────────────────────────────────────────────────────────

# Source: LangGraph CLI 0.4.12 lokalny serwer agentów
thread = client.post("/threads", json={}).json()
with client.stream("POST", f"/threads/{thread['thread_id']}/runs/stream",
    json={"assistant_id": "agent", "input": {"messages": [...]}, "stream_mode": "values"}
) as r:
    for line in r.iter_lines(): ...

# ────────────────────────────────────────────────────────────

# Source: MinHash do deduplikacji segmentów wiedzy
import unicodedata, re
def normalize_v1(text: str) -> list[str]:
    t = unicodedata.normalize("NFKC", text).lower()
    return re.findall(r"\w+", t, flags=re.UNICODE)

# ────────────────────────────────────────────────────────────

# Source: MinHash do deduplikacji segmentów wiedzy
from datasketch import MinHash
def minhash_for_text(text, shingle=5, num_perm=128):
    m = MinHash(num_perm=num_perm)
    toks = normalize_v1(text)
    for sh in [" ".join(toks[i:i+shingle]) for i in range(len(toks)-shingle+1)]:
        m.update(sh.encode("utf-8"))
    return m

# ────────────────────────────────────────────────────────────

# Source: Minimalny schemat bitemporalny z wyzwalaczami
import json, hashlib, unicodedata

def canonicalize(obj):
    if isinstance(obj, dict):
        return {k: canonicalize(obj[k]) for k in sorted(obj.keys())}
    if isinstance(obj, list):
        return [canonicalize(x) for x in obj]
    if isinstance(obj, str):
        return unicodedata.normalize("NFC", obj)
    return obj

def sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def canonical_json(obj) -> str:
    return json.dumps(canonicalize(obj), ensure_ascii=False,
                      separators=(",", ":"), sort_keys=True)

def item_checksum(v, pk, op, business_from_us, business_to_us, payload):
    return sha256_hex(canonical_json({
        "v": v, "pk": pk, "op": op,
        "business_from_us": business_from_us,
        "business_to_us": business_to_us,
        "payload": payload
    }))

# ────────────────────────────────────────────────────────────

# Source: Modele embeddingów działające offline na CPU
from sentence_transformers import SentenceTransformer
m = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
emb = m.encode(["tekst"], normalize_embeddings=True)

# ────────────────────────────────────────────────────────────

# Source: Modele embeddingów działające offline na CPU
emb = np.asarray(emb, dtype=np.float32)
emb = emb / np.linalg.norm(emb)
conn.execute("INSERT INTO vec(emb, doc_id) VALUES(?,?)", (emb.tobytes(), "doc-001"))

# ────────────────────────────────────────────────────────────

# Source: New advances in AI working memory_05
@dataclass
class WorkingMemory:
    goal: str
    definition_of_done: List[str] = field(default_factory=list)
    subgoals: List[str] = field(default_factory=list)
    current_step: str = ""
    blockers: List[str] = field(default_factory=list)
    constraints: Dict[str, Any] = field(default_factory=dict)
    tools: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    artifacts: Dict[str, Any] = field(default_factory=dict)
    events: List[WMEvent] = field(default_factory=list)
    max_events: int = 32
    local_facts: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    token_budget: int = 1200

# ────────────────────────────────────────────────────────────

# Source: New advances in AI working memory_05
def set_fact(self, key, value, ttl_sec=3600):
    self.local_facts[key] = {"value": value, "expires_utc": int(time.time()) + ttl_sec}

def gc_facts(self):
    now = int(time.time())
    self.local_facts = {k: v for k, v in self.local_facts.items() if v["expires_utc"] > now}

# ────────────────────────────────────────────────────────────

# Source: New advances in AI working memory_05
def snapshot(self) -> dict:
    obj = asdict(self)
    obj["snapshot_hash"] = _stable_hash(obj)
    obj["snapshot_utc"] = int(time.time())
    return obj

# ────────────────────────────────────────────────────────────

# Source: New advances in long-lived agents
def utility(age_days, access_count, confidence, diversity_penalty,
            half_life=60, w=(0.35,0.25,0.25,0.15)):
    rec = 0.5 ** (age_days / half_life)
    acc = math.log1p(access_count) / math.log(101)
    return w[0]*rec + w[1]*acc + w[2]*confidence + w[3]*(1-diversity_penalty)

# ────────────────────────────────────────────────────────────

# Source: Notion AI: siła w prostocie architektury
DEFAULT_PATCH_POLICY = PatchPolicy(
    allowed_ops={"FILTER", "MAP", "VALIDATE", "SQL"},
    mutable_keys={"where", "expr", "schema", "invariants", "query"},
    immutable_keys={"path", "in", "out", "into", "out_table", "table"},
    forbid_new_keys=True
)

# ────────────────────────────────────────────────────────────

# Source: Offline migracja stabilnych ID
# Generowanie stabilnych ID odpornych na kolizje
import uuid, hashlib

def stable_id(namespace: str, key: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, f"{namespace}:{key}"))

# ────────────────────────────────────────────────────────────

# Source: Pomiar mJ operację w Python+SQLite_04
def mj_per_op(delta_uj, dur_s, ops_count, idle_mW):
    work_mJ = delta_uj / 1000.0
    baseline_mJ = (idle_mW * dur_s) if idle_mW else 0.0
    net_mJ = max(0.0, work_mJ - baseline_mJ)
    return net_mJ / max(1, ops_count), work_mJ, baseline_mJ, net_mJ

# ────────────────────────────────────────────────────────────

# Source: Pomiar mJ operację w Python+SQLite_04
def iqr_bounds(xs, k=3.0):
    xs = sorted(xs)
    q1, q3 = statistics.quantiles(xs, n=4)[0], statistics.quantiles(xs, n=4)[2]
    iqr = q3 - q1
    return (q1 - k*iqr, q3 + k*iqr)

# ────────────────────────────────────────────────────────────

# Source: Prosty detektor braków YAML - CSV + SQLite_03
def trigram_score(text):
    s = set(text[i:i+3] for i in range(len(text)-2)) if len(text) >= 3 else set()
    return min(1.0, len(s) / 50.0)

# ────────────────────────────────────────────────────────────

# Source: Pętla auto‑apply z adaptacją PID
@dataclass
class PIDCfg:
    target=0.90; Kp=0.3; Ki=0.05; Kd=0.1
    Tmin=0.50; Tmax=0.95; Imax=0.5

def step(sr, cfg=PIDCfg()):
    e = cfg.target - sr
    I = max(-cfg.Imax, min(cfg.Imax, state["I"] + e))
    D = e - state["e_prev"]
    u = cfg.Kp*e + cfg.Ki*I + cfg.Kd*D
    thr = max(cfg.Tmin, min(cfg.Tmax, state["threshold"] + u))
    if abs(thr - state["threshold"]) < cfg.min_delta:
        thr = state["threshold"]
    state.update(I=I, e_prev=e, threshold=thr)
    return thr

# ────────────────────────────────────────────────────────────

# Source: SQLite JSONB jako warstwa refleksji
# Whitelist projekcja przed JCS kanonizacją
def project_state_for_hash(full_state):
    return {
        "schema_version": full_state.get("schema_version", 1),
        "inputs":    full_state.get("inputs", {}),
        "reasoning": full_state.get("reasoning", {}),
        "actions":   full_state.get("actions", []),
        "outputs":   full_state.get("outputs", {}),
        "env":       full_state.get("env", {}),
    }

# Liczenie hash łańcucha
canonical_bytes = jcs_canonicalize(project_state_for_hash(state))
state_hash  = "sha256:" + sha256_hex(canonical_bytes)
prev_chain  = prev_chain_hash or "GENESIS"
chain_hash  = "sha256:" + sha256_hex((prev_chain + "\n" + state_hash).encode("utf-8"))

# ────────────────────────────────────────────────────────────

# Source: SQLite checkpointing i snapshoty dla replay_04
def canon_json(obj): return json.dumps(obj, ensure_ascii=False, separators=(",",":"), sort_keys=True)
def sha256_hex(s):   return hashlib.sha256(s.encode()).hexdigest()

def append_event(conn, agg_id, event_type, payload_obj):
    payload = canon_json(payload_obj)
    conn.execute("BEGIN IMMEDIATE")
    conn.execute(
        "INSERT INTO event_journal(ts_utc,agg_id,event_type,payload,payload_sha256) VALUES(?,?,?,?,?)",
        (utc_now_iso(), agg_id, event_type, payload, sha256_hex(payload))
    )
    conn.commit()

# ────────────────────────────────────────────────────────────

# Source: Samoregulujące się bazy wiedzy SQLite
fp = simhash64(text)
b0,b1,b2,b3 = buckets_16(fp)
cand = conn.execute("SELECT ref_id, simhash64 FROM dedup_semhash
  WHERE ref_table=? AND (b0=? OR b1=? OR b2=? OR b3=?)", ...)
for ref_id, other in cand:
    if hamming64(fp, int(other)) <= SEM_THRESH:
        raise DuplicateError(ref_id)

# ────────────────────────────────────────────────────────────

# Source: Szkielet arkusza gotowego do audytu
import hashlib, csv

def row_hash(row: dict) -> str:
    canonical = ",".join(row[c].strip() for c in COLUMNS)
    return hashlib.sha256(canonical.encode()).hexdigest()

def is_duplicate(csv_path, row):
    h = row_hash(row)
    with open(csv_path) as f:
        for existing in csv.DictReader(f):
            if row_hash(existing) == h:
                return True
    return False

# ────────────────────────────────────────────────────────────

# Source: Utrzymanie spójności logów przez upcastery zdarzeń
def upcast_to_latest(event, upcasters):
    e = event
    while True:
        applicable = [u for u in upcasters if u.can_handle(e)]
        if not applicable:
            return e
        e = sorted(applicable, key=lambda u: u.target_version)[0].upgrade(e)

# ────────────────────────────────────────────────────────────

# Source: Wizualizacja klastrów błędów w patch_audit
# Aggregacja macierzy heatmapy
pivot = df.pivot_table(index="subsystem", columns="failure_type",
                       values="patch_id", aggfunc="count", fill_value=0)
pivot.to_csv("runs/heatmap_matrix.csv")

# ────────────────────────────────────────────────────────────

# Source: Ścieżki decyzyjne agentów w SQLite
import hashlib, json
def canon_hash(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(',',':')).encode('utf-8')
    ).hexdigest()
# topic_key = canon_hash({"input_hash": ih, "agent_profile_id": ap})

# ────────────────────────────────────────────────────────────

# Source: Śledzenie pochodzenia uruchomień AI
import hashlib, json
def sha256_json(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(',',':')).encode('utf-8')
    ).hexdigest()
def run_hash(input_hash, code_hash, env_hash):
    return hashlib.sha256((input_hash+code_hash+env_hash).encode()).hexdigest()

# ────────────────────────────────────────────────────────────

# Source: Śledzenie pochodzenia uruchomień AI
run_id = recorder.start_run(engine_name, config_json)
step_id = recorder.start_step(run_id, idx=1, name="retrieve", input_json)
# ... wykonanie kroku ...
recorder.finish_step(step_id, output_json, artifact_refs=[])
recorder.finish_run(run_id, status="OK")
