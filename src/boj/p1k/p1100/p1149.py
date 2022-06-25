from typing import List


def rgb_distance(n: int, _colors: List[List[int]]) -> None:
    """
    1번집을 고정했을때
    1. 1번집 색깔이 R, 2번집 색깔이 B
    2. 1번집 색깔이 R, 2번집 색깔이 G
    3. 1번집 색깔이 G, 2번집 색깔이 B
    4. 1번집 색깔이 G, 2번집 색깔이 R
    5. 1번집 색깔이 B, 2번집 색깔이 R
    6. 1번집 색깔이 B, 2번집 색깔이 G
    """

    colors = [[0, 0, 0]] + _colors
    answer = 1e9

    for start in range(3):
        d = [[0] * 3 for _ in range(n + 1)]
        for j in range(3):
            if start == j:
                d[1][start] = colors[1][start]
            else:
                d[1][j] = 1001
        for k in range(2, n + 1):
            d[k][0] = min(d[k - 1][1], d[k - 1][2]) + colors[k][0]
            d[k][1] = min(d[k - 1][0], d[k - 1][2]) + colors[k][1]
            d[k][2] = min(d[k - 1][0], d[k - 1][1]) + colors[k][2]

        answer = min(answer, d[n][0], d[n][1], d[n][2])

    print(answer)
