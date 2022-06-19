def ioioi(n: int, length: int, string: str) -> None:
    IOI = "IOI"
    answer = 0
    idx = 0
    count = 0

    while idx < length - 1:
        if string[idx:idx + 3] == IOI:
            idx += 2
            count += 1
            if count == n:
                answer += 1
                count -= 1
            continue
        idx += 1
        count = 0
    print(answer)
