def solution(n):
    answer = 1
    for i in range(1, (n // 2) + 1):
        for j in range(i + 1, n + 1):
            i += j
            if i == n:
                answer += 1
                break

            if i > n:
                break
    return answer