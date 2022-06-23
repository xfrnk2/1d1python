from typing import Sequence, Tuple, List
import pytest

from src.boj.p5k.p5500.p5557 import first_grade

cases: Sequence[Tuple[int, List[int], int]] = [
    (11, [8, 3, 2, 4, 8, 7, 2, 4, 0, 8, 8], 10)
]


@pytest.mark.parametrize("n, numbers, expected", cases)
def test_first_grade(n: int, numbers: List[int], expected: int, capsys):  # noqa
    first_grade(n, numbers)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
