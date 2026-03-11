"""
ishkarim_sqlite — moduł z obszaru sqlite.

SQLite jako baza agentów: WAL, FTS5, checkpointing, event-sourcing, JSONB, embeddingi.

Źródła: 154 katalogów z repozytorium Ishkarim.
"""
from __future__ import annotations

__version__ = "0.1.0"
__area__ = "sqlite"



MODULES: list[str] = [
    '5‑minutowy pre‑mortem dla decyzji',
    'AGI pamięć długowiecznych agentów open-r1',
    'AI w grach Behavior Trees, GOAP i szybkie starty procgen',
    'ASCII-wizualizacja różnic w bazie wiedzy',
    'Agent TODO atomowe jednostki pracy',
    'Agent TODO atomowe zadania i planista offline',
    'Agent TODO z atomowym wykonywaniem i checkpointami',
    'Agent TODO z dokumentów i wersjami artefaktów',
    'Agent TODO z dokumentów: pipeline i audyt',
    'Agent TODO: dokumenty w zadania z audytem',
    'Agent „TODO z dokumentów”: testy i metryki',
    'Append‑only JSONL + SQLite: bezpieczne migawki i GC',
    'Atestacja zakresów LTX-WAL w Litestream',
    'Automated Artifact Scoring Gate',
    'Automatyczna indukcja schematów LinkML + SQLite_04',
    'Automatyczne snapshoty DB w kontenerach Podman',
    'Bezpieczeństwo przez zwodzenie: case study i metryki',
    'Bez‑ML: polskie NLU przez automaty i logikę',
    'Bitemporalny checkpointer z SQLite i JSON‑Patch',
    'Blueprint agenta ToDo-Agent z CLI i sandomboxem',
    'Blueprint for Self‑Healing DevOps Systems',
    'Blueprint for a proactive, self‑healing Linux',
    'Budżet wykonania dla każdego cyklu agenta',
    'CPU-Only AGI — Key Findings',
    'Checklist inwariantów B‑Tree przy odtwarzaniu snapshotów',
    'Checklist pętli idempotentnych i upsertów',
    'Choosing CRDTs for Multi‑Agent Editing',
    'Cosign + DSSE - podpisy i atestacje SQLite',
    'Cykl WAL i test deterministycznego replaya_04',
    'Detecting Missing Links with SHACL Shapes',
    'Detecting tool noise through seed tasks',
    'Deterministyczny przepływ YAML → SQLite → graf',
    'Deterministyczny replay i podpisane snapshoty',
    'Deterministyczny replayer i testy międzyjęzykowe dla SQLite',
    'DevOps, który sam się naprawia',
    'Dlaczego reset prestiżu w grach daje satysfakcję',
    'DocSchema QA walidacja JSON Schema i linting_04',
    'Dodaj metryki uzdrawiania do run_manifest',
    'Dwa wskaźniki centralizacji decyzji',
    'Dwuczasowa oś pamięci dla agentów',
    'Dwuczasowy dziennik z JSON‑Patch i triggerami',
    'Event‑sourcing z SQLite — wzorce i testy',
    'Flagi i ID w programowaniu',
    'Formalny automat dla bramek TIU',
    'Funkcje i moduły SQLite',
    'Genealogia uczenia maszynowego',
    'GitHub Copilot z pamięcią między agentami',
    'Git‑backed pamięć i migracje z Dolt i Beads',
    'Git‑first JSONL + SQLite — kompaktowanie i\u202fpodsumowania',
    'Gry jako modele baz wiedzy',
    'Interfejsy semantyczne i Graph-RAG',
    'Inwarianty replayera i testy deterministyczne_04',
    'Jak rozpoznać zakleszczenie między agentami',
    'Jak unikać „fantomowych" cytowań w badaniach',
    'Jedna niezmienność każdego zdarzenia: zawsze musi istnieć wyjście',
    'Kompakcja i audyt GC w bazach CRDT-SQLite',
    'Kontrola integralności SQLite i offline replay',
    'Kontrola wersji dla światów fabularnych',
    'Kopia WAL i snapshoty dla odtwarzania offline_04',
    'Kryptograficzne znaczniki dla uruchomień AI',
    'LangGraph CLI 0.4.12 lokalny serwer agentów',
    'LangGraph Checkpoint 4.0.0: duża aktualizacja',
    'LangGraph Checkpointing i trwałość stanu agenta',
    'Lekki test idempotencji w CI',
    'Linux as a proactive security loop',
    'Lista kontrolna dla ewaluacji i zgodności SQLite',
    'LiteFS i Cosign: podpisy i sumy kontrolne snapshotów',
    'Litestream 0 5 8 poprawione WAL‑verify i podpisy w CI_04',
    'Litestream i wal‑browser: narzędzia do odtwarzania WAL',
    'Lokalna walidacja manifestów JSON‑Schema w SQLite',
    'Lokalne wzorce pamięci i checkpointów agentów',
    'Lokalny TUI do inspekcji śladów JSONL',
    'MinHash do deduplikacji segmentów wiedzy',
    'Minimalny schemat bitemporalny z wyzwalaczami',
    'Modele embeddingów działające offline na CPU',
    'Modularny harness testowy dla modułów Crawlera',
    'Najnowsze lokalne AGI i autonomia',
    'New Breakthroughs in spatial maps',
    'New advances in AI working memory_05',
    'New advances in interactive narratives',
    'New advances in long-lived agents',
    'New simulation datasets & tools',
    'New tools for rollback  and reproducibility',
    'Nie recyklinguj ID zdarzeń — wersjonuj dane',
    'Normalizacja identyfikatorów przed deduplikacją',
    'Notion AI: siła w prostocie architektury',
    'Nowa fala CPU‑first w AI',
    'Nowe badania o pamięci AI',
    'Nowe preprinty i narzędzia — przegląd',
    'Nowości: mapy i cyfrowe bliźniaki',
    'Nowość SQLite `VACUUM INTO` z parametrem reserve — uwagi o WAL_04',
    'Nowość SQLite: Walidacja wymagań przez Spectral i checklisty',
    'Odtwarzanie deterministycznych uruchomień agentów',
    'Offline migracja stabilnych ID',
    'Pamięć trwała i odporność agentów',
    'Pipeline: inferencja, formalizacja i walidacja schematów JSON',
    'Plan instalacji i testów CPU‑only dla SQLite‑vec_04',
    'Playbook bezpieczeństwo adaptacyjne i zwodnicze',
    'Podpisy Sigstore i attestacje w SQLite',
    'Podpisy i weryfikacja snapshotów w CI pipeline',
    'Podpisywane snapshoty SQLite i kontrola spójności',
    'Pokój-refaktoryzacja zamiast walki z bossem',
    'Polityka jako kod',
    'Pomiar mJ operację w Python+SQLite_04',
    'Poniedziałkowe Monitory: symulacje i lokalna autonomia',
    'Postgres + DiskANN: testy p95 i kompresja',
    'Praktyczne wzorce GC, TTL i\u202fcheckpointów w\u202fSQLite',
    'Projekt: lokalny ledger SQLite z TTL i checkpointami JSON‑delta',
    'Projektowanie wizualnych przepływów wiedzy',
    'Prosty SQL‑probe i manifest JSON do attestu',
    'Prosty detektor braków YAML - CSV + SQLite_03',
    'Pętla auto‑apply z adaptacją PID',
    'Recepta na FTS5 wczytywanie i łączenie segmentów_04',
    'Rejestrowanie decyzji agentów w Ledgerze AI',
    'Replikacja między wersjami: VACUUM INTO, WAL i polityka sum kontrolnych',
    'Reprodukowalne buildy SQLite‑vec i SQLite‑vss_04',
    'Retencja, kompakcja i testy offline dla agentów',
    'Roundtrip LinkML → JSON‑Schema → SQLite',
    'Równoległość sesji CLI: manifesty i nadzór',
    'SQLite Changesets — audyt i odtwarzanie zmian',
    'SQLite JSONB jako warstwa refleksji',
    'SQLite Session + sqldiff — podpisane migawki i\u202fzmiany',
    'SQLite checkpointing i snapshoty dla replay_04',
    'SQLite‑first trwała pamięć agentów',
    'Samo-naprawiający DevOps w lokalnym środowisku',
    'Samoregulujące się bazy wiedzy SQLite',
    'Samouzdrawiające pętle oparte na patch-audytach',
    'Semantyczne interfejsy do baz wiedzy',
    'Silnik do połączeń grafowych',
    'Silniki z dowodami: Z3, cvc5, Kissat, Soufflé',
    'Sonda inwariantów na poziomie stron SQLite_04',
    'Sondowanie stron i replay WAL',
    'Strategie audytu JSONB w SQLite',
    'Szkielet arkusza gotowego do audytu',
    'Test Gates jako żywe kontrakty',
    'Testy replay WAL i walidacja checksum',
    'Textual 7.3 i Grafana – nowe sposoby na widok danych',
    'Textual 7.3.0 — nowoczesne interfejsy terminalowe',
    'Top\xa03 priorytety na jutro',
    'Tripwire dla regresji buildów',
    'Trwała pamięć agenta - git, bitemporalność, CRDT',
    'Utrzymanie spójności logów przez upcastery zdarzeń',
    'Wizualizacja klastrów błędów w patch_audit',
    'Wizualne grafy wiedzy i przepływy danych',
    'Wspólna pamięć dla sesji CLI',
    'Wykrywanie dryfu schematów i bramki CI',
    'Wzorce implementacji rejestrów danych',
    'Zachowuj SQLITE_SOURCE_ID dla audytu binariów',
    'Zamień projekt w konkretny następny krok',
    'Zasada ‘pytaj tylko gdy utkniesz’',
    'bito‑lint: lokalna, deterministyczna kontrola jakości dokumentów',
    'Ćwiczenia odtwarzania bazy: WAL, VACUUM, backupy',
    'Ścieżki decyzyjne agentów w SQLite',
    'Śledzenie pochodzenia uruchomień AI',
]


_REPO_ROOT: str | None = None


def _find_repo_root() -> str:
    """Auto-discover the Ishkarim repo root by walking up from __file__."""
    from pathlib import Path
    p = Path(__file__).resolve().parent
    for _ in range(10):
        if (p / "CATALOG.md").exists() or (p / "CHANGELOG.md").exists():
            return str(p)
        p = p.parent
    return str(Path(__file__).resolve().parents[5])  # fallback


def load_knowledge_index(root: str | None = None) -> list[dict]:
    """
    Zwraca listę rekordów ze wszystkich katalogów-źródeł obszaru.

    Args:
        root: ścieżka do katalogu głównego repozytorium (opcjonalne)

    Returns:
        Lista słowników z kluczami: name, doc_id, maturity, area
    """
    import re
    from pathlib import Path

    if root is None:
        root = _find_repo_root()

    results = []
    for name in MODULES:
        tags_path = Path(root) / name / "TAGS.md"
        if not tags_path.exists():
            continue
        tags = tags_path.read_text(errors="replace")
        doc_id = ""
        maturity = "draft"
        m = re.search(r"^doc_id:\s*(\S+)", tags, re.M)
        if m:
            doc_id = m.group(1)
        m2 = re.search(r"^maturity:\s*(\S+)", tags, re.M)
        if m2:
            maturity = m2.group(1)
        results.append({"name": name, "doc_id": doc_id, "maturity": maturity, "area": "sqlite"})
    return results


__all__ = ["MODULES", "load_knowledge_index", "__version__", "__area__"]
