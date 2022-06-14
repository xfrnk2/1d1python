from src.boj.p17k.p17400.p17484 import moon_travel
from typing import Sequence, Tuple, List
import pytest

cases: Sequence[Tuple[List[str], int]] = [
(["5 8 5 1", "3 5 8 4", "9 77 65 5", "2 1 5 2", "5 98 1 5", "4 95 67 58"], 29),
]


@pytest.mark.parametrize("area, expected", cases)
def test_moon_travel(area: List[str], expected: int, capsys):  # noqa
    moon_travel(area)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
