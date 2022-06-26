from typing import Sequence, Tuple

import pytest
from src.boj.p11k.p11400.p11444 import fibo_six

cases: Sequence[Tuple[int, int]] = [
    (1000, 517691607),
    (3, 2),
    (4, 3)
]


@pytest.mark.parametrize("number, expected", cases)
def test_fibo_six(number: int, expected: int, capsys):  # noqa
    fibo_six(number)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
