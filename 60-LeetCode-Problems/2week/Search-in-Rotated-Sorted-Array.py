class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        
        min_idx = nums.index(min(nums))
        numbers = nums[min_idx:] + nums[:min_idx]
       
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = (lo + hi)//2
            print(mid)
            if numbers[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return nums.index(numbers[lo])