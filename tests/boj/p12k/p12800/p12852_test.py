from typing import Sequence, Tuple

import pytest
from src.boj.p12k.p12800.p12852 import make_one

cases: Sequence[Tuple[int, str]] = [
    (2, "1\n2 1")
]


@pytest.mark.parametrize("number, expected", cases)
def test_make_one(number: int, expected: str, capsys):  # noqa
    make_one(number)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
