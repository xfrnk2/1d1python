from typing import Sequence, Tuple, List

import pytest
from src.boj.p16k.p16900.p16951 import block_game

cases: Sequence[Tuple[int, int, List[int], int]] = [
    (4, 1, [1, 2, 1, 5], 2),
    (4, 1, [1, 2, 3, 4], 0)
]


@pytest.mark.parametrize("n, k, array, expected", cases)
def test_array_rotation(n: int, k: int, array: List[int], expected: int):  # noqa
    assert block_game(n, k, array) == expected
