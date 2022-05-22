from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [[] for _ in range(2000)]

        def search(cur, lev):
            if not cur:
                return

            res[lev].append(cur.val)
            search(cur.left, lev + 1)
            search(cur.right, lev + 1)

        search(root, 0)
        return list(filter(lambda x: x, res))
