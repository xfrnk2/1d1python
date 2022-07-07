from collections import defaultdict
from typing import List


def visit(vertex_data: dict, visited: List[int], vertex1: int) -> None:
    if visited[vertex1]:
        return
    visited[vertex1] = 1
    for vertex2 in vertex_data[vertex1]:
        visit(vertex_data, visited, vertex2)


def connected_elements_number(n: int, m: int, edges: List[List[int]]) -> None:
    """
    1. 모든 입력값을 각 숫자별 배열을 만들어 저장한다. (예: 1과 대응하는 1과 연결된 리스트)
    2. 1~ N까지 순회한다.
    3. 방문한 목록에 추가해가며 모든 연결된 정점을 방문한다.
    """
    vertex_data = defaultdict(list)
    visited = [0 for _ in range(n + 1)]  # 방문시 1
    count = 0

    for edge in edges:
        vertex1, vertex2 = edge
        vertex_data[vertex1].append(vertex2)
        vertex_data[vertex2].append(vertex1)

    for vertex1 in range(1, n + 1):

        if visited[vertex1]:
            continue
        visited[vertex1] = 1
        count += 1
        for vertex2 in vertex_data[vertex1]:
            visit(vertex_data, visited, vertex2)

    print(count)
