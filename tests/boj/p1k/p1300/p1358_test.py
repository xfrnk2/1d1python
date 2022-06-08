from typing import Sequence, Tuple
import pytest

from src.boj.p1k.p1300.p1358 import hockey

cases: Sequence[Tuple[str, str, str, str, str, str, str, str, str]] = [
    ("20","10","5","0","3", "15 5", "1 5", "1 1", "2"),

]


@pytest.mark.parametrize("w, h, x, y, p, player1, player2, player3, expected", cases)
def test_hockey(w: str, h: str, x: str, y: str, p: str, player1: str, player2: str, player3: str, expected: str, capsys):  # noqa
    hockey(w, h, x, y, p, player1, player2, player3)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
