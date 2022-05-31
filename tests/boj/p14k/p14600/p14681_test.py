from src.boj.p14k.p14600.p14681 import choose_quadrant
from typing import Sequence, Tuple
import pytest

cases: Sequence[Tuple[str, str, int]] = [
("12", "5", 1)
]


@pytest.mark.parametrize("x, y, expected", cases)
def test_choose_quadrant(x: str, y: str, expected: int, capsys):  # noqa
    choose_quadrant(x, y)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
