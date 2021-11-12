def prime(a):
    if a in (2, 3):
        return 1
    elif a % 2 == 0:
        return 0
    else:
        for i in range(3, int(a ** (1 / 2)) + 1):
            if a % i == 0:
                return 0
        return 1


def solution(n):
    answer = 0
    for i in range(2, n + 1):
        answer += prime(i)
    return answer