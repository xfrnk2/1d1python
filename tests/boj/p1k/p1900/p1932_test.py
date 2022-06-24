from typing import List, Sequence, Tuple

import pytest
from src.boj.p1k.p1900.p1932 import digit_triangle

cases: Sequence[Tuple[int, List[List[int]], int]] = [
    (5, [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]], 30),
    (1, [[1]], 1)
]


@pytest.mark.parametrize("n, numbers, expected", cases)
def test_digit_triangle(n: int, numbers: List[List[int]], expected: int, capsys):  # noqa
    digit_triangle(n, numbers)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
