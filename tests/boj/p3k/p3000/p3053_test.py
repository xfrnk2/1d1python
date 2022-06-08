from typing import Sequence, Tuple, List
import pytest

from src.boj.p3k.p3000.p3053 import taxicap_geometry

cases: Sequence[Tuple[str, str, str]] = [
    ("1", "3.141593", "2.000000"),
    ("21", "1385.442360", "882.000000")
]


@pytest.mark.parametrize("r, expected1, expected2", cases)
def test_melon_field(r: str, expected1: str, expected2: str, capsys):  # noqa
    taxicap_geometry(r)
    captured = capsys.readouterr()
    assert captured.out == f'{expected1}\n{expected2}\n'
