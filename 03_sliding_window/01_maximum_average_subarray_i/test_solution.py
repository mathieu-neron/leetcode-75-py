import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement findMaxAverage")


@pytest.mark.parametrize("nums,k,expected", [
    ([1, 12, -5, -6, 50, 3], 4, 12.75),
    ([5], 1, 5.0)
])
def test_findMaxAverage(nums,k, expected):
    assert Solution().findMaxAverage(nums,k) == pytest.approx(expected)
