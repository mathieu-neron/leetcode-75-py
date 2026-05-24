import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement compress")


@pytest.mark.parametrize("chars,want_len,want_prefix", [
    (['a', 'a', 'b', 'b', 'c', 'c', 'c'], 6, ['a', '2', 'b', '2', 'c', '3']),
    (['a'], 1, ['a']),
    (['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'], 4, ['a', 'b', '1', '2'])
])
def test_compress(chars, want_len, want_prefix):
    got_len = Solution().compress(chars)
    assert got_len == want_len
    assert chars[:got_len] == want_prefix
