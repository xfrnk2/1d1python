from typing import Sequence, Tuple, List
import pytest

from src.boj.p2k.p2200.p2292 import honeycomb

cases: Sequence[Tuple[int, str]] = [
    (13, "3"),
    (58, "5")
]


@pytest.mark.parametrize("target, expected", cases)
def test_melon_field(target: int, expected: str, capsys):  # noqa
    honeycomb(target)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
