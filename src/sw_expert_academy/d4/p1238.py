from collections import defaultdict, deque
from typing import List


def contact(n: int, first: int, nodes: List[int]) -> int:
    edges = defaultdict(list)
    visit = {x: False for x in set(nodes)}
    visit[first] = True
    for i in range(0, n, 2):
        edges[nodes[i]].append(nodes[i + 1])

    next_nodes = deque(edges[first])
    while next_nodes:

        temp = deque([])
        for t in next_nodes:

            if not visit[t]:
                visit[t] = True
                for elem in edges[t]:

                    if not visit[elem]:
                        temp.append(elem)

        if not temp:
            return max(next_nodes)
        next_nodes = temp

    return 0
