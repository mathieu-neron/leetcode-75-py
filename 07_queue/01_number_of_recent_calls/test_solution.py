import pytest
from solution import RecentCounter

pytestmark = pytest.mark.skip(reason="TODO: implement RecentCounter")


def test_recentcounter():
    obj = RecentCounter()
    assert obj.ping(1) == 1
    assert obj.ping(100) == 2
    assert obj.ping(3001) == 3
    assert obj.ping(3002) == 3
