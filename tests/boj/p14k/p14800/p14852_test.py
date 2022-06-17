from src.boj.p14k.p14800.p14852 import tile3
from typing import Sequence, Tuple
import pytest

cases: Sequence[Tuple[str, int]] = [
("1", 2),
("2", 7),
("3", 22),
("4", 71)
]


@pytest.mark.parametrize("input_value, expected", cases)
def test_tile3(input_value: str, expected: int, capsys):  # noqa
    tile3(input_value)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
