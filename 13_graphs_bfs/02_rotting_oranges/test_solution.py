import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement orangesRotting")


@pytest.mark.parametrize("grid,expected", [
    ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
    ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
    ([[0, 2]], 0)
])
def test_orangesRotting(grid, expected):
    assert Solution().orangesRotting(grid) == expected
