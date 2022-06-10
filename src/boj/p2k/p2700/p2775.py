def president(k: int, n: int) -> None:
    apart = [[x for x in range(1, 15)] for _ in range(15)]
    for i in range(1, 15):
        for j in range(14):
            apart[i][j] = sum(apart[i - 1][:j + 1])
    print(apart[k][n - 1])
