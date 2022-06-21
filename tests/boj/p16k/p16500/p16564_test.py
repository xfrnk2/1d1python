from src.boj.p16k.p16500.p16564 import hios_progamer
from typing import Sequence, Tuple, List
import pytest

cases: Sequence[Tuple[int, int, List[int], int]] = [
    (3, 10, [10, 20, 15], 17)
]


@pytest.mark.parametrize("n, point, team, expected", cases)
def test_hios_progamer(n: int, point: int, team: List[int], expected: int, capsys):  # noqa
    hios_progamer(n, team, point)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
