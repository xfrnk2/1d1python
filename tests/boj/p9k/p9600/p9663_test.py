from typing import Sequence, Tuple

import pytest
from src.boj.p9k.p9600.p9663 import n_queen

cases: Sequence[Tuple[int, int]] = [
    (8, 92)
]


@pytest.mark.parametrize("n, expected", cases)
def test_n_queen(n: int, expected: int, capsys):  # noqa
    n_queen(n)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
