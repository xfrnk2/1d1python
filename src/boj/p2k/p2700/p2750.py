def sort_numbers(input_value_numbers: str) -> None:
    numbers = list(map(int, input_value_numbers.split()))
    print(*sorted(numbers))
