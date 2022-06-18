from typing import Sequence, Tuple, List
import pytest

from src.boj.p1k.p1200.p1238 import party

cases: Sequence[Tuple[str, List[str], int]] = [
    ("4 8 2",
    ["1 2 4",
    "1 3 2",
    "1 4 7",
    "2 1 1",
    "2 3 5",
    "3 1 2",
    "3 4 4",
    "4 2 3"],
    10)
]


@pytest.mark.parametrize("info, roads, expected", cases)
def test_party(info: str, roads: List[str], expected: int, capsys):  # noqa
    party(info, roads)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
