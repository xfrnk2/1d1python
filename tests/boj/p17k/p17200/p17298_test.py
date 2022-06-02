from src.boj.p17k.p17200.p17298 import right_big_number
from typing import Sequence, Tuple
import pytest

cases: Sequence[Tuple[str, str, str]] = [
    ("4", "3 5 2 7", "5 7 7 -1"),
    ("4", "9 5 4 8", "-1 8 8 -1")
]


@pytest.mark.parametrize("n, numbers, expected", cases)
def test_right_big_number(n: str, numbers: str, expected: int, capsys):  # noqa
    right_big_number(n, numbers)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
