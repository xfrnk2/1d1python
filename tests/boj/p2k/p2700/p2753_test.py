from typing import Sequence, Tuple
import pytest

from src.boj.p2k.p2700.p2753 import leap_year

cases: Sequence[Tuple[str, str]] = [
    ("2000", "1"),
    ("1999", "0")
]


@pytest.mark.parametrize("year, expected", cases)
def test_multiplication(year: str, expected: str, capsys):  # noqa
    leap_year(year)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
