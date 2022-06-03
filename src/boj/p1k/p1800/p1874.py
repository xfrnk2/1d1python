def stack_sequence(input_value_n: str, input_value_numbers: str) -> None:
    N = int(input_value_n)
    given_numbers = list(map(int, input_value_numbers.split()))

    current_idx = 0
    answer = []
    stack = []
    is_avaiable = True

    for _ in range(N):
        current_number = given_numbers.pop(0)
        while current_idx < current_number:
            current_idx += 1
            answer.append("+")
            stack.append(current_idx)
        if stack[-1] == current_number:
            stack.pop()
            answer.append("-")
            continue
        is_avaiable = False
        break

    if is_avaiable:
        print("\n".join(answer))
        return
    print("NO")
