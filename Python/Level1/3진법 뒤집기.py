def solution(n):
    answer = 0
    temp = []

    while n > 0:
        temp.append(n % 3)
        n //= 3

    temp.reverse()

    for i in range(len(temp)):
        answer += temp[i] * (3 ** i)
    return answer