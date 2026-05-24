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

pytestmark = pytest.mark.skip(reason="TODO: implement reverseList")


@pytest.mark.parametrize("head,expected", [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([1, 2], [2, 1]),
    ([], [])
])
def test_reverseList(head, expected):
    got = Solution().reverseList(build_list(head))
    assert list_to_arr(got) == expected
