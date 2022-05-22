from typing import List, Union


class Solution:
    def nextPermutation(self, nums: List[int]) -> Union[List[int], None]:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) <= 1:
            return nums

        isMP = False
        suffix = len(nums) - 1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] >= nums[i]:
                if i == 1:
                    isMP = True
                continue
            suffix = i
            break

        if isMP:
            nums.reverse()
            return None

        p = len(nums) - 1
        while nums[suffix - 1] >= nums[p]:
            p -= 1

        nums[p], nums[suffix - 1] = nums[suffix - 1], nums[p]
        nums[suffix:] = nums[len(nums) - 1:suffix - 1:-1]
        return nums
