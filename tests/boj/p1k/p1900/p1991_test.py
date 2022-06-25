from typing import List, Sequence, Tuple

import pytest
from src.boj.p1k.p1900.p1991 import tree_traversal

cases: Sequence[Tuple[int, List[List[str]], List[str]]] = [
    (7,
     [
         ["A", "B", "C"],
         ["B", "D", "."],
         ["C", "E", "F"],
         ["E", ".", "."],
         ["F", ".", "G"],
         ["D", ".", "."],
         ["G", ".", "."]
     ],
     ["ABDCEFG",
      "DBAECFG",
      "DBEGFCA"]
     )
]


@pytest.mark.parametrize("n, nodes, expected", cases)
def test_digit_triangle(n: int, nodes: List[List[str]], expected: List[str]):  # noqa
    result = tree_traversal(n, nodes)
    assert result == expected
