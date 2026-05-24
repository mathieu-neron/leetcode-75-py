import pytest
from solution import SmallestInfiniteSet

pytestmark = pytest.mark.skip(reason="TODO: implement SmallestInfiniteSet")


def test_smallestinfiniteset():
    obj = SmallestInfiniteSet()
    obj.addBack(2)
    assert obj.popSmallest() == 1
    assert obj.popSmallest() == 2
    assert obj.popSmallest() == 3
    obj.addBack(1)
    assert obj.popSmallest() == 1
    assert obj.popSmallest() == 4
    assert obj.popSmallest() == 5
