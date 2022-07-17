from typing import List, Sequence, Tuple

import pytest
from src.sw_expert_academy.d4.p1226 import maze

cases: Sequence[Tuple[List[str], int]] = [
    (
        [
            "1111111111111111",
            "1210000000100011",
            "1010101110101111",
            "1000100010100011",
            "1111111010101011",
            "1000000010101011",
            "1011111110111011",
            "1010000010001011",
            "1010101111101011",
            "1010100010001011",
            "1010111010111011",
            "1010001000100011",
            "1011101111101011",
            "1000100000001311",
            "1111111111111111",
            "1111111111111111"], 1
    )
]


@pytest.mark.parametrize("field, expected", cases)
def test_maze(field: List[str], expected: int):  # noqa
    assert expected == maze(field)
