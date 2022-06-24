def no_decrement(n: int) -> None:
    d = [[x for x in range(10, 0, -1)] for _ in range(n + 1)]
    for i in range(2, n + 1):
        for j in range(10):
            d[i][j] = sum(d[i - 1][j:])
    print(d[n][0])
