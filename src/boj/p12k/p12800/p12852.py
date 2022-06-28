from typing import Any, List


def solve(n: int):
    d: List[Any] = [[0, [1]] for _ in range(n + 1)]

    for i in range(2, n + 1):

        d[i][0] = d[i - 1][0] + 1
        d[i][1] = d[i - 1][1] + [i]

        if i % 3 == 0 and d[i // 3][0] < d[i][0] - 1:
            d[i][0] = d[i // 3][0] + 1
            d[i][1] = d[i // 3][1] + [i]

        if i % 2 == 0 and d[i // 2][0] < d[i][0] - 1:
            d[i][0] = d[i // 2][0] + 1
            d[i][1] = d[i // 2][1] + [i]

    print(d[n][0])
    print(*d[n][1][::-1])


def make_one(n: int) -> None:
    solve(n)
