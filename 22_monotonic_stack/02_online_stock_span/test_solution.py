import pytest
from solution import StockSpanner

pytestmark = pytest.mark.skip(reason="TODO: implement StockSpanner")


def test_stockspanner():
    obj = StockSpanner()
    assert obj.next(100) == 1
    assert obj.next(80) == 1
    assert obj.next(60) == 1
    assert obj.next(70) == 2
    assert obj.next(60) == 1
    assert obj.next(75) == 4
    assert obj.next(85) == 6
