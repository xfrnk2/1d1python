from typing import Sequence, Tuple, List

import pytest
from src.boj.p2k.p2000.p2075 import n_big_number

cases: Sequence[Tuple[int, List[List[int]], int]] = [
    (5, [
        [12, 7, 9, 15, 5],
        [13, 8, 11, 19, 6],
        [21, 10, 26, 31, 16],
        [48, 14, 28, 35, 25],
        [52, 20, 32, 41, 49]
    ], 35
     )
]


@pytest.mark.parametrize("n, matrix, expected", cases)
def test_n_big_number(n: int, matrix: List[List[int]], expected: str, capsys):  # noqa
    n_big_number(n, matrix)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
