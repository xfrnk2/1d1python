from typing import Sequence, Tuple, List
import pytest

from src.boj.p2k.p2400.p2477 import melon_field

cases: Sequence[Tuple[int, List[Tuple[int, int]], int]] = [
    (7, [(4, 50), (2, 160), (3, 30), (1, 60), (3, 20), (1, 100)], 47600)
]


@pytest.mark.parametrize("n, distances, expected", cases)
def test_melon_field(n: int, distances: List[Tuple[int]], expected: int, capsys):  # noqa
    melon_field(n, distances)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
