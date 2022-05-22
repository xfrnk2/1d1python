from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        zero = 0

        while idx < len(nums):
            if nums[idx] == 0:
                idx += 1
                continue
            nums[idx], nums[zero] = nums[zero], nums[idx]
            zero += 1
            idx += 1
