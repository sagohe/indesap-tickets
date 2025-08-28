# tests/conftest.py
from __future__ import annotations

import os
import sys
from pathlib import Path

# Inserta la raíz del repo en sys.path ANTES de importar app/sd
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import pytest  # noqa: E402
from app.storage import store  # noqa: E402


# Resetea el store antes y después de cada test (IDs deterministas)
@pytest.fixture(autouse=True)
def reset_store():
    store._data.clear()
    store._seq = 0
    yield
    store._data.clear()
    store._seq = 0
