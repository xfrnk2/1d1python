from src.boj.p18k.p18100.p18108 import be_to_ad
from typing import Sequence, Tuple
import pytest

cases: Sequence[Tuple[str, int]] = [
("2541", 1998)
]


@pytest.mark.parametrize("be, expected", cases)
def test_be_to_ad(be: str, expected: int, capsys):  # noqa
    be_to_ad(be)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
