from math import factorial


def factorial_zero_number(n: int) -> int:

    count = 0
    for x in str(factorial(n))[::-1]:
        if x != '0':
            break
        count += 1
    return count
