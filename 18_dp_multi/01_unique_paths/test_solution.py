import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement uniquePaths")


@pytest.mark.parametrize("m,n,expected", [
    (3, 7, 28),
    (3, 2, 3)
])
def test_uniquePaths(m,n, expected):
    assert Solution().uniquePaths(m,n) == expected
