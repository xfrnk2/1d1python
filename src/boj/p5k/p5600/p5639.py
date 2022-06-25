import sys
from typing import List

sys.setrecursionlimit(10 ** 6)


def binary_search_tree(pre_order: List[int]) -> List[int]:
    """
    pre_order: PLR
    post_order: LRP
    ([50, 30, 24, 5, 28, 45, 98, 52, 60],
    [5, 28, 24, 45, 30, 60, 52, 98, 50])
    """
    answer = []

    def post_order(start, end) -> None:
        nonlocal answer, n, pre_order
        if start > end:
            return
        right = end + 1

        for i in range(start + 1, end + 1):
            if pre_order[start] < pre_order[i]:
                right = i
                break

        post_order(start + 1, right - 1)
        post_order(right, end)
        answer.append(pre_order[start])
        pass

    n = len(pre_order)
    post_order(0, n - 1)
    return answer
