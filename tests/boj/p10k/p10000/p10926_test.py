from src.boj.p10k.p10000.p10926 import surprise
from typing import Sequence, Tuple
import pytest

cases: Sequence[Tuple[str, str]] = [
("joonas", "joonas??!"),
("baekjoon", "baekjoon??!"),
]

@pytest.mark.parametrize("user, expected", cases)
def test_number_of_words(user: str, expected: str, capsys):  # noqa
    surprise(user)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
