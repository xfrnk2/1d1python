# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def search(cur, lo, hi):
            if not cur:
                return True
            if not lo < cur.val < hi:
                return False
            return search(cur.left, lo, cur.val) and search(cur.right, cur.val, hi)
            
        return search(root, float('-inf'), float('inf'))