from functools import reduce


def multiplication(num1: str, num2: str):
    a = int(num1)
    results = []

    for i in range(len(num2) - 1, -1, -1):
        result = a * int(num2[i])
        results.append(result)

    for result in results:
        print(result)
    print(reduce(lambda acc, cur: acc + cur, [j * (10 ** i) for i, j in enumerate(results)], 0))
