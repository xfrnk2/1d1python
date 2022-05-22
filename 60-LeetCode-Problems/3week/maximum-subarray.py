from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        d = [0] * len(nums)

        d[0] = nums[0]
        for i in range(1, len(nums)):
            total = nums[i] + d[i - 1]
            if total > nums[i]:
                d[i] = total
            else:
                d[i] = nums[i]
        return max(d)
