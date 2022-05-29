from src.boj.p25k.p25000.p25083 import sprout


def test_sprout(capsys):  # noqa
    sprout()

    expected = '         ,r\'"7\nr`-_   ,\'  ,/\n \\. ". L_r\'\n   `~\\/\n      |\n      |\n'

    captured = capsys.readouterr()
    assert captured.out == expected