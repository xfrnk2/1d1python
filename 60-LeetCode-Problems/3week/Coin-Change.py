from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins = sorted(coins)
        inf = float('inf')

        d = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        for j in range(1, amount + 1):
            d[0][j] = inf

        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] <= j:
                    d[i][j] = min(d[i][j - coins[i - 1]] + 1, d[i - 1][j])
                else:
                    d[i][j] = d[i - 1][j]

        res = d[-1][-1]
        if res == inf:
            return -1
        return res
