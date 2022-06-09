def dial(string: str) -> None:
    answer = len(string)
    ALPHABET_DICT = {2: "ABC", 3: "DEF", 4: "GHI",
                     5: "JKL", 6: "MNO", 7: "PQRS", 8: "TUV", 9: "WXYZ"}

    for c in string:
        for key, value in ALPHABET_DICT.items():
            if c in value:
                answer += key
    print(answer)
