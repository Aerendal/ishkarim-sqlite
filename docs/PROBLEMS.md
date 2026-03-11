# PROBLEMS — ishkarim-sqlite

> SQLite jako baza agentów AI — WAL, checkpointing, FTS5, event-sourcing w jednym pliku

## ✅ Co ten projekt rozwiązuje

- ✅ Trwała pamięć agenta **bez zewnętrznych baz danych** (wszystko w jednym .db pliku)
- ✅ Event-sourcing z pełnym replayem — odtworzenie historii decyzji agenta
- ✅ WAL snapshoty z podpisami Cosign — audytowalny ślad zmian
- ✅ FTS5 full-text search nad notatkami/logami agenta
- ✅ Bitemporalna historia zmian (kiedy nastąpiło vs kiedy dowiedzieliśmy się)

---

## ❌ Czego ten projekt NIE rozwiązuje

- ❌ Współbieżność wielu procesów zapisu — SQLite WAL obsługuje jednego writera naraz
- ❌ Dystrybucja stanu między wieloma maszynami — lokalne, single-node
- ❌ Streaming/real-time events — batch insert, nie message queue
- ❌ Automatyczna kompakcja dużych WAL plików w tle

---

## ⚠️ Znane problemy i ograniczenia

- ⚠️ **WAL checkpoint** może blokować readery w edge cases — używaj `PRAGMA wal_checkpoint(PASSIVE)`
- ⚠️ **JSONB** w SQLite nie waliduje schematów — wymaga dodatkowej warstwy (SHACL/JSON-Schema z `ishkarim-schema`)
- ⚠️ **Duże blobs** (embeddingi) spowalniają backup/snapshot — brak natywnej kompresji blob
- ⚠️ **FTS5 snippet()** ma ograniczenia z polskimi znakami przy tokenizerze unicode61

---

## 🎯 Przypadki użycia

- 🎯 Agent który pamięta poprzednie sesje bez zewnętrznego Redis/Postgres
- 🎯 Audit trail dla systemów AI wymagających zgodności z regulacjami (RODO, ISO 27001)
- 🎯 Lokalne IDE/narzędzie z historią działań użytkownika
- 🎯 Prototypowanie systemów event-sourced przed przejściem na Kafka/EventStore

---

## 📊 Matryca decyzyjna

| Pytanie | Odpowiedź |
|---------|-----------|
| Czy potrzebujesz GPU? | **NIE** — zaprojektowany dla CPU-only |
| Czy działa offline? | **TAK** — zero zewnętrznych zależności sieciowych |
| Czy jest produkcyjny? | **WZORCE** — referencja do implementacji, nie plug-and-play |
| Czy obsługuje skalowanie? | **LOKALNIE** — single-node, do ~kilku tysięcy dokumentów |
| Licencja? | **MIT** — możesz używać w projektach komercyjnych |

---

## 🔗 Powiązane projekty

Inne moduły Ishkarim które uzupełniają ten projekt:

| Projekt | Relacja |
|---------|---------|
| `ishkarim-rag` | Wyszukiwanie semantyczne nad bazą wiedzy |
| `ishkarim-sqlite` | Trwała pamięć i event-sourcing |
| `ishkarim-agent` | Architektura agentów AI |
| `ishkarim-security` | Bezpieczeństwo systemów AI |
| `ishkarim-bench` | Benchmarki wydajnościowe |

---

*Ostatnia aktualizacja: 2026-03-11 | Generator: `scripts/enrich_projects.py`*
