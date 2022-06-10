from src.boj.p18k.p18100.p18111 import minecraft
from typing import Sequence, Tuple, List
import pytest

cases: Sequence[Tuple[str, List[str], str]] = [
    ("3 4 99", ["0 0 0 0", "0 0 0 0", "0 0 0 1"], "2 0"),
    ("3 4 1", ["64 64 64 64", "64 64 64 64", "64 64 64 63"], "1 64"),
    ("3 4 0", ["64 64 64 64", "64 64 64 64", "64 64 64 63"], "22 63"),
    ("3 4 11", ["29 51 54 44", "22 44 32 62", "25 38 16 2"], "250 35"),
    ("4 4 36", ["15 43 61 21", "19 33 31 55", "48 63 1 30", "31 28 3 8"], "355 32")

]


@pytest.mark.parametrize("info, field, expected", cases)
def test_minecraft(info: str, field: List[str], expected: str, capsys):  # noqa
    minecraft(info, field)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
