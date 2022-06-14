from typing import List


def moon_travel(_area: List[str]) -> None:
    area = [list(map(int, row.split())) for row in _area]
    answer = float('inf')
    width = len(area[0])
    height = len(area)
    res = []

    def move(weight: int, x: int, y: int, result: int):
        nonlocal area, answer, width, height
        if not (0 <= y < width):
            return
        if height <= x:
            res.append(result)
            return

        for w in [-1, 0, 1]:
            if w == weight:
                continue
            move(w, x + 1, y + w, result + area[x][y])

    for i in range(len(area[0])):
        move(2, 0, i, 0)
    print(min(res))
