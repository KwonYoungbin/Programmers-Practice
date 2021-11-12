def solution(answers):
    answer = []
    c1, c2, c3 = 0, 0, 0

    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == supo1[i % len(supo1)]:
            c1 += 1
        if answers[i] == supo2[i % len(supo2)]:
            c2 += 1
        if answers[i] == supo3[i % len(supo3)]:
            c3 += 1

    max_val = max(c1, max(c2, c3))

    if c1 == max_val: answer.append(1)
    if c2 == max_val: answer.append(2)
    if c3 == max_val: answer.append(3)

    return answer