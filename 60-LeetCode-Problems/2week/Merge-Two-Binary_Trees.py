from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> Optional[TreeNode]:
        # // root * depth -1, 0
        # if root1 and not root2:
        #     return root1
        # elif root2 and not root1:
        #     return root2
        # elif not root1 and not root2:
        #     return
        r = TreeNode(root1.val + root2.val)
        p1 = root1
        p2 = root2

        # def cal(a, b):
        #     result = None
        #     if a and b:
        #         result =  a.val + b.val
        #     elif a and not b:
        #         result = a.val
        #     elif not a and b:
        #         result = b.val
        #     return result

        def setTree(aa, bb):
            # v = cal(aa, bb)
            # if v is None:
            #     return
            # return TreeNode(v)
            return None  # temporary value

        def solution(r, a1, a2):

            a1_left_next = a2_left_next = None
            if a1:
                a1_left_next = a1.left
            if a2:
                a2_left_next = a2.left

            a1_right_next = a2_right_next = None
            if a1:
                a1_right_next = a1.right
            if a2:
                a2_right_next = a2.right

            v1 = setTree(a1_left_next, a2_left_next)
            v2 = setTree(a1_right_next, a2_right_next)

            if v1:
                r.left = v1
                solution(r.left, a1_left_next, a2_left_next)
            if v2:
                r.right = v2
                solution(r.right, a1_right_next, a2_right_next)

        solution(r, p1, p2)
        return r
