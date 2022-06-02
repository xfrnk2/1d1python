def stack_sequence(input_value_n: str, input_value_numbers: str) -> None:
    n = int(input_value_n)
    numbers = list(map(int, input_value_numbers.split()))

    cnt = 0
    res = []
    stack = []
    isValid = True

    for i in range(n):
        cur = numbers.pop(0)
        while cnt < cur:
            cnt += 1
            res.append("+")
            stack.append(cnt)
        if stack[-1] == cur:
            stack.pop()
            res.append("-")
            continue
        isValid = False
        break

    if isValid:
        print("\n".join(res))
        return
    print("NO")
