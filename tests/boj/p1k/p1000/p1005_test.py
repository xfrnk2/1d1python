from typing import List, Sequence, Tuple

import pytest
from src.boj.p1k.p1000.p1005 import acm_craft

cases: Sequence[Tuple[int, int, List[int], List[List[int]], int, int]] = [
    (4, 4, [10, 1, 100, 10], [[1, 2], [1, 3], [2, 4], [3, 4]], 4, 120),
    (8, 8, [10, 20, 1, 5, 8, 7, 1, 43], [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6],
                                         [5, 7], [6, 7], [7, 8]], 7, 39),
    (7, 8, [0, 0, 0, 0, 0, 0, 0], [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5],
                                   [4, 6], [5, 7], [6, 7]], 7, 0)
]


@pytest.mark.parametrize("n, k, times, buildings, required_building, expected", cases)
def test_acm_craft(n: int, k: int, times: List[int], buildings: List[List[int]], required_building: int, expected: int,
                   capsys):  # noqa
    acm_craft(n, k, times, buildings, required_building)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
