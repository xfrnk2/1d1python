from typing import Sequence, Tuple, List
import pytest

from src.boj.p5k.p5600.p5622 import dial

cases: Sequence[Tuple[str, str]] = [
    ("WA", "13"),
    ("UNUCIC", "36")
]


@pytest.mark.parametrize("string, expected", cases)
def test_dial(string: str, expected: str, capsys):  # noqa
    dial(string)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
