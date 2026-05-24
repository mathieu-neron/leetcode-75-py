import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement maxArea")


@pytest.mark.parametrize("height,expected", [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1)
])
def test_maxArea(height, expected):
    assert Solution().maxArea(height) == expected
