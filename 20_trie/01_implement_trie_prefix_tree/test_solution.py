import pytest
from solution import Trie

pytestmark = pytest.mark.skip(reason="TODO: implement Trie")


def test_trie():
    obj = Trie()
    obj.insert('apple')
    assert obj.search('apple') == True
    assert obj.search('app') == False
    assert obj.startsWith('app') == True
    obj.insert('app')
    assert obj.search('app') == True
