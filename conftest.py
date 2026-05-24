"""Per-problem `from solution import ...` shim.

Every problem folder has its own `solution.py`. To let each `test_solution.py`
import its own `solution` module without packaging boilerplate, we hook into
pytest's module-collection phase: just before pytest imports a `test_solution.py`,
we (1) make the test's parent directory the front of `sys.path`, and (2) evict
any cached `solution` module so the next `from solution import ...` re-resolves
against the right folder.
"""
import sys
from pathlib import Path


def pytest_collectstart(collector):
    if collector.__class__.__name__ != "Module":
        return
    path = getattr(collector, "path", None) or getattr(collector, "fspath", None)
    if path is None:
        return
    test_file = Path(str(path))
    if test_file.name != "test_solution.py":
        return

    parent = str(test_file.parent)
    while parent in sys.path:
        sys.path.remove(parent)
    sys.path.insert(0, parent)
    sys.modules.pop("solution", None)
