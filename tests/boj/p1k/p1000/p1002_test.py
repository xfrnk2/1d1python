from typing import Sequence, Tuple
import pytest

from src.boj.p1k.p1000.p1002 import turret

cases: Sequence[Tuple[str, int]] = [
    ("0 0 13 40 0 37", 2),
    ("0 0 3 0 7 4", 1),
    ("1 1 1 1 1 5", 0)
]


@pytest.mark.parametrize("input_values , expected", cases)
def test_the_little_prince(input_values: str, expected: int, capsys):  # noqa
    turret(input_values)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
