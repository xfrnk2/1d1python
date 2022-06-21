from typing import List


def rotate(n: int, m: int, array: List[List[int]]) -> List[List[int]]:
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    nn, nm = n - 1, m - 1
    direction = 0

    vertical_direction = [0, 2]
    x, y = 0, 0

    while 0 < nn and 0 < nm:

        prev_num = array[x][y]

        while direction < 4:
            if direction in vertical_direction:
                count = nn
            else:
                count = nm
            for i in range(count):
                nx = x + dx[direction]
                ny = y + dy[direction]
                array[nx][ny], prev_num = prev_num, array[nx][ny]
                x, y = nx, ny
                print(array)

            direction += 1

        nn -= 2
        nm -= 2
        x += 1
        y += 1

        direction = 0

    return array


def array_rotation(n: int, m: int, r: int, array: List[List[int]]) -> List[List[int]]:
    for _ in range(r):
        rotate(n, m, array)
    return array
