from typing import List, Tuple
import pytest

from src.leetcode.problems.linked_list.linked_list_cycle_ii import ListNode, Solution

cases: List[Tuple[List[int], int, str]] = [
    ([3, 2, 0, -4], 1, "tail connects to node index 1"),
    ([1, 2], 0, "tail connects to node index 0"),
    ([1], -1, "no cycle")
]


@pytest.mark.parametrize("head, pos, expected", cases)
def test_linked_list_cycle(head: List[int], pos: int, expected: str):  # noqa

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

    ans = Solution().detectCycle(head_node, pos)
    assert ans == expected
