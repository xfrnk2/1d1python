from collections import deque
from typing import List


def n_big_number(n: int, matrix: List[List[int]]) -> None:
    queue_list = [deque(sorted(matrix[i], reverse=True)) for i in range(n)]

    answer = 0

    for _ in range(n):

        maximum_number_idx = 0
        maximum_number = 0
        for idx, q in enumerate(queue_list):
            if maximum_number < q[0]:
                maximum_number, maximum_number_idx = q[0], idx

        answer = queue_list[maximum_number_idx].popleft()

    print(answer)
