from typing import Sequence, Tuple
import pytest

from src.boj.p1k.p1100.p1152 import number_of_words

cases: Sequence[Tuple[str, int]] = [
    ("The Curious Case of Benjamin Button", 6),
    (" The first character is a blank", 6),
    ("The last character is a blank ", 6)
]


@pytest.mark.parametrize("sentence, expected", cases)
def test_number_of_words(sentence: str, expected: int, capsys):  # noqa
    number_of_words(sentence)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
