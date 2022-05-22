from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        lo, hi = max(weights), sum(weights)

        while lo < hi:

            mid = (lo + hi) // 2

            cnt = 0
            level = mid
            for w in weights:

                if level - w < 0:
                    cnt += 1
                    level = mid - w
                else:
                    level -= w

            if cnt < days:
                hi = mid
            else:
                lo = mid + 1

        return lo
