import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement minCostClimbingStairs")


@pytest.mark.parametrize("cost,expected", [
    ([10, 15, 20], 15),
    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6)
])
def test_minCostClimbingStairs(cost, expected):
    assert Solution().minCostClimbingStairs(cost) == expected
