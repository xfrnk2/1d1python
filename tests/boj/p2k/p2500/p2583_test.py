from typing import List, Sequence, Tuple

import pytest
from src.boj.p2k.p2500.p2583 import get_areas

cases: Sequence[Tuple[int, int, int, List[List[int]], int, str]] = [
    (5, 7, 3, [[0, 2, 4, 4], [1, 1, 2, 5], [4, 0, 6, 2]], 3, "1 7 13")
]


@pytest.mark.parametrize("m, n, k, squares, expected1, expected2", cases)
def test_get_areas(m: int, n: int, k: int, squares: List[List[int]],
                   expected1: int, expected2: str,
                   capsys):  # noqa
    get_areas(m, n, k, squares)
    captured = capsys.readouterr()
    assert captured.out == f'{expected1}\n{expected2}\n'
