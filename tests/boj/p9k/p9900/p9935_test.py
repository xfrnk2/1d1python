from typing import Sequence, Tuple

import pytest
from src.boj.p9k.p9900.p9935 import string_explosion

cases: Sequence[Tuple[str, str, str]] = [
    ("mirkovC4nizCC44", "C4", "mirkovniz"),
    ("12ab112ab2ab", "12ab", "FRULA")
]


@pytest.mark.parametrize("string, bomb, expected", cases)
def test_string_explosion(string: str, bomb: str, expected: str, capsys):  # noqa
    string_explosion(string, bomb)
    captured = capsys.readouterr()
    assert captured.out == f'{expected}\n'
