import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement countBits")


@pytest.mark.parametrize("n,expected", [
    (2, [0, 1, 1]),
    (5, [0, 1, 1, 2, 1, 2])
])
def test_countBits(n, expected):
    assert Solution().countBits(n) == expected
