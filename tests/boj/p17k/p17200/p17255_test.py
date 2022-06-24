from typing import Sequence, Tuple

import pytest
from src.boj.p17k.p17200.p17255 import make_n

cases: Sequence[Tuple[int, int]] = [
    (521, 4),
    (9111, 4)
]


@pytest.mark.parametrize("n, expected", cases)
def test_make_n(n: int, expected: int, capsys):  # noqa
    make_n(n)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
