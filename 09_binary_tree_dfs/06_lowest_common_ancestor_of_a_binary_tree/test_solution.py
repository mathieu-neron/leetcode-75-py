import pytest
from solution import Solution, TreeNode


def build_tree(arr):
    if not arr or arr[0] is None:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while queue and i < len(arr):
        node = queue.pop(0)
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root


def level_order(root):
    if root is None:
        return []
    out = []
    queue = [root]
    while queue:
        n = queue.pop(0)
        if n is None:
            out.append(None)
            continue
        out.append(n.val)
        queue.append(n.left)
        queue.append(n.right)
    while out and out[-1] is None:
        out.pop()
    return out


def find_node(root, val):
    if root is None:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

pytestmark = pytest.mark.skip(reason="TODO: implement lowestCommonAncestor")


@pytest.mark.parametrize("tree,p,q,expected", [
    ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3),
    ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5),
    ([1, 2], 1, 2, 1)
])
def test_lowestCommonAncestor(tree, p, q, expected):
    root = build_tree(tree)
    pn = find_node(root, p)
    qn = find_node(root, q)
    got = Solution().lowestCommonAncestor(root, pn, qn)
    assert got is not None and got.val == expected
