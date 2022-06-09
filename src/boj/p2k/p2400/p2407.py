def factorial(x: int) -> int:
    if x < 2:
        return x
    return x * factorial(x - 1)


def combination(n: int, m: int):
    print(factorial(n) // (factorial(m) * factorial(n - m)))
