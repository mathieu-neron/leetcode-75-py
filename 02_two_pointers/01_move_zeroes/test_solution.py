import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement moveZeroes")


@pytest.mark.parametrize("nums,expected", [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([0], [0])
])
def test_moveZeroes(nums, expected):
    Solution().moveZeroes(nums)
    assert nums == expected
