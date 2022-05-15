class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        arr = []
        self.cal(arr, "", 0, 0, n)
        return arr
    
    def cal(self, arr, cur, opened, closed, n):
        if len(cur) == n * 2:
            arr.append(cur)
            return
        
        if opened < n:
            self.cal(arr, cur + "(", opened + 1, closed, n)
        if opened > closed:
            self.cal(arr, cur + ")", opened, closed + 1, n)
            
        
        
#         1. (, 1, 0 
#         2. ((, 2, 0   // 1
#         3. (((, 3, 0 // 2
#         4. (((), 3, 1 // 2
#         5. ((()), 3, 2 // 3
#         6. ((())), 3, 3 // 4
            
#         7. ((), 2, 1 // 1
#         8. (()(, 3, 1 // 2
              ....