class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
       
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        
        t = [[0] * (n+1) for _ in range(m+1)]
        t[0][1] = 1
                
        for i in range(1, m+1):
            for j in range(1, n+1):
                if obstacleGrid[i-1][j-1] == 1:
                    continue
                t[i][j] = t[i-1][j] + t[i][j-1]
  
        return t[-1][-1]