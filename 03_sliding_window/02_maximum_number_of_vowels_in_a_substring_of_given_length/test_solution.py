import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement maxVowels")


@pytest.mark.parametrize("s,k,expected", [
    ('abciiidef', 3, 3),
    ('aeiou', 2, 2),
    ('leetcode', 3, 2)
])
def test_maxVowels(s,k, expected):
    assert Solution().maxVowels(s,k) == expected
