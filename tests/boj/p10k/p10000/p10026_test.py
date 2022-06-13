from src.boj.p10k.p10000.p10026 import red_green_color_weakness
from typing import Sequence, Tuple
import pytest

cases: Sequence[Tuple[int, str, str]] = [
    (5, "RRRBB GGBBB BBBRR BBRRR RRRRR", "4 3"),
    (1, "R", "1 1")
]


@pytest.mark.parametrize("size, field, expected", cases)
def test_surprise(size: int, field: str, expected: str, capsys):  # noqa
    red_green_color_weakness(size, field)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
