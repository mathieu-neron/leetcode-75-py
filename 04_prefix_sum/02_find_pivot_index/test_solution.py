import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement pivotIndex")


@pytest.mark.parametrize("nums,expected", [
    ([1, 7, 3, 6, 5, 6], 3),
    ([1, 2, 3], -1),
    ([2, 1, -1], 0)
])
def test_pivotIndex(nums, expected):
    assert Solution().pivotIndex(nums) == expected
