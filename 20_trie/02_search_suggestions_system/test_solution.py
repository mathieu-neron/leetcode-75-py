import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement suggestedProducts")


@pytest.mark.parametrize("products,searchWord,expected", [
    (['mobile', 'mouse', 'moneypot', 'monitor', 'mousepad'], 'mouse', [['mobile', 'moneypot', 'monitor'], ['mobile', 'moneypot', 'monitor'], ['mouse', 'mousepad'], ['mouse', 'mousepad'], ['mouse', 'mousepad']]),
    (['havana'], 'havana', [['havana'], ['havana'], ['havana'], ['havana'], ['havana'], ['havana']])
])
def test_suggestedProducts(products,searchWord, expected):
    assert Solution().suggestedProducts(products,searchWord) == expected
