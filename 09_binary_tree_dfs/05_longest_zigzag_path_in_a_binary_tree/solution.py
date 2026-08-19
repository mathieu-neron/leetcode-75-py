# LeetCode 1372: Longest ZigZag Path in a Binary Tree
# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode => None' = None, right: 'TreeNode => None' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        max = 0

        def dfs(node: TreeNode | None, is_left: bool, height: int) -> None:
            if node is None:
                return
            nonlocal max
            max = max(max, height)

            if is_left:
                dfs(node.left, True, 1)
                dfs(node.right, False, height + 1)
            else:
                dfs(node.right, False, 1)
                dfs(node.left, True, height + 1)

        dfs(root, True, 0)
        dfs(root, False, 0)

        return max
