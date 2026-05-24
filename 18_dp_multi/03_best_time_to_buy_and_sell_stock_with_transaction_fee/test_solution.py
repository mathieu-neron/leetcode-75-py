import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement maxProfit")


@pytest.mark.parametrize("prices,fee,expected", [
    ([1, 3, 2, 8, 4, 9], 2, 8),
    ([1, 3, 7, 5, 10, 3], 3, 6)
])
def test_maxProfit(prices,fee, expected):
    assert Solution().maxProfit(prices,fee) == expected
