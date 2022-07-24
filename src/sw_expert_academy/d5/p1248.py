from collections import defaultdict, deque
from typing import List, Tuple


def get_parent(_edges: List[int], edges: dict, parent: int, p1: int, p2: int) -> int:
    q = deque([(1, [1], 0)])
    v1 = []
    v2 = []

    while q:
        cur, path, height = q.popleft()
        for target in edges[cur]:
            if target == p1:
                v1 = path
                continue
            if target == p2:
                v2 = path
                continue

            q.append((target, path + [target], height + 1))
    for i in range(min(len(v1), len(v2))):
        if v1[i] != v2[i]:
            parent = v1[i - 1]
            break
    return parent


def same_parent(v: int, e: int, p1: int, p2: int, _edges: List[int]) -> Tuple:
    edges = defaultdict(list)
    parent = _edges[0]
    total = 0

    for i in range(0, e * 2, 2):
        edges[_edges[i]].append(_edges[i + 1])

    def get_total() -> None:
        nonlocal edges, parent, total

        q = deque([parent])
        while q:
            cur = q.popleft()
            total += 1

            for v in edges[cur]:
                q.append(v)

    parent = get_parent(_edges, edges, parent, p1, p2)
    get_total()
    return parent, total
