def string_explosion(string: str, _bomb: str) -> None:
    bomb = list(_bomb)
    bomb_len = len(bomb)

    stack = []
    for c in string:
        stack.append(c)
        if stack[-1] == bomb[-1] and stack[- bomb_len:] == bomb:
            for _ in range(bomb_len):
                stack.pop()

    if stack:
        print("".join(stack))
    else:
        print("FRULA")
