from collections import deque


def solution(n, a, b):
    answer = 0
    q = deque([x for x in range(1, n + 1)])

    while q:
        left = q.popleft()
        right = q.popleft()

        if [a, b] == [left, right] or [b, a] == [left, right]:
            answer += 1
            break
        elif a in [left, right]:
            q.append(a)
            answer += 1
        elif b in [left, right]:
            q.append(b)
        else:
            q.append(left)

    #     answer = 0
    #     q = deque([i for i in range(1, n+1)])

    #     while q:
    #         l = q.popleft()
    #         r = q.popleft()

    #         if [l,r] == [a,b] or [l,r] == [b,a]:
    #             answer += 1
    #             break
    #         elif a in [l,r]:
    #             q.append(a)
    #             answer += 1
    #         elif b in [l,r]:
    #             q.append(b)
    #         else:
    #             q.append(l)

    return answer