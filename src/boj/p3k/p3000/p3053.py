import math


def taxicap_geometry(input_value: str) -> None:
    r = int(input_value)
    res1 = f'{r * r * math.pi:.6f}'
    res2 = f'{r * r * 2:.6f}'
    print(res1)
    print(res2)
