def exam_score(input_value: str):
    score = int(input_value)
    if 90 <= score <= 100:
        print("A")
        return
    if 80 <= score < 90:
        print("B")
        return
    if 70 <= score < 80:
        print("C")
        return
    if 60 <= score < 70:
        print("D")
        return
    print("F")
