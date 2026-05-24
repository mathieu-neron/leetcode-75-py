import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement longestSubarray")


@pytest.mark.parametrize("nums,expected", [
    ([1, 1, 0, 1], 3),
    ([0, 1, 1, 1, 0, 1, 1, 0, 1], 5),
    ([1, 1, 1], 2)
])
def test_longestSubarray(nums, expected):
    assert Solution().longestSubarray(nums) == expected
