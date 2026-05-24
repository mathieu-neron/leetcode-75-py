import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement equalPairs")


@pytest.mark.parametrize("grid,expected", [
    ([[3, 2, 1], [1, 7, 6], [2, 7, 7]], 1),
    ([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]], 3)
])
def test_equalPairs(grid, expected):
    assert Solution().equalPairs(grid) == expected
