from src.boj.p11k.p11600.p11660 import prefix_sum
from typing import List, Sequence, Tuple
import pytest

cases: Sequence[Tuple[int, int, List[List[int]], List[List[int]], List[int]]] = [
    (4, 3, [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]],
    [[2, 2, 3, 4], [3, 4, 3, 4], [1, 1, 4, 4]], [27, 6, 64])
]

@pytest.mark.parametrize("n, m, matrix, section, expected", cases)
def test_prefix_sum(n: int, m: int, matrix: List[List[int]], section: List[List[int]], expected: List[int], capsys):  # noqa
    assert expected == prefix_sum(n, m, matrix, section)
