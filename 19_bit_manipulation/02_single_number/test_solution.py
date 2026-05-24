import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement singleNumber")


@pytest.mark.parametrize("nums,expected", [
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4),
    ([1], 1)
])
def test_singleNumber(nums, expected):
    assert Solution().singleNumber(nums) == expected
