import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement combinationSum3")


@pytest.mark.parametrize("k,n,expected", [
    (3, 7, [[1, 2, 4]]),
    (3, 9, [[1, 2, 6], [1, 3, 5], [2, 3, 4]]),
    (4, 1, [])
])
def test_combinationSum3(k,n, expected):
    got = Solution().combinationSum3(k,n)
    assert sorted(sorted(x) for x in got) == sorted(sorted(x) for x in expected)
