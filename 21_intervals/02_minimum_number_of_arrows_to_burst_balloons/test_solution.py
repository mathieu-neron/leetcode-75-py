import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement findMinArrowShots")


@pytest.mark.parametrize("points,expected", [
    ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
    ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
    ([[1, 2], [2, 3], [3, 4], [4, 5]], 2)
])
def test_findMinArrowShots(points, expected):
    assert Solution().findMinArrowShots(points) == expected
