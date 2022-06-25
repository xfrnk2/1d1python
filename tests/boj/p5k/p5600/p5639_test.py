from typing import Sequence, Tuple, List

import pytest
from src.boj.p5k.p5600.p5639 import binary_search_tree

cases: Sequence[Tuple[List[int], List[int]]] = [
    ([50, 30, 24, 5, 28, 45, 98, 52, 60], [5, 28, 24, 45, 30, 60, 52, 98, 50])
]


@pytest.mark.parametrize("pre_order, expected", cases)
def test_binary_search_tree(pre_order: List[int], expected: List[int]):  # noqa
    result = binary_search_tree(pre_order)
    assert result == expected
