from typing import Sequence, Tuple
import pytest

from src.boj.p1k.p1100.p1157 import word_study

cases: Sequence[Tuple[str, str]] = [
    ("Mississipi", "?"),
    ("zZa", "Z")
]


@pytest.mark.parametrize("word, expected", cases)
def test_number_of_words(word: str, expected: str, capsys):  # noqa
    word_study(word)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
