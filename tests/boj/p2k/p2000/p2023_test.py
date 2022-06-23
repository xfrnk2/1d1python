from typing import Sequence, Tuple, List

import pytest
from src.boj.p2k.p2000.p2023 import amazing_decimal

cases: Sequence[Tuple[int, List[int]]] = [
    (4, [2333, 2339, 2393, 2399, 2939, 3119, 3137, 3733, 3739, 3793, 3797, 5939, 7193, 7331, 7333, 7393])
]


@pytest.mark.parametrize("n, expected", cases)
def test_n_big_number(n: int, expected: List[int]):  # noqa
    assert amazing_decimal(n) == expected

