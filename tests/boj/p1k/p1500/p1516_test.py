from typing import List, Sequence, Tuple
import pytest

from src.boj.p1k.p1500.p1516 import game_development

cases: Sequence[Tuple[int, List[str], List[int]]] = [
    (5, ["10 -1", "10 1 -1", "4 1 -1", "4 3 1 -1", "3 3 -1"], [10,20, 14, 18, 17])
]


@pytest.mark.parametrize("n, buildings, expected", cases)
def test_game_development(n: int, buildings: List[str], expected: List[int], capsys):  # noqa
    assert game_development(n, buildings) == expected
    
    
