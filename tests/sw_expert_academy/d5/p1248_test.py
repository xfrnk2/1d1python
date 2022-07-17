from typing import List, Sequence, Tuple

import pytest
from src.sw_expert_academy.d5.p1248 import same_parent

cases: Sequence[Tuple[int, int, int, int, List[int], Tuple[int, int]]] = [
    (13, 12, 8, 13, [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 7, 12, 5, 9, 5, 8, 6, 10, 6, 11, 11, 13], (3, 8)),
    (50, 49, 24, 31,
     [31, 7, 2, 17, 27, 32, 14, 30, 1, 21, 45, 26, 44, 27, 39, 11, 26, 3, 48, 6, 3, 44, 2, 49, 42, 13, 48, 8, 23, 33,
      11, 10, 8, 42, 41, 31, 17, 4, 8, 22, 25, 23, 21, 41, 28, 25, 13, 16, 46, 2, 31, 35, 42, 19, 32, 18, 27, 50, 45,
      15, 28, 20, 46, 28, 44, 40, 40, 5, 15, 48, 9, 34, 1, 46, 17, 29, 35, 36, 21, 45, 14, 37, 23, 14, 6, 39, 11, 9, 19,
      24, 26, 47, 16, 38, 40, 12, 47, 43], (21, 35))
]


@pytest.mark.parametrize("v, e, p1, p2, edges, expected", cases)
def test_shortest_path(v: int, e: int, p1: int, p2: int, edges: List[int], expected: Tuple[int, int]):  # noqa
    assert expected == same_parent(v, e, p1, p2, edges)
