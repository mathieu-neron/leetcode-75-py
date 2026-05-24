import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement minDistance")


@pytest.mark.parametrize("word1,word2,expected", [
    ('horse', 'ros', 3),
    ('intention', 'execution', 5)
])
def test_minDistance(word1,word2, expected):
    assert Solution().minDistance(word1,word2) == expected
