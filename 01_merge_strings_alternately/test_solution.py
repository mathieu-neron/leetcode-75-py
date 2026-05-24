import pytest
from solution import Solution


@pytest.mark.parametrize(
    "word1,word2,expected",
    [
        ("abc", "pqr", "apbqcr"),
        ("ab", "pqrs", "apbqrs"),
        ("abcd", "pq", "apbqcd"),
        ("", "xyz", "xyz"),
        ("xyz", "", "xyz"),
    ],
)
def test_merge_alternately(word1, word2, expected):
    assert Solution().mergeAlternately(word1, word2) == expected
