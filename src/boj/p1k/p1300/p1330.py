def compare_two_numbers(numbers: str) -> None:
    a, b = map(int, numbers.split(" "))
    if a > b:
        print(">")
        return
    if a < b:
        print("<")
        return
    print("==")
