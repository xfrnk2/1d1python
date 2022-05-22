from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 3:
            return max(nums)
        res = 0
        lhs_prev1, lhs_prev2 = nums[1], max(nums[1], nums[2])
        rhs_prev1, rhs_prev2 = nums[0], max(nums[0], nums[1])

        for i in range(3, len(nums)):
            lhs_prev2, lhs_prev1 = max(lhs_prev1 + nums[i], lhs_prev2), lhs_prev2
            rhs_prev2, rhs_prev1 = max(rhs_prev1 + nums[i - 1], rhs_prev2), rhs_prev2
            res = max(res, lhs_prev2, rhs_prev2)

        return res

#
#
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#
#         if len(nums) <= 3:
#             return max(nums)
#         res = 0
#
#         d = [0] * len(nums)
#         d2 = [0] * len(nums)
#
#         d[1], d[2] = nums[1], max(nums[1], nums[2])
#         d2[0], d2[1] = nums[0], max(nums[0], nums[1])
#
#         for i in range(3, len(nums)):
#             d[i] = max(d[i - 2] + nums[i], d[i - 1])
#             d2[i - 1] = max(d2[i - 3] + nums[i - 1], d2[i - 2])
#             res = max(res, d[i], d2[i - 1])
#
#         return res
