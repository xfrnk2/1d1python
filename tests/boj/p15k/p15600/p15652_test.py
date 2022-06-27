from typing import Sequence, Tuple

import pytest
from src.boj.p15k.p15600.p15652 import n_and_m

cases: Sequence[Tuple[int, int, str]] = [
    (3, 3, "1 1 1\n1 1 2\n1 1 3\n1 2 2\n1 2 3\n1 3 3\n2 2 2\n2 2 3\n2 3 3\n3 3 3")
]


@pytest.mark.parametrize("n, m, expected", cases)
def test_choose_quadrant(n: int, m: int, expected: str, capsys):  # noqa
    n_and_m(n, m)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
