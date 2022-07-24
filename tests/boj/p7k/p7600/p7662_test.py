from typing import Sequence, Tuple, List

import pytest
from src.boj.p7k.p7600.p7662 import double_priority_queue

cases: Sequence[Tuple[int, List[str], str]] = [
    (7, ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"], "EMPTY"),
    (9, ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"], "333 -45")
]


@pytest.mark.parametrize("n, input_value, expected", cases)
def test_check_is_tree(n: int, input_value: List[str], expected: str, capsys):  # noqa
    double_priority_queue(n, input_value)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
