from collections import deque
from typing import List


def check_is_ripe(n: int, m: int, box: List[List[int]]) -> bool:
    for i in range(m):
        for j in range(n):
            if box[i][j] == -1:
                continue
            if box[i][j] == 0:
                return False
    return True


def work(n: int, m: int, tomato_points: deque, box: List[List[int]]) -> int:
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited = [[0 for _ in range(n)] for _ in range(m)]
    answer = 0
    while tomato_points:
        r, c, num = tomato_points.popleft()

        visited[r][c] = 1
        answer = num
        for i in range(4):
            nx, ny = dx[i] + r, dy[i] + c
            if nx < 0 or m <= nx or ny < 0 or n <= ny or box[nx][ny] == -1 or box[nx][ny] == 1:
                continue
            box[nx][ny] = 1
            tomato_points.append((nx, ny, num + 1))
    return answer


def tomato(n: int, m: int, box: List[List[int]]) -> int:
    tomato_points = deque([])
    tomato_status = []

    for row in range(m):
        for col in range(n):
            now = box[row][col]
            if now == -1:
                continue
            tomato_status.append(now)
            if box[row][col] == 1:
                tomato_points.append((row, col, 0))

    if len(set(tomato_status)) == 1:
        if tomato_status[0] == 1:
            return 0
        else:
            return -1

    answer = work(n, m, tomato_points, box)
    if not check_is_ripe(n, m, box):
        return -1
    return answer
