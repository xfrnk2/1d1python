import sys
from collections import deque

input = sys.stdin.readline


def break_wall_and_move(n: int, m: int, matrix) -> None:
    def solve(n: int, m: int) -> int:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
        visited[0][0][0] = 1
        queue: deque = deque()
        queue.append((0, 0, 0))
        while queue:
            x, y, c = queue.popleft()

            if x == n - 1 and y == m - 1:
                return visited[x][y][c]

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 > nx or nx >= n or 0 > ny or ny >= m:
                    continue

                if matrix[nx][ny] == 1 and c == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))

                elif matrix[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    visited[nx][ny][c] = visited[x][y][c] + 1
                    queue.append((nx, ny, c))
        return -1

    print(solve(n, m))
