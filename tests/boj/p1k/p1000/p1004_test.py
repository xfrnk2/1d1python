from typing import Sequence, Tuple
import pytest

from src.boj.p1k.p1000.p1004 import the_little_prince

cases: Sequence[Tuple[str, str, str, int]] = [
    ("-5 1", "12 1", "1 1 8,-3 -1 1,2 2 2,5 5 1,-4 5 1,12 1 1,12 1 2", 3)
]


@pytest.mark.parametrize("start_point, end_point, planets, expected", cases)
def test_the_little_prince(start_point: str, end_point: str, planets: str, expected: int, capsys):  # noqa
    the_little_prince(start_point, end_point, planets)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
