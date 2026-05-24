import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement gcdOfStrings")


@pytest.mark.parametrize("str1,str2,expected", [
    ('ABCABC', 'ABC', 'ABC'),
    ('ABABAB', 'ABAB', 'AB'),
    ('LEET', 'CODE', '')
])
def test_gcdOfStrings(str1,str2, expected):
    assert Solution().gcdOfStrings(str1,str2) == expected
