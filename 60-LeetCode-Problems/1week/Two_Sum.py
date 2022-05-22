from typing import List, Union


class Solution:
    def twoSum(self, nums: List[int], target: int) -> Union[List[int], None]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None
