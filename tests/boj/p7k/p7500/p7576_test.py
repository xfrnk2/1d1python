from typing import Sequence, Tuple, List

import pytest
from src.boj.p7k.p7500.p7576 import tomato

cases: Sequence[Tuple[int, int, List[List[int]], int]] = [
    (6, 4, [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]], 8),
    (6, 4, [[0, -1, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]], -1),
    (6, 4, [[1, -1, 0, 0, 0, 0], [0, -1, 0, 0, 0, 0], [0, 0, 0, 0, -1, 0], [0, 0, 0, 0, -1, 1]], 6)
]


@pytest.mark.parametrize("n, m, box, expected", cases)
def test_check_is_tree(n: int, m: int, box: List[List[int]], expected: int, capsys):  # noqa
    result = tomato(n, m, box)
    assert result == expected
