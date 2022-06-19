from typing import Sequence, Tuple, List
import pytest

from src.boj.p5k.p5500.p5525 import ioioi

cases: Sequence[Tuple[int, int, str, int]] = [
    (1, 13, "OOIOIOIOIIOII", 4),
    (2, 13, "OOIOIOIOIIOII", 2)
]


@pytest.mark.parametrize("n, length, string, expected", cases)
def test_ioioi(n: int, length: int, string: str, expected: int, capsys):  # noqa
    ioioi(n, length, string)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
