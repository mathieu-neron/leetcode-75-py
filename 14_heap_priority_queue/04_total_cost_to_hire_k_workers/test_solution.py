import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement totalCost")


@pytest.mark.parametrize("costs,k,candidates,expected", [
    ([17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4, 11),
    ([1, 2, 4, 1], 3, 3, 4)
])
def test_totalCost(costs,k,candidates, expected):
    assert Solution().totalCost(costs,k,candidates) == expected
