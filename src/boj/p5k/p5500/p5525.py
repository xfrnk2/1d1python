def ioioi(n: int, string: str) -> None:
    o_count = (n + 1)
    target = "O".join("I" * o_count)
    answer = 0
    for i in range(len(string)):
        if string[i:i + len(target)] == target:
            answer += 1
    print(answer)
