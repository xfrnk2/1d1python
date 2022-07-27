from src.boj.p16k.p16200.p16236 import baby_shark
from typing import Sequence, Tuple, List
import pytest

cases: Sequence[Tuple[int, List[List[int]], int]] = [
(3, [[0, 0, 0], [0, 0, 0], [0, 9, 0]], 0),
(3, [[0, 0, 1], [0, 0, 0], [0, 9, 0]], 3),
(4, [[4, 3, 2, 1], [0, 0, 0, 0], [0, 0, 9, 0], [1, 2, 3, 4]], 14)
]


@pytest.mark.parametrize("n, field, expected", cases)
def test_roll_cake(n: int, field: List[int], expected: int):  # noqa
    assert baby_shark(n, field) == expected
