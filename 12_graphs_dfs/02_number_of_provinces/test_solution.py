import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement findCircleNum")


@pytest.mark.parametrize("isConnected,expected", [
    ([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2),
    ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3)
])
def test_findCircleNum(isConnected, expected):
    assert Solution().findCircleNum(isConnected) == expected
