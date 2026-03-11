"""
test_sqlite.py — testy dla modułu ishkarim_sqlite.
"""
import pytest


class TestImport:
    """Weryfikuje, że moduł importuje się poprawnie."""

    def test_import_main(self):
        import ishkarim_sqlite
        assert ishkarim_sqlite.__version__ == "0.1.0"

    def test_area(self):
        import ishkarim_sqlite
        assert ishkarim_sqlite.__area__ == "sqlite"

    def test_modules_list_nonempty(self):
        import ishkarim_sqlite
        assert len(ishkarim_sqlite.MODULES) > 0

    def test_submodule_imports(self):
        from ishkarim_sqlite import utils
        assert utils is not None


class TestKnowledgeIndex:
    """Testuje load_knowledge_index()."""

    def test_returns_list(self, tmp_path):
        import ishkarim_sqlite
        result = ishkarim_sqlite.load_knowledge_index(root=str(tmp_path))
        assert isinstance(result, list)

    def test_record_keys(self, tmp_path):
        import os, ishkarim_sqlite
        # create a minimal fake source dir
        src_dir = tmp_path / ishkarim_sqlite.MODULES[0]
        src_dir.mkdir(parents=True, exist_ok=True)
        (src_dir / "TAGS.md").write_text("doc_id: DOC-TEST-001\nmaturity: draft\n")
        result = ishkarim_sqlite.load_knowledge_index(root=str(tmp_path))
        if result:
            assert set(result[0].keys()) >= {"name", "doc_id", "maturity", "area"}


class TestUtils:
    """Testuje narzędzia pomocnicze."""

    def test_read_work_md_missing(self, tmp_path):
        from ishkarim_sqlite.utils import read_work_md
        assert read_work_md(tmp_path) == ""

    def test_extract_tags_missing(self, tmp_path):
        from ishkarim_sqlite.utils import extract_tags
        assert extract_tags(tmp_path) == {}

    def test_extract_python_blocks(self):
        from ishkarim_sqlite.utils import extract_python_blocks
        md = """```python
def greet():
    return "hello world"

result = greet()
print(result)
```"""
        blocks = extract_python_blocks(md)
        assert len(blocks) == 1
        assert "print" in blocks[0]
