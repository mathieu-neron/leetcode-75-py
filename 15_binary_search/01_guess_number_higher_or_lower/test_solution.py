import pytest
from solution import Solution
import solution as _sol

pytestmark = pytest.mark.skip(reason="TODO: implement ")


@pytest.mark.parametrize("n,pick", [
    (10, 6),
    (1, 1),
    (2, 1)
])
def test_guessNumber(monkeypatch, n, pick):
    def fake_guess(num):
        if num == pick: return 0
        return -1 if pick < num else 1
    monkeypatch.setattr(_sol, 'guess', fake_guess)
    assert Solution().guessNumber(n) == pick
