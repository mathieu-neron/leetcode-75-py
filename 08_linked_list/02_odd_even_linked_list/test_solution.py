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

pytestmark = pytest.mark.skip(reason="TODO: implement oddEvenList")


@pytest.mark.parametrize("head,expected", [
    ([1, 2, 3, 4, 5], [1, 3, 5, 2, 4]),
    ([2, 1, 3, 5, 6, 4, 7], [2, 3, 6, 7, 1, 5, 4])
])
def test_oddEvenList(head, expected):
    got = Solution().oddEvenList(build_list(head))
    assert list_to_arr(got) == expected
