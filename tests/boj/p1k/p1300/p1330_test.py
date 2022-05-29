from typing import Sequence, Tuple
import pytest

from src.boj.p1k.p1300.p1330 import compare_two_numbers

cases: Sequence[Tuple[str, str]] = [
    ("1 2", "<"),
    ("10 2", ">"),
    ("5 5", "==")
]


@pytest.mark.parametrize("numbers, expected", cases)
def test_compare_two_numbers(numbers: str, expected: str, capsys):  # noqa
    compare_two_numbers(numbers)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
