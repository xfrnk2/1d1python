from typing import List, Tuple
import heapq


def synchronize(heap_list, visit) -> None:
    while heap_list and not visit[heap_list[0][1]]:
        heapq.heappop(heap_list)


def double_priority_queue(n: int, input_value: List[str]) -> None:
    min_heap: List[Tuple[int, int]]
    max_heap: List[Tuple[int, int]]

    min_heap = []
    max_heap = []
    visit = [0 for _ in range(1000001)]

    for i in range(n):
        op, value = input_value[i].split()
        number = int(value)

        if op == "I":
            heapq.heappush(min_heap, (number, i))
            heapq.heappush(max_heap, (-number, i))
            visit[i] = 1
        elif number == 1:
            synchronize(max_heap, visit)
            if max_heap:
                visit[max_heap[0][1]] = 0
                heapq.heappop(max_heap)
        else:
            synchronize(min_heap, visit)
            if min_heap:
                visit[min_heap[0][1]] = 0
                heapq.heappop(min_heap)
    synchronize(max_heap, visit)
    synchronize(min_heap, visit)

    answer = ""
    if max_heap and min_heap:
        answer = f"{-max_heap[0][0]} {min_heap[0][0]}"
    else:
        answer = "EMPTY"
    print(answer)
