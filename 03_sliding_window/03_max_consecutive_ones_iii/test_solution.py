import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement longestOnes")


@pytest.mark.parametrize("nums,k,expected", [
    ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6),
    ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3, 10)
])
def test_longestOnes(nums,k, expected):
    assert Solution().longestOnes(nums,k) == expected
