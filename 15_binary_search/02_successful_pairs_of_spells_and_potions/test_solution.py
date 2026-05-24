import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement successfulPairs")


@pytest.mark.parametrize("spells,potions,success,expected", [
    ([5, 1, 3], [1, 2, 3, 4, 5], 7, [4, 0, 3]),
    ([3, 1, 2], [8, 5, 8], 16, [2, 0, 2])
])
def test_successfulPairs(spells,potions,success, expected):
    assert Solution().successfulPairs(spells,potions,success) == expected
