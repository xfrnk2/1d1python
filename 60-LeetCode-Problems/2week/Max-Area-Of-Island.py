from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        row_len = len(grid)
        col_len = len(grid[0])
        max_cnt = 0

        def visit(x, y, cnt):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or row_len <= nx or col_len <= ny:
                    continue

                if grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    cnt = max(cnt, visit(nx, ny, cnt + 1))

            return cnt

        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 1:
                    grid[row][col] = 2
                    max_cnt = max(max_cnt, visit(row, col, 1))
        return max_cnt
