def cnt(val):
    count = 0
    for i in range(1, val + 1):
        if val % i == 0:
            count += 1

    if count % 2 == 0:
        return val
    else:
        return (-1) * val


def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        answer += cnt(i)

    return answer