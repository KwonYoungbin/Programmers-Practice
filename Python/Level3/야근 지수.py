def solution(n, works):
    answer = 0

    if sum(works) <= n:
        return 0

    for i in range(max(works), 0, -1):
        if n == 0:
            break
        for j in range(len(works)):
            if works[j] == i:
                works[j] -= 1
                n -= 1
            if n == 0:
                break

    for w in works:
        answer += w ** 2

    return answer