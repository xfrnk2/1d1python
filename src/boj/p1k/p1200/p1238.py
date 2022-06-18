from typing import Any, Tuple, List

def init_graph(n: int, roads: List[str]) -> List[List[Any]]:
    graph = [[0 if j == i else float('inf') for j in range(n + 1)] for i in range(n + 1)]
    for road in roads:
        a, b, cost = road
        graph[a][b] = cost
    # graph[0][0] = float('inf')
    return graph

# distances 내부의 최소 거리를 가지는 정점의 번호를 반환
def get_point_has_minimum_distance(n: int, distances: List[int], visited: List[bool]) -> int:
    m = float('inf')
    idx = 0
    for i in range(1, n + 1):
        if distances[i] < m and not visited[i]:
            m = distances[i]
            idx = i
    return idx


def dijkstra(n: int, start: int, graph: List[List[Any]], visited: List[bool], distances: List[Any], target: int) -> int:
    

    # b점 까지의 거리를 시작점 a를 기준으로 초기화
    for i in range(1, n + 1):
        distances[i] = graph[start][i]

    # a는 방문 처리
    visited[start] = True
    for _ in range(n - 1): # 횟수 시작 노드를 제외한 n - 1번만큼 방문
        current = get_point_has_minimum_distance(n, distances, visited)

        visited[current] = True
        for j in range(1, n + 1):
            if not visited[j]:
                if distances[current] + graph[current][j] < distances[j]:
                    distances[j] = distances[current] + graph[current][j]

    return distances[target]



def party(_info: str, _roads: List[str]) -> None:
    N, M, X = map(int, _info.split())
    roads = [list(map(int, r.split())) for r in _roads]
    
    graph = init_graph(N, roads)
    
    visited = [False for i in range(N + 1)]
    distances = [i for i in range(N + 1)]

    answer = 0
    for i in range(1, N + 1):
        go = dijkstra(N, i, graph, visited[:], distances[:], X)
        back = dijkstra(N, X, graph, visited[:], distances[:], i)
        answer = max(answer, go + back)

    print(answer)
    
    
    