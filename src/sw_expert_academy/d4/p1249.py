from collections import deque
from typing import Any, List


def supply_furnace(n: int, field: List[List[int]]) -> Any:
    visit = [[float('inf')] * n for _ in range(n)]
    visit[0][0] = 0

    queue = deque([(0, 0)])

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or n <= nx or ny < 0 or n <= ny:
                continue
            if visit[x][y] + field[nx][ny] < visit[nx][ny]:
                visit[nx][ny] = visit[x][y] + field[nx][ny]
                queue.append((nx, ny))

    return visit[-1][-1]
