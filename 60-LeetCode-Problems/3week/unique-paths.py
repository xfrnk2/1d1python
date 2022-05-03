class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        t = [[1] * n for _ in range(m)]
        
        
        for i in range(1, m):
            for j in range(1, n):
                
                t[i][j] = t[i-1][j] + t[i][j-1]
        return t[-1][-1]