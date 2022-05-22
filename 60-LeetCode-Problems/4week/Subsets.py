from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets: List[List[int]] = [[]]

        for num in nums:
            for y in range(len(subsets)):
                subsets.append(subsets[y] + [num])
        return subsets
