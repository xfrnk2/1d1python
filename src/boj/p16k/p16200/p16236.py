from collections import deque
from typing import Any, List, Tuple

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def get_eatable_fish_coordinates(size: int, field: List[List[int]], distance: List[List[Any]]) -> List[
        Tuple[int, int, int]]:
    n = len(field)
    result = []
    for i in range(n):
        for j in range(n):
            if 0 < field[i][j] < size:
                result.append((i, j, distance[i][j]))
    return result


def check_is_valid_range(n: int, x: int, y: int) -> bool:
    return 0 <= x < n and 0 <= y < n


def get_distance_matrix(size: int, start_x: int, start_y: int, field: List[List[int]]) -> List[List[float]]:
    n = len(field)

    distance = [[float('inf')] * n for _ in range(n)]
    q = deque([(start_x, start_y)])
    distance[start_x][start_y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not check_is_valid_range(n, nx, ny):
                continue
            if size < field[nx][ny]:
                continue

            if distance[nx][ny] > distance[x][y] + 1:
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx, ny))

    return distance


def find_shark(n: int, field: List[List[int]]) -> Tuple[int, int]:
    for i in range(n):
        for j in range(n):
            if field[i][j] == 9:
                return i, j
    return 0, 0


def baby_shark(n: int, field: List[List[int]]) -> int:
    move_count = 0
    start_x, start_y = find_shark(n, field)
    size = 2
    required_fish = size

    field[start_x][start_y] = 0

    while True:

        distance = get_distance_matrix(size, start_x, start_y, field)
        targets = get_eatable_fish_coordinates(size, field, distance)

        if not targets:
            break

        targets.sort(key=lambda x: (x[2], x[0], x[1]))
        start_x, start_y = targets[0][0], targets[0][1]
        move_count += targets[0][2]
        field[start_x][start_y] = 0
        required_fish -= 1
        if required_fish <= 0:
            size += 1
            required_fish = size

    return move_count
