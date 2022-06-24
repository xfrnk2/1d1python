from typing import Sequence, Tuple, List

import pytest
from src.boj.p3k.p3000.p3067 import coin_problem

cases: Sequence[Tuple[int, List[int], int, int]] = [
    (2, [1, 2], 1000, 501),
    (3, [1, 5, 10], 100, 121),
    (2, [5, 7], 22, 1)
]


@pytest.mark.parametrize("n, coins, money, expected", cases)
def test_coin_problem(n: int, coins: List[int], money: int, expected: int, capsys):  # noqa
    coin_problem(n, coins, money)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
