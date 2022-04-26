# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        
        def search (root, c):
            if not root:
                return
            c += root.val
            if not root.left and not root.right and targetSum == c:
                return True
            return search(root.left, c) or search(root.right, c)
            
        return search(root, 0)