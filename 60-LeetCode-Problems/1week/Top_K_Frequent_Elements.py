import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        d = dict()

        for i in nums:
            d[i] = d.get(i, 0) + 1

        counts = [(value, key) for key, value in d.items()]
        heap = []
        for value, key in counts:
            heapq.heappush(heap, (-value, key))

        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res


'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        d = dict()

        for i in nums:
            d[i] = d.get(i, 0) + 1

        return heapq.nlargest(k, d, d.get)
'''
