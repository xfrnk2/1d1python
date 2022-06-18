from src.boj.p11k.p11700.p11727 import two_mul_n_tile
from typing import Sequence, Tuple
import pytest

cases: Sequence[Tuple[int, str]] = [
   (2, "3"),
   (8, "171"),
   (12, "2731")
]


@pytest.mark.parametrize("number, expected", cases)
def test_three_decimal(number: int, expected: str, capsys):  # noqa
    two_mul_n_tile(number)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
