import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement calcEquation")


@pytest.mark.parametrize("equations,values,queries,expected", [
    ([['a', 'b'], ['b', 'c']], [2.0, 3.0], [['a', 'c'], ['b', 'a'], ['a', 'e'], ['a', 'a'], ['x', 'x']], [6.0, 0.5, -1.0, 1.0, -1.0])
])
def test_calcEquation(equations,values,queries, expected):
    assert Solution().calcEquation(equations,values,queries) == pytest.approx(expected)
