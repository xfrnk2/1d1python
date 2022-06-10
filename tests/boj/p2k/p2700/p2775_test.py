from typing import Sequence, Tuple

import pytest
from src.boj.p2k.p2700.p2775 import president

cases: Sequence[Tuple[int, int, str]] = [
    (1, 3, "6"),
    (2, 3, "10")
]


@pytest.mark.parametrize("k, n, expected", cases)
def test_multiplication(k: int, n: int, expected: str, capsys):  # noqa
    president(k, n)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
