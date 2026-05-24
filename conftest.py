import sys
from pathlib import Path


def pytest_collection_modifyitems(config, items):
    for item in items:
        sys.path.insert(0, str(Path(item.fspath).parent))
