from typing import Sequence, Tuple

import pytest
from src.boj.p2k.p2700.p2741 import print_n

cases: Sequence[Tuple[int, str]] = [
    (5, "1\n2\n3\n4\n5")
]


@pytest.mark.parametrize("n, expected", cases)
def test_multiplication(n: int, expected: str, capsys):  # noqa
    print_n(n)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
