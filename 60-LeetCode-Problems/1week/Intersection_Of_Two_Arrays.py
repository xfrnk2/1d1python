from typing import List, Set


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> Set[int]:
        return set(nums1).intersection(nums2)
