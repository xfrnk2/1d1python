from typing import List, Sequence, Tuple

import pytest
from src.boj.p15k.p15600.p15666 import n_and_m

cases: Sequence[Tuple[int, int, List[int], str]] = [
    (4, 4, [1, 1, 2, 2], "1 1 1 1\n1 1 1 2\n1 1 2 2\n1 2 2 2\n2 2 2 2"),
    (4, 2, [9, 7, 9, 1], "1 1\n1 7\n1 9\n7 7\n7 9\n9 9"),
    (3, 1, [4, 4, 2], "2\n4"),
    (1, 1, [1], "1")
]


@pytest.mark.parametrize("n, m, array, expected", cases)
def test_choose_quadrant(n: int, m: int, array: List[int], expected: str, capsys):  # noqa
    n_and_m(n, m, array)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
