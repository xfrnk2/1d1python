from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        acc = [nums[0]]
        for i in nums[1:]:
            acc.append(acc[-1] + i)
        d = {0: 1}

        for i in acc:
            if i - k in d:
                res += d[i - k]
            d[i] = d.get(i, 0) + 1
        return res
