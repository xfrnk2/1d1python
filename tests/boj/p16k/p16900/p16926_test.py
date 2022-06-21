from typing import Sequence, Tuple, List

import pytest
from src.boj.p16k.p16900.p16926 import array_rotation

cases: Sequence[Tuple[int, int, int, List[List[int]], List[List[int]]],] = [
    (4, 4, 2, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
     [[3, 4, 8, 12], [2, 11, 10, 16], [1, 7, 6, 15], [5, 9, 13, 14]]
     ),
    (2, 2, 3, [[1, 1], [1, 1]], [[1, 1], [1, 1]]),
    (5, 4, 7, [[1, 2, 3, 4], [7, 8, 9, 10], [13, 14, 15, 16], [19, 20, 21, 22], [25, 26, 27, 28]],
     [[28, 27, 26, 25], [22, 9, 15, 19], [16, 8, 21, 13], [10, 14, 20, 7], [4, 3, 2, 1]])
]


@pytest.mark.parametrize("n, m, r, array, expected", cases)
def test_array_rotation(n: int, m: int, r: int, array: List[List[int]], expected: List[List[int]]):  # noqa
    assert array_rotation(n, m, r, array) == expected
