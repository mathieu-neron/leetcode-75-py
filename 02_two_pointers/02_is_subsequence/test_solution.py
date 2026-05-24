import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement isSubsequence")


@pytest.mark.parametrize("s,t,expected", [
    ('abc', 'ahbgdc', True),
    ('axc', 'ahbgdc', False)
])
def test_isSubsequence(s,t, expected):
    assert Solution().isSubsequence(s,t) == expected
