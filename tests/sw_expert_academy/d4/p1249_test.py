from typing import List, Sequence, Tuple

import pytest
from src.sw_expert_academy.d4.p1249 import supply_furnace

cases: Sequence[Tuple[int, List[List[int]], int]] = [
    (6, [[0, 1, 1, 0, 0, 1], [0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1], [1, 0, 1, 0, 0, 1], [0, 1, 0, 1, 0, 1],
         [1, 1, 1, 0, 1, 0]], 2)
]


@pytest.mark.parametrize("n, data, expected", cases)
def test_supply_furnace(n: int, data: List[List[int]], expected: str):  # noqa
    assert expected == supply_furnace(n, data)
