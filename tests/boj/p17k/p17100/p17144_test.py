from typing import List, Sequence, Tuple

import pytest
from src.boj.p17k.p17100.p17144 import good_by_pm

cases: Sequence[Tuple[int, int, int, List[List[int]], int]] = [
    (7, 8, 1,
     [[0, 0, 0, 0, 0, 0, 0, 9], [0, 0, 0, 0, 3, 0, 0, 8], [-1, 0, 5, 0, 0, 0, 22, 0], [-1, 8, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 10, 43, 0],
      [0, 0, 5, 0, 15, 0, 0, 0], [0, 0, 40, 0, 0, 0, 20, 0]], 188),

    (7, 8, 50, [[
        0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 3, 0, 0, 8],
        [-1, 0, 5, 0, 0, 0, 22, 0],
        [-1, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 10, 43, 0],
        [0, 0, 5, 0, 15, 0, 0, 0, ],
        [0, 0, 40, 0, 0, 0, 20, 0]], 46)
]


@pytest.mark.parametrize("r, c, t, matrix, expected", cases)
def test_good_bye_pm(r: int, c: int, t: int, matrix: List[List[int]], expected: int, capsys):  # noqa
    good_by_pm(r, c, t, matrix)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
