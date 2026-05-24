import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement letterCombinations")


@pytest.mark.parametrize("digits,expected", [
    ('23', ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']),
    ('', []),
    ('2', ['a', 'b', 'c'])
])
def test_letterCombinations(digits, expected):
    assert sorted(Solution().letterCombinations(digits)) == sorted(expected)
