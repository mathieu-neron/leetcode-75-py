import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement minEatingSpeed")


@pytest.mark.parametrize("piles,h,expected", [
    ([3, 6, 7, 11], 8, 4),
    ([30, 11, 23, 4, 20], 5, 30),
    ([30, 11, 23, 4, 20], 6, 23)
])
def test_minEatingSpeed(piles,h, expected):
    assert Solution().minEatingSpeed(piles,h) == expected
