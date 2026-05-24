import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement asteroidCollision")


@pytest.mark.parametrize("asteroids,expected", [
    ([5, 10, -5], [5, 10]),
    ([8, -8], []),
    ([10, 2, -5], [10]),
    ([-2, -1, 1, 2], [-2, -1, 1, 2])
])
def test_asteroidCollision(asteroids, expected):
    assert Solution().asteroidCollision(asteroids) == expected
