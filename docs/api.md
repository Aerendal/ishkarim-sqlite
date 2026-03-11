# API — ishkarim_sqlite

> SQLite jako baza agentów: WAL, FTS5, checkpointing, event-sourcing.

## Moduł główny: `ishkarim_sqlite`

```python
import ishkarim_sqlite
```

### Publiczne atrybuty

| Atrybut | Typ | Opis |
|---------|-----|------|
| `__version__` | `str` | Wersja pakietu (np. `"0.1.0"`) |
| `__area__` | `str` | Nazwa obszaru tematycznego (`"sqlite"`) |
| `MODULES` | `list[str]` | Lista 222 nazw katalogów-źródeł |

### `load_knowledge_index(root=None) → list[dict]`

Zwraca listę rekordów metadanych dla wszystkich katalogów-źródeł obszaru.

**Parametry:**
- `root` — ścieżka do katalogu głównego repozytorium (opcjonalne, autodiscovery jeśli `None`)

**Zwraca:** listę słowników z kluczami:
```python
{
    "name":     str,   # nazwa katalogu (np. "Hybrid RAG w SQLite")
    "doc_id":   str,   # identyfikator (np. "DOC-RAG-0042")
    "maturity": str,   # FROZEN | DECISION | DRAFT
    "area":     str,   # "sqlite"
}
```

**Przykład:**
```python
import ishkarim_sqlite

docs = ishkarim_sqlite.load_knowledge_index()
print(f"Znaleziono {len(docs)} katalogów")

# Filtruj po dojrzałości
frozen = [d for d in docs if d["maturity"] == "FROZEN"]
print(f"FROZEN: {len(frozen)}")
```

---

## Moduł: `ishkarim_sqlite.utils`

```python
from ishkarim_sqlite.utils import read_work_md, extract_tags, extract_python_blocks
```

### `def read_work_md(dir_path: str | Path) -> str:`

Wczytuje WORK.md z podanego katalogu.

### `def extract_tags(dir_path: str | Path) -> dict:`

Parsuje TAGS.md i zwraca słownik metadanych.

### `def extract_python_blocks(work_md: str) -> list[str]:`

Wyodrębnia bloki ```python z tekstu Markdown.


---

## Snippety kodu: `ishkarim_sqlite.snippets`

Fragmenty kodu wyekstrahowane z WORK.md (referencyjne, nie produkcyjne):

- `snippets/wal.py`
- `snippets/extracted.py`
- `snippets/sqlite.py`
- `snippets/checkpoint.py`
- `snippets/replay.py`

### Jak używać snippetów

```python
# Snippety są dostępne jako pliki .py w katalogu snippets/
# Możesz je przeglądać, kopiować fragmenty do własnych projektów

import importlib.util, pathlib
snippet_path = pathlib.Path(ishkarim_sqlite.__file__).parent / "snippets" / "retrieved_snippet.py"
# Przeczytaj jako tekst (bezpieczniejsze niż import dla fragmentów z błędami):
print(snippet_path.read_text())
```

---

## Rozszerzenia i zależności opcjonalne

```bash
# Podstawowe (bez ML)
pip install -e "projects/ishkarim-sqlite"

# Z modelami embeddings (dla RAG)
pip install -e "projects/ishkarim-sqlite[rag]"

# Z narzędziami SQLite
pip install -e "projects/ishkarim-sqlite[sqlite]"

# Środowisko deweloperskie (z pytest)
pip install -e "projects/ishkarim-sqlite[dev]"
```

---

## Uruchomienie testów

```bash
# Testy jednostkowe (bez danych repo)
pytest projects/ishkarim-sqlite/tests/test_sqlite.py -v

# Testy domenowe (wymagają repo Ishkarim)
pytest projects/ishkarim-sqlite/tests/test_sqlite_domain.py -v

# Wszystkie testy
pytest projects/ishkarim-sqlite/tests/ -v

# Z pokryciem kodu
pytest projects/ishkarim-sqlite/tests/ --cov=ishkarim_sqlite --cov-report=term-missing
```

---

## Benchmarki

```bash
python projects/ishkarim-sqlite/benchmarks/bench_sqlite.py
```

*Wygenerowano automatycznie przez `scripts/enrich_projects.py`*
