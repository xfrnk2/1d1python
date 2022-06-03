from typing import List


def right_big_number(input_value_n: str, input_value_numbers: str) -> None:
    N = int(input_value_n)
    given_numbers = list(map(int, input_value_numbers.split(' ')))
    stack: List[List[int]] = []
    answer = [-1 for _ in range(N)]

    for i in range(N):
        while stack and stack[-1][1] < given_numbers[i]:
            idx, number = stack.pop()
            answer[idx] = given_numbers[i]
        stack.append([i, given_numbers[i]])
    print(*answer)
