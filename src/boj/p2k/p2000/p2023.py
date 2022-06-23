from typing import List


def is_decimal(a):
    if (a < 2):
        return False
    for i in range(2, a):
        if (a % i == 0):
            return False
    return True


def solve(n: int, l: int, x: int, result: List[int]) -> None:
    if n <= l:
        result.append(x)
        return
    for i in range(1, 10):

        nx = x * 10 + i

        if is_decimal(nx):
            solve(n, l + 1, nx, result)


def amazing_decimal(n: int) -> List[int]:
    answer = []
    for i in [2, 3, 5, 7]:
        solve(n, 1, i, answer)
    return answer
