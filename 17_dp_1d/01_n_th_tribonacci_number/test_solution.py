import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement tribonacci")


@pytest.mark.parametrize("n,expected", [
    (4, 4),
    (25, 1389537),
    (0, 0)
])
def test_tribonacci(n, expected):
    assert Solution().tribonacci(n) == expected
