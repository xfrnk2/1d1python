def leap_year(input_value: str) -> None:
    year = int(input_value)
    condition = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    if condition:
        print("1")
        return
    print("0")
