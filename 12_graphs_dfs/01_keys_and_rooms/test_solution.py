import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement canVisitAllRooms")


@pytest.mark.parametrize("rooms,expected", [
    ([[1], [2], [3], []], True),
    ([[1, 3], [3, 0, 1], [2], [0]], False)
])
def test_canVisitAllRooms(rooms, expected):
    assert Solution().canVisitAllRooms(rooms) == expected
