from collections import deque
from typing import List


def maze(field: List[str]):
    size = 16
    start = end = None
    visit = [[0] * size for _ in range(size)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(size):
        for j in range(size):
            if field[i][j] == "2":
                start = (i, j)
            if field[i][j] == "3":
                end = (i, j)

    q = deque([start])

    while q:
        x, y = q.pop()  # type: ignore
        visit[x][y] = 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or size <= nx or ny < 0 or size <= ny or visit[nx][ny] == 1:
                continue

            if end == (nx, ny):
                return 1

            if field[nx][ny] == "0":
                q.append((nx, ny))
    return 0
