from src.boj.p11k.p11000.p11502 import three_decimal
from typing import Sequence, Tuple
import pytest

cases: Sequence[Tuple[int, str]] = [
    (7, "2 2 3"),
    (11, "2 2 7"),
    (25, "3 3 19")
]


@pytest.mark.parametrize("number, expected", cases)
def test_three_decimal(number: int, expected: str, capsys):  # noqa
    three_decimal(number)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
