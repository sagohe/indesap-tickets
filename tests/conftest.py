from __future__ import annotations

import os
import sys

# Añade la raíz del repo al sys.path para que "app" y "sdk" se puedan importar
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import pytest  # noqa: E402  (import después del sys.path)

from app.storage import store  # noqa: E402


# Resetea el store antes y después de cada test (IDs deterministas)
@pytest.fixture(autouse=True)
def reset_store():
    store._data.clear()
    store._seq = 0
    yield
    store._data.clear()
    store._seq = 0