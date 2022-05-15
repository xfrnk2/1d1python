class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]

        for num in nums:
            for y in range(len(subsets)):
                subsets.append(subsets[y]+[num])
        print(subsets)
        return subsets