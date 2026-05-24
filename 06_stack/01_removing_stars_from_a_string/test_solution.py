import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement removeStars")


@pytest.mark.parametrize("s,expected", [
    ('leet**cod*e', 'lecoe'),
    ('erase*****', '')
])
def test_removeStars(s, expected):
    assert Solution().removeStars(s) == expected
