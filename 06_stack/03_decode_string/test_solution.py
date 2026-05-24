import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement decodeString")


@pytest.mark.parametrize("s,expected", [
    ('3[a]2[bc]', 'aaabcbc'),
    ('3[a2[c]]', 'accaccacc'),
    ('2[abc]3[cd]ef', 'abcabccdcdcdef')
])
def test_decodeString(s, expected):
    assert Solution().decodeString(s) == expected
