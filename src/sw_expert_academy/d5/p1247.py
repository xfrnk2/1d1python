from typing import List, Union


def shortest_path(n: int, input_value: List[int]) -> Union[float, int]:
    start = input_value[:2]
    end = input_value[2:4]
    nodes = []
    answer = float('inf')
    for i in range(4, len(input_value), 2):
        nodes.append((input_value[i], input_value[i + 1]))

    def get_distance(x1: int, y1: int, x2: int, y2: int) -> int:
        return abs(x1 - x2) + abs(y1 - y2)

    def search(count: int, path: List[int], total: int) -> None:
        nonlocal nodes, answer
        if count == n:
            x1, y1 = nodes[path[-1]]
            x2, y2 = end
            result = get_distance(x1, y1, x2, y2)

            answer = min(answer, result + total)

        for i, node in enumerate(nodes):
            if i in path:
                continue

            x2, y2 = node
            if count == 0:
                x1, y1 = start
            else:
                x1, y1 = nodes[path[-1]]
            search(count + 1, path + [i], total + get_distance(x1, y1, x2, y2))

    search(0, [], 0)
    return answer
