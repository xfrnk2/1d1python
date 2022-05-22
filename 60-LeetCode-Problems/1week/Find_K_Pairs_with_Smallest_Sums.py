import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        res = []
        heap = []
        for i in range(len(nums2)):
            heapq.heappush(heap, (nums1[0] + nums2[i], 0, i))

        while len(res) < k and heap:
            v, n1, n2 = heapq.heappop(heap)
            res.append([nums1[n1], nums2[n2]])
            if len(nums1) > n1 + 1:
                heapq.heappush(heap, (nums1[n1 + 1] + nums2[n2], n1 + 1, n2))
        return res
