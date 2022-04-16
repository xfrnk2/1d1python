# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        def search_tree (node, depth):
            
            if not node.left and not node.right:
                return depth
            
            l = r = 0
            
            if node.left:
                l = rec(node.left, depth + 1)
            if node.right:
                r = rec(node.right, depth + 1)
            
            return max(l, r)
        
        return search_tree(root, 1)