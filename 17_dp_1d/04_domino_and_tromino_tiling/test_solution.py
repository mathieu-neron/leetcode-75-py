import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement numTilings")


@pytest.mark.parametrize("n,expected", [
    (3, 5),
    (1, 1),
    (4, 11)
])
def test_numTilings(n, expected):
    assert Solution().numTilings(n) == expected
