import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement reverseWords")


@pytest.mark.parametrize("s,expected", [
    ('the sky is blue', 'blue is sky the'),
    ('  hello world  ', 'hello world'),
    ('a good   example', 'example good a')
])
def test_reverseWords(s, expected):
    assert Solution().reverseWords(s) == expected
