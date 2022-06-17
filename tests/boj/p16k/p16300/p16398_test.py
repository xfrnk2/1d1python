from src.boj.p16k.p16300.p16398 import planet_connection
from typing import Sequence, Tuple, List
import pytest

cases: Sequence[Tuple[str, List[str]]] = [
(3, ["0 2 3", "2 0 1", "3 1 0"], 3),
(5, ["0 6 8 1 3", "6 0 5 7 3", "8 5 0 9 4", "1 7 9 0 6", "3 3 4 6 0"], 11)
]


@pytest.mark.parametrize("n, planets, expected", cases)
def test_planet_connection(n: int, planets: List[str], expected: int, capsys):  # noqa
    planet_connection(n, planets)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
