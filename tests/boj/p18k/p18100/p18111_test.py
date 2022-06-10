from src.boj.p18k.p18100.p18111 import minecraft
from typing import Sequence, Tuple
import pytest

cases: Sequence[Tuple[str, int]] = [
("3 4 99", "0 0 0 0", "0 0 0 0", "0 0 0 1", "2 0"),
("3 4 1", "64 64 64 64", "64 64 64 64", "64 64 64 63", "1 64"),
("3 4 0", "64 64 64 64", "64 64 64 64", "64 64 64 63", "22 63")

]


@pytest.mark.parametrize("info, row1, row2, row3, expected", cases)
def test_minecraft(info: str, row1: str, row2: str, row3: str, expected: str, capsys):  # noqa
    minecraft(info, row1, row2, row3)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
