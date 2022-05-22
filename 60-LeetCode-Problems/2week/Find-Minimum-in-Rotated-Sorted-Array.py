from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            if nums[lo] < nums[hi]:
                return nums[lo]
            mid = (lo + hi) // 2

            if nums[lo] <= nums[mid]:
                lo = mid + 1
            else:
                hi = mid

        return nums[lo]
