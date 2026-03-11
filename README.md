# ishkarim-sqlite

> SQLite jako baza agentów: WAL, FTS5, checkpointing, event-sourcing, JSONB, embeddingi.

## Instalacja

```bash
pip install -e projects/ishkarim-sqlite
```

Lub lokalnie z tego repozytorium:

```bash
cd projects/ishkarim-sqlite
pip install -e ".[dev]"
```

## Użycie

```python
import ishkarim_sqlite as m

# Lista dostępnych modułów
print(m.MODULES)

# Wczytaj indeks wiedzy
docs = m.load_knowledge_index()
```

## Obszar tematyczny

Ten projekt agreguje wiedzę z **154 katalogów** obszaru `sqlite`:

- `5‑minutowy pre‑mortem dla decyzji`
- `AGI pamięć długowiecznych agentów open-r1`
- `AI w grach Behavior Trees, GOAP i szybkie starty procgen`
- `ASCII-wizualizacja różnic w bazie wiedzy`
- `Agent TODO atomowe jednostki pracy`
- `Agent TODO atomowe zadania i planista offline`
- `Agent TODO z atomowym wykonywaniem i checkpointami`
- `Agent TODO z dokumentów i wersjami artefaktów`
- … i 146 więcej (pełna lista w [MODULES.md](MODULES.md))

## Przykładowe źródła

### 5‑minutowy pre‑mortem dla decyzji

# WORK: 5‑minutowy pre‑mortem dla decyzji
## 0-Metadane
- Katalog: 5‑minutowy pre‑mortem dla decyzji
- Pliki: 12 (bez placeholderów; pliki 01–12 zawierają treść, 13–60 są puste)
- Tagi: pre-mortem, decyzje, ryzyka, ADR, CI-gate, DORA, SQLite, rollback, baseline, governance

### AGI pamięć długowiecznych agentów open-r1

# WORK: AGI pamiec dlugowiecznych agentow open-r1
## 0-Metadane
- Katalog: AGI pamiec dlugowiecznych agentow open-r1
- Pliki: 9 (bez placeholderow; pliki 1-9 zawieraja tresc, 10-60 sa puste)
- Tagi: AGI, Open-R1, DeepSeek-R1, pamiec-agentow, Hindsight, reading-notes, KANBAN, SQLite, FTS5, sqlite-vec, LangGraph, architektura

### AI w grach Behavior Trees, GOAP i szybkie starty procgen

# AI w grach Behavior Trees, GOAP i szybkie starty procgen
## 0-Metadane
- Pliki: 10
- Tagi: Godot, BehaviorTrees, GOAP, NPC, headless, telemetria, procgen, SQLite, GDScript
- Status: done


## Struktura projektu

```
ishkarim-sqlite/
├── pyproject.toml        # installable package
├── README.md
├── MODULES.md            # pełny indeks 154 katalogów-źródeł
├── src/
│   └── ishkarim_sqlite/
│       ├── __init__.py   # publiczne API
│       ├── utils.py      # wspólne narzędzia
│       └── *.py          # kod wyekstrahowany z WORK.md
├── tests/
│   ├── __init__.py
│   └── test_sqlite.py
└── docs/
    ├── overview.md
    └── sources.md
```

## Testy

```bash
pytest projects/ishkarim-sqlite/tests/ -v
```

## Źródło danych

Katalogi źródłowe znajdują się w katalogu głównym repozytorium Ishkarim.
Każdy katalog zawiera `WORK.md` (notatki badawcze) i `TAGS.md` (metadane).

---
*Wygenerowano automatycznie przez `scripts/build_projects.py`*
