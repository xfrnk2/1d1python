def solve(a: int, b: int, c: int) -> int:
    if b == 0:
        return 1

    temp = solve(a, b // 2, c)
    if b % 2 == 0:
        return temp * temp % c
    else:
        return temp * temp * a % c


def multiply(a: int, b: int, c: int) -> int:
    return solve(a, b, c)
