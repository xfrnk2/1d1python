class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        d = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    d[i] = max(d[i], d[j] + 1)

        return max(d)

# 잘못 접근한 방법 // why? 합의 연속성이 보장되지 못하기 때문이다
#         if len(nums) < 2:
#             return 1
#         d = [(nums[0], 1)]
#         if nums[0] < nums[1]:
#             d.append((nums[1], 2))
#         else:
#             d.append((nums[1], 1))
        
#         for i in range(2, len(nums)):
            
#             b = max([x[1] for x in d[:-1]])

#             if d[-1][0] < nums[i]:
#                 d.append((nums[i], d[-1][1] + 1))

#             elif d[-1][0] > nums[i] and d[-2][0] < nums[i]:
#                 d.append((nums[i], b + 1))
              
#             elif min([x[0] for x in d]) > nums[i]:
#                 d.append((nums[i], 1))
#                

#         return d[-1][-1]