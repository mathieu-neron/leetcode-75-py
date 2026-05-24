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

pytestmark = pytest.mark.skip(reason="TODO: implement searchBST")


@pytest.mark.parametrize("tree,val,expected", [
    ([4, 2, 7, 1, 3], 2, [2, 1, 3]),
    ([4, 2, 7, 1, 3], 5, [])
])
def test_searchBST(tree, val, expected):
    got = Solution().searchBST(build_tree(tree), val)
    assert inorder(got) == expected
