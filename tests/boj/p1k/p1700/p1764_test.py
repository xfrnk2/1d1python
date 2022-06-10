from typing import Sequence, Tuple, List
import pytest

from src.boj.p1k.p1700.p1764 import the_dbj

cases: Sequence[Tuple[List[str], List[str], str]] = [
    (["ohhenrie", "charlie", "baesangwook"], ["obama", "baesangwook", "ohhenrie", "clinton"], "baesangwook ohhenrie")
]


@pytest.mark.parametrize("the_d, the_b, expected", cases)
def test_the_dbj(the_d: List[str], the_b: List[str], expected: str, capsys):  # noqa
    the_dbj(the_d, the_b)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
