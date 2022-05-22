from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        row_len = len(grid)
        col_len = len(grid[0])
        cnt = 0

        def visit(x, y):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or row_len <= nx or col_len <= ny:
                    continue

                if grid[nx][ny] == "1":
                    grid[nx][ny] = "2"
                    visit(nx, ny)

        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == "1":
                    cnt += 1
                    grid[row][col] = "2"
                    visit(row, col)
        return cnt
