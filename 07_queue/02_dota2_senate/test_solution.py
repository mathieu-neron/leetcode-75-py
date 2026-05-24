import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement predictPartyVictory")


@pytest.mark.parametrize("senate,expected", [
    ('RD', 'Radiant'),
    ('RDD', 'Dire')
])
def test_predictPartyVictory(senate, expected):
    assert Solution().predictPartyVictory(senate) == expected
