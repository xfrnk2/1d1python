class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums)
        
        
        d = [0] * len(nums)
        d[0] = nums[0]
        d[1] = nums[1]
        
        for i in range(len(nums)):
            for j in range(i-1):
                d[i] = max(d[j] + nums[i], d[i])
        
        return max(d)