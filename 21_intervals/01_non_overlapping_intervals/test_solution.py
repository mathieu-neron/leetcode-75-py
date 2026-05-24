import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement eraseOverlapIntervals")


@pytest.mark.parametrize("intervals,expected", [
    ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
    ([[1, 2], [1, 2], [1, 2]], 2),
    ([[1, 2], [2, 3]], 0)
])
def test_eraseOverlapIntervals(intervals, expected):
    assert Solution().eraseOverlapIntervals(intervals) == expected
