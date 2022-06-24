from typing import Sequence, Tuple

import pytest
from src.boj.p1k.p1600.p1629 import multiply

cases: Sequence[Tuple[int, int, int, int]] = [
    (10, 11, 12, 4)
]


@pytest.mark.parametrize("a, b, c, expected", cases)
def test_multiply(a: int, b: int, c: int, expected: int):  # noqa
    assert multiply(a, b, c) == expected
