from typing import Sequence, Tuple, List
import pytest

from src.boj.p2k.p2200.p2206 import break_wall_and_move

cases: Sequence[Tuple[int, int, List[List[int]], int]] = [
    # (6, 4, ["0100", "1110", "1000", "0000", "0111", "0000"], 15),
    # (4, 4, ["0111", "1111", "1111", "1110"], -1)
    (6, 4, [[0, 1, 0, 0], [1, 1, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]], 15),
    (4, 4, [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0]], -1),
    (1, 2, [[0, 1]], 2),
    (1, 1, [[0]], 1)
]


@pytest.mark.parametrize("n, m, matrix, expected", cases)
def test_melon_field(n: int, m: int, matrix: List[List[int]], expected: int, capsys):  # noqa
    break_wall_and_move(n, m, matrix)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
