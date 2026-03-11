"""
checkpoint.py — fragmenty kodu z WORK.md dla obszaru sqlite.

UWAGA: To są fragmenty referencyjne wyekstrahowane z notatek badawczych.
Mogą wymagać dostosowania przed użyciem w produkcji.

Zawiera 1 fragmentów. Każdy poprzedzony komentarzem ze źródłem.
"""
# ruff: noqa
# type: ignore
from __future__ import annotations

# Source: LangGraph Checkpoint 4.0.0: duża aktualizacja
# Minimalny dual-read adapter (schemat)
class DualReadCheckpointer:
    def get_tuple(self, config):
        try:
            return self.v4_saver.get_tuple(config)
        except IncompatibleSchemaError:
            return self.v3_saver.get_tuple(config)
    
    def put(self, config, checkpoint, metadata, new_versions):
        # Zawsze zapisuj do v4
        return self.v4_saver.put(config, checkpoint, metadata, new_versions)
