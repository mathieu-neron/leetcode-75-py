import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement reverseVowels")


@pytest.mark.parametrize("s,expected", [
    ('IceCreAm', 'AceCreIm'),
    ('leetcode', 'leotcede')
])
def test_reverseVowels(s, expected):
    assert Solution().reverseVowels(s) == expected
