import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement largestAltitude")


@pytest.mark.parametrize("gain,expected", [
    ([-5, 1, 5, 0, -7], 1),
    ([-4, -3, -2, -1, 4, 3, 2], 0)
])
def test_largestAltitude(gain, expected):
    assert Solution().largestAltitude(gain) == expected
