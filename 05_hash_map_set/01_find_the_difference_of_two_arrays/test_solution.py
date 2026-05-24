import pytest
from solution import Solution

pytestmark = pytest.mark.skip(reason="TODO: implement findDifference")


@pytest.mark.parametrize("nums1,nums2,expected", [
    ([1, 2, 3], [2, 4, 6], [[1, 3], [4, 6]]),
    ([1, 2, 3, 3], [1, 1, 2, 2], [[3], []])
])
def test_findDifference(nums1,nums2, expected):
    got = Solution().findDifference(nums1,nums2)
    assert sorted(sorted(x) for x in got) == sorted(sorted(x) for x in expected)
