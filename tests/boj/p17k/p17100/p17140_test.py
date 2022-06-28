from typing import List, Sequence, Tuple

import pytest
from src.boj.p17k.p17100.p17140 import two_dimensional_operation

cases: Sequence[Tuple[int, int, int, List[List[int]], int]] = [
    (1, 2, 2,
     [
         [1, 2, 1],
         [2, 1, 3],
         [3, 3, 3]
     ], 0),
    (1, 2, 1,
     [[1, 2, 1],
      [2, 1, 3],
      [3, 3, 3]], 1),
    (
        1, 2, 4,
        [[1, 2, 1],
         [2, 1, 3],
         [3, 3, 3]], 52
    ),
    (
        1, 2, 3,
        [[1, 2, 1],
         [2, 1, 3],
         [3, 3, 3]], 2
    ),
    (
        4, 4, 1,
        [[1, 2, 1],
         [2, 1, 3],
         [3, 3, 3]], 2
    )
]


@pytest.mark.parametrize("r, c, t, array, expected", cases)
def test_two_dimensional_operation(r: int, c: int, t: int, array: List[List[int]], expected: int, capsys):  # noqa
    two_dimensional_operation(r, c, t, array)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
