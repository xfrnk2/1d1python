from src.boj.p16k.p16200.p16236 import baby_shark
from typing import Sequence, Tuple, List
import pytest

cases: Sequence[Tuple[int, List[List[int]], int]] = [
(3, [[0, 0, 0], [0, 0, 0], [0, 9, 0]], 0),
(3, [[0, 0, 1], [0, 0, 0], [0, 9, 0]], 3),
(4, [[4, 3, 2, 1], [0, 0, 0, 0], [0, 0, 9, 0], [1, 2, 3, 4]], 14),

(6, [[5, 4, 3, 2, 3, 4], [4, 3, 2, 3, 4, 5], [3, 2, 9, 5, 6, 6], 
    [2, 1, 2, 3, 4, 5], [3, 2, 1, 6, 5, 4], [6, 6, 6, 6, 6, 6]], 60),
    
 (6, [[6, 0, 6, 0, 6, 1], [0, 0, 0, 0, 0, 2], [2, 3, 4, 5, 6, 6], [0, 0, 0, 0, 0, 2], [0, 2, 0, 0, 0, 0], [3, 9, 3, 0, 0, 1]], 48)
]


@pytest.mark.parametrize("n, field, expected", cases)
def test_roll_cake(n: int, field: List[int], expected: int):  # noqa
    assert baby_shark(n, field) == expected
