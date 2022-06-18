from typing import Sequence, Tuple, List
import pytest

from src.boj.p5k.p5500.p5525 import ioioi

cases: Sequence[Tuple[int, str, int]] = [
    (1, "OOIOIOIOIIOII", 4),
    (2, "OOIOIOIOIIOII", 2)
]


@pytest.mark.parametrize("n, string, expected", cases)
def test_ioioi(n: int, string: str, expected: int, capsys):  # noqa
    ioioi(n, string)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
