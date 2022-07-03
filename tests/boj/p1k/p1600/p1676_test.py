from typing import Sequence, Tuple

import pytest
from src.boj.p1k.p1600.p1676 import factorial_zero_number

cases: Sequence[Tuple[int, int]] = [
    (10, 2),
    (3, 0)
]


@pytest.mark.parametrize("n, expected", cases)
def test_sum_square_number(n: int, expected: int, capsys):  # noqa
    assert factorial_zero_number(n) == expected
