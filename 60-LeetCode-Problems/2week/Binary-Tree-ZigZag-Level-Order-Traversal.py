from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res: List[List[int]] = [[] for _ in range(2000)]

        def search(cur, lev):
            if not cur:
                return
            if lev % 2 == 1:
                res[lev].insert(0, cur.val)
            else:
                res[lev].append(cur.val)
            search(cur.left, lev + 1)
            search(cur.right, lev + 1)

        search(root, 0)
        ans: List[List[int]] = list(filter(lambda x: x, res))
        return ans
