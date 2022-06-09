from typing import Sequence, Tuple
import pytest

from src.boj.p2k.p2400.p2407 import combination

cases: Sequence[Tuple[int, int, str]] = [
    (100, 6, "1192052400")
]


@pytest.mark.parametrize("n, m, expected", cases)
def test_melon_field(n: int, m: int, expected: str, capsys):  # noqa
    combination(n, m)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
