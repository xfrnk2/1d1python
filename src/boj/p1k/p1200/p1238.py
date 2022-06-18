import heapq
import sys
from typing import Any, List, Tuple

input = sys.stdin.readline


def dijkstra(n: int, start: int, roads: List[List[Tuple[int, int]]]) -> List[Any]:
    distance = [1e9 for _ in range(n + 1)]
    distance[start] = 0
    heap: List[Tuple[int, int]] = []
    heapq.heappush(heap, (0, start))

    while heap:
        cost, pos = heapq.heappop(heap)
        for p, c in roads[pos]:
            c += cost
            if c < distance[p]:
                distance[p] = c
                heapq.heappush(heap, (c, p))
    return distance


def party(_info: str, _roads: List[str]) -> None:
    N, M, X = map(int, _info.split())
    roads: List[Any] = [[] for _ in range(N + 1)]
    for r in _roads:
        a, b, cost = map(int, r.split())
        roads[a].append((b, cost))

    answer = [0] * (N + 1)
    for k in range(1, N + 1):
        result = dijkstra(N, k, roads)
        isBack = k == X
        if isBack:
            for i, dist in enumerate(result):
                answer[i] += dist
        else:
            answer[k] += result[X]

    answer.pop(0)
    print(max(answer))
