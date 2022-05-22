from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def search_tree(node, depth):
            if not node.left and not node.right:
                return depth

            lhs = rhs = 10e5

            if node.left:
                lhs = search_tree(node.left, depth + 1)
            if node.right:
                rhs = search_tree(node.right, depth + 1)

            return min(lhs, rhs)

        return search_tree(root, 1)
