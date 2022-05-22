from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        t = [0] * len(prices) + [0]
        t[0] = prices[0]
        m = t[0]

        for i in range(len(prices)):
            m = min(m, prices[i])
            if m < prices[i]:
                t[i] = prices[i] - m

        print(t)

        return max(t[1:])
