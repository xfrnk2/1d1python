from typing import List, Sequence, Tuple

import pytest
from src.boj.p15k.p15900.p15970 import draw_arrow

cases: Sequence[Tuple[int, List[Tuple[int, int]], int]] = [
    (7, [(6, 1), (7, 2), (9, 1), (10, 2), (0, 1), (3, 1), (4, 1)], 16),
]


@pytest.mark.parametrize("n, points, expected", cases)
def test_draw_arrow(n: int, points: List[Tuple[int, int]], expected: str, capsys):  # noqa
    draw_arrow(n, points)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
