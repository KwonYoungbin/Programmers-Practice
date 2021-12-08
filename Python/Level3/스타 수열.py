from collections import deque, Counter

def solution(a):
    answer = 0
    if len(a) <= 1:
        return 0

    counter = Counter(a)
    values = deque(sorted(counter.keys(), key=lambda x: counter[x], reverse=True))

    while values:
        now = values.popleft()
        if counter[now] * 2 <= answer:
            continue

        idx = 0
        cnt = 0
        while idx < len(a) - 1:
            if a[idx] == a[idx + 1] or (a[idx] != now and a[idx + 1] != now):
                idx += 1
                continue
            elif a[idx] == now or a[idx + 1] == now:
                idx += 2
                cnt += 2

        if cnt > answer:
            answer = cnt

    return answer

# 다른 풀이
from collections import deque, Counter

def solution(a):
    answer = 0
    if len(a) <= 1:
        return 0

    counter = Counter(a).most_common()
    for n, c in counter:
        if c * 2 <= answer:
            continue

        idx = 1
        cnt = 0
        while idx < len(a):
            if a[idx - 1] == a[idx] or (a[idx - 1] != n and a[idx] != n):
                idx += 1
                continue

            idx += 2
            cnt += 2

        if cnt > answer:
            answer = cnt

    return answer