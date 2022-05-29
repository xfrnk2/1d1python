def leap_year(year: str) -> None:
    year = int(year)
    condition = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    if condition:
        print("1")
        return
    print("0")
