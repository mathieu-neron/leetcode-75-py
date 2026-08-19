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


@pytest.mark.parametrize("tree,expected", [
    ([1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1], 3),
    ([1, 1, 1, None, 1, None, None, 1, 1, None, 1], 4),
    ([1], 0)
])
def test_longestZigZag(tree, expected):
    got = Solution().longestZigZag(build_tree(tree))
    assert got == expected
