from src.sw_expert_academy.d3.p14361 import same_number_multiple
from typing import List, Sequence, Tuple
import pytest

cases: Sequence[Tuple[int, List[str], str]] = [
    (3, ["142857", "1", "1035"], "#1 possible\n#2 impossible\n#3 possible")
]


@pytest.mark.parametrize("n, data, expected", cases)
def test_same_number_multiple(n: int, data: List[str], expected: str, capsys):  # noqa
    same_number_multiple(n, data)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
