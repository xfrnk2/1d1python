import heapq
from typing import List


def n_big_number(n: int, matrix: List[List[int]]) -> None:
    heap: List[int]
    heap = []

    for i in range(n):
        current_row_matrix = matrix[i]

        if heap:
            for number in current_row_matrix:

                if heap[0] < number:
                    heapq.heappop(heap)
                    heapq.heappush(heap, number)

        else:
            for number in current_row_matrix:
                heapq.heappush(heap, number)

    print(heap[0])
