from typing import List, Sequence, Tuple
import pytest

from src.boj.p1k.p1100.p1197 import the_shortest_spanning_tree

cases: Sequence[Tuple[int, int, List[int], int]] = [
    (3, 3, [[1, 2, 1], [2, 3, 2], [1, 3, 3]], 3)
]


@pytest.mark.parametrize("v, e, edges, expected", cases)
def test_the_shortest_spanning_tree(v: int, e: int, edges: List[int], expected: int):  # noqa
    assert expected == the_shortest_spanning_tree(v, e, edges)
