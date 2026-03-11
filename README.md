# ishkarim-sqlite

> **SQLite jako baza agentów AI — WAL, checkpointing, FTS5, event-sourcing w jednym pliku**

[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)]()
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![CPU-only](https://img.shields.io/badge/CPU-only-orange)]()

## Problem, który rozwiązujemy

- Trwała pamięć agenta
- Event-sourcing z pełnym replayem — odtworzenie historii decyzji agenta
- WAL snapshoty z podpisami Cosign — audytowalny ślad zmian

Pełna lista → [docs/PROBLEMS.md](docs/PROBLEMS.md)

## Szybki start

```bash
# Instalacja
pip install -e projects/ishkarim-sqlite

# Demo (10 sekund)
python projects/ishkarim-sqlite/demo.py
```

## Użycie w kodzie

```python
import ishkarim_sqlite as m

# Wszystkie 154 katalogi wiedzy obszaru 'sqlite'
docs = m.load_knowledge_index()
print(f"{len(docs)} katalogów | obszar: {m.__area__}")

# Narzędzia pomocnicze
from ishkarim_sqlite.utils import read_work_md, extract_tags, extract_python_blocks
```

## Dla kogo

- Agent który pamięta poprzednie sesje bez zewnętrznego Redis/Postgres
- Audit trail dla systemów AI wymagających zgodności z regulacjami (RODO, ISO 27001)
- Lokalne IDE/narzędzie z historią działań użytkownika

## Dokumentacja

| Plik | Zawartość |
|------|-----------|
| [docs/PROBLEMS.md](docs/PROBLEMS.md) | Co rozwiązuje / czego nie / znane problemy |
| [docs/api.md](docs/api.md) | Dokumentacja API |
| [docs/overview.md](docs/overview.md) | Przegląd obszaru |
| [docs/sources.md](docs/sources.md) | Źródłowe katalogi wiedzy |
| [MODULES.md](MODULES.md) | Pełny indeks 154 katalogów |

## Testy i benchmarki

```bash
# Testy jednostkowe
pytest tests/test_sqlite.py -v

# Testy domenowe (z prawdziwymi danymi)
pytest tests/test_sqlite_domain.py -v

# Benchmarki wydajnościowe
python benchmarks/bench_sqlite.py --quick
```

## Struktura projektu

```
ishkarim-sqlite/
├── demo.py                    ← uruchom mnie
├── pyproject.toml
├── README.md
├── MODULES.md                 ← 154 katalogów-źródeł
├── docs/
│   ├── PROBLEMS.md            ← co rozwiązuje / czego nie
│   ├── api.md                 ← dokumentacja API
│   ├── overview.md
│   └── sources.md
├── src/ishkarim_sqlite/
│   ├── __init__.py            ← MODULES list + load_knowledge_index()
│   ├── utils.py               ← read_work_md, extract_tags, extract_python_blocks
│   └── snippets/              ← kod z WORK.md (referencyjny)
├── tests/
│   ├── test_sqlite.py         ← testy jednostkowe
│   └── test_sqlite_domain.py  ← testy domenowe
└── benchmarks/
    └── bench_sqlite.py        ← benchmarki wydajnościowe
```

## Ograniczenia

> ⚠️ To projekt **referencyjny** — wzorce i wiedza, nie gotowa biblioteka produkcyjna.
> Przed wdrożeniem produkcyjnym przeczytaj [docs/PROBLEMS.md](docs/PROBLEMS.md).

---

*Część ekosystemu [Ishkarim](../../README.md) — 154 katalogów wiedzy obszaru `sqlite`*
*Wygenerowano: 2026-03-11 | `scripts/build_projects.py` + `scripts/enrich_projects.py`*
