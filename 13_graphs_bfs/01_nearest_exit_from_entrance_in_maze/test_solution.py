import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement nearestExit")


@pytest.mark.parametrize("maze,entrance,expected", [
    ([['+', '+', '.', '+'], ['.', '.', '.', '+'], ['+', '+', '+', '.']], [1, 2], 1),
    ([['+', '+', '+'], ['.', '.', '.'], ['+', '+', '+']], [1, 0], 2),
    ([['.', '+']], [0, 0], -1)
])
def test_nearestExit(maze,entrance, expected):
    assert Solution().nearestExit(maze,entrance) == expected
