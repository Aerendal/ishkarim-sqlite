"""
test_sqlite_domain.py — testy domenowe dla ishkarim_sqlite.

Testy używają prawdziwych danych z repozytorium Ishkarim.
Wymagają, że pakiet jest zainstalowany (pip install -e .).
"""
import pytest
from pathlib import Path
import ishkarim_sqlite
from ishkarim_sqlite import load_knowledge_index


@pytest.fixture
def repo_root():
    """Zwraca ścieżkę do katalogu głównego repozytorium Ishkarim."""
    root = Path(__file__).resolve().parents[3]  # projects/ishkarim-sqlite/tests/ → repo root
    assert (root / "CATALOG.md").exists() or (root / "CHANGELOG.md").exists(), \
        f"Nie znaleziono repo root w {root}. Uruchom testy z poziomu repozytorium."
    return root


class TestRealData:
    """Testy z prawdziwymi danymi z repozytorium."""

    def test_sqlite_docs_count(self, repo_root):
        """Obszar SQLite powinien mieć >100 katalogów."""
        docs = load_knowledge_index(root=str(repo_root))
        assert len(docs) > 100, f"Expected >100 SQLite docs, got {len(docs)}"

    def test_sqlite_doc_ids_prefix(self, repo_root):
        """Doc IDs w obszarze SQLite powinny zaczynać się od DOC-SQLITE."""
        docs = load_knowledge_index(root=str(repo_root))
        sqlite_docs = [d for d in docs if d["doc_id"].startswith("DOC-SQLITE")]
        assert len(sqlite_docs) > 0, "Brak dokumentów z prefiksem DOC-SQLITE"

    def test_sqlite_wal_topics_present(self, repo_root):
        """Powinna być przynajmniej jedna notatka o WAL/checkpointing."""
        from ishkarim_sqlite.utils import read_work_md
        docs = load_knowledge_index(root=str(repo_root))
        wal_found = False
        for doc in docs:
            if "wal" in doc["name"].lower() or "checkpoint" in doc["name"].lower():
                wal_found = True
                break
        assert wal_found, "Brak katalogów z temtyką WAL/checkpoint"


class TestModuleIntegrity:
    """Weryfikuje integralność modułu jako pakietu."""

    def test_version_format(self):
        assert re.match(r"\d+\.\d+\.\d+", ishkarim_sqlite.__version__)

    def test_modules_all_strings(self):
        for name in ishkarim_sqlite.MODULES:
            assert isinstance(name, str), f"MODULES entry not a string: {name!r}"
            assert name, "Empty module name found"

    def test_load_returns_correct_area(self, repo_root):
        docs = load_knowledge_index(root=str(repo_root))
        for doc in docs[:5]:
            assert doc["area"] == "sqlite"

    def test_tags_parseable(self, repo_root):
        """Pliki TAGS.md powinny być parsowalny przez extract_tags."""
        from ishkarim_sqlite.utils import extract_tags
        docs = load_knowledge_index(root=str(repo_root))
        errors = []
        for doc in docs[:10]:
            tags = extract_tags(Path(str(repo_root)) / doc["name"])
            if not tags:
                errors.append(doc["name"])
        assert len(errors) < 5, f"Zbyt wiele błędów parsowania TAGS.md: {errors}"

    def test_work_md_readable(self, repo_root):
        """Pliki WORK.md powinny być czytelne dla przynajmniej 80% katalogów."""
        from ishkarim_sqlite.utils import read_work_md
        docs = load_knowledge_index(root=str(repo_root))
        readable = 0
        for doc in docs[:20]:
            content = read_work_md(Path(str(repo_root)) / doc["name"])
            if content:
                readable += 1
        assert readable >= min(14, max(1, int(len(docs) * 0.5))), f"Tylko {readable}/{min(20, len(docs))} plików WORK.md czytelnych"


import re
