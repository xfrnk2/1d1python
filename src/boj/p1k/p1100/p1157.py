def word_study(word: str) -> None:
    counter = {}
    for c in word:
        if c.islower():
            c = c.upper()
        counter[c] = counter.get(c, 0) + 1

    item_list = counter.items()
    minimum = max(item_list, key=lambda x: x[1])[1]

    result = []
    for k, v in item_list:
        if v == minimum:
            result.append(k)

    if len(result) == 1:
        print(result.pop())
    else:
        print("?")
