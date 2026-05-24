import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement increasingTriplet")


@pytest.mark.parametrize("nums,expected", [
    ([1, 2, 3, 4, 5], True),
    ([5, 4, 3, 2, 1], False),
    ([2, 1, 5, 0, 4, 6], True)
])
def test_increasingTriplet(nums, expected):
    assert Solution().increasingTriplet(nums) == expected
