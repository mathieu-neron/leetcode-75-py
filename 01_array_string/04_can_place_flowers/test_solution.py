import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement canPlaceFlowers")


@pytest.mark.parametrize("flowerbed,n,expected", [
    ([1, 0, 0, 0, 1], 1, True),
    ([1, 0, 0, 0, 1], 2, False)
])
def test_canPlaceFlowers(flowerbed,n, expected):
    assert Solution().canPlaceFlowers(flowerbed,n) == expected
