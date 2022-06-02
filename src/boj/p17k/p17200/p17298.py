from typing import List


def right_big_number(input_value_n: str, input_value_numbers: str) -> None:
    n = int(input_value_n)
    numbers = list(map(int, input_value_numbers.split(' ')))
    right_big_numbers = [-1 for _ in range(n)]
    stack: List[List[int]] = []

    for i in range(n):
        while stack and stack[-1][0] < numbers[i]:
            val, idx = stack.pop()
            right_big_numbers[idx] = numbers[i]
        stack.append([numbers[i], i])
    print(*right_big_numbers)
