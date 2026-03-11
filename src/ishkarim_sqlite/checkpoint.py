"""
checkpoint.py — kod wyekstrahowany z WORK.md dla obszaru sqlite.

Zawiera 1 fragmentów kodu. Każdy fragment poprzedzony komentarzem
z nazwą katalogu-źródła.
"""
from __future__ import annotations



# ────────────────────────────────────────────────────────────# Source: LangGraph Checkpoint 4.0.0: duża aktualizacja
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
