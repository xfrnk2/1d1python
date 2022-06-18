from src.boj.p11k.p11500.p11508 import two_plus_one_sale
from typing import Sequence, Tuple, List
import pytest

cases: Sequence[Tuple[int, List[int], int]] = [
    (4, [3, 2, 3, 2], 8),
    (6, [6, 4, 5, 5, 5, 5], 21),
    (5, [4, 5, 4, 5, 4], 18)
]


@pytest.mark.parametrize("n, milks, expected", cases)
def test_two_plus_one_sale(n: int, milks: List[int], expected: int, capsys):  # noqa
    two_plus_one_sale(n, milks)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
