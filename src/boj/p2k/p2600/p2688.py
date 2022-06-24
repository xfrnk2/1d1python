def no_decretion(n: int):
    numbers = []
    d = [0 for _ in range(n + 1)]
    d[1] = 10

    for i in range(10):
        stringfied_number = abs(i - 10)
        numbers.append(stringfied_number)
    print(numbers)


"""
# 00
# 01
# 02
# 03
# 04
#
# 55,
#
# 11
# 12
# 13
# 14
# 15
# 16
#
# 45
#
# 36
#
# 28
#
# 21
#
#
# 15
#
# 10
#
# 6
# 3
# 1
# 0
"""
