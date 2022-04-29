# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def search(po, io):
            if not io:
                return
            idx = io.index(po.pop(0))
            cur = TreeNode(io[idx])
            cur.left = search(po, io[0:idx])
            cur.right = search(po, io[idx+1:])
            return cur
            
        return search(preorder, inorder)