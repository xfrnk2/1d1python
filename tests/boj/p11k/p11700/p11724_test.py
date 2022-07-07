from typing import List, Sequence, Tuple

import pytest
from src.boj.p11k.p11700.p11724 import connected_elements_number

cases: Sequence[Tuple[int, int, List[List[int]], int]] = [
    (6, 5, [[1, 2], [2, 5], [5, 1], [3, 4], [4, 6]], 2),
    (6, 8, [[1, 2], [2, 5], [5, 1], [3, 4], [4, 6], [5, 4], [2, 4], [2, 3]], 1)
]


@pytest.mark.parametrize("n, m, edges, expected", cases)
def test_connected_elements_number(n: int, m: int, edges: List[List[int]], expected: str, capsys):  # noqa
    connected_elements_number(n, m, edges)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
