from typing import Sequence, Tuple
import pytest

from src.boj.p2k.p2500.p2588 import multiplication

cases: Sequence[Tuple[str, str, str]] = [
    ("472", "385",
     "2360\n3776\n1416\n181720"),
    ("321", "123",
     "963\n642\n321\n39483")
]


@pytest.mark.parametrize("num1, num2, expected", cases)
def test_multiplication(num1: str, num2: str, expected: str, capsys):  # noqa
    multiplication(num1, num2)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
