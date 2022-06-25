from typing import List, Sequence, Tuple

import pytest
from src.boj.p1k.p1100.p1149 import rgb_distance

cases: Sequence[Tuple[int, List[List[int]], int]] = [
    (3, [[26, 40, 83], [49, 60, 57], [13, 89, 99]], 96)
]


@pytest.mark.parametrize("n, colors, expected", cases)
def test_rgb_distance(n: int, colors: List[List[int]], expected: int, capsys):  # noqa
    rgb_distance(n, colors)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
