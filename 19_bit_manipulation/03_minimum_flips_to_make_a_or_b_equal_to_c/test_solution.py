import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement minFlips")


@pytest.mark.parametrize("a,b,c,expected", [
    (2, 6, 5, 3),
    (4, 2, 7, 1),
    (1, 2, 3, 0)
])
def test_minFlips(a,b,c, expected):
    assert Solution().minFlips(a,b,c) == expected
