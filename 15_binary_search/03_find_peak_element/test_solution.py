import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement findPeakElement")


@pytest.mark.parametrize("nums", [
    ([1, 2, 3, 1],),
    ([1, 2, 1, 3, 5, 6, 4],),
    ([1],)
])
def test_findPeakElement(nums):
    i = Solution().findPeakElement(nums)
    assert 0 <= i < len(nums)
    if i > 0:
        assert nums[i] > nums[i-1]
    if i < len(nums) - 1:
        assert nums[i] > nums[i+1]
