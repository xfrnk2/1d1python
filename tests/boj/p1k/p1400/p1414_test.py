from typing import Sequence, Tuple, List
import pytest

from src.boj.p1k.p1400.p1414 import help_the_poor

cases: Sequence[Tuple[int, List[str], str]] = [
    (3, ["abc", "def", "ghi"], "40"),
    (2, ["a0", "0b"], "-1"),
    (4, ["0X00", "00Y0", "0000", "00Z0"], "0"),
    (2, ["Az", "aZ"], "105"),
    (4, ["0top", "c0od", "er0o", "pen0"], "134")
]


@pytest.mark.parametrize("size, cables, expected", cases)
def test_help_the_poor(size: int, cables: List[str], expected: str, capsys):  # noqa
    help_the_poor(size, cables)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
