import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement longestCommonSubsequence")


@pytest.mark.parametrize("text1,text2,expected", [
    ('abcde', 'ace', 3),
    ('abc', 'abc', 3),
    ('abc', 'def', 0)
])
def test_longestCommonSubsequence(text1,text2, expected):
    assert Solution().longestCommonSubsequence(text1,text2) == expected
