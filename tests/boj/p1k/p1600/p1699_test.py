from typing import Sequence, Tuple

import pytest
from src.boj.p1k.p1600.p1699 import sum_square_number

cases: Sequence[Tuple[int, int]] = [
    (7, 4),
    (1, 1),
    (4, 1),
    (11, 3),
    (13, 2)
]


@pytest.mark.parametrize("n, expected", cases)
def test_sum_square_number(n: int, expected: int, capsys):  # noqa
    assert sum_square_number(n) == expected
