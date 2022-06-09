def honeycomb(target: int) -> None:
    increment = 6
    increment_quantity = 6
    number = 1
    count = 0

    while number <= target:
        number += increment
        increment += increment_quantity
        count += 1
    print(count + 1)
