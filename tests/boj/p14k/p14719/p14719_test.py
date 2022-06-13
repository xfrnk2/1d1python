from src.boj.p14k.p14700.p14719 import rain_water
from typing import Sequence, Tuple
import pytest

cases: Sequence[Tuple[str, str, int]] = [
("4 4", "3 0 1 4", 5),
("4 8", "3 1 2 3 4 1 1 2", 5),
("3 5", "0 0 0 2 0", 0),
("1 1", "0", 0),
("1 2", "1 0", 0),
("2 3", "2 1 2", 1)
]


@pytest.mark.parametrize("vh, blocks, expected", cases)
def test_rain_water(vh: str, blocks: str, expected: int, capsys):  # noqa
    rain_water(vh, blocks)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
