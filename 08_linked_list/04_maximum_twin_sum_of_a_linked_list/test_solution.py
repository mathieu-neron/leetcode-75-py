import pytest
from solution import Solution, ListNode


def build_list(arr):
    dummy = ListNode()
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def list_to_arr(head):
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out

pytestmark = pytest.mark.skip(reason="TODO: implement pairSum")


@pytest.mark.parametrize("head,expected", [
    ([5, 4, 2, 1], 6),
    ([4, 2, 2, 3], 7),
    ([1, 100000], 100001)
])
def test_pairSum(head, expected):
    got = Solution().pairSum(build_list(head))
    assert got == expected
