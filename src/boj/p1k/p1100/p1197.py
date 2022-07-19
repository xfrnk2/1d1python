from typing import List


def find(parent: List[int], x: int) -> int:
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent: List[int], a: int, b: int) -> None:
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def the_shortest_spanning_tree(v: int, e: int, edges: List[List[int]]) -> int:
    edges.sort(key=lambda x: x[2])
    parent = [x for x in range(v + 1)]
    minimum_flow = 0
  
    for edge in edges:
        a, b, cost = edge
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            minimum_flow += cost
        
    return minimum_flow