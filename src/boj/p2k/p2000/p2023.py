import math
from typing import List


def is_decimal(n):
    for i in range(2, int(math.sqrt(n)) + 1):  # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False
    return True


def solve(n: int, length: int, x: int, result: List[int]) -> None:
    if n <= length:
        result.append(x)
        return
    for i in range(1, 10):
        nx = x * 10 + i

        if is_decimal(nx):
            solve(n, length + 1, nx, result)


def amazing_decimal(n: int) -> List[int]:
    answer: List[int] = []

    for i in [2, 3, 5, 7]:
        solve(n, 1, i, answer)
    return answer
