def solution(n, stations, w):
    answer = 0
    start = 1

    for s in stations:
        end = s - w
        size = end - start
        answer += size // (2 * w + 1)
        if size % (2 * w + 1) != 0:
            answer += 1
        start = s + w + 1

    if start <= n:
        size = n - start + 1
        answer += size // (2 * w + 1)
        if size % (2 * w + 1) != 0:
            answer += 1

    return answer