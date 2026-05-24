import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement closeStrings")


@pytest.mark.parametrize("word1,word2,expected", [
    ('abc', 'bca', True),
    ('a', 'aa', False),
    ('cabbba', 'abbccc', True)
])
def test_closeStrings(word1,word2, expected):
    assert Solution().closeStrings(word1,word2) == expected
