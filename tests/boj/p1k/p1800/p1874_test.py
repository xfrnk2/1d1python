from typing import Sequence, Tuple
import pytest

from src.boj.p1k.p1800.p1874 import stack_sequence

cases: Sequence[Tuple[str, str, str]] = [
    ("8", "4 3 6 8 7 5 2 1", "+\n+\n+\n+\n-\n-\n+\n+\n-\n+\n+\n-\n-\n-\n-\n-"),
    ("5", "1 2 5 3 4", "NO")
]


@pytest.mark.parametrize("n, numbers, expected", cases)
def test_stack_sequence(n: str, numbers:str, expected: str, capsys):  # noqa
    stack_sequence(n, numbers)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
