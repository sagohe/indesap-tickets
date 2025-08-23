import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from app.storage import store

@pytest.fixture(autouse=True)
def reset_store():
    # antes de cada test
    store._data.clear()
    store._seq = 0
    yield
    # después de cada test (por si algún test deja algo)
    store._data.clear()
    store._seq = 0