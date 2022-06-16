from src.boj.p16k.p16200.p16206 import roll_cake
from typing import Sequence, Tuple, List
import pytest

cases: Sequence[Tuple[int, List[int], int]] = [
(1, [10, 10, 10], 3),
(1, [10, 10, 20], 4),
(3, [20, 20, 20], 6),
(8, [34, 45, 56, 12, 23], 8),
(7, [10, 20, 30, 40, 50], 11),
(1, [1], 0),
(2, [18, 19, 20], 3)
]


@pytest.mark.parametrize("cuttable_count, cakes, expected", cases)
def test_roll_cake(cuttable_count: int, cakes: List[int], expected: int, capsys):  # noqa
    roll_cake(cuttable_count, cakes)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
