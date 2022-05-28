from typing import Tuple, List
import pytest

from src.leetcode.problems.linked_list.linked_list_cycle import ListNode, Solution

cases: List[Tuple[List[int], int, bool]] = [
    ([3, 2, 0, -4], 1, True),
    ([1, 2], 0, True),
    ([1], -1, False)
]


@pytest.mark.parametrize("head, pos, expected", cases)
def test_linked_list_cycle(head: List[int], pos: int, expected: bool):  # noqa

    head_node = ListNode(head[0])
    prev_node = head_node
    pos_node = None

    for i in range(1, len(head)):
        prev_node.next = ListNode(i)
        prev_node = prev_node.next
        if i == pos:
            pos_node = prev_node

    if pos == 0:
        prev_node.next = head_node
    elif 0 < pos:
        prev_node.next = pos_node

    ans = Solution().hasCycle(head_node)
    assert ans == expected
