import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement maxOperations")


@pytest.mark.parametrize("nums,k,expected", [
    ([1, 2, 3, 4], 5, 2),
    ([3, 1, 3, 4, 3], 6, 1)
])
def test_maxOperations(nums,k, expected):
    assert Solution().maxOperations(nums,k) == expected
