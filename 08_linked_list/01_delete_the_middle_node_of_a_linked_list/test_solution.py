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

pytestmark = pytest.mark.skip(reason="TODO: implement deleteMiddle")


@pytest.mark.parametrize("head,expected", [
    ([1, 3, 4, 7, 1, 2, 6], [1, 3, 4, 1, 2, 6]),
    ([1, 2, 3, 4], [1, 2, 4]),
    ([2, 1], [2])
])
def test_deleteMiddle(head, expected):
    got = Solution().deleteMiddle(build_list(head))
    assert list_to_arr(got) == expected
