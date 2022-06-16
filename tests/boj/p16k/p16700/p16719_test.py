from src.boj.p16k.p16700.p16719 import zoac
from typing import Sequence, Tuple, List
import pytest

cases: Sequence[Tuple[str, List[str]]] = [
("ZOAC", ["A", "AC", "OAC", "ZOAC"]),
("BAC", ["A", "AC", "BAC"]),
("CBA", ["A", "BA", "CBA"]),
("STARTLINK", ["A", "AI", "AIK", "AINK", "ALINK", "ARLINK", "ARTLINK", "SARTLINK", "STARTLINK"]),
("AB", ["A", "AB"]),
("A", ["A"])
]


@pytest.mark.parametrize("string, expected", cases)
def test_zoac(string: str, expected: int, capsys):  # noqa
    zoac(string)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
