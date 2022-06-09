from typing import Sequence, Tuple, List
import pytest

from src.boj.p6k.p6400.p6416 import check_is_tree

cases: Sequence[Tuple[List[Tuple[int, int]], bool]] = [
    ([(6, 8), (5, 3), (5, 2), (6, 4), (5, 6)], True),
    ([(3, 8), (6, 8), (6, 4), (5, 3), (5, 6), (5, 2)], False),
    ([], True),
    ([(1, 2)], True)
]


@pytest.mark.parametrize("nodes, expected", cases)
def test_check_is_tree(nodes: List[Tuple[int, int]], expected: bool, capsys):  # noqa
    result = check_is_tree(nodes)
    assert result == expected
