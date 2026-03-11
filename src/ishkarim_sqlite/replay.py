"""
replay.py — kod wyekstrahowany z WORK.md dla obszaru sqlite.

Zawiera 1 fragmentów kodu. Każdy fragment poprzedzony komentarzem
z nazwą katalogu-źródła.
"""
from __future__ import annotations



# ────────────────────────────────────────────────────────────# Source: Zasada ‘pytaj tylko gdy utkniesz’
# Deterministyczny zegar w testach
store = ReplayStore(db_path, time_fn=lambda: fake_ts)

# Scoring: suma ważona (nie ML)
score = debt_trend*0.30 + retry_pressure*0.25 + dominant_error*0.20 \
      + planned_pressure*0.05 - idle_penalty*0.05 - flapping_pen*0.20
ask = score >= 0.65
