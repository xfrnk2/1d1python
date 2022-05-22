from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        def backtrack(low, r, nums):
            if low == r:
                return result.append(list(nums))  # We reached the end of the recursion
                # tree
            else:
                for i in range(low, r + 1):
                    nums[low], nums[i] = nums[i], nums[low]
                    backtrack(low + 1, r, nums)
                    nums[i], nums[low] = nums[low], nums[i]

        backtrack(0, n - 1, nums)
        return result
