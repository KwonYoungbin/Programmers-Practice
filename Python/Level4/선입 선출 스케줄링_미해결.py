from collections import deque

def solution(n, cores):
    answer = 0
    if n <= len(cores):
        return n

    arr = deque([[] for _ in range(max(cores))])
    n -= len(cores)

    for i, val in enumerate(cores):
        arr[val - 1].append(i)

    while n > 0:
        now = arr.popleft()
        arr.append([])
        if len(now) != 0:
            n -= len(now)
            for idx in now:
                arr[cores[idx] - 1].append(idx)

            if n <= 0:
                now.sort()
                answer = now[n - 1] + 1

    return answer