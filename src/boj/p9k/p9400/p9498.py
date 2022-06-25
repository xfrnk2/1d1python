def exam_score(input_value: str):
    score = int(input_value)
    answer = "F"
    if 90 <= score <= 100:
        answer = "A"
    elif 80 <= score < 90:
        answer = "B"
    elif 70 <= score < 80:
        answer = "C"
    elif 60 <= score < 70:
        answer = "D"
    print(answer)
