# import itertools
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
      

#         res = list(map(list, itertools.permutations(nums)))
#         print(res) # 3개의 원소로 수열 만들기
#         return res
        
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        result = []
        def backtrack(l,r,nums) :
            if l==r :
                return result.append(list(nums)) #We reached the end of the recursion
                                                 #tree
            else : 
                for i in range(l,r+1) :
                    nums[l], nums[i] = nums[i], nums[l]
                    backtrack(l+1,r,nums)
                    nums[i],nums[l] = nums[l], nums[i]
        backtrack(0,n-1,nums)
        return result