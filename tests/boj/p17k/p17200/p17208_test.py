from typing import List, Sequence, Tuple

import pytest
from src.boj.p17k.p17200.p17208 import cow_burger

cases: Sequence[Tuple[int, int, int, List[List[int]], int]] = [
    (4, 3, 4, [[2, 5], [1, 2], [3, 3], [2, 1]], 2),
    (5, 5, 5, [[5, 5], [7, 3], [2, 9], [8, 5], [2, 9]], 1),
    (3, 4, 4, [[1, 1], [1, 1], [1, 2]], 3),
    (2, 1, 1, [[5, 5], [5, 5]], 0),
    (3, 5, 5, [[1, 5], [2, 2], [2, 2]], 2),
    (1, 1, 1, [[1, 1]], 1)
]


@pytest.mark.parametrize("n, m, k, orders, expected", cases)
def test_cow_burger(n: int, m: int, k: int, orders: List[List[int]], expected: int, capsys):  # noqa
    cow_burger(n, m, k, orders)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
