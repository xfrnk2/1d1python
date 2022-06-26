import sys
from typing import List

input = sys.stdin.readline


def fibo_six(n: int) -> None:
    matrix = [[1, 1], [1, 0]]
    init_fibo_value = [[1], [1]]

    def divide_and_conquer(n, mat) -> List[List[int]]:
        if n == 1:
            return mat
        if n % 2 == 1:
            return multiply_matrix(divide_and_conquer(n - 1, mat), mat)
        else:
            return divide_and_conquer(n // 2, multiply_matrix(mat, mat))

    def multiply_matrix(a, b) -> List[List[int]]:
        updated = [[0] * len(b[0]) for _ in range(len(a[0]))]
        for i in range(2):
            for j in range(len(b[0])):
                total = 0
                for k in range(len(a[0])):
                    total += a[i][k] * b[k][j]
                updated[i][j] = total % 1000000007
        return updated

    answer = 1
    if 3 <= n:
        answer = multiply_matrix(divide_and_conquer(n - 2, matrix), init_fibo_value)[0][0]
    print(answer)
