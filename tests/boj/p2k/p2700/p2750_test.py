from typing import Sequence, Tuple
import pytest

from src.boj.p2k.p2700.p2750 import sort_numbers

cases: Sequence[Tuple[str, str]] = [
    ("5 2 3 4 1", "1 2 3 4 5")
]


@pytest.mark.parametrize("numbers, expected", cases)
def test_sort_numbers(numbers: str, expected: str, capsys):  # noqa
    sort_numbers(numbers)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
