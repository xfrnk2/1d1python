from src.boj.p25k.p25000.p25083 import Solution
from pathlib import Path

def test_answer(capsys):  # noqa
    Solution.answer()
 
    expected = '         ,r\'"7\nr`-_   ,\'  ,/\n \\. ". L_r\'\n   `~\\/\n      |\n      |\n'

    captured = capsys.readouterr()
    assert captured.out == expected