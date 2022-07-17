from typing import List, Sequence, Tuple

import pytest
from src.sw_expert_academy.d5.p1247 import shortest_path

cases: Sequence[Tuple[int, List[int], int]] = [
    (5, [0, 0, 100, 100, 70, 40, 30, 10, 10, 5, 90, 70, 50, 20], 200),
    (6, [88, 81, 85, 80, 19, 22, 31, 15, 27, 29, 30, 10, 20, 26, 5, 14], 304)
]


@pytest.mark.parametrize("n, input_value, expected", cases)
def test_shortest_path(n: int, input_value: List[int], expected: int):  # noqa
    assert expected == shortest_path(n, input_value)
